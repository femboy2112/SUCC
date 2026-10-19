"""Independent CRT source/mutation and Poisson factorial gate-location controls."""
import unittest
from fractions import Fraction as Q
from math import gcd, lcm, factorial

from observational_succ.borwein_abc_contacts import (
    ContactError, TimedPrimeGate, abc_prime_power_contact,
    deterministic_succ_gate_crt, poisson_gate_coefficients,
    poisson_polynomial, poisson_tail_bound, prime_power,
)


class ABCDeltaContactsTest(unittest.TestCase):
    def test_source_relative_abc_phase_power_and_nonunits(self):
        c=abc_prime_power_contact(3,125,2,7)
        self.assertEqual(c.c,128)
        self.assertEqual((c.valuation,c.modulus,c.relative_phase,c.locked),
                         (7,128,1,True))
        self.assertFalse(abc_prime_power_contact(3,125,2,8).locked)
        self.assertEqual(abc_prime_power_contact(3,125,5,1).relative_phase,None)
        self.assertFalse(abc_prime_power_contact(3,125,5,1).locked)
        self.assertTrue(abc_prime_power_contact(1,8,3,2).locked)
        for a,b in ((1,8),(3,125),(5,1024),(4,7),(8,9),(17,41)):
            for p in (2,3,5,7,11):
                for k in (1,2,3):
                    v=abc_prime_power_contact(a,b,p,k)
                    self.assertEqual(v.locked,(a+b)%(p**k)==0)
                    if b%p:
                        self.assertEqual(v.relative_phase==1,v.locked)
                    else:
                        self.assertIsNone(v.relative_phase)

    def test_exact_primitive_cancellation_gate_versus_bruteforce(self):
        for p,k in ((2,1),(2,3),(3,2),(5,1)):
            m=p**k
            for a in range(1,51):
                for b in range(1,29):
                    if gcd(a,b)!=1:
                        continue
                    c=abc_prime_power_contact(a,b,p,k)
                    self.assertEqual(c.locked,((a+b)%m==0))
                    self.assertEqual(c.valuation>=k,c.locked)

    def test_prime_power_gate_rejects_fake_source(self):
        for p,e in ((4,1),(6,2),(1,1),(3,0),(5,True),(2,100)):
            with self.assertRaises(ContactError):
                prime_power(p,e)
        with self.assertRaises(ContactError):
            abc_prime_power_contact(6,9,3,1)
        with self.assertRaises(ContactError):
            abc_prime_power_contact(True,5,3,1)
        with self.assertRaises(ContactError):
            TimedPrimeGate(4,1,1,1)
        with self.assertRaises(ContactError):
            TimedPrimeGate(3,2,9,1)

    def test_crt_delta_sandwich_matches_independent_source_scan(self):
        words=(
            (TimedPrimeGate(3,1,1,1),TimedPrimeGate(3,1,1,1)),
            (TimedPrimeGate(3,1,1,1),TimedPrimeGate(3,1,2,1)),
            (TimedPrimeGate(2,2,1,1),TimedPrimeGate(2,3,2,2)),
            (TimedPrimeGate(3,1,1,1),TimedPrimeGate(5,1,4,2)),
            (TimedPrimeGate(2,2,0,1),TimedPrimeGate(2,3,4,2)),
            (TimedPrimeGate(3,2,4,2),TimedPrimeGate(3,1,0,4)),
            (TimedPrimeGate(5,1,1,2),TimedPrimeGate(7,1,3,4),
             TimedPrimeGate(5,2,2,1)),
        )
        for word in words:
            v=deterministic_succ_gate_crt(word)
            M=lcm(*(p.prime**p.depth for p in word))
            good=[]
            for start in range(M):
                n=start
                alive=True
                for gate in word:
                    n+=gate.succ
                    if n%(gate.prime**gate.depth)!=gate.target:
                        alive=False;break
                if alive:good.append(start)
            self.assertEqual(bool(good),v.compatible,word)
            if good:
                self.assertEqual(v.combined_period,M)
                self.assertEqual(good,[v.initial_residue])
        with self.assertRaises(ContactError):
            deterministic_succ_gate_crt(())
        with self.assertRaises(ContactError):
            deterministic_succ_gate_crt([TimedPrimeGate(3,1,1,1)])

    def test_poisson_gate_placement_changes_result_at_first_return(self):
        for p in (2,3,5,7):
            terminal,every=poisson_gate_coefficients(p,2*p)
            self.assertEqual(terminal[0],every[0])
            for jumps in range(1,2*p+1):
                n=1+jumps
                self.assertEqual(terminal[jumps],int(n%p==1%p))
                self.assertEqual(every[jumps],0)
            self.assertEqual(terminal[p],1)
            self.assertEqual(every[p],0)
            t=Q(3,2)
            positive=poisson_polynomial(t,terminal)-poisson_polynomial(t,every)
            self.assertGreaterEqual(positive,t**p/factorial(p))
            self.assertEqual(poisson_polynomial(t,every),Q(1))

    def test_factorial_does_not_guarantee_suppression_with_many_paths(self):
        # m! permitted orderings exactly neutralize the time-order simplex.
        for m in range(1,10):
            for t in (Q(1,2),Q(3,2)):
                simplex=t**m/factorial(m)
                all_permutations=factorial(m)*simplex
                self.assertEqual(all_permutations,t**m)

    def test_poisson_tail_bound_is_a_probability_normalized_bound(self):
        # This is a rigorously derived inequality. Probe the rational
        # coefficients; avoid pretending exp(-t) is rational.
        for t in (Q(0),Q(1,4),Q(3,2),Q(3)):
            for cutoff in range(0,12):
                b=poisson_tail_bound(t,cutoff)
                self.assertEqual(b,t**(cutoff+1)/factorial(cutoff+1))
                self.assertGreaterEqual(b,0)
        with self.assertRaises(ContactError):
            poisson_polynomial(Q(1),[1,0,1])
        with self.assertRaises(ContactError):
            poisson_polynomial(Q(-1), (1,))
        with self.assertRaises(ContactError):
            poisson_polynomial(Q(1), (True,False))
        with self.assertRaises(ContactError):
            poisson_tail_bound(Q(-1),3)


if __name__=="__main__":
    unittest.main()
