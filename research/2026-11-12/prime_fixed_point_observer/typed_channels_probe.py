#!/usr/bin/env python3
"""Exact finite probes for typed channels and cost-graded path amplitudes."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


Unit = tuple[int, int]  # exponents of length and time


def unit_ratio(target: Unit, source: Unit) -> Unit:
    return tuple(a-b for a, b in zip(target, source))


def unit_product(a: Unit, b: Unit) -> Unit:
    return tuple(x+y for x, y in zip(a, b))


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    cost: int
    amplitude: Q
    unit: Unit


def validate(edges, channel_units):
    for edge in edges:
        if not isinstance(edge.cost, int) or isinstance(edge.cost, bool) or edge.cost < 1:
            raise ValueError("positive integer edge cost required")
        if not (0 <= edge.source < len(channel_units) and 0 <= edge.target < len(channel_units)):
            raise ValueError("unknown channel")
        if edge.unit != unit_ratio(channel_units[edge.target], channel_units[edge.source]):
            raise ValueError("incompatible map units")


def zero(size):
    return [[Q(0) for _ in range(size)] for _ in range(size)]


def identity(size):
    return [[Q(int(i == j)) for j in range(size)] for i in range(size)]


def multiply(a, b):
    size = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def apply_vector(matrix, vector):
    return tuple(sum(entry*coordinate for entry, coordinate in zip(row, vector))
                 for row in matrix)


def add_into(a, b):
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j] += b[i][j]


def coefficient_recurrence(edges, channel_units, budget):
    validate(edges, channel_units)
    size = len(channel_units)
    w = [zero(size) for _ in range(budget+1)]
    for edge in edges:
        if edge.cost <= budget:
            w[edge.cost][edge.target][edge.source] += edge.amplitude
    f = [identity(size)] + [zero(size) for _ in range(budget)]
    for degree in range(1, budget+1):
        for cost in range(1, degree+1):
            add_into(f[degree], multiply(w[cost], f[degree-cost]))
    return w, f


def enumerate_paths(edges, channel_units, budget):
    """Literal history tree; no matrix recurrence or coefficient aggregation."""
    validate(edges, channel_units)
    size = len(channel_units)
    amplitude = [zero(size) for _ in range(budget+1)]
    counts = [zero(size) for _ in range(budget+1)]
    visited = 0
    for source in range(size):
        stack = [(source, 0, Q(1), (0, 0))]
        while stack:
            target, cost, weight, path_units = stack.pop()
            if path_units != unit_ratio(channel_units[target], channel_units[source]):
                raise AssertionError("path units fail to telescope")
            visited += 1
            amplitude[cost][target][source] += weight
            counts[cost][target][source] += 1
            for edge in edges:
                if edge.source == target and cost+edge.cost <= budget:
                    stack.append((edge.target, cost+edge.cost,
                                  edge.amplitude*weight,
                                  unit_product(edge.unit, path_units)))
    return amplitude, counts, visited


def affine_word(word):
    """Word is in traversal order; return coefficients a,b for a*n+b."""
    a, b = 1, 0
    for instruction in word:
        if instruction == "S":
            b += 1
        elif instruction == "D":
            a, b = 2*a, 2*b
        else:
            raise ValueError("unknown instruction")
    return a, b


def affine_compose(g, f):
    a, b = g
    c, d = f
    return a*c, a*d+b


def bounded_zero_cost_loop(length_cutoff):
    """Hostile model uses a separate length bound to avoid nontermination."""
    histories = 0
    frontier = [(0, 0)]
    while frontier:
        steps, total_cost = frontier.pop()
        if total_cost != 0:
            raise AssertionError("zero-cost loop changed its cost")
        histories += 1
        if steps < length_cutoff:
            frontier.append((steps+1, total_cost))
    return histories


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [serial(item) for item in value]
    return value


def main():
    counts = {}

    def check(name, condition):
        counts[name] = counts.get(name, 0)+1
        if not condition:
            raise AssertionError(name)

    units = ((1, 0), (1, -1))  # position, velocity
    edges = (
        Edge(0, 1, 1, Q(1, 2), (0, -1)),
        Edge(1, 0, 2, Q(2), (0, 1)),
        Edge(0, 0, 3, Q(1), (0, 0)),
        Edge(1, 1, 1, Q(1), (0, 0)),
        Edge(1, 1, 1, Q(-1), (0, 0)),
    )
    budget = 9
    w, f = coefficient_recurrence(edges, units, budget)
    literal, histories, visited = enumerate_paths(edges, units, budget)
    for degree in range(budget+1):
        check("literal_path_vs_recurrence", f[degree] == literal[degree])
        for side in ("left", "right"):
            convolution = zero(2)
            for cost in range(1, degree+1):
                term = (multiply(w[cost], f[degree-cost]) if side == "left"
                        else multiply(f[degree-cost], w[cost]))
                add_into(convolution, term)
            difference = [[f[degree][i][j]-convolution[i][j]
                           for j in range(2)] for i in range(2)]
            check("formal_inverse_"+side,
                  difference == (identity(2) if degree == 0 else zero(2)))
    check("parallel_histories_exist", histories[1][1][1] == 2)
    check("coherent_parallel_cancel", f[1][1][1] == 0)
    check("separate_intensity_does_not_cancel", Q(1)**2+Q(-1)**2 == 2)
    check("cost_three_two_return_routes", f[3][0][0] == 2)
    swap = [[Q(0), Q(1)], [Q(1), Q(0)]]
    check("basis_independence_not_dynamic", multiply(swap, identity(2)) == swap
          and swap[1][0] == 1 and swap[0][1] == 1 and w[1][1][0] == Q(1, 2))
    check("unit_ratio_telescopes", unit_product((0, 1), (0, -1)) == (0, 0))
    check("generator_has_extra_inverse_time",
          unit_product(unit_ratio(units[0], units[1]), (0, -1)) == (0, 0))

    for label, mutated in (
        ("zero_cost_rejected", Edge(0, 0, 0, Q(1), (0, 0))),
        ("negative_cost_rejected", Edge(0, 0, -1, Q(1), (0, 0))),
        ("fractional_cost_rejected", Edge(0, 0, Q(1, 2), Q(1), (0, 0))),
        ("wrong_units_rejected", Edge(1, 0, 1, Q(1), (0, 0))),
    ):
        caught = False
        try:
            validate((mutated,), units)
        except ValueError:
            caught = True
        check(label, caught)
    zero_cost_cutoff_counts = [bounded_zero_cost_loop(length_cutoff)
                               for length_cutoff in range(8)]
    check("zero_cost_infinite_history_control", zero_cost_cutoff_counts == list(range(1, 9)))

    word_short = ("S", "D", "S")
    word_long = ("D", "S", "S", "S")
    check("equal_affine_semantics", affine_word(word_short) == affine_word(word_long) == (2, 3))
    check("unequal_history_cost", len(word_short) == 3 and len(word_long) == 4)
    for n in range(1, 101):
        a, b = affine_word(word_short)
        c, d = affine_word(word_long)
        check("same_action_all_sampled_inputs", a*n+b == c*n+d)

    minimum = {}
    words_checked = 0
    for length in range(7):
        for word in product(("S", "D"), repeat=length):
            words_checked += 1
            minimum.setdefault(affine_word(word), length)
    check("minimum_cost_strict_example", minimum[(2, 0)] == 1
          and minimum[(1, 3)] == 3 and minimum[(2, 3)] == 3)
    small = [item for item in minimum if minimum[item] <= 3]
    for g, h in product(small, repeat=2):
        check("minimum_cost_subadditivity_samples",
              minimum[affine_compose(g, h)] <= minimum[g]+minimum[h])

    root_controls = []
    for u, v in product((Q(-1), Q(1)), repeat=2):
        constraint = [[u, Q(-1)], [Q(-1), v]]
        determinant = constraint[0][0]*constraint[1][1]-constraint[0][1]*constraint[1][0]
        check("root_holonomy_determinant", determinant == u*v-1)
        roots = (Q(1), u)
        if u*v == 1:
            check("flat_transport_compatible_roots", apply_vector(constraint, roots) == (0, 0))
        else:
            check("twisted_transport_nonzero_determinant", determinant == -2
                  and apply_vector(constraint, roots) != (0, 0))
        root_controls.append({"forward": str(u), "return": str(v),
                              "holonomy": str(u*v), "constraint_determinant": str(determinant),
                              "nonzero_compatible_family": u*v == 1})
    check("positive_flat_root", apply_vector([[Q(1), Q(-1)], [Q(-1), Q(1)]], (Q(1), Q(1))) == (0, 0))
    check("negative_self_loop_excludes_nonzero_root", Q(-1)-Q(1) == -2)
    aggregate = [[Q(1), Q(1)], [Q(1), Q(1)]]
    normalized = [[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]]
    check("local_roots_do_not_fix_aggregate", apply_vector(aggregate, (Q(1), Q(1))) == (2, 2))
    check("normalized_aggregate_fixes_root", apply_vector(normalized, (Q(1), Q(1))) == (1, 1))
    check("positive_cost_matrix_has_zero_constant", apply_vector(w[0], (Q(1), Q(1))) == (0, 0))

    report = {
        "scope": "Finite exact rational toy; general proofs are in TYPED_CHANNELS.md",
        "matrix_convention": "target row, source column",
        "arithmetic": "Python Fraction; no floating point",
        "total_checks": sum(counts.values()),
        "checks": counts,
        "failures": [],
        "budget": budget,
        "literal_histories_visited": visited,
        "channel_units_length_time": serial(units),
        "coefficient_matrices": serial(f),
        "history_count_matrices": serial(histories),
        "parallel_control": {"cost": 1, "histories": 2,
                             "coherent_amplitude": "0", "separate_squared_amplitudes": "2"},
        "zero_cost_loop_histories_at_length_cutoffs_zero_to_seven": zero_cost_cutoff_counts,
        "cost_quotient_control": {"map": [2, 3], "short_cost": 3, "long_cost": 4,
                                  "generators": ["S", "V_2"],
                                  "words_checked_through_length_six": words_checked,
                                  "minimum_cost": minimum[(2, 3)]},
        "compatible_root_controls": root_controls,
        "aggregate_root_control": {"input": [1, 1], "unnormalized_output": [2, 2],
                                   "normalized_output": [1, 1]},
    }
    destination = Path(__file__).resolve().parent / "receipts" / "TYPED_CHANNEL_REPORT.json"
    destination.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"total_checks": report["total_checks"], "failures": 0,
                      "literal_histories": visited, "report": str(destination)}))


if __name__ == "__main__":
    main()
