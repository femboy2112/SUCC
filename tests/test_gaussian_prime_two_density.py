"""Gaussian 2 ramification, local half-density, Peano two successor steps."""
import unittest
from fractions import Fraction as F
from observational_succ.gaussian_prime_two_density import (
 GaussianDensityError, gaussian_multiply_matrix, matrix_product,
 lattice_norm_and_half_density, local_prime_half_density_square,
 first_two_step_source, inert_prime_negative_control, authenticated_two_prime_source,
)

class TrueGaussianTwo(unittest.TestCase):
 def test_first_two_steps_rotation_norm_and_index(self):
  r=first_two_step_source()
  self.assertEqual(r["additive_two_successor_steps"],2)
  self.assertEqual(r["gaussian_prime"],(1,1))
  self.assertEqual(r["gaussian_norm"],2)
  self.assertEqual(r["first_one_step_index_two_L2_squared_amplitude"],"1/2")
  self.assertEqual(r["two_gaussian_multiplicative_steps_matrix"],((0,-2),(2,0)))
  self.assertTrue(r["additive_S_squared_is_NOT_multiplicative_pi_squared"])
  self.assertFalse(r["Weil_half_density_uniquely_derived_from_Gaussian_2"])

 def test_form_invariance_for_many_gaussian_lattice_maps(self):
  for a,b in ((1,1),(2,1),(-3,1),(0,2),(5,7)):
   x=lattice_norm_and_half_density(a,b)
   self.assertEqual(x["norm"],a*a+b*b)
   self.assertEqual(F(x["normalized_squared_amplitude"]),F(1,a*a+b*b))
   self.assertFalse(x["signed_Weil_form_constructed"])

 def test_orthogonal_two_succ_reconstruction(self):
  M=gaussian_multiply_matrix(1,1)
  self.assertEqual(matrix_product(M,M),((0,-2),(2,0)))
  self.assertEqual(gaussian_multiply_matrix(2,0),((2,0),(0,2)))
  self.assertNotEqual(matrix_product(M,M),gaussian_multiply_matrix(2,0))

 def test_gaussian_p5_positive_and_p3_inert_negative(self):
  self.assertEqual(lattice_norm_and_half_density(2,1)["norm"],5)
  self.assertEqual(local_prime_half_density_square(5),F(1,5))
  self.assertTrue(inert_prime_negative_control()["gaussian_norm_geometry_not_universal_explanation"])
  self.assertEqual(local_prime_half_density_square(3),F(1,3))
  self.assertEqual(local_prime_half_density_square(2,3),F(1,8))
  for p in (1,4,6,9,True,2.0):
   with self.assertRaises(GaussianDensityError):local_prime_half_density_square(p)
  for z in ((0,0),(1.0,1),(True,0)):
   with self.assertRaises(GaussianDensityError):lattice_norm_and_half_density(*z)

class FrozenSuzukiTwo(unittest.TestCase):
 def test_authenticated_suzuki_half_density_matches_gaussian_square_only(self):
  try:import observational_succ.source_weil_hierarchy
  except ImportError:self.skipTest("frozen source unavailable")
  s=authenticated_two_prime_source()
  self.assertEqual(s["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
  self.assertTrue(s["same_number_not_same_carrier_intertwiner"])
  self.assertFalse(s["full_signed_Weil_form_identified"])
  self.assertFalse(s["RH_proved"])

if __name__=="__main__":unittest.main()
