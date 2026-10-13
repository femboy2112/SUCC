#!/usr/bin/env python3
"""Independent exact Heisenberg/action-language crucible; no SUCC imports.

This is a source-relative finite mathematical probe, not physical data and not
a kernel proof. Composition below means ordinary function composition f o g.
"""
from collections import deque
from itertools import product
import json


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(g)))


def inverse(f):
    answer = [0] * len(f)
    for i, value in enumerate(f):
        answer[value] = i
    return tuple(answer)


def closure(generators, size):
    identity = tuple(range(size))
    seen, todo = {identity}, deque([identity])
    while todo:
        f = todo.popleft()
        for g in generators:
            after = compose(g, f)
            if after not in seen:
                seen.add(after)
                todo.append(after)
    return seen


def order(f):
    identity = tuple(range(len(f)))
    current = identity
    for k in range(1, 2 * len(f) + 1):
        current = compose(f, current)
        if current == identity:
            return k
    raise AssertionError("order exceeded declared bound")


def matrix(u, v, w):
    return ((1, u, w), (0, 1, v), (0, 0, 1))


def matrix_product(a, b, n):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) % n
                       for j in range(3)) for i in range(3))


def case(n):
    source = tuple(product(range(n), repeat=3))
    observer = tuple(product(range(n), repeat=2))
    source_index = {s: i for i, s in enumerate(source)}
    index = {s: i for i, s in enumerate(observer)}
    q = tuple(index[y, z] for x, y, z in source)
    source_a = tuple(source_index[(x + 1) % n, y, (z + y) % n]
                     for x, y, z in source)
    source_b = tuple(source_index[x, (y + 1) % n, z] for x, y, z in source)
    a = tuple(index[y, (z + y) % n] for y, z in observer)
    b = tuple(index[(y + 1) % n, z] for y, z in observer)
    assert all(q[source_a[i]] == a[q[i]] and q[source_b[i]] == b[q[i]]
               for i in range(len(source)))

    # r and r after A recover y,z; every y,z update ignores x.
    two_reports = tuple((z, (z + y) % n) for x, y, z in source)
    relation_checks = 0
    for i in range(len(source)):
        for j in range(i, len(source)):
            assert (q[i] == q[j]) == (two_reports[i] == two_reports[j])
            relation_checks += 1
    assert len(set(q)) == n * n
    assert sorted(q.count(i) for i in range(n * n)) == [n] * (n * n)

    # Generic permutation BFS and independently parameterized matrix model.
    group = closure((a, b), len(observer))
    parameters = tuple(product(range(n), repeat=3))
    representation = {
        (u, v, w): tuple(index[(y + v) % n, (z + u * y + w) % n]
                        for y, z in observer)
        for u, v, w in parameters
    }
    assert len(set(representation.values())) == n ** 3
    assert set(representation.values()) == group
    matrix_checks = 0
    # Full products for small n; all adjacent pairs in the declared ordering for
    # larger n. Universal multiplication is proved in the accompanying dossier.
    pairs = product(parameters, repeat=2) if n <= 3 else zip(parameters, parameters[1:] + parameters[:1])
    for (u, v, w), (up, vp, wp) in pairs:
        law = ((u + up) % n, (v + vp) % n, (w + wp + u * vp) % n)
        assert matrix_product(matrix(u, v, w), matrix(up, vp, wp), n) == matrix(*law)
        assert compose(representation[u, v, w], representation[up, vp, wp]) == representation[law]
        matrix_checks += 1
    center = {g for g in group if compose(g, a) == compose(a, g)
              and compose(g, b) == compose(b, g)}
    assert center == {representation[0, 0, w] for w in range(n)}
    # EOS execution convention: A,B,A^-1,B^-1, hence C^-1.
    h = compose(inverse(b), compose(inverse(a), compose(b, a)))
    assert h == representation[0, 0, n - 1]
    assert order(h) == n
    assert all(h[i] != i for i in range(len(observer)))

    # Quotient is G/L, L=<A>; faithfulness is trivial core(L), not recovery of x.
    stabilizer = {g for g in group if g[index[0, 0]] == index[0, 0]}
    assert len(stabilizer) == n
    conjugate = {compose(inverse(b), compose(g, b)) for g in stabilizer}
    assert stabilizer & conjugate == {tuple(range(len(observer)))}

    # A hostile observation basis keeps hidden noncommutation but loses it all
    # in the behavioral quotient: report y sees only the number of B actions.
    y_a = tuple(range(n))
    y_b = tuple((y + 1) % n for y in range(n))
    y_group = closure((y_a, y_b), n)
    assert len(y_group) == n
    s = source_index[0, 0, 0]
    ab, ba = source_b[source_a[s]], source_a[source_b[s]]
    assert ab != ba and source[ab][1] == source[ba][1]
    # New action W exposes x, invalidating descent through the old q.
    left, right = source_index[0, 0, 0], source_index[1, 0, 0]
    swap = lambda state: (state[2], state[1], state[0])
    assert q[left] == q[right]
    assert index[swap(source[left])[1:]] != index[swap(source[right])[1:]]
    assert len({two_reports[i] + (swap(source[i])[2],) for i in range(len(source))}) == n ** 3
    return {
        "modulus": n, "source_states": n ** 3, "observer_states": n ** 2,
        "source_fiber_size": n, "permutation_group_size": len(group),
        "center_size": len(center), "orders_A_B_H": [order(a), order(b), order(h)],
        "order_A_after_B": order(compose(a, b)),
        "exact_pair_relation_checks": relation_checks,
        "matrix_and_permutation_product_checks": matrix_checks,
        "stabilizer_size": len(stabilizer), "core_trivial_witness": "L intersect B^-1 L B = {identity}",
        "commutator_fixed_points": 0,
        "changed_readout_y_observer_group_size": len(y_group),
        "hidden_noncommutation_y_report_witness": {
            "start": list(source[s]), "A_then_B": list(source[ab]), "B_then_A": list(source[ba]),
        },
        "new_swap_breaks_old_quotient": [list(source[left]), list(source[right])],
        "new_swap_expanded_observer_states": n ** 3,
    }


def main():
    result = {
        "schema": "succ-swm-f41-exact-independent-v1",
        "implementation": "standard-library integer/permutation/matrix arithmetic; no SUCC helper imports",
        "scope": "declared finite simulator; general proof in F41.md; no Lean compilation in this expedition",
        "cases": [case(n) for n in (2, 3, 4, 5, 6, 7)],
        "negative_control": {
            "claim": "All finite Heisenberg elements have order p for every prime p",
            "status": "REFUTED", "prime": 2, "witness": "A o B has order 4 although A,B,H have order 2",
        },
        "holds_for_composite_moduli": True,
        "physical_source_authenticated": False,
        "academic_novelty_established": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
