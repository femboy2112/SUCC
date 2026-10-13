"""Fresh audit G oracles; never call target validation/oracle helpers.

Default module roots are the integrated repository.  Isolated target roots can
be supplied while the campaign is still integrating frozen cluster commits.
All arithmetic is exact.  Source tables and oracle access are declared models.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path
from random import Random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import observational_succ
from observational_succ.eodcs_multi_action_source import ActionSource
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument


def load_target(root, name):
    path = Path(root) / "observational_succ" / (name + ".py")
    spec = importlib.util.spec_from_file_location("observational_succ." + name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, sha256(path.read_bytes()).hexdigest()


def exact_json(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): exact_json(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [exact_json(v) for v in value]
    if isinstance(value, (frozenset, set)):
        return [exact_json(v) for v in sorted(value, key=repr)]
    return value


def rational_matrix(rows, cols, rng):
    return tuple(tuple(Q(rng.randrange(-3, 4), rng.randrange(1, 6))
                       for _ in range(cols)) for _ in range(rows))


def full_block_trajectory(A, B, C, D, E, H, x0, z0, inputs):
    """One unpartitioned source matrix; no kernels or target arithmetic."""
    r, h = len(A), len(D)
    source = tuple(tuple(A[i]) + tuple(B[i]) for i in range(r)) + tuple(
        tuple(C[i]) + tuple(D[i]) for i in range(h))
    drive = tuple(tuple(row) for row in E) + tuple(tuple(row) for row in H)
    state = tuple(map(Q, x0)) + tuple(map(Q, z0))
    trajectory = [state]
    for u in inputs:
        state = tuple(sum((source[i][j] * state[j] for j in range(r+h)), Q(0))
                      + sum((drive[i][j] * u[j] for j in range(len(u))), Q(0))
                      for i in range(r+h))
        trajectory.append(state)
    return tuple(row[:r] for row in trajectory), tuple(row[r:] for row in trajectory)


def memoryless_reference(A, E, x0, inputs):
    x, states = tuple(map(Q, x0)), [tuple(map(Q, x0))]
    for u in inputs:
        x = tuple(sum((A[i][j] * x[j] for j in range(len(x))), Q(0))
                  + sum((E[i][j] * u[j] for j in range(len(u))), Q(0))
                  for i in range(len(x)))
        states.append(x)
    return tuple(states)


def audit_linear(F):
    rng = Random(79032026)
    records = []
    for case in range(72):
        r, h, m = 1 + case % 3, 1 + (case // 3) % 6, 1 + (case // 18) % 2
        A, B, C = rational_matrix(r, r, rng), rational_matrix(r, h, rng), rational_matrix(h, r, rng)
        E, H = rational_matrix(r, m, rng), rational_matrix(h, m, rng)
        kind = ("nonnormal-upper", "singular-upper", "nilpotent-shift", "decoupled-initial")[case % 4]
        raw = rational_matrix(h, h, rng)
        if kind == "nonnormal-upper":
            D = tuple(tuple(raw[i][j] if j >= i else Q(0) for j in range(h)) for i in range(h))
        elif kind == "singular-upper":
            D = tuple(tuple(Q(0) if j < i or (i == j == h-1) else raw[i][j]
                            for j in range(h)) for i in range(h))
        elif kind == "nilpotent-shift":
            D = tuple(tuple(Q(i + 1 == j) for j in range(h)) for i in range(h))
        else:
            D = raw
            C = tuple(tuple(Q(0) for _ in range(r)) for _ in range(h))
            H = tuple(tuple(Q(0) for _ in range(m)) for _ in range(h))
        if case % 9 == 0:
            B = tuple(tuple(Q(0) for _ in range(h)) for _ in range(r))
        x0 = tuple(Q(rng.randrange(-3, 4), 7) for _ in range(r))
        z0 = tuple(Q(rng.randrange(-3, 4), 11) for _ in range(h))
        if not any(z0):
            z0 = (Q(1),) + z0[1:]
        inputs = tuple(tuple(Q(rng.randrange(-3, 4), 13) for _ in range(m))
                       for _ in range(h+5))
        system = F.BlockSystem(A, B, C, D, E, H)
        xs, zs = full_block_trajectory(A, B, C, D, E, H, x0, z0, inputs)
        mismatches = [n for n in range(len(inputs))
                      if system.memory_successor(xs[:n+1], inputs[:n+1], z0) != xs[n+1]]
        if mismatches:
            raise AssertionError(("hidden-memory mismatch", case, mismatches))
        # Independently test the finite closure certificate by driving the full
        # source, not by recalculating its BD^kC/H kernel coefficients.
        zero_inputs = tuple(tuple(Q(0) for _ in range(m)) for _ in range(h+2))
        zero_z = tuple(Q(0) for _ in range(h))
        zero_x = tuple(Q(0) for _ in range(r))
        zero_initial_closed = True
        for i in range(r):
            initial = tuple(Q(i == j) for j in range(r))
            resolved, _ = full_block_trajectory(A, B, C, D, E, H, initial, zero_z, zero_inputs)
            zero_initial_closed &= resolved == memoryless_reference(A, E, initial, zero_inputs)
        for j in range(m):
            drive = (tuple(Q(i == j) for i in range(m)),) + zero_inputs[1:]
            resolved, _ = full_block_trajectory(A, B, C, D, E, H, zero_x, zero_z, drive)
            zero_initial_closed &= resolved == memoryless_reference(A, E, zero_x, drive)
        all_initial_closed = True
        for j in range(h):
            hidden = tuple(Q(i == j) for i in range(h))
            resolved, _ = full_block_trajectory(A, B, C, D, E, H, zero_x, hidden, zero_inputs)
            all_initial_closed &= resolved == memoryless_reference(A, E, zero_x, zero_inputs)
        cert = system.closure_certificate()
        if (cert["zero_hidden_initial_closure"] != zero_initial_closed
                or cert["all_hidden_initial_closure"] != all_initial_closed):
            raise AssertionError(("closure certificate disagrees with full trajectories", case))
        records.append({"case": case, "kind": kind, "shape": [r, h, m],
                        "blocks": {"A": A, "B": B, "C": C, "D": D, "E": E, "H": H},
                        "x0": x0, "z0": z0, "inputs": inputs,
                        "resolved_full_source_trajectory": xs,
                        "hidden_full_source_trajectory": zs,
                        "memory_mismatches": mismatches,
                        "zero_initial_closure": zero_initial_closed,
                        "all_initial_closure": all_initial_closed})
    # Null kernel with a nonzero hidden-initial forcing is a decisive mutant.
    A, B, C, D, E, H = ((Q(0),),), ((Q(1), Q(0)),), ((Q(0),), (Q(0),)), \
        ((Q(0), Q(1)), (Q(0), Q(0))), ((Q(0),),), ((Q(0),), (Q(0),))
    initial_system = F.BlockSystem(A, B, C, D, E, H)
    hidden = (Q(0), Q(1))
    inputs = ((Q(0),),) * 4
    resolved, _ = full_block_trajectory(A, B, C, D, E, H, (Q(0),), hidden, inputs)
    if resolved != ((Q(0),), (Q(0),), (Q(1),), (Q(0),), (Q(0),)):
        raise AssertionError("nilpotent hidden-initial positive control failed")
    return {"cases": records,
            "nonzero_hidden_initial_zero_convolution_control": {
                "resolved_trajectory": resolved,
                "closure_certificate": initial_system.closure_certificate(),
                "omitting_initial_term_is_false": any(row[0] for row in resolved)}}


def tensor_fourier_low_modes(velocity, cutoff_squared=1):
    """Direct tensor-product convolution followed by div and Leray.

    Stores coefficient divided by i, so every value remains rational.
    This uses div(u tensor u), not the target's trigonometric advection formula.
    """
    tensor = {}
    for p, v in velocity.items():
        for q, w in velocity.items():
            k = tuple(p[j] + q[j] for j in range(2))
            if sum(x*x for x in k) > cutoff_squared:
                continue
            cell = tensor.setdefault(k, [[Q(0), Q(0)], [Q(0), Q(0)]])
            for i in range(2):
                for j in range(2):
                    cell[i][j] += v[i] * w[j]
    out = {}
    for k, cell in tensor.items():
        norm = sum(x*x for x in k)
        if norm == 0:
            continue
        div = tuple(sum((Q(k[j]) * cell[i][j] for j in range(2)), Q(0)) for i in range(2))
        component = sum((Q(k[i]) * div[i] for i in range(2)), Q(0)) / norm
        out[k] = tuple(div[i] - component * k[i] for i in range(2))
    return out


def cosine_modes(k, a, ell, b):
    return {k: tuple(Q(x)/2 for x in a), tuple(-x for x in k): tuple(Q(x)/2 for x in a),
            ell: tuple(Q(x)/2 for x in b), tuple(-x for x in ell): tuple(Q(x)/2 for x in b)}


def audit_fluid(F):
    integers = (5, 17, 97, 257, 4099, 65537, 1000003, 1000000007)
    records = []
    for n in integers:
        velocity = cosine_modes((n, 0), (0, 1), (n, 1), (1, -n))
        if any(sum(Q(k[j]) * v[j] for j in range(2)) for k, v in velocity.items()):
            raise AssertionError("audit velocity is not incompressible")
        convolution = tensor_fourier_low_modes(velocity)
        sine = tuple(-2*x for x in convolution[(0, 1)])
        target = F.fluid_high_high_witness(n)
        if sine != target["leray_advection_sine"] or sine != (Q(-1, 2), Q(0)):
            raise AssertionError(("fluid pressure-projected triad failure", n, sine))
        normalized = cosine_modes((n, 0), (0, 1), (n, 1), (Q(1, n), -1))
        normalized_low = tensor_fourier_low_modes(normalized)
        normalized_sine = tuple(-2*x for x in normalized_low[(0, 1)])
        if normalized_sine != (Q(-1, 2*n), Q(0)):
            raise AssertionError("bounded amplitude normalization law failed")
        records.append({"n": n, "source_modes": velocity, "low_tensor_divergence_over_i": convolution,
                        "leray_advection_sine": sine,
                        "normalized_leray_advection_sine": normalized_sine,
                        "unnormalized_mean_energy": Q(n*n+2, 2),
                        "normalized_mean_energy": Q(1) + Q(1, 2*n*n)})
    # Fresh rotated/source-scaled families, with no target helper for their
    # expected coefficient, test pressure removal and tensor orientation.
    exotic = []
    for n, slope, scale in ((29, 3, Q(2, 7)), (113, -5, Q(-3, 11)), (997, 41, Q(1, 13))):
        k, ell = (n, -slope), (n, 1-slope)
        a, b = (Q(slope, n), Q(1)), (scale * Q(1-slope, n), -scale)
        modes = cosine_modes(k, a, ell, b)
        if any(sum(Q(mode[j]) * value[j] for j in range(2))
               for mode, value in modes.items()):
            raise AssertionError("fresh sloped velocity is not incompressible")
        result = tensor_fourier_low_modes(modes)
        sine = tuple(-2*x for x in result[(0, 1)])
        if sine == (Q(0), Q(0)) or sine[1] != 0:
            raise AssertionError("fresh pressure-projected triad unexpectedly vanished")
        exotic.append({"k": k, "ell": ell, "a": a, "b": b, "projected_sine": sine})
    if tensor_fourier_low_modes({}) != {}:
        raise AssertionError("zero field acquired nonlinear residual")
    return {"target_family_fresh_integer_cases": records,
            "additional_incompressible_scaled_source_families": exotic,
            "uniform_bounded_energy_nonzero_limit_claimed": False}


def pair_separators(outputs_left, transitions_left, outputs_right, transitions_right):
    """Backward separation over the full product, no reachable-product BFS.

    A marked pair has a literal finite word witness.  Exhausting the least
    fixed point proves unmarked pairs agree under every finite word.
    """
    pairs = tuple(product(range(len(outputs_left)), range(len(outputs_right))))
    marked = {(s, t): () for s, t in pairs if outputs_left[s] != outputs_right[t]}
    while True:
        additions = {}
        for s, t in pairs:
            if (s, t) in marked:
                continue
            for a, (left, right) in enumerate(zip(transitions_left, transitions_right)):
                successor = (left[s], right[t])
                if successor in marked:
                    additions[s, t] = (a,) + marked[successor]
                    break
        if not additions:
            return marked
        marked.update(additions)


def reachable_states(transitions, initial=0):
    states = {initial}
    while True:
        new = states | {row[s] for row in transitions for s in states}
        if new == states:
            return states
        states = new


def independent_class_count(outputs, transitions, reachable=None):
    marked = pair_separators(outputs, transitions, outputs, transitions)
    representatives = []
    for s in sorted(range(len(outputs)) if reachable is None else reachable):
        if all((s, t) in marked for t in representatives):
            representatives.append(s)
    return len(representatives)


def audit_learning(D):
    rng = Random(79192026)
    records = []
    for case in range(96):
        n, action_count = 1 + case % 10, 1 + (case // 10) % 3
        actions = tuple("a" + str(i) for i in range(action_count))
        outputs = tuple("o" + str(rng.randrange(3)) for _ in range(n))
        transitions = tuple(tuple(rng.randrange(n) for _ in range(n)) for _ in actions)
        if case % 4 == 0 and n > 1:
            # Deliberately inaccessible interior states: prepared-root learning
            # must match reachable residuals, not count every declared interior.
            transitions = tuple(tuple(0 if s == 0 else row[s] for s in range(n)) for row in transitions)
        if case % 5 == 0:
            partial = tuple(tuple(None if rng.randrange(3) == 0 else row[s] for s in range(n))
                            for row in transitions)
            source = D.partial_source(outputs, actions, partial, source_id="audit-partial-%d" % case)
            n = len(source.states)
            outputs = source.outputs
            index = {state: i for i, state in enumerate(source.states)}
            transitions = tuple(tuple(index[state] for state in row) for row in source.transitions)
            kind = "observable-partial-action-totalization"
        else:
            states = tuple(str(i) for i in range(n))
            source = ActionSource("audit-learning-%d" % case, 0, "audit-independent-source",
                                  states, outputs, actions,
                                  tuple(tuple(states[s] for s in row) for row in transitions))
            kind = "possibly-unreachable-random-total-source"
        queried = []
        teacher_calls = []
        def membership(word):
            state = 0
            for a in word:
                state = transitions[actions.index(a)][state]
            queried.append(word)
            return outputs[state]
        def teacher(model):
            separators = pair_separators(outputs, transitions, model.outputs, model.transitions)
            witness = separators.get((0, model.initial))
            teacher_calls.append({"candidate_states": len(model.outputs),
                                  "product_pairs_marked": len(separators), "witness": witness})
            return None if witness is None else tuple(actions[a] for a in witness)
        model, receipt = D.learn_history_memory(actions, membership, teacher, max_rounds=100)
        if model is None:
            raise AssertionError(("fresh learner exhausted budget", case))
        full_separator = pair_separators(outputs, transitions, model.outputs, model.transitions)
        reachable = reachable_states(transitions)
        minimal = independent_class_count(outputs, transitions, reachable)
        if (0, model.initial) in full_separator or len(model.outputs) != minimal:
            raise AssertionError(("fresh learner all-word or minimum reachable mismatch", case))
        birth = D.construct_memory(source)
        full_minimum = independent_class_count(outputs, transitions)
        if len(birth.classes) != full_minimum:
            raise AssertionError(("source-table memory constructor nonminimal", case))
        records.append({"case": case, "kind": kind, "state_count": n,
                        "actions": actions, "source_outputs": outputs,
                        "source_transition_indices": transitions,
                        "reachable_states": sorted(reachable),
                        "minimal_reachable_classes": minimal,
                        "learned_classes": len(model.outputs), "complete_source_classes": full_minimum,
                        "teacher_calls": teacher_calls,
                        "membership_queries": len(queried),
                        "target_receipt_status": receipt["status"],
                        "all_word_equivalence_verified_by_product_fixed_point": True})
    # A bounded-testing teacher violates the exact teacher contract.  Keep the
    # accepted-but-false hypothesis as an access-gate control, not a refutation
    # of the correctly conditioned learning theorem.
    delay, cutoff = 19, 7
    outputs = ("0",) * delay + ("1",)
    transitions = (tuple(min(s+1, delay) for s in range(delay+1)),)
    def delayed_membership(word):
        return "1" if len(word) >= delay else "0"
    def truncated_teacher(model):
        return next((("a",) * n for n in range(cutoff+1)
                     if model.run(("a",) * n) != delayed_membership(("a",) * n)), None)
    false_model, false_receipt = D.learn_history_memory(("a",), delayed_membership, truncated_teacher)
    if false_model.run(("a",) * delay) == "1":
        raise AssertionError("truncated teacher failed to calibrate a false all-word certificate")
    return {"cases": records,
            "false_equivalence_teacher_control": {"teacher_cutoff": cutoff, "source_delay": delay,
                "returned_status": false_receipt["status"], "claimed_model_states": len(false_model.outputs),
                "exact_counterexample": ["a"] * delay,
                "correct_source_output": "1", "accepted_model_output": "0",
                "exact_teacher_assumption_violated": True},
            "unavailable_single_carrier_reset_control": {
                "source_outputs": ["0", "1", "2"],
                "sole_action_transition_indices": [[1, 2, 2]],
                "prepared_root": 0,
                "post_probe_state": 1,
                "all_states_reachable_after_first_probe": sorted(reachable_states(((1, 2, 2),), 1)),
                "reset_to_prepared_root_by_allowed_action_word_exists":
                    0 in reachable_states(((1, 2, 2),), 1),
                "membership_empty_from_prepared_root": "0",
                "membership_empty_from_current_carrier": "1",
                "independent_repreparation_or_source_law_required": True}}


def strategy_trees(outcome_sets, horizon):
    """Enumerate syntactic public trees, with no source-specific pruning."""
    levels = [(None,)]
    for depth in range(1, horizon+1):
        previous = levels[-1]
        trees = [None]
        for a, outcomes in enumerate(outcome_sets):
            for children in product(previous, repeat=len(outcomes)):
                trees.append((a, tuple(zip(outcomes, children))))
        levels.append(tuple(trees))
    return levels[-1]


def full_strategy_cost(outputs, transitions, enabled, targets, costs, horizon):
    """Full original-source trajectory simulation for EVERY public tree."""
    outcome_sets = tuple(tuple(sorted(set(row))) for row in outputs)
    best, tested, valid = None, 0, 0
    for tree in strategy_trees(outcome_sets, horizon):
        tested += 1
        leaves, spends = {}, []
        legal = True
        for original in range(len(targets)):
            current, path, spent, node = original, (), Q(0), tree
            while node is not None:
                a, children = node
                if not enabled[a][current]:
                    legal = False
                    break
                result = outputs[a][current]
                current = transitions[a][current]
                path += ((a, result),)
                spent += costs[a]
                node = dict(children)[result]
            if not legal:
                break
            if path in leaves and leaves[path] != targets[original]:
                legal = False
                break
            leaves[path] = targets[original]
            spends.append(spent)
        if legal:
            valid += 1
            worst = max(spends)
            best = worst if best is None else min(best, worst)
    return best, tested, valid


def audit_costs(D):
    rng = Random(79222026)
    records = []
    for case in range(120):
        n, action_count = 1 + case % 6, 1 + (case // 6) % 3
        outputs = tuple(tuple(rng.randrange(2) for _ in range(n)) for _ in range(action_count))
        transitions = tuple(tuple(rng.randrange(n) for _ in range(n)) for _ in range(action_count))
        enabled = tuple(tuple(bool(rng.randrange(4)) for _ in range(n)) for _ in range(action_count))
        targets = tuple(str(rng.randrange(3)) for _ in range(n))
        costs = tuple(Q(rng.randrange(1, 10), rng.randrange(1, 6)) for _ in range(action_count))
        actions = tuple(Instrument("probe%d" % a, outputs[a], transitions[a], enabled[a])
                        for a in range(action_count))
        field = FiniteCarrier(n, actions, "audit-strategy-%d" % case, "original-source-target")
        byname = {a.name: cost for a, cost in zip(actions, costs)}
        for horizon in range(3):
            oracle, count, valid = full_strategy_cost(outputs, transitions, enabled, targets, costs, horizon)
            actual = D.optimal_cost(field, targets, byname, horizon)
            if actual["worst_case_cost"] != oracle:
                raise AssertionError(("fresh destructive policy cost mismatch", case, horizon, oracle, actual))
            records.append({"case": case, "horizon": horizon, "state_count": n,
                            "source_action_outputs": outputs, "source_transition_indices": transitions,
                            "enabled_menus": enabled, "original_targets": targets, "costs": costs,
                            "independent_optimum": oracle, "target_optimum": actual["worst_case_cost"],
                            "full_public_trees_evaluated": count, "valid_source_complete_trees": valid})
    # Missing original states changes feasibility; no table sample certifies
    # its own completeness.  This is a calibrated source-class gate.
    complete = FiniteCarrier(3, (Instrument("read", (0, 0, 1), (0, 1, 2), (True,)*3),),
                             "complete", "same-original-target")
    incomplete = FiniteCarrier(2, (Instrument("read", (0, 1), (0, 1), (True,)*2),),
                               "omitted-source", "same-original-target")
    whole = D.optimal_cost(complete, ("0", "1", "1"), {"read": Q(1)}, 2)
    sample = D.optimal_cost(incomplete, ("0", "1"), {"read": Q(1)}, 2)
    if whole["worst_case_cost"] is not None or sample["worst_case_cost"] != 1:
        raise AssertionError("source completeness mutation control failed")
    return {"cases": records, "source_completeness_mutation": {
        "complete_source_optimum": whole["worst_case_cost"],
        "sample_source_optimum": sample["worst_case_cost"],
        "unreported_source_state_omitted": 1}}


def run(computation_root, physics_root):
    D, dhash = load_target(computation_root, "cambrian_d_computation")
    F, fhash = load_target(physics_root, "cambrian_f_closure")
    return {"schema": "cambrian-audit-g-exact-holdouts-v1",
            "target_source_sha256": {"D": dhash, "F": fhash},
            "linear_memory": audit_linear(F), "fluid": audit_fluid(F),
            "history_learning": audit_learning(D), "costed_destructive_probes": audit_costs(D),
            "target_validation_helpers_or_oracles_called": False,
            "original_source_authentication_established": False,
            "academic_novelty_established": False,
            "independent_external_referee": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--computation-root", default=str(ROOT))
    parser.add_argument("--physics-root", default=str(ROOT))
    parser.add_argument("--output", default=str(ROOT / "research/2026-10-13/CAMBRIAN_AUDIT_G_RAW.json"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = exact_json(run(args.computation_root, args.physics_root))
    if args.check:
        if json.loads(Path(args.output).read_text()) != result:
            raise AssertionError("Frozen audit receipt differs from fresh exact replay")
    else:
        Path(args.output).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"linear_cases": len(result["linear_memory"]["cases"]),
                      "fluid_integer_cases": len(result["fluid"]["target_family_fresh_integer_cases"]),
                      "learner_cases": len(result["history_learning"]["cases"]),
                      "cost_cases": len(result["costed_destructive_probes"]["cases"]),
                      "all_exact_comparisons_passed": True,
                      "raw_output": args.output}, indent=2))
