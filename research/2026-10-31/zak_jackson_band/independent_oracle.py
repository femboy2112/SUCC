"""Algorithmically independent exact coefficient and source verification oracle."""
from fractions import Fraction
from itertools import product


def quadruple_frequency_counts(length: int) -> dict[int,int]:
    """Direct 4-tuple enumeration, not triangular polynomial convolution."""
    if not 2 <= length <= 16:
        raise ValueError('tiny exhaustive oracle only')
    d = {}
    for i,j,k,l in product(range(length),repeat=4):
        x = i+j-k-l
        d[x] = d.get(x,0)+1
    return d


def rational_original_source(x: Fraction | int) -> Fraction:
    """Horner numerator with independently factored odd/base denominators."""
    x=Fraction(x)
    if x<1: raise ValueError('x>=1')
    numerator=16+x*(-89+120*x)
    factors=(2*x-1,4*x-1,8*x-7,8*x-3)
    d=Fraction(1)
    for v in factors: d*=v
    return numerator/d


def direct_flat_top_frequency(length: int, freq: int) -> Fraction:
    """Direct four-index tuples and integer-frequency interval condition."""
    d=quadruple_frequency_counts(length)
    return Fraction(sum(v for k,v in d.items() if abs(freq-k)<=3*length),length**4)


def direct_laurent_moment(j:int)->int:
    if type(j) is not int or j<0: raise ValueError('nonnegative j')
    return 4*7**j-2*4**j-3**j-2**j
