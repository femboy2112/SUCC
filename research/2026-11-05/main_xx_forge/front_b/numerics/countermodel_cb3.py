"""countermodel_cb3.py - CB-3 countermodel instrument (Daniel Bernoulli).

Digit laws p(tau) with p_0=1/16, F_{p}(tau)=tau on a bump tau in (0.3,0.7); digits of alpha drawn
independently with law p(tau_j); gauge-form J_{A,m,k} sweep; exact expectations under the
product measure; non-normality witnesses; second-order selected carry statistic J2.

mpmath is used ONLY inside `with mp.workdps(...)` blocks.  numpy default_rng for sampling.
"""
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oracle_b as OB  # noqa: E402

DELTA = 0.02
LO_B, HI_B = 0.3, 0.7
L_SOLVE = 50          # hex digits of tau used when solving (tail <= (max p)^50 ~ 1e-52)
L_VERIFY = 70         # hex digits used when verifying residual
DPS_MP = 80
L_FLOAT = 40


# ------------------------------------------------------------------ tau_j and hex digits (exact integers)
def tau_fraction(j):
    k = (((64 * j * j).bit_length() - 1) // 4)       # floor(log16(64 j^2)), exact
    return Fraction(16 ** k, 64 * j * j)


def tau_digits_rational(fr, L):
    """first L hex digits of a rational in [0,1) (tau=1 not expected inside bump)."""
    num, den = fr.numerator, fr.denominator
    out = []
    r = num
    for _ in range(L):
        r *= 16
        a, r = divmod(r, den)
        out.append(a)
    return out


# ------------------------------------------------------------------ mp (high precision) builder
def _bump_mp(mp, tau):
    x = (tau - mp.mpf(1) / 2) / (mp.mpf(1) / 5)
    if abs(x) >= 1:
        return mp.mpf(0)
    return mp.exp(1 - 1 / (1 - x * x))


def F_grad_mp(mp, p, digs):
    F = mp.mpf(0)
    W = mp.mpf(1)
    cnt = [0] * 16
    G = [mp.mpf(0)] * 16
    cum = [mp.mpf(0)] * 17
    for a in range(16):
        cum[a + 1] = cum[a] + p[a]
    for a in digs:
        Ca = cum[a]
        F += W * Ca
        for b in range(a):
            G[b] += W
        for b in range(16):
            if cnt[b]:
                G[b] += W * cnt[b] / p[b] * Ca
        W *= p[a]
        cnt[a] += 1
    return F, G


def build_p_mp(mp, tau_fr, L=L_SOLVE, delta=DELTA):
    """law p(tau) as list of 16 mpf; call inside mp.workdps.  tau_fr: Fraction."""
    tau = mp.mpf(tau_fr.numerator) / mp.mpf(tau_fr.denominator)
    u = [mp.mpf(1) / 16] * 16
    phi = _bump_mp(mp, tau)
    if phi == 0:
        return u
    digs = tau_digits_rational(tau_fr, L)
    F0, g = F_grad_mp(mp, u, digs)
    mean = sum(g[1:]) / 15
    gV = [mp.mpf(0)] + [g[a] - mean for a in range(1, 16)]
    w = [mp.mpf(0)] * 16
    w[1], w[2] = mp.mpf(1), mp.mpf(-1)
    gw = sum(a * b for a, b in zip(gV, w))
    gg = sum(a * a for a in gV)
    wperp = [w[a] - gw / gg * gV[a] for a in range(16)]
    p0 = [u[a] + mp.mpf(delta) * phi * wperp[a] for a in range(16)]
    c = mp.mpf(0)
    for _ in range(12):
        p = [p0[a] + c * gV[a] for a in range(16)]
        F, G = F_grad_mp(mp, p, digs)
        f = F - tau
        if abs(f) < mp.mpf(10) ** (-(DPS_MP - 15)):
            break
        fp = sum(G[a] * gV[a] for a in range(16))
        c -= f / fp
    return [p0[a] + c * gV[a] for a in range(16)]


def verify_p_mp(mp, p, tau_fr, L=L_VERIFY):
    tau = mp.mpf(tau_fr.numerator) / mp.mpf(tau_fr.denominator)
    digs = tau_digits_rational(tau_fr, L)
    F, _ = F_grad_mp(mp, p, digs)
    return F - tau


def _grid_node(args):
    import mpmath as mp
    i, h = args
    tau_fr = Fraction(i, 2000)
    with mp.workdps(DPS_MP):
        p = build_p_mp(mp, tau_fr)
        res = verify_p_mp(mp, p, tau_fr)
        pm = [float(x) for x in p]
        return dict(i=i, tau=float(tau_fr), p=pm, resid=float(abs(res)), resid_str=mp.nstr(abs(res), 5),
                    p0_err=float(abs(p[0] - mp.mpf(1) / 16)), sum_err=float(abs(sum(p) - 1)),
                    p_min=float(min(p)), maxdev=float(max(abs(x - mp.mpf(1) / 16) for x in p)))


def build_grid(procs=6, lo=500, hi=1500):
    from multiprocessing import Pool
    with Pool(procs) as pool:
        nodes = pool.map(_grid_node, [(i, None) for i in range(lo, hi + 1)], chunksize=8)
    return nodes


def grid_report(nodes):
    arr = np.array([n["p"] for n in nodes])
    steps = np.abs(np.diff(arr, axis=0)).max(axis=1)
    return dict(n_nodes=len(nodes), tau_lo=nodes[0]["tau"], tau_hi=nodes[-1]["tau"],
                max_residual=max(n["resid"] for n in nodes),
                max_residual_str=max(nodes, key=lambda n: n["resid"])["resid_str"],
                max_p0_err=max(n["p0_err"] for n in nodes), max_sum_err=max(n["sum_err"] for n in nodes),
                min_p=min(n["p_min"] for n in nodes),
                max_abs_dev_from_uniform=max(n["maxdev"] for n in nodes),
                nodes_nonuniform=int(sum(n["maxdev"] > 1e-12 for n in nodes)),
                max_adjacent_step_Linf=float(steps.max()), grid_h=float(nodes[1]["tau"] - nodes[0]["tau"]),
                max_step_over_h=float(steps.max() / (nodes[1]["tau"] - nodes[0]["tau"])),
                edge_values=dict((("tau=%.4f" % n["tau"]), n["maxdev"]) for n in nodes
                                 if abs(n["tau"] - 0.3005) < 1e-9 or abs(n["tau"] - 0.6995) < 1e-9 or abs(n["tau"] - 0.5) < 1e-9
                                 or abs(n["tau"] - 0.35) < 1e-9))


# ------------------------------------------------------------------ float64 vectorised production solver
def F_G_vec(p, digs):
    Nb, L = digs.shape
    cum = np.cumsum(p, axis=1) - p
    ar = np.arange(Nb)
    F = np.zeros(Nb)
    W = np.ones(Nb)
    cnt = np.zeros((Nb, 16))
    G = np.zeros((Nb, 16))
    idx = np.arange(16)[None, :]
    for i in range(L):
        a = digs[:, i].astype(np.int64)
        Ca = cum[ar, a]
        F += W * Ca
        G += W[:, None] * (idx < a[:, None])
        G += (W * Ca)[:, None] * cnt / p
        W = W * p[ar, a]
        cnt[ar, a] += 1
    return F, G


def bump_vec(tau):
    x = (tau - 0.5) / 0.2
    out = np.zeros_like(tau)
    m = np.abs(x) < 1
    out[m] = np.exp(1 - 1 / (1 - x[m] ** 2))
    return out


def solve_float(taus, digs, delta=DELTA):
    """taus (Nb,) float, digs (Nb,L) uint8 -> p (Nb,16)."""
    Nb = len(taus)
    u = np.full((Nb, 16), 1 / 16)
    F0, g = F_G_vec(u, digs)
    gV = g.copy()
    gV[:, 0] = 0
    gV[:, 1:] -= gV[:, 1:].mean(axis=1, keepdims=True)
    w = np.zeros((Nb, 16))
    w[:, 1], w[:, 2] = 1, -1
    gw = (gV * w).sum(1)
    gg = (gV * gV).sum(1)
    wperp = w - (gw / gg)[:, None] * gV
    phi = bump_vec(taus)
    p0 = u + delta * phi[:, None] * wperp
    c = np.zeros(Nb)
    for _ in range(10):
        p = p0 + c[:, None] * gV
        F, G = F_G_vec(p, digs)
        f = F - taus
        fp = (G * gV).sum(1)
        c = c - f / fp
    p = p0 + c[:, None] * gV
    F, _ = F_G_vec(p, digs)
    return p, F - taus


class Laws:
    """production law table PJ[j-1] = p(tau_j) for j=1..N (uniform off the bump)."""

    def __init__(self, N):
        self.N = N
        taus = np.zeros(N)
        inb = np.zeros(N, dtype=bool)
        fr = [None] * N
        for j in range(1, N + 1):
            f = tau_fraction(j)
            t = float(f)
            taus[j - 1] = t
            if LO_B < t < HI_B:
                inb[j - 1] = True
                fr[j - 1] = f
        self.taus = taus
        self.inbump = inb
        idxs = np.nonzero(inb)[0]
        digs = np.array([tau_digits_rational(fr[i], L_FLOAT) for i in idxs], dtype=np.uint8)
        PJ = np.full((N, 16), 1 / 16)
        res = np.zeros(0)
        if len(idxs):
            p, res = solve_float(taus[idxs], digs)
            PJ[idxs] = p
        self.PJ = PJ
        self.float_resid_max = float(np.abs(res).max()) if len(res) else 0.0
        self.n_bump = int(len(idxs))
        self.CP = np.cumsum(PJ, axis=1) - PJ          # CP[j,a] = sum_{a'<a} p_{a'}
        self.cum = np.cumsum(PJ, axis=1)
        self.bump_idx = idxs
        self.bump_fr = [fr[i] for i in idxs]

    def sample(self, seed):
        rng = np.random.default_rng(seed)
        U = rng.random(self.N)
        D = (U[:, None] >= self.cum[:, :15]).sum(axis=1).astype(np.uint8)   # inverse CDF
        return D

    def uniform_laws(self):
        u = Laws.__new__(Laws)
        u.N = self.N
        u.PJ = np.full((self.N, 16), 1 / 16)
        u.CP = np.cumsum(u.PJ, axis=1) - u.PJ
        u.cum = np.cumsum(u.PJ, axis=1)
        return u


def uniform_digits(N, seed):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 16, N).astype(np.uint8)


# ------------------------------------------------------------------ tails and admissibility
class Tails:
    def __init__(self, nmax):
        self.nmax = nmax
        self.LO, self.HI = OB.tail_intervals(nmax)
        self.Tf = np.array([v / OB.SC for v in self.LO])
        P = [0]
        for v in self.LO:
            P.append(P[-1] + v)
        self.P = P

    def sum_lo(self, a, b):     # sum_{n=a}^{b} LO[n]
        return self.P[b + 1] - self.P[a]

    def dmax(self, A, dstop=16):
        """largest d with S_d(n)=16^d T_n - T_{n+d} < 1 for all n in [A,2A) (monotone in d)."""
        best = 1
        for d in range(2, dstop):
            Sd = 16.0 ** d * self.Tf[A:2 * A] - self.Tf[A + d:2 * A + d]
            mx = Sd.max()
            if abs(mx - 1) < 1e-9:
                # exact decision: S_d(n) < 1  <=>  16^d HI[n] - LO[n+d] < SC (sufficient) ; check all n near top
                n0 = A + int(np.argmax(Sd))
                ok = all(16 ** d * self.HI[n] - self.LO[n + d] < OB.SC for n in range(max(A, n0 - 3), min(2 * A, n0 + 4)))
                adm = ok
            else:
                adm = mx < 1
            if adm:
                best = d
            else:
                break
        return best


# ------------------------------------------------------------------ digit arrays -> z (float, 13 digits)
def zfloat(D):
    """Zf[j] = 0.D[j] D[j+1] ... (13 hex digits, exact dyadic) ; D 0-based, D[i] = D_{i+1}."""
    N = len(D)
    Z = np.zeros(N - 13)
    for i in range(13):
        Z += D[i:N - 13 + i].astype(np.float64) * 16.0 ** (-(i + 1))
    return Z


def z_exact_int(D, j, nd=100):
    s = "".join("0123456789abcdef"[v] for v in D[j:j + nd])
    return int(s, 16) << (400 - 4 * nd) if nd < 100 else int(s, 16)


def b_vector(D, Zf, T, A, m, k, extra=0):
    """b_{n,m,k} for n in [A, 2A+extra) from digit array D; returns (b, margin_min, n_exact_fallbacks, unresolved)."""
    d = m + k
    n = np.arange(A, 2 * A + extra)
    lo = 16.0 ** m * T.Tf[n + k]
    up = 16.0 ** d * T.Tf[n]
    z = Zf[n + d]
    b = (z >= lo) & (z < up)
    mg = np.minimum(np.abs(z - lo), np.abs(z - up))
    amb = np.nonzero(mg < 1e-13)[0]
    unresolved = 0
    for i in amb:
        nn = int(n[i])
        zi = z_exact_int(D, nn + d)
        tl_lo, tl_hi = 16 ** m * T.LO[nn + k], 16 ** m * T.HI[nn + k]
        tu_lo, tu_hi = 16 ** d * T.LO[nn], 16 ** d * T.HI[nn]
        # z known to [zi, zi+1)
        if zi >= tl_hi and zi + 1 <= tu_lo:
            b[i] = True
        elif zi + 1 <= tl_lo or zi >= tu_hi:
            b[i] = False
        else:
            unresolved += 1
    return b, float(mg.min()), int(len(amb)), unresolved


def delta_sum_exact(T, A, m, k):
    d = m + k
    s = 16 ** d * T.sum_lo(A, 2 * A - 1) - 16 ** m * T.sum_lo(A + k, 2 * A - 1 + k)
    return Fraction(s, OB.SC)


def J_all(D, Zf, T, A, dmax):
    out = {}
    minmg = 1.0
    amb = 0
    unres = 0
    for d in range(2, dmax + 1):
        for m in range(1, d):
            k = d - m
            b, mg, na, nu = b_vector(D, Zf, T, A, m, k)
            sd = delta_sum_exact(T, A, m, k)
            J = (Fraction(int(b.sum())) - sd) / A
            out["%d,%d" % (m, k)] = float(J)
            minmg = min(minmg, mg)
            amb += na
            unres += nu
    return out, minmg, amb, unres


# ------------------------------------------------------------------ exact expectations under the product measure
def cdf_pos(t, base, laws, L=18):
    F = np.zeros_like(t)
    W = np.ones_like(t)
    x = t.copy()
    for i in range(L):
        x = x * 16
        a = np.floor(x).astype(np.int64)
        x = x - a
        F += W * laws.CP[base + i, a]
        W = W * laws.PJ[base + i, a]
    return F


def Eb_minus_delta(T, laws, A, m, k):
    d = m + k
    n = np.arange(A, 2 * A)
    lo = 16.0 ** m * T.Tf[n + k]
    up = np.minimum(16.0 ** d * T.Tf[n], 1 - 2.0 ** -53)
    base = n + d
    e = cdf_pos(up, base, laws) - cdf_pos(lo, base, laws)
    return e - (up - lo)


def expectedJ(T, laws, A, m, k):
    return float(Eb_minus_delta(T, laws, A, m, k).mean())


def H_joint(x, y, base, ell, laws):
    xx = x.copy()
    Fpre = np.zeros_like(x)
    W = np.ones_like(x)
    for i in range(ell):
        xx = xx * 16
        a = np.floor(xx).astype(np.int64)
        xx = xx - a
        Fpre += W * laws.CP[base + i, a]
        W = W * laws.PJ[base + i, a]
    Fy = cdf_pos(y, base + ell, laws)
    Fm = cdf_pos(np.minimum(xx, y), base + ell, laws)
    return Fpre * Fy + W * Fm


def haar_inter(a, b, a2, b2, ell):
    """Leb(I cap T^-ell I'), I=[a,b), I'=[a2,b2) subsets of [0,1] (float64, closed form)."""
    N = 16.0 ** ell
    ln = b2 - a2

    def g(x):
        y = N * x
        fl = np.floor(y)
        return fl * ln / N + np.clip(y - fl - a2, 0, ln) / N
    return g(b) - g(a)


def expectedJ2(T, laws, A, m, k, ell):
    d = m + k
    n = np.arange(A, 2 * A)
    top = 1 - 2.0 ** -53
    a1 = 16.0 ** m * T.Tf[n + k]
    b1 = np.minimum(16.0 ** d * T.Tf[n], top)
    a2 = 16.0 ** m * T.Tf[n + ell + k]
    b2 = np.minimum(16.0 ** d * T.Tf[n + ell], top)
    base = n + d
    eb = (H_joint(b1, b2, base, ell, laws) - H_joint(a1, b2, base, ell, laws)
          - H_joint(b1, a2, base, ell, laws) + H_joint(a1, a2, base, ell, laws))
    hv = haar_inter(a1, b1, a2, b2, ell)
    return float((eb - hv).mean()), float(hv.mean())


def empiricalJ2(D, Zf, T, A, m, k, ell):
    d = m + k
    b, mg, na, nu = b_vector(D, Zf, T, A, m, k, extra=ell)
    n = np.arange(A, 2 * A)
    top = 1 - 2.0 ** -53
    a1 = 16.0 ** m * T.Tf[n + k]
    b1 = np.minimum(16.0 ** d * T.Tf[n], top)
    a2 = 16.0 ** m * T.Tf[n + ell + k]
    b2 = np.minimum(16.0 ** d * T.Tf[n + ell], top)
    hv = haar_inter(a1, b1, a2, b2, ell)
    bb = b[:A].astype(np.float64) * b[ell:A + ell].astype(np.float64)
    return float((bb - hv).mean()), float(hv.mean()), mg, nu


# ------------------------------------------------------------------ instrument self-checks
class _ConstLaws:
    def __init__(self, p, N):
        self.PJ = np.tile(np.array(p, dtype=float), (N, 1))
        self.CP = np.cumsum(self.PJ, axis=1) - self.PJ
        self.cum = np.cumsum(self.PJ, axis=1)
        self.N = N


def selfcheck_cb3(nsamp=2_000_000, seed=424242):
    """(1) closed-form Haar counting vs joint-CDF algebra with UNIFORM laws; (2) CDF/joint algebra vs Monte Carlo
    with a strongly non-uniform law; (3) exact floats F(tau)=tau on the production laws is checked elsewhere."""
    import mpmath as mp
    out = {}
    N = 64
    u = _ConstLaws([1 / 16] * 16, N)
    rng = np.random.default_rng(5)
    worst = 0.0
    for ell in (1, 2, 3):
        a = rng.random(300) * 0.3
        b = a + rng.random(300) * 0.4
        a2 = rng.random(300) * 0.3
        b2 = a2 + rng.random(300) * 0.4
        base = np.full(300, 5)
        hv = haar_inter(a, b, a2, b2, ell)
        hj = (H_joint(b, b2, base, ell, u) - H_joint(a, b2, base, ell, u)
              - H_joint(b, a2, base, ell, u) + H_joint(a, a2, base, ell, u))
        worst = max(worst, float(np.abs(hv - hj).max()))
    out["uniform_joint_vs_closed_form_max_diff"] = worst
    # strongly non-uniform constant law (builder law at tau=1/3 plus an exaggerated 3<->9 transfer for MC visibility)
    with mp.workdps(DPS_MP):
        p = [float(x) for x in build_p_mp(mp, Fraction(1, 3))]
    p[3] += 0.03
    p[9] -= 0.03
    nl = _ConstLaws(p, N)
    rng = np.random.default_rng(seed)
    U = rng.random((nsamp, 24))
    digs = (U[:, :, None] >= nl.cum[0][None, None, :15]).sum(axis=2)
    z = np.zeros(nsamp)
    for i in range(24):
        z += digs[:, i] * 16.0 ** (-(i + 1))
    res = []
    for (x, y, ell) in [(0.37, 0.22, 1), (0.37, 0.22, 2), (0.81, 0.45, 1), (0.05, 0.9, 3), (0.2, 0.2, 1)]:
        w = (z * 16 ** ell) % 1.0
        mc = float(((z < x) & (w < y)).mean())
        base = np.array([3])
        ex = float(H_joint(np.array([x]), np.array([y]), base, ell, nl)[0])
        sig = math.sqrt(max(ex * (1 - ex), 1e-12) / nsamp)
        hv_cdf = float(cdf_pos(np.array([x]), base, nl)[0])
        res.append(dict(x=x, y=y, ell=ell, exact=ex, mc=mc, z_score=(mc - ex) / sig,
                        uniform_value=float(haar_inter(np.array([0.0]), np.array([x]), np.array([0.0]), np.array([y]), ell)[0]),
                        cdf_x=hv_cdf, mc_cdf_x=float((z < x).mean())))
    out["mc_joint_vs_exact"] = res
    out["mc_max_abs_zscore"] = max(abs(r["z_score"]) for r in res)
    out["nonuniformity_visible_max_|exact-uniform|"] = max(abs(r["exact"] - r["uniform_value"]) for r in res)
    return out


# ------------------------------------------------------------------ witnesses
def witnesses_empirical(D, N):
    d = D[:N - 1]                       # indices j=1..N-1
    cnt = np.bincount(d, minlength=16) / len(d)
    pairs = (D[:N - 2] == D[1:N - 1]).mean()
    return dict(freq=cnt.tolist(), f1_minus_f2=float(cnt[1] - cnt[2]), max_dev=float(np.abs(cnt - 1 / 16).max()),
                pairs_minus_1_16=float(pairs - 1 / 16))


def witnesses_expected(laws, N):
    P = laws.PJ[:N - 1]
    ef = P.mean(axis=0)
    pairs = (laws.PJ[:N - 2] * laws.PJ[1:N - 1]).sum(axis=1).mean()
    return dict(freq=ef.tolist(), f1_minus_f2=float(ef[1] - ef[2]), max_dev=float(np.abs(ef - 1 / 16).max()),
                pairs_minus_1_16=float(pairs - 1 / 16))


# ------------------------------------------------------------------ stages
AS_POW2 = [2 ** e for e in range(10, 18)]
AS_HALF = [int(round(2 ** (e + 0.5))) for e in range(10, 17)]
SEEDS_PRE = [20261105, 1, 2]
SEEDS_SUP = list(range(3, 13))


def fit_slope(As, ys):
    xs = np.log(np.array(As, dtype=float))
    ys = np.log(np.array(ys, dtype=float))
    ok = np.isfinite(ys)
    sl, ic = np.polyfit(xs[ok], ys[ok], 1)
    return float(sl), float(np.exp(ic))


_G = {}


def _setup(Amax):
    if "T" not in _G or _G["Amax"] < Amax:
        Nd = 2 * Amax + 400
        _G["Amax"] = Amax
        _G["Nd"] = Nd
        _G["T"] = Tails(Nd + 40)
        _G["laws"] = Laws(Nd)
    return _G


def _pi_digits(Nd, quick):
    # D_i (1-based) = hex digit sequence of pi/16 = 0.3243F6A8...  -> D[0]=3, D[i]=h_i
    h = OB.pi_hex_digits(Nd + 30)
    return np.concatenate([[3], h[:Nd - 1]]).astype(np.uint8)


def _sweep_one(args):
    kind, seed, As = args
    G = _G
    T, laws, Nd = G["T"], G["laws"], G["Nd"]
    if kind == "cb3":
        D = laws.sample(seed)
    elif kind == "unif":
        D = uniform_digits(Nd, seed)
    elif kind == "pi":
        D = G["pi_D"]
    Zf = zfloat(D)
    res = {}
    for A in As:
        dmax = T.dmax(A)
        J, mg, na, nu = J_all(D, Zf, T, A, dmax)
        vals = np.array(list(J.values()))
        key = max(J, key=lambda q: abs(J[q]))
        N = 2 * A
        res[A] = dict(dmax=dmax, n_triples=len(J), max_abs_J=float(np.abs(vals).max()), argmax=key,
                      rms_J=float(np.sqrt((vals ** 2).mean())), mean_J=float(vals.mean()),
                      min_margin=mg, ambiguous_fallbacks=na, unresolved=nu,
                      wit=witnesses_empirical(D, N), J=J)
    return dict(kind=kind, seed=seed, res=res)


def stage_cb3(quick=False, procs=6):
    from multiprocessing import Pool
    out = {"numpy": np.__version__}
    t0 = time.time()
    As_pow = [2 ** e for e in range(10, 15 if quick else 18)]
    As_half = [int(round(2 ** (e + 0.5))) for e in range(10, 14 if quick else 17)]
    As = sorted(As_pow + As_half)
    Amax = max(As)
    # --- p(tau) grid construction (mp 80 dps) ---
    t1 = time.time()
    nodes = build_grid(procs, 500, 1500) if not quick else build_grid(procs, 600, 1400)[::2]
    out["grid"] = grid_report(nodes)
    out["grid_time"] = time.time() - t1
    # --- setup ---
    G = _setup(Amax)
    T, laws, Nd = G["T"], G["laws"], G["Nd"]
    out["laws"] = dict(N=Nd, n_in_bump=laws.n_bump, frac_in_bump=laws.n_bump / Nd,
                       float_residual_max=laws.float_resid_max,
                       max_abs_dev_from_uniform=float(np.abs(laws.PJ - 1 / 16).max()),
                       p0_exact_1_16=bool(np.all(laws.PJ[:, 0] == 1 / 16)),
                       min_p=float(laws.PJ.min()), row_sum_err=float(np.abs(laws.PJ.sum(1) - 1).max()))
    # cross-check float vs mp on random actual tau_j in bump
    import mpmath as mp
    rng = np.random.default_rng(777)
    sel = rng.choice(len(laws.bump_idx), size=min(30, len(laws.bump_idx)), replace=False)
    maxd = 0.0
    maxres = 0.0
    with mp.workdps(DPS_MP):
        for s in sel:
            fr = laws.bump_fr[s]
            pm = build_p_mp(mp, fr)
            res = verify_p_mp(mp, pm, fr)
            maxres = max(maxres, float(abs(res)))
            pf = laws.PJ[laws.bump_idx[s]]
            maxd = max(maxd, max(abs(float(pm[a]) - pf[a]) for a in range(16)))
    out["selfcheck"] = selfcheck_cb3()
    out["float_vs_mp_on_actual_tau_j"] = dict(n=int(len(sel)), max_abs_p_diff=maxd, max_mp_residual=maxres)
    # --- pi digits ---
    t2 = time.time()
    G["pi_D"] = _pi_digits(Nd, quick)
    out["pi_digits_time"] = time.time() - t2
    # --- exact expected J (bias) for CB-3 ---
    bias = {}
    t3 = time.time()
    for A in As:
        dm = T.dmax(A)
        vals = {}
        for d in range(2, dm + 1):
            for m in range(1, d):
                vals["%d,%d" % (m, d - m)] = expectedJ(T, laws, A, m, d - m)
        v = np.array(list(vals.values()))
        bias[A] = dict(dmax=dm, max_abs=float(np.abs(v).max()), rms=float(np.sqrt((v ** 2).mean())),
                       argmax=max(vals, key=lambda q: abs(vals[q])), per_triple=vals)
    out["expected_J_bias"] = bias
    out["bias_time"] = time.time() - t3
    # --- empirical sweeps ---
    tasks = [("cb3", s, As) for s in SEEDS_PRE + (SEEDS_SUP[:2] if quick else SEEDS_SUP)]
    tasks += [("unif", s, As) for s in ([101, 102] if quick else list(range(101, 113)))]
    tasks += [("pi", 0, As)]
    t4 = time.time()
    with Pool(procs) as pool:
        sw = pool.map(_sweep_one, tasks, chunksize=1)
    out["sweep_time"] = time.time() - t4
    out["sweeps"] = [dict(kind=s["kind"], seed=s["seed"],
                          res={str(A): {k: v for k, v in r.items() if k != "J"} for A, r in s["res"].items()},
                          J_per_triple={str(A): r["J"] for A, r in s["res"].items()} if s["kind"] in ("pi",) or s["seed"] in SEEDS_PRE else None)
                     for s in sw]
    # --- expected witnesses ---
    wexp = {}
    for A in As:
        wexp[A] = witnesses_expected(laws, 2 * A)
    out["witness_expected_cb3"] = wexp
    # liminf over fine N grid
    Ns = np.unique(np.round(np.exp(np.linspace(np.log(2 ** 10), np.log(2 * Amax), 600))).astype(int))
    cs = np.cumsum(laws.PJ, axis=0)
    f1 = (cs[Ns - 2, 1] - cs[Ns - 2, 2]) / (Ns - 1)
    pr = np.cumsum((laws.PJ[:-1] * laws.PJ[1:]).sum(axis=1))
    pw = pr[Ns - 3] / (Ns - 2) - 1 / 16
    md = np.abs(cs[Ns - 2] / (Ns - 1)[:, None] - 1 / 16).max(axis=1)
    out["witness_expected_minmax_over_N"] = dict(N_lo=int(Ns[0]), N_hi=int(Ns[-1]),
                                                 f1_minus_f2_min=float(f1.min()), f1_minus_f2_max=float(f1.max()),
                                                 pairs_min=float(pw.min()), pairs_max=float(pw.max()),
                                                 max_dev_min=float(md.min()), max_dev_max=float(md.max()))
    # --- slopes ---
    summ = {}
    pre = [s for s in out["sweeps"] if s["kind"] == "cb3"]
    unif = [s for s in out["sweeps"] if s["kind"] == "unif"]
    for tag, lst in (("cb3_all_seeds", pre), ("uniform_iid_null", unif)):
        for subset_name, subset in (("pow2", As_pow), ("half", As_half), ("all", As)):
            if not subset:
                continue
            mx = [np.mean([s["res"][str(A)]["max_abs_J"] for s in lst]) for A in subset]
            rm = [np.mean([s["res"][str(A)]["rms_J"] for s in lst]) for A in subset]
            summ["%s_%s_meanseeds_maxabsJ_slope" % (tag, subset_name)] = fit_slope(subset, mx)
            summ["%s_%s_meanseeds_rmsJ_slope" % (tag, subset_name)] = fit_slope(subset, rm)
    for s in pre:
        if s["seed"] in SEEDS_PRE:
            mx = [s["res"][str(A)]["max_abs_J"] for A in As]
            summ["cb3_seed%d_maxabsJ_slope_all" % s["seed"]] = fit_slope(As, mx)
    pis = [s for s in out["sweeps"] if s["kind"] == "pi"][0]
    summ["pi_maxabsJ_slope_all"] = fit_slope(As, [pis["res"][str(A)]["max_abs_J"] for A in As])
    summ["expected_bias_maxabs_slope_all"] = fit_slope(As, [bias[A]["max_abs"] for A in As])
    summ["expected_bias_rms_slope_all"] = fit_slope(As, [bias[A]["rms"] for A in As])
    out["slopes"] = summ
    out["As"] = As
    out["wall"] = time.time() - t0
    return out


def _j2_task(args):
    kind, seed, As = args
    G = _G
    T, laws, Nd = G["T"], G["laws"], G["Nd"]
    if kind == "cb3":
        D = laws.sample(seed)
    elif kind == "unif":
        D = uniform_digits(Nd, seed)
    else:
        D = G["pi_D"]
    Zf = zfloat(D)
    res = {}
    for A in As:
        dm = T.dmax(A)
        reps = {"k_large(1,dm-1)": (1, dm - 1), "k1(dm-1,1)": (dm - 1, 1), "balanced": (dm // 2, dm - dm // 2)}
        r = {}
        for nm, (m, k) in reps.items():
            if m < 1 or k < 1:
                continue
            b, mg, na, nu = b_vector(D, Zf, T, A, m, k)
            sdl = delta_sum_exact(T, A, m, k)
            J1 = float((Fraction(int(b.sum())) - sdl) / A)
            row = dict(m=m, k=k, J=J1)
            for ell in (1, 2, 3):
                j2, hm, mg2, nu2 = empiricalJ2(D, Zf, T, A, m, k, ell)
                row["J2_l%d" % ell] = j2
                row["haar_mean_l%d" % ell] = hm
            r[nm] = row
        res[A] = dict(dmax=dm, reps=r)
    return dict(kind=kind, seed=seed, res=res)


def stage_j2(quick=False, procs=6):
    from multiprocessing import Pool
    t0 = time.time()
    As_pow = [2 ** e for e in range(10, 15 if quick else 18)]
    As_half = [int(round(2 ** (e + 0.5))) for e in range(10, 14 if quick else 17)]
    As = sorted(As_pow + As_half)
    G = _setup(max(As))
    T, laws, Nd = G["T"], G["laws"], G["Nd"]
    G["pi_D"] = _pi_digits(Nd, quick)
    out = {"As": As}
    # exact expectations (CB-3), uniform control, coherent (b==0)
    unif = laws.uniform_laws()
    exp = {}
    for A in As:
        dm = T.dmax(A)
        reps = {"k_large(1,dm-1)": (1, dm - 1), "k1(dm-1,1)": (dm - 1, 1), "balanced": (dm // 2, dm - dm // 2)}
        e = {}
        for nm, (m, k) in reps.items():
            if m < 1 or k < 1:
                continue
            row = dict(m=m, k=k, E_J=expectedJ(T, laws, A, m, k), E_J_uniform_control=expectedJ(T, unif, A, m, k))
            for ell in (1, 2, 3):
                b2, hm = expectedJ2(T, laws, A, m, k, ell)
                u2, _ = expectedJ2(T, unif, A, m, k, ell)
                row["E_J2_l%d" % ell] = b2
                row["E_J2_uniform_control_l%d" % ell] = u2
                row["coherent_J2_l%d" % ell] = -hm
            sdl = delta_sum_exact(T, A, m, k)
            row["coherent_J"] = float(-sdl / A)
            e[nm] = row
        exp[A] = dict(dmax=dm, reps=e)
    out["expected"] = exp
    tasks = [("cb3", s, As) for s in SEEDS_PRE + (SEEDS_SUP[:2] if quick else SEEDS_SUP)]
    tasks += [("unif", s, As) for s in ([101, 102] if quick else list(range(101, 113)))]
    tasks += [("pi", 0, As)]
    with Pool(procs) as pool:
        sw = pool.map(_j2_task, tasks, chunksize=1)
    out["empirical"] = [dict(kind=s["kind"], seed=s["seed"], res={str(A): v for A, v in s["res"].items()}) for s in sw]
    out["wall"] = time.time() - t0
    return out
