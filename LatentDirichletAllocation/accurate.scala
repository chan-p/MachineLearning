package accuracy

import scala.collection.mutable._
import scala.math.pow

package object Accuracy{
  class method(){
    def Perplexity(M:Int,Z:Int,phiT:Seq[Map[Any,Double]],thetaD:Seq[Seq[Double]],corpus:Seq[Seq[String]]){
      var N = 0
      var total = 0.0
      for(m <- 0 to (M-1)){
        var per = 0.0
        for(index <- 0 to (corpus(m).size-1)){
          N = N + 1
          for(z <- 0 to (Z-1)){
            val c = (corpus(m)(index),z)
            if(phiT(z).contains(c))per = per + (phiT(z)(c) * thetaD(m)(z))
          }
          total = total + Math.log(per)
        }
      }
      total = total/N.toDouble
      println("Perplexity:"+pow(Math.E,total))
    }
  }
}
