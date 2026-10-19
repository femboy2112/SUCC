"""Independent quotient, pairing and mutation controls for the Haar no-go."""

from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
import unittest

from observational_succ.institute_atomic_haar import (
    Cylinder, exact_control_report, haar_unit_mass, harmonic_pairing_norm_squared,
    mobius_coefficients, mobius_value, residue_unit_mass, valuation_shell,
)


class AtomicHaarControls(unittest.TestCase):
    def test_euler_product_against_residue_count_for_every_subfamily(self):
        for size in range(5):
            for family in combinations((2, 3, 5, 7), size):
                self.assertEqual(haar_unit_mass(family), residue_unit_mass(family))
                self.assertGreater(haar_unit_mass(family), 0)

    def test_mobius_projection_against_direct_divisibility(self):
        for size in range(5):
            for family in combinations((2, 3, 5, 7), size):
                for integer in range(1, 301):
                    self.assertEqual(mobius_value(family, integer),
                                     int(all(integer % p for p in family)))
                self.assertEqual(mobius_value(family, 1), 1)

    def test_true_cylinder_isometry_and_adjoint_with_changed_period(self):
        for p, m, n in product((2, 3, 5), (1, 2, 4, 7), (1, 3, 5)):
            f = Cylinder(tuple(Q((3 * i + 2) % 7 - 3, 5) for i in range(m)))
            g = Cylinder(tuple(Q((2 * i + 1) % 5 - 2, 3) for i in range(n)))
            bf, cg = f.divide_cutoff(p), g.multiply_pullback(p)
            self.assertEqual(bf.period, p * m)
            self.assertEqual(p * bf.inner(bf), f.inner(f))
            self.assertEqual(p * bf.inner(g), f.inner(cg))
            self.assertTrue(bf.multiply_pullback(p).equivalent(f))

    def test_range_projection_and_double_commutation(self):
        f = Cylinder((Q(1), Q(-2), Q(3, 7), Q(0)))
        for p in (2, 3, 5):
            projected = f.multiply_pullback(p).divide_cutoff(p)
            for x in range(projected.period):
                self.assertEqual(projected(x), f(x) if x % p == 0 else 0)
            for q in (2, 3, 5):
                if p != q:
                    self.assertTrue(f.divide_cutoff(p).multiply_pullback(q).equivalent(
                        f.multiply_pullback(q).divide_cutoff(p)))

    def test_finite_multishift_shell_orthogonality_and_norm(self):
        family = (2, 3)
        shells = [(ks, valuation_shell(family, ks)) for ks in product(range(3), repeat=2)]
        for ks, shell in shells:
            scale = prod(p ** k for p, k in zip(family, ks))
            self.assertEqual(shell.inner(shell), haar_unit_mass(family) / scale)
            for other_ks, other in shells:
                if other_ks != ks:
                    self.assertEqual(shell.inner(other), 0)

    def test_dirac_distribution_duality_at_actual_integer_points(self):
        # Transposition is checked independently of point-push notation.
        phi = Cylinder((Q(1), Q(2), Q(-3), Q(5, 7), Q(-11, 13)))
        for p, n in product((2, 3, 5, 7), range(1, 51)):
            self.assertEqual(phi.multiply_pullback(p)(n), phi(p * n))
            expected = phi(n // p) if n % p == 0 else 0
            self.assertEqual(phi.divide_cutoff(p)(n), expected)
            # Required half-density, squared after clearing common radicals.
            self.assertEqual(Q(1, p * n), Q(1, p) * Q(1, n))
            if n % p == 0:
                self.assertEqual(p * Q(1, n), Q(1, n // p))

    def test_mutations_retain_exact_failure_receipts(self):
        one = Cylinder((Q(1),))
        self.assertEqual(one.divide_cutoff(2).inner(one.divide_cutoff(2)), Q(1, 2))
        self.assertNotEqual(one.inner(one), one.divide_cutoff(2).inner(one.divide_cutoff(2)))
        self.assertEqual(mobius_value((2, 3, 5), 7), 1)
        self.assertEqual(mobius_value((2, 3, 5, 7), 7), 0)
        # Evaluating the two independently defined dual routes at phi=1
        # detects the wrong unweighted embedding after squaring.
        self.assertNotEqual(one(2) ** 2, one.multiply_pullback(2)(1) ** 2 / 2)
        report = exact_control_report()
        self.assertEqual(report["authority"], "EXACT_FINITE_CONTROLS_ONLY")

    def test_harmonic_extension_obstruction_and_dyadic_lower_bound(self):
        for k in range(1, 9):
            self.assertGreaterEqual(harmonic_pairing_norm_squared(2 ** k), 1 + Q(k, 2))

    def test_nonclosable_graph_sequence_cylinder_discrepancy(self):
        from observational_succ.institute_atomic_haar import harmonic_graph_witness
        for size in (1, 2, 7, 32, 257):
            for period in (1, 2, 3, 6, 11):
                w = harmonic_graph_witness(size, period)
                self.assertEqual(sum(w["masses"]), 1)
                self.assertEqual(w["source_norm_squared"],
                                 1 / harmonic_pairing_norm_squared(size))
                self.assertTrue(all(abs(m-w["haar_cylinder_mass"]) <=
                                    w["coordinate_error_bound"] for m in w["masses"]))

    def test_invalid_carriers_and_composite_mutations_are_rejected(self):
        for family in ((4,), (1,), (2, 2), (True,), (2.0,)):
            with self.assertRaises(ValueError):
                haar_unit_mass(family)
        with self.assertRaises(ValueError):
            Cylinder(())
        with self.assertRaises(TypeError):
            Cylinder((0.5,))
        with self.assertRaises(ValueError):
            residue_unit_mass((2, 3, 5), maximum_period=10)
        with self.assertRaises(ValueError):
            valuation_shell((2, 3), (1,))
        self.assertEqual(mobius_coefficients(()), {1: 1})


if __name__ == "__main__":
    unittest.main()
