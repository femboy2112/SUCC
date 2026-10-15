"""Rule-checked meta-model proof capsules: recursive composition without ghost theorems.

No unrestricted general proof-checker, no cryptographic attestation; this is a
finite-source and authenticated-theta research calculus with explicit firewalls.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

from .recursive_model_interactions import (
    SourceCarrier, Model, global_fiber, goal_projection, min_unsat_cores
)
from .certified_contour_observer import authentic_theta_square
from .recursive_operator_gluing import certify_schur

class ProofCapsuleError(ValueError):pass

@dataclass(frozen=True)
class Capsule:
    kind: str
    source: str
    domain: str
    conclusion: tuple
    premises: frozenset[str]
    parent_capsules: tuple[str,...]
    status: str
    rh_proved: bool = False

    def __post_init__(self):
        if self.rh_proved:raise ProofCapsuleError('RH status cannot be introduced by finite meta rule')
        if self.kind not in ('RELATIONAL_CONSTRAINT','RELATIONAL_OBSTRUCTION','CONTOUR_ZERO_COUNT','RATIONAL_SCHUR_SIGN'):
            raise ProofCapsuleError('unknown proof-capsule rule')


def relation_capsule(carrier: SourceCarrier,roots:tuple[Model,...],scope):
    if not roots:raise ProofCapsuleError('at least one source hypothesis required')
    allowed=goal_projection(carrier,roots,scope)
    support=frozenset().union(*(m.support for m in roots))
    return Capsule('RELATIONAL_CONSTRAINT',carrier.source_id,
                   'FINITE_DECLARED_TABLE/'+','.join(carrier.scope(tuple(scope))),
                   tuple(sorted(allowed)),support,tuple(sorted(support)),
                   'PROVED_CONDITIONAL_ON_DECLARED_SOURCE_LAWS')


def obstruction_capsule(carrier,roots):
    if global_fiber(carrier,roots):
        raise ProofCapsuleError('no contradiction in the original source fiber')
    cores=min_unsat_cores(carrier,roots)
    return Capsule('RELATIONAL_OBSTRUCTION',carrier.source_id,
                   'FINITE_DECLARED_TABLE',tuple(tuple(sorted(c)) for c in cores),
                   frozenset().union(*cores),tuple(sorted({x for c in cores for x in c})),
                   'PROVED_CONDITIONAL_ON_DECLARED_SOURCE_LAWS')


def schur_capsule(A,C,B):
    c=certify_schur(A,C,B)
    return Capsule('RATIONAL_SCHUR_SIGN','DECLARED_FINITE_OPERATOR_SOURCE',
                   'FINITE_RATIONAL_MATRIX',
                   ('PSD' if c.complete_psd else 'NOT_PSD',
                    tuple(tuple(str(x) for x in r) for r in c.schur)),
                   frozenset(('A','B','C','POSITIVE_DEFINITE_A')),
                   ('SCHUR_CONGRUENCE',),
                   'PROVED_CONDITIONAL_ON_DECLARED_BLOCKS')


def contour_capsule(theta_data,halfwidth=Q(3),R=Q(11,2),comparison=13):
    c=authentic_theta_square(theta_data,halfwidth,R,comparison)
    if c.source_status!='AUTHENTIC_REPLAYED_INTEGER_THETA' or c.lower_clearance<=0:
        raise ProofCapsuleError('source replay and strict contour clearance required')
    return Capsule('CONTOUR_ZERO_COUNT','AUTHENTIC_Q_XI_COMPLETED_THETA',
                   'CCW_COMPLEX_SQUARE_CENTER_ONE_HALF_HALF_SIDE_'+str(halfwidth),
                   (c.count,),
                   frozenset(('ACTUAL_THETA_POISSON','SOURCE_INTERVAL_JETS',
                              'GLOBAL_COMPLEX_ERROR','ARGUMENT_PRINCIPLE')),
                   ('SOURCE_XI_JET_CERTIFICATE','POLYNOMIAL_WINDING_CERTIFICATE'),
                   'PROVED_MATHEMATICAL_SOURCE_BOUNDED_DOMAIN')


def combine_verified(first:Capsule,second:Capsule):
    """Compose matching same-source same-domain reports; NOT blind independence."""
    if first.source!=second.source or first.domain!=second.domain:
        raise ProofCapsuleError('source/domain incompatibility; no transport functor')
    if first.kind != second.kind:
        raise ProofCapsuleError('unjustified cross-language composition')
    if first.conclusion!=second.conclusion:
        raise ProofCapsuleError('two reports disagree: adjudication required')
    return Capsule(first.kind,first.source,first.domain,first.conclusion,
                   first.premises|second.premises,
                   first.parent_capsules+second.parent_capsules,
                   first.status if first.status==second.status else 'MIXED_PROVENANCE_NOT_BLIND_INDEPENDENCE')


def ask_global_weil_positivity(capsules):
    """No rule permits a bounded contour, finite source or Schur toy to prove RH."""
    if not capsules or any(not isinstance(c,Capsule) for c in capsules):
        raise ProofCapsuleError('rule-checked capsules required')
    raise ProofCapsuleError('UNVERIFIED: source-identical all-test Weil sign inequality absent')
