"""Independent finite exact controls for source-centered SUCC classical theorems."""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import unittest

from observational_succ.classical_unit_origin import (
    ArithmeticRay, ClassicalOriginError, LogBox,
    certify_finite_cocycle, chart_multiplier, chart_successor,
    dense_kernel_approximation,
    classical_unit_origin_probe, decode_source, forced_affine_cocycle,
    formal_product, horizon_report, intersect_rays, log_dilate, log_inner,
    log_reflect, residue_fiber_sizes, residue_map_norm_squared,
    source_coordinate, unbounded_residue_witness,
)


class UnitOriginAlgebraTests(unittest.TestCase):
    def test_formal_group_axioms_and_reflection(self):
        for x, y, z in product(range(-3, 4), repeat=3):
            for chart in ("n_minus_one", "one_minus_n"):
                f = lambda a, b: formal_product(a, b, chart)
                self.assertEqual(f(x, 0), x)
                self.assertEqual(f(x, y), f(y, x))
                self.assertEqual(f(f(x, y), z), f(x, f(y, z)))
            self.assertEqual(formal_product(-x, -y, "one_minus_n"),
                             -formal_product(x, y, "n_minus_one"))

    def test_source_laws_and_affine_succ_fucc_semidirect_relation(self):
        for chart, sign in (("n_minus_one", 1), ("one_minus_n", -1)):
            for n, m, k in product(range(1, 10), range(1, 8), range(5)):
                x = source_coordinate(n, chart)
                self.assertEqual(decode_source(x, chart), n)
                self.assertEqual(chart_multiplier(x, m, chart),
                                 source_coordinate(m * n, chart))
                self.assertEqual(chart_successor(x, k, chart),
                                 source_coordinate(n + k, chart))
                self.assertEqual(chart_multiplier(chart_successor(x, k, chart), m, chart),
                                 chart_successor(chart_multiplier(x, m, chart), m * k, chart))
                self.assertEqual(chart_multiplier(x, m, chart), m * x + sign * (m - 1))

    def test_source_zero_is_multiplicative_unit_not_absorber(self):
        for m in (2, 3, 4, 6, 11):  # composite inputs do NOT certify Euler primality
            self.assertEqual(chart_multiplier(0, m, "n_minus_one"), m - 1)
            self.assertEqual(chart_multiplier(0, m, "one_minus_n"), 1 - m)
            self.assertNotEqual(chart_multiplier(0, m, "n_minus_one"), m * 0)
        with self.assertRaises(ClassicalOriginError):
            decode_source(-1, "n_minus_one")
        with self.assertRaises(ClassicalOriginError):
            decode_source(1, "one_minus_n")

    def test_affine_cocycle_two_rigidity_and_mutation(self):
        for c2 in (-4, -1, 0, 1, 5):
            table = {m: forced_affine_cocycle(m, c2) for m in range(1, 19)}
            self.assertTrue(certify_finite_cocycle(table))
            for a, b in product(range(1, 19), repeat=2):
                self.assertEqual(forced_affine_cocycle(a * b, c2),
                                 a * forced_affine_cocycle(b, c2) +
                                 forced_affine_cocycle(a, c2))
            table[6] += 1
            self.assertFalse(certify_finite_cocycle(table))
        self.assertFalse(certify_finite_cocycle({1: 0, 2: 1, 3: 4, 6: 5}))

    def test_invalid_types_and_missing_source(self):
        with self.assertRaises(ClassicalOriginError):
            source_coordinate(True, "n_minus_one")
        with self.assertRaises(ClassicalOriginError):
            source_coordinate(0, "n_minus_one")
        with self.assertRaises(ClassicalOriginError):
            formal_product(1, 2, "unknown")
        with self.assertRaises(ClassicalOriginError):
            chart_multiplier(0, 0, "n_minus_one")
        with self.assertRaises(ClassicalOriginError):
            chart_successor(0, -1, "n_minus_one")
        with self.assertRaises(ClassicalOriginError):
            certify_finite_cocycle({1: 0, 3: 2})


class CRTAndHilbertBoundaryTests(unittest.TestCase):
    def test_pairwise_compatible_not_yet_globally_visible(self):
        rays = (ArithmeticRay(1, 2), ArithmeticRay(2, 3), ArithmeticRay(3, 5))
        self.assertEqual([intersect_rays((rays[i], rays[j])).start
                          for i, j in ((0, 1), (0, 2), (1, 2))], [5, 3, 8])
        self.assertEqual(horizon_report(rays, 9)["state"], "BEYOND_HORIZON")
        self.assertEqual(horizon_report(rays, 22)["visible_witness"], None)
        self.assertEqual(horizon_report(rays, 23)["visible_witness"], 23)
        self.assertEqual(intersect_rays(rays), ArithmeticRay(23, 30))
        self.assertEqual(horizon_report((ArithmeticRay(0, 2), ArithmeticRay(1, 2)), 99)["state"],
                         "INCONSISTENT")

    def test_crt_matches_independent_exhaustive_finite_oracle(self):
        family = [ArithmeticRay(a, m) for m in (1, 2, 3, 4, 5, 6)
                  for a in range(0, 7)]
        for a, b in product(family, repeat=2):
            ray = intersect_rays((a, b))
            bound = max(a.start, b.start) + lcm(a.step, b.step)
            matches = [n for n in range(bound + 1) if a.contains(n) and b.contains(n)]
            self.assertEqual(ray is None, not matches)
            if ray:
                self.assertEqual(ray.start, matches[0])
                self.assertEqual(ray.step, lcm(a.step, b.step))
                for n in range(bound + 1):
                    self.assertEqual(ray.contains(n), a.contains(n) and b.contains(n))

    def test_finite_residue_map_operator_norm_is_max_fiber_size(self):
        for n, h in product(range(1, 10), range(1, 35)):
            counts = tuple(sum(i % n == j for i in range(h)) for j in range(n))
            self.assertEqual(residue_fiber_sizes(n, h), counts)
            self.assertEqual(residue_map_norm_squared(n, h), max(counts))
            self.assertEqual(sum(counts), h)
        for k in (1, 2, 3, 10, 100):
            witness = unbounded_residue_witness(7, k)
            self.assertEqual(witness["ratio_squared"], k)
            self.assertEqual(witness["finite_operator_norm_squared"], k)
            self.assertEqual(witness["output_norm_squared"], k**2)

    def test_exact_dense_kernel_approximation(self):
        for n, k in product((2, 3, 5, 7), (1, 2, 5, 100)):
            witness = dense_kernel_approximation(n, k)
            coeff = witness["kernel_coefficients"]
            addresses = witness["kernel_addresses"]
            self.assertEqual(len(addresses), k + 1)
            self.assertEqual(sum(coeff), 0)
            self.assertTrue(all(x % n == 0 for x in addresses))
            self.assertEqual(sum(c*c for c in coeff[1:]), Q(1, k))
            self.assertEqual(witness["distance_to_e_zero_squared"], Q(1, k))

    def test_negative_controls_for_bad_typed_geometry(self):
        for ray in ((-1, 2), (0, 0), (True, 2), (1, 1.5)):
            with self.assertRaises(ClassicalOriginError):
                ArithmeticRay(*ray)
        with self.assertRaises(ClassicalOriginError):
            intersect_rays([])
        with self.assertRaises(ClassicalOriginError):
            horizon_report((ArithmeticRay(0, 1),), -1)


class ClassicalMellinParityTests(unittest.TestCase):
    def test_exact_log_L2_parity_and_dilation_covariance(self):
        packets = (
            (LogBox(Q(-3, 2), Q(1, 2), Q(2, 3)),
             LogBox(Q(0), Q(5, 4), Q(-3, 2))),
            (LogBox(Q(-5, 4), Q(-1, 2), Q(7, 5)),),
        )
        for g in packets:
            self.assertEqual(log_reflect(log_reflect(g)), g)
            for h in (Q(0), Q(1, 3), Q(-9, 7), Q(5, 2)):
                self.assertEqual(log_inner(g, g), log_inner(log_reflect(g), log_reflect(g)))
                self.assertEqual(log_inner(g, g), log_inner(log_dilate(g, h), log_dilate(g, h)))
                self.assertEqual(log_reflect(log_dilate(log_reflect(g), h)), log_dilate(g, -h))
                self.assertEqual(log_dilate(log_dilate(g, h), -h), g)
        self.assertEqual(log_inner(packets[0], packets[1]),
                         log_inner(log_reflect(packets[0]), log_reflect(packets[1])))

    def test_half_density_is_necessary_exact_counterexample(self):
        # f=1_[1,2] in L2(dx). Naive inversion f(1/x) has norm²=1/2,
        # while correct Jf=x^-1*f(1/x) has norm²=int_(1/2)^1 x^-2 dx=1.
        original_norm_sq = Q(2 - 1)
        wrong_norm_sq = Q(1) - Q(1, 2)
        correct_norm_sq = Q(1, Q(1, 2)) - Q(1, 1)
        self.assertEqual(original_norm_sq, correct_norm_sq)
        self.assertNotEqual(original_norm_sq, wrong_norm_sq)

    def test_exact_mellin_at_critical_real_argument(self):
        # For f(x)=x^-1/2*g(log x), M_f(1/2)=integral g(u) du.
        g = (LogBox(Q(-3), Q(-1), Q(2)), LogBox(Q(0), Q(3, 2), Q(-1)))
        moment = lambda ps: sum((b.hi - b.lo) * b.amplitude for b in ps)
        self.assertEqual(moment(g), Q(5, 2))
        self.assertEqual(moment(g), moment(log_reflect(g)))

    def test_type_guards_and_receipt(self):
        with self.assertRaises(ClassicalOriginError):
            LogBox(0.0, 1, 1)
        with self.assertRaises(ClassicalOriginError):
            LogBox(2, 1, 1)
        with self.assertRaises(ClassicalOriginError):
            log_dilate((), 0.1)
        receipt = classical_unit_origin_probe()
        self.assertEqual(receipt["crt_triple_first_witness"], 23)
        self.assertFalse(receipt["analytic_zeta_functional_equation_proved"])
        self.assertFalse(receipt["global_weil_positivity_or_RH_proved"])


if __name__ == "__main__":
    unittest.main()
