"""Exact rational controls for the Defect-Window Tomography research note.

This module checks small finite models only. No tests imply a universal
source-identification theorem, π normality, or a physical latent carrier.
"""

from fractions import Fraction
import unittest


def matmul(left, right):
    """Multiply nonempty, rectangular small matrices over the rationals."""
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible or empty matrix")
    if any(len(row) != len(left[0]) for row in left):
        raise ValueError("ragged left matrix")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("ragged right matrix")
    return tuple(
        tuple(
            sum((Fraction(left[i][k]) * Fraction(right[k][j])
                 for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def matvec(matrix, vector):
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("incompatible or empty matrix/vector")
    return tuple(
        sum((Fraction(entry) * Fraction(value)
             for entry, value in zip(row, vector)), Fraction(0))
        for row in matrix
    )


def matsub(left, right):
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("matrix shapes differ")
    return tuple(
        tuple(Fraction(a) - Fraction(b) for a, b in zip(row_a, row_b))
        for row_a, row_b in zip(left, right)
    )


def rank(matrix):
    """Exact Gauss-Jordan rank; no floating-point tolerances."""
    if not matrix:
        return 0
    cols = len(matrix[0])
    if any(len(row) != cols for row in matrix):
        raise ValueError("ragged matrix")
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row:
                factor = a[row][col]
                if factor:
                    a[row] = [
                        a[row][j] - factor * a[pivot_row][j]
                        for j in range(cols)
                    ]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


class DefectWindowTomographyTests(unittest.TestCase):
    """DWT-01–05 exact examples and adversarial mutations."""

    def setUp(self):
        self.p = ((1, 0, 0), (0, 1, 0))
        self.b = ((0, 1), (-1, 0))
        self.k_persistent = ((0, 1, 1), (-1, 0, 0), (0, 0, 1))
        self.k_doubling = ((0, 1, 1), (-1, 0, 0), (0, 0, 2))
        self.k_invisible = ((0, 1, 0), (-1, 0, 0), (0, 0, 2))
        self.defect = ((0, 0, 1), (0, 0, 0))
        self.initial = (1, 2, 3)

    def one_step_defect(self, k):
        return matsub(matmul(self.p, k), matmul(self.b, self.p))

    def test_shadow_defects_are_the_hidden_coordinate(self):
        self.assertEqual(self.one_step_defect(self.k_persistent), self.defect)
        self.assertEqual(matvec(self.defect, self.initial), (3, 0))
        # A alone cannot predict x' from x; B alone cannot predict y' from y.
        self.assertEqual(matvec((self.p[0],), (0, 1, 0)), (0,))
        self.assertEqual(matvec((self.p[0],), matvec(self.k_persistent, (0, 1, 0))), (1,))
        self.assertEqual(matvec((self.p[1],), (1, 0, 0)), (0,))
        self.assertEqual(matvec((self.p[1],), matvec(self.k_persistent, (1, 0, 0))), (-1,))
        # Even both present shadows miss the hidden direction, which escapes.
        self.assertEqual(matvec(self.p, (0, 0, 1)), (0, 0))
        self.assertEqual(matvec(self.p, matvec(self.k_persistent, (0, 0, 1))), (1, 0))

    def test_one_step_operator_is_identical_for_distinct_sources(self):
        self.assertEqual(matmul(self.p, self.k_persistent),
                         matmul(self.p, self.k_doubling))
        self.assertEqual(self.one_step_defect(self.k_persistent),
                         self.one_step_defect(self.k_doubling))
        self.assertNotEqual(self.k_persistent, self.k_doubling)
        self.assertEqual(self.one_step_defect(self.k_doubling), self.defect)

    def test_delayed_holdout_splits_exact_rivals(self):
        first_a = matvec(self.k_persistent, self.initial)
        first_b = matvec(self.k_doubling, self.initial)
        self.assertEqual(matvec(self.p, first_a), (5, -1))
        self.assertEqual(matvec(self.p, first_a), matvec(self.p, first_b))
        self.assertEqual(matvec(self.p, matvec(self.k_persistent, first_a)), (2, -5))
        self.assertEqual(matvec(self.p, matvec(self.k_doubling, first_b)), (5, -5))
        self.assertEqual(first_a[2], 3)
        self.assertEqual(first_b[2], 6)

    def test_dynamic_observability_grows_beyond_current_report(self):
        self.assertEqual(rank(self.p), 2)
        observation_one = self.p + matmul(self.p, self.k_persistent)
        self.assertEqual(rank(observation_one), 3)
        # A mutation that forgets hidden-to-visible coupling must fail the rank gain.
        observation_mutant = self.p + matmul(self.p, self.k_invisible)
        self.assertEqual(rank(observation_mutant), 2)

    def test_independent_third_window_vs_redundant_window(self):
        new = ((1, 2, 1),)
        redundant = ((1, 2, 0),)
        self.assertEqual(rank(self.p + new), 3)
        self.assertEqual(rank(self.p + redundant), 2)
        self.assertEqual(matvec(new, matvec(self.k_persistent, self.initial)), (6,))
        self.assertEqual(matvec(new, matvec(self.k_doubling, self.initial)), (9,))
        self.assertEqual(matvec(redundant, matvec(self.k_persistent, self.initial)), (3,))
        self.assertEqual(matvec(redundant, matvec(self.k_doubling, self.initial)), (3,))

    def test_sign_erasure_aliases_opposite_hidden_directions(self):
        plus = matvec(self.defect, (1, 2, 3))
        minus = matvec(self.defect, (1, 2, -3))
        self.assertEqual(plus, (3, 0))
        self.assertEqual(minus, (-3, 0))
        self.assertNotEqual(plus, minus)
        self.assertEqual(tuple(abs(x) for x in plus), tuple(abs(x) for x in minus))

    def test_calibrated_coordinate_transport_preserves_rank_not_numbers(self):
        source_chart = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
        observer_chart = ((2, 0), (0, 1))
        observer_chart_inverse = ((Fraction(1, 2), 0), (0, 1))
        # Both source_chart and observer_chart source inverse are exact.
        changed_k = matmul(matmul(source_chart, self.k_persistent), source_chart)
        changed_p = matmul(matmul(observer_chart, self.p), source_chart)
        changed_b = matmul(matmul(observer_chart, self.b), observer_chart_inverse)
        changed_d = matsub(matmul(changed_p, changed_k),
                           matmul(changed_b, changed_p))
        expected_d = matmul(matmul(observer_chart, self.defect), source_chart)
        self.assertEqual(changed_d, expected_d)
        self.assertEqual(changed_d, ((0, 0, -2), (0, 0, 0)))
        self.assertEqual(rank(changed_d), rank(self.defect))
        self.assertNotEqual(changed_d, self.defect)

    def test_zero_defect_cannot_reconstruct_permanently_hidden_source(self):
        self.assertEqual(self.one_step_defect(self.k_invisible),
                         ((0, 0, 0), (0, 0, 0)))
        hidden_state = (0, 0, 1)
        for step in range(8):
            self.assertEqual(matvec(self.p, hidden_state), (0, 0),
                             msg="hidden state leaked at step %d" % step)
            self.assertEqual(hidden_state[2], 2 ** step)
            hidden_state = matvec(self.k_invisible, hidden_state)


if __name__ == "__main__":
    unittest.main()
