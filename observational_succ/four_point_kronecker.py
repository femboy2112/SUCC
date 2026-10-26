"""Kronecker / golden elliptic numeric diagnostics with explicit authority labels.

The first Kronecker limit formula is a CLASSICAL ANALYTIC THEOREM, not proved
by these finite mpmath calculations. No spectral phase bound or pi normality.
"""
from __future__ import annotations

from contextlib import contextmanager
from fractions import Fraction as Q
import mpmath as mp

from .seinfeld_four_point import Golden, LAMBDA_GOLD


@contextmanager
def workdps(dps):
    if type(dps) is not int or not 30<=dps<=150:
        raise ValueError('30..150 mpmath decimal digits')
    with mp.workdps(dps):
        yield


def exact_real_to_mp(value):
    if isinstance(value, Golden):
        return (mp.mpf(value.a.numerator)/value.a.denominator +
                (mp.sqrt(5)-1)/2*mp.mpf(value.b.numerator)/value.b.denominator)
    if type(value) in (int,Q):
        v=Q(value)
        return mp.mpf(v.numerator)/v.denominator
    if isinstance(value, str):
        return mp.mpf(value)
    raise TypeError('exact rational, Golden element, or decimal string only')


def imaginary_period(lambda_value, dps=70):
    """For 0<λ<1: τ=i*K(1−λ)/K(λ) with K(m) parameter m."""
    with workdps(dps):
        v=exact_real_to_mp(lambda_value)
        if not 0<v<1:
            raise ValueError('nondegenerate real Legendre four-point parameter')
        return + (mp.ellipk(1-v)/mp.ellipk(v))


def eta_imaginary(y, terms=80):
    """Numerically truncated eta product; no analytic error certificate here."""
    if type(terms) is not int or not 8<=terms<=1000:
        raise ValueError('declared product truncation')
    y=mp.mpf(y)
    if y<=0:raise ValueError('positive imaginary period required')
    q=mp.exp(-2*mp.pi*y)
    return mp.exp(-mp.pi*y/12)*mp.fprod(1-q**n for n in range(1,terms+1))


def kronecker_finite_part(y,terms=80):
    """CLASSICAL FORMULA evaluated numerically. FP_{s=1} Z(iy,s)."""
    y=mp.mpf(y)
    eta=eta_imaginary(y,terms)
    return 2*mp.pi*(mp.euler-mp.log(2)-mp.log(mp.sqrt(y)*eta**2))


def epstein_poisson(y,s,terms=12):
    """Independent convergent Poisson/Bessel expansion for Re(s)>1.

    The truncation is a numerical consistency check, not outward interval
    arithmetic. Terms are omitted only at their exponentially small tails.
    """
    if type(terms) is not int or not 4<=terms<=40:
        raise ValueError('bounded independent check')
    y=mp.mpf(y);s=mp.mpf(s)
    if y<=0 or s<=1:raise ValueError('positive y and real s>1')
    first=2*mp.zeta(2*s)*y**s
    second=(2*mp.sqrt(mp.pi)*mp.gamma(s-mp.mpf('.5'))/mp.gamma(s)
            *mp.zeta(2*s-1)*y**(1-s))
    tail=8*mp.pi**s/mp.gamma(s)*mp.sqrt(y)*mp.fsum(
        (mp.mpf(n)/m)**(s-mp.mpf('.5'))*mp.besselk(s-mp.mpf('.5'),2*mp.pi*n*m*y)
        for m in range(1,terms+1) for n in range(1,terms+1))
    return first+second+tail


def cusp_remainder(y,terms=80):
    """R(y)-2pi(gamma-log2) >0, with a PROVED simple analytic cap.

    The expression is computed by an eta product for diagnostic purposes;
    the inequality is proved analytically in the adjacent dossier.
    """
    y=mp.mpf(y)
    if y<=0:raise ValueError('positive y')
    fp=kronecker_finite_part(y,terms)
    corrected=fp-mp.pi**2*y/3+mp.pi*mp.log(y)
    target=2*mp.pi*(mp.euler-mp.log(2))
    q=mp.exp(-2*mp.pi*y)
    bound=4*mp.pi*q/(1-q)**2
    return {'y':y,'cusp_regularized':corrected,'limit':target,
            'positive_difference':corrected-target,'explicit_upper':bound,
            'numerical_not_proof':True}


def golden_signature(dps=70,terms=100):
    """Distinct geometric, renormalization, and arbitrary golden-reference data."""
    with workdps(dps):
        lam=exact_real_to_mp(LAMBDA_GOLD)
        y=imaginary_period(LAMBDA_GOLD,dps)
        eta=eta_imaginary(y,terms)
        eta_square=eta_imaginary(1,terms)
        shape=mp.log(mp.sqrt(y)*eta**2)
        square_shape=mp.log(eta_square**2)
        fp=kronecker_finite_part(y,terms)
        golden_diff=lam-mp.euler
        return {k:+v for k,v in {
            'lambda':lam,'period_y':y,'eta':eta,'log_shape':shape,
            'kronecker_finite_part':fp,
            'square_reference_difference':-2*mp.pi*(shape-square_shape),
            'gamma_subtracted_from_lambda':golden_diff,
            'j_exact_numerically':mp.mpf(2048),
        }.items()} | {'numerical_not_proof':True,'normality_proved':False}
