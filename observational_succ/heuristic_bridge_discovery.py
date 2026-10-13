"""Structural-vibe → candidate laws → cost-aware exact Bayesian experiment planning.

Uses the previous SUCC source-derived positive Stieltjes two-vs-three-mode
counterexample. No true internal circuit is supplied; an abstract shape prior
and legal (hypothetical) Bernoulli probes define a transparent mathematical
experiment. The tool discovers s=4 separates model shapes after s=0..3 do not.
"""
from __future__ import annotations
from fractions import Fraction as Q
from .contextual_heuristics import (
    ModelShape, ModelProbe, ProbeReceipt, HeuristicTower,
    shape_prior, bridge_pushforward_posterior, HeuristicError,
)
from .categorical_repair_synthesis import StieltjesLaw, positive_passive_alias


def declared_sensor(h:Q)->tuple[Q,Q]:
    """Artificial Bernoulli sensor law: P(positive|h)=(1+2h)/(2+2h).

    h>=0; positive response increases positive-report likelihood.
    This is NOT claimed to be a physically calibrated current sensor.
    """
    h=Q(h)
    if h<0:raise HeuristicError("Positive passive scalar transfer required")
    p=(1+2*h)/(2*(1+h))
    return p,1-p


def passive_probe(laws:dict[str,StieltjesLaw],s:Q,*,context="passive-port-rc",
                  cost=Q(1),noise_group=""):
    s=Q(s)
    if s<0:raise HeuristicError("Only s>=0 Laplace observations authorized")
    return ModelProbe(name=f"bernoulli@{s}",context=context,
                      outcomes=("positive","negative"),
                      kernels={label:declared_sensor(law.response(s))
                               for label,law in laws.items()},
                      cost=Q(cost),noise_group=noise_group)


def exact_response_probe(laws:dict[str,StieltjesLaw],s:Q,*,context="passive-port-rc"):
    s=Q(s)
    names=tuple(sorted({str(law.response(s)) for law in laws.values()}))
    return ModelProbe(name=f"exact-response@{s}",context=context,
                      outcomes=names,
                      kernels={k:tuple(Q(int(out==str(law.response(s))))
                                       for out in names)
                               for k,law in laws.items()},cost=Q(3))


def holdout_shape_demo():
    """Exact epistemic experiment with unknown true model, independent of RH."""
    alias=positive_passive_alias((0,1,2,3))
    names=("two-mode","three-mode")
    laws=dict(zip(names,(alias.lower,alias.higher)))
    shapes=(ModelShape(names[0],"passive-port-rc",
                       frozenset(("passive","network","memory","two-modes")),5,"degree-2"),
            ModelShape(names[1],"passive-port-rc",
                       frozenset(("passive","network","memory","three-modes")),6,"degree-3"))
    tower=HeuristicTower(shapes,frozenset(("passive","network","memory")),
                         source_id="declared-abstract-passive-source",epoch=0,basis_id="scalar-resolvent-v1")
    observations=tuple(passive_probe(laws,Q(s)) for s in (0,1,2,3))
    first_rank=tower.rank_probes(observations+(passive_probe(laws,Q(4)),))
    prior=dict(tower.posterior)
    for s,probe in enumerate(observations):
        # An explicitly independent mathematical Bernoulli experiment with
        # a legitimate possible outcome (never a sourced physical record).
        tower.observe(probe,ProbeReceipt(
            event_id=f"sim-{s}",source_id=tower.source_id,epoch=tower.epoch,
            basis_id=tower.basis_id,probe=probe.name,outcome="positive",
            observer="E",origin="declared_simulation"))
    post=dict(tower.posterior)
    holdout=passive_probe(laws,Q(4))
    exact_holdout=exact_response_probe(laws,Q(4))
    outcome_for_two=str(alias.lower.response(Q(4)))
    # Exact readout is a hypothetical stronger instrument, not actually performed.
    hypothetical={k:w*exact_holdout.law(k)[exact_holdout.outcomes.index(outcome_for_two)]
                  for k,w in post.items()}
    z=sum(hypothetical.values(),Q(0))
    return {"source_type":"DECLARED_STIELTJES_MODELS",
            "lower_degree":alias.lower.degree,"higher_degree":alias.higher.degree,
            "first_four_frequency_responses_equal":all(alias.lower.response(s)==alias.higher.response(s) for s in range(4)),
            "prior":prior,"posterior_after_four_independent_reports":post,
            "s4_expected_target_gini_gain":tower.expected_gini_gain(holdout),
            "s4_exact_report_would_separate":hypothetical[names[0]]/z==1,
            "ranked_probes":first_rank,
            "all_prior_source_assumptions_declared":True,
            "actual_source_authenticated":False,
            "formal_proof_from_positive_posterior":False}


def cross_context_analogy_demo():
    """Exact probabilistic coordinate transport across law-equivalent *models*.

    The mathematical adapter changes physical labels and source IDs. It does
    not claim a measured electrical sample was a measured thermal sample.
    """
    alias=positive_passive_alias((0,1,2,3))
    laws={"RC:two":alias.lower,"RC:three":alias.higher}
    twin={"Heat:two":alias.lower,"Heat:three":alias.higher}
    rc=(ModelShape("RC:two","RC",frozenset(("network",)),4,"2"),
        ModelShape("RC:three","RC",frozenset(("network",)),5,"3"))
    thermal=(ModelShape("Heat:two","Heat",frozenset(("diffusion",)),4,"2"),
             ModelShape("Heat:three","Heat",frozenset(("diffusion",)),5,"3"))
    r=HeuristicTower(rc,frozenset(),source_id="RC-context",epoch=0,basis_id="rational-transfer")
    t=HeuristicTower(thermal,frozenset(),source_id="HEAT-context",epoch=0,basis_id="rational-transfer")
    a=passive_probe(laws,Q(4),context="RC")
    b=passive_probe(twin,Q(4),context="Heat")
    mapping={"RC:two":"Heat:two","RC:three":"Heat:three"}
    return {"translated_posterior":bridge_pushforward_posterior(r,t,mapping,((a,b),)),
            "thermal_prior":t.prior,
            "likelihood_generator_preserved":True,
            "physical_source_shared":False}
