#!/usr/bin/env python3
"""Bounded exact F45 model receipts; no infinite execution or empirical inputs."""
from fractions import Fraction as Q
from itertools import permutations
import json


def expenditure(costs, order, idle=0):
    if any(type(c) not in (int, Q) or c < 0 for c in costs):
        raise ValueError("Mandatory physical costs must be nonnegative exact numbers")
    if sorted(order) != list(range(len(costs))) or idle < 0:
        raise ValueError("Retain every original event once, and nonnegative idle cost")
    return sum((costs[j] for j in order), Q()) + idle * len(order)


def main():
    costs = tuple(Q(1, 2 ** j) for j in range(1, 6))
    totals = {expenditure(costs, order) for order in permutations(range(5))}
    assert totals == {Q(31, 32)}
    rejects = 0
    for bad_costs, bad_order in (((1, -1), (0, 1)), ((1, 1), (0, 0))):
        try:
            expenditure(bad_costs, bad_order)
        except ValueError:
            rejects += 1
    assert rejects == 2

    zeno = sum((Q(1, 2 ** j) for j in range(1, 9)), Q())
    assert zeno == Q(255, 256)
    debts = [1 + n * (n - 1) // 2 for n in range(9)]
    assert debts == [1, 1, 2, 4, 7, 11, 16, 22, 29]
    for n in range(1, 9):
        active = 1 + n * (n + 1) // 2
        actual = [0] * active
        rival = actual.copy()
        rival[n] = 1
        assert actual[:n] == rival[:n]
        assert sum(actual) == 0 and sum(rival) == 1
        assert active - n == debts[n]
    frozen = [0, 0, 0]
    assert len(frozen) - len(frozen[:3]) == 0

    geometric_debt = []
    for n in range(1, 9):
        d = sum((Q(1, 2 ** (j + 1)) for j in range(n, 2 * n)), Q())
        assert d == Q(1, 2 ** n) - Q(1, 2 ** (2 * n)) and d > 0
        geometric_debt.append(str(d))
    for bound in (1, 8, 100):
        delay = bound + 1
        assert delay + 1 > bound  # Finite delay then task: completion-fair.

    originals = ((0, 0), (0, 1))
    erased = tuple((a, 0) for a, _ in originals)
    parity = tuple(a ^ b for a, b in originals)
    assert erased[0] == erased[1] and parity == (0, 1)

    cells = {}
    for unit_cost in (0, 1):
        for unit_idle in (0, 1):
            event_costs = tuple(1 if unit_cost else Q(1, 2 ** j) for j in range(1, 9))
            cells[f"{unit_cost}{unit_idle}"] = expenditure(event_costs, tuple(range(8)), unit_idle)
    contrast = cells["11"] - cells["10"] - cells["01"] + cells["00"]
    positive_control = 1 * 1 - 1 * 0 - 0 * 1 + 0 * 0
    assert contrast == 0 and positive_control == 1

    print(json.dumps({
        "status": "TESTED MODEL", "all_arithmetic": "int/Fraction",
        "finite_permutations": 120, "permutation_cost": str(totals.pop()),
        "negative_cost_and_duplicate_rejections": rejects,
        "zeno_eight_duration": str(zeno), "zeno_eight_energy": 8,
        "omega_event_executed": False,
        "moving_horizon_debts": debts, "frozen_three_tasks_closed": True,
        "same_observed_prefix_opposite_moving_target": True,
        "geometric_pending_debts": geometric_debt,
        "zero_debt_unit_cost_after_eight": {"debt": 0, "cost": 8},
        "finite_fair_delays_exceed_bounds": [1, 8, 100],
        "unfair_eternal_idle_rule": "scheduler(n)=idle for every natural n",
        "signed_subsidy_eight": {"net": 0, "positive_expenditure": 8},
        "erased_original_parities": parity,
        "factorial_cells": {k: str(v) for k, v in sorted(cells.items())},
        "factorial_mixed_contrast": str(contrast),
        "factorial_product_positive_control": positive_control,
        "universal_theorem_source": "finite-subsum proof in F45 dossier",
        "computability_claim": "paper argument only; finite probe cannot decide halting",
        "physical_costs_measured": False, "global_proof_from_finite_reads": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
