"""Exact binary refinement of the authentic centered carry.

These instruments identify and count inverse branches.  They do not prove
that the BBP-selected branch frequencies are asymptotically uniform.
All decisions use exact rational arithmetic; no floating thresholds occur.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd
from typing import Mapping, Sequence


def _rational(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("an exact integer or Fraction is required")
    return Q(value)


def _integer(value: int, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"an integer >= {minimum} is required")
    return value


def centered(value: Q | int) -> Q:
    """The representative in [-1/2, 1/2); the half-turn is negative."""
    value = _rational(value)
    return value - (value + Q(1, 2)).__floor__()


def rational_residue(value: Q | int, modulus: int) -> int:
    """Reduction of a rational whose denominator is a unit modulo modulus."""
    value = _rational(value)
    _integer(modulus, 2)
    if gcd(value.denominator, modulus) != 1:
        raise ValueError("the rational denominator must be a modular unit")
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def centered_carry(
    current_difference: Q | int,
    forcing_difference: Q | int,
    successor_difference: Q | int,
    radix: int = 16,
) -> int:
    """Return the integer in radix*d + e = d_next + kappa.

    Both differences are centered again to give this function a unique
    convention.  Inconsistent inputs are rejected rather than rounded.
    """
    _integer(radix, 2)
    value = (radix * centered(current_difference)
             + _rational(forcing_difference)
             - centered(successor_difference))
    if value.denominator != 1:
        raise ValueError("the input differences do not obey the forced step")
    return value.numerator


@dataclass(frozen=True)
class BinaryBranchProfile:
    radix: int
    sample_count: int
    radius: Q
    forcing_span: Q
    signed_counts: tuple[tuple[int, int], ...]
    nested_counts: tuple[int, ...]

    @property
    def endpoint_pairs(self) -> int:
        return self.nested_counts[0]

    @property
    def zero_pairs(self) -> int:
        return self.nested_counts[-1]

    @property
    def conditional_retentions(self) -> tuple[Q, ...]:
        # Every nested set contains all self-pairs, so its size is positive.
        return tuple(Q(b, a) for a, b in
                     zip(self.nested_counts, self.nested_counts[1:]))

    @property
    def retention(self) -> Q:
        return Q(self.zero_pairs, self.endpoint_pairs)

    def residue_counts(self, modulus: int) -> tuple[int, ...]:
        _integer(modulus, 2)
        result = [0] * modulus
        for carry, count in self.signed_counts:
            result[carry % modulus] += count
        return tuple(result)


def binary_branch_profile(
    current: Sequence[Q | int],
    forcing: Sequence[Q | int],
    radius: Q | int,
    *,
    radix: int = 16,
    successor: Sequence[Q | int] | None = None,
) -> BinaryBranchProfile:
    """Count nested 2-adic carry fibers in one exact forced transition.

    The radix must be a power of two.  The forcing span plus radius must be
    strictly less than 1/2, and radius is at most 1/4.  For endpoint-close
    pairs these hypotheses give |kappa| <= radix/2 and identify the central
    inverse branch with kappa=0.  The j-th nested count imposes 2**j | kappa.

    Runtime is quadratic in the sample count; this is a diagnostic oracle,
    not a proposed fast large-window algorithm.
    """
    _integer(radix, 2)
    if radix & (radix - 1):
        raise ValueError("the radix must be a power of two")
    radius = _rational(radius)
    if not Q(0) <= radius <= Q(1, 4):
        raise ValueError("radius must lie in [0, 1/4]")
    if not current or len(current) != len(forcing):
        raise ValueError("nonempty current and forcing arrays must align")
    xs = tuple(_rational(x) % 1 for x in current)
    fs = tuple(_rational(f) for f in forcing)
    span = max(fs) - min(fs)
    if span + radius >= Q(1, 2):
        raise ValueError("forcing span plus radius must be < 1/2")
    ys = tuple((radix*x+f) % 1 for x, f in zip(xs, fs))
    if successor is not None:
        if len(successor) != len(xs):
            raise ValueError("successor array must align")
        observed = tuple(_rational(y) % 1 for y in successor)
        if observed != ys:
            raise ValueError("successor samples do not obey the forcing")
    counts: Counter[int] = Counter()
    for s, x_s in enumerate(xs):
        for t, x_t in enumerate(xs):
            d_next = centered(ys[t] - ys[s])
            if abs(d_next) > radius:
                continue
            d = centered(x_t - x_s)
            carry = centered_carry(d, fs[t] - fs[s], d_next, radix)
            if abs(carry) > radix // 2:
                raise ArithmeticError("centered-carry support theorem failed")
            if (abs(d) <= Q(1, 2*radix)) != (carry == 0):
                raise ArithmeticError("central-branch identification failed")
            counts[carry] += 1
    levels = radix.bit_length() - 1
    nested = tuple(sum(count for carry, count in counts.items()
                       if carry % (1 << j) == 0)
                   for j in range(levels + 1))
    return BinaryBranchProfile(radix, len(xs), radius, span,
                               tuple(sorted(counts.items())), nested)


def residue_marginal(
    signed_law: Mapping[int, Q | int], modulus: int,
) -> tuple[Q, ...]:
    """Project a finite signed measure on integer carries to a residue ring."""
    _integer(modulus, 2)
    result = [Q(0)] * modulus
    for carry, weight in signed_law.items():
        if type(carry) is not int:
            raise ValueError("carry labels must be integers")
        result[carry % modulus] += _rational(weight)
    return tuple(result)


def reconstruct_carry_law_mod_11_13(
    modulo_11: Sequence[Q | int], modulo_13: Sequence[Q | int],
) -> tuple[Q, ...]:
    """Recover a nonnegative law/count table on carries -8,...,8.

    Separate marginals suffice because the support is known and bounded.
    Returned entries are ordered -8,...,8.  Inconsistent or negative
    reconstructed tables are rejected.  Total mass need not equal one.
    The inverse has sharp sup-norm constant 3 when the two input errors
    share a common sup-norm budget; this does not assert uniformity.
    """
    if len(modulo_11) != 11 or len(modulo_13) != 13:
        raise ValueError("the residue arrays must have lengths 11 and 13")
    a = tuple(_rational(x) for x in modulo_11)
    b = tuple(_rational(x) for x in modulo_13)
    c = {k: b[k % 13] for k in range(-4, 5)}
    c[-8], c[-7] = a[3]-c[3], a[4]-c[4]
    c[7], c[8] = a[7]-c[-4], a[8]-c[-3]
    c[5], c[6] = b[5]-c[-8], b[6]-c[-7]
    c[-6], c[-5] = b[7]-c[7], b[8]-c[8]
    if (min(c.values()) < 0
            or residue_marginal(c, 11) != a
            or residue_marginal(c, 13) != b):
        raise ValueError("marginals have no nonnegative carry law on [-8,8]")
    return tuple(c[k] for k in range(-8, 9))


def conditional_zero_upper(
    endpoint_pairs: int,
    retentions: Sequence[Q | int],
    allowances: Sequence[Q | int],
    sample_count: int,
) -> Q:
    """Compose inequalities S_j <= theta_j*S_(j-1) + C_j*n.

    This computes only the conditional algebraic implication.  It does not
    assert that the supplied inequalities hold on the actual BBP source.
    """
    _integer(endpoint_pairs, 0)
    _integer(sample_count)
    if not retentions or len(retentions) != len(allowances):
        raise ValueError("nonempty retention and allowance arrays must align")
    result = Q(endpoint_pairs)
    for theta, allowance in zip(retentions, allowances):
        theta, allowance = _rational(theta), _rational(allowance)
        if not 0 <= theta <= 1 or allowance < 0:
            raise ValueError("retentions lie in [0,1]; allowances are >= 0")
        result = theta*result + allowance*sample_count
    return result
