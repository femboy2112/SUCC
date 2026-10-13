"""Exact finite source-changing probability objects for SWM-C17--C24.

An instrument is a JOINT kernel P(report, after | before). Histories retain
P(original, current | actual public history); a current marginal cannot replace
that law. All source identities here are declared mathematical contracts, not
physical attestations. No probabilities are inferred from possibility support.

Classical finite-kernel, Bayes, Blackwell and finite-horizon control mathematics.
The small exact feasibility enumerator deliberately raises on budget exhaustion.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb
from typing import Hashable


class ProbabilityError(ValueError):
    pass


class SearchBudgetError(ProbabilityError):
    """An incomplete search is never an infeasibility certificate."""


def rational(value):
    if type(value) is int or type(value) is Q:
        return Q(value)
    raise ProbabilityError("Require exact int/Fraction, never float or bool")


def distribution(values):
    result = tuple(rational(v) for v in values)
    if not result or any(v < 0 for v in result) or sum(result, Q(0)) != 1:
        raise ProbabilityError("Require a normalized nonnegative finite law")
    return result


def _label(value):
    try:
        hash(value)
    except TypeError as error:
        raise ProbabilityError("Immutable hashable report labels required") from error


@dataclass(frozen=True)
class StochasticInstrument:
    name: str
    source_id: str
    input_space: str
    output_space: str
    after_count: int
    rows: tuple[tuple[tuple[Hashable, int, Q], ...], ...]
    cost: Q = Q(1)

    def __post_init__(self):
        if any(type(x) is not str or not x for x in
               (self.name, self.source_id, self.input_space, self.output_space)):
            raise ProbabilityError("Declared source and carrier spaces required")
        if type(self.after_count) is not int or self.after_count <= 0 or not self.rows:
            raise ProbabilityError("Nonempty finite before and after carriers required")
        canonical = []
        for row in self.rows:
            weights = {}
            for report, after, value in row:
                _label(report)
                if type(after) is not int or not 0 <= after < self.after_count:
                    raise ProbabilityError("Post-state outside declared carrier")
                probability = rational(value)
                if probability < 0:
                    raise ProbabilityError("Negative kernel weight")
                key = (report, after)
                weights[key] = weights.get(key, Q(0)) + probability
            if sum(weights.values(), Q(0)) != 1:
                raise ProbabilityError("Every joint instrument row must normalize")
            canonical.append(tuple((r, y, p) for (r, y), p in weights.items() if p))
        cost = rational(self.cost)
        if cost < 0:
            raise ProbabilityError("Nonnegative finite instrument cost required")
        object.__setattr__(self, "rows", tuple(canonical))
        object.__setattr__(self, "cost", cost)

    @property
    def before_count(self):
        return len(self.rows)

    @property
    def outcomes(self):
        return tuple(dict.fromkeys(r for row in self.rows for r, _, _ in row))


def compose(first: StochasticInstrument, second: StochasticInstrument):
    """Sequential reports remain ordered pairs, including carrier backaction."""
    if (first.source_id != second.source_id or
            first.output_space != second.input_space or
            first.after_count != second.before_count):
        raise ProbabilityError("Composition requires a typed common actual carrier")
    rows = []
    for row in first.rows:
        weights = {}
        for a, middle, p in row:
            for b, after, q in second.rows[middle]:
                key = ((a, b), after)
                weights[key] = weights.get(key, Q(0)) + p*q
        rows.append(tuple((r, y, p) for (r, y), p in weights.items()))
    return StochasticInstrument(first.name+";"+second.name, first.source_id,
                               first.input_space, second.output_space,
                               second.after_count, tuple(rows), first.cost+second.cost)


def _joint(values):
    result = tuple(tuple(rational(v) for v in row) for row in values)
    if (not result or not result[0] or any(len(row) != len(result[0]) for row in result)
            or any(v < 0 for row in result for v in row)
            or sum((sum(row, Q(0)) for row in result), Q(0)) != 1):
        raise ProbabilityError("Require normalized joint original/current law")
    return result


def _update(joint, instrument, outcome):
    if len(joint[0]) != instrument.before_count:
        raise ProbabilityError("History/instrument carrier size mismatch")
    new = [[Q(0)]*instrument.after_count for _ in joint]
    for original, row in enumerate(joint):
        for before, weight in enumerate(row):
            for report, after, p in instrument.rows[before]:
                if report == outcome:
                    new[original][after] += weight*p
    prob = sum((sum(row, Q(0)) for row in new), Q(0))
    if not prob:
        return Q(0), None
    return prob, tuple(tuple(v/prob for v in row) for row in new)


@dataclass(frozen=True)
class ProbabilityEvent:
    instrument: str
    outcome: Hashable
    conditional_probability: Q


@dataclass(frozen=True)
class StochasticHistory:
    source_id: str
    initial_space: str
    current_space: str
    initial_joint: tuple[tuple[Q, ...], ...]
    joint: tuple[tuple[Q, ...], ...]
    events: tuple[ProbabilityEvent, ...] = ()
    path_probability: Q = Q(1)

    def __post_init__(self):
        if any(type(x) is not str or not x for x in
               (self.source_id, self.initial_space, self.current_space)):
            raise ProbabilityError("Declared original/current source types required")
        initial, joint = _joint(self.initial_joint), _joint(self.joint)
        if len(initial) != len(joint) or type(self.events) is not tuple:
            raise ProbabilityError("Original state labels and immutable events required")
        path = rational(self.path_probability)
        if not 0 < path <= 1 or any(type(e) is not ProbabilityEvent for e in self.events):
            raise ProbabilityError("Malformed actual event history")
        if any(not 0 < rational(e.conditional_probability) <= 1 for e in self.events):
            raise ProbabilityError("Actual outcomes need positive conditional probabilities")
        object.__setattr__(self, "initial_joint", initial)
        object.__setattr__(self, "joint", joint)
        object.__setattr__(self, "path_probability", path)

    @classmethod
    def from_joint(cls, source_id, carrier_space, joint):
        law = _joint(joint)
        return cls(source_id, carrier_space, carrier_space, law, law)

    @classmethod
    def original(cls, source_id, carrier_space, prior):
        prior = distribution(prior)
        return cls.from_joint(source_id, carrier_space,
                             tuple(tuple(p if i == j else Q(0)
                                         for j in range(len(prior)))
                                   for i, p in enumerate(prior)))

    @property
    def original_posterior(self):
        return tuple(sum(row, Q(0)) for row in self.joint)

    @property
    def current_posterior(self):
        return tuple(sum((row[j] for row in self.joint), Q(0))
                     for j in range(len(self.joint[0])))

    def advance(self, instrument, outcome):
        if (instrument.source_id != self.source_id or
                instrument.input_space != self.current_space):
            raise ProbabilityError("Stale/cross-source instrument requires a verified map")
        prob, new = _update(self.joint, instrument, outcome)
        if not prob:
            raise ProbabilityError("Impossible event cannot be appended")
        return StochasticHistory(self.source_id, self.initial_space,
                                 instrument.output_space, self.initial_joint, new,
                                 self.events+(ProbabilityEvent(instrument.name, outcome, prob),),
                                 self.path_probability*prob)

    def verify(self, registry):
        replay = StochasticHistory.from_joint(self.source_id, self.initial_space,
                                             self.initial_joint)
        for event in self.events:
            if event.instrument not in registry:
                raise ProbabilityError("Missing instrument provenance for replay")
            replay = replay.advance(registry[event.instrument], event.outcome)
        if replay != self:
            raise ProbabilityError("Stored joint law/history differs from exact replay")
        return True


@dataclass(frozen=True)
class LawDescent:
    descends: bool
    witness: tuple[int, int] | None
    report_laws: tuple[tuple[Q, ...], ...]
    atoms: tuple[tuple[Hashable, Hashable], ...]
    refinement: tuple[tuple[Hashable, tuple[Q, ...]], ...]


def law_descent(instrument, before_report, after_report):
    """Exact iff for descent of P(public outcome, next report | source state)."""
    before_report, after_report = tuple(before_report), tuple(after_report)
    if (len(before_report) != instrument.before_count or
            len(after_report) != instrument.after_count):
        raise ProbabilityError("Complete before/after reports required")
    for report in before_report+after_report:
        _label(report)
    atoms = tuple(dict.fromkeys((r, after_report[y])
                               for row in instrument.rows for r, y, _ in row))
    laws = []
    for row in instrument.rows:
        law = {a: Q(0) for a in atoms}
        for report, y, p in row:
            law[(report, after_report[y])] += p
        laws.append(tuple(law[a] for a in atoms))
    witness = next(((i, j) for i in range(len(laws)) for j in range(i)
                    if before_report[i] == before_report[j] and laws[i] != laws[j]), None)
    return LawDescent(witness is None, witness, tuple(laws), atoms,
                      tuple(zip(before_report, laws)))


def conditional_product(separator, left, right):
    """P(z,a,b)=P(z)P(a|z)P(b|z): CI is an INPUT, not inferred."""
    separator = distribution(separator)
    left, right = tuple(distribution(r) for r in left), tuple(distribution(r) for r in right)
    if (len(left) != len(separator) or len(right) != len(separator) or
            len({len(r) for r in left}) != 1 or len({len(r) for r in right}) != 1):
        raise ProbabilityError("Full common separator and conditional kernels required")
    return tuple(tuple(tuple(p*a*b for b in right[z]) for a in left[z])
                 for z, p in enumerate(separator))


def bayes_product_square(separator, left, right, left_likelihood, right_likelihood):
    """Update once by u(z,a)v(z,b), then compare reconstructed CI factors.

    Local normalizers must be used to update the COMMON separator. Updating
    each marginal independently and ignoring its changed separator is unsound.
    """
    base = conditional_product(separator, left, right)
    u = tuple(tuple(rational(v) for v in row) for row in left_likelihood)
    v = tuple(tuple(rational(w) for w in row) for row in right_likelihood)
    if (len(u) != len(base) or len(v) != len(base) or
            any(len(u[z]) != len(base[z]) or len(v[z]) != len(base[z][0])
                for z in range(len(base))) or
            any(not 0 <= w <= 1 for row in u+v for w in row)):
        raise ProbabilityError("Likelihood factors must have full typed shapes in [0,1]")
    weighted = tuple(tuple(tuple(p*u[z][a]*v[z][b] for b, p in enumerate(row))
                           for a, row in enumerate(slab)) for z, slab in enumerate(base))
    total = sum((p for slab in weighted for row in slab for p in row), Q(0))
    if not total:
        raise ProbabilityError("Bayes undefined on impossible evidence")
    direct = tuple(tuple(tuple(p/total for p in row) for row in slab) for slab in weighted)
    za = tuple(sum((rational(p)*w for p, w in zip(left[z], u[z])), Q(0))
               for z in range(len(base)))
    zb = tuple(sum((rational(p)*w for p, w in zip(right[z], v[z])), Q(0))
               for z in range(len(base)))
    posterior_z = tuple(rational(p)*za[z]*zb[z]/total for z, p in enumerate(separator))
    # Zero-mass conditional fibers have arbitrary normalized representatives.
    la = tuple(tuple(rational(p)*w/za[z] for p, w in zip(left[z], u[z]))
               if za[z] else distribution(left[z]) for z in range(len(base)))
    rb = tuple(tuple(rational(p)*w/zb[z] for p, w in zip(right[z], v[z]))
               if zb[z] else distribution(right[z]) for z in range(len(base)))
    staged = conditional_product(posterior_z, la, rb)
    if staged != direct:
        raise ArithmeticError("Exact factorized Bayes/CI product square failed")
    return direct, staged


@dataclass(frozen=True)
class Experiment:
    source_id: str
    rows: tuple[tuple[Q, ...], ...]

    def __post_init__(self):
        rows = tuple(distribution(row) for row in self.rows)
        if (type(self.source_id) is not str or not self.source_id or not rows or
                len({len(row) for row in rows}) != 1):
            raise ProbabilityError("Common source and complete signal laws required")
        object.__setattr__(self, "rows", rows)


def garbling_verifies(more, less, channel):
    if more.source_id != less.source_id or len(more.rows) != len(less.rows):
        raise ProbabilityError("Experiments must share original source labels")
    channel = tuple(distribution(row) for row in channel)
    if len(channel) != len(more.rows[0]) or any(len(row) != len(less.rows[0]) for row in channel):
        raise ProbabilityError("Garbling has incompatible signal alphabets")
    return all(sum((p*channel[i][j] for i, p in enumerate(row)), Q(0)) == less.rows[s][j]
               for s, row in enumerate(more.rows) for j in range(len(less.rows[0])))


def _rref(coefficients, rhs):
    """Independent exact row reduction; return pivots and augmented matrix."""
    matrix = [list(map(Q, row))+[Q(b)] for row, b in zip(coefficients, rhs)]
    width = len(coefficients[0])
    pivots, next_row = [], 0
    for column in range(width):
        index = next((i for i in range(next_row, len(matrix)) if matrix[i][column]), None)
        if index is None:
            continue
        matrix[next_row], matrix[index] = matrix[index], matrix[next_row]
        scale = matrix[next_row][column]
        matrix[next_row] = [v/scale for v in matrix[next_row]]
        for i in range(len(matrix)):
            if i != next_row and matrix[i][column]:
                scale = matrix[i][column]
                matrix[i] = [v-scale*w for v, w in zip(matrix[i], matrix[next_row])]
        pivots.append(column)
        next_row += 1
        if next_row == len(matrix):
            break
    inconsistent = any(not any(row[:-1]) and row[-1] for row in matrix)
    return pivots, matrix, inconsistent


def find_garbling(more, less, *, max_bases=20000):
    """Necessary/sufficient finite exact feasibility by exhaustive BFS vertices.

    Return a source-independent rational channel, or None ONLY after exhaustive
    infeasibility. This is exponential and deliberately intended for tiny models.
    """
    if more.source_id != less.source_id or len(more.rows) != len(less.rows):
        raise ProbabilityError("Experiments must share original source labels")
    if type(max_bases) is not int or max_bases < 1:
        raise ProbabilityError("Positive exact enumeration budget required")
    m, n = len(more.rows[0]), len(less.rows[0])
    equations, rhs = [], []
    for i in range(m):
        equations.append(tuple(Q(int(k//n == i)) for k in range(m*n)))
        rhs.append(Q(1))
    for source, row in enumerate(more.rows):
        for j in range(n):
            equations.append(tuple(row[k//n] if k % n == j else Q(0) for k in range(m*n)))
            rhs.append(less.rows[source][j])
    pivots, _, impossible = _rref(equations, rhs)
    if impossible:
        return None
    rank = len(pivots)
    if comb(m*n, rank) > max_bases:
        raise SearchBudgetError("Garbling basis enumeration exceeds declared budget")
    for columns in combinations(range(m*n), rank):
        restricted = [tuple(row[c] for c in columns) for row in equations]
        ps, reduced, inconsistent = _rref(restricted, rhs)
        if inconsistent or len(ps) != rank:
            continue
        solution = [Q(0)]*(m*n)
        for i, column in enumerate(ps):
            solution[columns[column]] = reduced[i][-1]
        if any(v < 0 for v in solution):
            continue
        channel = tuple(tuple(solution[i*n+j] for j in range(n)) for i in range(m))
        if not garbling_verifies(more, less, channel):
            raise ArithmeticError("Exact feasibility candidate failed independent channel check")
        return channel
    return None


@dataclass(frozen=True)
class PolicyResult:
    cost: Q | None
    action: str | None
    examined: int
    horizon: int


def optimal_zero_error_cost(history, instruments, target, horizon, *, max_nodes=100000):
    """Least EXPECTED cost among deterministic policies finishing by horizon.

    Every positive-probability branch must certify the original target. Prior
    zero atoms are excluded; this is not a source-universal proof on those atoms.
    All instruments are total on the declared finite carrier. No reset is added.
    """
    target, instruments = tuple(target), tuple(instruments)
    if len(target) != len(history.joint) or type(horizon) is not int or not 0 <= horizon <= 20:
        raise ProbabilityError("Full original targets and finite horizon 0..20 required")
    if type(max_nodes) is not int or max_nodes < 1 or len({a.name for a in instruments}) != len(instruments):
        raise ProbabilityError("Distinct actions and positive recursion budget required")
    for value in target:
        _label(value)
    if any(a.source_id != history.source_id for a in instruments):
        raise ProbabilityError("Policy menu contains a cross-source instrument")
    examined = 0

    @lru_cache(None)
    def solve(joint, space, depth):
        nonlocal examined
        examined += 1
        if examined > max_nodes:
            raise SearchBudgetError("Policy search exceeds declared state budget")
        labels = {target[i] for i, row in enumerate(joint) if sum(row, Q(0))}
        if len(labels) == 1:
            return Q(0), None
        if depth == 0:
            return None, None
        candidates = []
        for instrument in instruments:
            if instrument.input_space != space or instrument.before_count != len(joint[0]):
                continue
            expected, feasible = instrument.cost, True
            for outcome in instrument.outcomes:
                p, child = _update(joint, instrument, outcome)
                if not p:
                    continue
                value, _ = solve(child, instrument.output_space, depth-1)
                if value is None:
                    feasible = False
                    break
                expected += p*value
            if feasible:
                candidates.append((expected, instrument.name))
        return min(candidates) if candidates else (None, None)

    cost, action = solve(history.joint, history.current_space, horizon)
    return PolicyResult(cost, action, examined, horizon)


def commutation_defect(first, second):
    """Full outcome-subkernel commutation, not just equal terminal marginals."""
    if (first.input_space != first.output_space or second.input_space != second.output_space
            or first.input_space != second.input_space):
        raise ProbabilityError("Concurrent square needs a common unchanged carrier type")
    ab, ba = compose(first, second), compose(second, first)
    for state in range(ab.before_count):
        forward = {(a, b, y): p for (a, b), y, p in ab.rows[state]}
        reverse = {(a, b, y): p for (b, a), y, p in ba.rows[state]}
        for atom in dict.fromkeys(tuple(forward)+tuple(reverse)):
            if forward.get(atom, Q(0)) != reverse.get(atom, Q(0)):
                return state, atom, forward.get(atom, Q(0)), reverse.get(atom, Q(0))
    return None


def causal_ville_audit(null, alternative, instruments, policy, horizon, threshold):
    """Exact path-conditioned LR audit on a predictable finite action tree.

    Null/alternative share the SAME source instrument contract but can have
    different initial laws. Each history is filtered separately. Absolute
    continuity is checked before any likelihood ratio update.
    """
    threshold = rational(threshold)
    if threshold <= 1 or type(horizon) is not int or not 0 <= horizon <= 12:
        raise ProbabilityError("Threshold >1 and exact horizon 0..12 required")
    registry = {a.name: a for a in instruments}
    if len(registry) != len(instruments):
        raise ProbabilityError("Unique instrument names required")
    examined = 0

    def visit(h0, h1, public, wealth, probability, depth, crossed):
        nonlocal examined
        examined += 1
        crossed = crossed or wealth >= threshold
        if depth == horizon or h1 is None:
            return probability*wealth, probability if crossed else Q(0)
        name = policy(public)
        if name not in registry:
            raise ProbabilityError("Public policy chose undeclared instrument")
        action = registry[name]
        if (action.source_id != h0.source_id or action.input_space != h0.current_space or
                h1.source_id != h0.source_id or h1.current_space != h0.current_space):
            raise ProbabilityError("Null/alternative actions require a common causal type")
        branches = []
        for outcome in action.outcomes:
            p0, _ = _update(h0.joint, action, outcome)
            p1, _ = _update(h1.joint, action, outcome)
            if p1 and not p0:
                raise ProbabilityError("Alternative not absolutely continuous at this history")
            if p0:
                next1 = h1.advance(action, outcome) if p1 else None
                branches.append(visit(h0.advance(action, outcome), next1,
                                      public+((name, outcome),), wealth*p1/p0,
                                      probability*p0, depth+1, crossed))
        return tuple(sum((b[j] for b in branches), Q(0)) for j in range(2))

    expectation, crossing = visit(null, alternative, (), Q(1), Q(1), 0, False)
    if expectation != 1 or crossing > 1/threshold:
        raise ArithmeticError("Calibrated exact likelihood-ratio/Ville audit failed")
    return {"expectation": expectation, "crossing_probability": crossing,
            "ville_bound": 1/threshold, "nodes": examined}


def reversible_memory_lift(update):
    """Sharp worst-case cardinal bound for an injective lift x -> (f(x),m(x))."""
    update = tuple(update)
    if not update:
        raise ProbabilityError("Nonempty finite source map required")
    fibers, lift = {}, []
    for after in update:
        _label(after)
        memory = fibers.get(after, 0)
        fibers[after] = memory+1
        lift.append((after, memory))
    if len(set(lift)) != len(update):
        raise ArithmeticError("Constructed reversible source/memory lift is not injective")
    return max(fibers.values()), tuple(lift)


# Finite real rational CP submodel; no complex quantum/physical attestation claim.
def _matrix(values):
    result = tuple(tuple(rational(v) for v in row) for row in values)
    if not result or not result[0] or len({len(row) for row in result}) != 1:
        raise ProbabilityError("Nonempty rectangular exact matrix required")
    return result


def _transpose(matrix):
    return tuple(zip(*matrix))


def _matmul(left, right):
    if len(left[0]) != len(right):
        raise ProbabilityError("Incompatible matrix dimensions")
    return tuple(tuple(sum((left[i][k]*right[k][j] for k in range(len(right))), Q(0))
                       for j in range(len(right[0]))) for i in range(len(left)))


def _matsum(matrices, count):
    return tuple(tuple(sum((m[i][j] for m in matrices), Q(0))
                       for j in range(count)) for i in range(count))


def _determinant(matrix):
    remaining = [list(row) for row in matrix]
    value = Q(1)
    for column in range(len(matrix)):
        pivot = next((i for i in range(column, len(matrix)) if remaining[i][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            remaining[column], remaining[pivot] = remaining[pivot], remaining[column]
            value = -value
        scale = remaining[column][column]
        value *= scale
        for i in range(column+1, len(matrix)):
            factor = remaining[i][column]/scale
            remaining[i] = [x-factor*y for x, y in zip(remaining[i], remaining[column])]
    return value


def density(values):
    matrix = _matrix(values)
    n = len(matrix)
    if n > 4 or any(len(row) != n for row in matrix) or _transpose(matrix) != matrix:
        raise ProbabilityError("Real symmetric density dimension 1..4 required")
    if sum((matrix[i][i] for i in range(n)), Q(0)) != 1:
        raise ProbabilityError("Density must have trace one")
    for k in range(1, n+1):
        for indices in combinations(range(n), k):
            minor = tuple(tuple(matrix[i][j] for j in indices) for i in indices)
            if _determinant(minor) < 0:
                raise ProbabilityError("Density must be PSD (all principal minors)")
    return matrix


@dataclass(frozen=True)
class CPInstrument:
    """Any finite Kraus multiplicity per outcome, rectangular real matrices."""
    name: str
    operators: tuple[tuple[Hashable, tuple[tuple[tuple[Q, ...], ...], ...]], ...]

    def __post_init__(self):
        if type(self.name) is not str or not self.name or not self.operators:
            raise ProbabilityError("Nonempty named CP instrument required")
        labels, groups = set(), []
        for outcome, raw in self.operators:
            _label(outcome)
            if outcome in labels or not raw:
                raise ProbabilityError("Distinct outcomes with nonempty Kraus families required")
            labels.add(outcome)
            groups.append((outcome, tuple(_matrix(k) for k in raw)))
        shapes = {(len(k), len(k[0])) for _, family in groups for k in family}
        if len(shapes) != 1:
            raise ProbabilityError("Common input/output dimensions required")
        out_count, in_count = next(iter(shapes))
        if max(out_count, in_count) > 4:
            raise ProbabilityError("Exact real CP instrument dimension at most four")
        complete = _matsum(tuple(_matmul(_transpose(k), k)
                                 for _, family in groups for k in family), in_count)
        identity = tuple(tuple(Q(int(i == j)) for j in range(in_count)) for i in range(in_count))
        if complete != identity:
            raise ProbabilityError("CP instrument must satisfy sum K^T K = identity")
        object.__setattr__(self, "operators", tuple(groups))

    def unnormalized(self, rho, outcome):
        rho = density(rho)
        families = dict(self.operators)
        if outcome not in families:
            raise ProbabilityError("Outcome outside declared CP instrument")
        family = families[outcome]
        if len(rho) != len(family[0][0]):
            raise ProbabilityError("Density/CP input dimensions differ")
        return _matsum(tuple(_matmul(_matmul(k, rho), _transpose(k)) for k in family),
                       len(family[0]))

    def event(self, rho, outcome):
        unnormalized = self.unnormalized(rho, outcome)
        p = sum((unnormalized[i][i] for i in range(len(unnormalized))), Q(0))
        if not p:
            raise ProbabilityError("Impossible CP outcome")
        return p, density(tuple(tuple(v/p for v in row) for row in unnormalized))


def compose_cp(first, second):
    groups = []
    for r, ks in first.operators:
        for s, ls in second.operators:
            groups.append(((r, s), tuple(_matmul(l, k) for k in ks for l in ls)))
    return CPInstrument(first.name+";"+second.name, tuple(groups))
