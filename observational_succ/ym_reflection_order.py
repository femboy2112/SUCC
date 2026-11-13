"""Exact reflection-order controls for finite SU(2) Wilson approximations.

Proofs and hypotheses: research/2026-11-13/yang_mills_succ/
coupled_wilson/REFLECTION_ORDER.md.  These are finite certificates, not
continuum Yang--Mills or mass-gap proofs.
"""

from fractions import Fraction
from math import ceil, comb, factorial
from typing import Sequence

from observational_succ.ym_reflection_bridge import haar_moment, polynomial_product
from observational_succ.ym_succ_character import (
    _natural, _rational as _q, chebyshev_character as su2_character,
)


def reflected_sum_pair(
    density: Sequence[int | Fraction],
    left: Sequence[int | Fraction],
    right: Sequence[int | Fraction],
) -> Fraction:
    """Unnormalized integral Q(x+y) left(x) right(y) against product Haar.

    Real rational polynomials only.  A reflected form on complex tests
    conjugates the coefficients in its first slot; no complex API is implied.
    """
    density, left, right = (tuple(map(_q, p)) for p in (density, left, right))
    return sum(
        (
            coefficient * comb(degree, split) * a * b
            * haar_moment(split + i) * haar_moment(degree - split + j)
            for degree, coefficient in enumerate(density)
            for split in range(degree + 1)
            for i, a in enumerate(left)
            for j, b in enumerate(right)
        ), Fraction(0),
    )


def even_taylor_character_coefficients(
    beta: int | Fraction, degree: int,
) -> tuple[Fraction, ...]:
    """Exact nonnegative character expansion of P_degree(beta*x).

    Requires nonnegative coupling and even degree: positive type plus
    pointwise strict positivity, respectively.  RP additionally requires
    the reflection split stated in the companion proof.
    """
    beta = _q(beta)
    _natural(degree)
    if beta < 0 or degree % 2:
        raise ValueError("nonnegative beta and nonnegative even degree required")
    coefficients = [Fraction(0) for _ in range(degree + 1)]
    for j in range(degree + 1):
        scalar = beta**j / (factorial(j) * 2**j)
        for k in range(j // 2 + 1):
            multiplicity = comb(j, k) - (comb(j, k - 1) if k else 0)
            coefficients[j - 2 * k] += scalar * multiplicity
    return tuple(coefficients)


def factorwise_expectation_error(
    betas: Sequence[int | Fraction], degrees: Sequence[int],
    observable_bound: int | Fraction = 1,
) -> Fraction:
    """Rational upper bound 2 M 3**ceil(2 sum beta) sum beta**(K+1)/(K+1)!.

    Valid for bounded observations of any finite Wilson source with the
    given couplings.  No reflection assumptions are needed for this error
    estimate; they are needed for exact RP of the approximants.
    """
    if len(betas) != len(degrees):
        raise ValueError("one even degree per coupling required")
    betas = tuple(map(_q, betas))
    bound = _q(observable_bound)
    if bound < 0:
        raise ValueError("observable bound must be nonnegative")
    for beta, degree in zip(betas, degrees):
        even_taylor_character_coefficients(beta, degree)
    tail = sum(
        (beta**(degree + 1) / factorial(degree + 1)
         for beta, degree in zip(betas, degrees)), Fraction(0),
    )
    return 2 * bound * 3 ** ceil(2 * sum(betas, Fraction(0))) * tail


def global_square_witness() -> dict[str, object]:
    """The beta=1, order-two global Taylor-square RP countercertificate."""
    density = polynomial_product((1, Fraction(1, 2), Fraction(1, 8)),
                                 (1, Fraction(1, 2), Fraction(1, 8)))
    character = su2_character(4)
    partition = reflected_sum_pair(density, (1,), (1,))
    cross = reflected_sum_pair(density, (1,), character) / partition
    detail = reflected_sum_pair(density, character, character) / partition
    witness = [-value / cross for value in character]
    witness[0] += 1
    return {
        "density": density,
        "partition": partition,
        "character": character,
        "gram": ((Fraction(1), cross), (cross, detail)),
        "witness": tuple(witness),
        "reflected_square": reflected_sum_pair(density, witness, witness) / partition,
    }
