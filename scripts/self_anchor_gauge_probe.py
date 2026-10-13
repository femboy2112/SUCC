"""Exact deterministic reproducibility receipt for the GENIE finite laboratory."""

import itertools
import json

from observational_succ.self_anchor_gauge import (
    CandidateWorld, decoder_audit, equality_signature, minimal_calibrations,
    permutation_worlds, sensor_transport, transported_change,
)


def report():
    cases = {}
    for n in range(1, 6):
        worlds = permutation_worlds(n)
        full = decoder_audit(worlds)
        solutions = minimal_calibrations(worlds)
        expected = tuple(itertools.combinations(range(n), max(0, n - 1)))
        assert solutions == expected
        assert full.sufficient == (n == 1)
        assert all(decoder_audit([w]).sufficient for w in worlds)
        cases[str(n)] = {
            "candidate_dictionaries": len(worlds),
            "individual_world_decoders_valid": True,
            "uncalibrated_cross_world_decoder": full.sufficient,
            "minimum_known_reference_count": len(solutions[0]),
            "minimum_reference_sets": [list(s) for s in solutions],
            "cross_world_collision_witness": None if full.witness is None else [
                {"world": c.world, "state": c.state, "report": list(c.report), "target": c.target}
                for c in full.witness],
        }
    perms = tuple(itertools.permutations(range(2)))
    drifting = tuple(CandidateWorld(
        f"cal={a};source={b}", "source-drift", 1, (0, 1), b,
        (0, 1), a, 0,
    ) for a in perms for b in perms)
    drifting_audit = decoder_audit(drifting, (0, 1))
    assert not drifting_audit.sufficient
    collapse = CandidateWorld("collapse", "lost-information", 1, (0, 1),
                              (0, 0), (0, 1), (0, 1))
    assert minimal_calibrations([collapse]) == ()
    old, new = (0, 1), (1, 0)
    tr = sensor_transport(old, new)
    assert transported_change(old[0], new[0], tr) is False
    assert transported_change(old[0], new[1], tr) is True
    return {
        "status": "EXACT_FINITE_MODEL_ONLY",
        "claims_physical_calibration": False,
        "claims_tlica_empirically_validated": False,
        "claims_academic_priority": False,
        "claims_general_language_discovery": False,
        "source_model": "stipulated complete finite tables; stable mappings only when explicitly constrained",
        "permutation_bases": cases,
        "drifting_mapping_even_full_calibration": drifting_audit.sufficient,
        "noninjective_sensor_repaired_by_calibration": False,
        "self_relative_pattern": list(equality_signature(("red", "blue", "red"))),
        "false_raw_change_under_drift": old[0] != new[0],
        "corrected_change_under_declared_transport": transported_change(old[0], new[0], tr),
        "tests": "python -m unittest discover -s tests -p test_self_anchor_gauge.py -v",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
