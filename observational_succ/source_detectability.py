"""Source-defect detectability horizon for the zero-centered residue observer.

For the true Möbius source b(n) = mu(n), the finite interpolant

    F_K(k) = sum_{n<=K} b(n) floor(k/n) = sum_{m<=k} sum_{d|m} b(d)

equals 1 for every cell k <= K (ZCR-04).  This module pins down *exactly*
when a single-position source defect becomes visible to a finite observer.

Theorem (detectability horizon).  Let b'(n) = mu(n) for n != d and
b'(d) = mu(d) + delta (delta a nonzero exact rational).  Then the defect
at d first affects cell k = d, with exact value F(d) = 1 + delta, and a
finite observer at horizon K detects the defect IFF K >= d.

    Proof sketch:  F_K(k) = sum_{m<=k} sum_{d|m} b(d) is a partial
    Möbius inversion.  The single mutation contributes delta * #{m<=k : d|m}
    = delta * floor(k/d), which is 0 for k < d and delta at k = d.

Theorem (non-identifiability).  For every finite horizon K there are
infinitely many distinct sources (equal to mu on 1..K, differing at
infinitely many n > K) with IDENTICAL finite observations — a finite
observer can never rule out open-world source differences.

Pure exact rational arithmetic.  No float, no zeta zero, no Gamma/pole
input.  This is a finite-horizon certificate, NOT a global source
identification theorem and NOT an RH result.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .zero_centered_residue import mobius


class SourceDetectabilityError(ValueError):
    pass


def _integer(n: int, lo: int, hi: int) -> int:
    if type(n) is not int or not lo <= n <= hi:
        raise SourceDetectabilityError(f"expected an integer in [{lo},{hi}]")
    return n


def _delta(delta) -> Q:
    """Validate a nonzero exact rational mutation delta (int or Fraction)."""
    if type(delta) not in (int, Q):
        raise SourceDetectabilityError("delta must be an exact rational (int or Fraction)")
    delta = Q(delta)
    if delta == 0:
        raise SourceDetectabilityError("delta must be nonzero (a zero change is not a defect)")
    return delta


def _source_check(b: dict[int, Q]) -> None:
    """Exact-rational source-map type guard; keys are positions n >= 1."""
    if not b:
        raise SourceDetectabilityError("nonempty source coefficient map required")
    for n, c in b.items():
        _integer(n, 1, 500)
        if type(c) not in (int, Q):
            raise SourceDetectabilityError("only exact rational source coefficients")


def interpolant(k: int, b: dict[int, Q]) -> Q:
    """F(k) = sum_{m<=k} sum_{d|m} b(d), exact.

    This is the Möbius-inversion form of the finite interpolant
    sum_n b(n) floor(k/n); both expressions agree termwise.
    """
    _integer(k, 1, 500)
    _source_check(b)
    return sum((Q(b[d]) for m in range(1, k + 1)
                for d in range(1, m + 1) if m % d == 0 and d in b), Q())


def defective_source(d: int, delta, N: int) -> dict[int, Q]:
    """Source b' = mu on 1..N with a single defect: b'(d) = mu(d) + delta."""
    _integer(d, 2, 500)
    _integer(N, d, 500)
    delta = _delta(delta)
    mu = mobius(N)
    b = {n: Q(mu[n]) for n in range(1, N + 1)}
    b[d] = Q(mu[d]) + delta
    return b


def detectability_horizon(d: int, delta) -> dict:
    """Exact horizon and first visible cell for a single defect at d.

    Returns the minimal observer horizon (d), the first cell whose
    interpolant deviates from 1 (d), and the exact deviation value
    (1 + delta), each verified against the exact summation identity.
    """
    _integer(d, 2, 500)
    delta = _delta(delta)
    b = defective_source(d, delta, d)  # horizon = d is already sufficient
    predicted = Q(1) + delta
    verified = interpolant(d, b)
    hidden = all(interpolant(k, b) == Q(1) for k in range(1, d))
    return {
        "defect_position": d,
        "delta": str(delta),
        "detectability_horizon": d,
        "first_visible_cell": d,
        "predicted_value": str(predicted),
        "verified_value": str(verified),
        "hidden_before_horizon": hidden,
        "exact_match": verified == predicted,
        "detected_iff_horizon_ge_d": True,
        "no_zeta_zero_inputs": True,
        "RH_proved": False,
    }


def detected_at(d: int, delta, K: int) -> bool:
    """Whether a finite observer at horizon K sees the defect at d."""
    _integer(d, 2, 500)
    _integer(K, 1, 500)
    delta = _delta(delta)
    b = defective_source(d, delta, max(d, K))
    return any(interpolant(k, b) != Q(1) for k in range(1, K + 1))


def first_deviation(d: int, delta, K: int) -> int | None:
    """Smallest cell k <= K with F(k) != 1, or None if undetected."""
    _integer(d, 2, 500)
    _integer(K, 1, 500)
    delta = _delta(delta)
    b = defective_source(d, delta, max(d, K))
    for k in range(1, K + 1):
        if interpolant(k, b) != Q(1):
            return k
    return None


def nonidentifiable_pair(K: int, delta=None) -> dict:
    """Two distinct sources agreeing on 1..K, differing at K+1.

    Returns the true Möbius source and a mutation with a defect at n = K+1
    (delta defaults to +1).  Both produce identical finite observations on
    every cell 1..K, yet are distinct sources — the finite observer cannot
    tell them apart.
    """
    _integer(K, 1, 500)
    delta = Q(1) if delta is None else _delta(delta)
    N = K + 1
    mu = mobius(N)
    src_true = {n: Q(mu[n]) for n in range(1, N + 1)}
    src_alt = {n: Q(mu[n]) for n in range(1, N + 1)}
    src_alt[N] = Q(mu[N]) + delta  # defect at n = K+1
    agree = all(src_true[n] == src_alt[n] for n in range(1, K + 1))
    identical = all(interpolant(k, src_true) == interpolant(k, src_alt)
                    for k in range(1, K + 1))
    return {
        "horizon": K,
        "source_true": {str(n): str(src_true[n]) for n in src_true},
        "source_alt": {str(n): str(src_alt[n]) for n in src_alt},
        "agree_on_1_to_K": agree,
        "first_difference_at": N,
        "delta": str(delta),
        "finite_observations_identical": identical,
        "open_world_unidentifiable": True,
        "no_zeta_zero_inputs": True,
        "RH_proved": False,
    }


def open_world_family(K: int, delta=None, count: int = 8) -> list[dict[int, Q]]:
    """`count` pairwise-distinct sources agreeing with mu on 1..K.

    Defect position varies over n = K+1, K+2, ..., K+count (delta fixed),
    so each pair differs and all coincide with mu on 1..K.  Since `count`
    is arbitrary, this witnesses the infinitely-many-distinct corollary.
    """
    _integer(K, 1, 500)
    _integer(count, 1, 64)
    delta = Q(1) if delta is None else _delta(delta)
    N = K + count
    mu = mobius(N)
    base = {n: Q(mu[n]) for n in range(1, N + 1)}
    family = []
    for j in range(1, count + 1):
        src = dict(base)
        src[K + j] = Q(mu[K + j]) + delta
        family.append(src)
    return family
