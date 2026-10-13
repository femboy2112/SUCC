"""Heuristics for Observational SUCC: exact conditional predictions, never proof.

All probabilities are model-conditional Fractions. Structural resemblance sets a
*declared prior*, not an empirical likelihood and not a probability of formal
mathematical truth. An observer can test compatible source-model hypotheses,
choose cost-aware probes and black-box observational quotients. Mathematically
familiar: Bayesian experimental design, sufficient statistics and model checking.

The observer MUST distinguish one observation from reusing the same noisy latent
source twice. Model-class exhaustiveness and instrument authenticity are never
inferred from a high posterior. No RH, physical-data or machine-learning claims.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping


class HeuristicError(ValueError):
    """Malformed model, corrupted scope or inapplicable probabilistic claim."""


class ModelClassMisspecified(HeuristicError):
    """The observed outcome has probability zero under EVERY live model."""


def exact(x):
    if type(x) is int or isinstance(x, Q):
        return Q(x)
    raise HeuristicError("Certified probabilities require exact int/Fraction, not float")


def _distribution(items):
    values=tuple(exact(v) for v in items)
    if not values or any(v<0 for v in values) or sum(values,Q(0))!=1:
        raise HeuristicError("Full normalized nonnegative finite likelihood law required")
    return values


@dataclass(frozen=True)
class ModelShape:
    label: str
    context: str
    signature: frozenset[str]
    code_length: int
    target: str

    def __post_init__(self):
        if (not self.label or not self.context or not self.target or
            type(self.code_length) is not int or not 1<=self.code_length<=80 or
            not isinstance(self.signature,frozenset) or
            any(type(s) is not str or not s for s in self.signature)):
            raise HeuristicError("Typed model shape, context, target and positive code length needed")


@dataclass(frozen=True)
class ModelProbe:
    name: str
    context: str
    outcomes: tuple[str,...]
    kernels: Mapping[str, tuple[Q,...]]
    cost: Q = Q(1)
    noise_group: str = ""
    conditioned_on: tuple[str,...] = ()

    def __post_init__(self):
        if (not self.name or not self.context or
            type(self.outcomes) is not tuple or not self.outcomes or
            len(set(self.outcomes))!=len(self.outcomes) or
            any(type(s) is not str or not s for s in self.outcomes)):
            raise HeuristicError("Typed finite, distinct experiment outcomes required")
        if exact(self.cost)<=0:
            raise HeuristicError("A probe requires a positive resource cost")
        if type(self.noise_group) is not str or any(
            type(e) is not str or not e for e in self.conditioned_on
        ) or len(set(self.conditioned_on))!=len(self.conditioned_on):
            raise HeuristicError("Malformed dependence/source-lease contract")
        if not self.kernels:
            raise HeuristicError("Declare likelihood for every candidate")
        for key,values in self.kernels.items():
            if not key or len(values)!=len(self.outcomes):
                raise HeuristicError("Missing outcome in an experimental likelihood")
            _distribution(values)

    def law(self,label):
        try:return _distribution(self.kernels[label])
        except KeyError as exc:raise HeuristicError("Candidate absent from probe law") from exc


@dataclass(frozen=True)
class ProbeReceipt:
    event_id: str
    source_id: str
    epoch: int
    basis_id: str
    probe: str
    outcome: str
    observer: str
    origin: str = "declared_simulation"

    def __post_init__(self):
        if (not self.event_id or not self.source_id or not self.basis_id or
            not self.probe or not self.outcome or not self.observer or
            type(self.epoch) is not int or self.epoch<0 or
            self.origin not in ("declared_simulation","empirical_claim")):
            raise HeuristicError("Missing lawful source/observer/epoch/event identity")


def shape_prior(models:tuple[ModelShape,...], observed_signature:frozenset[str]):
    """A deliberately DECLARED shape/MDL-inspired prior, not a learned law.

    Weight(M)=2^(number of shared tags - code length). Original shape tags
    must be pre-evidence. An empirical fact must NOT be used again as a prior.
    """
    if not models or len({m.label for m in models})!=len(models):
        raise HeuristicError("Unique nonempty model catalog required")
    if len({m.context for m in models})!=1:
        raise HeuristicError("Different contexts require a VERIFIED semantic bridge")
    if not isinstance(observed_signature,frozenset):
        raise HeuristicError("Use a stable, pre-evidence finite shape signature")
    weights={m.label:Q(2)**(len(m.signature & observed_signature)-m.code_length)
             for m in models}
    z=sum(weights.values(),Q(0))
    return {k:v/z for k,v in weights.items()}


def gini(distribution):
    """Quadratic (Brier/Gini) target uncertainty, exact rational."""
    vals=tuple(exact(x) for x in distribution)
    return 1-sum((p*p for p in _distribution(vals)),Q(0))


class HeuristicTower:
    def __init__(self,models:tuple[ModelShape,...],observed_shape:frozenset[str],
                 *,source_id:str,epoch:int,basis_id:str,
                 prior:Mapping[str,Q]|None=None):
        if not source_id or not basis_id or type(epoch) is not int or epoch<0:
            raise HeuristicError("Source ID, epoch and basis must be fixed")
        self.models=tuple(models)
        self.context=models[0].context if models else ""
        self.prior=shape_prior(models,observed_shape) if prior is None else {
            m.label:exact(prior[m.label]) for m in models}
        _distribution(tuple(self.prior.values()))
        self.posterior=dict(self.prior)
        self.source_id,self.epoch,self.basis_id=source_id,epoch,basis_id
        self.events:list[ProbeReceipt]=[]
        self.used_noise_groups:dict[str,list[str]]={}
        self.claimed_scope="DECLARED_PROBABILISTIC_MODEL_CLASS_ONLY"

    def _validate_probe(self,p:ModelProbe):
        if p.context!=self.context or set(p.kernels)!=set(self.posterior):
            raise HeuristicError("Unlicensed model-context or incomplete likelihood")
        if p.noise_group and p.noise_group in self.used_noise_groups:
            required=set(self.used_noise_groups[p.noise_group])
            if not required.issubset(p.conditioned_on):
                raise HeuristicError(
                    "Correlated evidence replay forbidden: supply a genuine conditional law"
                )
        if p.conditioned_on:
            known={e.event_id for e in self.events}
            if not set(p.conditioned_on).issubset(known):
                raise HeuristicError("Conditional likelihood claims unseen evidence")

    def observe(self,p:ModelProbe,record:ProbeReceipt):
        self._validate_probe(p)
        if ((record.source_id,record.epoch,record.basis_id)!=
            (self.source_id,self.epoch,self.basis_id) or record.probe!=p.name):
            raise HeuristicError("Source/version/basis/probe mismatch")
        if record.event_id in {e.event_id for e in self.events}:
            raise HeuristicError("An identical actual observation cannot be counted twice")
        if record.outcome not in p.outcomes:
            raise HeuristicError("Report outcome not in probe menu")
        j=p.outcomes.index(record.outcome)
        weighted={k:w*p.law(k)[j] for k,w in self.posterior.items()}
        z=sum(weighted.values(),Q(0))
        if z==0:
            raise ModelClassMisspecified(
                "Evidence is impossible under every admitted live hypothesis; expand/revise model class"
            )
        self.posterior={k:v/z for k,v in weighted.items()}
        self.events.append(record)
        if p.noise_group:
            self.used_noise_groups.setdefault(p.noise_group,[]).append(record.event_id)
        return dict(self.posterior)

    def forecast(self,p:ModelProbe):
        self._validate_probe(p)
        return {y:sum((self.posterior[k]*p.law(k)[j]
                        for k in self.posterior),Q(0))
                for j,y in enumerate(p.outcomes)}

    def target_posterior(self,posterior:Mapping[str,Q]|None=None):
        posterior=self.posterior if posterior is None else posterior
        d:dict[str,Q]={}
        for m in self.models:
            d[m.target]=d.get(m.target,Q(0))+posterior[m.label]
        return d

    def expected_gini_gain(self,p:ModelProbe,*,target_relative:bool=True):
        """Exact expected reduction; >=0 and equals weighted posterior dispersion."""
        prior=self.target_posterior() if target_relative else self.posterior
        initial=gini(tuple(prior.values()))
        predict=self.forecast(p)
        risk=Q(0)
        variance=Q(0)
        for j,y in enumerate(p.outcomes):
            prob=predict[y]
            if prob==0:continue
            post={k:self.posterior[k]*p.law(k)[j]/prob for k in self.posterior}
            grouped=self.target_posterior(post) if target_relative else post
            risk+=prob*gini(tuple(grouped.values()))
            variance+=prob*sum(((grouped[k]-prior[k])**2 for k in prior),Q(0))
        gain=initial-risk
        if gain<0 or gain!=variance:
            raise ArithmeticError("Quadratic Bayes-risk identity violated")
        return gain

    def rank_probes(self,probes,*,target_relative=True):
        cards=[]
        for p in probes:
            self._validate_probe(p)
            benefit=self.expected_gini_gain(p,target_relative=target_relative)
            cards.append((p.name,benefit,benefit/exact(p.cost)))
        return tuple(sorted(cards,key=lambda x:(-x[2],-x[1],x[0])))

    def observational_capsules(self,probes):
        """Merge shapes indistinguishable under all CURRENT authorized probes.

        Sound for repeated independent experiments from these kernels; future
        new probes, latent changes, or hidden interventions can split a class.
        """
        for p in probes:self._validate_probe(p)
        groups:dict[tuple, list[str]]={}
        for m in self.models:
            signature=tuple(p.law(m.label) for p in probes)
            groups.setdefault(signature,[]).append(m.label)
        classes=[]
        for values in groups.values():
            t={m.target for m in self.models if m.label in values}
            classes.append({"models":tuple(sorted(values)),
                            "mass":sum((self.posterior[m] for m in values),Q(0)),
                            "target_defined":len(t)==1,
                            "target":next(iter(t)) if len(t)==1 else None})
        return tuple(sorted(classes,key=lambda x:x["models"]))

    def verdict(self):
        supported={m.target for m in self.models if self.posterior[m.label]>0}
        return {"posterior":dict(self.posterior),
                "target_posterior":self.target_posterior(),
                "compatible_targets":tuple(sorted(supported)),
                "conditional_target_identified":len(supported)==1,
                "status":"HEURISTIC_NOT_FORMAL_PROOF",
                "source_authenticated":False,
                "source_class_exhaustive":False,
                "likelihood_correctness_empirically_verified":False}


def bridge_pushforward_posterior(tower:HeuristicTower, target:HeuristicTower,
                                  model_map:Mapping[str,str],
                                  probe_pairs:tuple[tuple[ModelProbe,ModelProbe],...]):
    """Finite naturality under a *bijective* structure/law preserving bridge.

    The bridge sends priors and action likelihoods to corresponding target
    coordinates. Contradictory kernels, contexts or base probabilities reject.
    """
    if set(model_map)!=set(tower.posterior) or set(model_map.values())!=set(target.posterior) or len(set(model_map.values()))!=len(model_map):
        raise HeuristicError("A valid finite Bayesian change of coordinates requires a bijection")
    if any(target.prior[model_map[m]]!=p for m,p in tower.prior.items()):
        raise HeuristicError("Context bridge must transport source priors too")
    for a,b in probe_pairs:
        tower._validate_probe(a)
        target._validate_probe(b)
        if a.outcomes!=b.outcomes:
            raise HeuristicError("Different units/outcomes need an explicit translation")
        for m,t in model_map.items():
            if a.law(m)!=b.law(t):
                raise HeuristicError("Bridge is not law-preserving on an experimental generator")
    return {model_map[m]:p for m,p in tower.posterior.items()}


def quotient_shape_prior(models:tuple[ModelShape,...],observed_shape:frozenset[str],
                          probes:tuple[ModelProbe,...]):
    """Representation-duplication resistant prior over CURRENT behavioral classes.

    Group by equal kernels for every permitted probe; class weight is the MAX
    unnormalized shape score of its listed presentations (shortest/best syntax).
    Split that mass uniformly within class, never treating extra copied syntax
    as new physical evidence. Only invariant within the DECLARED probe menu.
    """
    if not probes:raise HeuristicError("A behavioral prior requires a nonempty probe menu")
    individual=shape_prior(models,observed_shape)
    names={m.label for m in models}
    if any(p.context!=models[0].context or set(p.kernels)!=names for p in probes):
        raise HeuristicError("Same original-source experiment menu required")
    groups:dict[tuple,list[str]]={}
    for m in models:
        groups.setdefault(tuple(p.law(m.label) for p in probes),[]).append(m.label)
    # Normalization in 'individual' is common to all weights; max/sum retains
    # the exact same class prior as working with unnormalized 2^score weights.
    class_weight={signature:max(individual[m] for m in items)
                  for signature,items in groups.items()}
    z=sum(class_weight.values(),Q(0))
    return {m:class_weight[signature]/z/len(items)
            for signature,items in groups.items() for m in items}


def syntax_clone_counterexample():
    """Syntactic duplicate biases naive model priors; quotient prior avoids it.

    Behavioral equivalence here is relative to a fixed declared sensor menu;
    no inference about unmeasured contexts or carrier ontology follows.
    """
    base=(ModelShape("A","c",frozenset(),3,"A"),
          ModelShape("B","c",frozenset(),3,"B"))
    dup=base+(ModelShape("A-copy","c",frozenset(),3,"A"),)
    p1=ModelProbe("sensor","c",("yes","no"),
                  {"A":(Q(3,4),Q(1,4)),"B":(Q(1,4),Q(3,4))})
    p2=ModelProbe("sensor","c",("yes","no"),
                  {"A":(Q(3,4),Q(1,4)),"B":(Q(1,4),Q(3,4)),
                   "A-copy":(Q(3,4),Q(1,4))})
    naive_base=shape_prior(base,frozenset())
    naive_dup=shape_prior(dup,frozenset())
    protected_base=quotient_shape_prior(base,frozenset(),(p1,))
    protected_dup=quotient_shape_prior(dup,frozenset(),(p2,))
    return {"naive_A_before":naive_base["A"],
            "naive_A_after_syntax_clone":naive_dup["A"]+naive_dup["A-copy"],
            "quotient_A_before":protected_base["A"],
            "quotient_A_after":protected_dup["A"]+protected_dup["A-copy"],
            "behavioral_menu_is_exhaustive":False}


def binary_bernoulli_target_gain(prior_first,yes_first,yes_second):
    """Closed-form exact Gini gain for two opposite target classes.

    For a=P(M1), d=P(Y=yes|M1)-P(Y=yes|M2), q=P(Y=yes):
      gain = 2*a^2*(1-a)^2*d^2/[q*(1-q)].
    Vanishes iff either model had zero prior or predictions coincide, on
    the nondegenerate domain. A useful second-order diagnostic of weak probes.
    """
    a=exact(prior_first);u=exact(yes_first);v=exact(yes_second)
    if not 0<=a<=1 or not 0<=u<=1 or not 0<=v<=1:
        raise HeuristicError("Probabilities outside [0,1]")
    q=a*u+(1-a)*v
    if q in (0,1):return Q(0)
    return 2*a*a*(1-a)*(1-a)*(u-v)*(u-v)/(q*(1-q))
