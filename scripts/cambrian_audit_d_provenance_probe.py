#!/usr/bin/env python3
"""Audit provenance, branch identities, receipt hashes, and source-label controls.

This verifies evidence integrity and declared-source boundaries, not the
mathematical validity of E's arithmetic results or physical authentication.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.causal_nerode_succ import SourceChart, SourceTransportError
from observational_succ.cambrian_stochastic_transport import (
    JointInstrument, joint_descent, source_filter, observer_filter,
)

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
SNAPSHOT = "7af4c24284c870942e0140c2bbffdc95302aca3d"
WORKERS = {
    "A": ("5677e9c73096c05ef05cf49a9a119447d5c601f2", "01bf38fb282872cfe28362321809b30ea9f1b3f9"),
    "B": ("a71b8b9053ee81a67be2ed78c133a6c61e6766dd", "fb3499dfb6da9bd491bf89d01abe9de716b5d7b5"),
    "C": ("906de6f450b05d8be7cd4c8f3a0218f8a2392fe5", "c53588bf145e8ad09ffdd9acd5b5dc8262969994"),
    "D": ("810128e8fdd1f32a17852d828ee16e4b7ffb50f3", "6657950fc9275de03bfa68c864c73c15b1274380"),
    "E": ("c2c18c3ed638478448497fb6892a747f67ee6f9b", "5d34d3bd19c74b90bdff2e0fb962c8332c18f881"),
    "F": ("21ef59994f11d488a31632f731f4e4d7d9adbc77", "6fc5ae9f1a92abbab259b37440aefed23ee04e92"),
}


def git(*args, binary=False):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=not binary)


def patch_identity(commit):
    raw = git("show", "--pretty=format:", "--no-ext-diff", commit)
    return subprocess.check_output(["git", "patch-id", "--stable"], cwd=ROOT,
                                   input=raw, text=True).split()[0]


def worker_identity():
    result = {}
    for cluster, (original, integrated) in WORKERS.items():
        parent = git("show", "-s", "--format=%P", original).strip()
        assert parent == BASE
        original_paths = git("diff-tree", "--no-commit-id", "--name-only", "-r", original).splitlines()
        integrated_paths = git("diff-tree", "--no-commit-id", "--name-only", "-r", integrated).splitlines()
        assert original_paths == integrated_paths
        blobs = {p: git("rev-parse", original + ":" + p).strip() for p in original_paths}
        assert all(h == git("rev-parse", integrated + ":" + p).strip() for p,h in blobs.items())
        op, ip = patch_identity(original), patch_identity(integrated)
        assert op == ip
        result[cluster] = {"original_commit": original, "integration_cherry_pick": integrated,
                           "original_parent": parent, "same_patch_id": op,
                           "same_added_blobs": blobs, "count_as_one_research_result": True}
    return result


def old_rows(text):
    return {int(m.group(1)): m.group(0) for m in re.finditer(r"^\| O(\d+) \|.*$", text, re.M)
            if int(m.group(1)) <= 638}


def preserved_source(snapshot):
    frozen = git("show", BASE + ":docs/CLAIM_LEDGER.md")
    actual = git("show", snapshot + ":docs/CLAIM_LEDGER.md")
    assert frozen == actual
    assert set(old_rows(frozen)) == set(range(1,639))
    protected = git("diff", "--name-only", BASE, snapshot, "--", "provenance", "docs/CLAIM_LEDGER.md").splitlines()
    assert protected == []
    verified = json.loads(subprocess.check_output([sys.executable, "scripts/verify_provenance.py"], cwd=ROOT, text=True))
    assert verified["items"] == 72 and verified["status"] == "SOURCE_PROVENANCE_VERIFIED"
    return {"snapshot": snapshot, "historical_O_rows": 638, "complete_ledger_byte_equal": True,
            "protected_paths_changed": protected, "provenance_verifier": verified}


def artifact_path(key):
    p = Path(key)
    if not p.is_absolute():
        return ROOT / p
    for marker in ("/observational_succ/", "/scripts/", "/tests/", "/formal/"):
        if marker in key:
            return ROOT / (marker.strip("/") + "/" + key.split(marker, 1)[1])
    raise AssertionError("Unexpected absolute artifact path " + key)


def hash_receipts():
    research = ROOT / "research/2026-10-13"
    checks = []
    contracts = [("CAMBRIAN_A_VALIDATION.json", "sha256"),
                 ("CAMBRIAN_C_ASSIGNMENTS.json", "artifact_hashes_sha256"),
                 ("CAMBRIAN_E_ARITHMETIC_RECEIPT.json", "code_sha256"),
                 ("cambrian_f_results.json", "source_hashes")]
    contracts += [(f"CAMBRIAN_B_{i:02d}_RESULT.json", "provenance.files_sha256") for i in range(7,13)]
    for filename, field in contracts:
        obj = json.loads((research / filename).read_text())
        hashes = obj
        for key in field.split("."):
            hashes = hashes[key]
        assert isinstance(hashes,dict) and hashes
        for name, digest in hashes.items():
            path = artifact_path(name)
            actual = sha256(path.read_bytes()).hexdigest()
            assert actual == digest, (filename, name)
            checks.append({"receipt": filename, "artifact": str(path.relative_to(ROOT)), "sha256": actual})
    for filename, field, path in (
        ("CAMBRIAN_D_RESULTS.json","implementation_sha256","observational_succ/cambrian_d_computation.py"),
        ("CAMBRIAN_STOCHASTIC_RECEIPT.json","module_sha256","observational_succ/cambrian_stochastic_transport.py"),
    ):
        obj = json.loads((research/filename).read_text())
        digest = sha256((ROOT/path).read_bytes()).hexdigest()
        assert obj[field] == digest
        checks.append({"receipt": filename,"artifact":path,"sha256":digest})
    return checks


def inert_source_mutation():
    """A fresh changed-byte control that leaves all geometry output identical."""
    from observational_succ.cambrian_c_geometry import geometry_demo
    path = ROOT / "observational_succ/cambrian_c_geometry.py"
    raw = path.read_bytes()
    mutation = raw + b"\n# CAMBRIAN AUDIT D inert changed-byte control\n"
    with tempfile.TemporaryDirectory(prefix="cambrian_audit_d_") as directory:
        changed = Path(directory) / "same_math_changed_source.py"
        changed.write_bytes(mutation)
        spec = importlib.util.spec_from_file_location("observational_succ._audit_d_inert_mutant", changed)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        assert module.geometry_demo() == geometry_demo()
    original_hash, changed_hash = sha256(raw).hexdigest(), sha256(mutation).hexdigest()
    assert original_hash != changed_hash
    return {"same_complete_geometry_receipt": True, "changed_byte_hash_differs": True,
            "original_sha256": original_hash, "mutated_sha256": changed_hash,
            "math_replay_alone_detects_this_mutation": False,
            "stored_artifact_hash_contract_detects_this_mutation": True,
            "original_source_unchanged": path.read_bytes() == raw}


def assignments():
    p=ROOT/"research/2026-10-13"
    groups = {
        "A": list(map(int,json.loads((p/"CAMBRIAN_A_RECEIPT.json").read_text())["results"])),
        "B": [json.loads((p/f"CAMBRIAN_B_{i:02d}_RESULT.json").read_text())["assignment"] for i in range(7,13)],
        "C": json.loads((p/"CAMBRIAN_C_ASSIGNMENTS.json").read_text())["assignments_executed"],
        "D": list(map(int,json.loads((p/"CAMBRIAN_D_RESULTS.json").read_text())["assignments"])),
        "E": [a["assignment"] for a in json.loads((p/"CAMBRIAN_E_ASSIGNMENTS.json").read_text())["assignments"]],
        "F": json.loads((p/"cambrian_f_results.json").read_text())["assignment_ids"],
    }
    groups={k:list(map(int,v)) for k,v in groups.items()}
    assert all(len(v)==6 for v in groups.values())
    assert sorted(i for v in groups.values() for i in v)==list(range(1,37))
    return {"actual_worker_count":6,"actual_exploration_assignments":36,"groups":groups,
            "36_independent_research_agents_claimed":False,
            "audit_portfolio_size":8,"audits_at_frozen_snapshot":{"A":"committed","B":"committed",
                "C":"not_in_snapshot","D":"this_audit_in_progress","E":"not_in_snapshot",
                "F":"not_in_snapshot","G":"not_in_snapshot","H":"not_in_snapshot"},
            "remaining_audit_completion_requires_final_manifest":True}


def source_controls():
    before=SourceChart("one-source",2,"one-basis",("s",),("o",))
    valid=SourceChart("one-source",3,"one-basis",("t",),("p",))
    rejected=[]
    for name,after in (("source",SourceChart("alien",3,"one-basis",("t",),("p",))),
                       ("basis",SourceChart("one-source",3,"alien-basis",("t",),("p",))),
                       ("epoch",SourceChart("one-source",1,"one-basis",("t",),("p",)))):
        try:
            JointInstrument("action",before,after,("receipt",),((Q(1),),))
        except SourceTransportError:
            rejected.append(name)
        else:
            raise AssertionError("Bad source contract accepted")
    instrument=JointInstrument("action",before,valid,("receipt",),((Q(1),),))
    try:
        source_filter(instrument,(Q(1),),"forged-receipt")
    except SourceTransportError:
        rejected.append("receipt")
    else:
        raise AssertionError("Unknown receipt accepted")
    incomplete=JointInstrument("partial",before,valid,("receipt",),((Q(1),),),False)
    assert joint_descent(incomplete).descended and not joint_descent(incomplete).source_class_certified
    try:
        observer_filter(incomplete,(Q(1),),"receipt")
    except SourceTransportError:
        rejected.append("incomplete-source")
    else:
        raise AssertionError("Partial source got universal filter")
    q0=SourceChart("declared-source",0,"basis",("a","b"),("same","same"))
    q1=SourceChart("declared-source",1,"basis",("x","y"),("x","y"))
    p=(Q(3,8),Q(1,8),Q(1,8),Q(3,8))
    q=(Q(1,8),Q(3,8),Q(3,8),Q(1,8))
    correlation=JointInstrument("same-labels",q0,q1,("z","w"),(p,q))
    assert not joint_descent(correlation).descended
    first=JointInstrument("same-labels",q0,q1,("z","w"),(p,p))
    second=JointInstrument("same-labels",q0,q1,("z","w"),(q,q))
    assert first.name==second.name and first.before==second.before and first.rows!=second.rows
    return {"wrong_contracts_rejected":rejected,
            "equal_marginals_and_support_do_not_preserve_joint_correlation":True,
            "identical_source_and_action_labels_do_not_authenticate_equal_kernels":True,
            "source_class_complete_is_a_mathematical_declaration":True,
            "actual_physical_source_authentication_executed":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot",default=SNAPSHOT)
    parser.add_argument("--remote",action="store_true")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result={"schema":"succ-cambrian-audit-d-provenance-v1","execution_head":git("rev-parse","HEAD").strip(),
            "source_preservation":preserved_source(args.snapshot),"worker_identity":worker_identity(),
            "receipt_hash_checks":hash_receipts(),"assignment_accounting":assignments(),
            "inert_source_mutation":inert_source_mutation(),
            "source_identity_controls":source_controls(),
            "own_E_mathematics_reviewed":False,
            "receipt_runtime_exclusions":{"A":["python"],"B":["provenance.python_version"],
                "C":[],"D":["python"],"E":["python","execution_head_sha"],"F":[],"ST":[]},
            "all_mathematical_and_code_hash_fields_remain_comparison_inputs":True}
    if args.remote:
        proc=subprocess.run(["git","ls-remote","origin","refs/heads/main",
            "refs/heads/research/voyager-observational-profinite-completion-2026-10-13",
            "refs/heads/research/evolutionary-obstruction-synthesis-2026-10-13"],cwd=ROOT,
            text=True,capture_output=True,timeout=30)
        result["remote_read"]={"exit_code":proc.returncode,"ref_output":proc.stdout,"stderr":proc.stderr}
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")


if __name__=="__main__":
    main()
