"""B10 exact finite receipts; universal claims live in B10.md, not this sweep."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import resource
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.field_limit_countermodels import (  # noqa: E402
    OMEGA, delayed_rival_shadow, unrealizable_limit_prefix,
)
from observational_succ.voyager_profinite_frontier import (  # noqa: E402
    eventual_zero_lift,
)


def threshold_prefix(source: int, horizon: int) -> tuple[int, ...]:
    """Independent oracle for q(U^(n-1)(k)), U(k)=max(1,k-1)."""
    if type(source) is not int or source < 1 or type(horizon) is not int or horizon < 0:
        raise ValueError("Positive original source and nonnegative finite horizon")
    state = source
    word = []
    for _ in range(horizon):
        word.append(int(state == 1))
        state = max(1, state - 1)
    return tuple(word)


def one_pulse_prefix(source: int, horizon: int) -> tuple[int, ...]:
    """Independent oracle, source zero absorbing; positive k pulses at probe k."""
    if type(source) is not int or source < 0 or type(horizon) is not int or horizon < 0:
        raise ValueError("Natural original source and nonnegative finite horizon")
    state = source
    word = []
    for _ in range(horizon):
        word.append(int(state == 1))
        state = max(0, state - 1)
    return tuple(word)


def compact_mutant_report(probe: int, reciprocal_index: int) -> int:
    """Index zero means point 0; index k>0 means compact-source point 1/k."""
    return int(probe == (1 if reciprocal_index == 0 else reciprocal_index))


def receipt() -> dict:
    shadows = []
    for horizon in range(9):
        old = unrealizable_limit_prefix(horizon)
        witness = old["finite_realizing_source"]
        word = threshold_prefix(witness, horizon)
        assert word == old["finite_all_zero_history"] == (0,) * horizon
        assert threshold_prefix(witness, witness)[-1] == 1
        # Exhaustive finite minimality oracle, not an enumeration of all N.
        matching = [k for k in range(1, horizon + 2)
                    if threshold_prefix(k, horizon) == (0,) * horizon]
        assert matching == [horizon + 1]
        shadows.append({"horizon": horizon, "least_cost": witness,
                        "prefix": list(word), "witness_refuting_probe": witness})

    caps = []
    for cap in range(1, 6):
        # One actual probe, n=cap, refutes every member of this exact sublevel.
        outcomes = [threshold_prefix(k, cap)[-1] for k in range(1, cap + 1)]
        assert outcomes == [1] * cap
        caps.append({"cost_cap": cap, "single_refuting_probe": cap,
                     "sublevel_outcomes": outcomes})

    positive = []
    for source in range(7):
        horizon = source + 2
        word = one_pulse_prefix(source, horizon)
        original = OMEGA if source == 0 else source
        prior = tuple(delayed_rival_shadow(n, original) for n in range(1, horizon + 1))
        assert word == prior
        if source:
            candidates = [k for k in range(source + 1)
                          if one_pulse_prefix(k, source) == word[:source]]
            assert candidates == [source]
        positive.append({"source": source, "cost": source, "prefix": list(word)})

    voyager = []
    for horizon in range(7):
        machine = eventual_zero_lift((1,) * horizon, source_id=f"B10-h{horizon}")
        assert machine.trace(horizon) == (1,) * horizon
        assert machine.trace(horizon + 1)[-1] == 0
        voyager.append({"horizon": horizon, "states": len(machine.states),
                        "next_output": machine.trace(horizon + 1)[-1]})

    # Compact source {0} union {1/k}; index k denotes point 1/k.
    # Set trace(0)=e_1 and trace(1/k)=e_k: the zero thread is absent.
    discontinuity = {
        "q1_at_source_zero": compact_mutant_report(1, 0),
        "q1_at_reciprocals_2_through_6":
            [compact_mutant_report(1, k) for k in range(2, 7)]}
    assert discontinuity == {"q1_at_source_zero": 1,
                             "q1_at_reciprocals_2_through_6": [0] * 5}
    for horizon in range(1, 7):
        index = horizon + 1
        assert tuple(compact_mutant_report(n, index)
                     for n in range(1, horizon + 1)) == (0,) * horizon
    paths = ["observational_succ/voyager_profinite_frontier.py",
             "observational_succ/field_limit_countermodels.py",
             "research/2026-10-13/SWARM_ATLAS/B10_probe.py"]
    return {
        "claim_id": "SWM-B10",
        "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "status": "TESTED MODEL: exact finite shadows only",
        "threshold_phantom": shadows,
        "compact_sublevel_refutations": caps,
        "closed_image_noncompact_source_positive": positive,
        "voyager_eventual_zero_source": voyager,
        "compact_source_discontinuous_trace_mutation": discontinuity,
        "zero_cost_noncompact_sublevel_mutation": {
            "finite_prefix_costs_all_zero": True,
            "compact_sublevel_hypothesis_satisfied": False,
            "global_zero_realizer": False,
            "global_nonrealization_is_a_written_proof": True},
        "boundaries": {"finite_tests_prove_infinite_actualization": False,
                       "topological_properties_proved_by_script": False,
                       "physical_original_source_authenticated": False,
                       "full_suite_or_Lean_compiler_run": False},
        "sha256": {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                   for path in paths},
    }


if __name__ == "__main__":
    result = receipt()
    # RUSAGE_SELF.ru_maxrss can retain the pre-exec launcher's high-water mark.
    # /proc's VmHWM belongs to this executed program's current memory image.
    status = dict(line.split(":", 1) for line in Path("/proc/self/status").read_text().splitlines()
                  if ":" in line)
    program_hwm_kib = int(status["VmHWM"].split()[0])
    assert program_hwm_kib < 100 * 1024, (
        f"B10 resource contract exceeded: {program_hwm_kib} KiB")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"B10 program VmHWM: {program_hwm_kib} KiB (<100 MiB); "
          f"process-lifetime ru_maxrss: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} KiB",
          file=sys.stderr)
