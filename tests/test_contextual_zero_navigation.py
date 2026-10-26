"""Hostile exact finite tests for SUCC's contextual zero / observer backbone."""
from __future__ import annotations

import itertools
import unittest
from functools import lru_cache
from fractions import Fraction as Q

from observational_succ.coherent_zero_relations import Poly, ZeroRelation
from observational_succ.contextual_zero_navigation import (
    NavigationError, Probe, Move, SourceField, Knowledge, CoordinateChart,
    Policy, initial_knowledge, model_observe, model_move, inspect_zero,
    gauge_potential, plan_guaranteed, check_policy, realize_policy_in_model,
)


def cyclic_model(*, with_exact=True, with_parity=True):
    names=("x",)
    x=Poly.var(names,"x")
    universal=x*(x-1)*(x-2)*(x-3)
    probes=[]
    if with_parity:
        parity=(2*x**3-9*x**2+10*x)*Q(1,3)
        probes.append(Probe("Z4","parity",parity,1))
    if with_exact:
        probes.append(Probe("Z4","exact_x",x,1))
    return SourceField(
        "Z4", names, tuple((Q(i),) for i in range(4)),
        (ZeroRelation("Z4","finite source polynomial",universal),
         ZeroRelation("Z4","reflexive equality",x-x)),
        tuple(probes),
        (Move("Z4","left",(3,0,1,2),1),
         Move("Z4","right",(1,2,3,0),1)),
    )


def smaller_model(mapping):
    names=("x",)
    x=Poly.var(names,"x")
    return SourceField(
        "Z3",names,tuple((Q(i),) for i in range(3)),
        (ZeroRelation("Z3","finite",x*(x-1)*(x-2)),),
        (Probe("Z3","x",x,1), Probe("Z3","constant",Poly.const(names,0),1)),
        (Move("Z3","step",mapping,1),),
    )


class FoundationalZeroAndGauge(unittest.TestCase):
    def test_multiple_valid_zeros_hold_simultaneously_with_source(self):
        f=cyclic_model()
        self.assertEqual(len(f.universal_zeros),2)
        for law in f.universal_zeros:
            for state in f.states:
                self.assertEqual(law.expression.at(state),0)
        self.assertFalse(f.universal_zeros[0].expression.is_zero)
        self.assertTrue(f.universal_zeros[1].expression.is_zero)

    def test_false_universal_law_and_mismatched_source_rejected(self):
        f=cyclic_model()
        x=Poly.var(("x",),"x")
        with self.assertRaises(NavigationError):
            SourceField(f.source_id,f.coordinates,f.states,
                        f.universal_zeros+(ZeroRelation("Z4","false",x-1),),
                        f.probes,f.moves)
        with self.assertRaises(NavigationError):
            SourceField(f.source_id,f.coordinates,f.states,
                        (ZeroRelation("fake-Z4","false",x-x),),f.probes,f.moves)

    def test_zero_status_separates_present_from_global_truth(self):
        f=cyclic_model()
        k=initial_knowledge(f,budget=3)
        x=Poly.var(("x",),"x")
        z=inspect_zero(f,k,x-2)
        self.assertFalse(z.global_on_finite_carrier)
        self.assertFalse(z.entailed_at_current_belief)
        self.assertTrue(z.compatible_with_current_belief)
        self.assertEqual(z.current_counterexamples,(0,1,3))
        observed=model_observe(f,k,2,"exact_x")
        z=inspect_zero(f,observed,x-2)
        self.assertTrue(z.entailed_at_current_belief)
        self.assertFalse(z.global_on_finite_carrier)
        moved,w=model_move(f,observed,2,"right")
        self.assertEqual(w,3)
        self.assertFalse(inspect_zero(f,moved,x-2).compatible_with_current_belief)
        self.assertEqual(observed.journal[0].reported_value,Q(2))
        self.assertEqual(moved.journal[0].reported_value,Q(2))
        self.assertEqual(moved.journal[-1].kind,"movement")
        self.assertEqual(moved.journal[-1].after,(3,))

    def test_chart_transport_is_typed_and_may_be_many_to_one(self):
        f=cyclic_model()
        x=Poly.var(f.coordinates,"x")
        k=initial_knowledge(f)
        chart=CoordinateChart(f.source_id,("u","v"),(x,x*x))
        u=Poly.var(chart.target_coordinates,"u")
        v=Poly.var(chart.target_coordinates,"v")
        z=inspect_zero(f,k,u*u-v,chart=chart)
        self.assertTrue(z.global_on_finite_carrier)
        self.assertTrue(z.transported.is_zero)
        only_finite=inspect_zero(f,k,v*(v-1)*(v-4)*(v-9),chart=chart)
        self.assertTrue(only_finite.global_on_finite_carrier)
        self.assertFalse(only_finite.transported.is_zero)
        bad=CoordinateChart("other-source",("u",),(x,))
        with self.assertRaises(NavigationError):inspect_zero(f,k,u,chart=bad)
        with self.assertRaises(NavigationError):inspect_zero(f,k,u)

    def test_noninjective_chart_preserves_zeros_but_loses_sign(self):
        names=("x",)
        x=Poly.var(names,"x")
        roots=(x+2)*(x+1)*(x-1)*(x-2)
        field=SourceField("signed-model",names,
                          ((Q(-2),),(Q(-1),),(Q(1),),(Q(2),)),
                          (ZeroRelation("signed-model","finite law",roots),),
                          (Probe("signed-model","square",x*x,1),),())
        k=initial_knowledge(field,budget=1)
        measured=model_observe(field,k,3,"square")
        self.assertEqual(measured.possible,(0,3))
        chart=CoordinateChart("signed-model",("u",),(x*x,))
        u=Poly.var(("u",),"u")
        self.assertTrue(inspect_zero(field,measured,u-4,chart=chart).entailed_at_current_belief)
        self.assertFalse(inspect_zero(field,measured,x-2).entailed_at_current_belief)
        self.assertFalse(inspect_zero(field,measured,x+2).entailed_at_current_belief)
        self.assertEqual(measured.journal[-1].reported_value,Q(4))

    def test_gauge_zero_is_relative_not_absolute(self):
        values=(Q(7),Q(12),Q(-3),Q(10))
        shifted=tuple(v+Q(57,5) for v in values)
        self.assertEqual(gauge_potential(values,2),gauge_potential(shifted,2))
        self.assertEqual(gauge_potential(values,2)[2],0)
        self.assertNotEqual(gauge_potential(values,0),gauge_potential(values,2))

    def test_bad_contracts_fail_closed(self):
        f=cyclic_model()
        with self.assertRaises(NavigationError):
            SourceField("Z4",("x",),f.states,f.universal_zeros,
                        (Probe("Z4","free",Poly.var(("x",),"x"),0),),f.moves)
        with self.assertRaises(NavigationError):
            SourceField("Z4",("x",),f.states,f.universal_zeros,f.probes,
                        (Move("Z4","escape",(0,1,2,8),1),))
        with self.assertRaises(NavigationError):initial_knowledge(f,possible=(0,0),budget=3)
        with self.assertRaises(NavigationError):initial_knowledge(f,budget=-1)
        k=initial_knowledge(f,budget=0)
        with self.assertRaises(NavigationError):model_observe(f,k,0,"exact_x")
        with self.assertRaises(NavigationError):model_move(f,k,0,"left")
        with self.assertRaises(NavigationError):model_observe(f,initial_knowledge(f,budget=2),8,"exact_x")
        with self.assertRaises(NavigationError):model_observe(f,initial_knowledge(f,budget=2),0,"not_a_probe")


class GoalDirectedObserver(unittest.TestCase):
    def test_no_free_observation_and_false_reachability_refused(self):
        f=cyclic_model()
        k=initial_knowledge(f,budget=10)
        self.assertEqual(len(k.journal),0)
        self.assertEqual(k.possible,(0,1,2,3))
        no_probes=cyclic_model(with_exact=False,with_parity=False)
        result=plan_guaranteed(no_probes,initial_knowledge(no_probes,budget=10),(0,))
        self.assertIsNone(result.policy)
        self.assertEqual(result.status,"no_guarantee_within_declared_toolkit")
        parity_only=cyclic_model(with_exact=False,with_parity=True)
        no_path=plan_guaranteed(parity_only,initial_knowledge(parity_only,budget=10),(0,))
        self.assertIsNone(no_path.policy)
        self.assertEqual(k.possible,(0,1,2,3))

    def test_adaptive_plan_reaches_singleton_from_uncertainty(self):
        f=cyclic_model()
        k=initial_knowledge(f,budget=3)
        result=plan_guaranteed(f,k,(0,))
        self.assertEqual(result.status,"guaranteed_within_declared_toolkit")
        self.assertIsNotNone(result.policy)
        self.assertEqual(result.worst_cost,3)
        self.assertEqual(result.policy.kind,"probe")
        self.assertEqual(result.policy.name,"exact_x")
        self.assertEqual(check_policy(f,k,(0,),result.policy),3)
        for world in range(4):
            finish,actual=realize_policy_in_model(f,k,world,(0,),result.policy)
            self.assertEqual(actual,0)
            self.assertEqual(finish.possible,(0,))
            spent=k.budget-finish.budget
            self.assertLessEqual(spent,result.worst_cost)
            self.assertEqual(finish.journal[0].kind,"observation")
            self.assertEqual(finish.journal[0].reported_value,Q(world))
        self.assertEqual(k.journal,())  # planning has not actualized an observation

    def test_budget_two_is_insufficient_on_four_cycle(self):
        f=cyclic_model()
        k=initial_knowledge(f,budget=2)
        self.assertIsNone(plan_guaranteed(f,k,(0,)).policy)

    def test_partial_information_changes_observation_value(self):
        f=cyclic_model()
        k=initial_knowledge(f,possible=(1,2),budget=3)
        found=plan_guaranteed(f,k,(0,))
        self.assertIsNotNone(found.policy)
        self.assertEqual(check_policy(f,k,(0,),found.policy),found.worst_cost)
        for world in k.possible:
            _,ending=realize_policy_in_model(f,k,world,(0,),found.policy)
            self.assertEqual(ending,0)

    def test_already_in_target_and_policy_mutants(self):
        f=cyclic_model()
        k=initial_knowledge(f,possible=(0,),budget=0)
        ok=plan_guaranteed(f,k,(0,)).policy
        self.assertEqual(ok.kind,"goal")
        self.assertEqual(check_policy(f,k,(0,),ok),0)
        wrong=Policy("Z4",(0,1),"goal",None,0)
        with self.assertRaises(NavigationError):
            check_policy(f,initial_knowledge(f,possible=(0,1)),(0,),wrong)
        other=Policy("fake",(0,),"goal",None,0)
        with self.assertRaises(NavigationError):check_policy(f,k,(0,),other)
        k=initial_knowledge(f,budget=3)
        computed=plan_guaranteed(f,k,(0,)).policy
        truncated=Policy(computed.source_id,computed.belief,"probe",computed.name,
                         computed.worst_cost,None,computed.outcomes[:-1])
        with self.assertRaises(NavigationError):check_policy(f,k,(0,),truncated)
        forged=Policy(computed.source_id,computed.belief,"probe",computed.name,
                      computed.worst_cost-1,None,computed.outcomes)
        with self.assertRaises(NavigationError):check_policy(f,k,(0,),forged)

    def test_move_keeps_actual_model_world_in_new_belief(self):
        f=cyclic_model()
        for candidate in range(4):
            k=initial_knowledge(f,budget=5)
            moved,world=model_move(f,k,candidate,"right")
            self.assertIn(world,moved.possible)
            self.assertEqual(len(moved.possible),4)


class IndependentFinitePolicyOracle(unittest.TestCase):
    @staticmethod
    def independent_cost(field,belief,goal,budget):
        """Second algorithm, cost-to-go sets rather than proof-tree objects."""
        @lru_cache(None)
        def solve(b,bud):
            if all(i in goal for i in b):return 0
            outcomes=[]
            for move in field.moves:
                if move.cost<=bud:
                    future=tuple(sorted({move.successor[i] for i in b}))
                    value=solve(future,bud-move.cost)
                    if value is not None:outcomes.append(value+move.cost)
            for p in field.probes:
                if p.cost>bud:continue
                branches={}
                for i in b:
                    branches.setdefault(p.readout.at(field.states[i]),set()).add(i)
                if len(branches)<2:continue
                costs=[]
                for subset in branches.values():
                    score=solve(tuple(sorted(subset)),bud-p.cost)
                    if score is None:break
                    costs.append(score)
                else:outcomes.append(p.cost+max(costs))
            return min(outcomes) if outcomes else None
        return solve(belief,budget)

    def test_exhaustive_ternary_action_model_against_independent_solver(self):
        tested=0
        for transition in itertools.product(range(3),repeat=3):
            field=smaller_model(transition)
            for selected_goal in ((0,),(1,),(2,)):
                for budget in range(5):
                    k=initial_knowledge(field,budget=budget)
                    program=plan_guaranteed(field,k,selected_goal)
                    independent=self.independent_cost(field,k.possible,selected_goal,budget)
                    self.assertEqual(program.worst_cost,independent)
                    if program.policy is not None:
                        self.assertEqual(check_policy(field,k,selected_goal,program.policy),independent)
                        for world in k.possible:
                            finish,actual=realize_policy_in_model(field,k,world,selected_goal,program.policy)
                            self.assertIn(actual,selected_goal)
                            self.assertLessEqual(budget-finish.budget,independent)
                    tested+=1
        self.assertEqual(tested,27*3*5)


if __name__=="__main__":unittest.main()
