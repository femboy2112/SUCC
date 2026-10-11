#!/usr/bin/env python3
"""Exact finite twin-observer SUCC research receipt.

The probe menu, prior source family, calibrated mathematics and inferential
ability are identical. Only each observer's focus order differs. Actual
physical source-authentication and universal smooth-path inference are not
claimed by this finite synthetic table.
"""
import json

from observational_succ.twin_circle_observers import twin_circle_demo


def main():
    d = twin_circle_demo()
    assert d["status"] == "EXACT_TWIN_OBSERVER_LANGUAGE_INVARIANCE"
    assert d["initial_mathematical_knowledge_equal"] is True
    assert d["physical_probe_capabilities_identical"] is True
    assert d["reasoning_capability_identical"] is True
    assert d["initial_candidate_windings"] == [1,5,9]
    assert d["after_polynomial_focus_candidates"] == [1,9]
    assert d["after_trig_focus_candidates"] == [1]
    assert d["post_first_relay_knowledge_equal"] is True
    assert d["post_first_relay_operational_history_equal"] is False
    assert d["post_reciprocal_relay_operational_position_equal"] is True
    assert d["algebraic_and_trig_normalized_tangent_agree"] is True
    assert d["smooth_path_finite_jets_can_still_hide_an_extra_loop"] is True
    assert d["full_physical_continuum_trajectory_measured"] is False
    assert d["source_provenance_cryptographically_authenticated"] is False
    assert d["RH_claimed"] is False
    print(json.dumps(d,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
