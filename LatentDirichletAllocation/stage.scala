package stage

import scala.collection.mutable._
import read.Reader._
import scala.io.Source

package object Staging{
  class stage{
    var data = new read()
    def generate(num:Int):Seq[Seq[String]]={
      var list = Seq[Seq[String]]()
      var user = Seq[String]()
      var asd = Source.fromFile("../../My Research/Rakuten-real-/userID150-165.csv")
      for(line <- asd.getLines){user = user :+ line}
      for(a <- 0 to 0){
        println(user(a))
        var as = Source.fromFile("../../My Research/rakutendb/150-165/"+user(a)+".csv")
        for(line <- as.getLines){
          if(line.contains("http")!=true){
            val sp = line split ","
            list = list :+ data.run("../../My Research/rakutendb/LDA_item_word/"+sp(0)+".csv")
          }
        }
      }
      //for(n <- 0 to (num-1)){list = list :+ data.run("/Users/chan-p/Desktop/DataSet/text/lda_test"+(n).toString+".txt")}
      println("ok")
      return list
    }
  }
}
