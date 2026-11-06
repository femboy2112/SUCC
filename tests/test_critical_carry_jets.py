"""Exact source-specific critical-carry and observer-jet regression.

Only finite calculations; not a pi-normality or RH proof. Uses no pi digits.
"""
import unittest
from fractions import Fraction as F
from functools import lru_cache
from math import floor, log

ORIGINAL = (F(4), F(0), F(0), F(-2), F(-1), F(-1), F(0), F(0))
RADIAL = (F(2), F(-2), F(-1), F(-2), F(-1,2), F(-1,2), F(1,4), F(0))

@lru_cache(None)
def pole(n, taps=ORIGINAL):
    return sum((w/F(8*n-8+j) for j,w in enumerate(taps, 1)),F())

@lru_cache(None)
def forcing(n):
    p=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    assert p == pole(n)
    return p

@lru_cache(None)
def states(N):
    x=F()
    out=[x]
    for n in range(1,N+1):
        x=16*x+forcing(n)
        out.append(x)
    return tuple(out)

def block_force(n,m):
    return sum((16**(m-j)*forcing(n+j) for j in range(1,m+1)),F())

def carry_data(U,n,m):
    B=16**m
    x=U[n]%1
    R=block_force(n,m)
    W=(B*x).__floor__()
    K=(B*x+R).__floor__()
    literal=U[n+m].__floor__()-B*U[n].__floor__()
    assert K==literal
    return R,W,K,K-W,x

def epochs(A,m):
    U=states(2*A-1+m)
    results=[carry_data(U,n,m) for n in range(A,2*A)]
    return results

def rad_states(N):
    Z=F(); out=[Z]
    for n in range(1,N+1):
        Z=16*Z+pole(n,RADIAL)
        out.append(Z)
    return out

class CriticalCarryJets(unittest.TestCase):
    def test_01_original_source_identity(self):
        self.assertEqual(forcing(1),F(47,15))
        for n in range(2,1024):
            self.assertGreater(forcing(n),0)
            self.assertEqual(forcing(n),pole(n))

    def test_02_source_asymptotic_rational_bound(self):
        a=F(15,64)
        for n in range(2,1024):
            error=forcing(n)-a/n**2
            self.assertGreater(error,0)
            self.assertLess(error,F(1,n**3))

    def test_03_uniform_block_error_all_observer_orders(self):
        for n in (2,3,5,13,29,61,139,277,557):
            for m in range(1,9):
                B=16**m;R=block_force(n,m)
                self.assertLess(abs(R-F(B-1,64*n*n)),F(B,10*n**3))

    def test_04_exact_binary_threshold_and_carry(self):
        for n,m in ((13,2),(29,3),(61,3),(139,4),(277,5),(557,6)):
            U=states(n+m)
            R,W,K,b,x=carry_data(U,n,m)
            self.assertTrue(0<R<1)
            self.assertEqual(b, int((16**m*x)%1 >= 1-R))
            self.assertIn(b,(0,1))

    def test_05_preregistered_critical_epoch_counts(self):
        for A,m,expected in ((139,4,4),(139,5,48),(277,5,31),(557,5,15),(557,6,244)):
            data=epochs(A,m)
            self.assertTrue(all(F()<x[0]<F(1) for x in data))
            self.assertEqual(sum(row[3] for row in data),expected)

    def test_06_preregistered_coherent_seed_stays_uncorrected(self):
        # Source beta=0: U_n=-T_n. Bound T_n<=1/((8n+1)(8n+2)).
        for A,m in ((139,4),(139,5),(277,5),(557,5),(557,6)):
            B=16**m
            self.assertLess(B,(8*A+1)*(8*A+2))
            for n in (A,(3*A)//2,2*A-1):
                self.assertLess(block_force(n,m),1)
                # Since B*T_n<1 and T_(n+m)>0, W=K=B-1, so b=0.

    def test_07_original_radial_null_is_small(self):
        Z=rad_states(150)
        self.assertEqual(Z[0],0)
        for n in range(1,151):
            self.assertGreater(Z[n],0)
            self.assertLess(Z[n],F(11,20*(8*n+1)))
        self.assertLess(abs(float(Z[100]*100)-1/32),1e-3)

    def test_08_radial_deformation_source_naturality(self):
        U=states(70)
        Z=rad_states(70)
        for lam in (F(-3,4),F(0),F(2,7)):
            x=F();v=F()
            for n in range(1,70):
                x=16*x+forcing(n)+lam*pole(n,RADIAL)
                v=16*v+pole(n,RADIAL)
                self.assertEqual(x,U[n]+lam*Z[n])
                self.assertEqual(v,Z[n])

    def test_09_second_and_third_chronological_resonances(self):
        U=states(75)
        for n in (13,29,61):
            r1=forcing(n+1);r2=16*r1+forcing(n+2)
            self.assertEqual(16*U[n]-U[n+1],-r1)
            self.assertEqual(256*U[n]-U[n+2],-r2)
            self.assertEqual(16*U[n]-17*U[n+1]+U[n+2],r2-17*r1)
            # Last one has homogeneous charge 16-17*16+256=0.

    def test_10_root_grid_is_zero_to_bounded_observer(self):
        for q in (17,257):
            roots=[F(j,q) for j in range(q)]
            for h in (1,2,3,5,7):
                from cmath import exp
                from math import pi
                c=sum(exp(2j*pi*float(h*x)) for x in roots)/q
                self.assertLess(abs(c),2e-13)

if __name__=='__main__':unittest.main()
