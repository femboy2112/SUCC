"""Exact tests for formal Dirichlet cumulants and the multiplicativity theorem.

Everything is exact (sympy Rational / Integer); no floats are certificates.
All statements exercised here are FORMAL. Analytic convergence is tested only
through the separately-labeled ``AnalyticConvergenceClaim`` records and the exact
term-test witness. RH is untouched (no zero, half-density, or phase appears).
"""
import unittest
from fractions import Fraction

import sympy as sp

from observational_succ.dirichlet_cumulants import (
    DirichletCumulantError,
    num_distinct_prime_factors, is_mixed, mixed_indices,
    delta_array, dirichlet_convolve,
    dirichlet_log, dirichlet_exp,
    mixed_prime_cumulant, first_mixed_cumulant_closed_form,
    is_multiplicative_via_cumulants, first_nonzero_mixed_cumulant,
    multiplicative_extension, formal_euler_product_matches,
    local_euler_factor_coeffs,
    constant_one, mobius_source, liouville_source,
    divisor_count_source, euler_phi_source,
    completely_multiplicative, multiplicative_from_prime_powers,
    factorial_completely_multiplicative,
    next_mixed_integer_above, window_evasion_source,
    analytic_convergence_claim, completely_multiplicative_term_test_failure,
    characterization_contract, pointwise_window_contract, uniform_window_contract,
)
# independent second implementation of the same formal log, for cross-checking
from observational_succ.dirichlet_lambert import star_log_unit, star_exp

MULT_SOURCES = {
    "constant_one": constant_one,
    "mobius": mobius_source,
    "liouville": liouville_source,
    "tau": divisor_count_source,
    "phi": euler_phi_source,
}
COMPLETELY_MULT = {"constant_one": constant_one, "liouville": liouville_source}


class TestExactnessFirewall(unittest.TestCase):
    def test_float_rejected_in_source(self):
        with self.assertRaises(DirichletCumulantError):
            dirichlet_log(lambda n: 1.0, 8)

    def test_float_rejected_in_mapping(self):
        with self.assertRaises(DirichletCumulantError):
            dirichlet_log({1: 1, 2: 0.5, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}, 8)

    def test_requires_a1_equals_one(self):
        with self.assertRaises(DirichletCumulantError):
            dirichlet_log(lambda n: 2, 8)

    def test_bound_guard(self):
        with self.assertRaises(DirichletCumulantError):
            dirichlet_log(constant_one, 1)
        with self.assertRaises(DirichletCumulantError):
            dirichlet_log(constant_one, 10 ** 9)


class TestConvolutionBasics(unittest.TestCase):
    def test_delta_is_identity(self):
        d = delta_array(12)
        f = [sp.Integer(0)] + [sp.Integer(n) for n in range(1, 13)]
        self.assertEqual(dirichlet_convolve(f, d), f)

    def test_omega_and_mixed(self):
        self.assertEqual(num_distinct_prime_factors(1), 0)
        self.assertEqual(num_distinct_prime_factors(8), 1)   # 2^3
        self.assertEqual(num_distinct_prime_factors(12), 2)  # 2^2*3
        self.assertFalse(is_mixed(8))
        self.assertTrue(is_mixed(6))
        self.assertEqual(mixed_indices(16), [6, 10, 12, 14, 15])
        self.assertEqual(min(mixed_indices(64)), 6)  # smallest mixed integer is 6


class TestPart1FirstMixedCumulant(unittest.TestCase):
    def test_identity_symbolic(self):
        # b(pq) = a(pq) - a(p)a(q) with free symbolic coefficients
        a2, a3, a6 = sp.symbols("a2 a3 a6")
        src = {1: 1, 2: a2, 3: a3, 4: 0, 5: 0, 6: a6}
        b = dirichlet_log(src, 6)
        self.assertEqual(sp.simplify(b[6] - (a6 - a2 * a3)), 0)

    def test_identity_pq_6_10_15_35(self):
        # distinct-prime semiprimes across several sources
        for name, a in MULT_SOURCES.items():
            for (p, q) in [(2, 3), (2, 5), (3, 5), (5, 7)]:
                val = mixed_prime_cumulant(a, p, q)          # self-checks identity
                closed = first_mixed_cumulant_closed_form(a, p, q)
                self.assertEqual(sp.simplify(val - closed), 0, (name, p, q))
                # multiplicative sources: a(pq) = a(p)a(q) so b(pq) = 0
                self.assertEqual(sp.simplify(val), 0, (name, p, q))

    def test_identity_detects_defect(self):
        # a(6) perturbed: b(6) = 5 - 1 = 4
        a = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 5}
        self.assertEqual(mixed_prime_cumulant(a, 2, 3), 4)

    def test_requires_distinct_primes(self):
        with self.assertRaises(DirichletCumulantError):
            mixed_prime_cumulant(constant_one, 2, 2)
        with self.assertRaises(DirichletCumulantError):
            mixed_prime_cumulant(constant_one, 2, 4)  # 4 not prime


class TestPart2Characterization(unittest.TestCase):
    BOUND = 64

    def test_multiplicative_sources_have_prime_power_support(self):
        for name, a in MULT_SOURCES.items():
            self.assertTrue(is_multiplicative_via_cumulants(a, self.BOUND), name)
            self.assertIsNone(first_nonzero_mixed_cumulant(a, self.BOUND), name)
            b = dirichlet_log(a, self.BOUND)
            for n in mixed_indices(self.BOUND):
                self.assertEqual(sp.simplify(b[n]), 0, (name, n))

    def test_completely_multiplicative_bpk_formula(self):
        # b(p^k) = a(p)^k / k for completely multiplicative a
        for name, a in COMPLETELY_MULT.items():
            b = dirichlet_log(a, self.BOUND)
            for p in (2, 3, 5, 7):
                for k in range(1, 5):
                    if p ** k <= self.BOUND:
                        expect = sp.Rational(1, k) * sp.Integer(a(p)) ** k
                        self.assertEqual(sp.simplify(b[p ** k] - expect), 0, (name, p, k))

    def test_bp_equals_ap_always(self):
        # b(p) = a(p) for any source (single prime, no higher terms)
        a2 = sp.symbols("a2")
        b = dirichlet_log({1: 1, 2: a2, 3: 0, 4: 0, 5: 0}, 5)
        self.assertEqual(sp.simplify(b[2] - a2), 0)

    def test_converse_prime_power_support_implies_multiplicative(self):
        # Build b supported only on prime powers, exponentiate, check multiplicative.
        bound = 48
        def b_supp(n):
            if n == 1:
                return 0
            if num_distinct_prime_factors(n) >= 2:
                return 0
            # arbitrary exact values on prime powers
            return sp.Rational(1, n)
        a = dirichlet_exp(b_supp, bound)
        # a is multiplicative: check a(mn) = a(m)a(n) on coprime pairs
        self.assertTrue(formal_euler_product_matches(a, bound))
        self.assertTrue(is_multiplicative_via_cumulants(a, bound))

    def test_nonmultiplicative_detected(self):
        a = {n: 1 for n in range(1, 17)}
        a[6] = 5
        self.assertFalse(is_multiplicative_via_cumulants(a, 16))
        self.assertEqual(first_nonzero_mixed_cumulant(a, 16), 6)

    def test_contract_is_classical(self):
        c = characterization_contract()
        self.assertEqual(c.status, "CLASSICAL")
        self.assertIn("multiplicative", c.statement)


class TestCrossCheckAndRoundTrip(unittest.TestCase):
    BOUND = 40

    def test_matches_star_log_unit(self):
        # independent implementation in dirichlet_lambert must agree exactly
        for name, a in MULT_SOURCES.items():
            arr = tuple([Fraction(0)] + [Fraction(int(a(n))) for n in range(1, self.BOUND + 1)])
            theirs = list(star_log_unit(arr))
            mine = dirichlet_log(a, self.BOUND)
            for n in range(1, self.BOUND + 1):
                self.assertEqual(sp.Rational(theirs[n].numerator, theirs[n].denominator),
                                 sp.simplify(mine[n]), (name, n))

    def test_round_trip_exp_log(self):
        for name, a in MULT_SOURCES.items():
            b = dirichlet_log(a, self.BOUND)
            back = dirichlet_exp(b, self.BOUND)
            for n in range(1, self.BOUND + 1):
                self.assertEqual(sp.simplify(back[n] - sp.Integer(int(a(n)))), 0, (name, n))

    def test_round_trip_against_star_exp(self):
        a = divisor_count_source
        b = dirichlet_log(a, self.BOUND)
        barr = tuple([Fraction(0)] + [Fraction(int(sp.Rational(b[n]).p), int(sp.Rational(b[n]).q))
                                      for n in range(1, self.BOUND + 1)])
        theirs = list(star_exp(barr))
        for n in range(1, self.BOUND + 1):
            self.assertEqual(sp.Rational(theirs[n].numerator, theirs[n].denominator),
                             sp.Integer(int(a(n))), n)


class TestPart3Controls(unittest.TestCase):
    def test_genuine_multiplicative(self):
        self.assertTrue(is_multiplicative_via_cumulants(divisor_count_source, 60))
        # tau is NOT completely multiplicative: tau(4)=3 != tau(2)^2=4
        self.assertNotEqual(divisor_count_source(4), divisor_count_source(2) ** 2)

    def test_completely_multiplicative(self):
        # a(n) = 2^Omega(n): completely multiplicative with a(p) = 2
        a = completely_multiplicative(lambda p: 2)
        self.assertTrue(is_multiplicative_via_cumulants(a, 60))
        b = dirichlet_log(a, 60)
        for p in (2, 3, 5):
            for k in range(1, 4):
                if p ** k <= 60:
                    self.assertEqual(sp.simplify(b[p ** k] - sp.Rational(2 ** k, k)), 0)

    def test_counterfeit_defect_at_6(self):
        a = {n: 1 for n in range(1, 25)}
        a[6] = 5
        self.assertEqual(first_nonzero_mixed_cumulant(a, 24), 6)
        self.assertEqual(sp.simplify(dirichlet_log(a, 24)[6] - 4), 0)

    def test_correct_semiprimes_defect_at_12(self):
        # all distinct-prime semiprimes correct, first defect at 12 = 2^2 * 3
        a = {n: 1 for n in range(1, 41)}
        a[12] = 100
        for (p, q) in [(2, 3), (2, 5), (3, 5), (2, 7), (5, 7)]:
            if p * q <= 40:
                self.assertEqual(sp.simplify(mixed_prime_cumulant(a, p, q)), 0, (p, q))
        self.assertEqual(first_nonzero_mixed_cumulant(a, 40), 12)
        self.assertEqual(sp.simplify(dirichlet_log(a, 40)[12] - 99), 0)

    def test_correct_semiprimes_defect_at_30(self):
        # all semiprimes correct, first defect at 30 = 2*3*5 (three distinct primes)
        a = {n: 1 for n in range(1, 41)}
        a[30] = 2
        for (p, q) in [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7), (5, 7)]:
            if p * q <= 40:
                self.assertEqual(sp.simplify(mixed_prime_cumulant(a, p, q)), 0, (p, q))
        self.assertEqual(first_nonzero_mixed_cumulant(a, 40), 30)
        self.assertEqual(sp.simplify(dirichlet_log(a, 40)[30] - 1), 0)

    def test_formal_fine_but_analytic_unavailable(self):
        a = factorial_completely_multiplicative
        bound = 32
        # FORMAL object is fine: multiplicative, exact b(p^k) = (p!)^k / k, round trip.
        self.assertTrue(is_multiplicative_via_cumulants(a, bound))
        b = dirichlet_log(a, bound)
        for p in (2, 3, 5):
            for k in range(1, 4):
                if p ** k <= bound:
                    self.assertEqual(
                        sp.simplify(b[p ** k] - sp.Rational(sp.factorial(int(p)) ** k, k)), 0,
                        (p, k),
                    )
        back = dirichlet_exp(b, bound)
        for n in range(1, bound + 1):
            self.assertEqual(sp.simplify(back[n] - a(n)), 0, n)
        # ANALYTIC claim is a SEPARATE, labeled statement: diverges for all s.
        claim = analytic_convergence_claim("factorial_completely_multiplicative")
        self.assertFalse(claim.converges)
        self.assertIsNone(claim.half_plane)
        self.assertEqual(claim.status, "PROVED LOCAL")
        # exact term-test witness at several sigma: p! * p^{-sigma} > 1 for some prime p
        for sigma in (1, 5, 10, 50):
            wp = completely_multiplicative_term_test_failure(lambda p: sp.factorial(p), sigma)
            self.assertIsNotNone(wp, sigma)
            self.assertTrue(sp.factorial(wp) > sp.Integer(wp) ** sigma)


class TestPart4FormalEulerProduct(unittest.TestCase):
    def test_formal_product_matches_iff_multiplicative(self):
        for name, a in MULT_SOURCES.items():
            self.assertTrue(formal_euler_product_matches(a, 60), name)

    def test_formal_product_fails_on_defect(self):
        a = {n: 1 for n in range(1, 25)}
        a[6] = 5
        self.assertFalse(formal_euler_product_matches(a, 24))
        hat = multiplicative_extension(a, 24)
        self.assertEqual(hat[6], 1)   # reconstruction uses a(2)a(3) = 1
        self.assertEqual(hat[12], 1)

    def test_local_euler_factor_coeffs(self):
        # tau: local factor at p is sum_k (k+1) x^k  (a(p^k) = k+1)
        coeffs = local_euler_factor_coeffs(divisor_count_source, 2, 32)
        # 2^0..2^5 all <= 32, a(2^k) = tau(2^k) = k + 1
        self.assertEqual(coeffs, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_analytic_separate_convergent_source(self):
        claim = analytic_convergence_claim("constant_one")
        self.assertTrue(claim.converges)
        self.assertEqual(claim.half_plane, "Re(s) > 1")
        self.assertEqual(claim.status, "CLASSICAL")

    def test_no_term_test_failure_for_bounded_source(self):
        # constant_one: a(p)=1, 1 * p^{-sigma} <= 1 for sigma >= 0, no witness
        wp = completely_multiplicative_term_test_failure(lambda p: 1, 1)
        self.assertIsNone(wp)


class TestPart5FiniteDetection(unittest.TestCase):
    def test_next_mixed_above(self):
        self.assertEqual(next_mixed_integer_above(5), 6)
        self.assertEqual(next_mixed_integer_above(6), 10)
        self.assertEqual(next_mixed_integer_above(10), 12)

    def test_finite_criterion_detects_least_defect(self):
        # inspecting mixed n <= B finds exactly the least mixed cumulant <= B
        a = {n: 1 for n in range(1, 41)}
        a[30] = 2
        self.assertIsNone(first_nonzero_mixed_cumulant(a, 29))   # below defect: window clean
        self.assertEqual(first_nonzero_mixed_cumulant(a, 30), 30)

    def test_window_evasion_no_uniform_window(self):
        for B in (6, 10, 20, 37, 50):
            a, N = window_evasion_source(B)
            self.assertEqual(N, next_mixed_integer_above(B))
            bound = N + 2
            # passes the window test up to B ...
            self.assertTrue(is_multiplicative_via_cumulants(a, B), B)
            self.assertIsNone(first_nonzero_mixed_cumulant(a, B), B)
            # ... yet is non-multiplicative, revealed exactly at N
            self.assertFalse(is_multiplicative_via_cumulants(a, bound), B)
            self.assertEqual(first_nonzero_mixed_cumulant(a, bound), N, B)
            self.assertEqual(sp.simplify(dirichlet_log(a, bound)[N] - 1), 0, B)

    def test_illegal_quantifier_swap_flagged(self):
        pointwise = pointwise_window_contract()
        uniform = uniform_window_contract()
        self.assertEqual(pointwise.status, "PROVED LOCAL")
        self.assertEqual(uniform.status, "REFUTED")
        # B depends on a in the pointwise (sound) contract, not in the uniform one
        self.assertFalse(pointwise.is_uniform_in("B", "a"))
        self.assertTrue(uniform.is_uniform_in("B", "a"))
        # the proof_contracts guard fires on the illegal uniformization
        from observational_succ.proof_contracts import ProofContractError
        with self.assertRaises(ProofContractError):
            uniform.assert_not_uniformized_from(pointwise, "B", "a")


if __name__ == "__main__":
    unittest.main()
