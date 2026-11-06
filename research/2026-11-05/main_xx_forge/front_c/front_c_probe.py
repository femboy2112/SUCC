#!/usr/bin/env python3
"""Front C probe: mixed angular-radial correlation, prime-Frobenius orientation,
pair exclusion versus global equidistribution.

Deterministic.  Writes FINITE_RECEIPT.json next to this file.  No pi digits are
input anywhere: the true orbit is the exact integer-LCM recurrence of the
original four-pole source with U_0 = 0; the Green tail T_n is the backward
recurrence T_n = (T_{n+1} + r(n+1))/16 in fixed point; hex digits of pi/16 are
the source's own integer carries.

All finite numbers are OBSERVED-finite calibrations.  Nothing here proves an
asymptotic statement; the proofs live in PROOFS.md.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from fractions import Fraction
from math import gcd, isqrt

K = 256                     # phase fixed point bits
KT = 320                    # tail fixed point bits
ONE = 1 << K
MASK = ONE - 1

ORIG_TAPS = (4, 0, 0, -2, -1, -1, 0, 0)
MUT_TAPS = (5, 0, 0, -2, -1, -1, 0, 0)          # one-pole mutant w_1: 4 -> 5
SHARP_TAPS = (0, 8, 4, 4, 0, 0, -1, 0)
F = Fraction
ANG_TAPS = tuple(F(2 * a + b, 4) for a, b in zip(ORIG_TAPS, SHARP_TAPS))
RAD_TAPS = tuple(F(2 * a - b, 4) for a, b in zip(ORIG_TAPS, SHARP_TAPS))

EPOCHS = (256, 512, 1024, 2048, 4096)
HS = (1, 3)
P_SHORT = 61
HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- source ----
def r_taps(w, n):
    """r_w(n) = sum_j w_j / (8(n-1)+j) as an exact Fraction."""
    tot = F(0)
    for j, wj in enumerate(w, start=1):
        if wj:
            tot += F(wj) / (8 * (n - 1) + j)
    return tot


def r_orig(n):
    return F(4, 8 * n - 7) - F(2, 8 * n - 4) - F(1, 8 * n - 3) - F(1, 8 * n - 2)


def exact_orbit(w, N, seed=F(0)):
    """Integer-LCM exact recurrence.  Returns (X, C, last) with
    X[n] = floor(2^K x_n), x_n = {U_n}, n = 0..N;  C[n] = floor(16 x_{n-1} + r(n))
    (the literal carry), n = 1..N;  last = (num, den) of x_N."""
    s = F(seed)
    D = s.denominator
    num = s.numerator % D
    X = [(num << K) // D]
    C = [s.numerator // D]
    for n in range(1, N + 1):
        q = r_taps(w, n)
        a, b = q.numerator, q.denominator
        D2 = D * (b // gcd(D, b))
        V = 16 * num * (D2 // D) + a * (D2 // b)
        c = V // D2
        num = V - c * D2
        D = D2
        X.append((num << K) // D)
        C.append(c)
    return X, C, (num, D)


def fraction_orbit(w, N, seed=F(0)):
    """Independent plain Fraction recurrence (unwrapped U_n), n = 0..N."""
    U = [F(seed)]
    for n in range(1, N + 1):
        U.append(16 * U[-1] + r_taps(w, n))
    return U


def tail_fixed(w, N, extra=64):
    """Tk[n] ~ 2^K T_n for n=0..N, T_n = sum_{j>=1} 16^{-j} r_w(n+j).
    Backward recurrence in KT bits; |2^K T_n - Tk[n]| < 1.01 (see PROOFS)."""
    T = 0
    out = [0] * (N + 1)
    for n in range(N + extra - 1, -1, -1):
        q = r_taps(w, n + 1)
        T = (T + ((q.numerator << KT) // q.denominator)) // 16
        if n <= N:
            out[n] = T >> (KT - K)
    return out


# ---------------------------------------------------------------- helpers ---
def frac01(v):
    """fixed-point int in [0, 2^K) -> float in [0,1) (53-bit truncation)."""
    return (v & MASK) / ONE


def echar(v, h):
    t = ((h * v) & MASK) >> (K - 53)
    ang = 2.0 * math.pi * (t / float(1 << 53))
    return complex(math.cos(ang), math.sin(ang))


def rnd(x, d=12):
    if isinstance(x, complex):
        return [rnd(x.real, d), rnd(x.imag, d)]
    if isinstance(x, float):
        if x == 0.0 or not math.isfinite(x):
            return x
        return float(f"{x:.{d}g}")
    return x


def pair_counts(points, W_list):
    """Ordered off-diagonal pairs with circular distance <= W (W < 2^(K-1))."""
    s = sorted(points)
    n = len(s)
    ext = s + [p + ONE for p in s]
    out = []
    for W in W_list:
        j = 0
        tot = 0
        for i in range(n):
            if j < i + 1:
                j = i + 1
            si = s[i]
            while j < i + n and ext[j] - si <= W:
                j += 1
            tot += j - i - 1
        out.append(2 * tot)
    return out


def max_occupancy(points, W):
    s = sorted(points)
    n = len(s)
    ext = s + [p + ONE for p in s]
    j = 0
    best = 0
    for i in range(n):
        if j < i:
            j = i
        while j < i + n and ext[j] - s[i] <= W:
            j += 1
        best = max(best, j - i)
    return best


def W_of(w):
    """nominal fixed-point threshold for a real width w (float)."""
    return int(F(w) * ONE)


def weyl_stats(points, h):
    terms = [echar(v, h) for v in points]
    S = 0j
    smax = 0.0
    for t in terms:
        S += t
        smax = max(smax, abs(S))
    A = len(points)
    return terms, S / A, smax


def mixed_stats(a, terms, smax):
    A = len(a)
    M = sum(ai * ti for ai, ti in zip(a, terms))
    R = sum(a)
    V = abs(a[-1]) + sum(abs(a[i + 1] - a[i]) for i in range(A - 1))
    bv_ok = abs(M) <= V * smax * (1 + 1e-9) + 1e-9
    return {"M": rnd(M / A), "absM": rnd(abs(M) / A), "R_radial_null": rnd(R / A),
            "V": rnd(V), "bv_bound": rnd(V * smax / A), "bv_holds": bool(bv_ok)}


def sieve_spf(n):
    spf = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(m, spf):
    out = []
    while m > 1:
        p = spf[m]
        out.append(p)
        m //= p
    return out


def base15_digits_sqrt2(M):
    """b_1..b_M = base-15 digits of sqrt(2)-1 (exact isqrt)."""
    v = isqrt(2 * 15 ** (2 * M)) - 15 ** M
    digs = []
    for _ in range(M):
        v, d = divmod(v, 15)
        digs.append(d)
    digs.reverse()
    return digs


# ------------------------------------------------------- C2 algebra ---------
def chi2(a):
    return 1 if a % 8 in (1, 7) else -1


def chim4(a):
    return 1 if a % 4 == 1 else -1


CHARS = {"1": lambda a: 1, "chi_-4": chim4, "chi_8": chi2,
         "chi_-8": lambda a: chim4(a) * chi2(a)}


def j_a(a, l):
    v = (a * l) % 8
    return 8 if v == 0 else v


def S_op(a, w):
    out = []
    for l in range(1, 9):
        j = j_a(a, l)
        out.append(F(chi2(a)) ** (8 - l) * F(2) ** ((j - l) // 2) * F(w[j - 1]))
    return tuple(out)


def proj(chiname, w):
    ch = CHARS[chiname]
    acc = [F(0)] * 8
    for a in (1, 3, 5, 7):
        Sw = S_op(a, w)
        for i in range(8):
            acc[i] += ch(a) * Sw[i]
    return tuple(x / 4 for x in acc)


def residue_pU(U, p):
    """p*U as a p-integral rational, reduced mod p."""
    v = U * p
    if v.denominator % p == 0:
        raise ValueError("not p-integral")
    return (v.numerator * pow(v.denominator, -1, p)) % p


# Q(zeta_8) as 4-tuples over Q in basis 1, z, z^2, z^3 with z^4 = -1
def qz_mul(x, y):
    r = [F(0)] * 7
    for i in range(4):
        if x[i]:
            for j in range(4):
                r[i + j] += x[i] * y[j]
    return tuple(r[i] - (r[i + 4] if i + 4 < 7 else 0) for i in range(4))


def qz_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def qz_scale(c, x):
    return tuple(c * a for a in x)


QZ_ONE = (F(1), F(0), F(0), F(0))
ZETA = (F(0), F(1), F(0), F(0))
SQRT2 = (F(0), F(1), F(0), F(-1))      # zeta + zeta^{-1} = zeta - zeta^3

BAKER_NAMES = ("log sqrt2", "log(1+sqrt2)", "Log(sqrt2+i)", "Log(sqrt2-i)",
               "Log(2-i)", "Log(2+i)", "i*pi/4")
# Lambda_k = Log(1 - zeta^{-k}/sqrt2) = sum_i BAKER_M[k][i] * ell_i
BAKER_M = (
    (-1, -1, 0, 0, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, 1),
    (-1, 0, 1, 0, 0, 0, 0),
    (-1, 0, 0, 0, 1, 0, 1),
    (-1, 1, 0, 0, 0, 0, 0),
    (-1, 0, 0, 0, 0, 1, -1),
    (-1, 0, 0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, -1),
)


def baker_coeffs(w):
    """c_i(w) in Q(zeta8): I(w) = sum_i c_i(w) ell_i, from
    L_j = -(1/8) sum_k t_k^j Lambda_k,  t_k = sqrt2 zeta^k."""
    tk = []
    zk = QZ_ONE
    for k in range(8):
        tk.append(qz_mul(SQRT2, zk))
        zk = qz_mul(zk, ZETA)
    coeffs = [(F(0),) * 4 for _ in range(7)]
    for k in range(8):
        pw = QZ_ONE
        acc = (F(0),) * 4
        for j in range(1, 9):
            pw = qz_mul(pw, tk[k])
            if w[j - 1]:
                acc = qz_add(acc, qz_scale(F(w[j - 1]), pw))
        for i in range(7):
            m = BAKER_M[k][i]
            if m:
                coeffs[i] = qz_add(coeffs[i], qz_scale(F(-m, 8), acc))
    return coeffs


def nullspace(rows, ncols):
    """Exact RREF nullspace over Q.  rows: list of lists of Fractions."""
    Mx = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(Mx)) if Mx[i][c] != 0), None)
        if p is None:
            continue
        Mx[r], Mx[p] = Mx[p], Mx[r]
        pv = Mx[r][c]
        Mx[r] = [v / pv for v in Mx[r]]
        for i in range(len(Mx)):
            if i != r and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [a - f * b for a, b in zip(Mx[i], Mx[r])]
        piv.append(c)
        r += 1
        if r == len(Mx):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -Mx[i][fc]
        basis.append(tuple(v))
    return basis


def period_matrix_rows():
    """28 x 8 rational matrix: w -> all Q-coordinates of the 7 Baker coefficients."""
    cols = []
    for j in range(8):
        e = [0] * 8
        e[j] = 1
        cs = baker_coeffs(e)
        cols.append([x for c in cs for x in c])
    return [[cols[j][i] for j in range(8)] for i in range(28)]


def rank_of(vectors):
    if not vectors:
        return 0
    n = len(vectors[0])
    return len(vectors) - len(nullspace([[v[i] for v in vectors] for i in range(n)], len(vectors)))


def span_intersection(B1, B2):
    """basis of span(B1) ∩ span(B2) in Q^8 (exact)."""
    if not B1 or not B2:
        return []
    n = len(B1[0])
    rows = [[b[i] for b in B1] + [-c[i] for c in B2] for i in range(n)]
    ns = nullspace(rows, len(B1) + len(B2))
    out = []
    for v in ns:
        vec = [F(0)] * n
        for k, b in enumerate(B1):
            for i in range(n):
                vec[i] += v[k] * b[i]
        if any(vec):
            out.append(tuple(vec))
    # reduce to independent set
    indep = []
    for v in out:
        if rank_of(indep + [v]) > len(indep):
            indep.append(v)
    return indep


def isotypic_basis(chiname):
    vecs = []
    for j in range(8):
        e = [0] * 8
        e[j] = 1
        v = proj(chiname, e)
        if any(v) and rank_of(vecs + [v]) > len(vecs):
            vecs.append(v)
    return vecs


def period_numeric(w, dps=40):
    """I(w) = sum_j w_j sum_k 16^-k/(8k+j), local precision only."""
    import mpmath as mpm
    with mpm.workdps(dps):
        tot = mpm.mpf(0)
        for j in range(8):
            if w[j]:
                fj = F(w[j])
                tot += mpm.mpf(fj.numerator) / fj.denominator * mpm.nsum(
                    lambda kk: mpm.mpf(16) ** (-kk) / (8 * kk + j + 1), [0, mpm.inf])
        return float(tot)


def baker_numeric_check():
    """Verify the Baker-basis log identities and periods numerically (local precision)."""
    import mpmath as mpm
    with mpm.workdps(60):
        s2 = mpm.sqrt(2)
        z = mpm.exp(1j * mpm.pi / 4)
        ell = [mpm.log(s2), mpm.log(1 + s2), mpm.log(s2 + 1j), mpm.log(s2 - 1j),
               mpm.log(2 - 1j), mpm.log(2 + 1j), 1j * mpm.pi / 4]
        worst = mpm.mpf(0)
        for k in range(8):
            lam = mpm.log(1 - z ** (-k) / s2)
            rep = sum(BAKER_M[k][i] * ell[i] for i in range(7))
            worst = max(worst, abs(lam - rep))

        def L_direct(j):
            return mpm.nsum(lambda kk: mpm.mpf(16) ** (-kk) / (8 * kk + j), [0, mpm.inf])

        def I_baker(w):
            cs = baker_coeffs(w)
            tot = mpm.mpc(0)
            for i in range(7):
                cv = sum(mpm.mpf(cs[i][m].numerator) / cs[i][m].denominator * z ** m for m in range(4))
                tot += cv * ell[i]
            return tot

        def I_direct(w):
            return sum(mpm.mpf(F(w[j]).numerator) / F(w[j]).denominator * L_direct(j + 1)
                       for j in range(8) if w[j])
        out = {"max_log_identity_error": float(worst)}
        for name, w in (("orig", ORIG_TAPS), ("sharp", SHARP_TAPS), ("radial", RAD_TAPS),
                        ("angular", ANG_TAPS), ("mutant", MUT_TAPS)):
            ib = I_baker(w)
            idr = I_direct(w)
            out[name] = {"I_direct": float(idr), "I_baker_re": float(mpm.re(ib)),
                         "I_baker_im_abs": float(abs(mpm.im(ib))),
                         "abs_diff": float(abs(ib - idr)),
                         "I_over_pi": float(idr / mpm.pi)}
        return out


# ===================================================================== main ==
def main(write=True, epochs=EPOCHS):
    receipt = {"probe": "front_c_probe.py", "K_bits": K, "KT_bits": KT,
               "epochs": list(epochs), "hs": list(HS), "no_pi_digits_input": True}
    with open(os.path.abspath(__file__), "rb") as fh:
        receipt["probe_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    Amax = max(epochs)
    Nmax = 2 * Amax + 64 + 2

    # ---------------- exact orbits and tails ----------------
    X, C, _ = exact_orbit(ORIG_TAPS, Nmax)
    Tk = tail_fixed(ORIG_TAPS, Nmax)
    Xm, Cm, _ = exact_orbit(MUT_TAPS, 2 * Amax)
    Tkm = tail_fixed(MUT_TAPS, 2 * Amax)
    # cross-check integer-LCM against plain Fractions
    Ufr = fraction_orbit(ORIG_TAPS, 300)
    xc = all(((Ufr[n] - (Ufr[n].numerator // Ufr[n].denominator)) * ONE).__floor__() == X[n]
             for n in range(301))
    cc = all(C[n] == (Ufr[n].numerator // Ufr[n].denominator) - 16 * (Ufr[n - 1].numerator // Ufr[n - 1].denominator)
             for n in range(1, 301))
    # tail bounds 0 < 1/(64n^2) - T_n < 1/(64 n^3) (CC-01) on the fixed point values
    tail_ok = all(-2 < F(ONE, 64 * n * n) - Tk[n] < F(ONE, 64 * n ** 3) + 2
                  for n in range(1, min(2000, len(Tk))))
    receipt["instrument"] = {"lcm_vs_fraction_phase_n<=300": xc, "carry_vs_fraction_n<=300": cc,
                             "tail_CC01_bounds_n<2000": tail_ok}

    def k_of_P(P):
        fu = 0
        for n in range(1, P + 1):
            fu = 16 * fu + C[n]
        s = X[P] + Tk[P]
        margin = abs(s - ONE)
        return fu + (1 if s >= ONE else 0), margin

    k61, mg61 = k_of_P(P_SHORT)
    receipt["source_hex_digits_first16"] = format(k_of_P(16)[0], "x")
    receipt["P_short_margin_ulps_log2"] = rnd(math.log2(mg61 + 1))

    spf = sieve_spf(16 * Amax + 200)

    C1 = {}
    C3 = {}
    kappa = math.log(15) / math.log(16)
    digs15 = base15_digits_sqrt2(2 * Amax + 200)

    for A in epochs:
        idx = range(A, 2 * A)
        # ---- control orbits (x = actual same-forcing real orbit, z = completed)
        xT = [X[n] for n in idx]
        zT = [(X[n] + Tk[n]) & MASK for n in idx]
        xC = [(ONE - Tk[n]) & MASK for n in idx]
        zC = [0 for n in idx]
        P = 2 * A + 64
        kP, mgP = k_of_P(P)
        Mden = 16 ** P - 1
        cur = (kP * pow(16, A, Mden)) % Mden
        zPL = []
        for n in idx:
            zPL.append((cur << K) // Mden)
            cur = (cur * 16) % Mden
        xPL = [(zPL[i] - Tk[n]) & MASK for i, n in enumerate(idx)]
        M61 = 16 ** P_SHORT - 1
        cur = (k61 * pow(16, A, M61)) % M61
        zPS = []
        for n in idx:
            zPS.append((cur << K) // M61)
            cur = (cur * 16) % M61
        xPS = [(zPS[i] - Tk[n]) & MASK for i, n in enumerate(idx)]
        fifth = ONE // 5
        xR = [(v + fifth) & MASK for v in xT]
        zR = [(v + fifth) & MASK for v in zT]
        xM = [Xm[n] for n in idx]
        zM = [(Xm[n] + Tkm[n]) & MASK for n in idx]
        # fifteen-symbol orbit: z_n = sum_{k>=1} b_{n+k} 16^{-k}, 64 digits exact
        z15 = []
        cur = 0
        for kk in range(1, 65):
            cur = (cur << 4) | digs15[A + kk - 1]
        for n in idx:
            z15.append(cur)
            cur = ((cur << 4) & MASK) | digs15[n + 64]
        x15 = [(z15[i] - Tk[n]) & MASK for i, n in enumerate(idx)]
        # invariance sanity: z_{n+1} = {16 z_n} up to fixed-point error
        inv_err = max(abs(((16 * zT[i]) & MASK) - zT[i + 1]) for i in range(A - 1))
        inv_err = min(inv_err, ONE - inv_err)

        ctrls_x = {"TRUE": xT, "COH": xC, "PER_LONG": xPL, "PER_SHORT": xPS, "ROT": xR,
                   "MUT": xM, "FIFTEEN": x15}
        ctrls_z = {"TRUE": zT, "COH": zC, "PER_LONG": zPL, "PER_SHORT": zPS, "ROT": zR,
                   "MUT": zM, "FIFTEEN": z15}

        # ============================ C1 =================================
        TA = [Tk[n] / ONE for n in idx]
        rA = [float(r_orig(n)) for n in idx]
        carryT = [C[n + 1] for n in idx]
        # carry identity on TRUE: c_{n+1} = d_{n+1} + 16 e_n - e_{n+1}, e_n = 1[x_n >= 1 - T_n]
        ev = {n: (X[n] + Tk[n] >= ONE) for n in range(A, 2 * A + 1)}
        evmargin = min(abs(X[n] + Tk[n] - ONE) for n in range(A, 2 * A + 1))
        dT = [((X[n] + Tk[n]) & MASK) >> (K - 4) for n in idx]
        dmargin = min(min(((X[n] + Tk[n]) & MASK) % (ONE >> 4), (ONE >> 4) - ((X[n] + Tk[n]) & MASK) % (ONE >> 4))
                      for n in idx)
        carry_id = all(carryT[i] == dT[i] + 16 * ev[n] - ev[n + 1] for i, n in enumerate(idx))
        n_events = sum(ev[n] for n in idx)
        # front_b CB-1: b_{n,m,k} = 1[S_m(n+k) <= x_{n+d} < S_d(n)] when S_d(n) < 1
        cb1 = {}
        dcrit = max(d for d in range(2, 9)
                    if sum(F(16) ** (d - i) * r_orig(A + i) for i in range(1, d + 1)) < 1)
        for (m_, k_) in ((1, 1), (2, 1), (1, 2), (dcrit - 1, 1), (dcrit - 2, 2)):
            d_ = m_ + k_
            agree = 0
            ones = 0
            adm = True
            for n in idx:
                Sk = sum(F(16) ** (k_ - i) * r_orig(n + i) for i in range(1, k_ + 1))
                Sd = sum(F(16) ** (d_ - i) * r_orig(n + i) for i in range(1, d_ + 1))
                Sm = sum(F(16) ** (m_ - i) * r_orig(n + k_ + i) for i in range(1, m_ + 1))
                if Sd >= 1:
                    adm = False
                    break
                theta = (X[n] << (4 * d_)) & MASK
                dl = 16 ** m_ * Sk
                dl = dl - (dl.numerator // dl.denominator)
                b_def = theta + ((dl.numerator << K) // dl.denominator) >= ONE
                y = X[n + d_]
                b_int = ((Sm.numerator << K) // Sm.denominator) <= y < ((Sd.numerator << K) // Sd.denominator)
                agree += b_def == b_int
                ones += b_def
            cb1[f"m={m_},k={k_}"] = {"admissible": adm, "agree": agree, "of": A, "branch_ones": ones}
        # COH carries: floor(16 x_n + r(n+1)) with x_n = 1 - T_n  -> 15
        rfixK = {n: (r_orig(n).numerator << K) // r_orig(n).denominator for n in range(A, 2 * A + 1)}
        carryC = [(16 * xC[i] + rfixK[n + 1]) >> K for i, n in enumerate(idx)]
        coh_carry15 = all(c == 15 for c in carryC)

        def carries_fixed(xs):
            return [(16 * xs[i] + rfixK[n + 1]) >> K for i, n in enumerate(idx)]

        lab_liou = []
        lab_prime = []
        lab_frob = []
        for n in idx:
            m = 8 * n - 7
            fs = factor(m, spf)
            lab_liou.append(float((-1) ** len(fs)))
            lab_prime.append(math.log(m) if len(fs) == 1 else 0.0)
            lab_frob.append(float(chim4(max(fs))))
        weights_common = {"T_over_TA": [t / TA[0] for t in TA], "r_over_rA": [x / rA[0] for x in rA],
                          "liouville_8n-7": lab_liou, "prime_8n-7_log": lab_prime,
                          "chi-4_of_Pplus(8n-7)": lab_frob}
        c1A = {}
        for h in HS:
            jcrit = max(0, int(math.floor(math.log(A * A * math.log(A) / h, 16))))
            Lam = h * 16 ** jcrit / A ** 2
            haar_carry = sum(d * (complex(math.cos(2 * math.pi * h * (d + 1) / 16), math.sin(2 * math.pi * h * (d + 1) / 16))
                                  - complex(math.cos(2 * math.pi * h * d / 16), math.sin(2 * math.pi * h * d / 16)))
                             for d in range(16)) / (2j * math.pi * h)
            hrow = {"j_crit": jcrit, "Lambda": rnd(Lam), "haar_mean_floor16z_e_hz": rnd(haar_carry)}
            for cname, xs in ctrls_x.items():
                terms, cmean, smax = weyl_stats(xs, h)
                row = {"c_A": rnd(cmean), "abs_c_A": rnd(abs(cmean)), "max_window_over_A": rnd(smax / A)}
                ws = dict(weights_common)
                if cname == "TRUE":
                    ws["carry_c_{n+1}"] = [float(c) for c in carryT]
                elif cname == "MUT":
                    ws["carry_c_{n+1}"] = [float(Cm[n + 1]) for n in idx]
                else:
                    ws["carry_c_{n+1}"] = [float(c) for c in carries_fixed(xs)]
                for wname, a in ws.items():
                    row[wname] = mixed_stats(a, terms, smax)
                # critical chirp weight: e(h 16^j U_n) = e(h U_{n+j}) e(-h S_j(n))
                if cname in ("TRUE", "COH", "ROT"):
                    xs_shift = []
                    chirp = []
                    for n in idx:
                        if cname == "TRUE":
                            xn, xnj = X[n], X[n + jcrit]
                        elif cname == "COH":
                            xn, xnj = (ONE - Tk[n]) & MASK, (ONE - Tk[n + jcrit]) & MASK
                        else:
                            xn, xnj = (X[n] + fifth) & MASK, (X[n + jcrit] + fifth) & MASK
                        Sj = (xnj - ((xn << (4 * jcrit)) & MASK)) & MASK
                        chirp.append(echar(-Sj & MASK, h))
                        xs_shift.append(xnj)
                    tsh, _, smax_sh = weyl_stats(xs_shift, h)
                    mst = mixed_stats(chirp, tsh, smax_sh)
                    hf = weyl_stats([((v << (4 * jcrit)) & MASK) for v in xs], h)[1]
                    mst["direct_high_freq_c_A(h16^j)"] = rnd(hf)
                    mst["identity_abs_err"] = rnd(abs(hf - (sum(c * t for c, t in zip(chirp, tsh)) / A)))
                    mst["V_over_Lambda"] = rnd(mst["V"] / Lam) if Lam else None
                    row["critical_chirp"] = mst
                hrow[cname] = row
            # theorem checks
            tr = hrow["TRUE"]
            co = hrow["COH"]
            checks = {}
            for wname in weights_common:
                a = weights_common[wname]
                bound = 2 * math.pi * h * sum(abs(ai) * t for ai, t in zip(a, TA)) / A
                mC = complex(*co[wname]["M"])
                checks["coh_collapse_" + wname] = abs(mC - co[wname]["R_radial_null"]) <= bound * (1 + 1e-6) + 1e-12
                mT = complex(*tr[wname]["M"])
                mR = complex(*hrow["ROT"][wname]["M"])
                rot = complex(math.cos(2 * math.pi * h / 5), math.sin(2 * math.pi * h / 5))
                checks["rot_phase_" + wname] = abs(mR - rot * mT) <= 1e-9
                mPL = complex(*hrow["PER_LONG"][wname]["M"])
                checks["per_long_equal_" + wname] = abs(mPL - mT) <= 1e-9
            checks["bv_all"] = all(hrow[c][w]["bv_holds"] for c in ctrls_x for w in hrow[c]
                                   if isinstance(hrow[c][w], dict) and "bv_holds" in hrow[c][w])
            hrow["theorem_checks"] = checks
            c1A[f"h={h}"] = hrow
        c1A["carry_identity_TRUE"] = carry_id
        c1A["frontB_CB1_check_TRUE"] = cb1
        c1A["correction_events_TRUE"] = n_events
        c1A["event_margin_log2_ulps"] = rnd(math.log2(evmargin + 1))
        c1A["digit_margin_log2_ulps"] = rnd(math.log2(dmargin + 1))
        c1A["COH_all_carries_15"] = coh_carry15
        c1A["MUT_carry_from_exact"] = True
        C1[f"A={A}"] = c1A

        # ============================ C3 =================================
        widths = {"A^-1": A ** -1.0, "A^-1.5": A ** -1.5, "A^-2": A ** -2.0,
                  "1/(64A^2)": 1.0 / (64 * A * A), "A^-2(logA)^-4": A ** -2.0 * math.log(A) ** -4,
                  "A^-2.5": A ** -2.5, "A^-3": A ** -3.0}
        Wn = [W_of(w) for w in widths.values()]
        c3A = {"z_invariance_err_ulps": inv_err}
        for orb, ctrls in (("x", ctrls_x), ("z", ctrls_z)):
            for cname, pts in ctrls.items():
                cnt = pair_counts(pts, Wn)
                c3A[f"{orb}:{cname}:pairs"] = dict(zip(widths.keys(), cnt))
        # single-scale budget lemma on completed z orbits
        lem = {}
        for cname, pts in ctrls_z.items():
            rowL = {}
            for dname, delta in (("A^-1/2", A ** -0.5), ("4/A", 4.0 / A)):
                Wb = W_of(2 * delta) + 8
                Bcount = pair_counts(pts, [Wb])[0] + A          # include diagonal
                B = Bcount / A ** 2
                ratio = B / (2 * delta)
                for h in HS:
                    J = int(math.floor(math.log(1.0 / (4 * delta * h), 16))) + 1
                    _, cz, _ = weyl_stats(pts, h)
                    bound = (math.pi / 2) * math.sqrt(max(ratio - 1, 0.0) / (2 * J)) + 2 * (J - 1) / A
                    rowL[f"{dname}:h={h}"] = {"B_over_2delta": rnd(ratio), "J": J,
                                              "abs_c": rnd(abs(cz)), "bound": rnd(bound),
                                              "holds": abs(cz) <= bound + 1e-12}
            lem[cname] = rowL
        c3A["single_scale_lemma"] = lem
        # GPB-2 occupancy (#501) on COH x-orbit and TRUE x-orbit
        wg = A ** -2.0 * math.log(A) ** -4
        c3A["GPB2_w"] = rnd(wg)
        for cname in ("COH", "TRUE", "FIFTEEN"):
            occ = max_occupancy(ctrls_x[cname], W_of(wg))
            c3A[f"GPB2_max_occupancy_{cname}"] = occ
            c3A[f"GPB2_occ_over_(A/logA)_{cname}"] = rnd(occ / (A / math.log(A)))
        c3A["COH_explicit_occupancy_bound_1+1024wA^3"] = rnd(1 + 1024 * wg * A ** 3)
        # 15-symbol bookkeeping
        c3A["fifteen_expected_scale_exponent_2/kappa"] = rnd(2 / kappa)
        c3A["fifteen_digitF_count_in_window"] = sum(1 for n in range(A + 1, 2 * A + 65) if digs15[n - 1] == 15)
        C3[f"A={A}"] = c3A

    # nu_15 Fourier coefficient at h=1 (Bernoulli 15-uniform)
    nu = 1 + 0j
    for kk in range(1, 40):
        t = 16.0 ** (-kk)
        nu *= sum(complex(math.cos(2 * math.pi * d * t), math.sin(2 * math.pi * d * t)) for d in range(15)) / 15
    receipt["nu15_hat_1"] = rnd(nu)
    receipt["nu15_hat_1_abs"] = rnd(abs(nu))
    receipt["kappa_log15_over_log16"] = rnd(kappa)
    receipt["C1"] = C1
    receipt["C3"] = C3

    # ============================ C2 =====================================
    c2 = {}
    # group law and characters
    basis = [tuple(F(int(i == j)) for i in range(8)) for j in range(8)]
    glaw = all(S_op(a, S_op(b, e)) == S_op((a * b) % 8, e) for a in (1, 3, 5, 7) for b in (1, 3, 5, 7) for e in basis)
    c2["group_law_S_aS_b=S_ab"] = glaw
    iso = {ch: isotypic_basis(ch) for ch in CHARS}
    c2["isotypic_dims"] = {ch: len(v) for ch, v in iso.items()}
    c2["orig=S1,S5 fixed"] = S_op(1, ORIG_TAPS) == tuple(map(F, ORIG_TAPS)) and S_op(5, ORIG_TAPS) == tuple(map(F, ORIG_TAPS))
    c2["S3 orig = -sharp/2"] = S_op(3, ORIG_TAPS) == tuple(F(-x, 2) for x in SHARP_TAPS)
    for nm, w in (("orig", ORIG_TAPS), ("mutant", MUT_TAPS), ("angular", ANG_TAPS), ("radial", RAD_TAPS)):
        c2[f"components_{nm}"] = {ch: [str(x) for x in proj(ch, w)] for ch in CHARS}
    c2["mutant_has_chi8_or_chi-8"] = any(proj("chi_8", MUT_TAPS)) or any(proj("chi_-8", MUT_TAPS))
    # exact kernel of the period functional via the Baker basis
    rows = period_matrix_rows()
    ker = nullspace(rows, 8)
    c2["ker_I_dim"] = len(ker)
    c2["ker_I_basis"] = [[str(x) for x in v] for v in ker]
    c2["radial_in_ker"] = rank_of(ker + [RAD_TAPS]) == len(ker)
    c2["orig_in_ker"] = rank_of(ker + [tuple(map(F, ORIG_TAPS))]) == len(ker)
    stable = all(rank_of(ker + [S_op(a, v)]) == len(ker) for a in (1, 3, 5, 7) for v in ker)
    c2["ker_I_S_a_stable"] = stable
    for ch, B in iso.items():
        inter = span_intersection(B, ker)
        c2[f"dim(ker_I ∩ E_{ch})"] = len(inter)
        c2[f"basis(ker_I ∩ E_{ch})"] = [[str(x) for x in v] for v in inter]
        # which Baker coordinates are hit by the period map on E_chi
        hit = set()
        for v in B:
            cs = baker_coeffs(v)
            for i in range(7):
                if any(cs[i]):
                    hit.add(BAKER_NAMES[i])
        c2[f"baker_support_E_{ch}"] = sorted(hit)
        c2[f"periods_E_{ch}"] = [{"w": [str(x) for x in v], "I(w)": rnd(period_numeric(v)),
                                  "baker_coeffs": {BAKER_NAMES[i]: [str(x) for x in baker_coeffs(v)[i]]
                                                   for i in range(7) if any(baker_coeffs(v)[i])}}
                                 for v in B]
    c2["L-C2_ker∩E_chi-4_is_zero"] = c2["dim(ker_I ∩ E_chi_-4)"] == 0
    c2["baker_numeric"] = baker_numeric_check()

    # Frobenius shadow: p U_{kp} == U^{S_a w}_k (mod p), and seed blindness
    maxn = 3 * 211 + 2
    shadow = {}
    Uorig0 = fraction_orbit(ORIG_TAPS, maxn)
    Uorig5 = [u + F(16) ** n / 5 for n, u in enumerate(Uorig0)]
    Uorig13 = [u + F(16) ** n / 13 for n, u in enumerate(Uorig0)]
    Umut = fraction_orbit(MUT_TAPS, maxn)
    Saw = {a: fraction_orbit(S_op(a, ORIG_TAPS), 3) for a in (1, 3, 5, 7)}
    Sam = {a: fraction_orbit(S_op(a, MUT_TAPS), 3) for a in (1, 3, 5, 7)}
    primes = [p for p in range(11, 212) if all(p % q for q in range(2, isqrt(p) + 1))]
    tot = ok_o = ok_m = ok_rot = rot_eq = 0
    vis13 = []
    for k in (1, 2, 3):
        for p in primes:
            if p <= 8 * k:
                continue
            a = p % 8
            lhs = residue_pU(Uorig0[k * p], p)
            rhs = (Saw[a][k].numerator * pow(Saw[a][k].denominator, -1, p)) % p
            tot += 1
            ok_o += lhs == rhs
            lm = residue_pU(Umut[k * p], p)
            rm = (Sam[a][k].numerator * pow(Sam[a][k].denominator, -1, p)) % p
            ok_m += lm == rm
            l5 = residue_pU(Uorig5[k * p], p)
            ok_rot += l5 == rhs
            rot_eq += l5 == lhs
            if p == 13:
                try:
                    vis13.append({"k": k, "seed0": lhs, "seed1/13": residue_pU(Uorig13[k * p], p)})
                except ValueError:
                    vis13.append({"k": k, "seed0": lhs, "seed1/13": "not p-integral (p*U has p in denominator)"})
    shadow.update({"eligible_pk": tot, "orig_pass": ok_o, "mutant_pass_universal_action": ok_m,
                   "rot_1/5_pass": ok_rot, "rot_shadow_equals_true": rot_eq, "seed_1/13_at_p=13": vis13})
    c2["frobenius_shadow"] = shadow
    # orientation gauge: w -> -w negates every residue, keeps |c_A(h)|
    c2["reflection_negates_residues"] = all(
        (residue_pU(-Uorig0[k * p], p) + residue_pU(Uorig0[k * p], p)) % p == 0
        for k in (1, 2) for p in primes if p > 8 * k)
    # non-invariance line w_t = p_ang + t p_rad, same completion pi/16
    line = {}
    A0 = 1024
    base_terms = {}
    for t in (-1, 0, 1, 2):
        wt = tuple(a + t * b for a, b in zip(ANG_TAPS, RAD_TAPS))
        Xt, _, _ = exact_orbit(wt, 2 * A0)
        pts = [Xt[n] for n in range(A0, 2 * A0)]
        row = {"chi-4_component": [str(x) for x in proj("chi_-4", wt)],
               "trivial_component": [str(x) for x in proj("1", wt)]}
        for h in HS:
            _, cm, _ = weyl_stats(pts, h)
            row[f"c_A(h={h})"] = rnd(cm)
            base_terms[(t, h)] = cm
        line[f"t={t}"] = row
    for t in (-1, 0, 2):
        for h in HS:
            d = abs(base_terms[(t, h)] - base_terms[(1, h)])
            bnd = 2 * math.pi * h * abs(t - 1) / (32 * A0 + 16)
            line[f"t={t}"][f"diff_vs_orig_h={h}"] = rnd(d)
            line[f"t={t}"][f"bound_h={h}"] = rnd(bnd)
            line[f"t={t}"][f"within_bound_h={h}"] = d <= bnd + 1e-12
    c2["line_p_ang+t*p_rad_A=1024"] = line
    receipt["C2"] = c2

    # ============================ verdict flags ===========================
    flags = {}
    flags["P-C1-1_bv_all_epochs"] = all(C1[a][f"h={h}"]["theorem_checks"]["bv_all"] for a in C1 for h in HS)
    flags["P-C1-2_coh_collapse"] = all(v for a in C1 for h in HS for kk, v in C1[a][f"h={h}"]["theorem_checks"].items() if kk.startswith("coh_collapse"))
    flags["P-C1-3_rot_phase"] = all(v for a in C1 for h in HS for kk, v in C1[a][f"h={h}"]["theorem_checks"].items() if kk.startswith("rot_phase"))
    flags["P-C1-4_per_long"] = all(v for a in C1 for h in HS for kk, v in C1[a][f"h={h}"]["theorem_checks"].items() if kk.startswith("per_long"))
    flags["P-C1-5_carry_identity"] = all(C1[a]["carry_identity_TRUE"] and C1[a]["COH_all_carries_15"] for a in C1)
    flags["frontB_CB1_agrees_TRUE"] = all(v["admissible"] and v["agree"] == v["of"] for a in C1 for v in C1[a]["frontB_CB1_check_TRUE"].values())
    flags["P-C1-6_no_events_TRUE"] = all(C1[a]["correction_events_TRUE"] == 0 for a in C1)
    p7 = True
    for a in C1:
        Aval = int(a.split("=")[1])
        for h in HS:
            row = C1[a][f"h={h}"]
            p7 &= row["TRUE"]["liouville_8n-7"]["absM"] <= 0.25 and row["COH"]["liouville_8n-7"]["absM"] <= 0.25
            if Aval >= 256:
                p7 &= row["TRUE"]["prime_8n-7_log"]["absM"] / abs(row["TRUE"]["prime_8n-7_log"]["R_radial_null"]) <= 0.35
    flags["P-C1-7_observational"] = p7
    flags["P-C2-1_shadow_orig_and_mutant"] = shadow["orig_pass"] == shadow["eligible_pk"] == shadow["mutant_pass_universal_action"]
    flags["P-C2-2_seed_blind_1/5"] = shadow["rot_shadow_equals_true"] == shadow["eligible_pk"]
    flags["P-C2-3_mutant_impure"] = c2["mutant_has_chi8_or_chi-8"]
    flags["P-C2-4_L-C2"] = c2["L-C2_ker∩E_chi-4_is_zero"]
    flags["P-C2-5_ker_stable"] = c2["ker_I_S_a_stable"]
    flags["P-C2-6_line_within_bound"] = all(v for t in line.values() for kk, v in t.items() if kk.startswith("within_bound"))
    flags["P-C3-1_lemma_holds"] = all(r["holds"] for a in C3 for c in C3[a]["single_scale_lemma"].values() for r in c.values())
    flags["P-C3-2_fifteen_zero_pairs_A^-2.5"] = all(C3[a]["z:FIFTEEN:pairs"]["A^-2.5"] == 0 for a in C3)
    flags["P-C3-2_fifteen_c1_band"] = all(0.03 <= C1[a]["h=1"]["FIFTEEN"]["abs_c_A"] <= 0.11 for a in C1 if int(a.split("=")[1]) >= 512)
    flags["P-C3-3_true_le2_pairs_A^-2.5"] = all(C3[a]["z:TRUE:pairs"]["A^-2.5"] <= 2 and C3[a]["x:TRUE:pairs"]["A^-2.5"] <= 2 for a in C3)
    flags["P-C3-4_coh_all_pairs_1/(64A^2)"] = all(C3[a]["x:COH:pairs"]["1/(64A^2)"] == int(a.split("=")[1]) * (int(a.split("=")[1]) - 1) for a in C3)
    flags["P-C3-6_per_short_collisions"] = all(C3[a]["z:PER_SHORT:pairs"]["A^-3"] >= int(a.split("=")[1]) ** 2 // 61 - int(a.split("=")[1]) for a in C3)
    flags["P-C3-7_rot_equals_true_x"] = all(C3[a]["x:ROT:pairs"] == C3[a]["x:TRUE:pairs"] for a in C3)
    flags["P-C3-8_per_long_equals_true_z"] = all(C3[a]["z:PER_LONG:pairs"] == C3[a]["z:TRUE:pairs"] for a in C3)
    receipt["preregistered_flags"] = flags

    if write:
        with open(os.path.join(HERE, "FINITE_RECEIPT.json"), "w") as fh:
            json.dump(receipt, fh, indent=1, sort_keys=True, ensure_ascii=False)
            fh.write("\n")
    return receipt


if __name__ == "__main__":
    rec = main()
    for k, v in rec["preregistered_flags"].items():
        print(f"{k}: {v}")
    sys.exit(0)
