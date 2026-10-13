"""Partial, delayed, dependent evidence with exact finite coupling intervals.

Known marginal likelihoods do not define an observed joint likelihood.
The only probabilities here are conditional, declared mathematical source
laws. Neither posterior bounds nor noisy observations certify the source.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .relational_model_genetics import GeneticsError
from .source_coupling_bounds import frechet_bounds, probability


@dataclass(frozen=True)
class HypothesisMarginals:
    source_id: str
    epoch: int
    basis: str
    p_first: Q
    p_second: Q

    def __post_init__(self):
        if (not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0):
            raise GeneticsError("Missing source/epoch/basis for heuristic reports")
        probability(self.p_first)
        probability(self.p_second)


@dataclass(frozen=True)
class IntervalPosterior:
    lower: Q
    upper: Q
    attainable_corner_posteriors: tuple[Q, ...]
    h_joint_bounds: tuple[Q, Q]
    k_joint_bounds: tuple[Q, Q]


def posterior_both_yes_interval(prior_h: Q, h: HypothesisMarginals,
                                k: HypothesisMarginals) -> IntervalPosterior:
    """Exact sharp posterior range over all admissible separate couplings.

    Assumes a binary EXHAUSTIVE hypothesis class H,K and both reports true.
    Each model has its own unknown joint law, independently chosen in its
    Fréchet interval. Does NOT assume A and B are independent under H or K.
    """
    prior_h = probability(prior_h)
    if (h.source_id, h.epoch, h.basis) != (k.source_id, k.epoch, k.basis):
        raise GeneticsError("Two rival models must refer to the same source version")
    bh = frechet_bounds(h.p_first, h.p_second)
    bk = frechet_bounds(k.p_first, k.p_second)
    outcomes = set()
    for ph in (bh.lower, bh.upper):
        for pk in (bk.lower, bk.upper):
            denom = prior_h * ph + (1-prior_h) * pk
            if denom:
                outcomes.add(prior_h * ph / denom)
    if not outcomes:
        raise GeneticsError("The joint observation is impossible for all couplings")
    return IntervalPosterior(min(outcomes), max(outcomes),
                             tuple(sorted(outcomes)),
                             (bh.lower, bh.upper), (bk.lower, bk.upper))


@dataclass(frozen=True)
class ConditionalTwoReceipt:
    source_id: str
    epoch: int
    basis: str
    a_yes_h: Q
    a_yes_k: Q
    b_yes_given_a_h: Q
    b_yes_given_a_k: Q

    def __post_init__(self):
        if not self.source_id or not self.basis \
                or type(self.epoch) is not int or self.epoch < 0:
            raise GeneticsError("Conditional kernel requires a lawful source version")
        for v in (self.a_yes_h, self.a_yes_k,
                  self.b_yes_given_a_h, self.b_yes_given_a_k):
            probability(v)


def posterior_two_yes(prior_h: Q, joint: ConditionalTwoReceipt) -> Q:
    """Chain rule; B|A comes from one joint conditional source law."""
    prior_h = probability(prior_h)
    h = joint.a_yes_h * joint.b_yes_given_a_h
    k = joint.a_yes_k * joint.b_yes_given_a_k
    d = prior_h * h + (1-prior_h) * k
    if d == 0:
        raise GeneticsError("Conditioned-on event has zero source probability")
    return prior_h * h / d


@dataclass(frozen=True)
class EventBatch:
    source_id: str
    basis: str
    event_epoch: int
    reported_epoch: int
    likelihood_h: Q
    likelihood_k: Q

    def __post_init__(self):
        if (not self.source_id or not self.basis
                or type(self.event_epoch) is not int or self.event_epoch < 0
                or type(self.reported_epoch) is not int
                or self.reported_epoch < self.event_epoch):
            raise GeneticsError("A delayed receipt cannot precede its source event")
        probability(self.likelihood_h)
        probability(self.likelihood_k)


def epoch_conditioned_updates(
        prior_by_epoch: dict[int, Q], batches: tuple[EventBatch, ...],
        *, source_id: str, basis: str) -> dict[int, Q]:
    """One full-joint outcome batch per epoch, no undeclared transition.

    The event's source epoch, NOT arrival time, determines which hypothesis
    distribution can be updated. Different epochs retain separate priors.
    A second dependent report for the same event epoch needs a new explicit
    joint conditional kernel rather than an accidental product.
    """
    if not source_id or not basis:
        raise GeneticsError("Missing source contract")
    result = {}
    for epoch, prior in prior_by_epoch.items():
        if type(epoch) is not int or epoch < 0:
            raise GeneticsError("Malformed source epoch")
        result[epoch] = probability(prior)
    seen = set()
    for receipt in batches:
        if (receipt.source_id, receipt.basis) != (source_id, basis):
            raise GeneticsError("Unproved source/base transport")
        e = receipt.event_epoch
        if e not in result:
            raise GeneticsError("No independently declared prior for source epoch")
        if e in seen:
            raise GeneticsError("Dependent same-epoch reports require a joint law")
        seen.add(e)
        prior = result[e]
        denom = prior * receipt.likelihood_h + (1-prior) * receipt.likelihood_k
        if not denom:
            raise GeneticsError("Reported event was impossible for all rival models")
        result[e] = prior * receipt.likelihood_h / denom
    return result


def uncertainty_demo() -> dict:
    h = HypothesisMarginals("declared-noisy-source", 0, "paired", Q(3, 4), Q(3, 4))
    k = HypothesisMarginals("declared-noisy-source", 0, "paired", Q(1, 4), Q(1, 4))
    interval = posterior_both_yes_interval(Q(1, 2), h, k)
    duplicated = ConditionalTwoReceipt("declared-noisy-source", 0, "paired",
                                        Q(3, 4), Q(1, 4), Q(1), Q(1))
    independent = ConditionalTwoReceipt("declared-noisy-source", 0, "paired",
                                         Q(3, 4), Q(1, 4),
                                         Q(3, 4), Q(1, 4))
    delayed = (
        EventBatch("declared-noisy-source", "paired", 0, 1, Q(3, 4), Q(1, 4)),
        EventBatch("declared-noisy-source", "paired", 1, 1, Q(1, 3), Q(2, 3)),
    )
    updated = epoch_conditioned_updates({0: Q(1, 2), 1: Q(1, 2)},
                                         delayed, source_id="declared-noisy-source",
                                         basis="paired")
    return {
        "robust_posterior_interval": [str(interval.lower), str(interval.upper)],
        "independence_point_estimate": "9/10",
        "duplicated_conditional_receipt_posterior": str(posterior_two_yes(Q(1, 2), duplicated)),
        "new_conditionally_independent_receipt_posterior": str(posterior_two_yes(Q(1, 2), independent)),
        "source_event_epoch_posteriors": {str(e): str(p) for e, p in updated.items()},
        "unobserved_source_class_certified": False,
        "cross_epoch_transition_assumed": False,
        "physical_calibration_claimed": False,
    }
