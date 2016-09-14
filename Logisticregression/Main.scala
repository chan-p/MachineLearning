import scala.util.Random
import java.io.PrintWriter
import logisticregression.LogisticRegression

object Main {

    def main(args: Array[String]) {
        val gold:List[(Double, Double, Double)] = this.makeTestData(100)
        val logisticregression = new LogisticRegression
        val w:List[Double] = logisticregression.train(gold)

        val up = new PrintWriter("output/upper.tsv")
        val lo = new PrintWriter("output/lower.tsv")

        println(w)
        println(logisticregression.predicate(w,logisticregression.phi(-1,-1)))
        // gold.foreach({p =>
        //     val score = w(0) * p._1 + w(1) + p._2 + w(2)
        //     if (score >= 0.0) {
        //         up.println("%f\t%f".format(p._1, p._2))
        //     } else {
        //         lo.println("%f\t%f".format(p._1, p._2))
        //     }
        // })
        // up.close
        // lo.close

    }

    private def makeTestData(n: Int): List[(Double, Double, Double)] = {
        val r = new Random
        (1 to n).toList.map({(n) =>
            val x = (r.nextDouble() - 0.5) * 6.0
            val y = (r.nextDouble() - 0.5) * 6.0
            val t = if (this.h(x, y) >= 0.0) 1.0 else 0.0
            (x, y, t)
        })
    }

    private def h(x:Double, y:Double): Double = {
        5.0 * x + 3.0 * y - 1.0
    }

}
