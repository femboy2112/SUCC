"""Focused independent checks of critical Fejer source-tail and finite rational caps.
Nothing in this suite verifies any all-N pi-normality hypothesis.
"""
import unittest
from math import sqrt,pi
from fractions import Fraction
from experiment import (r_exact,r_four_poles,original,rational_tail,
                        fejer_weighted_spectrum,fejer_pair_float,
                        exact_majorant_quantized,near_pair_count,probe,run)
from spectral_transport import (original_mod_clock,shadow_mod_clock,
                                transformed_character)

class CriticalCollisionTests(unittest.TestCase):
    def test_exact_original_four_poles_and_rational_tail(self):
        self.assertEqual(original(1),[Fraction(0)])
        for n in range(1,1025):
            self.assertEqual(r_exact(n),r_four_poles(n))
            if n>=2:self.assertTrue(Fraction(0)<r_exact(n)<Fraction(1,n*n))
        for n in (1,2,17,100):
            self.assertLess(rational_tail(n),Fraction(1,15*(n+1)**2))

    def test_fejer_pair_identity_and_kernel_baseline(self):
        xs=original(32)
        for H in (5,8,16):
            p=fejer_pair_float([float(x) for x in xs],H)
            s=fejer_weighted_spectrum([float(x) for x in xs],H)
            self.assertAlmostEqual(p,s,places=8)
            self.assertGreaterEqual(s,1-1e-10)

    def test_exact_rational_upper_smaller_than_3_critical_scale(self):
        # Conservatively quantized exact rational majorants. Every assertion
        # is an integer comparison, not a floating Fourier estimate.
        for N in (128,256):
            cap=exact_majorant_quantized(original(N),N)
            self.assertTrue(cap['distinct_pairs'])
            self.assertLess(cap['bound_numerator'],3*cap['bound_denominator'])
        cap512=exact_majorant_quantized(original(512),512)
        self.assertTrue(cap512['distinct_pairs'])
        self.assertLess(cap512['bound_numerator'],3*cap512['bound_denominator'])
        self.assertEqual(cap512['bound_numerator'],769526344650)
        self.assertEqual(cap512['bound_denominator'],262144000000)

    def test_near_pairs_source_and_bad_controls(self):
        N=128
        xs=original(N)
        got=near_pair_count(xs,N)
        brute=sum(int(min(abs(a-b),1-abs(a-b))<=Fraction(1,N)) for a in xs for b in xs)
        self.assertEqual(got,brute)
        self.assertEqual(got,356)
        periodic=[Fraction(pow(16,n,17),17) for n in range(N)]
        self.assertEqual(near_pair_count(periodic,N),N*N//2)
        shadow=[Fraction(n,(2*n-1)**4) for n in range(N)]
        self.assertGreater(near_pair_count(shadow,N),N*N*0.95)

    def test_hilbert_source_tail_transfer_diagnostics(self):
        for N,H in ((32,8),(64,16),(128,32),(128,128),(256,256)):
            v=probe(N,H,do_majorant=False)
            self.assertLessEqual(v['sqrt_energy_distance_float'],4*sqrt(H*(H+1))/N+1e-9)
        self.assertLess(2+4*sqrt(pi/15),4)

    def test_two_place_clock_basis_isometry_and_odd_energy(self):
        for Q in (32,64,128):
            xs=original(Q)
            sh=[Fraction(n,(2*n-1)**4) for n in range(Q)]
            a=transformed_character(xs,original_mod_clock(Q))
            b=transformed_character(sh,shadow_mod_clock(Q))
            self.assertAlmostEqual(a['all_band_energy_float'],1.0,places=9)
            self.assertAlmostEqual(b['all_band_energy_float'],1.0,places=9)
            self.assertGreater(a['odd_2adic_band_energy_float'],0.3)
            self.assertLess(b['odd_2adic_band_energy_float'],0.001)

    def test_kempner_sparse_digit_but_large_collision(self):
        for N in (64,128,256):
            ph=[sum(16.0**(n-(1<<k)) for k in range(16) if (1<<k)>n)
                for n in range(N)]
            self.assertGreater(fejer_weighted_spectrum(ph,N),N/2)
            # Source and phase are NOT original pi; this is a hostile control.

    def test_finite_normality_ray_certificate(self):
        # Analytically derived implication: C_N,N < 3 controls each fixed h,
        # but at finite N can be weak and does not prove all-scale contraction.
        from cmath import exp
        N=512;h=1
        xs=original(N)
        w=abs(sum(exp(2j*pi*h*float(x)) for x in xs)/N)
        J=0
        while h*(16**(J+1))<=N//2:J+=1
        cap=Fraction(769526344650,262144000000)
        rhs=sqrt(float((cap-1)/(J+1)))+4*J/N+8/(3*sqrt(2*N))
        self.assertLess(w,rhs)
        self.assertLess(rhs,1)

if __name__=='__main__':unittest.main()
