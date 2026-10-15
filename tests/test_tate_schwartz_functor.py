"""Exact hostile controls: a rational dense Tate S(Qp) functor, not full adeles."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.tate_schwartz_functor import (
    PadicBall, PhaseAmplitude, SourceEvent, SourceWord, TateFunctorError,
    local_mellin_shell, critical_mellin_character, first_missing_prime,
)
from observational_succ.finite_fourier_carrier import dilate_function
from observational_succ.diagonal_adele_zeta import DiagonalSourceError


class SchwartzBallTests(unittest.TestCase):
    def test_canonical_padic_cosets_and_membership(self):
        for p in (2, 3, 5, 7):
            for k in range(-3, 4):
                for a in (F(1, p), F(-7, 2), F(5, 3), F(0), F(13, p**2)):
                    b = PadicBall(p, a, k)
                    self.assertTrue(b.contains(a))
                    self.assertEqual(b, PadicBall(p, b.a, k))
                    self.assertEqual(b.volume, F(p)**(-k))
                    self.assertEqual(b, b.shifted(F(p)**k))
                    self.assertEqual(b, b.shifted(7*F(p)**k))
                    self.assertEqual(b.shifted(F(p)**(k-1)), PadicBall(p, a+F(p)**(k-1), k))

    def test_nonintegral_valuation_scale_is_legal_upstairs(self):
        ball = PadicBall(2, F(1, 2), 0)
        after = ball.scaled(2)
        self.assertEqual(after.k, 1)
        self.assertEqual(after.volume, F(1, 2))
        self.assertEqual(after.scaled(F(1, 2)), ball)
        self.assertEqual(ball.scaled(F(1, 6)).k, -1)
        with self.assertRaises(DiagonalSourceError):
            dilate_function((1, 2, 3, 4), 2)
        # Multiplication by 2 on Q_2 is invertible, whereas it is NOT
        # invertible on finite Z/4Z: different carrier categories.

    def test_exact_local_Fourier_formula_and_annihilator(self):
        b = PadicBall(2, F(1, 2), 0)
        self.assertEqual(b.fourier(0), PhaseAmplitude(1, 0))
        self.assertEqual(b.fourier(1), PhaseAmplitude(1, F(1, 2)))
        self.assertEqual(b.fourier(F(1, 2)), PhaseAmplitude(0))
        for p in (2, 3, 5):
            for k in (-2, -1, 0, 1, 3):
                b = PadicBall(p, F(7, p**2), k)
                self.assertEqual(b.fourier(F(p)**(-k-1)), PhaseAmplitude(0))
                self.assertEqual(b.fourier(F(p)**(-k)).amplitude, b.volume)

    def test_source_affine_fourier_covariance_exact(self):
        rng = random.Random(217904)
        qs = (F(2), F(1, 2), F(3), F(1, 3), F(6), F(-2, 5), F(-7, 9))
        xis = (F(0), F(1), F(1, 2), F(2), F(1, 3), F(1, 9), F(27), F(-7, 5))
        for p in (2, 3, 5):
            for k in range(-3, 4):
                b = PadicBall(p, F(rng.randint(-30, 30), rng.randint(1, 12)), k)
                for q in qs:
                    d = F(rng.randint(-20, 20), rng.randint(1, 12))
                    for xi in xis:
                        r = b.local_affine_fourier(d, q, xi)
                        self.assertTrue(r["fourier_square"])
                        self.assertEqual(r["lhs"], r["rhs"])
                        self.assertFalse(r["complete_Qp_Fourier_proved_by_finite_test"])

    def test_real_phase_sign_mutation_does_not_commute(self):
        b = PadicBall(2, F(1, 2), 0)
        genuine = b.fourier(1)
        self.assertEqual(genuine.phase, F(1, 2))
        # p=3 sees the sign flip, unlike p=2 where +1/2=-1/2 modulo 1.
        b3 = PadicBall(3, F(1, 3), 0)
        genuine = b3.fourier(1)
        inverted = PhaseAmplitude(1, -genuine.phase)
        self.assertNotEqual(genuine, inverted)

    def test_wrong_haar_normalization_detectable(self):
        b = PadicBall(3, F(1, 3), -2)
        after = b.scaled(3)
        self.assertEqual(after.volume, b.volume * F(1, 3))
        self.assertNotEqual(after.fourier(0), b.fourier(0))

    def test_malformed_carriers_and_zero_dilation(self):
        with self.assertRaises(TateFunctorError):
            PadicBall(6, 0, 0)
        with self.assertRaises(TateFunctorError):
            PadicBall(1, 0, 0)
        with self.assertRaises(TateFunctorError):
            PadicBall(True, 0, 0)
        with self.assertRaises(TateFunctorError):
            PadicBall(2, F(0), True)
        with self.assertRaises(TateFunctorError):
            PadicBall(2, F(0), 129)
        with self.assertRaises(TateFunctorError):
            PadicBall(2, F(0), 0, "")
        with self.assertRaises(TateFunctorError):
            PadicBall(2, F(0), 0).scaled(0)


class CausalWordTests(unittest.TestCase):
    def test_affine_order_and_noncommutativity(self):
        origin = PadicBall(3, F(1, 3), 0)
        shift_then_mul = SourceWord(origin, (
            SourceEvent(origin.source_id, 0, 0, "SUCC", F(1, 3)),
            SourceEvent(origin.source_id, 0, 1, "PRIME_JET_FUCC", F(3))))
        mul_then_shift = SourceWord(origin, (
            SourceEvent(origin.source_id, 0, 0, "PRIME_JET_FUCC", F(3)),
            SourceEvent(origin.source_id, 0, 1, "SUCC", F(1, 3))))
        self.assertEqual(shift_then_mul.affine(), (F(3), F(1)))
        self.assertEqual(mul_then_shift.affine(), (F(3), F(1, 3)))
        self.assertNotEqual(shift_then_mul.execute(), mul_then_shift.execute())
        for xi in (F(0), F(1), F(1, 3), F(3)):
            self.assertTrue(shift_then_mul.fourier_receipt(xi)["fourier_naturality"])
            self.assertTrue(mul_then_shift.fourier_receipt(xi)["fourier_naturality"])

    def test_history_does_not_collapse_when_operator_does(self):
        start = PadicBall(2, F(1, 2), 0, "actual-declared-source", 5)
        e = (
            SourceEvent(start.source_id, 5, 0, "SUCC", 1),
            SourceEvent(start.source_id, 5, 1, "SUCC", -1),
            SourceEvent(start.source_id, 5, 2, "PRIME_JET_FUCC", 2),
            SourceEvent(start.source_id, 5, 3, "FUCC", F(1, 2)),
        )
        w = SourceWord(start, e)
        self.assertEqual(w.execute(), start)
        self.assertEqual(w.affine(), (F(1), F(0)))
        self.assertEqual(len(w.fourier_receipt(1)["event_receipts"]), 4)
        self.assertEqual(SourceWord(start, ()).execute(), start)
        self.assertNotEqual(w.events, ())

    def test_random_independent_affine_oracle(self):
        rng = random.Random(9328)
        for p in (2, 3, 5):
            for _ in range(75):
                start = PadicBall(p, F(rng.randint(-12, 12), 15), rng.randint(-3, 3))
                values = []
                events = []
                A, B = F(1), F(0)
                for i in range(5):
                    if rng.randint(0, 1):
                        q = rng.choice((F(-2), F(1, 2), F(3), F(-1, 3), F(5)))
                        events.append(SourceEvent(start.source_id, 0, i, "FUCC", q))
                        A *= q
                        B *= q
                    else:
                        d = F(rng.randint(-9, 9), rng.randint(1, 7))
                        events.append(SourceEvent(start.source_id, 0, i, "SUCC", d))
                        B += d
                w = SourceWord(start, tuple(events))
                self.assertEqual(w.affine(), (A, B))
                self.assertEqual(w.execute(), start.scaled(A).shifted(B))
                for xi in (F(0), F(1), F(1, p), F(p)):
                    self.assertTrue(w.fourier_receipt(xi)["fourier_naturality"])

    def test_invalid_source_history_and_prime_jet(self):
        b = PadicBall(5, 0, 0, "source-a", 7)
        for bad in (
            SourceEvent("source-b", 7, 0, "SUCC", 1),
            SourceEvent("source-a", 6, 0, "SUCC", 1),
            SourceEvent("source-a", 7, 2, "SUCC", 1),
        ):
            with self.assertRaises(TateFunctorError):
                SourceWord(b, (bad,))
        for val in (6, F(1, 5), -3, 1, 0):
            with self.assertRaises(TateFunctorError):
                SourceEvent("source-a", 7, 0, "PRIME_JET_FUCC", val)
        self.assertEqual(SourceEvent("source-a", 7, 0, "FUCC", 6).amount, 6)


class MellinAndWeilFirewallTests(unittest.TestCase):
    def test_local_Euler_factor_full_tail_and_missing_shell(self):
        for p in (2, 3, 5, 7):
            for s in (2, 3, 4, 7):
                for k in (-2, 0, 1, 3):
                    for depth in (0, 1, 2, 5, 10):
                        r = local_mellin_shell(p, s, k, depth)
                        self.assertEqual(r["exact_partial"] + r["exact_tail"], r["exact_full"])
                        self.assertEqual(r["exact_full"], F(p)**(-k*s) / (1-F(p)**(-s)))
                        self.assertFalse(r["gamma_factor_present"])
                        self.assertFalse(r["analytic_continuation_claimed"])

    def test_mutants_not_genuine_Euler_prime_places(self):
        for invalid in (1, 4, 6, 9, 15, True):
            with self.assertRaises(TateFunctorError):
                local_mellin_shell(invalid, 2, 0, 4)
        with self.assertRaises(TateFunctorError):
            local_mellin_shell(2, 1, 0, 5)

    def test_half_density_matched_to_log_Fourier_and_mutants(self):
        self.assertTrue(critical_mellin_character(F(1, 2))["is_critical_fourier"])
        self.assertFalse(critical_mellin_character(F(1, 2), F(1, 4))["is_critical_fourier"])
        self.assertFalse(critical_mellin_character(F(2, 3))["is_critical_fourier"])
        self.assertTrue(critical_mellin_character(F(2, 3), F(-1, 6))["is_critical_fourier"])
        # Two errors can cancel at one point, but then the source halfdensity is WRONG:
        self.assertFalse(critical_mellin_character(F(2, 3), F(-1, 6))["half_density_preserved"])

    def test_finite_source_mutant_not_a_true_prime_law(self):
        for P in (2, 3, 5, 8, 97, 1000):
            r = first_missing_prime(P)
            p = r["first_unobserved_prime"]
            self.assertGreater(p, P)
            self.assertFalse(r["mutant_satisfies_complete_actual_von_Mangoldt_source"])
            self.assertFalse(r["Weil_full_test_factorization_from_finite_samples"])
            self.assertTrue(r["smooth_autocorrelation_can_detect_later_prime"])
        with self.assertRaises(TateFunctorError):
            first_missing_prime(0)


if __name__ == "__main__":
    unittest.main()
