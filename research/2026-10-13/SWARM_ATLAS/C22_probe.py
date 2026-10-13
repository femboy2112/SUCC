"""Bounded exact C22 controls; declared simulators, never hardware receipts."""
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def native(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "observational_succ" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


n = native("noncommuting_proof_transport")
c = native("causal_nerode_succ")


def square(field, a="A", b="B"):
    one, two = field.action(a), field.action(b)
    for s in range(field.count):
        if one.enabled[s] and two.enabled[s] != two.enabled[one.transitions[s]]:
            return ["enabledness", s, a]
        if two.enabled[s] and one.enabled[s] != one.enabled[two.transitions[s]]:
            return ["enabledness", s, b]
        if one.enabled[s] and two.enabled[s]:
            ab, ba = field.run(s, (a, b)), field.run(s, (b, a))
            if ab.terminal_state != ba.terminal_state:
                return ["endpoint", s]
            if ab.observed_values != ba.observed_values[::-1]:
                return ["labelled-outcome", s, list(ab.observed_values), list(ba.observed_values)]
    return None


def matrix(size, entry):
    return tuple(tuple(Q(entry(s, t)) for t in range(size)) for s in range(size))


def mul(a, b):
    return tuple(tuple(sum((a[s][k] * b[k][t] for k in range(len(b))), Q(0))
                       for t in range(len(b[0]))) for s in range(len(a)))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(r, u)) for r, u in zip(a, b))


def tensor(a, b):
    return tuple(tuple(x * y for x in ra for y in rb) for ra in a for rb in b)


def main():
    yes = (True,) * 4
    bit_a, bit_b = tuple(s // 2 for s in range(4)), tuple(s % 2 for s in range(4))
    field = n.FiniteCarrier(4, (
        n.Instrument("A", bit_a, tuple(s ^ 2 for s in range(4)), yes),
        n.Instrument("B", bit_b, tuple(s ^ 1 for s in range(4)), yes)),
        "C22-declared-pair", "binary-pair-v1")
    assert square(field) is None
    schedules = (("a1", "a2", "b1"), ("a1", "b1", "a2"), ("b1", "a1", "a2"))
    labels = {"a1": "A", "a2": "A", "b1": "B"}
    for s in range(4):
        aligned = []
        for order in schedules:
            run = field.run(s, tuple(labels[e] for e in order))
            aligned.append((tuple(sorted(zip(order, run.observed_values))), run.terminal_state))
        assert len(set(aligned)) == 1
    parity = ("0", "1", "1", "0")
    for word in (("A", "B"), ("B", "A")):
        assert n.factor_original_claim(field, (0, 1, 2, 3), parity, word,
                                       target_id="original-XOR").valid
        assert n.check_source_semantics(field, (0, 1, 2, 3), parity, parity, word).source_semantics_preserved

    destructive = n.FiniteCarrier(4, (
        n.Instrument("A", bit_a, tuple(2 * (s // 2) for s in range(4)), yes),
        n.Instrument("B", bit_b, bit_b, yes)), "C22-destructive-pair", "binary-pair-v1")
    assert all(destructive.run(s, ("A", "B")).terminal_state ==
               destructive.run(s, ("B", "A")).terminal_state for s in range(4))
    damage = square(destructive)
    assert damage == ["labelled-outcome", 1, [0, 0], [1, 0]]
    lost = n.factor_original_claim(destructive, (0, 1, 2, 3), parity,
                                   ("A", "B"), target_id="original-XOR")
    assert not lost.valid and lost.collision == (0, 1)
    order_failure = square(n.reversible_noncommuting_bit_field())
    assert order_failure == ["endpoint", 1]
    masked = n.FiniteCarrier(2, (
        n.Instrument("A", (0, 0), (1, 0), (True, True)),
        n.Instrument("B", (0, 0), (0, 1), (True, False))), "C22-menu", "bit")
    mask_failure = square(masked)
    assert mask_failure == ["enabledness", 0, "A"]

    # Summed transition kernels commute; report-conditioned kernels do not.
    p = tuple(matrix(2, lambda s, t, u=u: int(s == t == u)) for u in (0, 1))
    flip = matrix(2, lambda s, t: int(t == 1 - s))
    assert mul(add(*p), flip) == mul(flip, add(*p))
    assert mul(p[0], flip) != mul(flip, p[0])
    # Local random reset instruments, reporting the local pre-state bit.
    ka = tuple(matrix(4, lambda s, t, u=u: Q(1, 2) if s // 2 == u and s % 2 == t % 2 else 0) for u in (0, 1))
    kb = tuple(matrix(4, lambda s, t, u=u: Q(1, 2) if s % 2 == u and s // 2 == t // 2 else 0) for u in (0, 1))
    assert all(sum(add(*k)[s]) == 1 for k in (ka, kb) for s in range(4))
    assert all(mul(a, b) == mul(b, a) for a in ka for b in kb)
    # Separate nondestructive bit probes with correlated initial source law.
    da = tuple(matrix(4, lambda s, t, u=u: int(s == t and s // 2 == u)) for u in (0, 1))
    db = tuple(matrix(4, lambda s, t, u=u: int(s == t and s % 2 == u)) for u in (0, 1))
    prior = (Q(1, 2), Q(0), Q(0), Q(1, 2))
    joint = {str((u, v)): sum(prior[s] * sum(mul(da[u], db[v])[s]) for s in range(4))
             for u in (0, 1) for v in (0, 1)}
    assert joint == {"(0, 0)": Q(1, 2), "(0, 1)": Q(0), "(1, 0)": Q(0), "(1, 1)": Q(1, 2)}
    assert all(mul(a, b) == mul(b, a) for a in da for b in db)
    assert joint["(0, 0)"] != Q(1, 2) * Q(1, 2)

    identity = matrix(2, lambda s, t: int(s == t))
    assert mul(tensor(flip, identity), tensor(identity, flip)) == tensor(flip, flip)
    assert mul(tensor(flip, identity), tensor(identity, flip)) == mul(tensor(identity, flip), tensor(flip, identity))
    assert mul(tensor(p[0], flip), tensor(flip, p[1])) == tensor(mul(p[0], flip), mul(flip, p[1]))
    charts = [c.SourceChart("C22-factor", e, "bit", ("0", "1"), ("0", "1")) for e in range(3)]
    first = c.CausalInstrument("flip", charts[0], charts[1], ("1", "0"))
    second = c.CausalInstrument("flip", charts[1], charts[2], ("1", "0"))
    assert c.causal_descent(first).descended
    assert c.causal_descent(c.compose_instruments(first, second)).descended
    actual = field.run(2, ("A", "A", "B"))
    return {
        "schema": "C22-exact-v1", "status": "TESTED MODEL", "source_parent": BASE,
        "python": platform.python_version(), "command": "PYTHONDONTWRITEBYTECODE=1 python research/2026-10-13/SWARM_ATLAS/C22_probe.py",
        "native_sha256": {name: hashlib.sha256((ROOT / "observational_succ" / (name + ".py")).read_bytes()).hexdigest()
                          for name in ("causal_nerode_succ", "noncommuting_proof_transport")},
        "controls": {"deterministic_square_all_four_sources": True, "three_linear_extensions_all_four_sources": True,
                     "original_target_factor_and_semantic_square_AB_BA": True,
                     "destructive_equal_endpoints_rejected": damage, "lost_original_XOR_pair": list(lost.collision),
                     "reversible_order_rejected": order_failure, "menu_rejected": mask_failure,
                     "unconditioned_commutation_insufficient": True, "rational_report_kernel_square": True,
                     "correlated_joint": {key: str(value) for key, value in joint.items()},
                     "tensor_interchange_and_native_vertical_descent": True},
        "selected_simulator_run": {"source_id": field.source_id, "basis_id": field.basis_id,
                                   "law_version": "C22-local-flips-v1",
                                   "native_public_signature": actual.public_signature,
                                   "event_ids_in_record_order": schedules[0], "required_poset_edges": [["a1", "a2"]],
                                   "declared_process_assignment": {"a1": "P", "a2": "P", "b1": "Q"},
                                   "poset_is_stipulated_fixture_not_inferred_from_native_epochs": True},
        "alternative_schedules_are_counterfactual_model_evaluations": True,
        "physical_source_authenticated": False, "simultaneous_measurement_claimed": False,
        "academic_novelty_claimed": False, "full_suite_run": False,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
