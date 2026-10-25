"""Exact weighted Pascal instruments for the authentic BBP source.

The fixed filters construct ternary and base-81 shadows.  Their positive
kernel certificates do not establish invariance of the selected real law.
All decisions use integers or Fractions; no pi digits select the source.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from math import comb

from observational_succ.bbp_source_memory import forcing
from observational_succ.bbp_two_adic import rational_mod
from observational_succ.pi_pascal_kernel import forcing_pascal_moment
from observational_succ.pi_pascal_source import difference_valuation


# Ascending integer numerator coefficients, common denominator, multiplier.
FILTERS = {
    "ternary4": ((-4, 1), 4, 3),
    "ternary5": ((-1, 1), 5, 3),
    "base81": ((3, -1, 1), 3, 81),
    "positive8": ((8, 1), 8, 3),
}


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _filter(name):
    if name not in FILTERS:
        raise ValueError("unknown fixed filter")
    return FILTERS[name]


def _convolve(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return tuple(result)


@lru_cache(maxsize=None, typed=True)
def source_states(last):
    """Original zero-initial rational BBP states, with no real oracle input."""
    _integer(last)
    result = [Q()]
    for n in range(1, last+1):
        result.append(16*result[-1]+forcing(n))
    return tuple(result)


@lru_cache(maxsize=None, typed=True)
def filter_power(name, order):
    """Exact numerator polynomial and denominator of a fixed filter power."""
    _integer(order)
    numerator, denominator, _ = _filter(name)
    answer = (1,)
    for _ in range(order):
        answer = _convolve(answer, numerator)
    return answer, denominator**order


def filtered_source(name, order, start=0):
    """P(E)^order U_start; its leading real mode is q^order 16^start alpha."""
    _integer(start)
    coefficients, denominator = filter_power(name, order)
    states = source_states(start+len(coefficients)-1)
    return sum((a*states[start+j] for j, a in enumerate(coefficients)), Q())/denominator


def ternary4_lift(order):
    """H_order=(E-4)^order U_0, before division by 4^order."""
    _integer(order)
    return 4**order*filtered_source("ternary4", order)


@lru_cache(maxsize=None, typed=True)
def _positive_moment(name, start, order):
    """Integral t^start |P(t)|^order g(x) dx, t=x^8, in a positive basis."""
    _integer(start)
    _integer(order)
    _filter(name)
    if name == "ternary4":
        return sum((comb(order, j)*3**(order-j)*
                    forcing_pascal_moment(start, j)
                    for j in range(order+1)), Q())/4**order
    if name == "ternary5":
        return forcing_pascal_moment(start, order)/5**order
    if name == "base81":
        # P(t)^k = 3^-k sum c_j t^j (1-t)^(2k-j),
        # where sum c_j z^j = (3+5z+3z^2)^k. All coefficients are positive.
        coefficients = (1,)
        for _ in range(order):
            coefficients = _convolve(coefficients, (3, 5, 3))
        return sum((a*forcing_pascal_moment(start+j, 2*order-j)
                    for j, a in enumerate(coefficients)), Q())/3**order
    return sum((comb(order, j)*8**(order-j)*forcing(start+j+1)
                for j in range(order+1)), Q())/8**order


def filter_error_interval(name, order, start=0, terms=4):
    """Strict positive enclosure of the absolute real kernel remainder.

    source = q^order 16^start alpha - sign*remainder; sign=(-1)^order
    for ternary4/5, and +1 for base81/positive8. The last filter's remainder
    grows asymptotically; the enclosure does not assert convergence.
    """
    _integer(terms, 1)
    _integer(start)
    _integer(order)
    _filter(name)
    lower = sum((_positive_moment(name, start+j, order)/16**(j+1)
                 for j in range(terms)), Q())
    upper = lower + _positive_moment(name, start+terms, order)/(15*16**terms)
    return lower, upper


def local_transport(name, start):
    """One local transform, its multiplier, and its exact source error."""
    _integer(start)
    _, _, multiplier = _filter(name)
    value = filtered_source(name, 1, start)
    if name == "base81":
        error = 5*forcing(start+1)+forcing(start+2)/3
    elif name == "ternary4":
        error = forcing(start+1)/4
    elif name == "ternary5":
        error = forcing(start+1)/5
    else:
        error = forcing(start+1)/8
    return value, multiplier, error


def base81_reset_source(start, order):
    """Zero-initial rational source for T_start=16^start alpha-U_start.

    S_k=P81(E)^k U_start-81^k U_start=81^k T_start-M_(start,k).
    For each fixed start>=2 the positive error is asymptotic to9/(64k^2).
    Normality is preserved by the rational affine change of constant;
    selected empirical laws are not asserted equal.
    """
    _integer(start)
    _integer(order)
    return filtered_source("base81", order, start)-81**order*source_states(start)[start]


def base81_reset_forcing(start, order):
    """Positive moment evaluation of S_(k+1)-81S_k, k=order>=0."""
    _integer(start)
    _integer(order)
    return (5*_positive_moment("base81", start, order)
            +_positive_moment("base81", start+1, order)/3)


def base81_reset_mahler(start, order):
    """Exact order-th origin coefficient of the reset source interpolation."""
    _integer(start)
    _integer(order)
    if order == 0:
        return Q()
    values = source_states(start+2*order)
    first = sum((comb(order, j)*(-1)**(order-j)*values[start+order+j]
                 for j in range(order+1)), Q())/3**order
    return first-80**order*values[start]


def phase_from_cover(numerator_phase, integer_residue, denominator):
    """Read {H/denominator} from {H} and floor(H) modulo denominator."""
    _integer(denominator, 1)
    _integer(integer_residue)
    if type(numerator_phase) not in (int, Q):
        raise ValueError("exact rational phase required")
    numerator_phase = Q(numerator_phase)
    if not 0 <= numerator_phase < 1 or integer_residue >= denominator:
        raise ValueError("phase or residue outside its canonical range")
    return (numerator_phase+integer_residue)/denominator


def endpoint_denominator_possible(multiplier, denominator):
    """Necessary all-degree endpoint congruences; not a sufficiency test."""
    _integer(multiplier, 2)
    _integer(denominator, 1)
    value = multiplier*denominator
    return all(min(value % modulus, (-value) % modulus) <= denominator
               for modulus in (16, 15))


@lru_cache(maxsize=None, typed=True)
def dyadic_mahler(kind, maximum_order):
    """Mahler coefficients for H=(E-4)^k U0 or G=P81(E)^k U0.

    The uniform profile and isometry are proved in the paper, not inferred
    from a finite permutation test. 'ternary4' is the UNNORMALIZED H here.
    """
    _integer(maximum_order)
    if kind not in ("ternary4", "base81"):
        raise ValueError("dyadic kind must be ternary4 or base81")
    states = source_states(2*maximum_order)
    result = [Q()]
    for j in range(1, maximum_order+1):
        if kind == "ternary4":
            value = sum((comb(j, i)*(-5)**(j-i)*states[i]
                         for i in range(j+1)), Q())
        else:
            value = sum((comb(j, i)*(-1)**(j-i)*states[j+i]
                         for i in range(j+1)), Q())/3**j
        result.append(value)
    return tuple(result)


def dyadic_filtered_mod(kind, index, bits):
    """Exact reduction of the proved continuous dyadic interpolation."""
    if type(index) is not int:
        raise ValueError("integer index required")
    _integer(bits, 1)
    degree = 1
    while difference_valuation(degree+1) < bits:
        degree += 1
    representative = index % (1 << bits)
    result = 0
    binomial = 1
    for j, coefficient in enumerate(dyadic_mahler(kind, degree)):
        if j:
            binomial = binomial*(representative-j+1)//j
        result += binomial*rational_mod(coefficient, bits)
    return result % (1 << bits)


def ambiguous_cylinders(multiplier, output_bits, lookahead):
    """Binary input cells that straddle a T_q output-word boundary.

    q is odd and 2^lookahead>=q. Returns exact indices at input depth
    output_bits+lookahead. This is circle multiplication, not radix conversion.
    """
    _integer(multiplier, 3)
    _integer(output_bits, 1)
    _integer(lookahead, 1)
    if multiplier % 2 == 0 or 2**lookahead < multiplier:
        raise ValueError("odd multiplier and enough lookahead required")
    return tuple(sorted({(2**lookahead*j)//multiplier
                         for j in range(1, multiplier*2**output_bits)
                         if j % multiplier}))


def alternating_words(length):
    _integer(length, 1)
    a = sum(1 << j for j in range(0, length, 2))
    return tuple(sorted((a, (1 << length)-1-a)))


def bernoulli_cdf(point, one_probability):
    """Exact CDF of iid biased binary digits at a rational point.

    F(x)=q F(2x) below 1/2; F(x)=q+p F(2x-1) above it.
    Eventual periodicity of a rational binary expansion closes the recurrence.
    The measure is nonatomic for 0<p<1, so endpoint conventions agree.
    """
    if type(point) not in (int, Q) or type(one_probability) not in (int, Q):
        raise ValueError("exact rational inputs required")
    point, p = Q(point), Q(one_probability)
    if not 0 <= point <= 1 or not 0 < p < 1:
        raise ValueError("point in [0,1] and probability in (0,1) required")
    if point == 1:
        return Q(1)
    q = 1-p
    seen, increments, weights = {}, [], []
    x = point
    while x not in seen and x:
        seen[x] = len(increments)
        digit = int(2*x)
        increments.append(q if digit else Q())
        weights.append(p if digit else q)
        x = 2*x-digit
    if not x:
        result = Q()
        loop = len(increments)
    else:
        loop = seen[x]
        a, b = Q(), Q(1)
        for inc, weight in zip(increments[loop:], weights[loop:]):
            a += b*inc
            b *= weight
        result = a/(1-b)
    for j in range(loop-1, -1, -1):
        result = increments[j]+weights[j]*result
    return result


def bernoulli_multiplied_half(multiplier, one_probability):
    """Exact mass of [0,1/2) under T_q applied to the binary Bernoulli law."""
    _integer(multiplier, 1)
    return sum((bernoulli_cdf(Q(2*j+1, 2*multiplier), one_probability)
                -bernoulli_cdf(Q(j, multiplier), one_probability)
                for j in range(multiplier)), Q())


def alternating_mass(length, one_probability):
    _integer(length, 1)
    if type(one_probability) not in (int, Q) or not 0 < one_probability < 1:
        raise ValueError("exact probability in (0,1) required")
    p = Q(one_probability)
    return sum((p**word.bit_count()*(1-p)**(length-word.bit_count())
                for word in alternating_words(length)), Q())
