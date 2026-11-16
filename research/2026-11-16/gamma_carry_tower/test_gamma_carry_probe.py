"""Focused source/gluing/finite-Gamma calibrations. No asymptotic pi inference."""
import unittest
from fractions import Fraction
from math import exp, pi
from gamma_carry_probe import (
    forcing, sigma, bit_carry_add, negbin_mod4, gamma_on_sigma,
    spectral_sigma, metric_sq, tower_metric_sq, lowmode_norm,
    branch_step, exact_orbit, refractory_length_reference, refractory_experiment,
)

class GammaCarryTests(unittest.TestCase):
    def test_cocycle_composition(self):
        for a in range(2):
            for b in range(2):
                for ap in range(2):
                    for bp in range(2):
                        x,y=bit_carry_add(a,b,ap,bp)
                        self.assertEqual((a+2*b+ap+2*bp)%4, x+2*y)

    def test_cocycle_sign(self):
        for c in range(4):
            for d in range(4):
                self.assertEqual(sigma(c+d),sigma(c)*sigma(d)*(-1)**((c%2)*(d%2)))

    def test_nonsplit_extension(self):
        self.assertFalse(any((2*x)%4==0 and x%2==1 for x in range(4)))

    def test_sign_characters(self):
        for c in range(4):
            self.assertAlmostEqual(sigma(c),((1+1j)*(1j)**c).real)

    def test_gamma_probability(self):
        for a in range(0,8):
            p=negbin_mod4(a)
            self.assertEqual(sum(p),1)
            self.assertTrue(all(x>=0 for x in p))

    def test_gamma_twist(self):
        for a in range(0,8):
            for c in range(4):
                self.assertAlmostEqual(float(gamma_on_sigma(c,a)),spectral_sigma(c,a),places=12)

    def test_gamma_shape_one(self):
        self.assertEqual(negbin_mod4(1), [Fraction(8,15),Fraction(4,15),Fraction(2,15),Fraction(1,15)])
        self.assertEqual([gamma_on_sigma(c,1) for c in range(4)], [Fraction(1,5),Fraction(-3,5),Fraction(-1,5),Fraction(3,5)])

    def test_gamma_circle_quarter_turn(self):
        # Exact 3-4-5 Gaussian rotations in shape-two Gamma cyclic character.
        z2=1/(2-1j)**2
        z3=4/(3-1j)**2
        self.assertAlmostEqual(abs(z2-(3+4j)/25),0,places=12)
        self.assertAlmostEqual(abs(z3-(8+6j)/25),0,places=12)
        self.assertAlmostEqual(abs(z2*z3-2j/25),0,places=12)
        self.assertAlmostEqual(abs((1+1j)*z2-(-1+7j)/25),0,places=12)

    def test_metric_mod_four(self):
        for c in range(4):
            for d in range(4):
                q=metric_sq(2,1,c,d)
                expect=0 if c==d else 2/5 if (c-d)%4==2 else 1/5+1/9
                self.assertAlmostEqual(q,expect,places=12)

    def test_metric_bilipschitz(self):
        for m in range(1,8):
            for a in (0,.3,1,2):
                for x,y in ((0,1),(1,3),(3,7),(7,23)):
                    q=metric_sq(m,a,x,y)
                    if x%(2**m)==y%(2**m):
                        self.assertAlmostEqual(q,0,places=10)
                    else:
                        self.assertLessEqual(q,2+1e-9)
                        self.assertGreaterEqual(q,2*3**(-2*a)-1e-9)

    def test_tower_snowflake(self):
        for M in (2,3,5,8):
            for x,y,v in ((0,1,0),(1,3,1),(2,6,2),(10,18,3)):
                target=0 if v>=M else 2*(2**(-v)-2**(-M))
                self.assertAlmostEqual(tower_metric_sq(M,0,x,y),target,places=10)

    def test_spectral_gap_failure(self):
        vals=[lowmode_norm(m,1.5) for m in (3,5,8,12)]
        self.assertTrue(all(vals[j]<vals[j+1] for j in range(len(vals)-1)))
        self.assertGreater(vals[-1],0.99999)

    def test_original_forcing(self):
        self.assertEqual(forcing(1),Fraction(47,15))
        for n in range(2,200):
            self.assertGreater(forcing(n),0)
            self.assertLess(forcing(n),Fraction(15,(8*(n-1)+1)*(8*(n-1)+2)))

    def test_source_step_seam(self):
        orig=exact_orbit(128)
        for n in range(1,128):
            c=int(orig[n]);u=orig[n]-c
            cnext,unext,j,eps=branch_step(n,c,u)
            self.assertEqual(cnext,int(orig[n+1]))
            self.assertEqual(unext,orig[n+1]-cnext)
            self.assertEqual(eps,int(unext<forcing(n+1)))
            self.assertEqual(cnext,16*c+j+eps)

    def test_step_not_mod_four_closed(self):
        c0,_,_,_=branch_step(8,0,Fraction(0))
        c1,_,_,_=branch_step(8,0,Fraction(1,16))
        self.assertNotEqual(c0%4,c1%4)

    def test_refractory_positive(self):
        for n in (2,8,24,64,128,1024,4096):
            records=refractory_experiment(n)
            self.assertEqual(len(records),refractory_length_reference(n))
            self.assertTrue(all(j==0 and e==0 for _,j,e in records))

    def test_gamma_not_source_mixing(self):
        # A constant (coherent, nonnormal) signal remains constant under a unital Gamma observer.
        for a in range(0,6):
            self.assertEqual(sum(negbin_mod4(a)),1)

if __name__=='__main__': unittest.main()
