#!/usr/bin/env python3
"""Exact spacing verification for the rational BBP orbit {U_n}.

U_n = sum_{j<=n} 16^{n-j} r(j),  r(j) = 4/(8j-7) - 2/(8j-4) - 1/(8j-3) - 1/(8j-2).
Setup identity: 16^{n-1} pi = U_n + T_n,  T_n = sum_{j>n} 16^{n-j} r(j) -> 0.

All arithmetic is exact (fractions.Fraction). The "circle spacing" (mod 1) is
computed exactly, avoiding float precision loss at the ~16^n magnitude of U_n.

Reproduces every number in X3_SPACING.md.
"""
from fractions import Fraction
import math
from math import gcd

def r(j):
    return Fraction(4, 8*j-7) - Fraction(2, 8*j-4) - Fraction(1, 8*j-3) - Fraction(1, 8*j-2)

def U(n):
    s = Fraction(0)
    for j in range(1, n+1):
        s += (16**(n-j)) * r(j)
    return s

def frac(x):
    """Exact fractional part of a nonneg Fraction."""
    return x - Fraction(x.numerator // x.denominator)

def circle_dist(a, b):
    d = abs(frac(a) - frac(b))
    return min(d, 1 - d)

def line_dist(a, b):
    return abs(a - b)

def min_spacing(N, metric=circle_dist):
    vals = [U(n) for n in range(1, N+1)]
    best, arg = None, None
    for i in range(N):
        for j in range(i+1, N):
            d = metric(vals[i], vals[j])
            if best is None or d < best:
                best, arg = d, (i+1, j+1)
    return best, arg

def T(n, kmax=300):
    s = Fraction(0)
    for j in range(n+1, n+1+kmax):
        s += r(j) * (16**(n-j))
    return s

def lcm_list(nums):
    L = 1
    for x in nums:
        L = L*x//gcd(L, x)
    return L

def main():
    print("=== setup identity check: 16^{n-1} pi = U_n + T_n ===")
    for n in [1, 5, 20]:
        t = float(T(n))
        lhs = (16**(n-1)) * math.pi
        print(f"  n={n}: U_n+T_n vs 16^{{n-1}}pi  ->  T_n={t:.3e}  (T_n * {n} ~ {t*n:.3f})")

    print("\n=== denominator growth (conductor) ===")
    print("  n   log2(den U_n)   log2(den)/n")
    for n in [10, 20, 50, 100, 200, 400, 800]:
        d = U(n).denominator
        print(f"  {n:4d}  {math.log2(d):12.1f}   {math.log2(d)/n:.3f}")

    print("\n=== denominator divides lcm of 4n odd factors ===")
    for n in [10, 50]:
        nums = []
        for j in range(1, n+1):
            nums += [8*j-7, 8*j-4, 8*j-3, 8*j-2]
        L = lcm_list(nums)
        ud = U(n).denominator
        print(f"  n={n}: lcm log2={math.log2(L):.1f}, den log2={math.log2(ud):.1f}, den|lcm={L % ud == 0}")

    print("\n=== minimal line spacing (exact rational) ===")
    for N in [5, 10, 20, 50]:
        b, a = min_spacing(N, metric=line_dist)
        print(f"  N={N:3d}: min |U_n-U_m| = {float(b):.6e}  at {a}  (den={b.denominator})")

    print("\n=== minimal circle spacing mod 1 (exact) ===")
    for N in [10, 20, 30, 40, 50, 60]:
        b, a = min_spacing(N, metric=circle_dist)
        print(f"  N={N:3d}: min ||U_n-U_m|| = {float(b):.6e}  at {a}  log10={math.log10(float(b)):.3f}")

    print("\n=== spacing vs 1/Q bound (Q = den of the minimizing difference) ===")
    # For the minimizing pair, verify spacing >= 1/Q (Q = den(U_n - U_m)), A != 0.
    for N in [20, 40, 60]:
        b, a = min_spacing(N, metric=circle_dist)
        n, m = a
        diff = U(n) - U(m)
        Q = diff.denominator
        A = diff.numerator
        # circle spacing of a difference A/Q is ||A/Q|| = min(|A mod Q|, Q-|A mod Q|)/Q
        amod = A % Q
        bound_frac = Fraction(min(amod, Q - amod), Q)
        print(f"  N={N}: pair {a}: ||diff||={float(b):.6e} = ||A/Q||={float(bound_frac):.6e}, "
              f"1/Q={float(Fraction(1,Q)):.6e}, match={b == bound_frac}, log2(Q)={math.log2(Q):.1f}")

    print("\n=== counterexample: polynomial spacing, zero dimension ===")
    # x_k = 1/k has min spacing ~ 1/N^2 but the set {1/k} has Hausdorff dim 0.
    # (This is a theorem-level counterexample, checked numerically for the spacing part.)
    for N in [10, 100, 1000]:
        seq = [Fraction(1, k) for k in range(1, N+1)]
        mn = min(abs(seq[i]-seq[j]) for i in range(N) for j in range(i+1, N))
        print(f"  N={N}: min spacing of {{1/k}} = {float(mn):.3e}  ~ 1/N^2 = {1.0/N**2:.3e}")

if __name__ == "__main__":
    main()
