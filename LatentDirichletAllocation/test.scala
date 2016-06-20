package test

import scala.collection.mutable._
import read.Reader._

package object Tester{
  class test{
    var data = new read()
    def generate(num:Int):Seq[Seq[String]]={
      var list = Seq[Seq[String]]()
      for(n <- 0 to (num-1)){list = list :+ data.run("/Users/TomonotiHayshi/Desktop/DataSet/text/lda_test"+(n).toString+".txt")}
      return list
    }
  }
}
