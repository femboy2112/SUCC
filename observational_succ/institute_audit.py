"""Strict research-graph integrity over the existing source proof capsules.

This checks declared contracts and bytes, not mathematical truth, physical
source authenticity, or the honesty of a recorded execution. Fresh kernel
execution is a separate gate. No command supplied by a registry is executed.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess

from .source_proof_certificate import CapsuleError, audit_capsules, _local_file


def _require(condition, message):
    if not condition:
        raise CapsuleError(message)


def _texts(value):
    return isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)


def audit_registry(registry: dict, root: Path) -> dict:
    """Fail closed on missing credentials, hidden premises and typed drift."""
    _require(registry.get("schema") == "SUCC_INSTITUTE_v1", "Unknown institute schema")
    claims = registry.get("claims")
    base = audit_capsules(claims, root)
    table = {c["claim_id"]: c for c in claims}
    results = {c["claim_id"]: c for c in base["claims"]}
    transports = registry.get("transports", [])
    _require(isinstance(transports, list), "Transport list required")
    seen = set()
    for edge in transports:
        _require(isinstance(edge, dict), "Typed transport required")
        key = (edge.get("from"), edge.get("to"))
        _require(key not in seen, "Duplicate transport")
        seen.add(key)
        _require(all(x in table for x in key), "Unknown transport endpoint")
        source, target = (table[x] for x in key)
        _require(key[0] in target["dependencies"], "Transport must cover a dependency")
        _require(edge.get("input") == source.get("signature") and
                 edge.get("output") == target.get("signature"), "Transport signature drift")
        _require(edge.get("authority") in ("PAPER_PROVED", "LEAN_KERNEL_PROVED", "CLASSICAL_IMPORTED"),
                 "Unverified transport cannot discharge a type change")
        _require(isinstance(edge.get("obligation"), str) and edge["obligation"].strip(),
                 "Explicit transport obligation required")
        _require(edge.get("evidence") in target["evidence"], "Transport proof evidence must be hash checked")
        if target["authority"] == "LEAN_KERNEL_PROVED":
            _require(edge.get("authority") == "LEAN_KERNEL_PROVED",
                     "Paper transport cannot feed kernel authority")
        if edge["authority"] == "LEAN_KERNEL_PROVED":
            _require(target["authority"] == "LEAN_KERNEL_PROVED" and
                     edge["evidence"]["kind"] == "LEAN_SOURCE" and
                     _texts(edge.get("kernel_declarations")) and bool(edge["kernel_declarations"]) and
                     set(edge["kernel_declarations"]) <= set(target.get("kernel_declarations", [])),
                     "Kernel transport needs declarations bound to the checked target source")

    for c in claims:
        cid = c["claim_id"]
        signature = c.get("signature")
        _require(isinstance(signature, dict) and set(signature) == {"source", "carrier", "topology"}
                 and all(isinstance(v, str) and v.strip() for v in signature.values()),
                 "Explicit source/carrier/topology signature required")
        for key in ("quantifiers", "prior_art", "novelty", "next_discriminator", "independent_check"):
            _require(isinstance(c.get(key), str) and c[key].strip(), f"Missing scholarly field {key}")
        _require(_texts(c.get("proof_debt")), "Explicit proof-debt list required")
        _require(set(results[cid]["open_dependencies"]) <= set(c["proof_debt"]),
                 "Unverified dependency missing from proof debt")
        for dep in c["dependencies"]:
            _require(set(results[dep]["retained_hypotheses"]) <= set(c["hypotheses"]),
                     "Dependency hypothesis laundering")
            _require(table[dep]["signature"] == signature or (dep, cid) in seen,
                     "Source/carrier/topology change without a proved comparison map")
            if c["authority"] == "LEAN_KERNEL_PROVED":
                _require(table[dep]["authority"] == "LEAN_KERNEL_PROVED",
                         "Paper/finite dependency cannot silently become kernel authority")
        credentials = c.get("git_sources")
        _require(isinstance(credentials, list) and credentials, "Git source credentials required")
        for source in credentials:
            _require(isinstance(source, dict), "Malformed Git source")
            commit, blob, path = (source.get(k) for k in ("commit", "blob", "path"))
            _require(all(isinstance(x, str) and re.fullmatch(r"[0-9a-f]{40}", x)
                         for x in (commit, blob)), "Full Git commit/blob identities required")
            _require(isinstance(path, str) and path and not Path(path).is_absolute()
                     and ".." not in Path(path).parts and "\0" not in path,
                     "Safe Git source path required")
            try:
                commit_kind = subprocess.check_output(["git", "cat-file", "-t", commit],
                                                      cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
                actual = subprocess.check_output(["git", "rev-parse", f"{commit}:{path}"],
                                                 cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
                kind = subprocess.check_output(["git", "cat-file", "-t", actual],
                                               cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
            except subprocess.CalledProcessError as exc:
                raise CapsuleError("Missing pinned Git source object") from exc
            _require(commit_kind == "commit", "Git source credential must name a commit object")
            _require(actual == blob and kind == "blob", "Git source identity mismatch")
        ci = c.get("ci")
        if ci is not None:
            _require(isinstance(ci, dict) and ci.get("checked_head") == ci.get("claim_head")
                     and bool(re.fullmatch(r"[0-9a-f]{40}", ci.get("checked_head", "")))
                     and ci.get("conclusion") == "success", "Stale or failed CI claim")
        if c["authority"] == "LEAN_KERNEL_PROVED":
            kinds = {kind: [e for e in c["evidence"] if e["kind"] == kind]
                     for kind in ("LEAN_SOURCE", "LEAN_RECEIPT", "AXIOM_MANIFEST")}
            _require(all(len(v) == 1 for v in kinds.values()), "One kernel source/receipt/manifest required")
            src = kinds["LEAN_SOURCE"][0]
            receipt = json.loads(_local_file(root, kinds["LEAN_RECEIPT"][0]["path"]).read_text())
            axioms = json.loads(_local_file(root, kinds["AXIOM_MANIFEST"][0]["path"]).read_text())
            _require(type(receipt.get("exit_code")) is int and receipt["exit_code"] == 0 and
                     type(receipt.get("negative_control_exit_code")) is int and
                     receipt["negative_control_exit_code"] == 1,
                     "Kernel execution or negative control failed")
            _require(receipt.get("source_sha256") == src["sha256"], "Stale Lean execution")
            _require(receipt.get("toolchain") == axioms.get("toolchain") ==
                     (root/"lean-toolchain").read_text().strip(), "Lean toolchain drift")
            _require(receipt.get("declarations") == axioms.get("declarations") and
                     set(c["kernel_declarations"]) <= set(receipt.get("declarations", {})),
                     "Kernel declaration or axiom mismatch")
            _require(all(_texts(v) and set(v) <= {"propext", "Classical.choice", "Quot.sound"}
                         for v in receipt["declarations"].values()), "Unapproved kernel axioms")
    return dict(schema="SUCC_INSTITUTE_AUDIT_v1", audit="CONTRACTS_AND_BYTES_VALID",
                claims=base["claims"], transport_edges=len(transports),
                theorems_proved_by_this_audit=[], physical_source_authentication=False,
                RH_proved=False)
