"""Independent bounded table evaluator and guarded single holdout execution.

Word denotations use prefix map composition, unlike the learner's per-state
interpreter. Tables and programmer provenance remain shared dependencies.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = ROOT / "holdout_execution_started.json"
REPORT = ROOT / "witness.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, value):
    with path.open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write("\n")


def certify(table, equations):
    labels = table["states"]
    if not (0 < len(labels) <= 128 and 0 < len(table["actions"]) <= 4):
        raise ValueError("Source exceeds declared resource bounds")
    if len(labels) != len(set(labels)) or len(table["actions"]) != len(set(table["actions"])):
        raise ValueError("Duplicate opaque labels")
    where = {name: i for i, name in enumerate(labels)}
    if len(table["transitions"]) != len(table["actions"]):
        raise ValueError("Incomplete action menu")
    rows = []
    for row in table["transitions"]:
        if len(row) != len(labels) or any(s not in where for s in row):
            raise ValueError("Incomplete or out-of-carrier transition")
        rows.append(tuple(where[s] for s in row))
    words = {tuple(w) for equation in equations for w in equation}
    if any(len(w) > 4 or any(type(v) is not int or not 0 <= v < 3 for v in w) for w in words):
        raise ValueError("Equation outside frozen typed grammar")
    prefixes = {w[:i] for w in words for i in range(len(w) + 1)}
    ordered = sorted(prefixes, key=lambda w: (len(w), w))
    failures, failed_instances, checked = {}, 0, 0
    assignment_count = len(rows) ** 3
    for assignment in itertools.product(range(len(rows)), repeat=3):
        maps = {(): tuple(range(len(labels)))}
        for word in ordered:
            if word:
                previous, transition = maps[word[:-1]], rows[assignment[word[-1]]]
                maps[word] = tuple(transition[s] for s in previous)
        for index, (lhs, rhs) in enumerate(equations):
            for s, (left, right) in enumerate(zip(maps[tuple(lhs)], maps[tuple(rhs)])):
                checked += 1
                if left != right:
                    failed_instances += 1
                    failures.setdefault(index, {
                        "equation": [lhs, rhs], "start_state": labels[s],
                        "assignment": [table["actions"][a] for a in assignment],
                        "left_endpoint": labels[left], "right_endpoint": labels[right]})
    return {"states": len(labels), "actions": len(rows),
            "assignments": assignment_count, "equations": len(equations),
            "equation_state_assignment_checks": checked,
            "failed_instances": failed_instances, "failed_equations": len(failures),
            "first_witness_per_failed_equation": list(failures.values()),
            "peak_word_map_cells": len(prefixes) * len(labels),
            "all_equations_valid": not failures}


def hidden_source_obstruction():
    words = tuple(w for n in range(3) for w in itertools.permutations((0, 1), n))
    source_step = lambda s, a: s if a in s else s + (a,)
    q = lambda s: sum(1 << a for a in s)
    quotient_step = lambda s, a: s | (1 << a)
    squares = [[list(s), a, q(source_step(s, a)), quotient_step(q(s), a)]
               for s in words for a in (0, 1)]
    assert all(left == right for _, _, left, right in squares)
    assert set(q(s) for s in words) == set(range(4))
    left = source_step(source_step((), 0), 1)
    right = source_step(source_step((), 1), 0)
    assert left != right and q(left) == q(right)
    assert all(quotient_step(quotient_step(s, 0), 1) ==
               quotient_step(quotient_step(s, 1), 0) for s in range(4))
    return {"source_states": [list(s) for s in words], "quotient_states": list(range(4)),
            "commuting_squares": squares, "surjective_report": True,
            "noninjective_report_pair": [list(left), list(right)],
            "same_report": q(left), "source_action_commutation": False,
            "quotient_action_commutation": True,
            "all_finite_observation_words_equal": "proved by commuting-square induction",
            "full_hidden_source_identity_inferred": False}


def main():
    if START.exists() or REPORT.exists():
        raise SystemExit("Single holdout execution already started; refusing replay")
    started = time.monotonic()
    freeze = json.loads((ROOT / "freeze_receipt.json").read_text())
    selection = json.loads((ROOT / "selected_laws.json").read_text())
    assert selection["holdout_reads"] == 0
    assert digest(ROOT / "training.json") == freeze["hashes"]["training.json"]
    train = json.loads((ROOT / "training.json").read_text())
    equations = selection["canonical_rewrites"]
    assert 0 < len(equations) <= 120
    training = [certify(t, equations) for t in train]
    assert all(t["all_equations_valid"] for t in training)
    broken = {**train[0], "transitions": [train[0]["transitions"][0][:-1],
                                            *train[0]["transitions"][1:]]}
    try:
        certify(broken, equations)
    except ValueError:
        malformed_rejected = True
    else:
        raise AssertionError("Malformed source unexpectedly certified")
    start = {"stage": 3, "command": "python research/2026-10-13/SWARM_ATLAS/F43/check_once.py",
             "checker_sha256": digest(Path(__file__)),
             "selection_sha256": digest(ROOT / "selected_laws.json"),
             "expected_holdout_sha256": freeze["hashes"]["holdout.json"],
             "one_attempt_guard_created_before_holdout_read": True}
    write_new(START, start)
    # The first and only evaluation reads the newly frozen holdout here.
    assert digest(ROOT / "holdout.json") == start["expected_holdout_sha256"]
    holdout = json.loads((ROOT / "holdout.json").read_text())
    assert len(holdout) == 3
    holdout_results = [certify(t, equations) for t in holdout]
    manifest = json.loads((ROOT / "source_manifest.json").read_text())
    assert digest(ROOT / "source_manifest.json") == freeze["hashes"]["source_manifest.json"]
    roles = manifest["holdout_roles_fixed_before_selection"]
    accepted = all(t["all_equations_valid"] if role == "transfer" else not t["all_equations_valid"]
                   for role, t in zip(roles, holdout_results))
    elapsed = time.monotonic() - started
    result = {**start, "exit": 0 if accepted and elapsed < 25 else 1,
              "training_independent_evaluation": training,
              "malformed_source_rejected": malformed_rejected,
              "holdout": [{"preregistered_role": role, **t}
                          for role, t in zip(roles, holdout_results)],
              "holdout_execution_count": 1, "holdout_consumed_for_selection": False,
              "source_obstruction": hidden_source_obstruction(),
              "elapsed_seconds": round(elapsed, 6), "time_limit_seconds": 25,
              "verdict": "TESTED MODEL" if accepted and elapsed < 25 else "FAILURE"}
    write_new(REPORT, result)
    print(json.dumps({"exit": result["exit"], "elapsed_seconds": result["elapsed_seconds"],
                      "verdict": result["verdict"], "holdout_execution_count": 1,
                      "holdout": [{k: v for k, v in t.items() if k != "first_witness_per_failed_equation"}
                                  for t in result["holdout"]]}, sort_keys=True))
    raise SystemExit(result["exit"])


if __name__ == "__main__":
    main()
