"""Independent exact modulo transport and non-unitarity controls."""
import unittest
from fractions import Fraction as Q
from math import gcd
from observational_succ.zero_centered_fucc import (
    modulus_transport,prime_power_drop,dilation_weight_ratio,
    additive_weight_ratio,composition,PullbackError)


class ZeroCenteredFUCCTests(unittest.TestCase):
    def test_modulus_transport_grid(self):
        for q in (2,3,5,6,7):
            for n in (2,3,4,5,6,8,9,12,16,25):
                for k in range(1,30):
                    r=modulus_transport(k,n,q)
                    self.assertTrue(r["exact"])
                    self.assertEqual(r["reduced_modulus"],n//gcd(n,q))
                    self.assertEqual(r["original_value"],Q((q*k)%n,n))
                    self.assertEqual(r["original_value"],r["reduced_value"])

    def test_authentic_prime_power_ladder(self):
        for p in (2,3,5,7):
            for a in range(1,5):
                for k in range(1,13):
                    self.assertEqual(prime_power_drop(p,a,k),
                                     Q(k%(p**(a-1)),p**(a-1)))

    def test_non_unitary_norm_ratios(self):
        for q in (2,3,5):
            ratio=[dilation_weight_ratio(k,q) for k in (1,2,10,100,1000)]
            self.assertTrue(all(x<y for x,y in zip(ratio,ratio[1:])))
            self.assertTrue(all(x<Q(q*q) for x in ratio))
            self.assertTrue(composition(5,2,q)["affine_carrier_identity"])
        self.assertEqual(additive_weight_ratio(1),3)
        self.assertLess(additive_weight_ratio(100),3)

    def test_bad_inputs_and_fake_prime_rejected(self):
        for test in (lambda:modulus_transport(0,2,3),
                     lambda:modulus_transport(1,1,3),
                     lambda:prime_power_drop(2,17,1),
                     lambda:prime_power_drop(6,2,1)):
            with self.assertRaises(PullbackError):
                test()


if __name__=="__main__":
    unittest.main()
