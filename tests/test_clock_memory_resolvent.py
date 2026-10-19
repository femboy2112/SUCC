"""Exact backward clock memory kernel / decay-at-infinity no-ghost controls."""
import unittest
from fractions import Fraction as F
from math import lcm
from observational_succ.bidirectional_cut import CutSourceError, certified_cut_residual
from observational_succ.clock_memory_resolvent import (
    memory_bounds, upper_cut_weight_bounds, backward_ladder_mutation,
    folded_memory_energy_bounds, haar_memory_transport_obstruction,
)


class BackwardMemoryTests(unittest.TestCase):
    def test_monotone_rational_memory_enclosures(self):
        for period in (1,2,6,12):
            for phase in (F(0),F(1,2),F(7,4)):
                a=memory_bounds(phase,period,depth=8)
                b=memory_bounds(phase,period,depth=16)
                self.assertTrue(a['lower']<=b['lower']<=b['upper']<=a['upper'])
                self.assertGreater(a['lower'],0)
                self.assertEqual(a['period'],period)

    def test_recurrence_is_source_derived(self):
        for period in (1,2,6):
            for phase in (F(0),F(1,7),F(8,3)):
                r=backward_ladder_mutation(phase,period,depth=24)
                self.assertTrue(r['boundary_decay_certified'])
                lo,hi=r['memory_difference_enclosure']
                self.assertLessEqual(lo,F(r['shift_law_exact']))
                self.assertGreaterEqual(hi,F(r['shift_law_exact']))

    def test_ghost_periodic_addition_preserves_shift_but_not_decay(self):
        good=backward_ladder_mutation(F(1,2),3,ghost=0)
        mutant=backward_ladder_mutation(F(1,2),3,ghost=F(1,5))
        self.assertEqual(good['shift_law_exact'],mutant['shift_law_exact'])
        self.assertTrue(good['boundary_decay_certified'])
        self.assertFalse(mutant['boundary_decay_certified'])

    def test_cut_boundary_has_one_sided_weight(self):
        L=6
        upper=upper_cut_weight_bounds(F(1),L,depth=18)
        below=upper_cut_weight_bounds(F(999,1000),L,depth=18)
        self.assertEqual(upper['near_cut_term'],1)
        self.assertEqual(below['near_cut_term'],0)
        self.assertGreater(upper['lower'],below['upper'])

    def test_folded_period_full_L2_interval_cross_oracle(self):
        for c in [(F(0),),(F(3,2),),(F(1),F(-1)),(F(1),F(-1),F(1))]:
            L=1
            for n in range(1,len(c)+1): L=lcm(L,n)
            folded=folded_memory_energy_bounds(c,L,J=20,subdivisions=10)
            independent=certified_cut_residual(c,R=max(30,30*L),terms=14)
            self.assertLessEqual(folded['full_squared_error_lower'],independent['upper'])
            self.assertGreaterEqual(folded['full_squared_error_upper'],independent['lower'])
            self.assertGreaterEqual(folded['full_squared_error_lower'],0)

    def test_ghost_source_and_bad_budgets_rejected(self):
        with self.assertRaises(CutSourceError): memory_bounds(-1,3)
        with self.assertRaises(CutSourceError): memory_bounds(F(0),3,depth=0)
        with self.assertRaises(CutSourceError): memory_bounds(F(0),3,depth=2001)
        with self.assertRaises(CutSourceError): upper_cut_weight_bounds(3,3)
        with self.assertRaises(CutSourceError): folded_memory_energy_bounds((1,1),3)
        with self.assertRaises(CutSourceError): folded_memory_energy_bounds((1,1),2,subdivisions=0)

    def test_probe_standalone_from_external_workdir(self):
        # Regression for source integration: a script launched directly from
        # outside repo must import its declared local package, no pip/CI magic.
        import os
        import subprocess
        import sys
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        result=subprocess.run(
            [sys.executable,str(root/'scripts/bidirectional_cut_probe.py'),'--verify'],
            cwd='/',env={**os.environ,'PYTHONPATH':''},
            text=True,capture_output=True,timeout=25,check=False,
        )
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('BIDIRECTIONAL_CUT_RECEIPT_VERIFIED',result.stdout)

    def test_total_variation_separation_is_source_certified(self):
        a=haar_memory_transport_obstruction(840,28)
        self.assertGreater(a['total_variation_distance_lower'],F(93,100))
        self.assertEqual(a['L2_norm_transport_squared_lower'],840)
        # Even though both source measures are bona fide probabilities,
        # their Hilbert metrics cannot be uniformly identified as L grows.
        self.assertTrue(a['growing_clock_not_uniformly_norm_equivalent'])
        self.assertTrue(haar_memory_transport_obstruction(2310,48)
                        ['total_variation_distance_lower']>a['total_variation_distance_lower'])

    def test_invalid_haar_memory_transport_domains(self):
        with self.assertRaises(CutSourceError): haar_memory_transport_obstruction(1,1)
        with self.assertRaises(CutSourceError): haar_memory_transport_obstruction(6,7)
        with self.assertRaises(CutSourceError): haar_memory_transport_obstruction(6,1)
        with self.assertRaises(CutSourceError): haar_memory_transport_obstruction(True,2)

    def test_memory_exact_reciprocal_square_identity_at_origin(self):
        a=memory_bounds(F(0),1,depth=128)
        # By Basel, this is pi^2/6; rational bounds certify the true sum
        # without evaluating transcendental constants or zeros.
        self.assertTrue(F(8,5)<a['lower']<a['upper']<F(17,10))
        self.assertLess(a['upper']-a['lower'],F(1,16000))


if __name__=='__main__':unittest.main()
