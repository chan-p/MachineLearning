import scala.collection.mutable._
import read.Reader._
import test.Tester._
import lda.TopicModel._
import scala.util.Random
import scala.util.control.Breaks

object main{
  def main(args: Array[String]): Unit = {
    val start = System.currentTimeMillis
    val lda = new LDA(1000,150)
    lda.run(0)
    println("実行時間："+(System.currentTimeMillis-start)+"msec")
  }
}
