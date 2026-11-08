#!/usr/bin/env python3
"""Main XXI integration-time receipt for #540 claim GA-09 (REFUTED false shortcut).

#540 CLAIM_LEDGER.md labels GA-09 -- "finite K=3 anti-clustering directly makes the
golden aperture energy E_a -> 0" -- as REFUTED, but its listed evidence only shows that
direct integration of the K-bound fails (E_a <= 1/A + (K-2)b/2).  A failed proof route
is not a refutation (AGENTS.md rule 11), so this file supplies the countermodel.

Countermodel (any A >= 1):  mu_A = (1/A) sum_{j<A} delta_{j L / A},  L = 2/3,
i.e. A equally spaced points filling an arc of length 2/3.  This is NOT the BBP source;
it is a general point configuration showing the K-bound alone cannot force Haar.

(i)  B_A(t) <= A + 3 A^2 t for every t in [0, 1/2]   (K = 3; covers ET4-OPEN's range
     [1/(A+1), 1/2] and GA-03's range [0, b]).
     Proof.  For t < 1/3: with d = |j-k|, dL/A < 2/3, so 1 - dL/A > 1/3 > t and
     d_T <= t  iff  d <= D := floor(tA/L).  Hence B_A(t) = A + 2DA - D(D+1) <= A + 2DA,
     while t >= D L / A gives 3 A^2 t >= 3 A D L = 2AD.  For t in [1/3, 1/2]:
     B_A(t) <= A^2 <= A + 3 A^2 t.                                                  QED
(ii) E_a(mu_A) -> E_a(nu_L) = sqrt(5)/9 - 1/6 > 0 (nu_L uniform on the arc), because
     mu_A => nu_L weakly and E_a(mu) = iint k_gold(x-y) dmu dmu with k_gold continuous
     (#540 GA-02).  The value is the integral of (b - d_T(u))_+ / b against the
     triangular difference density (L-|u|)/L^2 on [-L, L], minus b; positive since
     sqrt(5) > 3/2.

Conclusion: "K-anticlustering => E_a -> 0" is false for general configurations, so any
normality consequence of #536/#538's finite K=3 certificates must use source structure
(the x16 frequency-ray rigidity), exactly as #540 GA-03 says.  pi normality stays OPEN.

Exact arithmetic only: fractions.Fraction for distances, sympy Q(sqrt5) for energies.
Run:  python research/2026-11-07/main_xxi_receipts/ga09_countermodel.py
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction

import sympy as sp

L = Fraction(2, 3)
SQRT5 = sp.sqrt(5)
B_GOLD = (3 - SQRT5) / 2          # b = 1 - phi^-1 = phi^-2
E_LIMIT = SQRT5 / 9 - sp.Rational(1, 6)


def pair_distance_counts(A: int) -> dict[Fraction, int]:
    """Ordered off-diagonal pair counts by exact circular distance for the arc grid."""
    if not isinstance(A, int) or isinstance(A, bool) or A < 1:
        raise ValueError("A must be a positive integer")
    out: dict[Fraction, int] = {}
    for d in range(1, A):
        lin = d * L / A
        dist = min(lin, 1 - lin)
        out[dist] = out.get(dist, 0) + 2 * (A - d)
    return out


def k_max(A: int) -> Fraction:
    """max over all radii t in (0, 1/2] of (B_A(t) - A) / (A^2 t), exactly.

    B_A is a right-continuous step function, so the max is attained at a jump point.
    """
    B, best = A, Fraction(0)
    for dist, c in sorted(pair_distance_counts(A).items()):
        B += c
        if dist <= Fraction(1, 2):
            best = max(best, Fraction(B - A, A * A) / dist)
    return best


def golden_energy(A: int) -> sp.Expr:
    """E_a(mu_A) via #540 GA2: (1/(b A^2)) sum_{i,j} (b - d_T)_+ - b, exact in Q(sqrt5).

    d < b is decided exactly: for 0 <= d <= 1/2, d < b iff (3 - 2d)^2 > 5.
    """
    S = A * B_GOLD
    for dist, c in pair_distance_counts(A).items():
        if (3 - 2 * dist) ** 2 > 5:
            S += c * (B_GOLD - sp.Rational(dist.numerator, dist.denominator))
    return sp.nsimplify(sp.expand(S / (B_GOLD * A * A) - B_GOLD))


def limit_energy_by_integration() -> sp.Expr:
    """Independent route for E_a(nu_L): integrate against the difference density."""
    u = sp.symbols("u")
    Ls = sp.Rational(L.numerator, L.denominator)
    dens = (Ls - u) / Ls**2
    inner = sp.integrate((B_GOLD - u) * dens, (u, 0, B_GOLD))
    wrap = sp.integrate((B_GOLD - (1 - u)) * dens, (u, 1 - B_GOLD, Ls))
    return sp.simplify(2 * (inner + wrap) / B_GOLD - B_GOLD)


def receipt(As=(50, 200, 800)) -> dict:
    lim = limit_energy_by_integration()
    rows = []
    for A in As:
        K = k_max(A)
        E = golden_energy(A)
        rows.append({"A": A, "K_max": f"{K.numerator}/{K.denominator}",
                     "K_max_equals_3_minus_3_over_A": K == 3 - Fraction(3, A),
                     "K_max_le_3": K <= 3,
                     "E_a_exact": str(E), "E_a_float": float(sp.N(E, 30))})
    return {"claim": "#540 GA-09 receipt: K=3 anti-clustering does not force golden E_a -> 0",
            "status": "PROVED LOCAL (elementary, (i)+(ii)) + CERTIFIED FINITE rows",
            "configuration": "A-point uniform grid on an arc of length 2/3 (not the BBP source)",
            "E_limit_exact": str(lim), "E_limit_float": float(sp.N(lim, 30)),
            "E_limit_matches_closed_form": sp.simplify(lim - E_LIMIT) == 0,
            # sqrt5/9 > 1/6  <=>  sqrt5 > 3/2  <=>  5 > 9/4 ; plus sympy's exact sign decision on lim itself
            "E_limit_positive": bool(sp.Integer(5) > sp.Rational(9, 4)) and bool(sp.simplify(lim).is_positive),
            "rows": rows, "pi_normality": "OPEN"}


if __name__ == "__main__":
    out = receipt()
    json.dump(out, sys.stdout, indent=1)
    print()
    ok = out["E_limit_matches_closed_form"] and all(r["K_max_le_3"] and r["K_max_equals_3_minus_3_over_A"] for r in out["rows"])
    sys.exit(0 if ok else 1)
