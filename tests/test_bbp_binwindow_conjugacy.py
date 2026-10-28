"""Adversarial exact finite checks for the BBP infinite coherent-bin theorem.

The analytic all-Z2 zero and isometry are proved in the paper dossier;
finite tests are corroboration only. These tests must run in the native
SUCC tree on the actual imported four-pole source before integration.
"""
import unittest
from fractions import Fraction as Q

from observational_succ import bbp_binwindow_conjugacy as b


def independent_four_pole(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def independent_original(n):
    u=Q()
    for a in range(1,n+1):u=16*u+independent_four_pole(a)
    return u


def v2(num):
    x=abs(num)
    return (x&-x).bit_length()-1


class SourcePassports(unittest.TestCase):
    def test_original_rational_four_pole_and_negative_extension(self):
        for n in range(1,129):
            self.assertEqual(b.canceled_source_extension(n),independent_four_pole(n))
            self.assertEqual(b.source_verified(n),independent_four_pole(n))
            self.assertEqual(b.canceled_source_extension(n).denominator%2,1)
        for n in range(-128,1):
            self.assertEqual(b.canceled_source_extension(n), independent_four_pole(n))
            self.assertEqual(b.canceled_source_extension(n).denominator%2,1)

    def test_end_to_end_real_seed_and_rational_exactness(self):
        for n in (0,1,2,3,7,16,33,57):
            self.assertEqual(b.authentic_state(n),independent_original(n))
        self.assertEqual(b.authentic_state(1),Q(47,15))

    def test_invalid_domains_and_even_denominator_fail_closed(self):
        for input_value in (True,0.2,None):
            with self.assertRaises(ValueError):b.canceled_source_extension(input_value)
        with self.assertRaises(ValueError):b.source_verified(0)
        with self.assertRaises(ValueError):b.two_adic_mod(Q(1,2),2)
        with self.assertRaises(ValueError):b.stationary_window(-1,3)
        with self.assertRaises(ValueError):b.odometer_certificate(4)


class CanonicalZeroBoundary(unittest.TestCase):
    def test_source_boundary_cancels_through_48_hexadic_precisions(self):
        for k in range(1,49):
            receipt=b.zero_boundary_certificate(k)
            self.assertEqual(receipt['modulus_residue'],0)
            prefix=b.past_boundary_partial(k)
            self.assertEqual(b.two_adic_mod(prefix,k),0)
            # Nontrivial exact rational partial sum, not literally zero in Q.
            self.assertNotEqual(prefix,0)

    def test_boundary_has_valuation_at_least_four_times_precision(self):
        for k in range(1,33):
            prefix=b.past_boundary_partial(k)
            self.assertGreaterEqual(v2(prefix.numerator),4*k)
            # Observed stronger pattern v2(S_k)-4k=v2(k) is NOT claimed as a theorem.

    def test_integrand_and_logarithmic_primitive_identity(self):
        # Independent exact evaluations of the two rational integrands and
        # derivative-of-logs decomposition from the paper proof.
        for i in range(0,25):
            t=Q(i,24)
            numerator=-4*t**6+2*t**3+t*t+t
            den=1-16*t**8
            raw=numerator/den
            A=2*t*t-2*t+1
            B=1-2*t*t
            reduced=t*(t-1)/((2*t*t-1)*A)
            logarithmic_derivative=Q(1,8)*((4*t-2)/A -(-4*t)/B)+Q(1,4)/A
            self.assertEqual(raw,reduced)
            self.assertEqual(raw,logarithmic_derivative)
        # Algebraic Gaussian endpoint factors are fourth roots of unity.
        self.assertEqual((0-1j)**4,1)
        self.assertEqual((0+1j)**4,1)

    def test_source_specific_boundary_decoy_fails(self):
        # Counterfeit PR #320: T(0)=1, r*=16T(n-1)-T(n).
        # Its infinite 2-adic backward sum is -T(0)=-1, NOT 0.
        def T(n):return Q(n+1,(2*n+1)*(4*n+1)*(8*n+1))
        for k in (1,2,3,4,6,8,12):
            mod=16**k
            def rstar(n):return 16*T(n-1)-T(n)
            partial=sum((16**s*rstar(-s) for s in range(k)),Q())
            self.assertEqual(b.two_adic_mod(partial,k),mod-1)
        self.assertEqual(T(0),1)


class SlidingCoherentBins(unittest.TestCase):
    def test_labelled_negative_time_ghosts_are_source_specific_zeroes(self):
        for k in range(1,12):
            for n in range(k):
                report=b.negative_time_ghost_completion(n,k)
                self.assertTrue(report['nonzero_rational_witness'])
                self.assertEqual(report['formal_negative_terms'],k-n)
                self.assertEqual(report['ghost_residue_mod_16k'],0)
            report=b.negative_time_ghost_completion(k,k)
            self.assertFalse(report['nonzero_rational_witness'])
            self.assertFalse(report['source_requires_analytic_extension'])

    def test_all_time_exact_source_windows_including_early_times(self):
        for k in range(1,7):
            for n in range(0,36):
                result=b.window_agrees_with_zero_seed(n,k)
                self.assertEqual(result['direct_original'],result['infinite_past_window'])

    def test_sliding_window_anti_diagonal_is_ordered_and_typed(self):
        for n,k in ((0,4),(7,9),(40,4),(101,16)):
            terms=b.causal_diagonal(n,k)
            self.assertEqual(len(terms),k)
            self.assertEqual([a for a,s,w,r in terms],list(range(n,n-k,-1)))
            for a,s,w,r in terms:
                self.assertEqual(a+s,n)
                self.assertEqual(w,16**s)
                self.assertEqual(r,independent_four_pole(a))

    def test_double_counting_each_interior_source_index_occurs_k_times(self):
        low,high,win=20,100,7
        counts=b.bin_reindex_multiplicity(low,high,win)
        for a in range(low,high-win+1):self.assertEqual(counts[a],win)
        self.assertEqual(counts[low-win+1],1)
        self.assertEqual(counts[high-1],1)

    def test_exact_time_source_bin_equivalence(self):
        for k in (1,2,3):
            mod=16**k
            for n,m in ((0,1),(2,18),(12,100),(0,mod),(1,mod+1),(16,mod+17)):
                cert=b.isometry_receipt(n,m,k)
                self.assertEqual(cert['same_source_bin'],cert['same_target_bin'])

    def test_first_hex_word_is_source_specific_involution(self):
        values=tuple(b.first_hex_bin(n) for n in range(16))
        self.assertEqual(len(set(values)),16)
        self.assertEqual(values,tuple((-n+(2 if n%2 else 0))%16 for n in range(16)))
        self.assertEqual(tuple(values[values[n]] for n in range(16)),tuple(range(16)))
        for n in (16,17,29,35,401):self.assertEqual(b.first_hex_bin(n),values[n%16])

    def test_all_time_permutations_and_one_cycle_odometer(self):
        for k in (1,2,3):
            cert=b.odometer_certificate(k)
            self.assertEqual(cert.unique_residues,16**k)
            self.assertEqual(cert.time_zero_value,0)
            self.assertTrue(cert.one_cycle)
            self.assertFalse(cert.real_circle_pi_normality_proved)

    def test_2adic_marginal_uniformity_is_not_joint_independence(self):
        # Both time parity and observed-state parity are Haar, but perfectly coupled.
        obs=[b.stationary_window(n,1)%2 for n in range(16)]
        times=[n%2 for n in range(16)]
        self.assertEqual(obs,times)
        self.assertEqual(sum(obs),8)
        self.assertEqual(sum(times),8)
        self.assertEqual(sum(int(x==y) for x,y in zip(obs,times)),16)

    def test_real_circle_character_mismatch(self):
        real_adic=b.genuine_vs_2adic_Fourier_firewall()
        self.assertEqual(real_adic['original_real_fraction'],Q(2,15))
        self.assertEqual(real_adic['hexadic_turn'],Q(1,16))
        self.assertTrue(real_adic['real_and_2adic_turns_distinct'])
        self.assertFalse(real_adic['all_selected_real_Weyl_cancellation_proved'])


if __name__=='__main__':unittest.main()
