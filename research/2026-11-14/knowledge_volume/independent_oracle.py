"""Independent exact hostile audit for SUCC knowledge-volume proposals.

No imports from the repository or its new implementation. All source tables
are exhausted deterministically; no pseudorandom seed or floating point.
This script checks finite cases only. Universal proofs live in the audit note.
"""
from __future__ import annotations

import heapq
import json
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd


def horizon_set(transition, report, horizon):
    power = tuple(range(len(transition)))
    admitted = []
    for n in range(horizon + 1):
        outputs = {}
        valid = True
        for x, value in enumerate(report):
            future = report[power[x]]
            if value in outputs and outputs[value] != future:
                valid = False
                break
            outputs[value] = future
        if valid:
            admitted.append(n)
        power = tuple(transition[x] for x in power)
    return admitted


def separate_target_horizons(transition, evidence, target, horizon):
    power = tuple(range(len(transition)))
    admitted = []
    for n in range(horizon + 1):
        if all(evidence[x] != evidence[y]
               or target[power[x]] == target[power[y]]
               for x in range(len(transition)) for y in range(x)):
            admitted.append(n)
        power = tuple(transition[x] for x in power)
    return admitted


def local_fiber_horizons(transition, report, fiber_value, horizon):
    states = tuple(x for x, value in enumerate(report) if value == fiber_value)
    admitted = []
    for n in range(horizon + 1):
        if len({report[x] for x in states}) == 1:
            admitted.append(n)
        states = tuple(transition[x] for x in states)
    return admitted


def residue_minima(generators):
    """Exact shortest paths modulo the smallest generator (Apéry data)."""
    a = min(generators)
    least = {0: 0}
    pending = [(0, 0)]
    while pending:
        total, residue = heapq.heappop(pending)
        if total != least[residue]:
            continue
        for g in generators:
            nxt = (residue + g) % a
            value = total + g
            if nxt not in least or value < least[nxt]:
                least[nxt] = value
                heapq.heappush(pending, (value, nxt))
    return a, least


def two_rail_realization(generators):
    if not generators:
        c, p = 1, 1
        member = lambda n: n == 0
    else:
        a, least = residue_minima(generators)
        p = 0
        for g in generators:
            p = gcd(p, g)
        c = max(least.values())
        member = lambda n: n % a in least and n >= least[n % a]
    clocks = c + p
    transition = []
    report = []
    for q in range(clocks):
        nxt = q + 1 if q + 1 < clocks else c
        for bit in (0, 1):
            transition.append(2 * nxt + bit)
            report.append((q, 2 if member(q) else bit))
    return tuple(transition), tuple(report), member, c, p


def jump(a, b, n):
    if a == 0:
        if b != 0:
            raise ValueError("Not in the actual two-report source image")
        return F(0)
    return a * (b / a) ** n


def run():
    receipt = {"arithmetic": "integers and fractions.Fraction",
               "random_seed": None,
               "repository_implementation_imports": False}
    table_models = 0
    for t in product(range(4), repeat=4):
        for h in product(range(2), repeat=4):
            H = set(horizon_set(t, h, 24))
            assert 0 in H
            assert all(a + b in H for a in H for b in H if a + b <= 24)
            table_models += 1
    receipt["additivity"] = {"states": 4, "report_alphabet_size": 2,
                              "all_transition_tables": 256,
                              "all_report_tables": 16,
                              "models": table_models, "horizon": 24}

    permutation_models = 0
    for t in permutations(range(4)):
        for h in product(range(3), repeat=4):
            H = horizon_set(t, h, 24)
            d = next(n for n in H if n > 0)
            assert H == list(range(0, 25, d))
            permutation_models += 1
    receipt["permutations"] = {"states": 4, "report_alphabet_size": 3,
                                "all_transition_tables": 24,
                                "all_report_tables": 81,
                                "models": permutation_models, "horizon": 24}

    delayed = horizon_set((1, 2, 2), (0, 0, 1), 8)
    different_target = separate_target_horizons(
        (1, 2, 3, 0), (0, 0, 1, 2), (0, 0, 0, 1), 8)
    one_fiber = local_fiber_horizons((2, 3, 0, 3), (0, 0, 1, 1), 0, 8)
    assert delayed == [0, 2, 3, 4, 5, 6, 7, 8]
    assert different_target == [0, 1, 4, 5, 8]
    assert one_fiber == [0, 1, 3, 5, 7]
    assert 1 in different_target and 2 not in different_target
    assert 1 in one_fiber and 2 not in one_fiber
    receipt["scope_mutants"] = {
        "delayed_three_state_source": delayed,
        "different_target_breaks_addition": different_target,
        "single_current_fiber_breaks_addition": one_fiber,
        "both_overclaim_mutants_rejected": True,
    }

    lasso_models = 0
    largest_lasso = 0
    for size in range(4):
        for generators in combinations(range(1, 9), size):
            t, h, member, c, p = two_rail_realization(generators)
            horizon = max(120, c + 3 * p)
            H = horizon_set(t, h, horizon)
            assert H == [n for n in range(horizon + 1) if member(n)], generators
            # Independent bounded coin-sum DP, not the residue algorithm.
            reachable = {0}
            for n in range(horizon + 1):
                if n in reachable:
                    reachable.update(n + g for g in generators if n + g <= horizon)
            assert H == sorted(reachable), generators
            lasso_models += 1
            largest_lasso = max(largest_lasso, len(t))
    receipt["two_rail_realization"] = {
        "generator_universe": list(range(1, 9)),
        "generator_cardinalities": [0, 1, 2, 3],
        "models": lasso_models, "minimum_horizon": 120,
        "largest_source_states": largest_lasso,
        "three_way_agreement": "quotient horizons, residue minima, coin-sum DP",
        "one_pointed_unary_orbit_claimed": False,
    }

    grid = (F(-7, 3), F(-1), F(-1, 5), F(0), F(1, 7), F(1), F(5, 2))
    jump_checks = 0
    descent_checks = 0
    for x, y in product(grid, repeat=2):
        a, b = x, x * y
        value = x
        for n in range(19):
            assert jump(a, b, n) == value
            value *= y
            jump_checks += 1
        descriptor_next = (F(0), F(0)) if a == 0 else (b, b * b / a)
        assert descriptor_next == (x * y, x * y * y)
        descent_checks += 1
    instability_checks = 0
    for n in range(2, 9):
        for k in range(2, 18):
            eps = F(1, k)
            assert jump(eps ** n, eps ** (n - 1), n) == 1
            assert jump(F(0), F(0), n) == 0
            instability_checks += 1
    phantom = (F(0), F(0), F(1))
    assert phantom[0] * phantom[2] == phantom[1] ** 2
    assert not (phantom[1] == 0 and phantom[2] == 0)

    stable_checks = 0
    source_pairs = tuple(product(grid, repeat=2))
    for bound in (F(0), F(1, 3), F(1), F(3)):
        sources = [(x, y) for x, y in source_pairs if abs(y) <= bound]
        for (x, y), (xx, yy) in product(sources, repeat=2):
            a, b, aa, bb = x, x * y, xx, xx * yy
            for n in range(13):
                error = abs(jump(a, b, n) - jump(aa, bb, n))
                if n == 0:
                    allowance = abs(a - aa)
                elif n == 1:
                    allowance = abs(b - bb)
                else:
                    allowance = ((n - 1) * bound ** n * abs(a - aa)
                                 + n * bound ** (n - 1) * abs(b - bb))
                assert error <= allowance, (bound, a, b, aa, bb, n)
                stable_checks += 1
    receipt["polynomial_source"] = {
        "fraction_grid": [str(q) for q in grid],
        "jump_checks": jump_checks, "maximum_jump_horizon": 18,
        "descent_checks": descent_checks,
        "instability_family_checks": instability_checks,
        "phantom_triple": [str(q) for q in phantom],
        "phantom_shadow_passes_source_rejects": True,
        "bounded_multiplier_error_checks": stable_checks,
        "multiplier_bounds": ["0", "1/3", "1", "3"],
        "maximum_error_horizon": 12,
    }
    receipt["result"] = "PASS"
    return receipt


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
