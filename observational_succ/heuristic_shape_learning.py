"""Learning heuristic priors from INDEPENDENT verified model-solving tasks.

A finite hyper-Bayesian model of structural features: hypotheses are different
predeclared feature-weight schemes; verified past successful model selections
update probabilities of those schemes, which set priors on an independent new
context. Each past task must carry unique original-source identity to reject
training duplicates. Learning weights does not prove a theorem, imply causal
relevance or ensure out-of-distribution calibration. Entirely exact rational.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping
from .contextual_heuristics import ModelShape,HeuristicError,exact,_distribution


@dataclass(frozen=True)
class ShapeHeuristic:
    name:str
    feature_bonuses:Mapping[str,int]
    length_penalty:int=1

    def __post_init__(self):
        if (not self.name or type(self.length_penalty) is not int or
            not 0<=self.length_penalty<=8 or
            any(type(k) is not str or not k or type(v) is not int or abs(v)>16
                for k,v in self.feature_bonuses.items())):
            raise HeuristicError("Finite bounded structural weight grammar required")

    def model_prior(self, models:tuple[ModelShape,...], context_signature:frozenset[str]):
        if not models or len({m.label for m in models})!=len(models) or len({m.context for m in models})!=1:
            raise HeuristicError("One declared model competition in one context required")
        if not isinstance(context_signature,frozenset):
            raise HeuristicError("Explicit context signature required")
        weights={}
        for m in models:
            score=sum((self.feature_bonuses.get(f,0)
                       for f in m.signature & context_signature),0)
            score-=self.length_penalty*m.code_length
            weights[m.label]=Q(2)**score
        z=sum(weights.values(),Q(0))
        return {label:weight/z for label,weight in weights.items()}


@dataclass(frozen=True)
class IndependentSolvedTask:
    task_id:str
    source_id:str
    models:tuple[ModelShape,...]
    signature:frozenset[str]
    verified_winner:str
    declared_solution_certificate:str

    def __post_init__(self):
        if (not self.task_id or not self.source_id or
            not self.declared_solution_certificate or
            self.verified_winner not in {m.label for m in self.models}):
            raise HeuristicError("A training example needs unique source and independently checked winner")


class HeuristicMetaLearner:
    def __init__(self,schemes:tuple[ShapeHeuristic,...],priors:Mapping[str,Q]):
        if not schemes or len({s.name for s in schemes})!=len(schemes) or set(priors)!={s.name for s in schemes}:
            raise HeuristicError("One normalized hyperprior per unique heuristic scheme")
        self.schemes=schemes
        self.posterior={s.name:exact(priors[s.name]) for s in schemes}
        _distribution(tuple(self.posterior.values()))
        self.verified_tasks:list[IndependentSolvedTask]=[]
        self.claimed_physical_calibration=False

    def update_from_verified_task(self,task:IndependentSolvedTask):
        if any(t.task_id==task.task_id for t in self.verified_tasks):
            raise HeuristicError("Training task replay is not new evidence")
        if any(t.source_id==task.source_id for t in self.verified_tasks):
            raise HeuristicError("Correlated training tasks sharing one source need a JOINT likelihood")
        weighted={s.name:self.posterior[s.name]*s.model_prior(task.models,task.signature)[task.verified_winner]
                  for s in self.schemes}
        z=sum(weighted.values(),Q(0))
        if z==0:raise HeuristicError("Verified task impossible under every scheme")
        self.posterior={label:w/z for label,w in weighted.items()}
        self.verified_tasks.append(task)
        return dict(self.posterior)

    def prior_for_new_context(self,models:tuple[ModelShape,...],signature:frozenset[str]):
        if not models or len({m.label for m in models})!=len(models):
            raise HeuristicError("One declared target model family needed")
        distributions={s.name:s.model_prior(models,signature) for s in self.schemes}
        return {m.label:sum((self.posterior[s.name]*distributions[s.name][m.label]
                             for s in self.schemes),Q(0)) for m in models}


def learning_demo():
    models=(ModelShape("memory","test",frozenset(("storage",)),3,"yes"),
            ModelShape("static","test",frozenset(),3,"no"))
    schemes=(ShapeHeuristic("storage-is-useful",{"storage":2}),
             ShapeHeuristic("ignore-storage",{}))
    engine=HeuristicMetaLearner(schemes,{s.name:Q(1,2) for s in schemes})
    before=engine.prior_for_new_context(models,frozenset(("storage",)))
    task=IndependentSolvedTask("verified-001","source-001",models,frozenset(("storage",)),
                               "memory","independent mathematical validation of candidate")
    posterior=engine.update_from_verified_task(task)
    after=engine.prior_for_new_context(models,frozenset(("storage",)))
    return {"pretraining_model_prior":before,
            "hyperposterior_after_one_verified_task":posterior,
            "new_context_model_prior":after,
            "shape_confidence_changed":after["memory"]>before["memory"],
            "formal_truth_of_new_model_proved":False,
            "independence_of_source_trials_required":True,
            "empirical_calibration_authenticated":False}
