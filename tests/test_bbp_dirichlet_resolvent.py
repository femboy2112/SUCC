"""Source-specific rational certificates; analytic authority is the paper proof."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import unittest

from observational_succ import bbp_dirichlet_resolvent as response
from observational_succ.pi_source_collision import bbp_forcing


def determinant(matrix):
    """Independent exact elimination for the four-source certificate."""
    rows = [list(row) for row in matrix]
    value = Q(1)
    for k in range(len(rows)):
        pivot = next((j for j in range(k, len(rows)) if rows[j][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            value = -value
        value *= rows[k][k]
        for j in range(k + 1, len(rows)):
            ratio = rows[j][k] / rows[k][k]
            for i in range(k + 1, len(rows)):
                rows[j][i] -= ratio * rows[k][i]
    return value


class BBPDirichletResolventTests(unittest.TestCase):
    def test_imported_original_source_passport_and_shift_relation(self):
        source = Path(response.__file__).with_name("pi_source_collision.py")
        self.assertEqual(sha256(source.read_bytes()).hexdigest(),
                         "c3d1868624c3547124fd2cf33da35e10e8c48bec7922095cad83fb446f18a777")
        for n in list(range(1, 51)) + [127, 4096, 100003]:
            left, right = response.source_shift_identity(n)
            self.assertEqual(left, right)
            self.assertEqual(bbp_forcing(n), Q(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))

    def test_all_four_roots_are_load_bearing(self):
        self.assertEqual(len(set(response.POLES)), 4)
        for b in response.POLES:
            self.assertEqual(response.polynomial_value(response.SHIFT_DENOMINATOR, b), 0)
            self.assertNotEqual(response.polynomial_value(response.SHIFT_NUMERATOR, b), 0)
        # This exact determinant certifies the rank-four moment realization.
        hankel = [[response.asymptotic_coefficient(i+j+1) for j in range(4)]
                  for i in range(4)]
        self.assertEqual(determinant(hankel), Q(-225, 549755813888))

    def test_residues_independent_integer_formula_and_positive_bounds(self):
        self.assertEqual(response.asymptotic_coefficient(1), 0)
        for m in range(1, 101):
            expected = Q(4*7**m - 2*4**m - 3**m - 2**m, 8**(m+1))
            residue = response.pole_residue(m)
            self.assertEqual(residue, expected)
            lower, upper = response.coefficient_bounds(m + 1)
            self.assertLessEqual(lower, residue)
            self.assertLess(residue, upper)
        self.assertEqual(response.pole_residue(1), Q(15, 64))
        self.assertEqual(response.pole_residue(2), Q(151, 512))
        self.assertEqual(response.pole_residue(3), Q(1209, 4096))

    def test_fourth_order_residue_recurrence(self):
        for k in range(1, 70):
            self.assertEqual(response.coefficient_recurrence_residual(k), 0)

    def test_geometric_remainder_bound_on_authentic_forcing(self):
        for n in (1, 2, 3, 17, 97, 65537):
            for terms in (1, 2, 3, 8, 19, 40):
                remainder = bbp_forcing(n) - response.source_jet(n, terms)
                # Independent finite geometric identity including signed channels.
                direct = sum((w*b**terms / (n**terms*(n-b))
                              for w, b in zip(response.WEIGHTS, response.POLES)), Q(0))
                self.assertEqual(remainder, direct)
                self.assertGreater(remainder, 0)
                self.assertLess(remainder, response.source_jet_remainder_bound(n, terms))

    def test_certified_zeta_tail_bound_including_left_halfplane(self):
        for sigma in (Q(-19, 2), Q(-3), Q(-1, 2), Q(0), Q(7, 3)):
            k = max(2, int(-sigma) + 2)
            bound = response.zeta_expansion_tail_bound(k, sigma)
            # Bound each zeta term by its elementary integral upper bound.
            finite_upper = sum((response.asymptotic_coefficient(j) *
                                (1 + 1/(sigma+j-1))
                                for j in range(k+1, k+91)), Q(0))
            self.assertLess(finite_upper, bound)
            self.assertGreater(bound, 0)

    def test_exact_finite_part_basis_matches_handoff(self):
        self.assertEqual(response.finite_part_basis_coefficients(1),
            (Q(0), Q(15,64), Q(27,128), Q(31,128), Q(39,32), Q(31,64)))
        self.assertEqual(response.finite_part_basis_coefficients(0)[1], 0)
        for m in range(1, 31):
            self.assertEqual(response.finite_part_basis_coefficients(m)[1],
                             response.pole_residue(m))
        self.assertEqual([response.zeta_nonpositive(k) for k in range(6)],
                         [Q(-1,2), Q(-1,12), Q(0), Q(1,120), Q(0), Q(-1,252)])

    def test_entire_gamma_interpolation_has_strict_alternating_signs(self):
        for m in range(1, 80):
            value = response.gamma_regularized_negative_value(m)
            self.assertGreater((-1)**(m-1)*value, 0)
            self.assertLess(value * response.gamma_regularized_negative_value(m+1), 0)

    def test_positive_wrong_source_matches_two_residues_but_fails_equation(self):
        mutation = tuple(Q(w,100) for w in (-1, 10, -15, 6))
        changes = [sum((w*b**k for w,b in zip(mutation,response.POLES)), Q(0))
                   for k in range(4)]
        self.assertEqual(changes, [Q(0), Q(0), Q(0), Q(-15,12800)])
        for n in (1, 2, 7, 31, 997):
            altered = response.moment_matched_altered_forcing(n)
            self.assertGreater(altered, 0)
            self.assertNotEqual(altered, bbp_forcing(n))
            self.assertEqual(altered-bbp_forcing(n),
                sum((w/(n-b) for w,b in zip(mutation,response.POLES)), Q(0)))
            residual = (response.polynomial_value(response.SHIFT_DENOMINATOR,n)*altered
                        - response.polynomial_value(response.SHIFT_NUMERATOR,n))
            self.assertEqual(residual, Q(-3,2560))

    def test_no_multiplicative_source_even_after_normalizing_first_coefficient(self):
        # Multiplicativity of r(n)/r(1) would force this coprime 2,3 equality.
        self.assertNotEqual(bbp_forcing(6)*bbp_forcing(1),
                            bbp_forcing(2)*bbp_forcing(3))

    def test_entire_forcing_response_does_not_authenticate_zero_seed(self):
        left, right = Q(0), Q(1,15)
        for n in range(1, 25):
            old_left, old_right = left, right
            left = 16*left + bbp_forcing(n)
            right = 16*right + bbp_forcing(n)
            self.assertEqual(left-16*old_left, right-16*old_right)
            self.assertEqual(right-left, Q(16**n,15))
            self.assertEqual((right-left)%1, Q(1,15))

    def test_exact_input_domains(self):
        for invalid in (True, 1.0, "1", -1):
            with self.assertRaises(ValueError):
                response.pole_residue(invalid)
        with self.assertRaises(ValueError):
            response.pole_residue(0)
        with self.assertRaises(ValueError):
            response.zeta_expansion_tail_bound(3, -3)
        with self.assertRaises(ValueError):
            response.zeta_expansion_tail_bound(3, -2.0)


if __name__ == "__main__":
    unittest.main()
