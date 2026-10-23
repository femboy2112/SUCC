"""Hostile proof probes: geometry+Haar+symmetry do not determine EPR state."""
import unittest
from fractions import Fraction as F
from itertools import product
from observational_succ.relative_phase_source_couplings import (
  source_joint_coupling,source_marginals,relative_phase_distribution,
  diagonal_succ_invariant,diagonal_unit_dilation_invariant,
  epr_shift_support,epr_reciprocal_succ_mirror,unit_scale_shift,
  delayed_relative_phase_counterfeit
)
from observational_succ.observation_pinned_geometry import ObservationContractError

class TwoSidedSourceStateRigidityTests(unittest.TestCase):
 def test_all_shift_couplings_have_both_uniform_marginals(self):
  for p in (2,3,5):
   for k in (1,2):
    N=p**k
    for c in range(N):
     nu=source_joint_coupling(p,k,{c:F(1)})
     lhs,rhs=source_marginals(nu,p,k)
     self.assertEqual(lhs,(F(1,N),)*N)
     self.assertEqual(rhs,(F(1,N),)*N)
     self.assertEqual(relative_phase_distribution(nu,p,k)[c],1)
     self.assertTrue(diagonal_succ_invariant(nu,p,k))

 def test_independent_haar_and_perfect_correlated_both_satisfy_all_unit_symmetries(self):
  for p in (2,3,5):
   for k in (1,2):
    N=p**k
    diag=source_joint_coupling(p,k,{0:F(1)})
    independent=source_joint_coupling(p,k,{c:F(1,N) for c in range(N)})
    self.assertNotEqual(diag,independent)
    for nu in (diag,independent):
     self.assertTrue(diagonal_succ_invariant(nu,p,k))
     self.assertEqual(source_marginals(nu,p,k),((F(1,N),)*N,)*2)
     for q in (2,3,5,7,11):
      if q%p:
       self.assertTrue(diagonal_unit_dilation_invariant(nu,p,k,q))
    self.assertEqual(diag[(0,0)],F(1,N))
    self.assertEqual(independent[(0,0)],F(1,N*N))

 def test_pure_shift_epr_mirror_holds_for_every_relative_phase(self):
  for p in (2,3,5):
   for k in (1,2):
    N=p**k
    states=[epr_shift_support(p,k,c) for c in range(N)]
    self.assertEqual(len(set(states)),N)
    for c in range(N):
     lhs,rhs=epr_reciprocal_succ_mirror(p,k,c)
     self.assertEqual(lhs,rhs)
     self.assertEqual(len(lhs),N)
     for d in range(c+1,N):
      self.assertFalse(states[c]&states[d])

 def test_fucc_unit_action_transports_relative_phase_not_invariant_automatically(self):
  for p in (2,3,5):
   for k in (1,2,3):
    N=p**k
    for q in (2,3,5,7):
     if q%p:
      for c in range(N):
       expected=(q*c)%N
       self.assertEqual(unit_scale_shift(p,k,c,q),expected)
       cnu=source_joint_coupling(p,k,{c:F(1)})
       self.assertEqual(diagonal_unit_dilation_invariant(cnu,p,k,q),expected==c)

 def test_deep_relative_phase_is_invisible_to_every_fixed_horizon(self):
  for p in (2,3,5):
   for K in (1,2,3,4):
    x=delayed_relative_phase_counterfeit(p,K)
    self.assertTrue(x['same_through_depth_K'])
    self.assertTrue(x['separated_at_K_plus_one'])

 def test_mutant_relative_weights_and_nonunit_action_fail_closed(self):
  with self.assertRaises(ObservationContractError):
   source_joint_coupling(2,2,{0:F(1,2)})
  with self.assertRaises(ObservationContractError):
   source_joint_coupling(2,2,{0:0.5,1:0.5})
  with self.assertRaises(ObservationContractError):
   unit_scale_shift(2,2,1,2)
  with self.assertRaises(ObservationContractError):
   diagonal_unit_dilation_invariant(source_joint_coupling(2,1,{0:F(1)}),2,1,2)

if __name__=='__main__':unittest.main()
