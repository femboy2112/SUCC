"""Zero-reading-free, exact rational analytic *error budget* for complex theta.

This DOES NOT evaluate the Simpson sample values or certify their rounding.
It bounds the remainder once original theta sample enclosures are supplied.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial

class SimpsonBoundError(ValueError):pass

def e3_positive_witness():
    """Exact rational positivity establishing e^3 > 20."""
    return sum((Q(3**k,factorial(k)) for k in range(9)),Q())-20


def theta_d4_uniform_majorant():
    """Upper source bound for |d^4_t[psi(t)t^-3/4 cosh(z logt/2)]|.

    For t>=1, |Re z|<=1, |Im z|<=16; use pi<4, pi>3,
    |alpha|<9, exp(-3)<1/20; ratio majorant for n>=2.
    """
    assert e3_positive_witness()>0
    ratio=Q(3,2)**8/400
    return Q(16**4,20)+16**4*Q(2**8,400**2)/(1-ratio)


def simpson_component_bound(M:int):
    """Worst-case error in EACH real/imag component on t=[1,8].

    Composite Simpson M even equal cells, h=7/M, with sup |f''''|<3500.
    """
    if type(M) is not int or M<2 or M%2:
        raise SimpsonBoundError('even positive integer subinterval count required')
    assert theta_d4_uniform_majorant()<3500
    return Q(3500*7**5,180*M**4)


def theta_t8_analytic_tail():
    """Entire original theta tail bound, t>=8, BOTH cosine directions.

    For |Re z|<=1, t^(-3/4+|Re z|/2)<=1; pi>3 and
    exp(-3)<1/20 give sum_n exp(-24 n^2)/(3n^2).
    """
    p=Q(1,20**8)
    return p/(3*(1-p))


def original_xi_complex_remainder(M:int):
    """Rational ABSOLUTE Xi error given exact Simpson node evaluations.

    Domain |Re z|<=1, |Im z|<=16, F(z)=xi(1/2+z),
    F=1/2+(z^2-1/4) B(z). The error covers finite Simpson quadrature
    and t>=8 on the FULL original theta, not node rounding / mode truncation.
    """
    each=simpson_component_bound(M)+theta_t8_analytic_tail()
    return Q(1029,2)*each  # 2*(257+1/4) per-component bound
