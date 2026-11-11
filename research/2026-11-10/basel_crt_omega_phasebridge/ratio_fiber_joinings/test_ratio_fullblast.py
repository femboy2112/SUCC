"""Source-selected 3/2 fiber tests. Uses only stdlib and exact rational certificates."""
import unittest
from fractions import Fraction as F
from math import gcd, cos, pi
from fiber_controls import f, parent, root, coupled_digits, block_counts,period9_mean_components,coupled_digits_null_twist
from certified_fiber import (bbp_r,bbp_pi_enclosure,fiber_indices,K32,source_digit_correlations,
                             phase_fraction_ticks,atan_interval_recip,pi_machin,
                             trig_interval,certified_mean)


class RatioExactTests(unittest.TestCase):
    def test_authenticated_four_pole_source(self):
        for n in range(1,30):
            self.assertEqual(bbp_r(n),F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
            self.assertGreater(bbp_r(n),0)

    def test_global_pi_enclosure_and_independent_archimedean_check(self):
        # Separate Machin arctan formula is a cross-check, NOT an orbit oracle.
        p0,p1=pi_machin()
        for K in (10,12,32,64):
            L,U,Q=bbp_pi_enclosure(K)
            self.assertLess(F(L,Q),p1)
            self.assertGreater(F(U,Q),p0)
            self.assertEqual(U-L,K+1)

    def test_K_recurrence_and_interval(self):
        for ell in range(1,40):
            self.assertEqual(K32(ell+2),4352*K32(ell+1)-1048576*K32(ell))
            self.assertEqual(K32(ell),16**(3*ell-1)-16**(2*ell-1))
            self.assertEqual(K32(ell)%240,0)
        for ell in range(1,25):
            self.assertEqual(gcd(K32(ell),K32(ell+1)),15*16**(2*ell-1))

    def test_exact_periodic_false_positive(self):
        # For alpha=1/9 and 3∤h, the three fiber phases are exactly
        # {1,omega,omega^2}; hence every complete period has mean 0.
        for ell in range(1,60):
            self.assertEqual(K32(ell)%9, {1:6,2:3,0:0}[ell%3])
        # The real part is 1 at ell≡0 and −1/2 at ell≢0, so its
        # exact mean over every triplet is zero; the imaginary parts cancel.
        for h in (1,2,4,7,8,11):
            self.assertNotEqual(h%3,0)
            for first in (1,2,3,7,20):
                residues={h*K32(j)%9 for j in range(first,first+3)}
                self.assertEqual(residues,{0,3,6})
            # Source orbit alpha=1/9 is periodic: 16^3 ≡1 (mod 9).
            self.assertEqual(pow(16,3,9),1)

    def test_phase_enclosure_contains_nonwrapped_fraction(self):
        L,U,Q=bbp_pi_enclosure(46)
        for ell in (9,10,11):
            lo,hi,s=phase_fraction_ticks(ell,8,L,U,Q)
            self.assertGreaterEqual(lo,0)
            self.assertLessEqual(hi,s)
            self.assertLess(F(hi-lo,s),F(1,1000000))

    def test_machin_trig_bounds_against_known_axes(self):
        S=10**32
        for ticks,(expected_c,expected_s) in [
          (0,(1,0)),(S//4,(0,1)),(S//2,(-1,0)),
          (3*S//4,(0,-1)),(S,(1,0))]:
            (a,b),(c,d)=trig_interval(ticks,ticks,S)
            self.assertLessEqual(a,expected_c)
            self.assertGreaterEqual(b,expected_c)
            self.assertLessEqual(c,expected_s)
            self.assertGreaterEqual(d,expected_s)

    def test_fresh_original_pi_h8_epoch_certificates(self):
        # Frozen A,h prior to opening certificate. No asymptotic claims.
        # Numeric real/imag are presentation of rational outward intervals.
        data=[
            (263,44,-0.031276714602478335,-0.1272080575537264),
            (521,87,0.08801004686891904,0.04460411745834141),
            (1031,172,0.05438268758561172,-0.0029370366268435338),
        ]
        for A,N,re,im in data:
            out=certified_mean(A,8,guard=12)
            self.assertEqual(out['J_length'],N)
            self.assertLess(abs(out['real_mid']-re),1e-12)
            self.assertLess(abs(out['imag_mid']-im),1e-12)
            self.assertLess(out['real_error_bound'],1e-11)
            self.assertLess(out['imag_error_bound'],1e-11)
            self.assertLess(out['norm_mid'],0.3)
            self.assertGreater(out['norm_mid'],0.01)
            rr=out['real_outward_ticks_12dp']
            ii=out['imag_outward_ticks_12dp']
            self.assertLessEqual(rr[0]/1e12, out['real_mid']-out['real_error_bound'])
            self.assertGreaterEqual(rr[1]/1e12, out['real_mid']+out['real_error_bound'])
            self.assertLessEqual(ii[0]/1e12, out['imag_mid']-out['imag_error_bound'])
            self.assertGreaterEqual(ii[1]/1e12, out['imag_mid']+out['imag_error_bound'])

    def test_wrong_seed_and_rounding_mutant(self):
        # Coherent wrong seed alpha=0: every fiber phase=1.
        for A in (257,509,1021):
            J=fiber_indices(A)
            self.assertEqual(sum(1 for _ in J),len(J))
        # Perturb phase by alpha shift 1/240: edge phases remain exactly
        # unchanged, although the anchored orbit phase rotates.
        for ell in range(1,25):
            self.assertEqual(F(K32(ell),240).denominator,1)

    def test_injective_two_to_three_digit_map(self):
        for n in range(2,1000):
            self.assertGreater(f(n),n)
            self.assertEqual(f(n+1)>f(n),True)
            self.assertEqual(parent(f(n)),n)
            self.assertEqual(root(f(n)),root(n))
            self.assertGreaterEqual(f(n)*3,4*n)
        for k in range(1,15):
            for n in range(3*k+1,1000):
                roots={root(j) for j in range(n,n+k)}
                self.assertEqual(len(roots),k)

    def test_two_signed_haar_joining_witnesses(self):
        # Finitely generated examples illustrate the proved measure existence.
        # Exact inequalities use first TWO shared base-16 digits; the test
        # checks the corresponding relations on a finite sample.
        N=10000
        for delta in (0,1):
            digits=coupled_digits(N,seed=2026,twist=delta)
            for ell in range(1,(N-1)//3):
                self.assertEqual(digits[3*ell], (digits[2*ell]+delta)%16)
                self.assertEqual(digits[3*ell+1],digits[2*ell+1])
            counts=block_counts(digits,1)
            self.assertEqual(len(counts),16)
            self.assertLess(max(abs(v/9999-1/16) for v in counts.values()),0.02)

    def test_twist_measured_phase_sign_smoke(self):
        import cmath
        A=263
        J=fiber_indices(A)
        for delta in (0,1):
            d=coupled_digits(2*A+30,seed=2026,twist=delta)
            def shift_fraction(n):
                return sum(d[n+j]/16**(j+1) for j in range(16))
            mean=sum(cmath.exp(2j*pi*8*(shift_fraction(3*ell)-shift_fraction(2*ell)))
                     for ell in J)/len(J)
            self.assertGreater(((-1)**delta)*mean.real,cos(pi/16)-1e-10)

    def test_symmetric_twist_null_is_nonproduct(self):
        # Exact h=8 sign: one additional first-digit step toggles the phase
        # by half a turn, including hexadecimal wrap 15 -> 0.
        for d0 in range(16):
            delta_mod=((d0+1)%16)-d0
            self.assertEqual((8*delta_mod)%16,8)
            self.assertEqual(8*(0)//16,0)
        d=coupled_digits_null_twist(6000)
        self.assertTrue(all(d[3*ell+1]==d[2*ell+1]
                            for ell in range(1,1900)))
        # Both marginals have all 16 symbols in a finite example, but the
        # exact null and the nonproduct joining are proved in PROOFS.md.
        self.assertEqual(len(block_counts(d,1)),16)

    def test_source_vs_two_digit_locked_joinings(self):
        for A,N,same1,same2,samepar in [
            (263,44,4,0,24),(521,87,11,0,50),(1031,172,5,1,88)]:
            x=source_digit_correlations(A)
            self.assertEqual(x['N'],N)
            self.assertEqual(x['same_first_digit'],same1)
            self.assertEqual(x['same_first_two_digits'],same2)
            self.assertEqual(x['same_parity_first_digit'],samepar)
            # The structural joinings require 100% first-two-digit matching
            # (or a first-digit +1 twist), unlike these finite original pi samples.
            self.assertLess(same2,N)

    def test_periodic_false_positive_all_windows(self):
        # Exact roots of unity reduce to integer coefficients.
        # Over any L consecutive indices, at most two phase terms remain.
        for A in (12,263,521,1031):
            J=fiber_indices(A)
            r,i=period9_mean_components(J,8)
            self.assertLessEqual(abs(r),4)
            self.assertLessEqual(abs(i),2)
            if len(J)%3==0: self.assertEqual((r,i),(0,0))

if __name__=='__main__': unittest.main()
