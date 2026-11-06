"""oracle_b.py - INDEPENDENT pure-integer instrument for the carry-transport probe.

No Fraction objects, no mpmath.  Everything is a Python big integer over a common
denominator D = lcm of every pole denominator (and the seed denominator).

Contents
  * SPEC / MUTANT forcing specs (poles given as (num, den, off): num/(den*(8n-off)))
  * IntOracle: exact U_n numerators, repo definition (theta, delta, b) by integer mod,
    CB-1 claim (interval test) by integer comparison, per-triple tallies.
  * tail_intervals: rigorous fixed-point (2^400) enclosures of the Green tail T_n
    by the backward recurrence T_n = (T_{n+1} + r(n+1))/16 with outward rounding.
  * pi_hex_digits: independent integer Chudnovsky (binary splitting) for pi hex digits.
"""
import hashlib
import math
import sys

sys.setrecursionlimit(10000)

SC_BITS = 400
SC = 1 << SC_BITS

SOURCE = dict(name="source", poles=[(4, 1, 7), (-2, 1, 4), (-1, 1, 3), (-1, 1, 2)],
              const=(0, 1), sign=1, alt=False)


def mutant_specs():
    return {
        "M1_pole4to5": dict(name="M1_pole4to5", poles=[(5, 1, 7), (-2, 1, 4), (-1, 1, 3), (-1, 1, 2)],
                            const=(0, 1), sign=1, alt=False),
        "M2_const_1_1000": dict(name="M2_const_1_1000", poles=[], const=(1, 1000), sign=1, alt=False),
        "M3_unforced": dict(name="M3_unforced", poles=[], const=(0, 1), sign=1, alt=False),
        "M4_negated": dict(name="M4_negated", poles=SOURCE["poles"], const=(0, 1), sign=-1, alt=False),
        "M5_alternating": dict(name="M5_alternating", poles=SOURCE["poles"], const=(0, 1), sign=1, alt=True),
    }


def _denoms(spec, n):
    out = [den * (8 * n - off) for (_, den, off) in spec["poles"]]
    out.append(spec["const"][1])
    return out


def common_denominator(spec, nmax, extra=1):
    D = extra
    for n in range(1, nmax + 1):
        for q in _denoms(spec, n):
            D = D * q // math.gcd(D, q)
    return D


def R_int(spec, D, n):
    """D * r(n) as an exact integer (D must be divisible by every denominator)."""
    tot = 0
    for (num, den, off) in spec["poles"]:
        tot += num * (D // (den * (8 * n - off)))
    tot += spec["const"][0] * (D // spec["const"][1])
    tot *= spec["sign"]
    if spec["alt"] and (n & 1):
        tot = -tot
    return tot


def digest_bits(bits):
    return hashlib.sha256(bytes(bits)).hexdigest()[:16]


class IntOracle:
    """Exact integer oracle for one (spec, seed=(p,q), epoch A)."""

    def __init__(self, spec, A, dcap, seed=(0, 1)):
        self.spec = spec
        self.A = A
        self.dcap = dcap
        self.p, self.q = seed
        self.nlast = 2 * A - 1 + dcap + 2          # last index at which x is needed
        self.D = common_denominator(spec, self.nlast + dcap + 2, extra=self.q)
        D = self.D
        self.sd = D // self.q
        # stream N_n (U_n numerator over D) up to nlast; keep X_n = (N_n + seedpart) mod D on the window
        N = 0
        self.X = {}
        for n in range(1, self.nlast + 1):
            N = 16 * N + R_int(spec, D, n)
            if n >= A:
                self.X[n] = (N + ((self.p * pow(16, n, self.q)) % self.q) * self.sd) % D

    def R(self, n):
        return R_int(self.spec, self.D, n)

    def row(self, n):
        """S_d(n)*D for d=0..dcap via S_d = 16 S_{d-1} + R_{n+d}."""
        r = [0]
        s = 0
        for d in range(1, self.dcap + 1):
            s = 16 * s + self.R(n + d)
            r.append(s)
        return r

    def run(self, hook=None):
        A, D, dcap = self.A, self.D, self.dcap
        triples = [(m, d - m) for d in range(2, dcap + 1) for m in range(1, d)]
        rec = {t: dict(nadm=0, mm_b_adm=0, mm_d_adm=0, mm_b_inadm=0, mm_d_inadm=0, n_inadm=0,
                       sum_b=0, sum_deltaD=0, min_margin=None, min_margin_n=None,
                       bits_def=bytearray(), bits_claim=bytearray(), examples=[],
                       cls=dict(Sm_neg=0, Sd_ge1=0, Sd_neg=0, Sm_gt_Sd=0)) for t in triples}
        rows = {}
        p16 = [16 ** i for i in range(dcap + 2)]
        for n in range(A, 2 * A):
            for q in range(n, n + dcap):
                if q not in rows:
                    rows[q] = self.row(q)
            Sn = rows[n]
            Xn = self.X[n]
            for (m, k) in triples:
                d = m + k
                Sd = Sn[d]
                Sm = rows[n + k][m]
                # repo definition, integers
                thD = (p16[d] * Xn) % D
                dlD = (p16[m] * Sn[k]) % D
                b_def = 1 if thD + dlD >= D else 0
                # claim
                xnd = self.X[n + d]
                b_cl = 1 if (Sm <= xnd < Sd) else 0
                dl_cl = Sd - Sm
                adm = Sd < D
                if hook is not None:
                    hook(n, m, k, b_def, Sd, Sm, dlD, xnd, adm)
                rr = rec[(m, k)]
                rr["bits_def"].append(b_def)
                rr["bits_claim"].append(b_cl)
                rr["sum_b"] += b_def
                rr["sum_deltaD"] += dlD
                mmb = (b_def != b_cl)
                mmd = (dlD != dl_cl)
                if adm:
                    rr["nadm"] += 1
                    mg = D - Sd
                    if rr["min_margin"] is None or mg < rr["min_margin"]:
                        rr["min_margin"] = mg
                        rr["min_margin_n"] = n
                    rr["mm_b_adm"] += mmb
                    rr["mm_d_adm"] += mmd
                else:
                    rr["n_inadm"] += 1
                    rr["mm_b_inadm"] += mmb
                    rr["mm_d_inadm"] += mmd
                if mmb or mmd:
                    c = rr["cls"]
                    c["Sm_neg"] += Sm < 0
                    c["Sd_ge1"] += Sd >= D
                    c["Sd_neg"] += Sd < 0
                    c["Sm_gt_Sd"] += Sm > Sd
                    if len(rr["examples"]) < 3:
                        rr["examples"].append(dict(n=n, b_def=b_def, b_claim=b_cl, delta_eq=not mmd,
                                                   Sm_sign=(Sm > 0) - (Sm < 0), Sd_lt_1=bool(adm)))
            rows.pop(n, None)
        out = {}
        for (m, k), rr in rec.items():
            out["%d,%d" % (m, k)] = dict(
                m=m, k=k, d=m + k, n_total=A, nadm=rr["nadm"], n_inadm=rr["n_inadm"],
                mm_b_adm=rr["mm_b_adm"], mm_d_adm=rr["mm_d_adm"],
                mm_b_inadm=rr["mm_b_inadm"], mm_d_inadm=rr["mm_d_inadm"],
                sum_b=rr["sum_b"], sum_delta_num=rr["sum_deltaD"], sum_delta_den=D,
                min_margin_frac=(None if rr["min_margin"] is None else (rr["min_margin"], D)),
                min_margin_n=rr["min_margin_n"],
                digest_b_def=digest_bits(rr["bits_def"]), digest_b_claim=digest_bits(rr["bits_claim"]),
                mismatch_classes=rr["cls"], examples=rr["examples"])
        return out


# ------------------------------------------------------------------ rigorous Green tail
def _r_bounds(n):
    """rigorous integer bounds rlo <= SC*r(n) <= rhi for the source forcing."""
    a, b, c, e = 8 * n - 7, 8 * n - 4, 8 * n - 3, 8 * n - 2
    cd = lambda x, y: -((-x) // y)
    lo = (4 * SC) // a - cd(2 * SC, b) - cd(SC, c) - cd(SC, e)
    hi = cd(4 * SC, a) - (2 * SC) // b - SC // c - SC // e
    return lo, hi


def tail_intervals(nmax, extra=120):
    """lists lo[n], hi[n] (n=0..nmax) with lo[n] <= SC*T_n <= hi[n], T_n = sum_{j>=1}16^-j r(n+j).
    Start: 0 <= T_{N0} <= 1/10 (r>0 for all m, r(m)<=4/9 for m>=2 => T<=4/135)."""
    N0 = nmax + extra
    lo = 0
    hi = SC // 10 + 1
    LO = [0] * (nmax + 1)
    HI = [0] * (nmax + 1)
    for n in range(N0 - 1, -1, -1):
        rl, rh = _r_bounds(n + 1)
        lo = (lo + rl) // 16
        hi = -((-(hi + rh)) // 16)
        if n <= nmax:
            LO[n] = lo
            HI[n] = hi
    return LO, HI


# ------------------------------------------------------------------ independent pi (Chudnovsky)
def _bs(a, b, C3_24):
    if b - a == 1:
        if a == 0:
            Pab = Qab = 1
        else:
            Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            Qab = a * a * a * C3_24
        Tab = Pab * (13591409 + 545140134 * a)
        if a & 1:
            Tab = -Tab
        return Pab, Qab, Tab
    m = (a + b) // 2
    Pam, Qam, Tam = _bs(a, m, C3_24)
    Pmb, Qmb, Tmb = _bs(m, b, C3_24)
    return Pam * Pmb, Qam * Qmb, Qmb * Tam + Pam * Tmb


def pi_fixed(bits):
    """floor(pi * 2^bits) up to a few units in the last place; own Chudnovsky implementation."""
    gb = 64
    B = bits + gb
    terms = int(B / 47.11) + 3
    C3_24 = 640320 ** 3 // 24
    P, Q, T = _bs(0, terms, C3_24)
    sq = math.isqrt(10005 * (1 << (2 * B)))
    pi = (426880 * sq * Q) // T
    return pi >> gb


def pi_hex_digits(M):
    """numpy uint8 array h[1..M] of the first M hex digits of the fractional part of pi, plus the
    leading integer part digit 3 returned separately.  Guard digits dropped."""
    import numpy as np
    guard = 24
    bits = 4 * (M + guard)
    P = pi_fixed(bits)
    frac = P - (3 << bits)
    s = format(frac, "x").zfill(M + guard)[:M]
    arr = np.frombuffer(s.encode("ascii"), dtype=np.uint8)
    vals = np.where(arr >= 97, arr - 87, arr - 48).astype(np.uint8)
    return vals
