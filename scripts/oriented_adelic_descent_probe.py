"""Exact source proof receipt for the oriented-counting -> local adelic bridge.

No zero positions and no global Weil/RH success flags. Run from repo root:
    python scripts/oriented_adelic_descent_probe.py
"""
from __future__ import annotations

import json
from fractions import Fraction as Q

from observational_succ.oriented_mobius_adelic import (
    PrimeIncidence, reversal_ring_obstruction, uniform_negative_no_global_character,
    diagonal_norm_character_receipt,
)
from observational_succ.radial_projective_trace_bridge import (
    independent_three_route_prime_jet,original_weil_prime_tape_gate,
)
from observational_succ.full_prime_tower_transport import (
    projective_from_tate_crosscheck, finite_tower_tate_crosscheck,
)
from observational_succ.connes_compact_open_test_bridge import LocalScaleBall
from observational_succ.mobius_tate_gamma_remainder import (
    finite_tate_gamma_remainder, exact_divisor_cancel,
)


def receipt():
    boolean=PrimeIncidence((2,3,5),(1,1,1)).verdict()
    square=PrimeIncidence((2,),(2,)).verdict()
    if not boolean["oriented_positive_zeta_equals_inverse"]:
        raise AssertionError("boolean Möbius conjugacy falsified")
    if square["oriented_positive_zeta_equals_inverse"]:
        raise AssertionError("p² noninvertible parity mutant accepted")
    tree=independent_three_route_prime_jet(3,4)
    tape=original_weil_prime_tape_gate(120)
    proj=projective_from_tate_crosscheck(3)
    tate=finite_tower_tate_crosscheck((2,3,5),2,5)
    ball=LocalScaleBall(3,Q(4),2)
    gamma=finite_tate_gamma_remainder((2,3,5),2)
    if ball.trace_pairing!=Q(1,2) or not gamma["finite_places_exactly_cancel"]:
        raise AssertionError("Connes/Tate source-matched local contract failed")
    return {
        "base_carrier":"original integer SUCC + genuine prime FUCC",
        "boolean_orientation_exact_inverse":boolean["oriented_positive_zeta_equals_inverse"],
        "p_square_orientation_inverse_false":not square["oriented_positive_zeta_equals_inverse"],
        "p_square_first_defect":square["first_obstruction"],
        "grothendieck_negative_preserves_unit_multiplication":
            reversal_ring_obstruction()["preserves_unital_multiplication"],
        "uniform_finite_minus_descent_to_one_real_norm_character":
            uniform_negative_no_global_character(2,3)["continuous_arch_unitary_norm_character_can_compensate"],
        "valid_norm_character_diagonal_cancellation":
            diagonal_norm_character_receipt(Q(35,12))["sum_is_zero_for_every_prime"],
        "genuine_connes_tate_tree_p3_k4_local_coefficient_squared":tree["BT_radial_squared"],
        "complete_source_wavefront_horizon":tape["horizon"],
        "all_von_mangoldt_prime_power_labels_match":tape["exact_all_prime_power_labels_and_half_density_squares"],
        "original_projective_k0_k1_conditional":proj["conditional_mass"],
        "projective_is_all_positive_valuation_coarsening":False,
        "finite_complete_Tate_stage_matches":tate["agreement_all_local_prime_powers"],
        "genuine_padic_compact_open_trace_test":ball.trace_pairing,
        "Connes_test_reciprocal_half_density_invariant":
            ball.reciprocal_transport()["symmetric_half_density_invariant"],
        "mobius_divisor_source_n36":exact_divisor_cancel(36)["arithmetic_convolution_sum"],
        "Tate_finite_zeta_times_full_mobius_equals_one":gamma["finite_places_exactly_cancel"],
        "remaining_arch_Gamma_R_beta2_symbolic":gamma["remaining_archimedean_Gamma_R_monomial"],
        "PGL2_to_GL1_all_test_intertwiner_proved":False,
        "Connes_identity_principal_value_proved":False,
        "completed_Weil_distribution_identified":False,
        "source_derived_universal_Weil_PSD_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    print(json.dumps(receipt(),default=str,sort_keys=True,indent=2))
