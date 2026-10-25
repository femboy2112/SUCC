"""Exact Haar and finite-grid initial-selector source-ensemble controls.

Never promote source-ensemble bounds to selected BBP y0=0 cancellation.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt
from .pi_dyadic_prime_transfer import _bbp_states, _bbp_forcing, _centered
from .pascal_carry_interferometry import walsh_moments


def _prime(q: int) -> int:
    if type(q) is not int or q < 3 or q % 2 == 0 or any(q % k == 0 for k in range(3,isqrt(q)+1,2)):
        raise ValueError('odd prime sampling modulus required')
    return q


def order16(q: int) -> int:
    _prime(q)
    u=16%q
    period=1
    while u!=1:
        u=u*16%q
        period+=1
    return period


def haar_initial_selector_expectation(D: int, tau: Q) -> dict:
    """For any real additive deterministic forcing: exact Haar means.

    Integrate the forcing-driven radix16 orbit over x0 Haar, not over time.
    The selected x0=0 is a single zero-measure member; none of these
    statements give π-normality or the desired selected all-scale estimate.
    """
    if type(D) is not int or D < 1 or not (Q(0)<Q(tau)<=Q(1,4)):
        raise ValueError('D>=1, 0<tau<=1/4 required')
    tau=Q(tau)
    off=D*(D-1)
    q0=Q(D)+2*tau*off
    zero=Q(D)+tau*off/8
    assert 16*zero-q0==15*D
    return {'D':D,'tau':str(tau),'mean_Q0':str(q0),'mean_zero':str(zero),
            'mean_16Z_minus_Q0':15*D,
            'mean_nonempty_walsh_moment':D,
            'mean_primitive_shells':[D,2*D,4*D,8*D],
            'source_selector':'Haar average over all x0, NOT selected pi y0=0'}


def finite_grid_initial_selector_probe(source_last: int, indices: tuple[int,...],
                                       q: int,tau: Q) -> dict:
    """Exact enumeration of all initial j/q, with genuine BBP r(n).

    For every pair of distinct times the phase difference under x0=j/q
    cycles through a complete shifted Q-grid iff ord_q(16)>max lag.
    This yields |ensemble(16Z-Q0)-15D| <= 64 D(D-1)/q.
    Endpoint-inclusive arcs use the safe <=2/q per inverse branch.
    """
    _prime(q)
    if type(source_last) is not int or source_last < 1:
        raise ValueError('source_last integer >=1 required')
    if not indices or any(type(i) is not int or i<1 or i+1>source_last for i in indices):
        raise ValueError('indices must have certified source successors')
    if tuple(sorted(set(indices)))!=indices:
        raise ValueError('strictly increasing time indices required')
    tau=Q(tau)
    if not Q(0)<tau<=Q(1,4):
        raise ValueError('0<tau<=1/4 required')
    D=len(indices)
    period=order16(q)
    if period <= indices[-1]-indices[0]:
        raise ValueError('q clock does not separate all pair lag multipliers')
    zero=_bbp_states(source_last)
    powers={n:pow(16,n,q) for n in set(indices)|{i+1 for i in indices}}
    total_q0=0
    total_zero=0
    total_hist=[0]*16
    for j in range(q):
        shifted={n:(zero[n]+Q(j*powers[n],q))%1 for n in powers}
        for s in indices:
            for t in indices:
                d=_centered(shifted[t]-shifted[s])
                d_plus=_centered(shifted[t+1]-shifted[s+1])
                if abs(d_plus)>tau:
                    continue
                carry=16*d+_bbp_forcing(t+1)-_bbp_forcing(s+1)-d_plus
                if carry.denominator!=1:
                    raise AssertionError('source-centered integer carry lost')
                total_hist[int(carry)%16]+=1
                total_q0+=1
                total_zero+=(carry%16==0)
    moments=walsh_moments(total_hist)
    excess=Q(16*total_zero-total_q0,q)
    bound=Q(64*D*(D-1),q)
    assert abs(excess-15*D)<=bound
    return {'q':q,'order16':period,'D':D,'indices':list(indices),'tau':str(tau),
            'average_Q0':str(Q(total_q0,q)),'average_Z':str(Q(total_zero,q)),
            'average_signed_excess':str(excess),
            'Haar_signed_excess':15*D,
            'finite_grid_absolute_error':str(abs(excess-15*D)),
            'proved_grid_error_upper':str(bound),
            'average_walsh_moments':[str(Q(v,q)) for v in moments],
            'not_selected_source':True}
