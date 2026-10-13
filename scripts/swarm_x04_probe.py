#!/usr/bin/env python3
"""Independent exact X04 audits and finite-horizon/source-factor controls.

Run from repository root. The finite probes accompany paper proofs; they do
not establish the universally quantified theorems by enumeration.
"""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_completion import minimum_prefix_generator
from observational_succ.swarm_dynamics import tent_cylinder, tent_uncertainty


def partitions(length):
    """All set partitions as restricted-growth words; no orbit/lasso formula."""
    if length == 0:
        yield ()
        return
    def extend(prefix, largest):
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for value in range(largest + 2):
            yield from extend(prefix + [value], max(largest, value))
    yield from extend([0], 0)


def partition_minima(length, alphabet_size):
    """Solve path congruence constraints, then assign one output per block.

    Every state used by a finite observed path corresponds to one partition.
    Equal blocks must have equal observed successors, whenever both successors
    have been observed. Any unspecified last successor can be filled using an
    existing block, so satisfying partitions are complete realizability tests.
    """
    if length == 0:
        return {(): 1}, 1
    minima = {}
    examined = 0
    for partition in partitions(length):
        examined += 1
        edges = {}
        valid = True
        for before, after in zip(partition, partition[1:]):
            if before in edges and edges[before] != after:
                valid = False
                break
            edges[before] = after
        if not valid:
            continue
        blocks = max(partition) + 1
        for output in product(range(alphabet_size), repeat=blocks):
            word = tuple(output[state] for state in partition)
            minima[word] = min(minima.get(word, blocks), blocks)
    return minima, examined


def forward_tent(x):
    return 2*x if x <= Q(1, 2) else 2-2*x


def forward_interval(interval):
    """Exact image of an interval, splitting at the sole critical point."""
    lo, hi = interval
    values = [forward_tent(lo), forward_tent(hi)]
    if lo <= Q(1, 2) <= hi:
        values.append(Q(1))
    return min(values), max(values)


def itinerary(x, length):
    word = []
    for _ in range(length):
        word.append(int(x >= Q(1, 2)))
        x = forward_tent(x)
    return tuple(word)


def horizon_surrogate(language):
    """A minimal stationary source with exactly the supplied n-word language.

    Its states are n-words. Existence requires every vertex to have a successor
    in the higher-block graph. No factor from an original source is asserted.
    """
    words = tuple(sorted(set(language)))
    if not words or not words[0] or any(len(w) != len(words[0]) for w in words):
        raise ValueError("A nonempty language at a common positive horizon is required")
    successor = []
    for word in words:
        choices = [i for i, nxt in enumerate(words) if word[1:] == nxt[:-1]]
        if not choices:
            raise ValueError("A dead-end block cannot be the exact stationary language")
        successor.append(choices[0])
    return words, tuple(successor), tuple(word[0] for word in words)


def emitted_language(successor, reports, horizon):
    words = set()
    for initial in range(len(successor)):
        state = initial
        word = []
        for _ in range(horizon):
            word.append(reports[state])
            state = successor[state]
        words.add(tuple(word))
    return words


def de_bruijn_cycle(order, alphabet_size=2):
    """Euler circuit of the (order-1)-block graph, using Hierholzer's algorithm."""
    if order < 1 or alphabet_size < 1:
        raise ValueError("Positive order and alphabet size required")
    start = (0,)*(order-1)
    next_edge = {}
    stack = [(start, None)]
    circuit = []
    while stack:
        vertex, incoming = stack[-1]
        symbol = next_edge.get(vertex, 0)
        if symbol < alphabet_size:
            next_edge[vertex] = symbol + 1
            target = (vertex+(symbol,))[1:] if order > 1 else ()
            stack.append((target, symbol))
        else:
            stack.pop()
            if incoming is not None:
                circuit.append(incoming)
    return tuple(reversed(circuit))


def run():
    b16 = {"binary_words": 0, "ternary_words": 0, "set_partitions_examined": 0}
    for alphabet_size, max_length, key in ((2, 8, "binary_words"), (3, 5, "ternary_words")):
        for length in range(max_length+1):
            minima, examined = partition_minima(length, alphabet_size)
            assert len(minima) == alphabet_size**length
            b16["set_partitions_examined"] += examined
            for word, expected in minima.items():
                got = minimum_prefix_generator(word)
                assert got["state_count"] == expected, (word, expected, got)
                assert tuple(got["stream"](t) for t in range(length)) == word
                b16[key] += 1

    d28 = {"cylinders": 0, "forward_image_checks": 0, "max_depth": 9}
    for depth in range(10):
        seen = set()
        for cell in range(2**depth):
            interval = (Q(cell, 2**depth), Q(cell+1, 2**depth))
            word = itinerary(sum(interval)/2, depth)
            assert word not in seen
            seen.add(word)
            assert tent_cylinder(word) == interval, (word, interval)
            current = interval
            for steps in range(depth+4):
                width = current[1]-current[0]
                expected = Q(1, 2**max(depth-steps, 0))
                assert width == expected
                audit = tent_uncertainty(word, steps)
                assert audit["final_diameter"] == width, audit
                assert audit["final"] == current, audit
                d28["forward_image_checks"] += 1
                current = forward_interval(current)
            d28["cylinders"] += 1

    surrogate_checks = 0
    for horizon in range(1, 9):
        language = set(product((0, 1), repeat=horizon))
        states, step, report = horizon_surrogate(language)
        assert len(states) == 2**horizon
        assert emitted_language(step, report, horizon) == language
        cycle = de_bruijn_cycle(horizon)
        assert len(cycle) == 2**horizon
        cycle_step = tuple((i+1) % len(cycle) for i in range(len(cycle)))
        assert emitted_language(cycle_step, cycle, horizon) == language
        surrogate_checks += 1

    # Every complete binary-output stationary table on <=3 states supplies a
    # right-extendable language. Rebuild that language at each selected horizon.
    stationary_tables = 0
    higher_block_checks = 0
    for size in range(1, 4):
        for step in product(range(size), repeat=size):
            for report in product((0, 1), repeat=size):
                stationary_tables += 1
                for horizon in range(1, 5):
                    language = emitted_language(step, report, horizon)
                    words, rebuilt_step, rebuilt_report = horizon_surrogate(language)
                    assert len(words) == len(language)
                    assert emitted_language(rebuilt_step, rebuilt_report, horizon) == language
                    higher_block_checks += 1
    try:
        horizon_surrogate({(0, 1)})
    except ValueError:
        dead_end_rejected = True
    else:
        raise AssertionError("Impossible exact stationary language accepted")

    # Same original n-prefix, unequal next n-prefix: no quotient update exists.
    factor_witnesses = []
    for horizon in range(1, 9):
        first = (0,)*(horizon+1)
        second = (0,)*horizon+(1,)
        assert first[:horizon] == second[:horizon]
        assert first[1:] != second[1:]
        factor_witnesses.append({"horizon": horizon, "first": first, "second": second})

    # An adaptive prefix-cylinder cover guaranteeing width 2^-k at time t
    # must have every leaf at depth >=t+k. Full uniform-depth cover attains it.
    budget_checks = []
    for time in range(6):
        for precision_bits in range(1, 6):
            required = time+precision_bits
            assert Q(1, 2**(required-time)) == Q(1, 2**precision_bits)
            assert Q(1, 2**max(required-1-time, 0)) > Q(1, 2**precision_bits)
            budget_checks.append([time, precision_bits, required, 2**required])

    # Conflating arbitrary reports with prefix-cylinder reports is false:
    # report the dyadic bin of T^t(x) using only 2^k report values.
    future_bins = {"time": 4, "precision_bits": 3, "report_values": 8,
                   "prefix_cylinder_values_required": 128, "grid_checks": 0}
    for numerator in range(1025):
        x = Q(numerator, 1024)
        future = x
        for _ in range(future_bins["time"]):
            future = forward_tent(future)
        code = min(7, (future*8).numerator//(future*8).denominator)
        assert Q(code, 8) <= future <= Q(code+1, 8)
        future_bins["grid_checks"] += 1

    return {
        "mission": "X04", "status": "PASS", "arithmetic": "exact integers and Fraction",
        "base_commit": "24c93bf0c2bdd4f3f84e9be6367bec15308270ce",
        "B16_independent_path_partition_audit": b16,
        "D28_independent_forward_dyadic_audit": d28,
        "minimal_horizon_surrogates": {"full_binary_orders": surrogate_checks,
            "complete_source_tables": stationary_tables, "higher_block_checks": higher_block_checks,
            "dead_end_language_rejected": dead_end_rejected},
        "same_prefix_different_successor_witnesses": factor_witnesses,
        "prefix_resolution_budget": budget_checks,
        "arbitrary_future_report_counterexample": future_bins,
        "boundaries": {"single_word_00000000_states": 1,
            "all_length_8_words_source_states": 256,
            "binary_star_recognizer_states": 1,
            "time_dependent_external_report_internal_states": 1,
            "constant_observer_states": 1,
            "formal_kernel_claim": False,
            "finite_probes_prove_infinite_chaos": False},
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
