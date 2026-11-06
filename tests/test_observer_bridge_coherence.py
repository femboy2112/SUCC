"""Preregistered source and logic probes for the observer bridge coherence dossier."""
import sys, pathlib, unittest
from fractions import Fraction as Q
from math import lcm
HERE=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-04'/'observer_bridge_coherence'
sys.path.insert(0,str(HERE))
from coherence import (circle_bridge,finite_bridge_passport,independent_congruence_check,
                       original_prefix_probes,original_fourpole,integer_ring_phase_oracle,
                       bounded_machine_run,finite_switch_survival,hidden_bridge_reports,original_future_prime_discriminator)

SETS=(
    (Q(1,2),Q(1,3),Q(5,12)),
    (Q(7,20),Q(11,28),Q(13,45)),
    (Q(-7,16),Q(0),Q(19,50)),
)

class BridgeProofTests(unittest.TestCase):
    def test_preregistered_rational_sets(self):
        for probes in SETS:
            with self.subTest(probes=probes):
                p=finite_bridge_passport(probes)
                M=p['M']; alt=p['rival_winding']
                self.assertEqual(M,lcm(*(v.denominator for v in probes)))
                for q in probes:
                    self.assertTrue(independent_congruence_check(q,M))
                    self.assertEqual(circle_bridge(q,1),circle_bridge(q,alt))
                w=p['distinguishing_probe']
                self.assertEqual((circle_bridge(w,alt)-circle_bridge(w,1))%1,Q(1,2))
                self.assertFalse(independent_congruence_check(w,M))
    def test_independent_explicit_integer_oracle_enumerated_windings(self):
        for probes in SETS:
            M=lcm(*(q.denominator for q in probes))
            for c in range(1,2*M+2):
                all_equal=all(circle_bridge(q,1)==circle_bridge(q,c) for q in probes)
                integer_sufficient=all(((c-1)*q.numerator)%q.denominator==0 for q in probes)
                self.assertEqual(all_equal,integer_sufficient)
    def test_original_BBP_prefix_as_bridge_observation(self):
        obs=original_prefix_probes(12)
        p=finite_bridge_passport(obs)
        self.assertTrue(all(independent_congruence_check(x,p['M']) for x in obs))
        phase_oracle=integer_ring_phase_oracle(12)
        self.assertEqual(phase_oracle,obs[1::2])
        for j in (1,4,7,12):
            self.assertEqual(circle_bridge(original_fourpole(j),1),circle_bridge(original_fourpole(j),p['rival_winding']))
        self.assertEqual((circle_bridge(p['distinguishing_probe'],p['rival_winding'])-circle_bridge(p['distinguishing_probe'],1))%1,Q(1,2))
    def test_genuine_future_original_prime_probes(self):
        for horizon in (1,6,12,24):
            result=original_future_prime_discriminator(horizon)
            self.assertTrue(result['new_source_probe_refutes_rival'])
            self.assertEqual(result['selected_future_prime']%8,1)
            self.assertGreater(result['new_original_source_time'],horizon)
            self.assertNotEqual(result['new_phase_shift_under_alternative'],0)
        self.assertEqual(original_future_prime_discriminator(12)['selected_future_prime'],97)

    def test_dynamical_covariance_cannot_select_bridge(self):
        p=finite_bridge_passport(SETS[1])
        for q in (*SETS[1],Q(37,59),Q(-17,27)):
            for c in (1,p['rival_winding']):
                self.assertEqual(circle_bridge(16*q,c),circle_bridge(16*circle_bridge(q,c),1))
                self.assertEqual(circle_bridge(q+Q(11,41),c),
                                 (circle_bridge(q,c)+circle_bridge(Q(11,41),c))%1)
    def test_float_invalid(self):
        with self.assertRaises(TypeError):circle_bridge(0.5,1)
        with self.assertRaises(TypeError):circle_bridge(Q(1,5),1.0)
        with self.assertRaises(ValueError):finite_bridge_passport(())

class BusyBeaverBoundaryTests(unittest.TestCase):
    SCAN={ (0,1):(1,1,0),(0,0):(0,1,-1) }
    NONHALT={ (0,1):(1,1,0),(0,0):(0,1,0) }
    def test_preregistered_halting_prefix_budgets(self):
        for budget in (0,2,17,64,128):
            with self.subTest(budget=budget):
                got=bounded_machine_run(self.SCAN,initial_ones=17,max_steps=budget)
                self.assertEqual(got['status'], 'REFUTED_NONHALTING' if budget>=18 else 'UNVERIFIED_AFTER_BUDGET')
                self.assertFalse(got['nonhalting_proved'])
                if budget>=18:self.assertEqual(got['first_observed_halt_step'],18)
    def test_never_halt_not_proved_by_finite_execution(self):
        for budget in (0,2,17,64,128):
            got=bounded_machine_run(self.NONHALT,initial_ones=2,max_steps=budget)
            self.assertEqual(got['status'],'UNVERIFIED_AFTER_BUDGET')
            self.assertFalse(got['nonhalting_proved'])
    def test_no_missing_instruction_as_false_halt(self):
        with self.assertRaises(ValueError):bounded_machine_run({(0,0):(0,1,0)}, initial_ones=2,max_steps=1)
    def test_fixed_late_halt_refutable_only_at_late_step(self):
        for n in (1,3,12,40):
            self.assertEqual(bounded_machine_run(self.SCAN,initial_ones=n,max_steps=n)['status'],'UNVERIFIED_AFTER_BUDGET')
            self.assertEqual(bounded_machine_run(self.SCAN,initial_ones=n,max_steps=n+1)['first_observed_halt_step'],n+1)

class InverseLimitSourceTests(unittest.TestCase):
    def test_all_preregistered_moving_switches(self):
        for n in (1,2,5,12,32):
            s=finite_switch_survival(n,n+1)
            self.assertTrue(s['observed_all_zero'])
            self.assertFalse(s['infinite_never_switch_exists_in_declared_finite_switch_class'])
            self.assertFalse(finite_switch_survival(n,n)['observed_all_zero'])
    def test_observationally_permanent_hidden_tag(self):
        for horizon in (1,2,5,12,32):
            a=(1,0,1,1,0)*(horizon//5)+(1,0,1,1,0)[:horizon%5]
            p=hidden_bridge_reports(tuple(a),0,1)
            self.assertTrue(p['visible_indistinguishable'])
            self.assertTrue(p['new_hidden_probe_would_separate'])
            self.assertNotEqual(*p['hidden_probe_reports'])
    def test_witness_not_prematurely_global(self):
        for n in (1,2,5,12,32):
            x=finite_switch_survival(n,n+1)
            y=finite_switch_survival(n+1,n+1)
            self.assertTrue(x['observed_all_zero'])
            self.assertFalse(y['observed_all_zero'])

if __name__=='__main__':unittest.main()
