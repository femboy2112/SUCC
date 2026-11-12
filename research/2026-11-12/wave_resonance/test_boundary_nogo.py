"""Exact instances of infinite negative frozen-cutoff wave theorem WAVE-09."""
import unittest
from math import isqrt

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def icbrt(n):
    z=0
    while (z+1)**3<=n:z+=1
    return z

def rough_composite(n,z):
    return n>=4 and not prime(n) and all(n%d for d in range(2,z+1) if prime(d))

class TestBoundary(unittest.TestCase):
    def test_infinite_family_finite_instances(self):
        for p in (3,5,7,11,13,17,101,599):
            self.assertTrue(prime(p))
            X=p*p+1;N=2*p*p;z=icbrt(X)
            self.assertLess(z,p)
            R=C=0
            for a in range(max(2,N-X),min(X,N-2)+1):
                b=N-a
                if 2<=b<=X:
                    R+=prime(a) and prime(b)
                    C+=rough_composite(a,z) and rough_composite(b,z)
            self.assertEqual((R,C,R-C),(0,1,-1))

if __name__=='__main__':unittest.main()
