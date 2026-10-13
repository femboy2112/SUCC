#!/usr/bin/env python3
"""Exact independent X06 reversible-buffer and cost-composition audit.

Finite exhaustive evidence accompanies the paper proof. Memory means a label
making the original -> (retained endpoint, memory) map injective, not a global
permutation of unspecified registers or an energy bound.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_completion import minimum_prefix_generator
from observational_succ.swarm_probability import reversible_memory_lift
from observational_succ.swarm_resource_geometry import (
    debt_stages, finite_completion_possible,
)


def rank(outputs):
    """Largest fiber over a declared nonempty set of original inputs."""
    if not outputs:
        raise ValueError("A nonempty original carrier is required")
    return max(Counter(outputs).values())


def bits(capacity):
    if type(capacity) is not int or capacity < 1:
        raise ValueError("Positive integer memory alphabet required")
    return (capacity - 1).bit_length()


def assignment_oracle(outputs):
    """Brute-force injective encodings; does not calculate fiber counts."""
    for capacity in range(1, len(outputs) + 1):
        for labels in product(range(capacity), repeat=len(outputs)):
            if len(set(zip(outputs, labels))) == len(outputs):
                return capacity
    raise AssertionError("One label per original always suffices")


def common_buffer(endpoint_maps):
    """Optimal one-buffer encoding on a deterministic chain of endpoints.

    Every row enumerates E_n(x) for the SAME original x. Reject a purported
    next map that splits a previous endpoint fiber: that would have obtained
    undeclared information. Returns encodings on reachable images only.
    """
    rows = tuple(tuple(row) for row in endpoint_maps)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("Nonempty common original carrier and chain required")
    for before, after in zip(rows, rows[1:]):
        successor = {}
        for left, right in zip(before, after):
            if left in successor and successor[left] != right:
                raise ValueError("Next endpoint is not a function of the current endpoint")
            successor[left] = right
    # Color each final fiber; this same label separates every earlier fiber.
    used, memory = Counter(), []
    for endpoint in rows[-1]:
        memory.append(used[endpoint])
        used[endpoint] += 1
    images = tuple(tuple(zip(row, memory)) for row in rows)
    if any(len(set(image)) != len(rows[0]) for image in images):
        raise AssertionError("A shared final-fiber coloring must remain injective")
    return max(used.values()), tuple(memory), images


def report_composite(f, g, first_report, second_report):
    """X -> Z x O x P, retaining BOTH declared observation registers."""
    if len(f) != len(first_report) or len(g) != len(second_report):
        raise ValueError("Maps and reports must have matching declared carriers")
    if not f or not g or any(type(y) is not int or not 0 <= y < len(g) for y in f):
        raise ValueError("Nonempty composable finite maps required")
    return tuple((g[y], first_report[x], second_report[y]) for x, y in enumerate(f))


def audit_memory():
    count = 0
    for size in range(1, 6):
        for outputs_size in range(1, 4):
            for outputs in product(range(outputs_size), repeat=size):
                expected = assignment_oracle(outputs)
                actual, lift = reversible_memory_lift(outputs)
                assert actual == expected == rank(outputs)
                assert len(set(lift)) == size
                count += 1
    return {"complete_maps": count, "original_sizes": [1, 5],
            "target_sizes": [1, 3], "oracle": "all memory assignments, ascending capacity"}


def audit_composition():
    count = strict_rank = strict_bits = surjective = 0
    smallest_rank = smallest_bits = None
    for n in range(1, 5):
        for m in range(1, 5):
            for k in range(1, 4):
                for f in product(range(m), repeat=n):
                    for g in product(range(k), repeat=m):
                        composite = tuple(g[y] for y in f)
                        rf, rg, rc = rank(f), rank(g), rank(composite)
                        assert rc <= rf * rg
                        assert bits(rc) <= bits(rf) + bits(rg)
                        assert rc >= rf
                        capacity, memory, images = common_buffer((tuple(range(n)), f, composite))
                        assert capacity == rc
                        assert all(len(set(row)) == n for row in images)
                        # Each encoded-stage map is a bijection between its reachable images.
                        assert all(len(dict(zip(left, right))) == n
                                   for left, right in zip(images, images[1:]))
                        count += 1
                        if len(set(f)) == m and len(set(g)) == k:
                            surjective += 1
                            assert rc >= rg
                            record = {"f": f, "g": g, "ranks": [rf, rg, rc],
                                      "bits": [bits(rf), bits(rg), bits(rc)]}
                            if rc < rf * rg:
                                strict_rank += 1
                                smallest_rank = smallest_rank or record
                            if bits(rc) < bits(rf) + bits(rg):
                                strict_bits += 1
                                smallest_bits = smallest_bits or record
    assert smallest_rank["ranks"] == [2, 2, 3]
    assert len(smallest_rank["f"]) == 3
    assert len(smallest_bits["f"]) == 4
    return {"composable_pairs": count, "surjective_pairs": surjective,
            "strict_rank_pairs_surjective": strict_rank,
            "strict_bit_pairs_surjective": strict_bits,
            "minimal_strict_rank_control": smallest_rank,
            "minimal_strict_bits_control": smallest_bits}


def audit_reports():
    count = 0
    for n in range(1, 4):
        for m in range(1, 4):
            for k in range(1, 3):
                for f in product(range(m), repeat=n):
                    for g in product(range(k), repeat=m):
                        for r in product(range(2), repeat=n):
                            for s in product(range(2), repeat=m):
                                final = report_composite(f, g, r, s)
                                first = tuple(zip(f, r))
                                second = tuple(zip(g, s))
                                # Independently recover fiber sizes by the weighted sum over y.
                                weighted = {}
                                for z, o, p in set(final):
                                    weighted[(z, o, p)] = sum(
                                        sum(1 for x in range(n) if f[x] == y and r[x] == o)
                                        for y in range(m) if g[y] == z and s[y] == p)
                                assert weighted == Counter(final)
                                assert rank(first) <= rank(final) <= rank(first) * rank(second)
                                assert rank(final) <= rank(tuple(g[y] for y in f))
                                capacity, _, _ = common_buffer((tuple(range(n)), first, final))
                                assert capacity == rank(final)
                                count += 1
    return {"two_stage_reported_models": count,
            "reset_bit_without_retained_report": rank((0, 0)),
            "reset_bit_with_retained_bit_report": rank(((0, 0), (0, 1)))}


def audit_debt():
    cases = finite = infinite = coefficients = 0
    for d, a, b, r in product((Q(1, 2), Q(1), Q(2), Q(3)), repeat=4):
        actual = debt_stages(d, a, b, r, 12)
        for n, value in enumerate(actual):
            expected = (a**n * d - b * (a**n - r**n) / (a-r) if a != r
                        else a**n*d - n*b*a**(n-1))
            assert value == expected
            coefficients += 1
        prediction = finite_completion_possible(d, a, b, r)
        if prediction:
            current, power = d, Q(1)
            for n in range(1, 5001):
                current, power = a*current-b*power, power*r
                if current <= 0:
                    break
            else:
                raise AssertionError("Expected finite certificate missing within audit budget")
            finite += 1
        else:
            # Analytic noncompletion certificate: sum of nonnegative and positive terms.
            assert a > r and d-b/(a-r) >= 0 and b/(a-r) > 0
            infinite += 1
        cases += 1
    boundary = debt_stages(2, 1, 1, Q(1, 2), 12)
    assert boundary == tuple(Q(2, 2**n) for n in range(13))
    assert not finite_completion_possible(2, 1, 1, Q(1, 2))
    return {"positive_rational_parameter_tuples": cases,
            "exact_closed_form_values": coefficients,
            "finite_crossing_certificates": finite,
            "noncompletion_coefficient_certificates": infinite,
            "boundary": [str(x) for x in boundary],
            "post_stop_values": "Algebraic recurrence only; operational execution ends at first nonpositive value."}


def audit_separation():
    controls = []
    for n in range(1, 9):
        marker_word = (0,) * (n-1) + (1,)
        generator = minimum_prefix_generator(marker_word)["state_count"]
        assert generator == n
        # One prepared trajectory has one original alternative at every time.
        assert rank((n-1,)) == 1
        constant_generator = minimum_prefix_generator((0,) * n)["state_count"]
        assert constant_generator == 1 and rank((0,) * n) == n
        controls.append({"n": n, "marker_generator_states": n,
                         "single_preparation_buffer": 1,
                         "constant_word_generator_states": 1,
                         "reset_n_originals_buffer": n})
    # Once an original bit is erased, subsequent identity steps do not remove its debt.
    chain = ((0, 1),) + ((0, 0),) * 12
    assert [rank(row) for row in chain] == [1] + [2] * 12
    return {"source_state_vs_origin_buffer_controls": controls,
            "one_reset_then_identity_ranks": [rank(row) for row in chain],
            "recurrence_boundary_is_a_distinct_model": True}


def run():
    return {"mission": "SWM-X06", "parent": "71eaf11e48ca3ccb349858bba64abf36b59ee6f5",
            "status": "PROVED LOCAL paper; independent finite exact audits",
            "memory_audit": audit_memory(), "composition": audit_composition(),
            "retained_reports": audit_reports(), "debt_recurrence_audit": audit_debt(),
            "resource_separation": audit_separation(),
            "scope": "Injective encodings and reachable-image bijections, not unspecified global register permutations or energy."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
