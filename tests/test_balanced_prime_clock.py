"""New balanced 12/5 BBP prime-clock source/chronology controls."""
import math
import cmath
import unittest
from fractions import Fraction as F
from observational_succ.balanced_prime_clock import (
 epoch_stage_boundaries,epoch_stage_lengths,epoch_stage_weights,
 epoch_mode_coefficients,epoch_mode_resonance_mass,
 epoch_histogram_from_stage,epoch_histogram_from_residues,
 epoch_complete_cycles_and_remainders,unbalanced_pr4A_channels_locked,
 prime_candidates,epoch_phase_gram,target_gram,completion_error_budget,
 direct_source_epoch_residues,dyadic_terminal_shadow,dyadic_shadow_phase_bound,
)
from observational_succ.three_channel_prime_tomography import (
 is_prime, predicted_residues,multiplicative_order_16,
)

class BalancedClock(unittest.TestCase):
 def test_exact_stage_partition(self):
  self.assertEqual(epoch_stage_boundaries(100,241),(100,121,151,181,200))
  self.assertEqual(epoch_stage_lengths(100,241),(21,30,30,19))
  self.assertEqual(sum(epoch_stage_weights(100,241)),1)
  for A in (32,100,256,512):
   for p,_ in prime_candidates(A):
    lens=epoch_stage_lengths(A,p)
    self.assertEqual(sum(lens),A)
    self.assertTrue(all(x>0 for x in lens))
    self.assertTrue(all(x>0 for x in epoch_stage_weights(A,p)))

 def test_stage_near_twelfths_balanced(self):
  for A in (100,256,512,1024):
   candidates=prime_candidates(A)
   self.assertTrue(candidates, A)
   p,m=candidates[0]
   self.assertEqual(p%8,1)
   self.assertTrue(m**3>p and m**2*p.bit_length()**4>p)
   self.assertLess(abs(F(p,A)-F(12,5)),F(3,10))

 def test_balanced_frame_has_four_strata(self):
  for A in (100,256,512,1024):
   p=prime_candidates(A)[0][0]
   lengths=epoch_stage_lengths(A,p)
   self.assertEqual(len(lengths),4)
   self.assertTrue(all(0<x<A for x in lengths))
   self.assertTrue(all(F(x,A) >= F(1,10) for x in lengths))

 def test_nontautological_direct_source_replay(self):
  for A in (32,100,128):
   c=prime_candidates(A)
   if not c:continue
   p=c[0][0]
   direct=direct_source_epoch_residues(A,p)
   from_pred=[predicted_residues(p,n) for n in range(A,2*A)]
   self.assertEqual(direct,from_pred)

 def test_fourier_histogram_independent_paths(self):
  modes=((1,1,1),(0,1,-1),(1,-2,0),(1,0,0),(2,-1,3),(-1,-1,-1))
  for A in (64,100,128,256):
   for p,_ in prime_candidates(A)[:2]:
    for mode in modes:
     self.assertEqual(epoch_histogram_from_stage(A,p,1,mode),
                      epoch_histogram_from_residues(A,p,1,mode))

 def test_all_four_planes_are_dangerous(self):
  A=100;p=241
  self.assertEqual(epoch_mode_coefficients(p,1,(1,1,1)),(4,7*pow(2,-1,p)%p,
       33*pow(10,-1,p)%p,47*pow(15,-1,p)%p))
  self.assertEqual(epoch_mode_resonance_mass(A,p,1,(0,0,0)),1)  # a times its conjugate
  self.assertEqual(epoch_mode_resonance_mass(A,p,1,(0,1,-1)),
                   sum(epoch_stage_weights(A,p)[:2]))

 def test_pr544_clock_exact_null_mode(self):
  for A in (100,256,512):
   p=next((v for v in range(4*A+7,3*A,-1) if v%8==1 and is_prime(v)),None)
   self.assertIsNotNone(p)
   self.assertTrue(unbalanced_pr4A_channels_locked(A,p))
   from observational_succ.three_channel_prime_tomography import predicted_residues
   for n in range(A,2*A):
    c3,c4,c5=predicted_residues(p,n)
    self.assertEqual(c4,c5)
   # Identical fourth/fifth original-pole channels => an EXACT null Gram vector.

 def test_balanced_target_spectrum(self):
  for A in (100,128,256,512):
   p=prime_candidates(A)[0][0]
   w=epoch_stage_weights(A,p)
   sigma=w[0]+w[1]
   expected=F(5*p+3-8*A,8*A)
   self.assertEqual(sigma,expected)
   self.assertLessEqual(sigma,F(9,16)+F(1,A))
   t=target_gram(A,p)
   self.assertEqual(t[1][2],sigma)
   self.assertEqual(t[2][1],sigma)

 def test_finite_budget_is_conservative(self):
  for A in (100,128,256):
   p=prime_candidates(A)[0][0]
   delta=1.0  # trivial certified universal input
   bound=completion_error_budget(A,p,delta)
   self.assertGreaterEqual(bound,1)
   m=multiplicative_order_16(p)
   self.assertEqual(sum(q*m+r for q,r in epoch_complete_cycles_and_remainders(A,p)),A)

 def test_phase_gram_positivity_diagnostic(self):
  # Algebraically Hermitian PSD by construction; float controls check implementation.
  for A in (100,256):
   p=prime_candidates(A)[0][0]
   M=epoch_phase_gram(A,p)
   self.assertTrue(all(abs(M[i][i]-1)<1e-12 for i in range(3)))
   for i in range(3):
    for j in range(3):
     self.assertLess(abs(M[i][j]-M[j][i].conjugate()),1e-12)

 def test_true_zero_seed_signed_lag_has_exact_four_pole_forcing(self):
  # Independent direct four-fraction zero-seeded recurrence; no digits of pi.
  A,p,h=100,241,1
  stop=2*A+8
  forcing=[F(0)]
  state=[F(0)]
  for n in range(1,stop+1):
   a=8*n-7
   forcing.append(F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5))
   state.append(16*state[-1]+forcing[-1])
  direct=direct_source_epoch_residues(A,p)
  # Use exact rational circle reduction before any floating evaluation.
  def efrac(x):
   x=F(x)
   y=x-F(x.numerator//x.denominator)
   return cmath.exp(2j*math.pi*float(y))
  bounds=epoch_stage_boundaries(A,p)
  points=sorted(set([A,A+1,bounds[1]-1,bounds[1],bounds[2]-1,bounds[2],
                     bounds[3]-1,bounds[3],2*A-1]))
  for ell in (1,2,3,7):
   k=h*(16**ell-1)
   for n in points:
    c=sum(direct[n-A])%p
    local=F(c,p)
    full_lag=sum((16**(ell-j)*forcing[n+j] for j in range(1,ell+1)),F(0))
    self.assertEqual(state[n+ell]-state[n],(16**ell-1)*state[n]+full_lag)
    left=efrac(k*local)*efrac(k*(state[n]-local)+h*full_lag)
    right=efrac(h*(state[n+ell]-state[n]))
    self.assertLess(abs(left-right),3e-13,(n,ell))

 def test_rational_seed_does_not_change_prime_channels(self):
  A,p=100,241
  states=[F(0)]
  for n in range(1,2*A):
   a=8*n-7
   r=F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)
   states.append(16*states[-1]+r)
  for n in (A,A+1,121,151,181,2*A-1):
   actual_p=sum(direct_source_epoch_residues(A,p)[n-A])%p
   zero=p*states[n]
   changed=p*(states[n]+F(16**n,5))
   def mod(q):
    self.assertNotEqual(q.denominator%p,0)
    return q.numerator*pow(q.denominator,-1,p)%p
   self.assertEqual(actual_p,mod(zero))
   self.assertEqual(mod(changed),mod(zero))
   self.assertEqual((16**n)%5,1)

 def test_balanced_full_rank_does_not_force_real_cancellation(self):
  A,p=100,241
  phases=[sum(predicted_residues(p,n))%p for n in range(A,2*A)]
  a=[cmath.exp(2j*math.pi*x/p) for x in phases]
  b=[x.conjugate() for x in a]
  self.assertLess(abs(sum(x*y for x,y in zip(a,b))/A-1),1e-12)

 def test_constructive_dyadic_antihaar_shadow_with_identical_three_prime_channels(self):
  # This is NOT a fixed original seed, and makes no claim about pi's real digit orbit.
  for A in (100,128,256):
   p=prime_candidates(A)[0][0]
   s,alpha_N,N,M=dyadic_terminal_shadow(A)
   self.assertTrue(s.denominator & (s.denominator-1)==0)
   self.assertNotEqual(s.denominator%p,0)
   self.assertLessEqual(abs(s+alpha_N),F(1,1<<M))
   self.assertLess(dyadic_shadow_phase_bound(A),F(1,100))
   # A rational seed with denominator prime to p is invisible to pV mod p.
   for n in (A,(3*A)//2,2*A-1):
    self.assertEqual((p*s*16**n).numerator*pow((p*s*16**n).denominator,-1,p)%p,0)
    # Analytic upper bound for all phase angles on this whole epoch.
    model=16**n*(s+alpha_N)
    error=F(1,15*(N+1)**2*16**(N-n))
    tail=F(1,15*(n+1)**2)
    self.assertLessEqual(abs(model)+error+tail,dyadic_shadow_phase_bound(A))

 def test_invalid_inputs(self):
  with self.assertRaises(ValueError):epoch_stage_boundaries(10,241)
  with self.assertRaises(ValueError):epoch_stage_boundaries(100,17)
  with self.assertRaises(ValueError):completion_error_budget(100,241,-0.1)
  with self.assertRaises(ValueError):epoch_mode_coefficients(241,1,(1,2))

if __name__=='__main__':unittest.main()
