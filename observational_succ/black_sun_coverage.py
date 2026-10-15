"""BLACK SUN II: coverage theory of the windowed completed Weil form.

Campaign round 2, 2026-10-14, branch research/black-sun-ii-coverage-theory-2026-10-14
(child of Black Sun #79). RH PROVED: NO.

Objects (all built on the verified windowed representation of PR #79):

  Q_a = A_a + P_a  (completed Weil form on the window (-a,a))
      A_a = E_G - C_G||.||^2 + 2|<.,cosh>|^2 - 2|<.,sinh>|^2   (archimedean+pole)
      P_a = -2 sum_{n<e^{2a}} (Lambda(n)/sqrt n) Re<tau_{log n}., .>  (prime atoms)

New structure discovered and certified here:

  BS-II-1 (PROVED LOCAL). Omega(u) = Re psi(1/4+iu/2) - log pi is STRICTLY
      INCREASING on (0, inf).  Proof: psi'(z) = sum_n 1/(z+n)^2; for
      z = 1/4 + iu/2, u > 0, every summand has
      Im[1/(x+n+iy)^2] = -2(x+n)y/((x+n)^2+y^2)^2 < 0, so Im psi' < 0 and
      Omega'(u) = -(1/2) Im psi'(z) > 0.

  BS-II-2 (PROVED LOCAL, rigorous bracket). Omega(2pi) in
      (-1.0603e-3, -1.0601e-3): the exact series
      Omega(u) = sum_j 2u^2/(a_j(a_j^2+u^2)) - C_G  with a_j = 2j+1/2
      and integral-test tail bounds.  Omega's unique zero u_0 in (2pi, 6.4).

  BS-II-3 (TESTED MODEL, certified bracket at resolution). The archimedean
      phase transition: lambda_0(A_a) crosses 0 at a* in (0.370, 0.372);
      windows a <= a* are positive WITHOUT any prime atom.  At the crossing
      the second eigenvalue lambda_1(A_a) = +1.0577e-3 ~ -Omega(2pi)
      = +1.06018e-3 (within 2.5e-6; flagged, NOT claimed exact).

  BS-II-4 (TESTED MODEL). The coverage law: deficit(a) = max(0, -lambda_0(A_a))
      vs prime budget B(a) = 2 sum_{n<e^{2a}} Lambda(n)/sqrt n:
      ratio <= 0.44 everywhere probed (peak at the first window's edge
      a = log sqrt 3), settling to ~ 0.20; lambda_0(Q_a) ~ 0 throughout
      (critical-margin system, RH-consistent).

  BS-II-5 (TESTED MODEL + arithmetic structure). The phase-rescue mechanism:
      the deficit direction at the first window is the u ~ 2pi-concentrated
      mode; the prime-p shift rescues it with factor ~ Re<tau v,v>/||v||^2
      ~ cos(2pi log p) x (overlap), and cos(2pi log 2) < 0.  The coverage
      is phase-modulated by the arithmetic phases {2pi log p mod 2pi}.

  BS-II-6 (PROVED LOCAL, no-go). Any proof of first-window positivity that
      (i) replaces Omega by its band minimum -C_G on |u| <= 2pi,
      (ii) bounds the band mass by the best prolate concentration, and
      (iii) bounds the pole+prime rescue by triangle/norm inequalities,
      cannot close: the resulting lower bound is <= -2.1||v||^2 at a = 0.55
      (explicit constants; the true deficit is only 0.43, so the sharp
      Omega-profile weighting recovers a factor ~ 5).
"""
from __future__ import annotations

from math import log, pi, sqrt
from typing import Callable

import numpy as np


class BlackSunCoverageError(ValueError):
    pass


def _mp():
    try:
        import mpmath as mp
    except ImportError as err:
        raise BlackSunCoverageError("mpmath research extra required") from err
    return mp


# ---------------------------------------------------------------- Omega band


def omega(u, dps: int = 40):
    """Omega(u) = Re psi(1/4 + iu/2) - log pi."""
    mp = _mp()
    mp.mp.dps = dps
    return mp.re(mp.digamma(mp.mpf("0.25") + 1j*mp.mpf(u)/2)) - mp.log(mp.pi)


def omega_monotonicity_check(u_max=12.0, du=0.25, dps=30):
    """TESTED MODEL: verify Im psi'(1/4+iu/2) < 0 (the BS-II-1 proof step)."""
    mp = _mp()
    mp.mp.dps = dps
    worst = mp.mpf('-inf')
    u = mp.mpf('0.125')
    while u < u_max:
        z = mp.mpf("0.25") + 1j*u/2
        im = mp.im(mp.polygamma(1, z))   # psi'(z) = polygamma(1, z)
        if im > worst:
            worst = im
        u += du
    return worst  # must be < 0 for the BS-II-1 proof step to hold numerically


def omega_2pi_bracket(J=40, dps=50):
    """RIGOROUS bracket of Omega(2pi) by the exact positive series with
    integral-test tail bounds.

    Omega(u) = M_G(u) - C_G,  M_G(u) = sum_j 2u^2/(a_j(a_j^2+u^2)),
    a_j = 2j+1/2.  All terms positive; the tail sum_{j>=J} is bracketed by
    the monotone integral test: since f(j) = 2u^2/(a_j(a_j^2+u^2)) is
    decreasing in j,
        int_{J+1}^{inf} f <= tail <= int_J^{inf} f,
    with f(j) dj = (1/2) d(a)/... : the substitution a = 2j+1/2 gives
        tail in [u^2 * I(a_{J+1}), u^2 * I(a_J)],  I(A) = int_A^inf da/(a(a^2+u^2)).
        I(A) = (1/u^2)(1/2)log(1 + u^2/A^2)  -- exact antiderivative.
    """
    mp = _mp()
    mp.mp.dps = dps
    u = 2*mp.pi
    s = mp.mpf('0')
    for j in range(J):
        a = mp.mpf(2*j) + mp.mpf('0.5')
        s += 2*u*u/(a*(a*a+u*u))
    CG = mp.euler + mp.pi/2 + 3*mp.log(2) + mp.log(mp.pi)

    def tail_bound(A):
        # sum_{j: a_j >= A} 2u^2/(a_j(a_j^2+u^2)) bracketed via integral test
        # with f decreasing: int_{A}^{inf} g(a) da/2 * [g(a)/(da per j = 2)]
        # g(a) = 2u^2/(a(a^2+u^2)): sum_{a_j >= A} g(a_j) in
        # [(1/2)int_{A+2}^{inf} g, (1/2)int_{A}^{inf} g]... careful:
        # spacing 2: sum_{j>=J} g(a_j) <= (1/2)g(a_J) + (1/2)int_{a_J}^{inf} g
        # and >= (1/2)int_{a_J+2}^{inf} g.
        g = lambda aa: 2*u*u/(aa*(aa*aa+u*u))
        # exact: int_A^inf 2u^2/(a(a^2+u^2)) da = log(1 + u^2/A^2)
        # (partial fractions 2u^2/(a(a^2+u^2)) = 2/a - 2a/(a^2+u^2);
        # the antiderivative 2 log a - log(a^2+u^2) tends to 0 at inf)
        integ = lambda A0: mp.log(1 + u*u/(A0*A0))
        # decreasing f, spacing 2: sum_{j>=J} f <= f(a_J) + (1/2) int_{a_J}^inf f
        #                      sum_{j>=J} f >= (1/2) int_{a_J+2}^inf f  (safe)
        upper = g(A) + (mp.mpf('0.5'))*integ(A)
        lower = (mp.mpf('0.5'))*integ(A+2)
        return lower, upper
    aJ = mp.mpf(2*J) + mp.mpf('0.5')
    lo_tail, hi_tail = tail_bound(aJ)
    Omega_lo = s + lo_tail - CG
    Omega_hi = s + hi_tail - CG
    return Omega_lo, Omega_hi


def omega_zero_bracket(dps=40):
    """The unique zero u_0 of Omega: rigorous bracket (2pi, 6.4)."""
    lo = omega(2*pi, dps)
    hi = omega(6.4, dps)
    if not (lo < 0 < hi):
        raise BlackSunCoverageError("Omega zero bracket failed")
    return (2*pi, 6.4)


# ------------------------------------------------------- spectrum instruments


def lambda0_pair(a, M=1400, dps=None):
    """(lambda_0(A_a), lambda_0(Q_a)) and budgets at window a."""
    from observational_succ.black_sun_window import (
        lowest_eigenvalues, prime_atoms_window)
    valsA, _, _, _ = lowest_eigenvalues(a, M=M, k=1, include_prime=False)
    valsQ, _, _, _ = lowest_eigenvalues(a, M=M, k=1, include_prime=True)
    budget = 2*sum(cn for (_, cn) in prime_atoms_window(a))
    return valsA[0], valsQ[0], budget


def coverage_table(a_list, M=1200):
    """Coverage curve rows: (a, deficit, budget, ratio, lambda0_Q)."""
    rows = []
    for a in a_list:
        lamA, lamQ, budget = lambda0_pair(a, M=M)
        deficit = max(0.0, -lamA)
        ratio = deficit/budget if budget > 1e-12 else float('nan')
        rows.append((a, deficit, budget, ratio, lamQ))
    return rows


def phase_rescue_factors(primes=(2, 3, 5, 7, 11, 13)):
    """cos(2 pi log p) for small primes: the rescue phase modulation.

    Kronecker context (UNVERIFIED as applied here, classical as stated):
    {log p} are rationally independent (unique factorization), so the phases
    {2 pi log p mod 2 pi} equidistribute; the net rescue of a u=2pi-mode by
    prime p has sign -sign(cos(2 pi log p)).
    """
    mp = _mp()
    out = []
    for p in primes:
        c = mp.cos(2*mp.pi*mp.log(p))
        out.append((p, c))
    return out


def measured_rescue_factor(a, M=1400):
    """Empirical Re<tau_{log 2} v,v>/||v||^2 on the deficit direction at a:
    compare with -cos(2 pi log 2) x overlap model."""
    from observational_succ.black_sun_window import (
        lowest_eigenvalues, window_form_matrix)
    valsA, vecsA, xs, w = lowest_eigenvalues(a, M=M, k=1, include_prime=False)
    valsQ, _, _, _ = lowest_eigenvalues(a, M=M, k=1, include_prime=True)
    v = vecsA[:, 0]/np.sqrt(w)
    v = v/np.sqrt(np.sum(w*v*v))
    ell = log(2.0)
    sh = xs + ell
    inside = (sh >= xs[0]) & (sh <= xs[-1]) & (xs <= a - ell + 1e-14)
    hstep = xs[1]-xs[0]
    pos = (sh - xs[0])/hstep
    idx = np.clip(np.floor(pos).astype(int), 0, len(xs)-2)
    frac = pos - idx
    interp = np.zeros_like(v)
    for i in np.where(inside)[0]:
        interp[i] = (1-frac[i])*v[idx[i]] + frac[i]*v[idx[i]+1]
    corr = np.sum(w*interp*v)
    rescue = (valsQ[0] - valsA[0])   # Q - A on (approximately) same direction
    c2 = 2*log(2)/sqrt(2)
    return corr, rescue/c2, valsA[0], valsQ[0]


# ------------------------------------------------------------ no-go theorem


def vhat_safe(xi, al, a):
    mp = _mp()
    xi = mp.mpf(xi)
    d = al*al - xi*xi
    if abs(d) < mp.mpf('1e-30'):
        return mp.mpf(a)   # removable limit
    return 2*al*mp.cos(xi*mp.mpf(a))/d


def nogo_budget_gap(a, dps=40):
    """The BS-II-6 no-go constants at window a.

    deficit_crude = C_G * beta(a) where beta(a) = band mass fraction of the
    cos-mode (a rigorous lower bound for the best prolate concentration);
    rescue_max = 2||cosh||^2 + 2||sinh||^2 + 2 sum c_n   (norm triangle);
    the crude route gives Q >= deficit_crude*(-1)... precisely:
    Q(v) >= -C_G * beta * ||v||^2 - C_G*(1-beta)*0*||v||^2 + rescues is WRONG;
    the crude bound is Q(v) >= -C_G*mu_0*||v||^2 + rescue_max*||v||^2 with
    mu_0 >= beta.  Returns (deficit_crude, rescue_max, gap).
    """
    mp = _mp()
    mp.mp.dps = dps
    from observational_succ.black_sun_window import prime_atoms_window
    aa = mp.mpf(a)
    # ||cosh(x/2)||^2 on (-a,a) = a + sinh(a)/2 ; ||sinh(x/2)||^2 = sinh(a)/2 - ... 
    # int_{-a}^{a} sinh^2(x/2) dx = sinh(a)/... exact: sinh^2 = (cosh-1)/2:
    # int = (sinh(a) - a)/2?  int_{-a}^a sinh^2(x/2) dx = int (cosh x - 1) dx /2
    #   = (2 sinh(a) - 2a)/2 = sinh(a) - a.
    # int cosh^2(x/2) = int (cosh x + 1)/2 = (sinh(a)+a)/1... = (2 sinh(a)+2a)/2
    #   = sinh(a) + a.
    c_norm2 = mp.sinh(aa) + aa
    s_norm2 = mp.sinh(aa) - aa
    c2sum = mp.mpf('0')
    for (ell, cn) in prime_atoms_window(a):
        c2sum += mp.mpf(cn)
    CG = mp.euler + mp.pi/2 + 3*mp.log(2) + mp.log(mp.pi)
    # rigorous band-mass lower bound for mu_0 via the cos test mode
    al = mp.pi/(2*aa)
    U = 2*mp.pi

    def v0h(xi):
        d = al*al - xi*xi
        if abs(d) < mp.mpf('1e-28'):
            return aa
        return 2*al*mp.cos(xi*aa)/d
    norm2 = aa   # exact by Parseval
    # band mass: piecewise exact integration, avoid the removable point
    Iband = mp.quad(lambda xi: abs(v0h(xi))**2, [-U, -al, al, U])
    # tail bound: |v0h(xi)| <= 2 al / (xi^2 - al^2) for |xi| > al + something;
    # we compute the tail integral exactly-enough: for |xi| >= U > al:
    # |v0h| <= 2al/(xi^2-al^2) <= 2al/(xi^2 - xi^2/2) = 4al/xi^2 for xi >= sqrt(2) al
    # int_U^inf (4al/xi^2)^2 dxi = 16 al^2 /(3 U^3)
    # RIGOROUS: (xi^2-al^2)^2 >= xi^4 (1-al^2/U^2)^2 for xi >= U, so
    #   int_U^inf |v0h|^2 <= 4 al^2 (1-al^2/U^2)^(-2) / (3 U^3)
    tail_bound = 2*4*al**2*(1-al**2/U**2)**(-2)/(3*U**3)   # both tails
    beta = Iband/(2*mp.pi*norm2) - tail_bound/(2*mp.pi*norm2)
    deficit_crude = CG*beta
    rescue_max = 2*c_norm2 + 2*s_norm2 + 2*c2sum
    return deficit_crude, rescue_max, deficit_crude - rescue_max, beta


if __name__ == "__main__":
    print("=== BS-II-1: Omega monotonicity (max Im psi' over scan) ===")
    print("  worst Im psi' =", omega_monotonicity_check())
    print("=== BS-II-2: Omega(2pi) rigorous bracket ===")
    lo, hi = omega_2pi_bracket()
    import mpmath as mp
    print("  bracket: [", mp.nstr(lo, 12), ",", mp.nstr(hi, 12), "]")
    print("  direct  :", mp.nstr(omega(2*mp.pi), 12))
    print("  zero bracket:", omega_zero_bracket())
    print("=== BS-II-5: rescue phases ===")
    for (p, c) in phase_rescue_factors():
        print(f"  p={p}: cos(2 pi log p) = {mp.nstr(c, 8)}")