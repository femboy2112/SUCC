"""Exact hostile controls for the finite NO-GHOST certificate engine."""
import dataclasses
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.no_ghost import (
    Comparison, CouplingProblem, Event, FiniteContract, NoGhostError,
    RepairOption, Step, check_comparison, check_diamond,
    check_operational_weights, compose_maps, couple_contexts, enumerate_schedule,
    event_context_problem, joint_law, minimum_declared_repair, operational_equations, solve_nonnegative,
    three_coin_experiment, verify_diamond_failure, verify_dual,
    verify_higher_failure, verify_possible_history, verify_primal, verify_unavailable,
)


def odd_triangle():
    atoms = tuple(itertools.product((0, 1), repeat=3))
    restrictions = tuple(tuple((x[i], x[j]) for x in atoms)
                         for i, j in ((0, 1), (1, 2), (0, 2)))
    laws = ({(0, 1): Q(1, 2), (1, 0): Q(1, 2)},)*3
    return CouplingProblem(atoms, restrictions, laws)


def parity_diamond():
    """Same single-event marginals/endpoints, opposite pair correlations."""
    kernels = {}
    for a in ("a", "b"):
        kernels[((), a, "s", "ready")] = tuple(Step(z, "ready", z, Q(1, 2)) for z in (0, 1))
    for z in (0, 1):
        kernels[((('a', z),), 'b', 's', 'ready')] = (Step(z, 'ready', 'unit', Q(1)),)
        kernels[((('b', z),), 'a', 's', 'ready')] = (Step(1-z, 'ready', 'unit', Q(1)),)
    return FiniteContract('pair', 'bits', ('s',), ('ready',), {'ready': 0},
                          (Event('a'), Event('b')), (('s', 'ready', Q(1)),), kernels)


class ExactLinearTests(unittest.TestCase):
    def test_primal_exact_fraction(self):
        A, b = ((1, 1), (1, 0)), (1, Q(2, 7))
        r = solve_nonnegative(A, b)
        self.assertEqual(r.primal, (Q(2, 7), Q(5, 7)))
        self.assertTrue(verify_primal(A, b, r.primal))
        self.assertFalse(verify_primal(A, b, (Q(3, 7), Q(4, 7))))

    def test_linear_inconsistency_certificate(self):
        A, b = ((1, 1), (2, 2)), (1, 3)
        r = solve_nonnegative(A, b, max_bases=0)
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(A, b, r.dual))
        self.assertFalse(verify_dual(A, b, tuple(-x for x in r.dual)))

    def test_negative_unique_solution(self):
        A, b = ((1, 1), (1, 0)), (1, 2)
        r = solve_nonnegative(A, b)
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(A, b, r.dual))

    def test_zero_atom_universe(self):
        r = solve_nonnegative(((),), (1,))
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(((),), (1,), r.dual))

    def test_zero_equations_need_caller_normalization(self):
        r = solve_nonnegative(((0, 0),), (0,), max_bases=0)
        self.assertEqual(r.primal, (0, 0))

    def test_budget_is_unknown(self):
        r = solve_nonnegative(((1, 1),), (1,), max_bases=0)
        self.assertEqual(r.status, 'UNRESOLVED')
        self.assertIsNone(r.dual)

    def test_no_float_or_bool(self):
        for bad in (0.5, True):
            with self.assertRaises(NoGhostError):
                solve_nonnegative(((1, 1),), (bad,))

    def test_odd_triangle_farkas_and_mutation(self):
        problem = odd_triangle()
        A, b = problem.equations()
        r = couple_contexts(problem)
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(A, b, r.dual))
        # An independently supplied inequality: each bit triple has <=2
        # unequal pairs, whereas the requested contexts demand 3.
        y = [Q(2)]
        for labels in problem.restrictions:
            y.extend(-Q(int(x[0] != x[1])) for x in sorted(set(labels), key=repr))
        self.assertTrue(verify_dual(A, b, y))
        y[0] = Q(3)
        self.assertFalse(verify_dual(A, b, y))

    def test_positive_marginals(self):
        problem = odd_triangle()
        uniform = {(a, b): Q(1, 4) for a in (0, 1) for b in (0, 1)}
        problem = dataclasses.replace(problem, local_laws=(uniform,)*3)
        r = couple_contexts(problem)
        self.assertEqual(r.status, 'LAWFUL_GLUING')
        self.assertTrue(verify_primal(*problem.equations(), r.primal))

    def test_restriction_does_not_invent_excluded_atom(self):
        problem = CouplingProblem(('only_00', 'only_11'), ((0, 1), (0, 1)),
                                  ({0: Q(1)}, {1: Q(1)}))
        r = couple_contexts(problem)
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(*problem.equations(), r.dual))

    def test_solver_many_small_signed_systems(self):
        # Exhaustive hostile coefficient grid, not stochastic rounded LP checks.
        for row in itertools.product((-1, 0, 1), repeat=2):
            for rhs in range(-2, 3):
                A, b = ((1, 1), row), (1, rhs)
                r = solve_nonnegative(A, b)
                if r.primal is not None:
                    self.assertTrue(verify_primal(A, b, r.primal))
                else:
                    self.assertTrue(verify_dual(A, b, r.dual))


class CausalContractTests(unittest.TestCase):
    def test_three_coins_complete_law_schedules(self):
        model, fibers, _ = three_coin_experiment()
        self.assertEqual(len(fibers), 6)
        laws = [joint_law(atoms) for atoms in fibers.values()]
        self.assertTrue(all(law == laws[0] for law in laws))
        for atoms in fibers.values():
            self.assertEqual(len(atoms), 8)
            self.assertTrue(all(a.mass == Q(1, 8) for a in atoms))
        self.assertEqual(check_diamond(model, (), 'a', 'b', (('source', 'ready'),)).status,
                         'LAWFUL_GLUING')

    def test_same_marginals_endpoint_not_joint_law(self):
        model = parity_diamond()
        ab = enumerate_schedule(model, ('a', 'b')).atoms
        ba = enumerate_schedule(model, ('b', 'a')).atoms
        for event in ('a', 'b'):
            def marginal(atoms):
                return sum((x.mass for x in atoms if dict(x.public)[event] == 0), Q(0))
            self.assertEqual(marginal(ab), Q(1, 2))
            self.assertEqual(marginal(ba), Q(1, 2))
        self.assertEqual({x.current for x in ab+ba}, {'ready'})
        failure = check_diamond(model, (), 'a', 'b', (('s', 'ready'),))
        self.assertEqual(failure.status, 'CAUSAL_DIAMOND_FAILURE')
        self.assertTrue(verify_diamond_failure(model, (), failure.witness))
        bad = failure.witness[:-1]+(failure.witness[-2],)
        self.assertFalse(verify_diamond_failure(model, (), bad))

    def test_source_averaging_can_hide_dirac_diamond_failure(self):
        kernels = {}
        for s in (0, 1):
            kernels[((), 'a', s, 'ready')] = (Step(s, 'ready', 'unit', Q(1)),)
            kernels[((), 'b', s, 'ready')] = (Step(0, 'ready', 'unit', Q(1)),)
            kernels[((('a', s),), 'b', s, 'ready')] = (Step(0, 'ready', 'unit', Q(1)),)
            kernels[((('b', 0),), 'a', s, 'ready')] = (Step(1-s, 'ready', 'unit', Q(1)),)
        model = FiniteContract('mixed-source', 'bits', (0, 1), ('ready',), {'ready': 0},
                               (Event('a'), Event('b')),
                               ((0, 'ready', Q(1, 2)), (1, 'ready', Q(1, 2))), kernels)
        ab, ba = (enumerate_schedule(model, schedule).atoms for schedule in (('a', 'b'), ('b', 'a')))
        unindexed = lambda atoms: {tuple(sorted(x.public)): x.mass for x in atoms}
        self.assertEqual(unindexed(ab), unindexed(ba))
        self.assertNotEqual(joint_law(ab), joint_law(ba))
        self.assertEqual(check_diamond(model, (), 'a', 'b', ((0, 'ready'), (1, 'ready'))).status,
                         'CAUSAL_DIAMOND_FAILURE')

    def test_joint_law_diamond_does_not_imply_private_bijection(self):
        kernels = {
            ((), 'a', 's', 'ready'): (Step('tick', 'ready', 0, Q(1)),),
            ((('a', 'tick'),), 'b', 's', 'ready'): (Step('tick', 'ready', 0, Q(1)),),
            ((), 'b', 's', 'ready'): (Step('tick', 'ready', 0, Q(1, 2)), Step('tick', 'ready', 1, Q(1, 2))),
            ((('b', 'tick'),), 'a', 's', 'ready'): (Step('tick', 'ready', 0, Q(1)),),
        }
        model = FiniteContract('path-cardinality', 'bits', ('s',), ('ready',), {'ready': 0},
                               (Event('a'), Event('b')), (('s', 'ready', Q(1)),), kernels)
        ab, ba = (enumerate_schedule(model, schedule).atoms for schedule in (('a', 'b'), ('b', 'a')))
        self.assertEqual(check_diamond(model, (), 'a', 'b', (('s', 'ready'),)).status, 'LAWFUL_GLUING')
        self.assertEqual((len(ab), len(ba)), (1, 2))
        self.assertFalse(check_comparison(ab, ba, Comparison(('a', 'b'), ('b', 'a'), (0,))))

    def test_joint_law_diamond_does_not_preserve_future_menu(self):
        model, _, _ = three_coin_experiment()
        kernels = dict(model.kernels)
        del kernels[((('b', 'tick'), ('a', 'tick')), 'c', 'source', 'ready')]
        model = dataclasses.replace(model, kernels=kernels)
        self.assertEqual(check_diamond(model, (), 'a', 'b', (('source', 'ready'),)).status,
                         'LAWFUL_GLUING')
        self.assertEqual(enumerate_schedule(model, ('a', 'b', 'c')).status, 'LAWFUL_GLUING')
        self.assertEqual(enumerate_schedule(model, ('b', 'a', 'c')).status, 'SOURCE_INTERFACE_FAILURE')

    def test_destructive_measurements_unavailable(self):
        kernels = {((), a, 's', 'fresh'): (Step('ok', 'spent', 'unit', Q(1)),)
                   for a in ('a', 'b')}
        model = FiniteContract('destructive', 'resource', ('s',), ('fresh', 'spent'),
                               {'fresh': 0, 'spent': 1}, (Event('a'), Event('b')),
                               (('s', 'fresh', Q(1)),), kernels)
        for schedule in (('a', 'b'), ('b', 'a')):
            result = enumerate_schedule(model, schedule)
            self.assertEqual(result.status, 'SOURCE_INTERFACE_FAILURE')
            self.assertIn('EXECUTABILITY_FAILURE', result.reason)
            self.assertTrue(verify_unavailable(model, schedule, result.witness))
        self.assertEqual(check_diamond(model, (), 'a', 'b', (('s', 'fresh'),)).status,
                         'SOURCE_INTERFACE_FAILURE')

    def test_hidden_source_cannot_choose_action(self):
        model = FiniteContract('mixed', 'basis', ('s0', 's1'), ('ready',), {'ready': 0},
                               (Event('a'),), (('s0', 'ready', Q(1, 2)), ('s1', 'ready', Q(1, 2))),
                               {((), 'a', 's0', 'ready'): (Step('ok', 'ready', 0, Q(1)),)})
        r = enumerate_schedule(model, ('a',))
        self.assertEqual(r.status, 'SOURCE_INTERFACE_FAILURE')
        self.assertTrue(verify_unavailable(model, ('a',), r.witness))

    def test_dependencies_and_occurrences_are_not_optional(self):
        model, _, _ = three_coin_experiment()
        for schedule in (('a', 'a', 'c'), ('a', 'b')):
            with self.assertRaises(NoGhostError):
                enumerate_schedule(model, schedule)
        cyclic = dataclasses.replace(model, events=(Event('a', frozenset({'b'})), Event('b', frozenset({'a'})), Event('c')))
        with self.assertRaises(NoGhostError):
            cyclic.validate()

    def test_missing_kernel_probability_is_not_silent_loss(self):
        model, _, _ = three_coin_experiment()
        kernels = dict(model.kernels)
        key = next(iter(kernels))
        kernels[key] = (Step('tick', 'ready', 0, Q(1, 2)),)
        with self.assertRaises(NoGhostError):
            dataclasses.replace(model, kernels=kernels).validate()

    def test_source_label_cannot_be_rewritten(self):
        model, _, _ = three_coin_experiment()
        kernels = dict(model.kernels)
        key = ((), 'a', 'invented', 'ready')
        kernels[key] = (Step('tick', 'ready', 0, Q(1)),)
        with self.assertRaises(NoGhostError):
            dataclasses.replace(model, kernels=kernels).validate()

    def test_epoch_cannot_decrease(self):
        model = FiniteContract('epoch', 'basis', ('s',), ('late', 'early'),
                               {'late': 2, 'early': 1}, (Event('a'),), (('s', 'late', Q(1)),),
                               {((), 'a', 's', 'late'): (Step('ok', 'early', 0, Q(1)),)})
        with self.assertRaises(NoGhostError):
            model.validate()

    def test_enumeration_budget_does_not_refute_execution(self):
        model, _, _ = three_coin_experiment()
        r = enumerate_schedule(model, ('a', 'b', 'c'), max_atoms=3)
        self.assertEqual(r.status, 'UNRESOLVED')
        self.assertEqual(r.atoms, ())

    def test_access_verifier_rejects_undeclared_event_request(self):
        model, _, _ = three_coin_experiment()
        self.assertFalse(verify_unavailable(model, ('NOT_DECLARED',),
                                            ((), 'NOT_DECLARED', 'source', 'ready')))
        with self.assertRaises(NoGhostError):
            check_diamond(model, (), 'NOT_DECLARED', 'b', (('source', 'ready'),))


class CoherenceAndOperationalTests(unittest.TestCase):
    def test_lawful_chosen_private_maps_fail_braid(self):
        _, fibers, result = three_coin_experiment()
        bad, good = result['incoherent'], result['coherent']
        self.assertEqual(bad['status'], 'HIGHER_COHERENCE_FAILURE')
        self.assertTrue(bad['failures'])
        witness = next(i for i, x in enumerate(fibers[('a', 'b', 'c')])
                       if tuple(e.branch for e in x.events) == (0, 1, 0))
        self.assertTrue(verify_higher_failure(bad['left_maps'], bad['right_maps'], witness))
        self.assertFalse(verify_higher_failure(good['left_maps'], good['right_maps'], witness))
        self.assertEqual(good['status'], 'LAWFUL_GLUING')
        self.assertEqual(good['left'], good['right'])
        for maps in (bad['left_maps'], bad['right_maps']):
            for mapping in maps:
                self.assertEqual(compose_maps(mapping, mapping), tuple(range(8)))

    def test_comparison_preserves_source_and_public_evidence(self):
        _, fibers, _ = three_coin_experiment()
        source = fibers[('a', 'b', 'c')]
        target = fibers[('b', 'a', 'c')]
        comp = Comparison(('a', 'b', 'c'), ('b', 'a', 'c'), tuple(range(8)))
        self.assertTrue(check_comparison(source, target, comp))
        mutated = (dataclasses.replace(target[0], source='fake'),)+target[1:]
        self.assertFalse(check_comparison(source, mutated, comp))
        self.assertFalse(check_comparison(source, target, dataclasses.replace(comp, mapping=(0,)*8)))
        for field in ('source_id', 'basis'):
            foreign = tuple(dataclasses.replace(x, **{field: 'unrelated'}) for x in target)
            self.assertFalse(check_comparison(source, foreign, comp))

    def test_coherence_verifier_rejects_nonmaps_and_boolean_images(self):
        self.assertFalse(verify_higher_failure(((0,),), ((1000000,),), 0))
        self.assertFalse(verify_higher_failure(((0, 1),), ((True, False),), 0))
        self.assertFalse(verify_higher_failure(((0, 1),), ((0, 0),), 0))
        self.assertFalse(verify_higher_failure(((0, 1),), ((1, 0, 2),), 0))
        self.assertFalse(verify_higher_failure(((0, 1),), ((1, 0),), True))

    def test_support_coupling_is_not_operational_law(self):
        model = FiniteContract('fair-coin', 'bits', ('s',), ('ready',), {'ready': 0},
                               (Event('flip'),), (('s', 'ready', Q(1)),),
                               {((), 'flip', 's', 'ready'): (Step(0, 'ready', 0, Q(1, 2)), Step(1, 'ready', 1, Q(1, 2)))})
        atoms = enumerate_schedule(model, ('flip',)).atoms
        problem = CouplingProblem(tuple(x.identity for x in atoms), ((0, 1),),
                                  ({0: Q(3, 4), 1: Q(1, 4)},))
        supported = couple_contexts(problem)
        self.assertEqual(supported.status, 'LAWFUL_GLUING')
        self.assertEqual(supported.primal, (Q(3, 4), Q(1, 4)))
        self.assertFalse(check_operational_weights(model, ('flip',), atoms, supported.primal))
        self.assertTrue(check_operational_weights(model, ('flip',), atoms, (Q(1, 2), Q(1, 2))))
        support_A, support_b = problem.equations()
        flow_A, flow_b = operational_equations(model, ('flip',), atoms)
        r = solve_nonnegative(support_A+flow_A, support_b+flow_b)
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(support_A+flow_A, support_b+flow_b, r.dual))

    def test_operational_flow_unique_even_when_public_outcomes_silent(self):
        model, fibers, _ = three_coin_experiment()
        atoms = fibers[('a', 'b', 'c')]
        r = solve_nonnegative(*operational_equations(model, ('a', 'b', 'c'), atoms))
        self.assertEqual(r.primal, (Q(1, 8),)*8)
        self.assertFalse(check_operational_weights(model, ('a', 'b', 'c'), atoms, (Q(1),)+(Q(0),)*7))

    def test_operational_flow_rejects_atom_omission_and_forgery(self):
        model, fibers, _ = three_coin_experiment()
        atoms = fibers[('a', 'b', 'c')]
        with self.assertRaises(NoGhostError):
            operational_equations(model, ('a', 'b', 'c'), atoms[:-1])
        fake = (dataclasses.replace(atoms[0], source='invented'),)+atoms[1:]
        with self.assertRaises(NoGhostError):
            operational_equations(model, ('a', 'b', 'c'), fake)
        for field, value in (('current', 'fake'), ('mass', Q(1))):
            fake = (dataclasses.replace(atoms[0], **{field: value}),)+atoms[1:]
            with self.assertRaises(NoGhostError):
                operational_equations(model, ('a', 'b', 'c'), fake)

    def test_independent_possible_history_verifier(self):
        model, fibers, _ = three_coin_experiment()
        atom = fibers[('a', 'b', 'c')][0]
        self.assertTrue(verify_possible_history(model, ('a', 'b', 'c'), atom))
        for field, value in (('current', 'fake'), ('mass', Q(1)), ('source', 'invented'),
                             ('source_id', 'unrelated'), ('basis', 'foreign')):
            self.assertFalse(verify_possible_history(model, ('a', 'b', 'c'), dataclasses.replace(atom, **{field: value})))
        fake_event = dataclasses.replace(atom.events[0], branch=7)
        self.assertFalse(verify_possible_history(model, ('a', 'b', 'c'),
                                                dataclasses.replace(atom, events=(fake_event,)+atom.events[1:])))

    def test_contexts_project_only_recorded_occurrences(self):
        model, _, _ = three_coin_experiment()
        execution = enumerate_schedule(model, ('a', 'b', 'c'))
        problem = event_context_problem(execution, (('a', 'c'),), ({('tick', 'tick'): Q(1)},))
        self.assertEqual(couple_contexts(problem).status, 'LAWFUL_GLUING')
        with self.assertRaises(NoGhostError):
            event_context_problem(execution, (('unperformed',),), ({('tick',): Q(1)},))
        source_problem = event_context_problem(execution, (('b',),),
                                               ({('source', ('tick',)): Q(1)},), source_indexed=True)
        self.assertEqual(couple_contexts(source_problem).status, 'LAWFUL_GLUING')


class RepairMenuTests(unittest.TestCase):
    def test_finite_optimum_can_tie(self):
        bad = RepairOption('no-repair', Q(0), ((Q(1),),), (Q(-1),))
        left = RepairOption('retain-left', Q(1), ((Q(1),),), (Q(1),))
        right = RepairOption('retain-right', Q(1), ((Q(1),),), (Q(1),))
        r = minimum_declared_repair((bad, left, right), budget=2)
        self.assertEqual(r.status, 'REPAIR_CERTIFIED')
        self.assertEqual(r.minimum_cost, 1)
        self.assertEqual(set(r.options), {'retain-left', 'retain-right'})
        self.assertTrue(verify_dual(bad.A, bad.b, dict(r.results)['no-repair'].dual))

    def test_budget_failure_is_only_a_menu_claim(self):
        good = RepairOption('costly', Q(2), ((Q(1),),), (Q(1),))
        r = minimum_declared_repair((good,), budget=1)
        self.assertEqual(r.status, 'UNRESOLVED')
        self.assertIn('CERTIFIED_FINITE_MENU_EXHAUSTION', r.reason)

    def test_incomplete_repair_search_no_minimality_claim(self):
        item = RepairOption('unknown', Q(1), ((Q(1),),), (Q(1),))
        self.assertEqual(minimum_declared_repair((item,), budget=1, max_bases=0).status, 'UNRESOLVED')


if __name__ == '__main__':
    unittest.main()
