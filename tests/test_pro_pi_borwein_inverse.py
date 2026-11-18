"""Focused exact controls for the pro-pi swept instrument; no normality claim."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "research/2026-11-17/pro_pi_crucible/borwein_probe.py"
SPEC = importlib.util.spec_from_file_location("pro_pi_borwein_probe", PATH)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


class BorweinInverseTests(unittest.TestCase):
    def test_kernel_mean_by_exact_piecewise_integration(self):
        self.assertEqual(2*P.C*(F(1,2)-P.DELTA)**3/3, P.MEAN)
        self.assertEqual(4*P.C*(F(1,2)-P.DELTA), F(288,289))
        self.assertEqual(P.DELTA/(F(1,2)-P.DELTA), F(1,8))

    def test_delta_atom_sweep_and_interval_discrepancy(self):
        for origin in (F(), F(1,15), F(8,17)):
            mu = P.probability([origin])
            self.assertEqual(P.exact_sweep(mu)[0], F(608,7803))
            self.assertEqual(P.arc_discrepancy(mu), 1)
            self.assertLessEqual(1, F(1156,49)*P.exact_sweep(mu)[0])

    def test_grid_and_unequal_atom_certificates(self):
        cases = [P.probability([F(j,n) for j in range(n)]) for n in (2,3,5,9,16)]
        cases += [P.probability([F(1,7), F(2,5), F(5,6)], [F(1,2),F(1,3),F(1,6)])]
        for mu in cases:
            delta, origin, _ = P.exact_sweep(mu)
            d = P.arc_discrepancy(mu)
            self.assertEqual(abs(P.response(mu, origin)-P.MEAN), delta)
            self.assertLessEqual(d*d, F(1156,49)*delta)
            for j in range(97):
                self.assertLessEqual(abs(P.response(mu,F(j,97))-P.MEAN),delta)

    def test_distributional_inverse_via_exact_interval_integrals(self):
        cases = [P.probability([F(1,7)]),
                 P.probability([F(1,13),F(4,13),F(8,13)]),
                 P.probability([F(2,11),F(7,11)], [F(2,7),F(5,7)])]
        checks = 0
        for mu in cases:
            for a in range(1,12):
                for b in range(a+1,13):
                    left, right = F(a,17), F(b,17)
                    lhs, rhs = P.inverse_interval_sides(mu,left,right)
                    self.assertEqual(lhs,rhs)
                    checks += 1
        self.assertEqual(checks,198)

    def test_wrong_sign_shift_and_coefficient_are_detected(self):
        mu = P.probability([F(1,7),F(3,5)], [F(2,3),F(1,3)])
        left, right = F(1,11), F(5,11)
        lhs, rhs = P.inverse_interval_sides(mu,left,right)
        self.assertEqual(lhs,rhs)
        self.assertNotEqual(lhs,-rhs)
        unshifted = -F(289,288)*(P.response_derivative(mu,right)-P.response_derivative(mu,left))
        self.assertNotEqual(lhs,unshifted)
        mutated = P.interval_discrepancy(mu,left,right)+P.p_interval_discrepancy(mu,left,right)/7
        self.assertNotEqual(mutated,rhs)

    def test_source_states_and_rational_sweep_bounds(self):
        for b in (3,7,15,31):
            u = P.terminal(2*b)
            direct = sum((16**(2*b-j)*P.forcing(j) for j in range(1,2*b+1)),F())
            self.assertEqual(u,direct)
            mu = P.probability([u/16**k for k in range(1,b+1)])
            delta,_,_ = P.exact_sweep(mu)
            self.assertLessEqual(P.arc_discrepancy(mu)**2,F(1156,49)*delta)
            cert = P.source_certificate(b)
            self.assertFalse(cert["asymptotic_claim"])
            self.assertEqual(F(cert["sweep"]),delta)

    def test_stationary_periodic_controls_prevent_temporal_inference(self):
        for x in (F(),F(1,15),F(2,15)):
            self.assertEqual(P.frac(16*x),x)
            before=P.exact_sweep(P.probability([x]))[0]
            after=P.exact_sweep(P.probability([P.frac(16*x)]))[0]
            self.assertEqual(before,after)
            self.assertGreater(after,before/8)

    def test_invalid_probability_and_nonsmooth_derivative_rejected(self):
        with self.assertRaises(ValueError):
            P.probability([0,1],[F(2),F(-1)])
        with self.assertRaises(ValueError):
            P.probability([0],[F(1,2)])
        with self.assertRaises(ValueError):
            P.leak_derivative(F(1,2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
