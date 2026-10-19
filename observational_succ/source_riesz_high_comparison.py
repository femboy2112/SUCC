"""Infinite-dimensional source-conditional K-Riesz rank-one coercivity transport.

If original signed D>=kappa_star K on a closed parity high sector and
kappa0<=kappa_star, then C=kappa0 K+(kappa_star-kappa0) P^K_z is a valid
non-scalar source-dominated quadratic form. P^K_z(w)=|<Kw,z>|^2/<Kz,z>.
This transport cannot beat the *uniform* kappa_star K comparator; a
strict directional source theorem is a separate, unsolved obligation.
"""
from __future__ import annotations
from fractions import Fraction as F
from .direct_quotient_schur import exact_psd,exact_pd


class SourceComparisonError(ValueError):
    pass


def _r(x):
    if type(x) not in (int,F):raise SourceComparisonError("exact source rational only")
    return F(x)


def finite_K_riesz_profile(K,z,kappa0,kappa_star):
    """Exact finite algebra for universally valid sourced form inequality.

    General Hilbert-space proof is Cauchy-Schwarz in <Kw,v>. The caller must
    separately certify source D>=kappa_star K and K injectivity/domains.
    """
    K=tuple(tuple(_r(v) for v in row) for row in K)
    z=tuple(_r(v) for v in z)
    k0,ks=_r(kappa0),_r(kappa_star)
    n=len(K)
    if n<1 or n>8 or any(len(row)!=n for row in K) or len(z)!=n:
        raise SourceComparisonError("finite symmetric <=8 dimensional K required")
    if not 0<k0<=ks or not exact_pd(K):
        raise SourceComparisonError("proved SPD K and ordered positive kappa required")
    v=tuple(sum((K[i][j]*z[j] for j in range(n)),F(0)) for i in range(n))
    q=sum((z[i]*v[i] for i in range(n)),F(0))
    if q<=0:raise SourceComparisonError("nonzero K-energy witness required")
    delta=ks-k0
    P=tuple(tuple(v[i]*v[j]/q for j in range(n)) for i in range(n))
    C=tuple(tuple(k0*K[i][j]+delta*P[i][j] for j in range(n))
            for i in range(n))
    surplus=tuple(tuple(ks*K[i][j]-C[i][j] for j in range(n))
                  for i in range(n))
    if not exact_psd(P) or not exact_psd(surplus) or not exact_pd(C):
        raise ArithmeticError("K-Riesz comparison algebra failed")
    return {"K":K,"K_witness":z,"Kzz":q,"projector":P,"comparator":C,
            "full_scalar_minus_comparator":surplus,
            "rank_one_coefficient":delta,
            "dual_residual_gain_multiplier":delta/(k0*ks),
            "finite_comparison_verified":True,
            "infinite_original_source_verified":False,"RH_proved":False}


def source_high_riesz_witness(sector="odd", modes=(5,7), z=(F(1),F(0))):
    """Original signed Suzuki parity certificate creates a SOURCE form C.

    This does not promote a finite K block to infinite positivity; the latter
    follows from the inherited all-high source D>=ks K and Hilbert-space
    Cauchy-Schwarz. The returned finite matrix is an exact witness chart.
    """
    from .tate_weighted_bessel_four_schur import (
        source_parity_split_four_moment_coercivity_certificate,
    )
    from .suzuki_moment_schur import inverse_neumann_entry
    if sector not in ("odd","even") or type(modes) not in (tuple,list) or not modes:
        raise SourceComparisonError("one original high reflection sector required")
    if len(modes)!=len(z) or len(modes)>8:
        raise SourceComparisonError("finite witness coordinates must align")
    if any(type(k) is not int or not 5<=k<=30 or
           (k%2!=(1 if sector=="odd" else 0)) for k in modes):
        raise SourceComparisonError("true modes >=5 of one sector required")
    if len(set(modes))!=len(modes):
        raise SourceComparisonError("duplicate witness mode")
    cert=source_parity_split_four_moment_coercivity_certificate()
    source=cert[sector+"_sector"]
    ks=source["kappa_"+sector+"_exact_lower"]
    k0=source["kappa_"+sector+"_certified_rational"]
    if ks<=k0:raise SourceComparisonError("no source-certified coercivity slack")
    K=tuple(tuple(inverse_neumann_entry(F(1,2),i,j)
                  for j in modes) for i in modes)
    model=finite_K_riesz_profile(K,z,k0,ks)
    return {
        "source":"SHA_PINNED_ORIGINAL_SUZUKI_BESSEL4_RIESZ_HIGH_FORM",
        "source_sha":cert["source_suzuki_blob"],
        "genuine_prime_power_labels":cert["genuine_prime_power_labels"],
        "sector":sector,"mode_labels":tuple(modes),
        "kappa0":k0,"kappa_source_exact_lower":ks,
        "delta":model["rank_one_coefficient"],
        "Kzz":model["Kzz"],
        "finite_operator_chart":model["comparator"],
        "infinite_form_valid_given_inherited_source_theorem":True,
        "strict_gain_over_full_kappa_source_scalar":False,
        "RH_proved":False,
    }


def coercivity_slack_no_go():
    """Exact counterexample to lifting positive compression to rank-one Loewner.

    D-kappa*K=[[1,1],[1,1]] PSD; the 1x1 compression is positive,
    but no positive delta*e1e1* follows (indefinite remainder).
    """
    K=((F(1),F(0)),(F(0),F(1)))
    rest=((F(1),F(1)),(F(1),F(1)))
    delta=F(1,2)
    failed=((rest[0][0]-delta,rest[0][1]),
            (rest[1][0],rest[1][1]))
    return {
        "K":K,"original_residual_PSD":exact_psd(rest),
        "positive_finite_direction":rest[0][0]>0,
        "false_extra_rank_one_PSD":exact_psd(failed),
        "scope":"finite high compression alone cannot justify infinite rank-one improvement",
        "RH_proved":False,
    }
