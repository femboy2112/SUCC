"""Certified SIGNED BBP first-prime-window high-mode complex intervals.

Every angle is a rational circle state times genuine pi, with pi enclosed
independently by the Machin/arctan alternating series. Cos/sin are rational
Taylor enclosures, not a float pi input or digit sample. The results certify
finite source-selected high-mode interference, NOT asymptotic cancellation.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from math import factorial

from .bbp_prime_window_projection import (
    additive_clock_partition, source_complement_window,
)


def _natural(x,minimum=0):
    if type(x) is not int or x<minimum:
        raise ValueError("integer >= %d required" % minimum)
    return x


def _atan_rational_interval(denominator,terms):
    _natural(denominator,2)
    _natural(terms,1)
    total=sum((Q((-1)**j,(2*j+1)*denominator**(2*j+1))
               for j in range(terms)),Q())
    following=total+Q((-1)**terms,(2*terms+1)*denominator**(2*terms+1))
    return min(total,following),max(total,following)


def machin_pi_interval(terms=26):
    """Verified classical identity pi=16atan(1/5)-4atan(1/239)."""
    _natural(terms,1)
    return _machin_pi_cached(terms)


@lru_cache(None)
def _machin_pi_cached(terms):
    a,b=_atan_rational_interval(5,terms)
    c,d=_atan_rational_interval(239,terms)
    lo,hi=16*a-4*d,16*b-4*c
    assert Q(3)<lo<hi<Q(22,7)
    return lo,hi


def _box_add(first,second):
    return (first[0]+second[0],first[1]+second[1],
            first[2]+second[2],first[3]+second[3])


def _box_neg(box):
    return (-box[1],-box[0],-box[3],-box[2])


def _box_scale(box,scalar):
    scalar=Q(scalar)
    if scalar<0:return _box_neg(_box_scale(box,-scalar))
    return tuple(scalar*x for x in box)


def box_phase(exponent,terms=14,arctan_terms=26):
    """Rational rectangle for exp(2*pi*i*exponent), any exact rational.

    Taylor polynomials through degree 2*terms-1 have uniformly bounded
    derivative remainder <=(22/7)^(2*terms)/(2*terms)! for |angle|<=pi.
    Moving the Machin pi interval gives additive |z|*(hi-lo) error, where
    z is the rational exponent centered in [-1/2,1/2].
    """
    _natural(terms,1)
    _natural(arctan_terms,1)
    if type(exponent) not in (int,Q):
        raise ValueError("exact integer or Fraction character argument required")
    z=Q(exponent)%1
    if z>Q(1,2):z-=1
    pl,pu=machin_pi_interval(arctan_terms)
    mid=(pl+pu)/2
    angle=2*z*mid
    angle_sq=angle*angle
    cosval=Q()
    sinval=Q()
    cos_term=Q(1)
    sin_term=angle
    for j in range(terms):
        cosval+=cos_term
        sinval+=sin_term
        cos_term*=(-angle_sq)/Q((2*j+1)*(2*j+2))
        sin_term*=(-angle_sq)/Q((2*j+2)*(2*j+3))
    err=Q(22,7)**(2*terms)/factorial(2*terms)+abs(z)*(pu-pl)
    return (max(Q(-1),cosval-err),min(Q(1),cosval+err),
            max(Q(-1),sinval-err),min(Q(1),sinval+err))


def _box_sum(boxes,scalar):
    total=(Q(),Q(),Q(),Q())
    for box in boxes:
        total=_box_add(total,box)
    return _box_scale(total,scalar)


def _interval_distance_to_zero(lo,hi):
    if lo>0:return lo
    if hi<0:return -hi
    return Q()


def box_modulus_squared_interval(box):
    """Sound rational enclosure of squared complex absolute value."""
    rl,rh,il,ih=box
    lower=_interval_distance_to_zero(rl,rh)**2+_interval_distance_to_zero(il,ih)**2
    upper=max(rl*rl,rh*rh)+max(il*il,ih*ih)
    return lower,upper


def signed_prime_window_boxes(p,d,h=1,terms=14,arctan_terms=26):
    """Certified selected source W/Delta, low Q_d-part and high signed J.

    Uses the true p-primary splitting from the original BBP forcing and
    y0=0; d must divide Delta. All outputs have Fraction endpoints.
    Does not import independent sibling source modules or float pi.
    """
    data=additive_clock_partition(p,d,h)
    _natural(terms,1);_natural(arctan_terms,1)
    delta=data["delta"]
    if delta>60 or delta+delta*delta//d>320:
        raise ValueError("finite rational interval oracle exceeds declared cost cap")
    w=source_complement_window(p)
    a=[Q(4*h*pow(16,t,p),p) for t in range(delta)]
    full=_box_sum((box_phase(a[t]+h*w[t],terms,arctan_terms)
                   for t in range(delta)),Q(1,delta))
    K=delta//d
    low=_box_sum((box_phase(a[i]+h*w[j],terms,arctan_terms)
                  for r in range(d)
                  for i in range(r,delta,d)
                  for j in range(r,delta,d)),Q(1,d*K*K))
    high=_box_add(full,_box_neg(low))
    return {"full":full,"low":low,"high":high,
            "full_sq":box_modulus_squared_interval(full),
            "low_sq":box_modulus_squared_interval(low),
            "high_sq":box_modulus_squared_interval(high)}
