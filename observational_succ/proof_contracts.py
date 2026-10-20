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
from typing import Callable, Dict, List, Optional, Sequence, Tuple
from types import MappingProxyType

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
        object.__setattr__(self, "depends_on", tuple(self.depends_on))
        if len(set(self.depends_on)) != len(self.depends_on):
            raise ProofContractError("duplicate quantifier dependency")
        if self.kind not in ("forall", "exists"):
            raise ProofContractError(f"bad quantifier kind {self.kind!r}")


@dataclass(frozen=True)
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
        object.__setattr__(self, "prefix", tuple(self.prefix))
        object.__setattr__(self, "hypotheses", tuple(self.hypotheses))
        object.__setattr__(self, "open_obligations", tuple(self.open_obligations))
        object.__setattr__(self, "constant_dependencies", MappingProxyType(
            {k: tuple(v) for k, v in self.constant_dependencies.items()}))
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
        names = [q.var for q in self.prefix]
        if len(set(names)) != len(names):
            raise ProofContractError("duplicate quantified variable")
        for const, dependencies in self.constant_dependencies.items():
            q = self.prefix[self._position(const)]
            if set(dependencies) != set(q.depends_on):
                raise ProofContractError("contradictory quantifier dependency metadata")
        for i, q in enumerate(self.prefix):
            if type(q) is not Quantifier:
                raise ProofContractError("prefix requires exact Quantifier metadata")
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
            "source_authentic": False,
            "claimed_source_authentic": self.source_authentic,
            "method": self.method,
            "status": "UNVERIFIED",
            "claimed_status": self.status,
            "authority": "NON_AUTHORITATIVE_RESEARCH_METADATA",
            "open_obligations": list(self.open_obligations),
        }


# =========================================================================== #
# Legacy research bundles: callback execution and bibliographic metadata only.
# These do not discharge any proposition. Use proof_authority.Claim with typed
# immutable evidence for an authority verdict. Historical class names remain for
# compatibility; "verify" below means a diagnostic ran, not a theorem was proved.
# =========================================================================== #
@dataclass(frozen=True)
class CheckedCertificate:
    """Legacy callback diagnostic, explicitly NON-AUTHORITATIVE.

    Even literal True can come from `lambda: True`; its return value proves no
    theorem. Kept only to run reproducible research checks outside authority.
    """
    name: str
    check: Callable[[], object]
    description: str = ""

    def verify(self) -> bool:
        result = self.check()
        if result is not True:
            raise ProofContractError(
                f"certificate {self.name!r} did not verify (got {result!r}, "
                f"require literal True)"
            )
        return True


@dataclass(frozen=True)
class TheoremReference:
    """Bibliographic metadata only; not a checked theorem or obligation discharge."""
    name: str                     # e.g. "Polynomial.abc"
    system: str                   # e.g. "mathlib4 @ <rev>, Lean 4.x"
    axioms: Tuple[str, ...] = ()  # audited #print axioms set
    url: str = ""

    def __post_init__(self):
        object.__setattr__(self, "axioms", tuple(self.axioms))

    def uses_only(self, allowed: Sequence[str]) -> bool:
        return all(ax in set(allowed) for ax in self.axioms)


@dataclass(frozen=True)
class UndischargedAssumption:
    """An analytic hypothesis the contract DEPENDS ON but does not prove here.

    Recording it explicitly is the difference between an honest 'PROVED LOCAL
    conditional on X' and a silent overclaim."""
    name: str
    statement: str
    why_needed: str


@dataclass(frozen=True)
class SourceRealizationWitness:
    """Legacy source claim; only the closed Level D path can authenticate it."""
    object_name: str
    authentic: bool
    realization: Optional[object] = None
    note: str = ""
    receipt: Optional[dict] = None

    def __post_init__(self):
        from observational_succ.proof_authority import _freeze
        object.__setattr__(self, "receipt", _freeze(self.receipt))

    def verify(self) -> bool:
        if not self.authentic:
            return True
        from observational_succ.proof_authority import SourceRealization
        if type(self.realization) is not SourceRealization:
            raise ProofContractError("source claim requires an exact admitted Level D artifact")
        # No duck-typed method or fallback callback can confer authenticity.
        return SourceRealization.verify(self.realization, receipt=self.receipt)


@dataclass(frozen=True)
class ProofTransport:
    """Legacy callback diagnostic about a proposed transport, not proof authority.

    Checking selected witnesses cannot prove a universal implication. Use a
    separately checked formal implication for authoritative transport.
    """
    source: str
    target: str
    witness_check: Callable[[], object]
    note: str = ""

    def verify(self) -> bool:
        result = self.witness_check()
        if result is not True:
            raise ProofContractError(
                f"transport {self.source!r} -> {self.target!r} is INVALID "
                f"(witness check returned {result!r})"
            )
        return True


@dataclass(frozen=True)
class CarryingContract:
    """Immutable research bundle. `verify` never returns a proved claim status.

    A successful callback or unrelated reference may support investigation but
    cannot authenticate its English contract. Status fields are labelled claims.
    """
    contract: ProofContract
    certificates: List[CheckedCertificate] = field(default_factory=list)
    theorem_refs: List[TheoremReference] = field(default_factory=list)
    undischarged: List[UndischargedAssumption] = field(default_factory=list)
    source_witness: Optional[SourceRealizationWitness] = None
    transports: List[ProofTransport] = field(default_factory=list)

    def __post_init__(self):
        for field_name in ("certificates", "theorem_refs", "undischarged", "transports"):
            object.__setattr__(self, field_name, tuple(getattr(self, field_name)))
        if type(self.contract) is not ProofContract:
            raise ProofContractError("research bundle requires exact contract metadata")
        self.contract._validate_prefix()
        if self.source_witness is not None and self.contract.source_authentic != self.source_witness.authentic:
            raise ProofContractError("contradictory source-authenticity metadata")
        # CLASSICAL / PROVED LOCAL must be backed by *something* checkable, not a bare
        # label: at least one checked certificate or an external theorem reference.
        if self.contract.status in ("CLASSICAL", "PROVED LOCAL"):
            if not self.certificates and not self.theorem_refs:
                raise ProofContractError(
                    f"{self.contract.name!r} is {self.contract.status} but carries "
                    f"neither a checked certificate nor a theorem reference -- a "
                    f"status label is not a proof"
                )
        # a contract declaring source_authentic must carry a verifying witness
        if self.contract.source_authentic and self.source_witness is None:
            raise ProofContractError(
                f"{self.contract.name!r} sets source_authentic=True but has no "
                f"SourceRealizationWitness"
            )

    def verify(self) -> Dict[str, object]:
        self.__post_init__()  # recheck invariants at the final boundary
        checked = []
        for c in self.certificates:
            c.verify()
            checked.append(c.name)
        if self.source_witness is not None:
            self.source_witness.verify()
        for t in self.transports:
            t.verify()
        return {
            "name": self.contract.name,
            "status": "UNVERIFIED",
            "claimed_status": self.contract.status,
            "authority": "NON_AUTHORITATIVE_RESEARCH_METADATA",
            "certificates_verified": checked,
            "theorem_refs": [(r.name, r.system, r.axioms) for r in self.theorem_refs],
            "undischarged_assumptions": [(u.name, u.statement) for u in self.undischarged],
            "source_authentic": False,
            "claimed_source_authentic": self.contract.source_authentic,
            "transports_verified": [(t.source, t.target) for t in self.transports],
        }
