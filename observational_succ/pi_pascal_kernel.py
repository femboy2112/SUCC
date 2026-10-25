"""Exact Pascal kernels and carry-aware rational filters for the fixed BBP source.

The positive tail kernel proves the error enclosures, not distribution of the
selected orbit.  In particular, constructing a source shadowing base q does
not assert that its empirical law equals the original base-16 source law.
All public numerical inputs are integers or exact Fractions.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_source_memory import forcing


def _natural(value: int, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f"integer >= {lower} required")
    return value


def beta_with_integer_second(a: Q, order: int) -> Q:
    """B(a, order+1), using a rational product rather than floating gamma."""
    _natural(order)
    if type(a) not in (int, Q) or a <= 0:
        raise ValueError("positive exact rational first beta parameter required")
    a = Q(a)
    answer = 1 / a
    for j in range(1, order + 1):
        answer *= Q(j) / (a + j)
    return answer


def forcing_pascal_moment(start: int, order: int) -> Q:
    """D[start,order]=(-1)^order Delta^order r(start+1), strictly positive.

    This is the exact beta-integral evaluator.  Its proof uses the fixed
    polynomial g(x)=4-2x^3-x^4-x^5; it is not an arbitrary moment input.
    """
    _natural(start)
    _natural(order)
    return sum((weight * beta_with_integer_second(start + shift, order)
                for weight, shift in ((Q(4), Q(1, 8)),
                                      (-Q(2), Q(1, 2)),
                                      (-Q(1), Q(5, 8)),
                                      (-Q(1), Q(3, 4)))), Q()) / 8


def forcing_pascal_beta_bounds(start: int, order: int) -> tuple[Q, Q]:
    """Strict universal bounds (15/64)B < D < B/2, B=B(start+1/8,order+2)."""
    _natural(start)
    _natural(order)
    b = beta_with_integer_second(start + Q(1, 8), order + 1)
    return Q(15, 64) * b, b / 2


def tail_pascal_interval(start: int, order: int, terms: int = 4) -> tuple[Q, Q]:
    """Strict enclosure of R[start,order]=(-1)^order Delta^order T_start.

    Positive geometric summation avoids taking a difference of independently
    rounded tails.  The upper remainder is D[start+terms,order]/(15*16^terms).
    """
    _natural(start)
    _natural(order)
    _natural(terms, 1)
    lower = sum((forcing_pascal_moment(start + j, order) / 16**(j + 1)
                 for j in range(terms)), Q())
    return lower, lower + forcing_pascal_moment(start + terms, order) / (15 * 16**terms)


def signed_pascal_source(order: int) -> Q:
    """A_order=Delta^order U_0, with the authentic U_0=0.

    A_(k+1)=15*A_k+(-1)^k*D[0,k].  No pi approximation is used.
    """
    _natural(order)
    value = Q()
    for k in range(order):
        value = 15 * value + (-1)**k * forcing_pascal_moment(0, k)
    return value


def source_pascal_row(start: int, order: int, sign: int = -1) -> Q:
    """Literal (E+sign)^order U_start, sign=-1 or +1, from exact BBP states."""
    _natural(start)
    _natural(order)
    if type(sign) is not int or sign not in (-1, 1):
        raise ValueError("Pascal sign must be -1 or 1")
    states = [Q()]
    for n in range(1, start + order + 1):
        states.append(16 * states[-1] + forcing(n))
    return sum((comb(order, j) * sign**(order - j) * states[start + j]
                for j in range(order + 1)), Q())


def pascal_pi_interval(order: int, terms: int = 4) -> tuple[Q, Q]:
    """Rational pi enclosure from A_k/15^k+(-1)^k R_k/15^k=pi/16."""
    _natural(order)
    lower, upper = tail_pascal_interval(0, order, terms)
    value = signed_pascal_source(order)
    if order % 2:
        lower, upper = -upper, -lower
    scale = Q(16, 15**order)
    return scale * (value + lower), scale * (value + upper)


def _filter_parameters(multiplier: int, degree: int, order: int) -> Q:
    _natural(multiplier, 2)
    _natural(degree, 1)
    _natural(order)
    return Q(multiplier, 15**degree)


def rational_filter_coefficients(multiplier: int, degree: int) -> tuple[Q, ...]:
    """Ascending coefficients of P_(q,d)(E)=q*(E-1)^d/15^d."""
    scale = _filter_parameters(multiplier, degree, 0)
    return tuple(scale * (-1)**(degree - j) * comb(degree, j)
                 for j in range(degree + 1))


def scaled_pascal_source(multiplier: int, degree: int, order: int) -> Q:
    """X_k=(q/15^d)^k A_(dk), shadowing q^k*pi/16 when q<=15^d.

    Larger q is allowed for exact algebra but has no vanishing-error guarantee.
    """
    scale = _filter_parameters(multiplier, degree, order)
    return scale**order * signed_pascal_source(degree * order)


def scaled_pascal_error_interval(multiplier: int, degree: int, order: int,
                                 terms: int = 4) -> tuple[Q, Q]:
    """Strict positive bounds on |X_k-q^k*pi/16|; sign is (-1)^(dk+1)."""
    scale = _filter_parameters(multiplier, degree, order)**order
    lower, upper = tail_pascal_interval(0, degree * order, terms)
    return scale * lower, scale * upper


def scaled_pascal_forcing(multiplier: int, degree: int, order: int) -> Q:
    """Exact X_(k+1)-q*X_k, evaluated using the d authentic forcing moments.

    Its sign is (-1)^(dk); for even d it is strictly positive.  This new
    recurrence is derived from, but is not equal to, the original BBP forcing.
    """
    scale = _filter_parameters(multiplier, degree, order)
    block = sum((15**(degree - 1 - j) * (-1)**(degree * order + j)
                 * forcing_pascal_moment(0, degree * order + j)
                 for j in range(degree)), Q())
    return scale**(order + 1) * block


def coherent_filter_degree(multiplier: int) -> int:
    """Additive D(q)=sum_p v_p(q)*min{d>=1:p<=15^d}, q>=2.

    D(qr)=D(q)+D(r).  In particular D(2)=1,D(4)=2,D(16)=4.
    """
    _natural(multiplier, 2)
    remaining = multiplier
    prime = 2
    result = 0
    while prime * prime <= remaining:
        valuation = 0
        while remaining % prime == 0:
            remaining //= prime
            valuation += 1
        if valuation:
            degree, bound = 1, 15
            while bound < prime:
                degree += 1
                bound *= 15
            result += valuation * degree
        prime += 1
    if remaining > 1:
        degree, bound = 1, 15
        while bound < remaining:
            degree += 1
            bound *= 15
        result += degree
    return result


def filter_carry_modulus(multiplier: int, degree: int, order: int) -> int:
    """Required integer-carry modulus b^k for reduced q/15^d=a/b."""
    return _filter_parameters(multiplier, degree, order).denominator**order


def filtered_phase_from_carry(fractional_part: Q, carry_residue: int,
                              multiplier: int, degree: int, order: int) -> Q:
    """Compute {X_k} from {A_(dk)} and floor(A_(dk)) mod b^k.

    Omitting the carry residue is not a valid circle map when b^k>1.
    """
    scale = _filter_parameters(multiplier, degree, order)**order
    if type(fractional_part) not in (int, Q):
        raise ValueError("an exact fractional part is required")
    fractional_part = Q(fractional_part)
    if not 0 <= fractional_part < 1:
        raise ValueError("fractional part must lie in [0,1)")
    modulus = scale.denominator
    if type(carry_residue) is not int or not 0 <= carry_residue < modulus:
        raise ValueError("canonical integer carry residue required")
    return (scale.numerator * (fractional_part + carry_residue) / modulus) % 1


def absolute_shadow_endpoint_obstructions(multiplier: int) -> tuple[str, ...]:
    """Necessary endpoint tests for an INTEGER-polynomial absolute-error shadow.

    If P(16)=q and int P(t)^k d(rho)(t)->0, then P(0),P(1) are in {-1,0,1}.
    Passing these tests does not prove existence of P, or any normality claim.
    """
    _natural(multiplier, 2)
    failures = []
    if multiplier % 16 not in (0, 1, 15):
        failures.append("zero")
    if multiplier % 15 not in (0, 1, 14):
        failures.append("one")
    return tuple(failures)
