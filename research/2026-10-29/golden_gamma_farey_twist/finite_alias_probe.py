"""Explicit normality-impostor controls. These are NOT claims about π.

Source sequences are deliberately NON-BBP and disclose their construction.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction


def de_bruijn(alphabet: int, order: int) -> tuple[int, ...]:
    """FKM classical lexicographically least de Bruijn word B(alphabet,order).

    Its circular k-block histogram is uniform for every 1<=k<=order.
    Bounds prevent accidental very large allocations in interactive tests.
    """
    if type(alphabet) is not int or type(order) is not int or not 2<=alphabet<=16 or not 1<=order<=5 or alphabet**order>1000000:
        raise ValueError('alphabet 2..16 and order 1..5 with <=1 million cells required')
    a=[0]*(alphabet*order+1)
    output=[]
    def db(t,p):
        if t>order:
            if order%p==0:output.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,alphabet):
                a[t]=j
                db(t+1,t)
    db(1,1)
    if len(output)!=alphabet**order:
        raise ArithmeticError('de Bruijn generator length invariant failed')
    return tuple(output)


def circular_histogram(word, k):
    if not word or k<1:
        raise ValueError('nonempty word and positive block length required')
    n=len(word)
    return Counter(tuple(word[(j+l)%n] for l in range(k)) for j in range(n))


def rational_periodic_number(word, base):
    """The source is a repeating base-b word, hence rational and nonnormal."""
    if not word or not 2<=base<=16 or any(type(d) is not int or d<0 or d>=base for d in word):
        raise ValueError('valid positive-length base-b digit word required')
    n=0
    for d in word:n=base*n+d
    return Fraction(n,base**len(word)-1)


def exact_uniform_upto(word,base,order):
    if len(word)!=base**order:
        return False
    for k in range(1,order+1):
        hist=circular_histogram(word,k)
        if len(hist)!=base**k or set(hist.values())!={base**(order-k)}:
            return False
    return True


def finite_frequency_uniform(q,h):
    """Exact Fourier of the equally spaced q-point measure, integer h."""
    if type(q) is not int or q<1 or type(h) is not int:
        raise ValueError('q positive integer and h integer required')
    return 1 if h%q==0 else 0
