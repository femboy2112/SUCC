"""Exact joint-kernel descent for source-changing stochastic instruments.

The instrument supplies probabilities of BOTH successor state and receipt.
Support equality, equal unconditional successor laws, or equal normalized
posteriors alone are weaker contracts.  No empirical likelihood is invented.
This implements finite strong lumpability of an output-labelled kernel.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .causal_nerode_succ import SourceChart, SourceTransportError


def _probabilities(values: tuple[Q, ...], size: int) -> None:
    if (type(values) is not tuple or len(values) != size
            or any(type(p) is not Q or p < 0 for p in values)
            or sum(values, Q(0)) != 1):
        raise SourceTransportError("Expected a normalized exact rational law")


@dataclass(frozen=True)
class JointInstrument:
    """Rows are flattened (after-state, receipt) probabilities in that order."""

    name: str
    before: SourceChart
    after: SourceChart
    receipts: tuple[str, ...]
    rows: tuple[tuple[Q, ...], ...]
    source_class_complete: bool = True

    def __post_init__(self) -> None:
        if (type(self.name) is not str or not self.name
                or self.before.source_id != self.after.source_id
                or self.before.basis != self.after.basis
                or self.after.epoch < self.before.epoch
                or type(self.receipts) is not tuple or not self.receipts
                or len(set(self.receipts)) != len(self.receipts)
                or any(type(z) is not str or not z for z in self.receipts)
                or type(self.rows) is not tuple
                or len(self.rows) != len(self.before.states)
                or type(self.source_class_complete) is not bool):
            raise SourceTransportError("Invalid source/epoch/basis instrument contract")
        for row in self.rows:
            _probabilities(row, len(self.after.states) * len(self.receipts))

    def report_receipt_row(self, state: str) -> tuple[Q, ...]:
        """Joint pushforward J_s(r,z), not a guessed conditional law."""
        if state not in self.before.states:
            raise SourceTransportError("State outside declared source")
        row = self.rows[self.before.states.index(state)]
        outputs = self.after.image()
        width = len(self.receipts)
        result = [Q(0)] * (len(outputs) * width)
        for i, report in enumerate(self.after.observations):
            j = outputs.index(report)
            for k in range(width):
                result[j * width + k] += row[i * width + k]
        return tuple(result)


@dataclass(frozen=True)
class JointDescent:
    descended: bool
    source_class_certified: bool
    witness: tuple[str, str, str, tuple[Q, ...], tuple[Q, ...]] | None
    observer_rows: tuple[tuple[str, tuple[Q, ...]], ...]
    repaired_reports: tuple[tuple[str, tuple[str, tuple[Q, ...]]], ...]


def joint_descent(instrument: JointInstrument) -> JointDescent:
    """Exact iff and canonical ONE-STEP pair repair (q(s), J_s).

    Repair is a sufficient mathematical statistic, not an available sensor
    and not automatically a stable quotient for a later instrument.
    """
    representatives = {}
    witness = None
    repaired = []
    for state in instrument.before.states:
        report = instrument.before.report(state)
        row = instrument.report_receipt_row(state)
        repaired.append((state, (report, row)))
        if report in representatives:
            other, oldrow = representatives[report]
            if oldrow != row and witness is None:
                witness = (other, state, report, oldrow, row)
        else:
            representatives[report] = (state, row)
    descended = witness is None
    observer_rows = tuple((r, representatives[r][1])
                          for r in instrument.before.image()) if descended else ()
    return JointDescent(descended, descended and instrument.source_class_complete,
                        witness, observer_rows, tuple(repaired))


def push_reports(chart: SourceChart, prior: tuple[Q, ...]) -> tuple[Q, ...]:
    _probabilities(prior, len(chart.states))
    return tuple(sum((p for p, r in zip(prior, chart.observations) if r == report),
                     Q(0)) for report in chart.image())


@dataclass(frozen=True)
class BayesUpdate:
    evidence: Q
    posterior: tuple[Q, ...] | None


def _normalize(weights: tuple[Q, ...]) -> BayesUpdate:
    total = sum(weights, Q(0))
    return BayesUpdate(total, tuple(p / total for p in weights) if total else None)


def source_filter(instrument: JointInstrument, prior: tuple[Q, ...],
                  receipt: str) -> BayesUpdate:
    """Fine successor posterior; impossible receipts retain None, not a prior."""
    _probabilities(prior, len(instrument.before.states))
    if receipt not in instrument.receipts:
        raise SourceTransportError("Receipt outside instrument alphabet")
    k = instrument.receipts.index(receipt)
    width = len(instrument.receipts)
    weights = tuple(sum((prior[i] * row[j * width + k]
                         for i, row in enumerate(instrument.rows)), Q(0))
                    for j in range(len(instrument.after.states)))
    return _normalize(weights)


def observer_filter(instrument: JointInstrument, prior: tuple[Q, ...],
                    receipt: str) -> BayesUpdate:
    """Coarse filtering requires a certified complete mathematical source."""
    _probabilities(prior, len(instrument.before.image()))
    if receipt not in instrument.receipts:
        raise SourceTransportError("Receipt outside instrument alphabet")
    certificate = joint_descent(instrument)
    if not certificate.source_class_certified:
        raise SourceTransportError("No globally certified joint-kernel descent")
    k = instrument.receipts.index(receipt)
    width = len(instrument.receipts)
    rows = dict(certificate.observer_rows)
    weights = tuple(sum((prior[i] * rows[report][j * width + k]
                         for i, report in enumerate(instrument.before.image())), Q(0))
                    for j in range(len(instrument.after.image())))
    return _normalize(weights)


def filter_history(instruments: tuple[JointInstrument, ...],
                   prior: tuple[Q, ...], receipts: tuple[str, ...]) -> dict:
    """Replay a fixed finite source-changing path; prove no adaptive execution.

    The general induction also covers actions chosen from coarse receipt
    history if EVERY selected action separately satisfies joint descent.
    This function executes supplied instrument choices only.
    """
    if not instruments or len(instruments) != len(receipts):
        raise SourceTransportError("Nonempty matched instrument/receipt path required")
    for left, right in zip(instruments, instruments[1:]):
        if left.after != right.before:
            raise SourceTransportError("Stale or incompatible intermediate source chart")
    _probabilities(prior, len(instruments[0].before.states))
    fine = prior
    coarse = push_reports(instruments[0].before, fine)
    likelihood = Q(1)
    steps = []
    for instrument, receipt in zip(instruments, receipts):
        f = source_filter(instrument, fine, receipt)
        c = observer_filter(instrument, coarse, receipt)
        if f.evidence != c.evidence:
            raise AssertionError("Evidence likelihood failed to descend")
        likelihood *= f.evidence
        if f.posterior is None:
            if c.posterior is not None:
                raise AssertionError("Impossible fine receipt became possible")
            return {"possible": False, "likelihood": likelihood,
                    "posterior": None, "steps": tuple(steps)}
        fine = f.posterior
        coarse = c.posterior
        if push_reports(instrument.after, fine) != coarse:
            raise AssertionError("Bayesian report square failed")
        steps.append((f.evidence, coarse))
    return {"possible": True, "likelihood": likelihood,
            "posterior": coarse, "steps": tuple(steps)}
