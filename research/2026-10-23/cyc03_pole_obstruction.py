"""CORE DERIVATION: what does a nonzero weighted pole invariant obstruct?

Setting. Base b=16. A forcing r: N -> Q. Define the tail
    t_n = sum_{k>=1} b^{-k} r(n+k)          (n >= 0)
and the BBP tail identity
    b t_n = r(n+1) + t_{n+1}.                                 (T)
The cocycle: y_0 = 0, y_{n+1} = b y_n + r(n+1), and y_n + t_n = b^n t_0.

Question 1. When is r a COBOUNDARY, i.e. r(z) = b q(z-1) - q(z) for some q?
If it is, then telescopes: sum_{k=1}^{K} b^{-k} r(n+k)
    = sum b^{-k}[b q(n+k-1) - q(n+k)]
    = q(n) - b^{-K} q(n+K),
so t_n = q(n) exactly (if q bounded along the orbit). Then the cocycle is a
pure coboundary and the orbit is CONJUGATE to rotation by t_0 (no drift).

Question 2. If r is NOT a RATIONAL-FUNCTION coboundary, does t_n decay
slowly? NO general rate follows: the companion bbp_source_memory.py constructs
positive rational r_K(n)=K!/[n...(n+K)] of arbitrary polynomial decay
whose weighted pole invariant is (1-b)^K != 0. The former toy
r(n)=b^(-n) is ITSELF a coboundary with q(n)=b^(-n)/(b^2-1), though
q is not rational in the index n. It must not be used as an unrestricted
non-coboundary witness.

So the honest statement: the invariant obstructs the EXISTENCE OF A FINITE
RATIONAL COBOUNDARY, and hence obstructs the clean telescoping proof of
cancellation. It does NOT obstruct cancellation itself.

This module makes that precise, with exact arithmetic, and then asks the
question that actually matters: for the ACTUAL BBP r, does t_n decay, and how
does the four-pole structure control the rate?
"""
from __future__ import annotations

from fractions import Fraction as F


def forcing(m: int) -> F:
    """The BBP forcing r(m) = 4/(8m-7) - 2/(8m-4) - 1/(8m-3) - 1/(8m-2)."""
    if type(m) is not int or m < 1:
        raise ValueError("m >= 1 integer")
    return F(4, 8*m-7) - F(2, 8*m-4) - F(1, 8*m-3) - F(1, 8*m-2)


def pole_form(m: int) -> F:
    """Same r written as the collapsed pole rational function P(m)/D(m),
    P = 120m^2 - 89m + 16, D = (2m-1)(4m-1)(8m-7)(8m-3)."""
    if type(m) is not int or m < 1:
        raise ValueError("m >= 1 integer")
    P = 120*m*m - 89*m + 16
    D = (2*m-1)*(4*m-1)*(8*m-7)*(8*m-3)
    return F(P, D)


def tail_partial(n: int, K: int, b: int = 16) -> F:
    """Partial tail sum_{k=1}^{K} b^{-k} r(n+k), exact."""
    return sum((F(1, b**k) * forcing(n+k) for k in range(1, K+1)), F(0))


def tail_enclosure(n: int, K: int, b: int = 16) -> tuple[F, F]:
    """Rigorous enclosure of t_n using the source-sensitive remainder
    0 < t_n - partial < b^{-K} r(n+K+1)/15.  (Proven in the repo dossier.)"""
    lo = tail_partial(n, K, b)
    if type(b) is not int or b < 2:
        raise ValueError("base >= 2")
    hi = lo + F(1, b**K) * forcing(n+K+1) / F(b-1)
    return lo, hi


def is_coboundary_check_witness() -> dict:
    """The exact witness that r is NOT a coboundary in the rational 1-pole class.

    For a 1-pole-per-residue forcing, the weighted invariant at residue a is
    sum_j b^{-j} c_j and r = b q(z-1) - q(z) forces every such invariant to 0.
    The BBP poles have invariants (-1/8, -1/8, -1/4, +1/2): all nonzero.
    """
    poles = {F(7, 8): F(1, 2), F(1, 2): F(-1, 4),
             F(3, 8): F(-1, 8), F(1, 4): F(-1, 8)}
    return {"invariants": dict(poles),
            "all_nonzero": all(v != 0 for v in poles.values()),
            "sum": sum(poles.values())}


def geometric_non_coboundary() -> dict:
    """A non-coboundary whose tail nonetheless decays geometrically.

    Legacy function name retained for compatibility. r(n)=b^(-n)
    IS an exact sequence coboundary with q(n)=b^(-n)/(b^2-1):
    b*q(n-1)-q(n)=b^(-n).
    q is exponential, not a rational FUNCTION OF n.
    Thus this is only a rational-function-class restriction example.
    The genuine rational forcing countermodel is in bbp_source_memory.py.
    """
    b = F(16)
    # exact: t_n = sum b^{-k} b^{-(n+k)} = b^{-n} sum b^{-2k} = b^{-n}/(b^2-1)
    from fractions import Fraction
    val = Fraction(1, 1) / (b*b - 1) / (b**0)
    return {"r": "b^{-n}", "t_n": f"b^(-n)/(b^2-1) = {val} * b^(-n)",
            "exact_coboundary": "q(n)=b^(-n)/(b^2-1) and b*q(n-1)-q(n)=b^(-n)",
            "rational_function_in_n": False,
            "conclusion": "sequence coboundary; only excluded from the rational-function q class. The independent positive rational r_K(n) provides the genuine arbitrary-order decay control."}


def two_pole_toy(b: int = 16) -> dict:
    """The minimal honest toy: r(n) = c1/(n - p1)??  We use the CLEANEST exact
    2-pole model that mirrors BBP: r(n) = A/(q n - u) + B/(q n - v) with
    residues p1=u/q, p2=v/q.  Compute invariants and ask if zero invariants
    can be arranged with nonzero forcing."""
    # Toy: poles at a1=1/2, a2=1/4, coefficients c1, c2 in base b.
    # invariant1 = c1 (shift 0), invariant2 = c2.  For a coboundary need both 0.
    # So any nonzero 2-pole forcing with distinct residues is a non-coboundary.
    # But we can ASK: can a 2-pole non-coboundary have decaying tail? Yes:
    # take c1 = -c2 (equal magnitude), the leading 1/n^2 cancels partially...
    return {"statement": "any 2-pole forcing with distinct residues and nonzero "
                         "coefficients is a non-coboundary in the rational class",
            "note": "yet its tail may decay at ANY rate depending on how the "
                    "leading coefficients cancel -- the invariant is silent on rate"}


def leading_rate_after_cancellation() -> dict:
    """The real question: does the four-pole structure FORCE a specific rate?

    r(x) ~ 15/(64 x^2) + O(x^-3) for large x (proven constant 15/64).
    t_n = sum_{k>=1} b^{-k} r(n+k).
    If r(x) = A/x^2 + B/x^3 + ..., then
      t_n ~ A * sum b^{-k}/(n+k)^2 + ...
    and since sum b^{-k} = 1/(b-1) = 1/15, the leading term is A/(15 n^2) to
    first order in 1/n.  With A = 15/64 this gives 1/(64 n^2).  Consistent.
    The coefficients of the four forcing-index poles determine the collapsed
    polynomial P/D and its leading coefficient. In particular the first
    signed pole moment sum_i rho_i*a_i is exactly 15/64, so the tail
    coefficient is (sum rho_i*a_i)/(b-1). The poles are NOT circle states,
    and no dynamical "one-step annihilation" follows from their residues.
    """
    b, A = F(16), F(15, 64)
    lead = A / (b - 1)
    return {"leading_coefficient_of_t_n": str(lead),
            "check": "A/(b-1) = (15/64)/15 = 1/64  -- matches the proven rate",
            "finding": "the first signed forcing-index pole moment is 15/64 and "
                       "determines the leading tail coefficient 1/64"}


if __name__ == "__main__":
    print("=== witness: r is not a rational coboundary ===")
    w = is_coboundary_check_witness()
    for k, v in w["invariants"].items():
        print(f"  invariant at residue {k}: {v}")
    print("  all nonzero:", w["all_nonzero"], " sum:", w["sum"])
    print()
    print("=== corrected: geometric sequence IS a coboundary outside rational q ===")
    g = geometric_non_coboundary()
    for k, v in g.items():
        print(f"  {k}: {v}")
    print()
    print("=== the decisive structural finding ===")
    r = leading_rate_after_cancellation()
    for k, v in r.items():
        print(f"  {k}: {v}")
    print()
    print("=== enclosure of t_n for the true BBP forcing ===")
    for n in (0, 1, 2, 5, 10, 100):
        lo, hi = tail_enclosure(n, 60)
        print(f"  n={n:>3}: t_n in [{float(lo):.15e}, {float(hi):.15e}]  "
              f"1/(64(n+1)^2)={float(F(1,64*(n+1)**2)):.15e}")