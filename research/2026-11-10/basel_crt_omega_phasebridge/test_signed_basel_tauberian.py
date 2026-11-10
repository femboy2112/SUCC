#!/usr/bin/env python3
"""Exact finite controls of the signed Basel inverse-Abel identities."""
from fractions import Fraction
import unittest

def tails(seq):
    M=len(seq)-1
    F=[Fraction(0) for _ in range(M+2)]
    for n in range(M,0,-1):
        F[n]=F[n+1]+Fraction(seq[n],n*n)
    return F

def weight(A):
    return sum((Fraction(1,n*n) for n in range(A,2*A)),Fraction(0))

def inverse_abel(F,A):
    B=2*A
    return A*A*F[A]-(B-1)**2*F[B]+sum(((2*n-1)*F[n] for n in range(A+1,B)),Fraction(0))

def examples(M):
    seqs=[
        [0]+[1]*M,
        [0]+[(-1)**n for n in range(1,M+1)],
        [0]+[1 if n%7 in (1,5) else -1 for n in range(1,M+1)],
        [0]+[1 if n in (7,14,27,51,100) else 0 for n in range(1,M+1)]
    ]
    block=[0]
    p=1
    for n in range(1,M+1):
        if n==2*p:
            p*=2
        block.append((-1)**(p.bit_length()-1))
    seqs.append(block)
    return seqs

class SignedBaselTests(unittest.TestCase):
    def test_exact_inverse_abel(self):
        for seq in examples(256):
            F=tails(seq)
            for A in range(1,129):
                self.assertEqual(inverse_abel(F,A),sum(seq[A:2*A]))
    def test_finite_dyadic_tail_decomposition(self):
        for seq in examples(256):
            F=tails(seq)
            for A in (1,3,5,11,19,45,101,200):
                acc=Fraction(0)
                B=A
                while B<=256:
                    acc+=sum((Fraction(seq[n],n*n) for n in range(B,min(2*B,257))),Fraction(0))
                    B*=2
                self.assertEqual(acc,F[A])
    def test_quantitative_5_and_10_bounds(self):
        for seq in examples(256):
            F=tails(seq)
            for A in (1,2,3,8,11,25,60,123):
                c=Fraction(sum(seq[A:2*A]),A)
                d=max((n*abs(F[n]) for n in range(A,257)),default=Fraction(0))
                eta=max((abs((F[B]-F[min(2*B,257)])/weight(B))
                         for B in range(A,257)),default=Fraction(0))
                self.assertLessEqual(abs(c),5*d)
                self.assertLessEqual(d,2*eta)
                self.assertLessEqual(abs(c),10*eta)
    def test_weighted_shell_versus_tail_bound(self):
        for seq in examples(256):
            F=tails(seq)
            for A in (1,3,12,50,119,250):
                d=max((n*abs(F[n]) for n in range(A,257)),default=Fraction(0))
                B=(F[A]-F[min(2*A,257)])/weight(A)
                self.assertLessEqual(abs(B),3*d)
    def test_shell_weights_compare_integral(self):
        for A in range(1,80):
            W=weight(A)
            self.assertGreaterEqual(W,Fraction(1,2*A))
            self.assertLessEqual(W,Fraction(1,A))
    def test_constant_wrong_seed_does_not_cancel(self):
        for A in (11,32,100):
            f=sum((Fraction(1,n*n) for n in range(A,10001)),Fraction(0))
            self.assertLess(f,Fraction(1,A)+Fraction(1,A*A))
            self.assertLess(Fraction(1,A)-f,Fraction(1,10000))
        self.assertEqual(Fraction(sum([1]*100),100),1)
    def test_alternating_tail_cancellation_certificate(self):
        for A in (3,11,60):
            M=2*A+50
            f=sum((Fraction((-1)**n,n*n) for n in range(A,M+1)),Fraction(0))
            self.assertLessEqual(abs(f),Fraction(1,A*A))
    def test_dyadic_block_countermodel_shell(self):
        seq=examples(256)[-1]
        F=tails(seq)
        for A in (2,4,8,16,32,64,128):
            self.assertEqual(abs(Fraction(sum(seq[A:2*A]),A)),1)
            self.assertEqual(abs((F[A]-F[2*A])/weight(A)),1)

if __name__=="__main__":
    unittest.main(verbosity=2)
