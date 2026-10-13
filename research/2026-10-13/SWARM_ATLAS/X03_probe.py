"""Exact typed-constructor CEGIS; no production imports or source mutations.

Run: python -B research/2026-10-13/SWARM_ATLAS/X03_probe.py
The universal acceptance argument is X03.md; finite checks are corroboration.
"""
from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/2026-10-13/SWARM_ATLAS"
PARENT = "122c385843248b517fa05a39bd3cfeb5458621b5"
EDGES = ((0, 1), (1, 2), (0, 2), (0, 1))  # a,b,c,d; tree a,b
SOURCE = ("X03-declared-integral-class", 0, EDGES)


@dataclass(frozen=True)
class ClosedWalk:
    steps: tuple[tuple[int, int], ...]

    def __post_init__(self):
        vertex = 0
        for edge, sign in self.steps:
            if type(edge) is not int or edge not in range(4) or sign not in (-1, 1):
                raise ValueError("Invalid source-dart type")
            tail, head = EDGES[edge][::sign]
            if vertex != tail:
                raise ValueError("Noncomposable formal walk")
            vertex = head
        if not self.steps or vertex != 0:
            raise ValueError("Expected a nonempty closed source walk")


# Actual typed composition, including reversed original darts.
LOOPS = (ClosedWalk(((0, 1), (3, -1))),
         ClosedWalk(((0, 1), (1, 1), (2, -1))))


@dataclass(frozen=True)
class Guard:
    walk: ClosedWalk
    constructor: str

    def __post_init__(self):
        if not isinstance(self.walk, ClosedWalk) or self.constructor not in (
                "ResidueSum[2,3]", "IntegralSourceSum"):
            raise ValueError("No untyped guard or source-changing constructor")

    def read(self, weights):
        if self.constructor == "IntegralSourceSum":
            return (sum(sign * weights[edge] for edge, sign in self.walk.steps),)
        # Modular mode reads only each source dart's residues, then composes.
        return tuple(sum(sign * (weights[edge] % m)
                         for edge, sign in self.walk.steps) % m for m in (2, 3))


@dataclass(frozen=True)
class Program:
    guards: tuple[Guard, ...]

    def run(self, weights):
        if len(weights) != 4 or any(type(x) is not int for x in weights):
            raise ValueError("Exact declared integer labels required")
        for guard in self.guards:
            reading = guard.read(weights)
            if any(reading):
                return ("OBSTRUCTED", guard, reading)
        return ("GLUED", (0, weights[0], weights[0] + weights[1]))


def compile_genome(genome):
    """Nine ASTs; mutation introduces a typed sum/branch, not a fitted scalar."""
    return Program(tuple(Guard(loop, ("", "ResidueSum[2,3]",
                                      "IntegralSourceSum")[gene])
                         for loop, gene in zip(LOOPS, genome) if gene))


def verify_semantics(weights, result):
    """Independent raw equation/walk certificate checker; no Guard.read call."""
    if result[0] == "GLUED":
        potential = result[1]
        return all(potential[v] - potential[u] == w
                   for (u, v), w in zip(EDGES, weights))
    guard, claimed = result[1:]
    incidence = [0, 0, 0]
    total = 0
    for edge, direction in guard.walk.steps:
        u, v = EDGES[edge]
        incidence[u] -= direction
        incidence[v] += direction
        total += direction * weights[edge]
    if any(incidence) or total == 0:
        return False
    expected = ((total,) if guard.constructor == "IntegralSourceSum"
                else (total % 2, total % 3))
    return claimed == expected and any(expected)


def universal_counterexample(genome):
    """Explicit algebraic falsifier of every incomplete exact-cycle AST."""
    for chord, gene in zip((3, 2), genome):
        if gene != 2:
            labels = [1, 0, 1, 1]
            labels[chord] += 1 if gene == 0 else lcm(2, 3)
            return tuple(labels)
    return None  # Sound only by the complete-cycle proof in X03 section 5.


grammar = sorted(product(range(3), repeat=2), key=lambda g: (sum(g), g))
examples = [(1, 0, 1, 1)]
trace = []
while True:
    genome = next(g for g in grammar if all(
        verify_semantics(w, compile_genome(g).run(w)) for w in examples))
    proposed = compile_genome(genome)
    counterexample = universal_counterexample(genome)
    if counterexample is None:
        trace.append({"genome": genome, "counterexample": None,
                      "acceptance": "complete integral fundamental-cycle AST"})
        break
    assert not verify_semantics(counterexample, proposed.run(counterexample))
    trace.append({"genome": genome, "counterexample": counterexample,
                  "returned": proposed.run(counterexample)[0]})
    examples.append(counterexample)  # All previous failures remain mandatory.


def assignment_oracle(weights, edge_bound):
    # Exhaustive grounded vertex values; any valid tree primitive is in this box.
    radius = 2 * edge_bound
    return any(all(values[v] - values[u] == w
                   for (u, v), w in zip(EDGES, weights))
               for p, q in product(range(-radius, radius + 1), repeat=2)
               for values in ((0, p, q),))


bounded_sources = 0
for weights in product(range(-2, 3), repeat=4):
    answer = proposed.run(weights)
    assert verify_semantics(weights, answer)
    assert (answer[0] == "GLUED") == assignment_oracle(weights, 2)
    bounded_sources += 1


def bounded_zero(weights, bound, modulus, source=SOURCE):
    # Bound belongs to the original declared class and exact epoch/topology.
    if source != SOURCE or any(abs(w) > bound for w in weights):
        raise ValueError("Unlicensed source bound or source/epoch change")
    if modulus <= 3 * bound:
        raise ValueError("No certified fundamental-cycle detection bound")
    return all(sum(s * (weights[e] % modulus) for e, s in loop.steps)
               % modulus == 0 for loop in LOOPS)


for weights in product(range(-2, 3), repeat=4):
    assert bounded_zero(weights, 2, 7) == (proposed.run(weights)[0] == "GLUED")
rejections = []
for args in (((1, 0, 1, 7), 2, 7, SOURCE),
             ((1, 0, 1, 1), 2, 7, (SOURCE[0], 1, EDGES))):
    try:
        bounded_zero(*args)
    except ValueError:
        rejections.append("edge bound" if args[-1] == SOURCE else "stale epoch")
    else:
        raise AssertionError("Invalid original source contract accepted")
try:
    ClosedWalk(((1, 1), (0, -1)))
except ValueError:
    rejections.append("noncomposable walk")
else:
    raise AssertionError("Ill-typed constructor accepted")


# Independent A06 bridge: 25 complete states, two declared reset actions.
states = tuple(product(range(-2, 3), repeat=2))
index = {state: i for i, state in enumerate(states)}
actions = (tuple(index[(0, y)] for x, y in states),
           tuple(index[(x, 0)] for x, y in states))
exact_report = tuple(x == y for x, y in states)
modular_report = tuple((x - y) % 5 == 0 for x, y in states)  # 5 > B=4
assert exact_report == modular_report


def kernel(report):
    return frozenset((i, j) for i in range(25) for j in range(25)
                     if report[i] == report[j])


relation = kernel(exact_report)
block_counts = []
while True:
    block_counts.append(len({frozenset(j for i2, j in relation if i2 == i)
                             for i in range(25)}))
    nxt = frozenset((i, j) for i, j in relation
                    if all((a[i], a[j]) in relation for a in actions))
    if nxt == relation:
        break
    relation = nxt
reachable_safe = set()
for pair in kernel(modular_report):
    todo, seen, safe = deque([pair]), {pair}, True
    while todo:
        i, j = todo.popleft()
        if exact_report[i] != exact_report[j]:
            safe = False
            break
        for a in actions:
            p = (a[i], a[j])
            if p not in seen:
                seen.add(p)
                todo.append(p)
    if safe:
        reachable_safe.add(pair)
assert relation == reachable_safe
assert len(block_counts) - 1 <= 25 - block_counts[0]
assert (-4) % 5 == 1 % 5 and -4 != 1  # zero detection is not value recovery.
assert len({p % 9 for p in range(-4, 5)}) == 9  # 9 > 2B.


# Re-execute all prior hostile/mutation controls; retain their exact old files.
inherited = {}
for name in ("A03", "A06"):
    command = [sys.executable, "-B", str(BASE / f"{name}_probe.py")]
    run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                         timeout=30)
    assert run.returncode == 0, run.stderr
    output = json.loads(run.stdout)
    inherited[name] = {"command": command, "exit_code": run.returncode,
                       "stdout_sha256": sha256(run.stdout.encode()).hexdigest(),
                       "probe_sha256": sha256((BASE / f"{name}_probe.py").read_bytes()).hexdigest()}
    if name == "A03":
        inherited[name]["hostile_witness"] = output["hostile_witness"]
        assert all(output["hostile_witness"][k] for k in
                   ("missing_dart_rejected", "stale_source_rejected",
                    "disconnected_chart_rejected"))
    else:
        inherited[name]["mutations_rejected"] = output["mutations_rejected"]
        inherited[name]["cross_source_counterexample"] = output["cross_source_counterexample"]
        inherited[name]["same_carrier_incompatible_minima"] = output["same_carrier_incompatible_minima"]
        assert output["all_assertions_passed"]

hash_paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
              "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
              "research/2026-10-13/SWARM_ATLAS/A03.md",
              "research/2026-10-13/SWARM_ATLAS/A06.md",
              "research/2026-10-13/SWARM_ATLAS/reviews/A03_REVIEW.md",
              "research/2026-10-13/SWARM_ATLAS/reviews/A05_A06_C18_E33_PRINCIPAL.md",
              "observational_succ/relational_model_genetics.py",
              "observational_succ/evolutionary_bridge_search.py",
              "observational_succ/genetic_obstruction_holonomy.py",
              "research/2026-10-13/SWARM_ATLAS/X03_probe.py"]
print(json.dumps({"schema": "SWM-X03-exact-v1", "parent_sha": PARENT,
                  "command": "python -B research/2026-10-13/SWARM_ATLAS/X03_probe.py",
                  "successful_completion_exit_code": 0, "all_assertions_passed": True,
                  "cegis": {"grammar_size": len(grammar), "trace": trace,
                            "retained_counterexamples": examples[1:],
                            "accepted_guard_constructors": [g.constructor for g in proposed.guards]},
                  "independent_grounded_assignment_sources": bounded_sources,
                  "source_bound": {"edge_bound": 2, "vertices": 3,
                                   "generator_bound": 6, "detecting_modulus": 7,
                                   "rejections": rejections},
                  "finite_repair": {"states": 25, "period_bound": 4,
                                    "zero_modulus": 5, "value_modulus": 9,
                                    "block_counts": block_counts,
                                    "independent_product_reachability_equal": True},
                  "inherited_live_regressions": inherited,
                  "sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest()
                             for p in hash_paths},
                  "python": sys.version.split()[0],
                  "boundary": "paper theorem plus exact finite AST checks; independent acceptance pending"},
                 indent=2, sort_keys=True))
