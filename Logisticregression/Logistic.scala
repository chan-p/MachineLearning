import scala.util.Random
import scala.io.Source

object Logisitic{

  def train(gold:Seq[Seq[Int]], w:Seq[Double], ans:Seq[Double],eta:Double = 0.01 ,limit:Int = 100): Seq[Double] = {
    val new_w:Seq[Double] = trial(gold, w, eta,ans)

    if (w == new_w || limit <= 0) {
      return new_w
    } else {
      train(gold, new_w, ans,eta, limit-1)
    }
  }

  private def update(old_w:Seq[Seq[Int]],predicate:Double):
      //(1 - predocate)(feature())+2Cfeature()
      var new_A = Seq[Double]()
      

  private def trial(gold:Seq[Seq[Int]], w:Seq[Double], eta:Double,ans:Seq[Double]): Seq[Double] = {
    var new_w:Seq[Double] = w
    gold.foreach { p =>
      var new_A = Seq[Double]()
      val feature : Seq[Double] = phi(p)
      val predict: Double = predicate(new_w, feature)
      for(count <- 0 to (w.size-1)){
        new_A = new_A :+ (new_w(count) - eta * (predict - ans(count)) * feature(count))
      }
      new_w = new_A
    }
    new_w
  }

  def predicate(w: Seq[Double], phi: Seq[Double]):Double = {
    return sigmoid(innerProduct(w, phi))
  }

  private def innerProduct(a: Seq[Double], b: Seq[Double]): Double = {
    if (a.size != b.size) {
      throw new RuntimeException("list size isn't equal.")
    }
    var total = 0.0
    for(i <- 0 to (a.size-1)){
      total += a(i) * b(i)
    }
    return total
  }

  def phi(w:Seq[Int]):Seq[Double] = {
    var new_w = Seq[Double]()
    w.foreach(p =>
      new_w = new_w :+ p * 1.0
    )
    new_w = new_w :+ 1.0
    new_w
  }

  private def sigmoid(z:Double): Double = {
    1.0 / (1.0 + Math.exp(-z))
  }

  def parse(line:String):Seq[Int]={
    var li = Seq[Int]()
    val list = line split ","
    for(value <- list){li = li :+(value).toInt}
    return li
  }

  def test(w:Seq[Double],ans:Seq[Double]):Unit={
    val sourc = Source.fromFile("DB/db.csv")
    var lines = sourc.getLines
    var vec = Seq[Seq[Int]]()
    lines.foreach(line => vec = vec :+ parse(line))
    var count = 0
    vec.foreach { p =>
      var new_A = Seq[Double]()
      val feature : Seq[Double] = phi(p)
      val predict: Double = predicate(w, feature)
      println(predict +":"+ ans(count))
      count += 1
    }
  }


  def main(args:Array[String]):Unit={
    val source = Source.fromFile("DB/db.csv")
    var lines = source.getLines
    // source.close
    var vec = Seq[Seq[Int]]()
    var count = 0
    val r = new Random
    var ans = Seq[Double]()
    lines.foreach(line => vec = vec :+ parse(line))
    for(i <- 0 to 49){ans = ans :+ r.nextInt(2)*1.0}
    count = vec(0).size
    var w = Seq[Double]()
    for(i <- 0 to count){w = w :+ r.nextInt(3)*1.0}
    var ww = Seq[Double]()
    ww = train(vec,w,ans)
    // ww.foreach{value => println(value)}
    test(ww,ans)
  }
}
