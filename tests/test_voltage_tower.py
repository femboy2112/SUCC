"""Mathematical voltage certificate assembled through typed SUCC diagonal tower."""
import unittest
from dataclasses import replace

from observational_succ.gaussian_holonomy import GaussianSieve, HolonomyError
from observational_succ.voltage_tower import (
    VoltageTower, VoltageTowerError, completed_voltage_climb,
)


class VoltageTowerTests(unittest.TestCase):
    def test_true_prime_source_shards_certify_global_confinement(self):
        t=completed_voltage_climb()
        p=t.final_macro_succ()
        self.assertEqual(p.period,65)
        self.assertEqual(p.checked_vertices,2304)
        self.assertEqual(p.checked_directed_edges,4356)
        self.assertEqual(p.verified_shards,6)
        self.assertEqual(p.max_lifted_component,580)
        self.assertEqual(len(t.transport_log),14)
        self.assertEqual(len(t.event_log),20)
        self.assertTrue(p.mathematical_full_source_check)
        self.assertEqual(p.epistemic_macro_updates,1)
        with self.assertRaises(VoltageTowerError):t.final_macro_succ()

    def test_all_source_edges_are_partitioned_once_by_climbers(self):
        t=completed_voltage_climb()
        blocks=[]
        for n in t.climbers:
            s=t.shards['voltage-shard:'+n]
            blocks.extend(s.assigned)
        self.assertEqual(len(blocks),len(t.vertices))
        self.assertEqual(set(blocks),set(t.vertices))
        self.assertEqual(sum(t.shards['voltage-shard:'+n].checked_edges for n in t.climbers),4356)

    def test_cannot_verifiably_confinement_certify_escape_source(self):
        for factors in ((),((1,2),),((1,2),(1,4))):
            with self.assertRaisesRegex(HolonomyError,'Nonzero quotient holonomy'):
                VoltageTower(GaussianSieve(factors),1,3)

    def test_upper_floor_requires_two_previous_checked_shards(self):
        t=VoltageTower(GaussianSieve(((1,2),(2,3))),1,3)
        with self.assertRaisesRegex(VoltageTowerError,'prerequisites'):
            t.check_at('A1')
        t.check_at('A0');t.check_at('B0')
        t.relay('A0','A1')
        with self.assertRaisesRegex(VoltageTowerError,'prerequisites'):
            t.check_at('A1')
        t.relay('B0','A1')
        t.check_at('A1')

    def test_math_false_potential_rejected_locally(self):
        t=VoltageTower(GaussianSieve(((1,2),(2,3))),1,3)
        vertex=t.assigned['A0'][0]
        x,y=t.potentials[vertex]
        t.potentials[vertex]=(x+65,y)
        with self.assertRaisesRegex(VoltageTowerError,'Noncommuting source edge'):
            t.check_at('A0')

    def test_math_false_potential_rejected_at_base_even_if_shards_previously_passed(self):
        t=completed_voltage_climb()
        vertex=t.assigned['A0'][0]
        x,y=t.potentials[vertex]
        t.potentials[vertex]=(x+65,y)
        with self.assertRaisesRegex(VoltageTowerError,'source edge'):
            t.final_macro_succ()

    def test_false_shard_owner_source_and_edge_claims_rejected(self):
        for mutate in (
            lambda s:replace(s,origin='B2'),
            lambda s:replace(s,source_signature='wrong-sieve'),
            lambda s:replace(s,basis='wrong-vector-space'),
            lambda s:replace(s,checked_edges=s.checked_edges+1),
            lambda s:replace(s,assigned=s.assigned[1:]),
            lambda s:replace(s,parents=()),
        ):
            t=completed_voltage_climb()
            sid='voltage-shard:A2'
            t.shards[sid]=mutate(t.shards[sid])
            with self.assertRaises(VoltageTowerError):t.final_macro_succ()

    def test_dropped_diagonal_blocks_global_arithmetic_certificate_then_repairs(self):
        t=completed_voltage_climb(descent=False)
        t.relay('B2','A1')
        t.relay('B1','A0')
        t.relay('A1','B0')
        t.relay('A0','E');t.relay('B0','E')
        self.assertNotIn('voltage-shard:A2',t.known['E'])
        with self.assertRaisesRegex(VoltageTowerError,'never reached E'):
            t.final_macro_succ()
        t.relay('A2','B1');t.relay('B1','A0');t.relay('A0','E')
        self.assertEqual(t.final_macro_succ().max_lifted_component,580)

    def test_E_injected_references_do_not_replace_actual_relay(self):
        t=completed_voltage_climb(descent=False)
        t.known['E']=set(t.shards)
        with self.assertRaisesRegex(VoltageTowerError,'causal network replay'):
            t.final_macro_succ()

    def test_Forged_top_claim_does_not_substitute_for_shard_math(self):
        t=completed_voltage_climb()
        t.shards['voltage-shard:B2']=replace(t.shards['voltage-shard:B2'],checked_edges=0)
        with self.assertRaises(VoltageTowerError):t.final_macro_succ()

    def test_wrong_source_factor_rejected_before_receiving(self):
        t=completed_voltage_climb()
        t.sieve=GaussianSieve(((1,2),(1,4)))
        with self.assertRaisesRegex(VoltageTowerError,'signature drift'):
            t.final_macro_succ()

    def test_multiple_arrival_orders_agree_on_same_global_source_proof(self):
        a=completed_voltage_climb(descent=False)
        b=completed_voltage_climb(descent=False)
        for t in (a,b):
            for level in (2,1):
                t.relay(f'A{level}',f'B{level-1}')
                t.relay(f'B{level}',f'A{level-1}')
        a.relay('A0','E');a.relay('B0','E')
        b.relay('B0','E');b.relay('A0','E')
        self.assertEqual(a.final_macro_succ(),b.final_macro_succ())


if __name__=='__main__':unittest.main()
