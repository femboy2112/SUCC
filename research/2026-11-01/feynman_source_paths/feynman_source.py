"""Exact finite SUCC/BBP affine source and certificates for a rigorous Feynman lift.

The analytic quantum propagator and Fresnel distributions are PROVED in PROOFS.md.
Tests here certify finite rational source/cocycle, stationary path equations,
Gaussian covariance and the bounds' exact rational coefficient identities.
No numerical experiment establishes a continuum path integral or pi normality.
"""
from __future__ import annotations
from fractions import Fraction
from dataclasses import dataclass

BASE = 16


def source(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('n must be a positive integer')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def source_combined(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('positive integer index required')
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def orbit(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    if type(n) is not int or n < 0 or not isinstance(seed, Fraction):
        raise ValueError('nonnegative index and rational seed required')
    value = seed
    for j in range(1, n+1):
        value = BASE*value + source(j)
    return value


def affine_product(n: int) -> tuple[int, Fraction]:
    """Matrix F_n ... F_1 encoded as (slope, translation)."""
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative horizon')
    m, b = 1, Fraction(0)
    for j in range(1, n+1):
        m, b = BASE*m, BASE*b+source(j)
    return m, b


def weighted_action(n: int) -> Fraction:
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative horizon')
    return sum((source(j)/BASE**j for j in range(1,n+1)), Fraction(0))


def variance_clock(n: int) -> int:
    """C_N=sum_{j=0}^{N-1}16^(2j), exact Gaussian/Fresnel covariance."""
    if type(n) is not int or n < 1:
        raise ValueError('positive horizon')
    return (BASE**(2*n)-1)//(BASE**2-1)


def variance_clock_recursive(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError('positive horizon')
    c = 0
    for _ in range(n):
        c = BASE*BASE*c + 1
    return c


def stationary_path(n: int, initial: Fraction, final: Fraction,
                    epsilon: Fraction) -> tuple[tuple[Fraction,...],tuple[Fraction,...]]:
    """Unique stationary path of S=sum p_j(x_j-16x_(j-1)-r_j)-eps*p_j^2/2.

    All calculations are exact rationals. eps must be positive; eps=0 is a
    distributional delta constraint, not a regular stationary boundary problem.
    """
    if (type(n) is not int or n < 1 or not isinstance(initial,Fraction)
        or not isinstance(final,Fraction) or not isinstance(epsilon,Fraction)
        or epsilon <= 0):
        raise ValueError('positive finite n/epsilon and exact rational endpoints')
    delta = final - BASE**n*initial - orbit(n)
    p_final = delta / (epsilon*variance_clock(n))
    p = tuple(BASE**(n-j)*p_final for j in range(1,n+1))
    x = [initial]
    for j in range(1,n+1):
        x.append(BASE*x[-1] + source(j) + epsilon*p[j-1])
    assert x[-1] == final
    return tuple(x), p


def stationary_action(n: int, initial: Fraction, final: Fraction,
                      epsilon: Fraction) -> Fraction:
    x,p=stationary_path(n,initial,final,epsilon)
    result=sum((p[j-1]*(x[j]-BASE*x[j-1]-source(j))
                -epsilon*p[j-1]*p[j-1]/2 for j in range(1,n+1)),Fraction(0))
    delta=final-BASE**n*initial-orbit(n)
    assert result==delta*delta/(2*epsilon*variance_clock(n))
    return result


def exact_fourier_fresnel_phase(n:int, k:Fraction,
                                epsilon:Fraction, hbar:Fraction=Fraction(1)) -> Fraction:
    """Dimensionless exponent coefficient -eps*hbar*C_N*k²/2.
    Fourier-space kernel =16^(N/2)*e^(-ik(16^N x+U_N))*e^(i*returned).
    """
    if not isinstance(k,Fraction) or not isinstance(epsilon,Fraction) or epsilon<=0:
        raise ValueError('rational wavenumber and positive epsilon')
    if not isinstance(hbar,Fraction) or hbar<=0:
        raise ValueError('positive chosen action scale')
    return -epsilon*hbar*variance_clock(n)*k*k/2


def bandlimited_error_bound(n:int,epsilon:Fraction,hbar:Fraction,K:Fraction) -> Fraction:
    """Operator norm bound from |e^(i t)-1|<=|t| on input Fourier support |k|<=K."""
    if not isinstance(K,Fraction) or K<0 or not isinstance(epsilon,Fraction) or epsilon<0:
        raise ValueError('nonnegative rational data')
    if not isinstance(hbar,Fraction) or hbar<=0:
        raise ValueError('positive hbar')
    return epsilon*hbar*K*K*Fraction(variance_clock(n),2*BASE**(2*n))


def uniform_bandlimited_bound(epsilon:Fraction,hbar:Fraction,K:Fraction) -> Fraction:
    if not isinstance(epsilon,Fraction) or epsilon<0 or not isinstance(K,Fraction) or K<0 or not isinstance(hbar,Fraction) or hbar<=0:
        raise ValueError('nonnegative epsilon/K and positive scale')
    return epsilon*hbar*K*K/Fraction(2*(BASE**2-1))


def gaussian_phase_attenuation_exponent(n: int, h: int, sigma: Fraction) -> Fraction:
    """e(hU_n) exp(returned) for a normalized point-centered Gaussian input.
    The exponent includes the literal pi² symbol: output is rational
    coefficient multiplying pi²; exp(-2*pi²*h²*(16^n sigma)²).
    """
    if type(h) is not int or not isinstance(sigma,Fraction) or sigma<=0:
        raise ValueError('integer h and positive rational width')
    return -2*Fraction(h*h)*BASE**(2*n)*sigma*sigma


def heat_point_character_attenuation_exponent(n: int, h: int, epsilon: Fraction,
                                             hbar: Fraction = Fraction(1)) -> Fraction:
    """For POINT initial data and the SEPARATE positive Gaussian/Wick partner.

    Its character is e(h(16^n x0 + U_n))*exp(pi²*returned),
    with returned=-2*h²*epsilon*hbar*C_n. NOT the quantum Fresnel amplitude.
    """
    if type(h) is not int or not isinstance(epsilon,Fraction) or epsilon<0:
        raise ValueError('integer harmonic and nonnegative rational regulator')
    if not isinstance(hbar,Fraction) or hbar<=0:
        raise ValueError('positive action scale')
    return -2*Fraction(h*h)*epsilon*hbar*variance_clock(n)

def two_order_offset() -> Fraction:
    """d_(F2F1)-d_(F1F2) for exact first two source steps."""
    return Fraction(BASE-1)*(source(1)-source(2))


def two_order_gaussian_overlap_exponent(sigma: Fraction) -> Fraction:
    """Overlap magnitude exp(returned), with initial Gaussian std sigma.
    Difference between final packet centers is two_order_offset(),
    and final packet standard deviation is BASE²*sigma.
    """
    if not isinstance(sigma,Fraction) or sigma<=0:
        raise ValueError('positive rational sigma')
    return -(two_order_offset()**2)/(8*BASE**4*sigma*sigma)


def two_order_momentum_phase_coefficient(p0:Fraction,hbar:Fraction=Fraction(1)) -> Fraction:
    """Angle coefficient in <order12|order21>: -p0*Delta/(16² hbar)."""
    if not isinstance(p0,Fraction) or not isinstance(hbar,Fraction) or hbar<=0:
        raise ValueError('rational momentum and positive hbar')
    return -p0*two_order_offset()/(BASE**2*hbar)


def source_tail_bound(n:int)->Fraction:
    """For n>=1, T_n=sum_{j>=1}16^-j r(n+j) <1/(64 n²)."""
    if type(n) is not int or n<1:
        raise ValueError('positive integer n')
    return Fraction(1,64*n*n)


def counterfeit_point_mod_one(n:int, tail_terms:int=30)->Fraction:
    """Finite rational enclosing approximation to {16^n/5-T_n}, NOT selected pi.
    Rational q=1/5, 16^n/5 has real residue 1/5.
    """
    if type(n) is not int or n<1 or type(tail_terms) is not int or tail_terms<1:
        raise ValueError('positive integers')
    tail = sum((source(n+j)/BASE**j for j in range(1,tail_terms+1)),Fraction(0))
    return Fraction(1,5)-tail
