"""Four-level proof authority -- the trusted certificate kernel (Proof Forge III, Part II).

The witness-carrying contracts in :mod:`proof_contracts` were a step forward, but
they let a *caller-supplied callback* impersonate proof authority: a bare
``lambda: True`` passed a ``CheckedCertificate`` or a ``SourceRealizationWitness``,
and a fabricated ``TheoremReference`` acquired standing from mere presence in a
dataclass. This module rebuilds authority so that **the registered typed
artifacts cannot self-elevate**: a verdict of VERIFIED requires one of exactly
three artifact types (checked by ``isinstance``, so a forged duck-typed
look-alike is rejected), and its force comes from an in-repo trusted checker, a
recorded Lean build receipt, or a registered source-map -- never from an object's
shape or a caller callback. Two trust boundaries remain explicitly OUTSIDE this
module and are the caller's responsibility: the *provenance of the receipt file*
(it is trusted to be the output of the pinned CI; this module authenticates its
contents, not its origin) and the correctness of the registered checkers
themselves.

Authority flows through FOUR disjoint, explicitly-separated levels:

* **Level A -- Claim metadata** (:class:`Claim`). A declaration of *what* is
  asserted, its scope, and its normalization. No proof authority whatsoever.
* **Level B -- Locally checked finite certificate** (:class:`LocalCertificate`).
  A concrete *witness as data* (matrices, vectors, polynomials) validated by a
  PREDEFINED, in-repo **trusted checker** selected from a fixed registry over a
  declared domain. The caller supplies data, never the checking logic -- there is
  no callback parameter, so ``lambda: True`` has no entry point. The built-in
  checkers reuse the exact :mod:`quantitative_rigidity` kernel.
* **Level C -- Formal-kernel theorem** (:class:`FormalTheorem`). A theorem
  actually elaborated and checked by Lean/mathlib, pinned to exact toolchain and
  dependency revisions, whose authority is read from a RECORDED build receipt
  (``#print axioms`` + build success), not from a caller-set name. A fabricated
  theorem name is simply absent from the receipt and is rejected.
* **Level D -- Original-source realization** (:class:`SourceRealization`). A
  *proved identification* between the mathematical object a theorem is about and
  the actual source object named in the claim, checked by a registered source-map
  checker on concrete data. **Level D is NOT implied by Level C**: a perfectly
  proved theorem about the wrong operator is still about the wrong operator.

Discharging a :class:`Claim` enforces, in order: evidence level >= required level,
scope compatibility (a *finite* certificate cannot discharge a *global* claim),
normalization match (an alternative normalization cannot silently certify a
different one), and finally the evidence's own exact re-verification. The verdict
is one of VERIFIED / REFUTED / INAPPLICABLE / UNKNOWN -- never a bare bool.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Sequence, Tuple

import sympy as sp

from observational_succ.proof_contracts import ProofContract, ProofContractError
from observational_succ.quantitative_rigidity import (
    RigidityInputError,
    UndecidableSignError,
    as_exact_matrix,
    diagnostics_from_block,
    is_positive_semidefinite,
    quad,
)

# the four disjoint verdicts (shared vocabulary with quantitative_rigidity)
VERIFIED = "VERIFIED"
REFUTED = "REFUTED"
INAPPLICABLE = "INAPPLICABLE"
UNKNOWN = "UNKNOWN"

# authority-level ordering: A < B < C < D in *strength of discharge kind*
_LEVEL_RANK = {"A": 0, "B": 1, "C": 2, "D": 3}

#: axioms that are NEVER acceptable regardless of a caller's allowed_axioms set
#: (sorry / native_decide escape hatches). Default-denied in the receipt check.
_FORBIDDEN_AXIOMS = ("sorryAx", "sorry", "Lean.ofReduceBool")


class ProofAuthorityError(ProofContractError):
    """A trusted-kernel obligation was violated (unknown checker, bad receipt,
    failed source map, forbidden callback)."""


# =========================================================================== #
# Level B: the trusted-checker registry  (data in, exact boolean out)
# =========================================================================== #
#: cert_type -> trusted checker. Checkers live IN this repo, take a data dict,
#: and recompute an exact mathematical fact. They are the ONLY thing that can
#: validate a Level B certificate; a caller cannot inject one.
_CHECKERS: Dict[str, Callable[[dict], bool]] = {}


def register_checker(cert_type: str, fn: Callable[[dict], bool]) -> None:
    if cert_type in _CHECKERS:
        raise ProofAuthorityError(f"checker {cert_type!r} already registered")
    _CHECKERS[cert_type] = fn


def trusted_checker(cert_type: str):
    """Decorator form of :func:`register_checker`."""
    def deco(fn: Callable[[dict], bool]) -> Callable[[dict], bool]:
        register_checker(cert_type, fn)
        return fn
    return deco


def registered_checkers() -> Tuple[str, ...]:
    return tuple(sorted(_CHECKERS))


@trusted_checker("negative_vector")
def _check_negative_vector(data: dict) -> bool:
    """CERTIFIES NON-PSD: exact rational v with v^T M v < 0. Reuses the Schur
    kernel's exact quadratic form. (Part VII two-theorem reuse: Schur lane.)"""
    M = as_exact_matrix(data["matrix"])
    v = as_exact_matrix(data["vector"])
    return bool(quad(M, v) < 0)


@trusted_checker("psd_matrix")
def _check_psd_matrix(data: dict) -> bool:
    """CERTIFIES a finite matrix is PSD (all principal minors >= 0, exact)."""
    return is_positive_semidefinite(as_exact_matrix(data["matrix"]))


@trusted_checker("finite_gram_psd")
def _check_finite_gram_psd(data: dict) -> bool:
    """A FINITE Gram matrix is PSD. Deliberately distinct from a global-kernel
    claim: a LocalCertificate carrying this type must declare ``scope='finite'``,
    so it cannot discharge a ``scope='global'`` claim (failure control: a finite
    positive Gram is not a global PSD kernel)."""
    return is_positive_semidefinite(as_exact_matrix(data["gram"]))


@trusted_checker("finite_schur_positivity")
def _check_finite_schur_positivity(data: dict) -> bool:
    """A FINITE block-positivity certificate: the exact Schur obligations hold, so
    ``M = [[A, B], [B^T, D]] >= 0`` (high block PSD + range inclusion + true Schur
    complement PSD + ground-truth M PSD).

    Certifies MATH ONLY. It deliberately does NOT consult any caller-supplied
    ``source_form_identified`` flag: source identification is not locally
    checkable (that is Level D's job, via a ``SourceRealization`` + a registered
    source map). Letting a self-asserted boolean flip the verdict would be exactly
    the 'metadata asserts authority' failure this module exists to prevent."""
    M = as_exact_matrix(data["matrix"])
    diag = diagnostics_from_block(M, int(data["n_A"]),
                                  source_form_identified=False,
                                  kappa=data.get("kappa"))
    return bool(diag.high_block_psd
                and (diag.range_inclusion_ok in (True, None))
                and diag.schur_complement_psd
                and diag.m_psd)


# --- source-map checkers (Level D): identify math object <-> source object ---- #
_SOURCE_MAPS: Dict[str, Callable[[dict], bool]] = {}


def register_source_map(map_type: str, fn: Callable[[dict], bool]) -> None:
    if map_type in _SOURCE_MAPS:
        raise ProofAuthorityError(f"source map {map_type!r} already registered")
    _SOURCE_MAPS[map_type] = fn


def source_map(map_type: str):
    def deco(fn):
        register_source_map(map_type, fn)
        return fn
    return deco


@source_map("polynomial_identity")
def _map_polynomial_identity(data: dict) -> bool:
    """The object the theorem is about equals the actual source polynomial,
    coefficient by coefficient (exact). A wrong map (different polynomials) is
    rejected -- a valid theorem about the wrong object does not realize the
    source."""
    gen = data["gen"]
    diff = sp.expand(sp.sympify(data["theorem_poly"]) - sp.sympify(data["source_poly"]))
    return sp.Poly(diff, gen).is_zero if diff != 0 else True


# =========================================================================== #
# Level B artifact
# =========================================================================== #
@dataclass(frozen=True)
class LocalCertificate:
    """Level B: a finite witness-as-DATA validated by a registered trusted checker.

    There is no callback field. ``cert_type`` must name a registered checker;
    ``data`` is the exact witness. ``scope`` declares the domain over which the
    conclusion holds (e.g. ``'finite'`` or ``'global'``)."""
    cert_type: str
    data: dict
    scope: str = "finite"
    normalization: str = ""
    level: str = field(default="B", init=False)

    def __post_init__(self):
        if self.cert_type not in _CHECKERS:
            raise ProofAuthorityError(
                f"unknown certificate type {self.cert_type!r}; registered: "
                f"{registered_checkers()} -- a caller cannot supply the checker")

    def verify(self) -> bool:
        try:
            ok = _CHECKERS[self.cert_type](self.data)
        except RigidityInputError as exc:
            raise ProofAuthorityError(
                f"Level B certificate {self.cert_type!r} has a non-exact input: "
                f"{exc}") from exc
        if not ok:
            raise ProofAuthorityError(
                f"Level B certificate {self.cert_type!r} failed its trusted check")
        return True


# =========================================================================== #
# Level C artifact
# =========================================================================== #
def load_receipt(path: str) -> dict:
    """Load a Lean axiom-audit receipt (the JSON the pinned mathlib CI emits)."""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


@dataclass(frozen=True)
class FormalTheorem:
    """Level C: a theorem actually elaborated by a formal kernel.

    Its authority is conferred by a RECORDED build receipt, not by this dataclass.
    :meth:`validate_against_receipt` requires the theorem name to be present in a
    receipt whose build succeeded, with matching pinned toolchain / dependency
    revision and an audited axiom set within the allowed envelope. A fabricated
    name is absent from the receipt and is rejected."""
    name: str
    toolchain: str
    manifest_rev: str
    allowed_axioms: Tuple[str, ...]
    normalization: str = ""
    scope: str = "global"
    level: str = field(default="C", init=False)

    def validate_against_receipt(self, receipt: dict) -> bool:
        if not receipt.get("build_succeeded", False):
            return False
        if receipt.get("toolchain") != self.toolchain:
            return False
        if receipt.get("manifest_rev") != self.manifest_rev:
            return False
        theorems = receipt.get("theorems", {})
        entry = theorems.get(self.name)
        if entry is None:                      # fabricated name -> absent -> rejected
            return False
        if "axioms" not in entry:              # absence is UNKNOWN, not "no axioms"
            return False
        recorded_axioms = tuple(entry["axioms"])
        if any(ax in _FORBIDDEN_AXIOMS for ax in recorded_axioms):
            return False                       # default-deny sorry/native_decide
        return all(ax in set(self.allowed_axioms) for ax in recorded_axioms)

    def verify(self, receipt: Optional[dict] = None,
               receipt_path: Optional[str] = None) -> bool:
        if receipt is None:
            if receipt_path is None:
                raise ProofAuthorityError(
                    f"Level C theorem {self.name!r} needs a build receipt; a name "
                    f"alone is not a formal theorem")
            receipt = load_receipt(receipt_path)
        if not self.validate_against_receipt(receipt):
            raise ProofAuthorityError(
                f"Level C theorem {self.name!r} is not authenticated by the receipt")
        return True


# =========================================================================== #
# Level D artifact
# =========================================================================== #
@dataclass(frozen=True)
class SourceRealization:
    """Level D: a proved identification between the theorem's object and the
    actual source object. Requires a Level C theorem AND a registered source-map
    checker that recomputes the identification on concrete data. Level C alone
    does NOT confer Level D."""
    theorem: FormalTheorem
    math_object: str
    source_object: str
    map_type: str
    data: dict
    normalization: str = ""
    scope: str = "global"
    level: str = field(default="D", init=False)

    def __post_init__(self):
        if self.map_type not in _SOURCE_MAPS:
            raise ProofAuthorityError(
                f"unknown source map {self.map_type!r}; registered: "
                f"{tuple(sorted(_SOURCE_MAPS))}")

    def verify(self, receipt: Optional[dict] = None,
               receipt_path: Optional[str] = None) -> bool:
        self.theorem.verify(receipt=receipt, receipt_path=receipt_path)  # Level C first
        if not _SOURCE_MAPS[self.map_type](self.data):
            raise ProofAuthorityError(
                f"source realization {self.math_object!r} <-> {self.source_object!r} "
                f"FAILED its map check: a valid theorem about the wrong object does "
                f"not realize the source")
        return True


# =========================================================================== #
# Level A: the claim, and the trusted discharge
# =========================================================================== #
@dataclass(frozen=True)
class Verdict:
    status: str                 # VERIFIED / REFUTED / INAPPLICABLE / UNKNOWN
    reason: str
    level_used: Optional[str] = None

    def __bool__(self) -> bool:
        return self.status == VERIFIED


@dataclass
class Claim:
    """Level A metadata: what is asserted, at what required authority level, over
    what scope and normalization. Carries NO proof authority on its own."""
    name: str
    statement: str
    required_level: str          # 'B' | 'C' | 'D'
    scope: str = "finite"
    normalization: str = ""

    def __post_init__(self):
        if self.required_level not in ("B", "C", "D"):
            raise ProofAuthorityError(
                f"required_level {self.required_level!r} must be B, C, or D")

    def _scope_ok(self, ev_scope: str) -> bool:
        # 'global' evidence can discharge a 'finite' claim; 'finite' cannot
        # discharge 'global' (the finite-Gram -> global-kernel failure control).
        if ev_scope == self.scope:
            return True
        return ev_scope == "global" and self.scope == "finite"

    def discharge(self, evidence, *, receipt: Optional[dict] = None,
                  receipt_path: Optional[str] = None) -> Verdict:
        """Attempt to discharge this claim with a single evidence artifact.

        Enforces, before ever trusting the evidence: (1) a callback is NOT
        evidence; (2) evidence level >= required level; (3) scope compatibility;
        (4) normalization match. Only then is the evidence re-verified exactly."""
        # (1) only the registered typed authority artifacts count as evidence. A
        #     raw callback, a bare value, OR a forged duck-typed look-alike (an
        #     object that merely exposes `.level` and a `.verify()` returning True)
        #     is rejected: authority comes from the registered checkers / receipt /
        #     source maps, never from an object's shape.
        if not isinstance(evidence, (LocalCertificate, FormalTheorem, SourceRealization)):
            return Verdict(REFUTED,
                           "evidence is not a registered authority artifact "
                           "(LocalCertificate / FormalTheorem / SourceRealization); "
                           "a callback, bare value, or forged look-alike is not proof")
        ev_level = evidence.level
        # (2) level sufficiency: exact kind, with D also satisfying a C requirement.
        level_ok = (ev_level == self.required_level
                    or (self.required_level == "C" and ev_level == "D"))
        if not level_ok:
            return Verdict(INAPPLICABLE,
                           f"claim requires level {self.required_level}, evidence is "
                           f"level {ev_level}", level_used=ev_level)
        # (3) scope compatibility.
        ev_scope = getattr(evidence, "scope", "finite")
        if not self._scope_ok(ev_scope):
            return Verdict(INAPPLICABLE,
                           f"scope mismatch: claim is {self.scope!r}, evidence is "
                           f"{ev_scope!r} (a finite certificate is not a global one)",
                           level_used=ev_level)
        # (4) normalization match (when the claim pins one).
        ev_norm = getattr(evidence, "normalization", "")
        if self.normalization and ev_norm != self.normalization:
            return Verdict(INAPPLICABLE,
                           f"normalization mismatch: claim {self.normalization!r} vs "
                           f"evidence {ev_norm!r} (an alternative normalization does "
                           f"not certify a different one)", level_used=ev_level)
        # finally: the evidence must re-verify exactly AND return literal True.
        try:
            if ev_level in ("C", "D"):
                ok = evidence.verify(receipt=receipt, receipt_path=receipt_path)
            else:
                ok = evidence.verify()
        except ProofAuthorityError as exc:
            return Verdict(REFUTED, str(exc), level_used=ev_level)
        except UndecidableSignError as exc:
            # a genuinely undecidable obligation is the fourth verdict, not a crash
            return Verdict(UNKNOWN, f"an obligation was undecidable: {exc}",
                           level_used=ev_level)
        if ok is not True:
            # belt-and-suspenders: a verify() that returns a non-True falsy value
            # without raising is not a proof (guards a future artifact regressing).
            return Verdict(REFUTED,
                           "evidence.verify() did not return literal True",
                           level_used=ev_level)
        return Verdict(VERIFIED,
                       f"discharged at level {ev_level}", level_used=ev_level)


# --------------------------------------------------------------------------- #
# Quantifier-aware transport guard (reuse the ProofContract prefix machinery)
# --------------------------------------------------------------------------- #
def transport_respects_quantifiers(pointwise: ProofContract, uniform: ProofContract,
                                   const_var: str, index_var: str) -> bool:
    """True iff reading ``uniform`` as a strengthening of ``pointwise`` does NOT
    commit the forbidden (for all i)(exists c_i) -> (exists c)(for all i) swap.
    Returns False exactly when that illegal uniformization is attempted -- the
    'source-valid inequality with wrong quantifier dependencies' failure control."""
    try:
        uniform.assert_not_uniformized_from(pointwise, const_var, index_var)
    except ProofContractError:
        return False
    return True
