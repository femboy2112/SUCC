"""Independent exact arithmetic and hostile finite-height contact probes."""
import unittest
from fractions import Fraction as Q
from math import gcd

from observational_succ.borwein_abc_height import (
    HeightError, box_sum_contacts, factorization, height_error_bound,
    local_conditional_limit, mobius_sieve, partial_main,
    primitive_sum_contacts, receipt,
)


def independent_mu(n):
    if n == 1:
        return 1
    omega = 0
    for p in range(2, n+1):
        if all(p % d for d in range(2, int(p**0.5)+1)) and n % p == 0:
            omega += 1
            if n % (p*p) == 0:
                return 0
    return (-1)**omega


def brute_contacts(H, m):
    return sum(gcd(a,b)==1 and (a+b)%m==0
               for a in range(1,H+1) for b in range(1,H+1))


class HeightClockTest(unittest.TestCase):
    def test_cyclic_pair_cell_independent_bruteforce(self):
        for H in range(0,51):
            for m in range(1,85):
                expected=sum((x+y)%m==0
                             for x in range(1,H+1) for y in range(1,H+1))
                self.assertEqual(box_sum_contacts(H,m),expected,(H,m))
                deviation=abs(Q(expected)-Q(H*H,m))
                self.assertLessEqual(deviation,min(H,m-1))

    def test_mobius_is_independently_sourced(self):
        mu=mobius_sieve(700)
        self.assertEqual(mu[1],1)
        for n in range(1,701):
            self.assertEqual(mu[n],independent_mu(n),n)

    def test_primitive_pairs_exact_full_grid(self):
        for H in range(1,51):
            for m in range(1,70):
                self.assertEqual(primitive_sum_contacts(H,m),
                                 brute_contacts(H,m),(H,m))
        self.assertEqual(primitive_sum_contacts(32,2),213)
        self.assertEqual(primitive_sum_contacts(32,1),647)

    def test_prime_power_local_hypersurface_vs_brute_mod_p_k(self):
        for p,k in ((2,1),(2,2),(2,3),(2,4),
                    (3,1),(3,2),(3,3),(5,1),(5,2),(7,1)):
            q=p**k
            allowed=hits=0
            for a in range(q):
                for b in range(q):
                    if a%p==b%p==0:
                        continue
                    allowed+=1
                    hits+=(a+b)%q==0
            self.assertEqual(Q(hits,allowed),
                             local_conditional_limit(q))
        for m in (1,6,8,12,30,72,125,210,420):
            f=factorization(m)
            self.assertEqual(local_conditional_limit(m),
                             Q(1,m)*__import__("math").prod(
                                 (Q(p,p+1) for p,_ in f),start=Q(1)))

    def test_finite_mobius_certified_error_without_float_zeta(self):
        for H in range(1,80):
            for m in (1,2,3,4,5,6,8,9,16,30,64,75,257,100003):
                real=primitive_sum_contacts(H,m)
                partial=partial_main(H,m)
                self.assertLessEqual(abs(Q(real)-partial),
                                     height_error_bound(H)-H)
        self.assertEqual(height_error_bound(1),4)

    def test_archimedean_hard_cut_refutes_unbounded_local_inference(self):
        for H,m in ((6,13),(30,64),(80,257),(200,401)):
            r=receipt(H,m)
            self.assertTrue(r.height_forbidden)
            self.assertEqual(r.simultaneous_contacts,0)
            self.assertGreater(r.limiting_fraction,0)
        r=receipt(32,2)
        self.assertFalse(r.height_forbidden)
        self.assertEqual(r.actual_fraction,Q(213,647))
        self.assertEqual(r.limiting_fraction,Q(1,3))

    def test_uniform_conditional_absolute_error_model_bound(self):
        # Independent crude count B_H>=H^2/4 and elementary uniform
        # Mobius enclosure imply |N_H(m)/B_H - D(m)|<=8*E(H)/H^2.
        for H in (70,256,1024,5000):
            B=primitive_sum_contacts(H,1)
            self.assertGreaterEqual(B,Q(H*H,4))
            tol=Q(8*height_error_bound(H),H*H)
            for m in (1,2,3,4,9,16,17,30,64,125,210,257,2*H+1):
                N=primitive_sum_contacts(H,m)
                self.assertLessEqual(abs(Q(N,B)-local_conditional_limit(m)),
                                     tol)

    def test_hostile_inputs_are_not_silently_coerced(self):
        for m in (False,0,-1,2.5,10**12+1):
            with self.assertRaises(HeightError):
                primitive_sum_contacts(10,m)
        for H in (False,0,-1,1.1,100001):
            with self.assertRaises(HeightError):
                primitive_sum_contacts(H,3)
        with self.assertRaises(HeightError):
            receipt(2001,2)
        with self.assertRaises(HeightError):
            partial_main(4000,7)
        with self.assertRaises(HeightError):
            box_sum_contacts(4,True)


if __name__=="__main__":
    unittest.main()
