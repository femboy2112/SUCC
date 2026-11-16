"""Exact finite controls for arithmetic branch sectors and coherent codes.

No physical simulation or collapse law is asserted.  The route oracle below
uses explicit integer divisions, while the existing implementation supplies
the actual fresh-record isometry.  All amplitudes and decisions are exact.
The comparator's outputs are current calibrated arithmetic states; internal
records are used only to verify the construction, not compared as histories
between the two observers.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
from random import Random

from twin_transport import CenteredReturn, flag_branch, fresh_flags


def schedule(raw):
    """Use the existing validated constructor, rejecting invalid input."""
    return tuple(CenteredReturn(q, r) for q, r in raw)


def literal_path(raw, label):
    """Independent integer execution; never calls the return implementation."""
    if type(label) is not int or label < 0:
        raise ValueError("basis label must be a nonnegative integer")
    current, history = label, []
    for q, r in raw:
        quotient, remainder = divmod(current, q)
        history.append(int(remainder != 0))
        if remainder == 0:
            current = quotient * r
    return tuple(history), current


def prefix_lattice(raw):
    ratio, modulus = F(1), 1
    denominators = []
    for q, r in raw:
        ratio *= F(r, q)
        denominators.append(ratio.denominator)
        modulus = lcm(modulus, ratio.denominator)
    image = ratio * modulus
    if image.denominator != 1:
        raise AssertionError("all-success image multiplier is not integral")
    return modulus, image.numerator, tuple(denominators)


def record_cell(raw, record):
    if len(raw) != len(record) or any(type(x) is not int or x not in (0, 1)
                                     for x in record):
        raise ValueError("record must contain one exact bit per step")
    ratio, accepted, rejected = F(1), [], []
    for (q, r), bit in zip(raw, record):
        modulus = ratio.denominator * q // gcd(ratio.numerator, q)
        if bit:
            rejected.append(modulus)
        else:
            accepted.append(modulus)
            ratio *= F(r, q)
    positive_minimum = lcm(*accepted) if accepted else 1
    empty = any(positive_minimum % rejected_modulus == 0
                for rejected_modulus in rejected)
    period = lcm(*(accepted + rejected)) if accepted or rejected else 1
    return positive_minimum, tuple(rejected), ratio, empty, period


def cell_contains(cell, label):
    accepted, rejected, _, _, _ = cell
    return label % accepted == 0 and all(label % q != 0 for q in rejected)


def add_sparse(*states):
    result = {}
    for state in states:
        for key, coefficient in state.items():
            result[key] = result.get(key, F(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def scaled(state, factor):
    return {key: factor * value for key, value in state.items() if factor * value}


def inner(left, right):
    return sum((value * right.get(key, F(0)) for key, value in left.items()), F(0))


def density(state):
    return {(i, j): a * b for i, a in state.items() for j, b in state.items()
            if a * b}


def reduced_arithmetic(flagged):
    result = {}
    for (h, i), a in flagged.items():
        for (g, j), b in flagged.items():
            if h == g:
                result[i, j] = result.get((i, j), F(0)) + a * b
    return {key: value for key, value in result.items() if value}


def reduced_record(flagged):
    result = {}
    for (h, i), a in flagged.items():
        for (g, j), b in flagged.items():
            if i == j:
                result[h, g] = result.get((h, g), F(0)) + a * b
    return {key: value for key, value in result.items() if value}


def formula_channels(raw, source):
    arithmetic, record = {}, {}
    literal = {k: literal_path(raw, k) for k in source}
    for k, a in source.items():
        for ell, b in source.items():
            h, i = literal[k]
            g, j = literal[ell]
            if h == g:
                arithmetic[i, j] = arithmetic.get((i, j), F(0)) + a * b
            if i == j:
                record[h, g] = record.get((h, g), F(0)) + a * b
    return ({key: value for key, value in arithmetic.items() if value},
            {key: value for key, value in record.items() if value})


def run():
    counts = Counter()

    def check(group, condition, context=None):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group], context))

    pairs = [(q, r) for q in range(2, 10) for r in range(1, q) if gcd(q, r) == 1]
    rng = Random(2026111219)
    routes = [(), ((2, 1), (3, 2)), ((3, 2), (2, 1)),
              ((3, 2),) * 9, ((5, 2), (7, 3), (11, 7), (13, 5))]
    routes += [tuple(rng.choice(pairs) for _ in range(rng.randrange(1, 9)))
               for _ in range(72)]
    # Fresh parameter range, outside every random-training pair above.
    holdouts = [((17, 11), (29, 13), (43, 17)),
                ((71, 29), (101, 43)), ((127, 113), (131, 127), (257, 251))]
    routes += holdouts
    maximum_label = 0

    for route_index, raw in enumerate(routes):
        implementation = schedule(raw)
        modulus, image, denominators = prefix_lattice(raw)
        check("prefix_integer_image", modulus >= 1 and image >= 1)
        check("strict_descent_budget", modulus - image >= len(raw))
        if raw:
            previous, _, _ = prefix_lattice(raw[:-1])
            check("nested_success_lattices", modulus % previous == 0)
        labels = list(range(65)) + [97, 257, 1009, 104729]
        labels += [modulus * t for t in (1, 2, 3, 17)]
        if modulus > 1:
            labels += [modulus - 1, modulus + 1]
        labels = sorted(set(labels))
        maximum_label = max(maximum_label, max(labels))
        for k in labels:
            record, output = literal_path(raw, k)
            actual = fresh_flags(implementation, {k: F(1)})
            check("literal_vs_existing_flags", actual == {(record, output): F(1)},
                  (route_index, k))
            accepted = all(bit == 0 for bit in record)
            check("all_success_lattice", accepted == (k % modulus == 0),
                  (route_index, k))
            if accepted:
                check("all_success_output", output == image * (k // modulus))
            direct = {k: F(1)}
            for item in implementation:
                direct = item.apply(direct)
            expected = {image * (k // modulus): F(1)} if k % modulus == 0 else {}
            check("compressed_product", direct == expected)
            check("compressed_vs_flag_sector",
                  flag_branch(actual, (0,) * len(raw)) == direct)
            cell = record_cell(raw, record)
            check("realized_record_cell", cell_contains(cell, k))
            check("record_cell_output_multiplier", cell[2] * k == output)

        # This contains distinct sector patterns and exact non-normalized weights.
        source = {0: F(2, 3), 1: F(3, 5), 2: F(-4, 5),
                  3: F(5, 13), modulus: F(7, 25), 104729: F(-24, 25)}
        flagged = fresh_flags(implementation, source)
        check("enlarged_norm", sum(x*x for x in flagged.values()) == inner(source, source))
        predicted_arithmetic, predicted_record = formula_channels(raw, source)
        check("current_channel_formula", reduced_arithmetic(flagged) == predicted_arithmetic)
        check("complement_channel_formula", reduced_record(flagged) == predicted_record)
        trace = sum(value for (i, j), value in reduced_arithmetic(flagged).items() if i == j)
        check("current_trace", trace == inner(source, source))

        # An arbitrary logical state is encoded into the true path domain.
        logical = {0: F(3, 5), 1: F(-4, 5), 2: F(5, 13), 7: F(12, 13)}
        encoded = {modulus * k: a for k, a in logical.items()}
        expected = {((0,) * len(raw), image * k): a for k, a in logical.items()}
        check("finite_horizon_encoding", fresh_flags(implementation, encoded) == expected)

        for d in (1, 2, 3, 7, 16, 31):
            survivors = [k for k in range(d)
                         if flag_branch(fresh_flags(implementation, {k: F(1)}),
                                        (0,) * len(raw))]
            predicted_rank = 1 + (d - 1) // modulus
            check("twin_postselection_rank", len(survivors) == predicted_rank)
            check("twin_postselection_probability",
                  sum((F(1, d) for _ in survivors), F(0)) == F(predicted_rank, d))

    # Full Boolean-divisibility cells, including unrealizable histories.
    cell_routes = [(), ((3, 2),), ((2, 1), (3, 2)),
                   ((3, 2),) * 5, ((3, 2), (5, 4), (2, 1), (7, 3))]
    empty_cells, realized_cells = 0, 0
    for raw in cell_routes:
        for record in product((0, 1), repeat=len(raw)):
            cell = record_cell(raw, record)
            minimum, _, ratio, empty, period = cell
            if empty:
                empty_cells += 1
            else:
                realized_cells += 1
            check("sector_empty_criterion", cell_contains(cell, minimum) == (not empty))
            if not empty:
                check("sector_positive_witness", literal_path(raw, minimum)[0] == record)
                check("sector_range_integer", (minimum * ratio).denominator == 1)
            for k in range(129):
                check("sector_predicate", cell_contains(cell, k) ==
                      (literal_path(raw, k)[0] == record), (raw, record, k))
                check("sector_periodicity", cell_contains(cell, k) == cell_contains(cell, k + period))
    check("empty_cell_negative_control", empty_cells > 0)

    # General one-step common-range encodings, with independent output templates.
    code_pairs = pairs + [(17, 11), (29, 13), (43, 17), (71, 29)]
    for q, r in code_pairs:
        logical_labels = [j for j in range(1, 13) if j % q != 0]
        for a, b in ((F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
                     (F(5, 13), F(-12, 13)), (F(1), F(0))):
            check("encoding_normalization", a*a + b*b == 1)
            codes = [{q*j: a, r*j: b} for j in logical_labels]
            codes = [{k: x for k, x in c.items() if x} for c in codes]
            for i, code in enumerate(codes):
                j = logical_labels[i]
                flagged = fresh_flags(schedule(((q, r),)), code)
                expected = {((0,), r*j): a, ((1,), r*j): b}
                expected = {key: x for key, x in expected.items() if x}
                check("common_range_factorization", flagged == expected)
                check("current_logical_basis", reduced_arithmetic(flagged) == {(r*j, r*j): F(1)})
                expected_record = density({(0,): a, (1,): b})
                check("fixed_full_record_state", reduced_record(flagged) == expected_record)
                for m, other in enumerate(codes):
                    check("code_orthonormality", inner(code, other) == int(i == m))
            first, second = codes[:2]
            source = add_sparse(scaled(first, F(3, 5)), scaled(second, F(4, 5)))
            output = {r*logical_labels[0]: F(3, 5), r*logical_labels[1]: F(4, 5)}
            flagged = fresh_flags(schedule(((q, r),)), source)
            check("logical_superposition_preserved", reduced_arithmetic(flagged) == density(output))
            check("logical_superposition_record_constant",
                  reduced_record(flagged) == density({(0,): a, (1,): b}))

    t = schedule(((3, 2),))
    same = fresh_flags(t, {3: F(3, 5), 6: F(4, 5)})
    check("same_record_preserves_cross_term", reduced_arithmetic(same)[2, 4] == F(12, 25))
    split = fresh_flags(t, {1: F(3, 5), 3: F(4, 5)})
    check("different_records_remove_cross_term", reduced_arithmetic(split) ==
          {(1, 1): F(9, 25), (2, 2): F(16, 25)})
    alias = fresh_flags(t, {2: F(3, 5), 3: F(4, 5)})
    check("pure_output_can_erase_logical_state", reduced_arithmetic(alias) == {(2, 2): F(1)})
    check("lost_information_in_record", reduced_record(alias) ==
          density({(1,): F(3, 5), (0,): F(4, 5)}))
    check("distinct_classical_inputs_alias", reduced_arithmetic(fresh_flags(t, {2: F(1)})) ==
          reduced_arithmetic(fresh_flags(t, {3: F(1)})))

    # Mutation: deleting the flag or treating all flags as one predicts a cross
    # term which the correct trace explicitly removes.  The false rule fails.
    falsely_erased = {1: F(3, 5), 2: F(4, 5)}
    check("mutation_dropped_record_rejected", density(falsely_erased) != reduced_arithmetic(split))
    forward, backward = ((2, 1), (3, 2)), ((3, 2), (2, 1))
    check("mutation_final_ratio_domain_rejected", prefix_lattice(forward)[:2] == (6, 2))
    check("mutation_final_ratio_domain_rejected", literal_path(forward, 3)[0] != (0, 0))
    check("mutation_denominator_product_rejected", prefix_lattice(backward)[:2] == (3, 1))
    check("mutation_denominator_product_rejected", literal_path(backward, 3)[0] == (0, 0))

    # A two-step code uses an actual common output range of records 00 and
    # 10.  This is a fresh finite-path control of the general AC-05 theorem.
    multi_codes = [{6*j: F(3, 5), 3*j: F(4, 5)} for j in (1, 3, 5, 7)]
    for j, code in zip((1, 3, 5, 7), multi_codes):
        actual = fresh_flags(schedule(forward), code)
        expected = {((0, 0), 2*j): F(3, 5), ((1, 0), 2*j): F(4, 5)}
        check("multiple_record_path_code", actual == expected)
        check("multiple_record_path_pure_output", reduced_arithmetic(actual) ==
              {(2*j, 2*j): F(1)})
    multi_source = add_sparse(scaled(multi_codes[0], F(5, 13)),
                              scaled(multi_codes[1], F(12, 13)))
    multi_actual = fresh_flags(schedule(forward), multi_source)
    check("multiple_record_path_superposition", reduced_arithmetic(multi_actual) ==
          density({2: F(5, 13), 6: F(12, 13)}))
    check("multiple_record_path_environment", reduced_record(multi_actual) ==
          density({(0, 0): F(3, 5), (1, 0): F(4, 5)}))

    for n in range(0, 15):
        raw = ((3, 2),) * n
        modulus, image, _ = prefix_lattice(raw)
        check("repeated_return_exact_powers", (modulus, image) == (3**n, 2**n))
        # Current inputs move with the finite horizon: this refutes norm decay.
        check("moving_input_norm_witness", literal_path(raw, modulus) == ((0,) * n, image))
        for k in range(1, 65):
            if n >= k:
                check("fixed_prefix_termination", literal_path(raw, k)[0] != (0,) * n)
        for k in (1, 2, 4, 5, 7, 8):
            check("infinite_reject_sector_positive_control", literal_path(raw, k) == ((1,) * n, k))

    for malformed in ((0,), (0, 2), (True, 0), (0.0, 0)):
        try:
            record_cell(forward, malformed)
        except ValueError:
            check("malformed_records_rejected", True)
        else:
            check("malformed_records_rejected", False, malformed)

    return {
        "status": "PASS",
        "exact_checks": sum(counts.values()),
        "groups": dict(sorted(counts.items())),
        "finite_scope": {
            "routes": len(routes), "holdout_routes": len(holdouts),
            "maximum_route_length": max(map(len, routes)),
            "largest_tested_source_label": maximum_label,
            "one_step_code_pairs": len(code_pairs),
            "sector_description_routes": len(cell_routes),
            "empty_record_cells": empty_cells, "nonempty_record_cells": realized_cells,
            "seed": 2026111219,
        },
        "explicit_witnesses": {
            "protected_qubit": {
                "return": [3, 2],
                "code_1": {"3": "3/5", "2": "4/5"},
                "code_2": {"6": "3/5", "4": "4/5"},
                "outputs": [2, 4],
                "common_record_amplitudes": ["3/5", "4/5"],
                "common_record_density": [["9/25", "12/25"], ["12/25", "16/25"]],
            },
            "endpoint_multiplier_loses_domain": {
                "route": [[2, 1], [3, 2]], "total_ratio": "1/3",
                "true_input_lattice": 6, "true_output_lattice": 2,
                "rejected_input": 3,
            },
            "pure_current_output_not_information": {
                "return": [3, 2], "distinct_inputs": [2, 3], "same_output": 2,
                "records": [[1], [0]],
            },
            "different_record_cross_term": {
                "source": {"1": "3/5", "3": "4/5"},
                "before_cross_term": "12/25", "after_cross_term": "0",
            },
        },
        "scope": "Finite exact implementation controls of written universal proofs. No physical collapse law, complete infinite traversal, quantum speedup, source-independent truth certificate, or arithmetic asymptotic estimate.",
        "current_output_contract": "Only present calibrated output states and declared decoders are meeting data. Internal record labels are analyst-side verification data, not directly compared observer histories.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered, end="")
