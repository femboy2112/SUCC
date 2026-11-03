#!/usr/bin/env python3
"""Precision-safe verification of the within-cell cofiber structure.

All orbit/tail arithmetic in exact Fraction; pi-phase residue via mpmath at
adequate dps (dps >= 6*N/ln(10) + 60 firewall). No normality/RH claim.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 500  # ample for N up to ~2000


def r(n: int) -> Fraction:
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def T_tail(n: int, terms: int = 200) -> Fraction:
    """Exact tail T_n = sum_{j>=1} 16^{-j} r(n+j)."""
    s = Fraction(0)
    for j in range(1, terms + 1):
        s += Fraction(1, 16**j) * r(n + j)
    return s


def frac_pow16_pi(k: int) -> mp.mpf:
    """frac(16^k * pi), high precision."""
    x = mp.power(mp.mpf(16), k) * mp.pi
    return x - mp.floor(x)


def frac_U(n: int, terms: int = 200) -> mp.mpf:
    """{U_n} = {16^{n-1} pi - T_n} exactly (tail exact, phase high-precision)."""
    x = frac_pow16_pi(n - 1)
    t = T_tail(n, terms)
    val = x - (mp.mpf(t.numerator) / mp.mpf(t.denominator))
    return val - mp.floor(val)


def carry_indicator(n: int, terms: int = 200) -> int:
    """eps_n = 1[ {16^{n-1} pi} < T_n ]  (the wrap-around flag)."""
    x = frac_pow16_pi(n - 1)
    t = T_tail(n, terms)
    tt = mp.mpf(t.numerator) / mp.mpf(t.denominator)
    return 1 if x < tt else 0


def g_M(h: int, M: int) -> complex:
    """g_M(h) = int_0^1 e(h s / M) ds  (exact closed form)."""
    if h == 0:
        return 1.0 + 0j
    ph = 2 * mp.pi * mp.mpf(h) / mp.mpf(M)
    # (e^{i ph} - 1)/(i ph)
    return mp.mp.e ** (1j * ph) - 1


def build_decomposition(N: int, M: int, h: int, terms: int = 200):
    """Exact signed decomposition; returns cofiber, cell-imbalance, per-cell data."""
    pts = []          # (a_n, s_n) with s_n = M{U_n} - a_n in [0,1)
    for n in range(1, N + 1):
        fU = frac_U(n, terms)
        a = int(mp.floor(M * fU))
        s = M * fU - a
        pts.append((a, s))

    from collections import defaultdict
    count = defaultdict(int)
    for a, _ in pts:
        count[a] += 1

    p = {a: Fraction(count[a], N) for a in count}
    g = g_M(h, M)

    # w_{(a,h)} = (1/N) sum_{n:a_n=a} e(h s_n/M)
    w = {}
    for a in count:
        acc = mp.mpc(0)
        for aa, s in pts:
            if aa == a:
                acc += mp.e ** (1j * 2 * mp.pi * mp.mpf(h) * s / mp.mpf(M))
        w[a] = acc / mp.mpf(N)

    # d_{(a,h)} = w - p_a g_M(h)
    cofiber = mp.mpc(0)
    imbalance = mp.mpc(0)
    for a in count:
        d = w[a] - mp.mpf(p[a].numerator) / mp.mpf(p[a].denominator) * g
        cofiber += mp.e ** (1j * 2 * mp.pi * mp.mpf(h) * a / mp.mpf(M)) * d
        imbalance += (mp.e ** (1j * 2 * mp.pi * mp.mpf(h) * a / mp.mpf(M))
                      * (mp.mpf(p[a].numerator) / mp.mpf(p[a].denominator)
                         - mp.mpf(1) / mp.mpf(M)))

    return cofiber, imbalance, pts, p


if __name__ == "__main__":
    print("=== Cofiber decay in M (exact Fraction orbit/tail, N=512) ===")
    N = 512
    for h in (1, 5):
        print(f"\n--- h={h} ---")
        prev = None
        for M in (16, 32, 64, 128, 256):
            cof, imb, _, _ = build_decomposition(N, M, h)
            c = abs(complex(cof))
            print(f"  M={M:4d}: |cofiber|={c:.6f}   |cell-imb|={abs(complex(imb)):.6f}")
            prev = c

    print("\n=== Boundary-crossing (carry) count: sum eps_n ===")
    for Nc in (256, 512, 1024):
        tot = sum(carry_indicator(n) for n in range(1, Nc + 1))
        print(f"  N={Nc}: #carry-crossings = {tot}  (expect ~sum T_n ~ 0.016)")
