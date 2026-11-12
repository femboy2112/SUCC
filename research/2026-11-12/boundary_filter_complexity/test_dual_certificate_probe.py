import unittest
from fractions import Fraction as Q

from dual_certificate_probe import (
    fixed_point_calibration, grid_extension_debt, lower_bound, oscillation,
    smooth_grid_extension_debt, verify_local,
)


class DualCertificateBudgetTests(unittest.TestCase):
    def test_local_calibration_is_exact(self):
        data = fixed_point_calibration(7, 19)
        self.assertEqual(verify_local(*data), 0)
        self.assertEqual((16 * Q(1, 3)) % 1, Q(1, 3))

    def test_target_gain_and_coherent_zero(self):
        _, _, potentials, credits, errors = fixed_point_calibration(7, 19)
        self.assertEqual(lower_bound([Q(1, 3)] * 13, potentials, credits, errors), 18)
        self.assertEqual(lower_bound([Q()] * 13, potentials, credits, errors), 0)

    def test_endpoint_difference_budget_is_sharp(self):
        _, _, potentials, credits, errors = fixed_point_calibration(7, 19)
        target = Q(1, 3)
        endpoint_debt = ((potentials[-1][target] - potentials[-1][0])
                         - (potentials[0][target] - potentials[0][0]))
        bound = lower_bound([target] * 13, potentials, credits, errors)
        self.assertEqual(endpoint_debt, bound)
        self.assertLessEqual(bound, oscillation(potentials[0]) + oscillation(potentials[-1]))

    def test_missing_potential_cannot_support_positive_credit(self):
        tr, costs, potentials, credits, errors = fixed_point_calibration(0, 3)
        for row in potentials:
            for state in row:
                row[state] = Q()
        with self.assertRaises(ValueError):
            verify_local(tr, costs, potentials, credits, errors)

    def test_state_constant_gauge_cannot_create_gain(self):
        tr, costs, potentials, credits, errors = fixed_point_calibration(7, 19)
        before = lower_bound([Q(1, 3)] * 13, potentials, credits, errors)
        gauges = [Q(10 ** 6 * (n + 1) ** 2) for n in range(13)]
        shifted = [{s: value + gauges[n] for s, value in row.items()}
                   for n, row in enumerate(potentials)]
        shifted_credits = [c - gauges[n + 1] + gauges[n] for n, c in enumerate(credits)]
        self.assertEqual(verify_local(tr, costs, shifted, shifted_credits, errors), 0)
        self.assertEqual(lower_bound([Q(1, 3)] * 13, shifted, shifted_credits, errors), before)
        self.assertEqual(oscillation(shifted[-1]), oscillation(potentials[-1]))

    def test_restricted_domain_removes_no_go_hypothesis(self):
        target = Q(1, 3)
        tr = [{target: target}] * 4
        costs = [{target: Q(3, 2)}] * 4
        potentials = [{target: Q()}] * 5
        self.assertEqual(verify_local(tr, costs, potentials, [Q(3, 2)] * 4, [Q()] * 4), 0)
        self.assertEqual(lower_bound([target] * 5, potentials, [Q(3, 2)] * 4, [Q()] * 4), 6)

    def test_error_budget_must_be_paid(self):
        tr = [{0: 0}] * 3
        costs, potentials = [{0: Q()}] * 3, [{0: Q()}] * 4
        credits, errors = [Q(1, 7)] * 3, [Q(1, 7)] * 3
        self.assertEqual(verify_local(tr, costs, potentials, credits, errors), 0)
        self.assertEqual(lower_bound([0] * 4, potentials, credits, errors), 0)
        with self.assertRaises(ValueError):
            verify_local(tr, costs, potentials, credits, [Q()] * 3)

    def test_fourier_mass_bound_on_fixed_point_calibration(self):
        # V_n(x)=-n/2-n cos(2pi*x): nonconstant complex Fourier l1 mass n.
        _, _, potentials, _, _ = fixed_point_calibration(7, 19)
        for n, row in zip(range(7, 20), potentials):
            self.assertLessEqual(oscillation(row), 2 * n)

    def test_false_and_inexact_inputs_rejected(self):
        tr, costs, pots, credits, errors = fixed_point_calibration(0, 1)
        with self.assertRaises(TypeError):
            verify_local(tr, costs, pots, [1.5], errors)
        with self.assertRaises(ValueError):
            verify_local(tr, costs, pots, credits, [Q(-1)])
        costs[0].pop(Q(1, 3))
        with self.assertRaises(ValueError):
            verify_local(tr, costs, pots, credits, errors)

    def test_actual_four_pole_finite_tail_transport(self):
        # Finite terminal tail T_N=0, NOT the actual infinite BBP tail.
        # This checks source-specific transport algebra without decimal pi.
        from observational_succ.duck_bbp import forcing
        horizon = 24
        tail = [Q()] * (horizon + 1)
        for n in range(horizon - 1, -1, -1):
            j = n + 1
            direct = Q(4, 8*j-7) - Q(2, 8*j-4) - Q(1, 8*j-3) - Q(1, 8*j-2)
            self.assertEqual(forcing(j), direct)
            tail[n] = (tail[n + 1] + direct) / 16
        coherent = -tail[0]
        for n in range(horizon + 1):
            self.assertEqual(coherent + tail[n], 0)
            if n < horizon:
                coherent = 16 * coherent + forcing(n + 1)

    def test_dense_grid_debt_is_attained(self):
        # R(x)=-L*d_circle(x,Γ_q), a genuine L-Lipschitz residual.
        # At every grid point it is zero; a cell midpoint pays the full debt.
        for denominator in (1, 2, 3, 17, 19, 31):
            lipschitz = Q(7, 3)
            def residual(x):
                scaled = (denominator * x) % 1
                distance = min(scaled, 1 - scaled) / denominator
                return -lipschitz * distance
            for k in range(denominator):
                self.assertEqual(residual(Q(k, denominator)), 0)
            midpoint = Q(1, 2 * denominator)
            self.assertEqual(residual(midpoint), -grid_extension_debt(lipschitz, denominator))
            for k in range(5 * denominator):
                self.assertGreaterEqual(residual(Q(k, 5 * denominator)),
                                        -grid_extension_debt(lipschitz, denominator))

    def test_authentic_source_grids_are_forward_closed(self):
        from math import lcm
        from observational_succ.duck_bbp import forcing
        previous = 1
        previous_reduced = 1
        for n in range(1, 32):
            denominator = (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            current = lcm(previous, denominator)
            current_reduced = lcm(previous_reduced, forcing(n).denominator)
            self.assertEqual(current % previous, 0)
            self.assertEqual(current % forcing(n).denominator, 0)
            self.assertEqual(current_reduced % previous_reduced, 0)
            self.assertEqual(current % current_reduced, 0)
            self.assertGreaterEqual(current, 2*n-1)
            for input_grid, output_grid in ((previous, current),
                                            (previous_reduced, current_reduced)):
                for index in (0, 1, input_grid // 2, input_grid - 1):
                    state = Q(index, input_grid)
                    output = (16 * state + forcing(n)) % 1
                    self.assertEqual((output_grid * output).denominator, 1)
            previous = current
            previous_reduced = current_reduced

    def test_grid_debt_validation(self):
        for denominator in (0, -1, True, Q(2)):
            with self.assertRaises(ValueError):
                grid_extension_debt(Q(1), denominator)
        with self.assertRaises(ValueError):
            grid_extension_debt(Q(-1), 3)
        with self.assertRaises(TypeError):
            grid_extension_debt(1.0, 3)

    def test_smooth_cell_interpolation_constant_is_locally_sharp(self):
        # The quadratic is a cell-local C² calibration, not a periodic C²
        # function attaining the same global bound on every circle cell.
        for denominator in (1, 2, 3, 17, 31):
            curvature = Q(11, 7)
            width = Q(1, denominator)
            def polynomial(t):
                return curvature * t * (t - width) / 2
            self.assertEqual(polynomial(0), 0)
            self.assertEqual(polynomial(width), 0)
            self.assertEqual(polynomial(width / 2),
                             -smooth_grid_extension_debt(curvature, denominator))

    def test_smooth_interpolation_sign_and_endpoint_data(self):
        for denominator in (2, 7, 19):
            width, curvature = Q(1, denominator), Q(5, 3)
            for left, right in ((Q(), Q()), (Q(1, 9), Q()), (Q(2), Q(3, 7))):
                for quadratic in (curvature / 2, -curvature / 2, Q()):
                    for index in range(17):
                        t = width * Q(index, 16)
                        chord = left * (1 - t / width) + right * t / width
                        value = chord + quadratic * t * (t - width)
                        self.assertGreaterEqual(value, chord - curvature * t * (width - t) / 2)
                        self.assertGreaterEqual(value, -smooth_grid_extension_debt(curvature, denominator))

    def test_smooth_grid_debt_validation(self):
        for denominator in (0, -1, True, Q(2)):
            with self.assertRaises(ValueError):
                smooth_grid_extension_debt(Q(1), denominator)
        with self.assertRaises(ValueError):
            smooth_grid_extension_debt(Q(-1), 3)
        with self.assertRaises(TypeError):
            smooth_grid_extension_debt(1.0, 3)


if __name__ == "__main__":
    unittest.main()
