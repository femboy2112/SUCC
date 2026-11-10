import unittest
from collections import Counter
from fractions import Fraction as F
from math import isclose
from observational_succ.prime_birth_carry import (
 positive_parts, prime_check,balanced_boundaries,p_unit_residue,
 replay_epoch,stage_events,digit_word_counts,digit_tv_uniform,
 signed_carry_covariance,pulse_formula,shadow_seed,
 shadow_negative_certificate,stage_prime_digit_bound,chrono_stage_counts)
from observational_succ.duck_bbp import forcing

CLOCKS=((100,233),(128,313),(256,617),(512,1217),(1024,2473))

class PrimeCarryArithmetic(unittest.TestCase):
 def test_exact_three_channel_source(self):
  for n in range(1,300):
   a=positive_parts(n)
   self.assertTrue(all(t>0 for t in a))
   self.assertEqual(sum(a),forcing(n))
 def test_bounds_and_births(self):
  for A,p in CLOCKS:
   b=balanced_boundaries(A,p)
   k=(p-1)//8
   self.assertEqual(b,(A,4*k+1,5*k+1,6*k+1,2*A))
   events=stage_events(replay_epoch(A,p))
   self.assertEqual(tuple((n,j) for n,j,z,c in events),pulse_formula(p))
 def test_replay_exact_rational_cocycles(self):
  for A,p in CLOCKS:
   records=replay_epoch(A,p)
   self.assertEqual(len(records),A)
   self.assertTrue(all(-16<=r.carry_slip<=16 for r in records))
   self.assertTrue(all(r.injection_wrap==0 for r in records))
   self.assertTrue(all(0<=r.junction<=2 for r in records))
   self.assertTrue(all(r.prime_carry==sum(r.channel_carries)+r.junction-
                            16*r.junction_previous for r in records))
   self.assertTrue(all(r.residue==sum(r.channel_residues)%p for r in records))
 def test_prime_modular_phase_independent_oracle(self):
  A,p=100,233
  u=F(0); observed={r.n:r.residue for r in replay_epoch(A,p)}
  for n in range(1,2*A):
   u=16*u+forcing(n)
   if n>=A:self.assertEqual(p_unit_residue(u,p),observed[n])
 def test_cofactor_slip_nontrivial(self):
  A,p=128,313
  rows=replay_epoch(A,p)
  self.assertTrue(any(r.real_carry != r.prime_carry for r in rows))
  self.assertGreater(sum(r.real_carry!=r.prime_carry for r in rows),A//2)
  self.assertEqual(sum(r.real_carry==r.prime_carry for r in rows),11)
 def test_digit_spectral_covariance(self):
  for A,p in CLOCKS:
   rows=replay_epoch(A,p)
   for h in (1,3,7,8):
    x=signed_carry_covariance(rows,h)
    self.assertLess(x['reconstruction_error'],1e-12)
    self.assertLessEqual(abs(x['real_mean']),1+1e-12)
 def test_real_carry_different_same_prime_channels(self):
  A,p=100,233
  original=replay_epoch(A,p)
  rotated=replay_epoch(A,p,F(1,5))
  self.assertTrue(any(a.real_carry!=b.real_carry for a,b in zip(original,rotated)))
  self.assertTrue(all(a.prime_carry==b.prime_carry and
                      a.channel_residues==b.channel_residues
                      for a,b in zip(original,rotated)))
 def test_coherent_dyadic_shadow_has_real_carry15(self):
  for A,p in ((100,233),(128,313)):
   s=shadow_seed(A)
   self.assertTrue(shadow_negative_certificate(A,s))
   original=replay_epoch(A,p)
   shadow=replay_epoch(A,p,s)
   self.assertTrue(all(r.real_carry==15 for r in shadow))
   self.assertEqual([r.prime_carry for r in original],
                    [r.prime_carry for r in shadow])
   x=signed_carry_covariance(shadow,1)
   self.assertAlmostEqual(abs(x['real_mean']),1,places=12)
 def test_prime_word_histograms_and_tv(self):
  for A,p in ((100,233),(128,313),(256,617)):
   rows=replay_epoch(A,p)
   for d in (1,2,3):
    a=digit_word_counts(rows,d,prime=True)
    b=digit_word_counts(rows,d,prime=False)
    self.assertEqual(sum(a.values()),A-d+1)
    self.assertEqual(sum(b.values()),A-d+1)
    self.assertTrue(F(0)<=digit_tv_uniform(a,d)<=1)
    self.assertTrue(F(0)<=digit_tv_uniform(b,d)<=1)
    stages=chrono_stage_counts(rows,A,p,d)
    self.assertEqual(len(stages['stages']),4)
 def test_analytic_bound_inputs_and_finite_sanity(self):
  for A,p in CLOCKS:
   self.assertGreater(stage_prime_digit_bound(A,p,1,1.0),1)
   self.assertGreater(stage_prime_digit_bound(A,p,2,0.0),0)
 def test_unqualified_pole_birth_is_not_carry(self):
  A,p=100,233
  rows=replay_epoch(A,p)
  stages=stage_events(rows)
  self.assertEqual(len(stages),3)
  self.assertTrue(any(z != real for _,j,z,real in stages))
  self.assertTrue(all(forcing(n)<F(1,1000) for n,_,_,_ in stages))
 def test_fail_closed(self):
  with self.assertRaises(ValueError): balanced_boundaries(100,241*3)
  with self.assertRaises(ValueError): balanced_boundaries(100,233+1)
  with self.assertRaises(ValueError): replay_epoch(100,233,F(1,233))
  with self.assertRaises(ValueError): digit_tv_uniform(Counter(),1)
  with self.assertRaises(ValueError): signed_carry_covariance([],1)

if __name__=='__main__':unittest.main()

class JunctionFingerprint(unittest.TestCase):
 def test_source_clock_rational_stage_slopes(self):
  from observational_succ.prime_birth_carry import (
     STAGE_RATIONAL_SLOPES,STAGE_COMMON_DENOMINATORS,stage_index,
     predicted_channel_residues)
  for A,p in CLOCKS:
   rows=replay_epoch(A,p)
   for r in rows:
    self.assertEqual(r.channel_residues,predicted_channel_residues(r.n,A,p))
  self.assertEqual(STAGE_RATIONAL_SLOPES[-1],(45,24,25))
  self.assertEqual(STAGE_COMMON_DENOMINATORS[-1],30)
 def test_exact_rational_junction_laws(self):
  from observational_succ.prime_birth_carry import (
     STAGE_RATIONAL_SLOPES,junction_law_exact,weighted_junction_law)
  expected=[(F(1,4),F(1,2),F(1,4)),
            (F(11,42),F(10,21),F(11,42)),
            (F(11,60),F(19,30),F(11,60)),
            (F(159,940),F(311,470),F(159,940))]
  self.assertEqual([junction_law_exact(a) for a in STAGE_RATIONAL_SLOPES],expected)
  self.assertEqual(weighted_junction_law(),(F(2861,13160),F(3719,6580),F(2861,13160)))
 def test_exact_junction_parity_sign_transition(self):
  from observational_succ.prime_birth_carry import STAGE_RATIONAL_SLOPES,junction_law_exact
  lines=[q[0]-q[1]+q[2] for q in [junction_law_exact(a) for a in STAGE_RATIONAL_SLOPES]]
  self.assertEqual(lines,[F(0),F(1,21),-F(4,15),-F(76,235)])
 def test_prime_literal_word_extra_horizon_and_bound(self):
  from observational_succ.prime_birth_carry import conditional_prime_digit_bound
  A,p=128,313
  d=4
  rows=replay_epoch(A,p,lookahead=d-1)
  self.assertEqual(len(rows),A+d-1)
  self.assertEqual(sum(digit_word_counts(rows,d,prime=True).values()),A)
  eps,tv=conditional_prime_digit_bound(A,p,d,1.0)
  self.assertGreaterEqual(eps,1)
  self.assertEqual(tv,1.0)
  with self.assertRaises(ValueError):conditional_prime_digit_bound(A,p,A,0.0)
 def test_integer_unit_seed_nonchange_true_zero_clock(self):
  A,p=128,313
  c0=replay_epoch(A,p)
  c1=replay_epoch(A,p,F(5,7))
  self.assertTrue(all(a.prime_carry==b.prime_carry and
                      a.junction==b.junction for a,b in zip(c0,c1)))
  self.assertTrue(any(a.real_carry!=b.real_carry for a,b in zip(c0,c1)))

class RenormalizedBoundary(unittest.TestCase):
 def test_weighted_junction_is_pure_endpoints(self):
  from observational_succ.prime_birth_carry import renormalized_boundary_balance
  for A,p in ((100,233),(128,313),(256,617)):
   rows=replay_epoch(A,p)
   parts=(rows[:8],rows[8:16],rows[16:32],rows[:48],rows)
   for part in parts:
    t=renormalized_boundary_balance(part,p)
    self.assertEqual(t['prime_three_channel_weighted_sum'],
                     t['prime_three_channel_endpoints'])
    self.assertEqual(t['real_prime_weighted_slip'],
                     t['real_prime_cofactor_endpoints_plus_forcing'])
 def test_prime_birth_holonomy_exact(self):
  from observational_succ.prime_birth_carry import renormalized_boundary_balance
  A,p=100,233
  rows=replay_epoch(A,p)
  for n in (117,146,175):
   part=rows[n-A-2:n-A+3]
   self.assertEqual(len(part),5)
   renormalized_boundary_balance(part,p)
 def test_invalid_nonconsecutive_records(self):
  from observational_succ.prime_birth_carry import renormalized_boundary_balance
  r=replay_epoch(100,233)
  with self.assertRaises(ValueError):renormalized_boundary_balance((r[0],r[2]),233)

class SpectralPrimeBirthLines(unittest.TestCase):
 def test_prime_junction_periodic_clock(self):
  from observational_succ.prime_birth_carry import (
    periodic_junction_symbol,prime_order_16,stage_index)
  for A,p in ((100,233),(128,313),(256,617)):
   rows=replay_epoch(A,p)
   m=prime_order_16(p)
   first=(p-1)//8+1
   for r in rows:
    s=stage_index(r.n,A,p)
    self.assertEqual(periodic_junction_symbol(p,s,(r.n-first)%m),r.junction)
   for s in range(4):
    for u in range(10):
     self.assertEqual(periodic_junction_symbol(p,s,u),
                      periodic_junction_symbol(p,s,u+m))
 def test_four_stage_temporal_line_reconstruction(self):
  from observational_succ.prime_birth_carry import (
     junction_epoch_line_response,junction_direct_epoch_dft)
  for A,p in ((100,233),(128,313)):
   rows=replay_epoch(A,p)
   for t in (0,1,3):
    for h in (1,8):
     direct=junction_direct_epoch_dft(rows,h,t)
     reconstructed=junction_epoch_line_response(A,p,h,t)
     self.assertLess(abs(direct-reconstructed),2e-7,(A,p,t,h,direct,reconstructed))
 def test_unit_circle_resolvent_no_zero(self):
  from cmath import exp
  from math import pi
  for A,p in ((100,233),(128,313)):
   rows=replay_epoch(A,p)
   from observational_succ.prime_birth_carry import spectral_resolvent_junction
   for q in (exp(2j*pi/7),exp(2j*pi/11),-1,1):
    # Algebraic multiplier lower bound on unit circle: |1-16q|>=15.
    self.assertGreaterEqual(abs(1-16*q)+1e-12,15)
    spectral_resolvent_junction(rows[:16],q)

class IndependentRationalJunctionOracle(unittest.TestCase):
 def test_distinct_breakpoint_algorithm(self):
  """Independent finite geometric integration, no lcm-bin shortcut."""
  from observational_succ.prime_birth_carry import (
      STAGE_RATIONAL_SLOPES, junction_law_exact)
  for triple in STAGE_RATIONAL_SLOPES:
   points={F(0),F(1)}
   for a in triple:
    points.update(F(j,a) for j in range(1,a))
   points=sorted(points)
   out=[F(0),F(0),F(0)]
   S=sum(triple)
   for lo,hi in zip(points,points[1:]):
    q=sum(int(a*((lo+hi)/2)) for a in triple)
    splits={lo,hi}
    for t in (F(q+1,S),F(q+2,S)):
     if lo<t<hi:splits.add(t)
    splits=sorted(splits)
    for l,r in zip(splits,splits[1:]):
     mid=(l+r)/2
     y=sum(a*mid-int(a*mid) for a in triple)
     out[int(y)]+=r-l
   self.assertEqual(tuple(out),junction_law_exact(triple))
 def test_holdout_summary_is_exactly_integer_sourced(self):
  import json
  from pathlib import Path
  file=Path(__file__).resolve().parents[1]/'research/2026-11-08/prime_birth_carry/FINITE_RECEIPT_2048.json'
  if not file.exists():self.skipTest('research receipt not installed')
  r=json.loads(file.read_text())
  self.assertEqual((r['A'],r['p'],r['order_m']),(2048,4937,617))
  self.assertEqual([t['n'] for t in r['source_events']],[2469,3086,3703])
  self.assertEqual(r['local_real_exact_carry_matches'],117)
  self.assertEqual([t['counts'] for t in r['stage_junction']],
                   [[103,215,103],[175,288,154],[107,404,106],[55,287,51]])
  self.assertTrue(r['hostile']['all_wrong_real_carries_15'])
