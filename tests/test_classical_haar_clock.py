"""Exact independent fiber and Haar tower tests, including nonunit counterexamples."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import unittest

from observational_succ.classical_unit_origin import ClassicalOriginError
from observational_succ.classical_haar_clock import (
    PrimeHaarClock, classical_haar_clock_probe, condition, haar_inner,
    image_energy, multiply_observable, multiplier_operator_norm_squared,
    p_adic_size_of_uniform_atom, pullback, succ_observable,
)


class HaarTowerTests(unittest.TestCase):
    def test_exact_uniform_cylinder_isometry_and_adjoint(self):
        for p, lowr in ((2,1), (2,2), (2,3), (3,1), (3,2), (5,1)):
            for chart in ("n_minus_one", "one_minus_n"):
                lo = PrimeHaarClock(p, lowr, chart)
                hi = PrimeHaarClock(p, lowr+1, chart)
                f = tuple(Q(j % 5 - 2, 3) for j in range(lo.size))
                g = tuple(Q(j % 7 - 3, 5) for j in range(hi.size))
                pf, eg = pullback(lo, hi, f), condition(hi, lo, g)
                self.assertEqual(haar_inner(hi, pf, pf), haar_inner(lo, f, f))
                self.assertEqual(haar_inner(hi, pf, g), haar_inner(lo, f, eg))
                self.assertEqual(condition(hi, lo, pf), f)
                projected = pullback(lo, hi, eg)
                self.assertEqual(haar_inner(hi, projected, projected),
                                 haar_inner(lo, eg, eg))
                self.assertEqual(condition(hi, lo, projected), eg)

    def test_actual_source_affine_actions_descend_and_cohere(self):
        for p, r, chart in product((2, 3, 5), (1, 2), ("n_minus_one", "one_minus_n")):
            lo, hi = PrimeHaarClock(p, r, chart), PrimeHaarClock(p, r+1, chart)
            f = tuple(Q((j*3)%7-2, 5) for j in range(lo.size))
            pf = pullback(lo, hi, f)
            for m, step in product((1, 2, 3, 4, 6), (0, 1, 3)):
                self.assertEqual(pullback(lo, hi, multiply_observable(lo, f, m)),
                                 multiply_observable(hi, pf, m))
                self.assertEqual(pullback(lo, hi, succ_observable(lo, f, step)),
                                 succ_observable(hi, pf, step))
                # Koopman representation reverses source-map composition order.
                u_m = multiply_observable(hi, pf, m)
                self.assertEqual(succ_observable(hi, u_m, step),
                                 multiply_observable(hi, succ_observable(hi, pf, m*step), m))

    def test_multiplier_norm_fibers_and_unitary_vs_nonunit(self):
        for p,r in ((2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2)):
            for chart in ("n_minus_one", "one_minus_n"):
                level = PrimeHaarClock(p, r, chart)
                f = tuple(Q((i*7)%11-5, 5) for i in range(level.size))
                for m in range(1, 2*p+2):
                    outputs = [level.multiplier(x,m) for x in range(level.size)]
                    counted = tuple(outputs.count(y) for y in range(level.size))
                    self.assertEqual(level.fibers(m), counted)
                    self.assertEqual(len(level.image(m)), level.size//gcd(m,level.size))
                    self.assertEqual(multiplier_operator_norm_squared(level,m),gcd(m,level.size))
                    norm_out = haar_inner(level, multiply_observable(level,f,m),
                                          multiply_observable(level,f,m))
                    self.assertEqual(norm_out,gcd(m,level.size)*image_energy(level,f,m))
                    if gcd(m,level.size)==1:
                        self.assertEqual(norm_out,haar_inner(level,f,f))
                    # At nonunits the map is not necessarily isometric, but
                    # this is a verified exact support/energy identity.

    def test_conditional_expectation_fails_for_nonunit_multiplier(self):
        low, high = PrimeHaarClock(2,1), PrimeHaarClock(2,2)
        delta_one = (Q(0),Q(1),Q(0),Q(0))
        lhs = condition(high,low,multiply_observable(high,delta_one,2))
        rhs = multiply_observable(low,condition(high,low,delta_one),2)
        self.assertEqual(lhs,(Q(1),Q(0)))
        self.assertEqual(rhs,(Q(1,2),Q(1,2)))
        self.assertNotEqual(lhs,rhs)
        for m in (1,3,5,7):
            self.assertEqual(condition(high,low,multiply_observable(high,delta_one,m)),
                             multiply_observable(low,condition(high,low,delta_one),m))

    def test_raw_counting_norm_and_Qp_valuation_are_different(self):
        lo,hi = PrimeHaarClock(3,1),PrimeHaarClock(3,2)
        f=(Q(1),Q(2),Q(-1))
        pf=pullback(lo,hi,f)
        rawlo=sum(x*x for x in f)
        rawhi=sum(x*x for x in pf)
        self.assertEqual(rawhi,3*rawlo) # without Haar normalization not isometric
        self.assertEqual(haar_inner(lo,f,f),haar_inner(hi,pf,pf))
        self.assertEqual([p_adic_size_of_uniform_atom(PrimeHaarClock(2,r)) for r in (1,2,3)],
                         [2,4,8]) # Qp-valued atom p^-r has UNBOUNDED p-adic norm

    def test_source_guards_and_certified_receipt(self):
        for args in ((4,1),(1,2),(2,0),(2,20),(True,1)):
            with self.assertRaises(ClassicalOriginError):
                PrimeHaarClock(*args)
        low, high=PrimeHaarClock(2,1),PrimeHaarClock(3,2)
        with self.assertRaises(ClassicalOriginError):
            pullback(low,high,(1,2))
        with self.assertRaises(ClassicalOriginError):
            haar_inner(low,(0.0,1),(1,1))
        with self.assertRaises(ClassicalOriginError):
            multiply_observable(low,(1,1),0)
        receipt=classical_haar_clock_probe()
        self.assertTrue(receipt['nonunit_multiplication_breaks_conditional_commutation'])
        self.assertFalse(receipt['global_weil_positivity_or_RH_proved'])


if __name__ == '__main__':
    unittest.main()
