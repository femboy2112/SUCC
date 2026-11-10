"""Independent exact controls for digit cyclotomic returns and de Bruijn flux."""
import unittest
from fractions import Fraction
from collections import Counter
from itertools import product
from pathlib import Path
import math
from observational_succ.bbp_word_spectroscopy import (
 BASE, ORDERS, validate_digits, cyclotomic_balances, exact_reset_walk,
 word_counts_cyclic, word_counts_linear, de_bruijn_divergence, cycle_dimension, full_word_reset_horizons,
 primitive_word_sector, word_energy, spectral_refinement,
 iid_exact_balanced_probability, planar_return_probability,
 circle_digit_fourier_coeff, renormalized_real_energy,
)

class SpectralReturnTests(unittest.TestCase):
 def test_cyclotomic_antipodes(self):
  counts=[0]*16
  for i in range(16): counts[i]=i+1
  for m in ORDERS:
   b=cyclotomic_balances(counts,m)
   self.assertEqual(len(b),m//2)
   for h in range(1,16):
    if 16//math.gcd(16,h)==m:
     z=sum(c*complex(math.cos(2*math.pi*h*d/16),math.sin(2*math.pi*h*d/16)) for d,c in enumerate(counts))
     self.assertEqual(all(v==0 for v in b), abs(z)<1e-9)

 def test_phase_zero_vs_full_zero(self):
  x=(2,4,3,15)
  r=exact_reset_walk(x)
  self.assertEqual(r['spectral_zeros']['2'], [4])
  self.assertEqual(r['exact_uniform_histogram'],[])

 def test_full_word_reset_horizons(self):
  xs=tuple(range(16))*32
  self.assertEqual(full_word_reset_horizons(xs,1),list(range(16,len(xs)+1,16)))
  self.assertEqual(full_word_reset_horizons(xs,2),[])
  self.assertEqual(full_word_reset_horizons(xs,3),[])

 def test_uniform_cycle_all_depths(self):
  # All single symbols once: k=1 is zero, but depth2 is highly nonuniform.
  xs=tuple(range(16))
  r=spectral_refinement(xs,2)
  self.assertEqual(r['1']['energy'],0)
  self.assertEqual(r['2']['energy'],15)
  self.assertEqual(r['2']['new_energy'],15)
  self.assertEqual(sum(r['2']['primitive_sectors'].values()),15)

 def test_extreme_coherent_all_sectors(self):
  xs=(0,)*64
  r=spectral_refinement(xs,3)
  for k in range(1,4):
   B=BASE**k
   self.assertEqual(r[str(k)]['energy'],B-1)
   self.assertEqual(r[str(k)]['new_energy'], (B-1)-(BASE**(k-1)-1))

 def test_independent_parseval_by_exact_counts(self):
  for xs in ((0,1,2,3,4,5,6,7), tuple(range(16)), tuple([0,5,5,10]*8)):
   r=spectral_refinement(xs, 3)
   for k in range(1,4):
    counts=word_counts_cyclic(xs,k)
    self.assertEqual(r[str(k)]['energy'],word_energy(counts,len(xs),k))
    self.assertEqual(sum(r[str(k)]['primitive_sectors'].values()),r[str(k)]['new_energy'])

 def test_full_fourier_orthogonality(self):
  xs=(0,3,4,9,2,6,14,5)
  for k in (1,2):
   c=word_counts_cyclic(xs,k); e=word_energy(c,len(xs),k)
   total=0.
   for h in product(range(16),repeat=k):
    if all(a==0 for a in h):continue
    z=sum(v*complex(math.cos(2*math.pi*sum(a*b for a,b in zip(h,w))/16),
                             math.sin(2*math.pi*sum(a*b for a,b in zip(h,w))/16)) for w,v in c.items())/len(xs)
    total+=abs(z)**2
   self.assertAlmostEqual(float(e),total,places=10)

 def test_de_bruijn_open_boundary(self):
  xs=(1,2,3,1,2,3,4)
  for k in (2,3):
   c=word_counts_linear(xs,k)
   self.assertEqual(de_bruijn_divergence(c,k), {tuple(xs[:k-1]):1,tuple(xs[-k+1:]): -1})
   self.assertFalse(de_bruijn_divergence(word_counts_cyclic(xs,k),k))

 def test_cycle_rank(self):
  self.assertEqual(cycle_dimension(1),(16,16,15))
  self.assertEqual(cycle_dimension(2),(256,241,240))
  self.assertEqual(cycle_dimension(3),(4096,3841,3840))

 def test_iid_balanced_probability(self):
  self.assertEqual(iid_exact_balanced_probability(16),Fraction(math.factorial(16),16**16))
  self.assertEqual(iid_exact_balanced_probability(17),0)
  self.assertGreater(iid_exact_balanced_probability(16),iid_exact_balanced_probability(32))

 def test_planar_exact_returns(self):
  self.assertEqual(planar_return_probability(0),1)
  self.assertEqual(planar_return_probability(2),Fraction(1,4))
  self.assertEqual(planar_return_probability(4),Fraction(9,64))
  with self.assertRaises(ValueError):planar_return_probability(3)

 def test_gamma_critical_finite_part(self):
  m=1000
  p=1.
  partial=p
  for n in range(1,m+1):
   p*=((2*n-1)/(2*n))**2
   partial+=p
  prediction=(0.57721566490153286+math.log(16))/math.pi
  self.assertLess(abs(partial-math.log(m)/math.pi-prediction),1e-3)

 def test_arithmetic_progression_alias(self):
  self.assertEqual(circle_digit_fourier_coeff(1,0),0j)
  self.assertEqual(circle_digit_fourier_coeff(1,2),0j)
  self.assertNotEqual(circle_digit_fourier_coeff(1,17),0j)
  self.assertAlmostEqual(abs(circle_digit_fourier_coeff(1,17)),abs(circle_digit_fourier_coeff(1,1))/17,places=12)

 def test_renormalized(self):
  self.assertEqual(renormalized_real_energy(Fraction(15,16),16,1),1)

 def test_bad_data(self):
  with self.assertRaises(ValueError):validate_digits((1,16))
  with self.assertRaises(ValueError):word_counts_cyclic((0,1),3)
  with self.assertRaises(ValueError):cyclotomic_balances([0]*16,3)
  with self.assertRaises(ValueError):primitive_word_sector(Counter({(0,):4}),5,1,2)

if __name__ == '__main__': unittest.main()

class DigitCircleAliasTests(unittest.TestCase):
 def test_support_ladders(self):
  from observational_succ.bbp_word_spectroscopy import real_fourier_alias_condition,first_nonzero_digit_character
  for h,t_true,t_false,j in (
      ((1,),1,16,1), ((0,7),16*7,7,2), ((0,0,2),16*16*2,16*2,3),
      ((1,8,5),1,16,1), ((0,0,0,15),15*16**3,16**3,4)):
   self.assertEqual(first_nonzero_digit_character(h),j)
   self.assertTrue(real_fourier_alias_condition(h,t_true))
   self.assertFalse(real_fourier_alias_condition(h,t_false))

 def test_word_fourier_against_direct_step_integral(self):
  import cmath
  from observational_succ.bbp_word_spectroscopy import word_character_circle_fourier_coeff
  for h in ((1,0),(0,1),(5,3),(0,7),(0,0,1),(2,3,4)):
   size=16**len(h)
   for t in (-255, -32, -1, 0, 1, 17, 112, 256):
    actual=word_character_circle_fourier_coeff(h,t)
    if t==0:
     direct=sum(cmath.exp(2j*math.pi*sum(h[j]*((q//16**(len(h)-j-1))%16) for j in range(len(h)))/16) for q in range(size))/size
    else:
     factor=(1-cmath.exp(-2j*math.pi*t/size))/(2j*math.pi*t)
     direct=factor*sum(cmath.exp(2j*math.pi*sum(h[j]*((q//16**(len(h)-j-1))%16) for j in range(len(h)))/16)
                             * cmath.exp(-2j*math.pi*t*q/size) for q in range(size))
    self.assertLess(abs(actual-direct),2e-9, (h,t,actual,direct))

 def test_single_digit_alias(self):
  from observational_succ.bbp_word_spectroscopy import word_character_circle_fourier_coeff,circle_digit_fourier_coeff
  for h in (1,4,8,15):
   for t in (-31,-16,-1,0,1,4,8,15,17,31,32):
    self.assertLess(abs(word_character_circle_fourier_coeff((h,),t)-circle_digit_fourier_coeff(h,t)),2e-11)

class InheritedZeroOriginFixture(unittest.TestCase):
 def test_certified_previous_branch_prefix_resets(self):
  import hashlib
  from observational_succ.bbp_word_spectroscopy import full_word_reset_horizons
  path=Path(__file__).resolve().parents[1]/'research/2026-11-08/zero_origin_spectral_flux/CERTIFIED_HEX_16384.txt'
  raw=path.read_bytes()
  self.assertEqual(hashlib.sha256(raw).hexdigest(),'4c00dfdde55b749bdfb8e219df8116314111566f1c9711c7ee062d345d3321e1')
  ds=tuple(int(c,16) for c in raw.decode().strip())
  self.assertEqual(len(ds),16384)
  results=exact_reset_walk(ds)
  self.assertEqual({k:len(v) for k,v in results['spectral_zeros'].items()},
                   {'2':157,'4':5,'8':0,'16':0})
  self.assertEqual(results['spectral_zeros']['4'],[2,24,1132,1134,1148])
  self.assertEqual(results['exact_uniform_histogram'],[])
  self.assertEqual([full_word_reset_horizons(ds,k) for k in (1,2,3)],[[],[],[]])
  r=spectral_refinement(ds,max_depth=3)
  self.assertEqual(r['1']['energy'],Fraction(5477,8388608))
  self.assertEqual(r['2']['energy'],Fraction(8009,524288))
  self.assertEqual(r['3']['energy'],Fraction(8013,32768))
