"""Carrier-relative finite experiment realization and statistical certainty limits.

CLASSICAL conditional probability/Le Cam arguments with EXACT Fraction tables.
An internal response-history simulator reproduces every adaptive policy on
its DECLARED finite-horizon nonanticipatory response kernel, but this neither
validates that kernel empirically nor proves any claim about ontology.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from typing import Hashable, Mapping


class StatisticalFrontierError(ValueError):
    """False source law, noncausal or missing response kernel, or policy fault."""


def rat(x: object) -> F:
    if type(x) in (int, F):
        return F(x)
    raise StatisticalFrontierError("Probabilities must be exact rational numbers")


def _row(values: tuple[F, ...]) -> tuple[F, ...]:
    row = tuple(rat(x) for x in values)
    if not row or any(x < 0 for x in row) or sum(row, F(0)) != 1:
        raise StatisticalFrontierError("A response row must be an exact probability law")
    return row


@dataclass(frozen=True)
class ExperimentPair:
    """Two exact possible laws of the same ONE finite public experiment."""
    source_id: str
    outcomes: tuple[Hashable, ...]
    internal: tuple[F, ...]
    external: tuple[F, ...]

    def __post_init__(self) -> None:
        if not self.source_id or not self.outcomes or len(set(self.outcomes)) != len(self.outcomes):
            raise StatisticalFrontierError("One declared source and distinct outcomes required")
        if len(self.outcomes) != len(self.internal) or len(self.outcomes) != len(self.external):
            raise StatisticalFrontierError("Mismatched experiment outcomes")
        object.__setattr__(self, "internal", _row(self.internal))
        object.__setattr__(self, "external", _row(self.external))

    @property
    def total_variation(self) -> F:
        return sum((abs(x-y) for x, y in zip(self.internal, self.external)), F(0))/2

    @property
    def equal_prior_risk(self) -> F:
        """Minimum equal-prior Bayes classification error=(1-TV)/2."""
        return sum((min(x, y) for x, y in zip(self.internal, self.external)), F(0))/2

    @property
    def certainty_possible(self) -> bool:
        """Single-shot ZERO-ERROR identification possible iff disjoint support."""
        return self.equal_prior_risk == 0

    def push(self, public_outcomes: tuple[Hashable,...],
             rows: tuple[tuple[F,...],...], *, name: str) -> "ExperimentPair":
        """Apply the SAME observer Markov kernel to both hypotheses.

        Total variation cannot grow; the optimal Bayesian ontology error
        cannot decrease under this lossy observer change. This is classical
        data processing, NOT evidence that either hypothesis is true.
        """
        if not public_outcomes or len(set(public_outcomes)) != len(public_outcomes):
            raise StatisticalFrontierError("Nonempty distinct public outcome labels required")
        if len(rows)!=len(self.outcomes) or not name:
            raise StatisticalFrontierError("One shared Markov row per actual outcome")
        mat=tuple(_row(tuple(row)) for row in rows)
        if any(len(row)!=len(public_outcomes) for row in mat):
            raise StatisticalFrontierError("Wrong stochastic kernel output width")
        new_p=tuple(sum((self.internal[i]*mat[i][j]
                         for i in range(len(self.outcomes))),F(0))
                    for j in range(len(public_outcomes)))
        new_q=tuple(sum((self.external[i]*mat[i][j]
                         for i in range(len(self.outcomes))),F(0))
                    for j in range(len(public_outcomes)))
        result=ExperimentPair(self.source_id+":observer="+name, public_outcomes,new_p,new_q)
        if result.total_variation>self.total_variation or result.equal_prior_risk<self.equal_prior_risk:
            raise AssertionError("Classical statistical data processing violated")
        return result

    def independent_product_risk(self, n: int, *, max_sequences: int = 100000) -> F:
        """Exact binary testing risk for n iid copies; independence is a premise."""
        if type(n) is not int or n < 1 or len(self.outcomes)**n > max_sequences:
            raise StatisticalFrontierError("Invalid iid horizon or exhaustive resource limit")
        overlap = F(0)
        for word in product(range(len(self.outcomes)), repeat=n):
            p, q = F(1), F(1)
            for i in word:
                p *= self.internal[i]
                q *= self.external[i]
            overlap += min(p, q)
        return overlap/2

    def iid_chebyshev_error_upper(self, n: int) -> F:
        """Constructive error bound using a separating outcome and sample mean.

        With an outcome event of probability gap d>0, threshold midpoint
        distinguishes hypotheses with each error <=1/(n*d*d), by Var<=1/4.
        If p=q no such bound exists and the task is observationally dark.
        """
        if type(n) is not int or n < 1:
            raise StatisticalFrontierError("Positive integer sample horizon required")
        gap = max(abs(a-b) for a, b in zip(self.internal, self.external))
        if gap == 0:
            raise StatisticalFrontierError("No distinguishing outcome under these laws")
        return min(F(1), 1/(n*gap*gap))

    def invariant_forever_under_iid(self) -> bool:
        """Equal full one-shot laws imply every iid word law equals as well."""
        return self.internal == self.external


History = tuple[tuple[str, Hashable], ...]


@dataclass(frozen=True)
class OperationalKernel:
    """One nonanticipatory finite-horizon controlled stochastic source.

    A kernel gives P(outcome | exact PUBLIC history, chosen action), at
    every reachable history shorter than horizon. Its outcome law must be
    independent of counterfactual future actions; this is a premise.
    """
    source_id: str
    actions: tuple[str, ...]
    outcomes: tuple[Hashable, ...]
    horizon: int
    rows: Mapping[tuple[History, str], tuple[F, ...]]

    def __post_init__(self) -> None:
        if not self.source_id or not self.actions or not self.outcomes:
            raise StatisticalFrontierError("Nonempty source/actions/outcomes required")
        if len(set(self.actions)) != len(self.actions) or len(set(self.outcomes)) != len(self.outcomes):
            raise StatisticalFrontierError("Unique action and outcome labels required")
        if any(type(x) is not str or not x for x in self.actions):
            raise StatisticalFrontierError("Actions are named public operations")
        if type(self.horizon) is not int or not 1 <= self.horizon <= 8:
            raise StatisticalFrontierError("Finite source horizon 1..8 required")
        normalized = {key: _row(value) for key, value in self.rows.items()}
        expected = set()
        frontier = {()}
        for depth in range(self.horizon):
            nxt = set()
            for h in frontier:
                for a in self.actions:
                    key = (h, a)
                    expected.add(key)
                    if key not in normalized:
                        raise StatisticalFrontierError("Missing causal source response law")
                    for out, mass in zip(self.outcomes, normalized[key]):
                        if mass > 0:
                            nxt.add(h+((a,out),))
            frontier = nxt
        if set(normalized) != expected:
            raise StatisticalFrontierError("Unreachable/future-conditioning source rows rejected")
        object.__setattr__(self, "rows", normalized)

    def step(self, history: History, action: str) -> tuple[tuple[Hashable, F, History], ...]:
        if len(history) >= self.horizon or action not in self.actions:
            raise StatisticalFrontierError("Action beyond declared source horizon")
        key = (history, action)
        if key not in self.rows:
            raise StatisticalFrontierError("Not a reachable/history-compatible action")
        return tuple((o,p,history+((action,o),)) for o,p in zip(self.outcomes,self.rows[key]) if p>0)

    def policy_distribution(self, policy: Mapping[History, str]) -> dict[History, F]:
        """Law of the full public transcript under one deterministic adaptive policy."""
        frontier = {(): F(1)}
        for _ in range(self.horizon):
            result: dict[History,F] = {}
            for hist, mass in frontier.items():
                if hist not in policy or policy[hist] not in self.actions:
                    raise StatisticalFrontierError("Policy must specify every reached history")
                for _, p, future in self.step(hist, policy[hist]):
                    result[future] = result.get(future,F(0)) + mass*p
            frontier = result
        if sum(frontier.values(),F(0)) != 1:
            raise AssertionError("Causal response law failed normalization")
        return frontier

    def internal_history_state_bound(self) -> dict:
        """Finite controllable simulator state cost, not free computation."""
        reachable={()}
        all_histories={()}
        for depth in range(self.horizon):
            next_level=set()
            for h in reachable:
                for a in self.actions:
                    next_level.update(h+((a,o),) for o,p,_ in self.step(h,a))
            reachable=next_level
            all_histories.update(reachable)
        m=len(self.actions)*len(self.outcomes)
        upper=sum(m**j for j in range(self.horizon+1))
        if not len(all_histories)<=upper:
            raise AssertionError("Finite internal realization resource count failed")
        return {"reachable_internal_states":len(all_histories),
                "worst_case_state_upper":upper,"nonzero_resource_cost":len(all_histories)>1,
                "physical_ontology_authenticated":False}

    def internal_realization(self) -> "HistoryOnlySimulator":
        """Construct an INTERNAL labeled stochastic carrier with state=history."""
        return HistoryOnlySimulator(self)


@dataclass(frozen=True)
class HistoryOnlySimulator:
    """The declared internal carrier's actual state is ONLY the public history.

    It reproduces ALL lawful adaptive policies, by induction on history.
    This is a classical operational representation, not a physical ontology.
    """
    source: OperationalKernel

    def transition(self, current: History, action: str):
        return self.source.step(current, action)

    def run_policy(self, policy: Mapping[History, str]) -> dict[History,F]:
        """Independent recursive dynamic-programming traversal of the simulator."""
        def go(history: History, mass: F, final: dict[History,F]):
            if len(history) == self.source.horizon:
                final[history] = final.get(history,F(0)) + mass
                return
            if history not in policy:
                raise StatisticalFrontierError("No action specified for this public state")
            for _, prob, future in self.transition(history, policy[history]):
                go(future,mass*prob,final)
        out: dict[History,F] = {}
        go((),F(1),out)
        return out


def rational_bernoulli_tree(horizon: int, *, action_sensitivity: bool = True) -> OperationalKernel:
    """Nontrivial exact public-history/action-dependent stochastic laboratory."""
    actions = ("LEFT", "RIGHT")
    outcomes = (0, 1)
    rows = {}
    frontier = {()}
    for depth in range(horizon):
        next_level = set()
        for hist in frontier:
            for a in actions:
                last = hist[-1][1] if hist else 0
                numerator = 1 + ((depth + last + int(a=="RIGHT" and action_sensitivity)) % 3)
                rows[hist,a] = (F(numerator, 4), 1-F(numerator,4))
                for o in outcomes:
                    next_level.add(hist+((a,o),))
        frontier = next_level
    return OperationalKernel("same public process; ontology unidentifiable",actions,outcomes,horizon,rows)
