"""Bounded generic word-equation learner; input is training.json only.

The supplied grammar is End(S): three action variables, composition, identity,
and words of length <=4. No constructor, normal-form function, family name,
holdout bytes, or expected presentation participates in candidate selection.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VARIABLES, MAX_LENGTH = 3, 4
WORDS = tuple(w for n in range(MAX_LENGTH + 1)
              for w in itertools.product(range(VARIABLES), repeat=n))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def indexed(table):
    states, actions, transitions = (table[k] for k in ("states", "actions", "transitions"))
    if not (1 <= len(states) <= 128 and 1 <= len(actions) <= 4):
        raise ValueError("Declared source/state/action budget exceeded")
    if len(set(states)) != len(states) or len(set(actions)) != len(actions):
        raise ValueError("Opaque labels must be distinct")
    if any(type(s) is not str for s in states + actions):
        raise ValueError("Labels are uninterpreted strings")
    if len(transitions) != len(actions) or any(len(t) != len(states) for t in transitions):
        raise ValueError("Complete source table required")
    positions = {s: i for i, s in enumerate(states)}
    try:
        return tuple(tuple(positions[s] for s in row) for row in transitions)
    except KeyError as e:
        raise ValueError("Transition leaves source carrier") from e


def signatures(table):
    transitions = indexed(table)
    result = {w: [] for w in WORDS}
    for assignment in itertools.product(range(len(transitions)), repeat=VARIABLES):
        for state in range(len(table["states"])):
            for word in WORDS:
                endpoint = state
                for variable in word:
                    endpoint = transitions[assignment[variable]][endpoint]
                result[word].append(endpoint)
    return {w: tuple(result[w]) for w in WORDS}


def classes(signatures_by_source):
    groups = {}
    for word in WORDS:
        signature = tuple(s[word] for s in signatures_by_source)
        groups.setdefault(signature, []).append(word)
    return sorted(groups.values(), key=lambda words: (len(words[0]), words[0]))


def rewrite(word, rules):
    """Contexts and variable-to-variable substitution only; strict descent."""
    while True:
        changed = False
        for lhs, rhs in rules:
            for offset in range(len(word) - len(lhs) + 1):
                assignment = {}
                match = True
                for variable, token in zip(lhs, word[offset:offset + len(lhs)]):
                    if variable in assignment and assignment[variable] != token:
                        match = False
                        break
                    assignment[variable] = token
                if match:
                    new = word[:offset] + tuple(assignment[v] for v in rhs) + word[offset + len(lhs):]
                    if len(new) >= len(word):
                        raise ValueError("Rewrite compression requires length decrease")
                    word, changed = new, True
                    break
            if changed:
                break
        if not changed:
            return word


def opaque_relabel(table):
    """Different names and reverse row/menu order, no source-law mutation."""
    states, actions = table["states"], table["actions"]
    names = {s: f"renamed-state-{i}" for i, s in enumerate(states)}
    return {"states": [names[s] for s in reversed(states)],
            "actions": [f"renamed-action-{i}" for i in reversed(range(len(actions)))],
            "transitions": [[names[s] for s in reversed(table["transitions"][i])]
                            for i in reversed(range(len(actions)))]}


def main():
    started = time.monotonic()
    output = ROOT / "selected_laws.json"
    if output.exists():
        raise SystemExit("Refusing to replace a frozen selection")
    freeze = json.loads((ROOT / "freeze_receipt.json").read_text())
    actual_hash = digest(ROOT / "training.json")
    assert actual_hash == freeze["hashes"]["training.json"]
    sources = json.loads((ROOT / "training.json").read_text())
    assert 1 <= len(sources) <= 3
    sigs = [signatures(t) for t in sources]
    groups = classes(sigs)
    canonical = {word: group[0] for group in groups for word in group}
    rules = [(word, canonical[word]) for word in WORDS if canonical[word] != word]
    basis = []
    for lhs, rhs in rules:
        if len(lhs) > len(rhs) and rewrite(lhs, basis) != rhs:
            basis.append((lhs, rhs))
    relabel_groups = classes([signatures(opaque_relabel(t)) for t in sources])
    assert relabel_groups == groups
    assert all(rewrite(lhs, basis) == rhs for lhs, rhs in rules)
    rejected = []
    for i, left in enumerate(WORDS):
        for right in WORDS[i + 1:]:
            if canonical[left] != canonical[right] and len(left) == len(right) == 2:
                rejected.append([list(left), list(right)])
    receipt = {"stage": 2, "command": "python research/2026-10-13/SWARM_ATLAS/F43/learn.py",
               "exit": 0, "learner_sha256": digest(Path(__file__)),
               "training_sha256": actual_hash, "holdout_reads": 0,
               "grammar": {"variables": VARIABLES, "maximum_length": MAX_LENGTH},
               "candidate_terms": len(WORDS),
               "candidate_equalities": len(WORDS) * (len(WORDS) - 1) // 2,
               "equality_classes": len(groups), "canonical_rewrites": rules,
               "compressed_basis": basis, "equivalence_classes": groups,
               "single_training_family_class_counts": [len(classes([s])) for s in sigs],
               "rejected_length_two_equalities": rejected,
               "relabel_and_row_order_invariant": True,
               "maximum_source_states": 128, "maximum_source_actions": 4,
               "variable_substitutions_per_source_maximum": 64,
               "elapsed_seconds": round(time.monotonic() - started, 6)}
    assert receipt["elapsed_seconds"] < 25
    with output.open("x", encoding="utf-8") as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps({k: v for k, v in receipt.items() if k not in
                     ("canonical_rewrites", "equivalence_classes", "rejected_length_two_equalities")},
                     sort_keys=True))


if __name__ == "__main__":
    main()
