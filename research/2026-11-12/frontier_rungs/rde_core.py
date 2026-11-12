#!/usr/bin/env python3
"""Exact kernel for RESTRICTED_EXPONENT.md (RDT-01 ... RDT-05).

Everything that carries a claim is exact (integers / fractions).  mpmath is used only
to *size* real numbers (|I_n|, distances to the nearest integer) at a working precision
that is checked against the size of the quantities involved.

Contents
--------
* valuations and S-parts of rationals;
* the restricted transference lemma RDT-01 as an executable inequality;
* exact linear forms:
    - tilted Legendre family for log 2         (RDT-05 theorem),
    - Dalzell family for pi                    (RDT-04),
    - even real family for pi                  (RDT-06, scout),
    - Gaussian one-pole family for pi          (RDT-06);
* rate functions of the tilted Legendre family (closed forms, no asymptotic fitting);
* continued fractions and the two-convergent decomposition of RDT-03.

Nothing here tests, or could test, an asymptotic claim about pi.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, gcd, log, sqrt
from typing import Iterable, Sequence

import mpmath as mp

# --------------------------------------------------------------------------------------
# valuations, S-parts
# --------------------------------------------------------------------------------------


def prime_factors(b: int) -> list[int]:
    out, p, m = [], 2, b
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def vp(x, p: int) -> int:
    """p-adic valuation of a nonzero rational."""
    x = F(x)
    if x == 0:
        raise ValueError("valuation of 0")
    e, n, d = 0, abs(x.numerator), x.denominator
    while n % p == 0:
        n //= p
        e += 1
    while d % p == 0:
        d //= p
        e -= 1
    return e


def s_part(x, primes: Iterable[int]) -> F:
    """Positive S-unit part of a nonzero rational: prod p^{v_p(x)} over p in S."""
    out = F(1)
    for p in primes:
        out *= F(p) ** vp(x, p)
    return out


def s_free(x, primes: Iterable[int]) -> F:
    """|x| divided by its S-part: a positive rational whose numerator and denominator
    are coprime to every p in S."""
    return abs(F(x)) / s_part(x, primes)


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_upto(n: int) -> int:
    out = 1
    for k in range(2, n + 1):
        out = lcm(out, k)
    return out


def odd_part(n: int) -> int:
    n = abs(int(n))
    while n and n % 2 == 0:
        n //= 2
    return n


# --------------------------------------------------------------------------------------
# RDT-01: the restricted transference lemma as an executable inequality
# --------------------------------------------------------------------------------------


def minimal_E(A, B, primes: Sequence[int]) -> F:
    """The least positive rational E with E*A, E*B in Z[1/b] whose S-free numerators are
    coprime (B != 0).  Any E admissible for RDT-01 would do; this one is the sharpest."""
    A, B = F(A), F(B)
    fa, fb = s_free(A, primes), (s_free(B, primes) if B != 0 else F(0))
    D = lcm(fa.denominator, fb.denominator) if B != 0 else fa.denominator
    na = (fa * D).numerator
    nb = (fb * D).numerator if B != 0 else 0
    return F(D, gcd(na, nb) if nb else na)


def transfer(A, B, I_abs, b: int, m: int, E=None, mode: str = "restricted", g: int = 1):
    """RDT-01 for the single form A*xi - B = I  (A, B exact rationals, |I| = I_abs > 0).

    Returns a dict with the S-unit u, the integer H = E|A|/u, the real Q = E|I|/u,
    g b^m Q, the flag `vanishing_possible` (g b^m B/A is an integer) and the certified
    lower bound for ||g b^m xi|| (None when the lemma is silent, i.e. g b^m Q >= 1).
    g >= 1 is an arbitrary fixed integer multiplier (denominators g*b^m, e.g. 15*16^m).

    mode = "restricted":   u_m = prod_p p^{min(v_p(EA), v_p(EB) + m v_p(b))}
    mode = "unrestricted": u   = prod_p p^{min(v_p(EA), v_p(EB))}   (the gcd of the
                           integer form; what the classical lemma uses for a general
                           denominator)
    mode = "mutant":       u_m of the restricted mode multiplied by b (a deliberately
                           false strengthening used as a mutation control)
    """
    A, B = F(A), F(B)
    primes = prime_factors(b)
    if E is None:
        E = minimal_E(A, B, primes)
    E = F(E)
    u = F(1)
    for p in primes:
        va = vp(E * A, p)
        if B == 0:
            e = va
        elif mode == "unrestricted":
            e = min(va, vp(E * B, p))
        else:
            e = min(va, vp(E * B * g, p) + m * vp(b, p))
        u *= F(p) ** e
    if mode == "mutant":
        u *= b
    H = abs(E * A) / u
    Q = mp.mpf(E.numerator) / E.denominator * I_abs / (mp.mpf(u.numerator) / u.denominator)
    bmQ = g * mp.mpf(b) ** m * Q
    ratio = g * F(b) ** m * B / A
    vanishing = ratio.denominator == 1
    Hf = mp.mpf(H.numerator) / H.denominator
    if bmQ < 1:
        bound = (1 - bmQ) / Hf
        if vanishing:
            bound = min(bound, bmQ / Hf)
    else:
        bound = None
    return dict(E=E, u=u, H=H, Q=Q, bmQ=bmQ, vanishing_possible=vanishing, bound=bound)


def dist_to_int(x):
    return abs(x - mp.nint(x))


# --------------------------------------------------------------------------------------
# polynomial helpers (integer coefficient lists, lowest degree first)
# --------------------------------------------------------------------------------------


def pmul(p: Sequence[int], q: Sequence[int]) -> list[int]:
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                out[i + j] += x * y
    return out


def ppow(p: Sequence[int], n: int) -> list[int]:
    out, base = [1], list(p)
    while n:
        if n & 1:
            out = pmul(out, base)
        n >>= 1
        if n:
            base = pmul(base, base)
    return out


# --------------------------------------------------------------------------------------
# the tilted Legendre family for log 2
#   I_n = int_0^1 x^{an} (1-x)^{bn} / (1+x)^{cn+1} dx = A_n log 2 - B_n
# --------------------------------------------------------------------------------------


def log2_form(a: int, b: int, c: int, n: int):
    """Exact (A_n, B_n) with I_n = A_n*log 2 - B_n, via t = 1 + x:
    I_n = int_1^2 (t-1)^{an} (2-t)^{bn} t^{-cn-1} dt."""
    an, bn, cn = a * n, b * n, c * n
    P = pmul(ppow([-1, 1], an), ppow([2, -1], bn))  # sum p_i t^i
    A = F(P[cn]) if cn < len(P) else F(0)
    S = F(0)
    for i, pi in enumerate(P):
        k = i - cn
        if k == 0 or pi == 0:
            continue
        S += pi * (F(2) ** k - 1) / k
    return A, -S


def log2_rates(a, b, c):
    """Closed-form rates of the tilted family (real weights allowed):
    alpha = -log max_{[0,1]} x^a (1-x)^b/(1+x)^c,
    logR  = log min_{rho>0} (1+rho)^a (2+rho)^b / rho^c   (Cauchy bound for |A_n|^{1/n}),
    Nstar = max(a+b-c, c)   (denominators),  gamma = max(b-c,0) log 2   (2-adic tilt)."""
    qa, qb, qc = c - a - b, -(b + c), a
    if abs(qa) < 1e-14:
        x0 = -qc / qb
    else:
        disc = qb * qb - 4 * qa * qc
        roots = [(-qb + sqrt(disc)) / (2 * qa), (-qb - sqrt(disc)) / (2 * qa)]
        x0 = [r for r in roots if 0 < r < 1][0]
    alpha = -(a * log(x0) + b * log(1 - x0) - c * log(1 + x0))
    # minimise f(rho) = a log(1+rho) + b log(2+rho) - c log rho ; f' = 0 is the quadratic
    # (a+b-c) rho^2 + (2a + b - 3c) rho - 2c = 0, with a unique positive root when a+b > c
    ra, rb, rc = a + b - c, 2 * a + b - 3 * c, -2 * c
    if ra <= 0:
        raise ValueError("need a + b > c (otherwise A_n = 0)")
    rho = (-rb + sqrt(rb * rb - 4 * ra * rc)) / (2 * ra)
    logR = a * log(1 + rho) + b * log(2 + rho) - c * log(rho)
    return dict(x0=x0, alpha=alpha, rho=rho, logR=logR, Nstar=max(a + b - c, c),
                gamma=max(b - c, 0) * log(2))


def log2_exponent(a, b, c):
    """The two quotients of RDT-05: (restricted, unrestricted) for the same forms.
    None when the classical criterion alpha > Nstar fails."""
    r = log2_rates(a, b, c)
    if r["alpha"] <= r["Nstar"]:
        return None, None
    res = (r["logR"] + r["Nstar"] - r["gamma"]) / (r["alpha"] - r["Nstar"] + r["gamma"])
    unr = (r["logR"] + r["Nstar"]) / (r["alpha"] - r["Nstar"])
    return res, unr


# --------------------------------------------------------------------------------------
# Dalzell family:  int_0^1 x^{4an} (1-x)^{4bn} / (1+x^2) dx = A_n*pi + B_n
# --------------------------------------------------------------------------------------


def dalzell_form(a: int, b: int, n: int):
    """Exact (A_n, B_n).  A_n is computed by honest polynomial division and must equal
    (-4)^{bn}/4 (RDT-04)."""
    N = pmul(ppow([0, 1], 4 * a * n), ppow([1, -1], 4 * b * n))
    # divide by 1 + x^2 (highest degree first)
    rem = list(N)
    quo = [0] * (len(N) - 2)
    for d in range(len(N) - 1, 1, -1):
        q = rem[d]
        quo[d - 2] = q
        rem[d] -= q
        rem[d - 2] -= q
    r0, r1 = rem[0], rem[1]
    # int_0^1 (r1 x + r0)/(1+x^2) = r1*log(2)/2 + r0*pi/4
    if r1 != 0:
        raise AssertionError("log 2 term present")
    B = sum(F(q, i + 1) for i, q in enumerate(quo))
    return F(r0, 4), B


def dalzell_criterion_value(a: float) -> float:
    """4H(a) + (1-a) log 4 for weights (a, 1-a): the quantity that would have to exceed 4
    (odd denominators up to 4(a+b)n, normalised a+b = 1) for the family to be usable."""
    return 4 * (-(a * log(a) + (1 - a) * log(1 - a))) + (1 - a) * log(4)


# --------------------------------------------------------------------------------------
# even real family (the parent's scout), kept for the record of the negative result
#   J_n = int_{-1}^{1} t^{2bn} (1-t^2)^{an} / (1+t^2)^{cn+1} dt = A_n*pi + B_n
# --------------------------------------------------------------------------------------


def even_pi_form(a: int, b: int, c: int, n: int):
    an, bn, m = a * n, b * n, c * n + 1
    P = pmul(ppow([-1, 1], bn), ppow([2, -1], an))  # in w = 1 + t^2
    gam, rho = {1: F(1, 4)}, {1: F(0)}
    for j in range(1, m + 1):
        gam[j + 1] = F(2 * j - 1, 2 * j) * gam[j]
        rho[j + 1] = F(1, 2 * j * 2 ** j) + F(2 * j - 1, 2 * j) * rho[j]
    A = B = F(0)
    for k, ck in enumerate(P):
        if ck == 0:
            continue
        if k < m:
            A += 2 * ck * gam[m - k]
            B += 2 * ck * rho[m - k]
        else:
            j = k - m
            B += ck * 2 * sum(F(comb(j, i), 2 * i + 1) for i in range(j + 1))
    return A, B


# --------------------------------------------------------------------------------------
# Gaussian one-pole family for pi
#   (1/i) int_{1-i}^{1+i} N(z)^n z^{-cn-1} dz = A_n*(pi/2) + B_n ,  N in Z[z]
#   (path crossing the positive real axis)
# --------------------------------------------------------------------------------------


def _im_pow(k: int) -> F:
    """Im((1+i)^k) for any integer k, exactly."""
    re, im = 1, 0
    for _ in range(abs(k)):
        re, im = re - im, re + im
    if k >= 0:
        return F(im)
    return F(-im, 2 ** (-k))


def gauss_form(N: Sequence[int], c: int, n: int):
    """Exact (A_n, B_n) with (1/i) * integral = A_n*(pi/2) + B_n.
    N is an integer polynomial (lowest degree first) with N(1+i) = 0 normally, but the
    identity holds for every N."""
    P = ppow(N, n)
    cn = c * n
    A = F(P[cn]) if cn < len(P) else F(0)
    B = F(0)
    for j, pj in enumerate(P):
        k = j - cn
        if k == 0 or pj == 0:
            continue
        B += pj * 2 * _im_pow(k) / k
    return A, B


def gauss_poly(a: int, mid: int, two: int, extra: Sequence[Sequence[int]] = ()) -> list[int]:
    """(z^2 - 2z + 2)^a (z - 1)^mid (z - 2)^two times optional extra integer factors."""
    P = pmul(pmul(ppow([2, -2, 1], a), ppow([-1, 1], mid)), ppow([-2, 1], two))
    for e in extra:
        P = pmul(P, list(e))
    return P


def form_metrics(Acoef, B, xi, primes: Sequence[int] = (2,)):
    """Finite-n bookkeeping for a form Acoef*xi + B = J (note the sign convention of the
    pi families).  Returns tau = v(A) - v(B) summed in log units, the classical
    (gcd-normalised integer) error e0 and height q0, and the restricted H and Q."""
    Acoef, B = F(Acoef), F(B)
    J = mp.mpf(Acoef.numerator) / Acoef.denominator * xi + mp.mpf(B.numerator) / B.denominator
    E = minimal_E(Acoef, B, primes)
    uA = s_part(E * Acoef, primes)
    uB = s_part(E * B, primes)
    lam = F(1)
    for p in primes:
        lam *= F(p) ** min(vp(E * Acoef, p), vp(E * B, p))
    q0 = abs(E * Acoef) / lam
    e0 = mp.mpf(E.numerator) / E.denominator * abs(J) / (mp.mpf(lam.numerator) / lam.denominator)
    H = abs(E * Acoef) / uA
    Q = mp.mpf(E.numerator) / E.denominator * abs(J) / (mp.mpf(uA.numerator) / uA.denominator)
    tau_log = float(mp.log(mp.mpf(uA.numerator) / uA.denominator) - mp.log(mp.mpf(uB.numerator) / uB.denominator))
    return dict(J=J, E=E, tau_log=tau_log, q0=q0, e0=e0, H=H, Q=Q)


def quotient(height, err):
    """log(height) / (-log(err)); None unless 0 < err < 1."""
    if not (0 < err < 1):
        return None
    h = mp.mpf(height.numerator) / height.denominator if isinstance(height, F) else mp.mpf(height)
    return float(mp.log(h) / (-mp.log(err)))


# --------------------------------------------------------------------------------------
# continued fractions and RDT-03
# --------------------------------------------------------------------------------------


def cf_convergents(x, count: int):
    """Partial quotients a_0.. and convergents (p_j, q_j), j = -1, 0, 1, ...; the returned
    lists are indexed so that conv[j + 1] = (p_j, q_j), conv[0] = (1, 0)."""
    a, conv = [], [(1, 0)]
    p_prev, q_prev, p, q = 0, 1, 1, 0  # (p_{-2}, q_{-2}), (p_{-1}, q_{-1})
    y = mp.mpf(x)
    for _ in range(count):
        ai = int(mp.floor(y))
        a.append(ai)
        p_prev, q_prev, p, q = p, q, ai * p + p_prev, ai * q + q_prev
        conv.append((p, q))
        frac = y - ai
        if frac == 0:
            break
        y = 1 / frac
    return a, conv


def two_convergent_decomposition(p: int, q: int, x, a, conv):
    """RDT-03(c).  For q >= 1 and p/q != x (x irrational, 0 < x, p >= 0) return
    (m, r, s, t) with (p, q) = r*(p_{m+1}, q_{m+1}) + s*(p_m, q_m)
                              = s*(p_{m+2}, q_{m+2}) - t*(p_{m+1}, q_{m+1}),
    r >= 0, s >= 1, t >= 1, r + t = s*a_{m+2}, where m is the largest index of the parity
    that puts p_m/q_m on the same side of x as p/q and not strictly between x and p/q."""
    above = mp.mpf(p) / q > x
    best = None
    j = -1 if above else 0
    while True:
        if j + 3 > len(conv) - 1:
            raise ValueError("not enough convergents supplied")
        pj, qj = conv[j + 1]
        ok = (p * qj <= pj * q) if above else (pj * q <= p * qj)  # p/q <= p_j/q_j  resp. >=
        if not ok:
            break
        best = j
        j += 2
    if best is None:
        raise ValueError("p/q < p_0/q_0: outside the range of the statement")
    m = best
    pm, qm = conv[m + 1]
    pm1, qm1 = conv[m + 2]
    pm2, qm2 = conv[m + 3]
    if above:
        r, s, t = q * pm - p * qm, p * qm1 - q * pm1, p * qm2 - q * pm2
    else:
        r, s, t = p * qm - q * pm, q * pm1 - p * qm1, q * pm2 - p * qm2
    assert (p, q) == (r * pm1 + s * pm, r * qm1 + s * qm)
    assert (p, q) == (s * pm2 - t * pm1, s * qm2 - t * qm1)
    assert r >= 0 and s >= 1 and t >= 1 and r + t == s * a[m + 2]
    return m, r, s, t


def hex_digits(x, count: int) -> list[int]:
    """First `count` hexadecimal digits of {x} (requires enough working precision)."""
    y = x - mp.floor(x)
    out = []
    for _ in range(count):
        y *= 16
        d = int(mp.floor(y))
        out.append(d)
        y -= d
    return out


# --------------------------------------------------------------------------------------
# prime savings for the tilted Legendre family (RDT-05)
# --------------------------------------------------------------------------------------


def log2_saving_segments(a: int, b: int, c: int):
    """The sub-intervals (lo, hi) of [0, 1) on which {a w} + {b w} < {c w}; the condition is
    1-periodic in w, and on each interval between consecutive multiples of 1/a, 1/b, 1/c it
    reads (a + b - c) w < floor(a w) + floor(b w) - floor(c w)."""
    from math import floor

    pts = sorted({F(k, d) for d in (a, b, c) for k in range(d + 1)})
    out = []
    for u, v in zip(pts[:-1], pts[1:]):
        mid = (u + v) / 2
        k = a + b - c
        rhs = floor(a * mid) + floor(b * mid) - floor(c * mid)
        if k > 0:
            lo, hi = u, min(v, F(rhs, k))
        elif k < 0:
            lo, hi = max(u, F(rhs, k)), v
        else:
            lo, hi = (u, v) if 0 < rhs else (u, u)
        if hi > lo:
            out.append((lo, hi))
    return out


def log2_saving(a: int, b: int, c: int, J: int = 60) -> F:
    """Exact rational lower bound s_J <= s for the saving
    s = int_{w >= 1/Nstar, {aw}+{bw}<{cw}} dw / w^2, using the translates j = 0..J-1 of the
    segments (all terms are positive, so every truncation is a valid lower bound)."""
    N = max(a + b - c, c)
    tot = F(0)
    for lo, hi in log2_saving_segments(a, b, c):
        for j in range(J):
            L, H = lo + j, hi + j
            if H <= F(1, N):
                continue
            L = max(L, F(1, N))
            tot += 1 / L - 1 / H
    return tot


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def log2_saved_primes(a: int, b: int, c: int, n: int) -> list[int]:
    """Odd primes p with p^2 > Nstar*n, p <= Nstar*n and (an mod p) + (bn mod p) < (cn mod p)."""
    N = max(a + b - c, c) * n
    return [p for p in range(3, N + 1, 2)
            if p * p > N and is_prime(p) and (a * n) % p + (b * n) % p < (c * n) % p]


def log2_Delta(a: int, b: int, c: int, n: int) -> int:
    """Delta_n = odd part of lcm(1..Nstar*n) divided by the saved primes (RDT-05, step 3)."""
    N = max(a + b - c, c) * n
    D = odd_part(lcm_upto(N))
    for p in log2_saved_primes(a, b, c, n):
        assert D % p == 0
        D //= p
    return D


def log2_exponent_with_saving(a: int, b: int, c: int, J: int = 60):
    """(restricted, unrestricted) quotients of RDT-05 with delta' = Nstar - s_J."""
    r = log2_rates(a, b, c)
    d = r["Nstar"] - float(log2_saving(a, b, c, J))
    if r["alpha"] <= d:
        return None, None
    return ((r["logR"] + d - r["gamma"]) / (r["alpha"] - d + r["gamma"]),
            (r["logR"] + d) / (r["alpha"] - d))


# --------------------------------------------------------------------------------------
# Rivoal 2007, eqs (1.3)-(1.6)   (CLASSICAL IMPORT; numerical evaluation of his formulas)
# --------------------------------------------------------------------------------------


def rivoal_L(kappa: float, a: int, b: int):
    """L(kappa, a, b) of Rivoal (1.6) for x = a/b, or None when kappa is not in his set
    script-L(a, b) = {kappa >= 1 : b^kappa e^kappa rho < 1}."""
    from math import e, exp

    x = a / b
    ax = abs(x)
    r0 = ((kappa - 1) * (x - 1) + sqrt((kappa - 1) ** 2 * (1 - x) ** 2 + 4 * kappa * (1 - x))) / (2 * kappa * ax)
    s = kappa * (1 + x) + 1 - x
    t0 = (s - sqrt(s * s - 4 * kappa * kappa * x)) / (2 * kappa * x)
    log_beta = kappa * log(1 + ax * r0) + log(1 - x + ax * r0) - log(ax * r0)
    log_rho = (kappa + 1) * log(ax) + kappa * log(t0) + log(1 - t0) - log(1 - x * t0)
    if kappa * log(abs(b)) + kappa + log_rho >= 0:
        return None
    return (log_beta - log_rho) / (-(log(abs(b)) + kappa + log_rho))


def rivoal_Lambda(a: int, b: int, kmax: float = 60.0, steps: int = 6000):
    """inf over kappa of L(kappa, a, b): coarse grid then golden-section refinement.
    Returns (Lambda, kappa) or None when the admissible set is empty on the grid."""
    best = None
    for i in range(steps + 1):
        k = 1 + (kmax - 1) * i / steps
        v = rivoal_L(k, a, b)
        if v is not None and (best is None or v < best[0]):
            best = (v, k)
    if best is None:
        return None
    h = (kmax - 1) / steps
    for _ in range(6):  # nested grids around the current best point
        lo, hi = max(1.0, best[1] - h), best[1] + h
        for i in range(201):
            k = lo + (hi - lo) * i / 200
            v = rivoal_L(k, a, b)
            if v is not None and v < best[0]:
                best = (v, k)
        h = (hi - lo) / 200
    return best


# --------------------------------------------------------------------------------------
# upper Pade table of log(1 - x)  (Rivoal 2007, Lemma 1; formulas from its proof)
# --------------------------------------------------------------------------------------


def pade_log_form(p: int, q: int, x):
    """Exact (Bhat(x), Ahat(x)) for p >= q >= 0 with
    Bhat(x)*log(1-x) - Ahat(x) = R(x) = O(x^{p+q+1}),
    Bhat(X) = sum_j (-1)^j C(q,j) C(p+j,q) X^{q-j}  in Z[X],
    Ahat(X) = sum_j sum_{k=1}^{j+p-q} (-1)^{j+1} C(q,j) C(p+j,q) X^{k+q-j}/k  in d_p^{-1} Z[X]."""
    x = F(x)
    Bv = Av = F(0)
    for j in range(q + 1):
        cj = (-1) ** j * comb(q, j) * comb(p + j, q)
        Bv += cj * x ** (q - j)
        for k in range(1, j + p - q + 1):
            Av += -cj * x ** (k + q - j) / k
    return Bv, Av


def pade_log_remainder_series(p: int, q: int, x, terms: int = 400):
    """R(x) from its hypergeometric series (-1)^{q+1} sum_k (k-q)_q/(k+p-q)_{q+1} x^{p+k},
    as an independent evaluation (mpmath)."""
    x = mp.mpf(F(x).numerator) / F(x).denominator
    tot = mp.mpf(0)
    for k in range(1, terms + 1):
        num = mp.mpf(1)
        for i in range(q):
            num *= k - q + i
        den = mp.mpf(1)
        for i in range(q + 1):
            den *= k + p - q + i
        tot += num / den * x ** (p + k)
    return (-1) ** (q + 1) * tot


def gauss_saving(a: int, mid: int, two: int, c: int, J: int = 60) -> F:
    """Rational lower bound for the prime saving of the Gaussian one-pole family
    N = (z^2-2z+2)^a (z-1)^mid (z-2)^two, pole order c (RDT-06(c)): the set
    {w >= 1/Nstar : 2{a w} + {mid w} + {two w} < {c w}} integrated against dw/w^2,
    truncated to the translates j < J of the segments in [0, 1)."""
    from math import floor

    weights = [(2, a)] + ([(1, mid)] if mid else []) + ([(1, two)] if two else [])
    N = max(c, 2 * a + mid + two - c)
    pts = sorted({F(k, w) for _, w in weights + [(1, c)] for k in range(w + 1)})
    tot = F(0)
    for u, v in zip(pts[:-1], pts[1:]):
        m_ = (u + v) / 2
        k = sum(d * w for d, w in weights) - c
        rhs = sum(d * floor(w * m_) for d, w in weights) - floor(c * m_)
        if k > 0:
            lo, hi = u, min(v, F(rhs, k))
        elif k < 0:
            lo, hi = max(u, F(rhs, k)), v
        else:
            lo, hi = (u, v) if 0 < rhs else (u, u)
        if hi <= lo:
            continue
        for j in range(J):
            L, H = lo + j, hi + j
            if H <= F(1, N):
                continue
            L = max(L, F(1, N))
            tot += 1 / L - 1 / H
    return tot


def gauss_saved_primes(a: int, mid: int, two: int, c: int, n: int) -> list[int]:
    N = max(c, 2 * a + mid + two - c) * n
    return [p for p in range(3, N + 1, 2)
            if p * p > N and is_prime(p)
            and 2 * ((a * n) % p) + (mid * n) % p + (two * n) % p < (c * n) % p]
