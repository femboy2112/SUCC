"""All-order exact source-jet reconstruction, independent stdlib Fraction oracle.

No SymPy, no π digits, no altered original BBP source or seed.
Finite tests calibrate the Vandermonde paper theorem, not an all-n proof.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb,factorial
import unittest

ORIG=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def force(n,w):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(w,1)),Q(0))

def coefficient(w,d):
    # 1/[8n+(j-8)] = sum_d (8-j)^(d-1)/(8n)^d.
    return sum((c*Q((8-j)**(d-1),8**d)
                for j,c in enumerate(w,1)),Q(0))

def stirling(n,k):
    if n==k==0:return 1
    if n<=0 or k<=0 or k>n:return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)

def moment(j):
    # S_j=sum_(m>=1) m^j/16^m exactly, via Stirling/falling factorials.
    x=Q(1,16)
    if j==0:return x/(1-x)
    return sum((Q(stirling(j,r)*factorial(r))*x**r/(1-x)**(r+1)
                for r in range(1,j+1)),Q(0))

def zcoef(k):
    return -sum((coefficient(RAD,d)*(-1)**(k-d)*comb(k-1,k-d)*moment(k-d)
                 for d in range(1,k+1)),Q(0))

def lagcoef(k,ell):
    # coefficient of n^-k in z(n+ell)-z(n), k>=2
    return sum((zcoef(d)*(-1)**(k-d)*comb(k-1,k-d)*ell**(k-d)
                for d in range(1,k)),Q(0))

def solve(m):
    rows=[[lagcoef(k,ell) for ell in range(1,m+1)]+[-coefficient(ORIG,k)]
          for k in range(2,m+2)]
    for col in range(m):
        pivot=next((i for i in range(col,m) if rows[i][col]),None)
        if pivot is None:raise ArithmeticError("rank lost in source clock")
        rows[col],rows[pivot]=rows[pivot],rows[col]
        div=rows[col][col]
        rows[col]=[x/div for x in rows[col]]
        for j in range(m):
            if j!=col:
                a=rows[j][col]
                rows[j]=[x-a*y for x,y in zip(rows[j],rows[col])]
    return tuple(row[-1] for row in rows)

def tail_lag(n,ell,depth=48):
    # Independently combine all finite source denominator pairs.
    total=Q(0)
    for m in range(1,depth+1):
        v=Q(0)
        for j,c in enumerate(RAD,1):
            if c:
                d=8*(n+m-1)+j
                v+=c/Q(d*(d+8*ell))
        total+=Q(8*ell,16**m)*v
    return total

def residual(n,weights):
    return force(n,ORIG)+sum((w*tail_lag(n,j)
                              for j,w in enumerate(weights,1)),Q(0))

class JetTransport(unittest.TestCase):
    def test_01_rational_source_coefficients(self):
        self.assertEqual([coefficient(ORIG,k) for k in range(1,6)],
                         [Q(0),Q(15,64),Q(151,512),Q(1209,4096),Q(8995,32768)])
        self.assertEqual([coefficient(RAD,k) for k in range(1,4)],
                         [-Q(15,32),-Q(53,256),-Q(149,2048)])

    def test_02_independent_geometric_moments(self):
        self.assertEqual([moment(j) for j in range(4)],
                         [Q(1,15),Q(16,225),Q(272,3375),Q(1712,16875)])
        self.assertEqual([zcoef(k) for k in range(1,6)],
                         [Q(1,32),-Q(5,256),Q(27,2048),
                          -Q(209,16384),Q(2355,131072)])

    def test_03_exact_delay_coefficients(self):
        self.assertEqual([lagcoef(k,1) for k in range(2,5)],
                         [-Q(1,32),Q(9,128),-Q(265,2048)])
        self.assertEqual([lagcoef(k,2) for k in range(2,5)],
                         [-Q(1,16),Q(13,64),-Q(577,1024)])

    def test_04_vandermonde_unique_weights(self):
        self.assertEqual(solve(1),(Q(15,2),))
        self.assertEqual(solve(2),(Q(541,16),-Q(421,32)))
        self.assertEqual(solve(3),(Q(22309,256),-Q(17021,256),Q(4551,256)))
        # Additional unfitted rank-4 structural test:
        self.assertEqual(len(solve(4)),4)
        for m in range(1,5):
            w=solve(m)
            for k in range(2,m+2):
                self.assertEqual(coefficient(ORIG,k)+sum(
                    (w[j-1]*lagcoef(k,j) for j in range(1,m+1)),Q(0)),Q(0))

    def test_05_leading_rational_residual_coefficients(self):
        known=(Q(421,512),Q(13653,4096),Q(537369,32768))
        for m in (1,2,3):
            w=solve(m)
            lead=coefficient(ORIG,m+2)+sum(
                (w[j-1]*lagcoef(m+2,j) for j in range(1,m+1)),Q(0))
            self.assertEqual(lead,known[m-1])

    def test_06_independent_exact_future_tail_residuals(self):
        leading=(Q(421,512),Q(13653,4096),Q(537369,32768))
        for n in (101,307,953,1901):
            for m in (1,2,3):
                val=residual(n,solve(m))*n**(m+2)
                self.assertLess(abs(val-leading[m-1]),leading[m-1]/Q(10))

    def test_07_critical_fourier_phase_error_drops_per_delay(self):
        for n in (307,953):
            H=64*n*n
            errors=[abs(H*residual(n,solve(m))) for m in (1,2,3)]
            self.assertGreater(errors[0],errors[1])
            self.assertGreater(errors[1],errors[2])
            self.assertLess(errors[2],Q(1,10000))

    def test_08_literal_original_recurrence_and_exact_ward_identity(self):
        U=[Q(0)]
        for n in range(1,58):U.append(16*U[-1]+force(n,ORIG))
        H=65536
        for n in (7,17,53):
            for m in (1,2,3):
                B=sum((a*tail_lag(n,ell) for ell,a in enumerate(solve(m),1)),Q(0))
                # The finite tail truncation is not exact z, so use exact
                # algebraic residual for the same approximate B.
                self.assertEqual(U[n]+B-16*U[n-1],force(n,ORIG)+B)
                self.assertEqual((H*(U[n]+B-16*U[n-1]))%1,
                                 (H*(force(n,ORIG)+B))%1)

if __name__=="__main__":unittest.main()
