"""Read-only source bytes, ancestry, environment, and inherited manifests."""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "2b0628f52e9d88993c2e3ffa30b9748adfb781f0"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


counts = {}
for directory, key in (("prime_stroboscope", "source_files"),
                       ("arithmetic_barrier", "files"),
                       ("gamma_all_places", "files")):
    base = HERE.parent / directory
    manifest = json.loads((base / "SOURCE_MANIFEST.json").read_text())
    for name, record in manifest[key].items():
        data = (base / name).read_bytes()
        assert hashlib.sha256(data).hexdigest() == record["sha256"], (directory, name)
        relative = (base/name).relative_to(ROOT).as_posix()
        assert data == git("show", PARENT+":"+relative), relative
    counts[directory] = len(manifest[key])

remote = json.loads((HERE / "receipts/initial_remote.json").read_text())
ancestry = []
for pr in remote["prs"]:
    subprocess.run(["git", "merge-base", "--is-ancestor", pr["base_sha"], pr["head_sha"]],
                   cwd=ROOT, check=True)
    actual = git("rev-parse", "origin/"+pr["head"]).decode().strip()
    assert actual == pr["head_sha"], (pr["number"], actual)
    ancestry.append({"pr": pr["number"], "head": actual,
                     "base": pr["base_sha"], "base_is_ancestor": True})

source_paths = ["AGENTS.md", "docs/METHOD.md", "docs/OPERATIONAL_TRIANGLE.md",
    "provenance/IMPORT_MANIFEST.json", "observational_succ/succ_internal_matrix_walk.py",
    "observational_succ/bbp_source_memory.py", "observational_succ/bbp_two_adic.py",
    "research/2026-10-27/BBP_BINWINDOW_ZERO_BOUNDARY.md",
    "research/2026-10-27/PI_SELECTED_BOUNDARY_CRT_FRONTIER.md",
    "research/2026-10-29/triangle_genesis_repair/MAIN_XVI_HANDOFF.md",
    "research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md",
    "research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md",
    "research/2026-10-30/arithmetic_barrier/arithmetic/ARITHMETIC_THEOREMS.md"]
inputs = {}
for name in source_paths:
    data = (ROOT/name).read_bytes()
    assert data == git("show", PARENT+":"+name)
    inputs[name] = {"sha256": hashlib.sha256(data).hexdigest(),
                    "git_blob": git("rev-parse", PARENT+":"+name).decode().strip()}

print(json.dumps({"status": "PASS", "parent": PARENT,
    "unchanged_inherited_manifest_files": counts, "ancestry": ancestry,
    "source_inputs": inputs, "python": sys.version,
    "packages": {p: importlib.metadata.version(p) for p in
                 ("mpmath", "numpy", "sympy", "scipy", "observational-succ")},
    "branch": git("branch", "--show-current").decode().strip(),
    "main": git("rev-parse", "origin/main").decode().strip(),
    "worktrees": git("worktree", "list", "--porcelain").decode()}, indent=2))
