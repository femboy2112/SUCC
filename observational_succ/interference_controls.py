"""Exact finite blind-spot controls for source-labelled interference reports.

Rational turns represent circle characters without floating trigonometry.
Phase arrays, finite laws, and periodic radix points are distinct interfaces.
Nothing here authenticates a supplied array as the zero-seeded BBP orbit.
Proofs and source-attached controls are in the interference-atlas adversary
notes. No original source or observation module is modified.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from math import gcd, lcm


MAX_POINTS = 4096
MAX_GRAPH = 64
MAX_PROBES = 256
MAX_BITS = 8


def _q(value) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact int or Fraction required")
    return Q(value)


def _int(value, low=0, high=None) -> int:
    if type(value) is not int or value < low or (high is not None and value > high):
        raise ValueError("integer outside the declared bounded domain")
    return value


def _phases(values, maximum=MAX_POINTS) -> tuple[Q, ...]:
    if not isinstance(values, (tuple, list)) or not 1 <= len(values) <= maximum:
        raise ValueError("nonempty bounded phase list required")
    return tuple(_q(value) % 1 for value in values)


def _edges(size, edges):
    _int(size, 1, MAX_GRAPH)
    if not isinstance(edges, (tuple, list)) or len(edges) > MAX_PROBES:
        raise ValueError("bounded edge list required")
    result = []
    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 2:
            raise ValueError("each edge has two vertex indices")
        result.append(tuple(_int(i, 0, size-1) for i in edge))
    return tuple(result)


def pair_phase_signature(phases, edges) -> tuple[Q, ...]:
    """Turns of z_i conjugate(z_j) for the labelled, oriented edges."""
    values = _phases(phases, MAX_GRAPH)
    return tuple((values[i]-values[j]) % 1 for i, j in _edges(len(values), edges))


def pair_gauge_components(size: int, edges) -> tuple[tuple[int, ...], ...]:
    """One unconstrained U(1) gauge per component of the pair graph."""
    edges = _edges(size, edges)
    parent = list(range(size))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, j in edges:
        parent[root(j)] = root(i)
    groups = {}
    for i in range(size):
        groups.setdefault(root(i), []).append(i)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda g: g[0]))


def pair_gauge_offsets(left, right, edges) -> tuple[Q, ...] | None:
    """Component rotations if pair reports agree, else None."""
    left, right = _phases(left, MAX_GRAPH), _phases(right, MAX_GRAPH)
    if len(left) != len(right):
        raise ValueError("phase vectors must have equal length")
    components = pair_gauge_components(len(left), edges)
    offsets = tuple((b-a) % 1 for a, b in zip(left, right))
    if any(any(offsets[i] != offsets[group[0]] for i in group) for group in components):
        return None
    return tuple(offsets[group[0]] for group in components)


def references_fix_pair_gauges(size: int, edges, references) -> bool:
    """Known phase values determine all circle phases iff every component is anchored."""
    components = pair_gauge_components(size, edges)
    if not isinstance(references, (tuple, list)):
        raise ValueError("reference vertex list required")
    refs = {_int(i, 0, size-1) for i in references}
    return all(any(i in refs for i in group) for group in components)


def _rows(rows, size=None):
    if not isinstance(rows, (tuple, list)) or not 1 <= len(rows) <= MAX_PROBES:
        raise ValueError("nonempty bounded integer exponent rows required")
    if size is None:
        if not isinstance(rows[0], (tuple, list)):
            raise ValueError("integer exponent rows required")
        size = len(rows[0])
    _int(size, 1, MAX_GRAPH)
    result = []
    for row in rows:
        if not isinstance(row, (tuple, list)) or len(row) != size or any(type(x) is not int for x in row):
            raise ValueError("consistent exact integer exponent rows required")
        result.append(tuple(row))
    return tuple(result)


def monomial_phase_signature(phases, exponent_rows) -> tuple[Q, ...]:
    """Exact turns of finite integer monomial characters, including conjugates."""
    values = _phases(phases, MAX_GRAPH)
    return tuple(sum((a*x for a, x in zip(row, values)), Q()) % 1
                 for row in _rows(exponent_rows, len(values)))


def global_charge_gcd(exponent_rows) -> int:
    """Residual global gauge order after connected pair data; zero means U(1)."""
    result = 0
    for row in _rows(exponent_rows):
        result = gcd(result, sum(row))
    return result


def seed_phase_alias_spacing(probes, *, base=16) -> Q | None:
    """For reports e(h U_n(s)), indistinguishable seed shifts are spacing*Z.

    Returns None if every h is zero, in which case all real seed shifts
    are invisible. This is a phase-report kernel, not full seed recovery.
    """
    base = _int(base, 2, 256)
    if not isinstance(probes, (tuple, list)) or not 1 <= len(probes) <= MAX_PROBES:
        raise ValueError("bounded (time, integer frequency) probes required")
    divisor = 0
    for probe in probes:
        if not isinstance(probe, (tuple, list)) or len(probe) != 2:
            raise ValueError("each probe is (time, integer frequency)")
        time = _int(probe[0], 0, 256)
        frequency = probe[1]
        if type(frequency) is not int:
            raise ValueError("integer Fourier frequency required")
        divisor = gcd(divisor, frequency*base**time)
    return None if divisor == 0 else Q(1, divisor)


def phase_alias_modulus(phases) -> int:
    """A common-denominator moving frequency aliases every supplied rational phase."""
    result = 1
    for phase in _phases(phases):
        result = lcm(result, phase.denominator)
    return result


def radix_cycle(point, *, base=16, max_period=MAX_POINTS) -> tuple[Q, ...]:
    """Actual purely periodic rational orbit under x -> base*x mod 1.

    Coprime denominator guarantees periodicity. Budget exhaustion raises
    rather than declaring the orbit aperiodic or normal.
    """
    base = _int(base, 2, 256)
    maximum = _int(max_period, 1, MAX_POINTS)
    start = _q(point) % 1
    if gcd(start.denominator, base) != 1:
        raise ValueError("pure-period interface requires denominator coprime to the base")
    values, current = [], start
    for _ in range(maximum):
        values.append(current)
        current = (base*current) % 1
        if current == start:
            return tuple(values)
    raise ValueError("period exceeds declared finite budget")


def coset_character_phase(phases, frequency: int) -> Q | None:
    """Mean character on a complete uniform circle coset.

    None denotes exact zero. Otherwise the returned rational turn denotes
    a unit character value. Rejects arbitrary arrays and unequal sampling.
    """
    values = _phases(phases)
    if type(frequency) is not int:
        raise ValueError("integer frequency required")
    size, origin = len(values), min(values)
    expected = {(origin+Q(j, size)) % 1 for j in range(size)}
    if len(set(values)) != size or set(values) != expected:
        raise ValueError("phases are not one complete equally weighted coset")
    return None if frequency % size else (frequency*origin) % 1


def _digits(digits, base):
    base = _int(base, 2, 256)
    if not isinstance(digits, (tuple, list)) or not 1 <= len(digits) <= MAX_POINTS:
        raise ValueError("nonempty bounded digit word required")
    return tuple(_int(d, 0, base-1) for d in digits)


def cyclic_word_counts(digits, depth: int, *, base=16) -> dict[tuple[int, ...], int]:
    values = _digits(digits, base)
    depth = _int(depth, 1, 32)
    return dict(Counter(tuple(values[(i+j) % len(values)] for j in range(depth))
                        for i in range(len(values))))


def de_bruijn_cycle(*, base=16, order=2) -> tuple[int, ...]:
    """Classical cyclic de Bruijn word via an Euler circuit, not a BBP source."""
    base, order = _int(base, 2, 16), _int(order, 1, 8)
    if base**order > MAX_POINTS:
        raise ValueError("de Bruijn circuit exceeds the finite edge budget")
    vertices = base**(order-1)
    next_digit = [0]*vertices
    stack, labels = [(0, None)], []
    while stack:
        vertex, entering = stack[-1]
        if next_digit[vertex] < base:
            digit = next_digit[vertex]
            next_digit[vertex] += 1
            stack.append(((base*vertex+digit) % vertices, digit))
        else:
            stack.pop()
            if entering is not None:
                labels.append(entering)
    result = tuple(reversed(labels))
    if len(result) != base**order:
        raise ArithmeticError("Euler circuit failed to consume every edge")
    return result


def periodic_radix_point(digits, *, base=16) -> Q:
    """The actual rational point 0.overline(digits), with the all-maximal seam excluded."""
    values = _digits(digits, base)
    if all(d == base-1 for d in values):
        raise ValueError("all-maximal expansion represents the endpoint seam 1")
    numerator = 0
    for digit in values:
        numerator = base*numerator+digit
    return Q(numerator, base**len(values)-1)


def leading_digit(turn, *, base=16) -> int:
    base = _int(base, 2, 256)
    value = base*(_q(turn) % 1)
    return value.numerator//value.denominator


def _binary_law(law):
    if not isinstance(law, (tuple, list)) or not 2 <= len(law) <= 2**MAX_BITS:
        raise ValueError("bounded binary probability law required")
    size = len(law)
    if size & (size-1):
        raise ValueError("binary law length must be a power of two")
    values = tuple(_q(x) for x in law)
    if any(x < 0 for x in values) or sum(values, Q()) != 1:
        raise ValueError("probabilities must be nonnegative and sum to one")
    return values


def walsh_perturbation(bits: int, mask: int, bias=1) -> tuple[Q, ...]:
    """P(x)=2^-bits [1+bias*(-1)^popcount(x&mask)], preserving all other Walsh modes."""
    bits = _int(bits, 1, MAX_BITS)
    mask = _int(mask, 1, 2**bits-1)
    bias = _q(bias)
    if not -1 <= bias <= 1:
        raise ValueError("bias must lie in [-1,1]")
    return tuple((1+bias*(-1)**((x & mask).bit_count()))/2**bits for x in range(2**bits))


def walsh_moments(law, masks) -> tuple[Q, ...]:
    values = _binary_law(law)
    if not isinstance(masks, (tuple, list)) or len(masks) > len(values):
        raise ValueError("bounded Walsh mask list required")
    masks = tuple(_int(mask, 0, len(values)-1) for mask in masks)
    if len(set(masks)) != len(masks):
        raise ValueError("duplicate Walsh masks are not additional observations")
    return tuple(sum((weight*(-1)**((x & mask).bit_count())
                      for x, weight in enumerate(values)), Q()) for mask in masks)


def power_two_character_remainder(law, frequency: int) -> tuple[Q, ...]:
    """Exact rational coefficient vector modulo Phi_(2^k)=X^(2^(k-1))+1.

    The mean exp(2*pi*i*frequency*x/len(law)) is zero iff all returned
    coefficients vanish. The trivial character returns the singleton (1,).
    """
    values = _binary_law(law)
    if type(frequency) is not int:
        raise ValueError("integer Fourier frequency required")
    size = len(values)
    divisor = gcd(frequency, size)
    order = size//divisor
    if order == 1:
        return (Q(1),)
    multiplier = frequency//divisor
    counts = [Q()]*order
    for x, weight in enumerate(values):
        counts[(multiplier*x) % order] += weight
    return tuple(counts[j]-counts[j+order//2] for j in range(order//2))


def cyclic_sign_correlations(signs) -> tuple[Q, ...]:
    """All cyclic pair lags of a labelled sign stream; not its full word law."""
    if not isinstance(signs, (tuple, list)) or not 1 <= len(signs) <= MAX_GRAPH:
        raise ValueError("bounded sign stream required")
    if any(type(sign) is not int or sign not in (-1, 1) for sign in signs):
        raise ValueError("signs must be exact +1 or -1")
    size = len(signs)
    return tuple(Q(sum(signs[(i+k) % size]*signs[i] for i in range(size)), size)
                 for k in range(size))


def geometric_label_rivals(period: int):
    """Finite quotient of geometric-H click laws for a uniform coset versus Haar.

    Row r=1..period collects all positive H congruent to r modulo period.
    Columns are (coin=0, coin=1). Only this retained report is compared;
    no sampled-clock identities or phase values are included.
    """
    period = _int(period, 1, 256)
    denominator = 2**period-1
    weights = tuple(Q(2**(period-r), denominator) for r in range(1, period+1))
    haar = tuple((weight/2, weight/2) for weight in weights)
    control = haar[:-1]+((weights[-1], Q()),)
    return control, haar


def chi_square(left, right) -> Q:
    """Exact finite chi-square(left||right); right must have full support."""
    if not isinstance(left, (tuple, list)) or not isinstance(right, (tuple, list)):
        raise ValueError("finite probability vectors required")
    if not 1 <= len(left) == len(right) <= 512:
        raise ValueError("equal bounded probability vector sizes required")
    left, right = tuple(_q(x) for x in left), tuple(_q(x) for x in right)
    if any(p < 0 for p in left) or any(q <= 0 for q in right):
        raise ValueError("left must be nonnegative and right strictly positive")
    if sum(left, Q()) != 1 or sum(right, Q()) != 1:
        raise ValueError("probability vectors must sum to one")
    return sum(((p-q)**2/q for p, q in zip(left, right)), Q())
