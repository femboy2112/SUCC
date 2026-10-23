"""Independent exact witnesses, including mutations of mirror orientation."""
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ.boundary_realization_selection import matmul, matrix_inverse
from observational_succ.finite_adelic_character_bridge import diagonal_rational_reciprocity
from observational_succ.reality_pin_quantum_global import (
    arithmetic_interaction, arithmetic_density, diagonal_commutator,
    rational_mirror, transpose, quantum_global_receipt,
)


class RealityPinQuantumGlobalTests(unittest.TestCase):
    def test_prime_three_defect_survives_additive_cancellation(self):
        for size in (3, 4, 7):
            for beta in (2, 3, 5):
                for sigma in (2, 3, 4):
                    for additive in (Q(0), Q(1), -Q(1, 2 ** sigma), Q(-7, 3)):
                        k = arithmetic_interaction(size, sigma, additive)
                        rho = arithmetic_density(size, beta)
                        comm = diagonal_commutator(k, rho)
                        self.assertEqual(comm[0][2], Q(1, 3 ** sigma) * (rho[2] - rho[0]))
                        self.assertNotEqual(comm[0][2], 0)

    def test_independent_direct_matrix_commutator(self):
        k = arithmetic_interaction(4)
        rho = arithmetic_density(4)
        diagonal = tuple(tuple(rho[i] if i == j else Q(0) for j in range(4)) for i in range(4))
        left, right = matmul(k, diagonal), matmul(diagonal, k)
        oracle = tuple(tuple(left[i][j] - right[i][j] for j in range(4)) for i in range(4))
        self.assertEqual(diagonal_commutator(k, rho), oracle)

    def test_null_stationarity_and_exact_receipt(self):
        self.assertEqual(diagonal_commutator(((2, 0), (0, 3)), (Q(3, 4), Q(1, 4))), ((0, 0), (0, 0)))
        receipt = quantum_global_receipt()
        self.assertEqual(receipt["cancelled_1_to_2_edge"], "0")
        self.assertEqual(receipt["K_rho_minus_rho_K_1_3"], "-32/441")

    def test_source_composite_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_interaction(6, primes=(2, 3, 6))
        with self.assertRaises(ValueError):
            arithmetic_interaction(6, primes=(2, 2))

    def test_mirror_actual_matrix_identity_and_wrong_orientation(self):
        d = ((Q(2), Q(1)), (Q(1), Q(2)))  # positive eigenvalues 1,3
        a = ((Q(0), Q(0)), (Q(1), Q(0)))
        mirror = rational_mirror(a, d)
        self.assertEqual(matmul(a, d), matmul(d, transpose(mirror)))
        self.assertNotEqual(matmul(a, d), matmul(d, mirror))
        self.assertNotEqual(matmul(a, d), matmul(d, a))

    def test_mirror_is_antihomomorphism_not_homomorphism(self):
        d = ((Q(1), Q(0)), (Q(0), Q(1, 2)))
        a = ((Q(0), Q(1)), (Q(0), Q(0)))
        b = transpose(a)
        m_ab = rational_mirror(matmul(a, b), d)
        self.assertEqual(m_ab, matmul(rational_mirror(b, d), rational_mirror(a, d)))
        self.assertNotEqual(m_ab, matmul(rational_mirror(a, d), rational_mirror(b, d)))

    def test_boundary_dark_thermal_mass(self):
        # K1=[1], K2=diag(1,2), b=e1: identical complete boundary response.
        for s in (Q(0), Q(1), Q(5, 7), Q(19)):
            r1 = matrix_inverse(((1 + s,),))
            r2 = matrix_inverse(((1 + s, Q(0)), (Q(0), 2 + s)))
            self.assertEqual(r1[0][0], r2[0][0])
        # beta=log(2); these Boltzmann weights are exact, not approximated logs.
        self.assertEqual(Q(1, 2) / (Q(1, 2) + Q(1, 4)), Q(2, 3))
        self.assertNotEqual(Q(2, 3), Q(1))

    def test_factorial_convergence_is_not_real_convergence(self):
        for k in range(2, 13):
            for modulus in range(1, k + 1):
                self.assertEqual(factorial(k) % modulus, 0)
            self.assertGreater(factorial(k), factorial(k - 1))

    def test_actual_global_character_sign_and_mutation(self):
        for q in (Q(1, 6), Q(-7, 30), Q(29, 210), Q(2)):
            report = diagonal_rational_reciprocity(q)
            self.assertEqual(report["all_places_total_phase"], 0)
            if 2 * q % 1:
                # Conjugating only the finite place changes the global phase.
                wrong = (q + report["finite_positive_phase"]) % 1
                self.assertNotEqual(wrong, 0)

    def test_schur_base_change_at_good_prime_residues(self):
        # Rational Schur source C=7, E=(1,2), A=[[3,1],[1,4]], B=E^T.
        inverse = matrix_inverse(((Q(3), Q(1)), (Q(1), Q(4))))
        correction = matmul(matmul(((Q(1), Q(2)),), inverse), ((Q(1),), (Q(2),)))[0][0]
        response = Q(7) - correction
        self.assertEqual(response, Q(65, 11))
        for p in (3, 5, 7, 13, 17):
            # Independent adjugate calculation over F_p; p=11 excluded.
            inverse_mod = ((4 * pow(11, -1, p) % p, -pow(11, -1, p) % p),
                           (-pow(11, -1, p) % p, 3 * pow(11, -1, p) % p))
            correction_mod = sum((1, 2)[i] * inverse_mod[i][j] * (1, 2)[j]
                                 for i in range(2) for j in range(2)) % p
            source_then_reduce = response.numerator * pow(response.denominator, -1, p) % p
            self.assertEqual((7 - correction_mod) % p, source_then_reduce)


if __name__ == "__main__":
    unittest.main()
