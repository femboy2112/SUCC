#!/usr/bin/env python3
"""B16: bounded exact source-realizer oracle; never samples an infinite source."""
import hashlib
import json
import sys
from collections import deque
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.nerode_probe_growth import ObserverDynamics, nerode_fixpoint
from observational_succ.eodcs_multi_action_source import ActionSource, action_congruence
from observational_succ.voyager_profinite_frontier import powers_of_two_pulse

PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def lasso(word):
    """Smallest compatible orbit, with explicit witness, not a suffix heuristic."""
    if not word:
        return 1, 0, 1
    return min((m + p, m, p) for m in range(len(word))
               for p in range(1, len(word) - m + 1)
               if all(word[i] == word[i + p]
                      for i in range(m, len(word) - p)))


def brute_minima(alphabet, horizon):
    """Enumerate complete Moore machines, independent of lasso minimization."""
    best = {}
    machines = 0
    for n in range(1, horizon + 1):
        for reports in product(alphabet, repeat=n):
            for transition in product(range(n), repeat=n):
                machines += 1
                state, trace = 0, []
                for _ in range(horizon):
                    trace.append(reports[state])
                    state = transition[state]
                best.setdefault(tuple(trace), n)
    for word in product(alphabet, repeat=horizon):
        assert best[word] == lasso(word)[0], (word, best[word], lasso(word))
    return machines, len(best)


def pair_classes(reports, transitions):
    """Pair-graph future distinguishability, independent of partition refinement."""
    n = len(reports)
    classes = []
    for i in range(n):
        for block in classes:
            queue, seen, equal = deque([(i, block[0])]), set(), True
            while queue:
                s, t = queue.popleft()
                if (s, t) in seen:
                    continue
                seen.add((s, t))
                if reports[s] != reports[t]:
                    equal = False
                    break
                queue.extend((u[s], u[t]) for u in transitions)
            if equal:
                block.append(i)
                break
        else:
            classes.append([i])
    return classes


def canonical(prefix, cycle):
    p = next(d for d in range(1, len(cycle) + 1)
             if len(cycle) % d == 0
             and all(cycle[i] == cycle[i % d] for i in range(len(cycle))))
    m = len(prefix)
    def value(t):
        return prefix[t] if t < len(prefix) else cycle[(t-len(prefix)) % len(cycle)]
    while m and value(m - 1) == value(m - 1 + p):
        m -= 1
    return m, p


def main():
    enumeration = [dict(alphabet=a, horizon=h, machines=n, words=w)
                   for a, h in [("01", 4), ("abc", 3)]
                   for n, w in [brute_minima(tuple(a), h)]]
    checked = 0
    for m in range(3):
        for p in range(1, 4):
            for word in product(("(", ")", "µ"), repeat=m+p):
                states = tuple("q"+str(i) for i in range(m+p))
                transition = tuple(range(1, m+p)) + (m,)
                src = ObserverDynamics("B16-lasso", 0, "atomic-symbols", states,
                                       tuple(states[i] for i in transition), word)
                expected = sum(canonical(word[:m], word[m:]))
                independent = pair_classes(word, (transition,))
                native = nerode_fixpoint(src)
                assert len(independent) == len(native.stable_classes) == expected
                checked += 1
    # Bounded Dyck language: actual quotient maps, not a visual analogy.
    depth = 3
    states = tuple(str(i) for i in range(depth+1)) + ("dead",)
    reports = ("yes",) + ("no",) * (depth+1)
    opens = tuple(range(1, depth+2)) + (depth+1,)
    closes = (depth+1,) + tuple(range(depth)) + (depth+1,)
    source = ActionSource("B16-bounded-Dyck", 0, "stack-depth", states, reports,
                          ("(", ")"), tuple(tuple(states[i] for i in u)
                                              for u in (opens, closes)))
    certificate = action_congruence(source)
    blocks = pair_classes(reports, (opens, closes))
    assert len(blocks) == len(certificate.equivalence_classes) == depth+2
    quotient = {s: i for i, block in enumerate(certificate.equivalence_classes)
                for s in block}
    for block in certificate.equivalence_classes:
        for a in source.actions:
            assert len({quotient[source.step(s, a)] for s in block}) == 1
    # Repeat nested markers: displayed depth/number of gaps does not add debt.
    assert sum(canonical((), tuple("(())"))) == 4
    assert sum(canonical((), tuple("XXXX"))) == 1
    assert canonical(("a",), ("b", "a")) == (0, 2)
    duplicates = ObserverDynamics("B16-many-to-one", 0, "constant-cycle",
                                  tuple(str(i) for i in range(6)),
                                  tuple(str((i+1) % 6) for i in range(6)),
                                  ("X",) * 6)
    duplicate_blocks = nerode_fixpoint(duplicates).stable_classes
    assert len(duplicate_blocks) == 1
    duplicate_map = {s: 0 for s in duplicates.states}
    assert all(duplicate_map[duplicates.step(s)] == 0
               and duplicates.report(s) == "X" for s in duplicates.states)
    partial = (0, 0, 1, 0)
    compatible = lambda i, j: all(partial[i+k] == partial[j+k]
                                 for k in range(len(partial)-max(i, j)))
    assert compatible(0, 3) and compatible(3, 1) and not compatible(0, 1)
    def dyck(word):
        balance = 0
        for c in word:
            balance += 1 if c == "(" else -1
            if balance < 0:
                return False
        return balance == 0
    witnesses = [(i, j, ")"*i) for i in range(6) for j in range(i+1, 6)]
    assert all(dyck("("*i+w) != dyck("("*j+w) for i, j, w in witnesses)
    pulses = []
    for k in range(1, 7):
        word = tuple(powers_of_two_pulse(i) for i in range(2**(k+1)+1))
        count, m, p = lasso(word)
        assert count >= 2**k
        pulses.append(dict(k=k, horizon=len(word), gap_bound=2**k,
                           exact_prefix_minimum=count, witness_preperiod=m, witness_period=p))
    paths = ["observational_succ/nerode_probe_growth.py",
             "observational_succ/eodcs_multi_action_source.py",
             "observational_succ/voyager_profinite_frontier.py",
             "formal/EODCS_VoyagerMemoryDebt.lean"]
    print(json.dumps(dict(parent=PARENT, status="TESTED MODEL", exact_arithmetic=True,
                         finite_prefix_enumeration=enumeration,
                         ternary_lassos_checked=checked, pulse_prefixes=pulses,
                         bounded_dyck=dict(depth=depth, source_states=len(states),
                                           residual_classes=len(blocks), quotient_map=quotient),
                         reachable_six_cycle=dict(source_states=6, residual_states=1,
                                                  quotient_map=duplicate_map),
                         unrestricted_dyck_six_residual_witnesses=witnesses,
                         nested_period_states=4, collapsed_markers_states=1,
                         finite_overlap_compatibility_nontransitive=True,
                         native_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                        for p in paths},
                         probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         command="timeout 30s python research/2026-10-13/SWARM_ATLAS/B16_probe.py",
                         timeout_seconds=30,
                         physical_source_authenticated=False,
                         infinite_computation_executed=False), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
