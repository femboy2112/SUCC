import unittest
from fractions import Fraction as F
from geometry_probe import *

class GeometryTests(unittest.TestCase):
    def test_authentic_source_and_seed(self):
        self.assertEqual(forcing(1),F(47,15))
        self.assertEqual(orbit(0),[F(0)])
        for n in (1,2,7,19,73):
            expected=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            self.assertEqual(forcing(n),expected)
    def test_positive_endpoint_normalization(self):
        for n in (1,3,7,17):
            for c in (AUTH,kernel_mutant(3),kernel_mutant(4),age_mutant(128)):
                p=endpoint_weights(n,c)
                self.assertEqual(sum(p),1)
                self.assertTrue(all(x>0 for x in p))
    def test_second_jet_formula(self):
        for z in (F(0),F(1,7),F(1,2),F(5,6),F(1)):
            zero,first,second=pgf_coefficients(z)
            self.assertEqual(first,-(z-1)*(511*z-302)/(120*(z-2)**4))
            self.assertEqual(second,(z-1)*(159826*z**3-46581*z*z-131748*z+35212)/(14400*(z-2)**6))
    def test_positive_cubic_matches_first_not_second(self):
        self.assertEqual(source_jets(AUTH,2),source_jets(kernel_mutant(3),2))
        self.assertEqual(source_jets(kernel_mutant(3),3)[3]-source_jets(AUTH,3)[3],6)
        for z in (F(0),F(1,7),F(1,2),F(5,6)):
            a=pgf_coefficients(z);b=pgf_coefficients(z,kernel_mutant(3))
            self.assertEqual(a[:2],b[:2])
            self.assertEqual(b[2]-a[2],F(1,160)*((2-z)**-4-(2-z)**-2))
    def test_quartic_evades_second_jet(self):
        self.assertEqual(source_jets(AUTH,3),source_jets(kernel_mutant(4),3))
        for z in (F(0),F(1,3),F(4,5),F(1)):
            self.assertEqual(pgf_coefficients(z),pgf_coefficients(z,kernel_mutant(4)))
        self.assertNotEqual(forcing(17),forcing(17,kernel_mutant(4)))
    def test_exact_finite_roots(self):
        self.assertEqual(root_interval(1),(F(1),F(1)))
        lo,hi=root_interval(2)
        q=F(576147,1824887)
        self.assertLessEqual(lo,q);self.assertGreaterEqual(hi,q)
    def test_rational_circle_positivity_identity(self):
        pts=[circle_unit(F(j,7)) for j in (-5,-2,0,1,4)]
        for t in (F(-2,3),F(0),F(3,5)):
            mean,disp,var=positive_lift_identity([F(1,5)]*5,pts,circle_unit(t))
            self.assertGreater(disp,0);self.assertGreater(var,0)
    def test_exact_reconstruction_forces_degeneracy(self):
        target=circle_unit(F(2,3))
        mean,disp,var=positive_lift_identity([F(1,3),F(2,3)],[target,target],target)
        self.assertEqual(mean,target);self.assertEqual(disp,0);self.assertEqual(var,0)
        with self.assertRaises(ValueError):
            positive_lift_identity([F(2),F(-1)],[target,target])
    def test_near_lift_exact_bound(self):
        for t in (F(1,3),F(1,17),F(1,257)):
            mean,disp,var=positive_lift_identity([F(1,2)]*2,[circle_unit(t),circle_unit(-t)])
            self.assertEqual(disp,2*(1-mean[0]))
            self.assertLessEqual(var,disp)
    def test_affine_commutator_source_specific_seed_blind(self):
        for c in (AUTH,age_mutant(128),kernel_mutant(3)):
            for i,j in ((1,2),(3,7),(17,31)):
                for seed in (F(0),F(1,16),F(-9,7)):
                    self.assertEqual(affine_commutator(i,j,seed,c)-seed,15*(forcing(j,c)-forcing(i,c)))
    def test_literal_carry_kept_beyond_walsh(self):
        rows=phase_and_carry(40)
        for n,(x,k) in enumerate(rows,1):
            old=F(0) if n==1 else rows[n-2][0]
            self.assertEqual(16*old+forcing(n),x+k)
            self.assertTrue(0<=x<1)
            for mask in range(16):
                self.assertIn(walsh(mask,k),(-1,1))
        self.assertEqual(walsh(2,0),1);self.assertEqual(walsh(2,6),-1)
        self.assertEqual(0%6,6%6)
    def test_tensor_normalization_and_nontrivial_dispersion(self):
        for n in (3,7,17):
            t=carry_grade_tensor(n)
            self.assertEqual(t[0][0],1)
            self.assertTrue(all(abs(x)<=1 for row in t for x in row))
            self.assertTrue(any(abs(x)<1 for x in t[0][1:]))
    def test_integer_and_eventual_aliases(self):
        a=phase_and_carry(20,F(0));b=phase_and_carry(20,F(1));c=phase_and_carry(20,F(1,16))
        self.assertEqual(a,b)
        # Initial 1/16 adds exactly one to the first literal carry, then coalesces.
        self.assertEqual(a[0][0],c[0][0]);self.assertEqual(a[0][1]+1,c[0][1]);self.assertEqual(a[1:],c[1:])
    def test_domains(self):
        with self.assertRaises(ValueError): forcing(0)
        with self.assertRaises(ValueError): kernel_mutant(3,F(-1))
        with self.assertRaises(ValueError): pgf_coefficients(F(1,2),((0,F(1)),))

if __name__=='__main__':unittest.main()
