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


# =========================================================================== #
# Witness-carrying contracts (Operation Rigidity Forge, Part VIII)
#
# The classes above track *what is claimed*. The classes below make a contract
# carry *authority* -- a proof object that re-verifies itself, an external theorem
# reference with its audited axioms, an honestly-flagged undischarged assumption, a
# source-realization witness that a bare boolean cannot fake, and a transport whose
# validity is CHECKED on a witness rather than asserted.
#
# Guiding rule: **metadata must never impersonate proof.** A `CheckedCertificate`
# has no stored truth value; its `verify()` recomputes an exact certificate. A
# `SourceRealizationWitness` claiming authenticity WITHOUT an identification map is
# rejected. Lean / mathlib / an independent exact oracle remains the authority on
# formal derivations; this layer specializes in source identification, transport
# obligations, quantitative error accounting, and obstruction reporting.
# =========================================================================== #
@dataclass
class CheckedCertificate:
    """A proof object that re-verifies itself by EXACT recomputation.

    ``holds`` is never stored -- it is produced by calling ``check()``, which must
    recompute an exact certificate and return the literal ``True``. A truthy-but-not-
    True value (a nonzero int, a nonempty list) is treated as a failure, so a sloppy
    check cannot pass as a proof."""
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
    """An EXTERNAL authority that discharges an obligation (e.g. a mathlib theorem).

    The SUCC layer does not re-prove it; it records the authority and, for a formal
    checker, the audited axiom set from ``#print axioms``. The authority is
    explicitly NOT the SUCC layer -- that separation is the point."""
    name: str                     # e.g. "Polynomial.abc"
    system: str                   # e.g. "mathlib4 @ <rev>, Lean 4.x"
    axioms: Tuple[str, ...] = ()  # audited #print axioms set
    url: str = ""

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


@dataclass
class SourceRealizationWitness:
    """Whether the object is the genuine source or a synthetic proxy.

    ``authentic=True`` is ACCEPTED only when an ``identification`` callable is
    supplied and recomputes to literal True. A bare ``authentic=True`` with no
    identification is rejected: a boolean is not a source certificate (AGENTS.md
    sec. 6)."""
    object_name: str
    authentic: bool
    identification: Optional[Callable[[], object]] = None
    note: str = ""

    def verify(self) -> bool:
        if not self.authentic:
            return True
        if self.identification is None:
            raise ProofContractError(
                f"{self.object_name!r} asserts source authenticity with NO "
                f"identification witness: a boolean is not a source certificate"
            )
        if self.identification() is not True:
            raise ProofContractError(
                f"{self.object_name!r} identification witness did not verify"
            )
        return True


@dataclass
class ProofTransport:
    """Transport of one established result to another via a translation map.

    VALID only if ``witness_check`` recomputes (exactly) that applying the map to the
    source's certified conclusion actually yields the target's conclusion. An invalid
    transport -- mismatched hypotheses, an illegal quantifier swap, or a false
    implication on a concrete witness -- fails ``verify()`` and is rejected, instead
    of being asserted by a label."""
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


@dataclass
class CarryingContract:
    """A proof contract bundled with the authority that actually discharges it.

    ``verify()`` runs every attached certificate, source witness, and transport, and
    requires that an external ``TheoremReference`` is present whenever the claimed
    status is CLASSICAL with no in-repo checked certificate (so 'CLASSICAL' cannot be
    a bare label). Returns a structured verification record; raises on any failure."""
    contract: ProofContract
    certificates: List[CheckedCertificate] = field(default_factory=list)
    theorem_refs: List[TheoremReference] = field(default_factory=list)
    undischarged: List[UndischargedAssumption] = field(default_factory=list)
    source_witness: Optional[SourceRealizationWitness] = None
    transports: List[ProofTransport] = field(default_factory=list)

    def __post_init__(self):
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
            "status": self.contract.status,
            "certificates_verified": checked,
            "theorem_refs": [(r.name, r.system, r.axioms) for r in self.theorem_refs],
            "undischarged_assumptions": [(u.name, u.statement) for u in self.undischarged],
            "source_authentic": self.contract.source_authentic,
            "transports_verified": [(t.source, t.target) for t in self.transports],
        }
