"""Closed, proposition-bound proof authority.

Threat model: untrusted *data* presented to trusted installed Python code and
its reviewed checker/catalogue. This is not a sandbox for hostile Python code
executing in the same interpreter. Monkeypatching, replacing installed files,
and tampering with the trusted catalogue are outside that boundary.

B proves an exact finite rational matrix proposition. C cites the entire exact
Lean proposition from a coordinator-admitted, actually kernel-checked build;
raw JSON and English prose confer no authority. D is deliberately unavailable:
the old polynomial-identity callback did not prove theorem/source transport.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
from typing import Optional, Tuple

import sympy as sp

from observational_succ._formal_catalogue import APPROVED_RECORD_DIGESTS
from observational_succ.proof_contracts import ProofContract, ProofContractError
from observational_succ.quantitative_rigidity import (
    UndecidableSignError, diagnostics_from_block, is_positive_semidefinite, quad,
)

VERIFIED, REFUTED, INAPPLICABLE, UNKNOWN = "VERIFIED", "REFUTED", "INAPPLICABLE", "UNKNOWN"
_STANDARD_AXIOMS = frozenset(("propext", "Classical.choice", "Quot.sound"))
_ROOT = Path(__file__).resolve().parents[1]


class ProofAuthorityError(ProofContractError):
    """Evidence failed a trusted check; this does not refute the claimed theorem."""


def _freeze(value):
    if isinstance(value, sp.MatrixBase):
        return tuple(tuple(value[i, j] for j in range(value.cols)) for i in range(value.rows))
    if isinstance(value, dict) or isinstance(value, MappingProxyType):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(v) for v in value)
    if isinstance(value, set):
        return frozenset(value)
    return value


def _rational(value):
    # Never sympify arbitrary strings, floats, expressions, or callbacks.
    if type(value) is int or type(value) is Fraction or isinstance(value, sp.Rational):
        return sp.Rational(value)
    raise ProofAuthorityError("finite authority accepts exact rational entries only")


def _matrix(value, *, square=True):
    value = _freeze(value)
    if not isinstance(value, tuple) or not value or not isinstance(value[0], tuple) or not value[0]:
        raise ProofAuthorityError("matrix must be a nonempty rectangular array")
    width = len(value[0])
    if any(not isinstance(row, tuple) or len(row) != width for row in value):
        raise ProofAuthorityError("matrix must be rectangular")
    rows = tuple(tuple(_rational(x) for x in row) for row in value)
    if square:
        if len(rows) != width or any(rows[i][j] != rows[j][i] for i in range(width) for j in range(width)):
            raise ProofAuthorityError("matrix proposition requires a rational symmetric square matrix")
    return rows


@dataclass(frozen=True)
class MatrixProposition:
    """Exactly `matrix is PSD` or `matrix is not PSD` over real vectors.

    This is a finite rational symmetric matrix, never an infinite kernel or an
    original arithmetic source. Entries and dimensions are part of the statement.
    """
    predicate: str
    matrix: tuple

    def __post_init__(self):
        if self.predicate not in ("psd", "not_psd"):
            raise ProofAuthorityError("unknown matrix predicate")
        object.__setattr__(self, "matrix", _matrix(self.matrix))


@dataclass(frozen=True)
class FormalProposition:
    """The entire universal theorem type in one exact checked environment.

    `type_expr` is exported by Lean, including hypotheses and quantifiers. No
    implicit substitution, English interpretation, or logical transport is offered.
    A specialization/implication requires a separately checked declaration.
    """
    name: str
    type_expr: str
    environment_sha256: str
    toolchain: str
    manifest_rev: str

    @property
    def type_sha256(self):
        return hashlib.sha256(self.type_expr.encode("utf-8")).hexdigest()


def register_checker(*_args, **_kwargs):
    raise ProofAuthorityError("checker registration is closed; changes require installed-code review")


def trusted_checker(*_args, **_kwargs):
    raise ProofAuthorityError("caller decorators cannot register proof authority")


def register_source_map(*_args, **_kwargs):
    raise ProofAuthorityError("source-map registration is closed; no source transport is admitted")


def source_map(*_args, **_kwargs):
    raise ProofAuthorityError("caller decorators cannot register source authority")


def _check_negative(data):
    return bool(quad(sp.Matrix(data["matrix"]), sp.Matrix(data["vector"])) < 0)


def _check_psd(data):
    return is_positive_semidefinite(sp.Matrix(data["matrix"]))


def _check_schur(data):
    diag = diagnostics_from_block(sp.Matrix(data["matrix"]), data["n_A"], source_form_identified=False)
    return bool(diag.high_block_psd and diag.range_inclusion_ok in (True, None)
                and diag.schur_complement_psd and diag.m_psd)


_CHECKERS = MappingProxyType({"negative_vector": _check_negative,
                             "psd_matrix": _check_psd,
                             "finite_gram_psd": _check_psd,
                             "finite_schur_positivity": _check_schur})


def registered_checkers() -> Tuple[str, ...]:
    return tuple(sorted(_CHECKERS))


@dataclass(frozen=True)
class LocalCertificate:
    """Immutable data; its exact conclusion is extracted by trusted code."""
    cert_type: str
    data: dict
    scope: str = "finite"
    normalization: str = ""
    level: str = field(default="B", init=False)

    def __post_init__(self):
        if self.cert_type not in _CHECKERS:
            raise ProofAuthorityError("unknown certificate type; checking code is not caller supplied")
        if self.scope != "finite":
            raise ProofAuthorityError("all installed local certificates have finite scope")
        try:
            key = "gram" if self.cert_type == "finite_gram_psd" else "matrix"
            data = {"matrix": _matrix(self.data[key])}
            if self.cert_type == "negative_vector":
                data["vector"] = _matrix(self.data["vector"], square=False)
                if len(data["vector"]) != len(data["matrix"]) or len(data["vector"][0]) != 1:
                    raise ProofAuthorityError("negative witness must be a matching column vector")
            if self.cert_type == "finite_schur_positivity":
                n = self.data["n_A"]
                if type(n) is not int or not 0 < n < len(data["matrix"]):
                    raise ProofAuthorityError("n_A must be an integer strictly between zero and matrix size")
                data["n_A"] = n
        except (KeyError, TypeError) as exc:
            raise ProofAuthorityError("certificate is missing required exact data") from exc
        object.__setattr__(self, "data", MappingProxyType(data))

    @property
    def proposition(self):
        return MatrixProposition("not_psd" if self.cert_type == "negative_vector" else "psd",
                                 self.data["matrix"])

    def verify(self):
        if _CHECKERS[self.cert_type](self.data) is not True:
            raise ProofAuthorityError("finite certificate failed exact recomputation")
        return True


def load_receipt(path):
    """Read untrusted JSON. Loading never authenticates a build."""
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def record_digest(record):
    """Canonical record digest used by the reviewed installed catalogue."""
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode("utf-8")).hexdigest()


def _authenticate_record(record):
    """Exact allowlist admission plus current-source verification, fail closed.

    The catalogue is changed only after an actual pinned build is independently
    inspected. There is deliberately no public admission function.
    """
    if type(record) is not dict or record_digest(record) not in APPROVED_RECORD_DIGESTS:
        raise ProofAuthorityError("untrusted build record: no reviewed kernel-build admission")
    if record.get("schema") != "succ.lean.kernel.v1":
        raise ProofAuthorityError("wrong kernel record schema")
    hashes = record.get("source_hashes")
    if not isinstance(hashes, dict) or not hashes:
        raise ProofAuthorityError("missing exact checked source hashes")
    for relative, digest in hashes.items():
        source = (_ROOT / relative).resolve()
        if not source.is_relative_to(_ROOT) or not source.is_file():
            raise ProofAuthorityError("checked source is unavailable or outside installed tree")
        if hashlib.sha256(source.read_bytes()).hexdigest() != digest:
            raise ProofAuthorityError("checked source hash changed: " + relative)
    return record


@dataclass(frozen=True)
class FormalTheorem:
    """A reference to an admitted exact Lean theorem; a name alone is metadata."""
    name: str
    toolchain: str
    manifest_rev: str
    allowed_axioms: Tuple[str, ...] = ("propext", "Classical.choice", "Quot.sound")
    normalization: str = ""
    scope: str = "global"
    type_expr: str = ""
    environment_sha256: str = ""
    level: str = field(default="C", init=False)

    def __post_init__(self):
        object.__setattr__(self, "allowed_axioms", tuple(self.allowed_axioms))
        if self.scope != "global":
            raise ProofAuthorityError("formal reference states the entire theorem; no implicit specialization")

    @property
    def proposition(self):
        return FormalProposition(self.name, self.type_expr, self.environment_sha256,
                                 self.toolchain, self.manifest_rev)

    @classmethod
    def from_receipt(cls, name, receipt):
        record = _authenticate_record(receipt)
        try:
            entry = record["theorem_exports"][name]
            theorem = cls(name, record["toolchain"], record["manifest_rev"],
                          type_expr=entry["type_expr"], environment_sha256=record["environment_sha256"])
        except (KeyError, TypeError) as exc:
            raise ProofAuthorityError("unknown theorem or malformed kernel export") from exc
        theorem.verify(receipt=record)
        return theorem

    def validate_against_receipt(self, receipt):
        try:
            record = _authenticate_record(receipt)
            entry = record["theorem_exports"][self.name]
            return (bool(self.type_expr) and len(self.environment_sha256) == 64
                    and record["toolchain"] == self.toolchain
                    and record["manifest_rev"] == self.manifest_rev
                    and record["environment_sha256"] == self.environment_sha256
                    and entry["type_expr"] == self.type_expr
                    and entry["type_sha256"] == self.proposition.type_sha256
                    and "axioms" in entry
                    and set(entry["axioms"]) <= _STANDARD_AXIOMS
                    and set(entry["axioms"]) <= set(self.allowed_axioms))
        except (ProofAuthorityError, KeyError, TypeError, ValueError):
            return False

    def verify(self, receipt=None, receipt_path=None):
        if receipt is None and receipt_path is not None:
            receipt = load_receipt(receipt_path)
        if receipt is None or not FormalTheorem.validate_against_receipt(self, receipt):
            raise ProofAuthorityError("exact formal proposition lacks an authenticated checked build")
        return True


@dataclass(frozen=True)
class SourceRealization:
    """Legacy source metadata, deliberately without Level D proof authority.

    Equal caller-supplied polynomials do not identify a theorem instantiation or
    an original signed source. No source transport checker is currently admitted.
    """
    theorem: FormalTheorem
    math_object: str
    source_object: str
    map_type: str
    data: dict
    normalization: str = ""
    scope: str = "global"
    level: str = field(default="D", init=False)

    def __post_init__(self):
        object.__setattr__(self, "data", _freeze(self.data))

    def verify(self, **_kwargs):
        raise ProofAuthorityError("no proposition-bound original-source transport has been admitted")


@dataclass(frozen=True)
class Verdict:
    status: str
    reason: str
    level_used: Optional[str] = None

    def __bool__(self):
        return self.status == VERIFIED


@dataclass(frozen=True)
class Claim:
    """A typed proposition and explanatory label, never proof in itself.

    English strings remain accepted as research metadata but cannot be VERIFIED.
    REFUTED means the offered evidence failed, not that the proposition is false.
    """
    name: str
    statement: object
    required_level: str
    scope: str = "finite"
    normalization: str = ""

    def __post_init__(self):
        if self.required_level not in ("B", "C", "D"):
            raise ProofAuthorityError("required_level must be B, C, or D")

    def discharge(self, evidence, *, receipt=None, receipt_path=None):
        # Exact types, not duck typing or virtual overrides. Arbitrary subclass
        # code must not replace the installed checker at this data boundary.
        if type(evidence) not in (LocalCertificate, FormalTheorem, SourceRealization):
            return Verdict(REFUTED, "evidence is not an installed exact artifact type")
        level = evidence.level
        if level != self.required_level or self.scope != evidence.scope:
            return Verdict(INAPPLICABLE, "authority kind or scope does not match", level)
        if self.normalization != evidence.normalization:
            return Verdict(INAPPLICABLE, "normalization does not match", level)
        if type(evidence) is SourceRealization:
            return Verdict(INAPPLICABLE, "no checked source identification/transport available", level)
        expected_type = MatrixProposition if level == "B" else FormalProposition
        if type(self.statement) is not expected_type:
            return Verdict(INAPPLICABLE, "claim requires a typed proposition, not an English assertion", level)
        if self.statement != evidence.proposition:
            return Verdict(INAPPLICABLE, "evidence proves a different exact proposition", level)
        try:
            if level == "B":
                LocalCertificate.verify(evidence)
            else:
                FormalTheorem.verify(evidence, receipt=receipt, receipt_path=receipt_path)
        except UndecidableSignError as exc:
            return Verdict(UNKNOWN, str(exc), level)
        except (ProofAuthorityError, ValueError, KeyError, TypeError) as exc:
            return Verdict(REFUTED, str(exc), level)
        return Verdict(VERIFIED, "exact typed proposition discharged", level)


def transport_respects_quantifiers(pointwise: ProofContract, uniform: ProofContract,
                                   const_var: str, index_var: str) -> bool:
    try:
        uniform.assert_not_uniformized_from(pointwise, const_var, index_var)
    except ProofContractError:
        return False
    return True
