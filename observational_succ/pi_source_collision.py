"""Exact BBP source collision probes; no asymptotic normality certificate.

Paper proofs and scope: research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md.
This self-contained module avoids the incompatible bbp_minimal_path APIs on
the separately audited PR #260/#261 branches. All source values and decisions
are integers/Fractions; no supplied pi digits or floating thresholds are used.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt
from typing import Sequence


def _integer(value: int, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"an integer >= {minimum} is required")
    return value


def _rational(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _prime(p: int) -> int:
    _integer(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("prime required")
    return p


def bbp_forcing(n: int) -> Q:
    """Authentic four-pole forcing, with n starting at 1."""
    _integer(n)
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def bbp_states(last: int) -> tuple[Q, ...]:
    """Return y_0,...,y_last, y_0=0, y_n={16 y_(n-1)+r(n)}."""
    _integer(last, 0)
    result = [Q(0)]
    for n in range(1, last + 1):
        result.append((16*result[-1]+bbp_forcing(n)) % 1)
    return tuple(result)


def tail_upper(n: int) -> Q:
    """Paper bound 0<t_n<1/((8n+1)(8n+2)); not an estimate from data."""
    _integer(n, 0)
    return Q(1, (8*n+1)*(8*n+2))


def order16(p: int) -> int:
    _prime(p)
    if p == 2:
        raise ValueError("16 must be invertible modulo p")
    u = 16 % p
    length = 1
    while u != 1:
        u = 16*u % p
        length += 1
    return length


@dataclass(frozen=True)
class BBPPrimeWindow:
    prime: int
    start: int  # true pi orbit indices start,...,4*start-1
    period: int
    states: tuple[Q, ...]  # y_(start+1+t)
    local: tuple[Q, ...]
    complement: tuple[Q, ...]

    @property
    def length(self) -> int:
        return len(self.states)

    @property
    def tail_bound(self) -> Q:
        return tail_upper(self.start + 1)

    def conjugate(self, a: int) -> tuple[Q, ...]:
        _integer(a)
        if a >= self.prime:
            raise ValueError("nonzero residue 1 <= a < p required")
        return tuple((a*u+w) % 1 for u, w in zip(self.local, self.complement))


def prime_window(p: int) -> BBPPrimeWindow:
    """The authentic first p-birth window for primes p=1 mod 8."""
    _prime(p)
    if p % 8 != 1:
        raise ValueError("first-window contract requires p = 1 mod 8")
    m = (p-1)//8
    period = order16(p)
    if m % period:
        raise ArithmeticError("quadratic-residue order contract violated")
    source = bbp_states(4*m)
    values = source[m+1:4*m+1]
    local = tuple(Q(4*pow(16, t, p) % p, p) for t in range(3*m))
    complement = tuple((v-u) % 1 for v, u in zip(values, local))
    if any(w.denominator % p == 0 for w in complement):
        raise ArithmeticError("p-free complementary phase was lost")
    result = BBPPrimeWindow(p, m, period, values, local, complement)
    if result.conjugate(1) != values:
        raise ArithmeticError("selected-source reconstruction failed")
    return result


def cell_counts(phases: Sequence[Q | int], cells: int) -> dict[int, int]:
    _integer(cells)
    if not phases:
        raise ValueError("nonempty finite sample required")
    return dict(Counter(int((_rational(x) % 1)*cells) for x in phases))


def cell_collision(phases: Sequence[Q | int], cells: int) -> Q:
    """M sum_a p_a^2, including self-pairs; a finite diagnostic only."""
    counts = cell_counts(phases, cells)
    return Q(cells*sum(c*c for c in counts.values()), len(phases)**2)


def small_ball_pairs(phases: Sequence[Q | int], radius: Q) -> int:
    """Ordered circular close pairs, diagonal included, exact O(n log n).

    The strict radius<1/2 domain prevents double-counting antipodal pairs.
    Duplicates and exact threshold equalities are retained.
    """
    radius = _rational(radius)
    if not 0 <= radius < Q(1, 2):
        raise ValueError("requires 0 <= exact radius < 1/2")
    if not phases:
        raise ValueError("nonempty finite sample required")
    points = sorted(_rational(x) % 1 for x in phases)
    n = len(points)
    doubled = points + [x+1 for x in points]
    j = 1
    forward = 0
    for i in range(n):
        j = max(j, i+1)
        while j < i+n and doubled[j]-doubled[i] <= radius:
            j += 1
        forward += j-i-1
    return n+2*forward


def galois_collision_bounds(p: int, radius: Q) -> tuple[Q, Q]:
    """Complement-uniform bounds on mean normalized close-pair count.

    Requires the complete 3m first-window sample, not a truncated period.
    The bounds are a proved finite theorem; they do not select a=1.
    """
    _prime(p)
    if p % 8 != 1:
        raise ValueError("requires p = 1 mod 8")
    radius = _rational(radius)
    if not 0 <= radius < Q(1, 2):
        raise ValueError("requires 0 <= exact radius < 1/2")
    period = order16(p)
    k = (2*p*radius).__floor__()
    lower_grid = max(Q(0), Q(k-1, p-1))
    upper_grid = min(Q(1), Q(k+1, p-1))
    unequal = 1-Q(1, period)
    return unequal*lower_grid, Q(1, period)+unequal*upper_grid


def galois_collision_mean(window: BBPPrimeWindow, radius: Q) -> Q:
    total = sum(small_ball_pairs(window.conjugate(a), radius)
                for a in range(1, window.prime))
    return Q(total, (window.prime-1)*window.length**2)


def carry_collision_check(before: Sequence[Q], after: Sequence[Q], cells: int) -> dict:
    """Check the factor-two cell-energy transport on an exact finite pair.

    Hypothesis: each after phase is before plus a forward displacement in
    [0,1/M). This function validates that hypothesis; it never assumes it.
    """
    _integer(cells)
    if not before or len(before) != len(after):
        raise ValueError("equal nonempty sample lengths required")
    displacements = [(_rational(v)-_rational(u)) % 1
                     for u, v in zip(before, after)]
    if any(d >= Q(1, cells) for d in displacements):
        raise ValueError("forward source displacement exceeds one cell")
    c_before = cell_collision(before, cells)
    c_after = cell_collision(after, cells)
    return {"before": c_before, "after": c_after,
            "forward_bound": c_after <= 2*c_before,
            "reverse_bound": c_before <= 2*c_after}


def adversarial_complement(p: int, cells: int) -> tuple[Q, ...]:
    """p-free finite control aligning selected phases in one tiny arc.

    This changes the authentic complementary BBP source. It refutes only
    source-blind typicality claims, never the complete BBP contract.
    """
    _prime(p)
    _integer(cells, 3)
    if p % 8 != 1:
        raise ValueError("requires p = 1 mod 8")
    q = 2*cells*p+1  # coprime to p, larger than cell count
    length = 3*((p-1)//8)
    result = []
    for t in range(length):
        u = Q(4*pow(16, t, p) % p, p)
        # Ceiling picks z_t(1) in [0,1/q), even through circle wrap.
        target = (-u) % 1
        ceil_num = -((-target*q).__floor__())
        result.append(Q(ceil_num, q) % 1)
    return tuple(result)
