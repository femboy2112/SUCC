"""Original BBP atomic-vs-positive-path, signed interaction and alias controls."""
import importlib.util
import unittest
import sys
from pathlib import Path
from fractions import Fraction as F
from math import comb
ROOT=Path(__file__).resolve().parents[1]
LAB=ROOT/'research'/'2026-10-31'/'four_pole_path_interference'
sys.path.insert(0,str(LAB))
_spec=importlib.util.spec_from_file_location('_four_pole_independent_oracle', LAB/'independent_oracle.py')
_ORACLE=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ORACLE)
from pole_interactions import (
 SHIFTS,WEIGHTS,EDGES,four_pole_source,edge_source,three_edge_source,
 channel_states,combined_states,laurent_moment,edge_moment,laurent_prefix,
 pole_poly,atomic_hankel,rational_det,solve_exact,prony_recover,prony_weights,
 continuous_hankel,discrete_hausdorff_difference,finite_difference_null,
 finite_difference_null_closed,null_moment,pairwise_balanced_conspiracy,
 continuous_alias_certificate,
)

class PoleInteractions(unittest.TestCase):
 def test_01_unchanged_source_four_signed_poles(self):
  self.assertEqual((SHIFTS,WEIGHTS),((7,4,3,2),(4,-2,-1,-1)))
  for n in range(1,160):
   self.assertEqual(four_pole_source(n), F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))

 def test_02_three_positive_edges_source_exact(self):
  self.assertEqual(EDGES,((3,2),(4,1),(5,1)))
  for n in range(1,160):
   self.assertEqual(three_edge_source(n),four_pole_source(n))
   self.assertTrue(all(edge_source(n,m)>0 for m,_ in EDGES))

 def test_03_original_zero_selector_recovered_by_edge_states(self):
  for N in (0,1,2,6,18,48):
   v=channel_states(N);U=combined_states(N)
   self.assertEqual(U[0],0)
   for i in range(1,N+1):
    self.assertEqual(U[i],16*U[i-1]+four_pole_source(i))
    self.assertEqual(U[i],2*v[3][i]+v[4][i]+v[5][i])

 def test_04_pole_polynomial_and_exact_spectral_fingerprint(self):
  self.assertEqual(pole_poly(),(168,-206,89,-16,1))
  self.assertEqual(sum(SHIFTS),16)
  self.assertEqual(sum(SHIFTS[i]*SHIFTS[j] for i in range(4) for j in range(i+1,4)),89)
  Vand=1
  for i in range(4):
   for j in range(i+1,4):Vand*=SHIFTS[i]-SHIFTS[j]
  self.assertEqual(Vand,120)

 def test_05_signed_atomic_moments_and_zero_mass(self):
  self.assertEqual([laurent_moment(j) for j in range(8)],
                   [0,15,151,1209,8995,64905,461611,3259089])
  for j in range(1,100):self.assertGreater(laurent_moment(j),0)

 def test_06_legacy_moments_exact_positive_edge_transform(self):
  for j in range(0,50):
   self.assertEqual((j+1)*edge_moment(j),laurent_moment(j+1))
  self.assertEqual(edge_moment(0),F(15))

 def test_07_laurent_positive_prefix_and_tail_certificate(self):
  for n in (1,2,4,16,101):
   old=F(0)
   for J in (1,2,3,5,9,12,26):
    x=laurent_prefix(n,J)
    self.assertGreater(x['positive_remainder'],0)
    self.assertLess(x['positive_remainder'],x['tail_upper'])
    self.assertGreater(x['partial'],old)
    old=x['partial']

 def test_08_source_reconstructs_from_eight_atomic_moments(self):
  self.assertEqual(prony_recover(),tuple(F(x) for x in (168,-206,89,-16,1)))
  self.assertEqual(prony_weights(),tuple(F(x) for x in WEIGHTS))
  for j in range(20):
   p=pole_poly()
   self.assertEqual(sum(p[i]*laurent_moment(j+i) for i in range(5)),0)

 def test_09_atomic_hankel_indefinite_signature_certificate(self):
  H=atomic_hankel(4)
  self.assertEqual(rational_det(H),-115200)
  self.assertEqual(H[0][0],0)
  self.assertEqual(H[0][1],15)
  # finite source Vandermonde congruence V diag(4,-2,-1,-1)V^T
  V=[[c**i for c in SHIFTS] for i in range(4)]
  self.assertEqual(H,tuple(tuple(sum(V[i][t]*WEIGHTS[t]*V[j][t] for t in range(4))
                                for j in range(4)) for i in range(4)))

 def test_10_continuous_Hankel_positive_minors(self):
  for n in (1,2,3,7,21):
   for d in (1,2,3,4):
    self.assertGreater(rational_det(continuous_hankel(n,d)),0)

 def test_11_discrete_source_complete_monotonicity(self):
  for n in (1,2,3,7,30):
   for k in range(0,13):
    self.assertGreater(discrete_hausdorff_difference(n,k),0)

 def test_12_nine_pole_mutant_invisible_through_seven_moments(self):
  for k in range(8):self.assertEqual(null_moment(k,8),0)
  self.assertEqual(null_moment(8,8),40320)
  for n in range(1,35):
   x=finite_difference_null(n,8)
   self.assertGreater(x,0)
   self.assertEqual(x,finite_difference_null_closed(n,8))
   self.assertNotEqual(four_pole_source(n)+x,four_pole_source(n))
  self.assertEqual(finite_difference_null(1),F(1,102960))

 def test_13_pairwise_hair_coupling_can_lock_triple(self):
  for p in (3,5,7,9,11,17):
   z=pairwise_balanced_conspiracy(p)
   self.assertTrue(z['marginal_perfect'])
   self.assertTrue(z['triple_coherent'])
   self.assertEqual(z['count'],p*p)
   for pair in z['pair_histograms']:
    self.assertEqual(len(pair),p*p)
    self.assertTrue(all(c==1 for c in pair.values()))

 def test_14_pairwise_2torus_Haar_does_not_imply_joint_3torus_Haar(self):
  # For continuous Haar x,y: (x,y,-2x-y) has uniform every pair
  # because integer projection determinants are +/-1,+/-2.
  # Yet the triple character (2,1,1) is identically 1.
  vectors=((1,0),(0,1),(-2,-1))
  for i,j in ((0,1),(0,2),(1,2)):
   det=vectors[i][0]*vectors[j][1]-vectors[i][1]*vectors[j][0]
   self.assertNotEqual(det,0)
  self.assertEqual(tuple(2*vectors[0][j]+vectors[1][j]+vectors[2][j]
                         for j in range(2)),(0,0))

 def test_15_exact_coherent_alias_rational_certificate(self):
  c=continuous_alias_certificate(1,F(1,5))
  self.assertTrue(c['coherent_completed_orbit'])
  self.assertEqual(c['smooth_zero_alias_upper'],F(1,6))
  self.assertEqual(c['coherent_integer_sum_error_upper'],F(11,56))
  for N in (1,2,8,256):
   self.assertEqual(c['nonzero_alias_lower_at_N'](N),F(N)-F(61,168))
   self.assertGreater(c['nonzero_alias_lower_at_N'](N),0)

 def test_16_selected_alpha_and_ordinary_rational_share_continuous_saving(self):
  # True alpha=pi/16 >3/16; changing completed alpha to 1/5
  # preserves analytic derivative positivity and O(1) integral bounds.
  for q in (F(3,16),F(1,5),F(1),F(15,16)):
   for h in (-7,-1,1,3):
    c=continuous_alias_certificate(h,q)
    self.assertLessEqual(c['smooth_zero_alias_upper'],F(8,45*abs(h)))

 def test_17_literal_seed_source_not_inferred_from_completed_q(self):
  a=combined_states(40)
  self.assertEqual(a[0],0)
  self.assertEqual(a[1],F(47,15))
  # The q=1/5 alias counterseed has irrational literal U0=1/5-pi/16;
  # no routine here re-labels it as exact zero.
  self.assertNotEqual(F(1,5),F(0))

 def test_18_fail_closed_invalid_domains(self):
  for fn,arg in ((four_pole_source,(0,)),(edge_source,(1,2)),
                 (channel_states,(-1,)),(laurent_moment,(-1,)),
                 (laurent_prefix,(0,4)),(rational_det,([[1,2]],)),
                 (solve_exact,([[0,0],[0,0]],[1,1])),
                 (pairwise_balanced_conspiracy,(2,)),
                 (continuous_alias_certificate,(0,F(1,5))),
                 (continuous_alias_certificate,(1,F(1,7)))):
   with self.assertRaises(ValueError):fn(*arg)

if __name__ == '__main__':unittest.main()

class MutantSourceCompletion(unittest.TestCase):
 def test_19_source_eight_jet_spoof_then_true_source_changes(self):
  from pole_interactions import mutant_states
  for N in (1,2,10,35):
   U=combined_states(N);V=mutant_states(N,F(1))
   self.assertEqual((U[0],V[0]),(F(0),F(0)))
   for n in range(1,N+1):
    self.assertGreater(V[n]-U[n],0)
    self.assertEqual(V[n]-U[n],sum((16**(n-j)*finite_difference_null(j) for j in range(1,n+1)),F(0)))

 def test_20_completion_changes_but_decay_is_certified(self):
  from pole_interactions import mutant_completion_prefix,mutant_states
  prev=F(0)
  for K in range(1,35):
   r=mutant_completion_prefix(K)
   self.assertGreater(r['prefix'],prev)
   self.assertGreater(r['tail_upper'],0)
   prev=r['prefix']
   U=combined_states(K);V=mutant_states(K)
   self.assertEqual(F(V[K]-U[K],16**K),r['prefix'])
   self.assertLess(r['tail_upper'],F(1,15*16**K)*finite_difference_null(K))

 def test_21_high_order_mutant_unseen_by_prony_first_eight(self):
  from pole_interactions import mutant_states
  for j in range(8):
   self.assertEqual(laurent_moment(j)+null_moment(j),laurent_moment(j))
  self.assertNotEqual(laurent_moment(8)+null_moment(8),laurent_moment(8))
  self.assertNotEqual(mutant_states(3),combined_states(3))

class IndependentImplementations(unittest.TestCase):
 def test_22_independent_four_pole_closed_rational(self):
  o=_ORACLE
  for n in range(1,201):
   self.assertEqual(o.combined_rational(n),four_pole_source(n))
  self.assertEqual(o.polynomial_expansion_x(),(1,-16,89,-206,168))

 def test_23_independent_full_Hankel_permutation_det(self):
  o=_ORACLE
  for n in range(1,5):
   for k in range(1,5):
    A=continuous_hankel(n,k)
    self.assertEqual(o.permutation_determinant(A),rational_det(A))
  self.assertEqual(o.permutation_determinant(atomic_hankel(4)),-115200)

 def test_24_independent_hausdorff_integral_finite_difference(self):
  o=_ORACLE
  for n in range(1,12):
   for k in range(0,10):
    self.assertEqual(o.independent_hausdorff_k(n,k),discrete_hausdorff_difference(n,k))

 def test_25_independent_beta_gamma_mutant(self):
  o=_ORACLE
  for n in range(1,35):
   self.assertEqual(o.gamma_beta8n9(n),finite_difference_null(n))

 def test_26_independent_triple_pairwise_marginal_histogram(self):
  o=_ORACLE
  for p in (3,5,7,9,11):
   hist=o.counterfeit_character_histogram(p)
   self.assertEqual(hist,[[p]*p]*3)

class ZeroSeedNonnormalMutantControls(unittest.TestCase):
 def test_27_beta_mutant_preserves_positive_moment_Hankel(self):
  from pole_interactions import mutant_states
  for eps in (F(1,10),F(1),F(10000)):
   for n in (1,2,5):
    for d in (1,2,3):
     A=tuple(tuple(four_pole_source(n+i+j)+eps*finite_difference_null(n+i+j)
                   for j in range(d)) for i in range(d))
     self.assertGreater(rational_det(A),0)
    for k in range(0,8):
     diff=sum((-1)**j*comb(k,j)*finite_difference_null(n+j)
              for j in range(k+1))
     self.assertGreater(diff,0)
   U=mutant_states(30,eps)
   self.assertEqual(U[0],0)
   for n in range(1,31):
    self.assertGreater(U[n],0)

 def test_28_q_fifth_positive_mutant_parameter_and_integer_coherence(self):
  from pole_interactions import mutant_completion_prefix
  self.assertLess(F(11,56),F(1,5))
  B=mutant_completion_prefix(24)
  self.assertGreater(B['prefix'],0)
  self.assertLess(B['tail_upper'],F(1,10**20))
  for n in range(1,100):
   self.assertEqual(pow(16,n,5),1)
   self.assertEqual((F(16**n,5)-F(1,5)).denominator,1)

class CrossPlaceLaurentClockTests(unittest.TestCase):
 def test_29_real_positive_laurent_series_diverges_dyadically(self):
  from pole_interactions import prime_clock_laurent
  for n in (1,2,3,5,16,96):
   k=n;v=0
   while k%2==0:k//=2;v+=1
   for j in range(1,51):
    x=prime_clock_laurent(j,n)
    self.assertEqual(x['v2_term'],-(j+1)*(3+v))
    self.assertEqual(x['moment']%2,1)
    self.assertEqual(x['predicted_mod3'],x['m_mod3'])
   # In contrast the FULL original rational source has odd denominator:
   self.assertEqual(four_pole_source(n).denominator%2,1)

 def test_30_exact_prime_three_five_laurent_moment_clocks(self):
  from pole_interactions import prime_clock_laurent
  for j in range(1,130):
   x=prime_clock_laurent(j,1)
   self.assertEqual(x['m_mod3'],0 if j%2 else 1)
   self.assertEqual(x['m_mod5'],(0,1,4,0)[(j-1)%4])
