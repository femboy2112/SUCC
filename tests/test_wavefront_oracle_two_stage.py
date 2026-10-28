"""Exact rational and adversarial source-derived two-stage wavefront tests."""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from observational_succ.wavefront_oracle_two_stage import (
    SourceGeometry, one_stage_prob, run_two_stages, recurrence_residual,
    geometric_impulse_response, critical_grade, critical_rescaled_grade,
    critical_second_difference, finite_wavefront_past,
    finite_memory_information_defects, depth_defect_residual, one_stage_forcing_residual,
    equal_stage_critical_grade,equal_stage_depth_difference,run_equal_stage_tower,
)

class TestSourceTwoStage(unittest.TestCase):
    def test_authentic_source_R_identity(self):
        for x in (Q(0),Q(1,8),Q(1,2),Q(3,4),Q(9,10)):
            g=SourceGeometry(x)
            R=(1-x)/((2-x*x)*(x*x-2*x+2))
            self.assertEqual(g.source_total(),R)
            self.assertEqual(g.normalization * R,(1-x)/4)
            for j in range(12):
                self.assertEqual(g.raw_grade(j), R*g.grade_probability(j))

    def test_grade_probability_convolution(self):
        for x in (Q(0),Q(1,4),Q(1,2),Q(5,6),Q(1)):
            g=SourceGeometry(x)
            for j in range(15):
                q=sum((one_stage_prob(g.u,k)*one_stage_prob(g.v,j-k)
                      for k in range(j+1)),Q(0))
                self.assertEqual(q,g.grade_probability(j))

    def test_endpoint_is_double_geom(self):
        g=SourceGeometry(Q(1))
        self.assertEqual((g.u,g.v,g.normalization),(Q(1,2),Q(1,2),Q(1,4)))
        for j in range(30):
            self.assertEqual(g.grade_probability(j), critical_grade(j))
        self.assertEqual(g.mean_extra_delay(),Q(2))
        self.assertEqual(g.variance_extra_delay(),Q(4))

    def test_x_parameter_checks(self):
        for bad in (Q(-1,3),Q(11,10)):
            with self.assertRaises(ValueError):SourceGeometry(bad)
        for bad in (-1, Q(-1,2)):
            with self.assertRaises(ValueError):critical_grade(bad)

    def test_discriminant_and_collision(self):
        for x in (Q(0),Q(1,2),Q(7,8),Q(1)):
            g=SourceGeometry(x)
            self.assertEqual(g.u+g.v,x)
            self.assertEqual(g.u*g.v,x**3*(2-x)/4)
            self.assertEqual(g.discrim,x*x*(1-x)**2)
        self.assertEqual(SourceGeometry(Q(1)).discrim,0)

    def test_second_order_packet_recurrence_all_x(self):
        for x in (Q(0),Q(1,8),Q(1,2),Q(7,8),Q(1)):
            g=SourceGeometry(x)
            a=[g.grade_probability(j) for j in range(32)]
            for j in range(2,len(a)):
                self.assertEqual(a[j],x*a[j-1]-g.u*g.v*a[j-2])

    def test_double_root_finite_difference(self):
        for j in range(150):
            self.assertEqual(critical_rescaled_grade(j),j+1)
            self.assertEqual(critical_second_difference(j),0)
            self.assertEqual(critical_grade(j+2),
                             critical_grade(j+1)-critical_grade(j)/4)

    def test_minimum_causal_latency(self):
        for x in (Q(0),Q(1,3),Q(1)):
            sig=(Q(1),)+(Q(0),)*50
            e1,e2=run_two_stages(sig,x)
            self.assertEqual(e1[0],0)
            self.assertEqual(e2[0],0)
            self.assertEqual(e2[1],0)
            for t in range(len(sig)):
                self.assertEqual(e2[t],geometric_impulse_response(x,t))

    def test_arbitrary_source_exact_difference(self):
        for x in (Q(0),Q(1,3),Q(2,3),Q(1)):
            signal=[Q((t*t*3)%17-8,2*t+1) for t in range(28)]
            self.assertEqual(recurrence_residual(signal,x),(Q(0),)*len(signal))

    def test_depth_defect_exact_innovation_recursion(self):
        for x in (Q(0),Q(1,5),Q(1,2),Q(5,6),Q(1)):
            signal=[Q((t*t*3)%19-9,2*t+1) for t in range(45)]
            self.assertEqual(depth_defect_residual(signal,x),(Q(0),)*45)
            self.assertEqual(one_stage_forcing_residual(signal,x),(Q(0),)*45)

    def test_signed_discrepancy_not_necessarily_information_loss(self):
        for v in (Q(-1),Q(1)):
            signal=[Q(v),Q(0),Q(0),Q(0),Q(0)]
            a,b=run_two_stages(signal,Q(1))
            assert a[1]-b[1] == v*Q(1,2)
        self.assertNotEqual(run_two_stages([Q(1),Q(0)],Q(1)),
                            run_two_stages([Q(-1),Q(0)],Q(1)))

    def test_no_time_advance_in_filter(self):
        x=Q(3,5)
        signal_a=[Q(0)]*14
        signal_b=signal_a.copy()
        signal_b[-1]=Q(12345)
        _,E_a=run_two_stages(signal_a,x)
        _,E_b=run_two_stages(signal_b,x)
        self.assertEqual(E_a,E_b)

    def test_same_forcing_cannot_identify_bbp_seed(self):
        # The observer map only sees forcing; it cannot distinguish BBP U0.
        forcing=[Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
                 for n in range(1,9)]
        zero=Q(0); mutated=Q(1,7)
        for n,f in enumerate(forcing,1):
            zero=16*zero+f;mutated=16*mutated+f
            self.assertEqual(mutated-zero,Q(16**n,7))
        _,e2a=run_two_stages(forcing,Q(1))
        _,e2b=run_two_stages(forcing,Q(1))
        self.assertEqual(e2a,e2b)
        self.assertNotEqual(zero,mutated)

    def test_all_depth_binomial_hierarchy_but_only_depth2_source(self):
        for depth in range(1,7):
            for j in range(42):
                self.assertEqual(equal_stage_depth_difference(depth,j),0)
            pulse=[Q(1)]+[Q(0)]*70
            out=run_equal_stage_tower(pulse,depth)
            for t in range(len(out)):
                expected=equal_stage_critical_grade(depth,t-depth) if t>=depth else Q(0)
                self.assertEqual(out[t],expected)
        for j in range(30):
            self.assertEqual(equal_stage_critical_grade(2,j),critical_grade(j))

    def test_tower_depth_source_not_auto_extension(self):
        self.assertNotEqual(equal_stage_critical_grade(3,0),critical_grade(0))
        with self.assertRaises(ValueError):equal_stage_critical_grade(0,4)
        with self.assertRaises(ValueError):run_equal_stage_tower([Q(1)],-1)

    def test_third_stage_is_mutation_not_source(self):
        # A third independent Geom(1/2) would have coefficient C(j+2,2)/2^(j+3)
        # which already differs at j=0 from the actual source's w0=1/4.
        self.assertEqual(critical_grade(0),Q(1,4))
        self.assertNotEqual(critical_grade(0),Q(1,8))

class TestEpistemicControls(unittest.TestCase):
    def test_proper_past_sets(self):
        w=tuple(range(20))
        for t in range(2,20):
            oracle=finite_wavefront_past(w,t,0)
            e1=finite_wavefront_past(w,t,1)
            e2=finite_wavefront_past(w,t,2)
            self.assertTrue(set(e2).issubset(e1))
            self.assertTrue(set(e1).issubset(oracle))
            self.assertNotIn(w[t],e1)
            self.assertNotIn(w[t-1],e2)

    def test_stochastic_variance_defect_is_not_gamma(self):
        self.assertEqual(finite_memory_information_defects(9,3,Q(1)),
                         (Q(0),Q(1),Q(2),Q(3)))
        self.assertEqual(finite_memory_information_defects(9,3,Q(0)),
                         (Q(0),)*4)
        self.assertEqual(finite_memory_information_defects(9,3,Q(3,8)),
                         (Q(0),Q(3,8),Q(3,4),Q(9,8)))

    def test_invalid_budgets(self):
        with self.assertRaises(ValueError):finite_memory_information_defects(3,4)
        with self.assertRaises(ValueError):finite_wavefront_past((1,2),2,1)

if __name__=='__main__':unittest.main()
