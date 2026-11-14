"""Quantale-weighted ancestral quotients: a small exact laboratory.

Companion to research/2026-11-14/principia_observatoris_second_forge/agents/
OPUS_II_CAUSAL_GEOMETER.md (theorems CG-1 ... CG-13).  Stdlib only; exact values
(bool, int, ``fractions.Fraction``, frozensets, ``math.inf`` as the tropical
bottom).

Status.  The underlying mathematics is CLASSICAL in different clothes:
quantale-enriched relations / Lawvere metric spaces (Lawvere 1973; Stubbe;
Hofmann-Seal-Tholen "Monoidal Topology"), shortest-path potentials (LP duality),
may/must abstraction (Larsen-Thomsen 1988; Dams-Gerth-Grumberg 1997), lumpability
(Kemeny-Snell 1960), bisimulation, Beck-Chevalley/mates (Kelly-Street 1974).
The assembly as a weighted generalisation of SUCC's PAP-01..PAP-05
(docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md) is new to the project; scholarly
novelty is not claimed.  Executable checks here are finite validation, not
proofs; the proofs are in the report.

Conventions (load-bearing for noncommutative V).
  * ``R[u][v]`` is the weight of the edge u -> v.  A path x0->x1->...->xn has
    weight R[x0][x1] (x) R[x1][x2] (x) ... in PATH ORDER (left to right).
  * A predicate phi: X -> V is R-closed when phi(u) (x) R[u][v] <= phi(v).
  * ``ldiv(a, c)`` is the left residual a\\c = V{b : a (x) b <= c};
    ``rdiv(c, b)`` is the right residual c/b = V{a : a (x) b <= c}.
  * A report map is a tuple ``q`` of ints in range(m); m may exceed the image.
No source authentication, probability, physics, RH or pi conclusion is supplied.
"""
from __future__ import annotations

import math
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Callable, Hashable, Iterable, Sequence

INF = math.inf


class QuantaleError(ValueError):
    """Malformed structure, failed certificate or non-terminating closure."""


# ---------------------------------------------------------------------------
# Quantales (and, for mutation tests, lattice-ordered monoids that are not)
# ---------------------------------------------------------------------------

class Quantale:
    """Complete lattice with associative unital tensor (interface only)."""

    name = "abstract"
    finite = False
    integral = False      # unit == top; then simple paths suffice for closure
    bottom: Hashable
    top: Hashable
    unit: Hashable

    def leq(self, a, b) -> bool: raise NotImplementedError
    def join2(self, a, b): raise NotImplementedError
    def meet2(self, a, b): raise NotImplementedError
    def tensor(self, a, b): raise NotImplementedError

    def join(self, values: Iterable) -> Hashable:
        out = self.bottom
        for v in values:
            out = self.join2(out, v)
        return out

    def meet(self, values: Iterable) -> Hashable:
        out = self.top
        for v in values:
            out = self.meet2(out, v)
        return out

    def elements(self) -> tuple:
        raise QuantaleError(f"{self.name} is not enumerable")

    def ldiv(self, a, c):
        """a\\c, by enumeration (finite case)."""
        return self.join(b for b in self.elements() if self.leq(self.tensor(a, b), c))

    def rdiv(self, c, b):
        """c/b, by enumeration (finite case)."""
        return self.join(a for a in self.elements() if self.leq(self.tensor(a, b), c))

    def lt(self, a, b) -> bool:
        return self.leq(a, b) and a != b

    def axiom_failures(self) -> list[str]:
        """Exhaustive finite check of the quantale axioms (empty list = quantale).

        For a finite lattice, binary-join and empty-join distributivity on both
        sides is equivalent to arbitrary-join distributivity.
        """
        el = self.elements()
        bad: list[str] = []
        for a, b in product(el, repeat=2):
            j, mt = self.join2(a, b), self.meet2(a, b)
            if not (self.leq(a, j) and self.leq(b, j)):
                bad.append(f"join not upper bound {a},{b}")
            if not (self.leq(mt, a) and self.leq(mt, b)):
                bad.append(f"meet not lower bound {a},{b}")
        for a in el:
            if self.tensor(self.unit, a) != a or self.tensor(a, self.unit) != a:
                bad.append(f"unit fails at {a}")
            if self.tensor(a, self.bottom) != self.bottom or \
                    self.tensor(self.bottom, a) != self.bottom:
                bad.append(f"empty-join distributivity fails at {a}")
        for a, b, c in product(el, repeat=3):
            if self.tensor(self.tensor(a, b), c) != self.tensor(a, self.tensor(b, c)):
                bad.append(f"associativity fails {a},{b},{c}")
            if self.tensor(a, self.join2(b, c)) != self.join2(self.tensor(a, b),
                                                              self.tensor(a, c)):
                bad.append(f"left distributivity fails {a},{b},{c}")
            if self.tensor(self.join2(a, b), c) != self.join2(self.tensor(a, c),
                                                              self.tensor(b, c)):
                bad.append(f"right distributivity fails {a},{b},{c}")
        return bad

    def is_commutative(self) -> bool:
        el = self.elements()
        return all(self.tensor(a, b) == self.tensor(b, a) for a, b in product(el, repeat=2))


class TableQuantale(Quantale):
    """Finite lattice-ordered monoid given by an order and a tensor function.

    It is a quantale only if ``axiom_failures()`` is empty; the class is also
    used deliberately for the non-distributive mutation M3.
    """

    finite = True

    def __init__(self, name: str, elements: Sequence, leq: Callable,
                 tensor: Callable, unit) -> None:
        self.name = name
        self._el = tuple(elements)
        self._leq = leq
        self._tensor = tensor
        self.unit = unit
        el = self._el
        bots = [a for a in el if all(leq(a, b) for b in el)]
        tops = [a for a in el if all(leq(b, a) for b in el)]
        if len(bots) != 1 or len(tops) != 1:
            raise QuantaleError("A finite lattice needs a least and greatest element")
        self.bottom, self.top = bots[0], tops[0]
        self.integral = unit == self.top
        self._j: dict = {}
        self._m: dict = {}
        self._t: dict = {}
        for a, b in product(el, repeat=2):
            ub = [c for c in el if leq(a, c) and leq(b, c)]
            least = [c for c in ub if all(leq(c, d) for d in ub)]
            lb = [c for c in el if leq(c, a) and leq(c, b)]
            great = [c for c in lb if all(leq(d, c) for d in lb)]
            if len(least) != 1 or len(great) != 1:
                raise QuantaleError(f"Not a lattice at {a},{b}")
            self._j[a, b], self._m[a, b] = least[0], great[0]
            t = tensor(a, b)
            if t not in el:
                raise QuantaleError("tensor leaves the carrier")
            self._t[a, b] = t

    def elements(self) -> tuple:
        return self._el

    def leq(self, a, b) -> bool:
        return self._leq(a, b)

    def join2(self, a, b):
        return self._j[a, b]

    def meet2(self, a, b):
        return self._m[a, b]

    def tensor(self, a, b):
        return self._t[a, b]


class PowersetMonoidQuantale(Quantale):
    """P(M) for a finite monoid M: union, pointwise product, unit {e}."""

    finite = True

    def __init__(self, name: str, monoid: Sequence, mult: Callable, e) -> None:
        self.name = name
        self.monoid = tuple(monoid)
        self.mult = mult
        self.e = e
        for a, b in product(self.monoid, repeat=2):
            if mult(a, b) not in self.monoid:
                raise QuantaleError("monoid product leaves the carrier")
        for a in self.monoid:
            if mult(e, a) != a or mult(a, e) != a:
                raise QuantaleError("monoid unit fails")
        for a, b, c in product(self.monoid, repeat=3):
            if mult(mult(a, b), c) != mult(a, mult(b, c)):
                raise QuantaleError("monoid not associative")
        self.bottom = frozenset()
        self.top = frozenset(self.monoid)
        self.unit = frozenset({e})
        self.integral = self.unit == self.top
        self._el = None

    def elements(self) -> tuple:
        if self._el is None:
            out = []
            for bits in product((False, True), repeat=len(self.monoid)):
                out.append(frozenset(m for m, b in zip(self.monoid, bits) if b))
            self._el = tuple(out)
        return self._el

    def leq(self, a, b) -> bool:
        return a <= b

    def join2(self, a, b):
        return a | b

    def meet2(self, a, b):
        return a & b

    def tensor(self, a, b):
        return frozenset(self.mult(x, y) for x in a for y in b)

    def ldiv(self, a, c):
        return frozenset(m for m in self.monoid if all(self.mult(x, m) in c for x in a))

    def rdiv(self, c, b):
        return frozenset(m for m in self.monoid if all(self.mult(m, y) in c for y in b))


class ViterbiQuantale(Quantale):
    """([0,1], <=, max, x, unit 1) over Fractions: best-path relevance."""

    name = "viterbi[0,1]"
    integral = True
    bottom, top, unit = Fraction(0), Fraction(1), Fraction(1)

    def leq(self, a, b): return a <= b
    def join2(self, a, b): return max(a, b)
    def meet2(self, a, b): return min(a, b)
    def tensor(self, a, b): return a * b

    def ldiv(self, a, c):
        return Fraction(1) if a <= c else c / a

    rdiv = lambda self, c, b: self.ldiv(b, c)  # commutative


class TropicalQuantale(Quantale):
    """Lawvere's ([0,inf], >=, inf, +, 0) over Fractions and math.inf.

    V-order is REVERSED numeric order: a <=_V b iff a >= b.  Join is numeric
    min, bottom is inf, top = unit = 0.
    """

    name = "tropical[0,inf]"
    integral = True
    bottom, top, unit = INF, Fraction(0), Fraction(0)

    def leq(self, a, b): return a >= b
    def join2(self, a, b): return min(a, b)
    def meet2(self, a, b): return max(a, b)

    def tensor(self, a, b):
        return INF if INF in (a, b) else a + b

    def ldiv(self, a, c):
        if a == INF:
            return Fraction(0)
        if c == INF:
            return INF
        return max(c - a, Fraction(0))

    rdiv = lambda self, c, b: self.ldiv(b, c)


def boolean() -> TableQuantale:
    return TableQuantale("Boolean", (False, True), lambda a, b: (not a) or b,
                         lambda a, b: a and b, True)


def truncated_tropical(c: int) -> TableQuantale:
    """{0,...,c,inf}, reversed order, a(x)b = a+b if a+b <= c else inf (budget c)."""
    el = tuple(range(c + 1)) + (INF,)
    return TableQuantale(f"tropical<= {c}", el, lambda a, b: a >= b,
                         lambda a, b: a + b if a + b <= c else INF, 0)


def saturating_tropical(c: int) -> TableQuantale:
    """{0,...,c,inf}, reversed order, a(x)b = min(a+b, c) (c reads ">= c"), inf absorbing.

    Unlike the budget version, a |-> (a < inf) is a STRICT homomorphism to Boolean."""
    el = tuple(range(c + 1)) + (INF,)
    return TableQuantale(f"saturating tropical {c}", el, lambda a, b: a >= b,
                         lambda a, b: INF if INF in (a, b) else min(a + b, c), 0)


def bottleneck_chain(n: int) -> TableQuantale:
    """{0,...,n-1} with max as join and min as tensor (a frame, unit n-1)."""
    return TableQuantale(f"maxmin chain {n}", tuple(range(n)), lambda a, b: a <= b,
                         min, n - 1)


def cyclic_monoid(k: int) -> PowersetMonoidQuantale:
    return PowersetMonoidQuantale(f"P(Z/{k})", tuple(range(k)),
                                  lambda a, b: (a + b) % k, 0)


def left_zero_monoid() -> PowersetMonoidQuantale:
    """P(M), M = {e, a, b}, xy = x for x, y in {a, b}: NONcommutative (ab=a, ba=b)."""
    def mult(x, y):
        if x == "e":
            return y
        return x
    return PowersetMonoidQuantale("P(left-zero{e,a,b})", ("e", "a", "b"), mult, "e")


OVERFLOW = "#"


def truncated_free_monoid(alphabet: str, max_len: int) -> PowersetMonoidQuantale:
    """P(Sigma^{<=L} + {#}): path languages, words longer than L collapse to #."""
    words = [""]
    layer = [""]
    for _ in range(max_len):
        layer = [w + s for w in layer for s in alphabet]
        words.extend(layer)
    words.append(OVERFLOW)

    def mult(u, v):
        if OVERFLOW in (u, v) or len(u) + len(v) > max_len:
            return OVERFLOW
        return u + v
    return PowersetMonoidQuantale(f"P({alphabet}*<= {max_len})", tuple(words), mult, "")


def m3_lattice_monoid() -> TableQuantale:
    """MUTATION: the diamond M3 with tensor = meet.  Associative, unital,
    monotone, but NOT a quantale (meet does not distribute over joins)."""
    el = ("0", "a", "b", "c", "1")

    def leq(x, y):
        return x == y or x == "0" or y == "1"

    def meet(x, y):
        if leq(x, y):
            return x
        if leq(y, x):
            return y
        return "0"
    return TableQuantale("M3 (meet) NOT a quantale", el, leq, meet, "1")


# ---------------------------------------------------------------------------
# V-relations, closures, predicates
# ---------------------------------------------------------------------------

Rel = tuple  # tuple of tuples


def identity(V: Quantale, n: int) -> Rel:
    return tuple(tuple(V.unit if i == j else V.bottom for j in range(n)) for i in range(n))


def compose(V: Quantale, R: Rel, S: Rel) -> Rel:
    n, mid, p = len(R), len(S), len(S[0]) if S else 0
    return tuple(tuple(V.join(V.tensor(R[i][j], S[j][k]) for j in range(mid))
                       for k in range(p)) for i in range(n))


def rel_join(V: Quantale, R: Rel, S: Rel) -> Rel:
    return tuple(tuple(V.join2(a, b) for a, b in zip(r, s)) for r, s in zip(R, S))


def rel_leq(V: Quantale, R: Rel, S: Rel) -> bool:
    return all(V.leq(a, b) for r, s in zip(R, S) for a, b in zip(r, s))


def closure(V: Quantale, R: Rel, max_iter: int = 10_000) -> Rel:
    """R* = V_n R^n, as the least fixed point of S = I v S;R (Kleene iteration)."""
    n = len(R)
    ident = identity(V, n)
    S = ident
    for _ in range(max_iter):
        T = rel_join(V, ident, compose(V, S, R))
        if T == S:
            return S
        S = T
    raise QuantaleError("closure did not stabilise")


def power(V: Quantale, R: Rel, k: int) -> Rel:
    S = identity(V, len(R))
    for _ in range(k):
        S = compose(V, S, R)
    return S


def path_sum_oracle(V: Quantale, R: Rel) -> Rel:
    """Independent oracle: join of path-ordered products over ALL finite paths.

    Finite V: breadth-first search over (state, accumulated value) pairs, so no
    distributivity is used.  Infinite but integral V: simple paths suffice.
    """
    n = len(R)
    out = []
    for x in range(n):
        row = [V.bottom] * n
        if V.finite:
            seen = {(x, V.unit)}
            queue = deque(seen)
            while queue:
                u, val = queue.popleft()
                row[u] = V.join2(row[u], val)
                for v in range(n):
                    if R[u][v] != V.bottom:
                        nxt = (v, V.tensor(val, R[u][v]))
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
        else:
            if not V.integral:
                raise QuantaleError("simple-path oracle needs an integral quantale")
            stack = [(x, V.unit, frozenset({x}))]
            while stack:
                u, val, used = stack.pop()
                row[u] = V.join2(row[u], val)
                for v in range(n):
                    if v not in used and R[u][v] != V.bottom:
                        stack.append((v, V.tensor(val, R[u][v]), used | {v}))
        out.append(tuple(row))
    return tuple(out)


def is_closed(V: Quantale, R: Rel, phi: Sequence) -> bool:
    n = len(R)
    return all(V.leq(V.tensor(phi[u], R[u][v]), phi[v])
               for u in range(n) for v in range(n))


def is_closed_wrong_side(V: Quantale, R: Rel, phi: Sequence) -> bool:
    """MUTATION: R(u,v) (x) phi(u) <= phi(v).  Characterises the REVERSED closure."""
    n = len(R)
    return all(V.leq(V.tensor(R[u][v], phi[u]), phi[v])
               for u in range(n) for v in range(n))


def all_predicates(V: Quantale, n: int):
    return product(V.elements(), repeat=n)


def closed_predicates(V: Quantale, R: Rel) -> list[tuple]:
    return [phi for phi in all_predicates(V, len(R)) if is_closed(V, R, phi)]


def predicate_closure(V: Quantale, Rs: Rel, phi: Sequence) -> tuple:
    """Cl(phi)(v) = V_u phi(u) (x) R*(u,v): least closed predicate above phi."""
    n = len(Rs)
    return tuple(V.join(V.tensor(phi[u], Rs[u][v]) for u in range(n)) for v in range(n))


def predicate_interior(V: Quantale, Rs: Rel, phi: Sequence) -> tuple:
    """Int(phi)(u) = /\\_v phi(v)/R*(u,v): greatest closed predicate below phi."""
    n = len(Rs)
    return tuple(V.meet(V.rdiv(phi[v], Rs[u][v]) for v in range(n)) for u in range(n))


def hereditary_meet(V: Quantale, R: Rel, x: int, z: int, predicates=None):
    """CG-1(a): /\\{phi(z) : phi R-closed, k <= phi(x)} (finite enumeration)."""
    preds = closed_predicates(V, R) if predicates is None else predicates
    return V.meet(phi[z] for phi in preds if V.leq(V.unit, phi[x]))


def residuated_meet(V: Quantale, R: Rel, x: int, z: int, predicates=None):
    """CG-1(a'): /\\{phi(x)\\phi(z) : phi R-closed}."""
    preds = closed_predicates(V, R) if predicates is None else predicates
    return V.meet(V.ldiv(phi[x], phi[z]) for phi in preds)


# ---------------------------------------------------------------------------
# Observation quotients
# ---------------------------------------------------------------------------

def fibres(q: Sequence[int], m: int) -> tuple:
    return tuple(tuple(u for u in range(len(q)) if q[u] == a) for a in range(m))


def exists_quotient(V: Quantale, R: Rel, q: Sequence[int], m: int) -> Rel:
    """May-quotient Q(a,b) = V{R(u,v) : q(u)=a, q(v)=b}."""
    F = fibres(q, m)
    return tuple(tuple(V.join(R[u][v] for u in F[a] for v in F[b]) for b in range(m))
                 for a in range(m))


def forall_quotient(V: Quantale, R: Rel, q: Sequence[int], m: int) -> Rel:
    """Must-quotient Q_A(a,b) = /\\_{q(u)=a} V_{q(v)=b} R(u,v)  (forall-exists)."""
    F = fibres(q, m)
    return tuple(tuple(V.meet(V.join(R[u][v] for v in F[b]) for u in F[a])
                       for b in range(m)) for a in range(m))


def backward_must_quotient(V: Quantale, R: Rel, q: Sequence[int], m: int) -> Rel:
    """Backward must: /\\_{q(v)=b} V_{q(u)=a} R(u,v): every target rep has a witness."""
    F = fibres(q, m)
    return tuple(tuple(V.meet(V.join(R[u][v] for u in F[a]) for v in F[b])
                       for b in range(m)) for a in range(m))


def push(V: Quantale, phi: Sequence, q: Sequence[int], m: int) -> tuple:
    """q_! phi(b) = V_{q(u)=b} phi(u)."""
    return tuple(V.join(phi[u] for u in range(len(q)) if q[u] == b) for b in range(m))


def push_forall(V: Quantale, phi: Sequence, q: Sequence[int], m: int) -> tuple:
    """q_* phi(b) = /\\_{q(u)=b} phi(u)."""
    return tuple(V.meet(phi[u] for u in range(len(q)) if q[u] == b) for b in range(m))


def pull(psi: Sequence, q: Sequence[int]) -> tuple:
    """q^* psi = psi o q."""
    return tuple(psi[a] for a in q)


def source_profile(V: Quantale, Rs: Rel, q: Sequence[int], m: int, x: int) -> tuple:
    """rho^_x(b) = V_{q(z)=b} R*(x,z): the true source value from x to report b."""
    return push(V, Rs[x], q, m)


def image(q: Sequence[int]) -> set:
    return set(q)


@dataclass(frozen=True)
class QuotientLab:
    """All derived objects for one finite model (V, R, q, m)."""

    V: Quantale
    R: Rel
    q: tuple
    m: int

    @property
    def n(self) -> int:
        return len(self.R)

    def __post_init__(self) -> None:
        n = len(self.R)
        if any(len(r) != n for r in self.R) or len(self.q) != n:
            raise QuantaleError("square relation and one report per state required")
        if any(type(a) is not int or not 0 <= a < self.m for a in self.q):
            raise QuantaleError("reports must lie in range(m)")
        object.__setattr__(self, "Rs", closure(self.V, self.R))
        Q = exists_quotient(self.V, self.R, self.q, self.m)
        object.__setattr__(self, "Q", Q)
        object.__setattr__(self, "Qs", closure(self.V, Q))
        QA = forall_quotient(self.V, self.R, self.q, self.m)
        object.__setattr__(self, "QA", QA)
        object.__setattr__(self, "QAs", closure(self.V, QA))
        object.__setattr__(self, "profiles", tuple(
            source_profile(self.V, self.Rs, self.q, self.m, x) for x in range(n)))

    # -- CG-3: exactness, four conditions -------------------------------------
    def selected_exact(self, x: int) -> bool:
        return self.profiles[x] == self.Qs[self.q[x]]

    def cond1_all_start(self) -> bool:
        return all(self.selected_exact(x) for x in range(self.n))

    def cond2_fibre_constant(self) -> bool:
        return all(self.profiles[x] == self.profiles[y] for x in range(self.n)
                   for y in range(self.n) if self.q[x] == self.q[y])

    def cond3_push_preserves_closed(self, predicates=None) -> bool:
        preds = closed_predicates(self.V, self.R) if predicates is None else predicates
        return all(is_closed(self.V, self.Q, push(self.V, phi, self.q, self.m))
                   for phi in preds)

    def cond4_saturation_preserves_closed(self, predicates=None) -> bool:
        preds = closed_predicates(self.V, self.R) if predicates is None else predicates
        return all(is_closed(self.V, self.R, pull(push(self.V, phi, self.q, self.m), self.q))
                   for phi in preds)

    def selected_criterion(self, x: int) -> bool:
        """CG-4: exact at x iff q_! rho_x is Q-closed iff its saturation is R-closed."""
        return is_closed(self.V, self.Q, self.profiles[x])

    def selected_saturation_criterion(self, x: int) -> bool:
        return is_closed(self.V, self.R, pull(self.profiles[x], self.q))

    # -- CG-6/7: may/must sandwich and must-profile ---------------------------
    def sandwich(self, x: int) -> tuple:
        a = self.q[x]
        return self.QAs[a], self.profiles[x], self.Qs[a]

    def must_profile(self) -> Rel:
        """M(a,b) = /\\_{q(x)=a} rho^_x(b): optimal representative-uniform bound."""
        F = fibres(self.q, self.m)
        return tuple(tuple(self.V.meet(self.profiles[x][b] for x in F[a])
                           for b in range(self.m)) for a in range(self.m))

    def may_profile(self) -> Rel:
        """S(a,b) = V_{q(x)=a} rho^_x(b) = (q_! R*)(a,b)."""
        F = fibres(self.q, self.m)
        return tuple(tuple(self.V.join(self.profiles[x][b] for x in F[a])
                           for b in range(self.m)) for a in range(self.m))

    def may_equals_must_on_image(self) -> bool:
        return all(self.QAs[a] == self.Qs[a] for a in image(self.q))

    def lumpable(self) -> bool:
        """One-step: q_! R(x,.) constant on fibres (V-analogue of Kemeny-Snell)."""
        rows = [push(self.V, self.R[x], self.q, self.m) for x in range(self.n)]
        return all(rows[x] == rows[y] for x in range(self.n) for y in range(self.n)
                   if self.q[x] == self.q[y])

    def unpointed_exact(self) -> bool:
        """Q* = q_!R* on the image: the whole fibre-to-fibre distance commutes."""
        S = self.may_profile()
        im = image(self.q)
        return all(self.Qs[a][b] == S[a][b] for a in im for b in im)

    def fully_faithful(self) -> bool:
        """R*(x,z) = Q*(qx,qz) for all source states."""
        return all(self.Rs[x][z] == self.Qs[self.q[x]][self.q[z]]
                   for x in range(self.n) for z in range(self.n))

    def kernel_within_isomorphism(self) -> bool:
        V, Rs = self.V, self.Rs
        return all(V.leq(V.unit, Rs[x][y]) for x in range(self.n) for y in range(self.n)
                   if self.q[x] == self.q[y])

    # -- CG-8: adjunctions, Beck-Chevalley ------------------------------------
    def left_adjoint(self, phi: Sequence) -> tuple:
        """L = Cl_Q o q_! : Cl(R) -> Cl(Q)."""
        return predicate_closure(self.V, self.Qs, push(self.V, phi, self.q, self.m))

    def right_adjoint(self, phi: Sequence) -> tuple:
        """Int_Q o q_* : Cl(R) -> Cl(Q)."""
        return predicate_interior(self.V, self.Qs, push_forall(self.V, phi, self.q, self.m))

    def left_bc(self, predicates=None) -> bool:
        preds = closed_predicates(self.V, self.R) if predicates is None else predicates
        return all(self.left_adjoint(phi) == push(self.V, phi, self.q, self.m)
                   for phi in preds)

    def right_bc(self, predicates=None) -> bool:
        preds = closed_predicates(self.V, self.R) if predicates is None else predicates
        return all(self.right_adjoint(phi) == push_forall(self.V, phi, self.q, self.m)
                   for phi in preds)

    def backward_exact(self) -> bool:
        """For all a in Y, z in X: Q*(a, qz) = V_{q(x)=a} R*(x,z)."""
        F = fibres(self.q, self.m)
        return all(self.Qs[a][self.q[z]] == self.V.join(self.Rs[x][z] for x in F[a])
                   for a in range(self.m) for z in range(self.n))

    def backward_coverage(self) -> bool:
        """Q(a,b) <= /\\_{q(v)=b} V_{q(u)=a} R*(u,v)."""
        B = backward_must_quotient(self.V, self.Rs, self.q, self.m)
        return rel_leq(self.V, self.Q, B)

    # -- CG-9: ghost defect ----------------------------------------------------
    def ghost_defect(self, phi: Sequence) -> tuple:
        """(q_! phi, L phi, D) with D(b) = L phi(b) \\ q_! phi(b); zero iff k <= D(b) all b."""
        pushed = push(self.V, phi, self.q, self.m)
        lifted = predicate_closure(self.V, self.Qs, pushed)
        return pushed, lifted, tuple(self.V.ldiv(l, p) for l, p in zip(lifted, pushed))

    def defect_is_zero(self, phi: Sequence) -> bool:
        return all(self.V.leq(self.V.unit, d) for d in self.ghost_defect(phi)[2])

    def global_defect(self):
        """G = /\\_{x,b} Q*(qx,b) \\ rho^_x(b); exact iff k <= G.  Tropical: the worst
        shortcut max_{x,b}(d_src - d_Q); Boolean: True iff no ghost anywhere."""
        return self.V.meet(self.V.ldiv(self.Qs[self.q[x]][b], self.profiles[x][b])
                           for x in range(self.n) for b in range(self.m))

    def support_reachable(self, x: int) -> set:
        seen, stack = {x}, [x]
        while stack:
            u = stack.pop()
            for v in range(self.n):
                if self.R[u][v] != self.V.bottom and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen

    def ghost_reports(self, x: int) -> tuple:
        """Reports b at which the quotient over-claims from the selected start x."""
        return tuple(b for b, d in enumerate(self.ghost_defect(self.Rs[x])[2])
                     if not self.V.leq(self.V.unit, d))


def model(V: Quantale, R: Rel, q: Sequence[int], m: int | None = None) -> QuotientLab:
    q = tuple(q)
    return QuotientLab(V, tuple(tuple(r) for r in R), q, (max(q) + 1) if m is None else m)


# ---------------------------------------------------------------------------
# CG-10: partitions and the coarsest exact refinement
# ---------------------------------------------------------------------------

def restricted_growth(n: int):
    """All set partitions of range(n) as restricted-growth label tuples."""
    for labels in product(range(n), repeat=n):
        if n == 0 or (labels[0] == 0 and all(labels[i] <= 1 + max(labels[:i])
                                             for i in range(1, n))):
            yield labels


def normalise(labels: Sequence[int]) -> tuple:
    seen: dict = {}
    return tuple(seen.setdefault(a, len(seen)) for a in labels)


def refines(p: Sequence[int], r: Sequence[int]) -> bool:
    """p finer than (or equal to) r."""
    n = len(p)
    return all(r[i] == r[j] for i in range(n) for j in range(n) if p[i] == p[j])


def partition_join(p: Sequence[int], r: Sequence[int]) -> tuple:
    n = len(p)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(n):
        for j in range(n):
            if p[i] == p[j] or r[i] == r[j]:
                parent[find(i)] = find(j)
    return normalise([find(i) for i in range(n)])


def partition_meet(p: Sequence[int], r: Sequence[int]) -> tuple:
    return normalise(list(zip(p, r)))


def is_exact_partition(V: Quantale, Rs: Rel, labels: Sequence[int]) -> bool:
    """CG-3 condition (2) for the partition `labels`, from a precomputed R*."""
    lab = normalise(labels)
    m = max(lab) + 1
    prof = [push(V, Rs[x], lab, m) for x in range(len(lab))]
    return all(prof[x] == prof[y] for x in range(len(lab)) for y in range(len(lab))
               if lab[x] == lab[y])


def coarsest_exact_refinement(V: Quantale, R: Rel, q: Sequence[int]) -> tuple:
    """Partition refinement: split blocks by V-profiles until stable (CG-10)."""
    Rs = closure(V, R)
    cur = normalise(q)
    while True:
        m = max(cur) + 1
        keys = [(cur[x], push(V, Rs[x], cur, m)) for x in range(len(cur))]
        nxt = normalise(keys)
        if nxt == cur:
            return cur
        cur = nxt


# ---------------------------------------------------------------------------
# CG-11: weighted ghost certificate (generalises PAP-05)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class WeightedGhost:
    start: int
    report_path: tuple
    path_weight: Hashable
    invariant: tuple
    bound: Hashable


def check_weighted_ghost(V: Quantale, R: Rel, q: Sequence[int], m: int, start: int,
                         report_path: Sequence[int], invariant: Sequence) -> WeightedGhost:
    """Verify a quotient path (weight w) and an R-closed phi with k <= phi(start)
    such that w is NOT <= q_!phi(end).  Then Q*(q start, end) exceeds the true source
    value from `start` (by CG-1(a)).  No search is trusted; every premise is checked."""
    Q = exists_quotient(V, R, q, m)
    path = tuple(report_path)
    if not path or path[0] != q[start]:
        raise QuantaleError("quotient path must start at the selected observation")
    w = V.unit
    for a, b in zip(path, path[1:]):
        w = V.tensor(w, Q[a][b])
    phi = tuple(invariant)
    if not is_closed(V, R, phi):
        raise QuantaleError("invariant is not R-closed")
    if not V.leq(V.unit, phi[start]):
        raise QuantaleError("invariant does not contain the selected start")
    bound = push(V, phi, q, m)[path[-1]]
    if V.leq(w, bound):
        raise QuantaleError("path weight is within the invariant bound: no ghost certified")
    return WeightedGhost(start, path, w, phi, bound)


# ---------------------------------------------------------------------------
# CG-5: change of base
# ---------------------------------------------------------------------------

def base_change(h: Callable, R: Rel) -> Rel:
    return tuple(tuple(h(v) for v in r) for r in R)


def hom_failures(V: Quantale, W: Quantale, h: Callable) -> dict:
    """Which morphism laws h: V -> W satisfies, by exhaustive check on finite V."""
    el = V.elements()
    joins = all(h(V.join2(a, b)) == W.join2(h(a), h(b)) for a, b in product(el, repeat=2)) \
        and h(V.bottom) == W.bottom
    strict_t = all(h(V.tensor(a, b)) == W.tensor(h(a), h(b)) for a, b in product(el, repeat=2))
    lax_t = all(W.leq(W.tensor(h(a), h(b)), h(V.tensor(a, b))) for a, b in product(el, repeat=2))
    oplax_t = all(W.leq(h(V.tensor(a, b)), W.tensor(h(a), h(b)))
                  for a, b in product(el, repeat=2))
    return {
        "joins": joins,
        "strict": joins and strict_t and h(V.unit) == W.unit,
        "lax": joins and lax_t and W.leq(W.unit, h(V.unit)),
        "oplax": joins and oplax_t and W.leq(h(V.unit), W.unit),
    }


def min_length_hom(max_len: int) -> Callable:
    """P(Sigma^{<=L} + #) -> saturating tropical L+1: L |-> min length, # |-> L+1
    (meaning ">= L+1"), empty language |-> inf.  A strict quantale homomorphism."""
    def h(lang):
        if not lang:
            return INF
        return min(max_len + 1 if w == OVERFLOW else len(w) for w in lang)
    return h


def finite_support_hom(a) -> bool:
    """tropical -> Boolean: a |-> (a < inf)."""
    return a != INF


# ---------------------------------------------------------------------------
# CG-12: signed weights (not a quantale)
# ---------------------------------------------------------------------------

def mat_mul(A, B):
    n, k, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum((A[i][j] * B[j][l] for j in range(k)), Fraction(0))
                       for l in range(p)) for i in range(n))


def mat_pow(A, t: int):
    n = len(A)
    P = tuple(tuple(Fraction(int(i == j)) for j in range(n)) for i in range(n))
    for _ in range(t):
        P = mat_mul(A, P)
    return P


def mat_inv(A):
    """Exact Gauss-Jordan inverse over Fractions; None if singular."""
    n = len(A)
    M = [[Fraction(v) for v in row] + [Fraction(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return tuple(tuple(row[n:]) for row in M)


def resolvent(A):
    """(I - A)^{-1}, the signed analogue of the closure sum_t A^t; None if singular."""
    n = len(A)
    return mat_inv(tuple(tuple(Fraction(int(i == j)) - A[i][j] for j in range(n))
                         for i in range(n)))


def supp(a) -> bool:
    return a != 0


def structural_walks(A, t: int) -> tuple:
    """Boolean: W[y][x] = exists a length-t walk x -> y in the support graph.
    Column convention: A[y][x] is the weight of the edge x -> y."""
    n = len(A)
    B = boolean()
    S = tuple(tuple(supp(A[y][x]) for x in range(n)) for y in range(n))
    P = identity(B, n)
    for _ in range(t):
        P = tuple(tuple(any(S[y][w] and P[w][x] for w in range(n)) for x in range(n))
                  for y in range(n))
    return P


def aggregated_response(A, q: Sequence[int], m: int, x: int, t: int) -> tuple:
    """sum_{q(z)=b} (A^t)[z][x]: the fibre-aggregated net response from source x."""
    P = mat_pow(A, t)
    return tuple(sum((P[z][x] for z in range(len(q)) if q[z] == b), Fraction(0))
                 for b in range(m))


def fibre_sum_quotient(A, q: Sequence[int], m: int):
    """Signed analogue of the may-quotient: Qhat[b][a] = sum over fibre pairs."""
    n = len(q)
    return tuple(tuple(sum((A[z][u] for u in range(n) for z in range(n)
                            if q[u] == a and q[z] == b), Fraction(0))
                       for a in range(m)) for b in range(m))


def mean_quotient(A, q: Sequence[int], m: int):
    """Abar[b][a] = (1/|a|) sum_{q(x)=a} sum_{q(z)=b} A[z][x]; equals the lumped
    matrix when A is lumpable.  The signed stand-in for the idempotent join."""
    n = len(q)
    size = [sum(1 for x in range(n) if q[x] == a) for a in range(m)]
    return tuple(tuple(sum((A[z][x] for x in range(n) for z in range(n)
                            if q[x] == a and q[z] == b), Fraction(0)) / size[a]
                       if size[a] else Fraction(0) for a in range(m)) for b in range(m))


def signed_lumpable(A, q: Sequence[int], m: int) -> bool:
    """Kemeny-Snell: sum_{q(z)=b} A[z][x] depends only on q(x) (V^T A = Ahat V^T)."""
    n = len(q)
    cols = [tuple(sum((A[z][x] for z in range(n) if q[z] == b), Fraction(0))
                  for b in range(m)) for x in range(n)]
    return all(cols[x] == cols[y] for x in range(n) for y in range(n) if q[x] == q[y])


def lumped_matrix(A, q: Sequence[int], m: int):
    """Ahat[b][a] = sum_{q(z)=b} A[z][x] for a representative x of a (needs lumpable)."""
    if not signed_lumpable(A, q, m):
        raise QuantaleError("not lumpable: the lumped matrix depends on the representative")
    n = len(q)
    reps = {}
    for x in range(n):
        reps.setdefault(q[x], x)
    return tuple(tuple(sum((A[z][reps[a]] for z in range(n) if q[z] == b), Fraction(0))
                       if a in reps else Fraction(0) for a in range(m)) for b in range(m))


def walk_polynomial(edges: Sequence[tuple], x: int, y: int, t: int) -> dict:
    """(A^t)[y][x] as a polynomial in one indeterminate per support edge.

    Returns {sorted monomial (tuple of edges with repetition): positive int}.
    Coefficients are nonnegative integers (walk counts per monomial)."""
    poly: dict = {((), x): 1}
    for _ in range(t):
        nxt: dict = {}
        for (mono, end), c in poly.items():
            for e in edges:
                if e[0] == end:
                    key = (tuple(sorted(mono + (e,))), e[1])
                    nxt[key] = nxt.get(key, 0) + c
        poly = nxt
    out: dict = {}
    for (mono, end), c in poly.items():
        if end == y:
            out[mono] = out.get(mono, 0) + c
    return out


def evaluate_polynomial(poly: dict, weights: dict) -> Fraction:
    total = Fraction(0)
    for mono, c in poly.items():
        term = Fraction(c)
        for e in mono:
            term *= weights[e]
        total += term
    return total
