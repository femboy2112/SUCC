"""Independent finite acquisition audit; deliberately no production DP oracle.

Run from an integrated checkout, or pass --repo to the audited worktree.
The oracle rebuilds raw beliefs, enumerates stationary policies, and simulates
each fixed original source. Its finite scope is evidence, not the theorem.
"""
import argparse
from dataclasses import replace
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from random import Random
import sys


def raw_oracle(problem, initial):
    """No production arena, goal, branches, Bellman recurrence or rank logic."""
    table = {(e.start, e.action): e for e in problem.edges}
    targets = dict(zip(problem.origins, problem.target))

    def done(belief):
        return len({targets[x] for x, _ in belief}) == 1

    def outcomes(belief, action):
        if any((z, action) not in table for _, z in belief):
            return None
        groups = {}
        for x, z in belief:
            edge = table[z, action]
            groups.setdefault((edge.receipt, edge.cost), []).append((x, edge.target))
        return tuple(tuple(sorted(c)) for c in groups.values())

    seen, todo = {initial}, [initial]
    while todo:
        belief = todo.pop()
        if done(belief):
            continue
        for action in problem.actions:
            for child in outcomes(belief, action) or ():
                if child not in seen:
                    seen.add(child)
                    todo.append(child)
    pending = sorted(b for b in seen if not done(b))
    options = [tuple(a for a in problem.actions if outcomes(b, a) is not None)
               or (None,) for b in pending]
    policy_count = 1
    for option in options:
        policy_count *= len(option)
    if policy_count > 262144:
        raise RuntimeError("UNRESOLVED: independent policy enumeration cap")
    best = None
    for choices in product(*options):
        policy = dict(zip(pending, choices))
        costs = []
        for actual, _ in initial:
            belief, paid, visited = initial, Q(0), set()
            while not done(belief):
                if belief in visited or policy[belief] is None:
                    break
                visited.add(belief)
                action = policy[belief]
                edge = table[dict(belief)[actual], action]
                paid += edge.cost
                belief = tuple(sorted(
                    (x, table[z, action].target) for x, z in belief
                    if (table[z, action].receipt, table[z, action].cost)
                    == (edge.receipt, edge.cost)))
            else:
                costs.append(paid)
                continue
            break
        if len(costs) == len(initial):
            cost = max(costs)
            best = cost if best is None else min(best, cost)
    return best, tuple(sorted(seen)), policy_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    sys.path.insert(0, str(args.repo))
    from observational_succ import information_repair as production

    Acquisition, ProbeEdge = production.Acquisition, production.ProbeEdge
    source = Path(production.__file__)
    counts = {"exhaustive_two_origin_models": 0, "fresh_three_origin_models": 0,
              "advice_budget_comparisons": 0, "rejected_value_mutations": 0,
              "rejected_rank_mutations": 0, "maximum_stationary_policies": 0}

    def compare(problem, start):
        expected, beliefs, number = raw_oracle(problem, start)
        counts["maximum_stationary_policies"] = max(
            counts["maximum_stationary_policies"], number)
        cert = production.solve_acquisition(problem, (start,))
        assert cert.beliefs == beliefs, "Raw/projection arena mismatch"
        assert production.check_acquisition(problem, cert)
        assert dict(zip(cert.beliefs, cert.values))[start] == expected
        return expected

    carriers, actions = ("s", "t"), ("a", "b")
    entries = (None,) + tuple(product(carriers, ("0", "1"), (Q(0), Q(1))))
    for rows in product(entries, repeat=4):
        edges = tuple(ProbeEdge(z, a, *row)
                      for (z, a), row in zip(product(carriers, actions), rows)
                      if row is not None)
        problem = Acquisition(carriers, actions, edges, ("x", "y"), carriers,
                              ("X", "Y"), ("q", "q"))
        compare(problem, problem.start(problem.origins))
        counts["exhaustive_two_origin_models"] += 1

    rng = Random(202610199113)
    for trial in range(140):
        carriers = ("s", "t", "u")
        edges = tuple(ProbeEdge(z, a, rng.choice(carriers), str(rng.randrange(2)),
                                Q(rng.randrange(3), 2))
                      for z, a in product(carriers, actions) if rng.randrange(5))
        problem = Acquisition(carriers, actions, edges, ("x", "y", "z"),
                              carriers, ("X", "Y", "Z"), ("q", "q", "q"))
        compare(problem, problem.start(problem.origins))
        counts["fresh_three_origin_models"] += 1
        # Independently value every original subset, then enumerate literal
        # advice strings. This uses neither production partitions nor its
        # one-deletion minimal-infeasible-set test.
        values = {}
        for size in range(1, 4):
            for subset in combinations(problem.origins, size):
                values[frozenset(subset)] = raw_oracle(
                    problem, problem.start(subset))[0]
        cert = production.solve_acquisition(problem)
        budgets = {Q(0), Q(1, 4)} | {v for v in values.values() if v is not None}
        for budget in budgets:
            feasible = {s: v is not None and v <= budget for s, v in values.items()}
            forbidden = tuple(sorted(tuple(sorted(s)) for s, okay in feasible.items()
                                     if not okay and all(okay2 for t, okay2
                                                         in feasible.items() if t < s)))
            minimal = None
            for colors in range(1, 4):
                for code in product(range(colors), repeat=3):
                    blocks = {frozenset(x for x, c in zip(problem.origins, code) if c == k)
                              for k in code}
                    if all(feasible[b] for b in blocks):
                        minimal = colors
                        break
                if minimal is not None:
                    break
            point = production.advice_at_budget(problem, cert, budget)
            assert point["labels"] == minimal
            assert point["advice_bits"] == (minimal - 1).bit_length()
            assert point["minimal_infeasible"] == forbidden
            counts["advice_budget_comparisons"] += 1
        # Wrong costs/infinity must fail even when the rest is authentic.
        for index, value in enumerate(cert.values):
            wrong = Q(0) if value is None else value + Q(1, 2)
            mutated = list(cert.values)
            mutated[index] = wrong
            try:
                production.check_acquisition(problem, replace(cert, values=tuple(mutated)))
            except production.RepairError:
                counts["rejected_value_mutations"] += 1
            else:
                raise AssertionError("False value certificate accepted")
            if cert.ranks[index] is not None and cert.ranks[index] > 0:
                ranks = list(cert.ranks)
                ranks[index] = 0
                try:
                    production.check_acquisition(problem, replace(cert, ranks=tuple(ranks)))
                except production.RepairError:
                    counts["rejected_rank_mutations"] += 1
                else:
                    raise AssertionError("False termination rank accepted")
    print(json.dumps({
        "status": "PASS", "audited_source_sha256": sha256(source.read_bytes()).hexdigest(),
        "seed": 202610199113, "skipped_models": 0, "counts": counts,
        "boundary": "Finite exact tests; positional completeness relies on the proof. "
                    "Only raw model dataclasses are shared with the oracle. "
                    "All costs are observed; all originals stay fixed during simulation."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
