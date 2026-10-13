"""Bounded exact SWM-B11 controls; the written proof supplies the universal no-go."""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.checkpoint_meta_tower import FiniteController, enumerate_action_words
from observational_succ.godel_succ import delayed_halt, halted_by, two_counter_loop
from observational_succ.voyager_profinite_frontier import (
    TraceSource, finite_model_critical_probe_witnesses, powers_of_two_pulse,
)


def search(states, report, target, probe_at, checkpoints):
    """Finite prefix of the partial algorithm; exhaustion reports UNRESOLVED."""
    witnesses = {}
    if not states:
        return {"status": "REFUTED", "checkpoints": 0, "witnesses": []}
    for stage in range(checkpoints):
        context = probe_at(stage)
        proposed = target(context)
        for state in states:
            if state not in witnesses and report(state, context) != proposed:
                witnesses[state] = context
        if len(witnesses) == len(states):
            return {"status": "REFUTED", "checkpoints": stage + 1,
                    "witnesses": [[s, witnesses[s]] for s in states]}
    return {"status": "UNRESOLVED", "checkpoints": checkpoints,
            "witnesses": [[s, witnesses[s]] for s in states if s in witnesses]}


def verify(states, report, target, witnesses):
    """Replay each source mismatch, independent of the search bookkeeping."""
    supplied = dict(witnesses)
    return len(witnesses) == len(supplied) == len(states) and set(supplied) == set(states) and all(
        report(s, supplied[s]) != target(supplied[s]) for s in states)


def independent_halted_by(program, bound):
    """Direct bounded recurrence, compared against the imported monitor."""
    pc, a, b = 0, 0, 0
    for tick in range(bound + 1):
        op = program[pc]
        if op[0] == "HALT":
            return True
        if tick == bound:
            return False
        if op[0] == "INC":
            if op[1] == 0:
                a += 1
            else:
                b += 1
            pc = op[2]
        else:
            value = a if op[1] == 0 else b
            pc = op[2] if value else op[3]
            if value:
                if op[1] == 0:
                    a -= 1
                else:
                    b -= 1
    raise AssertionError("Bounded recurrence must return")


def main():
    zero = TraceSource("b11-zero", 0, "unary", ("s",), (0,), ("s",), "s")
    report = lambda s, n: zero.report(s)
    empty = search((), report, lambda n: 0, lambda n: n, 0)
    assert empty == {"status": "REFUTED", "checkpoints": 0, "witnesses": []}
    assert verify((), report, lambda n: 0, [])
    cases = []
    for delay in (0, 7, 37, 71):
        program = (("HALT",),) if delay == 0 else delayed_halt(delay)
        target = lambda n, p=program: int(halted_by(p, n))
        for n in range(73):
            assert target(n) == independent_halted_by(program, n)
        result = search(zero.states, report, target, lambda n: n, 73)
        assert result["status"] == "REFUTED"
        assert result["witnesses"] == [["s", delay]]
        assert verify(zero.states, report, target, result["witnesses"])
        if delay:
            prefix = search(zero.states, report, target, lambda n: n, delay)
            assert prefix["status"] == "UNRESOLVED"
            assert not verify(zero.states, report, target, [["s", delay - 1]])
        cases.append({"delay": delay, **result, "certificate_cardinality": 1})

    loop = two_counter_loop()
    for n in range(73):
        assert halted_by(loop, n) == independent_halted_by(loop, n) is False
    loop_result = search(zero.states, report, lambda n: int(halted_by(loop, n)),
                         lambda n: n, 73)
    assert loop_result["status"] == "UNRESOLVED"

    # A lawful reordered exhaustive enumeration can expose a late coordinate first.
    target37 = lambda n: int(halted_by(delayed_halt(37), n))
    swapped = lambda n: 37 if n == 0 else 0 if n == 37 else n
    reordered = search(zero.states, report, target37, swapped, 1)
    assert reordered["witnesses"] == [["s", 37]]

    states, bad = ("a", "b", "c"), {"a": 2, "b": 5, "c": 9}
    sparse = lambda s, n: int(n == bad[s])
    exact = search(states, sparse, lambda n: 0, lambda n: n, 10)
    assert verify(states, sparse, lambda n: 0, exact["witnesses"])
    assert len(exact["witnesses"]) == 3
    for omitted in range(3):
        subset = [w for i, w in enumerate(exact["witnesses"]) if i != omitted]
        assert not verify(states, sparse, lambda n: 0, subset)

    # A certificate against a supplied sample does not exhaust the actual source.
    incomplete = search((0,), lambda s, n: s, lambda n: 1, lambda n: n, 1)
    assert incomplete["status"] == "REFUTED"
    assert not verify((0, 1), lambda s, n: s, lambda n: 1, incomplete["witnesses"])

    # Both traces supplied as finite stationary tables: product bound is sharp.
    delay = 37
    target_states = tuple(f"t{i}" for i in range(delay + 1))
    finite_target = TraceSource("b11-finite-target", 0, "unary", target_states,
        (0,) * delay + (1,),
        target_states[1:] + (target_states[-1],), target_states[0])
    pair = (zero.initial, finite_target.initial)
    seen, tick = set(), 0
    while pair not in seen:
        if zero.report(pair[0]) != finite_target.report(pair[1]):
            break
        seen.add(pair)
        pair = (zero.step(pair[0]), finite_target.step(pair[1]))
        tick += 1
    assert tick == len(zero.states) * len(finite_target.states) - 1 == delay
    pulse = finite_model_critical_probe_witnesses(zero, powers_of_two_pulse)
    assert pulse["probe_times"] == (("s", 2),)  # constructive, not least mismatch
    controller = FiniteController(("A", "B"), (1, 0)).eventual_period()
    words = enumerate_action_words(("A", "B"), 3)
    assert len(words) == 15 and controller["cycle_length"] == 2

    paths = ("observational_succ/voyager_profinite_frontier.py",
             "observational_succ/checkpoint_meta_tower.py",
             "observational_succ/godel_succ.py",
             "provenance/IMPORT_MANIFEST.json",
             "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_GODEL_BRIDGE.md",
             "research/2026-10-13/SWARM_ATLAS/B11_probe.py")
    print(json.dumps({
        "claim_id": "SWM-B11", "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "command": "python research/2026-10-13/SWARM_ATLAS/B11_probe.py",
        "python": platform.python_version(), "status": "EXACT_BOUNDED_CONTROLS_PASS",
        "validation_history": [
            {"exit_code": 1, "failure": "AssertionError: pulse witness incorrectly expected 1",
             "repair": "existing constructive period refutation selects 2; no earliest claim"},
            {"exit_code": 0, "scope": "all bounded assertions in this probe"}],
        "delayed_halting": cases, "loop_prefix": loop_result,
        "empty_source_certificate": empty,
        "reordered_contexts": reordered, "sharp_cardinality_three": exact,
        "incomplete_source_certificate_rejected": True,
        "forged_early_witness_rejected": True,
        "finite_table_product": {"source_states": 1, "target_states": 38,
                                 "first_mismatch": tick, "bound_sharp": True},
        "specialized_pulse_witness": pulse["probe_times"],
        "finite_controller_cycle": controller["cycle_length"],
        "externally_enumerated_words_to_depth_three": len(words),
        "universal_undecidability_proved_by_execution": False,
        "source_tables_physically_authenticated": False,
        "sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
