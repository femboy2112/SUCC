"""Independent finite oracles and hostile controls for primorial phase clocks."""
import unittest
from fractions import Fraction
from math import factorial, gcd, isqrt, prod

from observational_succ.prime_phase_clocks import (
    PhaseClockError, aligned_primes, backward_factorial_primes, euclid_witness,
    factorial_locked, factorial_prime_power_profile, factorial_witness,
    factorization, fixed_window_crt_law, ghost_two_adic_pair, phase_window, prime, prime_clock_profile,
    prime_prefix, primes_up_to, primorial, sqrt_window_perfect,
)
from observational_succ.rad_ris_transport import rad, ris


def independent_is_prime(n):
    return n >= 2 and all(n % d != 0 for d in range(2, isqrt(n) + 1))


def independent_prime_factors(n):
    """Reference by divisibility over every integer, not optimized prime trial."""
    return tuple(q for q in range(2, n + 1)
                 if n % q == 0 and independent_is_prime(q))


class PrimorialClockPhaseTest(unittest.TestCase):
    def test_prime_source_oracles(self):
        reference = tuple(i for i in range(2, 1501) if independent_is_prime(i))
        self.assertEqual(primes_up_to(1500), reference)
        self.assertEqual(prime_prefix(8), (2, 3, 5, 7, 11, 13, 17, 19))
        for i in range(1, 1501):
            self.assertEqual(prime(i), independent_is_prime(i))

    def test_factorization_and_rad_ris_bridge(self):
        for n in range(1, 2000):
            f = factorization(n)
            self.assertEqual(prod(q ** e for q, e in f), n)
            self.assertEqual(tuple(q for q, _ in f), independent_prime_factors(n))
            self.assertEqual(prod(q for q, _ in f), rad(n))
            self.assertEqual(n // prod(q for q, _ in f), ris(n))
        for p in (31, 61, 211, 421, 2311, 120121, 870871):
            x = prime_clock_profile(p)
            self.assertEqual(x.prime, p)
            self.assertEqual(x.radical * x.residual, p - 1)
            self.assertEqual(x.synchronized_primes,
                             tuple(q for q, _ in x.factorization))
            self.assertEqual(x.prefix_depth,
                             next((k for k, q in enumerate(prime_prefix(11))
                                   if (p - 1) % q), 11))
        self.assertEqual(prime_clock_profile(870871).synchronized_count, 7)
        self.assertEqual(prime_clock_profile(870871).prefix_depth, 6)
        self.assertEqual(prime_clock_profile(870871).residual, 1)
        self.assertEqual(prime_clock_profile(120121).radical, 30030)
        self.assertEqual(prime_clock_profile(120121).residual, 4)

    def test_phase_score_fixed_window_and_shift(self):
        four = (2, 3, 5, 7)
        a = phase_window(211, four)
        self.assertEqual(a.residues, (1, 1, 1, 1))
        self.assertEqual(a.residue_sum, 4)
        self.assertEqual(a.forward_slip_sum, 0)
        self.assertEqual(a.synchronized, four)
        self.assertTrue(a.perfectly_locked)
        b = phase_window(31, four)
        self.assertEqual(b.residues, (1, 1, 1, 3))
        self.assertEqual(b.residue_sum, 6)
        self.assertEqual(b.forward_slip_sum, 2)
        self.assertEqual(b.mean_normalized_forward_slip, Fraction(1, 14))
        self.assertEqual(b.mean_normalized_circular_slip, Fraction(1, 14))
        self.assertFalse(b.perfectly_locked)

    def test_wheel_search_against_independent_brute_force(self):
        examples = {1: (3, 5, 7), 2: (7, 13, 19),
                    3: (31, 61, 151), 4: (211, 421, 631),
                    5: (2311, 4621, 9241), 6: (120121, 150151, 180181),
                    7: (4084081, 5105101, 8168161)}
        for k, first_three in examples.items():
            M = primorial(k)
            self.assertEqual(M, prod(prime_prefix(k)))
            found = aligned_primes(k, 30, 3)
            self.assertEqual(tuple(p for _, p in found), first_three)
            self.assertEqual(tuple(t for t, _ in found),
                             tuple((p - 1) // M for p in first_three))
            for t, p in found:
                self.assertTrue(independent_is_prime(p))
                self.assertEqual((p - 1) % M, 0)
                self.assertTrue(all(p % q == 1 for q in prime_prefix(k)))
            # Verify every earlier CRT candidate was independently composite.
            for t in range(1, found[-1][0]):
                q = t * M + 1
                self.assertEqual(independent_is_prime(q),
                                 q in first_three)

    def test_euclid_composite_is_not_a_prime(self):
        self.assertEqual(euclid_witness(3), (31, True, None))
        self.assertEqual(euclid_witness(4), (211, True, None))
        self.assertEqual(euclid_witness(5), (2311, True, None))
        self.assertEqual(euclid_witness(6), (30031, False, 59))
        self.assertEqual(30031, 59 * 509)
        self.assertEqual(30031 % 13, 1)
        self.assertNotEqual(59 % 3, 1)
        self.assertEqual(gcd(30031, primorial(6)), 1)
        with self.assertRaises(PhaseClockError):
            prime_clock_profile(30031)

    def test_factorial_is_deeper_clock_lock(self):
        self.assertEqual(factorial_prime_power_profile(5),
                         ((2, 3), (3, 1), (5, 1)))
        self.assertEqual(factorial_prime_power_profile(6),
                         ((2, 4), (3, 2), (5, 1)))
        for m in range(2, 11):
            f = factorial(m)
            self.assertEqual(f, prod(q ** e for q, e in
                                     factorial_prime_power_profile(m)))
            self.assertEqual(f % prod(primes_up_to(m)), 0)
        self.assertEqual(factorial_witness(3), (7, True, None))
        self.assertEqual(factorial_witness(5), (121, False, 11))
        self.assertEqual(factorial_witness(6), (721, False, 7))
        self.assertEqual(backward_factorial_primes(4, 10, 1), ((3, 73),))
        self.assertTrue(factorial_locked(73, 4))
        self.assertFalse(factorial_locked(31, 4))

    def test_finite_ghost_probes_same_first_digit_different_second(self):
        first_mod4_one, first_mod4_three = ghost_two_adic_pair(3)
        self.assertEqual((first_mod4_one, first_mod4_three), (61, 31))
        for q in (2, 3, 5):
            self.assertEqual(first_mod4_one % q, 1)
            self.assertEqual(first_mod4_three % q, 1)
        self.assertEqual(first_mod4_one % 4, 1)
        self.assertEqual(first_mod4_three % 4, 3)
        for k in range(2, 8):
            self.assertEqual((primorial(k) + 1) % 4, 3)
        for m in range(4, 11):
            self.assertEqual((factorial(m) + 1) % 4, 1)

    def test_sqrt_window_full_class_finite_control(self):
        expected = (2, 3, 5, 7, 13, 19, 31)
        actual = tuple(p for p in primes_up_to(10000) if sqrt_window_perfect(p))
        self.assertEqual(actual, expected)
        self.assertFalse(sqrt_window_perfect(211))
        self.assertTrue(sqrt_window_perfect(31))
        # Finite agreement is NOT the universal proof; that is in the dossier.

    def test_global_lower_prime_perfect_finite_control(self):
        observed = []
        for p in primes_up_to(250):
            if all(p % q == 1 for q in primes_up_to(p - 1)):
                observed.append(p)
        self.assertEqual(observed, [2, 3])

    def test_exact_prime_divisor_sync_for_all_small_primes(self):
        clock_candidates = (2, 3, 5, 7, 11)
        for p in primes_up_to(6000):
            profile = prime_clock_profile(p)
            self.assertEqual(profile.synchronized_count, len(profile.factorization))
            for q in clock_candidates:
                if q < p:
                    self.assertEqual(p % q == 1, q in profile.synchronized_primes)
            if p > 11:
                window = phase_window(p, clock_candidates)
                self.assertEqual(window.perfectly_locked, (p - 1) % 2310 == 0)
                self.assertEqual(window.residue_sum, len(clock_candidates)
                                 + sum((p % q) - 1 for q in clock_candidates))

    def test_full_crt_phase_distribution_against_independent_residue_oracle(self):
        from collections import Counter
        for clocks in ((2,), (2, 3), (2, 3, 5), (2, 3, 5, 7)):
            law = fixed_window_crt_law(clocks)
            modulus = prod(clocks)
            allowed = [a for a in range(1, modulus + 1) if gcd(a, modulus) == 1]
            raw_oracle = Counter(sum(a % q for q in clocks) for a in allowed)
            sync_oracle = Counter(sum(a % q == 1 for q in clocks) for a in allowed)
            denominator = len(allowed)
            self.assertEqual(law.modulus, modulus)
            self.assertEqual(law.reduced_residue_count, denominator)
            self.assertEqual(dict(law.residue_sum_distribution),
                             {s: Fraction(c, denominator) for s, c in raw_oracle.items()})
            self.assertEqual(dict(law.sync_count_distribution),
                             {s: Fraction(c, denominator) for s, c in sync_oracle.items()})
            self.assertEqual(law.all_locked_fraction, Fraction(1, denominator))
            e_raw = sum((Fraction(s * c, denominator)
                         for s, c in raw_oracle.items()), Fraction())
            e_sync = sum((Fraction(s * c, denominator)
                          for s, c in sync_oracle.items()), Fraction())
            self.assertEqual(law.expected_residue_sum, e_raw)
            self.assertEqual(law.expected_sync_count, e_sync)
            self.assertEqual(law.variance_residue_sum,
                             sum((Fraction(c, denominator) * (s-e_raw)**2
                                  for s, c in raw_oracle.items()), Fraction()))
            self.assertEqual(law.variance_sync_count,
                             sum((Fraction(c, denominator) * (s-e_sync)**2
                                  for s, c in sync_oracle.items()), Fraction()))
        law = fixed_window_crt_law((2, 3, 5, 7))
        self.assertEqual(law.reduced_residue_count, 48)
        self.assertEqual(law.expected_sync_count, Fraction(23, 12))
        self.assertEqual(law.expected_residue_sum, Fraction(17, 2))
        self.assertEqual(law.variance_residue_sum, Fraction(53, 12))
        with self.assertRaises(PhaseClockError):
            fixed_window_crt_law((37,))

    def test_hostile_input_and_type_controls(self):
        for bad in (False, 0, -1, 1.5, 250000001):
            with self.assertRaises(PhaseClockError):
                prime(bad)
        for clocks in ((2, 4), (3, 2), (2, 2), (), [2, 3], (2, 1000003)):
            with self.assertRaises(PhaseClockError):
                phase_window(31, clocks)
        with self.assertRaises(PhaseClockError):
            phase_window(31, (2, 31))
        with self.assertRaises(PhaseClockError):
            phase_window(49, (2, 3))
        with self.assertRaises(PhaseClockError):
            prime_prefix(12)
        with self.assertRaises(PhaseClockError):
            aligned_primes(3, True)
        with self.assertRaises(PhaseClockError):
            factorial_witness(13)
        with self.assertRaises(PhaseClockError):
            factorial_locked(9, 4)
        with self.assertRaises(PhaseClockError):
            ghost_two_adic_pair(3, 1)


if __name__ == "__main__":
    unittest.main()
