package read

import scala.io.Source
import scala.collection.mutable._

package object Reader{
  class read(){
    def read(path:String):scala.io.BufferedSource=Source.fromFile(path)
    def data(s:scala.io.BufferedSource):Seq[String]={
      var list = Seq[String]()
      for(line <- s.getLines){
        val sp = line split " "
        for(s <- sp){list = list :+s}
      }
      return list
    }
    def run(path:String):Seq[String]=data(read(path))
  }
}
