import unittest
from observational_succ.local_global_descent import VoltageSource,Dart
from observational_succ.cycle_support_budget import fundamental_cycle_certificate,adversarial_cycle_probe_lower_bound
from observational_succ.constructive_gluing_tower import gaussian_voltage_source
from observational_succ.gaussian_holonomy import GaussianSieve

class CycleSupportTests(unittest.TestCase):
    def test_fundamental_cycle_zero_and_negative(self):
        v=((0,),(1,),(2,))
        for k in (-2,1):
            g=VoltageSource('cycle3',v,(Dart('a',v[0],v[1],(1,)),Dart('b',v[1],v[2],(1,)),Dart('c',v[2],v[0],(k,))),1,3)
            a=fundamental_cycle_certificate(g)
            self.assertEqual(a.independent_cycles,1)
            self.assertEqual(a.global_exact,(k==-2))
            if k==1:self.assertEqual(abs(a.cycles[0].voltage[0]),3)

    def test_two_cycles_need_two_cycle_oracle_checks(self):
        graph=VoltageSource('bowtie',(0,1,2),(Dart('a',0,1,(2,)),Dart('b',1,0,(-2,)),
             Dart('c',0,2,(3,)),Dart('d',2,0,(-3,))),1)
        report=fundamental_cycle_certificate(graph)
        self.assertEqual(report.independent_cycles,2)
        self.assertTrue(report.global_exact)
        lower=adversarial_cycle_probe_lower_bound(2)
        self.assertEqual(lower['required_distinct_cycle_probes'],2)
        self.assertEqual(lower['single_fault_sources'],((1,0),(0,1)))

    def test_genuine_gaussian_sieve_cycle_rank(self):
        g=gaussian_voltage_source(GaussianSieve(((1,2),(2,3))),1)
        c=fundamental_cycle_certificate(g)
        self.assertEqual(c.vertices,2304)
        self.assertEqual(c.darts,4356)
        self.assertTrue(c.global_exact)
        self.assertEqual(c.components,243)
        self.assertEqual(c.independent_cycles,4356-2304+243)

    def test_self_loop_nonzero_fundamental_cycle(self):
        g=VoltageSource('loop',((0,),),(Dart('l',(0,),(0,),(4,)),),1,4)
        c=fundamental_cycle_certificate(g)
        self.assertEqual(c.independent_cycles,1)
        self.assertFalse(c.global_exact)
        self.assertEqual(c.cycles[0].voltage,(4,))

if __name__=='__main__':unittest.main()
