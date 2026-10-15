"""Run reproducible finite model receipts for the SUCC three-field taxonomy."""
from __future__ import annotations

from fractions import Fraction
import json

from observational_succ.field_completion_gates import (
    DyadicGlobalCode, FiniteGlobalSource, HaltTrace, antidiagonal_stage,
    stagewise_candidate_failure, noncompact_escape,
    phantom_target_receipt, delayed_discriminator, factorial_solenoid_clock,
    dyadic_zero_boundary
)


def main() -> None:
    source = FiniteGlobalSource(
        "Q-physical-interpretation-DECLARED",
        "standard-dyadic-and-circle",
        "finite-global-source-access"
    )
    dyadic = DyadicGlobalCode(source, 17).coherence(12, 8)
    solenoid = factorial_solenoid_clock(source, 17, 7)
    traces = (HaltTrace(0, 4, 0), HaltTrace(2, 7, 1))
    finite_path = antidiagonal_stage(6, traces)
    delayed_path = stagewise_candidate_failure(2, 6, traces)
    empty_limit = noncompact_escape(13)
    phantom = phantom_target_receipt()
    repaired = phantom_target_receipt(add_separating_probe=True)
    late = delayed_discriminator(1024)
    zero_boundary = dyadic_zero_boundary(128)
    if not (dyadic["bonding_verified"]
            and solenoid["circle_bonding_coherent"]
            and finite_path["stage_member"]
            and not delayed_path["canonical_stage_choices_nested"]
            and empty_limit["inverse_limit_empty"]
            and not phantom["hidden_target_identifiable"]
            and repaired["hidden_target_identifiable"]
            and late["eventual_separation_exists"]
            and not zero_boundary["Boolean_zero_target_continuous_on_Z2"]):
        raise AssertionError("Field proof-gate positive/negative control failed")
    report = {
        "source_status": "DECLARED_EXACT_MODEL_NOT_EMPIRICALLY_AUTHENTICATED",
        "simple": {"dyadic_query_program": dyadic, "connected_circle_stage": solenoid},
        "idealhard_finite_control": {
            "finite_tree_stage": finite_path,
            "greedy_choice_obstruction": delayed_path,
            "universal_kleene_no_computable_path_theorem_proved_by_execution": False,
            "global_path_exists": "CLASSICAL_THEOREM_ONLY"
        },
        "fucked_impossible_noncompact": empty_limit,
        "fucked_phantom": phantom,
        "new_source_probe_repair": repaired,
        "no_uniform_finite_deadline": late,
        "profinite_discontinuous_exact_zero": zero_boundary,
        "finite_only_checks_establish_universal_global_results": False,
        "tate_schwartz_bruhat_functor_certified": False,
        "completed_weil_form_positive": False,
        "RH_proved": False,
    }
    print(json.dumps(report, default=lambda x: str(x)
                     if isinstance(x, Fraction) else repr(x), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
