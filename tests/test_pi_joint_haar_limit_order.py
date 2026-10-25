"""Local-Haar multiplier and genuinely noncommuting limit theorem controls.

The limit theorem is a PAPER proof; finite computation checks distinct
Ramanujan/shell routes, never infers an infinite limit by fitting samples.
"""
from __future__ import annotations

import cmath
from fractions import Fraction as Q
from math import pi
import unittest

from observational_succ.pi_joint_prime_carrier import (
    forcing, local_primary, primes_through, joint_primary,
    ramanujan_prime_power_mean, forcing_local_haar_character,
    forcing_haar_shell_oracle, forcing_haar_product,
)


class AdelicHaarLimitOrder(unittest.TestCase):
    def test_ramanujan_exact_formula_with_independent_finite_exponential_oracle(self):
        for p in (3,5,7,11,13):
            for k in (1,2,3):
                modulus=p**k
                for h in (0,1,2,p,p*p,2*p**2):
                    mean=ramanujan_prime_power_mean(p,k,h)
                    values=[cmath.exp(2j*pi*(h*u%modulus)/modulus)
                            for u in range(modulus) if u%p]
                    finite=sum(values)/len(values)
                    self.assertLess(abs(finite-float(mean)),1e-11)

    def test_local_forcing_haar_two_independent_exact_derived_routes(self):
        for p in (7,11,13,17,19,23,31):
            for h in (0,1,-1,2,3,p,p*p,2*p*p,p*p*p,17):
                formula=forcing_local_haar_character(p,h)
                oracle=forcing_haar_shell_oracle(p,h)
                self.assertEqual(formula,oracle)
                self.assertGreater(formula,0)
                self.assertLessEqual(formula,1)
        self.assertEqual(forcing_local_haar_character(7,1),Q(17,49))
        self.assertEqual(forcing_local_haar_character(11,1),Q(73,121))
        self.assertEqual(forcing_local_haar_character(13,1),Q(113,169))
        self.assertEqual(forcing_local_haar_character(7,7),Q(311,343))

    def test_finite_independent_haar_product_strict_decay(self):
        ps=[7,11,13,17,19,23,29,31,37,41]
        products=[forcing_haar_product(ps[:k],1) for k in range(len(ps)+1)]
        self.assertEqual(products[0],1)
        self.assertEqual(products[1],Q(17,49))
        self.assertTrue(all(0<products[k+1]<products[k] for k in range(len(ps))))
        self.assertEqual(forcing_haar_product(ps,0),1)
        # A too-strong guessed threshold 1/30 was refuted: exact product
        # is 9327351230426029199 / 234295420524634222039 ~= 0.03981.
        # Preserve the adverse calibration and assert the correct <1/20.
        self.assertGreater(products[-1],Q(1,30))
        self.assertLess(products[-1],Q(1,20))

    def test_actual_forcing_has_small_real_tail_not_a_haar_mean(self):
        for n in range(1,1301):
            val=forcing(n)
            self.assertTrue(0<val<Q(8,n*n))
            # The rational pointwise full product must be the true r(n).
            if n<=64:
                self.assertEqual(sum((v for _,v in joint_primary(val)),Q())%1,val%1)
        # Full character e(h*r(n)) tends to 1; no finite truncation can
        # substitute this for a Haar-average product at growing prime cutoffs.
        self.assertNotEqual(forcing_local_haar_character(7,1),Q(1))

    def test_fixed_prime_sampling_agrees_with_local_haar_limit_as_noncertifying_oracle(self):
        # Sampling residue representatives modulo p^K is not an exact Haar
        # quadrature at poles: their deeper digits remain unobserved.
        # The error shrinks; exact theorem comes from the shell proof.
        for p,h,k in ((7,1,5),(7,7,4),(11,1,4),(13,1,3)):
            M=p**k
            sampled=sum(cmath.exp(2j*pi*float((h*local_primary(forcing(n),p))%1))
                        for n in range(1,M+1))/M
            truth=float(forcing_local_haar_character(p,h))
            self.assertLess(abs(sampled-truth),Q(8,p**((k+1)//2)))

    def test_domains(self):
        bad=[lambda:forcing_local_haar_character(3,1),
             lambda:forcing_haar_shell_oracle(5,1),
             lambda:forcing_local_haar_character(7,0.5),
             lambda:ramanujan_prime_power_mean(7,0,1),
             lambda:ramanujan_prime_power_mean(9,1,1)]
        for fn in bad:
            with self.assertRaises(ValueError):fn()

if __name__=='__main__':unittest.main()
