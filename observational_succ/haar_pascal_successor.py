"""Signed Pascal hierarchy (I-S_16)^m on the authenticated Haar word frame.

A positive-minus-negative unit successor generates binomial/Pascal weights.
The Fourier gap decreases exponentially with m; it is NOT a pi-normality proof.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
from observational_succ.haar_successor_junction import B, ZERO, word_law, collision_energy


def pascal_successor_energy(digits: list[int], starts: int, depth: int, order: int) -> Fraction:
    """Exact signed Pascal successor energy, no cyclic time-wrap.

    For all order>=1,
      (2-sqrt(2+sqrt2))**order * (E_(depth+1)-E_depth)
         <= J_order <= 4**order * (E_(depth+1)-E_depth).
    The code asserts the weaker rational lower constant (3/20)**order.
    """
    if order < 1 or depth < 0 or starts < 1 or starts+depth+1 > len(digits):
        raise ValueError("order>=1 and sufficient actual source word")
    edge = word_law(digits, starts, depth+1)
    prefix = word_law(digits, starts, depth)
    support = set()
    for e in edge:
        for shift in range(order+1):
            support.add(e[:-1]+((e[-1]+shift)%B,))
    coeff = [(-1)**k*comb(order,k) for k in range(order+1)]
    value = B**(depth+1)*sum((sum((coeff[k]*edge.get(e[:-1]+((e[-1]-k)%B,),ZERO)
              for k in range(order+1)),ZERO)**2 for e in support),ZERO)
    detail = collision_energy(edge,depth+1)-collision_energy(prefix,depth)
    assert 20**order*value >= 3**order*detail
    assert value <= 4**order*detail
    return value
