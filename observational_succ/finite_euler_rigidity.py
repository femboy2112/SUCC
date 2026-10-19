"""Exact calibration for finite Euler reflection and positive Poisson rigidity.

Universal analytic claims live in PAPER_C_GENERALIZED_PRIME_RIGIDITY.tex.
Finite evaluations are falsifiers, not proofs of a functional identity.
"""
from collections import Counter
from fractions import Fraction
from math import prod


def _exact(x):
    if type(x) not in (int, Fraction):
        raise ValueError("exact rational input required")
    return Fraction(x)


def _bases(values):
    values = tuple(_exact(x) for x in values)
    if any(x <= 1 for x in values):
        raise ValueError("Euler bases must exceed one")
    return values


def euler_ratio(U, V, s):
    """Evaluate at a nonzero integer, where none of these factors vanishes."""
    U, V = _bases(U), _bases(V)
    if type(s) is not int or s == 0:
        raise ValueError("nonzero integer exponent required; zero needs analytic limits")
    return prod((1-u**(-s) for u in U), start=Fraction(1)) / prod(
        (1-v**(-s) for v in V), start=Fraction(1))


def inversion_certificate(U, V, n):
    """F(-n)=epsilon*C**n*F(n), including unequal cardinalities."""
    U, V = _bases(U), _bases(V)
    if type(n) is not int or n <= 0:
        raise ValueError("positive integer exponent required")
    sign = (-1)**(len(U)+len(V))
    scale = prod(U, start=Fraction(1))/prod(V, start=Fraction(1))
    left = euler_ratio(U,V,-n)
    right = sign*scale**n*euler_ratio(U,V,n)
    if left != right:
        raise ArithmeticError("finite inversion identity failed")
    return {"negative_value":left,"positive_value":euler_ratio(U,V,n),
            "parity":sign,"product_ratio":scale,"identity_verified":True}


def reflection_obstruction(U,V):
    """Finite input signature used by the proved classification theorem.

    For the real positive axis, the first unmatched base b has
    b**t * log(F(t)) -> -signed_multiplicity. This is a paper limit.
    """
    U,V=_bases(U),_bases(V)
    counts=Counter(U)
    counts.subtract(V)
    remaining={b:m for b,m in counts.items() if m}
    base=min(remaining) if remaining else None
    return {"order_at_zero":len(U)-len(V),
            "product_ratio":prod(U,start=Fraction(1))/prod(V,start=Fraction(1)),
            "same_multiset":not remaining,
            "least_unmatched_base":base,
            "signed_multiplicity":remaining[base] if remaining else 0,
            "reflection_possible_by_paper_theorem":not remaining}


def symmetric_atom_poisson_obstruction(x, weight=1):
    """For atoms of weight w at +/-x, pi²*(mu(sinc²)-mu({0})) >= bound.

    Uses sin(pi*delta)>=2*delta, delta=distance(x,Z)<=1/2.
    A positive bound contradicts unit-gap Fourier self-duality. No assertion
    that a finite atom list is an infinite Fourier certificate is made.
    """
    x,weight=_exact(x),_exact(weight)
    if x < 1 or weight <= 0:
        raise ValueError("positive source weight and atom at least one required")
    floor=x.numerator//x.denominator
    distance=min(x-floor,floor+1-x)
    return {"distance_to_integer":distance,
            "pi_squared_excess_lower":8*weight*distance*distance/(x*x),
            "integer_atom":distance==0,
            "exact_at_half_integer":distance==Fraction(1,2)}


def positive_selfdual_gap_mutant(s):
    """Z(s)=((2**s+2**(1-s))/3)*zeta(s), not a Beurling source.

    Its positive self-dual measure is (2/3)delta_(2Z)+(1/3)delta_(Z/2),
    with mass one at zero but a forbidden atom of weight 1/3 at 1/2.
    """
    if type(s) is not int:
        raise ValueError("integer calibration exponent required")
    return (Fraction(2)**s+Fraction(2)**(1-s))/3
