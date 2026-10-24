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
    """A reported countermodel with separately audited source membership.

    Strings are NOT evidence of class membership. membership_checked records
    only the result of a caller-supplied FINITE executable checker, which does
    not establish the soundness of an arbitrary universal mathematical class.
    The negative margin is exact arithmetic; theorem authority remains external.
    """

    claim: str
    witness: str
    membership: str
    violation: F
    membership_checked: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(self, "violation", _q(self.violation, "violation"))

    @property
    def refutes(self) -> bool:
        """Relative to a supplied, executed finite membership checker only."""
        return self.violation < 0 and self.membership_checked

    @property
    def negative_margin(self) -> bool:
        return self.violation < 0

    def report(self) -> str:
        kind = ("FINITE-CHECKED REFUTATION RELATIVE TO SUPPLIED CHECKER"
                if self.refutes else
                "UNVERIFIED MEMBERSHIP: negative margin alone is NOT a refutation"
                if self.negative_margin else
                "does NOT refute (violation >= 0)")
        return (f"[M2] {kind}: claim={self.claim!r}\n"
                f"     witness={self.witness}\n"
                f"     membership={self.membership}\n"
                f"     exact violation={self.violation}")


def exact_countermodel(claim: str, witness: str, membership: str,
                       violation, *, source_witness=None,
                       membership_checker=None) -> Countermodel:
    """Package a negative-margin witness with an optional finite source checker.

    With no checker, refutes=False even when violation is negative.
    A supplied predicate does not by itself constitute an independent proof
    that the source belongs to the full mathematical hypothesis class.
    """
    if membership_checker is not None and not callable(membership_checker):
        raise MechanismError("membership checker must be callable")
    checked = False
    if membership_checker is not None:
        result = membership_checker(source_witness)
        if type(result) is not bool:
            raise MechanismError("membership checker must return an exact bool")
        checked = result
    return Countermodel(claim=claim, witness=witness,
                        membership=membership, violation=_q(violation, "violation"),
                        membership_checked=checked)


# --------------------------------------------------------------------- M8
@dataclass(frozen=True)
class ThresholdReport:
    """The exact flip value of the conclusion and the distance to it."""

    threshold: F
    available: F
    direction: str          # > means true above the bracket
    exact: bool
    lower: F | None = None
    upper: F | None = None

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
                f"     DYADIC threshold bracket = [{self.lower}, {self.upper}]\n"
                f"     exact threshold identified = {self.exact}")


def threshold_bisect(predicate: Callable[[F], bool], lo, hi,
                     direction: str = ">", steps: int = 96) -> F:
    """Rational midpoint of a finite dyadic threshold BRACKET.

    Caller must prove monotonicity separately. Exact Fraction arithmetic
    does not identify the true real threshold in finite time in general.
    """
    a,b=threshold_bisect_interval(predicate,lo,hi,direction,steps)
    return (a+b)/2


def threshold_report(predicate, lo, hi, available, direction=">",
                     steps: int = 96) -> ThresholdReport:
    """Exact dyadic ARITHMETIC produces a bracket, NOT an exact real threshold."""
    a,b=threshold_bisect_interval(predicate,lo,hi,direction,steps)
    return ThresholdReport(threshold=(a+b)/2,
                           available=_q(available, "available"),
                           direction=direction, exact=False, lower=a,upper=b)


def threshold_bisect_interval(predicate, lo, hi, direction=">", steps=96):
    """Return a dyadic threshold bracket, assuming caller's monotonicity claim."""
    lo, hi = _q(lo,"lo"),_q(hi,"hi")
    if type(steps) is not int or steps<1 or direction not in (">","<"):
        raise MechanismError("valid direction and positive steps required")
    plo,phi=bool(predicate(lo)),bool(predicate(hi))
    if plo==phi:
        raise MechanismError("predicate is not separating on supplied bracket")
    if (direction==">" and (plo or not phi)) or (direction=="<" and (not plo or phi)):
        raise MechanismError("endpoint truth orientation contradicts direction")
    for _ in range(steps):
        mid=(lo+hi)/2
        if bool(predicate(mid))==plo:
            lo=mid
        else:
            hi=mid
    return lo,hi


# --------------------------------------------------------------------- M1
@dataclass(frozen=True)
class CriterionAudit:
    """Metadata-only diagnostic about premises and known failure modes.

    It does not prove the caller's Boolean claims, source faithfulness,
    functorial injectivity on hom-sets, or target-relative sufficiency.
    Those are distinct mathematical proof obligations.
    """

    target: str
    premise: str
    generic_in_x: bool
    premise_equivalent_to_target: bool
    falsifier_named: bool
    failure_observable_at_target: bool = True
    structural_feature_killed_in_one_step: bool = False

    @property
    def verdict(self) -> str:
        if self.premise_equivalent_to_target:
            return "TAUTOLOGY: premise is equivalent to target; no relocation"
        if not self.falsifier_named:
            return "HOLLOW: no stated way the premise could be false"
        if self.structural_feature_killed_in_one_step:
            return ("TRANSIENT_QUOTIENT_WARNING: supplied feature vanishes under a "
                    "claimed quotient, but the full source may still control future "
                    "dynamics; prove a source/action/readout commuting diagram")
        if not self.failure_observable_at_target:
            return ("TARGET_TEST_INCOMPLETE: a hidden failure may invalidate "
                    "target sufficiency; this metadata cannot prove categorical "
                    "non-faithfulness or absence of a source factor")
        if self.generic_in_x:
            return ("GENERIC IMPLICATION: may be useful only after proving its "
                    "premise for the authenticated selected source; generic "
                    "applicability is not a mathematical failure")
        return "OK: criterion is specific, falsifiable and faithful"

    def report(self) -> str:
        return (f"[M1] target={self.target!r}\n"
                f"     premise={self.premise!r}\n"
                f"     verdict={self.verdict}")


def criterion_audit(target: str, premise: str, generic_in_x: bool,
                    premise_equivalent_to_target: bool,
                    falsifier_named: bool,
                    failure_observable_at_target: bool = True,
                    structural_feature_killed_in_one_step: bool = False,
                    ) -> CriterionAudit:
    for name, v in (("generic_in_x", generic_in_x),
                    ("premise_equivalent_to_target", premise_equivalent_to_target),
                    ("falsifier_named", falsifier_named),
                    ("failure_observable_at_target", failure_observable_at_target),
                    ("structural_feature_killed_in_one_step",
                     structural_feature_killed_in_one_step)):
        if type(v) is not bool:
            raise MechanismError(f"{name} must be a bool")
    return CriterionAudit(target=target, premise=premise,
                          generic_in_x=generic_in_x,
                          premise_equivalent_to_target=premise_equivalent_to_target,
                          falsifier_named=falsifier_named,
                          failure_observable_at_target=failure_observable_at_target,
                          structural_feature_killed_in_one_step=(
                              structural_feature_killed_in_one_step))


__all__ = ["MechanismError", "Countermodel", "exact_countermodel",
           "ThresholdReport", "threshold_bisect", "threshold_bisect_interval", "threshold_report",
           "CriterionAudit", "criterion_audit"]