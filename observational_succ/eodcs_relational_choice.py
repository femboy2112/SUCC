"""Set-valued source interventions: transport of *possibilities*, not probabilities.

When s has many lawful successors, an observable state may evolve into a
SET of successor reports. A report-level set-valued transition exists
exactly when each old-report fiber has identical observed successor SETS.

The coarsest sufficient mathematical repair is (old-report, successor-set).
This does not justify equal-probability weighting, subjective certainty,
physical copies, accessible branch sampling, or stochastic dynamics.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product

from .causal_nerode_succ import SourceChart, SourceTransportError


@dataclass(frozen=True)
class RelationalIntervention:
    name: str
    before: SourceChart
    after: SourceChart
    successors: tuple[tuple[str, ...], ...]
    all_states_exhaustive: bool = True
    cost: Q = Q(1)
    physical_source_authenticated: bool = False

    def __post_init__(self):
        if (not self.name or not isinstance(self.name, str)
                or self.before.source_id != self.after.source_id
                or self.before.basis != self.after.basis
                or self.after.epoch < self.before.epoch
                or type(self.successors) is not tuple
                or len(self.successors) != len(self.before.states)
                or any(type(row) is not tuple or not row
                       or len(set(row)) != len(row)
                       or any(t not in self.after.states for t in row)
                       for row in self.successors)
                or type(self.all_states_exhaustive) is not bool
                or not isinstance(self.cost, Q) or self.cost <= 0
                or self.physical_source_authenticated):
            raise SourceTransportError(
                "Requires an inhabited exact source-versioned transition relation")

    def possible_states(self, source: str) -> tuple[str, ...]:
        if source not in self.before.states:
            raise SourceTransportError("Unavailable original-source address")
        return self.successors[self.before.states.index(source)]

    def possible_reports(self, source: str) -> tuple[str, ...]:
        return tuple(sorted({self.after.report(t)
                             for t in self.possible_states(source)}))


@dataclass(frozen=True)
class RelationalDescentCertificate:
    source_id: str
    before_epoch: int
    after_epoch: int
    basis: str
    source_action: str
    descended_to_set_valued_observer: bool
    deterministic_observer_possible: bool
    source_witness: tuple[str, str, str,
                          tuple[str, ...], tuple[str, ...]] | None
    full_observed_transition: tuple[tuple[str, tuple[str, ...]], ...]
    canonical_augmented_reports: tuple[
        tuple[str, tuple[str, tuple[str, ...]]], ...]
    old_class_count: int
    new_class_count: int
    source_class_certified: bool
    physical_source_authenticated: bool = False


def relational_descent(source: RelationalIntervention) -> RelationalDescentCertificate:
    """Emit exact set-valued original-source witness and universal repair.

    The witness s,t shares old report but disagrees on future support.
    The canonical pair quotient stores old q and finite successor support;
    it is not a physically materialized new sensor.
    """
    fiber_supports: dict[str, set[tuple[str, ...]]] = {}
    witness = None
    full = []
    augmented = []
    for s in source.before.states:
        old = source.before.report(s)
        fut = source.possible_reports(s)
        old_class = fiber_supports.setdefault(old,set())
        if old_class and fut not in old_class and witness is None:
            other = next(t for t in source.before.states
                         if source.before.report(t)==old and
                         source.possible_reports(t)!=fut)
            witness = (other,s,old,source.possible_reports(other),fut)
        old_class.add(fut)
        augmented.append((s,(old,fut)))
    for old,support in sorted(fiber_supports.items()):
        if len(support)==1:
            full.append((old,next(iter(support))))
    descended = witness is None
    if descended and len(full)!=len(source.before.image()):
        raise AssertionError("No single observable support was assigned to every fiber")
    deterministic = descended and all(len(reports)==1 for _,reports in full)
    return RelationalDescentCertificate(
        source.before.source_id,source.before.epoch,source.after.epoch,
        source.before.basis,source.name,descended,deterministic,
        witness,tuple(full) if descended else (),
        tuple(augmented),len(fiber_supports),
        len({pair for _,pair in augmented}),
        source.all_states_exhaustive and descended,
    )


def compose_relations(first: RelationalIntervention,
                      second: RelationalIntervention) -> RelationalIntervention:
    """Actual relational composition ∪_t R(s,t)·S(t,u), not product weights."""
    if (first.after != second.before or
            first.after.epoch != second.before.epoch):
        raise SourceTransportError("Unlicensed intermediate chart/base transport")
    result=[]
    for s in first.before.states:
        result.append(tuple(t for t in second.after.states
                            if any(t in second.possible_states(mid)
                                   for mid in first.possible_states(s))))
    return RelationalIntervention(
        first.name+";"+second.name,first.before,second.after,tuple(result),
        first.all_states_exhaustive and second.all_states_exhaustive,
        first.cost+second.cost)


def universally_sufficient_refinement(
        source: RelationalIntervention,
        candidate: tuple[tuple[str, str], ...]) -> bool:
    """Exact finite universal factor test independent from descent emitter."""
    if tuple(s for s,_ in candidate)!=source.before.states:
        raise SourceTransportError("Refinement must preserve complete state domain")
    r=dict(candidate)
    return all(
        r[s]!=r[t] or
        (source.before.report(s)==source.before.report(t) and
         source.possible_reports(s)==source.possible_reports(t))
        for s,t in product(source.before.states,repeat=2))


def source_likelihood_mutant(
        source: RelationalIntervention,
        hidden_laws: tuple[tuple[Q, ...], ...]
        ) -> dict:
    """Guard the gap between support knowledge and a probability law.

    Each row has positive mass exactly on its declared successor states;
    equality of mathematical supports DOES NOT imply equality of numerical
    likelihoods or of updated probabilities.
    """
    if (type(hidden_laws) is not tuple or len(hidden_laws)!=len(source.before.states)):
        raise SourceTransportError("Likelihood rows must be source-addressed")
    output_probabilities=[]
    for s,row in zip(source.before.states,hidden_laws):
        if (type(row) is not tuple or len(row)!=len(source.possible_states(s))
                or any(not isinstance(x,Q) or x<=0 for x in row)
                or sum(row,Q(0))!=1):
            raise SourceTransportError("Full exact positive conditional law required")
        masses={}
        for t,m in zip(source.possible_states(s),row):
            key=source.after.report(t)
            masses[key]=masses.get(key,Q(0))+m
        output_probabilities.append((s,tuple(sorted(masses.items()))))
    return {
        "source_version":(source.before.source_id,source.before.epoch,
                          source.after.epoch),
        "law_by_source_state":tuple(output_probabilities),
        "same_observable_support_is_not_same_probability_law":True,
        "empirical_calibration_claimed":False,
    }


def relational_choice_demo() -> dict:
    states=("s0","s1")
    successors=("u0","u1")
    before=SourceChart("declared-branch",0,"binary",states,("0","0"))
    after=SourceChart("declared-branch",1,"binary",successors,("cold","warm"))
    # Both old states lead to both observed successors. Nondeterministic
    # original source, but identical set-valued observer support.
    r=RelationalIntervention("branch",before,after,
                              (("u0","u1"),("u0","u1")))
    cert=relational_descent(r)
    if not cert.descended_to_set_valued_observer or cert.deterministic_observer_possible:
        raise AssertionError("Must construct relation-valued, not scalar, successor")
    # Same source support, different probabilities: support transport alone
    # is not a stochastic Bayesian kernel.
    laws=source_likelihood_mutant(
        r,((Q(1,4),Q(3,4)),(Q(3,4),Q(1,4))))
    second=RelationalIntervention(
        "coarsen",after,SourceChart("declared-branch",2,"binary",
                                  ("v0","v1"),("end","end")),
        (("v0",),("v1",)))
    composition=compose_relations(r,second)
    c2=relational_descent(composition)
    falsifier=RelationalIntervention("different-support",before,after,
                                     (("u0",),("u1",)))
    failed=relational_descent(falsifier)
    return {
        "source":"declared-branch",
        "source_multivalued":True,
        "observable_set_valued_transition":[list(pair)
                                             for pair in cert.full_observed_transition],
        "set_valued_observation_descends":cert.descended_to_set_valued_observer,
        "deterministic_observation_descends":cert.deterministic_observer_possible,
        "support_equal_but_likelihoods_different":
            laws["law_by_source_state"][0][1]!=laws["law_by_source_state"][1][1],
        "composed_reconciled_observer_is_deterministic":
            c2.deterministic_observer_possible,
        "incompatible_original_fiber_witness":
            [failed.source_witness[0],failed.source_witness[1]],
        "source_class_complete":cert.source_class_certified,
        "physical_source_authenticated":False,
        "probabilistic_interpretation_inferred_from_support":False,
    }
