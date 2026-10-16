"""True completed-zeta Gamma-tail enclosure for original Suzuki Neumann 30-mode mixed derivatives.

NO zeta-zero inputs; existing original source snapshot remains SHA pinned.

For true a=1/2 source low modes u_i(x)=P_i(2x) of mean zero,
  M_(k,i)=<u'_k,(G u_i)'> .
The original finite-J operator G_J uses the *infinite completed contact*
and truncates the negative Gamma potential. Thus
  (G_infinity-G_J) u_i
   =sum_(j>=J) c_j ∫_-a^a exp(-alpha_j|x-y|)u_i(y)dy,
  c_j=4/(4j+1)^2, alpha_j=(4j+1)/2.
The constant c_j term vanishes since ∫u_i=0.

Integration by parts in the SOURCE integration variable y yields
  d_x(E_alpha u_i)(x)
    =E_alpha u'_i(x)
     + exp(-alpha|x+a|)u_i(-a)
     - exp(-alpha|x-a|)u_i(a).
Using |u_i(±a)|=1, ||u'_k||_inf<=k(k+1) on [-1/2,1/2],
||u'_i||_2²=2i(i+1), and ||E_alpha||_(2->2)<=2/alpha,
the mixed moment tail is bounded by
  |M_inf(k,i)-M_J(k,i)|
   <= [2i(i+1)+4k(k+1)] * sum_(j>=J) 8/(4j+1)^3
   <= [2i(i+1)+4k(k+1)]*
       [1/(4J+1)^2+8/(4J+1)^3] .
A source-derived O(J^-2) bound. By reflection symmetry M_(k,i)=0
when i+k odd, for ALL Gamma stages and the completed source.

This does NOT construct the pure source derivative Gram T, high resolvent,
low Schur sign or all-test Weil positivity. Every finite-J true-source
input uses suzuki_signed_mixed30.original_mixed_derivative_gram and
suzuki_legendre_source._pinned_source; no synthetic covariance substitution.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .suzuki_legendre_source import _pinned_source
from .suzuki_signed_mixed30 import (
    OriginalMixedGaugeError,original_mixed_derivative_gram
)


class CompletedMixedGammaError(ValueError):
    """Malformed genuine original-source mixed moment or Gamma tail request."""


def gamma_mixed_spectral_tail(J:int)->F:
    """Exact source-independent rational majorant of sum_j>=J c_j/alpha_j."""
    if type(J) is not int or not 1<=J<=64:
        raise CompletedMixedGammaError("Original finite source mixed J supported 1..64")
    d=4*J+1
    return F(1,d*d)+F(8,d*d*d)


def true_mixed_legendre_tail_bound(J:int,k:int,i:int)->F:
    """Original a=1/2, u_k'=P_k'(2x) source-specific rational bound."""
    from .suzuki_neumann_dual_gauge import ordinal
    _pinned_source()
    try:
        k=ordinal(k)
        i=ordinal(i)
    except (TypeError,ValueError) as exc:
        raise CompletedMixedGammaError("Original Legendre modes k,i=1..30 only") from exc
    return (2*i*(i+1)+4*k*(k+1))*gamma_mixed_spectral_tail(J)


@dataclass(frozen=True)
class CompletedMixed30SourceCertificate:
    source:str
    original_source_blob:str
    J:int
    rank:int
    low_modes:tuple[int,...]
    source_finite_matrix:tuple
    completed_matrix_enclosures:tuple
    gamma_tail_factors:tuple
    all_original_parity_zero_entries_retained:bool
    original_infinite_Gamma_integral_enclosed:bool=True
    pure_H1_derivative_Gram_computed:bool=False
    original_low_30_Schur_PSD_proved:bool=False
    RH_proved:bool=False


def authentic_infinite_gamma_mixed_rows(
        J:int,rank:int=30,low_modes:tuple[int,...]=(1,)) ->CompletedMixed30SourceCertificate:
    """Convert genuine original finite-J source matrix to full Gamma enclosures.

    Each outward Fraction interval encloses the ACTUAL completed
    mixed Neumann derivative moment; the row/column source is verified.
    This bounds each component, not its coupled full 30x30 Schur sign.
    """
    src=_pinned_source()
    if (type(rank) is not int or not 1<=rank<=30
            or type(low_modes) is not tuple or not low_modes
            or len(set(low_modes))!=len(low_modes)
            or any(type(v) is not int or not 1<=v<=30 for v in low_modes)):
        raise CompletedMixedGammaError("Original mode indices and finite rectangular source requested")
    try:
        actual=original_mixed_derivative_gram(J,rank,low_modes)
    except (OriginalMixedGaugeError,ValueError) as exc:
        raise CompletedMixedGammaError("Original signed source finite mixed Gram refused") from exc
    if (actual.source!="AUTHENTIC_Q_ZETA_SUZUKI_G_J_TRUE_LOWHIGH_DERIVATIVE"
            or actual.original_source_blob!="0cc8510b71d178fc79e8d410a86d8b6014cf9178"):
        raise ArithmeticError("Original immutable Suzuki mixed source passport is invalid")
    matrix=[]
    factors=[]
    parity=True
    for k,row in enumerate(actual.matrix_intervals,1):
        newrow=[]
        bounds=[]
        for i,v in zip(low_modes,row):
            if type(v) is not src.I:
                raise ArithmeticError("Original signed source interval type changed")
            if (i+k)%2:
                if (v.lo,v.hi)!=(F(),F()):
                    raise ArithmeticError("Original real Gamma parity contradicts exact source")
                newrow.append(src.I(F(),F()))
                bounds.append(F())
            else:
                err=true_mixed_legendre_tail_bound(J,k,i)
                newrow.append(src.I(v.lo-err,v.hi+err))
                bounds.append(err)
            if (i+k)%2 and newrow[-1]!=(src.I(F(),F())):
                parity=False
        matrix.append(tuple(newrow))
        factors.append(tuple(bounds))
    return CompletedMixed30SourceCertificate(
        "SHA_PINNED_AUTHENTIC_COMPLETED_ZETA_SUZUKI_MIXED30",
        actual.original_source_blob,J,rank,low_modes,
        actual.matrix_intervals,tuple(matrix),tuple(factors),parity
    )


def completed_mixed_gamma_two_stage_intersection(
        J1:int,J2:int,rank:int=3,low_modes:tuple[int,...]=(1,))->dict:
    """Exact same-source consistency of two Gamma-regulator mixed moment boxes."""
    if type(J1) is not int or type(J2) is not int or not 1<=J1<J2<=64:
        raise CompletedMixedGammaError("Two strictly ordered true finite Gamma source regulators")
    A=authentic_infinite_gamma_mixed_rows(J1,rank,low_modes)
    B=authentic_infinite_gamma_mixed_rows(J2,rank,low_modes)
    intersections=[]
    for rowa,rowb in zip(A.completed_matrix_enclosures,B.completed_matrix_enclosures):
        r=[]
        for va,vb in zip(rowa,rowb):
            lo=max(va.lo,vb.lo)
            hi=min(va.hi,vb.hi)
            if lo>hi:
                raise ArithmeticError("True Suzuki finite-J stages contradict completed original source")
            r.append((lo,hi))
        intersections.append(tuple(r))
    return {"source":"SAME_ORIGINAL_SHA_PINNED_MIXED_GAMMA",
            "ranks":(rank,len(low_modes)),
            "Gamma_stages":(J1,J2),
            "J1_gamma_tail_bound":gamma_mixed_spectral_tail(J1),
            "J2_gamma_tail_bound":gamma_mixed_spectral_tail(J2),
            "source_completed_mixed_intersection":tuple(intersections),
            "all_true_entries_source_consistent":True,
            "original_full_pure_H1_Gram_built":False,
            "original_low_Schur_sign_proved":False,
            "RH_proved":False}



def original_completed_first_mixed_negative_source(J:int=64)->dict:
    """REAL completed-source M_11<0, checked by two different derivations.

    The first Legendre mode u1(x)=2x has u1'(x)=2. Thus
       M_11=<2,(G u1)'> = 2*(F1(a)-F1(-a)).
    For the even original source and odd u1, F1 is odd:
       M_11=4*F1(a) = 2*mu,
    where mu=2∫_0^1(1-2t)g(t)dt, the independently implemented
    original TRUE Neumann dual flux in suzuki_neumann_source_flux.py.

    The full true infinite-Gamma M_11 must lie in BOTH the J-stage
    interval expanded by the analytic O(J^-2) tail and twice the
    independently integrated completed-source flux interval. If
    either source interval fails to enclose a strictly negative value,
    return a hard failure instead of silently promoting a sign.
    This is a sign of the MIXED derivative, NOT Weil PSD/Schur sign.
    """
    from .suzuki_neumann_source_flux import genuine_infinite_first_flux
    M=authentic_infinite_gamma_mixed_rows(J,1,(1,))
    mixed=M.completed_matrix_enclosures[0][0]
    flux=genuine_infinite_first_flux(16)
    f_lo,f_hi=flux["full_infinite_source_flux_interval"]
    from_flux=(2*f_lo,2*f_hi)
    lo=max(mixed.lo,from_flux[0])
    hi=min(mixed.hi,from_flux[1])
    if lo>hi:
        raise ArithmeticError("Two genuine original-source Gamma completions disagree")
    if hi>=0 or mixed.hi>=0 or from_flux[1]>=0:
        raise ArithmeticError("Original strict first mixed negativity not source certified")
    return {
       "source":"ORIGINAL_ZETA_M11_COMPLETED_GAMMA_SHA_PINNED",
       "true_mixed_source_J":J,
       "mixed_analytic_tail_bound":true_mixed_legendre_tail_bound(J,1,1),
       "original_Fourier_Legendre_infinite_source_interval":
           (mixed.lo,mixed.hi),
       "independent_original_flux_identity_interval":from_flux,
       "intersection_rigorous_negative":(lo,hi),
       "source_first_mixed_M11_strictly_negative":True,
       "not_original_Weil_quadratic_eigenvalue":True,
       "original_30_low_Schur_PSD_proved":False,
       "RH_proved":False,
    }
