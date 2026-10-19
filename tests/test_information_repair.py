"""Exact repair, destructive identification, and independent policy enumeration."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from random import Random

from observational_succ.future_safe_quotient import Machine, State, Edge
from observational_succ.information_repair import (
    RepairError, ProbeEdge, Acquisition, stable_repair, check_repair,
    partitions, goal, branches, solve_acquisition, check_acquisition,
    advice_at_budget, advice_frontier,
)


def destructive_example(escape=False):
    carriers = ('x', 'y', 'z', 'u', 'v')
    edges = [ProbeEdge('x', 'a', 'x', 'alone', Q(1)),
             ProbeEdge('y', 'a', 'u', 'merged', Q(1)),
             ProbeEdge('z', 'a', 'u', 'merged', Q(1)),
             ProbeEdge('x', 'b', 'v', 'merged', Q(1)),
             ProbeEdge('y', 'b', 'v', 'merged', Q(1)),
             ProbeEdge('z', 'b', 'z', 'alone', Q(1))]
    actions = ('a', 'b') + (('reveal',) if escape else ())
    for carrier in ('u', 'v'):
        for a in actions:
            edges.append(ProbeEdge(carrier, a, carrier, 'destroyed', Q(0)))
    if escape:
        for x in ('x', 'y', 'z'):
            edges.append(ProbeEdge(x, 'reveal', x, x, Q(2)))
    return Acquisition(carriers, actions, tuple(edges), ('x', 'y', 'z'),
                       ('x', 'y', 'z'), ('X', 'Y', 'Z'), ('q', 'q', 'q'))


def independent_policy_oracle(problem, cert, initial):
    """Enumerate stationary policies, simulate every fixed ORIGINAL source.

    No production Bellman recurrence, branches, goal or rank checker is used.
    """
    targets = dict(zip(problem.origins, problem.target))
    table = {(e.start, e.action): e for e in problem.edges}
    pending = [b for b in cert.beliefs if len({targets[x] for x, _ in b}) > 1]
    options = [tuple(a for a in problem.actions if all((s, a) in table for _, s in b))
               or (None,) for b in pending]
    best = None
    for choices in product(*options):
        policy = dict(zip(pending, choices))
        costs = []
        for actual, _ in initial:
            b, paid, visited = initial, Q(0), set()
            while len({targets[x] for x, _ in b}) > 1:
                if b in visited or policy[b] is None:
                    break
                visited.add(b)
                a = policy[b]
                actual_current = dict(b)[actual]
                observed = table[actual_current, a]
                paid += observed.cost
                b = tuple(sorted((x, table[s, a].target) for x, s in b
                                 if (table[s, a].receipt, table[s, a].cost) ==
                                    (observed.receipt, observed.cost)))
            else:
                costs.append(paid)
                continue
            break
        if len(costs) == len(initial):
            candidate = max(costs)
            best = candidate if best is None else min(best, candidate)
    return best


class TestInformationRepair(unittest.TestCase):
    def test_auxiliary_labels_reused_across_q_fibers(self):
        m = Machine(tuple(State(str(i), 'S', str(i % 3)) for i in range(6)), (), ())
        q = ('left',)*3 + ('right',)*3
        repair = stable_repair(m, q)
        self.assertTrue(check_repair(m, q, repair))
        self.assertEqual((repair.labels, repair.bits), (3, 2))
        self.assertEqual(repair.auxiliary, (0, 1, 2, 0, 1, 2))
        with self.assertRaises(RepairError):
            check_repair(m, q, replace(repair, bits=1))

    def test_refinement_must_propagate_preexisting_q_splits(self):
        m = Machine(tuple(State(x, 'S', 'same') for x in ('u', 'v', 'w')), ('a',),
                    (Edge('u', 'a', 'u', Q(0)), Edge('v', 'a', 'w', Q(0)),
                     Edge('w', 'a', 'w', Q(0))))
        repair = stable_repair(m, ('zero', 'zero', 'one'))
        self.assertEqual(repair.quotient.blocks, (('u',), ('v',), ('w',)))
        self.assertEqual((repair.labels, repair.bits), (2, 1))

    def test_repair_minimality_against_all_partitions_on_fresh_models(self):
        rng = Random(202610194307)
        for _ in range(160):
            states = tuple(State(str(i), 'S', str(rng.randrange(2))) for i in range(4))
            edges = tuple(Edge(str(i), 'a', str(rng.randrange(4)), Q(rng.randrange(3), 2))
                          for i in range(4) if rng.randrange(4))
            m = Machine(states, ('a',), edges)
            q = tuple(str(rng.randrange(2)) for _ in states)
            repair = stable_repair(m, q)
            self.assertTrue(check_repair(m, q, repair))
            table = {(e.start, e.action): e for e in edges}
            valid = []
            for p in partitions(tuple(s.name for s in states)):
                label = {s: i for i, b in enumerate(p) for s in b}
                okay = True
                for b in p:
                    signatures = set()
                    for s in b:
                        e = table.get((s, 'a'))
                        signatures.add((q[int(s)], states[int(s)].output(),
                                        None if e is None else (e.cost, label[e.target])))
                    okay &= len(signatures) == 1
                if okay:
                    valid.append(p)
            self.assertEqual(len(repair.quotient.blocks), min(map(len, valid)))
            for colors in range(1, repair.labels):
                self.assertFalse(any(
                    all(q[int(x)] != q[int(y)] or code[int(x)] != code[int(y)]
                        for i, a in enumerate(repair.quotient.blocks)
                        for b in repair.quotient.blocks[i+1:] for x in a for y in b)
                    for code in product(range(colors), repeat=4)))

    def test_pairwise_diagnosis_does_not_give_one_joint_policy(self):
        p = destructive_example()
        cert = solve_acquisition(p)
        self.assertTrue(check_acquisition(p, cert))
        values = dict(zip(cert.beliefs, cert.values))
        for subset in (('x', 'y'), ('x', 'z'), ('y', 'z')):
            self.assertEqual(values[p.start(subset)], Q(1))
        self.assertIsNone(values[p.start(p.origins)])
        point = advice_at_budget(p, cert, Q(1))
        self.assertEqual(point['minimal_infeasible'], (('x', 'y', 'z'),))
        self.assertEqual((point['labels'], point['advice_bits']), (2, 1))

    def test_sharp_advice_cost_frontier_and_original_target_survives_destruction(self):
        p = destructive_example(True)
        self.assertEqual([(x['advice_bits'], x['budget']) for x in advice_frontier(p)],
                         [(2, Q(0)), (1, Q(1)), (0, Q(2))])
        cert = solve_acquisition(p)
        destroyed = (('y', 'u'), ('z', 'u'))
        self.assertIsNone(dict(zip(cert.beliefs, cert.values))[destroyed])
        # A CURRENT-state target would falsely call the merged carrier resolved.
        self.assertEqual(len({carrier for _, carrier in destroyed}), 1)
        self.assertFalse(goal(p, destroyed))

    def test_safe_lawfulness_forbids_probe_enabled_at_only_one_hypothesis(self):
        p = Acquisition(('s', 't'), ('a',), (ProbeEdge('s', 'a', 's', 'yes', Q(0)),),
                        ('x', 'y'), ('s', 't'), ('X', 'Y'), ('q', 'q'))
        b = p.start(p.origins)
        self.assertIsNone(branches(p, b, 'a'))
        self.assertIsNone(solve_acquisition(p, (b,)).values[0])

    def test_zero_cost_loop_cannot_forge_terminating_success(self):
        p = Acquisition(('s', 't'), ('loop',),
                        (ProbeEdge('s', 'loop', 's', 'same', Q(0)),
                         ProbeEdge('t', 'loop', 't', 'same', Q(0))),
                        ('x', 'y'), ('s', 't'), ('X', 'Y'), ('q', 'q'))
        b = p.start(p.origins)
        cert = solve_acquisition(p, (b,))
        self.assertEqual(cert.values, (None,))
        self.assertTrue(check_acquisition(p, cert))
        forged = replace(cert, values=(Q(0),), policy=('loop',), ranks=(1,))
        with self.assertRaisesRegex(RepairError, 'rank'):
            check_acquisition(p, forged)

    def test_exact_fractional_costs_and_cost_receipts(self):
        p = Acquisition(('s', 't'), ('a',),
                        (ProbeEdge('s', 'a', 's', 'same', Q(1, 3)),
                         ProbeEdge('t', 'a', 't', 'same', Q(1, 2))),
                        ('x', 'y'), ('s', 't'), ('X', 'Y'), ('q', 'q'))
        b = p.start(p.origins)
        cert = solve_acquisition(p, (b,))
        self.assertEqual(dict(zip(cert.beliefs, cert.values))[b], Q(1, 2))
        self.assertTrue(check_acquisition(p, cert))

    def test_independent_policy_enumeration_holdouts(self):
        rng = Random(202610196109)
        for _ in range(90):
            edges = tuple(ProbeEdge(s, a, rng.choice(('s', 't')), str(rng.randrange(2)),
                                    Q(rng.randrange(3), 2))
                          for s, a in product(('s', 't'), ('a', 'b')) if rng.randrange(4))
            p = Acquisition(('s', 't'), ('a', 'b'), edges,
                            ('x', 'y'), ('s', 't'), ('X', 'Y'), ('q', 'q'))
            b = p.start(p.origins)
            cert = solve_acquisition(p, (b,))
            self.assertTrue(check_acquisition(p, cert))
            self.assertEqual(dict(zip(cert.beliefs, cert.values))[b],
                             independent_policy_oracle(p, cert, b))

    def test_cost_and_policy_mutations_are_rejected(self):
        p = destructive_example(True)
        cert = solve_acquisition(p)
        i = cert.beliefs.index(p.start(p.origins))
        for wrong in (Q(0), Q(3), None):
            values = list(cert.values)
            values[i] = wrong
            with self.assertRaises(RepairError):
                check_acquisition(p, replace(cert, values=tuple(values)))
        with self.assertRaises(RepairError):
            solve_acquisition(p, max_beliefs=1)
        with self.assertRaises(RepairError):
            Acquisition(('s',), ('a',), (ProbeEdge('s', 'a', 's', '', 0.1),),
                        ('x',), ('s',), ('X',), ('q',))


if __name__ == '__main__':
    unittest.main()
