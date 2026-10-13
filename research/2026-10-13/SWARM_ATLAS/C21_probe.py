"""C21: bounded exact pair-belief and hidden-cost controls; not certification."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from itertools import product
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.adaptive_proof_policy import (
    solve_adaptive_claim, conditional_source_field,
)
from observational_succ.noncommuting_proof_transport import (
    FiniteCarrier, Instrument, _bit_field,
)


def native_rows(field):
    return {a.name: {x: ((a.outputs[x], a.transitions[x], Fraction(1)),)
                     for x in range(field.count) if a.enabled[x]}
            for a in field.actions}


def edges(rows, belief):
    result = {}
    for action, table in rows.items():
        if any(x not in table for _, x in belief):
            continue
        buckets = {}
        for s, x in belief:
            for o, y, _ in table[x]:
                buckets.setdefault(o, set()).add((s, y))
        result[action] = {o: tuple(sorted(b)) for o, b in buckets.items()}
    return result


def attractor(rows, root, target):
    seen, queue, graph = {root}, [root], {}
    for b in queue:
        graph[b] = edges(rows, b)
        for branches in graph[b].values():
            for child in branches.values():
                if child not in seen:
                    assert len(seen) < 512, "probe closure cap"
                    seen.add(child)
                    queue.append(child)
    ranks = {b: 0 for b in queue if len({target[s] for s, _ in b}) == 1}
    while True:
        fresh = {b: 1 + min(max(ranks[c] for c in branches.values())
                           for branches in graph[b].values()
                           if all(c in ranks for c in branches.values()))
                 for b in queue if b not in ranks and any(
                     all(c in ranks for c in branches.values())
                     for branches in graph[b].values())}
        if not fresh:
            return ranks.get(root), len(graph)
        ranks.update(fresh)


def exact_cost(rows, root, target, horizon):
    """Public-history computed possibility costs; actual hidden cost is not read."""
    @lru_cache(None)
    def rec(profile, h):
        if len({target[s] for s, _, _ in profile}) == 1:
            return max(d for _, _, d in profile)
        if h == 0:
            return float("inf")
        values = []
        for table in rows.values():
            if any(x not in table for _, x, _ in profile):
                continue
            buckets = {}
            for s, x, d in profile:
                for o, y, k in table[x]:
                    assert k >= 0
                    branch = buckets.setdefault(o, {})
                    branch[s, y] = max(branch.get((s, y), Fraction(-1)), d+k)
            values.append(max(rec(tuple(sorted((s, y, d) for (s, y), d
                                                in branch.items())), h-1)
                              for branch in buckets.values()))
        return min(values, default=float("inf"))
    return rec(tuple((s, x, Fraction(0)) for s, x in root), horizon)


def main():
    parity = ("0", "1", "1", "0")
    full = tuple((s, s) for s in range(4))
    controls = {}
    for name, field, expected in (
        ("destructive", _bit_field(), None),
        ("nondestructive", _bit_field(nondestructive=True), 2),
        ("joint", _bit_field(with_joint=True), 1),
        ("conditional", conditional_source_field(), 2),
    ):
        rank, size = attractor(native_rows(field), full, parity)
        native = solve_adaptive_claim(field, (0, 1, 2, 3), parity, target_id="C21")
        assert rank == native.rank == expected
        controls[name] = {"rank": rank, "reachable_beliefs": size}
    same = ((0, 0), (3, 3))
    assert attractor(native_rows(_bit_field()), same, parity)[0] == 0
    lost = ((0, 0), (1, 0))
    assert attractor(native_rows(_bit_field(nondestructive=True)), lost, parity)[0] is None
    many = ((0, 0), (0, 1), (1, 2), (1, 3))
    assert attractor(native_rows(_bit_field(nondestructive=True)), many, ("0", "1"))[0] == 1
    controls["correlated_source"] = {"prior_rank": 0, "full_destructive_rank": None}
    controls["uncertain_original_current"] = {"lost_rank": None, "multivalued_rank": 1}

    binary = ((0, 0), (1, 1))
    labels = ("0", "1")
    wait = {x: ((-1, x, Fraction(0)),) for x in (0, 1)}
    read = {x: ((x, x, Fraction(1, 3)),) for x in (0, 1)}
    zero = {"wait": wait, "read": read}
    assert attractor(zero, binary, labels)[0] == 1
    assert exact_cost(zero, binary, labels, 4) == Fraction(1, 3)
    assert min(Fraction(0), Fraction(1, 3)) == 0  # Spurious scalar fixed point.
    assert attractor({"wait": wait}, binary, labels)[0] is None
    retry = {"try": {x: ((-1, x, Fraction(0)), (x, x, Fraction(0))) for x in (0, 1)}}
    assert attractor(retry, binary, labels)[0] is None
    assert exact_cost(retry, binary, labels, 6) == float("inf")
    menu = {"only-zero": {0: ((0, 0, Fraction(0)),)}}
    assert attractor(menu, binary, labels)[0] is None
    controls["zero_cost_nontermination"] = {"proper_value": "1/3", "wait_only_rank": None,
                                           "adversarial_retry_rank": None, "private_menu_rank": None}

    correlated = {"A": {0: ((0, 1, Fraction(9)),), 2: ((0, 3, Fraction(0)),)},
                  "B": {1: ((0, 1, Fraction(0)),), 3: ((1, 3, Fraction(9)),)}}
    phase_root = ((0, 0), (1, 2))
    assert attractor(correlated, phase_root, labels)[0] == 2
    assert exact_cost(correlated, phase_root, labels, 3) == 9
    costs_a = [correlated["A"][x][0][2] for _, x in phase_root]
    costs_b = [correlated["B"][correlated["A"][x][0][1]][0][2] for _, x in phase_root]
    actual = [int(a+b) for a, b in zip(costs_a, costs_b)]
    separate = int(max(costs_a) + max(costs_b))
    assert actual == [9, 9] and separate == 18
    controls["hidden_cost_correlation"] = {"actual_totals": actual, "exact_minimax": 9,
                                            "sum_of_separate_maxima": separate}
    cheaper = {"direct": {x: ((s, x, Fraction(5)),) for s, x in phase_root},
               "prepare": {0: ((0, 1, Fraction(0)),), 2: ((0, 3, Fraction(0)),)},
               "finish": {1: ((0, 1, Fraction(1)),), 3: ((1, 3, Fraction(1)),)}}
    assert attractor(cheaper, phase_root, labels)[0] == 1
    assert exact_cost(cheaper, phase_root, labels, 1) == 5
    assert exact_cost(cheaper, phase_root, labels, 2) == 1
    controls["rank_is_not_cost"] = {"minimum_rank": 1, "rank_one_cost": 5, "rank_two_cost": 1}

    checked = 0
    for u, v in product(product((0, 1), repeat=4), repeat=2):
        field = FiniteCarrier(2, (Instrument("A", u[:2], u[2:], (True, True)),
                                  Instrument("B", v[:2], v[2:], (True, True))), "C21", "v1")
        rows = native_rows(field)
        rank, size = attractor(rows, binary, labels)
        native = solve_adaptive_claim(field, (0, 1), labels, target_id="C21-exhaust")
        value = exact_cost(rows, binary, labels, size)
        assert rank == native.rank
        assert value == (float("inf") if rank is None else rank)
        checked += 1
    paths = ["observational_succ/adaptive_proof_policy.py",
             "observational_succ/noncommuting_proof_transport.py",
             "provenance/IMPORT_MANIFEST.json",
             "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
             "research/2026-10-13/SWARM_ATLAS/C21.md",
             "research/2026-10-11/NONCOMMUTING_PROOF_TRANSPORT.md"]
    paths.append(str(Path(__file__).resolve().relative_to(ROOT)))
    return {"status": "TESTED MODEL", "baseline": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
            "arithmetic": "integer and Fraction exact; infinity is nontermination sentinel",
            "controls": controls, "exhaustive_native_agreements": checked,
            "hidden_state_or_actual_cost_observed_by_policy": False, "resets_assumed": False,
            "sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            "scope": "bounded controls only; prose proof is not mechanically certified"}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
