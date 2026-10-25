"""Exact source-constraint interference on finite cyclic carriers.

A finite character average selects the unique recurrence history only after
the initial selector is supplied. Its observable transform retains that
selector explicitly. No time-average cancellation or pi normality is inferred.

The expanded Fourier laboratory is deliberately limited to small moduli and
bounded Cartesian sums. Authentic BBP rational-circle carriers can be much
larger: their projector is checked by exact modular constraints, and their
denominator refinements use inclusions, not profinite quotient reduction.
"""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import gcd, lcm

from .bbp_source_memory import forcing

MAX_FOURIER_MODULUS = 64
MAX_CARTESIAN_TERMS = 200_000


def _integer(value: int, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("strict integer in the stated domain required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _integers(values) -> tuple[int, ...]:
    if type(values) not in (tuple, list):
        raise ValueError("integer tuple or list required")
    return tuple(_integer(value) for value in values)


def _source(modulus, base, increments) -> tuple[int, int, tuple[int, ...]]:
    q = _integer(modulus, 2)
    b = _integer(base, 2)
    a = tuple(value % q for value in _integers(increments))
    return q, b, a


def _path(path, length, modulus) -> tuple[int, ...]:
    values = _integers(path)
    if len(values) != length:
        raise ValueError("candidate path has wrong horizon")
    return tuple(value % modulus for value in values)


def _selector(weights, modulus) -> tuple[Q, ...]:
    if type(weights) not in (tuple, list) or len(weights) != modulus:
        raise ValueError("one exact selector weight per initial state required")
    result = tuple(_rational(value) for value in weights)
    if sum(result, Q()) != 1:
        raise ValueError("selector weights must sum exactly to one")
    return result


def _small_modulus(modulus) -> int:
    q = _integer(modulus, 2)
    if q > MAX_FOURIER_MODULUS:
        raise ValueError("expanded Fourier certificate exceeds modulus budget")
    return q


def _trim(poly):
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def _monic_quotient(numerator, denominator):
    remainder = _trim(numerator)
    divisor = _trim(denominator)
    if divisor[-1] != 1:
        raise AssertionError("monic divisor required")
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and any(remainder):
        offset = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[offset] = coefficient
        for j, value in enumerate(divisor):
            remainder[offset + j] -= coefficient * value
        remainder = _trim(remainder)
    if any(remainder):
        raise AssertionError("cyclotomic polynomial division was inexact")
    return tuple(_trim(quotient))


@lru_cache(None)
def _cyclotomic_polynomial(q):
    polynomial = [-1] + [0] * (q - 1) + [1]
    for divisor in range(1, q):
        if q % divisor == 0:
            polynomial = _monic_quotient(polynomial,
                                         _cyclotomic_polynomial(divisor))
    return tuple(polynomial)


def cyclotomic_polynomial(modulus: int) -> tuple[int, ...]:
    """Phi_q in increasing powers, with validation before cached recursion."""
    return _cyclotomic_polynomial(_small_modulus(modulus))


def _reduce_coefficients(coefficients, q):
    polynomial = _cyclotomic_polynomial(q)
    remainder = _trim(coefficients)
    degree = len(polynomial) - 1
    while len(remainder) > degree:
        offset = len(remainder) - len(polynomial)
        coefficient = remainder[-1]
        for j, value in enumerate(polynomial):
            remainder[offset + j] -= coefficient * value
        remainder = _trim(remainder)
    return tuple(Q(remainder[j]) if j < len(remainder) else Q()
                 for j in range(degree))


def character_sum(modulus: int, exponents,
                  weights=None) -> tuple[Q, ...]:
    """Exact weighted root sum reduced modulo Phi_q; no complex floats."""
    q = _small_modulus(modulus)
    powers = _integers(exponents)
    if weights is None:
        coefficients = (Q(1),) * len(powers)
    else:
        if type(weights) not in (tuple, list) or len(weights) != len(powers):
            raise ValueError("one exact weight per exponent required")
        coefficients = tuple(_rational(value) for value in weights)
    raw = [Q()] * q
    for exponent, coefficient in zip(powers, coefficients):
        raw[exponent % q] += coefficient
    return _reduce_coefficients(raw, q)


@lru_cache(None)
def _character_delta(q, defect, phase_multiplier):
    raw = [Q()] * q
    for multiplier in range(q):
        raw[(phase_multiplier * multiplier * defect) % q] += Q(1, q)
    reduced = _reduce_coefficients(raw, q)
    if any(reduced[1:]) or reduced[0] not in (0, 1):
        raise AssertionError("normalized finite character sum was not 0/1")
    return tuple(raw), reduced, reduced[0]


def character_delta_certificate(modulus: int, defect: int,
                                phase_multiplier: int = 1) -> dict:
    """Expanded normalized character sum for one constraint.

    Nonunit phase_multiplier is intentionally allowed as a false-projector
    control. It enforces q | phase_multiplier*defect, a weaker constraint.
    """
    q = _small_modulus(modulus)
    d = _integer(defect) % q
    k = _integer(phase_multiplier) % q
    raw, reduced, value = _character_delta(q, d, k)
    return {"modulus": q, "defect": d, "phase_multiplier": k,
            "normalization": Q(1, q), "expanded_terms": q,
            "raw_normalized_coefficients": raw,
            "reduced_coefficients": reduced, "value": value,
            "authentic_constraint": d == 0,
            "phase_is_faithful": gcd(k, q) == 1}


def cyclic_path(modulus: int, base: int, increments,
                initial: int = 0) -> tuple[int, ...]:
    """The unique forward source history; base need not be invertible."""
    q, b, a = _source(modulus, base, increments)
    path = [_integer(initial) % q]
    for increment in a:
        path.append((b * path[-1] + increment) % q)
    return tuple(path)


def path_defects(modulus: int, base: int, increments, path,
                 initial: int | None = 0) -> tuple[int, ...]:
    """Initial and recurrence defects, or recurrence-only when initial=None."""
    q, b, a = _source(modulus, base, increments)
    x = _path(path, len(a) + 1, q)
    defects = [] if initial is None else [(x[0] - _integer(initial)) % q]
    defects.extend((x[j + 1] - b * x[j] - increment) % q
                   for j, increment in enumerate(a))
    return tuple(defects)


def projector_weight(modulus: int, base: int, increments, path,
                     initial: int | None = 0) -> Q:
    """Exact modular evaluation of the source projector at any modulus."""
    defects = path_defects(modulus, base, increments, path, initial)
    return Q(int(not any(defects)))


def interference_projector(modulus: int, base: int, increments, path,
                           initial: int | None = 0,
                           phase_multiplier: int = 1) -> dict:
    """Factorized expanded-character check, not a Cartesian dual expansion."""
    q = _small_modulus(modulus)
    k = _integer(phase_multiplier) % q
    defects = path_defects(q, base, increments, path, initial)
    factors = tuple(_character_delta(q, defect, k)[2] for defect in defects)
    value = Q(1)
    for factor in factors:
        value *= factor
    return {"defects": defects, "constraint_factors": factors,
            "value": value, "normalization": Q(1, q**len(defects)),
            "cartesian_dual_terms_not_enumerated": q**len(defects),
            "factorized_character_terms": q * len(defects),
            "phase_is_faithful": gcd(k, q) == 1}


def cartesian_interference(modulus: int, base: int, increments, path,
                           initial: int | None = 0,
                           phase_multiplier: int = 1) -> dict:
    """Actually enumerate all dual-variable tuples for one candidate path.

    A strict 200,000-term budget keeps exponential work explicit. This is a
    distinct finite oracle for the factorized character calculation.
    """
    q = _small_modulus(modulus)
    k = _integer(phase_multiplier) % q
    defects = path_defects(q, base, increments, path, initial)
    term_count = q**len(defects)
    if term_count > MAX_CARTESIAN_TERMS:
        raise ValueError("Cartesian dual sum exceeds declared term budget")
    raw = [Q()] * q
    for dual in product(range(q), repeat=len(defects)):
        exponent = k * sum(value * defect for value, defect in zip(dual, defects))
        raw[exponent % q] += 1
    reduced = _reduce_coefficients(raw, q)
    normalized = tuple(value / term_count for value in reduced)
    return {"cartesian_dual_terms_enumerated": term_count,
            "raw_coefficients": tuple(raw),
            "reduced_unnormalized_coefficients": reduced,
            "normalization": Q(1, term_count),
            "normalized_coefficients": normalized}


def enumerate_projector(modulus: int, base: int, increments,
                        initial: int | None = 0,
                        phase_multiplier: int = 1) -> dict:
    """Enumerate all candidate paths, comparing modular and Fourier factors.

    This does NOT enumerate every path together with every dual tuple.
    A nonfaithful phase is returned as a detected mismatch, not suppressed.
    """
    q, b, a = _source(_small_modulus(modulus), base, increments)
    k = _integer(phase_multiplier) % q
    if initial is not None:
        _integer(initial)
    count = q**(len(a) + 1)
    if count > MAX_CARTESIAN_TERMS:
        raise ValueError("candidate path count exceeds declared budget")
    selected_count = 0
    interference_count = Q()
    mismatches = 0
    for path in product(range(q), repeat=len(a) + 1):
        defects = path_defects(q, b, a, path, initial)
        direct = int(not any(defects))
        result = Q(1)
        for defect in defects:
            result *= _character_delta(q, defect, k)[2]
        selected_count += direct
        interference_count += result
        mismatches += result != direct
    return {"modulus": q, "base": b, "horizon": len(a),
            "candidate_paths_enumerated": count,
            "direct_accepted_paths": selected_count,
            "interference_total_mass": interference_count,
            "factorization_mismatches": mismatches,
            "initial_selector_present": initial is not None,
            "phase_is_faithful": gcd(k, q) == 1}


def selector_path_mass(modulus: int, base: int, increments,
                       path, selector) -> Q:
    """Normalized selector times transition projector; signed weights allowed."""
    q, b, a = _source(modulus, base, increments)
    x = _path(path, len(a) + 1, q)
    weights = _selector(selector, q)
    return weights[x[0]] * projector_weight(q, b, a, x, initial=None)


def dual_observable_transport(modulus: int, base: int, increments,
                              frequencies) -> dict:
    """Backward dual path and the remaining initial-boundary character."""
    q, b, a = _source(modulus, base, increments)
    h = _integers(frequencies)
    if len(h) != len(a) + 1:
        raise ValueError("one frequency per source state required")
    cumulative = [0] * len(h)
    running = 0
    for j in range(len(h) - 1, -1, -1):
        running = (h[j] + b * running) % q
        cumulative[j] = running
    offset = sum(a[j - 1] * cumulative[j] for j in range(1, len(h))) % q
    return {"initial_frequency": cumulative[0], "source_offset": offset,
            "dual_multipliers": tuple(-value % q for value in cumulative),
            "transported_frequencies": tuple(cumulative)}


def observable_transform(modulus: int, base: int, increments,
                         frequencies, selector) -> tuple[Q, ...]:
    """Exact e_q(source_offset)*sigmahat(initial_frequency).

    This concerns a prescribed finite observable, not its time average.
    """
    q = _small_modulus(modulus)
    weights = _selector(selector, q)
    data = dual_observable_transport(q, base, increments, frequencies)
    powers = tuple(data["source_offset"] + data["initial_frequency"] * s
                   for s in range(q))
    return character_sum(q, powers, weights)


def quotient_path_transport(fine_modulus: int, coarse_modulus: int,
                            base: int, increments, initial: int = 0) -> dict:
    """Compatible source paths under reduction of residue coordinates."""
    fine, b, a = _source(fine_modulus, base, increments)
    coarse = _integer(coarse_modulus, 2)
    if fine % coarse:
        raise ValueError("coarse modulus must divide fine modulus")
    s = _integer(initial)
    fine_path = cyclic_path(fine, b, a, s)
    coarse_path = cyclic_path(coarse, b, a, s)
    reduced = tuple(x % coarse for x in fine_path)
    if reduced != coarse_path:
        raise AssertionError("quotient path transport failed")
    return {"fine_path": fine_path, "coarse_path": coarse_path,
            "reduced_path": reduced, "character_frequency_scale": fine // coarse}


def circle_inclusion_transport(coarse_modulus: int, fine_modulus: int,
                               base: int, increments, initial: int = 0) -> dict:
    """Phase-preserving inclusion x mod q -> (Q/q)x mod Q.

    This is NOT the preceding quotient operation. Both source increments
    and initial state are scaled, preserving the physical circle phases.
    """
    coarse, b, a = _source(coarse_modulus, base, increments)
    fine = _integer(fine_modulus, 2)
    if fine % coarse:
        raise ValueError("fine modulus must be a multiple of coarse modulus")
    scale = fine // coarse
    s = _integer(initial)
    coarse_path = cyclic_path(coarse, b, a, s)
    fine_path = cyclic_path(fine, b, tuple(scale*x for x in a), scale*s)
    included = tuple(scale*x for x in coarse_path)
    if fine_path != included:
        raise AssertionError("circle inclusion did not commute with source")
    phases = tuple(Q(x, coarse) for x in coarse_path)
    if phases != tuple(Q(x, fine) for x in fine_path):
        raise AssertionError("physical circle phases changed under inclusion")
    return {"coarse_path": coarse_path, "fine_path": fine_path,
            "included_path": included, "scale": scale, "phases": phases}


def rational_residue(value: int | Q, modulus: int) -> int:
    """Rational residue coordinate; rejects denominator poles modulo q."""
    phase = _rational(value)
    q = _integer(modulus, 2)
    if gcd(phase.denominator, q) != 1:
        raise ValueError("rational denominator is not a unit modulo modulus")
    return phase.numerator * pow(phase.denominator, -1, q) % q


def circle_encoding(value: int | Q, modulus: int) -> int:
    """Circle subgroup coordinate, requiring denominator to divide q."""
    phase = _rational(value)
    q = _integer(modulus, 2)
    if q % phase.denominator:
        raise ValueError("circle denominator must divide carrier modulus")
    return (phase.numerator * (q // phase.denominator)) % q


def bbp_circle_carrier(horizon: int) -> dict:
    """Authentic BBP rational prefix in its exact odd denominator carrier.

    This function does not expand a root-of-unity sum of that large order.
    The cyclic arithmetic itself supplies the finite projector certificate.
    """
    n = _integer(horizon, 1)
    source = tuple(forcing(j) for j in range(1, n + 1))
    modulus = lcm(*(value.denominator for value in source))
    increments = tuple(circle_encoding(value, modulus) for value in source)
    path = cyclic_path(modulus, 16, increments, 0)
    rational_states = [Q()]
    unwrapped_states = [Q()]
    literal_carries = []
    cumulative_carries = [0]
    for value in source:
        pre_reduction = 16 * rational_states[-1] + value
        rational_states.append(pre_reduction % 1)
        carry = pre_reduction - rational_states[-1]
        unwrapped_states.append(16 * unwrapped_states[-1] + value)
        cumulative = unwrapped_states[-1] - rational_states[-1]
        if carry.denominator != 1 or cumulative.denominator != 1:
            raise AssertionError("source carry lift was not integral")
        literal_carries.append(carry.numerator)
        cumulative_carries.append(cumulative.numerator)
    phases = tuple(Q(x, modulus) for x in path)
    if phases != tuple(rational_states) or modulus % 2 == 0:
        raise AssertionError("authentic BBP carrier identity failed")
    return {"horizon": n, "modulus": modulus, "base": 16,
            "initial": 0, "forcing": source, "increments": increments,
            "path": path, "phases": phases,
            "unwrapped_states": tuple(unwrapped_states),
            "literal_carries": tuple(literal_carries),
            "cumulative_carries": tuple(cumulative_carries),
            "projector_weight": projector_weight(modulus, 16, increments, path),
            "expanded_fourier_sum": False,
            "circle_projector_alone_authenticates_integer_lift": False}


def bbp_prefix_inclusion(short_horizon: int, long_horizon: int) -> dict:
    """Authenticate BBP denominator inclusion on a shared source prefix."""
    short = _integer(short_horizon, 1)
    long = _integer(long_horizon, short)
    coarse = bbp_circle_carrier(short)
    fine = bbp_circle_carrier(long)
    if fine["modulus"] % coarse["modulus"]:
        raise AssertionError("source denominator sequence was not nested")
    scale = fine["modulus"] // coarse["modulus"]
    included = tuple(scale*x for x in coarse["path"])
    fine_prefix = fine["path"][:short + 1]
    if included != fine_prefix:
        raise AssertionError("selected BBP prefix inclusion failed")
    return {"short_horizon": short, "long_horizon": long,
            "coarse_modulus": coarse["modulus"],
            "fine_modulus": fine["modulus"], "scale": scale,
            "included_prefix": included, "fine_prefix": fine_prefix,
            "phases": coarse["phases"]}
