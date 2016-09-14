package logisticregression {

    import scala.util.Random

    class LogisticRegression {

        def train(gold:List[(Double, Double, Double)], w:List[Double] = List[Double](0.0, 0.0, 0.0), eta:Double = 0.1 ,limit:Int = 50): List[Double] = {
            val r = new Random
            val new_w:List[Double] = this.trial(r.shuffle(gold), w, eta)

            if (w == new_w || limit <= 0) {
                return new_w
            } else {
                train(gold, new_w, eta*0.9, limit-1)
            }
        }

        private def trial(gold:List[(Double, Double, Double)], w:List[Double], eta:Double): List[Double] = {
            var new_w:List[Double] = w

            gold.foreach { p =>

                val feature: List[Double] = this.phi(p._1, p._2)
                val predict: Double = this.predicate(new_w, feature)

                new_w = new_w.zip(feature).map((t) =>
                    // aw - eta + (predict - aglod._3) * aphi
                    t._1 - eta * (predict - p._3) * t._2
                )

            }

            new_w
        }

        def predicate(w: List[Double], phi: List[Double]):Double = {
            this.sigmoid(this.innerProduct(w, phi))
        }

        private def innerProduct(a: List[Double], b: List[Double]): Double = {
            if (a.size != b.size) {
                throw new RuntimeException("list size isn't equal.")
            }

            val products:List[Double] = a.zip(b).map((t) => t._1 * t._2)
            products.reduceLeft {(a,b) => a + b}
        }

        def phi(x:Double, y:Double):List[Double] = {
            List[Double](x * 1.0, y * 1.0, 1.0)
        }

        private def sigmoid(z:Double): Double = {
            1.0 / (1.0 + Math.exp(-z))
        }

    }

}
