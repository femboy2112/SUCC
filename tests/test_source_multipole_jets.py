"""Exact rational source multipole source-jet and primitive pair truncation.
It does not establish selected orbit normality.
"""
from fractions import Fraction as F
from math import factorial
import unittest
import sympy as sp

C=(7,4,3,2)
ORIG=(4,-2,-1,-1)
V=(1,-4,3,0)

def moment(weights,q):return sum(w*c**q for w,c in zip(weights,C))

def source(n,weights):return sum((F(w,8*n-c) for w,c in zip(weights,C)),F())

def block(n,m,weights):return sum((16**(m-j)*source(n+j,weights) for j in range(1,m+1)),F())

class MultipoleJets(unittest.TestCase):
 def test_01_source_moments_first_three_derivatives(self):
  self.assertEqual([moment(ORIG,q) for q in range(4)],[0,15,151,1209])
  z=sp.symbols('z')
  f=sum(sp.Rational(w)/(1-c*z) for w,c in zip(ORIG,C))
  for k in range(4):self.assertEqual(sp.diff(f,z,k).subs(z,0),factorial(k)*moment(ORIG,k))

 def test_02_three_primitive_pair_decomposition(self):
  for n in range(1,500):
   baseline=F(1,8*n-2)
   pairs=4*(F(1,8*n-7)-baseline)-2*(F(1,8*n-4)-baseline)-(F(1,8*n-3)-baseline)
   self.assertEqual(pairs,source(n,ORIG))
   self.assertGreater(pairs,0)

 def test_03_one_pole_mutation_changes_critical_exponent(self):
  changed=(5,-2,-1,-1)
  self.assertEqual(moment(changed,0),1)
  for n in (13,29,61,139,277,557):
   self.assertGreater(source(n,changed),0)
   self.assertLess(abs(n*source(n,changed)-F(1,8)),F(5,n))

 def test_04_double_null_second_shade_is_third_order(self):
  self.assertEqual([moment(V,k) for k in range(3)],[0,0,12])
  n=sp.symbols('n',integer=True,positive=True)
  expr=sum(sp.Rational(w)/(8*n-c) for w,c in zip(V,C))
  self.assertEqual(sp.factor(expr),3/((2*n-1)*(8*n-7)*(8*n-3)))
  for n0 in (5,13,29,61,139,277):
   self.assertGreater(source(n0,V),0)
   self.assertLess(abs(n0**3*source(n0,V)-F(3,128)),F(1,n0))

 def test_05_primitive_block_scale_control(self):
  # one extra pole: R~B/(120n). double-null V: R~B/(640 n^3).
  changed=(5,-2,-1,-1)
  for n,m in ((277,2),(557,2),(139,3)):
   B=16**m
   self.assertLess(abs(block(n,m,changed)-F(B-1,120*n)),F(B,n*n))
  for n,m in ((61,4),(139,5),(277,6)):
   B=16**m
   self.assertLess(abs(block(n,m,V)-F(B-1,640*n**3)),F(B,n**4))

if __name__=='__main__':unittest.main()
