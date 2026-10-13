"""Independent hostile policy-vs-path-support tests, all exact rational."""
import dataclasses
import unittest
from fractions import Fraction as Q

from observational_succ.no_ghost import (
    CouplingProblem, Event, FiniteContract, NoGhostError, Step,
    couple_contexts, verify_dual, verify_primal,
)
from observational_succ.no_ghost_policy import (
    compile_public_policy, operational_coupling, replay_public_policy,
    verify_policy_obstruction, verify_policy_solution,
)


def hidden_guess_contract(*, licensed_read=False):
    sources = (0, 1)
    events = (Event('guess0'), Event('guess1'))
    kernels = {}
    for s in sources:
        for guess in (0, 1):
            kernels[((), 'guess'+str(guess), s, 'ready')] = (
                Step(int(s == guess), 'ready', 'unit', Q(1)),)
    if licensed_read:
        events += (Event('read'),)
        for s in sources:
            kernels[((), 'read', s, 'ready')] = (Step(s, 'ready', 'unit', Q(1)),)
            for guess in (0, 1):
                kernels[((('read', s),), 'guess'+str(guess), s, 'ready')] = (
                    Step(int(s == guess), 'ready', 'unit', Q(1)),)
    return FiniteContract('hidden-fair-source', 'bit-label', sources, ('ready',),
                          {'ready': 0}, events,
                          ((0, 'ready', Q(1, 2)), (1, 'ready', Q(1, 2))), kernels)


class PublicPolicyTests(unittest.TestCase):
    def setUp(self):
        self.model = hidden_guess_contract()
        result = compile_public_policy(self.model, 1)
        self.assertEqual(result.status, 'COMPILED')
        self.system = result.system
        self.labels = (tuple(a.events[-1].outcome for a in self.system.atoms),
                       tuple(a.source for a in self.system.atoms))

    def test_legal_support_and_prior_do_not_authorize_oracle(self):
        laws = ({1: Q(1)}, {0: Q(1, 2), 1: Q(1, 2)})
        support = CouplingProblem(tuple(a.identity for a in self.system.atoms), self.labels, laws)
        r = couple_contexts(support)
        self.assertEqual(r.status, 'LAWFUL_GLUING')
        self.assertTrue(verify_primal(*support.equations(), r.primal))
        actual = operational_coupling(self.system, self.labels, laws)
        self.assertEqual(actual.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(*self.system.equations(self.labels, laws), actual.dual))
        self.assertTrue(verify_policy_obstruction(self.model, 1, self.labels, laws, actual.dual))
        self.assertFalse(verify_dual(*self.system.equations(self.labels, laws),
                                     tuple(-y for y in actual.dual)))

    def test_public_half_success_reconstructs_and_independently_replays(self):
        laws = ({0: Q(1, 2), 1: Q(1, 2)}, {0: Q(1, 2), 1: Q(1, 2)})
        r = operational_coupling(self.system, self.labels, laws)
        self.assertEqual(r.status, 'LAWFUL_GLUING')
        policy = self.system.policy(r.primal)
        actual = replay_public_policy(self.model, 1, policy)
        predicted = dict(zip((a.identity for a in self.system.atoms), self.system.weights(r.primal)))
        self.assertEqual(actual, {k: v for k, v in predicted.items() if v})
        self.assertEqual(sum(actual.values()), 1)
        self.assertTrue(verify_policy_solution(self.model, self.system, r.primal, self.labels, laws))

    def test_compiled_metadata_is_not_a_certificate_authority(self):
        laws = ({0: Q(1, 2), 1: Q(1, 2)}, {0: Q(1, 2), 1: Q(1, 2)})
        r = operational_coupling(self.system, self.labels, laws)
        doubled = dataclasses.replace(self.system, atoms=tuple(
            dataclasses.replace(a, mass=2*a.mass) for a in self.system.atoms))
        self.assertFalse(verify_policy_solution(self.model, doubled, r.primal, self.labels, laws))
        foreign = dataclasses.replace(self.system, source_id='foreign')
        self.assertFalse(verify_policy_solution(self.model, foreign, r.primal, self.labels, laws))
        self.assertFalse(verify_policy_solution(self.model, self.system, r.primal, self.labels, laws,
                                               max_prefixes=0))

    def test_dual_rechecks_actual_source_model_not_supplied_matrix(self):
        laws = ({1: Q(1)}, {0: Q(1, 2), 1: Q(1, 2)})
        r = operational_coupling(self.system, self.labels, laws)
        self.assertFalse(verify_policy_obstruction(self.model, 1, self.labels, laws,
                                                   tuple(-x for x in r.dual)))
        self.assertFalse(verify_policy_obstruction(self.model, 1, self.labels, laws, r.dual,
                                                   max_prefixes=0))

    def test_all_blind_mixtures_have_exact_half_success(self):
        for q in (Q(0), Q(1, 7), Q(1, 2), Q(5, 7), Q(1)):
            actual = replay_public_policy(self.model, 1, {(): {'guess0': q, 'guess1': 1-q}})
            success = sum((mass for identity, mass in actual.items()
                           if identity[-1][-1].outcome == 1), Q(0))
            self.assertEqual(success, Q(1, 2))

    def test_explicitly_licensed_read_enables_source_blind_adaptive_success(self):
        model = hidden_guess_contract(licensed_read=True)
        system = compile_public_policy(model, 2).system
        labels = (tuple(a.events[-1].outcome for a in system.atoms),)
        result = operational_coupling(system, labels, ({1: Q(1)},))
        self.assertEqual(result.status, 'LAWFUL_GLUING')
        policy = system.policy(result.primal)
        self.assertEqual(policy[()]['read'], 1)
        self.assertEqual(policy[(('read', 0),)]['guess0'], 1)
        self.assertEqual(policy[(('read', 1),)]['guess1'], 1)
        actual = replay_public_policy(model, 2, policy)
        self.assertEqual(sum(actual.values()), 1)
        self.assertTrue(all(identity[-1][-1].outcome == 1 for identity in actual))

    def test_forced_dead_end_cannot_be_postselected(self):
        system = compile_public_policy(self.model, 2).system
        self.assertFalse(system.atoms)
        r = operational_coupling(system, (), ())
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(*system.equations((), ()), r.dual))

    def test_partial_chance_dead_end_blocks_whole_action(self):
        model = FiniteContract('dead-end', 'bit', ('s',), ('ready',), {'ready': 0},
                              (Event('a'), Event('b', frozenset({'a'}))),
                              (('s', 'ready', Q(1)),),
                              {((), 'a', 's', 'ready'): (Step(0, 'ready', 0, Q(1, 2)),
                                                          Step(1, 'ready', 1, Q(1, 2))),
                               ((('a', 0),), 'b', 's', 'ready'): (Step('ok', 'ready', 0, Q(1)),)})
        system = compile_public_policy(model, 2).system
        r = operational_coupling(system, (), ())
        self.assertEqual(r.status, 'PROBABILITY_COUPLING_FAILURE')
        self.assertTrue(verify_dual(*system.equations((), ()), r.dual))

    def test_hidden_enabledness_excluded_from_public_menu(self):
        kernels = dict(self.model.kernels)
        del kernels[((), 'guess0', 1, 'ready')]
        model = dataclasses.replace(self.model, kernels=kernels)
        system = compile_public_policy(model, 1).system
        self.assertEqual(system.menus[()], ('guess1',))
        with self.assertRaises(NoGhostError):
            replay_public_policy(model, 1, {(): {'guess0': Q(1)}})

    def test_zero_horizon_preserves_preparation(self):
        system = compile_public_policy(self.model, 0).system
        result = operational_coupling(system, (), ())
        self.assertEqual(result.status, 'LAWFUL_GLUING')
        self.assertEqual(system.weights(result.primal), (Q(1, 2), Q(1, 2)))

    def test_bounded_compilation_never_false_negative(self):
        self.assertEqual(compile_public_policy(self.model, 1, max_prefixes=1).status, 'UNRESOLVED')
        self.assertEqual(compile_public_policy(self.model, 1, max_prefixes=3).status, 'UNRESOLVED')
        result = operational_coupling(self.system, (), (), max_bases=0)
        self.assertEqual(result.status, 'UNRESOLVED')

    def test_invalid_plans_policies_horizons_rejected(self):
        with self.assertRaises(NoGhostError):
            self.system.weights([Q(0)] * len(self.system.variables))
        for h in (-1, 3, True, 1.0):
            with self.assertRaises(NoGhostError):
                compile_public_policy(self.model, h)
        for policy in ({(): {'guess0': 0.5, 'guess1': 0.5}},
                       {(): {'guess0': 2, 'guess1': -1}},
                       {(): {'secret': 1}}):
            with self.assertRaises(NoGhostError):
                replay_public_policy(self.model, 1, policy)


if __name__ == '__main__':
    unittest.main()
