"""Deterministic exact SUCC index-at-infinity & weighted-clock source receipt.

Run from repo root:
  python scripts/mobius_index_infinity_probe.py

No random tests, numerical zeros, fake global RH/source sign claims.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
import sys

# Replay from any working directory without an undeclared editable install.
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.mobius_index_infinity import (
    finite_succ_boundary, finite_fucc_boundary,
    finite_sieve_count, shell_trace, sieve_projection,
    strong_sieve_limit, sieve_succ_commutator,
    exact_prime_jets_from_index_density,
    finite_normalized_trace_escape,sign_mutant_control,
    completed_source_blindness_controls,
)
from observational_succ.weighted_clock_cocycle import (
    memory_weight_bounds, finite_cocycle_composition,
    finite_grid_cocycle, cut_jump_and_unweighted_shift_lower,
    periodic_ghost_mutant,
)


def receipt():
    prime_set=(2,3,5)
    finite=finite_sieve_count(prime_set,210)
    index=finite_succ_boundary(12)
    fucc=finite_fucc_boundary(3,210)
    shell=shell_trace(2,3,210)
    genuine=exact_prime_jets_from_index_density(2,3)
    sieve=strong_sieve_limit(prime_set,(1,2,3,6,7,11,30))
    source_commutator=sieve_succ_commutator(prime_set,6)
    finite_grid=finite_grid_cocycle(6,2,12,2)
    rn=finite_cocycle_composition(6,F(1,2),1,-1,J=15)
    cut=cut_jump_and_unweighted_shift_lower(30)
    ghost=periodic_ghost_mutant(6,F(1,5))
    wrong=sign_mutant_control(2)
    trace_state=finite_normalized_trace_escape(300,1)
    blind=completed_source_blindness_controls()
    if not (finite["integer_source_trace"]==56 and
            finite["additive_profinite_unit_Haar"]==F(4,15) and
            index["finite_commutator_trace"]==0 and
            index["strong_limit_trace"]==1 and
            fucc["finite_commutator_trace"]==0 and
            shell["source_half_density_amplitude_squared"]==F(1,8) and
            genuine["normalized_amplitude_squared"]==F(1,8) and
            source_commutator["finite_sieve_edge_coefficient"]==-1 and
            source_commutator["difference_from_limit"]==-1 and
            rn["composed_sq"]==1 and
            finite_grid["weighted_norms_preserved_by_cocycle"] and
            cut["source_density_ratio_strict_lower"]==200 and
            ghost["integrated_source_mass_added"]==F(6,5) and
            not wrong["mutant_idempotent"] and
            trace_state["fixed_basis_probability"]==F(1,300) and
            blind["zeta_primitive_p2_dirichlet_coefficient"]==1 and
            blind["chi_minus_3_primitive_p2_coefficient"]==-1 and
            blind["unit_W_contact_mutation_effect"]==F(2048,3003) and
            not blind["full_signed_completed_W_identifiable_from_Vp_only"]):
        raise AssertionError("MII_SOURCE_INDEX_GENUINE_PROBE_FAILED")
    return {
        "source":"original integer SUCC + genuine prime FUCC",
        "finite_SUCC_commutator_trace":index["finite_commutator_trace"],
        "strong_limit_SUCC_index_defect_trace":index["strong_limit_trace"],
        "finite_FUCC_p3_commutator_trace":fucc["finite_commutator_trace"],
        "finite_FUCC_p3_bulk_Haar":fucc["limit_defect_bulk_trace_density"],
        "prime_sieve_source_count_at_210":finite["integer_source_trace"],
        "prime_sieve_unit_Haar":finite["additive_profinite_unit_Haar"],
        "signed_Mobius_positive_projection_at_7":sieve_projection(7,prime_set)["projection_diagonal"],
        "sieve_strong_limit_basis_unit":"|1><1|",
        "moving_SUCC_sieve_commutator_at_6":source_commutator["finite_sieve_edge_coefficient"],
        "p2_third_valuation_shell_density":shell["limit_additive_Haar_shell_density"],
        "p2_third_valuation_normalized_half_density_squared":genuine["normalized_amplitude_squared"],
        "true_Connes_Cp_squared":genuine["connes_Cp_squared"],
        "true_Tate_idele_norm":genuine["Tate_one_place_norm"],
        "arithmetic_log_commutator":genuine["original_H_Vp_commutator_symbol"],
        "true_clock_Haar_vs_weight":"distinct original source probability measures",
        "RN_pure_coboundary_loop_squared":rn["composed_sq"],
        "RN_finite_weighted_grid_isometry":finite_grid["weighted_norms_preserved_by_cocycle"],
        "physical_cut_L30_naive_shift_norm_squared_strict_lower":
            cut["source_density_ratio_strict_lower"],
        "periodic_ghost_changes_source_mass":ghost["integrated_source_mass_added"],
        "finite_normalized_trace_unit_basis_mass":trace_state["fixed_basis_probability"],
        "character_source_p2_zeta":blind["zeta_primitive_p2_dirichlet_coefficient"],
        "character_source_p2_chi_minus3":blind["chi_minus_3_primitive_p2_coefficient"],
        "Weil_contact_mutation_autocorrelation_effect":blind["unit_W_contact_mutation_effect"],
        "pure_positive_sieve_identifies_completed_Weil":blind["full_signed_completed_W_identifiable_from_Vp_only"],
        "Connes_canonical_principal_value_matched":False,
        "archimedean_Gamma_two_poles_contact_derived":False,
        "source_signed_completed_Weil_distribution_equated":False,
        "source_Weil_all_test_positive":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    print(json.dumps(receipt(),indent=2,sort_keys=True,default=str))
