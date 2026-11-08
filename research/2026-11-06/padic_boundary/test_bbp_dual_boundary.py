"""Exact, hostile source tests; finite checks are not universal proofs."""
from fractions import Fraction
import unittest
from bbp_dual_boundary import (
    source, four_pole, first_pole_mutant, h, coboundary_mutant,
    shadow_source, isometric_coboundary_mutant, mod_fraction, v_mod, u_mod, u_exact, valuation_two, odd_branch)

class SourceGeometry(unittest.TestCase):
    def test_four_pole_compact_including_negative_indices(self):
        for z in range(-100, 101):
            self.assertEqual(source(z),four_pole(z))
            self.assertEqual(source(z).denominator % 2,1)

    def test_2adic_isometry_of_rational_forcing(self):
        for k in range(1,12):
            for z in range(-18,19):
                x, y = z, z+(1<<k)
                self.assertEqual(valuation_two(source(x)-source(y)),k)

    def test_2adic_source_is_one_lipschitz(self):
        for k in range(1,14):
            for z in (0,1,2,13,-37,127):
                self.assertEqual(mod_fraction(source(z),k),mod_fraction(source(z+2**k),k))

    def test_integrand_identity_at_exact_rational_points(self):
        for x in map(Fraction,[0, Fraction(1,9),Fraction(1,3),Fraction(1,5),Fraction(4,5),1]):
            P=-4*x**6+2*x**3+x**2+x
            rhs=x/(2*(1-2*x+2*x*x))+x/(2*(1-2*x*x))
            self.assertEqual(P/(1-16*x**8),rhs)

class DualBoundaries(unittest.TestCase):
    def test_preseen_zero_precisions_calibration(self):
        for bits in (4,8,12,16,32,64,128,256,400,1024):
            self.assertEqual(v_mod(0,bits),0)

    def test_registered_new_zero_precisions(self):
        for bits in (2048,4096):
            self.assertEqual(v_mod(0,bits),0)

    def test_registered_mutant_is_nonzero_at_the_boundary(self):
        for bits in (1,8,128):
            self.assertEqual(v_mod(0,bits,first_pole_mutant)%2,1)

    def test_source_coboundary_preserves_zero_boundary(self):
        self.assertEqual(h(0),0)
        self.assertEqual(v_mod(0,2048,coboundary_mutant),0)
        for bits in (8,64,128):
            for z in (0,1,3,13,-7):
                self.assertEqual(v_mod(z,bits,coboundary_mutant),
                    (v_mod(z,bits)+mod_fraction(h(z),bits))%(1<<bits))

    def test_v_recurrence_modulo_arbitrary_precision(self):
        for bits in (4,8,12,24,48,80,192):
            for z in (-17,-2,-1,0,1,2,8,17):
                self.assertEqual(v_mod(z+1,bits),
                    (16*v_mod(z,bits)+mod_fraction(source(z+1),bits))%(1<<bits))

    def test_forward_history_matches_unique_padic_graph(self):
        for bits in (1,2,3,4,7,11,12,17,25,64,128):
            for n in (0,1,2,3,17,257):
                self.assertEqual(v_mod(n,bits),u_mod(n,bits))

    def test_new_periodicity_k11_k12(self):
        for bits in (11,12):
            for n in (0,1,2,17,257):
                self.assertEqual(u_mod(n,bits), v_mod(n+2**bits,bits))
                self.assertEqual(v_mod(n,bits), v_mod(n+2**bits,bits))

    def test_every_residue_occurs_at_all_small_depths(self):
        for bits in range(1,11):
            vals=[v_mod(z,bits) for z in range(1<<bits)]
            self.assertEqual(len(set(vals)),1<<bits)
            self.assertEqual(vals[0],0)
            self.assertEqual(set(vals),set(range(1<<bits)))

    def test_isometric_coboundary_mutant_is_not_a_source_fingerprint(self):
        self.assertNotEqual(isometric_coboundary_mutant(1),source(1))
        for bits in (1,2,4,8,16,64,2048):
            self.assertEqual(v_mod(0,bits,isometric_coboundary_mutant),0)
        for bits in range(1,9):
            vals=[v_mod(z,bits,isometric_coboundary_mutant) for z in range(1<<bits)]
            self.assertEqual(set(vals),set(range(1<<bits)))
        for n in range(0,21):
            self.assertEqual(u_exact(n,r=isometric_coboundary_mutant),u_exact(n)+2*h(n))

    def test_source_only_shadow_real_nonnormal_but_padic_haar(self):
        for n in range(0,15):
            self.assertEqual(u_exact(n,r=shadow_source), h(n))
        for bits in range(1,8):
            vals=[v_mod(z,bits,shadow_source) for z in range(1<<bits)]
            self.assertEqual(set(vals),set(range(1<<bits)))
            self.assertEqual(v_mod(0,bits,shadow_source),0)
        self.assertLess(h(10000),Fraction(1,100000000))

    def test_real_coboundary_finite_tails(self):
        for n in (0,1,3,8):
            for depth in (1,2,3,7):
                delta=sum((Fraction(1,16**j)*
                    (coboundary_mutant(n+j)-source(n+j))
                    for j in range(1,depth+1)),Fraction())
                self.assertEqual(delta, Fraction(1,16**depth)*h(n+depth)-h(n))

    def test_real_coboundary_orbit_exact(self):
        for n in range(0,21):
            self.assertEqual(u_exact(n,r=coboundary_mutant), u_exact(n)+h(n))

class ParityAnalogy(unittest.TestCase):
    def test_odd_2x_plus_one_four_steps_conjugate(self):
        for m in (1,3,5,33,-1):
            for t in (0,1,4,10):
                self.assertEqual(odd_branch(m,t)+1,(2**t)*(m+1))
            self.assertEqual(odd_branch(m,4)+1,16*(m+1))

    def test_real_and_padic_seed_difference_opposite(self):
        for n in (0,1,2,10,40):
            seed=Fraction(1,5)
            # Source cancels in difference; real circle always sees 1/5.
            self.assertEqual((16**n*seed)%1,seed)
            self.assertEqual(valuation_two(16**n*seed),4*n)
        for bits in (4,8,12,40,128):
            n=(bits+3)//4
            self.assertEqual(u_mod(n,bits,Fraction(1,5)), u_mod(n,bits))

if __name__=="__main__": unittest.main()
