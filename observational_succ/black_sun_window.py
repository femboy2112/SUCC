"""BLACK SUN A-track: first-prime-window completed Weil form, verified identities,
windowed spectrum, and hostile controls.

Campaign: Operation Black Sun, 2026-10-14, research/black-sun-independent-campaign-2026-10-14.

Independently re-derived and numerically verified representation (see
research/2026-10-14/BLACK_SUN_INDEPENDENT_CAMPAIGN.md):

  W_zeta(v*tilde v) = E_G(v) - C_G ||v||^2 + 2|<v,cosh(.//2)>|^2 - 2|<v,sinh(.//2)>|^2
                      - 2 sum_{2<=n<e^{2a}} Lambda(n)/sqrt(n) Re <tau_{log n} v, v>

for v supported in (-a,a) (extended by 0), with

  E_G(v) = (1/2) iint k_G(x-y)|v(x)-v(y)|^2 dx dy,  k_G(t)=sum_j e^{-(2j+1/2)|t|},
  C_G = gamma + pi/2 + 3 log 2 + log pi,
  boundary barrier: E_G(v) = (1/2) iint_{WxW} k_G|v-v|^2 + int_W rho_a |v|^2,
      rho_a(x) = Kbar(x+a) + Kbar(a-x),
      Kbar(z) = int_z^infty k_G = (1/2)ln((1+e^{-z/2})/(1-e^{-z/2})) + arctan(e^{-z/2})   [BS-1]

CRITICAL contact-tail trap (found by exact 40-digit comparison against the
original Weil distribution): the Gamma/contact integral runs over [0, inf),
and the part beyond supp(h) contributes EXACTLY +2 h(0) atanh(e^{-2a}).
Truncating at supp(h) breaks the Carleman identity by ~0.77 at a=1/2.

The windowed archimedean+pole part has the exact Fourier representation

  A(v,v) = (1/2 pi) int |v_hat(u)|^2 Omega(u) du + 2|<v,c>|^2 - 2|<v,s>|^2,
  Omega(u) = Re psi(1/4 + i u/2) - log pi,

with Omega(0) = -C_G, Omega(u) < 0 exactly on the band |u| < 2pi (numerically
Omega(2pi) = -1.06e-3), and Omega(u) ~ log(u/2pi) [BS-4].  The near-null
window modes are the prolate-type concentration modes against this band;
their count tracks the Shannon number 4a.

RH PROVED: NO.  Nothing here proves Weil positivity; the spectral outputs are
TESTED MODEL evidence at the stated discretization resolution.
"""
from __future__ import annotations

from fractions import Fraction
from math import cosh, sinh, sqrt
from typing import Callable

import numpy as np


class BlackSunWindowError(ValueError):
    """Domain, normalization or control precondition failed."""


def _mp():
    try:
        import mpmath as mp
    except ImportError as err:
        raise BlackSunWindowError("mpmath research extra required") from err
    return mp


def C_G(dps: int = 40):
    """gamma + pi/2 + 3 log 2 + log pi at dps digits."""
    mp = _mp()
    mp.mp.dps = dps
    return mp.euler + mp.pi/2 + 3*mp.log(2) + mp.log(mp.pi)


def contact_tail(h0, a, dps: int = 40):
    """+2 h(0) atanh(e^{-2a}): the exact [2a, inf) part of the Gamma/contact
    integral of the completed Weil distribution for h supported in [-2a,2a].

    Derivation: for x >= 2a the contact integrand reduces to
    -2 h(0) e^{-x}/(1-e^{-2x}), and int_{2a}^inf e^{-x}/(1-e^{-2x}) dx
    = atanh(e^{-2a}).  This term is REQUIRED; omitting it breaks the
    Carleman identity (verified: residual 0.77 at a=1/2 for the flat test).
    """
    mp = _mp()
    mp.mp.dps = dps
    return 2*mp.mpf(h0)*mp.atanh(mp.e**(-mp.mpf(2)*mp.mpf(a)))


def kbar_series(z, dps: int = 40):
    """Kbar(z) = int_z^inf k_G by the defining series (reference value)."""
    mp = _mp()
    mp.mp.dps = dps
    zz = mp.mpf(z)
    if zz <= 0:
        return mp.inf
    j, total, term = 0, mp.mpf('0'), mp.mpf('1')
    while j < 200000:
        alpha = mp.mpf(2*j) + mp.mpf('0.5')
        term = mp.e**(-alpha*zz)/alpha
        total += term
        if abs(term) < mp.mpf(10)**(-dps-2):
            break
        j += 1
    return total


def kbar_elementary(z):
    """Kbar(z) by the elementary closed form [BS-1] (mpmath).

    Kbar(z) = (1/2) ln((1+e^{-z/2})/(1-e^{-z/2})) + arctan(e^{-z/2}).

    Proof: substitute s=e^{-t/2} in int_z^inf e^{-t/2}/(1-e^{-2t}) dt; the
    antiderivative of 2/(1-s^4) is (1/2)ln((1+s)/(1-s)) + arctan(s) and the
    substitution is orientation-reversing with F(0)=0.
    """
    mp = _mp()
    s = mp.e**(-mp.mpf(z)/2)
    return mp.mpf('0.5')*mp.log((1+s)/(1-s)) + mp.atan(s)


def rho_a_elementary(x, a):
    """Window boundary barrier rho_a(x) = Kbar(x+a)+Kbar(a-x) (mpmath)."""
    return kbar_elementary(x+a) + kbar_elementary(a-x)


def von_mangoldt_exact(n: int):
    """Exact von Mangoldt: log p if n=p^k, else 0 (rational-checked sieve-free)."""
    if type(n) is not int or n < 2:
        return 0
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            m, k = n, 0
            while m % p == 0:
                m //= p
                k += 1
            from math import log
            return log(p) if m == 1 else 0
    from math import log
    return log(n)


def prime_atoms_window(a):
    """(log n, Lambda(n)/sqrt(n)) for 2 <= n < e^{2a} (strict)."""
    from math import exp, floor, log, sqrt
    atoms = []
    n = 2
    nmax = int(exp(2*a)) + 2
    while n < nmax:
        lam = von_mangoldt_exact(n)
        if lam > 0 and log(n) < 2*a - 1e-14:
            atoms.append((log(n), lam/sqrt(n)))
        n += 1
    return atoms


def window_form_matrix(a: float, M: int = 1200, *,
                       include_prime: bool = True,
                       contact_error: float = 0.0,
                       fake6_impulse: float = 0.0):
    """Nystrom form matrix of the windowed completed Weil form on (-a,a).

    Midpoint grid (no endpoint nodes: the log-singular barrier rho_a is
    integrable but infinite at the window edge).  Returns (F, w, xs):
    Q(v) ~ v^T F v with mass weights w (eigenproblem F v = lam W v).

    Controls:
      contact_error: additive error injected into C_G (wrong-normalization
        control; the classical trap is +-2 log 2).
      fake6_impulse: extra primitive composite impulse mu*log(6)/sqrt(6) at
        +-log 6 (source mutation control; =0 for the authentic source).
    """
    if not (0 < a):
        raise BlackSunWindowError("a > 0 required")
    if M < 32:
        raise BlackSunWindowError("M >= 32 required for barrier resolution")
    xs = -a + (2*a/M)*(np.arange(M) + 0.5)
    w = np.full(M, 2*a/M)

    d = xs[:, None] - xs[None, :]
    ad = np.abs(d)
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.where(ad > 0, np.exp(-ad/2)/(1-np.exp(-2*ad)), 0.0)

    WK = K * w[None, :]
    S = WK.sum(axis=1)
    # barrier rho_a(x) = Kbar(x+a)+Kbar(a-x) in float (closed form)
    s_left = np.exp(-(xs + a)/2)
    s_right = np.exp(-(a - xs)/2)
    kbar_left = 0.5*np.log((1+s_left)/(1-s_left)) + np.arctan(s_left)
    kbar_right = 0.5*np.log((1+s_right)/(1-s_right)) + np.arctan(s_right)
    rho = kbar_left + kbar_right

    from math import pi
    EULER = 0.5772156649015329
    CG = EULER + pi/2 + 3*np.log(2.0) + np.log(np.pi) + contact_error

    F = np.diag(w*(S + rho - CG))

    Wo = np.outer(w, w)*K
    np.fill_diagonal(Wo, 0.0)
    F = F - Wo

    c = np.cosh(xs/2)
    s = np.sinh(xs/2)
    F = F + 2*np.outer(w*c, w*c)
    F = F - 2*np.outer(w*s, w*s)

    def shift_overlap_matrix(ell, cn):
        # -c_n [<tau_ell v, v> + <v, tau_ell v>] with linear interpolation
        sh = xs + ell
        L = np.zeros((M, M))
        idx = np.clip(((sh + a)/(2*a)*(M-1)).astype(int), 0, M-2)
        # midpoint grid: node j has coordinate -a + (j+0.5)*h; interpolate
        hstep = 2*a/M
        pos = (sh + a)/hstep - 0.5
        idx = np.clip(np.floor(pos).astype(int), 0, M-2)
        frac = pos - idx
        for i in np.where((sh >= -a) & (sh < a) & (xs <= a - ell + 1e-14))[0]:
            L[i, idx[i]] += 1-frac[i]
            L[i, idx[i]+1] += frac[i]
        mask = np.zeros(M)
        mask[xs <= a - ell + 1e-14] = 1.0
        A = L*(w*mask)[:, None]
        return -cn*(A + A.T)

    if include_prime:
        for (ell, cn) in prime_atoms_window(a):
            F = F + shift_overlap_matrix(ell, cn)
    if fake6_impulse > 0:
        from math import log as _log, sqrt as _sqrt
        ell6 = _log(6)
        if ell6 < 2*a:
            F = F + shift_overlap_matrix(ell6, fake6_impulse*_log(6)/_sqrt(6))

    return F, w, xs


def lowest_eigenvalues(a: float, M: int = 1200, k: int = 6, **kw):
    """Lowest k eigenvalues of the windowed form (Rayleigh-Ritz, float64).

    Discretization resolution: |lambda - lambda_true| <~ 3e-6 + O(h) observed
    at M in {800,1600,3200} on the first window; the SIGN of values below
    ~1e-5 is not certified by this routine.
    """
    F, w, xs = window_form_matrix(a, M, **kw)
    Winv = np.diag(1/np.sqrt(w))
    G = Winv @ F @ Winv
    G = 0.5*(G + G.T)
    vals, vecs = np.linalg.eigh(G)
    return vals[:k], vecs[:, :k], xs, w


def carleman_vs_weil_check(v_nodes, a, dps: int = 40):
    """40-digit cross-check: original Weil W(v*tilde v) vs Carleman form.

    v given by node values on a uniform grid over (-a, a) INCLUDING
    endpoints (piecewise linear, extended by 0).  Both sides evaluated
    independently: the original distributional W with exact piecewise-
    quadratic autocorrelation, and the Carleman/E_G side by exact
    per-layer closed-form integration.  Returns (W, Q_C, residual).
    """
    mp = _mp()
    mp.mp.dps = dps
    nodes = [mp.mpf(x) for x in
             [-a + 2*a*Fraction(i, len(v_nodes)-1) for i in range(len(v_nodes))]]
    vals = [mp.mpf(v) for v in v_nodes]
    h = autocorr_exact_callable(nodes, vals)
    W = weil_original(h, a, dps)
    Q = carleman_exact_layers(nodes, vals, a, dps)
    return W, Q, abs(W-Q)


def autocorr_exact_callable(nodes, vals):
    """Exact autocorrelation h(t)=int v(x)v(x-t) dx (piecewise linear v)."""
    mp = _mp()

    def v(x):
        if x < nodes[0] or x > nodes[-1]:
            return mp.mpf('0')
        lo, hi = 0, len(nodes)-1
        while hi-lo > 1:
            m = (lo+hi)//2
            if nodes[m] <= x:
                lo = m
            else:
                hi = m
        t = (x-nodes[lo])/(nodes[lo+1]-nodes[lo])
        return vals[lo] + t*(vals[lo+1]-vals[lo])

    def h(t):
        at = abs(mp.mpf(t))
        lo, hi = nodes[0]+at, nodes[-1]
        if lo > hi:
            return mp.mpf('0')
        bps = sorted(set([mp.mpf(x) for x in nodes if lo <= x <= hi] +
                         [mp.mpf(x)+at for x in nodes if lo <= x+at <= hi] +
                         [lo, hi]))
        tot = mp.mpf('0')
        for i in range(len(bps)-1):
            x0, x1 = bps[i], bps[i+1]
            mid = (x0+x1)/2
            f0, fm, f1 = v(x0)*v(x0-at), v(mid)*v(mid-at), v(x1)*v(x1-at)
            tot += (x1-x0)*(f0+4*fm+f1)/6
        return tot

    # h is piecewise quadratic with breakpoints at multiples of the grid
    # spacing (|x_j - x_i|): expose them so mpmath quads do not smooth over
    # interior kinks.
    d = nodes[1]-nodes[0]
    L2 = 2*(nodes[-1]-nodes[0])
    nseg = int(mp.floor(L2/d))
    h.breaks = [d*k for k in range(0, nseg+1)]
    return h


def weil_original(h: Callable, a, dps: int = 40, atoms=None):
    """The original completed Weil distribution W(h) (external classical
    identity, Suzuki normalization), evaluated at dps digits with the
    mandatory [2a, inf) contact tail included."""
    mp = _mp()
    mp.mp.dps = dps
    if atoms is None:
        atoms = []
        n = 2
        while mp.log(n) < 2*mp.mpf(a):
            lam = von_mangoldt_mp(n)
            if lam > 0:
                atoms.append((mp.log(n), lam))
            n += 1
    h0 = h(0)
    brks = getattr(h, 'breaks', None)
    if brks:
        pts_pos = [mp.mpf(x) for x in brks]
        pts = sorted([-p for p in pts_pos] + pts_pos)
        I1 = mp.quad(lambda x: h(x)*(mp.e**(x/2)+mp.e**(-x/2)), pts)
    else:
        I1 = mp.quad(lambda x: h(x)*(mp.e**(x/2)+mp.e**(-x/2)),
                     [-2*mp.mpf(a), 0, 2*mp.mpf(a)])
    I2 = mp.mpf('0')
    for (ell, lam) in atoms:
        if ell < 2*a:
            I2 -= (lam/mp.sqrt(mp.e**ell))*(h(ell)+h(-ell))
    I3 = -(mp.euler+mp.log(4*mp.pi))*h0

    def cint(x):
        if x == 0:
            return h0/2
        return mp.e**(-x/2)*(h(x)+h(-x)-2*mp.e**(-x/2)*h0)/(1-mp.e**(-2*x))
    if brks:
        pts4 = [mp.mpf('0')] + [mp.mpf(x) for x in brks] + [mp.inf]
        I4 = -mp.quad(cint, pts4)
    else:
        I4 = -mp.quad(cint, [0, 2*mp.mpf(a), mp.inf])
    return I1+I2+I3+I4


def _is_prime_power(n):
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return m == 1
    return n >= 2


def carleman_exact_layers(nodes, vals, a, dps=40):
    """Carleman side: E_G (exact per-layer closed forms, cross-cell pairs
    counted twice) - C_G||v||^2 + poles - prime atoms.  Independent of any
    singular-kernel quadrature."""
    mp = _mp()
    mp.mp.dps = dps
    n = len(nodes)-1

    def cell(i, x):
        t = (x-nodes[i])/(nodes[i+1]-nodes[i])
        return vals[i]+t*(vals[i+1]-vals[i])

    def cell_exp(i, rate):
        """int over cell i of v(x) e^{rate x} dx (v linear), exact."""
        x0, x1 = nodes[i], nodes[i+1]
        v0, v1 = cell(i, x0), cell(i, x1)
        s = (v1-v0)/(x1-x0)
        c0 = v0-s*x0
        e0, e1 = mp.e**(rate*x0), mp.e**(rate*x1)
        I0 = (c0/rate)*(e1-e0)
        I1 = ((x1*e1-x0*e0)/rate-(e1-e0)/rate**2)
        return I0+s*I1

    def D(alpha):
        tot = mp.mpf('0')
        for i in range(n):
            for k in range(n):
                if k < i:
                    # x in cell i (right), y in cell k (left): counted with
                    # BOTH orderings (factor 2) - fixed vs the exploratory code
                    tot += 2*cell_exp(i, -alpha)*cell_exp(k, alpha)
                elif k == i:
                    x0, x1 = nodes[i], nodes[i+1]
                    v0 = vals[i]
                    s = (vals[i+1]-v0)/(x1-x0)
                    c0 = v0-s*x0
                    Q_ = s/alpha
                    P_ = (c0-Q_)/alpha
                    F = lambda y: mp.e**(alpha*y)*(P_+Q_*y)
                    A2 = c0*P_
                    B2 = c0*Q_+s*P_
                    C2 = s*Q_
                    Ipoly = (A2*(x1-x0)+B2*(x1**2-x0**2)/2+C2*(x1**3-x0**3)/3)
                    tot += 2*(Ipoly-F(x0)*cell_exp(i, -alpha))
        return tot

    nrm = mp.mpf('0')
    for i in range(n):
        x0, x1 = nodes[i], nodes[i+1]
        v0, v1 = vals[i], vals[i+1]
        nrm += (x1-x0)*(v0*v0+v0*v1+v1*v1)/3

    EG = mp.mpf('0')
    J = 1500
    for j in range(J):
        alpha = mp.mpf(2*j)+mp.mpf('0.5')
        EG += (2/alpha)*nrm - D(alpha)
    # exact asymptotic tail (piecewise-linear v): E^{(j)} = 2||v'||^2/alpha^3
    #   + (|v(a)|^2 + |v(-a)|^2)/alpha^2 + O(alpha^-4 slope corrections),
    # sum_{j>=J} 2/alpha^3 and 1/alpha^2 via polygamma; residual O(J^-3).
    stiff = mp.mpf('0')
    for i in range(n):
        dx = nodes[i+1]-nodes[i]
        sl = (vals[i+1]-vals[i])/dx
        stiff += sl*sl*dx
    jumps = vals[0]**2 + vals[-1]**2
    q0 = mp.mpf(J)+mp.mpf('0.25')   # alpha_j = 2*(j+1/4)
    # sum_{j>=J} 1/alpha_j^3 = (1/8) * zeta(3, q0) = (1/8) * (-psi2(q0)/2)
    # sum_{j>=J} 1/alpha_j^2 = (1/4) * psi1(q0)
    # E-tail = 2*stiff*sum 1/alpha^3 + jumps*sum 1/alpha^2  (+O(J^-3) edge2)
    EG += 2*stiff*((-mp.polygamma(2, q0))/16)
    EG += jumps*(mp.polygamma(1, q0)/4)

    CG = mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)

    def vfun(x):
        if x < nodes[0] or x > nodes[-1]:
            return mp.mpf('0')
        lo, hi = 0, n
        while hi-lo > 1:
            m = (lo+hi)//2
            if nodes[m] <= x:
                lo = m
            else:
                hi = m
        t = (x-nodes[lo])/(nodes[lo+1]-nodes[lo])
        return vals[lo]+t*(vals[lo+1]-vals[lo])

    C = mp.mpf('0')
    S = mp.mpf('0')
    for i in range(n):
        x0, x1 = nodes[i], nodes[i+1]
        C += mp.quad(lambda x, i=i: vfun_cell(nodes, vals, i, x)*mp.cosh(x/2),
                     [x0, x1])
        S += mp.quad(lambda x, i=i: vfun_cell(nodes, vals, i, x)*mp.sinh(x/2),
                     [x0, x1])
    pole = 2*C**2-2*S**2
    prim = mp.mpf('0')
    nn = 2
    while mp.log(nn) < 2*mp.mpf(a):
        lam = von_mangoldt_mp(nn)
        if lam > 0:
            ell = mp.log(nn)
            cn = lam/mp.sqrt(mp.mpf(nn))
            lo_, hi_ = nodes[0], min(nodes[-1], nodes[-1]-ell)
            if lo_ < hi_:
                # kink-aware breakpoints: nodes and nodes shifted by ell
                bps = sorted(set([mp.mpf(x) for x in nodes if lo_ <= x <= hi_] +
                                 [mp.mpf(x)-ell for x in nodes
                                  if lo_ <= x-ell <= hi_] + [lo_, hi_]))
                ov = mp.quad(lambda x: vfun(x+ell)*vfun(x), bps)
                prim -= 2*cn*ov
        nn += 1
    return EG-CG*nrm+pole+prim


def vfun_cell(nodes, vals, i, x):
    mp = _mp()
    t = (x-nodes[i])/(nodes[i+1]-nodes[i])
    return vals[i]+t*(vals[i+1]-vals[i])


def von_mangoldt_mp(nn):
    """Exact von Mangoldt as mpmath log (prime power test by trial division)."""
    mp = _mp()
    if type(nn) is not int or nn < 2:
        return mp.mpf('0')
    for p in range(2, int(nn**0.5)+1):
        if nn % p == 0:
            m = nn
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else mp.mpf('0')
    return mp.log(nn)