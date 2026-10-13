#!/usr/bin/env python3
"""Reproduce EODCS source-type, obstruction, holdout and coupling receipts."""
from __future__ import annotations

import json

from observational_succ.finite_poset_synthesis import quotient_demo
from observational_succ.voltage_cover_synthesis import language_birth_demo
from observational_succ.eodcs_source_uncertainty import uncertainty_demo
from observational_succ.eodcs_evolutionary_discovery import blind_source_demo


def receipt() -> dict:
    seeded = [blind_source_demo(seed) for seed in range(20)]
    first = quotient_demo()
    graph = language_birth_demo()
    evidence = uncertainty_demo()
    if not all(s["full_source_relatively_certified"] for s in seeded):
        raise AssertionError("Exact bounded source oracle failed")
    if not all(s["exact_oracle_rescue"] != s["genetic_success"] for s in seeded):
        raise AssertionError("Genetic/independent rescue statuses conflated")
    return {
        "status": "EXACT_FINITE_EODCS_CONDITIONAL_SOURCE",
        "poset_quotient_and_adjunction": first,
        "obstruction_trivializing_cover": graph,
        "dependent_uncertain_observations": evidence,
        "blinded_8_to_4_source": {
            "heldout_source_partition": seeded[0]["source_partition"],
            "heldout_source_adjoint": seeded[0]["right_adjoint"],
            "seed_count": len(seeded),
            "genetic_successes": sum(s["genetic_success"] for s in seeded),
            "genetic_failures_rescued_by_exact_oracle":
                sum(s["exact_oracle_rescue"] for s in seeded),
            "all_sources_exhaustively_certified":
                all(s["full_source_relatively_certified"] for s in seeded),
            "no_external_source_authenticated": True,
        },
        "scope": {
            "finite_source_relative_proof": True,
            "genetic_fitness_proves_theorem": False,
            "arbitrary_category_invention_claimed": False,
            "physical_source_authenticated": False,
            "independent_math_priority_claimed": False,
            "completed_Weil_form_positivity_or_RH_proved": False,
            "Lean_kernel_checked": False,
        },
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), sort_keys=True, indent=2))
