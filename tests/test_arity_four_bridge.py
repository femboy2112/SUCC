"""Exact source-independent algebra plus authentic BBP adapter cross-check."""
from __future__ import annotations

import importlib.util
import itertools
import random
import unittest
from fractions import Fraction

from observational_succ.arity_four_bridge import (
    GaussQ, Omega3, OMEGA, OMEGA_POWERS, IDENTITY, I, ONE,
    bbp_forcing, bbp_residue_prefix, congruence, coordinates,
    dagger, det, gauge_link, hermitian, hilbert_schmidt,
    matrix, minkowski, mmul, trace, triad_boundary, triad_defect,
    triad_mode, triad_sum_identity, wilson_triangle,
)


class TriadExactTests(unittest.TestCase):
    def test_primitive_cube_root(self):
        self.assertEqual(OMEGA * OMEGA, OMEGA_POWERS[2])
        self.assertEqual(OMEGA * OMEGA_POWERS[2], Omega3(1))
        self.assertEqual(sum(OMEGA_POWERS, Omega3()), Omega3())
        self.assertEqual(OMEGA.conjugate(), OMEGA_POWERS[2])
        self.assertEqual(OMEGA * OMEGA.conjugate(), Omega3(1))

    def test_sliding_defect_exhaustive(self):
        for z in itertools.product((-1, 0, 1), repeat=4):
            for k in (0, 1, 2, 3, -1):
                exact = OMEGA_POWERS[(2*k) % 3] * (z[3] - z[0])
                self.assertEqual(triad_defect(z, k), exact, (z, k))

    def test_window_sum_exhaustive(self):
        for length in (3, 4, 5, 6):
            for z in itertools.product((0, 1), repeat=length):
                for k in range(3):
                    lhs, rhs = triad_sum_identity(z, k)
                    self.assertEqual(lhs, rhs, (z, k))
                    if k:
                        self.assertEqual(lhs, triad_boundary(z, k))

    def test_spurious_cancellation_on_nonnormal_constant(self):
        z = [1] * 100
        self.assertEqual(triad_sum_identity(z, 1)[0], Omega3())
        self.assertEqual(triad_sum_identity(z, 2)[0], Omega3())
        self.assertEqual(triad_sum_identity(z, 0)[0], Omega3(3 * 98))

    def test_arithmetic_source_exact_cyclotomic_triads(self):
        samples = bbp_residue_prefix(12)
        for k in range(3):
            a, b = triad_sum_identity(samples, k)
            self.assertEqual(a, b)
            for i in range(10):
                self.assertEqual(triad_defect(samples[i:i+4], k),
                    OMEGA_POWERS[(2*k)%3] * (samples[i+3]-samples[i]))

    def test_refuse_malformed_windows(self):
        with self.assertRaises(ValueError): triad_mode([1,2], 1)
        with self.assertRaises(ValueError): triad_defect([1,2,3], 1)
        with self.assertRaises(ValueError): triad_sum_identity([1,2], 1)


class SpinorExactTests(unittest.TestCase):
    def test_real_four_component_inverse(self):
        for t,x,y,z in itertools.product((-2,0,3), repeat=4):
            v=(t,x,y,z)
            self.assertEqual(coordinates(hermitian(*v)), tuple(map(Fraction,v)))
            self.assertEqual(det(hermitian(*v)), GaussQ(minkowski(v)))
            self.assertEqual(trace(hermitian(*v)), GaussQ(2*t))

    def test_exact_mixed_polarization(self):
        a=(2,3,-1,4); b=(-1,5,2,1)
        A, B = hermitian(*a),hermitian(*b)
        lhs=(trace(A)*trace(B)-trace(mmul(A,B)))
        expected=2*(a[0]*b[0]-sum(a[j]*b[j] for j in range(1,4)))
        self.assertEqual(lhs, GaussQ(expected))

    def test_lorentz_action_generic_sl2_gaussian_rational(self):
        boost=matrix(2,0,0,Fraction(1,2))
        shear=matrix(1,GaussQ(Fraction(1,3), Fraction(2,5)),0,1)
        group=(IDENTITY,boost,shear,mmul(shear,boost))
        for g in group:
            self.assertEqual(det(g), ONE)
            for v in [(1,0,0,0),(3,4,-1,5),(0,0,0,1),
                      (Fraction(1,2),Fraction(-2,3),Fraction(3,7),Fraction(5,11))]:
                X=hermitian(*v)
                Y=congruence(g,X)
                self.assertEqual(dagger(Y),Y)
                self.assertEqual(det(Y),det(X))
                self.assertEqual(minkowski(coordinates(Y)),minkowski(v))

    def test_boost_coefficients_and_metric_boundary(self):
        boost=matrix(2,0,0,Fraction(1,2))
        v=coordinates(congruence(boost,hermitian(1,0,0,0)))
        self.assertEqual(v,(Fraction(17,8),Fraction(0),Fraction(0),Fraction(15,8)))
        self.assertEqual(minkowski(v),Fraction(1))
        self.assertEqual(hilbert_schmidt((1,0,0,0)),Fraction(2))
        self.assertEqual(hilbert_schmidt(v),Fraction(257,16))
        self.assertNotEqual(hilbert_schmidt(v),Fraction(2))

    def test_non_sl_det_mutant(self):
        mutant=matrix(2,0,0,1)
        X=hermitian(1,0,0,0)
        self.assertEqual(det(congruence(mutant,X)),GaussQ(4))
        self.assertNotEqual(det(congruence(mutant,X)),det(X))

    def test_nonhermitian_rejected(self):
        with self.assertRaises(ValueError): coordinates(matrix(1,1,0,1))
        with self.assertRaises(ValueError): minkowski([1,2,3])

    def test_unitary_triangle_and_gauge(self):
        ux=matrix(0,I,I,0)
        uz=matrix(I,0,0,-I)
        uy=matrix(0,1,-1,0)
        for g in (ux,uz,uy):
            self.assertEqual(det(g),ONE)
            self.assertEqual(mmul(dagger(g),g),IDENTITY)
        # Two-way walk is trivial when reverse is the inverse.
        self.assertEqual(mmul(dagger(ux),ux), IDENTITY)
        self.assertNotEqual(mmul(ux,ux), IDENTITY)  # hostile fake reverse
        edges=(IDENTITY, IDENTITY, uz)
        hol=wilson_triangle(*edges)
        self.assertEqual(trace(hol), GaussQ(0))
        frames=(ux, uy, uz)
        transformed=(gauge_link(edges[0],frames[0],frames[1]),
                     gauge_link(edges[1],frames[1],frames[2]),
                     gauge_link(edges[2],frames[2],frames[0]))
        target=congruence(frames[0],hol)
        self.assertEqual(wilson_triangle(*transformed),target)
        self.assertEqual(trace(wilson_triangle(*transformed)),trace(hol))
        self.assertEqual(wilson_triangle(IDENTITY,IDENTITY,IDENTITY),IDENTITY)


class SelectedSourceTests(unittest.TestCase):
    def test_seed_and_four_pole_transcription(self):
        self.assertEqual(bbp_residue_prefix(0), [Fraction(0)])
        self.assertEqual(bbp_forcing(1),Fraction(4)-Fraction(2,4)-Fraction(1,5)-Fraction(1,6))
        self.assertEqual(bbp_residue_prefix(1)[1],Fraction(47,15)%1)
        with self.assertRaises(ValueError): bbp_forcing(0)
        with self.assertRaises(ValueError): bbp_residue_prefix(-1)

    def test_rational_different_seed(self):
        a=bbp_residue_prefix(10,0)
        b=bbp_residue_prefix(10,Fraction(1,16))
        self.assertEqual(b[0]-a[0],Fraction(1,16))
        self.assertEqual(a[1:],b[1:])  # rational phase alias, not an origin identity

    @unittest.skipUnless(importlib.util.find_spec("observational_succ.selected_orbit"),
                         "requires full SUCC checkout")
    def test_against_canonical_selected_orbit(self):
        from observational_succ.selected_orbit import SelectedOrbit, original_forcing
        oracle=SelectedOrbit()
        for n,r in enumerate(bbp_residue_prefix(28)):
            self.assertEqual(oracle.state(n),r)
            if n:
                self.assertEqual(bbp_forcing(n),original_forcing(n))


if __name__ == "__main__":
    unittest.main()
