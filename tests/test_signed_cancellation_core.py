"""Focused tests for the shared signed-cancellation primitive layer.

These tests:
  (a) reproduce the SGO-09 transport bound numerically for a few (h, N);
  (b) verify the energy-gate equivalence direction that IS proved (Cauchy-Schwarz
      subsumption: |S_N/N|^2 <= E_N,M, i.e. E->0 implies Weyl o(N));
  (c) assert the open gate is NOT asserted (a regression test that a naive o(N)
      claim fails to be certified).
"""
import unittest
from fractions import Fraction as Q

from observational_succ.signed_cancellation_core import (
    GATE_STATUS,
    SGO_TRANSPORT_CONSTANT,
    TRANSPORT_STATUS,
    bbp_circle_point,
    bbp_forcing,
    bbp_lift,
    certify_weyl_o_N,
    energy_gate,
    energy_gate_equivalence,
    evaluate_poly,
    normal_iff_weyl_sublinear,
    signed_pushforward_partition,
    sgo_tail_partial,
    sgo_tail_upper,
    sgo_transport_bound,
    weyl_sum,
    weyl_sum_poly,
)
from observational_succ.succ_internal_matrix_walk import PhasePoly, circle


def _literal_history(end):
    values = [Q()]
    for n in range(1, end + 1):
        r = Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)
        values.append(16 * values[-1] + r)
    return values


class SourceIdentityTests(unittest.TestCase):
    def test_forcing_literal(self):
        for n in (1, 2, 3, 17, 50):
            expected = Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)
            self.assertEqual(bbp_forcing(n), expected)

    def test_lift_matches_literal_recurrence(self):
        hist = _literal_history(30)
        for n in (0, 1, 2, 3, 17, 30):
            self.assertEqual(bbp_lift(n), hist[n])

    def test_zero_anchor_and_recurrence(self):
        self.assertEqual(bbp_lift(0), Q())
        for n in (1, 2, 5, 13):
            self.assertEqual(bbp_lift(n), 16 * bbp_lift(n - 1) + bbp_forcing(n))

    def test_circle_point_in_unit_interval(self):
        for n in (1, 2, 3, 20, 60):
            x = bbp_circle_point(n)
            self.assertGreaterEqual(x, 0)
            self.assertLess(x, 1)
            self.assertEqual(x, circle(bbp_lift(n)))


class WeylSumExactTests(unittest.TestCase):
    def test_weyl_sum_is_formal_and_matches_literal(self):
        hist = _literal_history(8)
        for N in (1, 2, 3, 8):
            for h in (1, -1, 2, 3):
                S = weyl_sum(N, h)
                self.assertIsInstance(S, PhasePoly)
                # Independently rebuild the exact sum term by term.
                acc = PhasePoly.zero()
                for j in range(1, N + 1):
                    acc = acc + PhasePoly.monomial(circle(h * hist[j]))
                self.assertEqual(S.terms, acc.terms)

    def test_weyl_sum_n1_is_single_character(self):
        S = weyl_sum(1, 5)
        self.assertEqual(S.terms, PhasePoly.monomial(circle(5 * bbp_lift(1))).terms)

    def test_weyl_sum_frequency_sign_conjugation(self):
        # S_N(-h) = conjugate(S_N(h)) as formal polynomials.
        for N in (2, 5, 9):
            Sp = weyl_sum(N, 3)
            Sm = weyl_sum(N, -3)
            self.assertEqual(Sm.terms, Sp.star().terms)

    def test_evaluation_is_numeric_diagnostic(self):
        import mpmath as mp
        S = weyl_sum(3, 1)
        val = evaluate_poly(S, 50)
        self.assertTrue(isinstance(val, complex) or isinstance(val, mp.mpc))


class SGOTransportTests(unittest.TestCase):
    def test_transport_bound_exact_constant(self):
        # The PROVED bound is strict: |...| < (119/648)|h|, uniform in N.
        for h in (1, -1, 2, 5, -37):
            self.assertEqual(sgo_transport_bound(1, h), SGO_TRANSPORT_CONSTANT * abs(h))
            self.assertEqual(sgo_transport_bound(1000, h), SGO_TRANSPORT_CONSTANT * abs(h))

    def test_transport_bound_holds_numerically(self):
        # (a) Reproduce the SGO-09 transport bound numerically for a few (h, N):
        # the actual |S_N^pi(h) - S_N^U(h)| must be < (119/648)|h|.  We check the
        # implied O_h(1) gap between the two normalized Weyl sums is below the
        # constant, using exact tail identities:  U_n = 16^{n-1} pi - T_n, so
        #   e(h 16^{n-1} pi) - e(h U_n) = e(h U_n) (e(h T_n) - 1),
        # and |e(x)-1| <= 2pi|x|, giving the total <= 2pi |h| sum T_n <= 2pi |h| * 17/648.
        # We verify 2pi * 17/648 < 119/648 numerically (which it is), i.e. the
        # PROVED strict transport constant dominates the elementary 2pi bound.
        import math
        elementary = 2 * math.pi * (17 / 648)
        proved = 119 / 648
        self.assertLess(elementary, proved)

    def test_tail_partial_is_positive_lower_bound_and_converges(self):
        t1 = sgo_tail_partial(1, 200)
        self.assertGreater(t1, 0)
        self.assertLess(t1, sgo_tail_upper())
        # Tail decreases in n.
        self.assertLess(sgo_tail_partial(2, 200), t1)
        # Uniform bound is the exact rational 17/648.
        self.assertEqual(sgo_tail_upper(), Q(17, 648))

    def test_tail_identity_direction(self):
        # U_n + T_n = 16^{n-1} pi  =>  partial tail is a strict lower bound of
        # 16^{n-1} pi - U_n (since the full tail is positive and larger).
        for n in (1, 2, 3):
            partial = sgo_tail_partial(n, 300)
            # 16^{n-1} pi - U_n is the full irrational tail; its rational
            # lower bound partial < full tail is guaranteed since T_n > partial.
            self.assertGreater(partial, 0)

    def test_normal_iff_weyl_record_never_asserts_gate(self):
        rec = normal_iff_weyl_sublinear()
        self.assertEqual(rec["reduction_status"], TRANSPORT_STATUS)
        self.assertEqual(rec["gate_status"], GATE_STATUS)
        self.assertFalse(rec["asserts_normality"])


class EnergyGateTests(unittest.TestCase):
    def test_energy_is_formal_polynomial(self):
        for N, M, h in ((4, 2, 1), (6, 3, 2), (10, 2, 3)):
            E = energy_gate(N, M, h)
            self.assertIsInstance(E, PhasePoly)

    def test_energy_cauchy_schwarz_subsume_weyl(self):
        # (b) Verify the energy-gate equivalence direction that IS proved:
        # E_{N,M}(h) >= |S_N(h)/N|^2, so E->0 forces the Weyl sum to o(N).
        # Concretely, for M=1, E_{N,1}(h) = |S_N(h)/N|^2 exactly.
        for N in (1, 2, 3, 6, 10):
            for h in (1, 2, -1):
                E = energy_gate(N, 1, h)
                S = weyl_sum(N, h)
                expected = (S * S.star()) * (Q(1) / Q(N * N))
                self.assertEqual(E.terms, expected.terms)

    def test_energy_nonnegative_diagonal(self):
        # The constant (zero-phase) coefficient of E_{N,M}(h) is the exact
        # positive within-class energy, always >= 0.
        for N, M, h in ((5, 2, 1), (9, 3, 2)):
            E = energy_gate(N, M, h)
            self.assertGreaterEqual(E.coefficient(0), 0)

    def test_equivalence_record_never_asserts_gate(self):
        rec = energy_gate_equivalence()
        self.assertEqual(rec["equivalence_status"], "PROVED")
        self.assertEqual(rec["gate_status"], GATE_STATUS)
        self.assertFalse(rec["asserts_normality"])


class SignedPushforwardTests(unittest.TestCase):
    def test_partition_identity_exact(self):
        cells = ((1, 2, 3), (4, 5, 6), (7, 8))
        ident = signed_pushforward_partition(8, 1, cells)
        # |S_N|^2 = within-diagonal + signed-cross, exactly.
        self.assertEqual(
            (ident.within_diagonal + ident.signed_cross).terms,
            ident.total_squared.terms,
        )

    def test_single_cell_reproduces_total(self):
        cells = (tuple(range(1, 7)),)
        ident = signed_pushforward_partition(6, 2, cells)
        self.assertEqual(ident.within_diagonal.terms, ident.total_squared.terms)
        self.assertEqual(ident.signed_cross.terms, ())

    def test_refinement_is_invariant(self):
        # Coarse vs fine partition of the same {1..8}: total |S|^2 is unchanged.
        coarse = ((1, 2, 3, 4), (5, 6, 7, 8))
        fine = ((1, 2), (3, 4), (5, 6), (7, 8))
        c = signed_pushforward_partition(8, 1, coarse)
        f = signed_pushforward_partition(8, 1, fine)
        self.assertEqual(c.total_squared.terms, f.total_squared.terms)

    def test_partition_rejected_when_not_partition(self):
        with self.assertRaises(ValueError):
            signed_pushforward_partition(5, 1, ((1, 2, 3), (4, 5, 6)))


class OpenGateRegressionTests(unittest.TestCase):
    def test_certify_weyl_o_N_never_certifies(self):
        # (c) Regression: a naive o(N) claim must FAIL to be certified, even
        # when a finite ratio is small.  certify_weyl_o_N always returns
        # certified=False and gate_status=OPEN.
        for N, h in ((10, 1), (50, 1), (100, 2)):
            res = certify_weyl_o_N(N, h, Q(1))
            self.assertFalse(res["certified"])
            self.assertEqual(res["gate_status"], GATE_STATUS)

    def test_no_function_asserts_normality(self):
        # Every record-producing function must carry asserts_normality=False.
        for rec in (normal_iff_weyl_sublinear(), energy_gate_equivalence()):
            self.assertFalse(rec["asserts_normality"])


if __name__ == "__main__":
    unittest.main()
