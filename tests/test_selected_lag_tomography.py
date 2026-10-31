"""Research-only exact four-pole lag Gram, CRT and VdC tests."""
import sys
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'/'2026-10-31'/'selected_lag_tomography'))
from selected_lag import (
    r,original_states,lag_forcing,lag_identity,lag_forcing_bound,
    lag_phasor_error_bound_rational,shifted_lag_frequency,v_p_int,
    conductor_profile,signed_lag_exponents,gaussian_mul,gaussian_conj,
    gaussian_norm2,gaussian_sum,gaussian_vdc,vdc_lag_error_bound_rational,
    dyadic_character_zero,exact_dyadic_lag_histogram,
    coherent_lag_lower_bound,exact_gram_grouping)
from independent_oracle import window_energy,independently_unroll_difference,direct_shifted_character_histogram

class SelectedLagTests(unittest.TestCase):
    def test_01_original_source(self):
        self.assertEqual(r(1),F(47,15));self.assertEqual(r(2),F(106,819))
        for n in range(1,90):
            self.assertEqual(r(n),F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))

    def test_02_seed_label_is_exact_and_locked(self):
        for s in (0,F(7,19),F(-3,56)):
            A=original_states(35,s);B=original_states(35,0)
            for j in range(36):self.assertEqual(A[j]-B[j],16**j*F(s))
        self.assertEqual(original_states(0),(F(0),))

    def test_03_all_original_recurrence_lags(self):
        for s in (0,F(5,91)):
            for n in range(1,26):
                for k in range(1,9):
                    self.assertTrue(lag_identity(n,k,s))

    def test_04_independent_lag_exact_oracle(self):
        for n,k in ((1,1),(1,4),(4,3),(9,5),(21,6)):
            A,B,C=independently_unroll_difference(n,k)
            self.assertEqual(A,B+C)
            self.assertEqual(C,lag_forcing(n,k))

    def test_05_all_lag_forcing_positive_and_monotone(self):
        for k in range(1,9):
            last=lag_forcing(1,k)
            self.assertGreater(last,0)
            for n in range(2,55):
                x=lag_forcing(n,k)
                self.assertGreater(x,0)
                self.assertLess(x,last)
                last=x

    def test_06_global_source_error_bound(self):
        for k in range(1,8):
            val=sum((lag_forcing(n,k) for n in range(1,130)),F(0))
            self.assertLess(val,lag_forcing_bound(k))
            self.assertLess(lag_phasor_error_bound_rational(k,1),F(1,5)*16**k)

    def test_07_source_phase_arguments_exact(self):
        U=original_states(31)
        for k,h in product((1,2,3,6),(-7,-1,1,3)):
            a,b=signed_lag_exponents(U,k,h)
            self.assertEqual(len(a),31-k)
            for n,(aa,bb) in enumerate(zip(a,b),1):
                self.assertEqual((aa-bb)%1,(h*lag_forcing(n,k))%1)

    def test_08_conductor_3_5_LTE_exact_all_k(self):
        for k in range(1,900):
            a=conductor_profile(k)
            self.assertEqual(a['v2'],0)
            self.assertEqual(a['v3'],a['v3_by_lte'])
            self.assertEqual(a['v5'],a['v5_by_lte'])
            self.assertEqual(a['cofactor'],16**k-1)

    def test_09_first_conductors(self):
        self.assertEqual(conductor_profile(1)['cofactor'],15)
        self.assertEqual(conductor_profile(2)['cofactor'],255)
        self.assertEqual(v_p_int(255,17),1)
        self.assertEqual(shifted_lag_frequency(3,-2),-2*4095)

    def test_10_exact_Gaussian_unimodular_VdC(self):
        for N in (2,3,8,20,37):
            for K in range(1,N+1):
                z=[((1,0),(0,1),(-1,0),(0,-1))[j%4] for j in range(N)]
                x=gaussian_vdc(z,K)
                self.assertLessEqual(x['lhs'],x['rhs'])
                self.assertEqual(x['lhs'],K*K*gaussian_norm2(gaussian_sum(z)))

    def test_11_independent_window_energy_identity(self):
        for N in (2,4,9,21):
            for K in range(1,N+1):
                for mode in (0,1,2):
                    z=[((1,0),(0,1),(-1,0),(0,-1))[(j*j+mode*j+1)%4] for j in range(N)]
                    v=gaussian_vdc(z,K)
                    self.assertEqual(v['rhs'],(N+K-1)*window_energy(z,K))

    def test_12_exact_full_Gaussian_Gram_lag_partition(self):
        for N in (1,2,3,5,17,31):
            for offset in range(4):
                z=[((1,0),(0,1),(-1,0),(0,-1))[(j*3+offset)%4] for j in range(N)]
                d=exact_gram_grouping(z)
                self.assertEqual(d['offdiagonal'],d['twice_signed_lag'])

    def test_13_lag_error_moving_scale_and_no_excess(self):
        for N,K,h in ((16,2,1),(100,3,1),(256,2,3),(1000,3,7),(4096,4,-11),(65536,4,3)):
            x=vdc_lag_error_bound_rational(K,N,h)
            self.assertLessEqual(x['weighted_rational_upper'],x['coarse_upper'])
            self.assertGreaterEqual(x['weighted_rational_upper'],0)

    def test_14_source_local_character_balance(self):
        for a in (1,2,3,5):
            for k in (1,2,3,4):
                q=2**a
                for h in (1,3,q//2,q):
                    hist=exact_dyadic_lag_histogram(a,k,h)
                    self.assertEqual(sum(hist),q)
                    expected=dyadic_character_zero(a,k,h)
                    expected_nonzero=len(set((h*(16**k-1)*j)%q for j in range(q)))
                    self.assertEqual(sum(bool(v) for v in hist),expected_nonzero)
                    self.assertEqual(hist,tuple(direct_shifted_character_histogram(a,k,h)))
                    self.assertEqual(expected,h%q!=0)

    def test_15_local_2adic_source_DSI_unit_permutation(self):
        for a in range(1,9):
            h=1; hist=exact_dyadic_lag_histogram(a,1,h)
            self.assertEqual(hist,(1,)*(2**a))

    def test_16_coherent_counterseed_fails_lag_probe(self):
        for N in (16,200,4096):
            for k in (1,2,3):
                z=coherent_lag_lower_bound(N,k,1)
                self.assertEqual(z['coherent_count'],N-k)
                self.assertGreaterEqual(z['normalized_lower'],0)
                if N>1000:self.assertGreater(z['normalized_lower'],F(1,2))

    def test_17_adversarial_fourier_cancels_without_local_Haar(self):
        # Rational states 0 and 1 are complete mod2 but real phases agree.
        u=(F(0),F(1))
        self.assertEqual(sum((-1)**int(x) for x in u),0)
        self.assertEqual(sum(int(x%1==0) for x in u),2)

    def test_18_zero_van_der_corput_sign_and_unmatched_bound(self):
        for N in (4,10,25):
            z=[(1,0)]*N
            for K in range(1,N+1):
                r=gaussian_vdc(z,K)
                self.assertGreaterEqual(r['rhs'],r['lhs'])
            z=[((-1)**j,0) for j in range(N)]
            for K in (1,2,min(5,N)):
                self.assertGreaterEqual(gaussian_vdc(z,K)['rhs'],gaussian_vdc(z,K)['lhs'])

    def test_19_harmonic_and_lag_invalid_inputs(self):
        with self.assertRaises(ValueError):r(0)
        with self.assertRaises(ValueError):lag_forcing(0,1)
        with self.assertRaises(ValueError):shifted_lag_frequency(0,1)
        with self.assertRaises(ValueError):shifted_lag_frequency(1,0)
        with self.assertRaises(ValueError):gaussian_vdc([(1,0)],2)
        with self.assertRaises(ValueError):gaussian_vdc([(1,1)],1)
        with self.assertRaises(ValueError):original_states(0,0.5)

if __name__=='__main__':unittest.main()

class CertifiedSignedLagTests(unittest.TestCase):
    def test_20_cosines_are_rigorously_enclosed(self):
        from selected_lag import cos_interval, _machin_pi_bracket
        lo,hi=_machin_pi_bracket(20)
        self.assertLess(lo,F(22,7));self.assertGreater(hi,F(3))
        for x,expect in ((F(0),F(1)),(F(1,2),F(-1)),
                         (F(1,3),F(-1,2)),(F(2,3),F(-1,2)),
                         (F(1,4),F(0)),(F(3,4),F(0))):
            a,b=cos_interval(x)
            self.assertLessEqual(a,expect)
            self.assertGreaterEqual(b,expect)
            self.assertLess(b-a,F(1,10**10))
        for x in (F(1,7),F(19,81),F(-79,98)):
            self.assertEqual(cos_interval(x),cos_interval(-x))

    def test_21_finite_signed_certificate_shows_nontrivial_selected_saving(self):
        from selected_lag import (selected_signed_lag_interval,
                                 vdc_certificate_from_signed_lag_interval)
        for N,K in ((16,2),(64,3),(128,3)):
            I=selected_signed_lag_interval(N,K)
            self.assertLess(I[1]-I[0],F(1,10**9))
            upper=vdc_certificate_from_signed_lag_interval(N,K,1,I)
            self.assertLess(upper,F(1))

    def test_22_source_coherent_control_separates_selected_finite_scores(self):
        from selected_lag import (selected_signed_lag_interval,signed_lag_mass,
                                 vdc_lag_error_bound_rational)
        for N,K in ((64,3),(128,3)):
            score=selected_signed_lag_interval(N,K)
            lower=signed_lag_mass(K,N)-vdc_lag_error_bound_rational(K,N,1)['weighted_rational_upper']
            self.assertLess(score[1],lower)

    def test_23_critical_logarithmic_lag_source_budget(self):
        from selected_lag import vdc_lag_error_bound_rational
        for power in (2,3,4,6,10):
            N=16**power;K=power
            upper=vdc_lag_error_bound_rational(K,N,1)['coarse_upper']
            self.assertLessEqual(upper,F(11,420*K))
            for h in (2,7):
                self.assertLessEqual(vdc_lag_error_bound_rational(K,N,h)['coarse_upper'],
                                     F(11*abs(h),420*K))

    def test_24_full_real_lag_phase_exact_formal_control(self):
        # PR #432 full-tomography carrier uses n,k frequencies
        # h*(16^(n+k)-16^n) = h*16^n*(16^k-1).
        from selected_lag import shifted_lag_frequency
        for n in range(1,24):
            for k in range(1,14):
                for h in (-3,1,11):
                    self.assertEqual(h*(16**(n+k)-16**n),16**n*shifted_lag_frequency(k,h))

    def test_25_loss_of_local_haar_does_not_prove_real_harmonic(self):
        # exact parity character of rational U values can cancel even if
        # the real circle character has identical phases.
        z=(F(0),F(1))
        self.assertEqual(sum((-1)**int(t) for t in z),0)
        self.assertEqual(sum(int(t%1==0) for t in z),2)

class NonnormalShadowTests(unittest.TestCase):
    def test_26_irrational_near_zero_nonnormal_seed_mimics_all_finite_scores(self):
        from selected_lag import nearzero_nonnormal_shadow_lag_error_bound
        for N,K in ((16,2),(64,3),(128,4),(512,4)):
            prior=None
            for source_depth in (N,N+1,N+4,N+12):
                error=nearzero_nonnormal_shadow_lag_error_bound(source_depth,N,K,1)
                self.assertGreater(error,0)
                if prior is not None:self.assertLess(error,prior)
                prior=error
            self.assertLess(prior,F(1,10**9))

    def test_27_coherent_counterseed_away_from_nearzero_shadow(self):
        from selected_lag import (nearzero_nonnormal_shadow_lag_error_bound,
                                 signed_lag_mass,vdc_lag_error_bound_rational)
        for N,K in ((128,3),(256,3),(512,4)):
            error=nearzero_nonnormal_shadow_lag_error_bound(N+12,N,K,1)
            coherent=signed_lag_mass(K,N)-vdc_lag_error_bound_rational(K,N,1)['weighted_rational_upper']
            self.assertGreater(coherent,F(1,2))
            self.assertLess(error,F(1,10**10))

class NonHaarInvariantControls(unittest.TestCase):
    def test_28_single_mode_zero_not_enough_for_normality(self):
        # µ = (δ0+δ(1/3)+δ(2/3))/3 is exactly T16-invariant,
        # not Haar. Its Fourier coefficient vanishes at h not divisible by3.
        def orbit_mode_sum(h):
            return 3 if h%3==0 else 0
        for n in range(9):
            self.assertEqual((16**n)%3,1)
        for h in range(1,33):
            self.assertEqual(orbit_mode_sum(h),3 if h%3==0 else 0)
        self.assertEqual(orbit_mode_sum(1),0)
        self.assertNotEqual(orbit_mode_sum(3),0)
