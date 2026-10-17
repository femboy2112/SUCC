"""Joint original completed signed Suzuki S4 bound: source center + prime edge.

The actual prime2 high comparator κI+w(I-A_log2) has EXACT inverse.
The dual saving is the SUM of two positive terms:
    c_center ||g_center||² + c_edge ||g_R - T_b g_L||².
Earlier source_four_prime_schur certified the full-four center Gram.
Here a separately sourced genuine first-prime edge Gram is added.
Both finite-J source responses use original pole+contact+Gamma/prime data,
the original completed mixed projection moments, and rigorous tail errors.
The result is a valid SIGNED original S4 LOEwner lower, even if indefinite.
"""
from __future__ import annotations

from fractions import Fraction as F

from .source_four_prime_schur import (
    CertifiedFourPrimeSchurTrial, _mat,_quadratic
)
from .source_four_edge_gram import (
    authentic_four_edge_moments,phase_edge_energy_for_direction,
    phase_edge_Young_gram_lower
)
from .source_four_center_gram import SourceCenterError
from .authentic_prime_surplus import original_prime_surplus_source_passport
from .direct_quotient_schur import exact_psd


def CertifiedFourPrimeFullPhaseSchurTrial(*,J_center=64,J_G=64,J_deriv=2,
                                          J_edge=8,eta=F(1,8),digits=100):
    """Full 4x4 signed first-prime lower incorporating both source-dual savings.

    This computes a lower enclosure, not the exact infinite S4. A negative
    eigenvalue of the lower is AMBIGUOUS, not a counterexample to RH.
    """
    if type(eta) not in (int,F) or not 0<F(eta)<=1:
        raise SourceCenterError("Young eta rational in (0,1] required")
    eta=F(eta)
    center=CertifiedFourPrimeSchurTrial(
        J_center=J_center,J_G=J_G,J_deriv=J_deriv,digits=digits,eta=eta
    )
    edge=authentic_four_edge_moments(J=J_edge,J_G=J_G,digits=digits)
    src=original_prime_surplus_source_passport()
    if center["source_sha"]!=src["source_sha"] or edge["source_sha"]!=src["source_sha"]:
        raise SourceCenterError("independent source center/edge hash disagreement")
    w=src["positive_source_weight_floor"]
    kappas=(src["kappa_odd"],src["kappa_even"])
    cphase=tuple(w/(k*(k+2*w)) for k in kappas)
    edgelow=_mat(phase_edge_Young_gram_lower(edge,eta))
    phasedelta=tuple(tuple(cphase[i%2]*edgelow[i][j] for j in range(4))
                     for i in range(4))
    sourcebase=_mat(center["source_corrected_four_S4_Loewner_lower"])
    new=_mat(tuple(tuple(sourcebase[i][j]+phasedelta[i][j] for j in range(4))
                   for i in range(4)))
    if any(new[i][j]!=new[j][i] for i in range(4) for j in range(4)):
        raise ArithmeticError("genuine source phase cannot break reflection symmetry")
    # Unlike a fixed uncertain-rank-one Loewner matrix, this classical
    # two-variable exact cone decision preserves EVERY guaranteed directional
    # source gain. The source high form and original low signed bound are
    # already independently SHA-attested above.
    from .exact_source_two_dim_cone import exact_nonnegative_two_dimensional_source_cone
    baseline=_mat(center["source_original_trial_signed_scalar_S4_lower"])
    centerm=center["center_source_moment_nominal"]
    centere=center["center_interval_radii"]
    edgem=edge["nominal"];edgee=edge["errors"]
    widthmax=edge["edge_width_interval"][1]
    factors={0:F(4),1:F(768)}
    edgeweights={0:F(12)/widthmax**3,1:F(1)/widthmax}
    cone={}
    for parity,(i,j) in (("odd_derivative",(0,2)),("even_derivative",(1,3))):
        p=i%2
        features=(
            (centerm[i],centerm[j],centere[i],centere[j],
             center["per_parity_center_inverse_saving_coefficient"][p]*factors[p]),
            (edgem[i],edgem[j],edgee[i],edgee[j],
             cphase[p]*edgeweights[p]),
        )
        base=((baseline[i][i],baseline[i][j]),
              (baseline[j][i],baseline[j][j]))
        cone[parity]=exact_nonnegative_two_dimensional_source_cone(base,features)
    cone_positive=all(x["robust_lower_nonnegative_for_ALL_real_directions"]
                      for x in cone.values())
    first_window_positive=exact_psd(new) or cone_positive
    verdict="POSITIVE_CERTIFIED_FIRST_WINDOW" if first_window_positive else "AMBIGUOUS"
    directions={}
    xlist={
        "P1":(1,0,0,0),"P2":(0,1,0,0),"P3":(0,0,1,0),"P4":(0,0,0,1),
        "P1+P3":(1,0,1,0),"P1-P3":(1,0,-1,0),
        "P2+P4":(0,1,0,1),"P2-P4":(0,1,0,-1),
    }
    for label,vector in xlist.items():
        x=tuple(F(t) for t in vector)
        v=phase_edge_energy_for_direction(edge,x)
        sector=0 if x[0] or x[2] else 1
        saving=v*cphase[sector]
        base=center["source_direction_certificates"][label]
        directions[label]={
            "signed_source_full_S4_directional_lower":
                base["original_signed_S4_lower"]+saving,
            "arithmetic_center_strict_saving":
                base["strict_arithmetic_saving"],
            "arithmetic_prime_edge_strict_saving":saving,
            "total_arithmetic_strict_saving":
                base["strict_arithmetic_saving"]+saving,
        }
    return {
        "source":"REAL_COMPLETED_SIGNED_SUZUKI_FULL_FOUR_CENTER_AND_EDGE",
        "source_sha":src["source_sha"],
        "genuine_prime_label":src["true_prime_power_label"],
        "J_center":J_center,"J_edge":J_edge,"J_deriv":J_deriv,"J_G":J_G,
        "source_edge_intervals":edge["intervals"],
        "source_edge_width":edge["edge_width_interval"],
        "source_edge_nominal":edge["nominal"],
        "source_edge_errors":edge["errors"],
        "center_original_four_Loewner_lower":sourcebase,
        "edge_source_four_Loewner_improvement_lower":phasedelta,
        "original_complete_S4_center_plus_edge_Loewner_lower":new,
        "source_positive_S4_first_window":first_window_positive,
        "source_Loewner_lower_PSD":exact_psd(new),
        "exact_all_direction_source_robust_cone_PSD":cone_positive,
        "source_parity_cone_certificates":cone,
        "original_S4_verdict":verdict,
        "full_source_direction_certificates":directions,
        "edge_in_Loewner_improvement_is_PSD":exact_psd(phasedelta),
        "RH_proved":False,
    }
