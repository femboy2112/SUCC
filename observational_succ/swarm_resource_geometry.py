"""Exact resource recurrences, anchored graph models and finite clock gluing.

These are mathematical abstractions. No psychological, neuronal, thermodynamic,
musical-quality, or empirical synchronization conclusion is encoded.
"""
from __future__ import annotations
from collections import deque
from fractions import Fraction


class GeometryError(ValueError):
    pass


def debt_stages(initial, growth, service, service_growth, stages):
    values = tuple(Fraction(x) for x in (initial, growth, service, service_growth))
    d, a, b, r = values
    if min(values) <= 0 or type(stages) is not int or not 0 <= stages <= 10000:
        raise GeometryError("Positive rational resource law and finite horizon required")
    result, power = [d], Fraction(1)
    for _ in range(stages):
        d = a*d - b*power
        result.append(d)
        power *= r
    return tuple(result)


def finite_completion_possible(initial, growth, service, service_growth):
    d, a, b, r = map(Fraction, (initial, growth, service, service_growth))
    if min(d, a, b, r) <= 0:
        raise GeometryError("Positive resource-law parameters required")
    return r >= a or d < b/(a-r)


def dovetail_round_bound(index, steps):
    if any(type(x) is not int or x < 1 for x in (index, steps)):
        raise GeometryError("One-indexed task and positive step count required")
    last_round = index + steps - 1
    return last_round, last_round*(last_round+1)//2


def anchored_graph_matrix(count, edges, anchors):
    if type(count) is not int or not 1 <= count <= 64 or len(anchors) != count:
        raise GeometryError("Finite graph and matching anchors required")
    anchors = tuple(map(Fraction, anchors))
    if any(x < 0 for x in anchors):
        raise GeometryError("Anchors must be nonnegative")
    matrix = [[Fraction(i == j)*anchors[i] for j in range(count)] for i in range(count)]
    neighbors = [set() for _ in range(count)]
    for i, j, weight in edges:
        w = Fraction(weight)
        if any(type(x) is not int or not 0 <= x < count for x in (i, j)) or i == j or w <= 0:
            raise GeometryError("Positive weighted nonloop edges required")
        matrix[i][i] += w
        matrix[j][j] += w
        matrix[i][j] -= w
        matrix[j][i] -= w
        neighbors[i].add(j)
        neighbors[j].add(i)
    unseen = set(range(count))
    while unseen:
        component, todo = set(), [next(iter(unseen))]
        while todo:
            v = todo.pop()
            if v not in component:
                component.add(v)
                todo.extend(neighbors[v]-component)
        unseen -= component
        if not any(anchors[x] > 0 for x in component):
            raise GeometryError("Every component needs an anchor for positive definiteness")
    return tuple(map(tuple, matrix))


def solve_exact(matrix, rhs):
    n = len(matrix)
    if len(rhs) != n or any(len(row) != n for row in matrix):
        raise GeometryError("Square exact linear system required")
    rows = [[Fraction(x) for x in row] + [Fraction(y)] for row, y in zip(matrix, rhs)]
    for i in range(n):
        pivot = next((k for k in range(i, n) if rows[k][i]), None)
        if pivot is None:
            raise GeometryError("Singular linear system")
        rows[i], rows[pivot] = rows[pivot], rows[i]
        factor = rows[i][i]
        rows[i] = [x/factor for x in rows[i]]
        for j in range(n):
            if i != j:
                factor = rows[j][i]
                rows[j] = [x-factor*y for x, y in zip(rows[j], rows[i])]
    return tuple(row[-1] for row in rows)


def graph_evidence_update(matrix, baseline, node, observation, strength):
    n, eta = len(matrix), Fraction(strength)
    if len(baseline) != n or type(node) is not int or not 0 <= node < n or eta <= 0:
        raise GeometryError("Positive evidence on a declared graph node required")
    column = solve_exact(matrix, tuple(Fraction(i == node) for i in range(n)))
    denominator = 1 + eta*column[node]
    if denominator == 0:
        raise GeometryError("Evidence update singular")
    delta = eta*(Fraction(observation)-Fraction(baseline[node]))/denominator
    return tuple(Fraction(x) + delta*c for x, c in zip(baseline, column))


def clock_gluing(count, modulus, edges):
    """Exact Z/m-valued phase potentials or a cycle-holonomy receipt.

    Edge (u,v,lag) means theta[v]-theta[u] = lag mod m. Roots normalize
    each connected component; no absolute external time is manufactured.
    """
    if any(type(x) is not int for x in (count, modulus)) or count < 1 or modulus < 2:
        raise GeometryError("Finite clock graph and modulus >=2 required")
    neighbors = [[] for _ in range(count)]
    for u, v, lag in edges:
        if any(type(x) is not int for x in (u, v, lag)) or not 0 <= u < count or not 0 <= v < count:
            raise GeometryError("Clock edge outside domain")
        neighbors[u].append((v, lag % modulus))
        neighbors[v].append((u, -lag % modulus))
    phases, parent = {}, {}
    for root in range(count):
        if root in phases:
            continue
        phases[root], parent[root] = 0, None
        todo = deque([root])
        while todo:
            u = todo.popleft()
            for v, lag in neighbors[u]:
                wanted = (phases[u]+lag) % modulus
                if v not in phases:
                    phases[v], parent[v] = wanted, u
                    todo.append(v)
                elif phases[v] != wanted:
                    def root_path(x):
                        path = [x]
                        while parent[path[-1]] is not None:
                            path.append(parent[path[-1]])
                        return path
                    up, vp = root_path(u), root_path(v)
                    common = next(x for x in up if x in vp)
                    cycle = tuple(list(reversed(up[:up.index(common)+1])) + vp[:vp.index(common)+1])
                    return {"phases": None, "cycle": cycle,
                            "residual": (phases[u]+lag-phases[v]) % modulus,
                            "conflicting_edge": (u, v, lag)}
    return {"phases": tuple(phases[x] for x in range(count)), "cycle": None, "residual": 0}
