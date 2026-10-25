"""Exact twisted-observer readouts and stable circle-residual probes.

The BBP source lives in odd rational torsion. Doubling is injective there,
but its inverse has no uniform circle-metric bound. Coprime gains 2 and 3
repair that instability with the sharp squared-norm constant 4/3.

All finite certificates use integers, Fractions, or pairs of Fractions for
Gaussian rationals. No floating-point phase or pi digits enter a certificate.
These observational identities do not assert any asymptotic BBP cancellation.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import gcd

from .bbp_prime_window_projection import window_parameters

Gaussian = tuple[Q, Q]
ZERO: Gaussian = (Q(0), Q(0))
ONE: Gaussian = (Q(1), Q(0))


def _integer(value: int, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("strict integer in the stated domain required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _gaussian(value: Gaussian, *, unit: bool = False) -> Gaussian:
    if type(value) is not tuple or len(value) != 2:
        raise ValueError("Gaussian rational must be a length-two tuple")
    result = (_rational(value[0]), _rational(value[1]))
    if unit and _norm2(result) != 1:
        raise ValueError("unit Gaussian rational required")
    return result


def _add(first: Gaussian, second: Gaussian) -> Gaussian:
    return (first[0] + second[0], first[1] + second[1])


def _sub(first: Gaussian, second: Gaussian) -> Gaussian:
    return (first[0] - second[0], first[1] - second[1])


def _mul(first: Gaussian, second: Gaussian) -> Gaussian:
    return (first[0] * second[0] - first[1] * second[1],
            first[0] * second[1] + first[1] * second[0])


def _conjugate(value: Gaussian) -> Gaussian:
    return (value[0], -value[1])


def _norm2(value: Gaussian) -> Q:
    return value[0] ** 2 + value[1] ** 2


def _mean(values: tuple[Gaussian, ...]) -> Gaussian:
    size = len(values)
    return (sum((z[0] for z in values), Q()) / size,
            sum((z[1] for z in values), Q()) / size)


def circle_distance(value: int | Q) -> Q:
    """Exact distance to zero in R/Z; floats and booleans are rejected."""
    residue = _rational(value) % 1
    return min(residue, 1 - residue)


def two_branch_distance(value: int | Q) -> Q:
    """Distance to {0,1/2}, exactly half the doubled phase distance."""
    phase = _rational(value)
    return min(circle_distance(phase), circle_distance(phase - Q(1, 2)))


def bbp_odd_forcing(n: int) -> Q:
    """Authentic four-pole forcing regrouped over odd denominators.

    The two even-denominator terms combine to
    -(3n-1)/((2n-1)(4n-1)); no source term has been omitted.
    """
    _integer(n, 1)
    return (Q(4, 8 * n - 7) - Q(1, 8 * n - 3)
            - Q(3 * n - 1, (2 * n - 1) * (4 * n - 1)))


def bbp_odd_states(last_index: int) -> tuple[Q, ...]:
    """Authentic states y0,...,y_last_index, including initial zero."""
    _integer(last_index, 0)
    states = [Q()]
    for n in range(1, last_index + 1):
        state = (16 * states[-1] + bbp_odd_forcing(n)) % 1
        if state.denominator % 2 == 0:
            raise AssertionError("odd-denominator source invariant failed")
        states.append(state)
    return tuple(states)


def authentic_odd_complement_window(p: int) -> tuple[Q, ...]:
    """BBP first-birth complement from an independent odd-form recurrence.

    The inherited prime/order validator authenticates p=8m+1. The states
    themselves use the regrouped forcing above, not an existing window cache.
    """
    m, _, length, _ = window_parameters(p)
    states = bbp_odd_states(4 * m)
    result = tuple((states[m + 1 + t] - Q(4 * pow(16, t, p), p)) % 1
                   for t in range(length))
    if any(w.denominator % 2 == 0 or gcd(w.denominator, p) != 1
           for w in result):
        raise AssertionError("source complement lost its arithmetic type")
    return result


def doubling_inverse_certificate(value: int | Q,
                                 modulus: int | None = None) -> dict:
    """Sharp finite inverse bound ||w|| <= (q-1)/2 * ||2w||.

    q must be odd and annihilate w; it need not be the reduced denominator.
    This finite q-dependent bound is NOT a uniform inverse on odd torsion.
    """
    phase = _rational(value) % 1
    q = phase.denominator if modulus is None else _integer(modulus, 1)
    if q % 2 == 0 or (q * phase).denominator != 1:
        raise ValueError("odd modulus annihilating the phase required")
    residual = circle_distance(phase)
    doubled = circle_distance(2 * phase)
    constant = Q(q - 1, 2)
    upper = constant * doubled
    branch = two_branch_distance(phase)
    if residual > upper or 2 * branch != doubled:
        raise AssertionError("doubling certificate identity failed")
    return {"phase": phase, "modulus": q, "residual_distance": residual,
            "doubled_distance": doubled, "nearest_branch_distance": branch,
            "inverse_constant": constant, "residual_upper": upper,
            "exact_agreement": doubled == 0, "exact_zero": residual == 0}


def odd_doubling_instability(q: int) -> dict:
    """Sharp odd-torsion witness w=(q-1)/(2q), q>=3 odd."""
    _integer(q, 3)
    if q % 2 == 0:
        raise ValueError("odd q required")
    return doubling_inverse_certificate(Q(q - 1, 2 * q), q)


def _extended_gcd(first: int, second: int) -> tuple[int, int, int]:
    """Nonnegative gcd and Bezout coefficients for nonnegative inputs."""
    old_r, r = first, second
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def gain_observability(gains: tuple[int, ...] | list[int]) -> dict:
    """Exact/stable classification and a Bezout coercivity certificate.

    For d=gcd(gains), circle injectivity and stable recovery hold iff d=1.
    Odd-torsion injectivity alone holds iff d is a power of two. When d=1,
    returned coefficients a obey sum a_k*k=1 and the valid squared-norm
    constant sum a_k^2 follows by telescoping and Cauchy--Schwarz. It need
    not be the optimal constant; gain23_certificate supplies the sharp 4/3.
    """
    if type(gains) not in (tuple, list) or not gains:
        raise ValueError("nonempty tuple or list of integer gains required")
    data = tuple(_integer(k) for k in gains)
    if not any(data):
        raise ValueError("at least one nonzero gain required")
    divisor = 0
    coefficients: list[int] = []
    for k in data:
        new_gcd, left, right = _extended_gcd(divisor, abs(k))
        coefficients = [left * a for a in coefficients]
        coefficients.append(right if k >= 0 else -right)
        divisor = new_gcd
    if sum(a * k for a, k in zip(coefficients, data)) != divisor:
        raise AssertionError("Bezout certificate failed")
    stable = divisor == 1
    return {"gains": data, "gcd": divisor,
            "circle_injective": stable,
            "odd_torsion_injective": divisor & (divisor - 1) == 0,
            "uniformly_stable": stable,
            "bezout_coefficients": tuple(coefficients),
            "bezout_norm_constant":
                Q(sum(a * a for a in coefficients)) if stable else None}


def gain23_certificate(real_part: int | Q) -> dict:
    """Sharp coercivity certificate for any unit phase with given real part.

    No square root or trigonometric approximation is needed. With c=Re(v),
    |v^k-1|^2=2-2*T_k(c), and the quotient factor is
    4*(c+3/4)^2+3/4. c=-3/4 is an exact algebraic-unit sharpness witness.
    """
    c = _rational(real_part)
    if not -1 <= c <= 1:
        raise ValueError("unit-phase real part must lie in [-1,1]")
    residual = 2 - 2 * c
    gain2 = 2 - 2 * (2 * c * c - 1)
    gain3 = 2 - 2 * (4 * c * c * c - 3 * c)
    factor = 4 * (c + Q(3, 4)) ** 2 + Q(3, 4)
    upper = Q(4, 3) * (gain2 + gain3)
    if gain2 + gain3 != residual * factor or upper < residual:
        raise AssertionError("coprime-gain polynomial certificate failed")
    return {"real_part": c, "residual_squared": residual,
            "gain2_squared": gain2, "gain3_squared": gain3,
            "factor": factor, "factor_lower": Q(3, 4),
            "coercivity_constant": Q(4, 3), "residual_upper": upper,
            "slack": upper - residual}


def twisted_pair_gaussian(common: Gaussian, residual: Gaussian) -> dict:
    """Exact unit Gaussian pair A=UV, B=U*conj(V) and swap invariants.

    AB=U^2, A*conj(B)=V^2. Small A-B controls proximity of V to +/-1;
    it does not select the plus branch. Inputs must have exact unit norm.
    """
    u = _gaussian(common, unit=True)
    v = _gaussian(residual, unit=True)
    plus = _mul(u, v)
    minus = _mul(u, _conjugate(v))
    common_product = _mul(plus, minus)
    differential_product = _mul(plus, _conjugate(minus))
    if common_product != _mul(u, u) or differential_product != _mul(v, v):
        raise AssertionError("twisted readout algebra failed")
    return {"plus": plus, "minus": minus,
            "common_product": common_product,
            "differential_product": differential_product,
            "agreement_squared": _norm2(_sub(plus, minus)),
            "residual_squared": _norm2(_sub(v, ONE)),
            "pair_sum": _add(plus, minus),
            "pair_difference": _sub(plus, minus)}


def signed_projection_certificate(left: tuple[Gaussian, ...] | list[Gaussian],
                                  right: tuple[Gaussian, ...] | list[Gaussian],
                                  period: int) -> dict:
    """Exact bilinear low/high split under time-residue averaging.

    The target is mean(left_t*right_t), without a conjugation. Low/high
    cross terms vanish because the averaging kernel is real symmetric.
    The high term can have arbitrary signed phase; agreement does not
    force its decay. Its squared modulus obeys the standard variance bound.
    """
    if type(left) not in (tuple, list) or type(right) not in (tuple, list):
        raise ValueError("Gaussian sequences must be tuples or lists")
    if not left or len(left) != len(right):
        raise ValueError("nonempty sequences of equal length required")
    a = tuple(_gaussian(z) for z in left)
    b = tuple(_gaussian(z) for z in right)
    n = len(a)
    d = _integer(period, 1)
    if n % d:
        raise ValueError("period must divide sample length")
    a_means = tuple(_mean(a[r::d]) for r in range(d))
    b_means = tuple(_mean(b[r::d]) for r in range(d))
    a_low = tuple(a_means[t % d] for t in range(n))
    b_low = tuple(b_means[t % d] for t in range(n))
    a_high = tuple(_sub(x, y) for x, y in zip(a, a_low))
    b_high = tuple(_sub(x, y) for x, y in zip(b, b_low))
    total = _mean(tuple(_mul(x, y) for x, y in zip(a, b)))
    low = _mean(tuple(_mul(x, y) for x, y in zip(a_low, b_low)))
    high = _mean(tuple(_mul(x, y) for x, y in zip(a_high, b_high)))
    low_high = _mean(tuple(_mul(x, y) for x, y in zip(a_low, b_high)))
    high_low = _mean(tuple(_mul(x, y) for x, y in zip(a_high, b_low)))
    variance_a = sum((_norm2(x) for x in a_high), Q()) / n
    variance_b = sum((_norm2(x) for x in b_high), Q()) / n
    if (total != _add(low, high) or low_high != ZERO or high_low != ZERO
            or _norm2(high) > variance_a * variance_b):
        raise AssertionError("signed projection certificate failed")
    return {"total": total, "low": low, "high": high,
            "low_high": low_high, "high_low": high_low,
            "left_variance": variance_a, "right_variance": variance_b,
            "high_squared": _norm2(high),
            "high_squared_upper": variance_a * variance_b,
            "left_projected": a_low, "right_projected": b_low}
