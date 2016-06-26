package test

import scala.collection.mutable._
import scala.util.Random

package object Tester{
  //predict.scalaのテストクラス
  class test{
    //Map[Int,Double]の生成関数
    def generate():Map[Int,Double]={
      var map = {
        var b = Map.newBuilder[Int,Double]
        b.result
      }
      return map
    }
    //評価値行列生成関数
    def data(item:Int):(List[Map[Int,Double]],Double)={
      val user = 10
      var matrix = List[Map[Int,Double]]()
      var count:Double = 0.0
      for(i <- 0 to (user-1)){matrix = matrix :+ generate()}
      for(map <- matrix){
        count += (item.-(1)).toDouble
        for(k <- 0 to (item.-(1))){map += k -> ((Random.nextDouble()+0.5)*(Random.nextInt(4)+1).toDouble)}
      }
      for(i <- 0 to (user-1)){matrix(i) -= (Random.nextInt((item.-(1)))+1)}
      return (matrix,count)
    }
    //実行関数
    def run(item:Int):(List[Map[Int,Double]],Double)=data(item:Int)
  }
}
