#!/usr/bin/env python3
"""Exact bounded B15 controls; universal finality is proved in B15.md."""
from collections import deque
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.eodcs_multi_action_source import ActionSource, action_congruence
from observational_succ.causal_nerode_succ import SourceChart
from observational_succ.eodcs_relational_choice import RelationalIntervention, relational_descent
from observational_succ.carrier_statistical_limit import OperationalKernel

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def partition(states, outputs, row_signature):
    blocks = (tuple(states),)
    while True:
        classes = {s: i for i, block in enumerate(blocks) for s in block}
        grouped = {}
        for s in states:
            grouped.setdefault((outputs[s], row_signature(s, classes)), []).append(s)
        nxt = tuple(tuple(xs) for xs in grouped.values())
        if nxt == blocks:
            return blocks
        blocks = nxt


def deterministic():
    src = ActionSource("B15-Moore", 0, "binary", ("s", "t", "u", "v"),
                       ("0", "0", "0", "1"), ("a", "b"),
                       (("u", "u", "u", "v"), ("v", "v", "u", "v")))
    cert = action_congruence(src)
    blocks = cert.equivalence_classes
    assert blocks == (("s", "t"), ("u",), ("v",))
    beta = {s: i for i, block in enumerate(blocks) for s in block}
    output = tuple(src.report(block[0]) for block in blocks)
    step = tuple(tuple(beta[src.step(block[0], a)] for a in src.actions)
                 for block in blocks)

    # Each root denotes an actual function A* -> O by this finite presentation.
    def behavior(root, word):
        for a in word:
            root = step[root][src.actions.index(a)]
        return output[root]

    # The coalgebra square and quotient equations are exhaustive on actual maps.
    for s in src.states:
        assert output[beta[s]] == src.report(s)
        for i, a in enumerate(src.actions):
            assert step[beta[s]][i] == beta[src.step(s, a)]
    for h in range(4):
        for w in product(src.actions, repeat=h):
            for s in src.states:
                assert behavior(beta[s], w) == src.observe(s, w)
                for i, a in enumerate(src.actions):
                    assert behavior(beta[s], (a,) + w) == behavior(step[beta[s]][i], w)
    morphisms = []
    for values in product(range(len(blocks)), repeat=len(src.states)):
        f = dict(zip(src.states, values))
        if all(output[f[s]] == src.report(s) and
               all(step[f[s]][i] == f[src.step(s, a)] for i, a in enumerate(src.actions))
               for s in src.states):
            morphisms.append(f)
    assert morphisms == [beta]
    bad = ("s", "u", "b", src.observe("s", ("b",)), src.observe("u", ("b",)))
    assert src.report("s") == src.report("u") and bad[-2] != bad[-1]
    return {"beta": beta, "quotient_blocks": blocks, "quotient_output": output,
            "quotient_transitions_a_b": step, "finite_image_morphism_count": len(morphisms),
            "sample_word_bound": 3, "old_report_collapse_hostile_witness": bad}


def relational():
    states = ("p", "q", "r", "d")
    out = dict(zip(states, ("0", "0", "0", "1")))
    edges = {"p": ("p", "r", "d"), "q": ("q", "d"), "r": ("r",), "d": ("d",)}
    blocks = partition(states, out, lambda s, cls: tuple(sorted({cls[t] for t in edges[s]})))
    assert not any("p" in b and "q" in b for b in blocks)
    # Exact language equivalence by exhausting reachable subset-pairs, not a horizon.
    queue = deque([(frozenset({"p"}), frozenset({"q"}))])
    seen = set(queue)
    while queue:
        left, right = queue.popleft()
        assert bool(left) == bool(right)
        for o in ("0", "1"):
            pair = tuple(frozenset(t for s in xs for t in edges[s] if out[t] == o)
                         for xs in (left, right))
            if pair not in seen:
                seen.add(pair)
                queue.append(pair)
    before = SourceChart("B15-relation", 0, "binary", ("p", "q"), ("0", "0"))
    after = SourceChart("B15-relation", 1, "binary", states, tuple(out.values()))
    local = relational_descent(RelationalIntervention("a", before, after,
                                                      (edges["p"], edges["q"])))
    assert local.descended_to_set_valued_observer
    return {"states": states, "outputs": out, "successors": edges,
            "all_finite_output_traces_equal": True, "reachable_subset_pairs": len(seen),
            "bisimulation_blocks": blocks, "one_step_native_descent": True,
            "hostile_branch": "p -> r has no bisimilar q-successor",
            "minimum_state_scope": "complete unary Moore systems, any output set: 4 (proof in dossier)"}


def probabilistic():
    states = ("p", "q", "z0", "u", "r", "z1")
    out = {s: str(int(s == "z1")) for s in states}
    rows = {"p": {"z0": Q(1, 2), "u": Q(1, 2)}, "q": {"r": Q(1)},
            "z0": {"z0": Q(1)}, "u": {"z1": Q(1)},
            "r": {"z0": Q(1, 2), "z1": Q(1, 2)}, "z1": {"z1": Q(1)}}
    assert all(sum(row.values(), Q()) == 1 for row in rows.values())
    blocks = partition(states, out, lambda s, cls: tuple(
        sum((m for t, m in rows[s].items() if cls[t] == i), Q())
        for i in range(max(cls.values()) + 1)))
    assert not any("p" in b and "q" in b for b in blocks)

    def traces(s, transitions):
        law = {(out[s],): Q(1)}
        frontier = {(s, (out[s],)): Q(1)}
        for _ in range(transitions):
            nxt = {}
            for (current, word), mass in frontier.items():
                for t, weight in rows[current].items():
                    key = (t, word + (out[t],))
                    nxt[key] = nxt.get(key, Q()) + mass * weight
            frontier = nxt
        law = {}
        for (_, word), mass in frontier.items():
            law[word] = law.get(word, Q()) + mass
        return law

    for n in range(5):
        assert traces("p", n) == traces("q", n)
    assert rows["p"].get("u", Q()) == Q(1, 2) and rows["q"].get("u", Q()) == 0
    return {"rows": rows, "outputs": out, "bisimulation_blocks": blocks,
            "sample_transition_bound": 4, "two_transition_trace_law": traces("p", 2),
            "all_lengths_proof": "after 00, both choose absorbing 0/1 with probability 1/2",
            "mass_to_behavior_class_u_p_q": (Q(1, 2), Q(0))}


def history():
    a = "a"
    rows = {((), a): (Q(1, 2), Q(1, 2))}
    for bit in (0, 1):
        rows[(((a, bit),), a)] = (Q(1), Q(0))
        rows[(((a, bit), (a, 0)), a)] = (Q(1 - bit), Q(bit))
    kernel = OperationalKernel("B15-history", (a,), (0, 1), 3, rows)
    policy = {h: a for h, _ in rows}
    law = kernel.policy_distribution(policy)
    assert kernel.internal_realization().run_policy(policy) == law
    h0, h1 = ((a, 0), (a, 0)), ((a, 1), (a, 0))
    assert h0[-1] == h1[-1] and rows[h0, a] != rows[h1, a]
    return {"same_last_report_histories": (h0, h1), "next_rows": (rows[h0, a], rows[h1, a]),
            "history_augmented_policy_law": law, "terminal_extension_claimed": False}


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


if __name__ == "__main__":
    paths = ("provenance/IMPORT_MANIFEST.json", "observational_succ/eodcs_multi_action_source.py",
             "observational_succ/nerode_probe_growth.py", "observational_succ/eodcs_relational_choice.py",
             "observational_succ/carrier_statistical_limit.py", "observational_succ/operational_semantics.py")
    for p in paths:
        frozen = subprocess.check_output(["git", "show", BASE + ":" + p], cwd=ROOT)
        assert frozen == (ROOT / p).read_bytes(), "Source changed from declared parent"
    receipt = {"base_commit": BASE, "input_sha256": {
        p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        "deterministic": deterministic(), "relational": relational(),
        "probabilistic": probabilistic(), "history": history(),
        "status": "TESTED MODEL; universal theorems and counterexamples derived in B15.md",
        "universal_finality_machine_checked": False, "full_suite_run": False}
    print(json.dumps(serial(receipt), indent=2, sort_keys=True))
