"""Exact finite controls for signed completion and Hankel compression."""

from fractions import Fraction as Q
import unittest

import signed_completion as s


class SignedCompletionTests(unittest.TestCase):
    def test_chronological_product_telescope_noncommuting(self):
        a = (((1, 1), (0, 1)), ((2, 0), (1, 1)), ((1, -1), (1, 2)))
        b = (((1, 0), (0, 1)), ((2, Q(1, 3)), (0, 1)), ((1, 0), (1, 2)))
        cert = s.product_error_certificate(a, b)
        self.assertEqual(cert["difference"], cert["telescoped"])
        self.assertLessEqual(cert["error_norm"], cert["bound"])
        reversed_cert = s.product_error_certificate(tuple(reversed(a)), tuple(reversed(b)))
        self.assertNotEqual(cert["difference"], reversed_cert["difference"])
        self.assertEqual(s.product_error_certificate((), (), 2)["bound"], 0)

    def test_local_error_is_not_uniform_long_time_accuracy(self):
        for n in (1, 3, 8, 17):
            cert = s.product_error_certificate([((Q(11, 10),),)] * n, [((1,),)] * n)
            self.assertEqual(cert["error_norm"], Q(11, 10) ** n - 1)
            self.assertLessEqual(cert["error_norm"], cert["bound"])
        self.assertGreater(cert["error_norm"], 1)

    def test_resolvent_identity_and_budget(self):
        a = ((Q(1, 4), Q(1, 8)), (0, Q(-1, 3)))
        b = ((Q(1, 5), Q(1, 7)), (Q(1, 11), Q(-1, 4)))
        z = Q(2, 3)
        left_r = s.inverse(s.matsub(s.identity(2), s.scale(a, z)))
        right_r = s.inverse(s.matsub(s.identity(2), s.scale(b, z)))
        diff = s.matsub(left_r, right_r)
        self.assertEqual(diff, s.matmul(s.matmul(left_r, s.scale(s.matsub(a, b), z)), right_r))
        m = max(s.inf_norm(a), s.inf_norm(b))
        delta = s.inf_norm(s.matsub(a, b))
        self.assertLess(abs(z) * m, 1)
        self.assertLessEqual(s.inf_norm(diff), abs(z) * delta / (1 - abs(z) * m) ** 2)
        with self.assertRaises(ValueError):
            s.inverse(((0,),))

    def test_stationary_and_rotating_means_differ_despite_full_rank(self):
        self.assertEqual(sum(Q(1) for _ in range(32)) / 32, 1)
        self.assertEqual(sum(Q((-1) ** n) for n in range(32)) / 32, 0)
        rotation = ((0, -1), (1, 0))
        total = s.scale(s.identity(2), 0)
        power = s.identity(2)
        for _ in range(32):
            total = s.matadd(total, power)
            power = s.matmul(rotation, power)
        self.assertEqual(total, ((0, 0), (0, 0)))
        jordan = ((1, 1), (0, 1))
        total = s.scale(s.identity(2), 0)
        power = s.identity(2)
        for _ in range(10):
            total = s.matadd(total, power)
            power = s.matmul(jordan, power)
        self.assertEqual(s.scale(total, Q(1, 10))[0][1], Q(9, 2))

    def test_moving_signed_telescope_exact(self):
        states = ((1, 2), (3, -1), (2, 5), (-4, 3))
        operators = (((1, 1), (0, 1)), ((2, 0), (1, 1)), ((0, -1), (1, 0)))
        covectors = ((1, 0), (2, 1), (-1, 3), (2, -2))
        errors = (Q(1, 3), Q(-2, 5), Q(7, 11))
        cert = s.moving_signed_certificate(states, operators, covectors, errors)
        self.assertEqual(cert["target_sum"], cert["reconstructed_sum"])
        self.assertNotEqual(cert["projected_residual"], 0)
        self.assertNotEqual(cert["target_sum"], cert["boundary"])

    def test_time_dependent_gauge_preserves_all_scalar_terms(self):
        states = ((1, 2), (3, -1), (2, 5), (-4, 3))
        operators = (((1, 1), (0, 1)), ((2, 0), (1, 1)), ((0, -1), (1, 0)))
        covectors = ((1, 0), (2, 1), (-1, 3), (2, -2))
        frames = (((1, 1), (0, 1)), ((2, 0), (0, 1)), ((1, 0), (1, 1)), ((1, 2), (1, 3)))
        inv = tuple(s.inverse(a) for a in frames)
        new_states = tuple(s.matvec(frames[j], states[j]) for j in range(4))
        new_covectors = tuple(s.rowvec(covectors[j], inv[j]) for j in range(4))
        new_operators = tuple(s.matmul(s.matmul(frames[j + 1], operators[j]), inv[j]) for j in range(3))
        raw = s.moving_signed_certificate(states, operators, covectors)
        moved = s.moving_signed_certificate(new_states, new_operators, new_covectors)
        for key in ("target_sum", "boundary", "projected_residual", "output_error", "targets"):
            self.assertEqual(raw[key], moved[key])
        mutant = s.moving_signed_certificate(new_states, operators, new_covectors)
        self.assertNotEqual(raw["target_sum"], mutant["target_sum"])

    def test_signed_projected_residual_can_cancel_without_small_absolute_error(self):
        states = ((0,), (1,), (0,), (1,), (0,))
        operators = [((1,),)] * 4
        covectors = [(1,)] * 5
        cert = s.moving_signed_certificate(states, operators, covectors)
        self.assertEqual(cert["projected_residual"], 0)
        self.assertEqual(sum(abs(r[0]) for r in cert["residuals"]), 4)
        self.assertEqual(cert["target_sum"], 0)

    def test_fixed_orbit_coboundary_obstruction(self):
        cert = s.moving_signed_certificate([(1,)] * 5, [((1,),)] * 4, [(7,)] * 5)
        self.assertEqual(cert["target_sum"], 0)
        # A target identically one cannot be this residual-free coboundary.
        with_error = s.moving_signed_certificate([(1,)] * 5, [((1,),)] * 4, [(7,)] * 5, [1] * 4)
        self.assertEqual(with_error["target_sum"], 4)
        self.assertEqual(with_error["output_error"], 4)

    def test_debruijn_reference_windows_are_exactly_orthogonal(self):
        for order in range(2, 7):
            bits = s.binary_debruijn(order)
            self.assertEqual(len(bits), 2 ** order)
            words = {tuple(bits[(n + j) % len(bits)] for j in range(order)) for n in range(len(bits))}
            self.assertEqual(len(words), 2 ** order)
            signs = tuple(1 - 2 * b for b in bits)
            for width in range(2, order + 1):
                record = signs + signs[:width - 1]
                self.assertEqual(s.normalized_gram(s.hankel(record, width)), s.identity(width))

    def test_compression_distortion_for_refitted_rational_models(self):
        cases = 0
        for order in range(2, 7):
            signs = tuple(1 - 2 * b for b in s.binary_debruijn(order))
            for width in range(2, order + 1):
                record = signs + signs[:width - 1]
                for constant in (Q(-2), Q(-1, 2), Q(0), Q(2, 3), Q(3)):
                    cert = s.compression_certificate(record, [constant] * len(record), width, 1)
                    self.assertEqual(cert["gram_lower_bound"], 1)
                    self.assertGreaterEqual(cert["mean_square_error"], cert["error_lower_bound"])
                    self.assertLessEqual(cert["hankel_squared_error"], cert["multiplicity_upper_bound"])
                    cases += 1
                if width >= 3:
                    pred = tuple(Q(1, 2) + Q(2, 3) * (-1) ** n for n in range(len(record)))
                    cert = s.compression_certificate(record, pred, width, 2)
                    self.assertEqual(cert["prediction_rank"], 2)
                    self.assertGreaterEqual(cert["mean_square_error"], cert["error_lower_bound"])
        self.assertEqual(cases, 75)

    def test_false_rank_contract_rejected_and_coherent_model_survives(self):
        signs = tuple(1 - 2 * b for b in s.binary_debruijn(4))
        record = signs + signs[:3]
        with self.assertRaises(ValueError):
            s.compression_certificate(record, record, 4, 1)
        coherent = [Q(1)] * 20
        cert = s.compression_certificate(coherent, coherent, 4, 1)
        self.assertEqual(cert["mean_square_error"], 0)
        self.assertEqual(cert["gram_lower_bound"], 0)
        self.assertEqual(cert["error_lower_bound"], 0)
        zero_cert = s.compression_certificate(record, [0] * len(record), 4, 0)
        self.assertEqual(zero_cert["mean_square_error"], 1)
        self.assertEqual(zero_cert["prediction_rank"], 0)

    def test_complete_root_grid_reference_is_not_selected_orbit(self):
        self.assertEqual(s.complete_grid_delay_gram(2, 1, 4, 17), s.identity(4))
        self.assertEqual(s.complete_grid_delay_gram(3, 1, 4, 29), s.identity(4))
        self.assertEqual(s.complete_grid_delay_gram(16, 1, 3, 257), s.identity(3))
        self.assertEqual(s.complete_grid_delay_gram(16, 257, 3, 257), ((1, 1, 1),) * 3)
        self.assertEqual(s.radix_turns(16, Q(0), 12), (Q(0),) * 12)
        # One grid gives identity under ALL seeds, while its selected zero seed locks.
        self.assertNotEqual(s.complete_grid_delay_gram(16, 1, 3, 257), ((1, 1, 1),) * 3)

    def test_rational_periodic_phase_is_allowed_finite_linear_control(self):
        for base in (2, 3, 16):
            for period in (1, 2, 3, 5):
                phases = s.radix_turns(base, Q(1, base ** period - 1), 4 * period + 2)
                self.assertTrue(all(phases[n + period] == phases[n] for n in range(len(phases) - period)))
        self.assertEqual(s.recurrence_root_bound(16, (0, 1, 2)), 255)
        self.assertEqual(s.recurrence_root_bound(16, (1, 3)), 4080)
        self.assertEqual(s.recurrence_root_bound(16, (2,)), 0)

    def test_exactness_and_input_mutations(self):
        with self.assertRaises(TypeError):
            s.matrix(((0.1,),))
        self.assertEqual(s.gram_lower_bound(((-1,),)), -1)
        with self.assertRaises(TypeError):
            s.complete_grid_delay_gram(16, 1.5, 3, 257)
        with self.assertRaises(TypeError):
            s.radix_turns(16, Q(1, 17), 3, 1.5)
        with self.assertRaises(ValueError):
            s.recurrence_root_bound(16, (1, 1))
        with self.assertRaises(ValueError):
            s.compression_certificate([1, 2], [1, 2], 3, 1)
        with self.assertRaises(ValueError):
            s.moving_signed_certificate([(1,)], [], [(1,)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
