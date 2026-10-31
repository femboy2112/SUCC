"""Exact coefficient/divisor/scale checks for the P1--P3 source transport."""
from fractions import Fraction as F
import unittest

B=(7,4,3,2)
C=(4,-2,-1,-1)


def source(n,u=F(0)):
    a=8*n-7+u
    return F(6)/(a*(a+3))+F(4)/(a*(a+4))+F(5)/(a*(a+5))


def pole_source(n,beta):
    return sum((F(c)/(8*n-d) for c,d in zip(C,beta)),F(0))


def factor(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out


def sieve(n):
    flags=[True]*(n+1)
    if n>=0: flags[0]=False
    if n>=1: flags[1]=False
    for d in range(2,n+1):
        if flags[d]:
            for k in range(d*d,n+1,d):
                flags[k]=False
    return [p for p in range(2,n+1) if flags[p]]


def direct_log_coefficients(cutoff,s,z,u):
    coeff={}
    for n in range(2,cutoff+1):
        weight=z**n*F(n)**(-s)*source(n,u)
        for p,exponent in factor(n).items():
            coeff[p]=coeff.get(p,F(0))+exponent*weight
    return coeff


def prime_event_coefficients(cutoff,s,z,u,wrong_power_weight=False):
    coeff={}
    for p in sieve(cutoff):
        q=p
        k=1
        total=F(0)
        while q<=cutoff:
            for m in range(1,cutoff//q+1):
                n=q*m
                total+=(k if wrong_power_weight else 1)*z**n*F(n)**(-s)*source(n,u)
            q*=p
            k+=1
        coeff[p]=total
    return coeff


class PrimeWeightTests(unittest.TestCase):
    def test_complete_finite_log_prime_coefficient_identity(self):
        for cutoff in (8,31,97):
            for s in (-2,-1,0,2):
                for z,u in ((F(1,16),F(0)),(F(2,3),F(-3,7)),(F(1),F(5,9))):
                    self.assertEqual(direct_log_coefficients(cutoff,s,z,u),
                                     prime_event_coefficients(cutoff,s,z,u))

    def test_prime_power_clock_dilation_with_full_prefactor(self):
        for q in (2,4,8,9,25,49):
            for m in (1,2,7,23):
                for u in (F(-2,3),F(0),F(4,5)):
                    beta=tuple((F(b)-u)/q for b in B)
                    self.assertEqual(source(q*m,u),pole_source(m,beta)/q)
                    self.assertNotEqual(source(q*m,u),pole_source(m,beta))
                    for s in (-1,0,3):
                        z=F(1,16)
                        actual=z**(q*m)*F(q*m)**(-s)*source(q*m,u)
                        predicted=F(q)**(-s-1)*(z**q)**m*F(m)**(-s)*pole_source(m,beta)
                        self.assertEqual(actual,predicted)

    def test_log_prime_power_mutation_fails_at_four(self):
        s,z,u=0,F(1,16),F(0)
        correct=direct_log_coefficients(4,s,z,u)
        wrong=prime_event_coefficients(4,s,z,u,wrong_power_weight=True)
        self.assertEqual(wrong[2]-correct[2],z**4*source(4))
        self.assertGreater(wrong[2]-correct[2],0)
        self.assertEqual(wrong[3],correct[3])

    def test_one_source_shift_cannot_replace_vector_dilation(self):
        for q in (2,3,4,9,25):
            for u in (F(-3,5),F(0),F(2,7)):
                beta=tuple((F(b)-u)/q for b in B)
                common_shift=F(B[0])-beta[0]
                shifted=tuple(F(b)-common_shift for b in B)
                self.assertEqual(shifted[0],beta[0])
                self.assertNotEqual(shifted[1],beta[1])
                self.assertEqual(shifted[0]-shifted[1],3)
                self.assertEqual(beta[0]-beta[1],F(3,q))


if __name__=='__main__':
    unittest.main(verbosity=2)
