"""Independent exact finite controls for arity-five semantics, not RH/pi proofs."""
from __future__ import annotations

import itertools
import unittest
from fractions import Fraction

from observational_succ.arity_four_bridge import (GaussQ, Omega3, bbp_residue_prefix,
                                                 congruence, coordinates, det, hermitian,
                                                 minkowski, mmul, ONE)
from observational_succ.arity_five_hilbert import (
    ar1_factorization, boost_loop, cubic_loop_kernel, cycle_character,
    exact_phase_cocycle, loop_kernel, oriented_edge,
    parallelogram_defect, rational_determinant, tetrahedron_boundary,
    transform_edges, triangle_curvature,
)


class FourVertexCoherenceTests(unittest.TestCase):
    def test_triangle_nontrivial_and_gauge_invariant(self):
        a = {(0, 1): Fraction(1, 7), (0, 2): Fraction(1, 11),
             (1, 2): Fraction(1, 5)}
        f = triangle_curvature(a, 0, 1, 2)
        self.assertEqual(f, Fraction(1, 7)+Fraction(1, 5)-Fraction(1, 11))
        self.assertNotEqual(f, 0)
        self.assertEqual(triangle_curvature(a, 2, 1, 0), -f)
        gauge = {0: Fraction(4, 13), 1: Fraction(3, 7), 2: Fraction(-1, 2)}
        self.assertEqual(triangle_curvature(transform_edges(a, gauge), 0, 1, 2), f)
        with self.assertRaises(ValueError): triangle_curvature(a, 1, 1, 2)

    def test_tetrahedral_bianchi_exhaustive(self):
        edges = list(itertools.combinations(range(4), 2))
        for values in itertools.product((Fraction(0), Fraction(2, 3)), repeat=6):
            a = dict(zip(edges, values))
            self.assertEqual(tetrahedron_boundary(a, 0, 1, 2, 3), 0)
            gauge = {v: Fraction(v + 1, 7) for v in range(4)}
            self.assertEqual(tetrahedron_boundary(transform_edges(a, gauge), 0, 1, 2, 3), 0)
        with self.assertRaises(ValueError): tetrahedron_boundary({}, 0, 0, 1, 2)

    def test_mutant_wrong_tetrahedral_orientation_is_detected(self):
        a = {(0, 1): 1, (0, 2): 0, (0, 3): 0,
             (1, 2): 0, (1, 3): 0, (2, 3): 0}
        correct = tetrahedron_boundary(a, 0, 1, 2, 3)
        mutation = (triangle_curvature(a, 1, 2, 3)
                    + triangle_curvature(a, 0, 2, 3)
                    + triangle_curvature(a, 0, 1, 3)
                    + triangle_curvature(a, 0, 1, 2))
        self.assertEqual(correct, 0)
        self.assertNotEqual(mutation, 0)


class SameCarrierRepresentationTests(unittest.TestCase):
    def test_z_cycle_three_and_four_actions(self):
        for k,l in itertools.product(range(-3,4), repeat=2):
            self.assertEqual(cycle_character(k+l), cycle_character(k)*cycle_character(l))
            self.assertEqual(mmul(boost_loop(k),boost_loop(l)),boost_loop(k+l))
            self.assertEqual(det(boost_loop(k)), ONE)
            v=(Fraction(3,2),Fraction(4,3),Fraction(-2,5),Fraction(9,7))
            self.assertEqual(minkowski(coordinates(congruence(boost_loop(k),hermitian(*v)))),
                             minkowski(v))
        self.assertEqual(cycle_character(3),Omega3(1))
        self.assertNotEqual(boost_loop(3),boost_loop(0))

    def test_three_phase_into_five_gns_positive_kernel(self):
        idx=(-2,0,1,3,5)
        kernel=cubic_loop_kernel(idx,Fraction(2,3))
        for i,j in itertools.product(range(len(idx)),repeat=2):
            expected=Omega3(Fraction(2,3)**abs(idx[j]-idx[i])) * cycle_character(idx[j]-idx[i])
            self.assertEqual(kernel[i][j],expected)
            self.assertEqual(kernel[i][j].conjugate(),kernel[j][i])
        self.assertEqual(cubic_loop_kernel([0,1],2)[0][1],Omega3(2)*cycle_character(1))
        with self.assertRaises(TypeError): cycle_character(Fraction(1,2))


class FiveGateExactTests(unittest.TestCase):
    def test_toeplitz_exact_factorization_and_full_rank(self):
        # Independent matrix expansion, elimination, and closed determinant.
        for rho in (Fraction(0), Fraction(1, 2), Fraction(3, 5), Fraction(-1, 3)):
            for n in range(1, 9):
                b, d = ar1_factorization(n, rho)
                gram = [[rho ** abs(i-j) for j in range(n)] for i in range(n)]
                for i,j in itertools.product(range(n),repeat=2):
                    value = sum((b[i][k]*d[k]*b[j][k] for k in range(n)),Fraction(0))
                    self.assertEqual(value, gram[i][j])
                expected = (1-rho*rho)**(n-1)
                self.assertEqual(rational_determinant(gram), expected)
                if abs(rho) < 1:
                    self.assertGreater(expected, 0)

    def test_loop_kernel_unitary_twist_preserves_gram(self):
        indices = (-3, -1, 0, 2, 8)
        rho = Fraction(2, 5)
        k0, k1 = loop_kernel(indices, rho), loop_kernel(indices, rho, 1)
        phases = (GaussQ(1),GaussQ(0,1),GaussQ(-1),GaussQ(0,-1))
        for i,j in itertools.product(range(len(indices)),repeat=2):
            self.assertEqual(k1[i][j], k0[i][j]*phases[(indices[j]-indices[i])%4])
            self.assertEqual(k1[j][i], k1[i][j].conjugate())
        # Nonconsecutive Gram is a principal submatrix of a larger positive Gram.
        with self.assertRaises(TypeError): loop_kernel((0,Fraction(1,2)))

    def test_bad_rho_and_rank_collapse_counterexamples(self):
        rank1=loop_kernel((0,1,2,3), Fraction(1))
        self.assertTrue(all(v == GaussQ(1) for row in rank1 for v in row))
        nonpsd=loop_kernel((0,1), Fraction(2))
        self.assertEqual(nonpsd, ((GaussQ(1), GaussQ(2)),(GaussQ(2),GaussQ(1))))
        self.assertEqual(rational_determinant([[1,2],[2,1]]), -3)
        with self.assertRaises(ValueError): ar1_factorization(0, Fraction(1,2))

    def test_positive_form_requires_parallelogram_and_completeness(self):
        for v,w in [((1,0),(0,1)),((2,3),(-5,7)),((0,0),(2,3))]:
            self.assertEqual(parallelogram_defect(v,w,"l2"), 0)
        self.assertEqual(parallelogram_defect((1,0),(0,1),"l1"), 4)
        self.assertEqual(minkowski((0,1,0,0)), -1)
        # c_00 and its l2 completion share every finite inner product, but
        # c_00 omits the convergent l2 vector (2^-n)_n: completeness is extra.
        self.assertEqual(sum((Fraction(1,4)**n for n in range(12)),Fraction()),
                         (1-Fraction(1,4)**12)/Fraction(3,4))

    def test_source_blind_rank_one_cocycle_on_actual_and_counterseed(self):
        for phases in (bbp_residue_prefix(9, 0),
                       bbp_residue_prefix(9, Fraction(1,16)),
                       [Fraction(0)] * 10):
            e = exact_phase_cocycle(phases)
            for i,j,k in itertools.product(range(10),repeat=3):
                self.assertEqual((e[i][j]+e[j][k])%1, e[i][k])
            self.assertTrue(all(e[i][i] == 0 for i in range(10)))
        # Source and rational counterseed alias from n>=1 yet share this PSD law.
        self.assertEqual(bbp_residue_prefix(9)[1:],bbp_residue_prefix(9,Fraction(1,16))[1:])


if __name__ == "__main__":
    unittest.main()
