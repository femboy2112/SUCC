"""Bind a finite operational observational_succ journal to categorical observations.

This intentionally does NOT collapse shadow histories, observable scalar
coefficients, and object identity into one 'truth' or a claimed Weil metric.
"""
from __future__ import annotations

from .core import BudgetExceeded, DomainError
from .engine import Engine
from .yoneda import (DivisibilityCategory, PathCategory, forget_path_bridge,
                     restricted_yoneda)
from .resource_probe import (ProbeBudget, ValuationWord, compare_observers)


class Phenomenology:
    """A finite *probe regime* over the actual integrated event leaves.

    Two separate lenses:
      thin hom(j,target): extensional divisibility,
      path hom(j,target): intensional available ordered multiplication histories.

    Global objects are provided as formal shadow TARGETS; this does not grant
    the local observer an oracle that has already encountered their coefficients.
    """
    def __init__(self, engine: Engine, *, max_shadow_target=None, max_paths=10000):
        if not isinstance(engine, Engine) or not engine.arithmetic:
            raise DomainError("Arithmetic phenomenology requires an arithmetic Engine")
        if engine.frame.domain != "natural" or engine.frame.dimension != 1:
            raise DomainError("Phenomenology arithmetic adapter needs N0")
        self.engine=engine
        self.max_shadow_target = engine.limits.max_target if max_shadow_target is None else max_shadow_target
        if type(self.max_shadow_target) is not int or not 2 <= self.max_shadow_target <= engine.limits.max_target:
            raise BudgetExceeded("Shadow category must fit engine's finite target bound")
        known = engine.coefficients
        self.probes = tuple(sorted(n for n in known if 1 <= n <= self.max_shadow_target))
        self.multipliers = tuple(sorted(n for n in known if 2 <= n <= self.max_shadow_target))
        self.thin = DivisibilityCategory(tuple(range(1,self.max_shadow_target+1)))
        self.path = None if not self.multipliers else PathCategory(tuple(range(1,self.max_shadow_target+1)),
                                                             self.multipliers, max_paths=max_paths,
                                                             max_depth=engine.limits.max_depth)
        self.forget = None if self.path is None else forget_path_bridge(self.path)

    @property
    def horizon(self):
        return int(self.engine.coordinate[0])

    def _target(self, n):
        if type(n) is not int or not 2 <= n <= self.max_shadow_target:
            raise DomainError("Target is not in this bounded semantic category")
        return n

    def witness(self, n):
        n = self._target(n)
        thin_sig = restricted_yoneda(self.thin, n, self.probes)
        path_sig = None if self.path is None else restricted_yoneda(self.path,n,self.probes)
        shadow = self.engine.shadow(n, witnesses=True)
        return {"target":n, "horizon":self.horizon, "source_probes":list(self.probes),
                "coordinate_visited":self.horizon>=n,
                "observational_succ":shadow["stage"],
                "thin_representable_hom_sizes":[len(x) for x in thin_sig],
                "path_representable_hom_sizes":None if path_sig is None else [len(x) for x in path_sig],
                "shadow_weight":shadow["weight"],
                "shadow_histories":shadow["occurrences"],
                "histories_complete":shadow["complete"],
                "source_audit":shadow.get("source"),
                "epistemic_scope":"declared finite source and probe category; not global truth"}

    def compare(self, a,b):
        a,b=self._target(a),self._target(b)
        thin_a=restricted_yoneda(self.thin,a,self.probes)
        thin_b=restricted_yoneda(self.thin,b,self.probes)
        path_a=None if self.path is None else restricted_yoneda(self.path,a,self.probes)
        path_b=None if self.path is None else restricted_yoneda(self.path,b,self.probes)
        # The category-aware path profile stores all Hom(factors) words, not
        # merely a numeric endpoint. Full naturality is checked separately.
        resource=compare_observers(ValuationWord.from_integer(a),
                                   ValuationWord.from_integer(b),
                                   ProbeBudget(max(1,self.horizon)))
        return {"horizon":self.horizon, "targets":[a,b],
                "thin_indistinguishable":thin_a == thin_b,
                "path_indistinguishable":None if self.path is None else path_a == path_b,
                "thin_signature_a":[len(x) for x in thin_a],
                "thin_signature_b":[len(x) for x in thin_b],
                "path_signature_a":None if path_a is None else [len(x) for x in path_a],
                "path_signature_b":None if path_b is None else [len(x) for x in path_b],
                "earliest_full_divisibility_probe":resource.data(),
                "shadow_a":self.engine.shadow(a),
                "shadow_b":self.engine.shadow(b),
                "warning":"A target supplied by the caller is a semantic shadow object, not an observed source event"}

    def verify_forgetful_transport(self):
        if self.forget is None:
            return {"status":"no_observed_multipliers","source_count":len(self.probes)}
        return {**self.forget.verify(), **self.forget.hom_faithfulness()}


def example():
    from .engine import run_arithmetic
    eng=run_arithmetic(3)
    observer=Phenomenology(eng,max_shadow_target=36)
    comparison=observer.compare(6,12)
    assert comparison["thin_indistinguishable"] is True
    assert comparison["path_indistinguishable"] is False
    assert comparison["shadow_a"]["stage"] == "shadow"
    assert comparison["shadow_b"]["stage"] == "shadow"
    return {"comparison":comparison,
            "transfer":observer.verify_forgetful_transport(),
            "source_horizon":observer.horizon}
