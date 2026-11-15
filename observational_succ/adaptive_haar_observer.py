"""A declared four-state Bayesian experiment with a structural Haar channel.

S is a persistent connection bit; theta is a persistent target sign.  In the
independent fair-target family, the deep probe reports theta when S=1 and a
fresh fair sign when S=0.  Structural observations depend only on S.  Their
likelihoods, conditional freshness and physical applicability are assumptions,
not facts authenticated by this module.

The exact core retains the FULL joint posterior of (S, theta).  Resetting it to
an independent fair-target prior after a deep observation is unsound.  Existing
contextual_heuristics supplies source/epoch/receipt and replay gates; existing
heuristic_evidence_martingales supplies predictable-policy likelihood ratios.
This module adds a particular structural-to-Haar/information/option-value
interface, not a new Bayesian rule, physical attraction or quantum mechanism.

Fractions certify probabilities, projection energies and information intervals.
Functions ending in _nats and the Gibbs/two-stage policy interfaces use ordinary
floating point; their outputs are numerical recommendations, not certificates.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import exp, fsum, isfinite, log, log1p

from .recursive_observer import JointInstrument, rational


STATES = ((0, -1), (0, 1), (1, -1), (1, 1))
OUTCOMES = (-1, 1)
MAX_SERIES_TERMS = 128
MAX_REPETITIONS = 256
MAX_POLICY_ACTIONS = 16


def _probability(value) -> Q:
    value = rational(value)
    if not 0 <= value <= 1:
        raise ValueError("Probability must be an exact int/Fraction in [0, 1]")
    return value


def _outcome(value) -> int:
    if type(value) is not int or value not in OUTCOMES:
        raise ValueError("Outcome must be the integer sign -1 or +1")
    return value


def _bounded_integer(value, maximum: int, label: str, minimum: int = 0) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{label} must be an integer in {minimum}..{maximum}")
    return value


def _finite_number(value, label: str) -> float:
    if type(value) not in (int, float) and not isinstance(value, Q):
        raise ValueError(f"{label} must be a finite real numeric value")
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{label} must have a finite floating-point value") from exc
    if not isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


@dataclass(frozen=True)
class ConnectionBelief:
    """Normalized exact weights, in the order declared by STATES."""

    weights: tuple[Q, Q, Q, Q]

    def __post_init__(self):
        if type(self.weights) is not tuple or len(self.weights) != 4:
            raise ValueError("Exactly four joint-state weights in a tuple required")
        weights = tuple(_probability(w) for w in self.weights)
        if sum(weights, Q(0)) != 1:
            raise ValueError("Joint-state weights must sum to one")
        object.__setattr__(self, "weights", weights)

    @classmethod
    def independent_fair(cls, connection_probability) -> ConnectionBelief:
        p = _probability(connection_probability)
        return cls(((1 - p) / 2, (1 - p) / 2, p / 2, p / 2))

    @property
    def connection_probability(self) -> Q:
        return self.weights[2] + self.weights[3]

    @property
    def target_positive_probability(self) -> Q:
        return self.weights[1] + self.weights[3]

    @property
    def target_mean(self) -> Q:
        return 2 * self.target_positive_probability - 1

    @property
    def is_independent_fair(self) -> bool:
        return self.weights[0] == self.weights[1] and self.weights[2] == self.weights[3]


@dataclass(frozen=True)
class BinaryProbe:
    """P(report=+1 | S,theta) in STATES order; no hidden state transition.

    Repeating this kernel means fresh noise conditionally independent given
    (S,theta).  A copied old report instead has a deterministic conditional
    kernel after its original value is in the history.  Naming or relabelling
    a probe does not establish freshness or source authenticity.
    """

    name: str
    positive_likelihoods: tuple[Q, Q, Q, Q]

    def __post_init__(self):
        if type(self.name) is not str or not self.name:
            raise ValueError("A nonempty probe name required")
        if type(self.positive_likelihoods) is not tuple or len(self.positive_likelihoods) != 4:
            raise ValueError("Exactly four positive-report likelihoods required")
        object.__setattr__(self, "positive_likelihoods",
                           tuple(_probability(p) for p in self.positive_likelihoods))

    def likelihoods(self, outcome: int) -> tuple[Q, ...]:
        outcome = _outcome(outcome)
        if outcome == 1:
            return self.positive_likelihoods
        return tuple(1 - p for p in self.positive_likelihoods)

    def as_joint_instrument(self, cost=1) -> JointInstrument:
        """Adapter to the inherited source instrument, with identity transition.

        Outcome index 0 means -1, index 1 means +1.  Cost is a declared
        deterministic resource charge, not an additional source observation.
        """
        joint = tuple(tuple(((1 - p, p) if x == xp else (Q(0), Q(0)))
                            for xp in range(4))
                      for x, p in enumerate(self.positive_likelihoods))
        return JointInstrument(joint, rational(cost), self.name)


DEEP_PROBE = BinaryProbe("deep-connection", (Q(1, 2), Q(1, 2), Q(0), Q(1)))


def structural_probe(positive_if_connected, positive_if_unconnected) -> BinaryProbe:
    """Coarse C with P(C=+|S=1)=a, P(C=+|S=0)=b."""
    a = _probability(positive_if_connected)
    b = _probability(positive_if_unconnected)
    return BinaryProbe("structural-connection", (b, b, a, a))


def observe(belief: ConnectionBelief, probe: BinaryProbe, outcome: int):
    """Return (exact likelihood, posterior); an impossible event returns (0,None)."""
    if not isinstance(belief, ConnectionBelief) or not isinstance(probe, BinaryProbe):
        raise ValueError("Declared ConnectionBelief and BinaryProbe required")
    likelihoods = probe.likelihoods(outcome)
    weights = tuple(w * l for w, l in zip(belief.weights, likelihoods))
    probability = sum(weights, Q(0))
    if probability == 0:
        return Q(0), None
    return probability, ConnectionBelief(tuple(w / probability for w in weights))


def target_response_joint(belief: ConnectionBelief, probe: BinaryProbe):
    """Exact 2x2 joint law; rows theta=-1,+1, columns report=-1,+1."""
    if not isinstance(belief, ConnectionBelief) or not isinstance(probe, BinaryProbe):
        raise ValueError("Declared ConnectionBelief and BinaryProbe required")
    return tuple(tuple(sum((belief.weights[i] * probe.likelihoods(y)[i]
                            for i, (_, target) in enumerate(STATES) if target == t), Q(0))
                       for y in OUTCOMES) for t in OUTCOMES)


def target_detail_energy(belief: ConnectionBelief, probe: BinaryProbe = DEEP_PROBE) -> Q:
    """Exact Var(E[theta|report]), the reduction in squared-error Bayes risk."""
    joint = target_response_joint(belief, probe)
    initial_mean = belief.target_mean
    energy = Q(0)
    for j in range(2):
        mass = joint[0][j] + joint[1][j]
        if mass:
            conditional_mean = (joint[1][j] - joint[0][j]) / mass
            energy += mass * (conditional_mean - initial_mean) ** 2
    return energy


def hidden_link_haar_coefficient(belief: ConnectionBelief) -> Q:
    """The mixed theta*Y Haar coefficient p, only in the independent fair family."""
    if not isinstance(belief, ConnectionBelief) or not belief.is_independent_fair:
        raise ValueError("The p-only Haar formula requires the independent fair-target family")
    return belief.connection_probability


def posterior_link_after_successes(p, a, b, count: int) -> Q:
    """p*a^n / (p*a^n+(1-p)*b^n), for declared conditionally FRESH successes.

    This helper does not inspect receipts and cannot certify independence.
    An impossible sequence raises instead of constructing a posterior.
    """
    p, a, b = _probability(p), _probability(a), _probability(b)
    count = _bounded_integer(count, MAX_REPETITIONS, "Repetition count")
    connected = p * a ** count
    total = connected + (1 - p) * b ** count
    if total == 0:
        raise ValueError("The declared success sequence is impossible")
    return connected / total


def structural_promotion_energy(p, a, b) -> Q:
    """Exact Var(P(S=1|C)) = increase in expected deep detail energy.

    With q=P(C=+), the nondegenerate value is
    p^2*(1-p)^2*(a-b)^2/[q*(1-q)].  This is the squared weighted Haar
    coefficient of S on C.  It is not the immediate information about theta.
    """
    p, a, b = _probability(p), _probability(a), _probability(b)
    q = p * a + (1 - p) * b
    if q == 0 or q == 1:
        return Q(0)
    return p * p * (1 - p) ** 2 * (a - b) ** 2 / (q * (1 - q))


def hidden_link_information_interval(p, terms: int = 32) -> tuple[Q, Q]:
    """Certified rational bounds on I(p)=sum_{k>=1} p^(2k)/[2k(2k-1)].

    A geometric majorant bounds the remainder for p<1.  At p=1 use the
    rapidly convergent ln(2)=2*atanh(1/3) series.  The returned interval is
    mathematical; the separate floating-point information API is approximate.
    """
    p = _probability(p)
    terms = _bounded_integer(terms, MAX_SERIES_TERMS, "Series terms", 1)
    if p == 0:
        return Q(0), Q(0)
    if p == 1:
        x = Q(1, 3)
        lower = 2 * sum((x ** (2 * k + 1) / (2 * k + 1)
                         for k in range(terms)), Q(0))
        tail = 2 * x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
        return lower, lower + tail
    square = p * p
    lower = sum((square ** k / (2 * k * (2 * k - 1))
                 for k in range(1, terms + 1)), Q(0))
    geometric_tail = square ** (terms + 1) / (
        (2 * terms + 2) * (2 * terms + 1) * (1 - square))
    # The alternating harmonic remainder for ln(2) is at most 1/(2N+1).
    endpoint_tail = square ** (terms + 1) / (2 * terms + 1)
    return lower, lower + min(geometric_tail, endpoint_tail)


def _log_fraction(value: Q) -> float:
    if Q(1, 2) <= value <= 2:
        return log1p(float(value - 1))
    return log(value.numerator) - log(value.denominator)


def target_information_nats(belief: ConnectionBelief, probe: BinaryProbe = DEEP_PROBE) -> float:
    """Numerical I(theta;report) under the FULL current joint belief.

    Exact zero cells are omitted.  A negative floating-point rounding residue
    is clipped to zero.  Tiny positive information can round/underflow to zero;
    this API does not certify vanishing information or exact policy ties.
    """
    joint = target_response_joint(belief, probe)
    rows = tuple(sum(row, Q(0)) for row in joint)
    columns = tuple(sum((row[j] for row in joint), Q(0)) for j in range(2))
    return max(0.0, fsum(float(joint[i][j]) * _log_fraction(
        joint[i][j] / (rows[i] * columns[j]))
        for i in range(2) for j in range(2) if joint[i][j]))


def hidden_link_information_nats(p) -> float:
    """Numerical family I(p); p alone is not sufficient after arbitrary observations."""
    p = _probability(p)
    if p == 0:
        return 0.0
    if p == 1:
        return log(2.0)
    value = float(p)
    if value <= 0.5:
        # Positive series avoids cancellation of the linear terms near p=0.
        return fsum(value ** (2 * k) / (2 * k * (2 * k - 1))
                    for k in range(1, 33))
    if value == 1.0:
        return log(2.0)
    return ((1 + value) * log1p(value) + (1 - value) * log1p(-value)) / 2


@dataclass(frozen=True)
class TwoStagePlan:
    """Approximate net information utilities, all costs measured in nats."""

    direct_deep_net: float
    immediate_preparatory_net: float
    preparatory_then_optional_deep_net: float
    deep_after_outcome: tuple[bool, bool]
    first_action: str


def two_stage_information_plan(belief: ConnectionBelief, preparatory: BinaryProbe,
                               *, preparatory_cost, deep_cost) -> TwoStagePlan:
    """Compare stop, one deep probe, and preparatory-then-optional-deep.

    This is this declared three-plan menu, not an unrestricted multistep optimum.
    The preparatory report is retained; its target information plus conditional
    deep information gives the total by the chain rule.  Conditional fresh
    probe noise and deterministic costs are required.  Numerical ties stop.
    """
    c = _finite_number(preparatory_cost, "Preparatory cost")
    d = _finite_number(deep_cost, "Deep cost")
    if c < 0 or d < 0:
        raise ValueError("Information costs must be nonnegative")
    immediate = target_information_nats(belief, preparatory) - c
    direct = target_information_nats(belief, DEEP_PROBE) - d
    continuation_values = []
    choices = []
    for outcome in OUTCOMES:
        probability, posterior = observe(belief, preparatory, outcome)
        net = target_information_nats(posterior, DEEP_PROBE) - d if posterior else 0.0
        choices.append(bool(probability and net > 0))
        continuation_values.append(float(probability) * max(net, 0.0))
    staged = immediate + fsum(continuation_values)
    # Ordering resolves numerical ties toward fewer probes.
    first = max(((0.0, "stop"), (direct, "deep"), (staged, "preparatory")),
                key=lambda item: item[0])[1]
    return TwoStagePlan(direct, immediate, staged, tuple(choices), first)


def gibbs_probe_policy(reference: tuple[Q, ...], utilities: tuple,
                       temperature=1.0) -> tuple[float, ...]:
    """Numerical pi(a) proportional to q(a)*exp(V(a)/temperature).

    Reference probabilities are exact and normalized; zero reference mass
    remains zero.  Temperature is positive.  Very unfavorable supported
    actions can additionally underflow to zero in floating point.  Utilities
    and the prior action menu are declared, not inferred from correlations.
    """
    if (type(reference) is not tuple or type(utilities) is not tuple or
            not 1 <= len(reference) <= MAX_POLICY_ACTIONS or len(reference) != len(utilities)):
        raise ValueError("Matching finite policy tuples of size 1..16 required")
    reference = tuple(_probability(p) for p in reference)
    if sum(reference, Q(0)) != 1:
        raise ValueError("Reference action probabilities must sum to one")
    utilities = tuple(_finite_number(v, "Utility") for v in utilities)
    temperature = _finite_number(temperature, "Temperature")
    if temperature <= 0:
        raise ValueError("Temperature must be positive")
    center = max(v for p, v in zip(reference, utilities) if p)
    scores = tuple((_log_fraction(p) + (v - center) / temperature if p else float("-inf"))
                   for p, v in zip(reference, utilities))
    peak = max(scores)
    weights = tuple(exp(s - peak) if p else 0.0 for p, s in zip(reference, scores))
    total = fsum(weights)
    return tuple(w / total for w in weights)
