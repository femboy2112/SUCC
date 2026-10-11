"""Operational distinguishability under finite semantic observation.

This is a theorem about finite RATIONAL probability distributions and
classical postprocessing channels, motivated by an observer whose
physical measurement outcome is represented in a semantic vocabulary.

The statement is the total-variation data-processing inequality:

    TV(C*p, C*q) <= TV(p, q).

C is column-stochastic, so triangle inequality and positivity prove
the bound. No RH, Gödel oracle, physical model of a human brain, or
mathematical truth predicate enters the derivation.

The module also accepts outcome probabilities from the existing,
validated finite real-qubit Kraus instrument. The readout can discard
distinguishing information without erasing the original causal
measurement record. This is a MODEL of semantic lossy compression,
not an empirical theory of real-world understanding.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


class SemanticChannelError(ValueError):
    """Malformed finite probability, readout map or source domain."""


def _fraction(q) -> Fraction:
    if type(q) is int or isinstance(q, Fraction):
        return Fraction(q)
    raise SemanticChannelError("Only exact integers and Fractions are supported")


def _labels(seq, *, title) -> tuple[str, ...]:
    if type(seq) is not tuple or not 1 <= len(seq) <= 64:
        raise SemanticChannelError(f"{title} must be an immutable, nonempty bounded tuple")
    if any(type(x) is not str or not x or len(x) > 128 for x in seq):
        raise SemanticChannelError(f"{title} labels must be nonempty bounded strings")
    if len(seq) != len(set(seq)):
        raise SemanticChannelError(f"{title} labels must be unique")
    return seq


@dataclass(frozen=True)
class Evidence:
    """A normalized rational probability law over named observable outcomes."""
    labels: tuple[str, ...]
    weights: tuple[Fraction, ...]

    def __post_init__(self):
        _labels(self.labels, title="Evidence")
        if type(self.weights) is not tuple or len(self.weights) != len(self.labels):
            raise SemanticChannelError("Each evidence label must have one probability")
        probs = tuple(_fraction(w) for w in self.weights)
        if any(w < 0 for w in probs) or sum(probs, Fraction()) != 1:
            raise SemanticChannelError("Probabilities must be nonnegative and total exactly one")
        object.__setattr__(self, "weights", probs)

    @classmethod
    def from_counts(cls, labels: tuple[str, ...], counts: tuple[int, ...]):
        _labels(labels, title="Count source")
        if type(counts) is not tuple or len(labels) != len(counts):
            raise SemanticChannelError("Counts must match source labels")
        if any(type(n) is not int or n < 0 for n in counts) or not sum(counts) > 0:
            raise SemanticChannelError("Counts must be nonnegative integers with positive total")
        total = sum(counts)
        return cls(labels, tuple(Fraction(n, total) for n in counts))


@dataclass(frozen=True)
class SemanticReadout:
    """A declared stochastic map from physical outcomes to semantic symbols.

    rows[i][j] = P(output_j | input_i), each input row sums to one.
    The operation NEVER modifies source evidence/measurement history.
    """
    input_labels: tuple[str, ...]
    output_labels: tuple[str, ...]
    rows: tuple[tuple[Fraction, ...], ...]

    def __post_init__(self):
        _labels(self.input_labels, title="Readout input")
        _labels(self.output_labels, title="Readout output")
        if type(self.rows) is not tuple or len(self.rows) != len(self.input_labels):
            raise SemanticChannelError("One stochastic row is required per input")
        clean = []
        for row in self.rows:
            if type(row) is not tuple or len(row) != len(self.output_labels):
                raise SemanticChannelError("Stochastic output row has the wrong shape")
            values = tuple(_fraction(x) for x in row)
            if any(x < 0 for x in values) or sum(values, Fraction()) != 1:
                raise SemanticChannelError("Each row must be nonnegative and sum exactly to one")
            clean.append(values)
        object.__setattr__(self, "rows", tuple(clean))

    @classmethod
    def identity(cls, labels: tuple[str, ...]):
        _labels(labels, title="Identity labels")
        return cls(labels, labels, tuple(
            tuple(Fraction(int(i == j)) for j in range(len(labels)))
            for i in range(len(labels))
        ))

    def pushforward(self, distribution: Evidence) -> Evidence:
        if not isinstance(distribution, Evidence) or distribution.labels != self.input_labels:
            raise SemanticChannelError("Source evidence has the wrong named readout domain")
        out = tuple(sum((distribution.weights[i] * self.rows[i][j]
                         for i in range(len(self.input_labels))), Fraction())
                    for j in range(len(self.output_labels)))
        return Evidence(self.output_labels, out)

    def then(self, later: "SemanticReadout") -> "SemanticReadout":
        """Compose channels exactly; preserve the direction and type."""
        if not isinstance(later, SemanticReadout) or self.output_labels != later.input_labels:
            raise SemanticChannelError("Readout composition requires matching named interface")
        composed = tuple(
            tuple(sum((row[j] * later.rows[j][k]
                       for j in range(len(self.output_labels))), Fraction())
                  for k in range(len(later.output_labels)))
            for row in self.rows
        )
        return SemanticReadout(self.input_labels, later.output_labels, composed)


def total_variation(a: Evidence, b: Evidence) -> Fraction:
    if not isinstance(a, Evidence) or not isinstance(b, Evidence) or a.labels != b.labels:
        raise SemanticChannelError("Compare only distributions over identical named observations")
    return sum((abs(x-y) for x, y in zip(a.weights, b.weights)), Fraction()) / 2


@dataclass(frozen=True)
class DataProcessingCertificate:
    """A fully exact rational bound, for the declared input distributions."""
    before: Fraction
    after: Fraction
    slack: Fraction
    source_distinct: bool
    readout_distinct: bool
    general_theorem: str
    theorem_proved_from_channel_axioms: bool


def data_processing(a: Evidence, b: Evidence, channel: SemanticReadout):
    """Proof-bearing finite instance of total-variation contraction.

    For Δ_i = a_i-b_i, by positivity:
       Σ_j |Σ_i C_ij Δ_i| <= Σ_j Σ_i C_ij |Δ_i|
                                = Σ_i |Δ_i|.
    The right equality uses row-stochasticity. This proves the
    inequality for *every* pair of distributions; the function
    also checks its exact rational instance and reports the slack.
    """
    if not isinstance(channel, SemanticReadout):
        raise SemanticChannelError("Data processing requires a declared stochastic readout")
    before = total_variation(a, b)
    pa, pb = channel.pushforward(a), channel.pushforward(b)
    after = total_variation(pa, pb)
    if after > before:
        raise ArithmeticError("A stochastic semantic channel violated data-processing inequality")
    return DataProcessingCertificate(
        before, after, before-after, before>0, after>0,
        "TV(Cp,Cq) <= TV(p,q) by positive row-stochastic triangle inequality",
        True,
    )


def qubit_outcome_evidence(instrument, density):
    """Read probabilities from the exact real-qubit physical instrument."""
    from .quantum_records import Instrument
    if not isinstance(instrument, Instrument):
        raise SemanticChannelError("Physical evidence must come from a validated Kraus instrument")
    outcomes = instrument.probabilities(density)
    labels = tuple(outcomes)
    return Evidence(labels, tuple(outcomes[x] for x in labels))


def measurement_semantic_probe() -> dict:
    """Real-qubit example: Z distinguishes |0> and |1>, X does not.

    A subsequent forgetful symbol channel erases even the Z evidence.
    This demonstrates loss under observation/semantic processing,
    not loss of the underlying physical source or causal history.
    """
    from .quantum_records import INITIAL_ZERO, measure_x, measure_z

    initial_one = ((Fraction(0), Fraction(0)),
                   (Fraction(0), Fraction(1)))
    z, x = measure_z(), measure_x()
    z0 = qubit_outcome_evidence(z, INITIAL_ZERO)
    z1 = qubit_outcome_evidence(z, initial_one)
    x0 = qubit_outcome_evidence(x, INITIAL_ZERO)
    x1 = qubit_outcome_evidence(x, initial_one)
    forget = SemanticReadout(
        z0.labels, ("observed",), ((Fraction(1),), (Fraction(1),))
    )
    true_z = data_processing(z0, z1, SemanticReadout.identity(z0.labels))
    forgotten = data_processing(z0, z1, forget)
    true_x = total_variation(x0, x1)
    assert true_z.before == 1 and true_z.after == 1
    assert forgotten.after == true_x == 0
    return {
        "status": "EXACT_SEMANTIC_DATA_PROCESSING",
        "Z_outcomes_0_vs_1_TV": str(true_z.after),
        "X_outcomes_0_vs_1_TV": str(true_x),
        "Z_forgotten_TV": str(forgotten.after),
        "source_distinguishable_before_forgetting": True,
        "semantic_readout_invertible": False,
        "source_causal_records_erased": False,
        "physical_brain_model_claimed": False,
        "Weil_positivity_claimed": False,
    }
