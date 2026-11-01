"""Exact arithmetic controls for all-order Laurent signed-lag clock sharpness.

A self-contained independent oracle, using only Fraction and integer polynomial
recurrences. No pi normality or quantum/probabilistic theorem is asserted.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb

POLES = ((4, F(7, 8)), (-2, F(1, 2)), (-1, F(3, 8)), (-1, F(1, 4)))


def _order(d: int) -> int:
    if type(d) is not int or not 1 <= d <= 24:
        raise ValueError('finite certificate order 1..24 required')
    return d


def _xk(x: int | F, k: int) -> tuple[F, int]:
    if type(x) not in (int, F) or F(x) <= 0 or type(k) is not int or k < 1:
        raise ValueError('positive rational source coordinate and positive lag required')
    return F(x), k


def polynomial_derivative(coefficients: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((i + 1) * coefficients[i + 1] for i in range(len(coefficients) - 1))


def polynomial_multiply_x(coefficients: tuple[int, ...]) -> tuple[int, ...]:
    return (0,) + coefficients


def eval_poly(p: tuple[int, ...], x: F) -> F:
    value = F(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


@lru_cache(maxsize=32)
def moment(d: int) -> F:
    """Exact M_d=sum_(j>=1) j**d/16**j by x*d/dx on rational PGFs."""
    if type(d) is not int or not 0 <= d <= 25:
        raise ValueError('finite certificate moment 0..25 required')
    p = (0, 1)    # S_0=x/(1-x)
    for m in range(d):
        derivative = polynomial_derivative(p)
        q = [0] * (len(p) + 2)
        for i, c in enumerate(derivative):
            q[i + 1] += c
            q[i + 2] -= c
        for i, c in enumerate(p):
            q[i + 1] += (m + 1) * c
        p = tuple(q)
    t = F(1, 16)
    return eval_poly(p, t) / (1-t)**(d+1)


def source(z: int | F) -> F:
    if type(z) not in (int, F) or F(z) < 1:
        raise ValueError('source real time >=1 required')
    z = F(z)
    return sum((F(w, 8) / (z - p) for w, p in POLES), F(0))


def original_coefficient(j: int, d: int) -> F:
    _order(d)
    if type(j) is not int or j < 1:
        raise ValueError('positive source shift required')
    return sum((F(w, 8) * (p - j)**d for w, p in POLES), F(0))


def finite_leading(k: int, d: int) -> F:
    _order(d)
    if type(k) is not int or k < 1:
        raise ValueError('positive lag required')
    return sum((original_coefficient(j, d) / 16**j for j in range(1, k+1)), F(0))


def infinite_leading(d: int) -> F:
    """Closed rational c_d, not approximated by a finite geometric sum."""
    _order(d)
    return sum((F(w, 8) * sum((F(comb(d, t)) * p**(d-t) * (-1)**t * moment(t)
                             for t in range(d+1)), F(0))
                for w, p in POLES), F(0))


def true_source_lag(x: int | F, k: int) -> F:
    x, k = _xk(x, k)
    return sum((F(16**(k-j)) * source(x+j) for j in range(1, k+1)), F(0))


def corrected_lag(x: int | F, k: int, d: int) -> F:
    x, k = _xk(x, k)
    _order(d)
    return sum((F(16**(k-j))*sum((original_coefficient(j, a)/x**(a+1)
                     for a in range(1, d)), F(0)) for j in range(1, k+1)), F(0))


def residual(x: int | F, k: int, d: int) -> F:
    return true_source_lag(x, k) - corrected_lag(x, k, d)


def independent_residual(x: int | F, k: int, d: int) -> F:
    """Exact geometric-series remainder, independent of true minus truncated."""
    x, k = _xk(x, k)
    _order(d)
    return F(16**k, x**d)*sum((F(1,16**j)*sum((F(w,8)*(p-j)**d/(x+j-p)
             for w,p in POLES), F(0)) for j in range(1,k+1)), F(0))


def scaled_derivatives(x: int | F, k: int, d: int) -> tuple[F,F,F]:
    """R, R', R'' divided by 16**k, all exact rational at real positive x."""
    x,k=_xk(x,k)
    _order(d)
    terms=[F(0),F(0),F(0)]
    for j in range(1,k+1):
        for w,p in POLES:
            u=x+j-p
            amp=F(w,8)*(p-j)**d/16**j
            terms[0]+=amp/u
            terms[1]-=amp/u**2
            terms[2]+=2*amp/u**3
    v=terms[0]/x**d
    d1=-d*terms[0]/x**(d+1)+terms[1]/x**d
    d2=d*(d+1)*terms[0]/x**(d+2)-2*d*terms[1]/x**(d+1)+terms[2]/x**d
    return v,d1,d2


def derivative_certificate(x: int | F, k: int, d: int) -> dict:
    """Exact all-x envelope checks at the selected rational witness x."""
    x,k=_xk(x,k);_order(d)
    v,one,two=scaled_derivatives(x,k,d)
    c=finite_leading(k,d)
    m=moment(d+1)
    return {
        'value_error': abs(v-c/x**(d+1)),
        'value_bound': m/x**(d+2),
        'first_error':abs(one+(d+1)*c/x**(d+2)),
        'first_bound': (d+2)*m/x**(d+3),
        'second_error':abs(two-(d+1)*(d+2)*c/x**(d+3)),
        'second_bound':(d+2)*(d+3)*m/x**(d+4),
    }


def limiting_profile(d: int, c: F) -> tuple[F,F,F]:
    """Ratio a, reduced-lag limit 2a-a^2, coherent transport gap (1-a)^2."""
    _order(d)
    if type(c) not in (int,F) or not d+1 < F(c) < d+2:
        raise ValueError('requires d+1 < clock coefficient c < d+2')
    a=F(d+1,c)
    return (a, 2*a-a*a, (1-a)**2)


def mutation_fails_source_contract(n: int, k: int, d: int, strength: F=F(1,100)) -> bool:
    """Positive nonauthentic forcing +strength/(n+j)^2 violates original envelope."""
    n,k=_xk(n,k);_order(d)
    if strength<=0: raise ValueError('positive mutation required')
    mutant=true_source_lag(n,k)+sum((16**(k-j)*strength/(n+j)**2 for j in range(1,k+1)),F(0))
    return abs(mutant-corrected_lag(n,k,d)) > F(16**k, n**(d+1))*moment(d)
