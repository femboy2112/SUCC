"""Independent exact source, linear minimality, and mutation checks for BBP atoms."""
from fractions import Fraction as Q
import unittest

from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.bbp_atomic_substrate import (
    COMPLEX_BLOCK, INPUT_VECTOR, OUTPUT_ROW, PERIOD_COEFFICIENTS,
    QUADRATIC_BLOCK, TRANSITION, atomic_clock_certificate, atomic_coefficient,
    atomic_kernel_value, atomic_state, atomic_tail_certificate, compiled_forcing,
    kernel_identity_certificate, minimal_realization_certificate, recurrence_coefficients,
)


def multiply(left, right):
    return [[sum((left[i][k]*right[k][j] for k in range(len(right))), Q())
             for j in range(len(right[0]))] for i in range(len(left))]


def solve(matrix, vector):
    rows = [list(row)+[rhs] for row, rhs in zip(matrix, vector)]
    n = len(rows)
    for i in range(n):
        pivot = next(j for j in range(i, n) if rows[j][i])
        rows[i], rows[pivot] = rows[pivot], rows[i]
        value = rows[i][i]
        rows[i] = [x/value for x in rows[i]]
        for j in range(n):
            if i != j:
                factor = rows[j][i]
                rows[j] = [x-factor*y for x, y in zip(rows[j], rows[i])]
    return [row[-1] for row in rows]


def determinant(matrix):
    rows = [list(row) for row in matrix]
    value = Q(1)
    for i in range(len(rows)):
        pivot = next((j for j in range(i, len(rows)) if rows[j][i]), None)
        if pivot is None:
            return Q()
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            value = -value
        factor = rows[i][i]
        value *= factor
        for j in range(i+1, len(rows)):
            ratio = rows[j][i]/factor
            rows[j] = [x-ratio*y for x, y in zip(rows[j], rows[i])]
    return value


class BBPAtomicSubstrateTests(unittest.TestCase):
    def test_two_block_resolvent_against_independent_four_by_four_solve(self):
        for x in (Q(0), Q(1, 17), Q(2, 7), Q(1, 2), Q(13, 17), Q(1)):
            matrix = [[Q(i == j)-x*TRANSITION[i][j] for j in range(4)] for i in range(4)]
            state = solve(matrix, INPUT_VECTOR)
            value = sum((a*b for a, b in zip(OUTPUT_ROW, state)), Q())
            self.assertEqual(value, atomic_kernel_value(x))
            receipt = kernel_identity_certificate(x)
            self.assertEqual(value, receipt["original"])

    def test_matrix_coefficient_recurrence_and_eight_clock_independently(self):
        recurrence = recurrence_coefficients(130)
        current = [[x] for x in INPUT_VECTOR]
        for m in range(130):
            direct = sum((OUTPUT_ROW[i]*current[i][0] for i in range(4)), Q())
            self.assertEqual(atomic_state(m), tuple(row[0] for row in current))
            self.assertEqual(atomic_coefficient(m), direct)
            self.assertEqual(recurrence[m], direct)
            self.assertEqual(direct, PERIOD_COEFFICIENTS[m % 8]/16**(m//8))
            current = multiply(TRANSITION, current)
        for m in (0, 1, 7, 31, 97, 257, 1009):
            self.assertEqual(atomic_coefficient(m+8), atomic_coefficient(m)/16)

    def test_exact_source_poles_reconstructed_from_atoms(self):
        for n in (1, 2, 3, 7, 31, 97, 257, 1009, 65521):
            direct = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            self.assertEqual(compiled_forcing(n), direct)
            self.assertEqual(compiled_forcing(n), exact_forcing(n))

    def test_least_scalar_return_keeps_relative_sign(self):
        proof = atomic_clock_certificate()
        self.assertEqual(proof["quadratic_square"], ((Q(1, 2), Q()), (Q(), Q(1, 2))))
        self.assertEqual(proof["complex_fourth"], ((Q(-1, 4), Q()), (Q(), Q(-1, 4))))
        self.assertEqual(proof["scalar_returns_through_eight"], ((8, Q(1, 16)),))
        self.assertEqual(tuple(proof["fourth_power"][i][i] for i in range(4)),
                         (Q(1, 4), Q(1, 4), Q(-1, 4), Q(-1, 4)))

    def test_hankel_minimality_against_independent_elimination_and_channel_deletion(self):
        proof = minimal_realization_certificate()
        self.assertEqual(determinant(proof["hankel"]), Q(1, 16384))
        self.assertEqual(proof["denominator_at_numerator_root"], 1)
        for block, output in ((QUADRATIC_BLOCK, (Q(0), Q(-1, 8))),
                              (COMPLEX_BLOCK, (Q(1, 4), Q(0)))):
            current = [[Q(1)], [Q(0)]]
            coefficients = []
            for _ in range(7):
                coefficients.append(sum((output[i]*current[i][0] for i in range(2)), Q()))
                current = multiply(block, current)
            hankel = [[coefficients[i+j] for j in range(4)] for i in range(4)]
            self.assertEqual(determinant(hankel), 0)

    def test_weighted_contraction_on_signed_rational_states(self):
        proof = atomic_clock_certificate()
        metric = proof["metric"]
        for v in ((1, 0, 0, 0), (0, 1, 0, 0), (2, -3, 5, -7),
                  (Q(1, 3), Q(-2, 7), Q(5, 11), Q(3, 2))):
            advanced = [row[0] for row in multiply(TRANSITION, [[Q(x)] for x in v])]
            norm = sum((metric[i][i]*v[i]**2 for i in range(4)), Q())
            new_norm = sum((metric[i][i]*advanced[i]**2 for i in range(4)), Q())
            self.assertEqual(new_norm, norm/2)

    def test_finite_tail_defect_against_more_source_blocks(self):
        for n in (0, 1, 2, 7, 97, 1009):
            for depth in (1, 3, 8):
                certificate = atomic_tail_certificate(n, depth)
                longer = sum((exact_forcing(n+j)/16**j for j in range(1, depth+20)), Q())
                final_bound = Q(1, 16**(depth+19)*(8*(n+depth+19)+1)*(8*(n+depth+19)+2))
                self.assertLess(certificate.lower, longer)
                self.assertLess(longer+final_bound, certificate.upper)
                # Exact block regrouping, with the unmatched finite defect preserved.
                extra = atomic_tail_certificate(n+depth, 7)
                combined = atomic_tail_certificate(n, depth+7)
                self.assertEqual(combined.lower-certificate.lower, extra.lower/16**depth)

    def test_phase_or_output_mutations_break_authentic_source(self):
        # Removing the cross-channel relative sign changes the m=4 coefficient.
        self.assertNotEqual(atomic_coefficient(4), atomic_coefficient(0)/4)
        # Dropping the quadratic block changes c1, and therefore the transfer law.
        self.assertNotEqual(Q(1, 4)*COMPLEX_BLOCK[0][0], atomic_coefficient(1))
        # Reversing the minus sign of the -1/8 output fails the first coefficient cancellation.
        state = atomic_state(1)
        mutant = state[1]/8+state[2]/4
        self.assertNotEqual(mutant, atomic_coefficient(1))

    def test_domains_exclude_approximate_or_untyped_inputs(self):
        for call in (
            lambda: atomic_state(True), lambda: atomic_state(-1),
            lambda: recurrence_coefficients(-1), lambda: compiled_forcing(0),
            lambda: atomic_kernel_value(0.5), lambda: atomic_kernel_value(Q(3, 2)),
            lambda: atomic_tail_certificate(0, 0), lambda: atomic_tail_certificate(-1, 2),
        ):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
