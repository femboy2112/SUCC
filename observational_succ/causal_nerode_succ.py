"""Source-changing observation descent and *minimal* repair.

The mathematical question is whether a source intervention U:S0->S1
descends through reports q0:S0->O0 and q1:S1->O1:
                   q1 ∘ U = V ∘ q0.
The criterion is a fiber/kernel-pair inclusion, NOT a confidence score.
When it fails, (q0, q1∘U) is the coarsest refinement that makes a
one-step successor report representable. This does *not* invent a real
physical sensor, license a counterfactual reset, or transport an arbitrary
original-source claim.

All source laws are explicitly declared finite simulators. Composition and
proof support require exact source/basis/epoch contracts. No RH implication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from typing import Any


class SourceTransportError(ValueError):
    """A typed source, mathematical law or resource constraint failed."""


@dataclass(frozen=True)
class SourceChart:
    source_id: str
    epoch: int
    basis: str
    states: tuple[str, ...]
    observations: tuple[str, ...]  # total report law, aligned to states

    def __post_init__(self):
        if (not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.states) is not tuple or not self.states
                or len(set(self.states)) != len(self.states)
                or any(type(s) is not str or not s for s in self.states)
                or type(self.observations) is not tuple
                or len(self.observations) != len(self.states)
                or any(type(o) is not str or not o for o in self.observations)):
            raise SourceTransportError("Source chart requires total typed finite reports")

    def report(self, state: str) -> str:
        try:
            return dict(zip(self.states, self.observations))[state]
        except KeyError as ex:
            raise SourceTransportError("State outside its source chart") from ex

    def image(self) -> tuple[str, ...]:
        return tuple(sorted(set(self.observations)))

    def fibers(self) -> tuple[tuple[str, tuple[str, ...]], ...]:
        return tuple((o, tuple(s for s in self.states if self.report(s) == o))
                     for o in self.image())


@dataclass(frozen=True)
class CausalInstrument:
    name: str
    before: SourceChart
    after: SourceChart
    transitions: tuple[str, ...]  # total deterministic U:S0->S1
    cost: Q = Q(1)
    reset_available: bool = False
    source_authenticated: bool = False

    def __post_init__(self):
        if (not self.name or type(self.transitions) is not tuple
                or len(self.transitions) != len(self.before.states)
                or any(x not in self.after.states for x in self.transitions)
                or self.before.source_id != self.after.source_id
                or self.before.basis != self.after.basis
                or self.after.epoch < self.before.epoch
                or not isinstance(self.cost, Q) or self.cost <= 0
                or type(self.reset_available) is not bool
                or type(self.source_authenticated) is not bool):
            raise SourceTransportError(
                "Action must provide a total causal source/basis/epoch and cost contract")
        # The flag cannot authenticate a source; this simulator deliberately
        # rejects forged positive authentication claims.
        if self.source_authenticated:
            raise SourceTransportError("Declared simulator cannot attest physical source")

    def step(self, state: str) -> str:
        try:
            return dict(zip(self.before.states, self.transitions))[state]
        except KeyError as ex:
            raise SourceTransportError("Action state outside declared source") from ex

    def future_report(self, state: str) -> str:
        return self.after.report(self.step(state))


@dataclass(frozen=True)
class FiberObstruction:
    state_a: str
    state_b: str
    before_report: str
    future_a: str
    future_b: str


@dataclass(frozen=True)
class CausalDescentCertificate:
    source_id: str
    before_epoch: int
    after_epoch: int
    basis: str
    source_action: str
    descended: bool
    witness: FiberObstruction | None
    observed_successor: tuple[tuple[str, str], ...]
    repaired_reports: tuple[tuple[str, tuple[str, str]], ...]
    original_report_classes: int
    repaired_report_classes: int
    minimum_extra_fixed_width_bits: int
    extra_code: tuple[tuple[str, str], ...]
    repaired_successor: tuple[tuple[tuple[str, str], str], ...]
    physical_extra_probe_available: bool
    physical_source_authenticated: bool = False


def causal_descent(action: CausalInstrument) -> CausalDescentCertificate:
    """Exact kernel inclusion + constructive smallest sufficient refinement.

    Any decoder of both the previous and future report factors the pair.
    The integer bit lower bound is conditional on an available fixed-width
    supplemental channel with decoder knowing the original report.
    """
    before = action.before
    fibers = before.fibers()
    witness = None
    decoded = []
    repaired = []
    extra_code = {}
    max_splits = 1
    for current, states in fibers:
        next_values = sorted({action.future_report(s) for s in states})
        if len(next_values) > 1 and witness is None:
            a = states[0]
            b = next(s for s in states if action.future_report(s) !=
                     action.future_report(a))
            witness = FiberObstruction(
                a, b, current, action.future_report(a), action.future_report(b))
        max_splits = max(max_splits, len(next_values))
        if len(next_values) == 1:
            decoded.append((current, next_values[0]))
        width = (len(next_values)-1).bit_length()
        codes = {r: format(i, "0%db" % width) if width else ""
                 for i, r in enumerate(next_values)}
        for s in states:
            extra_code[s] = codes[action.future_report(s)]
    # Each old report fiber can reuse its local codebook, but the physical
    # hypothetical supplemental channel has one GLOBAL fixed width.
    global_width = (max_splits - 1).bit_length()
    extra_code = {s: extra_code[s].zfill(global_width) for s in before.states}
    repair_map = {s: (before.report(s), action.future_report(s))
                  for s in before.states}
    repaired = tuple((s, repair_map[s]) for s in before.states)
    successors = tuple(sorted({(repair_map[s], action.future_report(s))
                               for s in before.states}))
    if len(successors) != len(set(repair_map.values())):
        raise AssertionError("The constructed repair must define one target per fiber")
    if any(extra_code[a] == extra_code[b] and before.report(a) ==
           before.report(b) and action.future_report(a) != action.future_report(b)
           for a, b in product(before.states, repeat=2)):
        raise AssertionError("Failed to build source-relative minimal extra binary code")
    classes = len(set(repair_map.values()))
    if classes < len(fibers):
        raise AssertionError("Observation refinement paradox")
    return CausalDescentCertificate(
        before.source_id, before.epoch, action.after.epoch, before.basis,
        action.name, witness is None, witness,
        tuple(decoded) if witness is None else (),
        repaired, len(fibers), classes,
        global_width,
        tuple((s, extra_code[s]) for s in before.states),
        successors, False, False,
    )


def verify_refinement_factorization(
        action: CausalInstrument, proposed: tuple[tuple[str, str], ...]
        ) -> bool:
    """Verify whether an independent candidate observation r:S->R suffices.

    If both q0 and q1∘U factor through r, the canonical pair necessarily
    factors through r. Return false for bad candidate, not invented repair.
    """
    if tuple(s for s, _ in proposed) != action.before.states:
        raise SourceTransportError("Candidate must preserve ordered source domain")
    r = dict(proposed)
    grouped: dict[str, list[str]] = {}
    for s, y in proposed:
        grouped.setdefault(y, []).append(s)
    sufficient = all(
        len({action.before.report(s) for s in fiber}) == 1 and
        len({action.future_report(s) for s in fiber}) == 1
        for fiber in grouped.values())
    if sufficient:
        pair = {s: (action.before.report(s), action.future_report(s))
                for s in action.before.states}
        if any(pair[a] != pair[b] for a, b in product(action.before.states, repeat=2)
               if r[a] == r[b]):
            raise AssertionError("Independent sufficient refinement failed universal map")
    return sufficient


def compose_instruments(first: CausalInstrument,
                        second: CausalInstrument) -> CausalInstrument:
    """Composite original-source action, not composition of an invalid V."""
    if (first.after.source_id != second.before.source_id
            or first.after.epoch != second.before.epoch
            or first.after.basis != second.before.basis
            or first.after.states != second.before.states
            or first.after.observations != second.before.observations):
        raise SourceTransportError("No licensed intermediate source/context square")
    return CausalInstrument(
        first.name + ";" + second.name, first.before, second.after,
        tuple(second.step(first.step(s)) for s in first.before.states),
        first.cost + second.cost,
        first.reset_available and second.reset_available,
    )


@dataclass(frozen=True)
class ClaimAudit:
    before_claim_reportable: bool
    after_claim_reportable: bool
    intervention_preserves_original_claim: bool
    witness: tuple[str, str, str] | None
    observation_square_commutes: bool
    original_claim_transport_certified: bool


def audit_original_claim(action: CausalInstrument,
                         before_truth: tuple[bool, ...],
                         after_truth: tuple[bool, ...]) -> ClaimAudit:
    """A correct observational square is NOT an original-claim proof.

    Even reportable claims can have their truth flipped by an intervention.
    """
    if (type(before_truth) is not tuple or type(after_truth) is not tuple
            or len(before_truth) != len(action.before.states)
            or len(after_truth) != len(action.after.states)
            or any(type(x) is not bool for x in before_truth + after_truth)):
        raise SourceTransportError("Claim must be total Boolean source predicates")
    bp = dict(zip(action.before.states, before_truth))
    ap = dict(zip(action.after.states, after_truth))

    def reportable(chart: SourceChart, truth: dict[str, bool]) -> bool:
        return all(len({truth[s] for s in fiber}) == 1
                   for _, fiber in chart.fibers())

    p, q = reportable(action.before, bp), reportable(action.after, ap)
    mismatch = next(((s, str(bp[s]), str(ap[action.step(s)]))
                     for s in action.before.states
                     if bp[s] != ap[action.step(s)]), None)
    descending = causal_descent(action).descended
    return ClaimAudit(p, q, mismatch is None, mismatch, descending,
                      p and q and mismatch is None and descending)


def causal_repair_demo() -> dict[str, Any]:
    states = ("00", "01", "10", "11")
    # An observer reports only the first bit; the source update exchanges
    # the bits. Previously invisible second-bit differences become visible.
    before = SourceChart("source-v1", 0, "bits", states,
                         ("0", "0", "1", "1"))
    after = SourceChart("source-v1", 1, "bits", states,
                        ("0", "0", "1", "1"))
    switch = CausalInstrument("bit-swap", before, after,
                              ("00", "10", "01", "11"), Q(3, 2))
    receipt = causal_descent(switch)
    if receipt.descended or receipt.minimum_extra_fixed_width_bits != 1:
        raise AssertionError("Bit-swap must reveal a real one-bit transport gap")
    # Repeating the involution brings original report back, even though
    # each one-step attempt had an observational obstruction.
    end = SourceChart("source-v1", 2, "bits", states,
                      ("0", "0", "1", "1"))
    backward = CausalInstrument("bit-swap-again", after, end,
                                switch.transitions, Q(3, 2))
    composite = compose_instruments(switch, backward)
    composite_receipt = causal_descent(composite)
    if not composite_receipt.descended:
        raise AssertionError("Two identical bit swaps must be observational identity")

    identity = CausalInstrument("identity", before, before, states)
    flip_original_truth = audit_original_claim(identity,
                                                (False, False, True, True),
                                                (True, True, False, False))
    return {
        "one_step_source_obstruction": {
            "pair": [receipt.witness.state_a, receipt.witness.state_b],
            "old_shared_report": receipt.witness.before_report,
            "new_distinct_reports": [receipt.witness.future_a, receipt.witness.future_b],
            "one_step_v_exists": receipt.descended,
            "minimum_new_binary_bits": receipt.minimum_extra_fixed_width_bits,
            "canonical_augmented_states": receipt.repaired_report_classes,
        },
        "second_step_observational_identity": composite_receipt.descended,
        "first_step_obstruction_not_erased": not receipt.descended,
        "claim_transport_not_automatic": not flip_original_truth.original_claim_transport_certified,
        "physical_reset_and_probe_available": switch.reset_available,
        "external_source_authenticated": False,
    }
