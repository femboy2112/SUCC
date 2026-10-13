"""Finite observational quotient and compactness-uniformity controls."""
import unittest
from itertools import product
from observational_succ.carrier_shadow_fibers import (
    FiniteShadowSuite,DelayedSeparatingTower,ShadowFiberError,
)
from observational_succ.carrier_observational_frontier import (
    ontology_alias_model, destructive_parity_model)


class ShadowFiberTests(unittest.TestCase):
    def test_exact_two_bit_sources_require_two_static_probes(self):
        states=tuple((a,b) for a,b in product(range(2),repeat=2))
        s=FiniteShadowSuite("source two-bit",states,
            {"left":tuple(x[0] for x in states),"right":tuple(x[1] for x in states)},
            {x:x[0]^x[1] for x in states})
        r=s.minimal_complete_suite()
        self.assertEqual(r['status'],"FINITELY_CERTIFIABLE")
        self.assertEqual(r['suite'],("left","right"))
        self.assertEqual(r['minimum'],2)
        for state in states:
            self.assertEqual(s.target_report(r['suite'],s.report(state,r['suite']))['claim'],
                             state[0]^state[1])
        self.assertEqual(s.target_report(("left",),(0,))['status'],"UNRESOLVED")
        self.assertEqual(s.target_report(("left",),(9,))['status'],"INCONSISTENT_SOURCE")

    def test_all_source_hypotheses_alias_on_declared_observer(self):
        m, claim=ontology_alias_model()
        s=FiniteShadowSuite("same source",m.states,{
            a:tuple(m.step(st,a)[0] for st in m.states) for a in m.actions},claim)
        r=s.minimal_complete_suite()
        self.assertEqual(r['status'],"PERMANENTLY_DARK")
        self.assertEqual(r['pair'],("inside","outside"))
        self.assertFalse(r['source_authenticated'])

    def test_one_extra_probe_changes_reach(self):
        states=("inside","outside")
        s=FiniteShadowSuite("source",states,{"echo":("same","same"),"separator":(0,1)},
                            {"inside":"i","outside":"o"})
        self.assertEqual(s.minimal_complete_suite()['suite'],("separator",))

    def test_free_original_source_claim_requires_zero_measurements(self):
        s=FiniteShadowSuite("constant",(0,1),{"probe":(0,1)},{0:"yes",1:"yes"})
        self.assertEqual(s.minimal_complete_suite()['minimum'],0)
        self.assertEqual(s.target_report((),())['status'],"PROVED")

    def test_syntactic_row_completeness_and_budget(self):
        with self.assertRaises(ShadowFiberError):
            FiniteShadowSuite("x",(0,1),{"a":(0,)},{0:0,1:1})
        s=FiniteShadowSuite("x",(0,1),{"a":(0,1)},{0:0,1:1})
        with self.assertRaises(ShadowFiberError):
            s.minimal_complete_suite(max_probes=0)
        with self.assertRaises(ShadowFiberError):
            s.fiber(("unknown",),(0,))

    def test_countably_infinite_rivals_pointwise_but_not_uniformly_separated(self):
        t=DelayedSeparatingTower()
        for horizon in range(40):
            witness=t.alias_after(horizon)
            self.assertGreater(witness,horizon)
            self.assertEqual(t.trace(witness,horizon),t.trace(0,horizon))
            self.assertEqual(t.first_separator(witness),witness)
        self.assertEqual(t.bounded_source_horizon(12),12)

    def test_finite_proxy_minimal_suite_cost_grows_with_bound(self):
        for B in range(1,8):
            states=tuple(range(B+1))
            table={f'p{n}':tuple(int(s==n) for s in states) for n in range(1,B+1)}
            suite=FiniteShadowSuite(f'bounded-{B}',states,table,
                {s:int(s==0) for s in states})
            result=suite.minimal_complete_suite()
            self.assertEqual(result['minimum'],B)
            self.assertEqual(result['suite'],tuple(table))

    def test_pairwise_separability_not_safe_under_destructive_measurement(self):
        machine,claims=destructive_parity_model()
        # The same instantaneous output probes are STATICALLY sufficient.
        static=FiniteShadowSuite(machine.source_id,machine.states,
            {act:tuple(machine.step(s,act)[0] for s in machine.states)
             for act in machine.actions},claims)
        self.assertEqual(static.minimal_complete_suite()['minimum'],2)
        # But these instruments mutate the carrier; the static certificate
        # cannot be executed as one serial experiment in this setting.
        self.assertEqual(machine.adaptive_original_claim(claims)['rank'],None)

if __name__=='__main__':unittest.main()
