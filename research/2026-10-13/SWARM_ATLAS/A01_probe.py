#!/usr/bin/env python3
"""Exact independent oracle for SWM-A01; no repository helper imports.

Finite enumeration is a regression crucible, not the universal theorem's proof.
Run from the worktree root with --output to save a deterministic receipt.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys

PARENT_SHA = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def maps(domain_size: int, codomain_size: int):
    return itertools.product(range(codomain_size), repeat=domain_size)


def predicates(size: int):
    for mask in range(1 << size):
        yield frozenset(i for i in range(size) if mask & (1 << i))


def square_audit(f, g, p, q, counts):
    """Compute the actual map of dependent-sum witnesses at each y."""
    targets = []
    images = []
    domain_sizes = []
    for y in range(len(g)):
        target = {(x, a) for x in range(len(f)) if f[x] == g[y]
                  for a in range(counts[x])}
        image_list = [(p[w], a) for w in range(len(p)) if q[w] == y
                      for a in range(counts[p[w]])]
        targets.append(target)
        images.append(set(image_list))
        domain_sizes.append(len(image_list))
    return {
        "surjective": all(a == b for a, b in zip(images, targets)),
        "injective": all(n == len(image) for n, image in zip(domain_sizes, images)),
        "domain_sizes": domain_sizes,
        "codomain_sizes": [len(target) for target in targets],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    squares = boolean_checks = family_checks = 0
    weak_not_pullback = incomplete_squares = 0
    for nz in range(3):
        for nx in range(3):
            for ny in range(3):
                for f in maps(nx, nz):
                    for g in maps(ny, nz):
                        actual_pullback = {(x, y) for x in range(nx)
                                           for y in range(ny) if f[x] == g[y]}
                        for nw in range(4):
                            for p in maps(nw, nx):
                                for q in maps(nw, ny):
                                    if any(f[p[w]] != g[q[w]] for w in range(nw)):
                                        continue
                                    squares += 1
                                    comparison_image = {(p[w], q[w]) for w in range(nw)}
                                    surjective = comparison_image == actual_pullback
                                    injective = len(comparison_image) == nw
                                    boolean_all = True
                                    universal_all = True
                                    for support in predicates(nx):
                                        left = {y for y in range(ny)
                                                if any(f[x] == g[y] for x in support)}
                                        right = {q[w] for w in range(nw) if p[w] in support}
                                        boolean_all &= left == right
                                        # All-predecessor quantification uses complements.
                                        universal_left = {y for y in range(ny)
                                                          if all(x in support for x in range(nx)
                                                                 if f[x] == g[y])}
                                        universal_right = {y for y in range(ny)
                                                           if all(p[w] in support for w in range(nw)
                                                                  if q[w] == y)}
                                        universal_all &= universal_left == universal_right
                                        boolean_checks += 1
                                    require(boolean_all == surjective, "Existential BC classification failed")
                                    require(universal_all == surjective, "Universal BC classification failed")
                                    family_all = True
                                    for counts in itertools.product(range(3), repeat=nx):
                                        audit = square_audit(f, g, p, q, counts)
                                        family_all &= audit["surjective"] and audit["injective"]
                                        family_checks += 1
                                    require(family_all == (surjective and injective),
                                            "Proof-relevant BC classification failed")
                                    weak_not_pullback += int(surjective and not injective)
                                    incomplete_squares += int(not surjective)
    # Minimal all-nonempty missing-pair witness.
    missing = {
        "f": [0, 0], "g": [0], "p": [0], "q": [0],
        "support": [1], "left": [0], "right": [],
        "comparison_missing_pair": [1, 0],
    }
    missing_actual = square_audit((0, 0), (0,), (0,), (0,), (0, 1))
    require(not missing_actual["surjective"], "Missing pair mutation unexpectedly passed")
    # Smallest nonempty duplicate-witness square: Boolean truth sees one witness;
    # the proof-relevant sum has two distinct path receipts over the one source pair.
    duplicate = square_audit((0,), (0,), (0, 0), (0, 0), (1,))
    require(duplicate["surjective"] and not duplicate["injective"],
            "Duplicate witness mutation unexpectedly bijective")
    # Destructive carrier saturation, enumerated without decoder implementation.
    saturation_cases = 0
    for nx in range(3):
        for ny in range(3):
            for update in maps(nx, ny):
                for support in predicates(nx):
                    pushed = {update[x] for x in support}
                    repulled = {x for x in range(nx) if update[x] in pushed}
                    descends = any({x for x in range(nx) if update[x] in target} == support
                                   for target in predicates(ny))
                    require(descends == (repulled == set(support)), "Saturation theorem failed")
                    saturation_cases += 1
    # This intervention commutes with report erasure but cannot preserve the bit.
    update = (0, 0)
    old_report = (0, 1)
    after_report = ("erased",)
    report_transport = {0: "erased", 1: "erased"}
    observation_commutes = all(after_report[update[x]] == report_transport[old_report[x]]
                               for x in range(2))
    pushed_support = {update[1]}
    repulled_support = {x for x in range(2) if update[x] in pushed_support}
    require(observation_commutes and repulled_support == {0, 1},
            "Destructive source mutation not reproduced")
    source_change = {
        "original_sources": [0, 1], "update": [0, 0],
        "old_report": [0, 1], "new_report": ["erased"],
        "report_transport": [[0, "erased"], [1, "erased"]],
        "observation_square_commutes": observation_commutes,
        "original_support": [1], "pushed_support": [0],
        "repulled_support": [0, 1], "original_claim_descends": False,
    }
    # Old, immutable receipt h(x)=x restores original-state recovery;
    # recording only the current state cannot.
    historical_map = [(0, 0), (0, 1)]
    require(len(set(historical_map)) == 2, "History repair not injective")
    result = {
        "assignment": "SWM-A01", "parent_sha": PARENT_SHA,
        "python_version": sys.version.split()[0],
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "enumeration_bounds": {"X_Y_Z_sizes": [0, 1, 2], "W_sizes": [0, 1, 2, 3],
                               "family_fibre_sizes": [0, 1, 2]},
        "commuting_squares_checked": squares,
        "predicate_checks": boolean_checks, "finite_family_checks": family_checks,
        "weak_pullbacks_not_pullbacks": weak_not_pullback,
        "incomplete_commuting_squares": incomplete_squares,
        "saturation_cases_checked": saturation_cases,
        "missing_pair_witness": missing,
        "duplicate_pair_witness": {"f": [0], "g": [0], "p": [0, 0], "q": [0, 0],
                                   "comparison": duplicate},
        "destructive_update_witness": source_change,
        "immutable_history_repair": {"map": [[0, 0], [0, 1]],
                                     "mathematically_injective": True,
                                     "actual_available_receipt_assumed": True},
        "all_checks_passed": True,
        "mathematical_proof_source": "A01.md sections 4 and 5",
        "kernel_verified": False, "physical_source_authenticated": False,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
