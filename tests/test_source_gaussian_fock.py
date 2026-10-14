"""Stdlib focused rational checks; full analytic theorems have paper proofs."""
import unittest
from fractions import Fraction as Q
from observational_succ.source_gaussian_fock import (
    B2,C0,R0,SourceGaussianError,zero_disk,xi_prime_interval,
    source_tube,even_fock_tail,rouche,finite_ambiguity,receipt,
    exp_interval,pi_interval,even_gaussian_kernel_interval,
)
class SourceGaussianTests(unittest.TestCase):
    def test_original_source_norm(self):
        self.assertEqual(B2,Q(260,27))
        self.assertEqual(C0,Q(59,120))
    def test_original_xi_zero_disk(self):
        x=zero_disk()
        self.assertTrue(x['certified'])
        self.assertEqual(x['radius'],Q(47,100))
        self.assertLess(x['squared_remainder_upper'],x['squared_center_lower'])
        self.assertFalse(zero_disk(Q(1,2))['certified'])
    def test_exact_rational_gaussian_majorants(self):
        for x in (Q(),Q(1,4),Q(3,2)):
            lo,hi=exp_interval(x)
            self.assertLessEqual(lo,hi)
            self.assertGreater(lo,0)
        pl,ph=pi_interval()
        self.assertTrue(3<pl<ph<Q(22,7))
    def test_true_finite_prime_observations(self):
        x=xi_prime_interval(11,3)
        self.assertEqual(x['primes'],(2,3,5,7,11))
        self.assertLess(x['xi_lower'],x['xi_upper'])
        self.assertEqual(x['Euler_tail'],Q(1,242))
    def test_wrong_prime_and_missing_source(self):
        for fake in ((2,3,5,6,7,11),(2,3,7,11),(2,3,5,7,11,11)):
            with self.assertRaises(SourceGaussianError):
                xi_prime_interval(11,3,fake)
        with self.assertRaises(SourceGaussianError):
            xi_prime_interval(11,1)
    def test_reflected_gaussian_symmetry(self):
        x=even_gaussian_kernel_interval(Q(3,2),Q(5,2))
        y=even_gaussian_kernel_interval(Q(3,2),-Q(5,2))
        self.assertEqual(x,y)
    def test_prime_borehole_shrinks_evaluation_radius(self):
        x=source_tube(11,3,Q(12,5))
        self.assertLess(x['radius'],Q(1,4))
        self.assertGreater(x['unobserved_radius'],2)
        self.assertLess(x['lower'],x['upper'])
        self.assertFalse(x['RH_proved'])
    def test_exact_sample_returns_source_interval(self):
        x=source_tube(11,3,Q(5,2))
        self.assertEqual(x['radius'],0)
        self.assertLess(x['lower'],x['upper'])
    def test_rouche_zero_count_without_zero_lookup(self):
        x=rouche((Q(1),Q(-1)),Q(2),1,Q(3))
        self.assertTrue(x['certified'])
        self.assertEqual(x['zero_count'],2)
        self.assertFalse(rouche((Q(1),Q(-1)),Q(2),1,Q(7,2))['certified'])
    def test_nonuniqueness_still_source_typed(self):
        h=finite_ambiguity((Q(1),Q(2)),1)
        self.assertGreater(h['energy'],0)
        self.assertTrue(h['does_not_preserve_full_Euler_germ'])
        for x in (Q(1),Q(2)):
            self.assertEqual(sum((a*x**(2*j) for j,a in enumerate(h['coefficients'])),Q()),0)
    def test_reproducible_flags(self):
        r=receipt()
        self.assertTrue(r['zero_free_disk']['certified'])
        self.assertFalse(r['Gaussian_prior_proved_for_arithmetic'])
        self.assertFalse(r['RH_proved'])
if __name__=='__main__': unittest.main()
