"""Authenticated first-window source gate and conditional Gamma-truncated residual.

This bridges the PR #104 original Suzuki 30-moment high-source theorem to
the EXACT a-posteriori variational residual inequality, without declaring
user-supplied low entries / residual derivative Gram authenticated.

If r=QG(Px-Yx), r_J=QG_J(Px-Yx), then on (-1/2,1/2)
  ||(r-r_J)'||_2 <= delta_J * sqrt(||x||²+||Yx||²),
delta_J=963*[1/(4J+1)+4/(4J+1)²] (the ancestor's original Gamma
tail source norm bound; Q projection/Legendre derivative norm retained).
For eta>0,
  T_r <= (1+eta)T_{r_J}
         +(1+eta^-1) delta_J² (I+Y*Y).
Hence R0 <= L_Y + kappa^-1 times that matrix, conditional on
INDEPENDENTLY CERTIFIED original source A,B,D and derivative Gram T_J.

No Tate/Connes trace is silently identified, and no RH claim is made.
"""
from __future__ import annotations
from fractions import Fraction as F
from .one_object_relative_residual import (
    q,matrix,psd,add,scale,eye,gram,shape,ResidualSourceError
)

def authenticated_first_window_gate():
    """No free-form source label: replay original pinned arithmetic and high gap."""
    from . import hilbert_weil_atlas as atlas
    from . import suzuki_moment_schur as schur
    from . import source_weil_hierarchy as original
    source=atlas.authenticated_first_window_range_certificate()
    high=schur.source_moment30_certificate()
    original.assert_original_source_tape()
    kappa=F(369,10000)
    if (source["high_relative_Neumann_gap"]!=kappa or
        source["original_source_pinned_blob"]!=atlas.ORIGINAL_SUZUKI_SOURCE_BLOB or
        high["vanishing_moments"]!=30 or
        high["strict_high_L2_coercivity"]!=str(kappa) or
        source["RH_proved"] is not False):
        raise ResidualSourceError("original prime/Gamma/Sobolev range contract drift")
    return {
       "source":"RIEMANN_ZETA_ORIGINAL_COMPLETED_SIGNED_WEIL",
       "original_suzuki_git_blob":atlas.ORIGINAL_SUZUKI_SOURCE_BLOB,
       "integrated_main_origin":atlas.SOURCE_BRANCH_MAIN,
       "radius":F(1,2),
       "high_gap_relative_to":"Q_K_Neumann_Q_NOT_IDENTITY",
       "kappa":kappa,
       "low_legendre_modes":30,
       "reflection_parity_blocks":(15,15),
       "cross_mapping_to_H1_bounded":True,
       "zero_shift_cross_resolvent_form_finite":True,
       "finite_candidate_galerkin_residual_derived":False,
       "low_signed_schur_positivity_proved":False,
       "Tate_full_test_source_gluing_verified":False,
       "Connes_global_principal_value_trace_glued":False,
       "rh_proved":False
    }

def genuine_gamma_residual_tail(J):
    """Original Gamma-tail H1 gain, kappa, basis from authenticated SUCC."""
    if type(J) is not int or not 1<=J<=128:
        raise ResidualSourceError("finite original Gamma cutoff J 1..128")
    from . import hilbert_weil_atlas as atlas
    gate=authenticated_first_window_gate()
    result=atlas.original_source_cross_derivative_tail_budget(J)
    delta=q(result["source_high_cross_derivative_gain_upper"])
    if not delta>0:
        raise ArithmeticError("original gamma tail failed positivity")
    return dict(gate,J=J,gamma_cross_H1_error_bound=delta,
                gamma_source_is_original=True,
                derivative_Gram_from_full_original_G_source_verified=False)

def conditional_original_residual_gram(T_J,Y,J,eta):
    """Source Gamma + conditional derivative Gram in finite low dimension.

    T_J is an externally proposed Gram for actual r_J'; its truth is
    NOT authenticated by these exact matrix algebra checks.
    Y is a proposed actual high response in an orthonormal source basis;
    its original source/basis validity is also NOT authenticated here.
    """
    T_J=matrix(T_J,square=True)
    Y=matrix(Y)
    h,l=shape(Y)
    eps=q(eta)
    if (eps<=0 or l>4 or h>8 or shape(T_J)!=(l,l) or not psd(T_J)):
        raise ResidualSourceError("positive eta / PSD derivative Gram dimensions")
    src=genuine_gamma_residual_tail(J)
    delta=src["gamma_cross_H1_error_bound"]
    extra=add(eye(l),gram(Y,Y))
    bound=add(scale(1+eps,T_J),scale((1+1/eps)*delta*delta,extra))
    if not psd(bound):
        raise ArithmeticError("genuine Gamma candidate Gram negative")
    return {
      "source":src["source"],
      "original_suzuki_blob":src["original_suzuki_git_blob"],
      "radius":src["radius"],
      "kappa":src["kappa"],
      "original_gamma_modes":J,
      "H1_gamma_tail_gain":delta,
      "conditional_residual_derivative_Gram_upper":bound,
      "conditional_short_response_penalty_matrix":scale(1/src["kappa"],bound),
      "requires_independent_original_finiteJ_derivative_Gram_authentication":True,
      "requires_independent_original_low_high_response_basis_authentication":True,
      "actual_T_J_verified":False,
      "actual_Y_verified":False,
      "authentic_signed_low_A_minus_short_R0_positive_proved":False,
      "all_radii_RH_proved":False
    }
