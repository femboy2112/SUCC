"""Short exact Fraction regression for SUCC Basel/C_N/source observer.

The full expanded 16-test independently executed local source is described in
RAW_TEST_LOGS.md. These are finite models, NOT pi-normality certificates.
"""
from fractions import Fraction as F
from math import prod
import unittest


def forcing(a):
    a = F(a)
    return 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5)


def w(n, mutant=False):
    a = 8*n-7
    r = F(15,a*(a+3)) if mutant else forcing(a)
    return F(a*a,15)*r


def weighted_trace(ws):
    """O(N) exact Kirchhoff/Green trace of an arbitrary weighted cycle."""
    n=len(ws)
    rr=[1/x for x in ws]
    total=sum(rr,F(0))
    ps=[F(0)]
    for a in rr[:-1]:
        ps.append(ps[-1]+a)
    p=sum(ps,F(0))
    linear=sum(((2*j-n+1)*ps[j] for j in range(n)),F(0))
    squares=n*sum((v*v for v in ps),F(0))-p*p
    return (total*linear-squares)/(n*total)


def cycle(n):
    return F(n*n-1,12)


def one_link(n,weight):
    t=weight-1
    return cycle(n)-t*F(n*n-1,12*(n+t*(n-1)))


def source_excess(n,mutant=False):
    return 1/w(n,mutant)-1


def det(A):
    A=[[F(v) for v in r] for r in A]
    n=len(A)
    result=F(1)
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:
            return F(0)
        if k!=j:
            A[j],A[k]=A[k],A[j]
            result=-result
        pivot=A[j][j]
        result*=pivot
        for i in range(j+1,n):
            mult=A[i][j]/pivot
            for ell in range(j+1,n):
                A[i][ell]-=mult*A[j][ell]
            A[i][j]=0
    return result


def magnetic_halfturn(ws):
    """Integer/rational N-cycle magnetic Laplacian at holonomy -1."""
    n=len(ws)
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    for j,ww in enumerate(ws):
        k=(j+1)%n
        sign=-1 if k==0 else 1
        M[j][j]+=ww
        M[k][k]+=ww
        M[j][k]-=sign*ww
        M[k][j]-=sign*ww
    return M


class BaselSourceObserver(unittest.TestCase):
    def test_universal_basel_and_bernoulli_grid(self):
        for n in range(3,40):
            self.assertEqual(cycle(n)/n**2,F(1,12)*(1-F(1,n*n)))
            for k in range(n):
                x=F(k,n)
                continuum=F(1,12)-x/2+x*x/2
                discrete=F(1,n)*(F(n*n-1,12*n)-F(k*(n-k),2*n))
                self.assertEqual(continuum-discrete,F(1,12*n*n))

    def test_single_link_exact_and_source_mutant(self):
        for n in range(3,50):
            for mutant in (False,True):
                source=w(n,mutant)
                self.assertGreater(source,0)
                self.assertLess(source,1)
                self.assertGreater(one_link(n,source)-cycle(n),0)
                self.assertLess(abs((one_link(n,source)-cycle(n))/n),F(2,n))

    def test_exact_twist_determinant(self):
        for n in range(3,9):
            for mutant in (False,True):
                ws=[w(j,mutant) for j in range(1,n+1)]
                self.assertEqual(det(magnetic_halfturn(ws)),4*prod(ws))

    def test_source_order_is_not_determinant(self):
        x=[F(1),F(2),F(3),F(4)]
        y=[F(1),F(3),F(2),F(4)]
        self.assertEqual(det(magnetic_halfturn(x)),det(magnetic_halfturn(y)))
        self.assertEqual(weighted_trace(x),F(29,50))
        self.assertEqual(weighted_trace(y),F(119,200))

    def test_native_source_resistance_harmonic_jets(self):
        for n in range(1,100):
            a=8*n-7
            delta=source_excess(n)
            self.assertEqual(delta,F(59*a*a+465*a+900,a*(15*a*a+121*a+240)))
            f=delta-F(59,120*n)
            self.assertGreater(f,0)
            self.assertLessEqual(f,F(4,n*n))
            self.assertEqual(source_excess(n,True),F(3,a))

    def test_perturbative_5_8_error_bound(self):
        for n in range(3,20):
            ws=[w(j) for j in range(1,n+1)]
            D=sum((1/z-1 for z in ws),F(0))
            actual=weighted_trace(ws)-cycle(n)
            linear=F(n*n-1,12*n)*D
            self.assertLessEqual(abs(actual-linear),F(5,8)*D*D)

    def test_open_line_and_critical_weak_seam(self):
        for n in (3,7,23,1000):
            self.assertEqual(one_link(n,F(0)),F(n*n-1,6))
            for c in (F(1),F(2),F(5,3)):
                scaled=(one_link(n,c/n)-cycle(n))/n**2
                self.assertLess(abs(scaled-F(1,12*(1+c))),F(1,n))

    def test_seed_affinity_is_not_source_conductance(self):
        for seed in (F(0),F(1,15),F(-1,17)):
            u=seed
            for n in range(1,13):
                u=16*u+forcing(8*n-7)
                v=sum((16**(n-j)*forcing(8*j-7) for j in range(1,n+1)),F(0))
                self.assertEqual(u-v,16**n*seed)

if __name__=='__main__':
    unittest.main(verbosity=2)
