"""Exact genuine prime-power / Archimedean Gamma OU endpoint phase lock.

At a source wavefront b_n=log n, the TRUE j-th Gamma damping rate
alpha_j=(4j+1)/2 has exp(-alpha_j*b_n)=n^(-2j-1/2).
When a SOURCE-DERIVED product with the genuine prime coefficient
Lambda(n)/sqrt(n) occurs, the two half densities combine to n^(-2j-1).
These are algebraic identities, NOT a source theorem that the different
Weil channels multiply or compensate each other, and NOT RH positivity.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt


class PhaseLockError(ValueError):
    pass


def prime_power_parent(n):
    if type(n) is not int or n<2:
        raise PhaseLockError('genuine integer prime-power source required')
    for p in range(2,isqrt(n)+1):
        if any(p % q == 0 for q in range(2,isqrt(p)+1)):
            continue
        v=p
        while v<n:
            v*=p
        if v==n:
            return p
    if all(n%d for d in range(2,isqrt(n)+1)):
        return n
    raise PhaseLockError('composite non-prime-power (e.g. 6) has no new Euler impulse')


def phase_lock(n, gamma_index):
    """Returns exact rational part, symbolic 1/sqrt(n), true prime parent.

    No floats, logs, or analytic evaluations: e^-alpha log n is an exact
    algebraic radical. The combined half-density has an integral exponent.
    """
    p=prime_power_parent(n)
    if type(gamma_index) is not int or not 0<=gamma_index<=100000:
        raise PhaseLockError('genuine nonnegative Gamma ladder index required')
    j=gamma_index
    alpha=Q(4*j+1,2)
    return {'true_source_n':n,'prime_parent':p,'gamma_ou_decay_rate':alpha,
            'e_minus_alpha_log_n':'n^(-2j-1/2)',
            'exact_rational_times_inv_sqrt_n':Q(1,n**(2*j)),
            'original_euler_half_density':'1/sqrt(n)',
            'product_with_prime_weight':'log(p)/n^(2j+1)',
            'resulting_exact_rational_log_p_multiplier':Q(1,n**(2*j+1)),
            'source_product_not_assumed':True,'RH_proved':False}


def source_verified_phase_lock(n, gamma_index):
    """Read frozen actual source tape, reject synthetic and unlisted impulses.

    AUTHENTIC_TAPE currently enumerates n<=8 because the certified source
    wavefront API is scoped to 0<a<=1. This cannot assert all n tested.
    """
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .source_weil_hierarchy import AUTHENTIC_TAPE
    original=verify_original_suzuki_source()
    item=phase_lock(n,gamma_index)
    if (n,item['prime_parent']) not in AUTHENTIC_TAPE:
        raise PhaseLockError('impulse outside actual frozen original source tape')
    return dict(item,source_verified=True,source_receipt=original)
