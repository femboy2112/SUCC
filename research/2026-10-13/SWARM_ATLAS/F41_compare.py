#!/usr/bin/env python3
"""Rebuild the exact branch/blob comparison; --live-github adds current receipts.

Read-only git/gh commands. This does not merge, import, compile or execute EOS.
"""
import argparse
import hashlib
import json
import re
import subprocess

BASE = "1cb30a3d92420f1197fc1615a68fb4309c0e036d"
EOS = "b2774ca485db4b5b4f7ce92e535220352fb3af2f"
VOYAGER = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
PREFIX = "research/2026-10-13/"

REVIEWS = {
    ".github/workflows/obstruction-synthesis.yml": "Keep separate Lean4.19 lane and false-theorem control; do not alter root4.14 pin.",
    "docs/CLAIM_SUPPLEMENT_EVOLUTIONARY_SYNTHESIS.md": "Reference namespaced EOS IDs; compare semantics before any ledger integration.",
    "docs/EVOLUTIONARY_OBSTRUCTION_SYNTHESIS.md": "Preserve as sibling entry point if individual results are later ported.",
    "formal/obstruction_synthesis/DiscoveredInstance.lean": "p=3 learned tables and 9 finite claims; independently port only in isolated pinned lane.",
    "formal/obstruction_synthesis/RepairKernel.lean": "15 universal declarations; behavioral maximality and repair_fusion add useful explicit specs.",
    "formal/obstruction_synthesis/lean-toolchain": "4.19.0 local pin; cannot substitute for root4.14.0.",
    "observational_succ/evolving_bridge_search.py": "Immutable exact-verifier allele constraints; tighter fixed-bijection termination contract.",
    "observational_succ/evolving_observer_categories.py": "Generated tests and terminal behavioral quotient; shares scope with causal multi-action minimization.",
    "observational_succ/obstruction_discovery_lab.py": "Opaque indices but programmer-selected Heisenberg family and fixed commutator miner; independent derivation required.",
    "observational_succ/source_aware_amalgamation.py": "Exact Markov coupling and original/current filtering; complements Frechet ambiguity, does not replace it.",
    PREFIX + "DISCOVERY_PRECOMMIT.json": "Design precedes implementation holdouts; same source family remains common provenance.",
    PREFIX + "EVOLUTIONARY_OBSTRUCTION_RECEIPT.json": "Frozen exact output and old failure seeds; do not edit or relabel as new independent evidence.",
    PREFIX + "EVOLUTIONARY_OBSTRUCTION_SYNTHESIS.md": "EO1-EO11 written proofs and scope; no universal Python refinement or priority claim.",
    PREFIX + "VALIDATION_OBSTRUCTION_SYNTHESIS.json": "Historic local subset and CI receipts; freshly checked exact-head runs are recorded separately.",
    "scripts/evolutionary_obstruction_probe.py": "Parent helpers and finite simulator replay; importing this is not an independent oracle.",
    "tests/test_evolving_amalgamation.py": "CI/zero-mass/dependence/destructive/delay/replay controls; keep contracts when adapting.",
    "tests/test_evolving_bridge_discovery.py": "Fixed-bijection counterexample bounds, Heisenberg3/5/7 and stale-toolkit controls.",
    "tests/test_evolving_observer_categories.py": "Backward pair oracle plus all-partition tests; shared source tables, different algorithm.",
    "tests/test_evolving_receipt.py": "Binds calibration Lean tables to actual learned outputs; does not prove program refinement.",
}

# IDs are sibling claims, not promoted swarm ledger entries.
THEOREMS = [
    ("EOS-01", ["O587", "O610", "O611"], "Same action-word semantics; EOS adds explicit greatest equivalence specification."),
    ("EOS-02", ["O574", "O585", "O586"], "Failed action congruence yields necessary separating prefixed test; contracts agree."),
    ("EOS-03", ["O580", "O582"], "EOS r-b0 counts learned strict class refinements; Voyager n-b bound and stationary plateau are related, not identical."),
    ("EOS-04", ["O572", "O574", "O587"], "Terminal adequate surjective dynamic observer; quotient factorization, not arbitrary adjunction discovery."),
    ("EOS-05", ["O548"], "Powerset image/pullback adjunction differs from poset right-adjoint inference; safe independent spec target."),
    ("EOS-06", ["O574", "O587"], "New explicit repair_fusion equality; same source/actions and reachable pair image essential."),
    ("EOS-07", ["O561", "O607"], "Same dependence firewall: identical marginals or supports do not identify joint laws."),
    ("EOS-08", ["O546", "O553", "O597"], "Persistent exact constraints strengthen fixed permutation search; do not transfer bound to arbitrary genetic grammar."),
    ("EOS-09", ["O553", "O597"], "No contradiction: d-call bound needs fixed consistent bijection and informative complete verifier."),
    ("EOS-10", ["O547", "O554", "O596"], "Partial-source uncertainty agrees; factorial count is particular to unrestricted remaining bijections."),
    ("EOS-11", ["O561", "O562"], "CI picks one Markov coupling; Frechet retains all allowed couplings when CI is absent."),
    ("EOS-12", ["O563"], "Shared separator likelihood counted once; EOS gives explicit corrected gluing square."),
    ("EOS-13", ["O563", "O594", "O609"], "EOS joint model/original/current filter exceeds separate epoch-prior bookkeeping; remains model conditional."),
    ("EOS-14", ["O563", "O579"], "Single totally ordered stream buffering; no concurrent commutation theorem is supplied."),
    ("EOS-15", ["O596", "O638"], "Exact partial-table completion not implied by sampling, classical existence, or finite witness count."),
    ("EOS-16", ["O566", "O567", "O590"], "Heisenberg faithful action supplies actual permutation-voltage representation; classical finite family."),
    ("EOS-17", ["O588", "O591", "O611"], "Old x alias invariant under old actions; a genuinely new swap breaks quotient compatibility."),
    ("EOS-18", ["O564", "O610"], "Exact pinned Lean declarations independently checked in CI; incompatible lane pins must remain explicit."),
    ("EOS-19", ["O594", "O609", "O630"], "Neither branch proves executable Python fully refines all formal specifications."),
    ("EOS-20", ["O565", "O593", "O630"], "Fixed grammar/source constructors are programmer input; no open-world instrument invention or RH claim."),
]


def command(*args):
    return subprocess.check_output(args).decode().strip()


def blob(commit, path):
    result = subprocess.run(["git", "show", commit + ":" + path], capture_output=True)
    if result.returncode:
        return None
    return {
        "git_blob": command("git", "rev-parse", commit + ":" + path),
        "sha256": hashlib.sha256(result.stdout).hexdigest(),
        "bytes": len(result.stdout),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live-github", action="store_true")
    args = parser.parse_args()
    assert command("git", "merge-base", EOS, VOYAGER) == BASE
    changed = command("git", "diff", "--name-status", BASE, EOS).splitlines()
    assert all(line.startswith("A\t") for line in changed)
    assert {line.split("\t")[1] for line in changed} == set(REVIEWS)
    files = []
    for line in command("git", "diff", "--name-status", EOS, VOYAGER).splitlines():
        status, path = line.split("\t")
        files.append({
            "path": path, "status_EOS_to_VOYAGER": status,
            "base": blob(BASE, path), "EOS": blob(EOS, path), "VOYAGER": blob(VOYAGER, path),
            "review": REVIEWS.get(path, "VOYAGER-only addition/modification: preserve existing implementation, proof lane, receipts and canonical docs; this expedition proposes no overwrite."),
        })
    formal = {}
    for commit, paths in [
        (EOS, ["formal/obstruction_synthesis/RepairKernel.lean", "formal/obstruction_synthesis/DiscoveredInstance.lean"]),
        (VOYAGER, command("git", "ls-tree", "-r", "--name-only", VOYAGER, "formal").splitlines()),
    ]:
        formal[commit] = {path: re.findall(r"^theorem (\w+)", command("git", "show", commit + ":" + path), re.M)
                          for path in paths if path.endswith(".lean")}
    pins = {
        "EOS": command("git", "show", EOS + ":formal/obstruction_synthesis/lean-toolchain"),
        "VOYAGER": command("git", "show", VOYAGER + ":lean-toolchain"),
    }
    assert pins == {"EOS": "leanprover/lean4:v4.19.0", "VOYAGER": "leanprover/lean4:v4.14.0"}
    result = {
        "schema": "succ-swm-f41-branch-comparison-v1", "audit_date": "2026-10-13",
        "merge_base": BASE, "EOS": EOS, "VOYAGER": VOYAGER,
        "EOS_only_added_files": len(REVIEWS), "all_differing_files": files,
        "toolchain_pins": pins, "formal_theorem_declarations": formal,
        "claim_comparison": [{"EOS_id": eid, "VOYAGER_ids": ids, "assessment": text} for eid, ids, text in THEOREMS],
        "import_manifest": json.loads(command("git", "show", VOYAGER + ":provenance/IMPORT_MANIFEST.json"))["source_commit"],
        "archive_mutations_proposed": False, "EOS_code_imported": False,
        "Lean_executed_locally": False, "full_suite_executed_locally": False,
    }
    if args.live_github:
        result["live_GitHub_PRs"] = [json.loads(command("gh", "pr", "view", str(n), "--repo", "femboy2112/SUCC",
            "--json", "number,title,headRefOid,headRefName,baseRefName,isDraft,state")) for n in (45, 48)]
        run_ids = (38350341151, 38350341082, 38354710531, 38354710532)
        result["live_GitHub_runs"] = []
        for rid in run_ids:
            raw = json.loads(command("gh", "api", "repos/femboy2112/SUCC/actions/runs/" + str(rid)))
            result["live_GitHub_runs"].append({k: raw[k] for k in
                ("id", "head_sha", "conclusion", "status", "event", "html_url")})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
