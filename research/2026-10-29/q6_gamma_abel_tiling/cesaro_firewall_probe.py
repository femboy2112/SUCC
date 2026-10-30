"""Independent exact rational calibrations of GTQ6-15 universal Cesaro firewall.

The universal theorem is analytic; these finite tests are controls, not proof.
Original q_n is recomputed from the fixed four-pole forcing and no source mutation.
"""
from fractions import Fraction as F
from math import comb, gcd
import unittest

def r(n):return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def pascal(n):
    return [F(comb(n,j))*sum((F((-1)**k*comb(j,k))*r(2*n-j+k)
                               for k in range(j+1)),F())/r(n) for j in range(n+1)]

def d(j):return int(gcd(j+2,6)==1)-int(gcd(j,6)==1)

def mean_bound(L,N):return F(4,N)+F(88,N)*sum((F(1,n) for n in range(L,L+N)),F())

def real_harmonic_seam(n,seq):
    # The real harmonic-only edge is strictly below full A_j; tests do not
    # incorrectly treat it as the actual Gamma/golden complex seam.
    return sum((w*d(j)*(F(1,j+2)+F(1,j+3))*(seq[n+j]-seq[n+1])
                for j,w in enumerate(pascal(n))),F())

class NoGoTests(unittest.TestCase):
    def test_oily_first_moment_exact(self):
        self.assertEqual(sum((F(j*(j+1),2**(j+2)) for j in range(80)),F()),
                         F(2)-F(80*80+3*80+4,2**81))
    def test_complete_pascal_mass(self):
        for n in range(1,25):self.assertEqual(sum(pascal(n)),1)
    def test_uniform_bound_constant_sequence(self):
        seq=[F(1)]*100
        for n in range(3,40):self.assertEqual(real_harmonic_seam(n,seq),0)
    def test_bounded_periodic_and_sparse_sequences(self):
        sequences=[tuple(F(1 if i%2 else -1) for i in range(180)),
                   tuple(F(1 if i in (7,11,26,57,101,127) else 0) for i in range(180)),
                   tuple(F((7*i*i+3*i)%13-6,6) for i in range(180))]
        for seq in sequences:
            for L,N in ((3,10),(5,20),(10,50)):
                avg=sum((real_harmonic_seam(n,seq) for n in range(L,L+N)),F())/N
                self.assertLessEqual(abs(avg),mean_bound(L,N))
    def test_selector_origin_and_shift(self):
        self.assertEqual([d(j) for j in range(6)],[0,-1,0,1,0,0])
        self.assertEqual(sum((F(j*(j+1),2**(j+2)) for j in range(12)),F()),
                         F(2)-F(12*12+3*12+4,2**13))

if __name__=='__main__':unittest.main(verbosity=2)
