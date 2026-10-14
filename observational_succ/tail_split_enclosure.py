"""Tail-split enclosure: separate the exactly-known synchronized cells.

The periodic enclosure (PTE-01) bounded the whole L2(w) tail by the global
min/max defect over one period.  But the residue r = L is KNOWN EXACTLY:
F(L) = sum_n a_n (L mod n)/n = 0, so the defect at every synchronized cell
k = jL is exactly |1 - 0|^2 = 1.  Pulling those cells out of the min/max
average and adding their exact contribution gives a strictly sharper
two-sided enclosure.

Let c_r = |1 - F(r)|^2 (exact rationals, r = 1..L), with c_L = 1 exactly, and
let m' = min_{r<L} c_r,  M' = max_{r<L} c_r.  Let

    B = sum_{j: jL > K} 1/(jL(jL+1))          (exact blackout tail)

Then the global squared error E satisfies

    P_K + B + m' * (1/(K+1) - B)  <=  E  <=  P_K + B + M' * (1/(K+1) - B)

because the non-blackout cells carry total weight 1/(K+1) - B and defect in
[m', M'], while the blackout cells contribute exactly B.  The LOWER bound is strictly sharper than PTE-01 for every nonempty family
(the blackout cells' exact contribution is added on top of the min-defect
average).  The UPPER bound is strictly sharper whenever M' != 1 (i.e. the
non-blackout max defect differs from the blackout defect 1), and is dramatic
when the synchronized cells dominate (the LCM-blackout regime); when M' = 1
exactly it coincides with PTE-01, and the truncation remainder 1/(J L^2) can
epsilon-offset a vanishingly small gain -- it tends to 0 as J grows.

Exact rational arithmetic; the blackout tail is certified by truncating at J
with remainder bound  sum_{j>J} 1/(jL(jL+1)) < 1/(J L^2).  No floats, no
zeta zero, no Gamma/pole.  Finite certificate only; not a global L2 bound.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import lcm

from .periodic_tail_enclosure import prefix_sum, residue, value, PeriodicTailError


def defect_by_residue(a: dict[int, Q]) -> tuple[dict[int, Q], int]:
    """{r: |1 - F(r)|^2 for r=1..L} and the period L.  c_L is exactly 1."""
    if not a:
        raise PeriodicTailError("nonempty coefficient family required")
    for n, c in a.items():
        if type(c) not in (int, Q):
            raise PeriodicTailError("only exact rational coefficients")
    L = lcm(*a.keys())
    c = {r: (Q(1) - value(r, a)) ** 2 for r in range(1, L + 1)}
    # structural check: F(L) = 0, so c_L = 1 exactly
    if c[L] != 1:
        raise ArithmeticError("blackout defect must be exactly 1 (F(L)=0)")
    return c, L


def blackout_tail_interval(K: int, L: int, J: int | None = None) -> tuple[Q, Q]:
    """Certified [B_low, B_high] for B = sum_{j: jL>K} 1/(jL(jL+1)).

    B_low = sum_{j=j0..J} 1/(jL(jL+1))  (exact truncation),
    B_high = B_low + 1/(J L^2)          (remainder bound, telescoping).
    """
    K = int(K); L = int(L)
    if not (1 <= K <= 100_000 and 2 <= L <= 100_000_000):
        raise PeriodicTailError("K,L out of declared range")
    j0 = K // L + 1                       # smallest j with jL > K
    J = (j0 + 4096) if J is None else int(J)
    if J < j0:
        raise PeriodicTailError("truncation J must be >= j0")
    B_low = sum((Q(1, j * L * (j * L + 1)) for j in range(j0, J + 1)), Q())
    B_high = B_low + Q(1, J * L * L)
    return B_low, B_high


def tail_split_enclosure(a: dict[int, Q], K: int = 128, J: int | None = None) -> tuple[Q, Q]:
    """Strictly-sharpened [lower, upper] for the global squared L2(w) error.

    Returns (P_K + B_low + m'*(1/(K+1)-B_high),
             P_K + B_high + M'*(1/(K+1)-B_low))  in exact rationals.
    """
    K = int(K)
    if not 1 <= K <= 100_000:
        raise PeriodicTailError("K out of declared range")
    P = prefix_sum(a, K)
    c, L = defect_by_residue(a)
    m_ = min(c[r] for r in range(1, L))    # min over NON-blackout residues
    M_ = max(c[r] for r in range(1, L))    # max over NON-blackout residues
    B_low, B_high = blackout_tail_interval(K, L, J)
    w_hi = Q(1, K + 1) - B_high            # upper bound on non-blackout weight
    w_lo = Q(1, K + 1) - B_low             # lower bound on non-blackout weight
    if w_hi <= 0:
        raise PeriodicTailError("increase J so B_high < 1/(K+1)")
    lower = P + B_low + m_ * w_hi
    upper = P + B_high + M_ * w_lo
    return lower, upper
