"""Exact regression and hostile controls for the lawful-probe budget theorem forge."""
from __future__ import annotations

import itertools
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

# Allows isolated local execution without representing a full SUCC checkout.
root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from observational_succ.probe_budget import (
    Probe, Carrier, Quotient, Noncongruence, refined_quotient,
    minimum_fixed_budget, minimum_adaptive_budget, minimum_section_budget,
    stochastic_lift, point_lift, verify_point, verify_kernel,
    verify_adaptive_solution, target_unresolved_pairs,
)


def binary_split_carrier():
    return Carrier(
        (0,0,0,0), (tuple(range(4)),),
        (Probe('group', (0,0,1,1), Q(1)),
         Probe('A_detail', (0,1,0,0), Q(1)),
         Probe('B_detail', (0,0,0,1), Q(1))))


def stage_carrier(probes=True):
    # Twin u-predecessors -> twin v-predecessors -> swapping terminal w-fiber.
    # Base q merges v with w: no exact stochastic section. Marking the
    # middle pair produces a stochastic-only section; separating all three
    # source pairs yields a deterministic equivariant section.
    return Carrier((0,0,1,1,1,1), ((2,3,4,5,5,4),),
                   (Probe('middle_pair',(0,0,1,1,0,0),Q(2)),
                    Probe('within_pair',(0,1,0,1,0,1),Q(3))) if probes else ())


class ProbeBudgetTests(unittest.TestCase):
    def test_fixed_weighted_pair_cover_full_identification(self):
        m=binary_split_carrier()
        r=minimum_fixed_budget(m,tuple(range(4)))
        self.assertEqual((r.cost,r.indices),(Q(3),(0,1,2)))
        self.assertEqual(len(target_unresolved_pairs(m,tuple(range(4)))),6)
        self.assertIsNone(minimum_fixed_budget(
            Carrier(m.q,m.source_actions,m.probes[:2]),tuple(range(4))))

    def test_target_relative_cost_lower_than_source_id(self):
        m=binary_split_carrier()
        r=minimum_fixed_budget(m,(0,0,1,1))
        self.assertEqual((r.cost,r.indices),(Q(1),(0,)))
        self.assertEqual(minimum_fixed_budget(m,(9,9,9,9)).cost,Q(0))

    def test_adaptive_tree_beats_fixed_with_exact_certificate(self):
        m=binary_split_carrier()
        s=minimum_adaptive_budget(m,tuple(range(4)))
        self.assertEqual(s.worst_cost,Q(2))
        self.assertTrue(verify_adaptive_solution(m,s))
        self.assertEqual(minimum_fixed_budget(m,tuple(range(4))).cost,Q(3))

    def test_adaptive_target_relative_and_known_initial_report(self):
        m=binary_split_carrier()
        s=minimum_adaptive_budget(m,(0,0,1,1))
        self.assertEqual(s.worst_cost,Q(1))
        self.assertTrue(verify_adaptive_solution(m,s))
        m2=Carrier((0,0,1,1),m.source_actions,m.probes)
        s2=minimum_adaptive_budget(m2,(0,0,1,1))
        self.assertEqual(s2.worst_cost,Q(0))
        self.assertTrue(verify_adaptive_solution(m2,s2))

    def test_explicit_lawful_menu_does_not_invent_identity_oracle(self):
        model=Carrier((0,0,0),((0,1,2),),
                      (Probe('unavailable_hidden_id',(0,1,2),Q(1),available=False),
                       Probe('real_bit',(0,0,1),Q(4))))
        self.assertIsNone(minimum_fixed_budget(model,(0,1,2)))
        self.assertIsNone(minimum_adaptive_budget(model,(0,1,2)).worst_cost)
        # Distinguish ordinary equivariant selection from ACTUAL identification:
        # identity dynamics allow a point representative without revealing which
        # of the three current source states was really prepared.
        self.assertEqual(minimum_section_budget(model,'point').cost,Q(0))

    def test_oracle_available_as_model_is_not_physical_authentication(self):
        model=Carrier((0,0,0),((0,1,2),),
                      (Probe('source_ID',(0,1,2),Q(5),available=True),))
        r=minimum_fixed_budget(model,(0,1,2))
        self.assertEqual((r.cost,r.indices),(Q(5),(0,)))
        self.assertEqual(minimum_adaptive_budget(model,(0,1,2)).worst_cost,Q(5))

    def test_destructive_two_probes_cannot_single_copy_recover_C(self):
        m=Carrier((0,0,0),((0,1,2),),
                  (Probe('A',(1,0,0),Q(1),(0,0,0)),
                   Probe('B',(0,1,0),Q(1),(0,0,0))))
        result=minimum_adaptive_budget(m,(0,0,1))
        self.assertIsNone(result.worst_cost)
        self.assertTrue(verify_adaptive_solution(m,result))
        # Neither destructive probe is admitted as a passive refinement.
        self.assertEqual(m.admitted_passive(),())
        with self.assertRaises(ValueError):
            refined_quotient(m,(0,))

    def test_actual_passive_repair_of_destructive_model(self):
        m=Carrier((0,0,0),((0,1,2),),
                  (Probe('A',(1,0,0),Q(1),(0,0,0)),
                   Probe('B',(0,1,0),Q(1),(0,0,0)),
                   Probe('read_only_A',(1,0,0),Q(1)),
                   Probe('read_only_B',(0,1,0),Q(1))))
        result=minimum_adaptive_budget(m,(0,0,1))
        self.assertEqual(result.worst_cost,Q(2))
        self.assertTrue(verify_adaptive_solution(m,result))

    def test_merged_history_perfect_current_state_probe_still_fails(self):
        m=Carrier((0,0,0),((2,2,2),),
                  (Probe('perfect_present_readout',(0,1,2),Q(1)),))
        histories=(frozenset({(0,2),(1,2)}),)
        result=minimum_adaptive_budget(m,(0,1,2),initial_beliefs=histories)
        self.assertIsNone(result.worst_cost)
        self.assertTrue(verify_adaptive_solution(m,result))

    def test_inexact_report_action_is_not_stochastic_infeasibility(self):
        m=Carrier((0,0,0),((1,2,2),),
                  (Probe('read_b',(0,1,0),Q(1)),))
        q,obs=refined_quotient(m,(0,))
        self.assertIsNone(q)
        self.assertEqual(obs,Noncongruence(0,0,2))
        # Initial fully collapsed report admits invariant delta_c.
        coarse,bad=refined_quotient(m,())
        self.assertIsNone(bad)
        self.assertEqual(point_lift(coarse),(2,))
        self.assertTrue(verify_kernel(coarse,stochastic_lift(coarse)))

    def test_more_information_can_destroy_stochastic_backward_lift(self):
        m=Carrier((0,0,0),((1,2,2),),
                  (Probe('mark_a',(1,0,0),Q(1)),))
        z0,b0=refined_quotient(m,())
        z1,b1=refined_quotient(m,(0,))
        self.assertIsNone(b0);self.assertIsNone(b1)
        self.assertIsNotNone(stochastic_lift(z0))
        self.assertIsNone(stochastic_lift(z1))
        self.assertIsNone(point_lift(z1))
        self.assertEqual(minimum_section_budget(m,'stochastic').cost,Q(0))

    def test_two_step_stochastic_then_point_upgrade_exact_minima(self):
        m=stage_carrier()
        initial,_=refined_quotient(m,())
        self.assertIsNone(stochastic_lift(initial))
        r1=minimum_section_budget(m,'stochastic')
        r2=minimum_section_budget(m,'point')
        self.assertEqual((r1.cost,r1.indices),(Q(2),(0,)))
        self.assertEqual((r2.cost,r2.indices),(Q(5),(0,1)))
        self.assertIsNone(point_lift(r1.quotient))
        self.assertTrue(verify_kernel(r1.quotient,r1.witness))
        self.assertEqual(r1.witness[2],(Q(0),Q(0),Q(0),Q(0),Q(1,2),Q(1,2)))
        self.assertTrue(verify_point(r2.quotient,r2.witness))
        self.assertIsNone(minimum_section_budget(stage_carrier(False),'stochastic'))

    def test_single_sensor_stochastic_but_no_point_is_not_identity(self):
        m=Carrier((0,0),((1,0),),(Probe('bit',(0,1),Q(3)),))
        sto=minimum_section_budget(m,'stochastic')
        det=minimum_section_budget(m,'point')
        self.assertEqual((sto.cost,sto.indices),(Q(0),()))
        self.assertEqual((det.cost,det.indices),(Q(3),(0,)))
        self.assertTrue(verify_kernel(sto.quotient,sto.witness))

    def test_stochastic_section_is_not_a_prior_posterior(self):
        m=Carrier((0,0),((1,0),),())
        z,_=refined_quotient(m,())
        self.assertEqual(stochastic_lift(z),((Q(1,2),Q(1,2)),))
        self.assertNotEqual((Q(1,4),Q(3,4)),stochastic_lift(z)[0])

    def test_invalid_menu_contracts_and_overlarge_exact_search(self):
        with self.assertRaises(ValueError):
            Carrier((0,0),((0,1),),(Probe('x',(0,1),Q(0)),))
        with self.assertRaises(ValueError):
            Carrier((0,0),((0,1),),(Probe('x',(0,)),))
        with self.assertRaises(ValueError):
            Carrier((0,0),((0,1),),(Probe('x',(([],),0)),))
        with self.assertRaises(ValueError):
            Carrier((0,0),((0,1),),(Probe('x',(float('nan'),0)),))
        with self.assertRaises(ValueError):
            Carrier((0,0),((0,1),),(Probe('x',(0,1),Q(1)),Probe('x',(0,1),Q(2))))
        m=binary_split_carrier()
        with self.assertRaises(ValueError):
            minimum_fixed_budget(m,tuple(range(4)),cap=2)
        with self.assertRaises(ValueError):
            refined_quotient(m,(999,))
        large=Quotient(tuple(range(11)),(tuple(range(11)),),(tuple(range(11)),))
        with self.assertRaises(ValueError):
            stochastic_lift(large,max_states=10)

    def test_policy_certificate_rejects_forged_optimum(self):
        m=binary_split_carrier()
        solution=minimum_adaptive_budget(m,tuple(range(4)))
        self.assertTrue(verify_adaptive_solution(m,solution))
        root=next(iter(solution.initial_costs))
        solution.initial_costs[root]=Q(1)  # mutation of claimed bound
        self.assertFalse(verify_adaptive_solution(m,solution))
        solution.initial_costs[root]=Q(2)
        solution.all_values[root]=Q(1)  # mutation of Bellman lower bound
        self.assertFalse(verify_adaptive_solution(m,solution))

    def test_losing_certificate_rejects_forged_adversary(self):
        m=Carrier((0,0,0),((0,1,2),),
                  (Probe('A',(1,0,0),Q(1),(0,0,0)),
                   Probe('B',(0,1,0),Q(1),(0,0,0))))
        solution=minimum_adaptive_budget(m,(0,0,1))
        self.assertTrue(verify_adaptive_solution(m,solution))
        root=next(iter(solution.initial_costs))
        solution.all_values[root]=Q(0)  # falsely declare a non-goal a goal
        self.assertFalse(verify_adaptive_solution(m,solution))

    def test_small_exhaustive_stochastic_quotient_census_replays_626(self):
        # Independent implementation of the Section LP in the new module;
        # the previous round's count is 279 total, 24 infeasible with 3 states.
        seen=bad=0
        for ny in (1,2,3):
            for q in itertools.product(range(ny),repeat=3):
                if set(q)!=set(range(ny)): continue
                for t in itertools.product(range(3),repeat=3):
                    for u in itertools.product(range(ny),repeat=ny):
                        if all(q[t[x]]==u[q[x]] for x in range(3)):
                            z=Quotient(q,(u,),(t,))
                            k=stochastic_lift(z)
                            if k is None: bad+=1
                            else:self.assertTrue(verify_kernel(z,k))
                            seen+=1
        self.assertEqual((seen,bad),(279,24))

    def test_source_model_independent_reference_when_checkout_available(self):
        try:
            from observational_succ.equivariant_choice import (
                FiniteActionQuotient, stochastic_section as inherited_solver,
                point_section as inherited_point, verify_kernel as inherited_verify)
        except ImportError:
            self.skipTest('Original PR #626 module not in isolated local scaffold')
        for m in (stage_carrier(),
                  Carrier((0,0),((1,0),),()),
                  Carrier((0,1,1),((1,2,2),),())):
            z,_=refined_quotient(m,())
            inherited=FiniteActionQuotient(z.q,z.ny,z.source_actions,z.report_actions)
            s1=stochastic_lift(z)
            s2=inherited_solver(inherited)
            self.assertEqual(s1 is None,s2 is None)
            self.assertEqual(point_lift(z) is None,inherited_point(inherited) is None)
            if s1 is not None:
                self.assertTrue(inherited_verify(inherited,s1))
                self.assertTrue(verify_kernel(z,s2))


if __name__=='__main__':
    unittest.main(verbosity=2)
