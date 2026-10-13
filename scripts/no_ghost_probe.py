#!/usr/bin/env python3
"""Emit exact reproducible NO-GHOST demonstrations as JSON, never real receipts."""
from __future__ import annotations

import argparse
import dataclasses
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.no_ghost import (  # noqa: E402
    CouplingProblem, Event, FiniteContract, Step, couple_contexts,
    enumerate_schedule, event_context_problem, operational_equations, solve_nonnegative,
    three_coin_experiment, verify_dual, verify_higher_failure, verify_primal,
)
from observational_succ.no_ghost_policy import (  # noqa: E402
    compile_public_policy, operational_coupling, replay_public_policy,
    verify_policy_obstruction, verify_policy_solution,
)


def serialize(value):
    if dataclasses.is_dataclass(value):
        return serialize(dataclasses.asdict(value))
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serialize(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialize(x) for x in value]
    return value


def hidden_guess_contract(*, licensed_read=False):
    """Declared source-backed choice model; no test-module fixture dependency."""
    sources = (0, 1)
    events = (Event('guess0'), Event('guess1'))
    kernels = {}
    for source in sources:
        for guess in (0, 1):
            kernels[((), 'guess'+str(guess), source, 'ready')] = (
                Step(int(source == guess), 'ready', 'unit', Q(1)),)
    if licensed_read:
        events += (Event('read'),)
        for source in sources:
            kernels[((), 'read', source, 'ready')] = (Step(source, 'ready', 'unit', Q(1)),)
            for guess in (0, 1):
                kernels[((('read', source),), 'guess'+str(guess), source, 'ready')] = (
                    Step(int(source == guess), 'ready', 'unit', Q(1)),)
    return FiniteContract('NO_GHOST_HIDDEN_GUESS', 'immutable-bit-source', sources,
                          ('ready',), {'ready': 0}, events,
                          tuple((s, 'ready', Q(1, 2)) for s in sources), kernels)


def report():
    model, fibers, coherence = three_coin_experiment()
    bad, good = coherence['incoherent'], coherence['coherent']
    witness = next(i for i, x in enumerate(fibers[('a', 'b', 'c')])
                   if tuple(e.branch for e in x.events) == (0, 1, 0))
    assert verify_higher_failure(bad['left_maps'], bad['right_maps'], witness)
    atoms = tuple(itertools.product((0, 1), repeat=3))
    # Actual model-relative lawful atoms: immutable triple-bit source labels,
    # three deterministic nondestructive reads, one fixed uniform preparation.
    read_kernels = {}
    names = ('a', 'b', 'c')
    for source in atoms:
        for length in range(3):
            h = tuple((names[i], source[i]) for i in range(length))
            read_kernels[(h, names[length], source, 'ready')] = (
                Step(source[length], 'ready', 'unit', Q(1)),)
    reads = FiniteContract('NO_GHOST_SOURCE_BITS', 'bits', atoms, ('ready',), {'ready': 0},
                           tuple(Event(a) for a in names), tuple((s, 'ready', Q(1, 8)) for s in atoms),
                           read_kernels)
    executions = enumerate_schedule(reads, names)
    contexts = (('a', 'b'), ('b', 'c'), ('a', 'c'))
    negative = event_context_problem(executions, contexts, ({(0, 1): Q(1, 2), (1, 0): Q(1, 2)},)*3)
    A, b = negative.equations()
    obstruction = couple_contexts(negative)
    assert verify_dual(A, b, obstruction.dual)
    uniform = {(a, b): Q(1, 4) for a in (0, 1) for b in (0, 1)}
    positive = event_context_problem(executions, contexts, (uniform,)*3)
    coupling = couple_contexts(positive)
    assert verify_primal(*positive.equations(), coupling.primal)
    flow_A, flow_b = operational_equations(reads, names, executions.atoms)
    assert verify_primal(flow_A, flow_b, (Q(1, 8),)*8)
    assert verify_primal(*positive.equations(), (Q(1, 8),)*8)
    coin = FiniteContract('NO_GHOST_FAIR_COIN', 'bits', ('s',), ('ready',), {'ready': 0},
                          (Event('flip'),), (('s', 'ready', Q(1)),),
                          {((), 'flip', 's', 'ready'): (Step(0, 'ready', 0, Q(1, 2)), Step(1, 'ready', 1, Q(1, 2)))})
    coin_atoms = enumerate_schedule(coin, ('flip',)).atoms
    biased = CouplingProblem(tuple(a.identity for a in coin_atoms), ((0, 1),), ({0: Q(3, 4), 1: Q(1, 4)},))
    support = couple_contexts(biased)
    C, d = biased.equations()
    F, f = operational_equations(coin, ('flip',), coin_atoms)
    operational = solve_nonnegative(C+F, d+f)
    assert verify_dual(C+F, d+f, operational.dual)
    hidden = hidden_guess_contract()
    blind_system = compile_public_policy(hidden, 1).system
    blind_labels = (tuple(a.events[-1].outcome for a in blind_system.atoms),
                    tuple(a.source for a in blind_system.atoms))
    desired = ({1: Q(1)}, {0: Q(1, 2), 1: Q(1, 2)})
    blind_support = CouplingProblem(tuple(a.identity for a in blind_system.atoms), blind_labels, desired)
    blind_supported = couple_contexts(blind_support)
    blind_impossible = operational_coupling(blind_system, blind_labels, desired)
    policy_A, policy_b = blind_system.equations(blind_labels, desired)
    assert verify_primal(*blind_support.equations(), blind_supported.primal)
    assert verify_dual(policy_A, policy_b, blind_impossible.dual)
    assert verify_policy_obstruction(hidden, 1, blind_labels, desired, blind_impossible.dual)
    read_model = hidden_guess_contract(licensed_read=True)
    read_system = compile_public_policy(read_model, 2).system
    read_labels = (tuple(a.events[-1].outcome for a in read_system.atoms),)
    adaptive = operational_coupling(read_system, read_labels, ({1: Q(1)},))
    assert verify_policy_solution(read_model, read_system, adaptive.primal, read_labels, ({1: Q(1)},))
    policy = read_system.policy(adaptive.primal)
    replayed = replay_public_policy(read_model, 2, policy)
    predicted = dict(zip((a.identity for a in read_system.atoms), read_system.weights(adaptive.primal)))
    assert replayed == {key: value for key, value in predicted.items() if value}
    assert all(identity[-1][-1].outcome == 1 for identity in replayed)
    return serialize({
        'scope': 'Declared exact finite model. Every history is possible, not a performed event.',
        'three_event_coherence': {
            'source_id': model.source_id, 'schedules': len(fibers), 'atoms_per_schedule': 8,
            'atom_mass': Q(1, 8), 'chosen_cnot_maps': bad, 'coherent_token_swaps': good,
            'witness_bits': (0, 1, 0), 'witness_index': witness,
            'conclusion': 'Chosen lawful pair comparisons fail coherence; a coherent family exists on the same model.'},
        'odd_parity_triangle': {
            'source_id': reads.source_id, 'original_sources': atoms,
            'lawful_atoms': tuple(a.identity for a in executions.atoms),
            'A': A, 'b': b, 'status': obstruction.status, 'dual': obstruction.dual,
            'dual_check': True, 'checked_bases': obstruction.checked_bases},
        'positive_pair_contexts': {
            'original_sources': atoms, 'A': positive.equations()[0], 'b': positive.equations()[1],
            'status': coupling.status, 'support_only_coupling': coupling.primal,
            'fixed_preparation_operational_coupling': (Q(1, 8),)*8,
            'operational_flow_A': flow_A, 'operational_flow_b': flow_b, 'primal_check': True},
        'support_is_not_operation': {
            'source_kernel': (Q(1, 2), Q(1, 2)), 'requested_law': (Q(3, 4), Q(1, 4)),
            'support_only_status': support.status, 'support_only_weights': support.primal,
            'operational_status': operational.status, 'A': C+F, 'b': d+f,
            'dual': operational.dual, 'dual_check': True},
        'legal_support_and_prior_do_not_enable_hidden_oracle': {
            'source_id': hidden.source_id, 'horizon': 1,
            'requested_success': Q(1), 'original_source_prior': (Q(1, 2), Q(1, 2)),
            'support_only_status': blind_supported.status,
            'support_only_coupling': blind_supported.primal,
            'public_policy_status': blind_impossible.status,
            'variables': blind_system.variables, 'A': policy_A, 'b': policy_b,
            'dual': blind_impossible.dual, 'dual_check': True,
            'conclusion': 'Source-aware choice would succeed, but every blind public policy has success 1/2.'},
        'licensed_read_repairs_hidden_guess': {
            'source_id': read_model.source_id, 'horizon': 2, 'status': adaptive.status,
            'public_policy': policy, 'realization_plan': adaptive.primal,
            'operational_weights': read_system.weights(adaptive.primal),
            'independent_replay': [{'identity': key, 'mass': value} for key, value in replayed.items()],
            'replay_matches_linear_weights': True,
            'scope': 'Read action was explicitly supplied by the contract; the solver did not invent it.'},
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional exact JSON artifact path')
    args = parser.parse_args()
    value = report()
    rendered = json.dumps(value, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
        print(json.dumps({'output': str(args.output), 'verified': True}))
    else:
        print(rendered, end='')


if __name__ == '__main__':
    main()
