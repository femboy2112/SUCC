"""Fresh bounded exact witnesses; no author helpers, probes or receipts."""
import resource

CAP = 256 * 1024 * 1024
resource.setrlimit(resource.RLIMIT_AS, (CAP, CAP))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import time

AUTHOR = "/home/leah/succ_lab/swm-f48"
COMMIT = "224d049964b02fc42ad4fcbaa078944ed91da0a7"
BASE = "research/2026-10-13/F48/"


def main():
    started = time.monotonic()
    graph = {"l": {"l", "d"}, "d": set()}
    live = set(graph)
    while True:
        following = {v for v in live if graph[v] & live}
        if following == live:
            break
        live = following
    assert live == {"l"}
    surjective_state_subsystems = []
    for size in range(3):
        for chosen in combinations(graph, size):
            chosen = set(chosen)
            if all(graph[v] & chosen for v in chosen):
                surjective_state_subsystems.append(chosen)
    assert set().union(*surjective_state_subsystems) == live
    raw = [{("l",)}]
    for _ in range(4):
        raw.append({p + (child,) for p in raw[-1] for child in graph[p[-1]]})
    extended = [{p for p in stage if p[-1] in live} for stage in raw]
    assert all({p[:-1] for p in extended[n + 1]} == extended[n]
               for n in range(4))
    assert {p[:-1] for p in raw[2]} != raw[1]

    # All next public reports aggregate to a surjection; a selected report
    # need not extend each private root.
    roots = {0, 1}
    first = {(source, source) for source in roots}
    assert {p[0] for p in first} == roots
    report_zero = {p for p in first if p[1] == 0}
    assert {p[0] for p in report_zero} == {0}

    kraus_squared = ([Fraction(1)], [Fraction(1, 2), Fraction(1, 2)])
    assert all(sum(family) == 1 and all(x > 0 for x in family)
               for family in kraus_squared)
    assert [len(family) for family in kraus_squared] == [1, 2]

    # Every finite source n dies at n+1. The unbounded family is a symbolic
    # countermodel, not a computation of an infinite tree or event.
    for n in range(1, 5):
        assert all(k <= n for k in range(1, n + 1))
        assert not n + 1 <= n
    survival = {k: [n for n in range(1, 5) if k <= n] for k in range(6)}
    assert survival[4] == [4] and survival[5] == []
    cylinder_masses = [Fraction(1, 2**n) for n in range(5)]
    assert all(x > 0 for x in cylinder_masses)

    correlated = {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)}
    anticorrelated = {(0, 1): Fraction(1, 2), (1, 0): Fraction(1, 2)}
    def marginal(law, coordinate):
        return {bit: sum(p for pair, p in law.items() if pair[coordinate] == bit)
                for bit in (0, 1)}
    assert all(marginal(correlated, j) == marginal(anticorrelated, j) for j in (0, 1))
    report_mass = lambda law: sum(p for (s, c), p in law.items() if s == c)
    assert report_mass(correlated) == 1 and report_mass(anticorrelated) == 0
    coarse_actions, fine_actions = {"read"}, {"read", "wait"}
    assert coarse_actions <= fine_actions and coarse_actions != fine_actions
    enabled = {"fresh": True, "spent": False}
    assert enabled["fresh"] != enabled["spent"]

    states = list(product((0, 1), repeat=2))
    delays = {(a, b): (a, b) for a, b in states}
    assert len(set(delays.values())) == 4
    alpha = beta = gamma = 0  # Forced by equality at 00,10,01.
    assert all(alpha + beta*a + gamma*b == a*b for a, b in states[:3])
    assert alpha + beta + gamma != 1
    atoms = {"a": ("s0", "q0"), "b": ("s1", "q0"), "c": ("s0", "q1")}
    exact_image = {"a"}
    facets = ({"a", "b"}, {"a", "c"})
    assert all(exact_image < facet for facet in facets)
    assert atoms["b"][0] not in {atoms[x][0] for x in exact_image}
    assert atoms["c"][1] not in {atoms[x][1] for x in exact_image}

    source_maps = {}
    for name in ("F48_PHASE2_ARCHITECTURE.md", "F48_VALIDATION_MATRIX.md"):
        data = subprocess.check_output(["git", "-C", AUTHOR, "show", f"{COMMIT}:{BASE}{name}"])
        source_maps[name] = sha256(data).hexdigest()
        if name == "F48_PHASE2_ARCHITECTURE.md":
            text = data.decode()
            core = text[text.index("## 5."):text.index("## 7.")]
    result = {
        "review": "F48_PHASE2_A03_REVIEW", "author_commit": COMMIT,
        "source_sha256": source_maps, "sections_5_6_sha256": sha256(core.encode()).hexdigest(),
        "configured_address_space_cap_bytes": CAP, "configured_cpu_cap_seconds": 25,
        "author_helpers_or_probes_imported": False,
        "finite_full_graph": {"live_core": sorted(live),
                              "raw_stage_counts": [len(s) for s in raw],
                              "extendable_stage_counts": [len(s) for s in extended],
                              "closed_state_subsystems": [sorted(s) for s in surjective_state_subsystems]},
        "public_arrow_scope": {"aggregate_root_image": sorted(roots), "report_0_root_image": [0]},
        "Kraus_label_counts": [1, 2], "Kraus_squared_weights": [[str(x) for x in f] for f in kraus_squared],
        "finite_parameter_cap_4_survivors": survival,
        "unbounded_parameter_proof_receipt": "At every depth k choose n>=k; each fixed n is killed at n+1.",
        "nonclosed_admission_proof_receipt": {"admitted": "infinitely many 1s",
                                              "finite_zero_prefix_realizer": "0^n followed by 1^omega",
                                              "unadmitted_coherent_limit": "0^omega"},
        "positive_finite_cylinder_masses": [str(x) for x in cylinder_masses],
        "infinite_singleton_mass": "limit 2^-n = 0, by continuity from above; not an executed infinite event",
        "same_marginals_different_joint_reports": [str(report_mass(correlated)), str(report_mass(anticorrelated))],
        "one_way_action_lifting": {"coarse": sorted(coarse_actions), "fine": sorted(fine_actions)},
        "memory_omission_enabled_values": enabled,
        "two_delay_point_recovery": True, "linear_dictionary_captures_ab": False,
        "facets": [sorted(f) for f in facets], "exact_selected_image": sorted(exact_image),
        "facet_added_original": atoms["b"], "facet_added_current": atoms["c"],
        "scope": "Tiny exact controls and symbolic proof receipts; no infinitary membership computation",
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "self_peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "exit_code": 0, "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
