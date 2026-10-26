"""Check gamma/BBP relation against TWO independently specified source carriers."""
import unittest
from fractions import Fraction as Q

from observational_succ import integer_bbp_carrier as IC
from observational_succ import bbp_natural_carrier as NC
from observational_succ.zero_one_gamma_bridge import (
 authentic_bbp_forcing,bbp_gamma_cell_certificate,
 finite_jet_moment_mutant,shared_resolvent_certificate,gamma_r_finite_bracket,
)

class AuthenticSourceIntegration(unittest.TestCase):
 def test_main_odd_conductor_and_natural_four_poles_agree(self):
  for n in range(1,151):
   a,b=IC.forcing_pair(n)
   self.assertEqual(Q(a,b),NC.exact_forcing(n))
   self.assertEqual(Q(a,b),authentic_bbp_forcing(n))
   self.assertEqual(Q(a,b),Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))

 def test_gamma_one_source_cocycle_and_prime_normality_firewall(self):
  for n in range(1,101):
   t=bbp_gamma_cell_certificate(n,28)
   self.assertGreater(t.lower_ratio,4)
   self.assertLess(t.upper_ratio,30)
  p=shared_resolvent_certificate(8,30)
  self.assertLess(p.pi_outer.lower,p.pi_outer.upper)
  self.assertLess(p.unseen_gamma_tail.upper,Q(1,16**8))
  g2=gamma_r_finite_bracket(2,Q(1),80)
  self.assertLess(g2.lower,g2.upper)

 def test_matched_alternative_positive_kernel_is_not_original_source(self):
  a=finite_jet_moment_mutant(4,3)
  self.assertTrue(all(a.moment_shift(k)==0 for k in range(4)))
  self.assertGreater(a.moment_shift(4),0)
  self.assertGreater(a.resolvent_shift_bracket.lower,0)
  # Both carriers above explicitly use genuine original forcing, NOT this mutant.
  self.assertNotEqual(a.moment_shift(4),Q(0))

if __name__=='__main__':unittest.main()
