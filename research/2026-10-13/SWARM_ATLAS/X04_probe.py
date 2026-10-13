#!/usr/bin/env python3
"""X04 exact bounded calibration; infinite claims belong to the written proof."""
from collections import deque
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PARENT = "d5801ec680663717b4c93e72df96bfbd5a26a0f6"


def phase(graph):
    """Independent simple-cycle gcd, checked against rooted edge differences."""
    n = len(graph)
    lengths = set()
    for start in range(n):
        def visit(path):
            for target in graph[path[-1]]:
                if target == start:
                    lengths.add(len(path))
                elif target not in path:
                    visit(path + (target,))
        visit((start,))
        seen, queue = {start}, deque([start])
        while queue:
            for target in graph[queue.popleft()]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        assert len(seen) == n
    d = 0
    for length in lengths:
        d = gcd(d, length)
    assert d > 0
    distances, queue = {0: 0}, deque([0])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                queue.append(w)
    edge_gcd = 0
    for v, targets in enumerate(graph):
        for w in targets:
            edge_gcd = gcd(edge_gcd, abs(distances[v] + 1 - distances[w]))
    assert d == edge_gcd
    c = tuple(distances[v] % d for v in range(n))
    assert all((c[v] + 1) % d == c[w]
               for v, targets in enumerate(graph) for w in targets)
    return d, c, sorted(lengths)


def blocks(graph, width):
    words = [(v,) for v in range(len(graph))]
    for _ in range(width - 1):
        words = [word + (w,) for word in words for w in graph[word[-1]]]
    index = {word: i for i, word in enumerate(words)}
    edges = [(i, index[word[1:] + (w,)]) for i, word in enumerate(words)
             for w in graph[word[-1]]]
    return words, edges


def normalize(values):
    labels = {}
    return tuple(labels.setdefault(v, len(labels)) for v in values)


def partitions(n, prefix=(0,)):
    if len(prefix) == n:
        yield prefix
    else:
        for value in range(max(prefix) + 2):
            yield from partitions(n, prefix + (value,))


def successor(labels, edges):
    targets = {}
    for v, w in edges:
        if labels[v] in targets and targets[labels[v]] != labels[w]:
            return None
        targets[labels[v]] = labels[w]
    return targets


def audit(graph, widths):
    d, c, cycles = phase(graph)
    rows = []
    for width in widths:
        words, edges = blocks(graph, width)
        expected = {normalize(c[word[0]] % k for word in words)
                    for k in range(1, d + 1) if d % k == 0}
        actual, examined = set(), 0
        for labels in partitions(len(words)):
            examined += 1
            transition = successor(labels, edges)
            if transition is not None:
                actual.add(labels)
                assert all(transition[labels[v]] == labels[w] for v, w in edges)
        assert actual == expected
        rows.append(dict(width=width, blocks=len(words), partitions=examined,
                         lawful_partitions=sorted(actual)))
    return dict(period=d, cyclic_phase=c, simple_cycle_lengths=cycles, widths=rows)


def residual_cycle(word):
    """Exact suffix equality for a supplied periodic source, without truncation."""
    n = len(word)
    traces = [word[i:] + word[:i] for i in range(n)]
    labels = normalize(traces)
    edges = [(i, (i + 1) % n) for i in range(n)]
    assert successor(labels, edges) is not None
    assert all(traces[(i + 1) % n] == traces[i][1:] + traces[i][:1]
               and traces[i][0] == word[i] for i in range(n))
    return dict(source_states=n, residual_states=len(set(labels)),
                quotient_map=labels, trace_representatives=traces,
                current_report_autonomous=successor(word, edges) is not None)


def inherited(name):
    command = [sys.executable, "-B", str(HERE / (name + "_probe.py"))]
    run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                         timeout=30, check=True)
    parsed = json.loads(run.stdout)
    assert parsed == json.loads((HERE / (name + "_receipt.json")).read_text())
    return parsed, dict(command=[sys.executable, "-B", str((HERE / (name + "_probe.py")).relative_to(ROOT))],
                        exit=run.returncode, saved_receipt_equal=True,
                        stdout_sha256=sha256(run.stdout.encode()).hexdigest())


def main():
    graphs = {
        "D25_period2": ((2,), (2,), (0, 1)),
        "full_binary": ((0, 1), (0, 1)),
        "branching_period3": ((1,), (2,), (0, 3), (1,)),
        "cycle6": tuple(((i + 1) % 6,) for i in range(6)),
        "C_self_loop_mutant": ((2,), (2,), (0, 1, 2)),
        "cycles2_and3": ((1,), (0, 2), (0,)),
    }
    checks = {name: audit(graph, (1, 2, 3) if name not in
                         ("C_self_loop_mutant", "cycles2_and3") else (1, 2))
              for name, graph in graphs.items()}
    counter = residual_cycle((0, 0, 1))
    assert counter["residual_states"] == 3 and not counter["current_report_autonomous"]
    redundant = residual_cycle(("X",) * 6)
    assert redundant["residual_states"] == 1
    prefixes = []
    for n in range(1, 9):
        # Each binary prefix followed by 0^omega is an explicit legal source.
        words = tuple(product((0, 1), repeat=n))
        assert len(set(words)) == 2 ** n
        assert all(w in graphs["full_binary"][v] for word in words
                   for v, w in zip(word, word[1:]))
        prefixes.append(dict(width=n, distinct_trace_prefixes=len(words)))
    sample = (0, 0, 1, 0)
    compatible = lambda i, j: all(sample[i + k] == sample[j + k]
                                 for k in range(len(sample) - max(i, j)))
    assert compatible(0, 3) and compatible(3, 1) and not compatible(0, 1)
    d25, d25_run = inherited("D25")
    b16, b16_run = inherited("B16")
    assert all(d25["fixed_boundary"]["binary_flip_fails_for_both_labels"])
    assert b16["finite_overlap_compatibility_nontransitive"]
    assert b16["reachable_six_cycle"]["residual_states"] == 1
    paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
             "research/2026-10-13/SWARM_ATLAS/PROTOCOL.md",
             "research/2026-10-13/SWARM_ATLAS/X04.md"]
    paths += [str((HERE / (n + suffix)).relative_to(ROOT)) for n in ("D25", "B16")
              for suffix in (".md", "_probe.py", "_receipt.json")]
    result = dict(claim_id="SWM-X04", source_parent=PARENT,
                  status="PROVED LOCAL paper; TESTED MODEL finite receipt; independent acceptance pending",
                  command="timeout 60s python -B research/2026-10-13/SWARM_ATLAS/X04_probe.py",
                  python_version=sys.version.split()[0], graph_controls=checks,
                  period3_counterexample=counter, redundant_six_cycle=redundant,
                  full_binary_prefix_separators=prefixes,
                  truncated_suffix_compatibility=dict(prefix=sample, pairs=[[0, 3, True], [3, 1, True], [0, 1, False]]),
                  inherited=dict(D25=d25_run, B16=b16_run),
                  retained_controls=dict(D25_boundary=d25["fixed_boundary"],
                                         D25_mutation=d25["synthetic_C_self_loop_mutation"],
                                         B16_redundant=b16["reachable_six_cycle"],
                                         B16_truncation_nontransitive=True),
                  primary_sources=[dict(url="https://people.math.harvard.edu/~shlomo/docs/dynamical_systems.pdf",
                                        inspected="Sections 8.4-8.5; period and higher-block factor context"),
                                   dict(url="https://arxiv.org/pdf/1209.1872",
                                        inspected="Krieger 2012, page 6; word Shannon graph retains entire futures")],
                  source_sha256={p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
                  probe_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  infinite_computation_executed=False, physical_source_authenticated=False,
                  natural_acim_identified=False, academic_novelty_claimed=False,
                  independence="Exact algorithm contrasts share reasoner and fixtures; inherited reviews are separately authored")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
