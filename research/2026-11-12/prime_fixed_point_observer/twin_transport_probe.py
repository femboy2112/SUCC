"""Exact finite controls, independent literal oracles, and explicit scope."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import gcd
from pathlib import Path
from random import Random

from twin_transport import (CenteredReturn, LinearChain, LinearMap, Space,
                            flag_branch, fresh_flags, inner, sparse_inner)


def main() -> dict:
    counts: dict[str, int] = {}

    def check(condition: bool, group: str, label: object = "") -> None:
        counts[group] = counts.get(group, 0) + 1
        if not condition:
            raise AssertionError((group, label))

    # Literal path contraction: no matrix-composition or cut helper.
    def path_amplitude(chain, left, right):
        total = F(0)
        for indices in product(*(range(s.dimension) for s in chain.spaces)):
            value = left[indices[0]] * right[indices[-1]]
            for j, arrow in enumerate(chain.arrows):
                value *= arrow.entries[indices[j + 1]][indices[j]]
            total += value
        return total

    rng = Random(2026111203)
    for case in range(96):
        length = case % 5 + 1
        dimensions = [rng.randrange(1, 4) for _ in range(length + 1)]
        spaces = tuple(Space(f"case{case}-fiber{i}", d) for i, d in enumerate(dimensions))
        matrices = tuple(tuple(tuple(F(rng.randrange(-7, 8), rng.randrange(1, 6))
                                    for _ in range(dimensions[j]))
                              for _ in range(dimensions[j + 1]))
                         for j in range(length))
        arrows = tuple(LinearMap(spaces[i], spaces[i + 1], entries)
                       for i, entries in enumerate(matrices))
        chain = LinearChain(spaces, arrows)
        left = tuple(F(rng.randrange(-5, 6), 7) for _ in range(dimensions[0]))
        right = tuple(F(rng.randrange(-5, 6), 11) for _ in range(dimensions[-1]))
        profile = chain.cuts(left, right)
        oracle = path_amplitude(chain, left, right)
        for k, pairing in enumerate(profile.pairings):
            check(pairing == oracle, "cut_pairing_literal_paths", (case, k))
        check(all(d == 0 for d in profile.local_defects), "cut_defects", case)
        # Mutate one declared local matrix, preserving its channel types.
        slot = case % length
        changed = [list(row) for row in matrices[slot]]
        changed[0][0] += F(1, 13)
        other_arrows = list(arrows)
        other_arrows[slot] = LinearMap(spaces[slot], spaces[slot+1], changed)
        other = LinearChain(spaces, tuple(other_arrows))
        mixed = chain.cuts(left, right, reverse_chain=other)
        for k, defect in enumerate(mixed.local_defects):
            check(mixed.pairings[k+1] - mixed.pairings[k] == defect,
                  "local_defect_identity", (case, k))
        endpoint_difference = oracle - path_amplitude(other, left, right)
        check(sum(mixed.local_defects) == endpoint_difference,
              "telescoping_defect", case)

    rational_rotation = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
    reflection = ((F(1), F(0)), (F(0), F(-1)))
    for length in range(1, 13):
        spaces = tuple(Space(f"unitary-{length}-{i}", 2) for i in range(length+1))
        chain = LinearChain(spaces, tuple(LinearMap(spaces[i], spaces[i+1],
                            rational_rotation if i % 2 == 0 else reflection)
                                         for i in range(length)))
        check(all(a.is_unitary() for a in chain.arrows), "unitary_membership", length)
        for left in ((F(1), F(0)), (F(0), F(1)), (F(5, 13), F(12, 13))):
            compatible = chain.total().apply(left)
            for offset in ((F(0), F(0)), (F(2, 7), F(-3, 11))):
                right = tuple(a+b for a, b in zip(compatible, offset))
                gap = inner(offset, offset)
                profile = chain.cuts(left, right)
                for k, observed in enumerate(profile.squared_state_gaps):
                    check(observed == gap, "unitary_present_gap", (length, k))

    # Direct signed-permutation oracle, independent of block-map formulas.
    def basis_oracle(q, r, side, label, adjoint=False):
        if not adjoint:
            if side == 0:
                return (0, r * (label // q), 1) if label % q == 0 else (1, label, 1)
            return (1, q * (label // r), -1) if label % r == 0 else (0, label, 1)
        if side == 0:
            return (0, q * (label // r), 1) if label % r == 0 else (1, label, 1)
        return (1, r * (label // q), -1) if label % q == 0 else (0, label, 1)

    parameters = [(q, r) for q in range(2, 18) for r in range(1, q) if gcd(q, r) == 1]
    parameters += [(29, 11), (43, 17), (71, 29), (101, 43)]
    labels = list(range(129)) + [257, 509, 997, 1009, 104729]
    for q, r in parameters:
        t = CenteredReturn(q, r)
        for label in labels:
            # Original positive-label word V_r, S^(q-r), V_q* then recenter.
            forward = r * (label + 1) + q - r
            literal = forward // q - 1 if forward % q == 0 else None
            check(t.basis(label) == literal, "authentic_affine_word", (q, r, label))
            for side in (0, 1):
                source = ({label: F(1)}, {}) if side == 0 else ({}, {label: F(1)})
                for adjoint in (False, True):
                    destination, index, sign = basis_oracle(q, r, side, label, adjoint)
                    expected = ({index: F(sign)}, {}) if destination == 0 else ({}, {index: F(sign)})
                    result = t.unitary(source, adjoint=adjoint)
                    check(result == expected, "unitary_signed_permutation", (q, r, side, label, adjoint))
                    check(t.unitary(result, adjoint=not adjoint) == source,
                          "unitary_two_sided_inverse", (q, r, side, label, adjoint))
        x = {0: F(3, 5), q: F(4, 5), 997: F(2, 7)}
        y = {1: F(5, 13), q: F(-12, 13), 1009: F(7, 17)}
        ux, uy = t.unitary((x, {})), t.unitary((y, {}))
        check(sum(sparse_inner(a, b) for a, b in zip(ux, uy)) == sparse_inner(x, y),
              "extension_inner_products", (q, r))

    schedules = [((3, 2),) * 5, ((5, 2), (7, 3), (17, 5), (29, 11)),
                 ((71, 29), (101, 43), (17, 5)), ()]
    for schedule in schedules:
        returns = tuple(CenteredReturn(q, r) for q, r in schedule)
        sources = [{label: F(1)} for label in range(257)]
        sources += [{0: F(2, 3), 1: F(-3, 5), 1785: F(5, 7), 104729: F(-7, 11)}]
        for source in sources:
            flags = fresh_flags(returns, source)
            direct = source
            for t in returns:
                direct = t.apply(direct)
            check(flag_branch(flags, (0,) * len(returns)) == direct,
                  "fresh_flags_all_accept", (schedule, source))
            check(sum(v*v for v in flags.values()) == sparse_inner(source, source),
                  "fresh_flags_preserve_norm", (schedule, source))

    t = CenteredReturn(3, 2)
    rejected = {1: F(1)}
    check(t.apply(rejected) == {}, "negative_controls", "compressed rejection")
    check(t.unitary((rejected, {})) == ({}, rejected), "negative_controls", "retained rejection")
    check(t.unitary(t.unitary((rejected, {})))[0] == rejected,
          "negative_controls", "same environment can return rejected mass")
    check(t.apply(t.apply(rejected)) == {}, "negative_controls", "compressed powers differ")
    check(CenteredReturn(5, 1).apply({0: 1}) == CenteredReturn(5, 2).apply({0: 1}),
          "negative_controls", "root agrees")
    check(CenteredReturn(5, 1).apply({5: 1}) != CenteredReturn(5, 2).apply({5: 1}),
          "negative_controls", "whole map differs")
    return {
        "status": "PASS", "exact_checks": sum(counts.values()), "groups": counts,
        "finite_parameters": {"rational_chains": 96, "maximum_chain_length": 12,
                              "return_pairs": len(parameters), "basis_labels": len(labels),
                              "fresh_flag_schedules": len(schedules)},
        "negative_witness": {"return": [3, 2], "input_label": 1,
                             "compressed_two_steps": "zero vector",
                             "same_environment_two_steps_principal_output": "epsilon_1"},
        "comparison_contract": "Current outputs at one selected cut after declared frame transport; internal flag histories are not compared between observers.",
        "scope": "Exact finite calibration of proved formulas; no physical collapse, infinite meeting, global truth certificate, or full category dilation claim.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = main()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered, end="")
