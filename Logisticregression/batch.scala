import scala.util.Random
import java.io.PrintWriter
import logisticregression.LogisticRegression
import scala.io.Source

object Main {

    def parse(parse:String):(Dou)

    def main(args: Array[String]) {
        // val reader = new CSVReader(new FileReader("DB/db.csv"))
        val source = Source.fromFile("DB/db.csv")
        val lines = source.getLines
        val gold:List[(Double, Double, Double)]
        lines.foreach(line =>
          parse(line)
        )

        // val gold:List[(Double, Double, Double)] = this.makeTestData(100)
        // val logisticregression = new LogisticRegression
        // val w:List[Double] = logisticregression.train(gold)
        //
        //
        // println(w)
        // println(logisticregression.predicate(w,logisticregression.phi(-1,-1)))

    }
}
