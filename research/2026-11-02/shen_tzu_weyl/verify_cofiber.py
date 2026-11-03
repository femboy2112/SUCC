#!/usr/bin/env python3
"""Precision-safe verification: within-cell cofiber of the signed Weyl decomposition.

Two computations:
  (1) exact decomposition and cofiber magnitude vs M (reproduces parent's table),
  (2) tail-leg vs pi-phase-leg separation of the cofiber (supports claim ledger C3/C4).

All orbit/tail arithmetic exact Fraction; pi-phase residue mpmath at dps=2000
(firewall: need ~6*N/ln(10)+60 digits for frac(16^{n-1} pi)). No normality/RH claim.
"""
from fractions import Fraction
from collections import defaultdict
import mpmath as mp

mp.mp.dps = 2000


def r(n: int) -> Fraction:
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def T_tail(n: int, terms: int = 300) -> Fraction:
    s = Fraction(0)
    for j in range(1, terms + 1):
        s += Fraction(1, 16**j) * r(n + j)
    return s


def frac_pow16_pi(k: int) -> mp.mpf:
    x = mp.power(mp.mpf(16), k) * mp.pi
    return x - mp.floor(x)


def frac_U(n: int, terms: int = 300) -> mp.mpf:
    x = frac_pow16_pi(n - 1)
    t = T_tail(n, terms)
    val = x - (mp.mpf(t.numerator) / mp.mpf(t.denominator))
    return val - mp.floor(val)


def g_M(h: int, M: int) -> mp.mpc:
    if h == 0:
        return mp.mpf(1)
    ph = 2 * mp.pi * mp.mpf(h) / mp.mpf(M)
    return (mp.e ** (1j * ph) - 1) / (1j * ph)


def e_h(x: mp.mpf, h: int) -> mp.mpc:
    return mp.e ** (1j * 2 * mp.pi * mp.mpf(h) * x)


def decompose(N: int, M: int, h: int, terms: int = 300):
    pts = []
    for n in range(1, N + 1):
        fU = frac_U(n, terms)
        a = int(mp.floor(M * fU))
        s = M * fU - a
        pts.append((a, s))
    cnt = defaultdict(int)
    for a, _ in pts:
        cnt[a] += 1
    p = {a: Fraction(cnt[a], N) for a in cnt}
    g = g_M(h, M)
    w = {}
    for a in cnt:
        acc = mp.mpc(0)
        for aa, s in pts:
            if aa == a:
                acc += e_h(s / mp.mpf(M), h)
        w[a] = acc / mp.mpf(N)
    cofiber = mp.mpc(0)
    imbalance = mp.mpc(0)
    for a in cnt:
        pa = mp.mpf(p[a].numerator) / mp.mpf(p[a].denominator)
        ph = e_h(a / mp.mpf(M), h)
        cofiber += ph * (w[a] - pa * g)
        imbalance += ph * (pa - mp.mpf(1) / mp.mpf(M))
    imbalance *= g
    return cofiber, imbalance


def tail_leg_and_pi_leg(N: int, M: int, h: int, terms: int = 300):
    """Separate cofiber into (a) tail-driven first moment, (b) pi-phase first moment."""
    pts = []
    for n in range(1, N + 1):
        fU = frac_U(n, terms)
        a = int(mp.floor(M * fU))
        s = M * fU - a
        # s_n = sigma_n - M*T_n  (bulk); sigma_n = M x_n - floor(M x_n)
        x = frac_pow16_pi(n - 1)
        sig = M * x - mp.floor(M * x)
        t = T_tail(n, terms)
        tt = mp.mpf(t.numerator) / mp.mpf(t.denominator)
        pts.append((a, s, sig, M * tt))
    cnt = defaultdict(int)
    for a, *_ in pts:
        cnt[a] += 1
    # Taylor: e(h s/M) - g_M(h) ~ 2pi i h/M (s - 1/2) + ...
    coef = 2 * mp.pi * 1j * mp.mpf(h) / mp.mpf(M)
    tail_leg = mp.mpc(0)
    pi_leg = mp.mpc(0)
    for a in cnt:
        acc_t = mp.mpc(0)
        acc_p = mp.mpc(0)
        for aa, s, sig, MT in pts:
            if aa == a:
                acc_t += coef * (-MT) / mp.mpf(N)       # -M T_n term
                acc_p += coef * (sig - mp.mpf('0.5')) / mp.mpf(N)  # sigma - 1/2
        ph = e_h(a / mp.mpf(M), h)
        tail_leg += ph * acc_t
        pi_leg += ph * acc_p
    return tail_leg, pi_leg


if __name__ == "__main__":
    print("=== (1) Cofiber vs M, exact Fraction orbit/tail, N=512 ===")
    N = 512
    for h in (1, 5):
        print(f"--- h={h} ---")
        for M in (16, 64, 256):
            c, imb = decompose(N, M, h)
            print(f"  M={M:4d}: |cofiber|={abs(complex(c)):.6f}  |g*cell-imb|={abs(complex(imb)):.6f}")

    print("\n=== (2) Tail-leg vs pi-phase-leg of cofiber (first-moment Taylor), N=512 ===")
    for h in (1, 5):
        for M in (16, 256):
            tl, pl = tail_leg_and_pi_leg(N, M, h)
            print(f"  h={h} M={M}: |tail-leg|={abs(complex(tl)):.6f}  |pi-leg|={abs(complex(pl)):.6f}")

    print("\n=== (3) Boundary-crossing count (eps_n) — should be ~0 for these n ===")
    for Nc in (256, 512, 1024):
        tot = 0
        for n in range(1, Nc + 1):
            x = frac_pow16_pi(n - 1)
            t = T_tail(n)
            if x < (mp.mpf(t.numerator) / mp.mpf(t.denominator)):
                tot += 1
        print(f"  N={Nc}: #carry = {tot}")
