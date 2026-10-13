#!/usr/bin/env python3
"""F42: exact typed quotient-expression heredity, not scalar-fit genetics.

All source laws, constructors, selection rules and target are supplied here.
This bounded research probe neither reads holdouts nor edits native modules.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.categorical_repair_synthesis import (
    FiniteMealy, minimal_behavioral_quotient,
)
from observational_succ.relational_model_genetics import (
    Capsule, Port, PairedSourceTable, invent_bijective_bridges,
)
from observational_succ.genetic_obstruction_holonomy import (
    ParityEdge, discover_holonomy, verify_cycle_witness,
    brute_force_has_global_section,
)

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def canonical(values):
    table = {}
    return tuple(table.setdefault(v, len(table)) for v in values)


@dataclass(frozen=True)
class Source:
    source_id: str
    epoch: int
    basis: str
    machine: FiniteMealy

    def __post_init__(self):
        if (not self.source_id or not self.basis or type(self.epoch) is not int
                or self.epoch < 0 or self.machine.count > 8
                or len(self.machine.actions) > 2):
            raise ValueError("Source contract or finite budget violated")

    @property
    def contract(self):
        content = [self.source_id, self.epoch, self.basis,
                   self.machine.actions, self.machine.output,
                   self.machine.next_state]
        digest = sha256(json.dumps(content, separators=(",", ":")).encode()).hexdigest()
        return self.source_id, self.epoch, self.basis, digest


@dataclass(frozen=True)
class Gene:
    kind: str
    contract: tuple
    parents: tuple[int, ...]
    action: str | None = None


def evaluate(source, gene, previous):
    """DAG interpretation: every result is a surjection onto its actual image."""
    if gene.contract != source.contract:
        raise ValueError("Mutation changed its source/epoch/basis/table")
    if any(type(i) is not int or not 0 <= i < len(previous) for i in gene.parents):
        raise ValueError("Ill-founded or unowned expression parent")
    if gene.kind == "read" and not gene.parents and gene.action is None:
        raw = tuple(zip(*source.machine.output))
    elif gene.kind == "pre" and len(gene.parents) == 1:
        if gene.action not in source.machine.actions:
            raise ValueError("Mutation invented an action")
        parent = previous[gene.parents[0]]
        a = source.machine.actions.index(gene.action)
        raw = tuple(parent[t] for t in source.machine.next_state[a])
    elif gene.kind == "meet" and len(gene.parents) == 2 and gene.action is None:
        raw = tuple(zip(*(previous[i] for i in gene.parents)))
    else:
        raise ValueError("Unknown typed constructor")
    classes = canonical(raw)
    if len(classes) != source.machine.count or set(classes) != set(range(max(classes)+1)):
        raise AssertionError("Not a total surjection onto the declared quotient")
    return classes


def factor(child, parent):
    """Actual projection Child -> Parent; reject a purported refinement."""
    table = {}
    for q, p in zip(child, parent):
        if q in table and table[q] != p:
            raise ValueError("Offspring forgot an inherited distinction")
        table[q] = p
    return tuple(table[i] for i in range(max(child)+1))


def defect(source, classes):
    """Pairwise semantic verifier independent of signature-based construction."""
    m = source.machine
    for x, y in combinations(range(m.count), 2):
        if classes[x] != classes[y]:
            continue
        for a, name in enumerate(m.actions):
            if m.output[a][x] != m.output[a][y]:
                return {"kind": "READOUT", "pair": [x, y], "action": name}
            if classes[m.next_state[a][x]] != classes[m.next_state[a][y]]:
                return {"kind": "ACTION", "pair": [x, y], "action": name}
    return None


def distinguish(source, x, y):
    """Complete paired-state BFS: None proves equal traces for every word."""
    m = source.machine
    todo = deque([(x, y, ())])
    seen = {(x, y)}
    while todo:
        i, j, prefix = todo.popleft()
        for a, name in enumerate(m.actions):
            word = prefix + (name,)
            if m.output[a][i] != m.output[a][j]:
                return word
            pair = (m.next_state[a][i], m.next_state[a][j])
            if pair not in seen:
                seen.add(pair)
                todo.append((*pair, word))
    return None


def verify_witness(source, witness):
    x, y = witness["pair"]
    word = tuple(witness["word"])
    if witness["contract"] != list(source.contract):
        raise ValueError("Counterexample changed source")
    if source.machine.observe(x, word) == source.machine.observe(y, word):
        raise ValueError("Forged counterexample")


def certify(source, classes):
    if defect(source, classes) is not None:
        raise ValueError("Induced action/readout remains an obligation")
    m = source.machine
    reps = tuple(classes.index(i) for i in range(max(classes)+1))
    outputs = tuple(tuple(row[s] for s in reps) for row in m.output)
    transitions = tuple(tuple(classes[row[s]] for s in reps) for row in m.next_state)
    for s in range(m.count):
        for a in range(len(m.actions)):
            assert outputs[a][classes[s]] == m.output[a][s]
            assert transitions[a][classes[s]] == classes[m.next_state[a][s]]
    return {"actions": m.actions, "outputs": outputs, "transitions": transitions}


def evolve(source):
    """Counterexample-directed precomposition mutation + meet crossover.

    No reward function. Each chosen defect forces a strict refinement; the
    finite bound is n - initial_block_count accepted refinements.
    """
    genes, values, history, inherited = [], [], [], []

    def append(gene):
        classes = evaluate(source, gene, values)
        for witness in inherited:
            verify_witness(source, witness)
        projections = {}
        pre_image_map = None
        if gene.kind == "meet":
            projections = {str(i): factor(classes, values[i]) for i in gene.parents}
        if gene.kind == "pre":
            p = values[gene.parents[0]]
            a = source.machine.actions.index(gene.action)
            raw = tuple(p[t] for t in source.machine.next_state[a])
            pre_image_map = factor(classes, raw)
            assert len(set(pre_image_map)) == len(pre_image_map)
            assert tuple(pre_image_map[q] for q in classes) == raw
        obligation = defect(source, classes)
        genes.append(gene)
        values.append(classes)
        # Native Capsule validates the actual graph and retains source metadata.
        domain = tuple(map(str, range(source.machine.count)))
        qdomain = tuple(map(str, range(max(classes)+1)))
        graph = Capsule(f"q{len(genes)-1}", "declared finite quotient", source.source_id,
                        source.epoch, source.basis,
                        (Port("source_state", domain), Port("quotient_state", qdomain)),
                        tuple((str(s), str(q)) for s, q in enumerate(classes)))
        assert len(graph.rows) == source.machine.count
        history.append({"gene": len(genes)-1, "constructor": gene.kind,
                        "parents": gene.parents, "action": gene.action,
                        "classes": classes, "surjective_graph": graph.rows,
                        "factor_maps": projections, "obligation": obligation,
                        "pre_image_inclusion": pre_image_map,
                        "inherited_counterexamples": list(inherited),
                        "action_licensed": obligation is None})
        return len(genes)-1

    current = append(Gene("read", source.contract, ()))
    limit = source.machine.count - (max(values[current])+1)
    refinements = 0
    while (bad := defect(source, values[current])) is not None:
        if bad["kind"] != "ACTION" or refinements >= limit:
            raise AssertionError("Refinement theorem or finite budget failed")
        word = distinguish(source, *bad["pair"])
        if word is None:
            raise AssertionError("Action defect lacked an actual trace witness")
        witness = {"pair": bad["pair"], "word": word,
                   "contract": list(source.contract)}
        verify_witness(source, witness)
        inherited.append(witness)
        pre = append(Gene("pre", source.contract, (current,), bad["action"]))
        child = append(Gene("meet", source.contract, (current, pre)))
        if max(values[child]) <= max(values[current]):
            raise AssertionError("Chosen witness did not force strict refinement")
        current = child
        refinements += 1
    for witness in inherited:
        verify_witness(source, witness)
        x, y = witness["pair"]
        assert values[current][x] != values[current][y]
    terminal = certify(source, values[current])
    # BFS is a separate semantic route; native minimizer is shared-prior-art comparison.
    for x, y in combinations(range(source.machine.count), 2):
        assert (values[current][x] == values[current][y]) == (distinguish(source, x, y) is None)
    native = minimal_behavioral_quotient(source.machine)
    assert values[current] == tuple(native.block_of(s) for s in range(source.machine.count))
    return {"history": history, "accepted_refinements": refinements,
            "maximum_refinements": limit, "terminal_gene": current,
            "terminal_classes": values[current], "terminal_machine": terminal,
            "preserved_counterexamples": inherited, "pair_BFS_agrees": True,
            "native_minimizer_agrees": True}


def rejected(call):
    try:
        call()
    except ValueError as exc:
        return str(exc)
    raise AssertionError("Negative control escaped rejection")


def main():
    source = Source("F42-declared-duplicated-four-cycle", 0, "finite-Mealy-v1",
                    FiniteMealy(("step",), ((0, 0, 0, 1, 0, 0, 0, 1),),
                                ((1, 2, 3, 0, 5, 6, 7, 4),)))
    states = tuple(map(str, range(8)))
    table = PairedSourceTable(source.source_id, source.epoch, source.basis,
                             Port("state", states), Port("readout", ("0", "1")),
                             tuple((f"s{s}", str(s), str(source.machine.output[0][s]))
                                   for s in range(8)), True)
    assert invent_bijective_bridges(table) == ()
    result = evolve(source)
    q0 = tuple(result["history"][0]["classes"])
    qfinal = tuple(result["terminal_classes"])
    controls = {
        "unlicensed_initial_action": rejected(lambda: certify(source, q0)),
        "coarsening_forgets_inheritance": rejected(lambda: factor(q0, qfinal)),
        "unowned_action": rejected(lambda: evaluate(
            source, Gene("pre", source.contract, (0,), "invented"), [q0])),
        "changed_source": rejected(lambda: evaluate(
            source, Gene("read", ("other",) + source.contract[1:], ()), [])),
        "unsupplied_constructor": rejected(lambda: evaluate(
            source, Gene("completion", source.contract, (0,)), [q0])),
        "forged_witness": rejected(lambda: verify_witness(source, {
            "pair": [0, 4], "word": ["step"], "contract": list(source.contract)})),
    }
    # Preserve the native no-global-section corpse: quotient repair does not erase it.
    edges = (ParityEdge("A", "x", "y", 1), ParityEdge("B", "y", "z", 1),
             ParityEdge("C", "x", "z", 1))
    hol = discover_holonomy(edges)
    assert hol.obstruction is not None and verify_cycle_witness(edges, hol.obstruction)
    assert not brute_force_has_global_section(edges)
    # Fresh, unsealed hostile laws: constant readout and fully distinguishing readout.
    fresh = []
    for name, output in (("constant", (0,)*8), ("injective", tuple(range(8)))):
        control_source = Source("F42-"+name, 0, "finite-Mealy-v1",
                                FiniteMealy(("step",), (output,), source.machine.next_state))
        r = evolve(control_source)
        expected = 1 if name == "constant" else 8
        assert len(set(r["terminal_classes"])) == expected
        fresh.append({"name": name, "blocks": expected,
                      "refinements": r["accepted_refinements"], "pair_BFS_agrees": True})
    manifest = json.loads((ROOT / "provenance/IMPORT_MANIFEST.json").read_text())
    receipt = {
        "field": "F42", "source_parent_commit": BASE,
        "declared_source_contract": source.contract,
        "declared_source_table": {"actions": source.machine.actions,
                                  "outputs": source.machine.output,
                                  "transitions": source.machine.next_state},
        "declared_source_is_empirically_authenticated": False,
        "grammar_supplied_by_programmer": ["read", "pre(action, quotient)", "meet(q,r)"],
        "target_supplied_by_programmer": "greatest action-stable subrelation of readout kernel",
        "mutation_selection_supplied_by_programmer": "first exact action defect, then pre/meet",
        "native_bijection_candidate_count": 0, "cardinality_obstruction": [8, 2],
        "result": result, "negative_controls": controls, "fresh_unsealed_controls": fresh,
        "inherited_parity_corpse": {"global_section": False,
            "cycle_edges": hol.obstruction.edge_names,
            "cycle_nodes": hol.obstruction.cycle_nodes, "holonomy": 1},
        "import_manifest_source_commit": manifest["source_commit"],
        "native_dependencies_are_in_import_manifest": any(
            e["destination_path"] in {
                "observational_succ/relational_model_genetics.py",
                "observational_succ/categorical_repair_synthesis.py",
                "observational_succ/genetic_obstruction_holonomy.py"}
            for e in manifest["entries"]),
        "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": "python research/2026-10-13/SWARM_ATLAS/F42_probe.py",
        "exit_status": 0, "sealed_holdout_consumed": False,
        "academic_originality_claimed": False, "physical_meaning_established": False,
        "status": "TESTED MODEL; theorem proof is separately stated in F42.md",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
