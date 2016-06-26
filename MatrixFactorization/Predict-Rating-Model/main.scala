import scala.io.Source
import scala.collection.mutable._
import scala.util.Random
import test.Tester._
import read.Reader._
import predict.Predicter._

object main{
  def main(args: Array[String]): Unit = {
    val start = System.currentTimeMillis
    //インスタンス化(学習率,正則化項パラメーター,アイテム数,次元数)
    val mf = new MF(0.01,0.002,100,50)
    //実行(イテレーション数,次元数)
    mf.run(1000,50)
    println("実行時間："+(System.currentTimeMillis-start)+"msec")
  }
}
