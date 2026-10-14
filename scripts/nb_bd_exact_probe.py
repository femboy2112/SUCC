"""Probe: NB/BD finite table. mpmath 60 dps (NOT interval; Observed, not a sec-8 certificate). Read-only, writes nothing."""
from fractions import Fraction as F
from math import lcm
import mpmath as mp
mp.mp.dps = 60

def rr(m, n):
    L = lcm(m, n); tot = mp.mpf(0)
    for r in range(1, L):
        c = mp.mpf((r % m) * (r % n)) / (m * n)
        if c:
            tot += c * (mp.digamma(mp.mpf(r + 1) / L) - mp.digamma(mp.mpf(r) / L)) / L
    return tot

def beta(m):
    s = mp.mpf(0)
    for r in range(1, m):
        s += r * (mp.loggamma(mp.mpf(r) / m) - mp.loggamma(mp.mpf(r + 1) / m) + mp.digamma(mp.mpf(r + 1) / m) / m)
    return s / m

def dist_E(N):
    ns = list(range(2, N + 1))
    G = mp.matrix(len(ns), len(ns)); b = mp.matrix(len(ns), 1)
    for i, m in enumerate(ns):
        b[i] = mp.log(m) / m
        for j, n in enumerate(ns):
            G[i, j] = rr(m, n)
    return 1 - (b.T * mp.lu_solve(G, b))[0]

def dist_D(N, extra_inf=True):
    ns = list(range(1, N + 1))
    kappa = mp.log(2 * mp.pi) - mp.euler - 1
    G = mp.matrix(N, N); b = mp.matrix(N, 1)
    for i, m in enumerate(ns):
        b[i] = (mp.log(m) + 1 - mp.euler) / m
        for j, n in enumerate(ns):
            r = rr(m, n) if (m > 1 and n > 1) else mp.mpf(0)
            G[i, j] = r + (beta(m) if m > 1 else 0) / n + (beta(n) if n > 1 else 0) / m + kappa / (m * n) + (mp.mpf(1) / (m * n) if extra_inf else 0)
    return 1 - (b.T * mp.lu_solve(G, b))[0]

def mobius(n):
    r, p, x = 1, 2, n
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0: return 0
            r = -r
        p += 1
    if x > 1: r = -r
    return r

def Mert(k): return sum(mobius(i) for i in range(1, k + 1))

def interp(K, k, mK):
    # SUCC source-first interpolant: -mu(n) on clocks n<=K, plus (K+1)*m_K on clock K+1; clock_n(k)=(k mod n)/n
    v = -sum(F(mobius(n) * (k % n), n) for n in range(1, K + 1))
    return v + (K + 1) * mK * F(k % (K + 1), K + 1)

if __name__ == "__main__":
    c = mp.log(2 * mp.pi) - mp.euler
    print("constant log(2pi)-gamma =", mp.nstr(c, 12))
    print("N   E*_N(SUCC constrained)        D_N(classical L2(0,inf))      E/D")
    for N in range(2, 13):
        E, D = dist_E(N), dist_D(N)
        assert D < E <= c * D
        print("%-3d %-29s %-29s %s" % (N, mp.nstr(E, 22), mp.nstr(D, 22), mp.nstr(E / D, 8)))
    for K in (13, 30):
        mK = sum(F(mobius(n), n) for n in range(1, K + 1)); tot = mp.mpf(0)
        for k in range(1, 20001):
            e = 1 - interp(K, k, mK)
            tot += mp.mpf(e.numerator) ** 2 / e.denominator ** 2 / (k * (k + 1))
        print("source-first interpolant K=%d: l2 residual partial-sum lower bound (k<=20000) = %s" % (K, mp.nstr(tot, 10)))
