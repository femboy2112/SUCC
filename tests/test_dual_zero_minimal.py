"""Exact cyclic Fourier/Cayley smoke tests. No pi normality claim."""
import sys,unittest
from fractions import Fraction as F
from pathlib import Path
from sympy import Poly,Symbol,totient
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research/2026-11-04/dual_zero_real_carrier'))
from zero_minimal import source,phase,cayley,tangent_minpoly,degree_for_phase,reciprocal_source_phase,zero_projectors,even_odd_tangent_polys,tangent16,tangent_add,source_real_step

def mult(z,w):
    a,b=z;c,d=w
    return (a*c-b*d,a*d+b*c)
def power(z,n):
    y=(F(1),F(0))
    for _ in range(n):y=mult(y,z)
    return y

class SourceRealZero(unittest.TestCase):
    def test_authentic_poles_and_primal(self):
        self.assertEqual(source(1),F(47,15))
        self.assertEqual(source(1,True),F(109,35))
    def test_selected_odd_phases_and_degree(self):
        self.assertEqual(phase(1),F(2,15))
        self.assertEqual(phase(1,True),F(4,35))
        self.assertEqual(degree_for_phase(phase(1)),8)
        self.assertEqual(degree_for_phase(phase(1,True)),24)
    def test_wrong_rational_cayley_phase(self):
        self.assertEqual(cayley(F(4,35)),(F(1209,1241),F(280,1241)))
    def test_rational_circle_reciprocal(self):
        for t in (F(1,2),F(2,3),F(-3,5),F(8,13)):
            a,b=cayley(t)
            self.assertEqual(a*a+b*b,1)
            self.assertEqual(cayley(1/t),(-a,b))
    def test_dual_zero_projectors(self):
        for M in (3,5,15,35):
            p,q=zero_projectors(M)
            self.assertEqual(p*q*p,p/M)
            self.assertEqual((p*q).trace(),F(1,M))
            self.assertNotEqual(p*q,q*p)
    def test_cyclotomic_tangent_degree(self):
        for M in (3,5,7,9,15,35):
            p=tangent_minpoly(M)
            self.assertEqual(p.degree(),int(totient(M)))
            self.assertTrue(p.is_irreducible)
    def test_even_halfturn(self):
        self.assertEqual(reciprocal_source_phase(F(4,35)),F(27,70))
    def test_rational_forced_tangent_map(self):
        for t,s in ((F(1,3),F(1,7)),(F(-1,4),F(2,3)),(F(1,5),F(-1,8))):
            self.assertEqual(cayley(source_real_step(t,s)),mult(power(cayley(t),16),cayley(s)))
    def test_irrational_nonnormal_fixed_points(self):
        A,B=even_odd_tangent_polys();t=Symbol('t')
        Q=Poly(B.as_expr()-t*A.as_expr(),t)
        for M in (3,5,15):
            p=tangent_minpoly(M)
            self.assertEqual(Q.rem(Poly(p.as_expr().subs(Symbol('T'),t),t)),Poly(0,t))
    def test_algebraic_degree_does_not_force_haar(self):
        self.assertEqual((16*F(1,5))%1,F(1,5))
        self.assertEqual(degree_for_phase(F(1,5)),4)
if __name__=='__main__':unittest.main()
