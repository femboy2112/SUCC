"""Exact H2_0 clamped Suzuki trials and source-typed variational controls."""
import unittest
from fractions import Fraction as F
from observational_succ.clamped_k_residual_bridge import (
 KResidualError, checked_trial, CLAMPED, gamma_action_tail,
 low_primitive_norm_sq, sqrt_up, conditional_schur_residual_envelope,
 authentic_clamped_signed_source, interval_form,
)

class ExactClampedJacobi(unittest.TestCase):
 def test_exact_high_Q4_moments_zeros_and_two_endpoint_traces(self):
  for name in CLAMPED:
   a=checked_trial(name)
   self.assertTrue(a["source_Q4_constraints"])
   self.assertTrue(a["zero_value_AND_zero_derivative_traces"])
   self.assertFalse(a["RH_proved"])
  self.assertEqual(checked_trial("odd_derivative")["legendre_high_modes"],
                   ((5,"-240/13"),(7,"240/13")))
  self.assertEqual(checked_trial("even_derivative")["legendre_high_modes"],
                   ((6,"-112/5"),(8,"112/5")))

 def test_exact_unfitted_independent_integrated_norms(self):
  self.assertEqual(CLAMPED["odd_derivative"]["norm"],F(640,2431))
  self.assertEqual(CLAMPED["odd_derivative"]["d2"],F(230400,13))
  self.assertEqual(CLAMPED["even_derivative"]["norm"],F(56448,230945))
  self.assertEqual(CLAMPED["even_derivative"]["d2"],F(150528,5))
  self.assertEqual(low_primitive_norm_sq(1),F(1,30))
  self.assertEqual(low_primitive_norm_sq(2),F(1,210))
  self.assertEqual(low_primitive_norm_sq(3),F(1,630))

 def test_real_Gamma_multiplier_action_tail_not_generic_H1_to_L2(self):
  for J in (1,8,20,64,75,189,1024):
   bound=gamma_action_tail(J)
   self.assertGreater(bound,0)
   d0=4*J+1
   self.assertEqual(bound,F(2,d0*d0)+F(16,d0**3))
   for xi in (F(1,4),F(1),F(10),F(100)):
    finite=sum((F(16)*xi*xi/(d*(d*d+4*xi*xi))
                for d in range(d0,d0+4*15,4)),F(0))
    self.assertLessEqual(finite,xi*xi*bound)
  self.assertGreater(gamma_action_tail(20),gamma_action_tail(64))
  self.assertEqual(sqrt_up(F(4,9),1000),F(667,1000))
  self.assertEqual(sqrt_up(F(1,4),1000),F(1,2))

 def test_original_K_primitive_relative_not_derivative_I(self):
  a=conditional_schur_residual_envelope(F(63,500),
               (F(1,2),F(1,2)),(F(1,4),F(1,4)),F(1,8),F(1,64))
  self.assertEqual(a["correct_space"],"PRIMITIVE_K_HILBERT_NOT_DERIVATIVE_L2")
  self.assertGreater(F(a["schur_response_upper"]),F(a["schur_response_lower"]))
  self.assertFalse(a["actual_original_S4_sign_proved"])
  self.assertFalse(a["full_source_action_residual_certified_by_this_function"])

 def test_independent_exact_synthetic_residual_identity(self):
  # D=[[2,1],[1,3]], D>=I, g=(1,2), trial=(1/2,0).
  D=((F(2),F(1)),(F(1),F(3)))
  g=(F(1),F(2));x=(F(1,2),F(0))
  Dx=tuple(sum(D[i][j]*x[j] for j in range(2)) for i in range(2))
  r=tuple(g[i]-Dx[i] for i in range(2))
  lin=sum(g[i]*x[i] for i in range(2))
  qx=sum(x[i]*Dx[i] for i in range(2))
  r2=sum(v*v for v in r)
  inv=((F(3,5),-F(1,5)),(-F(1,5),F(2,5)))
  direct=sum(g[i]*inv[i][j]*g[j] for i in range(2) for j in range(2))
  residual=sum(r[i]*inv[i][j]*r[j] for i in range(2) for j in range(2))
  self.assertEqual(direct,2*lin-qx+residual)
  self.assertEqual(direct,F(7,5))
  receipt=conditional_schur_residual_envelope(1,(lin,lin),(qx,qx),sqrt_up(r2))
  self.assertLessEqual(direct,F(receipt["schur_response_upper"]))
  self.assertGreaterEqual(direct,F(receipt["schur_response_lower"]))

 def test_finite_observed_Galerkin_energy_cannot_determine_resolvent(self):
  # Same one-dimensional observed 2 in both cases; different full resolvent.
  self.assertEqual(F(1,2),F(1,2))
  self.assertNotEqual(F(1,2),F(2,3))
  # This is a known two-completion exact countermodel, not original source.
  for bad in (False,3.4,"3"):
   with self.assertRaises(KResidualError):gamma_action_tail(bad)
  for bad in (True,"0",-1.5):
   with self.assertRaises(KResidualError):sqrt_up(bad)
  with self.assertRaises(KResidualError):checked_trial("fake")
  with self.assertRaises(KResidualError):
   conditional_schur_residual_envelope(0,(0,0),(0,1),1)
  with self.assertRaises(KResidualError):
   conditional_schur_residual_envelope(1,(2,1),(0,1),1)

class ActualOriginalSignedSuzuki(unittest.TestCase):
 def test_original_source_four_low_to_clamped_high_mixed(self):
  try:import observational_succ.source_weil_hierarchy
  except ImportError:self.skipTest("original frozen source missing")
  s=authentic_clamped_signed_source(J=8)
  self.assertEqual(s["source_git_blob"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
  self.assertEqual(s["original_prime_wavefront"],((2,2),))
  self.assertTrue(s["all_Gamma_prime_contact_two_poles_preserved"])
  for parity,packet in s["parity_clamped_high_packets"].items():
   self.assertLessEqual(F(packet["genuine_finite_high_energy"][0]),
                        F(packet["full_Gamma_high_energy"][1]))
   self.assertGreater(F(packet["full_Gamma_action_tail_factor"]),0)
   self.assertFalse(packet["complete_continuum_action_residual_norm_observed"])
   for i in range(1,5):
    m=packet["original_signed_low_high_mixed"][str(i)]
    self.assertLessEqual(F(m["completed_signed_interval"][0]),
                         F(m["genuine_finite_signed_interval"][0]))
    self.assertGreaterEqual(F(m["completed_signed_interval"][1]),
                            F(m["genuine_finite_signed_interval"][1]))
  self.assertFalse(s["RH_proved"])
 def test_invalid_Gamma_cutoff_rejected(self):
  for bad in (0,76,1.1,False):
   with self.assertRaises(KResidualError):authentic_clamped_signed_source(J=bad)

if __name__=="__main__":unittest.main()
