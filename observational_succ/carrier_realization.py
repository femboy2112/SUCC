"""Positive carrier realization: linear predictive dimension vs lawful carriers.

Exact-rational theory of the boundary between a linear predictive
representation of a source-indexed controlled behavior and its realization
by a finite POSITIVE, LAWFUL carrier (nonnegative joint event kernels,
total/partial action availability, declared preparations).

Objects (all exact ``fractions.Fraction``; floats are rejected):

* ``PositiveCarrier``: finite carrier C, actions a with outcome alphabets
  Z_a, event matrices M[a][z] in Q_{>=0}^{C x C} with column convention
  M[a][z][c'][c] = P(outcome z, next c' | current c, action a), enabled sets
  E_a subset C (availability), and preparations pi_sigma in Delta(C).
  Mass law for every action: sum_z 1^T M[a][z] = 1^T on E_a.  States outside
  E_a are completed by the refusal outcome ``BOT`` (``'_|_'``) which keeps the
  state and emits mass 1: the "bottom completion".  A word is LEGAL at a
  source iff every action in it is enabled on the whole support of the
  current unnormalized law when it is applied.  Executing an action that is
  not uniformly available is not an observation; it is illegal.

* ``word probability`` p_sigma(w) = 1^T M_w pi_sigma with
  M_w = M[a_n][z_n] ... M[a_1][z_1] (first event acts first, rightmost).
  This is the JOINT unnormalized probability of the actual receipt history,
  not a posterior.

* ``LinearRealization``: minimal (reachable and observable) exact linear
  realization (V, T[a][z], v_sigma, tau) of the complete source-indexed
  behavior, computed by exact forward closure and observability quotient.
  dim V = rank of the full source-indexed Hankel matrix (finite proof via
  the realization; the finite Hankel blocks give matching lower bounds).

* Obstruction certificates for a proposed positive carrier dimension m:
  - nonnegative-rank lower bounds on finite Hankel blocks (fooling sets);
  - the peripheral-spectrum obstruction: in any finite positive realization
    the peripheral eigenvalues of every reachable event-word operator are
    rho times roots of unity (Frobenius); a rational irrational-angle
    rotation is a finite certificate of d+ = infinity;
  - a failed availability square (legality pattern not representable).

* Positive side: an exact LP verifier that turns a normalized, invariant,
  finitely generated cone into explicit stochastic event matrices B[a][z]
  (the cone theorem), and an exact equivalence certificate between two
  carriers (difference-realization reachable-space closure).

Everything here is MATHEMATICAL data about declared models.  Nothing
authenticates a physical preparation, reset, or sensor.
"""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass, field
from fractions import Fraction as Q
from typing import Hashable, Iterable, Sequence

from .carrier_indexed import CarrierError, rat

BOT = "_|_"

Vec = tuple[Q, ...]
Mat = tuple[tuple[Q, ...], ...]
Word = tuple[tuple[str, Hashable], ...]


class RealizationError(CarrierError):
    """A positive-carrier, cone, or certificate gate failed."""


# --------------------------------------------------------------------------
# exact linear algebra
# --------------------------------------------------------------------------

def vec(xs: Iterable) -> Vec:
    return tuple(rat(x) for x in xs)


def mat(rows: Iterable[Iterable]) -> Mat:
    out = tuple(vec(r) for r in rows)
    if out and any(len(r) != len(out[0]) for r in out):
        raise RealizationError("Ragged matrix")
    return out


def zeros(n: int, m: int) -> Mat:
    return tuple(tuple(Q(0) for _ in range(m)) for _ in range(n))


def identity(n: int) -> Mat:
    return tuple(tuple(Q(int(i == j)) for j in range(n)) for i in range(n))


def matmul(a: Mat, b: Mat) -> Mat:
    if not a or not b:
        return ()
    if len(a[0]) != len(b):
        raise RealizationError("Matrix shape mismatch")
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), Q(0)) for col in bt)
                 for row in a)


def matvec(a: Mat, v: Vec) -> Vec:
    if not a:
        return ()
    if len(a[0]) != len(v):
        raise RealizationError("Matrix/vector shape mismatch")
    return tuple(sum((x * y for x, y in zip(row, v)), Q(0)) for row in a)


def vecmat(v: Vec, a: Mat) -> Vec:
    if len(v) != len(a):
        raise RealizationError("Vector/matrix shape mismatch")
    return tuple(sum((v[i] * a[i][j] for i in range(len(v))), Q(0))
                 for j in range(len(a[0]) if a else 0))


def transpose(a: Mat) -> Mat:
    return tuple(zip(*a)) if a else ()


def kron(a: Mat, b: Mat) -> Mat:
    return tuple(tuple(x * y for x in ra for y in rb) for ra in a for rb in b)


def madd(a: Mat, b: Mat) -> Mat:
    return tuple(tuple(x + y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def mscale(c: Q, a: Mat) -> Mat:
    return tuple(tuple(c * x for x in r) for r in a)


def dot(u: Vec, v: Vec) -> Q:
    return sum((x * y for x, y in zip(u, v)), Q(0))


def rref(a: Mat) -> tuple[Mat, tuple[int, ...]]:
    """Exact reduced row echelon form and pivot columns."""
    rows = [list(r) for r in a]
    if not rows:
        return (), ()
    ncol = len(rows[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncol):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = 1 / rows[r][c]
        rows[r] = [x * inv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return tuple(tuple(x) for x in rows), tuple(pivots)


def rank(a: Mat) -> int:
    return len(rref(a)[1])


def nullspace(a: Mat, ncol: int | None = None) -> tuple[Vec, ...]:
    """Exact basis of {x : a x = 0}."""
    if not a:
        n = ncol or 0
        return tuple(tuple(Q(int(i == j)) for j in range(n)) for i in range(n))
    n = len(a[0])
    red, piv = rref(a)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        x = [Q(0)] * n
        x[f] = Q(1)
        for i, c in enumerate(piv):
            x[c] = -red[i][f]
        basis.append(tuple(x))
    return tuple(basis)


def solve_in_span(basis: Sequence[Vec], x: Vec) -> Vec | None:
    """Coordinates of x in the span of ``basis`` (exact), or None."""
    if not basis:
        return () if all(t == 0 for t in x) else None
    n = len(x)
    aug = tuple(tuple(basis[j][i] for j in range(len(basis))) + (x[i],)
                for i in range(n))
    red, piv = rref(aug)
    if len(basis) in piv:
        return None
    coords = [Q(0)] * len(basis)
    for i, c in enumerate(piv):
        coords[c] = red[i][len(basis)]
    return tuple(coords)


def charpoly(a: Mat) -> tuple[Q, ...]:
    """Exact characteristic polynomial coefficients (Faddeev-LeVerrier),
    highest degree first: det(xI - A)."""
    n = len(a)
    if n == 0:
        return (Q(1),)
    coeffs = [Q(1)]
    m = zeros(n, n)
    ident = identity(n)
    for k in range(1, n + 1):
        m = matmul(a, madd(m, mscale(coeffs[-1], ident)))
        c = -sum((m[i][i] for i in range(n)), Q(0)) / k
        coeffs.append(c)
    return tuple(coeffs)


# --------------------------------------------------------------------------
# positive carriers
# --------------------------------------------------------------------------

def _check_event_block(M: dict[Hashable, Mat], n: int, enabled: tuple[bool, ...],
                       action: str) -> None:
    if not M:
        raise RealizationError(f"Action {action!r} needs at least one outcome")
    for z, block in M.items():
        if len(block) != n or any(len(r) != n for r in block):
            raise RealizationError(f"Event matrix {action!r}/{z!r} is not {n}x{n}")
        if any(x < 0 for r in block for x in r):
            raise RealizationError(f"Negative event entry in {action!r}/{z!r}")
    for c in range(n):
        column_mass = sum((M[z][cp][c] for z in M for cp in range(n)), Q(0))
        if enabled[c]:
            if column_mass != 1:
                raise RealizationError(
                    f"Action {action!r} is not mass preserving on enabled state {c}")
        elif column_mass != 0:
            raise RealizationError(
                f"Action {action!r} has mass on disabled state {c}; "
                "availability is declared by the enabled set, not by a sensor")


@dataclass(frozen=True)
class PositiveCarrier:
    """A finite positive lawful carrier with declared preparations.

    ``events[a][z]`` are nonnegative rational matrices with the column
    convention events[a][z][next][current].  ``enabled[a]`` is the
    availability tuple.  On disabled states every outcome column must be
    zero; the bottom completion (``BOT``) supplies the refusal mass.
    ``preparations[sigma]`` are probability vectors on C.
    """
    states: tuple[Hashable, ...]
    events: dict[str, dict[Hashable, Mat]]
    preparations: dict[Hashable, Vec]
    enabled: dict[str, tuple[bool, ...]] = field(default_factory=dict)

    def __post_init__(self):
        n = len(self.states)
        if n == 0 or len(set(self.states)) != n:
            raise RealizationError("Distinct nonempty carrier states required")
        events = {}
        enabled = {}
        for a, blocks in self.events.items():
            if type(a) is not str or not a:
                raise RealizationError("Action names are nonempty strings")
            en = tuple(self.enabled.get(a, (True,) * n))
            if len(en) != n or any(type(b) is not bool for b in en):
                raise RealizationError("Enabled tuple must be one bool per state")
            blk = {z: mat(b) for z, b in blocks.items()}
            if BOT in blk and not all(en):
                raise RealizationError("A declared BOT outcome requires a total action "
                                       "(BOT is the bottom completion, not a sensor)")
            _check_event_block(blk, n, en, a)
            events[a] = blk
            enabled[a] = en
        preps = {}
        for s, p in self.preparations.items():
            v = vec(p)
            if len(v) != n or any(x < 0 for x in v) or sum(v, Q(0)) != 1:
                raise RealizationError(f"Preparation {s!r} is not a probability vector")
            preps[s] = v
        if not preps:
            raise RealizationError("At least one declared preparation required")
        object.__setattr__(self, "events", events)
        object.__setattr__(self, "enabled", enabled)
        object.__setattr__(self, "preparations", preps)

    @property
    def dimension(self) -> int:
        return len(self.states)

    @property
    def actions(self) -> tuple[str, ...]:
        return tuple(self.events)

    def outcomes(self, a: str) -> tuple[Hashable, ...]:
        return tuple(self.events[a])

    def is_total(self, a: str) -> bool:
        return all(self.enabled[a])

    def event(self, a: str, z: Hashable) -> Mat:
        """Event matrix including the bottom completion."""
        if z == BOT and BOT not in self.events[a]:
            n = self.dimension
            return tuple(tuple(Q(int(i == j and not self.enabled[a][j]))
                               for j in range(n)) for i in range(n))
        try:
            return self.events[a][z]
        except KeyError as exc:
            raise RealizationError(f"Unknown event {a!r}/{z!r}") from exc

    def completed_outcomes(self, a: str) -> tuple[Hashable, ...]:
        zs = self.outcomes(a)
        return zs if (self.is_total(a) or BOT in zs) else zs + (BOT,)

    def word_matrix(self, word: Word) -> Mat:
        m = identity(self.dimension)
        for a, z in word:
            m = matmul(self.event(a, z), m)
        return m

    def law(self, source: Hashable, word: Word) -> Vec:
        """Unnormalized current law M_w pi_sigma (the source-indexed J_h row)."""
        return matvec(self.word_matrix(word), self.preparations[source])

    def probability(self, source: Hashable, word: Word) -> Q:
        return sum(self.law(source, word), Q(0))

    def legal(self, source: Hashable, word: Word) -> bool:
        """Every action is uniformly available on the support when applied."""
        v = self.preparations[source]
        for a, z in word:
            if a not in self.events:
                raise RealizationError(f"Unknown action {a!r}")
            if z == BOT:
                return False
            if any(v[c] > 0 and not self.enabled[a][c] for c in range(len(v))):
                return False
            v = matvec(self.events[a][z], v)
            if all(x == 0 for x in v):
                return True  # zero-probability continuation; nothing to apply
        return True

    def available(self, source: Hashable, word: Word, a: str) -> bool:
        if not self.legal(source, word):
            return False
        v = self.law(source, word)
        return all(not (v[c] > 0 and not self.enabled[a][c]) for c in range(len(v)))

    def bottom_completion(self) -> "PositiveCarrier":
        """The total carrier in which refusal is the observable outcome BOT.
        This is a representation change, not a new sensor: BOT has
        probability zero exactly on legal (source, history, action) triples."""
        events = {}
        for a in self.actions:
            blk = dict(self.events[a])
            if not self.is_total(a):
                blk[BOT] = self.event(a, BOT)
            events[a] = blk
        return PositiveCarrier(self.states, events, dict(self.preparations), {})

    def tensor(self, other: "PositiveCarrier") -> "PositiveCarrier":
        """Independent product (both components act on every action).
        Outcomes are pairs; sources are pairs; enabled = conjunction."""
        if set(self.actions) != set(other.actions):
            raise RealizationError("Tensor factors must share the action alphabet")
        states = tuple((s, t) for s in self.states for t in other.states)
        events = {}
        enabled = {}
        for a in self.actions:
            events[a] = {(z1, z2): kron(self.events[a][z1], other.events[a][z2])
                         for z1 in self.outcomes(a) for z2 in other.outcomes(a)}
            enabled[a] = tuple(e1 and e2 for e1 in self.enabled[a] for e2 in other.enabled[a])
        preps = {(s1, s2): tuple(x * y for x in p1 for y in p2)
                 for s1, p1 in self.preparations.items()
                 for s2, p2 in other.preparations.items()}
        return PositiveCarrier(states, events, preps, enabled)


def words_up_to(carrier: PositiveCarrier, length: int, *, completed: bool = True
                ) -> list[Word]:
    """All action/outcome words of length <= ``length`` (bottom included)."""
    letters = [(a, z) for a in carrier.actions
               for z in (carrier.completed_outcomes(a) if completed else carrier.outcomes(a))]
    out: list[Word] = [()]
    frontier: list[Word] = [()]
    for _ in range(length):
        frontier = [w + (l,) for w in frontier for l in letters]
        out.extend(frontier)
    return out


# --------------------------------------------------------------------------
# minimal linear realization of the complete source-indexed behavior
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class LinearRealization:
    """Minimal exact linear realization (V, T, v_sigma, tau).

    Coordinates are with respect to an explicit basis of the reachable
    subspace of the ambient carrier space modulo the unobservable subspace.
    ``operators[a][z]`` act on coordinate columns; ``vectors[sigma]`` are the
    source preparation coordinates; ``mass`` is tau.  ``basis`` lists ambient
    representatives of the coordinate basis (reachable vectors), and
    ``observe`` lists ambient row functionals spanning the observables used
    to separate the quotient.
    """
    dimension: int
    operators: dict[str, dict[Hashable, Mat]]
    vectors: dict[Hashable, Vec]
    mass: Vec
    basis: tuple[Vec, ...]
    reachable_words: tuple[tuple[Hashable, Word], ...]
    observing_words: tuple[Word, ...]
    actions: tuple[str, ...]
    outcomes: dict[str, tuple[Hashable, ...]]

    def word_operator(self, word: Word) -> Mat:
        m = identity(self.dimension)
        for a, z in word:
            m = matmul(self.operators[a][z], m)
        return m

    def probability(self, source: Hashable, word: Word) -> Q:
        return dot(self.mass, matvec(self.word_operator(word), self.vectors[source]))

    def state(self, source: Hashable, word: Word) -> Vec:
        return matvec(self.word_operator(word), self.vectors[source])

    def mass_conserving(self) -> bool:
        """tau o sum_z T[a][z] = tau on all of V (automatic when minimal)."""
        for a in self.actions:
            total = zeros(self.dimension, self.dimension)
            for z in self.outcomes[a]:
                total = madd(total, self.operators[a][z])
            if vecmat(self.mass, total) != self.mass:
                return False
        return True


@dataclass(frozen=True)
class LinearSystem:
    """A (possibly signed) finite-dimensional predictive system in ambient
    coordinates: events[a][z] are n x n rational matrices, preparations are
    ambient vectors, ``mass`` is the mass functional tau (default 1^T).
    A PositiveCarrier is the special case of nonnegative events, probability
    preparations and tau = 1^T."""
    dimension: int
    events: dict[str, dict[Hashable, Mat]]
    preparations: dict[Hashable, Vec]
    mass: Vec | None = None

    def __post_init__(self):
        n = self.dimension
        ev = {a: {z: mat(b) for z, b in blocks.items()} for a, blocks in self.events.items()}
        for a, blocks in ev.items():
            for z, b in blocks.items():
                if len(b) != n or any(len(r) != n for r in b):
                    raise RealizationError(f"Event {a!r}/{z!r} is not {n}x{n}")
        preps = {s: vec(v) for s, v in self.preparations.items()}
        if any(len(v) != n for v in preps.values()) or not preps:
            raise RealizationError("Preparations must be ambient vectors")
        m = vec(self.mass) if self.mass is not None else tuple(Q(1) for _ in range(n))
        if len(m) != n:
            raise RealizationError("Mass functional has wrong length")
        object.__setattr__(self, "events", ev)
        object.__setattr__(self, "preparations", preps)
        object.__setattr__(self, "mass", m)

    @property
    def actions(self) -> tuple[str, ...]:
        return tuple(self.events)

    def outcomes(self, a: str) -> tuple[Hashable, ...]:
        return tuple(self.events[a])

    def event(self, a: str, z: Hashable) -> Mat:
        """Event matrix; an undeclared outcome of a declared action is the
        zero event (probability zero), e.g. BOT for a total action."""
        if a not in self.events:
            raise RealizationError(f"Unknown action {a!r}")
        return self.events[a].get(z, zeros(self.dimension, self.dimension))

    def word_matrix(self, word: Word) -> Mat:
        m = identity(self.dimension)
        for a, z in word:
            m = matmul(self.event(a, z), m)
        return m

    def state(self, source: Hashable, word: Word) -> Vec:
        return matvec(self.word_matrix(word), self.preparations[source])

    def probability(self, source: Hashable, word: Word) -> Q:
        return dot(self.mass, self.state(source, word))

    def mass_conserving(self) -> bool:
        for a in self.actions:
            total = zeros(self.dimension, self.dimension)
            for z in self.outcomes(a):
                total = madd(total, self.events[a][z])
            if vecmat(self.mass, total) != self.mass:
                return False
        return True

    @staticmethod
    def of_carrier(carrier: PositiveCarrier) -> "LinearSystem":
        comp = carrier.bottom_completion()
        return LinearSystem(comp.dimension,
                            {a: {z: comp.event(a, z) for z in comp.completed_outcomes(a)}
                             for a in comp.actions},
                            dict(comp.preparations))


def _reachable_closure(system: LinearSystem, letters: list[tuple[str, Hashable]]
                       ) -> tuple[list[Vec], list[tuple[Hashable, Word]]]:
    """Exact basis of span{M_w v_sigma}, each labelled by a (source, word)
    that reaches it.  Breadth-first, so labels are shortest found."""
    basis: list[Vec] = []
    labels: list[tuple[Hashable, Word]] = []
    frontier: list[tuple[Vec, Hashable, Word]] = []
    for s, v in system.preparations.items():
        if solve_in_span(basis, v) is None:
            basis.append(v)
            labels.append((s, ()))
        frontier.append((v, s, ()))
    idx = 0
    while idx < len(frontier):
        v, s, w = frontier[idx]
        idx += 1
        for a, z in letters:
            u = matvec(system.event(a, z), v)
            if any(x != 0 for x in u) and solve_in_span(basis, u) is None:
                basis.append(u)
                labels.append((s, w + ((a, z),)))
                frontier.append((u, s, w + ((a, z),)))
    return basis, labels


def _observable_closure(system: LinearSystem, letters: list[tuple[str, Hashable]]
                        ) -> tuple[list[Vec], list[Word]]:
    rows: list[Vec] = [system.mass]
    words: list[Word] = [()]
    frontier: list[tuple[Vec, Word]] = [(system.mass, ())]
    idx = 0
    while idx < len(frontier):
        f, w = frontier[idx]
        idx += 1
        for a, z in letters:
            g = vecmat(f, system.event(a, z))  # f o T_{a,z}: word (a z) then w
            if any(x != 0 for x in g) and solve_in_span(rows, g) is None:
                rows.append(g)
                words.append(((a, z),) + w)
                frontier.append((g, ((a, z),) + w))
    return rows, words


def minimal_realization(system: "LinearSystem | PositiveCarrier") -> LinearRealization:
    """Exact minimal linear realization of the complete (bottom-completed when
    the input is a carrier) source-indexed behavior.

    dim = rank of the infinite source-indexed Hankel matrix H_{(sigma,u),v}:
    H = O R with R the reachable matrix (columns M_u v_sigma) and O the
    observing matrix (rows tau M_v); rank H = dim(span R) - dim(span R cap
    ker O), which is what the quotient below computes.
    """
    if isinstance(system, PositiveCarrier):
        system = LinearSystem.of_carrier(system)
    letters = [(a, z) for a in system.actions for z in system.outcomes(a)]
    reach, rlabels = _reachable_closure(system, letters)
    obs, owords = _observable_closure(system, letters)
    profile = lambda v: tuple(dot(f, v) for f in obs)  # noqa: E731
    basis: list[Vec] = []
    blabels: list[tuple[Hashable, Word]] = []
    profiles: list[Vec] = []
    for v, lab in zip(reach, rlabels):
        p = profile(v)
        if solve_in_span(profiles, p) is None:
            basis.append(v)
            blabels.append(lab)
            profiles.append(p)
    d = len(basis)

    def coords(v: Vec) -> Vec:
        c = solve_in_span(profiles, profile(v))
        if c is None:
            raise RealizationError("Vector outside the reachable span")
        return c

    operators = {}
    for a in system.actions:
        operators[a] = {}
        for z in system.outcomes(a):
            cols = [coords(matvec(system.event(a, z), b)) for b in basis]
            operators[a][z] = tuple(tuple(cols[j][i] for j in range(d)) for i in range(d))
    vectors = {s: coords(v) for s, v in system.preparations.items()}
    mass = tuple(dot(system.mass, b) for b in basis)
    return LinearRealization(
        dimension=d, operators=operators, vectors=vectors, mass=mass,
        basis=tuple(basis), reachable_words=tuple(blabels),
        observing_words=tuple(owords), actions=system.actions,
        outcomes={a: system.outcomes(a) for a in system.actions})


# --------------------------------------------------------------------------
# Hankel blocks and nonnegative-rank lower bounds
# --------------------------------------------------------------------------

def hankel_block(carrier: PositiveCarrier,
                 rows: Sequence[tuple[Hashable, Word]],
                 cols: Sequence[Word]) -> Mat:
    """H[(sigma,u), v] = p_sigma(u v): joint unnormalized probabilities."""
    return tuple(tuple(carrier.probability(s, u + v) for v in cols) for s, u in rows)


def support_pattern(m: Mat) -> tuple[tuple[bool, ...], ...]:
    return tuple(tuple(x != 0 for x in r) for r in m)


def is_fooling_set(m: Mat, cells: Sequence[tuple[int, int]]) -> bool:
    """cells (i_k, j_k): all m[i_k][j_k] > 0 and for k != l,
    m[i_k][j_l] * m[i_l][j_k] == 0."""
    for i, j in cells:
        if m[i][j] <= 0:
            return False
    for (i1, j1), (i2, j2) in itertools.combinations(cells, 2):
        if m[i1][j2] != 0 and m[i2][j1] != 0:
            return False
    return True


def fooling_set_lower_bound(m: Mat, *, exhaustive_limit: int = 12
                            ) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Largest fooling set found (exhaustive if min(rows, cols) <= limit,
    otherwise greedy).  Any fooling set F gives rank+(m) >= |F|."""
    nr, nc = len(m), len(m[0]) if m else 0
    cells = [(i, j) for i in range(nr) for j in range(nc) if m[i][j] > 0]
    best: tuple[tuple[int, int], ...] = ()
    if min(nr, nc) <= exhaustive_limit:
        # fooling cells use distinct rows and distinct columns
        for size in range(min(nr, nc), 0, -1):
            found = False
            for rows_sel in itertools.combinations(range(nr), size):
                for cols_sel in itertools.permutations(range(nc), size):
                    cand = tuple(zip(rows_sel, cols_sel))
                    if is_fooling_set(m, cand):
                        best = cand
                        found = True
                        break
                if found:
                    break
            if found:
                break
        return len(best), best
    chosen: list[tuple[int, int]] = []
    for c in cells:
        if is_fooling_set(m, chosen + [c]):
            chosen.append(c)
    return len(chosen), tuple(chosen)


def tensor_fooling_set(f1: Sequence[tuple[int, int]], n1: tuple[int, int],
                       f2: Sequence[tuple[int, int]], n2: tuple[int, int]
                       ) -> tuple[tuple[int, int], ...]:
    """Fooling set of kron(A, B) from fooling sets of A (shape n1) and B
    (shape n2): the product set, in Kronecker index order."""
    _, c1 = n1
    r2, c2 = n2
    return tuple((i1 * r2 + i2, j1 * c2 + j2) for (i1, j1) in f1 for (i2, j2) in f2)


def nonneg_rank_upper_bound_certificate(carrier: PositiveCarrier,
                                        rows: Sequence[tuple[Hashable, Word]],
                                        cols: Sequence[Word]) -> dict:
    """The explicit factorization H = O R through the carrier: rank+ <= |C|."""
    R = tuple(tuple(x for x in carrier.law(s, u)) for s, u in rows)       # rows: states
    O = tuple(tuple(x for x in vecmat(tuple(Q(1) for _ in carrier.states),
                                      carrier.word_matrix(v))) for v in cols)
    H = hankel_block(carrier, rows, cols)
    recon = tuple(tuple(dot(R[i], O[j]) for j in range(len(cols))) for i in range(len(rows)))
    if recon != H:
        raise RealizationError("Internal: factorization does not reproduce the block")
    return {"inner_dimension": carrier.dimension,
            "left_factor_nonnegative": all(x >= 0 for r in R for x in r),
            "right_factor_nonnegative": all(x >= 0 for r in O for x in r)}


# --------------------------------------------------------------------------
# exact LP: membership in a finitely generated cone
# --------------------------------------------------------------------------

def cone_coordinates(generators: Sequence[Vec], x: Vec) -> Vec | None:
    """Exact nonnegative coordinates lambda >= 0 with sum_i lambda_i g_i = x,
    or None if x is outside cone(generators).  Phase-I simplex, Bland's rule
    (terminates; all arithmetic in Fractions)."""
    m = len(generators)
    n = len(x)
    if m == 0:
        return () if all(t == 0 for t in x) else None
    # rows: sum_i G[r][i] lam_i + s_r = x_r with x_r >= 0 (flip signs if needed)
    rows = []
    rhs = []
    for r in range(n):
        coeff = [generators[i][r] for i in range(m)]
        b = x[r]
        if b < 0:
            coeff = [-c for c in coeff]
            b = -b
        rows.append(coeff)
        rhs.append(b)
    # tableau: variables lam_0..lam_{m-1}, s_0..s_{n-1}; objective min sum s
    T = [rows[r] + [Q(int(r == k)) for k in range(n)] + [rhs[r]] for r in range(n)]
    basis = [m + r for r in range(n)]
    nvar = m + n
    # reduced costs for min sum s: c_j - sum over basic rows of row coefficients
    def reduced_costs():
        cost = [Q(0)] * (nvar + 1)
        for j in range(nvar + 1):
            cj = Q(1) if m <= j < nvar else Q(0)
            cost[j] = cj - sum((T[r][j] for r in range(n) if basis[r] >= m), Q(0))
        return cost
    while True:
        cost = reduced_costs()
        enter = next((j for j in range(nvar) if cost[j] < 0), None)
        if enter is None:
            break
        ratios = [(T[r][nvar] / T[r][enter], basis[r], r) for r in range(n) if T[r][enter] > 0]
        if not ratios:
            raise RealizationError("Unbounded phase-I LP; impossible")
        _, _, leave = min(ratios)
        piv = T[leave][enter]
        T[leave] = [t / piv for t in T[leave]]
        for r in range(n):
            if r != leave and T[r][enter] != 0:
                f = T[r][enter]
                T[r] = [t - f * u for t, u in zip(T[r], T[leave])]
        basis[leave] = enter
    objective = sum((T[r][nvar] for r in range(n) if basis[r] >= m), Q(0))
    if objective != 0:
        return None
    lam = [Q(0)] * m
    for r in range(n):
        if basis[r] < m:
            lam[basis[r]] = T[r][nvar]
    # verify exactly
    recon = tuple(sum((lam[i] * generators[i][r] for i in range(m)), Q(0)) for r in range(n))
    if recon != tuple(x) or any(l < 0 for l in lam):
        raise RealizationError("Internal LP verification failed")
    return tuple(lam)


@dataclass(frozen=True)
class ConeCertificate:
    """Result of checking a candidate normalized invariant cone."""
    valid: bool
    reason: str
    generators: tuple[Vec, ...]
    event_matrices: dict[str, dict[Hashable, Mat]]
    preparations: dict[Hashable, Vec]
    violations: tuple[tuple[str, Hashable, int], ...]


def verify_cone(realization: LinearRealization, generators: Sequence[Vec],
                *, require_mass_conservation: bool = True) -> ConeCertificate:
    """Cone theorem, constructive direction.

    Hypotheses checked exactly:
      (N)  tau(g_i) = 1 for every generator (normalization; implies the cone
           is pointed and meets ker tau only in 0);
      (P)  every source vector v_sigma lies in cone(g) -- then automatically a
           CONVEX combination because tau(v_sigma) = 1;
      (I)  every event operator maps every generator into cone(g):
           T[a][z] g_i = sum_j B[a][z][j][i] g_j with B >= 0;
      (M)  mass conservation on generators: sum_z tau(T[a][z] g_i) = 1, which
           is automatic for a minimal realization and is exactly the
           column-stochastic normalization 1^T sum_z B[a][z] = 1^T.
    Output: the explicit positive carrier (B, lambda) with the same behavior.
    """
    gens = tuple(vec(g) for g in generators)
    if not gens or any(len(g) != realization.dimension for g in gens):
        raise RealizationError("Generators must be nonempty vectors in V")
    for i, g in enumerate(gens):
        if dot(realization.mass, g) != 1:
            return ConeCertificate(False, f"generator {i} is not tau-normalized", gens, {}, {}, ())
    preps = {}
    for s, v in realization.vectors.items():
        lam = cone_coordinates(gens, v)
        if lam is None:
            return ConeCertificate(False, f"source {s!r} is outside the cone", gens, {}, {}, ())
        preps[s] = lam
    B: dict[str, dict[Hashable, Mat]] = {}
    violations = []
    for a in realization.actions:
        B[a] = {}
        for z in realization.outcomes[a]:
            cols = []
            for i, g in enumerate(gens):
                lam = cone_coordinates(gens, matvec(realization.operators[a][z], g))
                if lam is None:
                    violations.append((a, z, i))
                    lam = tuple(Q(0) for _ in gens)
                cols.append(lam)
            B[a][z] = tuple(tuple(cols[i][j] for i in range(len(gens))) for j in range(len(gens)))
    if violations:
        return ConeCertificate(False, "cone is not invariant", gens, B, preps, tuple(violations))
    if require_mass_conservation:
        for a in realization.actions:
            for i in range(len(gens)):
                col = sum((B[a][z][j][i] for z in realization.outcomes[a] for j in range(len(gens))), Q(0))
                if col != 1:
                    return ConeCertificate(False,
                                           f"mass not conserved on generator {i} under {a!r}: {col}",
                                           gens, B, preps, ())
    return ConeCertificate(True, "normalized invariant cone; carrier constructed", gens, B, preps, ())


def carrier_from_cone(cert: ConeCertificate) -> PositiveCarrier:
    if not cert.valid:
        raise RealizationError("Cannot build a carrier from an invalid cone certificate")
    m = len(cert.generators)
    return PositiveCarrier(tuple(range(m)), cert.event_matrices, dict(cert.preparations), {})


def normalize_ray(realization: LinearRealization, v: Vec) -> Vec | None:
    t = dot(realization.mass, v)
    if t <= 0:
        return None
    return tuple(x / t for x in v)


def reachable_cone_refinement(realization: LinearRealization, *, depth: int = 3,
                              max_generators: int = 64) -> dict:
    """Counterexample-guided search for an invariant cone INSIDE the closed
    reachable cone R: start from normalized reachable vectors up to ``depth``,
    add every image T g that escapes, prune generators that are nonnegative
    combinations of the others.  Returns LAWFUL_REALIZATION with the carrier,
    or UNRESOLVED with the frontier (never an impossibility verdict: R may be
    non-polyhedral while a larger invariant polyhedral cone exists, and it
    may be non-polyhedral with no finite carrier at all)."""
    letters = [(a, z) for a in realization.actions for z in realization.outcomes[a]]
    gens: list[Vec] = []
    frontier = [realization.vectors[s] for s in realization.vectors]
    seen = 0
    while frontier and seen < depth + 1:
        nxt = []
        for v in frontier:
            g = normalize_ray(realization, v)
            if g is not None and g not in gens:
                gens.append(g)
            for a, z in letters:
                nxt.append(matvec(realization.operators[a][z], v))
        frontier = nxt
        seen += 1
    rounds = 0
    while True:
        rounds += 1
        # prune
        pruned: list[Vec] = []
        for i, g in enumerate(gens):
            others = pruned + gens[i + 1:]
            if cone_coordinates(others, g) is None:
                pruned.append(g)
        gens = pruned
        cert = verify_cone(realization, gens)
        if cert.valid:
            return {"verdict": "LAWFUL_REALIZATION", "rounds": rounds,
                    "generators": tuple(gens), "certificate": cert}
        if cert.reason != "cone is not invariant":
            return {"verdict": "UNRESOLVED", "rounds": rounds, "reason": cert.reason,
                    "generators": tuple(gens)}
        added = 0
        for a, z, i in cert.violations:
            g = normalize_ray(realization, matvec(realization.operators[a][z], gens[i]))
            if g is not None and g not in gens:
                gens.append(g)
                added += 1
        if added == 0 or len(gens) > max_generators:
            return {"verdict": "UNRESOLVED", "rounds": rounds,
                    "reason": "generator budget exhausted; reachable cone may be non-polyhedral",
                    "generators": tuple(gens)}


# --------------------------------------------------------------------------
# peripheral-spectrum obstruction (finite certificate of d+ = infinity)
# --------------------------------------------------------------------------

def _rational_sqrt(q: Q) -> Q | None:
    if q < 0:
        return None
    n, d = q.numerator, q.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    if rn * rn == n and rd * rd == d:
        return Q(rn, rd)
    return None


def _divisors(n: int) -> list[int]:
    n = abs(n)
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
        i += 1
    return sorted(out)


def poly_eval(coeffs: Sequence[Q], x: Q) -> Q:
    acc = Q(0)
    for c in coeffs:
        acc = acc * x + c
    return acc


def poly_deflate(coeffs: Sequence[Q], root: Q) -> tuple[Q, ...]:
    """Exact synthetic division by (x - root); the remainder must vanish."""
    out = []
    acc = Q(0)
    for c in coeffs:
        acc = acc * root + c
        out.append(acc)
    if out[-1] != 0:
        raise RealizationError("Not a root")
    return tuple(out[:-1])


def rational_roots_and_remainder(coeffs: Sequence[Q]) -> tuple[list[Q], tuple[Q, ...]]:
    """All rational roots with multiplicity (rational root theorem, exact) and
    the remaining monic cofactor, which has no rational roots."""
    cs = [Q(c) for c in coeffs]
    while cs and cs[0] == 0:
        cs.pop(0)
    if not cs:
        raise RealizationError("Zero polynomial")
    lead = cs[0]
    cs = [c / lead for c in cs]
    roots: list[Q] = []
    while len(cs) > 1:
        # trailing zeros give root 0
        if cs[-1] == 0:
            roots.append(Q(0))
            cs = cs[:-1]
            continue
        den = 1
        for c in cs:
            den = math.lcm(den, c.denominator)
        ics = [int(c * den) for c in cs]
        a0, an = ics[-1], ics[0]
        found = None
        for p_ in _divisors(a0):
            for q_ in _divisors(an):
                for sign in (1, -1):
                    cand = Q(sign * p_, q_)
                    if poly_eval(cs, cand) == 0:
                        found = cand
                        break
                if found is not None:
                    break
            if found is not None:
                break
        if found is None:
            break
        roots.append(found)
        cs = list(poly_deflate(cs, found))
    return roots, tuple(cs)


def poly_mul(a: Sequence[Q], b: Sequence[Q]) -> tuple[Q, ...]:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def poly_divmod(a: Sequence[Q], b: Sequence[Q]) -> tuple[tuple[Q, ...], tuple[Q, ...]]:
    a = [Q(x) for x in a]
    b = [Q(x) for x in b]
    if len(a) < len(b):
        return (Q(0),), tuple(a)
    quot = [Q(0)] * (len(a) - len(b) + 1)
    for i in range(len(quot)):
        coef = a[i] / b[0]
        quot[i] = coef
        for j in range(len(b)):
            a[i + j] -= coef * b[j]
    rem = a[len(quot):]
    return tuple(quot), tuple(rem)


def cyclotomic(k: int) -> tuple[Q, ...]:
    """Exact coefficients (highest degree first) of the k-th cyclotomic
    polynomial, by Phi_k = (x^k - 1) / prod_{d | k, d < k} Phi_d."""
    if k < 1:
        raise RealizationError("k >= 1")
    num = [Q(1)] + [Q(0)] * (k - 1) + [Q(-1)]
    for d in range(1, k):
        if k % d == 0:
            num, rem = poly_divmod(num, cyclotomic(d))
            if any(r != 0 for r in rem):
                raise RealizationError("Internal cyclotomic division error")
            num = list(num)
    return tuple(num)


def euler_phi(k: int) -> int:
    return sum(1 for a in range(1, k + 1) if math.gcd(a, k) == 1)


def scaled_cyclotomic_order(coeffs: Sequence[Q], rho: Q) -> int | None:
    """If the monic polynomial ``coeffs`` equals rho^d Phi_k(x / rho) for some
    k with phi(k) = d (i.e. its roots are rho times the primitive k-th roots
    of unity), return k; else None.  Exact."""
    d = len(coeffs) - 1
    if d < 1 or rho <= 0:
        return None
    # phi(k) = d forces k <= 2 d^2 (phi(k) >= sqrt(k/2))
    for k in range(1, 2 * d * d + 2):
        if euler_phi(k) != d:
            continue
        phi = cyclotomic(k)
        scaled = tuple(phi[i] * rho ** i for i in range(d + 1))  # rho^d Phi_k(x/rho)
        if tuple(coeffs) == scaled:
            return k
    return None


def quadratic_root_of_unity_test(b: Q, c: Q) -> bool | None:
    """For an irreducible real quadratic x^2 - b x + c (b^2 < 4c) with roots
    rho e^{+-i theta}, rho^2 = c: returns True iff e^{i theta} is a root of
    unity.  Exact: w = lambda/conj(lambda) = lambda^2 / c satisfies
    c w^2 + (2c - b^2) w + c = 0, so w is a root of unity of degree <= 2
    iff that polynomial is (a multiple of) Phi_1^2, Phi_2^2, Phi_3, Phi_4 or
    Phi_6, i.e. iff b^2 / c in {0, 1, 2, 3} (b^2 = 4c is excluded)."""
    if b * b >= 4 * c or c <= 0:
        raise RealizationError("Not an irreducible real quadratic with complex roots")
    return (b * b) / c in (Q(0), Q(1), Q(2), Q(3))


def peripheral_spectrum_certificate(realization: LinearRealization, word: Word) -> dict:
    """Obstruction theorem (finite certificate), quantitative form.

    If an m-state positive carrier realizes the behavior, then for every
    event word w and every eigenvalue lambda of T_w (minimal realization)
    with |lambda| = rho(T_w):  lambda = rho * zeta with zeta a root of unity
    of order at most m.  Proof: rho(T_w) equals the spectral radius of
    M_w restricted to the positively reachable states S (exact mass growth);
    lambda is then a peripheral eigenvalue of a nonnegative matrix, so by
    Frobenius it lies in rho * (h-th roots of unity) for the imprimitivity
    index h of an irreducible block, and that block has at least h states.
    Hence  d+  >=  ord(lambda / rho),  and  d+ = infinity  when the ratio is
    not a root of unity.

    The routine computes det(xI - T_w) exactly, splits off rational roots,
    and decides the cofactor when it is quadratic, or a scaled cyclotomic
    polynomial rho^d Phi_k(x/rho) with rational rho.  Verdicts:
      FINITE_OBSTRUCTION  lower_bound = "infinity": no finite positive carrier
      LOWER_BOUND         lower_bound = k >= 2 states for every positive carrier
      NO_OBSTRUCTION      peripheral ratios trivial (order 1 or 2 only)
      UNRESOLVED          undecided cofactor (never reported as impossibility)
    No floating point is used anywhere.
    """
    T = realization.word_operator(word)
    cp = charpoly(T)
    roots, rem = rational_roots_and_remainder(cp)
    info = []
    for lam in roots:
        info.append({"factor": f"x - ({lam})", "degree": 1, "modulus_squared": lam * lam,
                     "ratio_order": 1 if lam >= 0 else 2, "root_of_unity_ratio": True})
    unresolved = False
    if len(rem) == 3:
        b, c = -rem[1], rem[2]
        disc = b * b - 4 * c
        if disc < 0:
            ratio = (b * b) / c
            orders = {Q(0): 4, Q(1): (6 if b > 0 else 3), Q(2): 8, Q(3): 12}
            info.append({"factor": f"x^2 - ({b}) x + ({c})", "degree": 2, "modulus_squared": c,
                         "root_of_unity_ratio": ratio in orders,
                         "ratio_order": orders.get(ratio),
                         "trace": b, "det": c, "cos_theta_squared": (b * b) / (4 * c)})
        else:
            info.append({"factor": f"x^2 - ({b}) x + ({c})", "degree": 2, "real_irrational": True,
                         "discriminant": disc, "root_of_unity_ratio": True, "ratio_order": 2,
                         "modulus_squared": None, "trace": b, "det": c})
    elif len(rem) > 3:
        d = len(rem) - 1
        entry = {"factor": "cofactor of degree %d" % d, "degree": d, "coefficients": rem,
                 "modulus_squared": None, "root_of_unity_ratio": None, "ratio_order": None}
        # scaled cyclotomic with rational rho: candidates rho from positive rational
        # roots and from rational square roots of the constant term^(1/d)
        candidates = set(abs(l) for l in roots if l != 0)
        const = rem[-1]
        for rho in sorted(candidates):
            k = scaled_cyclotomic_order(rem, rho)
            if k is not None:
                entry.update({"modulus_squared": rho * rho, "ratio_order": k,
                              "root_of_unity_ratio": True, "cyclotomic_order": k,
                              "rho": rho})
                break
        if entry["ratio_order"] is None:
            # last attempt: rho from exact d-th root of |const|
            r = _rational_root_n(abs(const), d)
            if r is not None:
                k = scaled_cyclotomic_order(rem, r)
                if k is not None:
                    entry.update({"modulus_squared": r * r, "ratio_order": k,
                                  "root_of_unity_ratio": True, "cyclotomic_order": k,
                                  "rho": r})
        if entry["ratio_order"] is None:
            unresolved = True
        info.append(entry)
    known = [e["modulus_squared"] for e in info if e.get("modulus_squared") is not None]
    unknown = [e for e in info if e.get("modulus_squared") is None]
    verdict = "UNRESOLVED"
    witness = None
    lower: int | str | None = None
    if known and not unresolved:
        rho2 = max(known)
        bounded = True
        for e in unknown:
            b, disc = e["trace"], e["discriminant"]
            r = _rational_sqrt(rho2)
            if r is None or 2 * r - abs(b) < 0 or disc > (2 * r - abs(b)) ** 2:
                bounded = False
        peripheral = [e for e in info if e.get("modulus_squared") == rho2]
        if bounded:
            if any(e["root_of_unity_ratio"] is False for e in peripheral):
                verdict = "FINITE_OBSTRUCTION"
                lower = "infinity"
                witness = next(e for e in peripheral if e["root_of_unity_ratio"] is False)
            else:
                lower = max(e["ratio_order"] for e in peripheral)
                witness = max(peripheral, key=lambda e: e["ratio_order"])
                verdict = "LOWER_BOUND" if lower >= 3 else "NO_OBSTRUCTION"
    return {"word": word, "charpoly": cp, "factors": info, "verdict": verdict,
            "lower_bound": lower, "witness": witness,
            "theorem": ("m-state positive carrier => every peripheral eigenvalue of every "
                        "minimal-realization event word operator is rho times a root of "
                        "unity of order <= m")}


def _rational_root_n(q: Q, n: int) -> Q | None:
    """Exact positive rational n-th root of q, or None."""
    if q <= 0:
        return None

    def iroot(x: int) -> int | None:
        lo, hi = 0, 1
        while hi ** n <= x:
            hi *= 2
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** n < x:
                lo = mid + 1
            else:
                hi = mid
        return lo if lo ** n == x else None
    rn, rd = iroot(q.numerator), iroot(q.denominator)
    if rn is None or rd is None:
        return None
    return Q(rn, rd)


# --------------------------------------------------------------------------
# exact equivalence certificate and distinguishing experiments
# --------------------------------------------------------------------------

def _direct_sum_difference(s1: LinearSystem, s2: LinearSystem) -> LinearSystem:
    if set(s1.actions) != set(s2.actions):
        raise RealizationError("Different action alphabets")
    n1, n2 = s1.dimension, s2.dimension
    events = {}
    for a in s1.actions:
        zs = list(s1.outcomes(a)) + [z for z in s2.outcomes(a) if z not in s1.outcomes(a)]
        events[a] = {}
        for z in zs:
            A = s1.events[a].get(z, zeros(n1, n1))
            B = s2.events[a].get(z, zeros(n2, n2))
            top = tuple(tuple(A[i]) + tuple(Q(0) for _ in range(n2)) for i in range(n1))
            bot = tuple(tuple(Q(0) for _ in range(n1)) + tuple(B[i]) for i in range(n2))
            events[a][z] = top + bot
    if set(s1.preparations) != set(s2.preparations):
        raise RealizationError("Different source alphabets")
    preps = {s: tuple(s1.preparations[s]) + tuple(s2.preparations[s]) for s in s1.preparations}
    mass = tuple(s1.mass) + tuple(-t for t in s2.mass)
    return LinearSystem(n1 + n2, events, preps, mass)


def equivalence_certificate(s1: "LinearSystem | PositiveCarrier",
                            s2: "LinearSystem | PositiveCarrier") -> dict:
    """Exact decision: do two systems have the same complete source-indexed
    behavior (all words, bottom included)?  Uses the difference system with
    mass (tau1, -tau2); equivalent iff its minimal realization is 0-dim.
    Otherwise returns an explicit distinguishing (source, word) with both
    probabilities -- a legal experiment candidate (legality must be checked
    separately against the availability structure)."""
    if isinstance(s1, PositiveCarrier):
        s1 = LinearSystem.of_carrier(s1)
    if isinstance(s2, PositiveCarrier):
        s2 = LinearSystem.of_carrier(s2)
    diff = _direct_sum_difference(s1, s2)
    R = minimal_realization(diff)
    if R.dimension == 0:
        return {"equivalent": True, "bound": s1.dimension + s2.dimension}
    # find a reachable basis vector with nonzero observation
    for (src, u), b in zip(R.reachable_words, R.basis):
        for v, f in zip(R.observing_words, _observable_closure(
                diff, [(a, z) for a in diff.actions for z in diff.outcomes(a)])[0]):
            if dot(f, b) != 0:
                w = u + v
                return {"equivalent": False, "source": src, "word": w,
                        "p1": s1.probability(src, w), "p2": s2.probability(src, w)}
    raise RealizationError("Internal: nonzero minimal dimension without witness")


# --------------------------------------------------------------------------
# availability, legality, adaptive policies: closed-loop transport
# --------------------------------------------------------------------------

def legality_pattern(carrier: PositiveCarrier, source: Hashable, depth: int
                     ) -> dict[Word, tuple[str, ...]]:
    """For every legal word u of length <= depth with p_sigma(u) > 0, the
    tuple of actions uniformly available after u.  This is the operational
    menu law; it is a function of the behavior of the bottom completion:
    a is available after u iff p_sigma(u a BOT) = 0 and u is legal."""
    out: dict[Word, tuple[str, ...]] = {}
    frontier: list[Word] = [()]
    for _ in range(depth + 1):
        nxt: list[Word] = []
        for u in frontier:
            if carrier.probability(source, u) == 0 or not carrier.legal(source, u):
                continue
            menu = tuple(a for a in carrier.actions if carrier.available(source, u, a))
            out[u] = menu
            for a in menu:
                for z in carrier.outcomes(a):
                    nxt.append(u + ((a, z),))
        frontier = nxt
    return out


def closed_loop_law(carrier: PositiveCarrier, source: Hashable, policy,
                    horizon: int) -> dict[Word, Q]:
    """Joint law of actual (action, receipt) histories of length == horizon
    under a public-history policy ``policy(u) -> {action: weight}`` (weights
    sum to 1; an empty dict stops).  P(h) = prod_i psi(a_i | h_<i) * p_sigma(h).
    Raises if the policy ever selects an action that is not uniformly
    available (an illegal policy)."""
    laws: dict[Word, Q] = {(): Q(1)}
    for _ in range(horizon):
        nxt: dict[Word, Q] = {}
        for u, weight in laws.items():
            if weight == 0:
                continue
            choice = policy(u)
            if not choice:
                nxt[u] = weight
                continue
            if sum((rat(w) for w in choice.values()), Q(0)) != 1:
                raise RealizationError("Policy weights must sum to one")
            for a, w in choice.items():
                if rat(w) == 0:
                    continue
                if not carrier.available(source, u, a):
                    raise RealizationError(f"Illegal policy: {a!r} not uniformly available after {u!r}")
                pu = carrier.probability(source, u)
                for z in carrier.outcomes(a):
                    h = u + ((a, z),)
                    ph = carrier.probability(source, h)
                    if ph == 0:
                        continue
                    nxt[h] = nxt.get(h, Q(0)) + weight * rat(w) * ph / pu
        laws = nxt
    return laws


def source_posterior(carrier: PositiveCarrier, prior: dict[Hashable, Q], word: Word
                     ) -> dict[Hashable, Q] | None:
    """Posterior over original sources given actual history ``word``;
    None when the evidence is zero.  Depends on the behavior only."""
    joint = {s: rat(prior[s]) * carrier.probability(s, word) for s in prior}
    ev = sum(joint.values(), Q(0))
    if ev == 0:
        return None
    return {s: j / ev for s, j in joint.items()}


def promotion_witness(fine: PositiveCarrier, coarse: PositiveCarrier, depth: int
                      ) -> dict | None:
    """A failed availability square: a legal (source, word) in both carriers
    whose uniformly-available menus differ, or a word legal in one and not
    the other.  None if the legality patterns agree to ``depth``."""
    for s in fine.preparations:
        if s not in coarse.preparations:
            raise RealizationError("Source alphabets differ")
        pf = legality_pattern(fine, s, depth)
        pc = legality_pattern(coarse, s, depth)
        for u in sorted(set(pf) | set(pc), key=lambda w: (len(w), repr(w))):
            if u not in pf or u not in pc or set(pf[u]) != set(pc[u]):
                return {"source": s, "word": u, "fine_menu": pf.get(u),
                        "coarse_menu": pc.get(u)}
    return None


# --------------------------------------------------------------------------
# canonical examples
# --------------------------------------------------------------------------

def calibration_matrix() -> Mat:
    """P = 1/2 [[1,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,1]]: row-stochastic,
    rank 3 (r1 - r2 - r3 + r4 = 0), nonnegative rank 4 (fooling set
    {(1,1),(2,3),(3,2),(4,4)}).  Lazy reflecting walk on the path 1-2-3-4."""
    h = Q(1, 2)
    return mat([[h, h, 0, 0], [h, 0, h, 0], [0, h, 0, h], [0, 0, h, h]])


def observed_chain_events(P: Mat) -> dict[Hashable, Mat]:
    """Action 'step and report the new position': M_z[c'][c] = P[c][z] [c'=z]."""
    n = len(P)
    return {z: tuple(tuple(P[c][z] if cp == z else Q(0) for c in range(n)) for cp in range(n))
            for z in range(n)}


def permutation_event(perm: Sequence[int]) -> Mat:
    n = len(perm)
    return tuple(tuple(Q(int(cp == perm[c])) for c in range(n)) for cp in range(n))


def path_walk_carrier(copies: int = 1) -> PositiveCarrier:
    """The separation family PW_n: n independent lazy reflecting path walks.
    Action 'a': every coordinate steps by P and the full position tuple is
    reported.  Action 'b': silent, deterministic pair swap (1 2)(3 4) on every
    coordinate; it does not commute with 'a'.  Source 'u' is the uniform
    preparation; Dirac sources 'd<i>' are declared as well for n = 1.
    Exact facts (proved in the dossier, tested here):
      linear predictive dimension r = 3^n;  positive carrier dimension d+ = 4^n."""
    if copies < 1:
        raise RealizationError("copies >= 1")
    P = calibration_matrix()
    preps: dict[Hashable, Vec] = {"u": (Q(1, 4),) * 4}
    if copies == 1:
        for i in range(4):
            preps[f"d{i}"] = tuple(Q(int(j == i)) for j in range(4))
    base = PositiveCarrier((0, 1, 2, 3), {"a": observed_chain_events(P),
                                          "b": {"s": permutation_event((1, 0, 3, 2))}},
                           preps if copies == 1 else {"u": preps["u"]})
    out = base
    for _ in range(copies - 1):
        out = out.tensor(base)
    return out


def rational_clock() -> LinearSystem:
    """The rational probability clock (dimension 3, no finite positive carrier).
    Coordinates (m, x, y); tau = (1, 1/4, 0); rotation by theta with
    cos theta = 3/5, sin theta = 4/5 (an irrational multiple of pi: Niven, or
    (3+4i)^n has imaginary part = 4 mod 5 for all n >= 1).
      action 'clock': outcome 'tick'  : T = 1/2 * diag(1, Rot_theta)
                      outcome 'reset' : T = v_* (tau - tau T_tick)   (rank one)
      action 'b'    : outcome 'ok'    : T = v_* tau  (silent hard reset; does
                                        not commute with tick)
    with v_* = (4/5)(1, 1, 0), sources s0 = (1,0,0) and s* = v_*.
    Mass conservation holds exactly; nonnegativity of every word probability
    follows from invariance of S = {lambda T_tick^k v : v in {s0, v_*}}."""
    c, s = Q(3, 5), Q(4, 5)
    Tt = mat([[Q(1, 2), 0, 0], [0, c / 2, -s / 2], [0, s / 2, c / 2]])
    tau = vec([1, Q(1, 4), 0])
    vstar = vec([Q(4, 5), Q(4, 5), 0])
    resid = tuple(t - u for t, u in zip(tau, vecmat(tau, Tt)))
    Tr = tuple(tuple(vstar[i] * resid[j] for j in range(3)) for i in range(3))
    Tb = tuple(tuple(vstar[i] * tau[j] for j in range(3)) for i in range(3))
    return LinearSystem(3, {"clock": {"tick": Tt, "reset": Tr}, "b": {"ok": Tb}},
                        {"s0": vec([1, 0, 0]), "sstar": vstar}, tau)


def companion(coeffs: Sequence[Q]) -> Mat:
    """Companion matrix of a monic polynomial (highest degree first)."""
    d = len(coeffs) - 1
    rows = []
    for i in range(d):
        row = [Q(0)] * d
        if i + 1 < d:
            row[i + 1] = Q(1)
        rows.append(row)
    for j in range(d):
        rows[d - 1][j] = -Q(coeffs[d - j])
    return tuple(tuple(r) for r in rows)


def cyclotomic_clock(k: int, *, visibility: Q = Q(1, 8)) -> LinearSystem:
    """The k-th cyclotomic clock C_k (rational data, dimension 1 + phi(k)).

    V = Q (mass axis) + Q^{phi(k)}; T_tick = 1/2 * (1 + C_k) with C_k the
    companion matrix of the k-th cyclotomic polynomial (order exactly k);
    tau = (1, eps, 0, ..., 0) with eps = ``visibility`` scaled so that every
    orbit value stays within 1/4 of the axis; 'reset' = v_* (tau - tau T_tick);
    silent 'b' = v_* tau.  Facts (dossier): linear dimension r = 1 + phi(k);
    every positive carrier has >= k states (peripheral eigenvalue
    (1/2) zeta_k, Frobenius imprimitivity); the k-orbit cone gives a
    k-state carrier; hence d+ = k exactly."""
    if k < 3:
        raise RealizationError("k >= 3 (k = 1, 2 give real rotations)")
    phi = cyclotomic(k)
    d = len(phi) - 1
    n = 1 + d
    C = companion(phi)
    Tt = [[Q(0)] * n for _ in range(n)]
    Tt[0][0] = Q(1, 2)
    for i in range(d):
        for j in range(d):
            Tt[i + 1][j + 1] = C[i][j] / 2
    Tt = tuple(tuple(r) for r in Tt)
    x = tuple(Q(int(i == 0)) for i in range(d))  # cyclic vector e_1 for C
    # orbit of x under C (k vectors); bound its first coordinates
    orbit = []
    v = x
    for _ in range(k):
        orbit.append(v)
        v = matvec(C, v)
    big = max(abs(o[0]) for o in orbit) or Q(1)
    eps = visibility / big  # |eps * (C^n x)_1| <= visibility <= 1/4
    if eps * big > Q(1, 4):
        raise RealizationError("visibility too large for manifest nonnegativity")
    tau = (Q(1), eps) + tuple(Q(0) for _ in range(d - 1))
    vstar = (Q(1),) + x
    t = dot(tau, vstar)
    vstar = tuple(c / t for c in vstar)
    resid = tuple(a - b for a, b in zip(tau, vecmat(tau, Tt)))
    Tr = tuple(tuple(vstar[i] * resid[j] for j in range(n)) for i in range(n))
    Tb = tuple(tuple(vstar[i] * tau[j] for j in range(n)) for i in range(n))
    v0 = (Q(1),) + tuple(Q(0) for _ in range(d))
    return LinearSystem(n, {"clock": {"tick": Tt, "reset": Tr}, "b": {"ok": Tb}},
                        {"s0": v0, "sstar": vstar}, tau)


def orbit_cone_carrier(system: LinearSystem, source: Hashable, word: Word, k: int
                       ) -> tuple[LinearRealization, ConeCertificate]:
    """Cone generated by the first k iterates of ``word`` on ``source`` in the
    minimal realization, verified by exact LP; returns the certificate."""
    R = minimal_realization(system)
    gens = []
    v = R.vectors[source]
    Tw = R.word_operator(word)
    for _ in range(k):
        g = normalize_ray(R, v)
        if g is None:
            raise RealizationError("orbit vector has nonpositive mass")
        gens.append(g)
        v = matvec(Tw, v)
    return R, verify_cone(R, gens)


def availability_square() -> tuple[PositiveCarrier, PositiveCarrier]:
    """Minimal failed availability square.
    FINE: states {0,1}; action 'a' (total): outcome 'o' w.p. 1, keep state;
          action 'b': enabled on state 0 only, outcome 'ok', keep state.
          sources: 'pure' = delta_0, 'mixed' = (1/2, 1/2).
    COARSE: one state, 'a' and 'b' total.
    Both carriers have identical probabilities on every legal word of FINE
    (all equal to 1), identical linear dimension 1 of the legal behavior,
    but COARSE promotes 'b' to legal for the mixed source: the policy
    'execute b' is legal in COARSE and illegal in FINE.  The bottom-completed
    FINE behavior has linear dimension 2 (p_mixed(b BOT) = 1/2 vs
    p_pure(b BOT) = 0), and 2 is the positive lawful carrier dimension."""
    one = Q(1)
    fine = PositiveCarrier((0, 1),
                           {"a": {"o": identity(2)},
                            "b": {"ok": mat([[one, 0], [0, 0]])}},
                           {"pure": (1, 0), "mixed": (Q(1, 2), Q(1, 2))},
                           {"b": (True, False)})
    coarse = PositiveCarrier((0,), {"a": {"o": ((one,),)}, "b": {"ok": ((one,),)}},
                             {"pure": (1,), "mixed": (1,)})
    return fine, coarse


# --------------------------------------------------------------------------
# the oracle
# --------------------------------------------------------------------------

def carrier_realization_oracle(system: "LinearSystem | PositiveCarrier", *,
                               proposed_dimension: int | None = None,
                               hankel_rows: Sequence[tuple[Hashable, Word]] | None = None,
                               hankel_cols: Sequence[Word] | None = None,
                               obstruction_words: Sequence[Word] | None = None,
                               cone_depth: int = 3, cone_budget: int = 64) -> dict:
    """Four-way verdict on positive carrier realizability.

    LAWFUL_REALIZATION      explicit carrier + exact equivalence certificate
    FINITE_OBSTRUCTION      rigorous lower bound > proposed dimension, or a
                            peripheral-spectrum certificate of d+ = infinity
    MORE_EXPERIMENTS_REQUIRED  (used by ``distinguishing_experiment``)
    UNRESOLVED              budget or horizon insufficient; never "impossible"
                            because a search timed out.
    """
    if isinstance(system, PositiveCarrier):
        src_carrier = system
        system = LinearSystem.of_carrier(system)
    else:
        src_carrier = None
    R = minimal_realization(system)
    report: dict = {"linear_dimension": R.dimension, "proposed_dimension": proposed_dimension,
                    "mass_conserving_minimal": R.mass_conserving()}
    lower = R.dimension
    certs = []
    if hankel_rows is not None and hankel_cols is not None and src_carrier is not None:
        H = hankel_block(src_carrier, hankel_rows, hankel_cols)
        size, cells = fooling_set_lower_bound(H)
        certs.append({"type": "fooling_set", "size": size, "cells": cells,
                      "block_rank": rank(H)})
        lower = max(lower, size)
    report["positive_dimension_lower_bound"] = lower
    report["certificates"] = certs
    for w in (obstruction_words or ()):
        c = peripheral_spectrum_certificate(R, w)
        certs.append({"type": "peripheral_spectrum", **c})
        if c["verdict"] == "FINITE_OBSTRUCTION":
            report["verdict"] = "FINITE_OBSTRUCTION"
            report["positive_dimension_lower_bound"] = "infinity"
            report["reason"] = "no finite positive carrier (peripheral spectrum)"
            return report
        if c["verdict"] == "LOWER_BOUND":
            lower = max(lower, c["lower_bound"])
    report["positive_dimension_lower_bound"] = lower
    if proposed_dimension is not None and proposed_dimension < lower:
        report["verdict"] = "FINITE_OBSTRUCTION"
        report["reason"] = f"every positive carrier has >= {lower} states"
        return report
    search = reachable_cone_refinement(R, depth=cone_depth, max_generators=cone_budget)
    report["cone_search_rounds"] = search["rounds"]
    if search["verdict"] == "LAWFUL_REALIZATION":
        cert = search["certificate"]
        carrier = carrier_from_cone(cert)
        eq = equivalence_certificate(system, carrier)
        if not eq["equivalent"]:
            raise RealizationError("Internal: cone carrier is not equivalent")
        report["carrier_dimension"] = carrier.dimension
        report["carrier"] = carrier
        report["equivalence"] = eq
        if proposed_dimension is None or carrier.dimension <= proposed_dimension:
            report["verdict"] = "LAWFUL_REALIZATION"
        else:
            report["verdict"] = "UNRESOLVED"
            report["reason"] = (f"a {carrier.dimension}-state carrier exists; the proposed "
                                f"dimension {proposed_dimension} is between the lower bound "
                                f"{lower} and that")
        return report
    report["verdict"] = "UNRESOLVED"
    report["reason"] = search.get("reason", "cone search budget exhausted")
    return report


def distinguishing_experiment(c1: "LinearSystem | PositiveCarrier",
                              c2: "LinearSystem | PositiveCarrier") -> dict:
    """Two candidate models consistent with the same finite data: return a
    (source, word) on which they differ, flagged MORE_EXPERIMENTS_REQUIRED,
    without asserting that the source preparation is physically available."""
    eq = equivalence_certificate(c1, c2)
    if eq["equivalent"]:
        return {"verdict": "EQUIVALENT", **eq}
    legal = None
    if isinstance(c1, PositiveCarrier):
        legal = c1.legal(eq["source"], eq["word"])
    return {"verdict": "MORE_EXPERIMENTS_REQUIRED", **eq, "legal_in_first": legal,
            "note": "a declared preparation is mathematical data, not an authenticated reset"}
