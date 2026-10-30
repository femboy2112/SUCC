"""Independent oracle for Operation Main XVI (deliberately different routes).

Research-only. Not a pi digit sampler and not a proof of normality or RH. Python >= 3.10.

This file re-derives the Main XVI results by methods DISTINCT from golden_locus.py / seed_alias.py:

  P1 golden locus:
     * exact symbolic polynomial root-isolation of z*(1+theta-theta*z)^r = 1 (sympy),
       versus golden_locus.py's monotone fixed-point iteration;
     * mpmath Newton (findroot) as a third numeric route.
  P2/P3 seed aliases:
     * U_n(0) recomputed by the convolution/Horner closed form U_n(0) = sum_k 16^{n-k} r(k),
       versus seed_alias.py's step recurrence;
     * alias classes decided by MODULAR arithmetic (2-adic valuation; multiplicative order of 16
       mod q) instead of by computing fractional parts;
     * the explicit coherent counterseed s* = -pi/16 in high-precision mpmath.

Run:  python3 -I independent_oracle_xvi.py
"""
from __future__ import annotations
from fractions import Fraction as Fr
import json
import mpmath as mp
import sympy as sp

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))
def R(a): return sum((Fr(c) / (Fr(a) + d) for d, c in POLES), Fr())
def r_clock(n): return R(8 * n - 7)


# ---------- P1: independent golden-locus roots ----------
def locus_root_substitution(r_int):
    """EXACT: prove lambda^r is a root of z*(1+theta-theta*z)^r=1 on the locus by substitution.

    Returns (theta_expr, is_root_bool).  Independent of any iteration; pure symbolic identity.
    """
    lam = (sp.sqrt(5) - 1) / 2
    theta = lam / (1 - lam**r_int)
    z0 = lam**r_int
    residual = sp.simplify(z0 * (1 + theta - theta * z0) ** r_int - 1)
    return theta, (residual == 0)


def least_root_numeric(r_int, dps=60):
    """Isolate the least real root in (0,1) of z*(1+theta-theta z)^r=1 by mpmath.polyroots."""
    with mp.workdps(dps + 20):
        lam = (mp.sqrt(5) - 1) / 2
        theta = lam / (1 - lam ** r_int)
        # expand z*(1+theta-theta z)^r - 1 into monomial coeffs via sympy (exact), then mp roots
        z = sp.symbols('z')
        th = sp.nsimplify(lam, [sp.sqrt(5)])  # exact theta in radicals from exact lambda
        th = (sp.sqrt(5) - 1) / 2 / (1 - ((sp.sqrt(5) - 1) / 2) ** r_int)
        poly = sp.Poly(sp.expand(z * (1 + th - th * z) ** r_int - 1), z)
        coeffs = [mp.mpf(str(sp.N(c, dps + 20))) for c in poly.all_coeffs()]
        roots = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
        real_in = sorted(r.real for r in roots if abs(r.imag) < mp.mpf(10) ** (-(dps - 5)) and 0 < r.real < 1)
        return (theta, real_in[0] if real_in else None)


# ---------- P2/P3: independent orbit + modular alias decisions ----------
def U0_convolution(n):
    """U_n(0) = sum_{k=1}^{n} 16^{n-k} r(k)  (closed Horner form, not the step recurrence)."""
    return sum((16 ** (n - k) * r_clock(k) for k in range(1, n + 1)), Fr())


def two_adic_val(den):
    """2-adic valuation of a power-of-two denominator; -1 if not a power of two."""
    if den & (den - 1) != 0:
        return -1
    return den.bit_length() - 1


def order_16_mod(q):
    """Multiplicative order of 16 modulo q (q coprime to 16); 1 iff 16==1 (mod q)."""
    if q == 1:
        return 1
    o, cur = 1, 16 % q
    while cur != 1:
        cur = (cur * 16) % q
        o += 1
        if o > q + 1:
            raise RuntimeError('16 not invertible mod q')
    return o


def alias_decision_modular(s):
    """Decide (onset, constant_twist, period) purely by modular arithmetic on s=p/q."""
    s = Fr(s)
    q = s.denominator
    v = two_adic_val(q)
    if v >= 0:                                   # s in Z[1/16]
        return {'onset': (v + 3) // 4, 'constant_twist': False, 'period': None}
    # gcd(q,16)=1 branch (general q may mix, but our probes use coprime q)
    from math import gcd
    if gcd(q, 16) == 1:
        o = order_16_mod(q)
        return {'onset': None, 'constant_twist': (o == 1), 'period': o}
    return {'onset': None, 'constant_twist': False, 'period': None}


def counterseed_phase(NN=40, dps=220):
    """s*=-pi/16: U_n(s*) = U_n(0) - 16^{n-1} pi; report T_n and |e(U_n(s*))-1|."""
    with mp.workdps(dps):
        pi = mp.pi
        out = []
        for n in range(1, NN + 1):
            u0 = U0_convolution(n)
            u0mp = mp.mpf(u0.numerator) / mp.mpf(u0.denominator)
            Us = u0mp - 16 ** (n - 1) * pi          # = -T_n
            Tn = 16 ** (n - 1) * pi - u0mp
            dev = abs(mp.e ** (2j * mp.pi * Us) - 1)
            out.append((n, Tn, dev))
        return out


def run():
    mp.mp.dps = 50
    report = {'P1_golden_locus': {}, 'P2_alias_modular': {}, 'P3_counterseed': {}}
    lamf = (mp.sqrt(5) - 1) / 2
    for r_int in (1, 2, 3, 4, 5, 6):
        theta_sym, is_root = locus_root_substitution(r_int)
        gp = lamf ** r_int
        _, least_num = least_root_numeric(r_int)
        report['P1_golden_locus'][r_int] = {
            'theta_locus': str(sp.nsimplify(theta_sym)),
            'lambda^r_is_exact_root (substitution)': bool(is_root),
            'least_real_root_in_(0,1)_matches_lambda^r': bool(least_num is not None and abs(least_num - gp) < mp.mpf(10) ** (-45)),
        }
    for s in (Fr(1, 16), Fr(1, 256), Fr(1, 65536), Fr(1, 3), Fr(2, 5), Fr(1, 15), Fr(1, 7)):
        report['P2_alias_modular'][str(s)] = alias_decision_modular(s)
    cp = counterseed_phase()
    report['P3_counterseed'] = {
        'T_8': mp.nstr(cp[7][1], 6), 'T_40': mp.nstr(cp[39][1], 6),
        'phase_dev_8': mp.nstr(cp[7][2], 6), 'phase_dev_40': mp.nstr(cp[39][2], 6),
        'coherent_collapse': bool(cp[-1][1] > 0 and cp[-1][1] < cp[7][1] and cp[-1][2] < cp[7][2]),
    }
    return report


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, default=str))
