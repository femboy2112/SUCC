"""Exact independent residue, box, and section oracles for Main VIII geometry."""
import unittest
from fractions import Fraction
from itertools import product
from math import gcd, lcm, prod

from sympy import Matrix

from observational_succ.viii_exterior_geometry import (
    SectionGeometryError, section_lattice, projected_box_enclosure,
    section_cell_budget, section_volume_factors,
)


class TestSectionLattices(unittest.TestCase):
    def test_full_rank_index_from_finite_residue_oracle(self):
        for m in range(1, 4):
            identity = tuple(tuple(int(i == j) for j in range(m)) for i in range(m))
            for ds in product(range(1, 4), repeat=m):
                for q in range(1, 5):
                    rec = section_lattice(identity, ds, q)
                    period = lcm(*ds, q)
                    accepted = sum(all(x % d == 0 for x, d in zip(xs, ds))
                                   and sum(xs) % q == 0
                                   for xs in product(range(period), repeat=m))
                    self.assertEqual(period ** m, rec.section_index * accepted)
                    self.assertEqual(rec.ambient_index, prod(ds) * q // gcd(q, gcd(*ds)))
                    self.assertEqual(rec.ambient_index, rec.section_index)
                    self.assertEqual(rec.covolume_squared, rec.section_index ** 2)

    def test_lower_rank_index_from_homomorphism_image(self):
        bases = [((1,), (1,), (1,)), ((1, 0), (2, -1), (0, 1)),
                 ((1, 0), (0, 1), (1, 1)), ((2, 1), (1, 1), (0, 1))]
        for basis in bases:
            B = Matrix(basis)
            for ds, q in [((2, 3, 2), 3), ((1, 2, 3), 4), ((2, 2, 1), 2)]:
                record = section_lattice(basis, ds, q)
                period = lcm(*ds, q)
                images = set()
                for zs in product(range(period), repeat=B.cols):
                    xs = list(B * Matrix(zs))
                    images.add(tuple(int(x) % d for x, d in zip(xs, ds)) + (int(sum(xs)) % q,))
                self.assertEqual(len(images), record.section_index)
                self.assertEqual(record.covolume_squared,
                                 record.section_index ** 2 * int((B.T * B).det()))

    def test_ambient_index_disappears_on_positive_section(self):
        for M in (3, 5, 17, 101):
            rec = section_lattice(((1, 0), (M - 1, -1), (0, 1)), (1, 1, 1), M)
            self.assertEqual(rec.ambient_index, M)
            self.assertEqual(rec.section_index, 1)
            points = [(1, j, M - 1 - j) for j in range(1, M - 1)]
            self.assertEqual(len(points), M - 2)
            self.assertTrue(all(gcd(*point) == 1 and sum(point) == M for point in points))

    def test_saturation_and_type_guards(self):
        for basis in [((2, 0), (0, 1)), ((2,), (2,)), ((1, 2), (2, 4))]:
            with self.assertRaises(SectionGeometryError):
                section_lattice(basis, (1,) * len(basis), 1)
        for bad in (True, 2.0, Fraction(2)):
            with self.assertRaises(SectionGeometryError):
                section_lattice(((1,),), (bad,), 1)
        with self.assertRaises(SectionGeometryError):
            section_lattice(((1,),), (1,), 0)

    def test_projected_rectangles_with_translates(self):
        for H in [((2, 1), (0, 3)), ((1, -7), (0, 4)), ((5, 0), (0, 1))]:
            inverse = Matrix(H).inv()
            for n1, n2 in product(range(6), repeat=2):
                bound = projected_box_enclosure(H, (n1, n2))
                for offset in ((0, 0), (1, -2), (-4, 5)):
                    count = 0
                    for x, y in product(range(1, n1 + 1), range(1, n2 + 1)):
                        coords = inverse * Matrix([x - offset[0], y - offset[1]])
                        count += all(z.is_Integer for z in coords)
                    self.assertLessEqual(bound.lower, count)
                    self.assertLessEqual(count, bound.upper)
                    self.assertLessEqual(abs(count - bound.volume_over_index), bound.absolute_error)
        with self.assertRaises(SectionGeometryError):
            projected_box_enclosure(((1, 0), (1, 1)), (3, 3))

    def test_full_simplex_cell_volume_bound(self):
        rec = section_lattice(((1, 0), (0, 1)), (2, 3), 5)
        beta = section_cell_budget(rec.lattice_basis, (Fraction(1, 3), Fraction(1, 3)))
        density = Fraction(1, 2 * rec.section_index)
        for X in range(0, 101, 5):
            count = sum(a % 2 == 0 and b % 3 == 0 and (a + b) % 5 == 0
                        for a in range(1, X + 1) for b in range(1, X - a + 1))
            lower, upper = section_volume_factors(2, X, beta)
            self.assertLessEqual(density * lower, count)
            self.assertLessEqual(count, density * upper)

    def test_rank_two_actual_simplex_volume_bound(self):
        for M in (3, 7, 11):
            rec = section_lattice(((1, 0), (M - 1, -1), (0, 1)), (1, 1, 1), M)
            center = (Fraction(1, 2 * M), Fraction(M - 1, 4 * M), Fraction(M - 1, 4 * M))
            beta = section_cell_budget(rec.lattice_basis, center)
            density = Fraction(M - 1, 2 * M ** 2)
            for X in range(101):
                T = X // M
                count = (M - 1) * T * (T + 1) // 2 - T
                lower, upper = section_volume_factors(2, X, beta)
                self.assertLessEqual(density * lower, count)
                self.assertLessEqual(count, density * upper)

    def test_cell_center_and_cutoff_guards(self):
        for center in [(0, Fraction(1, 2)), (1, 1), (0.2, 0.2), (True, Fraction(1, 4))]:
            with self.assertRaises(SectionGeometryError):
                section_cell_budget(((1, 0), (0, 1)), center)
        with self.assertRaises(SectionGeometryError):
            section_cell_budget(((1,), (1,)), (Fraction(1, 3), Fraction(1, 4)))
        with self.assertRaises(SectionGeometryError):
            section_volume_factors(2, 1.0, 1)


if __name__ == "__main__":
    unittest.main()
