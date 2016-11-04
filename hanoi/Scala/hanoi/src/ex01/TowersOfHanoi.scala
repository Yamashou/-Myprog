package ex01

import scala.Range
class TowersOfHanoi(val n: Int) {
  def hanoi(m: Int, from: Int, to: Int,work: Int,s: Array[List[Int]]){
    if(m==1){
      s(to) = s(from).head::s(to)
      s(from) = s(from).tail
      println(disp(s.toList.map(_.reverse)))
      
          
    }
  }
}