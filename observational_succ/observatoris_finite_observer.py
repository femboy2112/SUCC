"""OPUS I -- the finite observer (Principia Observatoris, Second Forge).

Exact laboratory for the report
research/2026-11-14/principia_observatoris_second_forge/agents/OPUS_I_FINITE_OBSERVER.md.

Scope: declared FINITE models only, exact int / Fraction / hashable labels.
Nothing here certifies a physical instrument, a brain, RH or normality.

Four parts, matching theorems FO-1 .. FO-12 of the report:

A1  pointed finite carriers (X, A, o_a, t_a, x0); transcript convention is the
    one of carrier_relative_targets.trace (each readout is recorded BEFORE that
    instrument's transition).  Behavioural equivalence, minimal core, sharp
    bounded-length identification and constructive reconstruction.
    CLASSICAL lineage: Moore (1956), Nerode (1958), Kalman realization;
    sharp unary family uses the Fine--Wilf extremal phenomenon.
A2  Boolean / finite-valued interaction expansions at a baseline (Moebius
    inversion on the Boolean lattice, CLASSICAL: Rota 1964), the intervention
    order horizon, baseline transport, and certification cost of ABSENCE.
A3  deterministic acyclic networks with clamping interventions: hidden-wiring
    non-identifiability, the realized-context lemma, an exact identifiability
    criterion for the unrestricted class.
A4  single-copy ("free") observability: an exact all-horizon decision by a
    least fixed point on belief sets; the destructive A,B,C control of
    docs/CARRIER_RELATIVE_TARGETS.md section 3.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import comb
from typing import Callable, Hashable, Iterable, Mapping


class ObserverError(ValueError):
    """Malformed declared model, inconsistent data, or violated hypothesis."""


BOTTOM = ("<unavailable>",)
"""Readout recorded when an instrument is unavailable (partial transition).

Treating refusal as an observable output is a MODELLING ASSUMPTION (see
future_safe_quotient.trace): it presumes a lawful rejection interface."""


def _popcount(x: int) -> int:
    return bin(x).count("1")


# ---------------------------------------------------------------------------
# A1. Pointed finite carriers
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FiniteCarrier:
    """Finite states 0..size-1, named instruments, readout[a][x], transition[a][x].

    transition[a][x] is an int or None (instrument unavailable at x).
    """

    size: int
    instruments: tuple
    readout: tuple
    transition: tuple
    start: int = 0

    def __post_init__(self) -> None:
        if type(self.size) is not int or self.size < 1:
            raise ObserverError("positive integer state count required")
        if (type(self.instruments) is not tuple or not self.instruments
                or any(type(a) is not str or not a for a in self.instruments)
                or len(set(self.instruments)) != len(self.instruments)):
            raise ObserverError("nonempty tuple of distinct instrument names required")
        p = len(self.instruments)
        if (type(self.readout) is not tuple or type(self.transition) is not tuple
                or len(self.readout) != p or len(self.transition) != p):
            raise ObserverError("one readout row and one transition row per instrument")
        for row in self.readout:
            if type(row) is not tuple or len(row) != self.size:
                raise ObserverError("readout rows must be aligned tuples")
            for v in row:
                if type(v) is float or v == BOTTOM:
                    raise ObserverError("exact, non-reserved readout values required")
                hash(v)
        for row in self.transition:
            if type(row) is not tuple or len(row) != self.size:
                raise ObserverError("transition rows must be aligned tuples")
            for v in row:
                if v is not None and (type(v) is not int or not 0 <= v < self.size):
                    raise ObserverError("transition targets must be states or None")
        if type(self.start) is not int or not 0 <= self.start < self.size:
            raise ObserverError("start must be a declared state")

    @property
    def is_total(self) -> bool:
        return all(v is not None for row in self.transition for v in row)

    def at(self, start: int) -> "FiniteCarrier":
        return FiniteCarrier(self.size, self.instruments, self.readout, self.transition, start)


def _tables(c: FiniteCarrier):
    """Totalized tables (n, R, T): unavailable -> BOTTOM readout and sink state."""
    if c.is_total:
        return c.size, [list(r) for r in c.readout], [list(t) for t in c.transition]
    n = c.size + 1
    sink = c.size
    R, T = [], []
    for r, t in zip(c.readout, c.transition):
        R.append([BOTTOM if t[x] is None else r[x] for x in range(c.size)] + [BOTTOM])
        T.append([sink if t[x] is None else t[x] for x in range(c.size)] + [sink])
    return n, R, T


def totalize(c: FiniteCarrier) -> tuple:
    """Return the totalized tables (states, readout, transition) as tuples."""
    n, R, T = _tables(c)
    return n, tuple(map(tuple, R)), tuple(map(tuple, T))


def _word_indices(c: FiniteCarrier, word) -> list:
    if type(word) is not tuple:
        raise ObserverError("words are tuples of instrument names")
    try:
        return [c.instruments.index(a) for a in word]
    except ValueError:
        raise ObserverError("instrument outside the declared toolkit") from None


def transcript(c: FiniteCarrier, word: tuple, state: int | None = None) -> tuple:
    """Readouts along `word` from `state` (default: the selected start)."""
    n, R, T = _tables(c)
    x = c.start if state is None else state
    if type(x) is not int or not 0 <= x < n:
        raise ObserverError("unknown state")
    out = []
    for a in _word_indices(c, word):
        out.append(R[a][x])
        x = T[a][x]
    return tuple(out)


def words(instruments: tuple, max_len: int, min_len: int = 1):
    """All words in length-lexicographic order."""
    for L in range(min_len, max_len + 1):
        yield from product(instruments, repeat=L)


def response_table(c: FiniteCarrier, max_len: int) -> dict:
    """f(w) = readout of the LAST letter of w, for all 1 <= |w| <= max_len.

    The transcript of w is (f(w[:1]), ..., f(w)), so this table and the set of
    all transcripts of length <= max_len carry the same information.
    """
    if type(max_len) is not int or max_len < 0:
        raise ObserverError("nonnegative integer length required")
    n, R, T = _tables(c)
    table = {}
    frontier = [((), c.start)]
    for _ in range(max_len):
        nxt = []
        for w, x in frontier:
            for i, a in enumerate(c.instruments):
                table[w + (a,)] = R[i][x]
                nxt.append((w + (a,), T[i][x]))
        frontier = nxt
    return table


def _refine(R, T, blocks, n):
    keys = [tuple((R[a][x], blocks[T[a][x]]) for a in range(len(R))) for x in range(n)]
    ids, out = {}, []
    for k in keys:
        out.append(ids.setdefault(k, len(ids)))
    return out


def k_blocks(c: FiniteCarrier, k: int) -> tuple:
    """Block ids of k-equivalence (agreement on all words of length <= k)."""
    n, R, T = _tables(c)
    blocks = [0] * n
    for _ in range(k):
        blocks = _refine(R, T, blocks, n)
    return tuple(blocks)


def behaviour_blocks(c: FiniteCarrier) -> tuple:
    """Block ids of all-word behavioural equivalence on the totalized carrier."""
    n, R, T = _tables(c)
    blocks = [0] * n
    count = 1
    while True:
        new = _refine(R, T, blocks, n)
        new_count = max(new) + 1
        if new_count == count:
            return tuple(new)
        blocks, count = new, new_count


def reachable(c: FiniteCarrier) -> tuple:
    n, R, T = _tables(c)
    seen = [c.start]
    found = {c.start}
    q = deque([c.start])
    while q:
        x = q.popleft()
        for a in range(len(T)):
            y = T[a][x]
            if y not in found:
                found.add(y)
                seen.append(y)
                q.append(y)
    return tuple(seen)


@dataclass(frozen=True)
class Core:
    """Canonical minimal (reachable and observable) pointed realization.

    rows[i] = (readouts per instrument, successor class per instrument); class 0
    is the class of the start; numbering is breadth-first in instrument order,
    so two cores are isomorphic iff they are equal.
    """

    instruments: tuple
    rows: tuple

    @property
    def size(self) -> int:
        return len(self.rows)

    def carrier(self) -> FiniteCarrier:
        p = len(self.instruments)
        readout = tuple(tuple(0 if r[0][a] == BOTTOM else r[0][a] for r in self.rows)
                        for a in range(p))
        transition = tuple(tuple(None if r[0][a] == BOTTOM else r[1][a] for r in self.rows)
                           for a in range(p))
        return FiniteCarrier(self.size, self.instruments, readout, transition, 0)


def _canonical(instruments, R, T, start, blocks) -> Core:
    order = {blocks[start]: 0}
    reps = [start]
    rows = []
    i = 0
    while i < len(reps):
        x = reps[i]
        nxt = []
        for a in range(len(R)):
            b = blocks[T[a][x]]
            if b not in order:
                order[b] = len(reps)
                reps.append(T[a][x])
            nxt.append(order[b])
        rows.append((tuple(R[a][x] for a in range(len(R))), tuple(nxt)))
        i += 1
    return Core(instruments, tuple(rows))


def core(c: FiniteCarrier) -> Core:
    n, R, T = _tables(c)
    return _canonical(c.instruments, R, T, c.start, behaviour_blocks(c))


def first_disagreement(c1: FiniteCarrier, c2: FiniteCarrier) -> tuple | None:
    """Shortest word on which the two pointed carriers' responses differ."""
    if c1.instruments != c2.instruments:
        raise ObserverError("responses are compared only for the same instrument names")
    n1, R1, T1 = _tables(c1)
    n2, R2, T2 = _tables(c2)
    start = (c1.start, c2.start)
    parent = {start: None}
    q = deque([start])
    while q:
        x, y = q.popleft()
        for a in range(len(R1)):
            if R1[a][x] != R2[a][y]:
                w = [c1.instruments[a]]
                node = (x, y)
                while parent[node] is not None:
                    node, letter = parent[node]
                    w.append(letter)
                return tuple(reversed(w))
            nxt = (T1[a][x], T2[a][y])
            if nxt not in parent:
                parent[nxt] = ((x, y), c1.instruments[a])
                q.append(nxt)
    return None


def agreement_horizon(c1: FiniteCarrier, c2: FiniteCarrier) -> int | None:
    """Largest L with identical responses on all words of length <= L; None = all."""
    w = first_disagreement(c1, c2)
    return None if w is None else len(w) - 1


def reconstruct_core(instruments: tuple, data: Mapping, n: int) -> Core:
    """Rebuild the core from responses on all words of length 1..2n-1 (FO-2c).

    The output always reproduces every supplied datum, and it EQUALS the true
    core whenever the hypothesis "core size <= n" holds.  Data detectably
    inconsistent with the bound raise ObserverError.  Under a FALSE bound the
    output can be a smaller machine that matches the truncated data; this is
    unavoidable (FO-2b sharpness), not a recoverable bug.
    """
    if type(n) is not int or n < 1:
        raise ObserverError("positive core-size bound required")
    instruments = tuple(instruments)
    need = 2 * n - 1
    for w in words(instruments, need):
        if w not in data:
            raise ObserverError(f"missing datum for word of length {len(w)}")
    p = len(instruments)
    if n == 1:
        rows = [tuple(data[(a,)] for a in instruments)]
        access = [()]
        nexts = [[0] * p]
    else:
        suffixes = list(words(instruments, n - 1))

        def row(u):
            return tuple(data[u + v] for v in suffixes)

        index = {row(()): 0}
        access = [()]
        nexts = []
        i = 0
        while i < len(access):
            u = access[i]
            nx = []
            for a in instruments:
                r = row(u + (a,))
                if r not in index:
                    if len(u) + 1 > n - 1:
                        raise ObserverError("data inconsistent with the declared core-size bound")
                    index[r] = len(access)
                    access.append(u + (a,))
                nx.append(index[r])
            nexts.append(nx)
            i += 1
        rows = [tuple(data[u + (a,)] for a in instruments) for u in access]
    readout = tuple(tuple(0 if rows[s][a] == BOTTOM else rows[s][a] for s in range(len(access)))
                    for a in range(p))
    transition = tuple(tuple(None if rows[s][a] == BOTTOM else nexts[s][a]
                             for s in range(len(access))) for a in range(p))
    rebuilt = FiniteCarrier(len(access), instruments, readout, transition, 0)
    check = response_table(rebuilt, need)
    if any(check[w] != data[w] for w in check):
        raise ObserverError("data inconsistent with the declared core-size bound")
    return core(rebuilt)


def _unary(readouts: list, transitions: list) -> FiniteCarrier:
    return FiniteCarrier(len(readouts), ("a",), (tuple(readouts),), (tuple(transitions),), 0)


def sharp_pair(n: int, m: int) -> tuple:
    """Unary carriers with core sizes n, m agreeing on lengths <= n+m-2, not n+m-1.

    Cycle of p states emitting c except d at positions k = q-1 (mod p), and a
    chain of q states copying the first q-1 outputs and then emitting c.
    """
    if type(n) is not int or type(m) is not int or n < 1 or m < 1:
        raise ObserverError("positive sizes required")
    if n == m == 1:
        return _unary([0], [0]), _unary([1], [0])
    swap = n == 1
    p, q = (m, n) if swap else (n, m)
    c, d = 0, 1

    def s(k):  # 1-indexed output of the cycle machine
        return d if (k - (q - 1)) % p == 0 else c
    cycle = _unary([s(i + 1) for i in range(p)], [(i + 1) % p for i in range(p)])
    chain = _unary([s(i + 1) if i + 1 <= q - 1 else c for i in range(q)],
                   [min(i + 1, q - 1) for i in range(q)])
    return (chain, cycle) if swap else (cycle, chain)


def restrict(c: FiniteCarrier, names: Iterable[str]) -> FiniteCarrier:
    names = tuple(names)
    idx = _word_indices(c, names)
    return FiniteCarrier(c.size, names, tuple(c.readout[i] for i in idx),
                         tuple(c.transition[i] for i in idx), c.start)


def toolkit_reduct_cores(c: FiniteCarrier, names: Iterable[str]) -> tuple:
    """(core of c with toolkit `names`, core of (core of c)|names) -- equal by FO-3."""
    names = tuple(names)
    return core(restrict(c, names)), core(restrict(core(c).carrier(), names))


def split_instrument(c: FiniteCarrier, name: str) -> FiniteCarrier:
    """Replace instrument (o, t) by a pure measurement (o, id) and pure action (0, t)."""
    if not c.is_total:
        raise ObserverError("splitting is declared for total carriers")
    i = c.instruments.index(name)
    others = [j for j in range(len(c.instruments)) if j != i]
    names = tuple(c.instruments[j] for j in others) + (name + "!measure", name + "!act")
    readout = tuple(c.readout[j] for j in others) + (c.readout[i], tuple(0 for _ in range(c.size)))
    transition = tuple(c.transition[j] for j in others) + (tuple(range(c.size)), c.transition[i])
    return FiniteCarrier(c.size, names, readout, transition, c.start)


def enumerate_carriers(n: int, instruments: tuple, alphabet: tuple = (0, 1)):
    """All TOTAL carriers on n states with the given instruments, start 0."""
    p = len(instruments)
    trans_rows = list(product(range(n), repeat=n))
    read_rows = list(product(alphabet, repeat=n))
    for ts in product(trans_rows, repeat=p):
        for rs in product(read_rows, repeat=p):
            yield FiniteCarrier(n, instruments, rs, ts, 0)


def same_partition(blocks_a: tuple, blocks_b: tuple) -> bool:
    return all((blocks_a[x] == blocks_a[y]) == (blocks_b[x] == blocks_b[y])
               for x in range(len(blocks_a)) for y in range(len(blocks_a)))


def to_carrier_relative(c: FiniteCarrier, source: str = "opus-i"):
    """Convert a TOTAL carrier to carrier_relative_targets.Carrier (unit costs)."""
    from .carrier_relative_targets import Carrier, Instrument
    if not c.is_total:
        raise ObserverError("carrier_relative_targets requires total transitions")
    insts = []
    for name, row, t in zip(c.instruments, c.readout, c.transition):
        codes = {}
        for v in row:
            codes.setdefault(v, len(codes))
        insts.append(Instrument(name, name + ":chart", tuple(Fraction(codes[v]) for v in row), t, 1))
    return Carrier(source, c.size, tuple(insts))


# ---------------------------------------------------------------------------
# A2. Interaction-order horizons on {0,1}^k and finite products
# ---------------------------------------------------------------------------

def _reduce(v: int, modulus: int | None) -> int:
    return v if modulus is None else v % modulus


def _check_boolean(values, k):
    if type(k) is not int or k < 0 or type(values) is not tuple or len(values) != 1 << k:
        raise ObserverError("a tuple of 2**k exact values (index = bitmask) is required")
    if any(type(v) is not int for v in values):
        raise ObserverError("integer group values required (G = Z or Z/m)")


def mobius_coefficients(values: tuple, k: int, baseline: int = 0,
                        modulus: int | None = None) -> tuple:
    """Delta_S f(c0) = sum_{T subset S} (-1)^{|S|-|T|} f(c0 xor 1_T), indexed by S."""
    _check_boolean(values, k)
    g = [values[baseline ^ T] for T in range(1 << k)]
    for i in range(k):
        bit = 1 << i
        for T in range(1 << k):
            if T & bit:
                g[T] = g[T] - g[T ^ bit]
    return tuple(_reduce(v, modulus) for v in g)


def synthesize(coeffs: tuple, k: int, baseline: int = 0, modulus: int | None = None) -> tuple:
    """Inverse: f(c0 xor 1_T) = sum_{S subset T} Delta_S."""
    g = list(coeffs)
    for i in range(k):
        bit = 1 << i
        for T in range(1 << k):
            if T & bit:
                g[T] = g[T] + g[T ^ bit]
    out = [0] * (1 << k)
    for T in range(1 << k):
        out[baseline ^ T] = _reduce(g[T], modulus)
    return tuple(out)


def interaction_horizon(values: tuple, k: int, baseline: int, j: int,
                        modulus: int | None = None) -> int | None:
    """min{|S| : j in S, Delta_S f(baseline) != 0}; None iff j is inessential."""
    coeffs = mobius_coefficients(values, k, baseline, modulus)
    sizes = [_popcount(S) for S in range(1 << k) if S >> j & 1 and coeffs[S] != 0]
    return min(sizes) if sizes else None


def ball_horizon(values: tuple, k: int, baseline: int, j: int) -> int | None:
    """Independent route: least radius whose Hamming ball holds a j-pair with a difference."""
    best = None
    for x in range(1 << k):
        y = x ^ (1 << j)
        if x < y and values[x] != values[y]:
            r = max(_popcount(x ^ baseline), _popcount(y ^ baseline))
            best = r if best is None else min(best, r)
    return best


def essential(values: tuple, k: int, j: int) -> bool:
    return any(values[x] != values[x ^ (1 << j)] for x in range(1 << k))


def independent_extension(values: tuple, k: int, baseline: int, j: int, r: int) -> tuple | None:
    """A j-independent function equal to `values` on the radius-r ball, or None."""
    out = list(values)
    for x in range(1 << k):
        y = x ^ (1 << j)
        if x > y:
            continue
        inx, iny = _popcount(x ^ baseline) <= r, _popcount(y ^ baseline) <= r
        if inx and iny and values[x] != values[y]:
            return None
        v = values[x] if inx or not iny else values[y]
        out[x] = out[y] = v
    return tuple(out)


def transport_coefficients(coeffs: tuple, k: int, shift: int,
                           modulus: int | None = None) -> tuple:
    """Coefficients at baseline b xor shift from those at b (FO-5):

    Delta_V(b xor C) = (-1)^{|V & C|} * sum_{V <= S <= V | C} Delta_S(b).
    """
    out = []
    for V in range(1 << k):
        free = shift & ~V
        total = 0
        sub = free
        while True:
            total += coeffs[V | sub]
            if sub == 0:
                break
            sub = (sub - 1) & free
        sign = -1 if _popcount(V & shift) % 2 else 1
        out.append(_reduce(sign * total, modulus))
    return tuple(out)


def mobius_degree(coeffs: tuple) -> int | None:
    sizes = [_popcount(S) for S, a in enumerate(coeffs) if a != 0]
    return max(sizes) if sizes else None


def variable_degree(coeffs: tuple, j: int) -> int | None:
    sizes = [_popcount(S) for S, a in enumerate(coeffs) if a != 0 and S >> j & 1]
    return max(sizes) if sizes else None


def _rank_mod_p(rows: list, p: int) -> int:
    rows = [[v % p for v in r] for r in rows]
    rank, col = 0, 0
    ncols = len(rows[0]) if rows else 0
    while rank < len(rows) and col < ncols:
        piv = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], p - 2, p)
        rows[rank] = [v * inv % p for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
        col += 1
    return rank


def certifies_absence(points: Iterable[int], k: int, d: int, j: int, p: int) -> bool:
    """Do values on `points` certify j-independence for EVERY degree<=d f into GF(p)?

    Certification is a property of the query set alone (the class is linear):
    it holds iff every degree<=d h vanishing on the points has no monomial
    containing j, i.e. every such coordinate functional is in the row space.
    """
    points = sorted(set(points))
    monos = [S for S in range(1 << k) if _popcount(S) <= d]
    M = [[1 if S & ~x == 0 else 0 for S in monos] for x in points]
    E = [[1 if S == T else 0 for S in monos] for T in monos if T >> j & 1]
    if not E:
        return True
    base = _rank_mod_p(M, p) if M else 0
    return _rank_mod_p(M + E, p) == base


def certification_cost(k: int, d: int) -> int:
    """2 * sum_{i<d} C(k-1, i): the exact minimum number of evaluations (FO-6)."""
    if type(k) is not int or type(d) is not int or k < 1 or not 0 <= d <= k:
        raise ObserverError("1 <= k and 0 <= d <= k required")
    return 2 * sum(comb(k - 1, i) for i in range(d))


def ball_pair_points(k: int, d: int, j: int, baseline: int = 0) -> tuple:
    """Optimal certificate: both j-values over the radius-(d-1) ball of the others."""
    mask = ~(1 << j)
    return tuple(x for x in range(1 << k) if _popcount((x ^ baseline) & mask) <= d - 1)


def exhaustive_minimum_certifying(k: int, d: int, j: int, p: int) -> int:
    """Verify FO-6 exhaustively: the ball pair certifies, and no smaller set does.

    Certification is monotone under supersets, so checking all sets of size
    t-1 suffices for the lower bound.
    """
    t = certification_cost(k, d)
    pts = ball_pair_points(k, d, j)
    if len(pts) != t or not certifies_absence(pts, k, d, j, p):
        raise ObserverError("upper-bound certificate failed")
    if t >= 1:
        for Q in combinations(range(1 << k), t - 1):
            if certifies_absence(Q, k, d, j, p):
                raise ObserverError(f"smaller certifying set found: {Q}")
    return t


def ball_points(k: int, r: int, baseline: int = 0) -> tuple:
    return tuple(x for x in range(1 << k) if _popcount(x ^ baseline) <= r)


# ---- finite value sets: reduction to anchored binary subcubes ----

def _contexts(value_sets):
    return product(*value_sets)


def general_essential(table: Mapping, value_sets: tuple, j: int) -> bool:
    for c in _contexts(value_sets):
        for a in value_sets[j]:
            if table[c] != table[c[:j] + (a,) + c[j + 1:]]:
                return True
    return False


def general_horizon(table: Mapping, value_sets: tuple, baseline: tuple, j: int) -> int | None:
    """Least |S| with j in S and a nonzero anchored coefficient Delta_S^b (any b)."""
    k = len(value_sets)
    alts = [tuple(v for v in vs if v != baseline[i]) for i, vs in enumerate(value_sets)]
    best = None
    for b in product(*alts):
        vals = []
        for T in range(1 << k):
            c = tuple(b[i] if T >> i & 1 else baseline[i] for i in range(k))
            vals.append(table[c])
        h = interaction_horizon(tuple(vals), k, 0, j)
        if h is not None:
            best = h if best is None else min(best, h)
    return best


def general_ball_horizon(table: Mapping, value_sets: tuple, baseline: tuple, j: int) -> int | None:
    def dist(c):
        return sum(1 for a, b in zip(c, baseline) if a != b)
    best = None
    for c in _contexts(value_sets):
        for a in value_sets[j]:
            e = c[:j] + (a,) + c[j + 1:]
            if table[c] != table[e]:
                r = max(dist(c), dist(e))
                best = r if best is None else min(best, r)
    return best


# ---- polynomial jets (CLASSICAL Taylor; exact Fractions) ----

def poly_eval(poly: Mapping, point: tuple) -> Fraction:
    total = Fraction(0)
    for e, coef in poly.items():
        term = Fraction(coef)
        for xi, ei in zip(point, e):
            term *= Fraction(xi) ** ei
        total += term
    return total


def taylor_jet(poly: Mapping, base: tuple, d: int) -> dict:
    """Coefficients of h^alpha (|alpha| <= d) in poly(base + h): the order-d jet."""
    jet = {}
    for e, coef in poly.items():
        ranges = [range(ei + 1) for ei in e]
        for alpha in product(*ranges):
            if sum(alpha) > d:
                continue
            term = Fraction(coef)
            for bi, ei, ai in zip(base, e, alpha):
                term *= comb(ei, ai) * Fraction(bi) ** (ei - ai)
            jet[alpha] = jet.get(alpha, Fraction(0)) + term
    return {a: v for a, v in jet.items() if v != 0}


def jet_predict(jet: Mapping, h: tuple) -> Fraction:
    return poly_eval(jet, h)


def poly_degree(poly: Mapping) -> int:
    return max((sum(e) for e, c in poly.items() if c != 0), default=-1)


# ---------------------------------------------------------------------------
# A3. Deterministic acyclic networks with clamping interventions
# ---------------------------------------------------------------------------

class Network:
    """Nodes in a fixed topological order; each node has a finite value set, a
    tuple of POTENTIAL parents (earlier nodes) and a total table on their
    product.  A root (no potential parents) holds a constant value."""

    def __init__(self, spec: Iterable) -> None:
        self.nodes, self.values, self.parents, self.tables = [], {}, {}, {}
        for name, vals, parents, fn in spec:
            if type(name) is not str or not name or name in self.values:
                raise ObserverError("distinct node names required")
            vals = tuple(vals)
            if len(vals) < 1 or len(set(vals)) != len(vals):
                raise ObserverError("finite value set of distinct values required")
            parents = tuple(parents)
            if any(p not in self.values for p in parents) or len(set(parents)) != len(parents):
                raise ObserverError("potential parents must be distinct EARLIER nodes")
            table = {}
            for ctx in product(*(self.values[p] for p in parents)):
                v = fn[ctx] if isinstance(fn, Mapping) else fn(*ctx)
                if v not in vals:
                    raise ObserverError(f"node {name} produced a value outside its set")
                table[ctx] = v
            self.nodes.append(name)
            self.values[name] = vals
            self.parents[name] = parents
            self.tables[name] = table
        self.nodes = tuple(self.nodes)

    def evaluate(self, clamps: Mapping | None = None) -> dict:
        clamps = dict(clamps or {})
        for n, v in clamps.items():
            if n not in self.values or v not in self.values[n]:
                raise ObserverError("clamp outside the declared nodes/values")
        state = {}
        for n in self.nodes:
            if n in clamps:
                state[n] = clamps[n]
            else:
                state[n] = self.tables[n][tuple(state[p] for p in self.parents[n])]
        return state

    def essential_parents(self, node: str) -> tuple:
        out = []
        ps = self.parents[node]
        table = self.tables[node]
        for i, p in enumerate(ps):
            if any(table[ctx] != table[ctx[:i] + (a,) + ctx[i + 1:]]
                   for ctx in table for a in self.values[p]):
                out.append(p)
        return tuple(out)

    def essential_graph(self) -> frozenset:
        return frozenset((p, n) for n in self.nodes for p in self.essential_parents(n))

    def has_essential_path(self, src: str, dst: str) -> bool:
        g = self.essential_graph()
        seen, stack = {src}, [src]
        while stack:
            u = stack.pop()
            if u == dst:
                return True
            for a, b in g:
                if a == u and b not in seen:
                    seen.add(b)
                    stack.append(b)
        return False

    def response(self, inputs: tuple, output: str) -> dict:
        """Accessible input-output data: clamp `inputs` jointly, read `output`."""
        return {ctx: self.evaluate(dict(zip(inputs, ctx)))[output]
                for ctx in product(*(self.values[i] for i in inputs))}


def experiment(clamps: Mapping, reads: Iterable[str]) -> tuple:
    return (tuple(sorted(clamps.items())), tuple(sorted(reads)))


def network_data(net: Network, experiments: Iterable) -> tuple:
    out = []
    for clamps, reads in experiments:
        state = net.evaluate(dict(clamps))
        out.append(tuple(state[r] for r in reads))
    return tuple(out)


def realized_contexts(net: Network, experiments: Iterable, node: str) -> frozenset:
    """Parent contexts of `node` realized while `node` is unclamped and read."""
    out = set()
    for clamps, reads in experiments:
        cl = dict(clamps)
        if node in cl or node not in reads:
            continue
        state = net.evaluate(cl)
        out.add(tuple(state[p] for p in net.parents[node]))
    return frozenset(out)


def enumerate_networks(skeleton: tuple, allowed: Callable | None = None):
    """All networks on skeleton ((name, values, potential_parents), ...).

    `allowed(name, parent_value_sets, table)` may filter node functions
    (e.g. monotone ones).
    """
    choices = []
    built = {}
    for name, vals, parents in skeleton:
        pv = [tuple(built[p]) for p in parents]
        ctxs = list(product(*pv))
        opts = []
        for outs in product(tuple(vals), repeat=len(ctxs)):
            table = dict(zip(ctxs, outs))
            if allowed is None or allowed(name, pv, table):
                opts.append(table)
        built[name] = tuple(vals)
        choices.append(opts)
    for tables in product(*choices):
        yield Network((name, vals, parents, t)
                      for (name, vals, parents), t in zip(skeleton, tables))


def monotone_table(name, parent_value_sets, table) -> bool:
    """Monotone w.r.t. the declared order of each value tuple (pointwise)."""
    ctxs = list(table)
    rank = [{v: i for i, v in enumerate(vs)} for vs in parent_value_sets]
    for c in ctxs:
        for e in ctxs:
            if all(rank[i][c[i]] <= rank[i][e[i]] for i in range(len(c))):
                if not table[c] <= table[e]:
                    return False
    return True


def class_identifies_graph(networks: Iterable, experiments: tuple) -> tuple:
    """(True, None) if equal data imply equal essential graphs; else a witness pair."""
    seen = {}
    for net in networks:
        sig = network_data(net, experiments)
        g = net.essential_graph()
        if sig in seen and seen[sig][0] != g:
            return False, (seen[sig][1], net)
        seen.setdefault(sig, (g, net))
    return True, None


def clamp_criterion(skeleton: tuple, experiments: tuple) -> bool:
    """FO-9: every node with potential parents is read, unclamped, with ALL its
    potential parents clamped to every joint context, in some experiment."""
    values = {name: tuple(v) for name, v, _ in skeleton}
    for name, _, parents in skeleton:
        if not parents:
            continue
        for ctx in product(*(values[p] for p in parents)):
            want = dict(zip(parents, ctx))
            if not any(name in reads and name not in dict(cl)
                       and all(dict(cl).get(p, None) == v for p, v in want.items())
                       for cl, reads in experiments):
                return False
    return True


def cancellation_pair() -> tuple:
    """Two-path signed cancellation (founding note, crucible 2) vs. no wiring."""
    sk = [("x", (0, 1), (), {(): 0})]
    n1 = Network(sk + [("z1", (0, 1), ("x",), lambda x: x),
                       ("z2", (0, 1), ("x",), lambda x: x),
                       ("y", (-1, 0, 1), ("z1", "z2"), lambda a, b: a - b)])
    n0 = Network(sk + [("z1", (0, 1), ("x",), lambda x: 0),
                       ("z2", (0, 1), ("x",), lambda x: 0),
                       ("y", (-1, 0, 1), ("z1", "z2"), lambda a, b: 0)])
    return n1, n0


def minimal_cancellation_pair() -> tuple:
    """One hidden binary node plus a direct edge: z = x, y = x XOR z."""
    sk = [("x", (0, 1), (), {(): 0})]
    n1 = Network(sk + [("z", (0, 1), ("x",), lambda x: x),
                       ("y", (0, 1), ("x", "z"), lambda x, z: x ^ z)])
    n0 = Network(sk + [("z", (0, 1), ("x",), lambda x: 0),
                       ("y", (0, 1), ("x", "z"), lambda x, z: 0)])
    return n1, n0


def gating_network() -> Network:
    """Monotone, cancellation-free: z1 = x, z2 = 0, y = z1 AND z2."""
    return Network([("x", (0, 1), (), {(): 0}),
                    ("z1", (0, 1), ("x",), lambda x: x),
                    ("z2", (0, 1), ("x",), lambda x: 0),
                    ("y", (0, 1), ("z1", "z2"), lambda a, b: a & b)])


def range_gate_network() -> Network:
    """Monotone single hidden ternary node: z = x in {0,1,2}, y = [z >= 2]."""
    return Network([("x", (0, 1), (), {(): 0}),
                    ("z", (0, 1, 2), ("x",), lambda x: x),
                    ("y", (0, 1), ("z",), lambda z: int(z >= 2))])


# ---------------------------------------------------------------------------
# A4. Single-copy (free) observability
# ---------------------------------------------------------------------------

def quotient(c: FiniteCarrier) -> tuple:
    """(class_of, k, R, T) of the behavioural quotient of the totalized carrier."""
    n, R, T = _tables(c)
    blocks = behaviour_blocks(c)
    k = max(blocks) + 1
    rep = {}
    for x in range(n):
        rep.setdefault(blocks[x], x)
    QR = [[R[a][rep[b]] for b in range(k)] for a in range(len(R))]
    QT = [[blocks[T[a][rep[b]]] for b in range(k)] for a in range(len(R))]
    return blocks, k, QR, QT


@dataclass(frozen=True)
class AccessPolicy:
    """Decision tree: leaf `answer`, or apply `instrument` and branch on readout."""
    answer: Hashable = None
    instrument: str | None = None
    children: tuple = ()


@dataclass(frozen=True)
class AccessResult:
    accessible: bool
    depth: int | None
    beliefs_explored: int
    policy: AccessPolicy | None


def _solve(c, initial, settled, fused, answer_of):
    """Least fixed point on reachable beliefs (frozensets of (label, class))."""
    blocks, k, QR, QT = quotient(c)
    p = len(QR)
    moves = {}
    order = [initial]
    seen = {initial}
    i = 0
    while i < len(order):
        B = order[i]
        i += 1
        if settled(B) or fused(B):
            moves[B] = []
            continue
        opts = []
        for a in range(p):
            groups = {}
            for lab, u in B:
                groups.setdefault(QR[a][u], set()).add((lab, QT[a][u]))
            kids = tuple((out, frozenset(g)) for out, g in groups.items())
            opts.append((a, kids))
            for _, kid in kids:
                if kid not in seen:
                    seen.add(kid)
                    order.append(kid)
        moves[B] = opts
    rank = {B: 0 for B in order if settled(B) and not fused(B)}
    choice = {}
    r = 0
    while True:
        r += 1
        new = {}
        for B in order:
            if B in rank:
                continue
            for a, kids in moves[B]:
                if all(kid in rank for _, kid in kids):
                    new[B] = r
                    choice[B] = (a, kids)
                    break
        if not new:
            break
        rank.update(new)

    def build(B):
        if rank[B] == 0:
            return AccessPolicy(answer=answer_of(B))
        a, kids = choice[B]
        return AccessPolicy(None, c.instruments[a],
                            tuple(sorted(((out, build(kid)) for out, kid in kids), key=repr)))
    if initial not in rank:
        return AccessResult(False, None, len(order), None)
    return AccessResult(True, rank[initial], len(order), build(initial))


def _start_set(c, start_set):
    S = tuple(range(c.size)) if start_set is None else tuple(sorted(set(start_set)))
    if not S or any(type(x) is not int or not 0 <= x < c.size for x in S):
        raise ObserverError("nonempty declared start set required")
    return S


def free_observability(c: FiniteCarrier, start_set: Iterable[int] | None = None) -> AccessResult:
    """Can ONE unresettable copy identify the behaviour class of its start in S?

    Equivalent to: every target in the counterfactual observation algebra
    (carrier_relative_targets) restricted to S is single-copy accessible.
    Exact for every horizon (no budget): the belief space is finite.
    """
    S = _start_set(c, start_set)
    blocks = behaviour_blocks(c)
    initial = frozenset((blocks[x], blocks[x]) for x in S)

    def settled(B):
        return len({lab for lab, _ in B}) == 1

    def fused(B):
        cur = {}
        for lab, u in B:
            if cur.setdefault(u, lab) != lab:
                return True
        return False
    return _solve(c, initial, settled, fused, lambda B: next(iter(B))[0])


def target_access(c: FiniteCarrier, target: Mapping, start_set: Iterable[int] | None = None) -> AccessResult:
    """All-horizon single-copy access to ONE target P (values on start states)."""
    S = _start_set(c, start_set)
    if any(x not in target for x in S):
        raise ObserverError("target must be declared on every possible start")
    blocks = behaviour_blocks(c)
    initial = frozenset((target[x], blocks[x]) for x in S)

    def settled(B):
        return len({lab for lab, _ in B}) == 1

    def fused(B):
        cur = {}
        for lab, u in B:
            if cur.setdefault(u, lab) != lab:
                return True
        return False
    return _solve(c, initial, settled, fused, lambda B: next(iter(B))[0])


def execute_policy(c: FiniteCarrier, policy: AccessPolicy, state: int, max_steps: int = 10_000):
    """Independent executor on the ORIGINAL (totalized) carrier."""
    n, R, T = _tables(c)
    node, x = policy, state
    for _ in range(max_steps):
        if node.instrument is None:
            return node.answer
        a = c.instruments.index(node.instrument)
        out = R[a][x]
        kids = dict(node.children)
        if out not in kids:
            raise ObserverError("policy lacks a branch for a realized readout")
        node, x = kids[out], T[a][x]
    raise ObserverError("policy did not terminate")


def class_nondisturbing(c: FiniteCarrier) -> bool:
    """t_a(x) ~ x for all a, x (behaviour class never changes)."""
    n, R, T = _tables(c)
    b = behaviour_blocks(c)
    return all(b[T[a][x]] == b[x] for a in range(len(T)) for x in range(n))


def class_injective(c: FiniteCarrier) -> bool:
    """Every instrument induces an injective map on behaviour classes."""
    blocks, k, QR, QT = quotient(c)
    return all(len(set(row)) == k for row in QT)


def commuting_idempotent(c: FiniteCarrier) -> bool:
    n, R, T = _tables(c)
    p = len(T)
    idem = all(T[a][T[a][x]] == T[a][x] for a in range(p) for x in range(n))
    comm = all(T[a][T[b][x]] == T[b][T[a][x]] for a in range(p) for b in range(p) for x in range(n))
    return idem and comm


def destructive_abc() -> FiniteCarrier:
    """docs/CARRIER_RELATIVE_TARGETS.md section 3: states A,B,C = 0,1,2."""
    return FiniteCarrier(3, ("a", "b"), ((1, 0, 0), (0, 1, 0)), ((0, 0, 0), (0, 0, 0)), 0)


def nondisturbing_abc() -> FiniteCarrier:
    return FiniteCarrier(3, ("a", "b"), ((1, 0, 0), (0, 1, 0)), ((0, 1, 2), (0, 1, 2)), 0)


def reset_and_readout() -> FiniteCarrier:
    """m reads the state without disturbance; r resets to 0 (not class-injective)."""
    return FiniteCarrier(2, ("m", "r"), ((0, 1), (0, 0)), ((0, 1), (0, 0)), 0)


def separately_but_not_jointly() -> FiniteCarrier:
    """States A,B,C,D = 0..3; start set {A,B,C}.  Instrument a (resp. b, c)
    flags A (resp. C, B) and then sends EVERY state to D.  Each Boolean target
    on the start set is single-copy accessible, but the class is not (FO-10d)."""
    flag = lambda s: tuple(int(x == s) for x in range(4))
    return FiniteCarrier(4, ("a", "b", "c"), (flag(0), flag(2), flag(1)),
                         ((3, 3, 3, 3),) * 3, 0)


def readout_swap() -> FiniteCarrier:
    """Disturbing but class-injective: read the bit, then flip it."""
    return FiniteCarrier(2, ("s",), ((0, 1),), ((1, 0),), 0)
