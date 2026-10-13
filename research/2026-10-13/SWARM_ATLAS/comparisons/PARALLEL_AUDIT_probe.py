"""Bounded exact comparison controls; no repository mathematics is imported."""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

SNAPSHOTS = {
    "PR49": "9bcb93965239c395653ad14e7c7afe65fa7faec0",
    "PR50": "759c30c72a2927212cdbfa41365800da96e5d515",
    "PR51": "bdb1fcfce875ee6c51fc62f78fbb4111582caadc",
}
BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ATLAS = "research/2026-10-13/SWARM_ATLAS/"


def git(*args):
    return subprocess.check_output(["git", *args])


def repair(relation, actions):
    current = frozenset(relation)
    while True:
        following = frozenset((x, y) for x, y in current
                              if all((a[x], a[y]) in current for a in actions))
        if following == current:
            return current
        current = following


def bayes(matrix):
    mass = sum(map(sum, matrix), F(0))
    return tuple(tuple(x / mass for x in row) for row in matrix)


def controls():
    output = {}
    # The predicate image forgets the two different receipt witnesses.
    comparison = ((0, 0), (0, 0))
    assert set(comparison) == {(0, 0)} and len(comparison) != len(set(comparison))
    output["A01_duplicate_witness"] = {"predicate_coverage": True,
                                        "witness_bijective": False}
    qx, qy, ax, ay, f = (0, 0), (0, 0, 1), (0, 1), (0, 2, 2), (0, 1)
    rx = {(x, y) for x in range(2) for y in range(2) if qx[x] == qx[y]}
    ry = {(x, y) for x in range(3) for y in range(3) if qy[x] == qy[y]}
    assert all(qx[x] == qy[f[x]] for x in range(2)) and f[ax[1]] != ay[f[1]]
    left = repair(rx, [ax])
    right = {(x, y) for x in range(2) for y in range(2)
             if (f[x], f[y]) in repair(ry, [ay])}
    assert left != right
    output["A06_missing_action_intertwiner"] = {"left": sorted(left), "right": sorted(right)}
    r = {(x, y) for x in range(4) for y in range(4)
         if (0, 0, 0, 1)[x] == (0, 0, 0, 1)[y]}
    a, b = (0, 0, 3, 0), (0, 2, 0, 0)
    sequential, combined = repair(repair(r, [b]), [a]), repair(r, [a, b])
    assert sequential != combined and (0, 1) in sequential and (b[0], b[1]) not in sequential
    output["A06_separate_repairs"] = {"sequential_pair_count": len(sequential),
                                        "joint_pair_count": len(combined)}
    p, p2 = ((F(3, 8), F(1, 8)), (F(1, 8), F(3, 8))), ((F(1, 8), F(3, 8)), (F(3, 8), F(1, 8)))
    posterior = [j[0][0] / (j[0][0] + j[1][0]) for j in (p, p2)]
    assert posterior == [F(3, 4), F(1, 4)]
    output["C17_equal_marginals"] = {"original_posterior_after_read0": list(map(str, posterior))}
    collision = bayes(((F(1, 4), F(0)), (F(0), F(1, 4))))
    reglued = ((F(1, 4), F(1, 4)), (F(1, 4), F(1, 4)))
    assert collision != reglued
    output["C18_nonfactor_likelihood"] = {"posterior": [[str(v) for v in row] for row in collision],
                                           "reglued": [[str(v) for v in row] for row in reglued]}
    source, grammar, extension = {0, 1}, {0}, {0, 1}
    constraint = lambda x: x == 1
    assert not any(map(constraint, grammar)) and any(map(constraint, source)) and any(map(constraint, extension))
    output["X03_core_carrier"] = {"grammar_unsat": True, "source_unsat": False,
                                   "extension_witness": 1, "safe_source_cache": False}
    # One original, a mixed two-current-state preparation, deterministic read.
    mixed_supports = [{0}, {0}]
    pure_supports = [[{0}, set()], [set(), {0}]]
    assert all(mixed_supports != pure for pure in pure_supports)
    output["X07_preparation"] = {"mixed_original_supports": [[0], [0]],
                                  "no_pure_preparation_recovers_both": True}
    paths1 = {("l", "l"), ("l", "d")}
    successors = {"l": ("l", "d"), "d": ()}
    paths2 = {path + (n,) for path in paths1 for n in successors[path[-1]]}
    truncated = {path[:-1] for path in paths2}
    assert ("l", "d") in paths1 - truncated and ("l", "l") in truncated
    output["B09_Cambrian_raw_prefixes"] = {"stage1": sorted(paths1), "stage2": sorted(paths2),
                                           "truncation_surjective": False,
                                           "arbitrary_depth_control": "the all-live branch"}
    for word in itertools.product((0, 1), repeat=5):
        likelihoods = [F(1) for _ in (0, 1)]
        for report in word:
            likelihoods = [v * (F(3, 4) if state == report else F(1, 4))
                           for state, v in enumerate(likelihoods)]
        assert all(v > 0 for v in likelihoods)
    output["C21_full_support_noise"] = {"all_32_depth5_words_retain_both_targets": True,
                                          "universal_reason": "finite products of strictly positive rows stay positive"}
    return output


def receipt():
    inspected = {
        "PR49": [ATLAS + name + ".md" for name in ("A01", "A06", "B09", "B10", "C17", "C18")]
                 + ["formal/SWM_A01_BaseChange.lean", "formal/SWM_B09_InverseFamilies.lean",
                    "formal/SWM_B09_TopologicalCompletion.lean", ATLAS + "registry.json"],
        "PR50": [ATLAS + name + ".md" for name in ("A01", "A06", "B09", "B10", "C17", "C18", "C21", "F48", "X03", "X07")]
                 + ["formal/Swarm_Repair.lean", "formal/swarm_topology/SwarmTopology.lean",
                    "formal/swarm_topology/SwarmPolicyCompactness.lean", "formal/swarm_topology/SwarmX01CompletionTransport.lean",
                    "formal/swarm_topology/lakefile.lean", "formal/swarm_topology/lake-manifest.json",
                    ATLAS + "FINAL_KERNEL_RECEIPT.json", ATLAS + "REGISTRY.json",
                    ATLAS + "reviews/RY_AUDIT.md", "observational_succ/swarm_gluing_cegis.py"],
        "PR51": ["formal/EODCS_CambrianRealization.lean", "research/2026-10-13/CAMBRIAN_C_GEOMETRY.md",
                    "research/2026-10-13/CAMBRIAN_STOCHASTIC_TRANSPORT.md", "research/2026-10-13/CAMBRIAN_AUDIT_C_RAW.json",
                    "research/2026-10-13/CAMBRIAN_SWARM_MANIFEST.json", "research/2026-10-13/CAMBRIAN_PUBLICATION_NOTES.md"],
    }
    hashes = {}
    changed = {}
    for name, ref in SNAPSHOTS.items():
        assert git("merge-base", SNAPSHOTS["PR49"], ref).decode().strip() == (ref if name == "PR49" else BASE)
        hashes[name] = [{"path": p, "blob_sha": git("rev-parse", ref + ":" + p).decode().strip(),
                         "sha256": hashlib.sha256(git("show", ref + ":" + p)).hexdigest()} for p in inspected[name]]
        changed[name] = set(git("diff", "--name-only", BASE, ref).decode().splitlines())
    own = json.loads(git("show", SNAPSHOTS["PR49"] + ":" + ATLAS + "registry.json"))
    sibling = json.loads(git("show", SNAPSHOTS["PR50"] + ":" + ATLAS + "REGISTRY.json"))
    cambrian = json.loads(git("show", SNAPSHOTS["PR51"] + ":research/2026-10-13/CAMBRIAN_SWARM_MANIFEST.json"))
    assert len(set(own["native_agents_genuinely_spawned_so_far"])) == 29
    assert sibling["execution_accounting"]["genuine_child_agents_spawned"] == 21
    assert cambrian["actual_research_workers"] == 6 and cambrian["audit_assignment_count"] == 8
    pins = {name: git("show", ref + ":lean-toolchain").decode().strip()
            for name, ref in SNAPSHOTS.items()}
    assert set(pins.values()) == {"leanprover/lean4:v4.14.0"}
    eos_ref = "b2774ca485db4b5b4f7ce92e535220352fb3af2f"
    eos_path = "formal/obstruction_synthesis/lean-toolchain"
    pins["EOS_isolated"] = git("show", eos_ref + ":" + eos_path).decode().strip()
    assert pins["EOS_isolated"] == "leanprover/lean4:v4.19.0"
    pin = "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84"
    assert pin in git("show", SNAPSHOTS["PR49"] + ":scripts/swm_topology_bootstrap.py").decode()
    assert pin in git("show", SNAPSHOTS["PR50"] + ":formal/swarm_topology/lakefile.lean").decode()
    formal50 = json.loads(git("show", SNAPSHOTS["PR50"] + ":" + ATLAS + "FINAL_KERNEL_RECEIPT.json"))
    formal_hash_matches = {row["file"]: hashlib.sha256(git("show", SNAPSHOTS["PR50"] + ":" + row["file"])).hexdigest() == row["sha256"] for row in formal50["files"]}
    assert all(formal_hash_matches.values())
    collisions = sorted(changed["PR49"] & changed["PR50"])
    assert len(collisions) == 27
    return {"schema_version": 1, "status": "SURVIVES_WITH_EXPLICIT_GATES_SCOPED_REVIEW",
            "snapshots": SNAPSHOTS, "common_base": BASE, "source_hashes": hashes,
            "toolchain_pins": pins, "common_mathlib_pin": pin,
            "EOS_pin_source": {"snapshot": eos_ref, "path": eos_path,
                               "blob_sha": git("rev-parse", eos_ref + ":" + eos_path).decode().strip()},
            "accounting": {"PR49_frozen_recorded_unique_children": 29, "live_total_not_audited": True,
                           "PR50_sibling_reported_children": 21, "PR50_processes_not_independently_witnessed": True,
                           "PR51_manifest_research_workers": cambrian["actual_research_workers"],
                           "PR51_audit_assignments": cambrian["audit_assignment_count"],
                           "owned_plus_sibling_aggregate": None},
            "path_collisions_PR49_PR50": collisions, "formal_PR50_receipt_source_hash_matches": formal_hash_matches,
            "kernel_rerun": False, "full_suite_run": False, "new_children_spawned": 0,
            "control_outputs": controls(), "controls_exit_code": 0,
            "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "reproduce": "python research/2026-10-13/SWARM_ATLAS/comparisons/PARALLEL_AUDIT_probe.py --output research/2026-10-13/SWARM_ATLAS/comparisons/PARALLEL_AUDIT.json"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(receipt(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
