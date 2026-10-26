"""Hostile exact algebra and independent numeric checks for the 4-point lift."""
from fractions import Fraction as Q
from math import gcd
import random
import unittest
import mpmath as mp
import sympy as sp

from observational_succ.seinfeld_four_point import (
    Golden,LAMBDA_GOLD,rat,cross_ratio,projective_transform,
    legendre_j,anharmonic_orbit,weierstrass_j,
    oriented_triangle_boundary,tetrahedral_face_syzygy,
    source_fourth_point,torsion_fiber_exponents,elliptic_four_torsion_pairing,
)
from observational_succ.four_point_kronecker import (
    imaginary_period,eta_imaginary,kronecker_finite_part,
    epstein_poisson,cusp_remainder,golden_signature,workdps,
)

class ProjectiveGoldenAndSource(unittest.TestCase):
    def test_exact_golden_field_and_projective_moduli(self):
        g=LAMBDA_GOLD
        self.assertEqual(g*g+g,Golden(1))
        self.assertEqual(1/g,1+g)
        self.assertEqual(g.conjugate(),Golden(-1,-1))
        self.assertEqual(g.norm(),Q(-1))
        self.assertEqual(legendre_j(g),Golden(2048))
        self.assertEqual(legendre_j(1-g),Golden(2048))
        self.assertEqual(len(set(anharmonic_orbit(g))),6)
        self.assertTrue(all(legendre_j(x)==Golden(2048) for x in anharmonic_orbit(g)))
        self.assertEqual(weierstrass_j(-30,25),Q(2048))
        with self.assertRaises(ValueError):legendre_j(0)
        with self.assertRaises(ValueError):legendre_j(1)
        with self.assertRaises(TypeError):rat(.5)

    def test_fourpoint_crossratio_is_mobius_invariant(self):
        self.assertEqual(cross_ratio(None,0,1,Q(3,5)),Q(3,5))
        rng=random.Random(107)
        samples=(None,Q(0),Q(1),Q(3,5))
        for _ in range(250):
            a,b,c,d=(rng.randrange(-7,8) for _ in range(4))
            if a*d-b*c==0:continue
            transformed=tuple(projective_transform(x,a,b,c,d) for x in samples)
            self.assertEqual(cross_ratio(*samples),cross_ratio(*transformed))
        with self.assertRaises(ValueError):cross_ratio(None,0,0,1)
        with self.assertRaises(ValueError):projective_transform(1,1,2,2,4)

    def test_source_fourth_point_and_sixfold_j_alias(self):
        x=source_fourth_point(1)
        self.assertEqual(x['unwrapped_state'],Q(47,15))
        self.assertEqual(x['circle_phase'],Q(2,15))
        self.assertNotEqual(x['j_invariant'],Q(2048))
        self.assertEqual(x['source'],'Q:Coherent-Main-X-four-pole-BBP')
        self.assertFalse(x['normality_proved'])
        for n in range(1,20):
            x=source_fourth_point(n)
            self.assertTrue(Q(0)<x['circle_phase']<Q(1))
            for variant in anharmonic_orbit(x['circle_phase']):
                self.assertEqual(legendre_j(variant),x['j_invariant'])
        with self.assertRaises(ValueError):source_fourth_point(0)

    def test_tetrahedral_null_syzygy_adds_only_two_independent_cycles(self):
        t=tetrahedral_face_syzygy()
        self.assertEqual(t['edge_boundary'],{})
        self.assertEqual((t['cycle_rank_triangle'],t['cycle_rank_tetrahedron']),(1,3))
        edge_basis=tuple((i,j) for i in range(4) for j in range(i+1,4))
        rows=[]
        for _,face in t['faces']:
            b=oriented_triangle_boundary(face)
            rows.append([b.get(edge,0) for edge in edge_basis])
        self.assertEqual(sp.Matrix(rows).rank(),3)
        with self.assertRaises(ValueError):oriented_triangle_boundary((0,0,1))

    def test_16_inverse_labels_are_not_isomorphic_groups(self):
        t=torsion_fiber_exponents()
        self.assertEqual(t['circle_fiber_size'],t['elliptic_4torsion_size'])
        self.assertIn(16,t['circle_element_orders'])
        self.assertNotIn(16,t['elliptic_element_orders'])
        self.assertEqual(max(t['elliptic_element_orders']),4)
        self.assertFalse(t['group_identification_proved'])

    def test_sixteen_symplectic_weyl_labels_not_a_cyclic_base16_clock(self):
        torsion=[(a,b) for a in range(4) for b in range(4)]
        self.assertEqual(len(torsion),16)
        self.assertTrue(all(elliptic_four_torsion_pairing(v,v)==0 for v in torsion))
        self.assertTrue(all(elliptic_four_torsion_pairing(v,w)==
            (-elliptic_four_torsion_pairing(w,v))%4 for v in torsion for w in torsion))
        self.assertTrue(all(any(elliptic_four_torsion_pairing(v,w)!=0 for w in torsion)
            for v in torsion if v!=(0,0)))
        # A finite exact ququart Weyl system; 16 mutually orthogonal operator labels.
        X=sp.zeros(4); Z=sp.zeros(4)
        for t in range(4):
            X[(t+1)%4,t]=1
            Z[t,t]=sp.I**t
        self.assertEqual(Z*X,sp.I*X*Z)
        W={(a,b):(X**a)*(Z**b) for a,b in torsion}
        for key,A in W.items():
            for other,B in W.items():
                self.assertEqual(sp.trace(A*B.conjugate().T),4 if key==other else 0)
        with self.assertRaises(ValueError):elliptic_four_torsion_pairing((1,),(0,1))

    def test_lattes_double_and_fourfold_degrees(self):
        x=sp.symbols('x')
        A=-30;B=25
        D2=sp.cancel((x**4-2*A*x*x-8*B*x+A*A)/(4*(x**3+A*x+B)))
        self.assertEqual(sp.degree(sp.fraction(D2)[0],x),4)
        D4=sp.cancel(D2.subs(x,D2))
        numerator,denominator=sp.fraction(D4)
        self.assertEqual(sp.degree(numerator,x),16)
        self.assertEqual(sp.degree(denominator,x),15)
        self.assertEqual(sp.cancel(D2.subs(x,Q(0))),9)
        # Degree equality with z^16 is only a numerical coincidence
        # of inverse fiber sizes, not a Möbius conjugacy.

    def test_all_lower_four_bit_masks_can_hide_top_parity(self):
        even=tuple(x for x in range(16) if x.bit_count()%2==0)
        coeff=[sum((-1)**((x&mask).bit_count()%2) for x in even)/len(even)
               for mask in range(16)]
        self.assertEqual(coeff[0],1)
        self.assertEqual(coeff[-1],1)
        self.assertEqual(coeff[1:15],[0]*14)

class KroneckerBoundaryTests(unittest.TestCase):
    def test_gold_kronecker_and_square_difference_via_two_routes(self):
        with workdps(55):
            g=golden_signature(55,70)
            self.assertEqual(int(g['j_exact_numerically']),2048)
            self.assertAlmostEqual(float(g['period_y']),.8962561123260153,places=13)
            y=g['period_y']
            fp1=kronecker_finite_part(y,70)
            fp2=kronecker_finite_part(1,70)
            self.assertTrue(abs((fp1-fp2)-g['square_reference_difference']) < mp.mpf('1e-45'))
            self.assertTrue(abs(g['gamma_subtracted_from_lambda']-mp.mpf('0.040818323848361987598074744283235686678')) < mp.mpf('1e-35'))
            e=mp.mpf('0.0005')
            v1=epstein_poisson(y,1+e,10)-mp.pi/e
            v2=epstein_poisson(y,1+e/2,10)-2*mp.pi/e
            self.assertTrue(abs(2*v2-v1-fp1)<mp.mpf('1e-6'))
            self.assertFalse(g['normality_proved'])

    def test_cusp_finite_part_and_exponential_error(self):
        with workdps(65):
            for y in (mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf(6)):
                witness=cusp_remainder(y,100)
                self.assertGreater(witness['positive_difference'],0)
                self.assertLess(witness['positive_difference'],witness['explicit_upper'])
            a=cusp_remainder(4,100)
            self.assertLess(a['positive_difference'],mp.mpf('2e-10'))

    def test_period_and_kronecker_inputs_are_typed(self):
        with self.assertRaises(ValueError):imaginary_period(0)
        with self.assertRaises(ValueError):imaginary_period(1)
        with self.assertRaises(ValueError):imaginary_period(Q(-1,3))
        with self.assertRaises(TypeError):imaginary_period(.5)
        with self.assertRaises(ValueError):cusp_remainder(-1)
        with self.assertRaises(ValueError):eta_imaginary(1,1)

if __name__=='__main__':unittest.main()
