#!/usr/bin/env python3
"""
Instrument B: INDEPENDENT second implementation of every CYC-01 quantity.
Differences from Instrument A (cyc01_instrument.py): no numpy, no sympy, no long-double; exact big-integer
remainder of the WHOLE truncated expansion (x = M/2^D, frac(b^j x) = ((M << s j) mod 2^D)/2^D, exact), phases
n*rem reduced mod 2^D in exact integers, trig in mpmath at stated dps; d_n by top-down lru_cache recursion with
trial-division factorisation (no shared code path with compute_D / factorint).
"""
import mpmath as mp
from functools import lru_cache

def trial_primes(n):
    ps, p = [], 2
    while p * p <= n:
        if n % p == 0:
            ps.append(p)
            while n % p == 0: n //= p
        p += 1 if p == 2 else 2
    if n > 1: ps.append(n)
    return ps

def cell_B(M, D, s, b, h, Rlist, Ns, dps):
    """M,D: x = M/2^D (binary, D bits). b = 2^s. returns {(R,N): dict of mpf}."""
    out = {}
    with mp.workdps(dps):
        P = int(dps * 3.33) + 48                        # phase kept to P bits (error 2^-P * n)
        Nmax = max(Ns)
        Wb = P + 64                                       # exact window width in bits (A uses 128); error of a phase n*frac < n*2^-Wb
        assert D - s * (Nmax - 1) >= Wb
        mask = (1 << Wb) - 1
        rems = [((M >> (D - s * j - Wb)) & mask) for j in range(Nmax)]    # exact bits s*j .. s*j+Wb of the expansion
        twopi = 2 * mp.pi
        @lru_cache(maxsize=None)
        def cpref(n):                                    # prefix sums of cos(2 pi n frac_j)
            acc, pref = mp.mpf(0), []
            for j in range(Nmax):
                u = (n * rems[j]) & mask
                acc += mp.cos(twopi * mp.mpf(u >> (Wb - P)) / mp.mpf(2) ** P)
                pref.append(acc)
            return pref
        def c(n, N): return cpref(n)[N - 1] / N
        @lru_cache(maxsize=None)
        def d(n, N):
            if n == 1: return mp.mpf(0)
            return min(d(n // p, N) + abs(c(n, N) - c(n // p, N)) for p in trial_primes(n))
        # |A|
        accC = mp.mpf(0); accS = mp.mpf(0); prefA = []
        for j in range(Nmax):
            u = (abs(h) * rems[j]) & mask
            ang = twopi * mp.mpf(u >> (Wb - P)) / mp.mpf(2) ** P
            accC += mp.cos(ang); accS += (1 if h > 0 else -1) * mp.sin(ang)
            prefA.append((accC, accS))
        for N in Ns:
            absA = mp.sqrt(prefA[N - 1][0] ** 2 + prefA[N - 1][1] ** 2) / N
            eta = max(mp.mpf(0), 2 * c(1, N))
            for R in Rlist:
                S = sum((R - dd) * d(abs(h) * (b ** dd - 1), N) for dd in range(1, R))
                T1 = mp.mpf(1) / R
                T2 = mp.mpf(R - 1) / (2 * R) * eta
                T3 = mp.mpf(2) / R ** 2 * S
                T4 = mp.mpf(2 * (R - 1) * (R - 2)) / (3 * R * N)
                rhs = mp.mpf(R - 1) / N + mp.sqrt(T1 + T2 + T3 + T4)
                out[(R, N)] = dict(absA=absA, eta=eta, S=S, T1=T1, T2=T2, T3=T3, T4=T4, RHS=rhs, GAP=rhs - absA)
    return out
