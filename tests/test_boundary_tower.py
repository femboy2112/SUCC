import unittest
from fractions import Fraction as F
from itertools import product
from observational_succ.boundary_tower import (
    BoundaryError, BoundaryLevel, PhaseRing, verify_ring_tower,
    refine_piecewise_linear,circle_distance,normalized_finite_valuations,
    arch_abs_from_places,check_rational_product_formula,
    order_of_limits_countermodel,harmonic_laurent_eval,
    holomorphic_boundary_admissible, monodromy_section_report)

class BoundaryTowerTests(unittest.TestCase):
    def test_dyadic_ring_refinement_exact(self):
        a=BoundaryLevel(1,'original','v1',(F(0),F(1,2)))
        levels=(a,)
        for i in range(4):levels+= (refine_piecewise_linear(levels[-1]),)
        c=verify_ring_tower(levels,F(1))
        self.assertEqual(c['sample_count'],32)
        self.assertEqual(c['boundary_sup_error_budget'],F(1,64))
        self.assertEqual(c['interior_sup_error_budget'],F(1,64))
        for t in (F(0),F(1,5),F(1,3),F(17,20),F(1)):
            self.assertEqual(levels[-1].at(t),a.at(t))

    def test_exact_stage_interpolation_and_circular_seam(self):
        x=BoundaryLevel(2,'s','basis',(F(0),F(1,4),F(1,2),F(1,4)))
        self.assertEqual(x.at(F(1,8)),F(1,8))
        self.assertEqual(x.at(F(7,8)),F(1,8))
        self.assertEqual(x.at(F(1)),x.at(F(0)))
        self.assertEqual(circle_distance(F(7,8),F(1,8)),F(1,4))
        self.assertEqual(verify_ring_tower((BoundaryLevel(1,'s','basis',(F(0),F(1,2))),x),F(1))['boundary_sup_error_budget'],F(1,8))

    def test_forged_source_basis_and_vertical_mutations(self):
        a=BoundaryLevel(1,'s','basis',(F(0),F(1,2)))
        with self.assertRaisesRegex(BoundaryError,'source/basis'):
            verify_ring_tower((a,BoundaryLevel(2,'different','basis',(0,F(1,4),F(1,2),F(1,4)))),F(1))
        with self.assertRaisesRegex(BoundaryError,'Vertical'):
            verify_ring_tower((a,BoundaryLevel(2,'s','basis',(0,F(1,4),0,F(1,4)))),F(1))
        with self.assertRaisesRegex(BoundaryError,'horizontal'):
            a.verify_lipschitz_edges(F(1,4))
        with self.assertRaises(BoundaryError):
            BoundaryLevel(1,'s','basis',(0,.5))

    def test_constant_data_not_complete_without_bound(self):
        a=BoundaryLevel(2,'s','basis',(0,0,0,0))
        self.assertEqual(a.at(F(1,8)),0)
        # Different global L-Lipschitz extensions agree on all four points.
        # A tent on one interval peaks at L*h/2; finite readings aren't unique.
        self.assertEqual(verify_ring_tower((BoundaryLevel(1,'s','basis',(0,0)),a),F(1))['boundary_sup_error_budget'],F(1,8))

    def test_phase_winding_and_ambiguity(self):
        for q in (8,16,32):
            n=q.bit_length()-1
            for degree in (-2,-1,0,1,2):
                if 2*abs(degree)>=q:continue
                ph=PhaseRing(n,tuple(F(k*degree,q) for k in range(q)))
                self.assertEqual(ph.winding(),degree)
        with self.assertRaisesRegex(BoundaryError,'Antipodal'):
            PhaseRing(1,(F(0),F(1,2))).winding()
        self.assertEqual(PhaseRing(3,tuple(F(2*k,8) for k in range(8))).winding()%2,0)

    def test_rational_product_formula_and_sign_alias(self):
        for numerator,denominator in product(range(-12,13),range(1,9)):
            if numerator==0:continue
            q=F(numerator,denominator)
            x=check_rational_product_formula(q)
            self.assertEqual(x['arch_magnitude'],abs(q))
            self.assertEqual(x['finite_exponents'],normalized_finite_valuations(-q))
        self.assertEqual(arch_abs_from_places({2:3,3:-2}),F(8,9))
        with self.assertRaisesRegex(BoundaryError,'finite rational places'):
            arch_abs_from_places({6:1})

    def test_double_limit_does_not_commute(self):
        for n in range(1,12):
            self.assertEqual(order_of_limits_countermodel(n,n+1),1)
            self.assertEqual(order_of_limits_countermodel(n+1,n),0)
        self.assertEqual(order_of_limits_countermodel(5,100),1)
        self.assertEqual(order_of_limits_countermodel(100,5),0)

    def test_exact_harmonic_extension_and_holomorphic_boundary_gate(self):
        f={1:(F(3,2),F(0)),-1:(F(0),F(2))}
        self.assertFalse(holomorphic_boundary_admissible(f))
        val=harmonic_laurent_eval(f,F(3,5),F(1,5))
        # 3/2 z + 2i * conj(z)
        self.assertEqual(val,(F(13,10),F(3,2)))
        g={0:(F(1),F(0)),1:(F(2),F(1)),3:(F(-1),F(0))}
        self.assertTrue(holomorphic_boundary_admissible(g))
        self.assertEqual(harmonic_laurent_eval({-1:(F(1),F(0))},F(1,3),F(1,4)),(F(1,3),-F(1,4)))
        with self.assertRaises(BoundaryError):harmonic_laurent_eval(g,F(1),F(0))

    def test_fixed_point_holonomy_and_claim_descent_separate(self):
        swap=monodromy_section_report((1,0),("same","same"))
        self.assertTrue(swap['nontrivial_holonomy'])
        self.assertEqual(swap['parallel_global_states'],())
        self.assertTrue(swap['claim_descends'])
        self.assertFalse(monodromy_section_report((1,0),("yes","no"))['claim_descends'])
        with_fixed=monodromy_section_report((1,0,2),("a","a","b"))
        self.assertEqual(with_fixed['parallel_global_states'],(2,))
        self.assertTrue(with_fixed['claim_descends'])
        self.assertEqual(len(with_fixed['orbits']),2)
        full=monodromy_section_report((0,1,2),("a","b","c"))
        self.assertEqual(full['parallel_global_states'],(0,1,2))
        self.assertTrue(full['claim_descends'])
        with self.assertRaises(BoundaryError):
            monodromy_section_report((1,1),("a","b"))

    def test_holomorphic_alias_for_any_finite_root_grid(self):
        # z**q -1 and 0 agree at all q-th roots; at center they differ by -1.
        for depth in range(1,6):
            q=1<<depth
            modes={q:(F(1),F(0)),0:(F(-1),F(0))}
            self.assertTrue(holomorphic_boundary_admissible(modes))
            self.assertEqual(harmonic_laurent_eval(modes,F(0),F(0)),(F(-1),F(0)))
            # Exact rational roots for q=4 are ±1,±i. Degree q alias is true generally by ζ**q=1.
        q=4
        for x,y in ((1,0),(0,1),(-1,0),(0,-1)):
            z=(F(x),F(y));pot=(F(1),F(0))
            from observational_succ.boundary_tower import complex_mul
            for _ in range(q):pot=complex_mul(pot,z)
            self.assertEqual(pot,(F(1),F(0)))

if __name__=='__main__':unittest.main()
