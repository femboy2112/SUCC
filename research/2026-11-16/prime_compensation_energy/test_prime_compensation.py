"""Exact rational finite regressions; no asymptotic mathematical claims."""
import unittest
from fractions import Fraction
from itertools import permutations
from math import gcd

from prime_compensation import (
    ZETA_MINUS_ONE, PrimeJetMinusOne, bernoulli_two, bbp_carry_sign,
    bbp_forcing, bbp_joint_shell, chi_at, coprime_residue_from_factors,
    euler_minus_one, hurwitz_residue_minus_one, is_prime, new_prime_predicate,
    normalized_linear, normalized_mixed, prime_transport_pair, signed_path_action,
    signed_path_sum, sieve_projector, validate_primes, boost_coeffs_minus_one,
    signed_boost_minus_one, projected_two_prime_paths, projected_two_prime_gap,
)

class ExactPrimeCompensation(unittest.TestCase):
    def test_genuine_primes_only(self):
        for bad in [(2, 6), (2,2), (1,3), (4,), (0,), (-3,2)]:
            with self.assertRaises(ValueError):validate_primes(bad)
        self.assertEqual(validate_primes((2,3,5)),(2,3,5))

    def test_prime_predicate_all_small(self):
        for n in range(2,300):
            self.assertEqual(new_prime_predicate(n),int(is_prime(n)),n)

    def test_path_coprime_all_small(self):
        for ps in [(),(2,),(2,3),(2,3,5),(3,7),(2,3,5,7)]:
            for n in range(1,121):
                self.assertEqual(signed_path_sum(n,ps),sieve_projector(n,ps))

    def test_bern_residual(self):
        for ps in [(),(2,),(2,3),(2,3,5),(2,3,5,7),(2,3,5,7,11)]:
            self.assertEqual(hurwitz_residue_minus_one(ps),coprime_residue_from_factors(ps))
            self.assertEqual(euler_minus_one(ps)*hurwitz_residue_minus_one(ps),ZETA_MINUS_ONE)

    def test_exact_ledger(self):
        self.assertEqual((euler_minus_one((2,3,5)),hurwitz_residue_minus_one((2,3,5))),
                         (Fraction(-1,8),Fraction(2,3)))
        self.assertEqual((euler_minus_one((2,3,5,7)),hurwitz_residue_minus_one((2,3,5,7))),
                         (Fraction(1,48),Fraction(-4)))

    def test_mixed_seams(self):
        for p in [2,3,5,7,11,19,29]:
            self.assertEqual(normalized_mixed(p,-1),Fraction(p*p,p-1))
            self.assertEqual(normalized_mixed(p,2),-Fraction(1,p*p*(p*p-1)))
            self.assertEqual(normalized_mixed(p,-1)+normalized_linear(p,-1),0)
            self.assertEqual(normalized_mixed(p,2)+normalized_linear(p,2),0)

    def test_linearization_failure(self):
        E=Fraction(1);R=ZETA_MINUS_ONE
        for p in (2,3,5,7):
            En,Rn=prime_transport_pair(E,R,p)
            de,dr=En-E,Rn-R
            self.assertNotEqual(R*de+E*dr,0)
            self.assertEqual(R*de+E*dr+de*dr,0)
            self.assertEqual((de*dr)/(E*R),normalized_mixed(p,-1))
            E,R=En,Rn

    def test_flat_prime_square(self):
        root=(Fraction(7,5),Fraction(-5,84)) # product -1/12
        for p,q in [(2,3),(3,5),(5,7),(7,13)]:
            first=prime_transport_pair(*prime_transport_pair(*root,p),q)
            second=prime_transport_pair(*prime_transport_pair(*root,q),p)
            self.assertEqual(first,second)
            self.assertEqual(first[0]*first[1],ZETA_MINUS_ONE)

    def test_formal_first_jet(self):
        for word in [(),(2,),(2,3),(3,2),(5,2,3),(2,3,5,7)]:
            state=PrimeJetMinusOne.root()
            for p in word:state=state.insert(p)
            self.assertEqual(state.E*state.R,ZETA_MINUS_ONE)
            self.assertEqual(state.invariant_jet(),{"zeta_prime":Fraction(1)})
        a=PrimeJetMinusOne.root()
        b=PrimeJetMinusOne.root()
        for p in (2,3,5):a=a.insert(p)
        for p in (5,2,3):b=b.insert(p)
        self.assertEqual(a,b)

    def test_positive_path_action(self):
        self.assertEqual(signed_path_action((2,3,5)),Fraction(59,4))
        self.assertEqual(signed_path_action((3,2,5)),Fraction(59,4))
        self.assertTrue(signed_path_action((2,3,5,7))>signed_path_action((2,3,5)))

    def test_full_state_vs_sum_readout(self):
        z=ZETA_MINUS_ONE
        x1=(Fraction(1),z);x2=(z,Fraction(1))
        self.assertEqual(sum(x1),sum(x2))
        self.assertEqual(x1[0]*x1[1],x2[0]*x2[1])
        self.assertNotEqual(sum(prime_transport_pair(*x1,3)),sum(prime_transport_pair(*x2,3)))
        # A single Euler-coordinate observer *does* descend when the prime is known.
        self.assertEqual(prime_transport_pair(Fraction(1),z,3)[0],Fraction(-1,2))

    def test_full_BBP_forcing(self):
        self.assertEqual(bbp_forcing(1),Fraction(47,15))
        for n in range(1,80):
            self.assertTrue(bbp_carry_sign(n) in (-1,1))

    def test_source_joining_identity(self):
        for start,length in [(3,8),(10,18),(25,12),(49,9)]:
            for primes in [(),(2,3),(2,3,5)]:
                a,j,d=bbp_joint_shell(start,length,primes)
                self.assertEqual(a-j,2*d)
                self.assertTrue(Fraction(0)<=d<=1)
                selected=sum(1 for n in range(start,start+length) if bbp_carry_sign(n)==-1)
                self.assertLessEqual(d,Fraction(selected,length))

    def test_fake_six_is_redundant_projector_not_factor(self):
        for n in range(1,201):
            authentic=sieve_projector(n,(2,3))
            mutated=authentic*int(n%6 !=0)
            self.assertEqual(authentic,mutated)
        self.assertNotEqual(Fraction(1,1-6)*euler_minus_one((2,3)),euler_minus_one((2,3)))

    def test_signed_boost_source_pair(self):
        e, r = Fraction(1), ZETA_MINUS_ONE
        u, v = (e+r)/2, (e-r)/2
        for p in (2,3,5,7,11):
            up, vp = signed_boost_minus_one(u, v, p)
            ep, rp = prime_transport_pair(e, r, p)
            self.assertEqual((up,vp),((ep+rp)/2,(ep-rp)/2))
            self.assertEqual(up*up-vp*vp, ZETA_MINUS_ONE)
            self.assertEqual(boost_coeffs_minus_one(p)[0]**2
                             -boost_coeffs_minus_one(p)[1]**2, 1)

    def test_projected_two_prime_inertial_gap(self):
        for p,q in [(2,3),(3,5),(3,7),(5,11),(7,13)]:
            cp,sp=boost_coeffs_minus_one(p)
            cq,sq=boost_coeffs_minus_one(q)
            for u in [Fraction(0), Fraction(1),Fraction(3,7),Fraction(-2,5)]:
                full, lost, gap = projected_two_prime_paths(u,p,q)
                self.assertEqual(full, u*(cp*cq+sp*sq))
                self.assertEqual(lost, u*cp*cq)
                self.assertEqual(gap, u*sp*sq)
                self.assertEqual(gap, projected_two_prime_gap(u,q,p))
        self.assertEqual(projected_two_prime_gap(Fraction(1),3,5),Fraction(45,32))
        self.assertEqual(projected_two_prime_gap(Fraction(1),2,5),Fraction(0))
        with self.assertRaises(ValueError):
            projected_two_prime_gap(Fraction(1),3,3)
        with self.assertRaises(ValueError):
            projected_two_prime_gap(Fraction(1),6,7)

if __name__=='__main__':unittest.main()
