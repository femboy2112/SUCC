"""Probabilistic crossover and delayed, source-changing observer evidence.

Exact finite rational mathematics. Conditional independence is an EXPLICIT
coupling hypothesis, never implied by different model names or two marginals.
Posterior confidence is conditional on the admitted model class, not a proof of
source ontology. Out-of-order delivery is buffered in the declared causal order.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from typing import Hashable, Mapping


class CouplingError(ValueError):
    pass


def rational(value) -> Q:
    if type(value) is int or type(value) is Q:
        return Q(value)
    raise CouplingError('Exact int/Fraction needed, not floating probabilities')


def distribution(values) -> tuple[Q, ...]:
    values = tuple(rational(v) for v in values)
    if not values or any(v < 0 for v in values) or sum(values, Q(0)) != 1:
        raise CouplingError('A full normalized nonnegative law is required')
    return values


@dataclass(frozen=True)
class Context:
    source: str
    version: int
    basis: str

    def __post_init__(self):
        if not self.source or not self.basis or type(self.version) is not int or self.version < 0:
            raise CouplingError('Source/version/basis required')


@dataclass(frozen=True)
class Marginal:
    context: Context
    variables: tuple[str, ...]
    rows: tuple[tuple[Hashable, ...], ...]
    weights: tuple[Q, ...]

    def __post_init__(self):
        if (not isinstance(self.context, Context) or not self.variables or
                len(set(self.variables)) != len(self.variables) or
                len(set(self.rows)) != len(self.rows) or len(self.rows) != len(self.weights) or
                any(len(r) != len(self.variables) for r in self.rows)):
            raise CouplingError('Malformed probability capsule')
        object.__setattr__(self, 'weights', distribution(self.weights))

    def project(self, variables: tuple[str, ...]) -> dict:
        if len(set(variables)) != len(variables) or set(variables)-set(self.variables):
            raise CouplingError('Projection to undeclared or duplicate variables')
        indices = [self.variables.index(v) for v in variables]
        ans = {}
        for row, w in zip(self.rows, self.weights):
            key = tuple(row[i] for i in indices)
            if w:
                ans[key] = ans.get(key, Q(0)) + w
        return ans

    def condition(self, likelihood: Mapping[tuple, Q], variables: tuple[str, ...]):
        support = self.project(variables)
        if set(support)-set(likelihood):
            raise CouplingError('Missing likelihood on supported source interface')
        li = {k: rational(v) for k, v in likelihood.items()}
        if any(v < 0 or v > 1 for v in li.values()):
            raise CouplingError('Likelihood must be between zero and one')
        idx = [self.variables.index(v) for v in variables]
        w = tuple(p * li.get(tuple(row[i] for i in idx), Q(0)) for row, p in zip(self.rows, self.weights))
        total = sum(w, Q(0))
        if not total:
            raise CouplingError('MISSPECIFIED: impossible evidence under source family')
        return Marginal(self.context, self.variables, self.rows, tuple(p/total for p in w))


def markov_amalgamate(left: Marginal, right: Marginal, *, assume_conditional_independence: bool = False) -> Marginal:
    """Glue on common coordinates Y as p(a,y,b)=p(a,y)p(y,b)/p(y).

    This is the unique coupling with the given marginals AND A independent B
    conditional on Y. It is not the unique coupling of the marginals alone.
    """
    if assume_conditional_independence is not True:
        raise CouplingError('Marginals do not determine a coupling; declare the CI hypothesis')
    if left.context != right.context:
        raise CouplingError('Cross-source crossover needs a verified source map')
    shared = tuple(v for v in left.variables if v in right.variables)
    if not shared:
        raise CouplingError('A declared common separator is required by this adapter')
    separator = left.project(shared)
    if separator != right.project(shared):
        raise CouplingError('Shared marginal mismatch: no joint source exists')
    li = tuple(left.variables.index(v) for v in shared)
    ri = tuple(right.variables.index(v) for v in shared)
    new = tuple(i for i, v in enumerate(right.variables) if v not in left.variables)
    variables = left.variables + tuple(right.variables[i] for i in new)
    rows, weights = [], []
    for x, px in zip(left.rows, left.weights):
        y = tuple(x[i] for i in li)
        for z, pz in zip(right.rows, right.weights):
            if px and pz and y == tuple(z[i] for i in ri):
                rows.append(x + tuple(z[i] for i in new))
                weights.append(px*pz/separator[y])
    result = Marginal(left.context, variables, tuple(rows), tuple(weights))
    if result.project(left.variables) != left.project(left.variables) or result.project(right.variables) != right.project(right.variables):
        raise AssertionError('Amalgamation failed to preserve parent marginals')
    return result


def separator_bayes_square(left: Marginal, right: Marginal, likelihood: Mapping[tuple, Q]) -> dict:
    shared = tuple(v for v in left.variables if v in right.variables)
    joint = markov_amalgamate(left, right, assume_conditional_independence=True)
    direct = joint.condition(likelihood, shared)
    staged = markov_amalgamate(left.condition(likelihood, shared), right.condition(likelihood, shared),
                              assume_conditional_independence=True)
    if direct.project(direct.variables) != staged.project(direct.variables):
        raise AssertionError('Bayes/Markov gluing naturality failed')
    return {'joint': joint, 'posterior': direct, 'staged': staged,
            'shared_evidence_count': 1, 'requires_CI': True}


def credal_target_interval(couplings: tuple[Marginal, ...], predicate) -> tuple[Q, Q]:
    """Exact extrema over a DECLARED finite convex hull of feasible couplings.

    This is not an automatic enumeration of all possible joint distributions.
    """
    if not couplings or len({(q.context, q.variables) for q in couplings}) != 1:
        raise CouplingError('One common source/interface per credal family')
    values = [sum((p for row, p in zip(q.rows, q.weights) if predicate(dict(zip(q.variables, row)))), Q(0))
              for q in couplings]
    return min(values), max(values)


@dataclass(frozen=True)
class StochasticAction:
    name: str
    outcomes: tuple[str, ...]
    transition: tuple[tuple[Q, ...], ...]
    emission: tuple[tuple[Q, ...], ...]

    def __post_init__(self):
        n = len(self.transition)
        if (not self.name or not self.outcomes or len(set(self.outcomes)) != len(self.outcomes) or
                not n or len(self.emission) != n or any(len(r) != n for r in self.transition) or
                any(len(r) != len(self.outcomes) for r in self.emission)):
            raise CouplingError('Full transition and post-state emission kernels required')
        object.__setattr__(self, 'transition', tuple(distribution(r) for r in self.transition))
        object.__setattr__(self, 'emission', tuple(distribution(r) for r in self.emission))


@dataclass(frozen=True)
class Hypothesis:
    name: str
    initial: tuple[Q, ...]
    actions: tuple[StochasticAction, ...]
    original_target: tuple[str, ...]

    def __post_init__(self):
        init = distribution(self.initial)
        object.__setattr__(self, 'initial', init)
        if (not self.name or not self.actions or len(self.original_target) != len(init) or
                len({a.name for a in self.actions}) != len(self.actions) or
                any(len(a.transition) != len(init) for a in self.actions)):
            raise CouplingError('Malformed evolving source hypothesis')

    def action(self, name):
        for a in self.actions:
            if a.name == name:
                return a
        raise CouplingError('Action outside hypothetical source contract')


@dataclass(frozen=True)
class CausalReceipt:
    event_id: str
    sequence: int
    context: Context
    action: str
    outcome: str

    def __post_init__(self):
        if not self.event_id or type(self.sequence) is not int or self.sequence < 0 or not self.action or not self.outcome:
            raise CouplingError('Receipt must identify event and causal sequence')


class EvolvingEvidence:
    """Joint posterior on (model, ORIGINAL source, CURRENT carrier).

    One declared causal event stream; network arrival order is not causal order.
    Parallel partially ordered streams would need extra commutation certificates.
    Model confidence never authenticates the simulator or source completeness.
    """
    def __init__(self, context: Context, models: tuple[Hypothesis, ...], prior: tuple[Q, ...]):
        prior = distribution(prior)
        if not models or len(models) != len(prior) or len({m.name for m in models}) != len(models):
            raise CouplingError('One weight per distinct candidate source model')
        signature = {(a.name, a.outcomes) for a in models[0].actions}
        if any({(a.name, a.outcomes) for a in m.actions} != signature for m in models):
            raise CouplingError('Compare model hypotheses only in a common experiment language')
        self.context, self.models = context, models
        self.joint = {(mi, s, s): pm*ps for mi, (m, pm) in enumerate(zip(models, prior))
                      for s, ps in enumerate(m.initial) if pm*ps}
        self.seen: dict[str, CausalReceipt] = {}
        self.pending: dict[int, CausalReceipt] = {}
        self.applied: list[CausalReceipt] = []
        self.predictive_probabilities: list[Q] = []

    def _step(self, law, receipt):
        new = {}
        for (mi, original, current), weight in law.items():
            action = self.models[mi].action(receipt.action)
            if receipt.outcome not in action.outcomes:
                raise CouplingError('Unsupported observed outcome')
            k = action.outcomes.index(receipt.outcome)
            for after, p in enumerate(action.transition[current]):
                value = weight*p*action.emission[after][k]
                if value:
                    key = (mi, original, after)
                    new[key] = new.get(key, Q(0)) + value
        total = sum(new.values(), Q(0))
        if not total:
            raise CouplingError('MISSPECIFIED: all remaining models reject the event')
        return {key: value/total for key, value in new.items()}, total

    def receive(self, record: CausalReceipt) -> dict:
        if record.context != self.context:
            raise CouplingError('Stale source/basis/version; rebase before using evidence')
        if record.event_id in self.seen:
            if self.seen[record.event_id] != record:
                raise CouplingError('An event identity was altered')
            return self.summary()
        if any(e.sequence == record.sequence for e in self.seen.values()):
            raise CouplingError('Conflicting events at one causal position')
        for m in self.models:
            if record.outcome not in m.action(record.action).outcomes:
                raise CouplingError('Malformed action/outcome before queueing')
        # Compute a transaction without mutating history on an impossible event.
        pending = dict(self.pending)
        pending[record.sequence] = record
        law, appended, probabilities = dict(self.joint), [], []
        next_seq = len(self.applied)
        while next_seq in pending:
            event = pending.pop(next_seq)
            law, prob = self._step(law, event)
            appended.append(event)
            probabilities.append(prob)
            next_seq += 1
        self.seen[record.event_id] = record
        self.pending, self.joint = pending, law
        self.applied.extend(appended)
        self.predictive_probabilities.extend(probabilities)
        return self.summary()

    def summary(self):
        targets = {}
        posterior = {m.name: Q(0) for m in self.models}
        for (mi, original, _), value in self.joint.items():
            t = self.models[mi].original_target[original]
            targets[t] = targets.get(t, Q(0)) + value
            posterior[self.models[mi].name] += value
        return {'model_posterior': posterior, 'original_target': targets,
                'applied': len(self.applied), 'buffered': len(self.pending),
                'status': 'MODEL_CONDITIONAL_NOT_A_FORMAL_SOURCE_PROOF',
                'source_authenticated': False, 'model_class_exhaustive': False}


@dataclass(frozen=True)
class FreshEvidenceContract:
    """Reject literal fitting/test reuse. This necessary check does NOT establish
    independence or remove distribution shift; source-conditioned laws remain
    a separate obligation for any statistical guarantee.
    """
    candidate_id: str
    context: Context
    fit_events: frozenset[str]

    def validate_test(self, events: tuple[CausalReceipt, ...]) -> bool:
        if not self.candidate_id or not events or len({e.event_id for e in events}) != len(events):
            raise CouplingError('Fresh distinct test events and candidate identity required')
        if any(e.context != self.context for e in events):
            raise CouplingError('Test source context changed')
        if self.fit_events & {e.event_id for e in events}:
            raise CouplingError('Adaptive-selection leakage: fitting evidence is not fresh testing')
        return True


def bridge_population(context: Context, left_values: tuple[str, ...], right_values: tuple[str, ...],
                      candidate_maps: tuple[tuple[str, ...], ...], prior: tuple[Q, ...], *, error_rate: Q) -> EvolvingEvidence:
    """Turn evolutionary bridge hypotheses into a source-conditional Bayes model.

    A `query:<left value>` action prepares that mathematical input and the
    hypothetical sensor returns the mapped right value with probability 1-error.
    Fresh sensor noise is CONDITIONALLY independent given the same latent bridge.
    The declared sensor is not an empirical calibration and the list may omit truth.
    This adapter ranks hypotheses; only a separate exact bridge verifier certifies.
    """
    error = rational(error_rate)
    n = len(left_values)
    if (n < 2 or n != len(right_values) or len(set(left_values)) != n or len(set(right_values)) != n or
            not candidate_maps or len(set(candidate_maps)) != len(candidate_maps) or not 0 <= error < 1 or
            any(len(m) != n or set(m) != set(right_values) for m in candidate_maps)):
        raise CouplingError('Distinct typed bijections and declared sensor error required')
    models = []
    for mi, mapping in enumerate(candidate_maps):
        emission = tuple(tuple(1-error if y == mapping[x] else error/(n-1) for y in right_values) for x in range(n))
        actions = tuple(StochasticAction('query:'+label, right_values,
                         tuple(tuple(Q(int(j == x)) for j in range(n)) for _ in range(n)), emission)
                        for x, label in enumerate(left_values))
        name = 'bridge:'+str(mi)
        models.append(Hypothesis(name, (Q(1),)+(Q(0),)*(n-1), actions, (name,)*n))
    return EvolvingEvidence(context, tuple(models), prior)
