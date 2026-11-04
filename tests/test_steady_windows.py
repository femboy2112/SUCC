"""Exact BBP window-balance diagnostics and strict theorem calibrations."""
import cmath
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research'/'2026-11-02'/'steady_window_balance'/'steady_windows.py'
S=importlib.util.spec_from_file_location('steady_windows',P)
w=importlib.util.module_from_spec(S);S.loader.exec_module(w)

def e(q):
 q=Fraction(q); a=(q.numerator%q.denominator)/q.denominator
 return cmath.exp(2j*math.pi*a)

class WindowTests(unittest.TestCase):
 def test_exact_odd_source_all_indices(self):
  for n in range(1,1025):
   self.assertEqual(w.source(n),w.odd_source(n))
   self.assertEqual(w.source(n).denominator%2,1)

 def test_actual_all_rational_denominators_odd(self):
  U=w.states(512)
  self.assertTrue(all(u.denominator%2 for u in U))
  for h in (1,2,3,16):
   for a,b in [(11,36),(0,17),(128,256)]:
    self.assertNotEqual(w.centered(h*(U[a]-U[b])),Fraction(1,2))

 def test_exact_causal_lag_all_four_original_poles(self):
  U=w.states(128)
  for n,L in [(0,1),(2,5),(30,13),(64,32)]:
   F=w.lag_forcing(U,n,L)
   self.assertEqual(U[n+L]-U[n], (16**L-1)*U[n]+F)

 def test_aligned_time_pair_bound_float_verification(self):
  U=w.states(1024)
  for a,L,h in [(16,8,1),(64,32,2),(128,64,3),(256,128,16),(512,256,1)]:
   C=w.exact_time_antiphase_cost(U,a,L,h)
   S=sum((e(h*U[n]) for n in range(a,a+2*L)),0j)
   self.assertLessEqual(abs(S)/(2*L),math.pi*float(C)+1e-10)

 def test_phase_bin_antiphase_partition_and_root_flip(self):
  for M,h in [(16,1),(64,2),(64,3),(64,16),(256,48),(256,7)]:
   pairs=w.antiphase_bin_pairs(M,h)
   self.assertEqual(len(pairs),M//2)
   self.assertEqual(sorted([v for a,b in pairs for v in (a,b)]),list(range(M)))
   for a,b in pairs:
    # center character is exactly negated by the half-cycle shift
    angle=Fraction(h*(b-a),M)
    self.assertEqual(angle.denominator,2)

 def test_source_phase_window_bound_float_verification(self):
  U=w.states(2048)
  for start,N,M,h in [(64,64,16,1),(128,128,32,2),
                       (256,256,64,3),(512,512,64,16),(1024,1024,256,1)]:
   counts=w.exact_phase_bins(U,start,N,M)
   C=w.antipodal_imbalance(counts,h)
   S=sum((e(h*U[n]) for n in range(start,start+N)),0j)
   self.assertLessEqual(abs(S)/N,float(C)+math.pi*abs(h)/M+1e-10)

 def test_imbalance_controlled_by_collision_excess_exactly(self):
  U=w.states(2048)
  for start,N,M,h in [(64,64,16,1),(128,128,64,2),(256,256,64,3),
                       (512,512,256,16),(1024,1024,256,1)]:
   counts=w.exact_phase_bins(U,start,N,M)
   A,E=w.coarse_phase_sensitivity(counts,h)
   self.assertLessEqual(A*A,E)
   self.assertGreaterEqual(E,0)

 def test_balanced_exact_phase_windows_control(self):
  for M,h in ((16,1),(64,2),(64,16)):
   counts=[7]*M
   self.assertEqual(w.antipodal_imbalance(counts,h),0)
   self.assertEqual(w.histogram_energy(counts),1)

 def test_wrong_seed_fixed_point_has_no_window_balance(self):
  for M,h in ((16,1),(64,2),(64,16)):
   counts=[0]*M
   counts[M//5]=1000
   self.assertEqual(w.antipodal_imbalance(counts,h),1)
   self.assertEqual(w.histogram_energy(counts),M)

 def test_false_even_h_global_halfturn(self):
  M=64; h=2; c=[0]*M
  c[0]=8;c[M//2]=8
  # ordinary global 1/2 reflection balances 2 cells, but h=2 character
  # sees both as identical. h-specific shift M/4 reveals imbalance.
  self.assertEqual(sum(abs(c[j]-c[j+M//2]) for j in range(M//2)),0)
  self.assertEqual(w.antipodal_imbalance(c,h),1)

 def test_source_finite_completion_cocycle(self):
  U=w.states(40)
  for B in (5,13,27,40):
   a=w.alpha_from_source(B)
   for n in range(B+1):
    self.assertEqual(U[n],16**n*a-w.finite_future(n,B))

 def test_source_pseudo_stationarity_character_bound(self):
  for N in (128,512):
   U=w.states(N)
   for h in (1,3,16):
    c0=sum((e(h*U[n]) for n in range(N)),0j)/N
    c1=sum((e(16*h*U[n]) for n in range(N)),0j)/N
    A,B=w.pseudo_stationarity_character_budget(N,h)
    self.assertLessEqual(abs(c1-c0),float(A)+math.pi*float(B)+1e-10)

 def test_second_integer_oracle_matches_fraction_source(self):
  D,arr=w.common_odd_modular_lift(511)
  U=w.states(511)
  self.assertEqual(D%2,1)
  for n in range(512):
   self.assertEqual(Fraction(arr[n],D),Fraction(U[n].numerator%U[n].denominator,U[n].denominator))

 def test_second_integer_oracle_matches_fraction_halfturn_cost(self):
  D,arr=w.common_odd_modular_lift(255)
  U=w.states(255)
  for a,L,h in [(16,8,1),(32,16,2),(64,32,16),(96,16,3)]:
   n,den=w.modular_time_pair_cost(D,arr,a,L,h)
   self.assertEqual(Fraction(n,den),w.exact_time_antiphase_cost(U,a,L,h))

 def test_second_integer_oracle_matches_fraction_histograms(self):
  D,arr=w.common_odd_modular_lift(511)
  U=w.states(511)
  for A,M in [(64,16),(128,64),(256,128)]:
   self.assertEqual(w.modular_bins(D,arr,A,A,M),w.exact_phase_bins(U,A,A,M))

if __name__=='__main__':unittest.main()
