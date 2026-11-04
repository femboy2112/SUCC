"""Exact Gaussian and auxiliary-Gamma stationary renormalization controls."""
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
import sys
P=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'stationary_e2_gamma'/'gamma_tangent_field.py'
S=importlib.util.spec_from_file_location('succ_gamma_tangent',P)
g=importlib.util.module_from_spec(S)
sys.modules[S.name]=g
S.loader.exec_module(g)

class GammaTangentTests(unittest.TestCase):
 def test_gaussian_ring_and_inverse(self):
  for a in (g.GQ(1,2),g.GQ(-3,F(1,2)),g.GQ(2,F(1,7))):
   self.assertEqual(a*a.inverse(),g.ONE)
   self.assertEqual(a.inverse()*a,g.ONE)

 def test_four_poles_numerical_vs_exact_source(self):
  for n in range(1,60):
   z=g.r_at(g.GQ(n))
   self.assertEqual(z.im,0)
   f=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
   self.assertEqual(z.re,f)

 def test_gamma_probability_fourier_modulus_le_one_samples(self):
  for n in (1,2,4,8,16,40):
   for w in (F(0),F(1,2),F(1),F(3)):
    x=g.gamma_source_factor(F(1,n),w)
    self.assertLessEqual(x.norm2(),1)
    self.assertGreater(x.norm2(),0)

 def test_shape_two_factor_and_zero_frequency(self):
  for n in (1,2,5,8):
   q=F(1,n)
   self.assertEqual(g.gamma_source_factor(q,0),g.ONE)
   self.assertEqual(g.tangent_corrector(q,0),g.ONE)
   self.assertEqual(g.gamma_shape2_factor(q,F(1,2)),g.ONE/(g.GQ(1,-q/2)*g.GQ(1,-q/2)))

 def test_gamma_corrector_exact_multiplier_factorization(self):
  for n in (1,2,3,5,8,16):
   for w in (F(1,2),F(1)):
    q=F(1,n)
    self.assertEqual(g.tangent_corrector(q,w)*g.gamma_shape2_factor(q,w),
                     g.gamma_source_factor(q,w))

 def test_full_corrected_product_equal_source_over_shape2(self):
  for n in range(0,14):
   for w in (F(0),F(1,2),F(1)):
    o=g.product_corrected(n,w)
    self.assertEqual(o.q,F(1,n+1))
    self.assertEqual(o.z*g.product_gamma2(n,w),g.product_raw(n,w))

 def test_nonzero_gaussian_corrected_factors(self):
  for n in range(1,70):
   q=F(1,n)
   u=g.tangent_corrector(q,F(1))
   self.assertGreater(u.norm2(),0)
   self.assertLess(abs(complex(u)-1),10/n**2)

 def test_source_specific_laurent_and_no_missing_lane(self):
  x=g.analytic_moment_source_coefficients()
  self.assertEqual(x['mass'],0)
  self.assertEqual(x['first_moment'],-15)
  self.assertEqual(x['leading_laurent'],F(15,64))

if __name__=='__main__':unittest.main()
