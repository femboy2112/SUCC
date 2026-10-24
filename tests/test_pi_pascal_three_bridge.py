"""Small additive SUCC bridge tests; source module never overwritten."""
import unittest
from fractions import Fraction as Q
from observational_succ.pi_pascal_three_bridge import (
 weighted_three,selected_shadow_error,tauber_identity,signed_filter,
 prime_square,prime_square_associator,mixed_selector,rational_tripling_fake,
)
from observational_succ.pi_source_collision import bbp_forcing,bbp_states

class PascalThreeBridge(unittest.TestCase):
 def test_ternary_pascal_row(self):
  self.assertEqual(weighted_three(4),tuple(map(lambda k:Q(k,81),(1,8,24,32,16))))
  for n in range(40):self.assertEqual(sum(weighted_three(n),Q()),1)
 def test_source_pi_fourier_bound(self):
  for n in range(40):self.assertEqual(selected_shadow_error(n,3),3*selected_shadow_error(n,1))
 def test_tauber_occupation(self):
  for n in (1,2,3,17,32,64):
   for s in (tuple([1]*n),tuple((-1)**i for i in range(n))):
    t=tauber_identity(s)
    self.assertLessEqual(Q(t['error'])**2,Q(t['squared_upper']))
 def test_signed_source_filter(self):
  for t in (1,2,13,33):
   for j in (1,2,3,4,5):
    z=signed_filter(t,j)
    c=Q(z['correction'])
    self.assertLessEqual(abs(c),Q(z['upper']))
    self.assertEqual(c>0,j%2==1)
 def test_true_source_prime_square(self):
  for q,r in ((2,2),(2,3),(2,5),(3,3),(3,5)):
   for t in (1,2,13,33):
    c=prime_square(q,r,t)
    self.assertLess(-Q(c['defect']),Q(c['absolute_upper']))
    self.assertEqual(c['asymptotic_t3_limit'],str(-Q((q-1)*(r-1),480)))
 def test_three_way_associator(self):
  for q,r,s in ((2,2,2),(2,2,3),(2,3,2),(3,2,2)):
   self.assertTrue(prime_square_associator(q,r,s))
 def test_joint_3_and_16_selection(self):
  z=mixed_selector(4,5)
  self.assertTrue(z['frequencies_distinct'])
  self.assertEqual(z['haar_L2_for_zero_forcing'],'1/20')
  self.assertLess(Q(z['selected_path_integral_abs_error']),Q(1,30*20))
  self.assertFalse(mixed_selector(4,5,q=4)['frequencies_distinct'])
 def test_rational_countermodel(self):
  for r,H in ((2,4),(3,12),(4,30)):
   a=rational_tripling_fake(r,H)
   self.assertTrue(a['vanishing_modes_proved'])
   self.assertEqual(a['base16_normality'],'FALSE')
 def test_strict_inputs(self):
  with self.assertRaises(ValueError):mixed_selector(0,1)
  with self.assertRaises(ValueError):prime_square(3,7,1)
  with self.assertRaises(ValueError):selected_shadow_error(2,0)

if __name__=='__main__':unittest.main()
