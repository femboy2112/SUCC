#!/usr/bin/env python3
"""Exact finite C20 controls; no empirical calibration or universal solver."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform
import subprocess

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ROOT = Path(__file__).resolve().parents[3]


def channel(matrix):
    assert matrix and matrix[0]
    assert all(len(row) == len(matrix[0]) for row in matrix)
    assert all(all(isinstance(p, Q) and p >= 0 for p in row)
               and sum(row, Q(0)) == 1 for row in matrix)
    return matrix


def matrix(rows):
    return channel(tuple(tuple(Q(x) for x in row) for row in rows))


def compose(left, right):
    channel(left)
    channel(right)
    assert len(left[0]) == len(right)
    return channel(tuple(tuple(sum((left[i][j] * right[j][k]
                                    for j in range(len(right))), Q(0))
                               for k in range(len(right[0])))
                         for i in range(len(left))))


def value(experiment, utility, prior):
    """Linear optimization: enumerate all extreme deterministic decisions."""
    channel(experiment)
    assert len(prior) == len(experiment) == len(utility)
    assert all(p >= 0 for p in prior) and sum(prior, Q(0)) == 1
    return max(sum((prior[t] * experiment[t][y] * utility[t][rule[y]]
                    for t in range(len(prior))
                    for y in range(len(experiment[0]))), Q(0))
               for rule in product(range(len(utility[0])),
                                   repeat=len(experiment[0])))


def tv(row, other):
    return sum((abs(a - b) for a, b in zip(row, other)), Q(0)) / 2


def history(original, word, erase, reset=False):
    current, receipt = original, []
    for name in word:
        if name == "a":
            receipt.append((name, "*"))
            current = 0 if erase else current
            if reset:
                current = original  # stipulated source-faithful re-preparation
        else:
            assert name == "b"
            receipt.append((name, current))
    return tuple(receipt)


def main():
    executed_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                            text=True).strip()
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"],
                   cwd=ROOT, check=True)
    anchors = ("provenance/IMPORT_MANIFEST.json",
               "observational_succ/probe_coherence.py",
               "observational_succ/operational_yoneda_descent.py",
               "observational_succ/eodcs_relational_choice.py")
    for path in anchors:
        frozen = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        assert (ROOT/path).read_bytes() == frozen, "Source anchor differs from immutable parent"
    e = matrix((("3/4", "1/4"), ("1/4", "3/4")))
    k = matrix((("2/3", "1/3"), ("1/3", "2/3")))
    f = matrix((("7/12", "5/12"), ("5/12", "7/12")))
    assert compose(e, k) == f
    simulations = 0
    for p, q in product((Q(i, 4) for i in range(5)), repeat=2):
        delta = matrix(((p, 1-p), (q, 1-q)))
        assert compose(e, compose(k, delta)) == compose(f, delta)
        simulations += 1
    assert all(x > 0 for row in e + f for x in row)
    assert tv(e[0], e[1]) == Q(1, 2)
    assert tv(f[0], f[1]) == Q(1, 6)
    rejected = 0
    for bad in (((Q(-1), Q(2)), (Q(0), Q(1))),
                ((Q(1), Q(1)), (Q(0), Q(1)))):
        try:
            channel(bad)
        except AssertionError:
            rejected += 1
    assert rejected == 2

    worlds = tuple(product((0, 1), repeat=2))
    a = matrix(tuple((1-x, x) for x, y in worlds))
    b = matrix(tuple((1-y, y) for x, y in worlds))
    ua = tuple(tuple(Q(guess == x) for guess in (0, 1)) for x, y in worlds)
    ub = tuple(tuple(Q(guess == y) for guess in (0, 1)) for x, y in worlds)
    prior = (Q(1, 4),) * 4
    scores = (value(a, ua, prior), value(b, ua, prior),
              value(a, ub, prior), value(b, ub, prior))
    assert scores == (Q(1), Q(1, 2), Q(1, 2), Q(1))
    assert a[0] == a[1] and b[0] != b[1]
    assert b[0] == b[2] and a[0] != a[2]

    assert all(history(t, (name,), False) == history(t, (name,), True)
               for t, name in product((0, 1), ("a", "b")))
    word = ("a", "b")
    kept = tuple(history(t, word, False) for t in (0, 1))
    erased = tuple(history(t, word, True) for t in (0, 1))
    assert erased[0] == erased[1] and kept[0] != kept[1]
    assert kept == tuple(history(t, word, True, reset=True) for t in (0, 1))
    identity = matrix(((1, 0), (0, 1)))
    constant = matrix(((1, 0), (1, 0)))
    reward = identity
    bit_prior = (Q(1, 2), Q(1, 2))
    assert value(identity, reward, bit_prior) == 1
    assert value(constant, reward, bit_prior) == Q(1, 2)

    paths = ("provenance/IMPORT_MANIFEST.json",
             "observational_succ/probe_coherence.py",
             "observational_succ/operational_yoneda_descent.py",
             "observational_succ/eodcs_relational_choice.py",
             "research/2026-10-13/SWARM_ATLAS/C20.md",
             "research/2026-10-13/SWARM_ATLAS/C20_probe.py")
    receipt = {
        "id": "C20", "status": "TESTED MODEL",
        "source_parent": BASE, "executed_head": executed_head,
        "branch": subprocess.check_output(["git", "branch", "--show-current"],
                                           cwd=ROOT, text=True).strip(),
        "python": platform.python_version(),
        "command": "timeout 30s python research/2026-10-13/SWARM_ATLAS/C20_probe.py",
        "arithmetic": "fractions.Fraction only", "exit_on_success": 0,
        "probability_premises": "stipulated rational laws and explicitly uniform priors",
        "source_support_is_not_calibration": True,
        "garbling": {"E": e, "K": k, "F": f,
                     "exact_decision_compositions": simulations,
                     "invalid_kernels_rejected": rejected,
                     "reverse_TV_obstruction": [Q(1, 6), Q(1, 2)]},
        "incomparable": {"source_worlds": worlds, "E": a, "F": b,
                         "guess_a_then_guess_b_values": scores},
        "no_reset": {"word": word, "kept_histories": kept,
                     "erased_histories": erased,
                     "initial_single_action_channels_equal": True,
                     "original_bit_decision_values": [Q(1), Q(1, 2)],
                     "contract": "action-preserving; no extra probe, reorder, hidden-source access or reset",
                     "stipulated_source_faithful_reset_control_passed": True},
        "universal_theorem": "CLASSICAL finite proof reconstructed in C20.md; not machine formalized",
        "academic_novelty_claimed": False,
        "acceptance": "independent crucible and principal review pending",
        "sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    }
    print(json.dumps(receipt, indent=2, default=str, sort_keys=True))


if __name__ == "__main__":
    main()
