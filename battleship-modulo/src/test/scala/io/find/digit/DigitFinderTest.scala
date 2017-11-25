package io.find.digit

import org.scalatest.FlatSpec

class DigitFinderTest extends FlatSpec {

  "DigitFinder findMod" should "2" in {
    val dividend = 1012
    val divisors = Set(1, 0, 2)
    val finder = new DigitFinder
    val mod = finder.findMod(dividend, divisors)
    assert(mod == 2)
  }

}
