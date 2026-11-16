"""Exact certificate replay and hostile Gamma-alias controls.

The rank oracle uses forward elimination independently of the production
augmented solve and its dual-witness construction.  No numeric tolerance.
"""
from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ.gamma_observer_descent import (
    GammaDescentError,
    integer_gamma_operator,
    linear_descent,
)


def multiply(left, right):
    columns = tuple(zip(*right))
    return tuple(tuple(sum((F(a) * F(b) for a, b in zip(row, col)), F(0))
                       for col in columns) for row in left)


def rank(matrix):
    rows = [list(map(F, row)) for row in matrix]
    found = 0
    for column in range(len(rows[0])):
        candidates = [i for i in range(found, len(rows)) if rows[i][column] != 0]
        if not candidates:
            continue
        rows[found], rows[candidates[0]] = rows[candidates[0]], rows[found]
        for i in range(found + 1, len(rows)):
            ratio = rows[i][column] / rows[found][column]
            for j in range(column, len(rows[0])):
                rows[i][j] -= ratio * rows[found][j]
        found += 1
        if found == len(rows):
            break
    return found


class GammaObserverDescentTests(unittest.TestCase):
    def assert_certificate(self, operator, report, certificate):
        after = multiply(report, operator)
        self.assertEqual(certificate.descends, rank(tuple(report) + after) == rank(report))
        if certificate.descends:
            self.assertIsNone(certificate.kernel_witness)
            self.assertIsNone(certificate.image_witness)
            self.assertEqual(after, multiply(certificate.factor, report))
        else:
            self.assertIsNone(certificate.factor)
            v = tuple((entry,) for entry in certificate.kernel_witness)
            self.assertEqual(multiply(report, v), tuple((F(0),) for _ in report))
            image = tuple(row[0] for row in multiply(after, v))
            self.assertEqual(image, certificate.image_witness)
            self.assertTrue(any(image))

    def test_valid_source_quotient_and_integer_shapes(self):
        source = ((F(1, 2), 0, 0), (F(1, 3), F(1, 2), 0), (0, F(1, 4), F(1, 2)))
        report = ((1, 0, 0),)
        raw = linear_descent(source, report)
        self.assert_certificate(source, report, raw)
        self.assertEqual(raw.factor, ((F(1, 2),),))
        for order in range(1, 9):
            averaged = integer_gamma_operator(source, order)
            result = linear_descent(averaged, report)
            self.assert_certificate(averaged, report, result)
            self.assertEqual(result.factor, ((F(2, 3) ** order,),))

    def test_sixth_shape_alias_is_not_source_descent(self):
        source = ((0, -1), (1, 1))
        report = ((1, 0),)
        raw = linear_descent(source, report)
        self.assert_certificate(source, report, raw)
        self.assertFalse(raw.descends)
        for order in (1, 2, 3, 4, 5, 7):
            averaged = integer_gamma_operator(source, order)
            result = linear_descent(averaged, report)
            self.assert_certificate(averaged, report, result)
            self.assertFalse(result.descends)
        sixth = integer_gamma_operator(source, 6)
        self.assertEqual(sixth, ((F(-1, 27), F(0)), (F(0), F(-1, 27))))
        result = linear_descent(sixth, report)
        self.assert_certificate(sixth, report, result)
        self.assertTrue(result.descends)
        self.assertEqual(result.factor, ((F(-1, 27),),))
        # The source is orthogonal in this positive definite rational metric.
        metric = ((2, 1), (1, 2))
        self.assertEqual(multiply(multiply(tuple(zip(*source)), metric), source), metric)
        self.assertEqual(metric[0][0] * metric[1][1] - metric[0][1] ** 2, 3)

    def test_first_two_shapes_match_raw_descent_on_rational_contractions(self):
        # All 81 source matrices have induced infinity norm <=1.
        # Nine report rows include zero and sign/coordinate changes.
        cases = 0
        for entries in product((F(-1, 2), F(0), F(1, 2)), repeat=4):
            source = (entries[:2], entries[2:])
            first = integer_gamma_operator(source, 1)
            second = integer_gamma_operator(source, 2)
            for row in product((-1, 0, 1), repeat=2):
                report = (row,)
                raw = linear_descent(source, report)
                self.assert_certificate(source, report, raw)
                for averaged in (first, second):
                    result = linear_descent(averaged, report)
                    self.assert_certificate(averaged, report, result)
                    self.assertEqual(result.descends, raw.descends)
                cases += 1
        self.assertEqual(cases, 729)

    def test_positive_six_cycle_has_same_averaged_observable_alias(self):
        # K e_j=e_(j+1 mod6) is a genuine doubly stochastic source.
        # P records one signed observable/mean, not its full probability law.
        source = tuple(tuple(int(i == (j + 1) % 6) for j in range(6))
                       for i in range(6))
        report = ((F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)),)
        self.assertTrue(all(sum(row) == 1 for row in source))
        self.assertTrue(all(sum(col) == 1 for col in zip(*source)))
        raw = linear_descent(source, report)
        self.assert_certificate(source, report, raw)
        self.assertFalse(raw.descends)
        after = multiply(report, source)
        self.assertEqual(report[0][1], report[0][5])
        self.assertEqual((after[0][1], after[0][5]), (F(-1, 2), F(1)))
        sixth = integer_gamma_operator(source, 6)
        self.assertTrue(all(entry >= 0 for row in sixth for entry in row))
        self.assertTrue(all(sum(row) == 1 for row in sixth))
        expected = tuple(F(-1, 27) * entry for entry in report[0])
        self.assertEqual(multiply(report, sixth), (expected,))
        result = linear_descent(sixth, report)
        self.assert_certificate(sixth, report, result)
        self.assertEqual(result.factor, ((F(-1, 27),),))

    def test_dependent_and_zero_report_rows(self):
        operator = ((F(1, 3), 0), (0, F(1, 2)))
        for report in (((1, 0), (2, 0), (0, 0)), ((0, 0), (0, 0)), ((1, 0), (0, 1))):
            result = linear_descent(operator, report)
            self.assert_certificate(operator, report, result)
            self.assertTrue(result.descends)

    def test_hidden_direction_in_multiple_report_channels(self):
        operator = ((1, 0, 0), (0, 0, 1), (0, 1, 0))
        report = ((1, 0, 0), (0, 1, 0))
        result = linear_descent(operator, report)
        self.assert_certificate(operator, report, result)
        self.assertFalse(result.descends)

    def test_resolvent_composition_exactly(self):
        source = ((F(1, 5), F(1, 3)), (F(-1, 4), F(1, 7)))
        first = integer_gamma_operator(source, 1)
        denominator = ((2 - source[0][0], -source[0][1]),
                       (-source[1][0], 2 - source[1][1]))
        self.assertEqual(multiply(denominator, first), ((1, 0), (0, 1)))
        for a, b in product(range(1, 5), repeat=2):
            self.assertEqual(multiply(integer_gamma_operator(source, a),
                                      integer_gamma_operator(source, b)),
                             integer_gamma_operator(source, a + b))

    def test_singular_resolvent_and_invalid_exact_domains_rejected(self):
        for source in (((2, 0), (0, 0)), ((2,),)):
            with self.assertRaises(GammaDescentError):
                integer_gamma_operator(source, 1)
        for source in ((), ((1, 2),), ((1, 0), (0,)), ((0.5,),), ((True,),)):
            with self.assertRaises(GammaDescentError):
                integer_gamma_operator(source, 1)
        for order in (0, -1, F(1, 2), 1.0, True):
            with self.assertRaises(GammaDescentError):
                integer_gamma_operator(((0,),), order)
        for report in ((), ((1, 0, 0),), ((1.0, 0),), ((1, 0), (1,))):
            with self.assertRaises(GammaDescentError):
                linear_descent(((1, 0), (0, 1)), report)

    def test_algebraic_domain_does_not_claim_positive_gamma_law(self):
        # Invertibility is enough for this algebra, but K=3 is not a
        # contraction and its positive-weight power series diverges.
        self.assertEqual(integer_gamma_operator(((3,),), 1), ((F(-1),),))


if __name__ == "__main__":
    unittest.main()
