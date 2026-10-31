"""Original four-pole BBP source Dirichlet pole and Gamma finite part."""
import unittest
from fractions import Fraction
import mpmath as mp
mp.mp.dps=95
D=(1,4,5,6);C=(4,-2,-1,-1)
A=Fraction(15,64)
W=tuple(Fraction(c*(8-d),64) for c,d in zip(C,D))

def source(n):
 return sum((Fraction(c,8*n-8+d) for c,d in zip(C,D)),Fraction(0))
def defect(n):return source(n)-A/Fraction(n*n)
def fp(c=C):
 return -mp.fsum(mp.mpf(ck*(8-d))/64*mp.digamma(mp.mpf(d)/8) for ck,d in zip(c,D))

class TwistedSourceTests(unittest.TestCase):
 def test_exact_weight_and_grade(self):
  self.assertEqual(W,(Fraction(7,16),Fraction(-1,8),Fraction(-3,64),Fraction(-1,32)))
  self.assertEqual(sum(W),A)
 def test_exact_partial_fraction(self):
  for n in range(1,513):
   got=sum((w/(Fraction(n-1)+Fraction(d,8)) for w,d in zip(W,D)),Fraction(0))
   self.assertEqual(n*source(n),got)
 def test_positive_defect_with_strict_tail(self):
  self.assertEqual(defect(1),Fraction(2783,960))
  for n in range(2,4096):
   g=defect(n)
   self.assertGreater(g,0)
   self.assertLessEqual(g,Fraction(35,27*n**3))
 def test_finite_harmonic_remainder_bound(self):
  F=fp()
  for N in (2,4,8,16,32,128):
   partial=sum((n*source(n) for n in range(1,N+1)),Fraction(0))
   self.assertLess(abs(mp.mpf(partial.numerator)/partial.denominator-A.numerator/A.denominator*mp.log(N)-F),
                   mp.mpf(A.numerator)/(2*A.denominator*N)+mp.mpf(35)/(27*N))
 def test_exact_positive_remainder_bound(self):
  gtarget=fp()-mp.mpf(15)/64*mp.euler
  for N in (2,4,8,16,32,128):
   partial=sum((n*defect(n) for n in range(1,N+1)),Fraction(0))
   rem=gtarget-mp.mpf(partial.numerator)/partial.denominator
   self.assertGreater(rem,0)
   self.assertLess(rem,mp.mpf(35)/(27*N))
 def test_same_residue_different_mutant_finite_part(self):
  mutant=(5,-5,0,0)
  self.assertEqual(sum(Fraction(c*(8-d),64) for c,d in zip(mutant,D)),A)
  self.assertGreater(abs(fp(mutant)-fp()),mp.mpf('0.01'))
 def test_laurent_finite_difference(self):
  F=fp()
  # Compare a source-specific rational partial Dirichlet remainder against Gamma finite part.
  for eps in (mp.mpf('0.02'),mp.mpf('0.01')):
   # Remove zeta's pole analytically, then compare finite-part limit.
   val=mp.mpf(15)/64*(mp.zeta(1+eps)-1/eps)
   rem=mp.fsum(mp.mpf(defect(n).numerator)/defect(n).denominator/mp.power(n,-1+eps) for n in range(1,4096))
   self.assertLess(abs(val+rem-F),mp.mpf('0.08'))

if __name__=='__main__':unittest.main()
