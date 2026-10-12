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

    def test_h0_h1_match_independent_cech_linear_algebra(self):
        # Independent of cech_dimensions' closed form: build the Cech
        # differential delta(f0,f_inf) = f0(z) - z^k f_inf(1/z) as an exact
        # rational matrix on a Laurent window and read H0 = dim ker,
        # H1 = dim coker directly. Verified stable across two window sizes
        # so the result is not a truncation artifact (cf. the k=11,12 window
        # false positives that appear only for too-small windows).
        def _rank(rows, ncols):
            m=[list(r) for r in rows]; r=0
            for col in range(ncols):
                piv=next((i for i in range(r,len(m)) if m[i][col]!=0),None)
                if piv is None: continue
                m[r],m[piv]=m[piv],m[r]
                inv=F(1)/m[r][col]; m[r]=[x*inv for x in m[r]]
                for i in range(len(m)):
                    if i!=r and m[i][col]!=0:
                        f=m[i][col]; m[i]=[a-f*b for a,b in zip(m[i],m[r])]
                r+=1
                if r==len(m): break
            return r
        def _cohomology(k,N):
            ncols=2*(N+1); m_lo=min(0,k-N); m_hi=max(N,k)
            rows={d:[F(0)]*ncols for d in range(m_lo,m_hi+1)}
            for j in range(N+1):
                rows[j][j]+=F(1)                 # a_j contributes +z^j
                rows[k-j][(N+1)+j]+=F(-1)         # b_j contributes -z^(k-j)
            rk=_rank(list(rows.values()),ncols)
            return ncols-rk, len(rows)-rk          # (h0=dim ker, h1=dim coker)
        for k in range(-8,9):
            h0a,h1a=_cohomology(k,20)
            h0b,h1b=_cohomology(k,26)
            self.assertEqual((h0a,h1a),(h0b,h1b),f"window-unstable cohomology at k={k}")
            c=cech_dimensions(k)
            self.assertEqual(h0a,c['h0_dimension'],f"independent H0 != closed form at k={k}")
            self.assertEqual(h1a,c['h1_dimension'],f"independent H1 != closed form at k={k}")
            self.assertEqual(h0a-h1a,k+1,f"independent chi != k+1 at k={k}")

    def test_fake_source_degree_and_float_inputs_blocked(self):
        for k in (1.0,'2',None,10**6):
            with self.assertRaises(DualChartError):cech_dimensions(k)
        with self.assertRaises(DualChartError):cech_reduce(2,{0:.5})
        with self.assertRaises(DualChartError):glue_dual_sections(2,{-1:1},{})
        with self.assertRaises(DualChartError):glue_dual_sections(2,{0:1},{-1:1})

if __name__=='__main__':unittest.main()
