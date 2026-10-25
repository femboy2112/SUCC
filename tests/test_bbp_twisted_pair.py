"""Independent exact hostile tests for the BBP twisted-pair/Galois observer.

Source and arithmetic checks are rational/integer only. These tests do
NOT prove the analytic BGK input or any pi-normality asymptotic.
"""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_twisted_pair import (
    authentic_window_prime, multiplicative_order_16, authentic_forcing,
    authentic_window, channel_phase, differential_phase,
    contragredient_label, delayed_matched_labels,
    opposite_pair_product_phase, chord_pair_moment,
    independent_chord_pair_oracle, galois_frame_spectrum,
    exact_frame_row_trace, p_free_fake_phase_source,
    orientation_connection, untwist_oriented_phases,
    two_pair_cosine_gain,
)


class AuthenticPrimeClockSource(unittest.TestCase):
    def test_real_BBP_source_primary_and_complement(self):
        for p in (17, 41, 73, 97):
            L, states = authentic_window(p)
            m = (p-1)//8
            self.assertEqual(len(states), 3*m)
            self.assertEqual(m % L, 0)
            for t, (y, u, w) in enumerate(states):
                self.assertEqual((u+w) % 1, y)
                self.assertEqual(u, Q(4*pow(16, t, p) % p, p))
                self.assertNotEqual(w.denominator % p, 0)
                if t+1 < len(states):
                    self.assertEqual(
                        states[t+1][2],
                        (16*w + authentic_forcing(m+2+t)) % 1)
        self.assertEqual(authentic_forcing(1), Q(47, 15))

    def test_pair_differential_cancels_authentic_common_mode(self):
        for p in (17, 41, 73, 97):
            _, states = authentic_window(p)
            for t, (_, _, w) in enumerate(states):
                for a,b in ((1, 2), (2, 3), (p-2, p-1)):
                    lhs = (channel_phase(p, 1, a, t, w)
                           - channel_phase(p, 1, b, t, w)) % 1
                    self.assertEqual(lhs, differential_phase(p, 1, a, b, t))
                    self.assertEqual(
                        opposite_pair_product_phase(p, 1, a, t, w),
                        (2*w) % 1)
        with self.assertRaises(ValueError):
            authentic_window_prime(15)
        with self.assertRaises(ValueError):
            differential_phase(17, 1, 1, 1, 0)

    def test_contragredient_carries_the_unknown_initial_label(self):
        for p in (17, 41, 73, 97):
            L, states = authentic_window(p)
            for a0 in (1, 2, 3):
                for t, (_, _, w) in enumerate(states):
                    a = contragredient_label(p, a0, t)
                    self.assertEqual(
                        channel_phase(p, 1, a, t, w),
                        (Q(4*a0, p)+w) % 1)
                    if t+1 < len(states):
                        an = contragredient_label(p, a0, t+1)
                        self.assertEqual(
                            (channel_phase(p, 1, an, t+1, states[t+1][2])
                             - channel_phase(p, 1, a, t, w)) % 1,
                            (states[t+1][2]-w) % 1)
                self.assertEqual(
                    contragredient_label(p, a0, L), a0)

    def test_authentic_curvature_calibrates_unknown_starting_wire(self):
        from observational_succ.bbp_twisted_pair import (
            locked_wire_curvature, recover_initial_wire_from_source)
        for p in (17,41,73,97):
            _, states = authentic_window(p)
            m = (p-1)//8
            for a0 in (1,2,3):
                for t in range(len(states)-1):
                    w, wn = states[t][2], states[t+1][2]
                    r = authentic_forcing(m+2+t)
                    kappa = locked_wire_curvature(p,1,a0,t,w,wn)
                    self.assertEqual(kappa,(r-Q(60*a0,p))%1)
                    self.assertEqual(
                        recover_initial_wire_from_source(p,1,kappa,r),a0)
                    self.assertEqual((kappa-r)%1,Q((-60*a0)%p,p))
                if len(states)>3:
                    w0,w1,w2=(states[i][2] for i in (0,1,2))
                    k0=locked_wire_curvature(p,1,a0,0,w0,w1)
                    k1=locked_wire_curvature(p,1,a0,1,w1,w2)
                    self.assertEqual((k1-k0)%1,
                         (authentic_forcing(m+3)-authentic_forcing(m+2))%1)
        with self.assertRaises(ValueError):
            recover_initial_wire_from_source(17,17,0,0)
        with self.assertRaises(ValueError):
            recover_initial_wire_from_source(17,1,Q(1,101),Q(0))

    def test_time_cross_pair_cancels_local_prime_clock(self):
        for p in (17, 41, 73, 97):
            _, states = authentic_window(p)
            for delay in range(1, min(5, len(states))):
                a, b = delayed_matched_labels(p, 2, delay)
                for t in range(len(states)-delay):
                    w, wd = states[t][2], states[t+delay][2]
                    self.assertEqual(
                        (channel_phase(p, 3, a, t, w)
                         - channel_phase(p, 3, b, t+delay, wd)) % 1,
                        (3*(w-wd)) % 1)

    def test_selected_absolute_channel_still_source_specific(self):
        _, states = authentic_window(17)
        for t, (y, u, w) in enumerate(states):
            self.assertEqual(channel_phase(17, 1, 1, t, w), y)
            self.assertEqual((y-u) % 1, w)


class PairMomentsAndInformationLoss(unittest.TestCase):
    def test_exact_chord_pair_Kummer_moments_and_first_p_alias(self):
        for p in (17, 41, 73, 97):
            for k in (0, 1, 2, 3, p-1, p):
                actual = chord_pair_moment(p, k)
                self.assertEqual(actual, independent_chord_pair_oracle(p, k))
                if 1 <= k < p:
                    self.assertEqual(actual, Q(p, p-1)*comb(2*k, k))
                elif k == p:
                    self.assertEqual(
                        actual, Q(p, p-1)*(comb(2*k, k)-2))
        self.assertEqual(chord_pair_moment(17, 1), Q(17, 8))
        self.assertEqual(
            Q(16,17)*chord_pair_moment(17, 17),
            comb(34, 17)-2)

    def test_galois_channel_gram_has_exact_source_independent_spectrum(self):
        for p in (17, 41, 73, 97, 113):
            L, eigs = galois_frame_spectrum(p)
            self.assertEqual(sum(n for _, n in eigs), p-1)
            self.assertEqual(sum(value*n for value, n in eigs), p-1)
            self.assertEqual(eigs[0], (Q(p, L), L-1))
            self.assertEqual(eigs[1], (Q(p-L, L), 1))
            self.assertEqual(eigs[2], (Q(0), p-1-L))
            for s in range(2*L):
                for t in range(2*L):
                    self.assertEqual(
                        exact_frame_row_trace(p, 1, s, t),
                        p-1 if (s-t) % L == 0 else -1)

    def test_unknown_swaps_need_the_connection_to_retain_signed_phase(self):
        relative = (Q(1,4),)*8
        swaps = (1, -1, 1, -1, -1, 1, -1, 1)
        measured = tuple((swaps[t]*relative[t]) % 1 for t in range(8))
        transport = orientation_connection(swaps)
        self.assertEqual(untwist_oriented_phases(measured, transport), relative)
        # An uncorrected orientation average gives zero for imaginary
        # fourth roots, though the true signal remains constant i.
        self.assertEqual(
            sum(1 if x == Q(1,4) else -1 for x in measured), 0)
        self.assertEqual(
            sum(1 if x == Q(1,4) else -1 for x in relative), 8)
        self.assertEqual(
            untwist_oriented_phases(tuple((-x)%1 for x in measured),
                                    transport),
            tuple((-x)%1 for x in relative))

    def test_p_free_fake_can_lock_selected_channel_without_changing_pair_data(self):
        p, N = 41, 15
        weights, drive, error = p_free_fake_phase_source(
            p, 1, 1, [0]*N, 101)
        self.assertLessEqual(error, Q(1, 202))
        self.assertTrue(all(z.denominator % p for z in weights+drive))
        for t in range(N):
            selected = channel_phase(p, 1, 1, t, weights[t])
            self.assertLessEqual(min(selected, 1-selected), Q(1,202))
            self.assertEqual(
                (channel_phase(p, 1, 1, t, weights[t])
                 -channel_phase(p, 1, 2, t, weights[t])) % 1,
                differential_phase(p, 1, 1, 2, t))
        _, true_states = authentic_window(p)
        self.assertNotEqual(weights[0], true_states[0][2])
        # The counterfeit is p-free but its forcing is NOT authentic BBP.
        self.assertNotEqual(drive[0], authentic_forcing((p-1)//8+2) % 1)

    def test_perfectly_flat_p_free_complement_can_fake_a_finite_selected_orbit(self):
        from observational_succ.bbp_twisted_pair import (
            flat_zero_forcing_counterfeit)
        for p in (17,41,73):
            horizon=3*(p-1)//8
            q,phases,error=flat_zero_forcing_counterfeit(p,1,horizon)
            self.assertEqual(q%p,1)
            self.assertEqual(len(phases),horizon)
            self.assertLess(error,Q(1,32*p))
            self.assertTrue(all(err<=error for w,err in phases))
            for t in range(horizon-1):
                self.assertEqual(phases[t+1][0],16*phases[t][0]%1)
            true=authentic_window(p)[1]
            self.assertNotEqual(phases[0][0],true[0][2])

    def test_general_signed_harmonic_counterfeit_source_contract(self):
        # The countermodel must be valid for genuinely arbitrary characters,
        # not just the h=1 special case. Both signs are source relevant.
        for p in (17, 41):
            for h in (1, 2, -3):
                n = 7
                targets = tuple(Q((j*j+2*j+1) % 17, 17)
                                for j in range(n))
                q = 1009
                weights, drive, err = p_free_fake_phase_source(
                    p, h, 1, targets, q)
                self.assertLessEqual(err, Q(abs(h), 2*q))
                self.assertTrue(all(w.denominator % p for w in weights+drive))
                for t in range(n):
                    val=channel_phase(p,h,1,t,weights[t])
                    difference=(val-targets[t])%1
                    self.assertLessEqual(min(difference,1-difference),
                                         Q(abs(h),2*q))
                    if t+1<n:
                        self.assertEqual((16*weights[t]+drive[t])%1,
                                         weights[t+1])
        with self.assertRaises(ValueError):
            p_free_fake_phase_source(17, 0, 1, [0,0], 101)

    def test_four_channel_unlabelled_balanced_pair_gain(self):
        for denominator in range(1, 100):
            for numerator in range(-denominator, denominator+1):
                self.assertGreaterEqual(
                    two_pair_cosine_gain(Q(numerator, denominator)), Q(1,2))
        self.assertEqual(two_pair_cosine_gain(Q(1,2)), Q(1,2))
        with self.assertRaises(ValueError):
            two_pair_cosine_gain(2)


if __name__ == "__main__":
    unittest.main()
