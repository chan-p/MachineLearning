package predict

import scala.io.Source
import scala.collection.mutable._
import scala.util.Random
import test.Tester._
import read.Reader._

package object Predicter{
  //MFに関するクラスを宣言
  class MF(g:Double,l:Double,item:Int,k:Int){
    //フィールド
    val gamma:Double = g
    val lam:Double = l
    val num_item = item
    val learner = new test() //testクラスをインスタンス化
    val (matrix,all) = learner.run(item) //run関数を実行
    // val learner = new reader() //readerクラスをインスタンス化
    // val (matrix,all) = learner.run("/Users/TomonotiHayshi/Desktop/DataSet/movie/learning.csv") //run関数を実行
    val num_user = matrix.size //ユーザー数
    var u_matrix = matrix_init(num_user,k) //ユーザー行列<-乱数初期化
    var i_matrix = matrix_init(num_item,k) //アイテム行列<-乱数初期化
    var u_bias = bias_init(num_user) //ユーザーバイアス<-乱数初期化
    var i_bias = bias_init(num_item) //アイテムバイス<-乱数初期化
    val ave_al = ave_all(matrix)/all //全体の平均評価値
    //全体の平均を求める関数
    def ave_all(Matrix:List[Map[Int,Double]]):Double={
      var all:Double = 0.0
      Matrix.foreach(log => log.foreach{case(key,value) => all += value})　//List[Map[key,value]]からvalueを取り出しallに加算
      return all
    }
    //行列_初期化関数
    def matrix_init(num:Int,k:Int):List[Map[Int,Double]]={
      var matrix = List[Map[Int,Double]]()
      for(i <- 1 to num){matrix = matrix :+ learner.generate()}
      for(map <- matrix){for(i <- 0 to (k-1)){map += i -> (Random.nextDouble()+0.1)}}
      return matrix
    }
    //バイアス初期化
    def bias_init(num:Int):Seq[Double]={
      var bias = Seq[Double]()
      for(k <- 1 to num){bias = bias :+(Random.nextDouble()+0.1)}
      return bias
    }
    //評価値予測関数
    def predict_rate(all:Double,u_bias:Double,i_bias:Double,rate:Double):Double=all+u_bias+i_bias+rate
    //誤差関数
    def error(rate:Double,all:Double,u_bias:Double,i_bias:Double,pre:Double):Double=rate-predict_rate(all,u_bias,i_bias,pre)
    //算出関数
    def cross(mapU:Map[Int,Double],mapI:Map[Int,Double],k:Int):Double={
      var total = 0.0
      for(i <- 0 to (k-1)){total += mapU(i) * mapI(i)}
      return total
    }
    //RMSE関数
    def rmse(matrix:List[Map[Int,Double]],u_matrix:List[Map[Int,Double]],i_matrix:List[Map[Int,Double]],u_bias:Seq[Double],i_bias:Seq[Double],k:Int){
      var err = 0.0
      var total = 0.0
      var count = 0.0
      for(user <- 0 to (matrix.size-1)){
        for(item <- matrix(user).keys){
          err += error(matrix(user)(item),ave_al,u_bias(user),i_bias(item),cross(u_matrix(user),i_matrix(item),k))
          count = count + 1.0
        }
        total += err * err
      }
      println("RMSE:"+Math.sqrt(total/count))
    }
    //学習関数
    def learn(k:Int){
      //学習フェーズ
      for(user <- 0 to (matrix.size-1)){
        for(item <- matrix(user).keys){
          val error_ui = error(matrix(user)(item),ave_al,u_bias(user),i_bias(item),cross(u_matrix(user),i_matrix(item),k))
          val g_e = gamma * error_ui
          val g_l = gamma * lam
          u_bias = u_bias.updated(user,(u_bias(user) + g_e - g_l * u_bias(user)))
          i_bias = i_bias.updated(user,(i_bias(item) + g_e - g_l * i_bias(item)))
          for(n <- 0 to (k-1)){
            var u = u_matrix(user)(n)
            var i = i_matrix(item)(n)
            var mu = u_matrix(user)
            var mi = i_matrix(item)
            mu = mu.updated(n,u_matrix(user)(n) + g_e * i - g_l * u)
            mi = mi.updated(n,i_matrix(item)(n) + g_e * u - g_l * i)
            u_matrix = u_matrix.updated(user,mu)
            i_matrix = i_matrix.updated(item,mi)
          }
        }
      }
    }
    //実行関数
    def run(roop:Int,k:Int){
      for(j <- 0 to roop){
        learn(k)
        if(j % 50 == 0)rmse(matrix,u_matrix,i_matrix,u_bias,i_bias,k)
      }
      // 結果出力
      println("Matrix")
      for(i <- 0 to 4){
        for(j <- 0 to (item.-(1))){if(matrix(i).contains(j))print("["+j+"]:"+matrix(i)(j)+",")}
        println()
      }
      println("ReMatrix")
      for(u <- 0 to 4){
        for(i <- 0 to (item.-(1))){print("["+i+"]:"+predict_rate(ave_al,u_bias(u),i_bias(i),cross(u_matrix(u),i_matrix(i),k))+",")}
        println()
      }
      println("Error")
      for(i <- 0 to 4){
        for(j <- 0 to (item.-(1))){if(matrix(i).contains(j))print("["+j+"]:"+matrix(i)(j) .-(predict_rate(ave_al,u_bias(i),i_bias(j),cross(u_matrix(i),i_matrix(j),k)))+",")}
        println()
      }
    }
  }
}
