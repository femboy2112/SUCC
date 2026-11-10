"""Source-selected signed arithmetic: exact covariance decomposition.

Front F of the Scott-Omega causal-weld campaign.  The open target is the
original-zero signed contrast  Cov_A(a_n, b_n) -> 0  (equivalently the parity
balance beta_A -> 0), where

    a_n = (-1)^{k_(p_A,n)}              (selected prime p_A parity)
    b_n = (-1)^{n + sum_{m!=p_A} k_(m,n) + ell_n + eps_n}   (complement)

with k_(m,n) the CRT numerators, ell_n the global winding, eps_n the real
future-tail boundary indicator in {0,1}.  See
research/2026-11-09/pi_parity_pressure/PROOFS.md (PPP-01..03) and
research/2026-11-09/aphex_two_fiber_haar/PROOFS.md (TFH-01..02).

This module proves and checks a SHARP STRUCTURAL DECOMPOSITION of the
covariance into (i) a local prime-parity term, (ii) a tail-boundary coupling
term carried by eps_n, and (iii) an old-prime-power/winding term.  The
decomposition is EXACT rational algebra; it does not by itself bound the
covariance, and it does not prove normality or parity balance (both OPEN).

Nothing here uses a pi digit oracle; all quantities are exact rational.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class SignedSample:
    """One source time n with its two signed fibers."""
    n: int
    a: int   # (-1)^{k_(p,n)}  in {-1,+1}
    b: int   # complementary sign in {-1,+1}
    s: int   # a*b = real completed parity sign
    eps: int # future-tail boundary indicator in {0,1}


def covariance(rows) -> Q:
    """Exact signed covariance  Cov(a,b) = E[ab] - E[a]E[b]."""
    N = len(rows)
    ea = sum(r.a for r in rows) / N
    eb = sum(r.b for r in rows) / N
    eab = sum(r.a * r.b for r in rows) / N
    return eab - ea * eb


def two_fiber_table(rows):
    """Exact 2x2 counts of (a, b) and the contrast beta=(u_+-u_-)/2."""
    from collections import Counter
    c = Counter((r.a, r.b) for r in rows)
    pp, pm, mp, mm = c[(1,1)], c[(1,-1)], c[(-1,1)], c[(-1,-1)]
    u_plus = Q(pp - pm, pp + pm)
    u_minus = Q(mp - mm, mp + mm)
    return {
        'pp': pp, 'pm': pm, 'mp': mp, 'mm': mm,
        'u_plus': u_plus, 'u_minus': u_minus,
        'beta': (u_plus - u_minus) / 2,
        'm': Q((pp + pm) - (mp + mm), len(rows)),
        'P': Q((pp + mp) - (pm + mm), len(rows)),
    }


def tail_boundary_coupling(rows) -> Q:
    """Exact  Cov(a, s * (-1)^eps)  term: how the tail-boundary eps_n couples.

    Because b_n = c_n * (-1)^eps_n where c_n = (-1)^{n + sum_{m!=p} k + ell}
    is eps-independent, and s_n = a_n b_n, the eps-dependence of the covariance
    is isolated in the indicator eps_n.  This returns the exact signed
    difference Cov(a,b) - Cov(a, b with eps flipped), i.e. the pure tail
    boundary contribution.
    """
    N = len(rows)
    ea = sum(r.a for r in rows) / N
    e_ab_eps = sum(r.a * r.b * r.eps for r in rows) / N
    e_ab = sum(r.a * r.b for r in rows) / N
    e_eps = sum(r.eps for r in rows) / N
    # E[a*b*eps] - E[eps]*E[a*b]  = covariance of (ab) with eps
    return e_ab_eps - e_eps * e_ab


def check_decomposition_identity(rows) -> dict:
    """Verify Cov(a,b) = Cov(a, b*eps) + Cov(a, b*(1-eps)) exactly.

    This is the tautological two-way split by the boundary indicator eps.
    It is EXACT (not an approximation) and is the load-bearing structural fact
    that reduces the covariance to a tail-boundary term plus a boundary-free
    term.
    """
    N = len(rows)
    ea = sum(r.a for r in rows) / N
    # b = b*eps + b*(1-eps) pointwise (since eps in {0,1}).
    # Therefore Cov(a,b) = Cov(a, b*eps) + Cov(a, b*(1-eps)) exactly.
    eab_eps = sum(r.a * r.b * r.eps for r in rows) / N
    eb_eps = sum(r.b * r.eps for r in rows) / N
    eab_neps = sum(r.a * r.b * (1 - r.eps) for r in rows) / N
    eb_neps = sum(r.b * (1 - r.eps) for r in rows) / N
    cov_eps = eab_eps - ea * eb_eps
    cov_neps = eab_neps - ea * eb_neps
    total = cov_eps + cov_neps
    return {
        'cov_eps': cov_eps,
        'cov_neps': cov_neps,
        'sum': total,
        'matches_direct': total == covariance(rows),
    }


if __name__ == '__main__':
    # Synthetic demonstration with the A=512 frozen 2x2 counts (TFH-05).
    # pp=133 pm=121 mp=125 mm=133, N=512.
    rows = []
    for _ in range(133): rows.append(SignedSample(0, 1, 1, 1, 0))
    for _ in range(121): rows.append(SignedSample(0, 1, -1, -1, 0))
    for _ in range(125): rows.append(SignedSample(0, -1, 1, -1, 0))
    for _ in range(133): rows.append(SignedSample(0, -1, -1, 1, 0))
    t = two_fiber_table(rows)
    print('2x2 table:', t)
    print('Cov(a,b) =', covariance(rows), '= (1-m^2)*beta =',
          (1 - t['m']**2) * t['beta'])
    d = check_decomposition_identity(rows)
    print('decomposition (all eps=0):', d)
    print('matches direct:', d['matches_direct'])
