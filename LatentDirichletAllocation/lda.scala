package lda

import scala.collection.mutable._
import read.Reader._
import test.Tester._
import stage.Staging._
import accuracy.Accuracy._
import scala.util.Random
import scala.util.control.Breaks

package object TopicModel{
  class LDA(k:Int,num_doc:Int){
    //フィールド
    var corpus = Seq[Seq[String]]() //文書[単語[String]]=各文書における単語
    var topic = Seq[Seq[Int]]() //文書[単語[Int]]=トピック番号
    var wordset = Seq[String]() //単語[String]=全ての単語
    var numTZ = Seq[Map[Any,Int]]() //文書[(単語,トピック番号)]->全文書における組み合わせ出現回数
    var numDZ = Map[Any,Int]() //(文書,トピック番号)->各文書におけるトピックの出現回数
    var numZ = Map[Int,Int]() //トピック番号->全文書における出現回数
    var numD = Map[Int,Int]() //文書->各文書における単語総数
    var K = k //トピック数
    var alpha = 0.1 //ハイパーパラメーターα
    var beta = 0.1 //ハイパーパラメーターβ
    var phiT = Seq[Map[Any,Double]]() //トピック[(単語,トピック)]->各トピックの各単語の出現確率
    var thetaD = Seq[Seq[Double]]() //文書[単語]->各文書におけるトピックの出現確率
    val b = new Breaks
    //初期化関数
    def init(){
      corpus = (new stage()).generate(num_doc)
      for(i <- 0 to (num_doc-1)){topic = topic :+ Seq[Int]()}
      for(z <- 0 to (k-1))numZ += (z -> 0)
      for(doc <- 0 to (corpus.size-1)){
        var words = corpus(doc)
        var numWZ = Map[Any,Int]()
        //index:単語インデックス
        for(index <- 0 to (words.size-1)){
          wordset = wordset :+ words(index) //wordsetに全文書の単語を追加
          val z = Random.nextInt(K) //トピック番号をランダムに生成
          topic(doc) = topic(doc) :+ z //各文書の単語へのトピック番号
          val wz = (words(index),z) //単語とトピック番号の組み合わせ
          //numWZにwzの組み合わせが存在するならカウントアップ、なければ1をセット
          if(numWZ.contains(wz)){numWZ = numWZ.updated(wz,numWZ(wz)+1)}else{numWZ = numWZ.updated(wz,1)}
          val dz = (doc,z) //文書とトピック番号の組み合わせ
          //numDZにdzの組み合わせが存在するならカウントアップ、なければ1をセット
          if(numDZ.contains(dz)){numDZ = numDZ.updated(dz,numDZ(dz)+1)}else{numDZ = numDZ.updated(dz,1)}
          //numDに文書docが存在するならカウントアップ、なければ1をセット
          if(numD.contains(doc)){numD = numD.updated(doc,numD(doc)+1)}else{numD = numD.updated(doc,1)}
          //numZにトピックzが存在するならカウントアップ、なければ1をセット
          if(numZ.contains(z)){numZ = numZ.updated(z,numZ(z)+1)}else{numZ = numZ.updated(z,1)}
        }
        numTZ = numTZ :+ numWZ
      }
    }
    //ギブスサンプリング
    def sampling(){
      println("smapling start")
      val sumAlpha = k * alpha //Kα
      val sumBeta = wordset.size * beta //Vβ
      for(doc <- 0 to (corpus.size-1)){
        val words = corpus(doc) //各文書ごとの単語セットwordset
        for(i <- 0 to (words.size-1)){
          //パラメーター削除
          val word = words(i) //各文書ごとの単語word
          val oldz = topic(doc)(i) //現在の単語wordに割り当てられたトピックoldz
          val oldwz = (word,oldz) //(単語word,現在割り当てられているoldz)
          numTZ(doc) = numTZ(doc).updated(oldwz,(numTZ(doc)(oldwz).-(1))) //現在注目している単語wordをパラメーターから削除
          val olddz = (doc,oldz) //(文書doc,現在注目している単語wordに割り当てられているトピックoldz)
          numDZ = numDZ.updated(olddz,(numDZ(olddz).-(1))) //現在注目している単語wordをパラメーターから削除
          numD = numD.updated(doc,(numD(doc).-(1))) //現在注目している単語wordをパラメーターから削除
          numZ = numZ.updated(oldz,(numZ(oldz).-(1))) //現在注目している単語wordをパラメーターから削除
          //サンプリング
          var probZ = Seq[Double]() //注目している単語における各トピックの出現確率
          for(z <- 0 to (k-1)){
            var numer1 = beta //β
            val wz = (word,z)
            if(numTZ(doc).contains(wz))numer1 = numer1 + numTZ(doc)(wz) //n_tz + β
            val denom1 = numZ(z) + sumBeta //n_z + Vβ
            var numer2 = alpha //α
            val dz = (doc,z)
            if(numDZ.contains(dz))numer2 = numer2 + numDZ(dz) //n_mz + α
            probZ = probZ :+ (numer1*numer2)/(denom1) //((n_tz + β)*(n_mz + α))/(n_z + Vβ)
          }
          //正規化
          var sumProbZ = 0.0
          for(p <- probZ){
            sumProbZ = sumProbZ + p
          }
          for(z <- 0 to (k-1))probZ = probZ.updated(z,(probZ(z)/sumProbZ)) //全て足し合わせると1
          //新しいZのサンプリング
          var newZ = -1
          var maxProbZ = 0.0
          //各単語におけるトピック出現確率が最大のトピックを単語の新しいトピック
          for(z <- 0 to (k-1)){
            if(probZ(z) > maxProbZ){
              newZ = z
              maxProbZ = probZ(z)
            }
          }
          //パラメーター更新
          topic(doc) = topic(doc).updated(i,newZ)
          val newWZ = (word,newZ)
          if(numTZ(doc).contains(newWZ)){numTZ(doc) = numTZ(doc).updated(newWZ,numTZ(doc)(newWZ)+1)}else{numTZ(doc) = numTZ(doc).updated(newWZ,1)}
          val newDZ = (doc,newZ)
          if(numDZ.contains(newDZ)){numDZ = numDZ.updated(newDZ,numDZ(newDZ)+1)}else{numDZ = numDZ.updated(newDZ,1)}
          numD = numD.updated(doc,numD(doc)+1)
          numZ = numZ.updated(newZ,numZ(newZ).+(1))
        }
      }
    }
    //ディリクレ分布による多項分布のパラメーター計算関数
    def computeParameters(){
      //トピック分布のパラメーター計算
      val sumAlpha = alpha * k //Kα
      for(d <- 0 to (corpus.size-1)){
        var theta = Seq[Double]() //トピック分布パラメーター//K次元確率ベクトル//各文書におけるトピックの出現確率
        for(z <- 0 to (k-1)){
          val value = ((numDZ((d,z)).toDouble).+(alpha))/((numD(d).toDouble).+(sumAlpha)) //(n_mz + α)/(n_m + Kα)
          theta = theta :+ value
        }
        thetaD = thetaD :+ theta
      }
      //単語分布のパラメーター計算
      val sumBeta = beta * wordset.size
      for(z <- 0 to (k-1)){
        var phi = Map[Any,Double]()
        for(word <- wordset){
          var numer = beta //β
          val wz = (word,z)
          for(d <- 0 to (corpus.size-1)){if(numTZ(d).contains(wz))numer = numer + numTZ(d)(wz)} //β + n_tz
          val denom = numZ(z) + sumBeta //n_z + Vβ
          // println(numZ(z))
          phi = phi.updated(wz,(numer/denom)) //(β + n_tz)/(n_z + Vβ)
        }
        phiT = phiT :+ phi
      }
    }
    //結果出力関数
    def output_result(){
      for(j <- 0 to (corpus.size-1)){
        print("Theta(D="+j.toString+"):")
        for(i <- 0 to (k-1))print(thetaD(j)(i) + ",")
        println()
      }
      (new method()).Perplexity(num_doc,k,phiT,thetaD,corpus)
    }
    //実行関数
    def run(itelate:Int){
      println("LDA Run")
      init()
      println("init")
      for(roop <- 0 to itelate)sampling()
      computeParameters()
      output_result()
    }
  }
}
