"""Exact rational SUCC circle/diameter path quotient and BBP source firewalls."""
import importlib.util
import pathlib
import sys
import unittest
from fractions import Fraction as F
from math import isqrt

ROOT=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'circle_path_ratio'

def load_unique(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

m=load_unique('succ_circle_ratio_'+str(id(object())),'circle_ratio.py')
o=load_unique('succ_circle_oracle_'+str(id(object())),'independent_oracle.py')

class Tests(unittest.TestCase):
    def test_wrong_sqrt(self):
        with self.assertRaises(m.CarrierError):m.sqrt_out(F(-1))
    def test_noninteger_flag(self):
        with self.assertRaises(m.CarrierError):m.chord_square_intervals(True)
    def test_sqrt_exact_square(self):
        self.assertEqual(m.sqrt_out(F(9,16)),(F(3,4),F(3,4)))
    def test_sqrt_outbound(self):
        lo,hi=m.sqrt_out(F(2),digits=35)
        self.assertLess(lo*lo,2)
        self.assertGreater(hi*hi,2)
    def test_chord_first(self):
        self.assertEqual(m.chord_square_intervals(0),m.Bound(F(4),F(4)))
        self.assertEqual(m.chord_square_intervals(1),m.Bound(F(2),F(2)))
    def test_polygon_k1(self):
        self.assertLess(m.polygon_pi_interval(1).lo,3)
        self.assertGreater(m.polygon_bracket(1).hi,F(39,10))
    def test_polygon_nested_positive(self):
        for k in range(1,13):
            x=m.chord_square_intervals(k)
            self.assertGreater(x.lo,0)
            self.assertLess(x.hi,4+F(1,10**75))
    def test_polygon_monotone_with_certified_ranges(self):
        vals=[m.polygon_pi_interval(k,100) for k in range(1,9)]
        for a,b in zip(vals,vals[1:]):self.assertLess(a.hi,b.lo)
    def test_polygon_upper_lower(self):
        for k in (1,2,3,4,7,10):
            x=m.polygon_bracket(k)
            self.assertLess(x.lo,x.hi)
            self.assertLess(x.hi,4+F(1,10**75))
    def test_source_two_implementations(self):
        for n in range(1,35):self.assertEqual(m.bbp_r(n),m.bbp_r_combined(n))
    def test_source_independent_oracle(self):
        for n in range(1,35):self.assertEqual(m.bbp_r(n),o.source_oracle(n))
    def test_source_positive_decreasing(self):
        for n in range(1,35):self.assertGreater(m.bbp_r(n),m.bbp_r(n+1))
    def test_source_bounds(self):
        for n in range(1,26):
            self.assertGreaterEqual(m.bbp_r(n+1),F(4,(8*n+1)*(8*n+2)))
            self.assertLess(m.bbp_r(n+1),F(15,64*n*n))
    def test_initial_true_source(self):
        self.assertEqual(m.bbp_r(1),F(47,15))
        self.assertEqual(m.bbp_r(2),F(106,819))
    def test_wilson_first(self):self.assertEqual(m.wilson_defect(1),F(12301,273))
    def test_wilson_decay(self):
        for n in range(1,28):
            self.assertGreater(m.wilson_defect(n),m.wilson_defect(n+1))
    def test_curvature_telescope(self):
        for n in range(1,31):
            self.assertEqual(sum((m.wilson_defect(j) for j in range(1,n)),F()),47-15*m.bbp_r(n))
    def test_wilson_short_identity(self):
        for n in range(1,29):
            self.assertEqual(m.wilson_upper(n),m.wilson_upper_faster(n))
    def test_wilson_independent(self):
        for n in range(1,25):self.assertEqual(m.wilson_upper(n),o.first_wilson(n))
    def test_wilson_upper_gt_bbp(self):
        for n in range(1,25):self.assertGreater(m.wilson_upper(n),m.bbp_lower(n))
    def test_bbp_orbit_double(self):
        for n in range(1,20):self.assertEqual(m.affine_orbit(n),o.bbp_oracle(n))
    def test_seed_affine(self):
        for n in range(1,20):
            self.assertEqual(m.affine_orbit(n,F(1,5))-m.affine_orbit(n),16**n*F(1,5))
    def test_radix_double_first(self):
        self.assertEqual(o.tangent_double_homogeneous(F(1,2),F(1)),(F(1),F(3,4)))
    def test_tangent_sum_associative(self):
        a,b,c=F(1,3),F(1,5),F(1,7)
        x1=o.angle_add_homogeneous(*o.angle_add_homogeneous(a,1,b,1),c,1)
        x2=o.angle_add_homogeneous(a,1,*o.angle_add_homogeneous(b,1,c,1))
        self.assertEqual(x1[0]*x2[1],x2[0]*x1[1])
    def test_projective_16(self):
        # independent binomial polynomial oracle, not the same recursive implementation
        for a,b in ((F(1,3),F(1)),(F(1),F(1)),(F(7,11),F(5)),(F(1),F(0))):
            self.assertEqual(o.radix16_homogeneous(a,b),o.radix16_pair_by_binomial(a,b))
    def four(self,a,b):
        for _ in range(4):a,b=o.tangent_double_homogeneous(a,b)
        return a,b
    def test_pi_geometric_and_bbp_bridge(self):
        for n in range(1,10):
            c=m.bridge_certificate(n,95)
            self.assertLess(c['bbp_lower'],c['polygon_lower_interval'].lo)
            self.assertGreater(c['certified_upper'],c['polygon_lower_interval'].hi)
            if n==1:self.assertGreater(c['polygon_lower_interval'].lo,F(392,125))
            self.assertEqual(c['certified_upper'],min(c['polygon_upper'],c['wilson_upper']))
    def test_analytic_bridge_threshold(self):
        for n in range(2,75):
            self.assertGreater(3*16**n,2*(8*n+1)*(8*n+2))
    def test_bbp_tail_bounds_independent(self):
        for n in range(1,70):
            self.assertLess(m.bbp_tail_lower(n),m.bbp_tail_upper(n))
    def test_polygon_higher_refinements(self):
        prev=m.polygon_pi_interval(4).lo
        for k in range(5,20):
            cur=m.polygon_pi_interval(k,100).lo
            self.assertGreater(cur,prev)
            prev=cur
    def test_radix16_group_law(self):
        for a,b in ((F(1,7),F(1,1)),(F(2,3),F(1,4)),(F(3,2),F(5,11))):
            x,y=o.radix16_homogeneous(a,b)
            self.assertEqual(o.circle_cayley(x,y),o.circle_power(o.circle_cayley(a,b),16))
    def test_poly_relations(self):
        self.assertEqual(m.source_step_laurent_poles(),(F(7,8),F(1,2),F(3,8),F(1,4)))

    def test_heat_ratio_pi_polygon_k1(self):
        # 2 equal upper-semicircle chords, each sqrt(2): polyline length²=8.
        for t in (F(1,7),F(3,2),F(99)):
            self.assertEqual(o.free_heat_log_ratio(F(8),t),F(2,t))
            self.assertEqual(o.normalized_heat_square_quotient(F(8),F(4),t),F(2))
    def test_heat_ratio_normalization_cancels(self):
        for a,b in ((F(7,3),F(2)),(F(17,7),F(5,2))):
            val=o.normalized_heat_square_quotient(a*a,b*b,F(19,11))
            self.assertEqual(val,(a/b)**2)
    def test_heat_regulator_positive(self):
        with self.assertRaises(ValueError):o.free_heat_log_ratio(F(9),F(0))
    def test_polygon_source_strict_interleaving(self):
        # The rational original Wilson upper and authentic BBP lower bracket
        # the actual independent geometry path quotient at every tested depth.
        for n in range(1,11):
            c=m.bridge_certificate(n,100)
            self.assertLess(c['bbp_lower'],c['polygon_lower_interval'].lo)
            self.assertLess(c['polygon_lower_interval'].hi,c['wilson_upper'])
            self.assertLess(c['polygon_lower_interval'].hi-c['bbp_lower'],c['bbp_tail_upper'])
    def test_wilson_bridge_width(self):
        for n in range(1,22):
            self.assertEqual(m.wilson_upper(n)-m.bbp_lower(n),F(16,15*16**n)*m.bbp_r(n+1))
    def test_homogeneous_infinity(self):
        # Rational 2× map has genuine projective poles, not discarded states.
        self.assertEqual(o.tangent_double_homogeneous(F(1),F(1)),(F(2),F(0)))
        self.assertEqual(o.circle_cayley(F(1),F(0)),(F(-1),F(0)))
        self.assertEqual(o.circle_cayley(*o.radix16_homogeneous(F(1),F(0))),(F(1),F(0)))
    def test_circle_unit_norm(self):
        for a,b in ((F(0),F(1)),(F(1),F(0)),(F(3),F(5)),(F(-7),F(9))):
            x,y=o.circle_cayley(a,b)
            self.assertEqual(x*x+y*y,1)
    def test_circle_angle_mobius(self):
        for a,b,c,d in ((F(2),F(3),F(5),F(7)),(F(1),F(0),F(1),F(1))):
            e,f=o.angle_add_homogeneous(a,b,c,d)
            self.assertEqual(o.circle_cayley(e,f),o.circle_product(o.circle_cayley(a,b),o.circle_cayley(c,d)))


    def test_odd_source_denominators(self):
        for n in range(1,33):
            self.assertEqual(m.bbp_r(n).denominator%2,1)
            self.assertEqual(m.affine_orbit(n).denominator%2,1)
    def test_combined_cyclotomic_conductor(self):
        for n in range(1,10):
            for k in (0,1,4,8):
                c=m.crt_joint_carrier(k,n)
                self.assertEqual(c['geometry_2power'],2**(k+2))
                self.assertEqual(c['bbp_odd']%2,1)
                self.assertEqual(c['combined'],c['geometry_2power']*c['bbp_odd'])
    def test_crt_reconstruct_samples(self):
        for n in range(1,7):
            c=m.crt_joint_carrier(4,n)
            a,b=c['geometry_2power'],c['bbp_odd']
            for x in (0,1,3,11,a,b,a*b-1):
                self.assertEqual(m.crt_reconstruct(x%a,x%b,a,b),x%(a*b))
    def test_crt_invalid(self):
        with self.assertRaises(m.CarrierError):m.crt_reconstruct(1,1,4,2)
        with self.assertRaises(m.CarrierError):m.crt_reconstruct(1,1,0,3)

    def test_invalid_bounds(self):
        with self.assertRaises(m.CarrierError):m.bbp_r(0)
        with self.assertRaises(m.CarrierError):m.polygon_bracket(0)
        with self.assertRaises(m.CarrierError):m.Bound(F(2),F(1))

if __name__=='__main__':unittest.main()
