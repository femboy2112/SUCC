"""Rational outward enclosures for authentic anchored Suzuki K_g.

Uses the EXACT SHA-pinned original signed source module from PR #85. Never
constructs a new positive covariance, never imports zeta zero locations.
Every successful principal-minor certificate covers only the named finite
rational source points, never all x,y or RH.
"""
from __future__ import annotations

from fractions import Fraction as F
from .one_object_transport import OneObjectError, _fraction, _int


def authentic_suzuki_g_interval(t: int | F, J: int = 128) -> tuple[F,F]:
    """Rational enclosure for TRUE infinite gamma-rung g(|t|), 0<=|t|<=2.

    Source.screw_interval includes C_inf and only the first J NEGATIVE
    gamma potential rungs; omitted tail belongs to [-gamma_tail(J),0].
    Its pinned source data are authenticated by Git SHA-1 blob identity.
    """
    z=abs(_fraction(t))
    _int(J,1,128)
    if z>2:
        raise OneObjectError("Original interval source covers |t|<=2 only")
    if z==0:
        return F(),F()
    from .suzuki_legendre_source import _pinned_source
    source=_pinned_source()
    value=source.screw_interval(z,J)
    remainder=source.gamma_tail(J)
    lo=value.lo-remainder
    hi=value.hi
    if lo>hi:
        raise ArithmeticError("Original signed source enclosure inverted")
    return lo,hi


def authentic_kernel_interval(x: int | F, y: int | F, J: int = 128) -> tuple[F,F]:
    """K_g(x,y)=g(x-y)-g(x)-g(-y)+g(0), exact outward interval."""
    a,b=_fraction(x),_fraction(y)
    if a==0 or b==0:
        # Exact anchored cancellation: do not inflate a-b-b with interval dependency.
        return F(),F()
    diff=authentic_suzuki_g_interval(a-b,J)
    gx=authentic_suzuki_g_interval(a,J)
    gy=authentic_suzuki_g_interval(b,J)
    return diff[0]-gx[1]-gy[1],diff[1]-gx[0]-gy[0]


def _multiply(a: tuple[F,F], b: tuple[F,F]) -> tuple[F,F]:
    vals=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return min(vals),max(vals)


def _square(a: tuple[F,F]) -> tuple[F,F]:
    if a[0]<=0<=a[1]:
        return F(),max(a[0]**2,a[1]**2)
    return min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2)


def source_two_point_minor(x: int | F, y: int | F, J: int = 128) -> dict:
    """True K_g 2x2 Gram principal minors, with rational interval arithmetic.

    Positive lower diagonal AND positive determinant => certified PSD on
    exactly span{delta_x-delta_0,delta_y-delta_0}, not whole Weil form.
    Negative upper diagonal or negative upper determinant => genuine
    original-source negative witness, subject to hostile source audit.
    Otherwise AMBIGUOUS.
    """
    a,b=_fraction(x),_fraction(y)
    if a==b or a==0 or b==0:
        raise OneObjectError("Distinct nonzero source anchor probes required")
    xx=authentic_kernel_interval(a,a,J)
    yy=authentic_kernel_interval(b,b,J)
    xy=authentic_kernel_interval(a,b,J)
    product=_multiply(xx,yy)
    square=_square(xy)
    det=(product[0]-square[1],product[1]-square[0])
    certified_positive=(xx[0]>0 and yy[0]>0 and det[0]>0)
    certified_negative=(xx[1]<0 or yy[1]<0 or det[1]<0)
    if certified_positive and certified_negative:
        raise ArithmeticError("Inconsistent exact sign certificate")
    status=("PROVED_FINITE_SOURCE_POSITIVE" if certified_positive else
            "PROVED_FINITE_SOURCE_NEGATIVE" if certified_negative else
            "UNRESOLVED_FINITE_BOUND")
    return {"points":(a,b),"gamma_rungs":J,"Kxx":xx,"Kyy":yy,"Kxy":xy,
            "determinant":det,"verdict":status,
            "actual_Weil_source":"EXACT_SHA_PINNED_ORIGINAL_ZETA",
            "nontrivial_zeros_used":False,"RH_proved":False}
