"""Quantifier-aware proof contracts (Proof Forge §3.5).

A proof contract is a lightweight, checkable record of *what a theorem actually
claims* and *what still has to be discharged* -- with the quantifier prefix made
explicit so the one error that silently destroys number-theoretic arguments is
mechanically catchable:

    turning   (for all N) (exists C_N)        [a pointwise bound]
    into      (exists C) (for all N)          [a uniform bound]

is illegal, and a finite experiment can never license it. This module tracks the
ordered quantifier prefix, each bound variable's domain, the explicit dependency
list of every constant, the finite->infinite transition, source authenticity,
proof method, status (AGENTS.md vocabulary), and the open obligations.

It does NOT prove anything by itself; it is bookkeeping that makes an overclaim
visible. Status vocabulary: CLASSICAL / PROVED LOCAL / TESTED MODEL / HYPOTHESIS
/ CONJECTURED / UNVERIFIED / REFUTED.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence

_VALID_STATUS = {
    "CLASSICAL", "PROVED LOCAL", "TESTED MODEL", "HYPOTHESIS",
    "CONJECTURED", "UNVERIFIED", "REFUTED",
}


class ProofContractError(ValueError):
    pass


@dataclass(frozen=True)
class Quantifier:
    kind: str           # "forall" or "exists"
    var: str
    domain: str
    # variables this bound symbol is ALLOWED to depend on (must be earlier in
    # the prefix). For an existential constant, this is the uniformity record.
    depends_on: Sequence[str] = field(default_factory=tuple)

    def __post_init__(self):
        if self.kind not in ("forall", "exists"):
            raise ProofContractError(f"bad quantifier kind {self.kind!r}")


@dataclass
class ProofContract:
    name: str
    statement: str
    prefix: List[Quantifier]          # ordered quantifier prefix
    hypotheses: List[str]
    constant_dependencies: Dict[str, List[str]]   # const -> vars it may depend on
    finite_to_infinite: str           # how (if at all) finite data becomes a universal claim
    source_authentic: bool            # is the object the genuine source, or a synthetic model?
    method: str
    status: str
    open_obligations: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.status not in _VALID_STATUS:
            raise ProofContractError(
                f"status {self.status!r} not in {sorted(_VALID_STATUS)}"
            )
        self._validate_prefix()

    def _position(self, var: str) -> int:
        for i, q in enumerate(self.prefix):
            if q.var == var:
                return i
        raise ProofContractError(f"variable {var!r} not bound in prefix")

    def _validate_prefix(self) -> None:
        """Every declared dependency must refer to an EARLIER bound variable."""
        for i, q in enumerate(self.prefix):
            for dep in q.depends_on:
                j = self._position(dep)
                if j >= i:
                    raise ProofContractError(
                        f"{q.var!r} declared to depend on {dep!r}, but {dep!r} is "
                        f"not quantified before it (position {j} >= {i})"
                    )

    def is_uniform_in(self, const_var: str, index_var: str) -> bool:
        """True iff `const_var` does NOT depend on `index_var`.

        Operationally: the existential `const_var` is uniform in `index_var`
        exactly when it is quantified BEFORE `index_var` (so it cannot see it)
        AND it does not list `index_var` as a dependency.
        """
        ci, ii = self._position(const_var), self._position(index_var)
        q = self.prefix[ci]
        return (ci < ii) and (index_var not in q.depends_on)

    def assert_not_uniformized_from(self, pointwise: "ProofContract",
                                    const_var: str, index_var: str) -> None:
        """Guard: refuse to read `self` as a uniform strengthening of a pointwise
        `pointwise` contract via an illegal quantifier swap.

        If `pointwise` has the constant depending on the index (for all index,
        exists const_index) and `self` claims the constant is uniform in the
        index (exists const, for all index), that is the forbidden swap.
        """
        pointwise_dependent = not pointwise.is_uniform_in(const_var, index_var)
        self_uniform = self.is_uniform_in(const_var, index_var)
        if pointwise_dependent and self_uniform:
            raise ProofContractError(
                f"ILLEGAL quantifier swap: {pointwise.name!r} has {const_var!r} "
                f"depending on {index_var!r} (pointwise), but {self.name!r} claims "
                f"{const_var!r} uniform in {index_var!r}. A finite experiment "
                f"cannot license (for all {index_var})(exists {const_var}) -> "
                f"(exists {const_var})(for all {index_var})."
            )

    def prefix_string(self) -> str:
        sym = {"forall": "A.", "exists": "E."}
        parts = []
        for q in self.prefix:
            dep = f"[dep:{','.join(q.depends_on)}]" if q.depends_on else ""
            parts.append(f"{sym[q.kind]}{q.var}:{q.domain}{dep}")
        return " ".join(parts)

    def as_record(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "statement": self.statement,
            "prefix": self.prefix_string(),
            "hypotheses": list(self.hypotheses),
            "constant_dependencies": dict(self.constant_dependencies),
            "finite_to_infinite": self.finite_to_infinite,
            "source_authentic": self.source_authentic,
            "method": self.method,
            "status": self.status,
            "open_obligations": list(self.open_obligations),
        }
