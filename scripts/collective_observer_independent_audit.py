#!/usr/bin/env python3
"""Independent hostile audit. Writes only an explicitly requested audit receipt.

Oracles use partition atoms, integer polynomial character sums, permutation
matrices, and exhaustive finite transducers, not implementation certificates.
All universal claims require the accompanying paper proof. No full suite/Lean.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import itertools as it
import json
import platform
import resource
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial, gcd, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True


def require(test, detail):
    if not test:
        raise AssertionError(detail)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError) as exc:
        return type(exc).__name__ + ': ' + str(exc)
    raise AssertionError('mutation accepted')


def ds(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def divpoly(p, q):
    p = trim(p)
    answer = [0] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and any(p):
        degree, c = len(p) - len(q), p[-1] // q[-1]
        answer[degree] += c
        for j, x in enumerate(q):
            p[j + degree] -= c * x
        p = trim(p)
    return tuple(trim(answer)), tuple(p)


@lru_cache(None)
def cyclotomic(n):
    p = (-1,) + (0,) * (n - 1) + (1,)
    for d in ds(n)[:-1]:
        p, rem = divpoly(p, cyclotomic(d))
        require(not any(rem), ('cyclotomic division', n, d))
    return p


@lru_cache(None)
def ramanujan(d, t):
    p = [0] * d
    for k in range(d):
        if gcd(k, d) == 1:
            p[k * t % d] += 1
    _, rem = divpoly(p, cyclotomic(d))
    require(len(rem) == 1, ('nonrational character sum', d, t, rem))
    return rem[0]


def rank(rows):
    a = [list(map(Q, r)) for r in rows]
    i = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        c = a[i][j]
        a[i] = [x / c for x in a[i]]
        for k in range(i + 1, len(a)):
            c = a[k][j]
            if c:
                a[k] = [x - c * y for x, y in zip(a[k], a[i])]
        i += 1
        if i == len(a):
            break
    return i


def atoms(n, moduli):
    groups = {}
    for x in range(n):
        groups.setdefault(tuple(x % m for m in moduli), []).append(x)
    return tuple(tuple(g) for g in groups.values())


def partition_projection(n, m):
    groups = atoms(n, (m,))
    return tuple(tuple(next((Q(1, len(g)) for g in groups if x in g and y in g), Q())
                       for y in range(n)) for x in range(n))


def modular_audit():
    mod = importlib.import_module('observational_succ.collective_modular')
    cases = {'clocks': 0, 'sectors': 0, 'pairs': 0, 'triples': 0}
    for n in range(1, 19):
        cases['clocks'] += 1
        es = {m: partition_projection(n, m) for m in ds(n)}
        ps = {}
        for d in ds(n):
            expected = tuple(tuple(Q(ramanujan(d, (x-y) % d), n) for y in range(n))
                             for x in range(n))
            ps[d] = expected
            require(mod.conditional_expectation(n, d) == es[d], ('partition E', n, d))
            require(mod.conductor_projector(n, d) == expected, ('Fourier P', n, d))
            require(rank(expected) == sum(gcd(k, d) == 1 for k in range(d)), ('rank', n, d))
            cases['sectors'] += 1
        for a, b in it.product(ds(n), repeat=2):
            # Direct intersection count for matrix multiplication of two averages.
            eaeb = tuple(tuple(Q(a*b, n*n) * sum((x-z) % a == 0 and (z-y) % b == 0
                            for z in range(n)) for y in range(n)) for x in range(n))
            require(eaeb == es[gcd(a, b)], ('E multiplication', n, a, b))
            partition_basis = [tuple(int(x in g) for x in range(n))
                               for m in (a, b) for g in atoms(n, (m,))]
            linear = rank(partition_basis)
            joint = len(atoms(n, (a, b)))
            out = mod.collective_sectors(n, (a, b))
            require((linear, joint) == (out.linear_dimension, out.joint_dimension),
                    ('independent ranks', n, a, b))
            require(joint == lcm(a, b), ('partition joint', n, a, b))
            expected_pool = tuple(tuple(sum((ps[d][x][y] for d in ds(n)
                                             if a % d == 0 or b % d == 0), Q())
                                       for y in range(n)) for x in range(n))
            require(mod.linear_pool_projector(n, (a, b)) == expected_pool,
                    ('linear pool projector', n, a, b))
            missing = tuple(tuple(es[joint][x][y] - expected_pool[x][y] for y in range(n))
                            for x in range(n))
            require(mod.missing_joint_projector(n, (a, b)) == missing,
                    ('missing projector', n, a, b))
            cases['pairs'] += 1
        if n <= 10:
            for ms in it.product(ds(n), repeat=3):
                out = mod.collective_sectors(n, ms)
                for s in out.sectors:
                    # Frequency k=n/d belongs to the span of joint partition atoms
                    # iff it is constant on every such atom. Test divisibility of phases.
                    k = n // s.conductor
                    order = next(r for r in range(4) if any(
                        all(all((k*(x-g[0])) % n == 0 for x in g) for g in atoms(n, subset))
                        for subset in it.combinations(ms, r)))
                    require(order == s.minimum_joint_menus, ('interaction order', n, ms, s))
                cases['triples'] += 1
    require(rank([tuple(int(x % 2 == r) for x in range(6)) for r in range(2)] +
                 [tuple(int(x % 3 == r) for x in range(6)) for r in range(3)]) == 4,
            'mod2/mod3 control')
    return {'status': 'PASS_FINITE_EXHAUSTIVE', 'counts': cases,
            'bounds': 'all N=1..18 divisor pairs; N=1..10 divisor triples',
            'oracle': 'partition indicator rank plus cyclotomic polynomial character sums',
            'control': {'N': 6, 'moduli': [2, 3], 'linear_rank': 4, 'joint_rank': 6,
                        'lost_vector': [2, 1, -1, -2, -1, 1]}}


def adaptive_quotient_audit():
    # Each action is a complete table q -> (output/rejection, next quotient).
    # Hidden bit may evolve; the quotient evolution is fiber-constant.
    actions = tuple(it.product(tuple(it.product(range(3), range(2))), repeat=2))
    policies = tuple(it.product(range(2), repeat=4))
    compared = 0
    for model in it.product(actions, repeat=2):
        for policy in policies:
            transcripts = []
            for start in range(4):
                state, a, transcript = start, policy[0], []
                for step in range(2):
                    output, qnext = model[a][state // 2]
                    transcript.append((a, output))
                    if output == 2:
                        break  # Illegal action is visible, not silently filtered.
                    state = 2*qnext + ((state % 2) ^ a)
                    a = policy[1 + output]
                transcripts.append(tuple(transcript))
            require(transcripts[0] == transcripts[1] and transcripts[2] == transcripts[3],
                    ('quotient leak', model, policy, transcripts))
            compared += 2
    # Executable counterexamples to omitted assumptions. Both worlds have q=0.
    mutations = {
        'legality': [('read', 'OK', 0), ('read', 'FORBIDDEN', None)],
        'cost': [('read', 0, 1), ('read', 0, 2)],
        'hidden_initial_memory': [('action_A', 0), ('action_B', 0)],
        'hidden_transition': [('move', 0, 'read', 0), ('move', 0, 'read', 1)],
        'history': [('read_after_A', 0), ('read_after_B', 0)],
    }
    for key, traces in mutations.items():
        require(traces[0] != traces[1], key)
    # Same marginal laws do not imply equal joint laws: correlated/anticorrelated bits.
    correlated = {(0, 0): Q(1, 2), (1, 1): Q(1, 2)}
    anticorrelated = {(0, 1): Q(1, 2), (1, 0): Q(1, 2)}
    for j in range(2):
        require(sum(p for y, p in correlated.items() if y[j] == 0) ==
                sum(p for y, p in anticorrelated.items() if y[j] == 0), 'marginal')
    require(correlated != anticorrelated, 'correlation side channel control')
    return {'status': 'PASS_FINITE_EXHAUSTIVE', 'models': len(actions)**2,
            'policies': len(policies), 'fiber_comparisons': compared,
            'horizon': 2, 'mutations': mutations,
            'marginal_only_refutation': {'world0': ['00', '11'], 'world1': ['01', '10']},
            'boundary': 'paper induction needs joint conditional kernels; finite count is not universal proof'}


def permutation_matrix(p):
    return tuple(tuple(int(i == p[j]) for j in range(5)) for i in range(5))


def matmul(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def transpose(a):
    return tuple(zip(*a))


def ambient_audit():
    w = importlib.import_module('observational_succ.wild_ambient_succ')
    table = w.a5_commutator_witnesses()
    # Independent parity: cycle decomposition, not the implementation's inversions.
    even = []
    for p in it.permutations(range(5)):
        seen, cycles = set(), 0
        for i in range(5):
            if i not in seen:
                cycles += 1
                while i not in seen:
                    seen.add(i)
                    i = p[i]
        if (5-cycles) % 2 == 0:
            even.append(p)
    mats = {p: permutation_matrix(p) for p in even}
    spectrum = set()
    for a, b in it.product(even, repeat=2):
        A, B = mats[a], mats[b]
        spectrum.add(matmul(matmul(matmul(A, B), transpose(A)), transpose(B)))
    require(spectrum == set(mats.values()) and len(spectrum) == 60, 'A5 commutator image')
    require(set(table) == set(even), 'complete A5 table domain')
    for z, (a, b) in table.items():
        A, B = mats[a], mats[b]
        require(matmul(matmul(matmul(A, B), transpose(A)), transpose(B)) == mats[z],
                ('commutator table entry', z))
    receipt = w.alexander_a5_finite_quotient()
    seeds = [mats[x] for x in receipt['stage_two_generators']]
    identity = permutation_matrix(tuple(range(5)))
    closure = {identity}
    while True:
        nxt = closure | {matmul(x, g) for x in closure for g in seeds}
        if nxt == closure:
            break
        closure = nxt
    require(closure == set(mats.values()), 'surjective stage two')
    root = receipt['root']
    levels = [(root,)]
    relations = 0
    for _ in range(7):
        levels.append(tuple(c for p in levels[-1] for c in table[p]))
        for p, a, b in zip(levels[-2], levels[-1][::2], levels[-1][1::2]):
            A, B = mats[a], mats[b]
            require(matmul(matmul(matmul(A, B), transpose(A)), transpose(B)) == mats[p],
                    'tower compatibility')
            relations += 1
    return {'status': 'PASS_FINITE_EXHAUSTIVE_WITH_RECURSIVE_PROOF', 'commutator_pairs': 3600,
            'complete_rule_entries': 60, 'stage_two_generated_order': len(closure),
            'recursive_relations_checked': relations, 'root_trace': sum(root[i] == i for i in range(5)),
            'identity_trace': 5, 'global_A5_quotient': 'established by complete rule + colimit compatibility',
            'source_dependency': 'Hatcher 2B.2 pp171-172 exterior group import; no physical realization'}


def miniature_fixture():
    from observational_succ.source_lambda import Passport
    from observational_succ.consensus_lambda import MiniPort
    from observational_succ.miniature_carrier import Carrier, Mini
    src = 'hostile-audit'
    states = tuple(''.join(s) for s in it.product('01', repeat=2))
    parent = Carrier(states, {name: {s: ''.join(str(1-int(c)) if j == bit else c
                      for j, c in enumerate(s)) for s in states}
                      for name, bit in [('left', 0), ('right', 1)]},
                     {s: s for s in states}, ('00',), src)
    ports = []
    for bit, name in enumerate(('left', 'right')):
        mini = Mini(('0', '1'), {'flip': {'0': '1', '1': '0'}},
                    {'0': name+'0', '1': name+'1'}, '0', src)
        ports.append(MiniPort(name, parent, mini, {s: s[bit] for s in states},
                              {'flip': (name,)}, {s: name+s[bit] for s in states}))
    return Passport(src, 3), parent, ports


def parent140_audit():
    from observational_succ.consensus_lambda import certify_dual_ports
    from observational_succ.miniature_carrier import compile_dual_product
    p, carrier, (left, right) = miniature_fixture()
    public = {s: ('left'+s[0], 'right'+s[1]) for s in carrier.states}
    raw = compile_dual_product(carrier, left.mini, right.mini, left.decoder, right.decoder,
                               ('left',), ('right',), public)
    require(raw['certified'] and raw['realization'] == 'independent_joint_factor', raw)
    try:
        raw['kind']
    except KeyError as exc:
        historical = repr(exc)
    else:
        raise AssertionError('historical schema mutation no longer reproduces')
    result = certify_dual_ports(left, right, p, ('left',), ('right',), public)
    require(result['certified_joint_model'] and result['status'] == raw['realization'], result)
    before = ROOT / 'research/2026-10-16/collective_observer_receipts/dual-port-before.log'
    ci = ROOT / 'research/2026-10-16/collective_observer_receipts/parent-140-failed-ci.log'
    require("KeyError: 'kind'" in before.read_text() and "KeyError: 'kind'" in ci.read_text(),
            'historical regression evidence missing')
    return {'status': 'PASS_REAL_CONTRACT_AND_HISTORICAL_MUTATION', 'current': result,
            'old_schema_mutation': historical, 'historical_logs': [str(before.relative_to(ROOT)),
                                                                 str(ci.relative_to(ROOT))]}


def effects_audit():
    e = importlib.import_module('observational_succ.collective_effects')
    from observational_succ.source_lambda import Passport, Read, Eq, Residue, Bool, Atlas, Forget
    p = Passport('effect-audit', 4)
    context = e.Context(p, (e.Event('r2', 'Alice', p, 2, 1),
                            e.Event('r3', 'Alice', p, 3, 2)))
    prefix = (e.Replay('r2', 'Alice'), e.Replay('r3', 'Alice'),
              e.Derive(Eq(Forget(Read(2)), Residue(2, 1)), (0, 1), 'Alice'))
    counters = {'compressed_read_attacks': 0, 'raw_relay_checks': 0, 'debt_checks': 0}
    for hops in range(1, 9):
        program, sender = list(prefix), 'Alice'
        for j in range(hops):
            receiver = f'actor{j}'
            program.append(e.Relay(len(program)-1, sender, receiver))
            sender = receiver
        out = e.run(tuple(program), context)
        require(out.artifacts[-1].origins == frozenset(('r2',)), 'compressed lineage')
        require(not out.artifacts[-1].readable_events, 'compressed permission leak')
        for modulus in (2, 3):
            rejects(lambda m=modulus: e.run(tuple(program)+(e.Derive(Read(m),
                           (len(program)-1,), sender),), context))
            counters['compressed_read_attacks'] += 1
    for modulus, index in ((2, 0), (3, 1)):
        out = e.run(prefix[:2]+(e.Relay(index, 'Alice', 'Bob'),
                              e.Derive(Read(modulus), (2,), 'Bob')), context)
        require(out.artifacts[-1].value.value == (1 if modulus == 2 else 2), 'raw relay')
        counters['raw_relay_checks'] += 1
    rejects(lambda: e.run(prefix[:2]+(e.Derive(Read(2), (0,), 'Bob'),), context))
    rejects(lambda: e.run((e.Replay('r2', 'Bob'),), context))
    rejects(lambda: e.run((e.Derive(Read(2), (), 'Alice'),), context))
    rejects(lambda: e.run((e.Derive(Bool(True), (0,), 'Alice'),), context))
    rejects(lambda: e.run((e.Predict(Read(2), Atlas(p, ((2, 1),)), 'Alice'),
                           e.Relay(0, 'Alice', 'Bob')), context))
    foreign = e.Context(Passport('effect-audit', 5), context.events)
    rejects(lambda: e.run((e.Replay('r2', 'Alice'),), foreign))
    branch = e.Context(p, (e.Event('branch', 'Alice', p, 2, 1, ('left',)),), ('right',))
    rejects(lambda: e.run((e.Replay('branch', 'Alice'),), branch))
    for length in range(1, 9):
        program = [e.AnalyticImport('conditional theorem', ('DEBT_A',))]
        for j in range(length):
            program.append(e.ExactQuadratic(((1, 0), (0, -1)), (0, 1), (len(program)-1,)))
            program.append(e.AnalyticImport('wrapped claim', (f'DEBT_{j}',), (len(program)-1,)))
        out = e.run(tuple(program), context)
        for a, b in zip(out.artifacts, out.artifacts[1:]):
            require(a.obligations <= b.obligations, 'debt erased')
            counters['debt_checks'] += 1
        require(not out.global_theorem_proved and out.new_physical_measurements == 0, 'promotion')
    mp, carrier, (left, _) = miniature_fixture()
    state = e.MacroState(mp, mp, frozenset(('00', '10')), frozenset(('token',)))
    nxt, receipt = e.miniature_action(state, left, 'flip', 'token')
    require(nxt.current.epoch == mp.epoch+1 and nxt.original == mp and not nxt.capabilities,
            'macro epoch/capability')
    require(not receipt['physical_action_executed'], 'physical promotion')
    rejects(lambda: e.miniature_action(nxt, left, 'flip', 'token'))
    again, _ = e.miniature_action(state, left, 'flip', 'token')
    require(again == nxt, 'counterfactual replay should remain deterministic')
    return {'status': 'PASS_TARGETED_HOSTILE_CHAINS', 'counts': counters,
            'macro': receipt, 'boundary': 'immutable counterfactual reuse is allowed; no joint execution certified'}


def policy_audit():
    p = importlib.import_module('observational_succ.collective_policy')
    @lru_cache(None)
    def trees(actions, depth):
        if not depth:
            return ('0', '1')
        smaller = trees(actions, depth-1)
        return ('0', '1') + tuple((a, l, r) for a in range(actions)
                                  for l, r in it.product(smaller, repeat=2))
    def accepts(tree, tables, original, current, remaining):
        if isinstance(tree, str):
            return tree == str(original)
        if remaining == 0:
            return False
        a, left, right = tree
        row = tables[a][current]
        return bool(row) and all(accepts((left, right)[public], tables, original,
                                        after, remaining-1) for public, after in row)
    def make(tables):
        actions = tuple(p.Action(str(j), 'A', 'probe', p.Cost(1, 1, observation_bits=1),
                        tuple(tuple(p.Outcome(str(y), z) for y, z in row) for row in a))
                        for j, a in enumerate(tables))
        return p.CollectiveModel('audit-model', 'original-bit', ('A',),
            (p.Source('s0', '0'), p.Source('s1', '1')),
            (p.JointState('c0', ('unchanged',)), p.JointState('c1', ('unchanged',))),
            ((0, 0), (1, 1)), actions)
    cases = winning = 0
    deterministic_rows = ((),) + tuple(((y, z),) for y, z in it.product(range(2), repeat=2))
    nondeterministic_rows = tuple(tuple(v for i, v in enumerate(it.product(range(2), repeat=2))
                                      if mask & (1 << i)) for mask in range(16))
    for n_actions, rows in ((2, deterministic_rows), (1, nondeterministic_rows)):
        action_tables = tuple(it.product(rows, repeat=2))
        for tables in it.product(action_tables, repeat=n_actions):
            model = make(tables)
            for depth in range(3):
                expected = any(all(accepts(tree, tables, s, s, depth) for s in range(2))
                               for tree in trees(n_actions, depth))
                budget = p.Cost(depth, depth, observation_bits=depth, certificate=1)
                result = p.solve_collective_policy(model, budget)
                require(result.winning == expected, ('raw tree disagreement', tables, depth))
                if result.winning:
                    replay = p.replay_policy(model, budget, result.policy)
                    require(replay.worst_cost.fits(budget), 'certificate replay cost')
                    winning += 1
                cases += 1
    # Menu-only distinction must not count as a uniform safe observation.
    menu = make(((((0, 0),), ()), ((), ((1, 1),))))
    require(not p.solve_collective_policy(menu, p.Cost(3, 3, observation_bits=3, certificate=1)).winning,
            'nonuniform legality used as observation')
    # Same current state cannot erase disagreement about the original source.
    from dataclasses import replace
    merge = replace(menu, initial=((0, 0), (1, 0)), actions=())
    require(not p.solve_collective_policy(merge, p.Cost(5, 5, certificate=1)).winning,
            'original/current collapse')
    # Replay must reject an omitted possible outcome, even if the retained branch wins.
    nd = make(((((0, 0), (1, 0)), ((1, 1),)),))
    rejects(lambda: p.replay_policy(nd, p.Cost(1, 1, observation_bits=1, certificate=1),
                     p.Policy(action='0', branches=(('0', p.Policy(claim='0')),))))
    # Cross-enabled execution requires every independent path budget coordinate.
    ladder = p.cross_enabled_model()
    budget = p.Cost(depth=8, actions=4, messages=4, communication_bits=1, observation_bits=1, certificate=9)
    result = p.solve_collective_policy(ladder, budget)
    require(result.winning, 'ladder failed with exact budget')
    replay = p.replay_policy(ladder, budget, result.policy)
    require(replay.worst_cost == budget, 'ladder cost exactness')
    for j, cap in enumerate(budget.vector):
        v = list(budget.vector)
        v[j] = cap-1
        require(not p.solve_collective_policy(ladder, p.Cost(*v)).winning,
                ('cost undercharge', j))
    for active in (('A',), ('B',)):
        require(not p.solve_collective_policy(p.restrict_observers(ladder, active), budget).winning,
                ('observer ablation', active))
    # Try to leak a carrier bit through a sender whose memory is identical.
    s = (p.JointState('c0', ('same', 'old')), p.JointState('c1', ('same', 'old')))
    action = p.Action('send', 'A', 'message', p.Cost(1, 0, 1, 1),
                      ((p.Outcome('0', 0),), (p.Outcome('1', 1),)), 'B')
    rejects(lambda: p.CollectiveModel('m', 't', ('A', 'B'),
             (p.Source('s0', '0'), p.Source('s1', '1')), s, ((0, 0), (1, 1)), (action,)))
    # Newly declared private readouts must pay bits and cannot update a bystander.
    st = (p.JointState('c0', ('same', 'same')), p.JointState('c1', ('same', 'same')),
          p.JointState('c0', ('saw0', 'same')), p.JointState('c1', ('saw1', 'same')))
    hidden = p.Action('hidden', 'A', 'probe', p.Cost(1, 1),
                       ((p.Outcome('constant', 2),), (p.Outcome('constant', 3),), (), ()))
    rejects(lambda: p.CollectiveModel('m', 't', ('A', 'B'),
                (p.Source('s0', '0'), p.Source('s1', '1')), st, ((0, 0), (1, 1)), (hidden,)))
    declared = replace(hidden, cost=p.Cost(1, 1, observation_bits=1),
                       rows=((p.Outcome('constant', 2, '0'),), (p.Outcome('constant', 3, '1'),), (), ()))
    private_model = p.CollectiveModel('m', 't', ('A', 'B'),
                (p.Source('s0', '0'), p.Source('s1', '1')), st, ((0, 0), (1, 1)), (declared,))
    require(not p.solve_collective_policy(private_model, p.Cost(2, 2, observation_bits=2, certificate=1)).winning,
            'private readout became public branch key')
    for bits, capacity in ((2, 1), (3, 2)):
        bounded = p.capacity_parity_model(bits, capacity)
        enough = p.capacity_parity_model(bits, bits)
        budget2 = p.Cost(bits+1, bits+1, observation_bits=bits+1, certificate=bits+2)
        require(not p.solve_collective_policy(bounded, budget2).winning, 'unperformed-history union')
        require(p.solve_collective_policy(enough, budget2).winning, 'capacity positive control')
    return {'status': 'PASS_INDEPENDENT_RAW_POLICY_ENUMERATION', 'bounded_comparisons': cases,
            'winning_certificates_replayed': winning, 'deterministic_two_action_models': 625,
            'nondeterministic_one_action_models': 256, 'depths': [0, 1, 2],
            'oracle': 'all labeled public binary trees on raw concrete trajectories; no belief recursion',
            'ladder_worst_cost': replay.worst_cost.vector,
            'boundary': 'declared tables and public-history central scheduler; physical and distributed realization external'}


def gamma_audit():
    g = importlib.import_module('observational_succ.collective_gamma')
    cases = 0
    meshes = tuple(sorted({Q(a, b) for a in range(1, 6) for b in range(1, 7)}))
    # Independent integer lattice enumeration on a shared denominator D:
    # period/(4*pi*D) is 1/gcd(integer mesh labels), checked via Bezout lattice.
    for hs in it.product(meshes, repeat=2):
        den = hs[0].denominator*hs[1].denominator
        aa, bb = (int(h*den) for h in hs)
        # Euclidean lattice generated by integer sums, not rational_gcd helper.
        lattice = {abs(u*aa+v*bb) for u in range(-bb, bb+1) for v in (-1, 0, 1)}
        smallest = min(x for x in lattice if x)
        # Include complete bounded Bezout rectangle for an exact independent minimum.
        smallest = min(abs(u*aa+v*bb) for u in range(-bb, bb+1)
                       for v in range(-aa, aa+1) if u*aa+v*bb)
        expected = Q(4*den, smallest)
        require(g.joint_period_pi(hs) == expected, ('period lattice', hs))
        for multiplier in (Q(0), Q(1, 2), Q(1), Q(3, 2), Q(-2)):
            candidate = multiplier*expected
            expected_period = all((candidate*h/4).denominator == 1 for h in hs)
            require(g.is_joint_period(hs, candidate) == expected_period, ('period test', hs))
        cases += 1
    # Periodicity is insufficient for injectivity. cos(t) has exact collisions
    # +/-pi/2 within a single length-2*pi fundamental interval.
    require(Q(-1, 2) != Q(1, 2) and Q(1) < 2, 'injectivity countermodel')
    # Normative Gamma_R(1)=1 is independent of the implementation's special functions.
    cert = g.certify_gamma(1, 0, Q(1, 4), -160, 16, digits=24)
    require(cert.enclosure.real.contains(1) and cert.enclosure.imag.contains(0), 'Gamma_R(1)')
    require(cert.coordinate_radius < Q(1, 10**7), 'Gamma certificate too broad')
    # Coop is fresh translated samples; omit/duplicate labels must fail upstream.
    kwargs = (1, Q(7, 5), Q(3, 4), 3, -120, 15)
    coop, lanes = g.cooperative_gamma(*kwargs, digits=24)
    direct = g.certify_gamma(1, Q(7, 5), Q(1, 4), -120, 15, digits=24)
    for a, b in ((coop.finite_sum.real, direct.finite_sum.real),
                 (coop.finite_sum.imag, direct.finite_sum.imag)):
        require(max(a.lower, b.lower) <= min(a.upper, b.upper), 'cooperative refinement')
    rejects(lambda: g.cooperative_gamma(*kwargs, digits=24, lanes=(0, 1, 1)))
    rejects(lambda: g.cooperative_gamma(*kwargs, digits=24, lanes=(0, 1)))
    return {'status': 'PASS_EXACT_PERIOD_LATTICE_AND_SOURCE_CONTROLS', 'rational_mesh_pairs': cases,
            'known_Gamma_R_1_radius': str(cert.coordinate_radius),
            'injectivity_boundary': 'no common nonzero period does not establish injection',
            'exact_counterexample': 'cos(-pi/2)=cos(pi/2)=0 inside one fundamental interval',
            'decoder_boundary': 'decode_lanes is untyped arithmetic; cooperative_gamma validates complete lane identity',
            'dependencies': ['normative Euler Gamma integral', 'padded Decimal exp contract', 'paper contour/tail bounds']}


def spectral_audit():
    s = importlib.import_module('observational_succ.collective_spectral')
    from dataclasses import replace
    forms = 0
    # Independent Gaussian-rational pairing using Python complex only on small
    # exact integers (all coordinates remain exactly representable).
    vectors = ((1, 0), (0, 1), (1, 1), (1, -1), (s.Gaussian(0, 1), 1))
    for a, d, re, im in it.product(range(-2, 3), repeat=4):
        G = s.HermitianForm(((a, s.Gaussian(re, im)), (s.Gaussian(re, -im), d)))
        for x, y in it.product(vectors, repeat=2):
            def z(v):
                return complex(v.real, v.imag) if isinstance(v, s.Gaussian) else complex(v)
            X, Y = tuple(map(z, x)), tuple(map(z, y))
            raw = X[0]*(a*Y[0].conjugate()+complex(re, im)*Y[1].conjugate()) + \
                  X[1]*(complex(re, -im)*Y[0].conjugate()+d*Y[1].conjugate())
            got = s.complex_polarization(G.quadratic, x, y)
            require(got == s.Gaussian(int(raw.real), int(raw.imag)), ('polarization', a, d, re, im))
            forms += 1
    ctx = s.Coordinates('sourcehash', 'commit', Q(1, 2), ('P1', 'P2'),
                        ('prime', 'gamma', 'poles'), (Q(1, 3), Q(1, 5)), 'Q')
    b = s.Bound(ctx, s.Interval(-2, 2), 'r0', frozenset(('shared',)))
    mutations = {'source_blob': 'other', 'source_commit': 'other', 'radius': Q(1),
                 'basis': ('P2', 'P1'), 'channels': ('prime', 'gamma'),
                 'metric_diagonal': (Q(1), Q(1)), 'target': 'other', 'convention': 'other'}
    for field, value in mutations.items():
        rejects(lambda f=field, v=value: s.intersect_bounds((b, s.Bound(replace(ctx, **{f: v}),
                      s.Interval(-1, 1), 'r1', frozenset(('new',))))))
    # Transitive dependency components must merge A--B--C, although A and C disjoint.
    bounds = (s.Bound(ctx, s.Interval(-2, 2), 'A', frozenset(('x',))),
              s.Bound(ctx, s.Interval(-1, 1), 'C', frozenset(('y',))),
              s.Bound(ctx, s.Interval(0, 1), 'B', frozenset(('x', 'y'))))
    for order in it.permutations(bounds):
        got = s.intersect_bounds(order)
        require(len(got['provenance_components']) == 1 and not got['independence_established'],
                'shared source counted independently')
    rejects(lambda: s.intersect_bounds((b, b)))
    rejects(lambda: s.intersect_bounds((b, s.Bound(ctx, s.Interval(3, 4), 'r1', frozenset(('y',))))))
    G = s.HermitianForm(((1, 2), (2, 1)))
    apparatus = s.QuadraticApparatus(G, ((1, 0), (0, 1)))
    rejects(lambda: s.complex_polarization(apparatus.measure, (1, 0), (0, 1)))
    require(G.quadratic((1, -1)) == -2 and G.quadratic((1, 0)) == G.quadratic((0, 1)) == 1,
            'positive marginals counterexample')
    margins = 0
    for denominator in range(4, 204):
        delta = Q(1, denominator)
        out = s.negative_witness_budget(delta)
        require(out['rational_quadratic_upper']+out['certification_error_allowance'] < 0,
                ('negative margin budget', delta))
        require(out['conditional_on_actual_negative_unit_direction'], 'conditional debt')
        margins += 1
    # Hidden soft mode: full Schur short -1/2 but any truncation before m sees +1/2.
    for depth in range(1, 25):
        out = s.hidden_soft_mode(depth)
        d, b, y = out['D_mm'], out['b_m'], out['witness_high_coefficient']
        energy = Q(1, 2)+2*b*y+d*y*y
        require(energy == -Q(1, 2), ('soft mode energy', depth))
        require(-energy/(1+y*y) == out['unit_witness_negative_margin'], 'margin collapse')
    return {'status': 'PASS_EXHAUSTIVE_SMALL_FORMS_AND_SOURCE_GUARDS', 'pairings': forms,
            'source_coordinate_mutants_rejected': list(mutations), 'budget_margins': margins,
            'hidden_soft_modes': 24, 'dependencies': 'typed bounds remain conditional; caller data are not authenticated',
            'source_replay': 'not rerun here: independent audit uses scalar/form algebra, sibling replay belongs to spectral lane'}


def legendre_scaled(n):
    # Rodrigues, differentiated symbolically then evaluated at 2x.
    out = [Q()]*(n+1)
    for v in range(n+1):
        k = 2*v-n
        if k >= 0:
            out[k] = Q((-1)**(n-v)*comb(n, v)*factorial(2*v)*2**k,
                       factorial(k)*2**n*factorial(n))
    return tuple(out)


def monomial_integral(n):
    return Q(0) if n % 2 else Q(1, 2**n*(n+1))


def spectral_projection_audit():
    s = importlib.import_module('observational_succ.collective_spectral')
    polynomials = [legendre_scaled(k) for k in range(6)]
    def inner(a, b):
        return sum((c*d*monomial_integral(i+j) for i, c in enumerate(a)
                    for j, d in enumerate(b)), Q())
    for i, j in it.product(range(6), repeat=2):
        require(inner(polynomials[i], polynomials[j]) == (Q(1, 2*i+1) if i == j else 0),
                ('Rodrigues normalization', i, j))
    moments = 0
    for j, k in it.product(range(1, 5), range(4)):
        psi = s.derivative_correlation_polynomial(j, k)
        for power in range(1, 20, 2):
            # Direct double integral of (x-y)^power l_j(y) l_k(x),
            # over the full square. No half-triangle/correlation helper.
            full = sum((comb(power, b)*(-1)**b*c*d*
                        monomial_integral(power-b+u)*monomial_integral(b+v)
                        for b in range(power+1) for u, c in enumerate(polynomials[k])
                        for v, d in enumerate(polynomials[j])), Q())
            reduced = sum((c/Q(power+i+1) for i, c in enumerate(psi)), Q())
            require(full == reduced, ('correlation orientation', j, k, power))
            if k == 0:
                # Boundary difference from g(r)=r^(power+1)/(power+1).
                endpoint = sum((c*Q(comb(power+1, b)*(-1)**b, power+1)*
                       (Q(1, 2)**(power+1-b)-Q(-1, 2)**(power+1-b))*
                       monomial_integral(b+v)
                       for v, c in enumerate(polynomials[j]) for b in range(power+2)), Q())
                require(endpoint == full, ('endpoint identity', j, power))
            moments += 1
    controls = 0
    for coefficients in it.product((-1, 0, 1), repeat=5):
        f = tuple(sum((coefficients[k]*(polynomials[k][i] if i < len(polynomials[k]) else 0)
                       for k in range(5)), Q()) for i in range(5))
        energy = inner(f, f)
        exact_moments = tuple(inner(f, p) for p in polynomials[:4])
        expected = Q(coefficients[4]**2, 9)
        exact = tuple(s.Interval(x, x) for x in exact_moments)
        coarse = {'mode': 1, 'finite_J_energy_upper': energy,
                  'projection_moment_intervals': tuple((x-Q(1, 10), x+Q(1, 10)) for x in exact_moments)}
        out = s.refine_projected_column(coarse, exact)
        require(out['projected_energy_upper'] == expected, 'orthogonal subtraction')
        # Widening moments may reduce removable energy, never yield a false upper.
        out2 = s.refine_projected_column(coarse, tuple(s.Interval(x-Q(1, 20), x+Q(1, 20))
                                                       for x in exact_moments))
        require(out2['projected_energy_upper'] >= expected, 'interval square orientation')
        controls += 1
    # Tail must be added in norm: residual and tail each unit in same direction.
    require((Q(1)+Q(1))**2 == 4 and Q(1)**2+Q(1)**2 == 2, 'tail cross-term control')
    # Total energy 2, low moment energy 1, finite residual norm 1, tail 1:
    # correct squared bound 4; subtracting low energy after norm tail gives >4.
    # More dangerously, subtracting FULL-source low energy from FINITE-source
    # total energy is unsound: h_J=l0, tail=-l0 -> full=0 is benign, while
    # h_J=l4 and tail=l0 gives finite total 1/9 minus full low energy 1 <0.
    require(Q(1, 9)-1 < 0, 'mismatched J moment counterexample')
    # Form/operator metric counterexample: on mode 1, c=1 means form entry1/3.
    # Treating a form entry1/3 as operator cap1/3 instead of 1 underbounds it.
    require(Q(1, 3)/Q(1, 3) == 1, 'W normalization')
    return {'status': 'PASS_INDEPENDENT_POLYNOMIAL_AND_PROJECTION_CONTROLS',
            'full_square_moment_identities': moments, 'Rodrigues_orthogonality_pairs': 36,
            'exact_and_interval_energy_controls': controls,
            'tail_counterexample': {'finite_residual_norm': 1, 'tail_norm': 1,
                                    'true_squared_norm': 4, 'incorrect_sum_of_squares': 2},
            'same_J_counterexample': 'h_J=l4; tail=l0: finite energy1/9 minus full low energy1 is negative',
            'normalization': 'input trace weights2j+1; output form subtract c/(2j+1)',
            'paper_dependency': 'inherited D>=kappa V*V; all source moments and energies at same finite J'}


def spectral_source_moment_audit(source_root=None):
    """Isolated cheap source moment check; does not rerun grid512 or full pipeline."""
    require(not any(n == 'observational_succ' or n.startswith('observational_succ.')
                    for n in sys.modules), 'run spectral_source alone to prevent mixed imports')
    import importlib.util
    spec = importlib.util.spec_from_file_location('audit_spectral_probe', ROOT/'scripts/collective_spectral_probe.py')
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    sibling = Path(source_root).resolve() if source_root is not None else ROOT.parent/'SUCC-arithmetic-resonance'
    pin = probe.verify_pin(sibling)  # identity guard only, not the mathematical oracle
    sys.path.insert(0, str(sibling))
    A = importlib.import_module('observational_succ.arithmetic_resolvent')
    L, source = A.L, A.verify_runtime_source()
    actual, endpoints = probe.exact_derivative_moments(A, 20)
    def add(a, b):
        return a[0]+b[0], a[1]+b[1]
    def scale(a, c):
        return min(a[0]*c, a[1]*c), max(a[0]*c, a[1]*c)
    def times(a, b):
        values = tuple(x*y for x in a for y in b)
        return min(values), max(values)
    def exact_integral(poly):
        return sum((c/Q(i+1) for i, c in enumerate(poly)), Q())
    def exp_integral(poly, alpha):
        # Independent direct rational Taylor quadrature. For alpha>=0,
        # e^(-alpha*r) Lagrange remainder <=alpha^(N+1)/(N+1)! on [0,1].
        # For alpha=-1/2, use e^(1/2)<2 for the derivative majorant.
        N, term, total = 200, Q(1), Q()
        for n in range(N+1):
            total += term*sum((c/Q(n+i+1) for i, c in enumerate(poly)), Q())
            term *= -alpha/Q(n+1)
        error = abs(term)*sum(abs(c) for c in poly)*(2 if alpha < 0 else 1)
        return total-error, total+error
    def polynomial_interval(poly, lo, hi):
        out = (Q(), Q())
        for i, c in enumerate(poly):
            out = add(out, scale((lo**i, hi**i), c))
        return out
    log2 = L.tight_log2(100)  # shared source constant enclosure, explicitly one source family
    invsqrt = source.sqrt_inverse(2)
    weight = times(log2, (invsqrt.lo, invsqrt.hi))
    contact = source.contact_iv()
    records = []
    for j, row in enumerate(actual, 1):
        for k, item in enumerate(row):
            poly = tuple(item['correlation_polynomial'])
            pole = add(scale(exp_integral(poly, Q(-1, 2)), -2),
                       scale(exp_integral(poly, Q(1, 2)), 2))
            ct = scale((contact.lo, contact.hi), exact_integral(poly)/2)
            primitive = (Q(),)+tuple(c/Q(i+1) for i, c in enumerate(poly))
            at_one = sum(primitive)
            at_log = polynomial_interval(primitive, *log2)
            prime = times(weight, (at_one-at_log[1], at_one-at_log[0]))
            gamma = (Q(), Q())
            for n in range(20):
                d = 4*n+1
                gamma = add(gamma, scale(exp_integral(poly, Q(d, 2)), Q(-2, d)))
            total = add(add(pole, ct), add(prime, gamma))
            for label, independent in (('pole', pole), ('contact', ct), ('prime2', prime),
                                       ('Gamma_finite', gamma), ('moment', total)):
                observed = item[label]
                require(max(independent[0], observed[0]) <= min(independent[1], observed[1]),
                        ('independent source integral mismatch', j, k, label))
            records.append({'mode': j, 'moment': k, 'independent_interval': tuple(map(str, total)),
                            'production_interval': tuple(map(str, item['moment'])),
                            'all_signed_channels_overlap': True})
    loaded = {}
    for name, module in sorted(sys.modules.items()):
        if name == 'observational_succ' or name.startswith('observational_succ.'):
            path = Path(module.__file__).resolve()
            rel = str(path.relative_to(sibling))
            loaded[rel] = hashlib.sha256(probe.pinned_bytes(sibling, rel)).hexdigest()
    require(probe.verify_pin(sibling) == pin, 'pinned tree drift')
    return {'status': 'PASS_INDEPENDENT_SIGNED_SOURCE_MOMENT_INTEGRATION', 'gamma_modes': 20,
            'source_pin': pin, 'loaded_sibling_modules': loaded,
            'oracle': '200-term rational Taylor integral and proved remainder; production uses antiderivative recurrence',
            'records': records, 'endpoint_checks': endpoints,
            'independent_source_count': 1,
            'shared_dependencies': ['pinned source identity', 'log2/contact/sqrt2 source intervals',
                                    'inherited whole-high coercivity for later response bound'],
            'full_source_grid_recomputed': False, 'source_sign': 'OPEN'}


def spectral_receipt_audit(source_root=None):
    base = ROOT/'research/2026-10-16/collective_observer_receipts'
    path = base/'spectral-source.json'
    raw = path.read_bytes()
    data = json.loads(raw)['arithmetic_experiment']
    independent = json.loads((base/'audit-spectral-source-moments-v1.json').read_text())['sections']['spectral_source']
    require(independent['status'].startswith('PASS'), 'independent source moment run absent')
    require(data['source_pin'] == independent['source_pin'], 'source pins disagree')
    packet_name = 'research/2026-10-16/arithmetic_resonance_receipts/resolvent-final-py313-packet.json'
    sibling = Path(source_root).resolve() if source_root is not None else ROOT.parent/'SUCC-arithmetic-resonance'
    packet_bytes = (sibling/packet_name).read_bytes()
    require(hashlib.sha256(packet_bytes).hexdigest() == data['source_pin']['documents'][packet_name],
            'inherited upper packet hash mismatch')
    packet = json.loads(packet_bytes)
    require(data['fresh_derivative_cell_receipt']['gamma_modes'] == independent['gamma_modes'] == 20,
            'finite J mismatch')
    require(data['source_sign'] == 'OPEN' and not data['actual_source_negative_direction_found']
            and data['independent_source_count'] == 1, 'source/negative promotion')
    cols = data['projected_columns']
    for j, (col, row) in enumerate(zip(cols, data['exact_signed_derivative_moments']), 1):
        total, removed = Q(col['finite_J_energy_upper']), Q()
        for k, (lo, hi) in enumerate(col['projection_moment_intervals']):
            lo, hi = Q(lo), Q(hi)
            lower_abs = min(abs(lo), abs(hi)) if lo*hi > 0 else Q()
            removed += (2*k+1)*lower_abs**2
            checked = independent['records'][4*(j-1)+k]
            oracle = tuple(map(Q, checked['independent_interval']))
            source_interval = tuple(map(Q, row[k]['moment']))
            require(max(oracle[0], source_interval[0]) <= min(oracle[1], source_interval[1]),
                    ('source receipt moment drift', j, k))
            require(max(lo, oracle[0]) <= min(hi, oracle[1]), ('refined moment misses oracle', j, k))
        require(removed == Q(col['removed_polynomial_energy_lower']), ('removed sum', j))
        require(total-removed == Q(col['projected_energy_upper']) >= 0, ('subtraction', j))
    kappa = Q(data['fresh_derivative_cell_receipt']['kappa'])
    results = {}
    for name, modes in (('odd', (1, 3)), ('even', (2, 4))):
        out, sector = data['projected_response'][name], data['sectors'][name]
        trace = sum(((2*j+1)*Q(cols[j-1]['projected_energy_upper']) for j in modes), Q())
        root, eta = Q(out['trace_sqrt_upper']), Q(out['derivative_operator_tail'])
        require(root**2 >= trace == Q(out['projected_normalized_trace_upper']), 'directed square root')
        require(eta == Q(data['fresh_derivative_cell_receipt']['sectors'][name]['whole_Gamma_derivative_operator_tail']),
                'whole tail mismatch')
        cap = (root+eta)**2/kappa
        require(cap == Q(out['R0_operator_upper_cap']) == Q(sector['new_R0_cap']), 'tail once in norm')
        require(cap < Q(sector['old_R0_cap']), ('strict response improvement', name))
        groups = sector['intersection']['provenance_components']
        require(len(groups) == 1 and not sector['intersection']['independence_established'], 'source inflation')
        lower = sector['new_lower']
        c = Q(lower['lower_cap'])
        form = tuple(tuple(Q(data['improved_S0_lower_form'][i-1][j-1]) for j in modes) for i in modes)
        slack = tuple(tuple(form[i][j]-(c/Q(2*modes[i]+1) if i == j else 0)
                            for j in range(2)) for i in range(2))
        require(slack[0][1] == slack[1][0] and slack[0][0] >= 0 and slack[1][1] >= 0
                and slack[0][0]*slack[1][1] >= slack[0][1]**2, 'generalized lower PSD')
        require(slack == tuple(tuple(map(Q, r)) for r in lower['slack']), 'slack receipt drift')
        upper = Q(sector['unchanged_upper'])
        upper_slack = tuple(tuple((upper/Q(2*i+1) if i == j else 0)-Q(packet['exactupper'][i-1][j-1])
                                  for j in modes) for i in modes)
        require(upper_slack[0][1] == upper_slack[1][0] and min(upper_slack[0][0], upper_slack[1][1]) >= 0
                and upper_slack[0][0]*upper_slack[1][1] >= upper_slack[0][1]**2, 'upper scalar PSD')
        require(upper_slack == tuple(tuple(map(Q, row)) for row in sector['upper_slack']), 'upper slack drift')
        for j in modes:
            expected = Q(data['fresh_A_lower_form'][j-1][j-1])-cap/Q(2*j+1)
            require(expected == Q(data['improved_S0_lower_form'][j-1][j-1]), 'W form conversion')
        require(c < 0 < Q(sector['unchanged_upper']), 'expected sign-unresolved bracket')
        results[name] = {'new_response_cap': str(cap), 'old_response_cap': sector['old_R0_cap'],
                         'lower_cap': str(c), 'upper_cap': sector['unchanged_upper'], 'sign': 'OPEN'}
    for i in range(4):
        for j in range(4):
            if i != j:
                require(data['improved_S0_lower_form'][i][j] == data['fresh_A_lower_form'][i][j],
                        'off-diagonal form unexpectedly changed')
    failed = json.loads((base/'spectral-projection-grid512-failed.json').read_text())['arithmetic_experiment']
    require(all(Q(c['removed_polynomial_energy_lower']) == 0 for c in failed['projected_columns']),
            'historical zero-removal attempt missing')
    require(all(not c['strict_response_improvement'] for c in failed['sectors'].values()),
            'historical failed improvement relabeled')
    require(path.read_bytes() == raw, 'source receipt changed during audit')
    return {'status': 'PASS_SOURCE_RECEIPT_ARITHMETIC_WITH_INDEPENDENT_MOMENTS',
            'receipt_sha256': hashlib.sha256(raw).hexdigest(), 'source_pin': independent['source_pin']['commit'],
            'sectors': results, 'original_source_count': 1, 'historical_zero_removal_preserved': True,
            'unreplayed_dependencies': ['512-cell source grid was executed by spectral lane',
                                      'inherited high coercivity and analytic source proofs',
                                      'upper trial integration is inherited; lower/upper scalar slacks independently rechecked here']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        help='write JSON to this explicit path (parent must exist); JSON also goes to stdout')
    parser.add_argument('--source-root', type=Path, default=ROOT.parent/'SUCC-arithmetic-resonance',
                        help='pinned PR137 checkout for spectral_source and spectral_receipt sections')
    parser.add_argument('--sections', nargs='+', default=['modular', 'adaptive', 'ambient', 'parent140', 'effects', 'policy', 'gamma', 'spectral', 'spectral_projection'])
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
    resource.setrlimit(resource.RLIMIT_AS, (768*1024**2, 768*1024**2))
    sections = {'modular': modular_audit, 'adaptive': adaptive_quotient_audit,
                'ambient': ambient_audit, 'parent140': parent140_audit, 'effects': effects_audit,
                'policy': policy_audit, 'gamma': gamma_audit, 'spectral': spectral_audit,
                'spectral_projection': spectral_projection_audit,
                'spectral_source': lambda: spectral_source_moment_audit(args.source_root),
                'spectral_receipt': lambda: spectral_receipt_audit(args.source_root)}
    started = time.monotonic()
    def hashes():
        paths = sorted(set(ROOT.glob('observational_succ/collective_*.py')) |
                       {ROOT/'observational_succ/wild_embedding_succ.py',
                        ROOT/'observational_succ/wild_ambient_succ.py',
                        ROOT/'observational_succ/consensus_lambda.py', ROOT/'scripts/collective_spectral_probe.py',
                        Path(__file__).resolve()})
        return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    before = hashes()
    receipt = {'started_utc': datetime.now(timezone.utc).isoformat(), 'python': platform.python_version(),
               'command': sys.argv, 'source_root': str(args.source_root.resolve()),
               'source_sha256_before': before, 'sections': {},
               'limits': {'cpu_seconds': 90, 'address_space_MiB': 768, 'concurrency': 1}}
    failures = 0
    for name in args.sections:
        tick = time.monotonic()
        try:
            result = sections[name]()
        except Exception as exc:
            result = {'status': 'FAIL', 'error': type(exc).__name__, 'detail': str(exc)}
            failures += 1
        result['elapsed_seconds'] = round(time.monotonic()-tick, 4)
        receipt['sections'][name] = result
    try:
        receipt['source_sha256_after'] = hashes()
    except OSError as exc:
        receipt['source_sha256_after'] = {}
        receipt['source_snapshot_error'] = str(exc)
    receipt['sources_stable_during_run'] = before == receipt['source_sha256_after']
    receipt['source_changes'] = sorted(p for p in before.keys() | receipt['source_sha256_after'].keys()
                                       if before.get(p) != receipt['source_sha256_after'].get(p))
    receipt['elapsed_seconds'] = round(time.monotonic()-started, 4)
    receipt['exit_code'] = int(bool(failures) or not receipt['sources_stable_during_run'])
    receipt['status'] = ('FAIL_SOURCE_INSTABILITY' if not receipt['sources_stable_during_run']
                         else 'FAIL_SECTION' if failures else 'PASS')
    data = json.dumps(receipt, indent=2, sort_keys=True, default=str)+'\n'
    if args.output:
        dest = args.output.resolve()
        dest.write_text(data)
    print(data, end='')
    return receipt['exit_code']


if __name__ == '__main__':
    raise SystemExit(main())
