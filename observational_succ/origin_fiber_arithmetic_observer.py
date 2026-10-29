"""Arithmetic source-/observer-typed factor fibers, exact finite core.

H_n=span{|a,b>:ab=n}; J|n>=d(n)^(-1/2) sum_ab=n|a,b>.
A_p raises first factor: (a,b)->(pa,b).  T_A increments first factor:
(a,b)->(a+1,b).  Their full pair-space action is an isometry, but
origin-locked compression C(X)=J^* X J need not preserve composition.

Use rational SQUARED amplitudes to avoid falsely treating square roots as
rational.  An independent SymPy oracle checks the actual amplitudes.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt


def divisors(n):
    if type(n) is not int or n<1:
        raise ValueError('positive source index required')
    d=[]
    for k in range(1,isqrt(n)+1):
        if n%k==0:
            d.append(k)
            if k*k!=n: d.append(n//k)
    return tuple(sorted(d))


def d(n):
    return len(divisors(n))


def pair_space(n):
    return tuple((a,n//a) for a in divisors(n))


def first_channel_additive(a,b):
    if type(a) is not int or type(b) is not int or min(a,b)<1:
        raise ValueError('positive pair indices')
    return a+1,b


def first_channel_prime(a,b,p):
    if type(p) is not int or p<2:
        raise ValueError('genuine prime validation required externally')
    return p*a,b


def compressed_channel_additive_sq(n):
    """Squared coefficients of C(S_A)|n>=sum_{b|n} |n+b>/sqrt(d(n)d(n+b)).

    Source targets n+b are distinct for distinct b.  These are *squared*
    amplitudes, not probabilities unless the observer measurement/collapse
    protocol is declared.  Coherent image has subunit basis norm.
    """
    return {n+b:F(1,d(n)*d(n+b)) for b in divisors(n)}


def compressed_channel_additive_sqnorm(n):
    return sum(compressed_channel_additive_sq(n).values(),F(0))


def nearest_successor_overlap_sq(n):
    """Squared coefficient of |n+1> in C(S_A)|n>."""
    return F(1,d(n)*d(n+1))


def compressed_channel_prime_overlap_sq(n,p):
    if type(p) is not int or p<2 or divisors(p)!=(1,p):
        raise ValueError('genuine prime required')
    def exponent(n,p):
        j=0
        while n%p==0:
            n//=p;j+=1
        return j
    j=exponent(n,p)
    return F(j+1,j+2)


def source_carry_difference_times_sq(n,signed_phase):
    """Diagnostic from exact compressed [M_h,S_A] observation.

    Returns sum_{b|n} |f(n+b)-f(n)|^2/(d(n)d(n+b)),
    where f(t) is an AUTHOR-DECLARED complex phase of the ORIGINAL source,
    NOT a new random digit law. signed_phase(t) is supplied explicitly.
    Numerical output is not a rigorous interval proof.
    """
    if type(n) is not int or n<1:
        raise ValueError('positive n required')
    z=signed_phase(n)
    if not isinstance(z,complex):
        raise TypeError('callable must return complex')
    return sum((float(weight)*abs(signed_phase(m)-z)**2
                for m,weight in compressed_channel_additive_sq(n).items()),0.0)


def simple_nonfunctoriality_defect_sq():
    """For |1>,  C(S_A A_2)-C(S_A) C(A_2) has norm^2=5/24.

    Literal first-channel operations are S_A(a,b)=(a+1,b), A_2(a,b)=(2a,b).
    C is J^*...J with uniform coherent divisor fibers.
    The channel product DOES satisfy its affine braid on full pair space;
    the intermediate compression introduces a nonzero defect.
    """
    return F(5,24)


def su2_j3(j,k):
    if type(j) is not int or j<0 or type(k) is not int or not 0<=k<=j:
        raise ValueError('source exponent j and split k required')
    return F(2*k-j,2)


def su2_ladder_plus_sq(j,k):
    su2_j3(j,k)
    return (k+1)*(j-k)


def su2_ladder_minus_sq(j,k):
    su2_j3(j,k)
    return k*(j-k+1)


def su2_raising_lowering_commutator(j,k):
    su2_j3(j,k)
    return F(su2_ladder_minus_sq(j,k)-su2_ladder_plus_sq(j,k))


def su2_casimir(j,k):
    """(J+J- + J-J+)/2 + J3^2; eigenvalue j(j+2)/4."""
    m=su2_j3(j,k)
    return F(su2_ladder_minus_sq(j,k)+su2_ladder_plus_sq(j,k),2)+m*m


def uniform_split_j3_variance(j):
    if type(j) is not int or j<0:
        raise ValueError('j>=0')
    return F(j*(j+2),12)


def uniform_split_imbalance_variance_coefficient(j):
    """Var[log(a/b) | ab=p^j] / (log p)^2; exact rational."""
    return 4*uniform_split_j3_variance(j)
