"""Exact source-coupling uncertainty: two heuristic marginals never entail
independence. Fréchet–Hoeffding bounds, joint observations, and a finite
latent-factor realization with an exact matrix-rank obstruction.

Probabilities use rational Fractions; the entire law is a DECLARED joint source,
not independent scientific data or an unconditional probability of math truth.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from .relational_model_genetics import GeneticsError


def probability(v)->Q:
    if type(v) is int or isinstance(v,Q):
        x=Q(v)
    else:raise GeneticsError('Exact rational probability required')
    if not 0<=x<=1:raise GeneticsError('Probability must lie in [0,1]')
    return x


@dataclass(frozen=True)
class CouplingInterval:
    p: Q
    q: Q
    lower: Q
    upper: Q
    independent: Q

    def realize(self,t:Q)->tuple[tuple[Q,Q],tuple[Q,Q]]:
        t=probability(t)
        if not self.lower<=t<=self.upper:
            raise GeneticsError('Invalid joint event probability for given marginals')
        return ((t,self.p-t),(self.q-t,1-self.p-self.q+t))


def frechet_bounds(p,q)->CouplingInterval:
    p,q=probability(p),probability(q)
    low=max(Q(0),p+q-1)
    high=min(p,q)
    i=p*q
    assert low<=i<=high
    return CouplingInterval(p,q,low,high,i)


@dataclass(frozen=True)
class JointBinarySource:
    source_id: str
    epoch: int
    basis: str
    law: tuple[tuple[Q,Q],tuple[Q,Q]]

    def __post_init__(self):
        if not self.source_id or not self.basis or type(self.epoch) is not int or self.epoch<0:
            raise GeneticsError('Joint probability needs one source, epoch and basis')
        if (type(self.law) is not tuple or len(self.law)!=2 or
            any(type(row) is not tuple or len(row)!=2 for row in self.law)):
            raise GeneticsError('Require 2 by 2 exact joint law')
        values=[probability(x) for row in self.law for x in row]
        if sum(values,Q(0))!=1:raise GeneticsError('Joint law must be normalized')

    @property
    def p(self):return sum(self.law[0],Q(0))

    @property
    def q(self):return self.law[0][0]+self.law[1][0]

    @property
    def intersection(self):return self.law[0][0]

    @property
    def det(self):
        (a,b),(c,d)=self.law
        return a*d-b*c

    @property
    def minimum_latent_cardinality_lower_bound(self)->int:
        """Ordinary matrix rank: each conditionally independent latent Z
        contributes a rank-one probability outer product. For 2x2 only.
        """
        if self.det!=0:return 2
        if any(x>0 for row in self.law for x in row):return 1
        raise ArithmeticError('A normalized probability law cannot vanish')

    def conditional_y_given_x(self):
        """A CONSTRUCTIVE |X|-state latent mixture Z=X, so rank bound 2
        is sharp for rank-two binary source laws. This does not make Z
        an authenticated hidden physical variable.
        """
        vals=[]
        for row in self.law:
            total=sum(row,Q(0))
            vals.append(tuple(x/total for x in row) if total else (Q(0),Q(0)))
        return tuple(vals)

    def verify_independent(self):
        return self.intersection==self.p*self.q


def combine_heuristic_marginals_demo():
    b=frechet_bounds(Q(2,3),Q(3,4))
    low=JointBinarySource('declared',0,'binary',b.realize(b.lower))
    mid=JointBinarySource('declared',0,'binary',b.realize(b.independent))
    hi=JointBinarySource('declared',0,'binary',b.realize(b.upper))
    assert all((x.p,x.q)==(b.p,b.q) for x in (low,mid,hi))
    return {'marginals':(str(b.p),str(b.q)),
            'allowed_intersection':(str(b.lower),str(b.upper)),
            'independent_overlap_is_only_one_admissible_case':str(b.independent),
            'different_realizable_joint_laws':3,
            'rank_two_correlated_example':hi.minimum_latent_cardinality_lower_bound,
            'missing_joint_source_implies_no_unique_posterior':True,
            'quantum_entanglement_claimed':False}
