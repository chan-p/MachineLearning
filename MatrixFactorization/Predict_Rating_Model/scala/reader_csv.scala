package read
import scala.io.Source
import scala.collection.mutable._
import scala.util.Random

package object Reader{
  class reader(){
    def read(path:String):scala.io.BufferedSource=Source.fromFile(path)
    def generate():Map[Int,Double]={
      var map = {
        val b = Map.newBuilder[Int,Double]
        b.result
      }
      return map
    }
    def data(s:scala.io.BufferedSource):(List[Map[Int,Double]],Double)={
      var matrix = List[Map[Int,Double]]()
      var user = 0
      var count = 0
      var map = generate()
      for(line <- s.getLines){
        count += 1
        val sp = line split ","
        if(sp(0).toInt != user){
          user += 1
          matrix = matrix :+ map
          map = generate()
        }
        map += sp(1).toInt -> sp(2).toDouble
      }
      return (matrix,count)
    }
    def run(path:String):(List[Map[Int,Double]],Double)=data(read(path))
  }
}
