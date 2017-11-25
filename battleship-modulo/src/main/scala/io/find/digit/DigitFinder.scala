package io.find.digit

class DigitFinder {


  def findMod(dividend: Int, divisors: Set[Int]): Int = {
    var numModDigits = 0
    for{
      d <- divisors
      if (d > 0)
      if (dividend % d == 0)
    } numModDigits += 1
    numModDigits
  }

}
