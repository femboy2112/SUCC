"""Exact independent check of conditional observation kernels on shared latent noise.

An observer cannot infer independence from distinct event IDs; a finite latent
model specifies joint outcomes. This module CERTIFIES model-relative
conditional kernels from one declared original source. It does not attest
actual physical instruments, which need separate empirical verification.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping
from .contextual_heuristics import ModelProbe,HeuristicError,_distribution


@dataclass(frozen=True)
class FiniteJointNoise:
    weights:Mapping[str,tuple[Q,...]]
    outcome_tables:Mapping[str,Mapping[str,tuple[str,...]]]

    def __post_init__(self):
        if not self.weights or not self.outcome_tables:
            raise HeuristicError("Nonempty finite latent laws and probe outputs required")
        for model,distribution in self.weights.items():
            _distribution(distribution)
            if model not in self.outcome_tables or not self.outcome_tables[model]:
                raise HeuristicError("Every model needs a complete latent-output table")
            for name,values in self.outcome_tables[model].items():
                if not name or len(values)!=len(distribution) or any(
                    type(v) is not str or not v for v in values):
                    raise HeuristicError("Every outcome must be a typed function of original latent")
        probes={tuple(sorted(v)) for v in self.outcome_tables.values()}
        if len(probes)!=1:
            raise HeuristicError("All model candidates must share the declared probe menu")

    def conditioned_distribution(self,model:str,next_probe:str,outcomes:tuple[str,...],
                                  history:tuple[tuple[str,str],...]=()):
        if model not in self.weights:
            raise HeuristicError("Model outside declared finite latent source")
        data=self.outcome_tables[model]
        if next_probe not in data:
            raise HeuristicError("Probe not in source latent menu")
        if len(set(outcomes))!=len(outcomes):
            raise HeuristicError("Repeated outcome names not permitted")
        ids=[]
        for i in range(len(self.weights[model])):
            if all(data[p][i]==y for p,y in history):
                ids.append(i)
        z=sum((self.weights[model][i] for i in ids),Q(0))
        if z==0:
            raise HeuristicError("Conditional law is undefined on zero-probability history")
        if any(data[next_probe][i] not in outcomes for i in ids):
            raise HeuristicError("Source can produce undeclared probe outcome")
        return tuple(sum((self.weights[model][i] for i in ids
                          if data[next_probe][i]==y),Q(0))/z for y in outcomes)

    def verify_claimed_conditional(self,probe:ModelProbe,
                                   history:tuple[tuple[str,str],...]=()):
        if set(self.weights)!=set(probe.kernels):
            raise HeuristicError("Source/model catalog mismatch")
        defects=[]
        for model in self.weights:
            actual=self.conditioned_distribution(model,probe.name,probe.outcomes,history)
            claimed=probe.law(model)
            if actual!=claimed:
                defects.append((model,actual,claimed))
        return {"source_conditional_law_verified":not defects,
                "first_witness":defects[0] if defects else None,
                "history":history,
                "physical_noise_independence_authenticated":False}


def repeated_measurement_witness():
    """Shared latent reused. Conditional second outcome conveys zero new info."""
    models=("H0","H1")
    noise=FiniteJointNoise(
        weights={"H0":(Q(1,2),Q(1,2)),"H1":(Q(3,4),Q(1,4))},
        outcome_tables={model:{"first":("yes","no"),"second":("yes","no")}
                        for model in models})
    first=ModelProbe("first","c",("yes","no"),
                     {"H0":(Q(1,2),Q(1,2)),"H1":(Q(3,4),Q(1,4))},
                     noise_group="shared-latent")
    second_bad=ModelProbe("second","c",first.outcomes,
                           first.kernels,noise_group="shared-latent",conditioned_on=("first-evidence",))
    second_good=ModelProbe("second","c",first.outcomes,
                            {"H0":(1,0),"H1":(1,0)},
                            noise_group="shared-latent",conditioned_on=("first-evidence",))
    return {"initial_source":noise.verify_claimed_conditional(first),
            "naive_reuse":noise.verify_claimed_conditional(second_bad,(("first","yes"),)),
            "sourced_conditional":noise.verify_claimed_conditional(second_good,(("first","yes"),)),
            "no_second_independent_observation_is_present":True}
