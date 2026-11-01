"""Independently structured, exact integer/rational checks; no global theorem oracle."""
from __future__ import annotations
from fractions import Fraction
from math import factorial


def source_via_combined_rational(n):
    n=Fraction(n)
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return (120*n*n-89*n+16)/d


def bump_l2_via_factorials(power=4):
    # (1/4) Beta(1/2, 2p+1) = 2**(4p) ((2p)!)^2 / (2 (4p+1)!)
    # Integral [-1,1] (1-y^2)^(2p) dy /4
    from math import comb
    j=2*power
    return Fraction(2**(2*j-1)*factorial(j)**2, factorial(2*j+1))


def finite_seed_series(k):
    source=Fraction(0)
    for j in range(k,0,-1):
        # independently compute a reverse nested polynomial in 1/16
        source=(source+source_via_combined_rational(j))/16
    return source


def source_states_from_explicit_sum(n):
    return sum((16**(n-j)*source_via_combined_rational(j)
               for j in range(1,n+1)),Fraction(0))
