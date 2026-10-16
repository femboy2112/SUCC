#!/usr/bin/env python3
"""Deterministic exact chronological-policy receipts; stdlib only."""
from dataclasses import asdict, replace
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.collective_policy import (  # noqa: E402
    Cost, Outcome, Policy, CollectivePolicyError, capacity_parity_model,
    cross_enabled_model, miniport_model, policy_wire, replay_policy,
    restrict_observers, solve_collective_policy,
)
from observational_succ.consensus_lambda import MiniPort  # noqa: E402
from observational_succ.knowledge_ladder import cross_enabled_ladder_demo  # noqa: E402
from observational_succ.miniature_carrier import Carrier, Mini  # noqa: E402
from observational_succ.source_lambda import Passport  # noqa: E402


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def controls():
    spec = spec_from_file_location("policy_independent_controls", ROOT / "tests/test_collective_policy.py")
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    independent = controls()
    model = cross_enabled_model()
    budget = Cost(8, 4, 4, 1, 1, 9)
    verdict = solve_collective_policy(model, budget)
    require(verdict.winning, "cross-enabled ladder lost")
    replay = replay_policy(model, budget, verdict.policy)
    require(replay.worst_cost == budget, "ladder metric changed")
    ablations = {"+".join(active) or "empty": solve_collective_policy(
        restrict_observers(model, active), budget).winning
        for active in ((), ("A",), ("B",), ("A", "B"))}
    require(ablations == {"empty": False, "A": False, "B": False, "A+B": True}, "isolation control failed")
    shortages = {}
    for i, name in enumerate(asdict(budget)):
        vector = list(budget.vector)
        vector[i] -= 1
        shortages[name] = solve_collective_policy(model, Cost(*vector)).winning
    require(not any(shortages.values()), "budget-coordinate negative control failed")
    old_ladder = cross_enabled_ladder_demo()
    probes = [a for a, _ in replay.leaves[0].history if not a.startswith("send:")]
    require(probes == old_ladder["alternating_probes"], "existing knowledge ladder signature changed")

    hostile = []
    for bits, capacity in ((2, 1), (3, 2)):
        blocked = capacity_parity_model(bits, capacity)
        allowance = Cost(5, 5, observation_bits=5, certificate=6)
        result = solve_collective_policy(blocked, allowance)
        require(not result.winning, "counterfactual probe union admitted")
        witnesses = []
        for selected in combinations(range(bits), capacity):
            # Sources all-zero and one at the unmeasured coordinate agree on
            # every performed report but have distinct original parity.
            missing = next(i for i in range(bits) if i not in selected)
            right = "".join("1" if i == missing else "0" for i in range(bits))
            transcripts = []
            for original in ("0" * bits, right):
                s = next(i for i, src in enumerate(blocked.sources) if src.name == original)
                c = dict(blocked.initial)[s]
                record = []
                for index in selected:
                    action = blocked.actions[index]
                    require(len(action.rows[c]) == 1, "declared pair not executable")
                    outcome = action.rows[c][0]
                    record.append((action.name, outcome.public))
                    c = outcome.after
                require(all(not a.rows[c] for a in blocked.actions), "capacity unexpectedly renewable")
                transcripts.append(record)
            require(transcripts[0] == transcripts[1], "hostile collision missing")
            witnesses.append({"performed": selected, "originals": ("0" * bits, right),
                              "targets": ("0", "1"), "same_public_history": transcripts[0]})
        full = capacity_parity_model(bits, bits)
        repaired = solve_collective_policy(full, Cost(bits, bits, observation_bits=bits, certificate=bits + 1))
        require(repaired.winning, "joint capacity positive control failed")
        replay_policy(full, repaired.budget, repaired.policy)
        hostile.append({"bits": bits, "capacity": capacity, "winning": result.winning,
                        "explored": result.explored, "collision_witnesses": witnesses,
                        "full_capacity_winning": repaired.winning})

    retry = independent.tiny((((Outcome("0", 0), Outcome("retry", 0)),
                               (Outcome("1", 1), Outcome("retry", 1))),))
    retry_budget = Cost(4, 4, observation_bits=8, certificate=5)
    require(not solve_collective_policy(retry, retry_budget).winning, "nondeterminism interpreted existentially")
    lucky = Policy(action="a", branches=(("0", Policy(claim="0")), ("1", Policy(claim="1"))))
    try:
        replay_policy(retry, retry_budget, lucky)
    except CollectivePolicyError as exc:
        lucky_rejection = str(exc)
    else:
        raise AssertionError("replay accepted a missing nondeterministic branch")

    source = "policy-mini-table"
    flip = {"0": "1", "1": "0"}
    parent = Carrier(("0", "1"), {"flip": flip}, {"0": "P0", "1": "P1"}, ("0", "1"), source)
    mini = Mini(("0", "1"), {"flip": flip}, {"0": "R0", "1": "R1"}, "0", source)
    port = MiniPort("bit", parent, mini, {"0": "0", "1": "1"}, {"flip": ("flip",)}, {"P0": "R0", "P1": "R1"})
    integrated, factor = miniport_model(port, Passport(source, 0), {"0": "T0", "1": "T1"})
    mini_result = solve_collective_policy(integrated, Cost(1, 1, observation_bits=1, certificate=2))
    mini_replay = replay_policy(integrated, mini_result.budget, mini_result.policy)
    require(all(leaf.original != leaf.current.carrier for leaf in mini_replay.leaves), "parent flip was not executed")

    exhaustive = independent.exhaustive_controls()
    require(exhaustive["budget_comparisons"] == 10572, "exhaustive coverage changed")
    paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
             "tests/test_collective_policy.py", "scripts/collective_policy_probe.py",
             "research/2026-10-16/COLLECTIVE_POLICY_THEOREM.md"]
    paths += [f"observational_succ/{name}.py" for name in (
        "collective_policy", "knowledge_ladder", "miniature_carrier", "miniature_stochastic",
        "adaptive_proof_policy", "noncommuting_proof_transport", "operational_yoneda_descent",
        "absorbing_frames", "interobserver_channels", "consensus_lambda", "source_lambda")]
    result = {
        "schema": "collective-policy-exact-v1",
        "status": "TESTED_MODEL_FINITE_CHRONOLOGICAL_AND_OR",
        "model_boundary": "declared complete finite source/current-state/resource/readout tables; no physical authentication",
        "cost_coordinate_order": list(asdict(budget)),
        "accounting": {
            "observation_bits": "fixed-width (public outcome, actor-private readout) alphabet per physical action",
            "communication_bits": "fixed-width payload alphabet per explicit send; framing excluded",
            "certificate": "declared per-path verification units, not minimal proof length or policy tree size",
            "resource_stock": "joint-state component, separate from cumulative costs",
        },
        "cross_enabled": {"model": asdict(model), "policy": policy_wire(verdict.policy),
                          "replay": asdict(replay), "worst_cost": asdict(replay.worst_cost),
                          "explored": verdict.explored, "coalition_winning": ablations,
                          "one_less_coordinate_winning": shortages,
                          "existing_knowledge_ladder_signature_matches": True,
                          "two_factor_winning_interaction": 1},
        "hostile_capacity_controls": hostile,
        "nondeterminism": {"retry_at_depth_four_winning": False,
                           "missing_branch_replay_rejection": lucky_rejection},
        "miniport": {"validation": factor, "policy": policy_wire(mini_result.policy),
                     "replay": asdict(mini_replay), "worst_cost": asdict(mini_replay.worst_cost)},
        "exhaustive_oracle": exhaustive,
        "independence_boundary": "distinct algorithms; same author and shared declared tables; no independent physical witness",
        "source_sha256": {path: sha256((ROOT / path).read_bytes()).hexdigest() for path in sorted(paths)},
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
