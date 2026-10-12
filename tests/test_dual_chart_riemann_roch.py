"""Exact projective dual-circle descent and genuinely nontrivial H1 obstructions."""
import sys,unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.dual_chart_riemann_roch import (
  DualChartError,cech_dimensions,glue_dual_sections,dual_chart_from_global,cech_reduce)

class DualChartRiemannRochTests(unittest.TestCase):
    def test_riemann_roch_dimensions_all_signed_twists(self):
        for k in range(-12,13):
            c=cech_dimensions(k)
            self.assertEqual(c['h0_dimension'],max(k+1,0))
            self.assertEqual(c['h1_dimension'],max(-k-1,0))
            self.assertEqual(c['euler_characteristic'],k+1)
            self.assertTrue(c['genus_zero_rr_verified'])

    def test_degree_zero_only_constants_even_when_charts_have_local_freedom(self):
        self.assertEqual(cech_dimensions(0)['global_section_monomials'],(0,))
        self.assertTrue(glue_dual_sections(0,{0:7},{0:7})['compatible'])
        self.assertFalse(glue_dual_sections(0,{1:1},{})['compatible'])
        self.assertFalse(glue_dual_sections(0,{},{1:1})['compatible'])

    def test_global_degree_two_is_three_dimensional(self):
        c=dual_chart_from_global(2,{0:F(1),1:F(2),2:F(3)})
        self.assertEqual(c['infinity_chart'],{0:F(3),1:F(2),2:F(1)})
        self.assertTrue(c['nontrivial_global_section'])
        self.assertEqual(c['allowed_global_modes'],(0,1,2))
        self.assertTrue(glue_dual_sections(2,c['zero_chart'],c['infinity_chart'])['compatible'])

    def test_negative_twist_rejects_any_nonzero_global_section(self):
        for k in (-1,-2,-3,-5):
            self.assertEqual(cech_dimensions(k)['h0_dimension'],0)
            self.assertFalse(glue_dual_sections(k,{0:1},{})['compatible'])
            self.assertTrue(dual_chart_from_global(k,{})['compatible'])
            with self.assertRaises(DualChartError):dual_chart_from_global(k,{0:1})

    def test_h1_nontrivial_even_when_both_charts_are_locally_legal(self):
        c=cech_reduce(-2,{-1:F(1)})
        self.assertEqual(c['obstruction_class'],{-1:F(1)})
        self.assertFalse(c['coboundary'])
        self.assertEqual(c['h1_dimension'],1)
        self.assertEqual(cech_reduce(-3,{-2:1,-1:2})['h1_dimension'],2)
        self.assertTrue(cech_reduce(-1,{0:2,-3:4})['coboundary'])

    def test_exact_cech_reduction_reconstructs_general_laurent(self):
        for k in range(-4,5):
            for coeff in product((-1,0,1),repeat=5):
                poly={j:c for j,c in zip(range(-2,3),coeff) if c}
                report=cech_reduce(k,poly)
                self.assertEqual(set(report['obstruction_class']).intersection(range(0,5)),set())
                self.assertEqual(report['coboundary'],
                    not any(k<j<0 for j in poly))

    def test_obstruction_invariant_under_local_coboundaries(self):
        k=-3
        raw={-2:F(7),-1:F(5),3:F(1),-4:F(2)}
        base=cech_reduce(k,raw)
        mutated=dict(raw)
        for n,c in ((0,F(100)),(7,F(2)),(-4,F(5)),(-8,F(-7))):
            mutated[n]=mutated.get(n,0)+c
        result=cech_reduce(k,mutated)
        self.assertEqual(base['obstruction_class'],result['obstruction_class'])
        self.assertEqual(base['obstruction_class'],{-2:F(7),-1:F(5)})

    def test_sheaf_transition_is_not_raw_equality(self):
        a=dual_chart_from_global(3,{0:1,2:4,3:7})
        self.assertNotEqual(a['zero_chart'],a['infinity_chart'])
        self.assertTrue(a['compatible'])
        self.assertEqual(a['infinity_chart'],{0:7,1:4,3:1})

    def test_fake_source_degree_and_float_inputs_blocked(self):
        for k in (1.0,'2',None,10**6):
            with self.assertRaises(DualChartError):cech_dimensions(k)
        with self.assertRaises(DualChartError):cech_reduce(2,{0:.5})
        with self.assertRaises(DualChartError):glue_dual_sections(2,{-1:1},{})
        with self.assertRaises(DualChartError):glue_dual_sections(2,{0:1},{-1:1})

if __name__=='__main__':unittest.main()
