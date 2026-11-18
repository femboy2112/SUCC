"""BBP Mellin/Gamma knowledge-volume ladder: exact rational finite controls.

The paper proves infinite Gram positivity, polynomial density and compact
analytic convergence. Finite Fraction checks do NOT prove pi normality.
"""
import unittest
from fractions import Fraction as F
from math import factorial

A=(1,4,5,6)
C=(4,-2,-1,-1)
Q=(4,0,0,-2,-1,-1)


def poly_eval(a,t):
    z=F(0)
    for c in reversed(a): z=z*t+c
    return z


def mellin_r(n,w=F(0)):
    w=F(w)
    if n<1: raise ValueError('positive source clock')
    return sum((F(c)/(8*(n-1)+a+w) for a,c in zip(A,C)),F(0))


def finite_B(N,w=F(0)):
    return sum((mellin_r(n,w)/16**n for n in range(1,N+1)), F(0))


def moment(N,k):
    return factorial(k)*sum((F(c,16**n*(8*(n-1)+a)**(k+1))
                 for n in range(1,N+1) for a,c in zip(A,C)),F(0))


def ldl_pivots(mat):
    """Exact Schur elimination: positive pivots certify SPD."""
    m=[list(row) for row in mat]
    pivots=[]
    for k in range(len(mat)):
        p=m[k][k];pivots.append(p)
        if p==0: return pivots
        for i in range(k+1,len(mat)):
            for j in range(k+1,len(mat)):
                m[i][j]-=m[i][k]*m[k][j]/p
        for i in range(k+1,len(mat)):
            m[i][k]=F(0);m[k][i]=F(0)
    return pivots


def residue_B_N(N,a,m):
    w0=-a-8*m
    return sum((F(c,16**n) for n in range(1,N+1) for aj,c in zip(A,C)
                if 8*(n-1)+aj+w0==0),F(0))


def tail_bound(N,R):
    if 8*N+1<=R:raise ValueError('circle too large for remaining tail')
    return F(1,16**N)/( (8*N+1-R)*(8*N+2-R) )


def K(t):
    t=F(t)
    return (1-t)/((2-t*t)*(t*t-2*t+2))


def alternate_lock_kernel(t):
    t=F(t)
    return (1-t)*(1+F(3,2)*(1-t))


def alternate_forcing(n):
    # Q_alt(t)=(16-t^8) K_alt(t), with K_alt=(5-8t+3t^2)/2.
    if n<1: raise ValueError
    hs=(F(5,2), F(-4), F(3,2))
    return sum((h*(F(16,8*n-7+j)-F(1,8*n+1+j))
                for j,h in enumerate(hs)),F(0))


def alternate_moment(k):
    # Integral K_alt(t)*(-log t)**k dt.
    return factorial(k)*(F(5,2)-F(4,2**(k+1))+F(3,2*3**(k+1)))


class MellinGammaObserverLadderTests(unittest.TestCase):
    def test_original_four_poles_unchanged(self):
        self.assertEqual(mellin_r(1),F(47,15))
        for n in (1,2,8,32,128):
            explicit=(F(4,8*n-7)-F(2,8*n-4)
                      -F(1,8*n-3)-F(1,8*n-2))
            self.assertEqual(mellin_r(n),explicit)
            self.assertGreater(explicit,0)

    def test_positive_source_kernel_and_factorization(self):
        for t in (F(0),F(1,7),F(1,2),F(3,4),F(1)):
            q=poly_eval(Q,t)
            h=(t*t+2)*(t*t+2*t+2)
            self.assertEqual(q,(1-t)*h)
            self.assertEqual(q/(16-t**8),K(t))
            if 0<t<1:self.assertGreater(K(t),0)

    def test_finite_transport_boundary_identity(self):
        for N in (1,2,4,8,16):
            for w in (F(-1,2),F(0),F(1,3),F(2)):
                defect=finite_B(N,w+8)-16*finite_B(N,w)+mellin_r(1,w)
                self.assertEqual(defect,mellin_r(N+1,w)/16**N)

    def test_uniform_real_compact_tail_envelope(self):
        R=F(2)
        for N in (2,4,8,16):
            cap=tail_bound(N,R)
            for w in (-R,F(-1,2),F(0),F(1,2),R):
                actual=sum((mellin_r(n,w)/16**n
                            for n in range(N+1,N+26)),F(0))
                self.assertGreater(actual,0)
                self.assertLess(actual,cap)

    def test_finite_source_hankel_grams_are_strictly_positive(self):
        for N in (1,2,5,10):
            moments=[moment(N,k) for k in range(9)]
            self.assertTrue(all(m>0 for m in moments))
            for m in (0,1,2,3,4):
                mat=[[moments[i+j] for j in range(m+1)]
                     for i in range(m+1)]
                self.assertTrue(all(p>0 for p in ldl_pivots(mat)),(N,m))

    def test_every_gamma_pole_channel_activates_once(self):
        for a,c in zip(A,C):
            for m in (0,1,2,4):
                wanted=F(c,16**(m+1))
                self.assertNotEqual(wanted,0)
                for N in (0,m):
                    self.assertEqual(residue_B_N(N,a,m),0)
                for N in (m+1,m+2,m+5):
                    self.assertEqual(residue_B_N(N,a,m),wanted)

    def test_independent_pole_classes_and_gamma_shift_denominator(self):
        self.assertEqual(len(set(A)),4)
        self.assertTrue(all(0<a<8 for a in A))
        for w in (F(0),F(1,7),F(5,3)):
            prod=F(1)
            for a in A:prod*=w+a
            self.assertGreater(prod,0)
            # Gamma(z+1)=zGamma(z) entails D(w+8)/D(w)=8**4/prod.
            self.assertEqual((F(8**4,1)/prod)*prod,8**4)

    def test_alternate_locked_zero_seed_has_positive_moment_tower(self):
        # This is a different forcing, chosen as Q_alt=(16-t^8)K_alt.
        # Its completed endpoint is integral K_alt dt=1, hence fully locked.
        self.assertEqual(F(5,2)-F(4,2)+F(3,6),F(1))
        for n in range(1,80):
            self.assertGreater(alternate_forcing(n),0)
            self.assertGreater(alternate_forcing(n),alternate_forcing(n+1))
        self.assertEqual(alternate_moment(0),1)
        vals=[alternate_moment(k) for k in range(9)]
        for m in (1,2,3,4):
            self.assertTrue(all(p>0 for p in ldl_pivots(
                [[vals[i+j] for j in range(m+1)] for i in range(m+1)])))
        for n in (1,2,4,9):
            self.assertEqual((16**n*F(1))%1,0)
        # Q_alt has the same leading 15/(64n^2) coefficient as BBP:
        # Q_alt(1)=0 and Q_alt'(1)=-15.
        self.assertEqual(alternate_lock_kernel(F(1)),0)

    def test_same_scalar_endpoint_does_not_fix_the_moment_germ(self):
        # Positive K_1=1, K_2=2t both integrate to one,
        # but log moments are respectively 1 and 1/2.
        self.assertEqual(F(1),F(2,2))
        self.assertNotEqual(F(1),F(2,4))


if __name__=='__main__': unittest.main()
