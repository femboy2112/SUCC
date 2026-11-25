import unittest
from dataclasses import replace
from fractions import Fraction
from observational_succ.principia_cm_theta import (
 CMSourceError, gaussian_shell, theta_shell_moment, det_bareiss,
 construct_cm_theta_certificate, verify_cm_theta_certificate,
 gaussian_moment_energy_upper_bound, lemniscate_derivative_jets,
 lemniscate_hasse_invariant, p_valuation, theta_derivative_partial, theta_derivative_tail_bound)
from observational_succ.principia_cm_period import (
 wp_laurent_coefficients, sigma2_wp_coefficients,
 normalized_theta_period_jets, lemma_theta_normalization_audit,
 lemniscate_formal_log_coefficients, first_honda_coordinate_jet)

class CMThetaTests(unittest.TestCase):
 def test_real_CM_source_shells(self):
  self.assertEqual(len(gaussian_shell(1)),4)
  self.assertEqual(len(gaussian_shell(2)),4)
  self.assertEqual(theta_shell_moment(2,4),-16)
  self.assertEqual(theta_shell_moment(8,4),-256)
  self.assertEqual(theta_shell_moment(2,2),0)
  self.assertEqual(theta_shell_moment(9,4),324)
 def test_exact_two_place_minor(self):
  for p in (3,7,11):
   for k in (1,2,3,4):
    with self.subTest(p=p,k=k):
     c=construct_cm_theta_certificate(p,k)
     info=verify_cm_theta_certificate(c)
     self.assertEqual(info['rank'],k)
     self.assertGreaterEqual(info['p_valuation'],2*k*(k-1))
     self.assertLessEqual(info['weighted_determinant_squared'], info['hadamard_bound_squared'])
 def test_specific_reconstruction(self):
  c=construct_cm_theta_certificate(3,2,Fraction(1,2))
  self.assertEqual(c.matrix,((4,4),(324,-1296)))
  self.assertEqual(verify_cm_theta_certificate(c)['determinant'],-6480)
  self.assertEqual(p_valuation(-6480,3),4)
 def test_real_global_theta_energy_bound(self):
  for p in (3,7):
   for k in (1,2,3,4):
    c=construct_cm_theta_certificate(p,k)
    cert=verify_cm_theta_certificate(c)
    for r,v in enumerate(cert['real_weighted_row_norm_squares']):
     self.assertLessEqual(v,gaussian_moment_energy_upper_bound(p,r,Fraction(1,2)))
 def test_false_split_prime_rejected(self):
  with self.assertRaises(CMSourceError):construct_cm_theta_certificate(5,2)
  self.assertNotEqual(theta_shell_moment(25,4),5**4*theta_shell_moment(1,4))
 def test_composite_fake_rejected(self):
  with self.assertRaises(CMSourceError):construct_cm_theta_certificate(15,2)
 def test_radial_not_holomorphic(self):
  self.assertEqual(theta_shell_moment(2,4),-16)
  self.assertEqual(sum((a*a+b*b)**2 for a,b in gaussian_shell(2)),16)
 def test_wrong_period_passport_and_vanishing_minor(self):
  c=construct_cm_theta_certificate(3,2)
  with self.assertRaises(CMSourceError):verify_cm_theta_certificate(replace(c,passport='undocumented-period'))
  forged=((4,4),(4,4))
  with self.assertRaises(CMSourceError):verify_cm_theta_certificate(replace(c,matrix=forged))
  self.assertEqual(det_bareiss(forged),0)
 def test_wrong_norm_and_q(self):
  c=construct_cm_theta_certificate(3,2)
  with self.assertRaises(CMSourceError):verify_cm_theta_certificate(replace(c,gaussian_norms=(9,27)))
  with self.assertRaises(CMSourceError):construct_cm_theta_certificate(3,2,Fraction(2))
 def test_no_double_count_from_repeated_column(self):
  c=construct_cm_theta_certificate(3,3)
  rows=tuple((row[0],row[0],row[2]) for row in c.matrix)
  with self.assertRaises(CMSourceError):verify_cm_theta_certificate(replace(c,matrix=rows))
  self.assertEqual(det_bareiss(rows),0)
 def test_lemniscate_actual_curve_jets(self):
  a=lemniscate_derivative_jets(17)
  self.assertEqual((a[1],a[5],a[9],a[13],a[17]),(1,-12,3024,-4390848,21224560896))
  self.assertTrue(all(a[i]==0 for i in range(18) if i%4 !=1))
 def test_exact_period_normalized_theta_derivatives(self):
  expected=(Fraction(1),Fraction(1,4),Fraction(17,16),Fraction(-111,64),
            Fraction(12513,256), Fraction(-146079,1024))
  self.assertEqual(normalized_theta_period_jets(5),expected)
  self.assertEqual(wp_laurent_coefficients(2)[:3],(Fraction(1),Fraction(1,5),Fraction(1,75)))
 def test_period_jet_integrality_exact_through_30(self):
  data=lemma_theta_normalization_audit(30)
  self.assertEqual(len(data["integral_normalized_jets"]),31)
  r30=data['coefficients'][30]
  self.assertEqual(p_valuation(r30.numerator,3),14)
  self.assertLess(14,45)  # naive simple-theta multiplicity is insufficient
 def test_actual_CM_formal_log_orientation(self):
  a=lemniscate_formal_log_coefficients(9)
  self.assertEqual(a[5],Fraction(1,10))
  self.assertEqual(a[9],Fraction(1,24))
  self.assertEqual(first_honda_coordinate_jet(3,1),Fraction(-7,24))
  self.assertEqual(first_honda_coordinate_jet(3,-1),Fraction(3,8))
  self.assertEqual(p_valuation(first_honda_coordinate_jet(3,1).numerator,3)-p_valuation(first_honda_coordinate_jet(3,1).denominator,3),-1)
  self.assertEqual(p_valuation(first_honda_coordinate_jet(3,-1).numerator,3)-p_valuation(first_honda_coordinate_jet(3,-1).denominator,3),1)
 def test_inert_orientation_holdout_primes(self):
  for p in (3,7,11,19,23):
   for unit,expected in ((1,-1),(-1,1)):
    x=first_honda_coordinate_jet(p,unit)
    v=p_valuation(x.numerator,p)-p_valuation(x.denominator,p)
    self.assertEqual(v,expected,(p,unit,v))
 def test_source_faithful_analytic_completion(self):
  q=Fraction(1,2)
  for r,N in ((0,12),(1,30),(2,50),(3,70)):
   partial=theta_derivative_partial(r,q,N)
   bound=theta_derivative_tail_bound(r,q,N)
   extended=theta_derivative_partial(r,q,N+25)
   self.assertLessEqual(abs(extended-partial),bound)
   self.assertGreater(bound,0)
  with self.assertRaises(CMSourceError):theta_derivative_tail_bound(5,q,0)
 def test_t_equals_one_gaussian_tail_no_transcendental_rounding(self):
  # pi>3 and e^3>20 give q=e^(-pi)<1/20; monotone bound is rigorous.
  q_upper=Fraction(1,20)
  for r,N in ((0,8),(1,20),(2,30)):
   self.assertGreater(theta_derivative_tail_bound(r,q_upper,N),0)
 def test_CM_Hasse_invariant(self):
  for p in (3,7,11,19):self.assertEqual(lemniscate_hasse_invariant(p),0)
  for p in (5,13,17):self.assertNotEqual(lemniscate_hasse_invariant(p),0)
  with self.assertRaises(CMSourceError):lemniscate_hasse_invariant(2)

if __name__=='__main__':unittest.main()
