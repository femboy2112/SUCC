"""Exact finite certificates for a chosen Farey/Gauss–Euler SUCC pairing.

Source-typed objects: golden continued-fraction periodic orbit and Gauss
invariant digit tails. Their difference is declared, not an intrinsic metric.
The source-independent calculation does NOT prove pi normality.
"""
from __future__ import annotations

from fractions import Fraction as Q


def golden_path(n: int) -> Q:
    """First n applications of f(x)=1/(1+x), starting x_0=0."""
    if type(n) is not int or not 0 <= n <= 100000:
        raise ValueError("n must be integer in [0,100000]")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return Q(a, b)


def golden_interval(n: int) -> tuple[Q, Q]:
    """Adjacent Fibonacci/Farey convergents bracket 1/phi."""
    if type(n) is not int or n < 1:
        raise ValueError("positive n required")
    a,b = golden_path(n), golden_path(n+1)
    if abs(a.numerator*b.denominator-b.numerator*a.denominator) != 1:
        raise ArithmeticError("Farey determinant is not a unit")
    return min(a,b),max(a,b)


def _atanh_log_interval(x: Q, terms: int) -> tuple[Q,Q]:
    if not Q(1) <= x <= Q(2):
        raise ValueError("local log chart is [1,2]")
    z=(x-1)/(x+1)
    partial=Q()
    for j in range(terms):
        partial += Q(2)*z**(2*j+1)/(2*j+1)
    tail=Q(2)*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return partial,partial+tail


def log_integer_interval(n: int, terms: int=20) -> tuple[Q,Q]:
    """Rigorous rational bracket for natural log(n), no floating point."""
    if type(n) is not int or n<1 or type(terms) is not int or not 1<=terms<=100:
        raise ValueError("n positive integer and terms in [1,100] required")
    k=n.bit_length()-1
    scaled=Q(n,1<<k)
    L2,U2=_atanh_log_interval(Q(2),terms)
    Ly,Uy=_atanh_log_interval(scaled,terms)
    return k*L2+Ly,k*U2+Uy


def gamma_interval(n: int, terms: int=20) -> tuple[Q,Q]:
    """E_n < gamma < E_n + 1/(2n), E_n=H_n-log(n+1)."""
    if type(n) is not int or not 1<=n<=100000:
        raise ValueError("positive bounded n required")
    harmonic=sum((Q(1,k) for k in range(1,n+1)),Q())
    log_lo,log_hi=log_integer_interval(n+1,terms)
    return harmonic-log_hi,harmonic-log_lo+Q(1,2*n)


def oily_defect_interval(n: int, terms: int=20) -> tuple[Q,Q]:
    """A certified interval for 1/phi - gamma, with declared conventions."""
    lambda_lo,lambda_hi=golden_interval(n)
    gamma_lo,gamma_hi=gamma_interval(n,terms)
    return lambda_lo-gamma_hi,lambda_hi-gamma_lo


def gauss_digit_tail_interval(k: int, terms: int=20) -> tuple[Q,Q]:
    """Interval for log(2)*Gauss_mu(a>=k)=log(1+1/k)."""
    if type(k) is not int or k<1:
        raise ValueError("positive k required")
    return _atanh_log_interval(Q(k+1,k),terms)


def farey_mediant(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    """Neighbors (a/b,c/d) must have determinant ±1."""
    if any(type(x) is not int for x in (*a,*b)) or a[1]<0 or b[1]<0:
        raise ValueError("integer rational coordinates and nonnegative denominators")
    if abs(a[0]*b[1]-b[0]*a[1]) != 1:
        raise ValueError("non-neighbor source edges")
    return (a[0]+b[0],a[1]+b[1])
