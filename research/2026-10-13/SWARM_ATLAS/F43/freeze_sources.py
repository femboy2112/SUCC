"""F43 source authority: generate new opaque tables, once, before learning.

This programmer supplies the source families. The learner receives only the
tables, never this constructor metadata or a named target presentation.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
TRAIN_SEED, HOLDOUT_SEED = 430013, 430099
GRAMMAR = {"variable_count": 3, "maximum_word_length": 4,
           "include_empty_word": True, "objective": "all universal word equalities"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(name, data):
    path = ROOT / name
    with path.open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
    return digest(path)


def opaque(states, actions, step, rng):
    """Independent opaque names and state/action row order for each table."""
    state_order, action_order = list(states), list(actions)
    rng.shuffle(state_order)
    rng.shuffle(action_order)
    labels = {s: f"s{rng.getrandbits(80):020x}" for s in state_order}
    names = {a: f"a{rng.getrandbits(80):020x}" for a in action_order}
    assert len(set(labels.values())) == len(states)
    assert len(set(names.values())) == len(actions)
    table = {"states": [labels[s] for s in state_order],
             "actions": [names[a] for a in action_order],
             "transitions": [[labels[step(s, a)] for s in state_order]
                             for a in action_order]}
    provenance = {"state_order": [repr(s) for s in state_order],
                  "action_order": [repr(a) for a in action_order],
                  "state_labels": [[repr(s), labels[s]] for s in state_order],
                  "action_labels": [[repr(a), names[a]] for a in action_order]}
    return table, provenance


def training_tables():
    """Training generation uses recursion and coordinate-wise first write."""
    rng = random.Random(TRAIN_SEED)
    words = []

    def grow(word):
        words.append(word)
        for a in (0, 1):
            if a not in word:
                grow(word + (a,))

    grow(())
    one = opaque(words, (0, 1),
                 lambda s, a: s if a in s else s + (a,), rng)
    paints = ((0, 1), (1, 0), (-1, 0))
    states = tuple(itertools.product((-1, 0, 1), repeat=2))
    two = opaque(states, paints,
                 lambda s, a: tuple(v if v else p for v, p in zip(s, a)), rng)
    return [one[0], two[0]], [one[1], two[1]]


def fresh_holdout_tables():
    """Separately generated labels/rows and a different word implementation.

    No training table or training RNG is read. Fresh data are still generated
    by this same programmer; this is NOT empirical source independence.
    """
    rng = random.Random(HOLDOUT_SEED)
    alphabet = tuple(range(4))
    words = tuple(w for n in range(5)
                  for w in itertools.permutations(alphabet, n))
    first = opaque(words, alphabet,
                   lambda s, a: tuple(dict.fromkeys((*s, a))), rng)
    union = opaque(tuple(range(8)), (1, 2, 4, 3), lambda s, a: s | a, rng)
    alphabet_control = (0, 1, 2)
    words_control = tuple(w for n in range(4)
                          for w in itertools.permutations(alphabet_control, n))
    last = opaque(words_control, alphabet_control,
                  lambda s, a: tuple(v for v in s if v != a) + (a,), rng)
    return [first[0], union[0], last[0]], [first[1], union[1], last[1]]


def main():
    outputs = ("training.json", "holdout.json", "source_manifest.json",
               "freeze_receipt.json")
    if any((ROOT / p).exists() for p in outputs):
        raise SystemExit("Refusing to overwrite any existing source freeze")
    train, train_maps = training_tables()
    holdout, holdout_maps = fresh_holdout_tables()
    hashes = {"training.json": write_new("training.json", train),
              "holdout.json": write_new("holdout.json", holdout)}
    manifest = {"parent_commit": PARENT, "training_seed": TRAIN_SEED,
                "holdout_seed": HOLDOUT_SEED, "grammar_fixed_before_selection": GRAMMAR,
                "training_families": ["injective words on two letters",
                                      "two-coordinate first-write paints"],
                "holdout_families": ["injective words on four letters",
                                     "three-atom subset union",
                                     "injective words retaining last occurrence"],
                "holdout_roles_fixed_before_selection": ["transfer", "transfer", "mismatch"],
                "training_maps": train_maps, "holdout_maps": holdout_maps,
                "source_independence": "separate seeds, labels, row generation; same programmer",
                "physical_authentication": False}
    hashes["source_manifest.json"] = write_new("source_manifest.json", manifest)
    receipt = {"stage": 1, "command": "python research/2026-10-13/SWARM_ATLAS/F43/freeze_sources.py",
               "exit": 0, "hashes": hashes, "generator_sha256": digest(Path(__file__)),
               "learner_files_exist_at_freeze": any((ROOT / p).exists() for p in
                                                     ("learn.py", "selected_laws.json")),
               "holdout_read_count_by_learner": 0,
               "source_state_counts": {"training": [len(t["states"]) for t in train],
                                       "holdout": [len(t["states"]) for t in holdout]}}
    assert not receipt["learner_files_exist_at_freeze"]
    write_new("freeze_receipt.json", receipt)
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
