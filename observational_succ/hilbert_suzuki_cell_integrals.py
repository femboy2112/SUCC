"""Exact source-complete FINITE-J Suzuki kernel cell integrals with rational IA.

The original signed screw potential is:
 g_J(r)= -4(e^(r/2)+e^(-r/2)-2)
         + sum_(n=p^m) log(p)/sqrt(n) * (r-log(n))_+
         + r*C_G/2
         -4 sum_(j<J) [1-e^(-(4j+1)r/2)]/(4j+1)^2.

For any rational cell [x0,x1] x [y0,y1] all four components integrate
to closed elementary expressions; the only approximation is OUTWARD
transcendental enclosures in pi/log/exp/gamma/sqrt. The projection
matrix M_ij = 1/h * double_integral g_J(x-y) has ZERO spatial quadrature
error as a *finite compressed block*. Projecting a continuum operator
to finite cells still has a separate (nonzero) operator error. Positive
Gamma tail and all-test Weil sign are not inferred from this finite block.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

from . import source_weil_hierarchy as src
from .hilbert_carrier import point,order_gate
from .hilbert_prime_hinge_integrals import (
    rat,source_rect,absolute_hinge_rect,authenticated_hinge_cell,
    HilbertHingeError
)

class SuzukiCellIntegralError(ValueError):
    pass

def exponential_signed(t):
    t=rat(t)
    return src.exp_pos(t) if t>=0 else src.exp_neg(-t)

def _integrate_exp(coeff,lo,hi):
    coeff=rat(coeff);lo=rat(lo);hi=rat(hi)
    if hi<=lo:raise SuzukiCellIntegralError("true rational nonempty 1D interval")
    if coeff==0:return src.I(hi-lo,hi-lo)
    return (exponential_signed(coeff*hi)-exponential_signed(coeff*lo))/coeff

def genuine_pole_rect(rect):
    x0,x1,y0,y1=rect
    plus=_integrate_exp(Q(1,2),x0,x1)*_integrate_exp(Q(-1,2),y0,y1)
    minus=_integrate_exp(Q(-1,2),x0,x1)*_integrate_exp(Q(1,2),y0,y1)
    area=(x1-x0)*(y1-y0)
    return -4*(plus+minus-2*area)

def genuine_contact_rect(rect):
    x0,x1,y0,y1=rect
    abs_r=absolute_hinge_rect(x0,x1,y0,y1,0)
    return src.contact_iv()*Q(1,2)*abs_r

def _ou_primitive(t,alpha):
    """Second antiderivative of exp(-alpha*t) 1_{t>0}, fixed at 0."""
    t,alpha=rat(t),rat(alpha)
    if alpha<=0:raise SuzukiCellIntegralError("positive Gamma OU decay rate")
    if t<=0:return src.I(Q(),Q())
    return (src.exp_neg(alpha*t)-1+alpha*t)/(alpha*alpha)

def genuine_ou_rect(rect,alpha):
    """Rigorous integral of exp(-alpha |x-y|), INCLUDING x=y crossing.

    Two exact four-corner second-antiderivative integrals. Every bound
    uses parent source's outward rational transcendental intervals.
    """
    x0,x1,y0,y1=rect
    if not (x0<x1 and y0<y1):
        raise SuzukiCellIntegralError("nonzero original source rectangle")
    def orient(a0,a1,b0,b1):
        return (_ou_primitive(a1-b0,alpha)-_ou_primitive(a0-b0,alpha)
                -_ou_primitive(a1-b1,alpha)+_ou_primitive(a0-b1,alpha))
    result=orient(x0,x1,y0,y1)+orient(y0,y1,x0,x1)
    if result.hi<0:raise ArithmeticError("positive OU kernel integral impossible")
    return src.I(max(Q(),result.lo),max(Q(),result.hi))

def genuine_gamma_rect(rect,J):
    if type(J) is not int or not 1<=J<=36:
        raise SuzukiCellIntegralError("genuine finite Gamma source J 1..36")
    x0,x1,y0,y1=rect
    area=(x1-x0)*(y1-y0)
    total=src.I(Q(),Q())
    for j in range(J):
        d=4*j+1
        ou=genuine_ou_rect(rect,Q(d,2))
        total+=Q(-4,d*d)*(src.I(area,area)-ou)
    return total

@dataclass(frozen=True)
class AuthenticSuzukiCellBlock:
    source:str
    radius:Q
    order:int
    J:int
    spatial_cell:tuple[int,int]
    value_lower:Q
    value_upper:Q
    prime_power_source:tuple
    spatial_quadrature_error:Q=Q()
    original_full_Gamma_pole_contact:bool=True
    positive_full_weil_proved:bool=False

def full_source_cell(a,order,ix,iy,J):
    """TRUE finite-J original g_J source, projected exactly onto one cell pair."""
    a=rat(a);k=order_gate(order)
    if k>4 or not 0<a<=1:raise SuzukiCellIntegralError("certified finite-cell budget")
    if type(J) is not int or not 1<=J<=12:
        raise SuzukiCellIntegralError("original Gamma computational bound 1..12")
    # Validate BOTH original Cartesian source indices before changing basis.
    source_rect(a,k,ix,iy)
    # Original g_J(r) is exactly even and depends only on |x-y|.
    # Canonicalizing to lag before transcendental interval evaluation prevents
    # distinct yet mathematically equal absolute-coordinate formulas from
    # generating different outward endpoint widths via cancellation.
    rect=source_rect(a,k,abs(ix-iy),0)
    if src.assert_original_source_tape() is not True:
        raise SuzukiCellIntegralError("source prime tape drift")
    parts=[genuine_pole_rect(rect),genuine_contact_rect(rect),
           genuine_gamma_rect(rect,J)]
    true_primes=src.authenticated_prime_wavefront(a)
    for n,p in true_primes:
        cert=authenticated_hinge_cell(a,k,ix,iy,n)
        parts.append(src.I(cert.lower,cert.upper))
    total=sum(parts,src.I(Q(),Q()))
    h=2*a/(1<<k)
    result=total/h  # normalized cell indicators in L²(-a,a)
    if result.lo>result.hi:
        raise ArithmeticError("original source arithmetic interval failed")
    return AuthenticSuzukiCellBlock(
       source="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3",
       radius=a,order=k,J=J,spatial_cell=(ix,iy),
       value_lower=result.lo,value_upper=result.hi,
       prime_power_source=true_primes)

def hilbert_source_complete_block(a,order,J):
    """Return ALL authentic finite-J Suzuki *projected* matrix intervals.

    The entries are visited in Hilbert order and then reconstructed in
    original row/column order. Exact source log/exp/Gamma/pole/contact.
    Matrix is signed. No interval eigenvalue sign or RH is claimed.
    """
    a=rat(a);k=order_gate(order)
    if k>3:raise SuzukiCellIntegralError("whole finite-source block order<=3")
    values=tuple(full_source_cell(a,k,i,j,J) for i,j in
                 (point(k,d) for d in range(4**k)))
    n=1<<k
    lo=[[None]*n for _ in range(n)]
    hi=[[None]*n for _ in range(n)]
    for cell in values:
        i,j=cell.spatial_cell
        lo[i][j]=cell.value_lower
        hi[i][j]=cell.value_upper
    if (any(v is None for row in lo+hi for v in row) or
        any(lo[i][j]!=lo[j][i] or hi[i][j]!=hi[j][i]
            for i in range(n) for j in range(n))):
        raise ArithmeticError("signed original source block lost pair symmetry")
    return {
       "source":"AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3",
       "a":a,"Hilbert_order":k,"J":J,
       "cells":n,
       "original_prime_power_tape":src.authenticated_prime_wavefront(a),
       "lower_matrix":tuple(tuple(row) for row in lo),
       "upper_matrix":tuple(tuple(row) for row in hi),
       "all_original_source_components":True,
       "full_cell_integrals_without_midpoint_sampling":True,
       "compressed_block_spatial_quadrature_error":Q(),
       "continuum_finite_projection_norm_error_proved_zero":False,
       "original_infinite_Gamma_tail_included":False,
       "completed_Weil_PSD_proved":False,
       "rh_proved":False,
    }


def source_toeplitz_block(a,order,J):
    """The original completed g_J depends ONLY on x-y, so N lags suffice.

    Hilbert can order N² *reads*, but is not an optimal unique-value
    computation strategy for translation-invariant Suzuki matrices.
    A SOURCE-TRUE corrected baseline is the Toeplitz lag cache, requiring
    N source interval evaluations rather than N² independent evaluations.
    """
    a=rat(a);k=order_gate(order)
    if k>4:raise SuzukiCellIntegralError("bounded exact lag cache order<=4")
    n=1<<k
    lags=tuple(full_source_cell(a,k,lag,0,J) for lag in range(n))
    low=tuple(tuple(lags[abs(i-j)].value_lower for j in range(n))
              for i in range(n))
    high=tuple(tuple(lags[abs(i-j)].value_upper for j in range(n))
               for i in range(n))
    if any(low[i][j]!=low[j][i] or high[i][j]!=high[j][i]
           for i in range(n) for j in range(n)):
        raise ArithmeticError("original arithmetic Toeplitz source symmetry drift")
    return {
       "source":"AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3",
       "radius":a,"order":k,"J":J,
       "grid_side":n,
       "unique_original_lag_integrals":n,
       "full_source_matrix_entries":n*n,
       "verified_source_toeplitz_kernel":True,
       "lower_matrix":low,
       "upper_matrix":high,
       "entire_prime_Gamma_pole_contact_finiteJ":True,
       "finite_projected_block_spatial_quadrature_error":Q(),
       "continuum_projection_error_zero":False,
       "hilbert_beats_toeplitz_source_evaluations":False,
       "completed_Weil_positive_proved":False,
    }
