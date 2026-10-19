"""Exact adversarial oracles for W-tricked synchronized prime-clock progressions."""
import unittest
from fractions import Fraction
from math import gcd, isqrt, prod

from observational_succ.green_tao_clock_ap import (
    ClockAPError, all_clocks_at_one, clock_check, exact_character_label,
    is_prime_exact, local_prime_factors, local_step_requirement,
    prime_clock_progression, prime_predecessor_factorization, search_first_grid,
    verify_prime_clock_grid, wheel_arithmetic,
)


def independent_prime(n: int) -> bool:
    """Slow different reference scanning ALL divisors, not odd-only trial division."""
    return n >= 2 and all(n % d != 0 for d in range(2, isqrt(n) + 1))


def independent_roots(w: int, length: int, step: int, q: int) -> set[int]:
    return {t for t in range(q)
            if any((1 + w * (t + j * step)) % q == 0 for j in range(length))}


class GreenTaoClockAPTest(unittest.TestCase):
    def test_source_primality_independent_control(self):
        for p in range(1, 3000):
            self.assertEqual(is_prime_exact(p), independent_prime(p))
        for p in (870871, 903211, 930931, 228254071, 269414641,
                  310575211, 351735781, 392896351):
            self.assertTrue(independent_prime(p), p)
        for n in (30031, 121, 721, 21506, 2612611):
            self.assertFalse(is_prime_exact(n), n)

    def test_870871_exact_factor_size_and_first_return(self):
        q = (2, 3, 5, 7, 11, 13, 29)
        w = wheel_arithmetic(q)
        self.assertEqual(w.modulus, 870870)
        self.assertEqual(w.totient, 161280)
        self.assertEqual(w.first_return, 870871)
        self.assertEqual(w.wheel_enrichment, Fraction(870870, 161280))
        self.assertEqual(w.relative_prime_density, Fraction(1, 161280))
        self.assertEqual(w.faithful_character_multiplier, 329629)
        self.assertEqual(w.minimum_distinguishing_bits, 20)
        self.assertEqual(prime_predecessor_factorization(870871),
                         tuple((p, 1) for p in q))
        self.assertTrue(is_prime_exact(w.first_return))
        self.assertTrue(all_clocks_at_one(870871, q))
        self.assertFalse(all_clocks_at_one(870872, q))

    def test_exact_character_is_faithful_not_just_phasor_heuristic(self):
        for q in ((2,), (2, 3), (2, 3, 5), (3, 5, 7), (5, 11, 17, 23, 29)):
            w = wheel_arithmetic(q)
            self.assertEqual(gcd(w.faithful_character_multiplier, w.modulus), 1)
            self.assertEqual(
                {exact_character_label(n, q)[0] for n in range(1, w.modulus + 1)},
                set(range(w.modulus)))
            for n in range(1, min(1000, w.modulus * 2) + 1):
                label, mod = exact_character_label(n, q)
                self.assertEqual(mod, w.modulus)
                self.assertEqual(label == 0, n % w.modulus == 1 % w.modulus)
                self.assertEqual(label == 0, all(n % r == 1 for r in q))

    def test_exact_3_by_3_clock_grid(self):
        q = prime_clock_progression(3, 2, 3)
        grid = verify_prime_clock_grid(q, start=2, step=2, count=3)
        self.assertEqual(q, (3, 5, 7))
        self.assertEqual(grid.wheel_modulus, 105)
        self.assertEqual(grid.endpoint_primes, (211, 421, 631))
        self.assertEqual(grid.endpoint_step, 210)
        self.assertEqual(grid.incidence_count, 9)
        self.assertEqual(grid.local_minimum_step, 2)
        self.assertEqual(search_first_grid(q, 3, 6), grid)

    def test_exact_4_by_4_clock_grid(self):
        q = prime_clock_progression(5, 6, 4)
        grid = verify_prime_clock_grid(q, start=46, step=6, count=4)
        self.assertEqual(q, (5, 11, 17, 23))
        self.assertEqual(grid.wheel_modulus, 21505)
        self.assertEqual(grid.endpoint_primes,
                         (989231, 1118261, 1247291, 1376321))
        self.assertEqual(grid.endpoint_step, 129030)
        self.assertEqual(grid.incidence_count, 16)
        self.assertEqual(grid.local_minimum_step, 6)
        self.assertEqual(search_first_grid(q, 4, 64), grid)

    def test_exact_5_by_5_clock_grid_and_variable_RIS(self):
        q = prime_clock_progression(5, 6, 5)
        grid = verify_prime_clock_grid(q, start=366, step=66, count=5)
        self.assertEqual(q, (5, 11, 17, 23, 29))
        self.assertEqual(grid.wheel_modulus, 623645)
        self.assertEqual(grid.endpoint_primes, (228254071, 269414641,
                         310575211, 351735781, 392896351))
        self.assertEqual(grid.endpoint_step, 41160570)
        self.assertEqual(grid.incidence_count, 25)
        self.assertEqual(grid.local_minimum_step, 6)
        self.assertEqual(search_first_grid(q, 5, 630), grid)
        for j, p in enumerate(grid.endpoint_primes):
            t = 366 + 66 * j
            self.assertEqual((p - 1) // grid.wheel_modulus, t)
            self.assertTrue(independent_prime(p))
            self.assertTrue(all(p % r == 1 for r in q))
            factors = prime_predecessor_factorization(p)
            self.assertEqual(prod(r**e for r, e in factors), p - 1)
            self.assertTrue(set(q).issubset({r for r, _ in factors}))
        self.assertEqual(prime_predecessor_factorization(grid.endpoint_primes[0]),
                         ((2, 1), (3, 1), (5, 1), (11, 1), (17, 1),
                          (23, 1), (29, 1), (61, 1)))
        self.assertEqual(prime_predecessor_factorization(grid.endpoint_primes[1]),
                         ((2, 4), (3, 3), (5, 1), (11, 1), (17, 1),
                          (23, 1), (29, 1)))

    def test_exact_local_prime_factors_against_independent_residue_scan(self):
        cases = (((3, 5, 7), 3, 1),
                 ((3, 5, 7), 3, 2),
                 ((5, 11, 17, 23), 4, 1),
                 ((5, 11, 17, 23), 4, 2),
                 ((5, 11, 17, 23), 4, 6),
                 ((5, 11, 17, 23, 29), 5, 66),
                 ((2, 3, 5, 7, 11, 13, 29), 5, 1))
        for clocks, length, step in cases:
            W = prod(clocks)
            rows = local_prime_factors(clocks, length, step, 31)
            for cell in rows:
                rejected = independent_roots(W, length, step, cell.prime)
                self.assertEqual(cell.forbidden_start_classes, len(rejected))
                self.assertEqual(cell.admissible_start_classes,
                                 cell.prime - len(rejected))
                self.assertEqual(cell.singular_series_factor,
                                 Fraction(cell.prime-len(rejected), cell.prime)
                                 * Fraction(cell.prime, cell.prime-1)**length)
        self.assertEqual(local_step_requirement((5, 11, 17, 23), 4), 6)
        self.assertEqual(local_step_requirement((5, 11, 17, 23, 29), 5), 6)
        self.assertEqual(local_step_requirement((3, 5, 7), 3), 2)
        self.assertEqual(local_step_requirement((2, 3, 5, 7, 11, 13, 29), 5), 1)
        self.assertEqual(local_prime_factors((5, 11, 17, 23), 4, 1, 7)[0]
                         .singular_series_factor, 0)
        self.assertTrue(all(cell.singular_series_factor > 0 for cell in
                            local_prime_factors((5, 11, 17, 23), 4, 6, 31)))

    def test_finite_optimum_is_not_a_global_least_prime_theorem(self):
        # Source-fixed last-multiplier cap = 630. Independently enumerate
        # ALL candidate pairs with end <=630, a DIFFERENT loop orientation.
        q = (5, 11, 17, 23, 29)
        W = prod(q)
        search = search_first_grid(q, 5, 630)
        self.assertIsNotNone(search)
        for step in range(1, 631):
            for start in range(1, 631 - 4*step):
                last = start + 4*step
                if last >= 630:  # witness greatest endpoint occurs at 630
                    continue
                p = 1 + W * start
                if independent_prime(p):
                    self.assertFalse(all(independent_prime(1+W*(start+j*step))
                                         for j in range(1, 5)))
        self.assertEqual(search.endpoint_primes[-1], 392896351)

    def test_hostile_composite_and_step_sources(self):
        for bad in ((5, 11, 17, 24), (7, 5, 11), (5, 5),
                    (2, 4), (), [3, 5, 7], (3, True, 7)):
            with self.assertRaises(ClockAPError):
                clock_check(bad)
        with self.assertRaises(ClockAPError):
            prime_clock_progression(5, 6, 6)  # 35 composite
        with self.assertRaises(ClockAPError):
            verify_prime_clock_grid((5, 11, 17, 23), 2, 1, 4)
        with self.assertRaises(ClockAPError):
            verify_prime_clock_grid((5, 11, 17, 23), 1, 6, 4)
        with self.assertRaises(ClockAPError):
            verify_prime_clock_grid((2, 3, 5), 2, 2, 3)  # clocks not AP
        with self.assertRaises(ClockAPError):
            verify_prime_clock_grid((5, 11, 17, 23, 29), 366, 66, True)
        with self.assertRaises(ClockAPError):
            local_prime_factors((5, 11, 17, 23), 4, True)
        for bad in (True, 0, -1, 1.5, 10**12+1):
            with self.assertRaises(ClockAPError):
                is_prime_exact(bad)
        self.assertIsNone(search_first_grid((5, 11, 17, 23, 29), 5, 100))


if __name__ == "__main__":
    unittest.main()
