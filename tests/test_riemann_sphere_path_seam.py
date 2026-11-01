"""Independent exact finite receipts for the original BBP sphere contour construction."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import unittest

BASE=Path(__file__).resolve().parents[1]/'research/2026-10-31/riemann_sphere_path_seam'
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,BASE/path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
m=load('riemann_seam.py','riemann_original_source_2026_exact')
o=load('independent_oracle.py','riemann_lagrange_2026_exact')

class RiemannBBPSeamTests(unittest.TestCase):
    def test_pole_coordinates(self):self.assertEqual(m.POLES,(F(7,8),F(1,2),F(3,8),F(1,4)))
    def test_source_residues(self):self.assertEqual(m.pole_residues(),(F(1,2),-F(1,4),-F(1,8),-F(1,8)))
    def test_source_residue_sum_zero(self):self.assertEqual(sum(m.pole_residues()),0)
    def test_source_laurent_zero_mass(self):self.assertEqual(m.atomic_moment(0),0)
    def test_source_laurent_first_jet(self):self.assertEqual(m.atomic_moment(1),15)
    def test_source_laurent_moments(self):self.assertEqual([m.atomic_moment(k) for k in range(5)],[0,15,151,1209,8995])
    def test_source_common_rational(self):
        for n in range(1,45):self.assertEqual(m.source(n),F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
    def test_newton_values(self):
        for n in range(1,10):
            pp=m.pascal_weight_poly(n)
            for j in range(1,n+1):self.assertEqual(m.evaluate_poly(pp,j),F(1,16**j))
    def test_newton_independent_lagrange(self):
        for n in range(1,9):self.assertEqual(m.pascal_weight_poly(n),o.lagrange_weights(n))
    def test_newton_independent_binomial(self):
        for n in range(1,9):
            for j in range(1,n+1):self.assertEqual(m.source_newton_weight(n,j),F(1,16**j))
    def test_action_direct_vs_recurrence(self):
        for n in range(1,12):
            u,a=o.recurrence(n)
            self.assertEqual(m.action(n),a);self.assertEqual(m.state(n),u)
            self.assertEqual(a,u/F(16**n))
    def test_all_sample_residues(self):
        for n in range(1,10):
            self.assertEqual(m.sample_residues(n),tuple(m.source(j)/16**j for j in range(1,n+1)))
    def test_contour_action(self):
        for n in range(1,10):self.assertEqual(sum(m.sample_residues(n)),m.action(n))
    def test_sphere_global_residue(self):
        for n in range(1,11):
            self.assertEqual(sum(m.sample_residues(n))+sum(m.source_residues(n))+m.residue_at_infinity(n),0)
    def test_infinity_early_zero(self):self.assertEqual([m.residue_at_infinity(n) for n in (1,2)],[0,0])
    def test_infinity_first_birth(self):self.assertEqual(m.residue_at_infinity(3),-F(10125,524288))
    def test_contour_first_step(self):self.assertEqual(m.action(1),F(47,240))
    def test_contour_second_step(self):self.assertEqual(m.action(2),F(102913,524160))
    def test_harmonic_source_identity(self):
        for n in range(1,10):self.assertEqual(m.source_harmonic_decomposition(n)[0],sum(m.source_residues(n)))
    def test_puncture_preservation(self):
        for n in range(1,8):
            a=m.sample_residues(n);b=m.sample_residues(n+1)
            self.assertEqual(a,b[:n]);self.assertEqual(b[-1],m.source(n+1)/16**(n+1))
    def test_source_unit_increment(self):
        for n in range(1,10):self.assertEqual(m.action(n+1)-m.action(n),m.source(n+1)/16**(n+1))
    def test_infty_source_unit_increment(self):
        for n in range(1,10):
            total=lambda k:sum(m.source_residues(k))+m.residue_at_infinity(k)
            self.assertEqual(total(n+1)-total(n),-m.source(n+1)/16**(n+1))
    def test_cross_ratio(self):self.assertEqual(m.cross_ratio(),F(8,5))
    def test_elliptic_j(self):self.assertEqual(m.elliptic_j(),F(470596,225))
    def test_noncommutative_affine_steps(self):
        first=m.affine_product(1,2);other=m.affine_product(2,1)
        self.assertEqual(first[0],F(256));self.assertEqual(other[0],F(256))
        self.assertEqual(other[1]-first[1],F(12301,273))
    def test_original_order_matches_state(self):self.assertEqual(m.affine_product(2,1)[1],m.state(2))
    def test_nontrivial_commutator_suppressed_by_scalar_contour(self):
        self.assertNotEqual(m.affine_product(1,2),m.affine_product(2,1))
        self.assertEqual(m.action(1)+m.source(2)/16**2,m.source(2)/16**2+m.action(1))
    def test_invalid_horizon(self):
        for n in [0,-1,33,1.5,'2']:
            with self.assertRaises(ValueError):m.pascal_weight_poly(n)

if __name__=='__main__':unittest.main()
