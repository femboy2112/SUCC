"""Exact two-boundary chart descent: algebraic P1 and Cech H0/H1 for O(k).

The opposite E / E'' charts are A1_z and A1_w, w=z^-1, with overlap
Gm=Spec(Q[z,z^-1]). An explicitly supplied transition f0=z^k f_inf
models O(k). Cohomology follows from the two-affine-open Cech complex.
Only finite exact Laurent polynomials over Q are handled computationally.
This is classical genus-zero Riemann--Roch, NOT zeta Gamma or RH.
"""
from __future__ import annotations
from fractions import Fraction as F
from typing import Mapping


class DualChartError(ValueError):
    """Malformed Laurent polynomial or unsupported transition/source."""


def _poly(coefficients: Mapping[int,F], *, nonnegative: bool = False) -> dict[int,F]:
    if not isinstance(coefficients, Mapping):
        raise DualChartError("Finite Laurent coefficient mapping required")
    out={}
    for degree, coefficient in coefficients.items():
        if type(degree) is not int or (nonnegative and degree<0):
            raise DualChartError("Integral monomial degrees required on declared chart")
        if type(coefficient) is not int and type(coefficient) is not F:
            raise DualChartError("Use exact rational coefficients only")
        c=F(coefficient)
        if c: out[degree]=c
    return dict(sorted(out.items()))


def _degree(k:int)->int:
    if type(k) is not int or abs(k)>10000:
        raise DualChartError("Bounded exact integral twist degree required")
    return k


def cech_dimensions(k:int) -> dict:
    """Compute H0/H1 and Euler characteristic for O(k) on projective line."""
    k=_degree(k)
    h0=max(k+1,0)
    h1=max(-k-1,0)
    return {"twist":k,"h0_dimension":h0,"h1_dimension":h1,
            "euler_characteristic":h0-h1,
            "global_section_monomials":tuple(range(0,k+1)) if k>=0 else (),
            "obstruction_monomials":tuple(range(k+1,0)) if k<=-2 else (),
            "genus_zero_rr_verified":h0-h1==k+1}


def glue_dual_sections(k:int, zero:Mapping[int,F], infinity:Mapping[int,F]) -> dict:
    """Check f_0(z) == z^k f_inf(1/z) on Gm, no hidden coefficients."""
    k=_degree(k)
    zero=_poly(zero,nonnegative=True)
    infinity=_poly(infinity,nonnegative=True)
    transported={k-degree:c for degree,c in infinity.items()}
    transported=dict(sorted(transported.items()))
    allowed=cech_dimensions(k)["global_section_monomials"]
    return {"compatible":zero==transported,
            "global_section":zero if zero==transported else None,
            "zero_chart":zero,
            "infinity_chart":infinity,
            "transported_infinity":transported,
            "allowed_global_modes":allowed,
            "source_transition":f"z^{k}",
            "nontrivial_global_section": bool(zero) and zero==transported}


def dual_chart_from_global(k:int, zero:Mapping[int,F]) -> dict:
    """Construct the other observer's chart data from valid global coefficients."""
    k=_degree(k)
    zero=_poly(zero,nonnegative=True)
    if any(j>k for j in zero):
        raise DualChartError("Global mode not allowed by specified twist")
    infinity={k-j:c for j,c in zero.items()}
    r=glue_dual_sections(k,zero,infinity)
    if not r["compatible"]:raise AssertionError("Constructed section failed overlap check")
    return r


def cech_reduce(k:int, laurent:Mapping[int,F]) -> dict:
    """Exact decomposition Laurent = zero_chart + z^k infinity_chart + H1.

    The obstruction is unique modulo coboundaries. One canonical choice
    assigns all powers n>=0 to zero chart, remaining powers n<=k to
    infinity chart; missing powers k<n<0 are invariant H1 classes.
    """
    k=_degree(k)
    v=_poly(laurent)
    zero={n:c for n,c in v.items() if n>=0}
    infinity={k-n:c for n,c in v.items() if n<0 and n<=k}
    obstruction={n:c for n,c in v.items() if n<0 and n>k}
    if any(j<0 for j in infinity):raise AssertionError("Invalid infinity chart exponent")
    reconstructed=dict(zero)
    for j,c in infinity.items():
        n=k-j
        reconstructed[n]=reconstructed.get(n,F(0))+c
    for n,c in obstruction.items():
        reconstructed[n]=reconstructed.get(n,F(0))+c
    if _poly(reconstructed)!=v:
        raise AssertionError("Cech Laurent decomposition did not reconstruct source")
    allowed=set(cech_dimensions(k)["obstruction_monomials"])
    if not set(obstruction)<=allowed:
        raise AssertionError("Obstruction outside computed H1 basis")
    return {"twist":k,"zero_cochain":zero,"infinity_cochain":dict(sorted(infinity.items())),
            "obstruction_class":obstruction,"coboundary":not bool(obstruction),
            "representative":v,
            "h1_dimension":len(allowed)}
