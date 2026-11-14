"""Exact response geometry of finite linear carriers (Principia Observatoris, Second Forge).

A carrier is a square rational matrix ``A`` acting by ``z_{t+1} = A z_t``;
``A[v][u]`` is the weight of the structural edge ``u -> v``.  The lag-``tau``
response of node ``y`` to a unit impulse at node ``x`` is ``(A**tau)[y][x]``
(the founding note's ``C A^{t-s-1} B`` with coordinate input and readout; its
lag index is shifted by one because it injects through ``B``).

Everything here is exact rational arithmetic on a DECLARED finite table.
Classical ingredients: Cayley-Hamilton, Harary's balance theorem for signed
graphs, diagonal similarity of matrices (Engel-Schneider; Fiedler-Ptak) and
finite propagation along a dependency graph.  The module assembles them into
checkable statements about when net response reflects structural dependency;
it authenticates no physical source and proves nothing about signed
arithmetic cancellation in any number-theoretic carrier.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product

Matrix = tuple[tuple[Fraction, ...], ...]


class ResponseGeometryError(ValueError):
    """Malformed carrier table or ill-typed request."""


def matrix(rows) -> Matrix:
    """Validate a square table and convert its entries to exact rationals."""
    out = tuple(tuple(Fraction(v) for v in row) for row in rows)
    n = len(out)
    if n == 0 or any(len(row) != n for row in out):
        raise ResponseGeometryError("A nonempty square table is required")
    return out


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(int(i == j)) for j in range(n)) for i in range(n))


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(n)), Fraction(0))
                       for j in range(n)) for i in range(n))


def powers(a: Matrix, horizon: int) -> tuple[Matrix, ...]:
    """``A**0, ..., A**horizon``."""
    if horizon < 0:
        raise ResponseGeometryError("Nonnegative horizon required")
    out = [identity(len(a))]
    for _ in range(horizon):
        out.append(mat_mul(a, out[-1]))
    return tuple(out)


def absolute(a: Matrix) -> Matrix:
    return tuple(tuple(abs(v) for v in row) for row in a)


def is_nonnegative(a: Matrix) -> bool:
    return all(v >= 0 for row in a for v in row)


def edges(a: Matrix) -> tuple[tuple[int, int], ...]:
    """Structural edges ``(u, v)`` meaning ``u -> v``, i.e. ``A[v][u] != 0``."""
    n = len(a)
    return tuple((u, v) for u in range(n) for v in range(n) if a[v][u] != 0)


def walk_exists(a: Matrix, horizon: int) -> tuple[tuple[tuple[bool, ...], ...], ...]:
    """``W[tau][y][x]``: a structural walk of length exactly ``tau`` from x to y."""
    n = len(a)
    pattern = tuple(tuple(a[v][u] != 0 for u in range(n)) for v in range(n))
    current = tuple(tuple(i == j for j in range(n)) for i in range(n))
    out = [current]
    for _ in range(horizon):
        current = tuple(tuple(any(pattern[y][k] and current[k][x] for k in range(n))
                              for x in range(n)) for y in range(n))
        out.append(current)
    return tuple(out)


def structural_distance(a: Matrix) -> tuple[tuple[int | None, ...], ...]:
    """``d[x][y]``: least number of structural edges from x to y; ``None`` if none."""
    n = len(a)
    succ = [[v for v in range(n) if a[v][u] != 0] for u in range(n)]
    table = []
    for x in range(n):
        dist: list[int | None] = [None] * n
        dist[x] = 0
        queue = deque([x])
        while queue:
            u = queue.popleft()
            for v in succ[u]:
                if dist[v] is None:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        table.append(tuple(dist))
    return tuple(table)


def effect_time(a: Matrix, x: int, y: int) -> int | None:
    """Least lag with nonzero net response of y to an impulse at x.

    ``None`` is an ALL-lag statement: by Cayley-Hamilton the scalar sequence
    ``(A**tau)[y][x]`` obeys a monic recurrence of order ``n``, so ``n``
    consecutive zeros (lags ``0..n-1``) force zero at every lag.  The bound is
    for this declared dimension; it is not a black-box guarantee.
    """
    n = len(a)
    for tau, p in enumerate(powers(a, n - 1)):
        if p[y][x] != 0:
            return tau
    return None


def switching_function(a: Matrix) -> tuple[int, ...] | None:
    """A sign vector ``s`` with ``s[v]*A[v][u]*s[u] >= 0`` for all entries, or ``None``.

    Existence is balance of the signed structure graph (Harary 1953): no closed
    walk of the underlying undirected signed multigraph has negative sign
    product.  A negative self-loop or an opposite-sign two-cycle is unbalanced.
    """
    n = len(a)
    sign: list[int | None] = [None] * n
    nbrs: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v in edges(a):
        s = 1 if a[v][u] > 0 else -1
        nbrs[u].append((v, s))
        nbrs[v].append((u, s))
    for root in range(n):
        if sign[root] is not None:
            continue
        sign[root] = 1
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, s in nbrs[u]:
                want = sign[u] * s
                if sign[v] is None:
                    sign[v] = want
                    queue.append(v)
                elif sign[v] != want:
                    return None
    return tuple(int(s) for s in sign)  # type: ignore[arg-type]


def is_balanced_up_to_sign(a: Matrix) -> bool:
    """Balance of ``A`` or of ``-A``: every walk of a given length between two
    nodes then has the same sign, so nothing can cancel at any lag (RG-4)."""
    negated = tuple(tuple(-v for v in row) for row in a)
    return switching_function(a) is not None or switching_function(negated) is not None


def cancellations(a: Matrix, horizon: int) -> tuple[tuple[int, int, int], ...]:
    """All ``(tau, x, y)`` with a structural walk but zero net response."""
    n = len(a)
    walks = walk_exists(a, horizon)
    out = []
    for tau, p in enumerate(powers(a, horizon)):
        for x in range(n):
            for y in range(n):
                if walks[tau][y][x] and p[y][x] == 0:
                    out.append((tau, x, y))
    return tuple(out)


def relevance(a: Matrix, horizon: int, discount: Fraction = Fraction(1)) -> Matrix:
    """``R_T[x][y] = max_{0<=tau<=T} discount**tau * |(A**tau)[y][x]|``.

    Note the index order: SOURCE first, then target.
    """
    if discount <= 0:
        raise ResponseGeometryError("Positive discount required")
    n = len(a)
    best = [[Fraction(0)] * n for _ in range(n)]
    scale = Fraction(1)
    for p in powers(a, horizon):
        for x in range(n):
            for y in range(n):
                best[x][y] = max(best[x][y], scale * abs(p[y][x]))
        scale *= discount
    return tuple(tuple(row) for row in best)


def triangle_violations(a: Matrix, s: int, t: int,
                        discount: Fraction = Fraction(1)) -> tuple[tuple[int, int, int], ...]:
    """Triples ``(x, y, z)`` with ``R_{s+t}(x,z) < R_s(x,y) * R_t(y,z)``."""
    n = len(a)
    rs, rt, rst = (relevance(a, h, discount) for h in (s, t, s + t))
    return tuple((x, y, z) for x, y, z in product(range(n), repeat=3)
                 if rst[x][z] < rs[x][y] * rt[y][z])


def rescale(a: Matrix, units: tuple[Fraction, ...]) -> Matrix:
    """Change of node units ``z' = D z``: returns ``D A D^{-1}``."""
    n = len(a)
    if len(units) != n or any(Fraction(d) <= 0 for d in units):
        raise ResponseGeometryError("One positive unit per node required")
    return tuple(tuple(Fraction(units[v]) * a[v][u] / Fraction(units[u])
                       for u in range(n)) for v in range(n))


def diagonal_similarity(a: Matrix, b: Matrix) -> tuple[Fraction, ...] | None:
    """Positive units ``d`` with ``B = D A D^{-1}``, or ``None`` when none exist.

    Requires equal zero patterns and equal entry signs.  The units are found by
    propagating ``d[v] = d[u] * B[v][u] / A[v][u]`` over the underlying
    undirected structure graph and then CHECKED on every edge, so a returned
    vector is a verified certificate; ``None`` is a verified refusal because
    the propagation is forced once a value is fixed on each weak component.
    """
    n = len(a)
    if len(b) != n:
        return None
    for u in range(n):
        for v in range(n):
            if (a[v][u] == 0) != (b[v][u] == 0):
                return None
            if a[v][u] != 0 and (a[v][u] > 0) != (b[v][u] > 0):
                return None
    ratio = {(u, v): b[v][u] / a[v][u] for u, v in edges(a)}
    nbrs: list[list[tuple[int, Fraction]]] = [[] for _ in range(n)]
    for (u, v), r in ratio.items():
        nbrs[u].append((v, r))
        nbrs[v].append((u, 1 / r))
    units: list[Fraction | None] = [None] * n
    for root in range(n):
        if units[root] is not None:
            continue
        units[root] = Fraction(1)
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, r in nbrs[u]:
                if units[v] is None:
                    units[v] = units[u] * r
                    queue.append(v)
    result = tuple(units)  # type: ignore[arg-type]
    return result if rescale(a, result) == b else None


def weak_components(a: Matrix) -> int:
    n = len(a)
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for u, v in edges(a):
        parent[find(u)] = find(v)
    return len({find(i) for i in range(n)})


def gauge_invariant_dimension(a: Matrix) -> int:
    """First Betti number ``|E| - |V| + c`` of the structure multigraph.

    For positive edge weights this is the number of independent magnitudes
    left after quotienting by node-unit changes: ``|E|`` weights, minus the
    ``|V| - c`` effective unit choices (a common factor on a weak component
    acts trivially).  Zero for a forest: every positive weighting of a forest
    pattern is a pure unit convention.
    """
    return len(edges(a)) - len(a) + weak_components(a)


def simple_cycle_products(a: Matrix) -> dict[tuple[int, ...], Fraction]:
    """Weight product of every simple directed cycle, keyed by its rotation
    starting at the least node.  Exponential; for small declared tables only."""
    n = len(a)
    succ = [[v for v in range(n) if a[v][u] != 0] for u in range(n)]
    out: dict[tuple[int, ...], Fraction] = {}

    def extend(start: int, path: list[int], weight: Fraction) -> None:
        u = path[-1]
        for v in succ[u]:
            w = weight * a[v][u]
            if v == start:
                out[tuple(path)] = w
            elif v > start and v not in path:
                path.append(v)
                extend(start, path, w)
                path.pop()

    for start in range(n):
        extend(start, [start], Fraction(1))
    return out


def quotient_pattern(a: Matrix, labels: tuple[int, ...]) -> Matrix:
    """Existential ("may") quotient structure: block edge iff some source edge."""
    n = len(a)
    if len(labels) != n or sorted(set(labels)) != list(range(len(set(labels)))):
        raise ResponseGeometryError("Labels must be 0..m-1, one per node, all used")
    m = len(set(labels))
    table = [[Fraction(0)] * m for _ in range(m)]
    for u, v in edges(a):
        table[labels[v]][labels[u]] = Fraction(1)
    return tuple(tuple(row) for row in table)


def detection_lower_bound(a: Matrix, cause: int, sensors: tuple[int, ...]) -> int | None:
    """Least structural distance from the cause to any sensor (``None``: never).

    No lawful record-driven policy on this declared carrier can have a record
    that depends on the cause before this time; see the cone lemma in
    CAUSAL_GEOMETRY.md.  It is a lower bound, attained by cancellation-free
    carriers and possibly exceeded by signed ones.
    """
    dist = structural_distance(a)[cause]
    reached = [dist[s] for s in sensors if dist[s] is not None]
    return min(reached) if reached else None


def warning_margin(a: Matrix, cause: int, target: int,
                   sensors: tuple[int, ...]) -> int | None:
    """Structural lead time ``d(cause,target) - d(cause,sensors)``.

    Positive: some sensor is structurally closer to the cause than the target
    is, so early warning is not excluded.  Zero or negative: on this carrier no
    policy reading only these sensors can have evidence strictly before the
    earliest possible effect on the target.  ``None``: the target or every
    sensor is structurally unreachable from the cause.
    """
    d_target = structural_distance(a)[cause][target]
    d_sensor = detection_lower_bound(a, cause, sensors)
    if d_target is None or d_sensor is None:
        return None
    return d_target - d_sensor


# The smallest all-lag hidden dependency: x -> y, x -> y', y -> z (+1), y' -> z (-1).
# Node order (x, y, y', z).  Every edge is live, yet z never responds to x.
SIGNED_DIAMOND: Matrix = matrix((
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 0),
))
