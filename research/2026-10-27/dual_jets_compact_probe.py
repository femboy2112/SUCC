"""Portable exact BBP dual-jet discriminant and modular-criticality receipt.

RESEARCH ONLY. Run: python research/2026-10-27/dual_jets_compact_probe.py
No stochastic, pi-normality, or RH inference.
"""
from math import factorial, isqrt

A = (16, -89, 120)
D = (21, -206, 712, -1024, 512)
W = (1427, -17744, 87800, -215040, 259584, -122880)


def ev(c, x):
    r = 0
    for a in c[::-1]:
        r = r * x + a
    return r


def deriv(c):
    return tuple(i * c[i] for i in range(1, len(c)))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return tuple(c)


def det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    previous, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((i for i in range(k + 1, n) if a[i][k]), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0, 'exact Bareiss failure'
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def res(a, b):
    n, m = len(a) - 1, len(b) - 1
    rows = [[0]*k + list(a[::-1]) + [0]*(m-k-1) for k in range(m)]
    rows += [[0]*k + list(b[::-1]) + [0]*(n-k-1) for k in range(n)]
    return det(rows)


def disc(a):
    n = len(a) - 1
    q, rem = divmod((-1)**(n*(n-1)//2)*res(a,deriv(a)),a[-1])
    assert rem == 0
    return q


def jet(a, d, x, p, kmax=3):
    aa, dd = [], []
    for cs, dst in ((a,aa),(d,dd)):
        for k in range(kmax+1):
            dst.append(ev(cs,x)*pow(factorial(k),-1,p)%p if cs else 0)
            cs = deriv(cs)
    inv = pow(dd[0],-1,p)
    c=[]
    for k in range(kmax+1):
        c.append((aa[k]-sum(dd[j]*c[k-j] for j in range(1,k+1)))*inv%p)
    return tuple(c)


def verify():
    apd=mul(deriv(A),D)
    adp=mul(A,deriv(D))
    assert W == tuple(x-y for x,y in zip(apd+(0,),adp))
    assert res(A,D)==-2**15*3**2*5**2
    assert disc(D)==2**24*3**2*5**2
    assert res(W,D)==-2**48*3**4*5**4
    p=52497217
    assert all(p%k for k in range(2,isqrt(p)+1))
    assert disc(W)==2**49*3**5*5**2*p
    assert jet(A,D,1,7)==(5,0,4,5)
    assert jet(A,D,5,7)==(1,0,1,6)
    x=22168154
    assert ev(D,x)%p and ev(W,x)%p==0 and ev(deriv(W),x)%p==0
    assert ev(deriv(deriv(W)),x)%p
    assert jet(A,D,x,p)==(34082935,0,0,5987934)
    return 'PASS: original BBP dual-W, exact resultant/discriminants, p7 and p52497217 higher jets'


if __name__ == '__main__':
    print(verify())
