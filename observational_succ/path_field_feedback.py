"""Exact finite distinctions between conditioning, reinforcement, and field growth.

The resistor model is a declared classical toy, not a stochastic BBP model.
The timeline factory uses the native bidirectional_source_histories interface;
its Doob machinery and the graph Dirichlet theory are inherited. A Polya/Beta
identity, same-endpoint path discriminator, and deterministic-factor firewall
have paper proofs in the accompanying research dossier. Tests certify finite
instances. None of these results proves selected arithmetic cancellation.

All probabilities and potentials are rational. Source-linked checks reuse the
native zero-seed BBP authenticator and formal rational character representation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .succ_internal_matrix_walk import PhasePoly, authentic_r


class PathFieldError(ValueError):
    """Invalid exact probability, finite path, field, or source factor."""


def _rational(value):
    if type(value) not in (int, Q):
        raise PathFieldError("exact integer/Fraction required, not float or bool")
    return Q(value)


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise PathFieldError(f"{name} must be an exact integer at least {minimum}")
    return value


def _probabilities(values):
    out = tuple(_rational(value) for value in values)
    if not out or min(out) < 0 or sum(out) != 1:
        raise PathFieldError("nonnegative exact probabilities of total mass one required")
    return out


def _word(word):
    if type(word) is not str or any(letter not in "LR" for letter in word):
        raise PathFieldError("a finite word over L and R is required")
    return word


@dataclass(frozen=True)
class TwoArmField:
    """Two unit-resistance arms with a perfectly conducting realized prefix.

Both arms have the same original number of edges. The shared source and each
realized prefix have potential zero; the remote endpoint has potential one.
Growth chooses between the two frontier edges proportionally to their currents
(the declared eta=1 rule). A completed connection is a terminal state.
"""

    length: int
    left_steps: int
    right_steps: int

    def __post_init__(self):
        _integer(self.length, "arm length", 2)
        _integer(self.left_steps, "left realized prefix")
        _integer(self.right_steps, "right realized prefix")
        if max(self.left_steps, self.right_steps) >= self.length:
            raise PathFieldError("the growth model stops when an arm reaches the endpoint")

    def potential_profile(self, arm):
        if arm not in ("L", "R"):
            raise PathFieldError("arm must be L or R")
        realized = self.left_steps if arm == "L" else self.right_steps
        return tuple(Q(max(0, node - realized), self.length - realized)
                     for node in range(self.length + 1))

    @property
    def currents(self):
        return Q(1, self.length - self.left_steps), Q(1, self.length - self.right_steps)

    @property
    def next_left(self):
        left, right = self.currents
        return left / (left + right)


def polya_next_left(left, right, alpha=1, beta=1):
    """Linear branch-count reinforcement, also a static Beta posterior mean."""
    _integer(left, "left count")
    _integer(right, "right count")
    alpha, beta = _rational(alpha), _rational(beta)
    if min(alpha, beta) <= 0:
        raise PathFieldError("positive prior/reinforcement weights required")
    return (alpha + left) / (alpha + beta + left + right)


def branch_timeline(horizon, model, *, arm_length=3, alpha=1, beta=1):
    """Build this toy's labelled count graph for the EXISTING path-law engine.

The result is (layers, kernels, initial), accepted without coercion by
bidirectional_source_histories.source_path_law and its native Doob conditioner.
For harmonic growth, the horizon ends by the earliest possible breakthrough.
"""
    _integer(horizon, "finite comparison horizon")
    if horizon > 12:
        raise PathFieldError("the exhaustive toy timeline has horizon at most twelve")
    branch_path_probability("", model, arm_length=arm_length, alpha=alpha, beta=beta)
    if model == "harmonic" and horizon > arm_length:
        raise PathFieldError("timeline would continue after a possible completed connection")
    layers = tuple(tuple((left, time - left) for left in range(time + 1))
                   for time in range(horizon + 1))
    kernels = []
    for layer in layers[:-1]:
        rows = {}
        for left, right in layer:
            if model == "fixed":
                probability = Q(1, 2)
            elif model == "reinforced":
                probability = polya_next_left(left, right, alpha, beta)
            else:
                probability = TwoArmField(arm_length, left, right).next_left
            rows[(left, right)] = (("L", (left + 1, right), probability),
                                   ("R", (left, right + 1), 1 - probability))
        kernels.append(rows)
    return layers, tuple(kernels), {(0, 0): Q(1)}


def branch_path_probability(word, model, *, arm_length=3, alpha=1, beta=1):
    """Probability of one ordered branch word under three explicitly different laws.

``fixed`` means known independent fair choices. ``reinforced`` increments the
chosen branch's positive weight. ``harmonic`` recomputes the two-arm Dirichlet
field after each realized edge; it stops at first completed connection.
"""
    word = _word(word)
    if model not in ("fixed", "reinforced", "harmonic"):
        raise PathFieldError("unknown declared path model")
    # Validate parameters even when the word is empty.
    if model == "reinforced":
        polya_next_left(0, 0, alpha, beta)
    if model == "harmonic":
        TwoArmField(arm_length, 0, 0)
    left = right = 0
    mass = Q(1)
    for letter in word:
        if model == "fixed":
            next_left = Q(1, 2)
        elif model == "reinforced":
            next_left = polya_next_left(left, right, alpha, beta)
        else:
            next_left = TwoArmField(arm_length, left, right).next_left
        mass *= next_left if letter == "L" else 1 - next_left
        left += letter == "L"
        right += letter == "R"
    return mass


def _rising(value, count):
    result = Q(1)
    for index in range(count):
        result *= value + index
    return result


def static_beta_path_probability(word, alpha=1, beta=1):
    """Integrate theta^L(1-theta)^R against one time-independent Beta bias.

The beta-integral ratio is exact for rational positive alpha,beta and integer
counts. Equality with the reinforced path law holds for every finite word,
not just for the one-step predictive mean. It does not identify interventions.
"""
    word = _word(word)
    alpha, beta = _rational(alpha), _rational(beta)
    if min(alpha, beta) <= 0:
        raise PathFieldError("positive Beta parameters required")
    left, right = word.count("L"), word.count("R")
    return (_rising(alpha, left) * _rising(beta, right) /
            _rising(alpha + beta, left + right))


def projection_leakage(weights, projected_successors, expected_successor):
    """Mass assigned to an arithmetic successor other than the selected one."""
    weights = _probabilities(weights)
    projected = tuple(_rational(value) for value in projected_successors)
    expected = _rational(expected_successor)
    if len(weights) != len(projected):
        raise PathFieldError("one projected successor per auxiliary outcome required")
    return sum((weight for weight, value in zip(weights, projected) if value != expected), Q())


def factor_character_modulus_lower_bound(weights, projected_successors, expected_successor):
    """Uniform bound max(0,1-2*epsilon) when epsilon leaves the selected successor.

For every unit character, the good outcomes contribute the same unit phase;
the other outcomes can change the conditional mean by at most 2*epsilon.
This is a lower bound on a single lifted transition, not on a time average.
"""
    leakage = projection_leakage(weights, projected_successors, expected_successor)
    return max(Q(), 1 - 2 * leakage)


@dataclass(frozen=True)
class FactorCharacterCertificate:
    """A single conditional transition, not a claim about arithmetic time averages."""

    expected_successor: Q
    frequency: int
    character: PhasePoly
    character_square: PhasePoly


def deterministic_factor_character(weights, projected_successors, expected_successor, frequency):
    """Certify that auxiliary mixing cannot alter a preserved deterministic factor.

If pi(Y')=T(pi(Y)) almost surely conditional on the current selected state,
then E[f(pi(Y'))|Y]=f(T(pi(Y))). The formal-character instance has square one.
Deterministic systems may nevertheless have cancellation across source times.
"""
    weights = _probabilities(weights)
    projected = tuple(_rational(value) for value in projected_successors)
    expected = _rational(expected_successor)
    if type(frequency) is not int:
        raise PathFieldError("an exact integer frequency is required")
    if projection_leakage(weights, projected, expected) != 0:
        raise PathFieldError("auxiliary transition changes the selected arithmetic factor")
    character = sum((weight * PhasePoly.monomial(frequency * value)
                     for weight, value in zip(weights, projected)), PhasePoly.zero())
    target = PhasePoly.monomial(frequency * expected)
    if character != target or character * character.star() != PhasePoly.one():
        raise ArithmeticError("deterministic-factor character identity failed")
    return FactorCharacterCertificate(expected, frequency, character, character * character.star())


@dataclass(frozen=True)
class AuthenticBBPFactorCertificate:
    source_index: int
    current: Q
    forcing: Q
    factor: FactorCharacterCertificate


def authenticated_bbp_factor_character(states, source_index, weights, projected_successors, frequency):
    """Use the native full-prefix authenticator, including U_0=0 and all four poles.

``source_index`` is the literal r(n) index, so n=1 checks U_0 -> U_1.
The auxiliary row is declared input, not a source-derived feedback law.
"""
    from .lambda_source_duality import verify_original_history

    _integer(source_index, "source index", 1)
    if not verify_original_history(states) or source_index > len(states):
        raise PathFieldError("a complete authentic zero-seeded BBP prefix is required")
    current = Q() if source_index == 1 else states[source_index - 2]
    forcing = authentic_r(source_index)
    expected = 16 * current + forcing
    factor = deterministic_factor_character(weights, projected_successors, expected, frequency)
    return AuthenticBBPFactorCertificate(source_index, current, forcing, factor)
