#!/usr/bin/env python3
"""Independent exact checker for a finite future-safe quotient certificate.

Only the Python standard library is imported.  In particular no SUCC generator,
partition algorithm, or witness search is called.  A successful check establishes
the supplied finite transition-table contract, not physical source authenticity.
Absent edges are treated as structural availability data.  A separator ending
in availability mismatch is not automatically an executable physical experiment.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


class CertificateError(ValueError):
    """The supplied certificate does not prove the stated finite contract."""


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def text(value):
    return type(value) is str and bool(value)


def exact_cost(value):
    require(type(value) is list and len(value) == 2,
            "cost must be [integer numerator, positive integer denominator]")
    a, b = value
    require(type(a) is int and type(b) is int and a >= 0 and b > 0,
            "nonnegative exact rational cost required; booleans are not integers")
    return Fraction(a, b)


def check_certificate(document):
    """Check local descent plus separating words between all quotient blocks.

    Local descent proves all-future preservation by induction on words.  One
    valid separating word per distinct block pair proves that no two blocks can
    merge while preserving the same observed/structural trace contract.
    """
    require(type(document) is dict, "certificate must be an object")
    for name in ("states", "actions", "edges"):
        require(type(document.get(name)) is list, f"{name} must be a list")
    require(document["states"], "nonempty finite state carrier required")
    states = {}
    task_schema = None
    for state in document["states"]:
        require(type(state) is dict, "state must be an object")
        name = state.get("name")
        require(text(name) and name not in states, "state names must be unique strings")
        require(text(state.get("source")) and type(state.get("observation")) is str,
                "source must be nonempty string; observation must be string")
        tasks = state.get("tasks")
        require(type(tasks) is list, "tasks must be a list")
        task_ids = set()
        normalized = []
        for task in tasks:
            require(type(task) is list and len(task) == 2 and text(task[0]) and type(task[1]) is str,
                    "task must be [string identifier, string declared result]")
            require(task[0] not in task_ids, "task identifiers must be unique per state")
            task_ids.add(task[0])
            normalized.append(tuple(task))
        keys = tuple(t[0] for t in normalized)
        if task_schema is None:
            task_schema = keys
        require(keys == task_schema, "all states require the same ordered task schema")
        states[name] = (state["source"], state["observation"], tuple(normalized))
    actions = document["actions"]
    require(all(text(a) for a in actions) and len(actions) == len(set(actions)),
            "action names must be unique strings")
    actions = set(actions)
    edges = {}
    for edge in document["edges"]:
        require(type(edge) is dict, "edge must be an object")
        start, action, target = (edge.get(k) for k in ("start", "action", "target"))
        require(text(start) and text(target) and text(action), "edge names must be strings")
        require(start in states and target in states and action in actions,
                "edge refers to an undeclared state or action")
        key = (start, action)
        require(key not in edges, "partial deterministic table cannot repeat an edge key")
        edges[key] = (target, exact_cost(edge.get("cost")))
    cert = document.get("certificate")
    require(type(cert) is dict, "certificate object required")
    blocks = cert.get("blocks")
    require(type(blocks) is list and blocks, "nonempty block list required")
    block_of = {}
    representatives = {}
    for i, block in enumerate(blocks):
        require(type(block) is list and block, "each block must be a nonempty list")
        for x in block:
            require(text(x) and x in states and x not in block_of,
                    "blocks must contain each declared state exactly once")
            block_of[x] = i
        representatives[block[0]] = i
    require(set(block_of) == set(states), "blocks must cover the entire carrier")

    checked_squares = 0
    for block in blocks:
        representative = block[0]
        for x in block:
            require(states[x] == states[representative], "output/task/source mismatch within block")
            for action in actions:
                left = edges.get((representative, action))
                right = edges.get((x, action))
                require((left is None) == (right is None), "availability mismatch within block")
                if left is not None:
                    require(left[1] == right[1], "cost mismatch within block")
                    require(block_of[left[0]] == block_of[right[0]],
                            "successor quotient mismatch: dynamics do not descend")
                checked_squares += 1

    separators = cert.get("separators")
    require(type(separators) is list, "separator list required")
    seen = set()
    witnesses = []
    for witness in separators:
        require(type(witness) is dict, "separator must be an object")
        left, right, word = (witness.get(k) for k in ("left", "right", "word"))
        require(text(left) and text(right) and left in representatives and right in representatives,
                "separator endpoints must be block first representatives")
        i, j = representatives[left], representatives[right]
        require(i != j, "separator must compare distinct blocks")
        pair = tuple(sorted((i, j)))
        require(pair not in seen, "duplicate block-pair separator")
        require(type(word) is list and all(text(a) and a in actions for a in word),
                "separator word must use declared actions")
        x, y = left, right
        kind = None
        for index in range(len(word) + 1):
            if states[x] != states[y]:
                require(index == len(word), "separator has unused suffix after output difference")
                kind = "PRESERVED_OUTPUT"
                break
            if index == len(word):
                break
            a = word[index]
            ex, ey = edges.get((x, a)), edges.get((y, a))
            if (ex is None) != (ey is None):
                require(index + 1 == len(word), "separator has unused suffix after availability difference")
                kind = "STRUCTURAL_LAWFULNESS"
                break
            require(ex is not None, "separator attempts action unavailable on both sides")
            if ex[1] != ey[1]:
                require(index + 1 == len(word), "separator has unused suffix after cost difference")
                kind = "EXACT_COST"
                break
            x, y = ex[0], ey[0]
        require(kind is not None, "word does not separate the supplied block representatives")
        seen.add(pair)
        witnesses.append({"left": left, "right": right, "word": word, "kind": kind})
    require(len(seen) == len(blocks) * (len(blocks) - 1) // 2,
            "every distinct block pair requires a separating word")
    return {"status": "EXACT_FINITE_CERTIFICATE_ACCEPTED", "states": len(states),
            "actions": len(actions), "blocks": len(blocks),
            "local_squares_checked": checked_squares, "separators_checked": len(seen),
            "witnesses": witnesses, "coarsest_for_declared_contract": True,
            "generator_imported": False, "physical_source_authenticated": False,
            "availability_assumed_observable": False, "universal_analytic_positivity_claimed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    try:
        result = check_certificate(json.loads(raw))
    except (CertificateError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "REJECTED", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1) from error
    result["input_sha256"] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
