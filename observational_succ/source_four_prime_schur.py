"""Authenticated four-mode S4 lower from authentic Gamma+prime2 center correlations.

SOURCE INPUT:
  1) Original signed A4 and differentiated TRUE quotient upper from the
     immutable PR155 projector-first source integrator at a=1/2.
  2) All four ORIGINAL completed mixed source moments independently replayed
     by inherited CertifiedTrial, real Gamma analytic centered source.
  3) Source-derived non-scalar first-prime high coercivity / ambient inverse.

For each real low direction x, R4(x) <= κ^-1 <g_x,g_x> -
  [w2/(κ(κ+w2))] ||(g_x)_true_center||²
with separate parity. Orthogonal center indicator and x indicator imply
  ||(g_x)_C0||² >=4 |Σ_odd x_i ℓ0(g_i)|²
                        +768 |Σ_even x_i ℓ1(g_i)|².
The source interval vector gives exact global matrix or nonlinear
direction-wise lower bounds. No invented positive Loewner rank-one
certificate under uncertain angle, no imaginary off-parity coupling.
"""
from __future__ import annotations

from fractions import Fraction as F
from .source_four_center_gram import (
    SourceCenterError,authentic_four_center_certificate,
    robust_center_energy_for_direction
)
from .authentic_prime_surplus import original_prime_surplus_source_passport
from .direct_quotient_schur import exact_psd


def _mat(M):
    M=tuple(tuple(F(v) for v in row) for row in M)
    if len(M)!=4 or any(len(row)!=4 for row in M):
        raise SourceCenterError("original signed source 4x4 matrix required")
    return M


def _quadratic(A,x):
    return sum((x[i]*A[i][j]*x[j] for i in range(4) for j in range(4)),F(0))


def _parity_lower(dirs,values,errors,w,eta):
    """Sharp Young lower for uncertain source rank-one interval vector."""
    m=tuple(values[i] for i in dirs)
    e=tuple(errors[i] for i in dirs)
    out=[[F(0)]*4 for _ in range(4)]
    total_error=sum(e,F(0))
    for i in dirs:
        for j in dirs:
            out[i][j]=w*(1-eta)*values[i]*values[j]
        out[i][i]-=w*(1/eta-1)*errors[i]*total_error
    return tuple(tuple(v for v in row) for row in out)


def _sec_psd(A):
    from .direct_quotient_schur import exact_psd
    A=_mat(A)
    if any(A[i][j] for i in range(4) for j in range(4) if (i-j)%2):
        raise ArithmeticError("broken source reflection sector")
    return exact_psd(A)


def _min_eig_lower(A,depth=40):
    from .certified_four_schur_trial import min_eig_lower
    return min_eig_lower(A,depth=depth)


def CertifiedFourPrimeSchurTrial(*,J_center=64,J_G=64,
                                 J_deriv=2,digits=100,eta=F(1,8)):
    """Real original signed source FOUR-MODE source-dependent Schur enclosure.

    If lower 4x4 PSD: first-window original S4 positive certificate.
    Otherwise AMBIGUOUS (a negative lower is NOT a negative original sign).
    Source signed Weil all-radii positivity and RH remain OPEN in either case.
    """
    if type(eta) not in (int,F) or not 0<F(eta)<=1:
        raise SourceCenterError("positive exact Young eta 0<eta<=1")
    eta=F(eta)
    from .analytic_suzuki_schur_gate import CertifiedAnalyticSuzukiTrial
    center=authentic_four_center_certificate(J=J_center,J_G=J_G)
    src=original_prime_surplus_source_passport()
    analytic=CertifiedAnalyticSuzukiTrial(
        (),J_deriv=J_deriv,J_galerkin=J_G,rank=5,digits=digits,
        young_eta=F(1,8)
    )
    if not analytic.get("source_passport_verified") or \
       analytic.get("RH_proved") or \
       center["source_sha"]!=src["source_sha"]:
        raise SourceCenterError("original source Sha, signed Gram or analytic tail gate failed")
    old=_mat(analytic["true_S4_Loewner_lower"])
    full=_mat(analytic["true_quotient_gram_upper"])
    kappa=(src["kappa_odd"],src["kappa_even"])
    w=src["positive_source_weight_floor"]
    coeff=(w/(kappa[0]*(kappa[0]+w)),
           w/(kappa[1]*(kappa[1]+w)))
    odd=_parity_lower((0,2),center["nominal"],center["errors"],F(4),eta)
    even=_parity_lower((1,3),center["nominal"],center["errors"],F(768),eta)
    center_lower=tuple(tuple(odd[i][j]+even[i][j] for j in range(4))
                       for i in range(4))
    improvement=tuple(tuple(coeff[i%2]*center_lower[i][j] for j in range(4))
                       for i in range(4))
    corrected=tuple(tuple(old[i][j]+improvement[i][j] for j in range(4))
                       for i in range(4))
    if any(corrected[i][j]!=corrected[j][i] for i in range(4) for j in range(4)):
        raise ArithmeticError("four-source arithmetic correction lost Hermitian reflection symmetry")
    src_sign=exact_psd(corrected)
    old_sign=exact_psd(old)
    basis=tuple(tuple(F(i==j) for i in range(4)) for j in range(4))
    directions={
        "P1":basis[0],
        "P2":basis[1],
        "P3":basis[2],
        "P4":basis[3],
        "P1+P3":(F(1),F(0),F(1),F(0)),
        "P1-P3":(F(1),F(0),F(-1),F(0)),
        "P2+P4":(F(0),F(1),F(0),F(1)),
        "P2-P4":(F(0),F(1),F(0),F(-1)),
    }
    dir_results={}
    for label,x in directions.items():
        lower_center=robust_center_energy_for_direction(center,x)
        saving=coeff[0 if x[0] or x[2] else 1]*lower_center
        source_lower=_quadratic(old,x)+saving
        dir_results[label]={
            "original_signed_S4_lower":source_lower,
            "original_scalar_only_S4_lower":_quadratic(old,x),
            "strict_arithmetic_saving":saving,
            "four_matrix_Young_lower":_quadratic(corrected,x),
        }
    p1=dir_results["P1"]
    from .source_prime_center_alignment import certified_true_P1_center_residual
    previous=certified_true_P1_center_residual(J=J_center,J_G=J_G)
    if not (p1["strict_arithmetic_saving"]>0 and
            previous["true_P1_source_prime_dual_saving_lower"]>0):
        raise ArithmeticError("original source P1 strict central saving lost")
    # Independent outward intervals need NOT be nested: their INTERSECTION,
    # already checked in the four-column source adapter, is load-bearing.
    # Strict positive bounds can differ slightly without source disagreement.
    return {
        "source":"REAL_COMPLETED_SUZUKI_SIGNED_S4_FOUR_PRIME_CENTER",
        "source_sha":src["source_sha"],
        "source_first_window":F(1,2),
        "source_true_prime_power":(2,2),
        "kappa_by_derivative_parity":kappa,
        "true_prime2_lower_w":w,
        "per_parity_center_inverse_saving_coefficient":coeff,
        "source_Gamma_J_center":J_center,
        "source_Gamma_J_derivative_energy":J_deriv,
        "center_interval_moments":center["intervals"],
        "center_ranktwo_nominal_matrix":center["center_nominal_ranktwo_Gram"],
        "center_ranktwo_Young_error_matrix_lower":center_lower,
        "center_interval_radii":center["errors"],
        "source_original_trial_signed_scalar_S4_lower":old,
        "source_corrected_four_S4_Loewner_lower":corrected,
        "original_scalar_S4_lower_certified_PSD":old_sign,
        "arithmetic_source_four_S4_lower_certified_PSD":src_sign,
        "arithmetic_source_four_S4_verdict":"POSITIVE_CERTIFIED_FIRST_WINDOW" if src_sign else "AMBIGUOUS",
        "improvement_Loewner_nonnegative":exact_psd(improvement),
        "center_Loewner_improvement_matrix":improvement,
        "center_Young_eta":eta,
        "source_direction_certificates":dir_results,
        "old_analytic_source_verdict":analytic["verdict"],
        "actual_source_P1_independent_replay":center["original_p1_replay_agrees"],
        "true_complete_signed_S4_sign_proved":src_sign,
        "RH_proved":False,
    }
