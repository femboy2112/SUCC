"""Independent source replay, geometric holdouts, and hostile future carries."""
from fractions import Fraction as Q
import unittest

from observational_succ.bbp_sparse_carry_transport import (
    authentic_carry_profiles, birth_carry_budget, carry_kernel_budget,
    carry_tail_upper, finite_carry_profile, sparse_carry_mode_upper,
    sparse_carry_width, truncation_depth, truncation_root_error_squared,
)
from observational_succ.gamma_bbp_signed_coherence import green_tail_prefix
from observational_succ.integer_bbp_carrier import source_states
from observational_succ.pi_source_genesis import character_interval


class SparseCarryTests(unittest.TestCase):
    def test_authentic_lift_carries_and_conductors_against_integer_engine(self):
        receipt = authentic_carry_profiles(257, 13)
        independent = source_states(270)
        for point, previous, current in zip(receipt.source, independent, independent[1:]):
            n = point.time
            literal_poles = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            self.assertEqual(point.forcing, literal_poles)
            self.assertEqual(point.lift, Q(current.numerator, current.conductor))
            self.assertEqual(point.conductor, current.conductor)
            self.assertEqual(point.carry, current.integer_part-16*previous.integer_part)
            self.assertEqual(point.conductor_birth, current.conductor != previous.conductor)
        self.assertTrue(any(not row.conductor_birth for row in receipt.source))
        self.assertEqual(receipt.source[0].lift, Q(47, 15))

    def test_finite_green_identity_retains_terminal_fractional_phase(self):
        receipt = authentic_carry_profiles(31, 9)
        for n, profile in enumerate(receipt.full_prefixes, 1):
            x = receipt.source[n-1].lift % 1
            future_x = receipt.source[n+8].lift % 1
            green = green_tail_prefix(n, 9)
            self.assertEqual(profile, x+green-future_x/16**9)
            self.assertNotEqual(profile, x+green)

    def test_censoring_uses_common_conductor_births_only(self):
        receipt = authentic_carry_profiles(48, 11)
        for n, (full, censored) in enumerate(zip(
                receipt.full_prefixes, receipt.birth_censored_prefixes), 1):
            removed = sum((Q(receipt.source[n+j-1].carry, 16**j)
                           for j in range(1, 12)
                           if receipt.source[n+j-1].conductor_birth), Q())
            self.assertEqual(full-censored, removed)
            self.assertGreaterEqual(censored, 0)
            self.assertLessEqual(full, Q(16, 15))
        # Changing the tape is observable, even if it retains the conductor labels.
        original = tuple(point.carry for point in receipt.source)
        mutant = list(original)
        mutant[2] = (mutant[2]+1) % 17
        self.assertNotEqual(finite_carry_profile(original, 1, 11),
                            finite_carry_profile(mutant, 1, 11))

    def test_kernel_mass_and_future_moment_independent_geometric_holdouts(self):
        for h in (1, 2, 4, 5, 73, 74, 1170, 1171, 65537, 10**12+39):
            with self.subTest(h=h):
                cap = carry_kernel_budget(h)
                self.assertGreaterEqual(16**cap.cutoff, 56*h)
                self.assertLess(16**(cap.cutoff-1), 56*h)
                length = cap.cutoff+17
                weights = tuple(min(Q(2), Q(112*h, 16**j))
                                for j in range(1, length+1))
                tail = Q(112*h, 15*16**length)
                moment_tail = Q(112*h, 16**length)*(Q(length, 15)+Q(16, 225))
                self.assertLessEqual(sum(weights, Q())+tail, cap.mass_upper)
                self.assertLessEqual(sum((j*w for j, w in enumerate(weights, 1)), Q())
                                     +moment_tail, cap.first_moment_upper)
                self.assertEqual(cap, carry_kernel_budget(-h))

    def test_future_only_change_refutes_omitting_boundary(self):
        # E intersect [1,N] is empty, but the next carry changes the final phase by 1/2.
        N = 16
        carries = (0,)*N+(8,)
        full = tuple(finite_carry_profile(carries, n, N+1-n) for n in range(1, N+1))
        self.assertEqual(full[-1], Q(1, 2))
        lower_real_error = sum((1-character_interval(x, x).outward(60).real_high
                                for x in full), Q())/N
        self.assertGreater(lower_real_error, Q(1, N))
        cap = sparse_carry_mode_upper(N, 1, 0)
        upper_real_error = sum((1-character_interval(x, x).outward(60).real_low
                                for x in full), Q())/N
        self.assertLess(upper_real_error, cap)

    def test_arbitrary_future_support_paid_by_first_moment(self):
        # Exhaustive finite kernels, with all unknown future carries changed.
        for N in (1, 7, 32):
            for h in (1, 19, 257):
                cap = carry_kernel_budget(h)
                future = sum((min(j, N)*min(Q(2), Q(112*h, 16**j))
                              for j in range(1, 50)), Q())
                self.assertLessEqual(future, cap.first_moment_upper)

    def test_uniform_truncation_and_sharp_all_sixteen_tail(self):
        for depth in (0, 1, 3, 13):
            tape = (16,)*(depth+21)
            full = finite_carry_profile(tape, 1, depth+20)
            short = finite_carry_profile(tape, 1, depth)
            self.assertEqual(full-short, carry_tail_upper(depth)*(1-Q(1, 16**20)))
            self.assertLess(full-short, carry_tail_upper(depth))
        receipt = authentic_carry_profiles(8, 12)
        longer = authentic_carry_profiles(8, 17)
        for short, long in zip(receipt.birth_censored_prefixes,
                               longer.birth_censored_prefixes):
            self.assertLessEqual(short, long)
            self.assertLess(long-short, receipt.uniform_tail_upper)

    def test_predeclared_width_and_future_read_budget(self):
        for t in (0, 1, 2, 16, 127, 1024):
            N = 2**t
            H = sparse_carry_width(N)
            if t >= 2:
                self.assertLessEqual((H-1)**2, t**3)
                self.assertGreater(H**2, t**3)
            depth = truncation_depth(N, H)
            self.assertGreaterEqual(16**depth, N*H**2)
            if depth:
                self.assertLess(16**(depth-1), N*H**2)
            # A deterministic O(1/(N sqrt(H))) root remainder, squared exactly.
            self.assertLessEqual(truncation_root_error_squared(H, depth),
                                 Q(112, 15)**2/Q(6*N*N*H))
        self.assertGreater(sparse_carry_width(2**1024), 1024)

    def test_budget_does_not_claim_purity_and_dense_edits_do_not_vanish(self):
        for N in (1, 32, 257, 2**128):
            receipt = birth_carry_budget(N)
            self.assertFalse(receipt.purity_proved)
            self.assertEqual(receipt.width, sparse_carry_width(N))
            self.assertEqual(receipt.root_energy_error_squared_upper,
                             (receipt.width-1)*receipt.mode_error_upper**2)
            self.assertGreater(sparse_carry_mode_upper(N, 1, N), Q(2))
        self.assertEqual(birth_carry_budget(257, 1).root_energy_error_squared_upper, 0)
        self.assertEqual(carry_kernel_budget(0).mass_upper, 0)
        self.assertEqual(finite_carry_profile((0,)*20, 2, 18), 0)

    def test_invalid_or_unauthenticated_inputs_are_rejected(self):
        for call in (lambda: authentic_carry_profiles(2000, 1),
                     lambda: authentic_carry_profiles(True, 2),
                     lambda: sparse_carry_width(0),
                     lambda: carry_kernel_budget(1.0),
                     lambda: finite_carry_profile((17,), 0, 1),
                     lambda: finite_carry_profile((1,), 1, 1),
                     lambda: finite_carry_profile((1,), 0, 1, (0,)),
                     lambda: sparse_carry_mode_upper(1, 1, 2)):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
