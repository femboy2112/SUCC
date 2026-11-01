"""Exact independent checks of the 3-by-5 BBP shadow conductor theorem."""
import importlib.util
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


A = load("_fireworks_conductor_arithmetic", ROOT / "research/2026-10-31/signed_lag_fireworks/arithmetic.py")
LAG = load("_fireworks_conductor_cosine", ROOT / "research/2026-10-31/selected_lag_tomography/selected_lag.py")


def trim(poly):
    while len(poly) > 1 and not poly[-1]:
        poly.pop()
    return poly


def divide(poly, divisor):
    """Independent generic integer monic polynomial division oracle."""
    work = list(poly)
    quotient = [0] * max(1, len(work)-len(divisor)+1)
    while len(work) >= len(divisor) and any(work):
        shift = len(work)-len(divisor)
        factor = work[-1]
        quotient[shift] = factor
        for j, coeff in enumerate(divisor):
            work[j+shift] -= factor*coeff
        trim(work)
    return trim(quotient), trim(work)


@lru_cache(None)
def cyclotomic(n):
    """Phi_n recovered from x^n-1 and ALL proper divisor polynomials."""
    polynomial = [-1]+[0]*(n-1)+[1]
    for divisor in range(1, n):
        if n % divisor == 0:
            polynomial, remainder = divide(polynomial, cyclotomic(divisor))
            assert remainder == [0]
    return tuple(polynomial)


def character_residual(q, residues, frequency, claimed_phase):
    poly = [0]*q
    for state in residues:
        poly[frequency*state % q] += 1
    if claimed_phase is not None:
        exponent = claimed_phase*q
        assert exponent.denominator == 1
        poly[int(exponent)] -= len(residues)
    return divide(trim(poly), cyclotomic(q))[1]


class ConductorShadowTests(unittest.TestCase):
    def test_original_four_poles_independent_combined_source(self):
        for n in range(1, 101):
            explicit = F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)
            self.assertEqual(A.original_source(n), explicit)

    def test_exact_orders_and_principal_cosets(self):
        for a, b in ((1, 1), (2, 1), (1, 2), (2, 2), (3, 2), (2, 3)):
            q, period = A.conductor(a, b)
            for c in (1, 2, 7, -11):
                states = A.orbit_residues(a, b, c)
                self.assertEqual(len(set(states)), period)
                self.assertEqual(set(states), set(range(c % 15, q, 15)))
                self.assertEqual(pow(16, period, q), 1)

    def test_generic_cyclotomic_full_period_fourier_oracle(self):
        for a, b in ((2, 1), (1, 2), (2, 2)):
            q, period = A.conductor(a, b)
            for c in (1, 2, 7):
                orbit = A.orbit_residues(a, b, c)
                for h in range(1, 2*period+1):
                    phase = A.period_character_phase(a, b, c, h)
                    self.assertEqual(character_residual(q, orbit, h, phase), [0])

    def test_generic_cyclotomic_lag_oracle_and_deeper_classes(self):
        for a, b in ((2, 2), (3, 2), (2, 3)):
            q, _ = A.conductor(a, b)
            orbit = A.orbit_residues(a, b, 7)
            for h in (1, 3, 5, 7, 11, -3):
                for k in (1, 2, 3, 5, 9, 15, 25, 45):
                    phase = A.lag_character_phase(a, b, 7, h, k)
                    self.assertEqual(character_residual(q, orbit, h*(16**k-1), phase), [0])

    def test_nonzero_lag_support_matches_two_prime_valuation_gate(self):
        def v(n, p):
            count = 0
            while n % p == 0:
                count += 1
                n //= p
            return count
        for a, b in ((2, 2), (3, 3), (5, 4)):
            for h in (1, 3, 5, 7, 9, 11, 15, 25):
                step = 3**max(0, a-2-v(h, 3))*5**max(0, b-2-v(h, 5))
                for k in range(1, 101):
                    self.assertEqual(A.lag_character_phase(a, b, 1, h, k) is not None,
                                     k % step == 0)

    def test_replacing_supported_roots_by_one_is_rejected(self):
        # q=225, P=15, h=1: EVERY lag is supported, but A_k=e(k/15).
        # The complete signed score tends to zero; its magnitude surrogate
        # tends to one. Generic cyclotomic reduction detects the false phase.
        orbit = A.orbit_residues(2, 2, 1)
        for k in range(1, 31):
            self.assertEqual(A.lag_character_phase(2, 2, 1, 1, k), F(k, 15) % 1)
        self.assertNotEqual(character_residual(225, orbit, 15, F(0)), [0])
        self.assertEqual(character_residual(225, orbit, 15, F(1, 15)), [0])

    def test_low_band_passes_and_fixed_higher_mode_fails(self):
        a, b = 4, 3
        _, period = A.conductor(a, b)
        for h in range(1, period):
            self.assertEqual(A.critical_signed_lag_limit(a, b, h), 0)
        for h in (period, -period, 2*period):
            self.assertEqual(A.critical_signed_lag_limit(a, b, h), 1)
            for k in (1, 3, 5, 15, 25):
                self.assertEqual(A.lag_character_phase(a, b, 7, h, k), F(0))

    def test_nearzero_seed_uses_original_rational_prefix(self):
        prior = None
        for depth in range(2, 8):
            receipt = A.near_zero_shadow(depth, depth, depth)
            c, q = receipt["c"], receipt["q"]
            self.assertEqual(c % 15, 1)
            self.assertLessEqual(receipt["completed_seed"], receipt["source_prefix"])
            self.assertLess(receipt["source_prefix"]-receipt["completed_seed"], F(15, q))
            original_state = LAG.original_states(depth)[-1]
            self.assertEqual(receipt["source_prefix"], original_state/16**depth)
            if prior is not None:
                self.assertLess(receipt["seed_absolute_upper"], prior)
            prior = receipt["seed_absolute_upper"]

    def test_tail_intervals_cover_independent_longer_source_sum(self):
        for n in (1, 2, 9, 31):
            lo, hi = A.source_tail_interval(n, 4)
            partial = sum((LAG.r(n+j)/16**j for j in range(1, 20)), F(0))
            self.assertLess(lo, partial)
            self.assertLess(partial, hi)
            self.assertLess(hi, F(1, 64*n*n))

    def test_clipped_tail_transport_against_finite_rational_majorant(self):
        for h in (1, 3, 5, 7, 11):
            for k in range(1, 5):
                frequency = h*(16**k-1)
                # Exact finite majorant using T_n<1/(64*n*n); no trig floats.
                majorant = sum((min(F(2), F(11*frequency, 112*n*n))
                                for n in range(1, 501)), F(0))
                self.assertLess(majorant, A.completed_tail_lag_error(k, h))

    def test_weighted_transport_closed_form(self):
        for K in range(1, 16):
            for h in (1, 5, 11):
                expected = F(2*A.ceiling_sqrt(h)*(4**(K+1)-12*K-4), 3*K*K*16**K)
                self.assertEqual(A.completed_tail_score_error(16**K, K, h), expected)
                self.assertLessEqual(expected, F(8*A.ceiling_sqrt(h), 3*K*K*4**K))

    def test_completed_low_mode_energy_bound_by_outward_rational_cosines(self):
        a, b, c, h, N, K = 2, 1, 1, 1, 40, 13
        q, period = A.conductor(a, b)
        lower = upper = F(0)
        for k in range(1, K):
            for n in range(1, N-k+1):
                phase = F(h*c*pow(16, n, q)*(16**k-1), q)
                lo, hi = LAG.cos_interval(phase)
                weight = F(2*(K-k), K*K*N)
                lower += weight*lo
                upper += weight*hi
        self.assertGreater(lower, -F(1, K))
        self.assertLess(upper, F((N+K-1)*period*period, K*K*N)-F(1, K))

    def test_input_contracts(self):
        for args in ((0, 1), (1, 0), (True, 1)):
            with self.assertRaises(ValueError):
                A.conductor(*args)
        with self.assertRaises(ValueError):
            A.orbit_residues(2, 2, 3)
        with self.assertRaises(ValueError):
            A.period_character_phase(2, 2, 1, 0)
        with self.assertRaises(ValueError):
            A.completed_tail_score_error(3, 4, 1)


if __name__ == "__main__":
    unittest.main()
