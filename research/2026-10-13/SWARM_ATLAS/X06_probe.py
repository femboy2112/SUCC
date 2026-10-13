"""X06 exact finite controls; no formal proof or physical-source certification."""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "830e99ffc89bc9ee5ae97cbbc433206be99aa96c"


def labels(values):
    seen = {}
    return tuple(seen.setdefault(v, len(seen)) for v in values)


def refine(q, transitions, costs):
    """Greatest report/immediate-cost/action-stable finite partition."""
    p = labels((q[s], tuple(costs[a][s] for a in range(len(transitions))))
               for s in range(len(q)))
    while True:
        nxt = labels((q[s], tuple(costs[a][s] for a in range(len(transitions))),
                      tuple(p[u[s]] for u in transitions)) for s in range(len(q)))
        if nxt == p:
            return p
        p = nxt


def words(alphabet, depth):
    return [w for k in range(depth + 1) for w in product(range(alphabet), repeat=k)]


def run(s, w, q, transitions, costs, combine=lambda x, y: x + y):
    total = 0
    for a in w:
        total = combine(total, costs[a][s])
        s = transitions[a][s]
    return q[s], total


def endpoint(s, w, transitions):
    for a in w:
        s = transitions[a][s]
    return s


def bounded_behavior_partition(q, transitions, costs):
    # Direct cumulative-word table, independent of partition refinement.
    ws = words(len(transitions), len(q) ** 2)
    return labels(tuple(run(s, w, q, transitions, costs) for w in ws)
                  for s in range(len(q)))


def equal_partition(a, b):
    return all((a[i] == a[j]) == (b[i] == b[j])
               for i in range(len(a)) for j in range(len(a)))


def finite_controls():
    count = 0
    for n, na in [(1, 1), (2, 1), (3, 1), (2, 2)]:
        for flat_u in product(range(n), repeat=n * na):
            u = tuple(flat_u[a*n:(a+1)*n] for a in range(na))
            for q in product(range(2), repeat=n):
                for flat_c in product(range(2), repeat=n * na):
                    c = tuple(flat_c[a*n:(a+1)*n] for a in range(na))
                    p = refine(q, u, c)
                    assert equal_partition(p, bounded_behavior_partition(q, u, c))
                    for a in range(na):
                        for s in range(n):
                            for t in range(n):
                                if p[s] == p[t]:
                                    assert q[s] == q[t] and c[a][s] == c[a][t]
                                    assert p[u[a][s]] == p[u[a][t]]
                    count += 1
    return {"machines": count, "scope": "binary reports/costs; unary <=3 states, two actions at 2 states",
            "oracle": "direct cumulative words of length <= n^2; refinement uses local edge signatures"}


def stream_lasso(output, u):
    p = refine(output, (u,), ((0,) * len(u),))
    orbit, seen, s = [], {}, 0
    while p[s] not in seen:
        seen[p[s]] = len(orbit)
        orbit.append(p[s])
        s = u[s]
    mu = seen[p[s]]
    return mu, len(orbit) - mu, p


def unary_controls():
    count = 0
    for mu in range(3):
        for period in range(1, 5):
            n = mu + period
            u = tuple(range(1, n)) + (mu,)
            for q in product(range(2), repeat=n):
                mq, pq, _ = stream_lasso(q, u)
                for c in product(range(2), repeat=n):
                    mc, pc, _ = stream_lasso(c, u)
                    mj, pj, joint = stream_lasso(tuple(zip(q, c)), u)
                    assert (mj, pj) == (max(mq, mc), lcm(pq, pc))
                    assert equal_partition(joint, refine(q, (u,), (c,)))
                    count += 1
    # Two independently primitive periods have a joint six-phase source.
    q, c = (0, 1, 0, 1, 0, 1), (0, 0, 1, 0, 0, 1)
    u = (1, 2, 3, 4, 5, 0)
    assert stream_lasso(tuple(zip(q, c)), u)[:2] == (0, 6)
    return {"lassos": count, "presented_mu": [0, 1, 2], "presented_period": [1, 2, 3, 4],
            "primitive_2_by_3": {"separate_counts": [2, 3], "joint_count": 6}}


def max_equal(s, t, q, u, c, initial=0):
    queue = deque([(s, t, initial, initial)])
    seen = set()
    while queue:
        x, y, bx, by = queue.popleft()
        key = x, y, bx, by
        if key in seen:
            continue
        seen.add(key)
        if (q[x], bx) != (q[y], by):
            return False, len(seen)
        for a in range(len(u)):
            queue.append((u[a][x], u[a][y], max(bx, c[a][x]), max(by, c[a][y])))
    return True, len(seen)


def noncancellation_control():
    # a: s->u, t->v, u->v, v->v; b makes all four states reachable.
    q, u, c = (0, 0, 0, 0), ((2, 3, 3, 3), (1, 0, 0, 0)), ((2, 2, 0, 1), (0, 0, 0, 0))
    same, visited = max_equal(0, 1, q, u, c)
    successor_same, _ = max_equal(2, 3, q, u, c)
    assert same and not successor_same
    assert len(set(refine(q, u, c))) == 4
    saturated_same, _ = max_equal(2, 3, q, u, c, initial=2)
    assert saturated_same and c[0][2] != c[0][3]
    return {"states": ["s", "t", "u", "v"], "transitions": u, "costs": c,
            "monoid": "([0,2], max, 0)", "s_t_behavior_equal": same,
            "u_v_behavior_equal": successor_same, "product_closure_nodes": visited,
            "cost_faithful_partition": [0, 1, 2, 3],
            "saturated_budget_alone_recovers_raw_cost": False,
            "unary_s_totals": [run(0, (0,)*k, q, u, c, max)[1] for k in range(5)],
            "unary_t_totals": [run(1, (0,)*k, q, u, c, max)[1] for k in range(5)]}


def distances(n, edges):
    d = [[None] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = Fraction(0)
    for s, t, c in edges:
        v = Fraction(c)
        d[s][t] = v if d[s][t] is None else min(v, d[s][t])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] is not None and d[k][j] is not None:
                    v = d[i][k] + d[k][j]
                    d[i][j] = v if d[i][j] is None else min(v, d[i][j])
    return d


def geometry_control():
    q = (0, 0, 1, 0, 0, 1)
    u = ((1, 2, 0, 4, 5, 3), (3, 4, 5, 0, 1, 2))
    c = ((1, 2, 3, 1, 2, 3), (4, 4, 4, 4, 4, 4))
    p = refine(q, u, c)
    assert p == (0, 1, 2, 0, 1, 2)
    reps = [p.index(r) for r in range(3)]
    ru = tuple(tuple(p[ua[s]] for s in reps) for ua in u)
    rc = tuple(tuple(ca[s] for s in reps) for ca in c)
    rq = tuple(q[s] for s in reps)
    dh = distances(6, [(s, u[a][s], c[a][s]) for a in range(2) for s in range(6)])
    dr = distances(3, [(r, ru[a][r], rc[a][r]) for a in range(2) for r in range(3)])
    triangle_checks = 0
    for d in (dh, dr):
        for i, j, k in product(range(len(d)), repeat=3):
            assert d[i][k] <= d[i][j] + d[j][k]
            triangle_checks += 1
    checks = 0
    for s in range(6):
        for r in range(3):
            assert dr[p[s]][r] == min(dh[s][t] for t in range(6) if p[t] == r)
            checks += 1
        for w in words(2, 4):
            assert run(s, w, q, u, c) == run(p[s], w, rq, ru, rc)
            assert p[endpoint(s, w, u)] == endpoint(p[s], w, ru)
        for v in words(2, 2):
            for w in words(2, 2):
                end = endpoint(s, v, u)
                assert endpoint(end, w, u) == endpoint(s, v+w, u)
                assert run(s, v+w, q, u, c)[1] == run(s, v, q, u, c)[1] + run(end, w, q, u, c)[1]
    assert dh[0][3] == 4 and dr[p[0]][p[3]] == 0
    bad = distances(4, [(0, 1, 1), (1, 2, 3), (2, 3, 1)])
    assert (bad[0][1], bad[2][3], bad[0][3]) == (1, 1, 5)
    return {"source_states": 6, "residual_states": 3, "partition": p,
            "fibre_distance_equalities": checks, "triangle_checks": triangle_checks,
            "quotient_distances": [[str(x) for x in row] for row in dr],
            "fixed_endpoint_shrink": {"physical": 4, "residual": 0},
            "spent_fresh_naive_triangle": [1, 1, 5], "reset_cost": 3}


def interface_controls():
    # A physical one-state action costs 1; legal continuations depend on history budget.
    limit = 2
    budget_edges = {0: 1, 1: 2}
    def legal_length(k):
        budget = 0
        for _ in range(k):
            if budget not in budget_edges:
                return False
            budget = budget_edges[budget]
        return True
    assert [legal_length(k) for k in range(4)] == [True, True, True, False]
    # Forgetting budget identifies two enabled endpoints with the disabled endpoint.
    collapsed_edges = {0: 0}
    collapsed = 0
    for _ in range(3):
        collapsed = collapsed_edges[collapsed]
    assert collapsed == 0
    originals = {0: (7, 1), 1: (2, 6)}
    exact = {s: sum(v) for s, v in originals.items()}
    separate = sum(max(v[i] for v in originals.values()) for i in range(2))
    assert exact == {0: 8, 1: 8} and separate == 13
    prefix = {s: v[0] for s, v in originals.items()}
    lifted = {s: prefix[s] + originals[s][1] for s in originals}
    assert lifted == exact
    first_costs = [Fraction(1, 2**(n+1)) for n in range(8)]
    assert len(set(first_costs)) == 8 and sum(first_costs) == Fraction(255, 256)
    return {"no_reset_budget": {"limit": limit, "legal_action_lengths": [0, 1, 2],
                                "complete_budget_edges": budget_edges,
                                "budget_projection": [0, 0, 0], "enabledness_reflected": False,
                                "forgotten_budget_accepts_length": 3},
            "private_correlation": {"original_costs": originals, "exact_totals": exact,
                                    "pair_budget_after_first": prefix, "pair_budget_after_second": lifted,
                                    "separate_maxima": separate, "budget_8_feasible": True},
            "clock_cost_prefix": [str(x) for x in first_costs],
            "clock_prefix_sum": str(sum(first_costs)),
            "infinite_claim_source": "dossier geometric-series and distinct-first-cost proofs",
            "summability_implies_finite_residuals": False,
            "one_state_unit_cost_implies_bounded_total": False}


def main():
    source_paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
                    "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
                    "provenance/origins/fuckingrh/research/2026-10-10/CATEGORICAL_YONEDA_RESOURCE_FRONTIER.md",
                    "provenance/origins/fuckingrh/research/2026-10-10/INFINITE_REALIZATION_LIMITS.md"]
    source_paths += [str((HERE / n).relative_to(ROOT)) for n in
                     ["PROTOCOL.md", "A08.md", "B16.md", "C21.md", "F45_PROOF_COST_SCHEDULING.md",
                      "reviews/A08_PRINCIPAL_REVIEW.md", "reviews/B16_PRINCIPAL_REVIEW.md",
                      "reviews/C21_PRINCIPAL_REVIEW.md", "reviews/F45_PRINCIPAL_REVIEW.md",
                      "X06.md", "X06_probe.py"]]
    out = {"id": "X06", "source_parent": PARENT,
           "status": "PROVED LOCAL paper derivation; TESTED MODEL receipt; separate review required",
           "finite_cancellative_controls": finite_controls(), "unary_joint_controls": unary_controls(),
           "noncancellation": noncancellation_control(), "geometry": geometry_control(),
           "interfaces": interface_controls(),
           "sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in source_paths},
           "literature": [{"url": "https://www.cs.nyu.edu/~mohri/pub/hwa.pdf", "location": "sections 1.2 and 6.3-6.4"},
                          {"url": "https://www.nsm.buffalo.edu/~sww/0papers/lawveres-metric-space-paper.pdf", "location": "author commentary pages 1-3"}],
           "kernel_checked": False, "physical_cost_calibrated": False,
           "independence": "one investigator; direct-word oracle and refinement share source fixtures",
           "remaining_smallest_lemma": "finite partial-action budget quotient path lifting, with enabledness reflected"}
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
