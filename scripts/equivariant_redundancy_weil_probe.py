"""Reproducible exact source receipt: observable redundant information gates.

Run from the unchanged original SUCC repo root:
    python scripts/equivariant_redundancy_weil_probe.py

This is an exact finite witness, not a global Connes trace or RH proof.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.equivariant_koszul_descent import (
    prime_chain_lift, trace_obstruction, unit_succ_dimension_control,
    normalized_prime_clock_retraction, original_prime_source_supertrace_gate,
)
from observational_succ.observable_redundancy_forms import (
    ExactSourceExtension, redundancy_controls,
)
from observational_succ.stabilized_exterior_source import (
    exact_stabilized_source_controls,
)
from observational_succ.source_homotopy_defect import (
    grade_zero_defect,pivot_invariance,signed_prime_distribution_receipt,
)


def receipt():
    origin=prime_chain_lift(1,2)
    new=prime_chain_lift(6,7)
    repeat=prime_chain_lift(4,2)
    clock=normalized_prime_clock_retraction(6,5)
    ghost=exact_stabilized_source_controls()
    pivot=pivot_invariance(30)
    local=signed_prime_distribution_receipt(40,{
        2:(F(1),F(1)),4:(F(2),F(-1)),
        8:(F(0),F(1)),9:(F(3),F(0)),6:(F(999),F(999)),
    })
    source=original_prime_source_supertrace_gate(40)
    signed=redundancy_controls()
    if (origin["quotient_homology"]!={1:1} or
        new["quotient_homology"]!={} or
        repeat["new_exterior_basis"]!=() or
        clock["normalized_trace_prime_log_coefficient"]!=1 or
        not ghost["first_ghost_reactivated_by_SUCC"]["newly_observable"] or
        signed["positive_hidden_C_indefinite_full_example"]["effective_source_form"]!=((F(-3),),) or
        not pivot["distinct_homotopies_give_same_source_trace"] or
        not local["no_composite6_source_term"] or
        not source["nonzero_original_prime_power_distribution_missing"]):
        raise AssertionError("source-relative redundancy crucible failed")
    return {
        "source":"SUCC original full integers, Vp and one genuine Weil prime tape",
        "origin_1_to_p_has_H1":origin["quotient_homology"],
        "new_p_at_n6_quotient_acyclic":new["quotient_acyclic"],
        "p_squared_continuation_chain_isomorphism":not repeat["new_exterior_basis"],
        "source_clock_normalized_trace_log5":clock["symbolic_clock_result"],
        "source_chains_prime_trace_erased":source["nonzero_original_prime_power_distribution_missing"],
        "homotopy_prime30_orientation_independence":pivot["distinct_homotopies_give_same_source_trace"],
        "original_signed_prime_test_terms":local["prime_terms"],
        "fake6_ignored_labels":local["ignored_nonprimepower_log_probe_labels"],
        "SUCC_6_to_7_fiber_dim":(
            unit_succ_dimension_control(6)["source_dimension"],
            unit_succ_dimension_control(6)["next_dimension"]),
        "stabilized_ghost_activation":ghost["first_ghost_reactivated_by_SUCC"]["newly_observable"],
        "positive_aux_hidden_negative_effective_schur":signed["positive_hidden_C_indefinite_full_example"]["effective_source_form"],
        "exact_null_aux_can_leave_negative_source":signed["negative_source_recovered_after_null_extension"],
        "source_gamma_contact_poles_reconstructed":False,
        "Connes_canonical_principal_value_identified":False,
        "completed_Weil_all_test_PSD_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    print(json.dumps(receipt(),sort_keys=True,indent=2,default=str))
