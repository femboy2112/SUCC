"""Independent exact Euler/multiplicativity controls for Gaussian prime2 bridge."""
import unittest
from fractions import Fraction as F
from observational_succ.gaussian_euler_shell_controls import (
 GaussianEulerError, chi_minus_four, splitting_type,
 gaussian_norm_shell_multiplier,gaussian_vs_rational_local,
 original_source_ramified_two_tower,
)

class GaussianDedekindLocal(unittest.TestCase):
 def test_three_genuinely_different_prime_types(self):
  self.assertEqual([splitting_type(p) for p in (2,3,5)],[
    "RAMIFIED_NORM_P","INERT_ONE_NORM_P_SQUARED","SPLIT_TWO_NORM_P"])
  self.assertEqual([chi_minus_four(p) for p in (2,3,5,7,13)], [0,-1,1,-1,1])

 def test_full_true_rational_prime2_log_tower_matched_no_zero_oracle(self):
  for sigma in (2,3,4):
   q=gaussian_vs_rational_local(2,sigma,8)
   self.assertEqual(q["euler_Q"],q["euler_Qi"])
   self.assertEqual(q["coefficients_of_log_p_by_integer_norm_exponent"],(1,)*8)
   self.assertEqual(q["squared_half_density_by_norm_exponent"][0],"1/2")
   self.assertEqual(q["squared_half_density_by_norm_exponent"][3],"1/16")
   self.assertFalse(q["full_completed_Weil_intertwiner_constructed"])

 def test_split_p5_doubles_every_prime_power_jet(self):
  q=gaussian_vs_rational_local(5,2,7)
  self.assertEqual(q["coefficients_of_log_p_by_integer_norm_exponent"],(2,)*7)
  self.assertEqual(F(q["euler_Qi"]),F(q["euler_Q"])**2)
  self.assertEqual(gaussian_norm_shell_multiplier(5,1),2)

 def test_inert_p3_has_first_nonzero_norm9_not_norm3(self):
  q=gaussian_vs_rational_local(3,2,8)
  self.assertEqual(q["coefficients_of_log_p_by_integer_norm_exponent"],(0,2,0,2,0,2,0,2))
  self.assertEqual(F(q["euler_Qi"]),F(1,1)/ (1-F(1,3**4)))
  self.assertEqual(gaussian_norm_shell_multiplier(3,1),0)
  self.assertEqual(gaussian_norm_shell_multiplier(3,2),2)
  self.assertEqual(q["squared_half_density_by_norm_exponent"][0],"1/3")

 def test_direct_multiplicative_euler_control_and_fake_inputs(self):
  for p in (2,3,5,7,11,13,17):
   for s in (2,3):
    v=gaussian_vs_rational_local(p,s,8)
    self.assertEqual(v["euler_Qi"],v["euler_Qi_direct_split_formula"])
    self.assertFalse(v["RH_proved"])
  for p in (6,9,4,1,True,2.5):
   with self.assertRaises(ValueError):gaussian_vs_rational_local(p)
  for s in (1,0,1.5,True):
   with self.assertRaises(GaussianEulerError):gaussian_vs_rational_local(2,s)
  for k in (0,-1,1.5,True):
   with self.assertRaises(GaussianEulerError):gaussian_norm_shell_multiplier(2,k)

class FrozenPrimeTwo(unittest.TestCase):
 def test_original_half_density_prime2_shells(self):
  try:import observational_succ.source_weil_hierarchy
  except ImportError:self.skipTest("frozen original Suzuki source not installed")
  d=original_source_ramified_two_tower(4)
  self.assertEqual(d["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
  self.assertTrue(d["gaussian_prime_ideal_norm2_tower_equal_by_LOG_DERIVATIVE"])
  self.assertFalse(d["full_adelic_gamma_poles_completed"])
  self.assertFalse(d["RH_proved"])
  for invalid in (0,-1,11,1.5,True):
   with self.assertRaises(GaussianEulerError):original_source_ramified_two_tower(invalid)

if __name__=="__main__":unittest.main()
