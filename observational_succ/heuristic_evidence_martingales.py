"""Anytime-valid likelihood-ratio evidence against a fully specified null.

A Bayes posterior is a model-dependent betting odds; a null e-process is an
actual finite-sample error control once the null's conditional laws are genuine.
The probe policy can be adaptive, but its choice must be predictable from public
history. Classical Doob/Ville likelihood-ratio martingale, not formal proof.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Callable
from .contextual_heuristics import ModelProbe, HeuristicError, exact


def lr_step(odds,probe:ModelProbe, outcome:str,*,null:str,alternative:str):
    """One exact likelihood-ratio update under identical public experiment."""
    if outcome not in probe.outcomes:
        raise HeuristicError("Unknown outcome")
    a=probe.law(null);b=probe.law(alternative)
    if any(v<=0 for v in a):
        raise HeuristicError("This elementary e-process requires full null support")
    return exact(odds)*b[probe.outcomes.index(outcome)]/a[probe.outcomes.index(outcome)]


@dataclass(frozen=True)
class LRReceipt:
    history:tuple[tuple[str,str],...]
    wealth:Q
    null:str
    alternative:str
    threshold:Q
    crosses:bool
    conclusion:"str"="EVIDENCE_AGAINST_SPECIFIED_NULL_NOT_ONTIC_PROOF"


def replay_lr(history:tuple[tuple[ModelProbe,str],...], *,null:str,alternative:str,alpha=Q(1,20)):
    alpha=exact(alpha)
    if not 0<alpha<1:raise HeuristicError("Confidence level must be in (0,1)")
    wealth=Q(1)
    trace=[]
    for p,y in history:
        wealth=lr_step(wealth,p,y,null=null,alternative=alternative)
        trace.append((p.name,y))
    return LRReceipt(tuple(trace),wealth,null,alternative,1/alpha,wealth>=1/alpha)


def adaptive_crossing_probability(policy:Callable[[tuple[tuple[str,str],...]],ModelProbe],
                                  horizon:int,*,null:str,alternative:str,
                                  alpha=Q(1,10)):
    """Exact null probability of EVER crossing 1/alpha in a finite adaptive tree.

    Checking this instance is not a proof of Ville's infinite-horizon bound:
    the bound follows from E[LR_(n+1)|history]=LR_n and optional stopping.
    """
    if type(horizon) is not int or not 0<=horizon<=12:
        raise HeuristicError("Finite exact tree horizon 0..12 required")
    alpha=exact(alpha)
    if not 0<alpha<1:raise HeuristicError("Alpha must lie in (0,1)")
    limit=1/alpha
    examined=0
    def rec(history,wealth,prob,depth):
        nonlocal examined
        examined+=1
        if wealth>=limit:return prob
        if depth==horizon:return Q(0)
        probe=policy(history)
        if not isinstance(probe,ModelProbe):
            raise HeuristicError("Adaptive experiment must be a previously declared lawful probe")
        p0=probe.law(null)
        return sum((rec(history+((probe.name,y),),
                        lr_step(wealth,probe,y,null=null,alternative=alternative),
                        prob*p0[i],depth+1)
                    for i,y in enumerate(probe.outcomes)),Q(0))
    crossing=rec((),Q(1),Q(1),0)
    if crossing>alpha:
        raise ArithmeticError("Anytime-valid null test violated Ville bound")
    return {"null_cross_probability":crossing,
            "upper_bound":alpha,"threshold":limit,
            "tree_nodes":examined,
            "valid_with_predictable_adaptive_probes":True,
            "physical_null_law_authenticated":False}


def noisy_limit_witness(p,even_trials:int):
    """Exact Chernoff/Bhattacharyya WRONG-MODEL bound for even n.

    Two i.i.d. Bernoulli models with P_true(up)=p, P_false(up)=1-p,
    equal strictly positive priors and 1/2 posterior decision threshold.
    Under true model: Pr(posterior_wrong>=1/2) <= B^n,
    B=2 sqrt(p*(1-p))<1. At even n the bound is exact rational.
    Since sum_n B^n is finite, wrong posterior converges to 0 a.s.
    No finite event establishes deductive certainty (full support).
    """
    p=exact(p)
    if not Q(1,2)<p<1 or type(even_trials) is not int or even_trials<0 or even_trials%2:
        raise HeuristicError("p in (1/2,1), even nonnegative trial count required")
    b2=4*p*(1-p)
    assert 0<b2<1
    return {"true_success_probability":p,
            "bhattacharyya_coefficient_squared":b2,
            "trial_count":even_trials,
            "wrong_majority_posterior_probability_upper":b2**(even_trials//2),
            "any_finite_trial_deductive_certainty":False,
            "almost_sure_limit_requires_iid_calibrated_laws":True}
