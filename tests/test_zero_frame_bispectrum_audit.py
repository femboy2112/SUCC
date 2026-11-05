"""Independent exact BBP delayed-bispectrum calibration, no pi input."""
from __future__ import annotations
import cmath
import math
import unittest
from fractions import Fraction as Q

A_TAPS = (Q(2), Q(2), Q(1), Q(0), Q(-1,2), Q(-1,2), Q(-1,4), Q(0))
R_TAPS = (Q(2), Q(-2), Q(-1), Q(-2), Q(-1,2), Q(-1,2), Q(1,4), Q(0))
P_TAPS = tuple(a+r for a,r in zip(A_TAPS, R_TAPS))


def source(n, taps):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(taps,1)), Q(0))


def states(N, taps, mod_one=False):
    x=Q(0)
    out=[x]
    for n in range(1,N+1):
        x=16*x+source(n,taps)
        if mod_one:
            x%=1
        out.append(x)
    return out


def correction(Z,n,m):
    return sum(((-1)**(m-j)*math.comb(m,j)*Z[n+j] for j in range(m+1)),Q(0))


def exp_rational(q):
    return cmath.exp(2j*math.pi*float(q%1))


class Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.N=1027
        cls.U=states(cls.N,P_TAPS,True)
        cls.Y=states(200,A_TAPS,True)
        cls.Z=states(cls.N,R_TAPS)

    def test_original_source_unchanged(self):
        self.assertEqual(P_TAPS,(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0)))
        for n in range(1,180):
            self.assertEqual(self.U[n],(self.Y[n]+self.Z[n])%1)

    def test_binomial_nonlinear_character_is_exact(self):
        for n in (1,7,32,128):
            for m in (1,2,3,4):
                coeffs=[(-1)**(j-1)*math.comb(m,j) for j in range(1,m+1)]
                self.assertEqual(sum(coeffs),1)
                weighted=sum((c*self.Z[n+j] for j,c in enumerate([0]+coeffs) if j),Q(0))
                self.assertEqual(weighted-self.Z[n],(-1)**(m+1)*correction(self.Z,n,m))

    def test_source_curvature_bound_exact_fractions(self):
        for n in (128,129,191,256,307,512,953):
            second=correction(self.Z,n,2)
            self.assertGreater(second,0)
            self.assertLess(second,Q(1,8*n**3))

    def test_critical_two_lag_phase_error(self):
        for A in (128,256,512):
            H=16**int(math.floor(math.log(A*A*math.log(A),16)))
            bound=math.pi*H/(4*A**3)
            errors=[]
            for n in range(A,2*A):
                delta=correction(self.Z,n,2)
                p=exp_rational(H*self.U[n]); q=p*exp_rational(-H*delta)
                errors.append(abs(p-q))
            self.assertLess(max(errors),bound)
            self.assertLess(sum(errors)/A,bound)

    def test_wrong_seed_rotation_does_not_create_mixing(self):
        seed=Q(1,5)
        for n in (1,17,128,307):
            self.assertEqual((16**n*seed)%1,seed)


if __name__=='__main__': unittest.main()
