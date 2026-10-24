"""Executable proof-mechanism audit: three small transducers.

Companion to docs/PROOF_MECHANISMS.md. These are *meta* tools: they do not
produce mathematical theorem content, they audit the SHAPE of an argument so
that the failure modes catalogued in the dossier are caught mechanically.

  M2  exact_countermodel   -- refute a universal claim with an exact witness
  M8  threshold_bisect     -- find the exact parameter value at which the
                              conclusion would flip, and compare to what is
                              available (the "distance to threshold" report)
  M1  criterion_audit      -- check that a conditional criterion is not a
                              tautology and not vacuous

All arithmetic is exact (int / Fraction). No floats anywhere: a float input is
an error, not a convenience.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Callable, Iterable, Sequence


class MechanismError(ValueError):
    """A malformed audit input. Not a mathematical claim."""


def _q(x, name: str) -> F:
    if type(x) is bool or not isinstance(x, (int, F)):
        raise MechanismError(f"{name}: exact int/Fraction required, got {type(x).__name__}")
    return F(x)


# --------------------------------------------------------------------- M2
@dataclass(frozen=True)
class Countermodel:
    """An exact refutation of a universally quantified claim.

    `witness` is the claimed member of the hypothesis class, `membership` is the
    exact evidence it really is one (the most-skipped step), `violation` is the
    exact signed margin by which the claim fails.
    """

    claim: str
    witness: str
    membership: str
    violation: F

    def __post_init__(self) -> None:
        object.__setattr__(self, "violation", _q(self.violation, "violation"))

    @property
    def refutes(self) -> bool:
        return self.violation < 0

    def report(self) -> str:
        kind = "REFUTES" if self.refutes else "does NOT refute (violation >= 0)"
        return (f"[M2] {kind}: claim={self.claim!r}\n"
                f"     witness={self.witness}\n"
                f"     membership={self.membership}\n"
                f"     exact violation={self.violation}")


def exact_countermodel(claim: str, witness: str, membership: str,
                       violation) -> Countermodel:
    """Wrap an exact countermodel, refusing a non-negative margin.

    A 'countermodel' whose violation is zero or positive is not a refutation;
    this is returned as such rather than silently promoted.
    """
    return Countermodel(claim=claim, witness=witness,
                        membership=membership, violation=_q(violation, "violation"))


# --------------------------------------------------------------------- M8
@dataclass(frozen=True)
class ThresholdReport:
    """The exact flip value of the conclusion and the distance to it."""

    threshold: F
    available: F
    direction: str          # ">" if the conclusion holds when param > threshold
    exact: bool

    @property
    def ratio(self) -> F | None:
        if self.threshold == 0:
            return None
        return abs(self.available / self.threshold)

    def report(self) -> str:
        r = self.ratio
        rtxt = f"{float(r):.4g}" if r is not None else "undefined"
        return (f"[M8] conclusion holds for param {self.direction} threshold\n"
                f"     exact threshold = {self.threshold}\n"
                f"     available       = {self.available}\n"
                f"     distance ratio  = {rtxt}\n"
                f"     exact bisection = {self.exact}")


def threshold_bisect(predicate: Callable[[F], bool], lo, hi,
                     direction: str = ">", steps: int = 96) -> F:
    """Exact bisection for the flip point of a monotone predicate.

    `predicate(p)` must be monotone in p and `predicate(lo) != predicate(hi)`.
    Returns the largest dyadic-rational p with `predicate(p)` true when
    direction == '>', else the smallest. Exact: no float is used.
    """
    lo, hi = _q(lo, "lo"), _q(hi, "hi")
    if type(steps) is not int or steps < 1:
        raise MechanismError("steps >= 1 integer required")
    plo, phi = bool(predicate(lo)), bool(predicate(hi))
    if plo == phi:
        raise MechanismError("predicate is not separating on [lo, hi]")
    if direction not in (">", "<"):
        raise MechanismError("direction must be '>' or '<'")
    for _ in range(steps):
        mid = (lo + hi) / 2
        if bool(predicate(mid)) == plo:
            lo = mid
        else:
            hi = mid
    return lo if direction == ">" else hi


def threshold_report(predicate, lo, hi, available, direction=">",
                     steps: int = 96) -> ThresholdReport:
    thr = threshold_bisect(predicate, lo, hi, direction, steps)
    return ThresholdReport(threshold=thr,
                           available=_q(available, "available"),
                           direction=direction, exact=True)


# --------------------------------------------------------------------- M1
@dataclass(frozen=True)
class CriterionAudit:
    """Shape audit of a conditional criterion `Target <= Premise`."""

    target: str
    premise: str
    generic_in_x: bool
    premise_equivalent_to_target: bool
    falsifier_named: bool

    @property
    def verdict(self) -> str:
        if self.premise_equivalent_to_target:
            return "TAUTOLOGY: premise is equivalent to target; no relocation"
        if not self.falsifier_named:
            return "HOLLOW: no stated way the premise could be false"
        if self.generic_in_x:
            return ("GENERIC: criterion holds for every source; cannot "
                    "discriminate the target from a generic one")
        return "OK: criterion is specific and falsifiable"

    def report(self) -> str:
        return (f"[M1] target={self.target!r}\n"
                f"     premise={self.premise!r}\n"
                f"     verdict={self.verdict}")


def criterion_audit(target: str, premise: str, generic_in_x: bool,
                    premise_equivalent_to_target: bool,
                    falsifier_named: bool) -> CriterionAudit:
    for name, v in (("generic_in_x", generic_in_x),
                    ("premise_equivalent_to_target", premise_equivalent_to_target),
                    ("falsifier_named", falsifier_named)):
        if type(v) is not bool:
            raise MechanismError(f"{name} must be a bool")
    return CriterionAudit(target=target, premise=premise,
                          generic_in_x=generic_in_x,
                          premise_equivalent_to_target=premise_equivalent_to_target,
                          falsifier_named=falsifier_named)


__all__ = ["MechanismError", "Countermodel", "exact_countermodel",
           "ThresholdReport", "threshold_bisect", "threshold_report",
           "CriterionAudit", "criterion_audit"]