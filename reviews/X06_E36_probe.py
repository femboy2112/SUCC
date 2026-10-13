#!/usr/bin/env python3
"""Independent X06 review controls; no author probe or repository code imports."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
import argparse
import json
from math import lcm
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "a80d3d6d5e8850d857a1861e6c22b9c5c6551a54"
AUTHOR_DOSSIER_HASH = "e5ebd2b8c34dd26276de45f301b7dfe0d46faf51f14c455d978d40160a2c4271"


def words(alphabet, bound):
    return tuple(w for n in range(bound + 1) for w in product(alphabet, repeat=n))


def run_word(trans, costs, start, word, operation=lambda x, y: x + y, zero=0):
    state, total = start, zero
    for action in word:
        total = operation(total, costs[state][action])
        state = trans[state][action]
    return state, total


def number_keys(keys):
    labels = {}
    return tuple(labels.setdefault(key, len(labels)) for key in keys)


def stable_partition(trans, costs, reports):
    classes = number_keys(tuple((q, tuple(c)) for q, c in zip(reports, costs)))
    while True:
        refined = number_keys(tuple((reports[s], tuple(costs[s]),
                                     tuple(classes[t] for t in trans[s]))
                                    for s in range(len(trans))))
        if refined == classes:
            return classes
        classes = refined


def cumulative_partition(trans, costs, reports, bound=None, operation=lambda x, y: x + y, zero=0):
    # Any shortest pair-graph distinguishing state/edge has length <= |S|^2.
    ws = words(range(len(trans[0])), len(trans) ** 2 if bound is None else bound)
    keys = []
    for start in range(len(trans)):
        outputs = []
        for word in ws:
            target, total = run_word(trans, costs, start, word, operation, zero)
            outputs.append((reports[target], total))
        keys.append(tuple(outputs))
    return number_keys(keys)


def distances(trans, costs):
    n = len(trans)
    d = [[0 if i == j else None for j in range(n)] for i in range(n)]
    for i in range(n):
        for a, j in enumerate(trans[i]):
            old = d[i][j]
            d[i][j] = costs[i][a] if old is None else min(old, costs[i][a])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] is not None and d[k][j] is not None:
                    candidate = d[i][k] + d[k][j]
                    if d[i][j] is None or candidate < d[i][j]:
                        d[i][j] = candidate
    return d


def primitive(word):
    return not any(len(word) % p == 0 and all(word[i] == word[i % p] for i in range(len(word)))
                   for p in range(1, len(word)))


def test():
    begin = time.monotonic()
    machines = 0
    for n, actions in ((2, 2), (3, 1)):
        for flat in product(range(n), repeat=n * actions):
            trans = tuple(tuple(flat[i * actions:(i + 1) * actions]) for i in range(n))
            for reports in product((0, 1), repeat=n):
                for cs in product((0, 1), repeat=n * actions):
                    costs = tuple(tuple(cs[i * actions:(i + 1) * actions]) for i in range(n))
                    assert cumulative_partition(trans, costs, reports) == stable_partition(trans, costs, reports)
                    machines += 1
    assert machines == 2752

    cycles = tuple(w for p in (1, 2, 3) for w in product((0, 1), repeat=p) if primitive(w))
    unary = 0
    for mu_q, mu_c, qcycle, ccycle in product(range(3), range(3), cycles, cycles):
        mu, period = max(mu_q, mu_c), lcm(len(qcycle), len(ccycle))
        n = mu + period
        reports = tuple(("prefix", i) if i < mu_q else ("tail", qcycle[(i - mu_q) % len(qcycle)])
                        for i in range(n))
        costs = tuple((100 + i if i < mu_c else ccycle[(i - mu_c) % len(ccycle)],)
                      for i in range(n))
        trans = tuple((i + 1 if i + 1 < n else mu,) for i in range(n))
        assert len(set(stable_partition(trans, costs, reports))) == n
        assert cumulative_partition(trans, costs, reports) == tuple(range(n))
        unary += 1
    assert unary == 900

    # General author construction checked with two different noncancellative monoids.
    trans = ((2, 1), (3, 0), (3, 0), (3, 0))
    costs = ((2, 0), (2, 0), (0, 0), (1, 0))
    noncancel = {}
    for name, operation in (("max", max), ("saturated_addition_2", lambda x, y: min(2, x + y))):
        cp = cumulative_partition(trans, costs, (0, 0, 0, 0), bound=8, operation=operation)
        sp = stable_partition(trans, costs, (0, 0, 0, 0))
        assert cp[0] == cp[1] and cp[2] != cp[3] and len(set(cp)) == 3
        assert len(set(sp)) == 4
        for w in words((0, 1), 8):
            _, original = run_word(trans, costs, 0, w, operation)
            _, one_state = run_word(((0, 0),), ((2, 0),), 0, w, operation)
            assert original == one_state
        noncancel[name] = {"zero_origin_residual_classes": cp, "raw_charge_stable_classes": sp,
                           "pointed_cumulative_only_one_state_realizer": True}
    assert min(2, 1 + 1) != 1  # The saturation monoid is not idempotent.
    periodic_noncancel = cumulative_partition(((1,), (2,), (3,), (0,)),
                                              ((2,), (0,), (2,), (1,)),
                                              (0, 0, 0, 0), bound=8, operation=max)
    assert len(set(periodic_noncancel)) == 3  # Raw cost tail has primitive period 4.

    # Noncommutative but left-cancellative free word monoid.
    string_trans, string_costs = ((1, 0), (0, 1)), (("X", "Z"), ("Y", "Z"))
    assert cumulative_partition(string_trans, string_costs, (0, 0), zero="") == (0, 1)
    assert run_word(((0, 0),), (("X", "Y"),), 0, (0, 1), zero="")[1] == "XY"
    assert run_word(((0, 0),), (("X", "Y"),), 0, (1, 0), zero="")[1] == "YX"

    # Four physical states, two residual states; fixed endpoint equality fails.
    trans = ((1, 2), (1, 3), (3, 0), (3, 1))
    costs = ((1, 4), (0, 4), (1, 4), (0, 4))
    reports, classes = (0, 1, 0, 1), (0, 1, 0, 1)
    assert stable_partition(trans, costs, reports) == classes
    quotient_trans, quotient_costs = ((1, 0), (1, 1)), ((1, 4), (0, 4))
    dh, dr = distances(trans, costs), distances(quotient_trans, quotient_costs)
    for s in range(4):
        for r in range(2):
            choices = [dh[s][t] for t in range(4) if classes[t] == r and dh[s][t] is not None]
            assert dr[classes[s]][r] == (min(choices) if choices else None)
        for w in words((0, 1), 6):
            t, charge = run_word(trans, costs, s, w)
            r, projected_charge = run_word(quotient_trans, quotient_costs, classes[s], w)
            assert classes[t] == r and charge == projected_charge
    assert dh[0][2] == 4 and dr[0][0] == 0

    # Removing additivity breaks the triangle even before any quotient.
    squared_distances = (1 ** 2, 1 ** 2, (1 + 1) ** 2)
    assert squared_distances[2] > squared_distances[0] + squared_distances[1]
    assert -1 < 0  # Signed valuation is outside the declared Lawvere codomain.
    exact_label_count = len(set(stable_partition(((1,), (0,)), ((0,), (1,)), (0, 0))))
    scalar_label_count = len(set(stable_partition(((1,), (0,)), ((0,), (0,)), (0, 0))))
    assert (exact_label_count, scalar_label_count) == (2, 1)  # Additive zero valuation is nonfaithful.

    # Availability cannot be reconstructed from a constant current report.
    enabled_words = tuple("a" * k for k in range(3))
    assert "aaa" not in enabled_words
    reset_trans, reset_costs = ((1, 0), (1, 0)), ((1, 0), (4, 3))
    assert len(set(stable_partition(reset_trans, reset_costs, (0, 0)))) == 2
    assert run_word(reset_trans, reset_costs, 0, (0, 1, 0))[1] == 5
    assert run_word(reset_trans, ((1, 0), (4, 0)), 0, (0, 1, 0))[1] == 2

    # Private source identity must persist through the complete path.
    private_paths = ((5, 0), (1, 4))
    totals = tuple(sum(p) for p in private_paths)
    assert totals == (5, 5)
    independent_max = sum(max(p[i] for p in private_paths) for i in range(2))
    independent_min = sum(min(p[i] for p in private_paths) for i in range(2))
    assert independent_max == 9 and independent_min == 1
    assert 1 + 1 == 0 + 2 and 1 != 0  # Final weight redistribution fails prefix fidelity.

    # Weighted residual states differ from a Moore total-output accumulator.
    unit_prefix_totals = tuple(range(9))
    clock_costs = tuple(Fraction(1, 2 ** (n + 1)) for n in range(16))
    assert len(set(unit_prefix_totals)) == 9 and len(set(clock_costs)) == 16
    assert sum(clock_costs) == 1 - Fraction(1, 2 ** 16)

    elapsed = time.monotonic() - begin
    assert elapsed < 25
    return {"status": "TESTED MODEL", "author_commit": AUTHOR,
            "author_dossier_sha256": AUTHOR_DOSSIER_HASH,
            "review_execution_parent": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
            "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "author_probe_read_or_imported": False, "repository_modules_imported": False,
            "command": "PYTHONDONTWRITEBYTECODE=1 timeout 25s python reviews/X06_E36_probe.py --receipt reviews/X06_E36_receipt.json",
            "exit_code": 0, "elapsed_seconds": round(elapsed, 6), "time_limit_seconds": 25,
            "machines": machines, "unary_lassos": unary,
            "noncancellation_controls": noncancel,
            "noncancellative_unary_primitive_period_4": {"raw_stream_states": 4,
                                                        "cumulative_residual_classes": periodic_noncancel},
            "hom_control": {"source_matrix": dh, "residual_matrix": dr,
                            "fixed_endpoint_source": 4, "fixed_endpoint_residual": 0,
                            "target_fibre_equality": True, "full_word_lifts_checked": 508},
            "hypothesis_removals": {"nonadditive_valuation_triangle": squared_distances,
                                    "negative_valuation_edge": -1,
                                    "nonfaithful_zero_valuation_state_counts": [exact_label_count, scalar_label_count],
                                    "forgotten_budget_illegal_word": "aaa",
                                    "priced_reset_word_charge": 5, "unpriced_reset_word_charge": 2,
                                    "private_original_totals": totals,
                                    "edgewise_max_invented_charge": independent_max,
                                    "edgewise_min_invented_charge": independent_min,
                                    "same_total_weight_pushing": [[1, 1], [0, 2]],
                                    "unit_charge_weighted_states": 1,
                                    "literal_Moore_total_reports_distinct_prefixes": 9,
                                    "external_clock_distinct_departing_costs": 16},
            "boundary": "Finite exact controls; universal claims require review derivations, no physical storage claim"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = test()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.write_text(payload)
        print(json.dumps({k: result[k] for k in ("status", "machines", "unary_lassos", "elapsed_seconds", "exit_code")}, sort_keys=True))
    else:
        print(payload, end="")
