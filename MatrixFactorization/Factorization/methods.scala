package MFmethods

package pbject MF{
  class methods(g:Double,l:Double,item:Int){
      //フィールド
      val num_item = item
      val num_user = matrix.size
      //行列_初期化関数(num×k(次元数))
      def matrix_init(num:Int,k:Int):List[Map[Int,Double]]={
        var matrix = List[Map[Int,Double]]()
        for(i <- 1 to num){matrix = matrix :+ learner.generate()}
        for(map <- matrix){for(i <- 0 to (k-1)){map += i -> (Random.nextDouble()+0.1)}}
        return matrix
      }
      //誤差関数
      def error(rate:Double,pre:Double):Double=rate-pre
      //算出関数(ユーザー行列,アイテム行列,次元数)
      def cross(mapU:Map[Int,Double],mapI:Map[Int,Double],k:Int):Double={
        var total = 0.0
        for(i <- 0 to (k-1)){total += mapU(i) * mapI(i)}
        return total
      }
      //RMSE関数
      def rmse(matrix:List[Map[Int,Double]],u_matrix:List[Map[Int,Double]]k:Int){
        var err = 0.0
        var total = 0.0
        var count = 0.0
        for(user <- 0 to (matrix.size-1)){
          for(item <- matrix(user).keys){
            err += error(matrix(user)(item),cross(u_matrix(user),i_matrix(item),k))
            count = count + 1.0
          }
          total += err * err
        }
        println("RMSE:"+Math.sqrt(total/count))
      }
  }
}
