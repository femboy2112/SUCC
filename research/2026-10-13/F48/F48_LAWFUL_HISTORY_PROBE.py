"""Independent exact F48 receipts. Standard library, no SUCC imports."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess


BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def relation(mask):
    return {pair for bit, pair in enumerate(product(range(2), repeat=2))
            if mask & (1 << bit)}


def main():
    # Two edges cover a three-vertex line. Independent global enumeration
    # is compared with the fiber product of independently enumerated edges.
    models = pairs_checked = 0
    for first_mask, second_mask in product(range(16), repeat=2):
        first, second = relation(first_mask), relation(second_mask)
        joined = {(a, b, d) for a, b in first for c, d in second if b == c}
        global_paths = {(a, b, c) for a, b, c in product(range(2), repeat=3)
                        if (a, b) in first and (b, c) in second}
        assert joined == global_paths
        for left in first:
            for right in second:
                pairs_checked += 1
                extensions = {p for p in global_paths
                              if p[:2] == left and p[1:] == right}
                assert len(extensions) == int(left[1] == right[0])
        models += 1

    # Forgetting the shared private state turns an incompatible pair into
    # equal public overlap reports. Both local images exist, the global
    # public image is empty. This is failed sheaf existence after projection.
    left, right = {(0, 0)}, {(1, 0)}
    coarse = lambda private_state: 0
    assert coarse(0) == coarse(1)
    assert not {(a, b, d) for a, b in left for c, d in right if b == c}
    # A stronger mutation has a genuine global section, but the specific
    # coarse-compatible local family still has no global extension.
    inhabited_left = {(0, 0), (1, 1)}
    inhabited_global = {(a, b, d) for a, b in inhabited_left
                        for c, d in right if b == c}
    projected_global = {(a, coarse(b), d) for a, b, d in inhabited_global}
    assert inhabited_global == {(1, 1, 0)}
    assert (0, coarse(0), 0) not in projected_global

    # Nondeterministic paths retain intermediate choices even after merging.
    private_paths = {("sigma", ("P", "L", "Z")),
                     ("sigma", ("P", "R", "Z"))}
    endpoint_pairs = {(sigma, states[-1]) for sigma, states in private_paths}
    assert len(private_paths) == 2 and len(endpoint_pairs) == 1
    # Truncation is an actual function on paths and is strictly coherent.
    for _, states in private_paths:
        assert states[:2][:1] == states[:1]
    # An endpoint-only object has two different private predecessors.
    assert {states[-2] for _, states in private_paths} == {"L", "R"}

    source_states = tuple(product(range(2), repeat=2))

    def action(state, name, destructive=True):
        a, b = state
        if name == "A":
            return a, (a, 0) if destructive else state
        if name == "B":
            return b, (0, b) if destructive else state
        raise ValueError("undeclared action")

    def run(source, names, destructive=True):
        current, outputs = source, []
        for name in names:
            outcome, current = action(current, name, destructive)
            outputs.append(outcome)
        return tuple(outputs), current

    destructive_joint = {run(s, names)[0] for s in source_states
                         for names in (("A", "B"), ("B", "A"))}
    assert (1, 1) not in destructive_joint
    assert action((1, 1), "A")[0] == action((1, 1), "B")[0] == 1
    assert run((1, 1), ("A", "B"), False)[0] == (1, 1)
    shadows = {}
    for name, rival in (("A", (0, 1)), ("B", (1, 0))):
        assert run((0, 0), (name,)) == run(rival, (name,))
        assert (rival[0] ^ rival[1]) != 0
        shadows[name] = {"sources": [[0, 0], list(rival)],
                         "common_public_and_post": run(rival, (name,))}

    # Exact positive full-support joint laws share their one-bit marginals.
    independent = {s: Q(1, 4) for s in source_states}
    correlated = {s: Q(3, 8) if s[0] == s[1] else Q(1, 8)
                  for s in source_states}
    for axis, value in product(range(2), repeat=2):
        assert sum(w for s, w in independent.items() if s[axis] == value) == Q(1, 2)
        assert sum(w for s, w in correlated.items() if s[axis] == value) == Q(1, 2)
    assert set(independent) == set(correlated) and independent != correlated

    # Pairwise fair anticorrelation requires three Boolean inequalities;
    # no global Boolean assignment can satisfy them simultaneously.
    triangle_realizers = [s for s in product(range(2), repeat=3)
                          if s[0] != s[1] and s[1] != s[2] and s[0] != s[2]]
    assert triangle_realizers == []
    anticorrelation = {(0, 1): Q(1, 2), (1, 0): Q(1, 2)}
    for axis, value in product(range(2), repeat=2):
        assert sum(w for s, w in anticorrelation.items() if s[axis] == value) == Q(1, 2)

    root = Path(__file__).resolve().parents[3]
    source_paths = [
        "AGENTS.md", "docs/METHOD.md", "docs/FOUNDATIONS.md",
        "docs/ARCHITECTURE.md", "provenance/IMPORT_MANIFEST.json",
        "observational_succ/noncommuting_proof_transport.py",
        "observational_succ/adaptive_proof_policy.py",
        "observational_succ/proof_backaction_debt.py",
        "observational_succ/causal_nerode_succ.py",
        "observational_succ/eodcs_relational_choice.py",
        "observational_succ/operational_yoneda_descent.py",
        "observational_succ/voyager_profinite_frontier.py",
        "research/2026-10-11/PROBE_COHERENCE_HORIZONS_AND_PROOF_SUPPORT.md",
        "research/2026-10-11/NONCOMMUTING_PROOF_TRANSPORT.md",
        "research/2026-10-13/EODCS_CAUSAL_NERODE_PROBE_GENESIS.md",
        "research/2026-10-13/VOYAGER_OBSERVATIONAL_PROFINITE_COMPLETION.md",
        "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
    ]
    hashes = {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
              for p in source_paths}
    for p in source_paths:
        frozen = subprocess.check_output(["git", "show", BASE + ":" + p], cwd=root)
        assert hashlib.sha256(frozen).hexdigest() == hashes[p]
    print(json.dumps({
        "investigator": "F48", "phase": "initial independent",
        "immutable_base": BASE,
        "scope": "finite declared mathematical models; no physical attestation",
        "commands": [{"command": "env PYTHONDONTWRITEBYTECODE=1 python research/2026-10-13/F48/F48_LAWFUL_HISTORY_PROBE.py", "exit": 0}],
        "edge_gluing": {"binary_relation_models": models,
                        "local_pairs_checked": pairs_checked,
                        "full_interface_equalizer": True},
        "coarse_overlap_no_go": {"left": [[0, 0]], "right": [[1, 0]],
                                 "common_public_overlap": 0,
                                 "private_global_sections": 0,
                                 "inhabited_global_mutant": sorted(inhabited_global),
                                 "unextendable_coarse_family": [0, 0, 0]},
        "private_path_vs_endpoint": {"path_count": len(private_paths),
                                     "endpoint_pair_count": len(endpoint_pairs)},
        "destructive_single_carrier": {"joint_reports": sorted(destructive_joint),
                                       "local_11_exists": True,
                                       "joint_11_exists": False,
                                       "nondestructive_11_exists": True,
                                       "original_parity_shadows": shadows},
        "probability_gluing": {"same_fair_marginals_and_full_support": True,
                                "joint_laws_distinct": True,
                                "independent_11": str(independent[(1, 1)]),
                                "correlated_11": str(correlated[(1, 1)]),
                                "anticorrelation_triangle_realizers": triangle_realizers},
        "source_sha256": hashes,
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "full_suite_or_compiler_run": False,
        "final_swarm_synthesis_complete": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
