"""Exact rational source/observer Pólya calculations, research-only.

Fixed primitive p only enters through a=p**(-4*epsilon). No zeta-zero data.
"""
from fractions import Fraction
from math import log


def source_law(j):
    assert j >= 0
    return [Fraction(1, j + 1)] * (j + 1)


def tilted_law(a, j):
    a = Fraction(a)
    assert 0 < a < 1 and j >= 0
    z = sum((a**k for k in range(j + 1)), Fraction())
    return [a**k/z for k in range(j + 1)]


def native_birth(j, k):
    assert 0 <= k <= j
    return Fraction(k + 1, j + 2)


def forced_birth(a, j, k):
    """Time-inhomogeneous Markov birth rate generating exactly tilted marginals."""
    a = Fraction(a)
    assert 0 < a < 1 and 0 <= k <= j
    return a**(j+1-k)*(1-a**(k+1))/(1-a**(j+2))


def evolve(q, j, transition):
    out = [Fraction()] * (j + 2)
    for k, v in enumerate(q):
        t = transition(j, k)
        assert 0 <= t <= 1
        out[k] += v*(1-t)
        out[k+1] += v*t
    return out


def fidelity_from_amplitudes(r, j):
    """Exact squared Hellinger affinity with uniform source for rational r>0."""
    r = Fraction(r)
    assert r > 0 and j >= 0
    sm = sum((r**k for k in range(j+1)), Fraction())
    norm2 = sum((r**(2*k) for k in range(j+1)), Fraction())
    return sm**2 / ((j+1)*norm2)


def kl_forward(a, j):
    """D(q_j || uniform) in natural logarithms."""
    a = float(a)
    z = (1-a**(j+1))/(1-a)
    ek = a/(1-a) - (j+1)*a**(j+1)/(1-a**(j+1))
    return log((j+1)/z) + ek*log(a)


def kl_reverse(a, j):
    """D(uniform || q_j) in natural logarithms."""
    a = float(a)
    z = (1-a**(j+1))/(1-a)
    return log(z/(j+1)) - (j/2)*log(a)
