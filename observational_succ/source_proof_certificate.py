"""Integrity/dependency checking for source-typed mathematical proof capsules.

This module is deliberately NOT a theorem prover or an authenticator of physical
sources. It reports recorded authority, outstanding premises and byte integrity.
Fresh Lean execution, paper review and exact arithmetic each retain their own
authority. Loading a capsule cannot promote a statement to a theorem.
"""
from __future__ import annotations

from enum import Enum
from hashlib import sha256
from pathlib import Path
import re


class Authority(str, Enum):
    CLASSICAL_IMPORTED = "CLASSICAL_IMPORTED"
    PAPER_PROVED = "PAPER_PROVED"
    LEAN_KERNEL_PROVED = "LEAN_KERNEL_PROVED"
    EXACT_FINITE_CHECK = "EXACT_FINITE_CHECK"
    TESTED_MODEL = "TESTED_MODEL"
    UNVERIFIED = "UNVERIFIED"
    REFUTED = "REFUTED"


class CapsuleError(ValueError):
    pass


def evidence_file(root: Path, relative: str, kind: str) -> dict:
    path = _local_file(root, relative)
    return {"path": relative, "sha256": sha256(path.read_bytes()).hexdigest(), "kind": kind}


def _local_file(root: Path, relative: str) -> Path:
    if type(relative) is not str or not relative or Path(relative).is_absolute():
        raise CapsuleError("Relative local evidence path required")
    root = root.resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise CapsuleError("Evidence must be an existing file inside the checkout")
    return path


def _text(value):
    return type(value) is str and bool(value.strip())


def audit_capsules(capsules: list[dict], root: Path) -> dict:
    """Check explicit structure, dependency closure and hashes, never truth.

    Commands in artifacts are descriptive only; no arbitrary embedded commands
    are executed. Classical/paper imports are recorded trust, not kernel proofs.
    """
    if type(capsules) is not list or not capsules:
        raise CapsuleError("Nonempty capsule list required")
    table = {}
    for c in capsules:
        if type(c) is not dict or not _text(c.get("claim_id")) or c["claim_id"] in table:
            raise CapsuleError("Unique claim identifiers required")
        table[c["claim_id"]] = c
    visited, visiting, results = set(), set(), []
    open_debts, effective_hypotheses = {}, {}

    def visit(cid):
        if cid in visiting:
            raise CapsuleError("Circular proof dependency")
        if cid in visited:
            return
        c = table[cid]
        visiting.add(cid)
        try:
            authority = Authority(c["authority"])
        except (KeyError, ValueError, TypeError) as exc:
            raise CapsuleError("Unknown proof authority") from exc
        for key in ("statement", "source", "operations_relations", "target_carrier",
                    "observation_morphisms", "topology_measure", "universal_property",
                    "comparison_maps", "source_identity", "source_epoch",
                    "hypotheses", "dependencies", "evidence", "access", "adversarial",
                    "scope", "conclusion_mode"):
            if key not in c:
                raise CapsuleError(f"Missing {key} for {cid}")
        for key in ("statement", "source", "operations_relations", "target_carrier",
                    "observation_morphisms", "topology_measure", "universal_property",
                    "comparison_maps", "source_identity"):
            if not _text(c[key]):
                raise CapsuleError(f"Empty or malformed {key}")
        if type(c["source_epoch"]) is not int or c["source_epoch"] < 0:
            raise CapsuleError("Exact nonnegative source epoch required")
        if c["scope"] not in ("FINITE_INSTANCE", "UNIVERSAL", "NUMERICAL_MODEL"):
            raise CapsuleError("Explicit finite/universal/model scope required")
        if c["conclusion_mode"] not in ("THEOREM_UNDER_HYPOTHESES", "INSTANCE_ONLY", "OPEN_TARGET", "COUNTEREXAMPLE"):
            raise CapsuleError("Explicit conclusion mode required")
        if type(c["hypotheses"]) is not list or any(not _text(x) for x in c["hypotheses"]):
            raise CapsuleError("Explicit hypothesis list required")
        if type(c["dependencies"]) is not list or any(not _text(x) for x in c["dependencies"]):
            raise CapsuleError("Explicit dependency IDs required")
        allowed_modes = {
            Authority.CLASSICAL_IMPORTED: {"THEOREM_UNDER_HYPOTHESES", "INSTANCE_ONLY"},
            Authority.PAPER_PROVED: {"THEOREM_UNDER_HYPOTHESES", "INSTANCE_ONLY"},
            Authority.LEAN_KERNEL_PROVED: {"THEOREM_UNDER_HYPOTHESES", "INSTANCE_ONLY"},
            Authority.EXACT_FINITE_CHECK: {"INSTANCE_ONLY"},
            Authority.TESTED_MODEL: {"INSTANCE_ONLY"},
            Authority.UNVERIFIED: {"OPEN_TARGET"},
            Authority.REFUTED: {"COUNTEREXAMPLE"},
        }
        if c["conclusion_mode"] not in allowed_modes[authority]:
            raise CapsuleError("Authority and conclusion mode contradict each other")
        if c["conclusion_mode"] == "INSTANCE_ONLY" and c["scope"] == "UNIVERSAL":
            raise CapsuleError("An instance cannot carry universal quantifier scope")
        unresolved = set()
        inherited_hypotheses = set(c["hypotheses"])
        for dep in c["dependencies"]:
            if dep not in table:
                raise CapsuleError(f"Undeclared dependency {dep}")
            visit(dep)
            unresolved.update(open_debts[dep])
            inherited_hypotheses.update(effective_hypotheses[dep])
            if table[dep]["authority"] in ("UNVERIFIED", "REFUTED", "TESTED_MODEL"):
                unresolved.add(dep)
        for assumption in c["hypotheses"]:
            if assumption.startswith("ASSUME:"):
                premise = assumption[len("ASSUME:"):]
                if premise not in table or premise == cid:
                    raise CapsuleError("ASSUME must name a declared distinct premise")
                # An ASSUME is debt even when its target is another conditional.
                # The schema has no semantic premise-discharge inference rule.
                unresolved.add(premise)
        if authority in (Authority.EXACT_FINITE_CHECK, Authority.TESTED_MODEL) and c["scope"] == "UNIVERSAL":
            raise CapsuleError("Finite/model evidence cannot be universal authority")
        if unresolved and authority not in (Authority.UNVERIFIED, Authority.REFUTED, Authority.TESTED_MODEL):
            if (c["conclusion_mode"] != "THEOREM_UNDER_HYPOTHESES" or
                    any(f"ASSUME:{dep}" not in c["hypotheses"] for dep in unresolved)):
                raise CapsuleError("Unproved premises cannot disappear from a theorem type")
        evidence = c["evidence"]
        if type(evidence) is not list or not evidence:
            raise CapsuleError("Evidence or explicit open-problem dossier required")
        kinds = set()
        for item in evidence:
            if type(item) is not dict or not _text(item.get("kind")):
                raise CapsuleError("Typed evidence required")
            path = _local_file(root, item.get("path"))
            digest = item.get("sha256")
            if type(digest) is not str or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise CapsuleError("SHA256 evidence digest required")
            if sha256(path.read_bytes()).hexdigest() != digest:
                raise CapsuleError(f"Evidence changed: {item['path']}")
            kinds.add(item["kind"])
        if authority == Authority.LEAN_KERNEL_PROVED:
            if not {"LEAN_SOURCE", "LEAN_RECEIPT", "AXIOM_MANIFEST"} <= kinds:
                raise CapsuleError("Kernel authority requires source, execution and axiom records")
            if (type(c.get("kernel_declarations")) is not list or not c["kernel_declarations"]
                    or any(not _text(x) for x in c["kernel_declarations"])):
                raise CapsuleError("Exact Lean declaration names required")
        if type(c["access"]) is not dict or type(c["adversarial"]) is not dict:
            raise CapsuleError("Access and adversarial records required")
        for field in ("permitted_observations", "constructible_witness", "oracle",
                      "probe_discrimination", "proof_theory", "execution_cost"):
            if not _text(c["access"].get(field)):
                raise CapsuleError(f"Missing access field {field}")
        for field in ("domain_tests", "negative_examples", "source_mutations", "replay"):
            if not _text(c["adversarial"].get(field)):
                raise CapsuleError(f"Missing adversarial field {field}")
        open_debts[cid] = unresolved
        effective_hypotheses[cid] = inherited_hypotheses
        results.append({"claim_id": cid, "recorded_authority": authority.value,
                        "conclusion_mode": c["conclusion_mode"],
                        "integrity": "HASHES_MATCH", "open_dependencies": sorted(unresolved),
                        "declared_hypotheses": c["hypotheses"],
                        "retained_hypotheses": sorted(inherited_hypotheses),
                        "semantic_authority_issued": None})
        visiting.remove(cid)
        visited.add(cid)

    for cid in table:
        visit(cid)
    return {"schema": "SUCC_CARRIER_PROOF_CERTIFICATE_v1", "audit": "STRUCTURE_AND_BYTES_VALID",
            "claims": results, "theorems_proved_by_this_audit": [],
            "physical_source_authentication": False, "RH_proved": False}
