"""Exact finite NO-GHOST certificates (model-relative, never empirical receipts).

Three distinct contracts are deliberately exposed:
* ``enumerate_schedule``: positive-probability POSSIBLE private executions of a
  fixed, public schedule under declared source-indexed kernels;
* ``couple_contexts``: an arbitrary distribution SUPPORTED on supplied atoms;
* ``check_operational_weights``: the much stronger fixed-preparation/kernel law.

Support is not frequency and possible is not performed. The kernel table is a
declared finite model, not authentication of a physical instrument. Complete
joint diamonds preserve source/outcome/endpoint law, not private path identity
or history-dependent future menus. No sheafification or sensor is synthesized.
All arithmetic is rational. Bounded search exhaustion means UNRESOLVED.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations
from typing import Hashable, Mapping, Sequence


class NoGhostError(ValueError):
    """A declared finite contract is malformed."""


def exact(value) -> Q:
    if type(value) not in (int, Q):
        raise NoGhostError("Use int/Fraction probabilities, never float or bool")
    return Q(value)


def _matrix(A, b):
    A = tuple(tuple(exact(x) for x in row) for row in A)
    b = tuple(exact(x) for x in b)
    if not A or len(A) != len(b) or len({len(row) for row in A}) != 1:
        raise NoGhostError("A nonempty rectangular equation system is required")
    return A, b


def verify_primal(A, b, p) -> bool:
    """Independent arithmetic check of A p=b, p>=0 (no solver trusted)."""
    try:
        A, b = _matrix(A, b)
        p = tuple(exact(x) for x in p)
        return (len(p) == len(A[0]) and all(x >= 0 for x in p)
                and all(sum((a*x for a, x in zip(row, p)), Q(0)) == rhs
                        for row, rhs in zip(A, b)))
    except (NoGhostError, TypeError):
        return False


def verify_dual(A, b, y) -> bool:
    """Farkas sign convention: y^T A>=0 and y^T b<0."""
    try:
        A, b = _matrix(A, b)
        y = tuple(exact(x) for x in y)
        return (len(y) == len(A) and
                all(sum((y[i]*A[i][j] for i in range(len(A))), Q(0)) >= 0
                    for j in range(len(A[0]))) and
                sum((v*w for v, w in zip(y, b)), Q(0)) < 0)
    except (NoGhostError, TypeError):
        return False


@dataclass(frozen=True)
class LinearResult:
    status: str
    primal: tuple[Q, ...] | None = None
    dual: tuple[Q, ...] | None = None
    checked_bases: int = 0
    reason: str = ""


def _reduce(A, b):
    """RREF with exact row-operation provenance T, so reduced A=T A."""
    m, n = len(A), len(A[0])
    rows = [list(row) + [b[i]] + [Q(int(i == j)) for j in range(m)]
            for i, row in enumerate(A)]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        div = rows[rank][col]
        rows[rank] = [x/div for x in rows[rank]]
        for i in range(m):
            if i != rank and rows[i][col]:
                coeff = rows[i][col]
                rows[i] = [x-coeff*y for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == m:
            break
    return rows, rank


def _unique_square(A, b):
    if not A:
        return ()
    rows, rank = _reduce(A, b)
    if rank != len(A):
        return None
    return tuple(row[len(A)] for row in rows)


def solve_nonnegative(A, b, *, max_bases: int = 100000) -> LinearResult:
    """Bounded exact feasibility and Farkas certification.

    Rational RREF first handles linear inconsistency. A feasible nonnegative
    cone combination has a basic feasible representative, so enumerate r-column
    bases. For infeasibility, enumerate vertices of {y: A^T y>=0, b^T y=-1}
    in full-row-rank coordinates: r-1 active atom inequalities suffice. This
    polyhedron is pointed because A has full row rank. Expand y through saved
    row operations and independently verify every returned certificate.
    """
    A, b = _matrix(A, b)
    if type(max_bases) is not int or max_bases < 0:
        raise NoGhostError("max_bases must be a nonnegative integer")
    m, n = len(A), len(A[0])
    reduced, rank = _reduce(A, b)
    for row in reduced[rank:]:
        if row[n]:
            y = tuple(-v/row[n] for v in row[n+1:])
            assert verify_dual(A, b, y)
            return LinearResult("PROBABILITY_COUPLING_FAILURE", dual=y,
                                reason="exact linear inconsistency")
    if rank == 0:
        p = (Q(0),)*n
        return LinearResult("LAWFUL_GLUING", primal=p,
                            reason="zero equation system; normalization is caller's contract")
    C = tuple(tuple(row[:n]) for row in reduced[:rank])
    d = tuple(row[n] for row in reduced[:rank])
    checked = 0
    for basis in combinations(range(n), rank):
        if checked >= max_bases:
            return LinearResult("UNRESOLVED", checked_bases=checked,
                                reason="primal basis budget exhausted")
        checked += 1
        x = _unique_square(tuple(tuple(row[j] for j in basis) for row in C), d)
        if x is not None and all(v >= 0 for v in x):
            p = [Q(0)]*n
            for j, v in zip(basis, x):
                p[j] = v
            assert verify_primal(A, b, p)
            return LinearResult("LAWFUL_GLUING", primal=tuple(p), checked_bases=checked,
                                reason="exact nonnegative solution; operational constraints only if supplied")
    for active in combinations(range(n), rank-1):
        if checked >= max_bases:
            return LinearResult("UNRESOLVED", checked_bases=checked,
                                reason="dual basis budget exhausted")
        checked += 1
        M = (d,) + tuple(tuple(C[i][j] for i in range(rank)) for j in active)
        y0 = _unique_square(M, (Q(-1),)+(Q(0),)*(rank-1))
        if y0 is None:
            continue
        y = tuple(sum((y0[i]*reduced[i][n+1+j] for i in range(rank)), Q(0))
                  for j in range(m))
        if verify_dual(A, b, y):
            return LinearResult("PROBABILITY_COUPLING_FAILURE", dual=y,
                                checked_bases=checked, reason="exact Farkas inequality")
    raise AssertionError("Exhaustive finite primal/dual search violated Farkas alternative")


PublicHistory = tuple[tuple[str, Hashable], ...]


@dataclass(frozen=True)
class Event:
    occurrence: str
    parents: frozenset[str] = frozenset()


@dataclass(frozen=True)
class Step:
    outcome: Hashable
    after: Hashable
    branch: Hashable
    probability: Q


@dataclass(frozen=True)
class PrivateEvent:
    occurrence: str
    outcome: Hashable
    before: Hashable
    after: Hashable
    branch: Hashable


@dataclass(frozen=True)
class PossibleHistory:
    source: Hashable
    initial: Hashable
    current: Hashable
    events: tuple[PrivateEvent, ...]
    mass: Q
    source_id: str = ""
    basis: str = ""

    @property
    def public(self) -> PublicHistory:
        return tuple((e.occurrence, e.outcome) for e in self.events)

    @property
    def identity(self):
        return self.source_id, self.basis, self.source, self.initial, self.events


@dataclass(frozen=True)
class FiniteContract:
    """Finite explicit source-indexed table. Missing rows mean unavailable.

    Epochs must not decrease. Resource contracts and extra memory are encoded in
    the declared states and enabled rows. Public selection cannot inspect source
    or private branch: enumerate_schedule checks uniform availability over the
    whole current public-history fiber. No adaptive-policy synthesis is claimed.
    """
    source_id: str
    basis: str
    sources: tuple[Hashable, ...]
    states: tuple[Hashable, ...]
    epochs: Mapping[Hashable, int]
    events: tuple[Event, ...]
    preparation: tuple[tuple[Hashable, Hashable, Q], ...]
    kernels: Mapping[tuple[PublicHistory, str, Hashable, Hashable], tuple[Step, ...]]

    def validate(self):
        if (type(self.source_id) is not str or not self.source_id or type(self.basis) is not str
                or not self.basis or not self.sources or not self.states):
            raise NoGhostError("Explicit source ID, basis, sources and states required")
        if len(set(self.sources)) != len(self.sources) or len(set(self.states)) != len(self.states):
            raise NoGhostError("Repeated source or current-state label")
        if set(self.epochs) != set(self.states) or any(type(v) is not int or v < 0 for v in self.epochs.values()):
            raise NoGhostError("Total nonnegative integer state epochs required")
        ids = {e.occurrence for e in self.events}
        if len(ids) != len(self.events) or any(type(e.occurrence) is not str or not e.occurrence or not e.parents <= ids
                                             or e.occurrence in e.parents for e in self.events):
            raise NoGhostError("Malformed event occurrences/dependencies")
        # Kahn's algorithm excludes cycles, including those with no self-edge.
        seen = set()
        while True:
            new = {e.occurrence for e in self.events if e.parents <= seen}
            if new <= seen:
                break
            seen |= new
        if seen != ids:
            raise NoGhostError("Cyclic event dependencies")
        prepkeys = set()
        for s, c, p in self.preparation:
            if s not in self.sources or c not in self.states or exact(p) < 0 or (s, c) in prepkeys:
                raise NoGhostError("Malformed/duplicate source-current preparation atom")
            prepkeys.add((s, c))
        if sum((exact(p) for _, _, p in self.preparation), Q(0)) != 1:
            raise NoGhostError("Preparation must have total mass one")
        parents = {e.occurrence: e.parents for e in self.events}
        for (h, a, s, c), row in self.kernels.items():
            done = set()
            for occurrence, outcome in h:
                hash(outcome)
                if occurrence not in ids or occurrence in done or not parents[occurrence] <= done:
                    raise NoGhostError("Kernel public history violates event ancestry")
                done.add(occurrence)
            if a not in ids or a in done or not parents[a] <= done or s not in self.sources or c not in self.states:
                raise NoGhostError("Kernel row has invalid event/source/current index")
            branches = set()
            for step in row:
                key = (step.outcome, step.after, step.branch)
                if key in branches or step.after not in self.states or exact(step.probability) < 0:
                    raise NoGhostError("Malformed/duplicate private kernel atom")
                branches.add(key)
                if self.epochs[step.after] < self.epochs[c]:
                    raise NoGhostError("Epoch reversal is not a licensed reset")
            if sum((exact(e.probability) for e in row), Q(0)) != 1:
                raise NoGhostError("Enabled complete joint kernel row must sum to one")
        return self


@dataclass(frozen=True)
class Enumeration:
    status: str
    atoms: tuple[PossibleHistory, ...] = ()
    witness: tuple = ()
    reason: str = ""


def enumerate_schedule(model: FiniteContract, schedule: Sequence[str], *, max_atoms=100000) -> Enumeration:
    """Enumerate a fixed complete lawful schedule; no atom is labelled actual."""
    model.validate()
    schedule = tuple(schedule)
    if type(max_atoms) is not int or max_atoms < 0:
        raise NoGhostError("Nonnegative atom budget required")
    parents = {e.occurrence: e.parents for e in model.events}
    if len(schedule) != len(parents) or set(schedule) != set(parents):
        raise NoGhostError("Schedule must contain each declared occurrence exactly once")
    done = set()
    for a in schedule:
        if not parents[a] <= done:
            raise NoGhostError("Schedule is not a linear extension")
        done.add(a)
    atoms = tuple(PossibleHistory(s, c, c, (), exact(p), model.source_id, model.basis)
                  for s, c, p in model.preparation if p)
    if len(atoms) > max_atoms:
        return Enumeration("UNRESOLVED", reason="initial atom budget exhausted")
    for a in schedule:
        # Every supported hidden state must admit this public choice. Never
        # condition preparation on the hidden fact that an action was enabled.
        for atom in atoms:
            key = atom.public, a, atom.source, atom.current
            if key not in model.kernels:
                return Enumeration("SOURCE_INTERFACE_FAILURE", witness=key,
                                   reason="EXECUTABILITY_FAILURE: unavailable on a supported public-history fiber")
        expanded = []
        for atom in atoms:
            for step in model.kernels[(atom.public, a, atom.source, atom.current)]:
                if step.probability:
                    event = PrivateEvent(a, step.outcome, atom.current, step.after, step.branch)
                    expanded.append(PossibleHistory(atom.source, atom.initial, step.after,
                                                    atom.events+(event,), atom.mass*exact(step.probability),
                                                    model.source_id, model.basis))
                    if len(expanded) > max_atoms:
                        return Enumeration("UNRESOLVED", reason="private-history atom budget exhausted")
        atoms = tuple(expanded)
    assert sum((x.mass for x in atoms), Q(0)) == 1
    return Enumeration("LAWFUL_GLUING", atoms, reason="POSSIBLE fixed-schedule executions only")


def verify_unavailable(model: FiniteContract, schedule, witness) -> bool:
    """Replay positive private paths to independently confirm an access failure."""
    try:
        model.validate()
        schedule = tuple(schedule)
        parents = {e.occurrence: e.parents for e in model.events}
        if len(schedule) != len(parents) or set(schedule) != set(parents):
            return False
        done = set()
        for event in schedule:
            if not parents[event] <= done:
                return False
            done.add(event)
        h, a, source, state = witness
        if (h, a, source, state) in model.kernels or tuple(x for x, _ in h) != tuple(schedule[:len(h)]) or schedule[len(h)] != a:
            return False
        reachable = {(s, c) for s, c, p in model.preparation if p > 0}
        public = ()
        for event, outcome in h:
            reachable = {(s, step.after) for s, c in reachable
                         for step in model.kernels.get((public, event, s, c), ())
                         if step.probability > 0 and step.outcome == outcome}
            public += ((event, outcome),)
        return (source, state) in reachable
    except (NoGhostError, TypeError, ValueError, IndexError):
        return False


def verify_possible_history(model: FiniteContract, schedule, atom: PossibleHistory) -> bool:
    """Replay one private path AND its full public support; independent of enumeration.

    This verifies a positive possible execution and its exact mass, never that
    the execution was performed. Public enabledness is checked across all hidden
    states compatible with each observed prefix, not only this private path.
    """
    try:
        model.validate()
        schedule = tuple(schedule)
        if (atom.source_id, atom.basis) != (model.source_id, model.basis):
            return False
        parents = {e.occurrence: e.parents for e in model.events}
        if len(schedule) != len(parents) or set(schedule) != set(parents):
            return False
        if tuple(e.occurrence for e in atom.events) != schedule:
            return False
        prep = {(s, c): exact(p) for s, c, p in model.preparation}
        mass = prep.get((atom.source, atom.initial), Q(0))
        if mass <= 0:
            return False
        support = {(s, c) for (s, c), p in prep.items() if p > 0}
        current, public, done = atom.initial, (), set()
        for event in atom.events:
            a = event.occurrence
            if not parents[a] <= done or event.before != current:
                return False
            if any((public, a, s, c) not in model.kernels for s, c in support):
                return False
            row = model.kernels[(public, a, atom.source, current)]
            choices = [step for step in row if (step.outcome, step.after, step.branch)
                       == (event.outcome, event.after, event.branch) and step.probability > 0]
            if len(choices) != 1:
                return False
            mass *= exact(choices[0].probability)
            support = {(s, step.after) for s, c in support
                       for step in model.kernels[(public, a, s, c)]
                       if step.probability > 0 and step.outcome == event.outcome}
            current, public = event.after, public+((a, event.outcome),)
            done.add(a)
        return current == atom.current and exact(atom.mass) == mass
    except (NoGhostError, TypeError, ValueError, KeyError):
        return False


def joint_law(atoms: Sequence[PossibleHistory]):
    """Source x occurrence-labelled receipts x final current state (not paths)."""
    law = defaultdict(Q)
    for atom in atoms:
        law[(atom.source_id, atom.basis, atom.source,
             tuple(sorted(atom.public, key=lambda x: x[0])), atom.current)] += atom.mass
    return dict(law)


@dataclass(frozen=True)
class DiamondResult:
    status: str
    witness: tuple = ()
    reason: str = ""


def _two_event_law(model, h, a, b, s, c):
    first = model.kernels.get((h, a, s, c))
    if first is None:
        return None
    law = defaultdict(Q)
    for x in first:
        if not x.probability:
            continue
        second = model.kernels.get((h+((a, x.outcome),), b, s, x.after))
        if second is None:
            return None
        for y in second:
            if y.probability:
                labels = tuple(sorted(((a, x.outcome), (b, y.outcome))))
                law[(labels, y.after)] += exact(x.probability)*exact(y.probability)
    return dict(law)


def _validate_diamond_domain(model, h, a, b):
    parents = {e.occurrence: e.parents for e in model.events}
    done = set()
    for occurrence, outcome in h:
        hash(outcome)
        if occurrence not in parents or occurrence in done or not parents[occurrence] <= done:
            raise NoGhostError("Diamond prefix violates declared event ancestry")
        done.add(occurrence)
    if (a == b or a not in parents or b not in parents or a in done or b in done
            or not parents[a] <= done or not parents[b] <= done):
        raise NoGhostError("Diamond requires distinct independent declared next occurrences")


def check_diamond(model: FiniteContract, h: PublicHistory, a: str, b: str,
                  inputs: Sequence[tuple[Hashable, Hashable]]) -> DiamondResult:
    """All-Dirac complete-law diamond on an explicitly declared input fiber.

    Equality is exactly equality of source-indexed joint outcome/endpoint laws
    for every preparation supported on ``inputs``. Branch-path bijections and
    legal future menus require additional data and are NOT inferred.
    """
    model.validate()
    _validate_diamond_domain(model, h, a, b)
    if not inputs or len(set(inputs)) != len(inputs):
        raise NoGhostError("Distinct events and nonempty distinct Dirac inputs required")
    for s, c in inputs:
        if s not in model.sources or c not in model.states:
            raise NoGhostError("Dirac input outside source/current fiber")
        left, right = _two_event_law(model, h, a, b, s, c), _two_event_law(model, h, b, a, s, c)
        if left is None or right is None:
            return DiamondResult("SOURCE_INTERFACE_FAILURE", (s, c, a, b),
                                 "Two schedules are not both uniformly enabled at this Dirac input")
        for atom in set(left) | set(right):
            if left.get(atom, Q(0)) != right.get(atom, Q(0)):
                return DiamondResult("CAUSAL_DIAMOND_FAILURE",
                                     (s, c, a, b, atom, left.get(atom, Q(0)), right.get(atom, Q(0))),
                                     "Full labelled outcome/current kernel differs")
    return DiamondResult("LAWFUL_GLUING", reason="Distributional diamond only; no future-menu/private-path claim")


def verify_diamond_failure(model, h, witness) -> bool:
    try:
        model.validate()
        s, c, a, b, atom, p, q = witness
        _validate_diamond_domain(model, h, a, b)
        if s not in model.sources or c not in model.states or type(p) not in (int, Q) or type(q) not in (int, Q):
            return False
        left, right = _two_event_law(model, h, a, b, s, c), _two_event_law(model, h, b, a, s, c)
        return (left is not None and right is not None and p != q
                and left.get(atom, Q(0)) == p and right.get(atom, Q(0)) == q)
    except (NoGhostError, TypeError, ValueError):
        return False


@dataclass(frozen=True)
class CouplingProblem:
    """Restrictions supplied by caller; provenance of atoms is a separate gate."""
    atoms: tuple[Hashable, ...]
    restrictions: tuple[tuple[Hashable, ...], ...]
    local_laws: tuple[Mapping[Hashable, Q], ...]

    def equations(self):
        if len(set(self.atoms)) != len(self.atoms) or len(self.restrictions) != len(self.local_laws):
            raise NoGhostError("Distinct atoms and one law per restriction required")
        A, b = [(Q(1),)*len(self.atoms)], [Q(1)]
        for restriction, law in zip(self.restrictions, self.local_laws):
            if len(restriction) != len(self.atoms) or any(exact(v) < 0 for v in law.values()) or sum((exact(v) for v in law.values()), Q(0)) != 1:
                raise NoGhostError("Total restriction and normalized nonnegative local law required")
            labels = set(restriction) | set(law)
            for label in sorted(labels, key=repr):
                A.append(tuple(Q(int(x == label)) for x in restriction))
                b.append(exact(law.get(label, 0)))
        return tuple(A), tuple(b)


def couple_contexts(problem: CouplingProblem, *, max_bases=100000) -> LinearResult:
    """Find source-SUPPORTED coupling, not fixed-kernel operational realization."""
    A, b = problem.equations()
    return solve_nonnegative(A, b, max_bases=max_bases)


def event_context_problem(execution: Enumeration, contexts, local_laws, *, source_indexed=False):
    """Project a previously enumerated execution to selected recorded outcomes.

    A context label is the tuple of outcomes in the supplied occurrence order;
    with source_indexed=True it is (original source, outcome tuple). The source
    index is mathematical conditioning data, not a license to read hidden source.
    Contexts are observational restrictions; standalone execution of a restriction
    (especially one omitting ancestors) is not asserted.
    """
    if execution.status != "LAWFUL_GLUING" or not execution.atoms:
        raise NoGhostError("A complete nonempty enumerated execution is required")
    if type(source_indexed) is not bool:
        raise NoGhostError("source_indexed must be boolean")
    ids = set(dict(execution.atoms[0].public))
    restrictions = []
    for context in contexts:
        if len(set(context)) != len(context) or not set(context) <= ids:
            raise NoGhostError("Context must select distinct declared occurrence labels")
        labels = []
        for atom in execution.atoms:
            if set(dict(atom.public)) != ids:
                raise NoGhostError("All execution atoms must contain the same event configuration")
            outcomes = tuple(dict(atom.public)[a] for a in context)
            labels.append((atom.source, outcomes) if source_indexed else outcomes)
        restrictions.append(tuple(labels))
    return CouplingProblem(tuple(a.identity for a in execution.atoms), tuple(restrictions), tuple(local_laws))


def operational_equations(model: FiniteContract, schedule, atoms: Sequence[PossibleHistory]):
    """Exact source/private-prefix flow for a FIXED schedule and preparation.

    Given a verified complete atom set, every source/root mass is fixed and each
    private child has K(child|prefix) times its parent's mass. The unique leaf
    solution is the actual declared kernel product law. Sums allow many private
    continuations; public policy-flow constraints belong to a separate layer.
    """
    full = enumerate_schedule(model, schedule)
    if full.status != "LAWFUL_GLUING":
        raise NoGhostError("Operational contract is not fully enumerable and executable")
    identities = tuple(a.identity for a in atoms)
    if len(set(identities)) != len(identities) or set(identities) != {a.identity for a in full.atoms}:
        raise NoGhostError("Operational leaf set must be complete and source-backed")
    if any(not verify_possible_history(model, schedule, a) for a in atoms):
        raise NoGhostError("Operational atoms have forged current state, path or probability")
    A, b = [], []
    for source, initial, p in model.preparation:
        A.append(tuple(Q(int(a.source == source and a.initial == initial)) for a in atoms))
        b.append(exact(p))
    seen = set()
    for atom in atoms:
        for k, event in enumerate(atom.events):
            prefix = atom.source, atom.initial, atom.events[:k]
            child = atom.source, atom.initial, atom.events[:k+1]
            if child in seen:
                continue
            seen.add(child)
            public = tuple((e.occurrence, e.outcome) for e in atom.events[:k])
            row = model.kernels[(public, event.occurrence, atom.source, event.before)]
            probability = next(exact(s.probability) for s in row
                               if (s.outcome, s.after, s.branch) == (event.outcome, event.after, event.branch))
            A.append(tuple(Q(int((x.source, x.initial, x.events[:k+1]) == child))
                           - probability*Q(int((x.source, x.initial, x.events[:k]) == prefix)) for x in atoms))
            b.append(Q(0))
    return tuple(A), tuple(b)


def check_operational_weights(model, schedule, atoms, weights) -> bool:
    try:
        A, b = operational_equations(model, schedule, atoms)
        return verify_primal(A, b, weights)
    except NoGhostError:
        return False


@dataclass(frozen=True)
class Comparison:
    """Typed chosen bijection between complete private-history fibers."""
    before: tuple[str, ...]
    after: tuple[str, ...]
    mapping: tuple[int, ...]


def check_comparison(source_atoms, target_atoms, comparison: Comparison) -> bool:
    """Checks law, source, preparation, retained public evidence and endpoint.

    Branch tokens are allowed to change: this certifies a chosen private-history
    isomorphism, not identity of physical random draws. If tokens are externally
    retained named evidence they must instead be included among public outcomes.
    """
    if (len(comparison.mapping) != len(source_atoms) or len(target_atoms) != len(source_atoms)
            or any(type(i) is not int for i in comparison.mapping)
            or set(comparison.mapping) != set(range(len(target_atoms)))):
        return False
    for i, j in enumerate(comparison.mapping):
        x, y = source_atoms[i], target_atoms[j]
        if (not x.source_id or not x.basis or not y.source_id or not y.basis
                or tuple(e.occurrence for e in x.events) != comparison.before
                or tuple(e.occurrence for e in y.events) != comparison.after
                or (x.source_id, x.basis, x.source, x.initial, x.current, x.mass, tuple(sorted(x.public)))
                != (y.source_id, y.basis, y.source, y.initial, y.current, y.mass, tuple(sorted(y.public)))):
            return False
    return True


def compose_maps(*maps):
    """Apply finite bijections left to right; validate every output, including the last."""
    if not maps:
        raise NoGhostError("At least one comparison map required")
    width = len(maps[0])
    result = tuple(range(width))
    for mapping in maps:
        if (len(mapping) != width or any(type(i) is not int for i in mapping)
                or set(mapping) != set(range(width))):
            raise NoGhostError("Comparison must be a total exact-integer bijection of the typed fiber")
        result = tuple(mapping[i] for i in result)
    return result


def verify_higher_failure(left_maps, right_maps, witness: int) -> bool:
    """Verify discrepancy of valid finite bijections only.

    Physical/source lawfulness must be checked separately with model-backed
    fibers and check_comparison; this arithmetic certificate alone cannot do it.
    """
    try:
        left, right = compose_maps(*left_maps), compose_maps(*right_maps)
        return (len(left) == len(right) and type(witness) is int
                and 0 <= witness < len(left) and left[witness] != right[witness])
    except (NoGhostError, TypeError, IndexError):
        return False


def three_coin_experiment():
    """Lawful silent coin events with bad chosen CNOT swaps and good token swaps.

    All 6 schedules use one source, one state, and 3 independent fair internal
    bits. Every adjacent CNOT comparison is a weight/source/evidence/endpoint
    preserving involution on private histories. Nevertheless its braid fails.
    Physical token transposition provides a coherent family on the SAME model.
    This is failure of the chosen matchings, not nonexistence of coherent ones.
    """
    ids = ("a", "b", "c")
    kernels = {}
    for length in range(3):
        for prefix in permutations(ids, length):
            h = tuple((a, "tick") for a in prefix)
            for a in ids:
                if a not in prefix:
                    kernels[(h, a, "source", "ready")] = (
                        Step("tick", "ready", 0, Q(1, 2)), Step("tick", "ready", 1, Q(1, 2)))
    model = FiniteContract("NO_GHOST_THREE_COINS", "declared-private-bits", ("source",), ("ready",),
                           {"ready": 0}, tuple(Event(a) for a in ids), (("source", "ready", Q(1)),), kernels)
    fibers = {schedule: enumerate_schedule(model, schedule).atoms for schedule in permutations(ids)}

    def comparison(before, position, coherent):
        after = list(before)
        after[position], after[position+1] = after[position+1], after[position]
        after = tuple(after)
        index = {tuple(e.branch for e in atom.events): i for i, atom in enumerate(fibers[after])}
        mapping = []
        for atom in fibers[before]:
            bits = [e.branch for e in atom.events]
            if coherent:
                bits[position], bits[position+1] = bits[position+1], bits[position]
            else:
                bits[position+1] ^= bits[position]
            mapping.append(index[tuple(bits)])
        result = Comparison(before, after, tuple(mapping))
        assert check_comparison(fibers[before], fibers[after], result)
        return result

    paths = ((0, 1, 0), (1, 0, 1))
    outputs = {}
    for coherent in (False, True):
        maps = []
        for path in paths:
            before, pathmaps = ids, []
            for position in path:
                comp = comparison(before, position, coherent)
                pathmaps.append(comp.mapping)
                before = comp.after
            maps.append(tuple(pathmaps))
        left, right = (compose_maps(*p) for p in maps)
        failures = tuple(i for i in range(8) if left[i] != right[i])
        outputs["coherent" if coherent else "incoherent"] = {
            "left_maps": maps[0], "right_maps": maps[1], "left": left, "right": right,
            "failures": failures,
            "status": "HIGHER_COHERENCE_FAILURE" if failures else "LAWFUL_GLUING"}
    return model, fibers, outputs


@dataclass(frozen=True)
class RepairOption:
    """Already declared legal alternative equations, with externally audited cost.

    Solving a menu does not authenticate its legal transformations, introduce
    a sensor, or manufacture missing memory. Each option must carry its own
    model-relative law/transport certificate outside this finite optimizer.
    """
    name: str
    cost: Q
    A: tuple[tuple[Q, ...], ...]
    b: tuple[Q, ...]


@dataclass(frozen=True)
class RepairResult:
    status: str
    minimum_cost: Q | None = None
    options: tuple[str, ...] = ()
    results: tuple[tuple[str, LinearResult], ...] = ()
    reason: str = ""


def minimum_declared_repair(options: Sequence[RepairOption], *, budget, max_bases=100000):
    """Exact minimum over a finite DECLARED-LEGAL menu; no universal least repair."""
    budget = exact(budget)
    if budget < 0 or len({x.name for x in options}) != len(options):
        raise NoGhostError("Nonnegative budget and distinct repair names required")
    checked = []
    for option in options:
        cost = exact(option.cost)
        if cost < 0:
            raise NoGhostError("Repair cost cannot be negative")
        if cost <= budget:
            checked.append((option, solve_nonnegative(option.A, option.b, max_bases=max_bases)))
    feasible = [(o, r) for o, r in checked if r.status == "LAWFUL_GLUING"]
    unknown = [(o, r) for o, r in checked if r.status == "UNRESOLVED"]
    reports = tuple((o.name, r) for o, r in checked)
    if not feasible:
        return RepairResult("UNRESOLVED", results=reports,
                            reason=("bounded menu contains unresolved options" if unknown else
                                    "CERTIFIED_FINITE_MENU_EXHAUSTION: no legal in-budget option in the declared menu; broader repairs remain unresolved"))
    cost = min(exact(o.cost) for o, _ in feasible)
    if any(exact(o.cost) <= cost for o, _ in unknown):
        return RepairResult("UNRESOLVED", results=reports, reason="An equal/cheaper menu item is unresolved")
    return RepairResult("REPAIR_CERTIFIED", cost,
                        tuple(o.name for o, _ in feasible if exact(o.cost) == cost), reports,
                        "Minimum cost among declared legal in-budget options; tied options need not have a least refinement")
