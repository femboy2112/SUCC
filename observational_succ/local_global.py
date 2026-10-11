"""Local/global finite observation comparison with strict causal prefix restriction.

The global model may have advanced farther in SUCC. We extract only the
locally observable, integrated prefix and reconstruct any shadow observable
from *that prefix*, never using the global model's future source leaves.

This is a finite observational-equivalence instrument, not RH undecidability,
physical relativity, or a theorem equating global mathematical models.
"""
from __future__ import annotations

from dataclasses import dataclass
import json

from .core import DomainError, BudgetExceeded, Scalar, ONE
from .engine import Engine, run_arithmetic
from .arithmetic import ShadowIndex, connected_audit
from .resource_probe import ValuationWord, ProbeBudget, compare_observers


@dataclass(frozen=True)
class Observation:
    n: int
    frame: str
    context: str
    probe: str
    value: Scalar

    def data(self):
        return {"n": self.n, "frame": self.frame,
                "context": self.context, "probe": self.probe,
                "value": self.value.data()}


def _integrated_prefix(engine, horizon):
    if not isinstance(engine, Engine) or not engine.arithmetic:
        raise DomainError("Observer comparison supports the causal N0 arithmetic adapter")
    if engine.frame.domain != "natural" or engine.frame.step != (1,):
        raise DomainError("The declared wavefront differs from unit natural SUCC")
    if type(horizon) is not int or not 0 <= horizon <= engine.limits.max_target:
        raise DomainError("Invalid finite interaction horizon")
    if any(r.kind == "reverse" for r in engine.records):
        raise DomainError("This comparator requires a forward journal; reversed histories require an enriched adapter")
    prefix = []
    for r in engine.records:
        if r.kind != "propagate":
            continue
        before = json.loads(r.before)
        pending = before.get("pending")
        if pending is None:
            raise DomainError("Malformed integration record")
        n = int(pending["coordinate"][0])
        # A natural-SUCC forward journal is ordered. Do not inspect a value
        # from the first event beyond the observer's declared wavefront.
        if n > horizon:
            break
        prefix.append(Observation(n, pending["frame"], pending["context"],
                                  pending["probe"], Scalar.from_data(pending["value"])))
    return tuple(prefix)


def compare_local_global(local: Engine, global_model: Engine, horizon: int,
                         *, shadow_targets=(6, 12), require_same_protocol=True):
    """Compare observations and shadow histories after causal restriction.

    No comparison of global target-label truth beyond the declared observer
    budget is made. A full global Engine history is passed by the investigator;
    its unseen suffix is NOT inspected for the finite comparison.
    """
    if local.frame.data() != global_model.frame.data():
        raise DomainError("Observer frames differ; provide a checked coordinate functor first")
    if local.conductor != global_model.conductor:
        raise DomainError("Character conductor differs; source protocols are not matched")
    if horizon > local.limits.max_target or horizon > global_model.limits.max_target:
        raise BudgetExceeded("Observation horizon exceeds an engine's declared limits")
    here = _integrated_prefix(local,horizon)
    above = _integrated_prefix(global_model,horizon)
    if len(here) < horizon or len(above) < horizon:
        return {"status":"incomplete_observation", "horizon":horizon,
                "local_integrations":len(here), "global_integrations_visible":len(above),
                "note":"Insufficient integrated events; absence is not a negative witness"}
    if require_same_protocol:
        same = here == above
    else:
        same = all(x.n == y.n and x.value == y.value for x,y in zip(here,above))
    first = next((n for n,(x,y) in enumerate(zip(here,above),1)
                  if (x != y if require_same_protocol else (x.n != y.n or x.value != y.value))),None)
    prefix_a={o.n:o.value for o in here}
    prefix_b={o.n:o.value for o in above}
    index_a=ShadowIndex(prefix_a,local.limits)
    index_b=ShadowIndex(prefix_b,global_model.limits)
    report=[]
    for target in shadow_targets:
        if type(target) is not int or not 2 <= target <= min(local.limits.max_target,global_model.limits.max_target):
            raise BudgetExceeded("Shadow target exceeds shared available semantic domain")
        x,y = index_a.entry(target),index_b.entry(target)
        audit_a=connected_audit(index_a,target,local.conductor) if target in prefix_a else None
        audit_b=connected_audit(index_b,target,global_model.conductor) if target in prefix_b else None
        report.append({"target":target, "local_shadow":x.data(),
                       "global_shadow_restricted":y.data(),
                       "equal":x.weight==y.weight and x.counts==y.counts and x.products==y.products,
                       "local_connected_source":audit_a,
                       "global_connected_source_restricted":audit_b,
                       "source_agrees":audit_a==audit_b,
                       "globally_actualized_here": target<=horizon})
    return {
        "status": "equivalent_on_declared_observations" if same else "distinguished",
        "horizon":horizon,
        "same_events": same,
        "first_difference_at_observation":first,
        "observations_checked":len(here),
        "shadow_comparisons":report,
        "protocol_sensitive":require_same_protocol,
        "global_suffix_read":False,
        "internal_model_equality_claimed":False,
        "epistemic_warning":
           "Equal accessible observations are not proof of equal hidden models, arithmetic axioms, global positivity, or RH"}


def prefix_demo():
    original=run_arithmetic(3)
    complete=run_arithmetic(12)
    mutant=run_arithmetic(12,overrides={6:Scalar("8/7")})
    at3=compare_local_global(original,mutant,3)
    at6=compare_local_global(run_arithmetic(6),mutant,6)
    assert at3["status"]=="equivalent_on_declared_observations"
    assert at6["status"]=="distinguished" and at6["first_difference_at_observation"]==6
    return {"local_at_3_vs_future_mutant":at3,
            "local_at_6_vs_realized_mutant":at6,
            "global_source_is_not_replaced_by_numeric_probeability":True}
