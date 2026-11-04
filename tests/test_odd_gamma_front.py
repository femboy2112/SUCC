"""Independent Fraction and hostile checks for source-authentic Gamma and prime passports."""
from __future__ import annotations
import importlib.util
from fractions import Fraction as Q
from pathlib import Path
import unittest
import math
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'research/2026-11-03/split_inert_gamma_lag/odd_gamma_front.py'
spec=importlib.util.spec_from_file_location('odd_gamma_front',SRC)
f=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)

class SourceGaussianGamma(unittest.TestCase):
    def test_original_source_unchanged(self):
        for n in range(1,90):
            baseline=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(f.source(n),baseline)
            self.assertEqual(f.real_source(n)+f.gaussian_source(n),baseline)

    def test_signed_zero_seed_gluing(self):
        arr=list(f.fraction_states(90))
        self.assertEqual(arr[0],(0,Q(0),Q(0),Q(0)))
        for n,h,g,u in arr:
            self.assertEqual(u,h+g)
            if n:
                self.assertEqual(u,16*arr[n-1][3]+f.source(n))

    def test_geometric_gamma_tail_vs_independent_source_series(self):
        for n in (1,2,5,17,49,113):
            lo,hi=f.geometric_gamma_tail_interval(n,120)
            # Independent truncated true source series: positive sum -rH.
            x=sum((-Q(1,16**j)*f.real_source(n+j) for j in range(1,23)),Q(0))
            # Uniform |rH(n+j)| <2, omitted tail <=2*16^(-22)/15.
            tol=Q(2,15*16**22)
            self.assertLessEqual(lo,x+tol)
            self.assertGreaterEqual(hi,x)
            self.assertLessEqual(hi-lo,Q(1,32*n*2**120))

    def test_rational_compensation_sharp_and_positive(self):
        for n in (1,2,3,17,49,113,257,1023):
            lo,hi=f.gamma_corrected_tail_interval(n,140)
            self.assertGreater(lo,0)
            self.assertLess(hi, f.uniform_gamma_bound(n))
            self.assertGreater(hi,lo)

    def test_exact_mixed_compensation_law(self):
        import mpmath as mp
        mp.mp.dps=115
        theta=lambda h,k:k*mp.pi/16+(k-h)*mp.log(2)/8
        for n,h,g,u in f.fraction_states(50):
            if n not in (1,3,17,49):continue
            for a,b in ((1,0),(0,1),(1,1),(2,-3),(17,19)):
                phase=a*h+b*g+f.mixed_phase_correction(n,a,b)
                # Compare (large) real unwrapped phase to completed alpha.
                v=mp.mpf(phase.numerator)/phase.denominator - mp.power(16,n)*theta(a,b)
                bound=f.mixed_phase_error_bound(n,a,b)
                self.assertLess(abs(v),mp.mpf(bound.numerator)/bound.denominator)

    def test_chord_upper_and_errors(self):
        for a,b in ((1,0),(1,1),(2,-3)):
            full=f.phase_sum_chord_upper(a,b)
            part=f.phase_sum_chord_upper(a,b,early=8)
            self.assertLess(part,full)
            self.assertGreaterEqual(full,0)
        for bad in (lambda:f.source(0),lambda:f.mixed_phase_correction(0,1,1),
                    lambda:f.geometric_gamma_tail_interval(1,0),
                    lambda:f.phase_sum_chord_upper(1,1,early=0)):
            with self.assertRaises(ValueError):bad()

class PrimePassports(unittest.TestCase):
    def test_inert_secondary_poles_are_real(self):
        # Earlier tempting window [k,2k) is FALSE. Both mod8 cases.
        for k,p,additional in ((11,43,Q(4,3)),(12,47,-Q(1,3))):
            self.assertEqual(f.inert_second_injection_index(k),(3*k+1)//2)
            self.assertEqual(f.pole_injection_residue(k,p),(-pow(2,-1,p))%p)
            n=f.inert_second_injection_index(k)
            self.assertEqual(f.pole_injection_residue(n,p),
                             (additional.numerator*pow(additional.denominator,-1,p))%p)
            with self.assertRaises(ValueError):f.window_prime_clock(p,k,n,'inert')

    def test_exact_residues_original_fraction(self):
        # Development A=16,32,64,128. Fresh A=96,192 in predeclared probe.
        for A in (16,32,64,128):
            ps=f.prime_passports(A)
            last=ps['stop']-1
            states=list(f.fraction_states(last))
            for kind in ('split','inert'):
                for p,birth in ps[kind]:
                    for n in range(A,ps['stop']):
                        x=p*states[n][3]
                        self.assertNotEqual(x.denominator%p,0)
                        observed=(x.numerator*pow(x.denominator,-1,p))%p
                        expected=f.window_prime_clock(p,birth,n,kind)
                        self.assertEqual(observed,expected,(A,kind,p,n))

    def test_class_disjointness_and_valid_windows(self):
        for A in (16,32,64,128,256):
            ps=f.prime_passports(A)
            self.assertTrue(all(p%8==1 for p,_ in ps['split']))
            self.assertTrue(all(p%4==3 for p,_ in ps['inert']))
            self.assertTrue(all(b<=A for p,b in ps['split']+ps['inert']))
            self.assertTrue(all(n2>=ps['stop'] for p,b in ps['inert']
                                for n2 in [f.inert_second_injection_index(b)]))

    def test_exact_prime_product_and_alias_counts(self):
        for A in (16,32,64,128,256):
            p=f.exact_prime_mass_profile(A)
            self.assertGreaterEqual(p['minimum_nonaliases_across_lags'],0)
            if A==32:
                self.assertFalse(p['exact_mass_dominates_full_window'])
            if A in (64,128):
                self.assertTrue(p['exact_mass_dominates_full_window'])

    def test_variable_interval_clean_and_original_no_repeat(self):
        for A,c0,c1 in ((64,7,5),(128,4,3),(96,5,4)):
            ps=f.prime_passports(A,c0,c1)
            states=list(f.fraction_states(ps['stop']-1))
            for typ in ('split','inert'):
                for p,birth in ps[typ]:
                    for n in range(A,ps['stop']):
                        z=p*states[n][3]
                        self.assertNotEqual(z.denominator%p,0)
                        self.assertEqual(z.numerator*pow(z.denominator,-1,p)%p,
                                         f.window_prime_clock(p,birth,n,typ))
            if f.exact_prime_mass_profile(A,c0,c1)['exact_mass_dominates_full_window']:
                # Exact finite selected rational non-repeat; proves no asymptotic.
                xs=[states[n][3]%1 for n in range(A,ps['stop'])]
                for h in (1,3,7,16):
                    self.assertEqual(len({(h*x)%1 for x in xs}),len(xs))

    def test_bad_window_c(self):
        for c in ((3,2),(1,1),(2,1)):
            with self.assertRaises(ValueError):f.prime_passports(16,*c)

if __name__ == '__main__':unittest.main()
