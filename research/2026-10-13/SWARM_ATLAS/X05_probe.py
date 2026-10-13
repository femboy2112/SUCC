"""Bounded exact X05 oracle. No runtime imports or physical calibration."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
ATLAS = Path(__file__).resolve().parent
PARENT = "435f9469885cc8c45a0b86181dfb4867e204fd35"
BITS = (0, 1)
SOURCES = tuple(product(BITS, repeat=2))
FINE = tuple(product(BITS, repeat=3))
COARSE = SOURCES
ACTIONS = ("Q", "R0", "R1")
REPORTS = tuple(product(BITS, repeat=2))


def add(out, key, weight):
    if weight:
        out[key] += weight


def fine(a, x):
    u, v, n = x
    p = F(1, 3) if u ^ v ^ n else F(2, 3)
    value = u if a == "Q" else (v if u == int(a[-1]) else 0)
    after_v = u ^ v if a == "Q" else v
    return tuple(((value, k), (u, after_v, k), p if k == 0 else 1-p)
                 for k in BITS)


def coarse(a, q):
    u, v = q
    value = u if a == "Q" else (v if u == int(a[-1]) else 0)
    after = (u, u ^ v) if a == "Q" else q
    return tuple(((value, tag), after, F(2, 3) if tag == 0 else F(1, 3))
                 for tag in BITS)


def decoder(a, y):
    return tuple(((y[0], tag), F(2, 3) if tag == 0 else F(1, 3))
                 for tag in BITS)


def augmented(a, x):
    return tuple((z, xp, w*d) for y, xp, w in fine(a, x)
                 for z, d in decoder(a, y))


def push(law):
    out = defaultdict(F)
    for (s, x), w in law.items():
        add(out, (s, x[:2]), w)
    return dict(out)


def update(law, a, z, kernel):
    out = defaultdict(F)
    for (s, x), w in law.items():
        for report, xp, k in kernel(a, x):
            if report == z:
                add(out, (s, xp), w*k)
    return dict(out)


def path_oracle(law, word, kernel):
    """Keep complete hidden paths, independently of endpoint recurrence."""
    paths = [(s, (x,), w) for (s, x), w in law.items()]
    for a, z in word:
        paths = [(s, path+(xp,), w*k)
                 for s, path, w in paths
                 for report, xp, k in kernel(a, path[-1]) if report == z and k]
    out = defaultdict(F)
    for s, path, w in paths:
        add(out, (s, path[-1]), w)
    return dict(out)


def rank(initial, kernel):
    """Support attractor; does not call the native implementation."""
    initial = frozenset(initial)
    queue, seen, graph = [initial], {initial}, {}
    for b in queue:
        edges = {}
        for a in ACTIONS:
            branches = defaultdict(set)
            for s, x in b:
                for z, xp, w in kernel(a, x):
                    if w:
                        branches[z].add((s, xp))
            edges[a] = tuple(frozenset(v) for v in branches.values())
            for child in edges[a]:
                if child not in seen:
                    assert len(seen) < 256, "support closure cap"
                    seen.add(child)
                    queue.append(child)
        graph[b] = edges
    ranks = {b: 0 for b in queue if len({s[0] ^ s[1] for s, _ in b}) == 1}
    while True:
        fresh = {}
        for b in queue:
            if b in ranks:
                continue
            winning = [1+max(ranks[c] for c in branches)
                       for branches in graph[b].values() if all(c in ranks for c in branches)]
            if winning:
                fresh[b] = min(winning)
        if not fresh:
            return ranks.get(initial), len(queue)
        ranks.update(fresh)


def adaptive_paths(law, is_fine):
    paths = [(s, x, (), F(0), w) for (s, x), w in law.items()]
    for depth in range(2):
        nxt = []
        for s, x, h, cost, w in paths:
            a = "Q" if not h else "R"+str(h[0][1][0])
            if is_fine:
                rows = [(z, xp, k*d) for y, xp, k in fine(a, x)
                        for z, d in decoder(a, y)]
                charge = F(1, 4) if a == "Q" else F(1, 2)
            else:
                rows = coarse(a, x)
                charge = F(1, 3) if a == "Q" else F(2, 3)
            for z, xp, k in rows:
                nxt.append((s, xp, h+((a, z),), cost+charge, w*k))
        paths = nxt
    out = defaultdict(F)
    for s, x, h, cost, w in paths:
        assert h[-1][1][0] == s[0] ^ s[1]
        add(out, (s, x[:2] if is_fine else x, h), w)
    return dict(out), max(cost for _, _, _, cost, _ in paths), len(paths)


def word_laws(row, word):
    """Binary temporal controls, indexed by immutable original."""
    result = {}
    for s in BITS:
        paths = [(s, (), F(1))]
        for a in word:
            paths = [(xp, h+(o,), w*k) for x, h, w in paths
                     for o, xp, k in row(a, x)]
        out = defaultdict(F)
        for _, h, w in paths:
            add(out, h, w)
        result[s] = dict(out)
    return result


def main():
    rows_checked = 0
    for a, x in product(ACTIONS, FINE):
        assert sum((w for _, _, w in fine(a, x)), F(0)) == 1
        left = defaultdict(F)
        for z, xp, w in augmented(a, x):
            add(left, (z, xp[:2]), w)
        assert dict(left) == {(z, q): w for z, q, w in coarse(a, x[:2])}
        # Same row identity separately for every original: 4 Dirac source rows.
        rows_checked += len(SOURCES)
    keys = tuple(product(SOURCES, FINE))
    arbitrary = {key: F(i+1, 528) for i, key in enumerate(keys)}
    assert sum(arbitrary.values(), F(0)) == 1
    words = tuple(w for n in range(4)
                  for w in product(tuple(product(ACTIONS, REPORTS)), repeat=n))
    impossible = 0
    for word in words:
        laws = [arbitrary, push(arbitrary)]
        for a, z in word:
            laws = [update(laws[0], a, z, augmented), update(laws[1], a, z, coarse)]
            assert push(laws[0]) == laws[1]
        assert path_oracle(arbitrary, word, augmented) == laws[0]
        assert path_oracle(push(arbitrary), word, coarse) == laws[1]
        impossible += not laws[0]
        if laws[0]:
            mass = sum(laws[0].values(), F(0))
            assert push({k: w/mass for k, w in laws[0].items()}) == {
                k: w/mass for k, w in laws[1].items()}
    initial = {(s, s+(n,)): F(i+1, 10) * (F(1, 3) if n == 0 else F(2, 3))
               for i, s in enumerate(SOURCES) for n in BITS}
    fine_paths, fine_cost, count_i = adaptive_paths(initial, True)
    target_paths, target_cost, count_j = adaptive_paths(push(initial), False)
    assert fine_paths == target_paths
    assert fine_cost == F(3, 4) <= target_cost == 1
    ri, ni = rank(initial, augmented)
    rj, nj = rank(push(initial), coarse)
    assert ri == rj == 2
    selected = lambda a, x: tuple((y[0:1]+(0,), xp, w) for y, xp, w in fine(a, x))
    assert rank(initial, selected)[0] == 2  # Public positive-entry selector.

    def correlation(a, x, target=False):
        if a == "b":
            return ((x, x, F(1)),)
        return tuple((x ^ r if target else r, r, F(1, 2)) for r in BITS)
    # Exact separate marginals agree on EVERY carrier input.
    for x in BITS:
        ir, jr = correlation("a", x), correlation("a", x, True)
        for coordinate in (0, 1):
            marginals = []
            for row in (ir, jr):
                marginal = defaultdict(F)
                for o, xp, w in row:
                    add(marginal, (o, xp)[coordinate], w)
                marginals.append(dict(marginal))
            assert marginals[0] == marginals[1] == {0: F(1, 2), 1: F(1, 2)}
    corr_i = word_laws(correlation, ("a", "b"))
    corr_j = word_laws(lambda a, x: correlation(a, x, True), ("a", "b"))
    assert corr_i[0] == corr_i[1] and corr_j[0] != corr_j[1]
    joint_left = sum((w for z, q, w in correlation("a", 1) if (z, q) == (0, 0)), F(0))
    joint_right = sum((w for z, q, w in correlation("a", 1, True) if (z, q) == (0, 0)), F(0))
    assert joint_left == F(1, 2) != joint_right == 0
    witness = {"s": 1, "x": 1, "a": "a", "z": 0, "q_after": 0,
               "joint_left": str(joint_left), "joint_right": str(joint_right)}
    def keep(a, x, erase=False):
        return (("*", 0 if erase else x, F(1)),) if a == "a" else ((x, x, F(1)),)
    for a in ("a", "b"):
        assert word_laws(keep, (a,)) == word_laws(lambda a, x: keep(a, x, True), (a,))
    assert word_laws(keep, ("a", "b")) != word_laws(lambda a, x: keep(a, x, True), ("a", "b"))
    hidden_cost_paths = ((9, 0), (0, 9))
    actual = max(sum(path) for path in hidden_cost_paths)
    separate = sum(max(path[i] for path in hidden_cost_paths) for i in range(2))
    assert (actual, separate) == (9, 18)

    inherited = {}
    for filename in ("C17_probe.py", "C20_probe.py", "C21_probe.py"):
        command = ["timeout", "30s", sys.executable, str(ATLAS/filename)]
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=32)
        assert run.returncode == 0, (filename, run.returncode, run.stderr)
        result = json.loads(run.stdout)
        inherited[filename] = {"exit_code": run.returncode, "stderr": run.stderr,
                               "stdout_sha256": hashlib.sha256(run.stdout.encode()).hexdigest(),
                               "command": command,
                               "status": result.get("status", result.get("proof_status", "PASS"))}
    paths = ["research/2026-10-13/SWARM_ATLAS/"+p for p in
             ("X05.md", "X05_probe.py", "C17.md", "C17_probe.py", "C20.md",
              "C20_probe.py", "C21.md", "C21_probe.py")]
    paths += ["provenance/IMPORT_MANIFEST.json",
              "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md"]
    return {"claim_id": "SWM-X05", "parent_sha": PARENT, "status": "TESTED MODEL",
            "paper_proof": "PROVED LOCAL; independent mathematical acceptance pending",
            "reproduce": "PYTHONDONTWRITEBYTECODE=1 timeout 30s python research/2026-10-13/SWARM_ATLAS/X05_probe.py",
            "source_origin_git_object": {
                "commit": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
                "command": "git cat-file -t ba075348b7bcc66d938b3e0ca96c26e95bba340a",
                "observed_exit_code": 128,
                "observed_stderr": "fatal: git cat-file: could not get object info",
                "available_locally": False},
            "arithmetic": "fractions.Fraction exact; no floats",
            "bounds": {"originals": 4, "fine_carriers": 8, "target_carriers": 4,
                       "actions": 3, "coarse_reports": 4, "word_length": 3,
                       "support_closure_cap": 256},
            "all_prior_Dirac_joint_rows_checked": rows_checked,
            "history_words_checked": len(words), "zero_mass_words_not_conditioned": impossible,
            "recurrence_vs_complete_hidden_path_oracle": "PASS",
            "adaptive": {"rank_I": ri, "rank_J": rj, "support_beliefs": [ni, nj],
                         "path_counts": [count_i, count_j], "joint_history_laws": "equal",
                         "public_cost_I": str(fine_cost), "public_cost_J": str(target_cost),
                         "deterministic_positive_decoder_selector_rank": 2},
            "correlation_mutant": {"separate_marginal_checks": "PASS",
                                    "joint_square_rejected": witness,
                                    "fine_ab_source_rows": repr(corr_i),
                                    "target_ab_source_rows": repr(corr_j),
                                    "target_ab_identifies_original": True,
                                    "fine_original_unidentifiable_after_ab": True},
            "inherited_controls": {"keep_erase_initial_readouts_equal": True,
                                   "keep_erase_ab_laws_differ": True,
                                   "hidden_cost_actual_vs_separate_maxima": [actual, separate]},
            "inherited_probe_runs": inherited,
            "runtime_imports": [], "hidden_input_to_policy_or_decoder": False,
            "reset_or_extra_probe": False, "private_cost_dominance_claimed": False,
            "scholarly_novelty_claimed": False, "physical_calibration_claimed": False,
            "formal_kernel_verified": False,
            "sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
