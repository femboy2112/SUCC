#!/usr/bin/env python3
"""Source-relative SUCC transport theorem: machine-readable exact finite receipt.

The proof relies on the declared finite source table and independent algebra.
These values do NOT authenticate a physical source or prove RH.
"""
import json
from observational_succ.precision_transport import precision_transport_demo


def main():
    x = precision_transport_demo()
    assert x["status"] == "SOURCE_RELATIVE_PRECISION_TRANSPORT_EXACT"
    assert x["p"] == 5 and x["source_precision"] == 2
    assert x["step_d"] == 5 and x["precision_debt_digits"] == 1
    assert x["source_repair_output_precision"] == 3
    assert x["coarse_output_precision"] == 2
    assert x["coarse_lost_digits"] == 1 and x["coarse_image_size"] == 5
    assert x["whole_clock_recovered_after_lift"] is True
    assert x["all_25_source_states_inverted"] is True
    assert x["low_digit_claim_minimum_precision"] == 2
    assert x["low_digit_claim_at_coarse_precision"] is True
    assert x["high_digit_claim_minimum_precision"] == 3
    assert x["high_digit_claim_at_coarse_precision"] is False
    assert x["high_digit_claim_after_repair"] is True
    assert len(x["high_digit_collision_witness"]) == 2
    assert x["two_nonzero_lifts_compose"] is True
    assert x["composition_debt_additive"] is True
    assert x["source_preserving_intervention"] is True
    assert x["destructive_intervention_status"] == "source-truth-changed"
    assert x["extra_precision_repairs_destructive_source_change"] is False
    assert x["zero_step_has_finite_full_repair"] is False
    assert x["finite_source_table_authenticates_physical_truth"] is False
    assert x["RH_Gamma_or_Weil_theorem_claimed"] is False
    print(json.dumps(x, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
