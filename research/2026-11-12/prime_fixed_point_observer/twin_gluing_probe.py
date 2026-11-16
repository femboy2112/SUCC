"""Exact, independent current-output, gluing and naturality controls.

Only declared present outputs are compared. Histories are not comparator
inputs. This standalone probe imports no other dossier implementation.
Universal results are proved in reviews/twin_observer_adversarial_audit.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


def matrix(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


def mul(a, b):
    assert len(a[0]) == len(b)
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def act(a, x):
    return tuple(sum((u * v for u, v in zip(row, x)), Q(0)) for row in a)


def inv2(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert d != 0
    return matrix(((a[1][1] / d, -a[0][1] / d),
                   (-a[1][0] / d, a[0][0] / d)))


def run():
    counts = {}
    witnesses = {}

    def check(section, statement):
        if not statement:
            raise AssertionError(section)
        counts[section] = counts.get(section, 0) + 1

    # Full overlapping present reports reconstruct the three-bit source.
    sources = tuple(product(range(2), repeat=3))
    left = lambda s: s[:2]
    right = lambda s: s[1:]
    lset = {left(s) for s in sources}
    rset = {right(s) for s in sources}
    pullback = {(l, r) for l in lset for r in rset if l[1] == r[0]}
    image = {(left(s), right(s)) for s in sources}
    check("full_gluing", image == pullback)
    check("full_gluing", len(image) == len(sources) == 8)
    for l, r in pullback:
        recovered = (l[0], l[1], r[1])
        check("full_gluing", recovered in sources)
        check("full_gluing", left(recovered) == l and right(recovered) == r)

    # Same charts with a global parity constraint: overlap alone is insufficient.
    even = tuple(s for s in sources if sum(s) % 2 == 0)
    even_image = {(left(s), right(s)) for s in even}
    check("existence_mutation", {left(s) for s in even} == lset)
    check("existence_mutation", {right(s) for s in even} == rset)
    bad_pair = ((0, 0), (0, 1))
    check("existence_mutation", bad_pair in pullback and bad_pair not in even_image)
    witnesses["matched_but_not_gluable"] = {"left": bad_pair[0], "right": bad_pair[1],
        "forced_triple": [0, 0, 1], "global_even_parity": False}

    # A hidden fourth bit defeats source uniqueness, not every target decoder.
    hidden = tuple(product(range(2), repeat=4))
    for pair in pullback:
        fiber = [s for s in hidden if (s[:2], s[1:3]) == pair]
        check("uniqueness_mutation", len(fiber) == 2)
        check("target_recovery", len({sum(s[:3]) % 2 for s in fiber}) == 1)
        check("target_recovery", {s[3] for s in fiber} == {0, 1})

    # Exhaust all 255 nonempty restrictions of the original source.
    surjective_subsets = 0
    for mask in range(1, 1 << len(sources)):
        subset = tuple(s for j, s in enumerate(sources) if mask & (1 << j))
        ls = {left(s) for s in subset}
        rs = {right(s) for s in subset}
        pairs = {(l, r) for l in ls for r in rs if l[1] == r[0]}
        img = {(left(s), right(s)) for s in subset}
        all_lift = all(any(left(s) == l and right(s) == r for s in subset)
                       for l, r in pairs)
        check("restricted_gluing", all_lift == (img == pairs))
        check("restricted_gluing", len(img) == len(subset))
        surjective_subsets += all_lift
    witnesses["restricted_gluing"] = {"nonempty_source_subsets": 255,
        "all_compatible_pairs_glue": surjective_subsets}

    # Target recovery from the current joint output: compare fiber constancy
    # against exhaustive existence of a truth-valued decoder on its image.
    assignments = tuple(product(range(2), repeat=4))
    factorable = 0
    for lvalues in assignments:
        for rvalues in assignments:
            outputs = tuple(zip(lvalues, rvalues))
            distinct = tuple(sorted(set(outputs)))
            for target in assignments:
                constant = all(outputs[i] != outputs[j] or target[i] == target[j]
                               for i in range(4) for j in range(4))
                exists = False
                for values in product(range(2), repeat=len(distinct)):
                    decoder = dict(zip(distinct, values))
                    if all(decoder[outputs[s]] == target[s] for s in range(4)):
                        exists = True
                        break
                check("target_factorization", constant == exists)
                factorable += constant
    witnesses["target_factorization"] = {"report_target_triples": 4096,
        "factorable_triples": factorable}

    # Transported frames give the same current output; raw histories never enter.
    ident = matrix(((1, 0), (0, 1)))
    e0, e1 = (Q(1), Q(0)), (Q(0), Q(1))
    swap = matrix(((0, 1), (1, 0)))
    check("frame_calibration", act(swap, (Q(2), Q(1))) == (Q(1), Q(2)))
    check("frame_calibration", act(swap, (Q(1), Q(2))) != (Q(1), Q(2)))
    projection = matrix(((1, 0),))
    sign = matrix(((1, 0), (0, -1)))
    check("root_and_coarse_output", act(ident, e0) == act(sign, e0))
    check("root_and_coarse_output", act(ident, e1) != act(sign, e1))
    check("root_and_coarse_output", mul(projection, ident) == mul(projection, sign))
    check("root_and_coarse_output", act(projection, (1, 1)) == act(projection, (1, -1)))

    # Two distinct reversible internal routes have exactly the same current
    # state. They cannot be distinguished by a state-only current output.
    check("history_nonidentifiability", mul(swap, swap) == ident)
    check("history_nonidentifiability", act(mul(swap, swap), (2, 3)) == act(ident, (2, 3)))

    # Naturality checked on generators extends to every enumerated word.
    # The graph is freely generated; no path equivalences are silently added.
    edges = (("a", 0, 1), ("b", 1, 0), ("c", 0, 0), ("d", 1, 1))
    words_checked = 0
    for t in (Q(-3, 2), Q(2, 3), Q(5), Q(11, 7)):
        eta = {0: matrix(((1, t), (0, 1))), 1: matrix(((1, 0), (t, 1)))}
        fm = {"a": matrix(((1, t), (0, 1))), "b": matrix(((0, 1), (-1, 0))),
              "c": matrix(((1, 0), (t, 1))), "d": matrix(((t, 0), (0, 1)))}
        gm = {name: mul(mul(eta[target], fm[name]), inv2(eta[source]))
              for name, source, target in edges}
        for name, source, target in edges:
            check("generator_naturality", mul(eta[target], fm[name]) == mul(gm[name], eta[source]))
        for start in (0, 1):
            frontier = [(start, ident, ident)]
            for length in range(8):
                for end, fword, gword in frontier:
                    check("path_naturality", mul(eta[end], fword) == mul(gword, eta[start]))
                    words_checked += 1
                if length < 7:
                    frontier = [(target, mul(fm[name], fw), mul(gm[name], gw))
                                for end, fw, gw in frontier
                                for name, source, target in edges if source == end]
    witnesses["naturality"] = {"change_of_frame_parameters": 4,
        "maximum_word_length": 7, "words_checked": words_checked}

    # A declared involution is a relation, not a consequence of twin agreement.
    bad = matrix(((1, 0), (0, 2)))
    check("shared_invalid_relation", mul(ident, bad) == mul(bad, ident))
    check("shared_invalid_relation", act(bad, e0) == e0)
    check("shared_invalid_relation", mul(bad, bad) != ident)
    check("valid_relation", mul(sign, sign) == ident)
    eta = matrix(((1, Q(7, 3)), (0, 1)))
    conjugate = mul(mul(eta, sign), inv2(eta))
    check("valid_relation", mul(conjugate, conjugate) == ident)
    p = matrix(((1, 0), (0, 0)))
    check("noninvertible_intertwiner", mul(p, ident) == mul(bad, p))
    check("noninvertible_intertwiner", mul(bad, bad) != ident)

    # Shared relabeling is a coordinate change only with its matching decoder.
    anchored = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 0)))
    f = matrix(((1, 0, 0), (0, 0, 1), (0, 1, 0)))
    relabeled = mul(mul(f, anchored), f)
    root = (Q(1), Q(0), Q(0))
    anchor_input = (Q(0), Q(1), Q(0))
    check("shared_source_relabeling", act(anchored, root) == act(relabeled, root))
    check("shared_source_relabeling", act(anchored, anchor_input) != act(relabeled, anchor_input))
    check("shared_source_relabeling", mul(relabeled, f) == mul(f, anchored))
    check("shared_source_relabeling", mul(mul(f, relabeled), f) == anchored)

    # Finite current input diagnostics cannot see a unitary sign beyond their window.
    for n in (2, 5, 17, 31, 128, 257):
        action = lambda k: -1 if k == n else 1
        for k in range(n):
            check("finite_window", action(k) == 1)
        check("finite_window", action(n) == -1 and abs(action(n) - 1) == 2)

    # Every finite segment has a meeting, but no common finite travel budget
    # serves arbitrarily distant ends. This is an integer-step model only.
    for n in (1, 2, 3, 8, 17, 101):
        for elapsed in range(n + 1):
            check("finite_meeting", (-n + elapsed == n - elapsed) == (elapsed == n))
    for budget in (0, 1, 7, 29, 1000):
        n = budget + 1
        check("no_uniform_meeting", -n + budget != n - budget)

    return {"status": "PASS", "exact_checks": sum(counts.values()),
            "checks_by_section": counts, "witnesses": witnesses,
            "comparison_contract": "Only calibrated current model outputs at the meeting; no raw histories.",
            "scope": "Finite exact controls, with universal proofs in the companion audit; no physical or arithmetic asymptotic claim."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
