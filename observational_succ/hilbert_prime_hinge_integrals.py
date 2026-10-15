"""Authentic Suzuki prime-power hinge CELL INTEGRALS, not midpoint samples.

Every original arithmetic prime contribution is
  w_n (|x-y|-log n)_+, w_n=log(p)/sqrt(n), n=p^r.
On a rational rectangle the positive hinge is a 4-corner finite difference
of t_+^3/6. Monotonicity in b=log n yields exact OUTWARD RATIONAL
source enclosures without *any* kink-crossing spatial quadrature error.

This certifies only the genuine PRIME PART of the full signed g_J.
The Gamma/contact/poles, high/low Schur resolvent and all-test sign are
NOT computed or asserted here. Main source: source_weil_hierarchy.py.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

from . import source_weil_hierarchy as source
from .hilbert_carrier import order_gate,point

class HilbertHingeError(ValueError):
    pass

def rat(x):
    if type(x) not in (int,Q):
        raise HilbertHingeError("exact rational arithmetic required")
    return Q(x)

def _plus_cubed(z):
    z=rat(z)
    return max(Q(),z)**3

def oriented_hinge_rect(x0,x1,y0,y1,threshold):
    """EXACT double integral of (x-y-b)_+ over rectangle.

    Formula from two integrations of truncated power:
      [(x1-y0-b)_+^3 -(x0-y0-b)_+^3
       -(x1-y1-b)_+^3 +(x0-y1-b)_+^3]/6
    """
    x0,x1,y0,y1,b=map(rat,(x0,x1,y0,y1,threshold))
    if not (x0<x1 and y0<y1 and b>=0):
        raise HilbertHingeError("positive-area rectangle and nonnegative hinge")
    value=(_plus_cubed(x1-y0-b)-_plus_cubed(x0-y0-b)
           -_plus_cubed(x1-y1-b)+_plus_cubed(x0-y1-b))/6
    if value<0:raise ArithmeticError("source hinge integral negative")
    return value

def absolute_hinge_rect(x0,x1,y0,y1,threshold):
    """EXACT original (|x-y|-b)_+ by two opposite directed hinges."""
    return (oriented_hinge_rect(x0,x1,y0,y1,threshold)
            +oriented_hinge_rect(y0,y1,x0,x1,threshold))

def source_rect(a,order,ix,iy):
    a=rat(a)
    k=order_gate(order)
    if not 0<a<=1:
        raise HilbertHingeError("first original Suzuki radius 0<a<=1")
    side=1<<k
    if any(type(x) is not int or not 0<=x<side for x in (ix,iy)):
        raise HilbertHingeError("original source rational grid indices")
    h=2*a/side
    return (-a+ix*h,-a+(ix+1)*h,-a+iy*h,-a+(iy+1)*h)

@dataclass(frozen=True)
class OriginalHingeCertificate:
    original_source:str
    radius:Q
    order:int
    ix:int
    iy:int
    n:int
    prime:int
    lower:Q
    upper:Q
    rectangle_area:Q
    midpoint_sampling_used:bool=False
    all_complete_weil_terms_included:bool=False
    signed_operator_positive_proved:bool=False

def authenticated_hinge_cell(a,order,ix,iy,n):
    """Exact outward interval of THE GENUINE weighted source hinge cell."""
    a=rat(a)
    k=order_gate(order)
    if k>6:raise HilbertHingeError("certified source cell cap order<=6")
    if type(n) is not int:
        raise HilbertHingeError("real prime-power index must be integer")
    original_tape=source.authenticated_prime_wavefront(a)
    found=[p for m,p in original_tape if m==n]
    if len(found)!=1:
        raise HilbertHingeError("independent fake 6, absent or out-of-window prime")
    p=found[0]
    original_box=source_rect(a,k,ix,iy)
    ell=source.log_iv(n)
    weight=source.log_iv(p)*source.sqrt_inverse(n)
    if weight.lo<=0:
        raise HilbertHingeError("original prime coefficient not certified positive")
    # The unweighted entire rectangle hinge decreases monotonically in b.
    area_lo=absolute_hinge_rect(*original_box,ell.hi)
    area_hi=absolute_hinge_rect(*original_box,ell.lo)
    if not 0<=area_lo<=area_hi:
        raise ArithmeticError("exact source hinge interval monotonicity failed")
    result=weight*source.I(area_lo,area_hi)
    h=2*a/(1<<k)
    return OriginalHingeCertificate(
        original_source="AUTHENTIC_Q_ZETA_PRIME_POWER_HALF_DENSITY",
        radius=a,order=k,ix=ix,iy=iy,n=n,prime=p,
        lower=result.lo,upper=result.hi,rectangle_area=h*h)

def original_prime_cell_sum(a,order,ix,iy):
    """THE ENTIRE TRUE prime hinge contribution for one cell, no Gamma."""
    a=rat(a)
    k=order_gate(order)
    if k>6:raise HilbertHingeError("source budget")
    atoms=source.authenticated_prime_wavefront(a)
    h=2*a/(1<<k)
    total=source.I(Q(),Q())
    for n,p in atoms:
        part=authenticated_hinge_cell(a,k,ix,iy,n)
        total+=source.I(part.lower,part.upper)
    return {
       "original_source":"AUTHENTIC_ZETA_COMPACT_PRIME_POWER_HINGES",
       "radius":a,"order":k,"cell":(ix,iy),
       "prime_power_atoms":atoms,
       "original_normalized_cell_matrix_lower":total.lo/h,
       "original_normalized_cell_matrix_upper":total.hi/h,
       "center_point_quadrature_used":False,
       "prime_hinge_spatial_error":Q(),
       "full_signed_Gamma_pole_contact_included":False,
       "positive_complete_Weil_form_proved":False,
    }

def hilbert_prime_cell_stream(a,order):
    """Hilbert-order ORIGINAL PRIME-ONLY compressed operator block intervals.

    Every matrix pair is visited exactly once, preserved under original
    row/col labels. Zero hinge spatial interpolation error; uncertainty
    remains only in independently enclosed log/sqrt constants.
    """
    a=rat(a);k=order_gate(order)
    if k>4:raise HilbertHingeError("all-cell source stream budget order<=4")
    entries=[]
    for d in range(4**k):
        ix,iy=point(k,d)
        v=original_prime_cell_sum(a,k,ix,iy)
        entries.append((ix,iy,v["original_normalized_cell_matrix_lower"],
                        v["original_normalized_cell_matrix_upper"]))
    N=1<<k
    low=[[None]*N for _ in range(N)]
    high=[[None]*N for _ in range(N)]
    for i,j,l,r in entries:
        low[i][j]=l
        high[i][j]=r
    if (any(any(v is None for v in row) for row in low+high)
        or any(low[i][j]!=low[j][i] or high[i][j]!=high[j][i]
               for i in range(N) for j in range(N))):
        raise ArithmeticError("original prime integral source symmetry/coverage failure")
    return {
        "original_source":"AUTHENTIC_Q_ZETA_PRIME_POWER_HALF_DENSITY",
        "radius":a,"Hilbert_order":k,
        "genuine_prime_powers":source.authenticated_prime_wavefront(a),
        "Hilbert_order_entries":tuple(entries),
        "all_original_pair_cells_visited":len(entries)==N*N,
        "source_interval_symmetric":True,
        "prime_hinge_spatial_quadrature_error":Q(),
        "full_original_signed_Weil_matrix_constructed":False,
        "global_positive_form_proved":False,
        "rh_proved":False,
    }
