"""Independent finite group, true-prime and loop-killing control cases."""
import random
import unittest
from math import gcd
from itertools import combinations

from observational_succ.gaussian_holonomy import (
    GaussianSieve, HolonomyError, LiftedLoop, _LatticeHNF, _bezout,
    certify_single_loop_elimination, certify_simultaneous_elimination,
    limit_holonomy_warning, quotient_holonomy, verify_refinement_commutes,
    gaussian_prime, fucc_path_observations,
)


class GaussianHolonomyTests(unittest.TestCase):
    def test_baseline_unrestricted_grid_has_all_translation_holonomy(self):
        r=quotient_holonomy(GaussianSieve(()),1)
        self.assertEqual(r.period,1)
        self.assertEqual(r.rank,2)
        self.assertEqual(r.hermite_basis,((1,0),(0,1)))
        self.assertEqual(r.subgroup_index,1)
        self.assertIsNotNone(r.nonzero_cycle)

    def test_prime_5_unit_step_escapes_with_exact_index(self):
        r=quotient_holonomy(GaussianSieve(((1,2),)),1)
        self.assertEqual(r.surviving_residues,16)
        self.assertEqual(r.rank,2)
        self.assertEqual(r.hermite_basis,((5,0),(0,5)))
        self.assertEqual(r.subgroup_index,25)
        r.nonzero_cycle.verify(GaussianSieve(((1,2),)),1)

    def test_prime_5_and_17_still_escapes(self):
        s=GaussianSieve(((1,2),(1,4)))
        r=quotient_holonomy(s,1)
        self.assertEqual(r.period,85)
        self.assertEqual(r.surviving_residues,4096)
        self.assertEqual(r.rank,2)
        self.assertEqual(r.hermite_basis,((85,0),(0,85)))
        self.assertEqual(r.subgroup_index,85**2)
        r.nonzero_cycle.verify(s,1)

    def test_prime_5_and_13_exactly_confines(self):
        s=GaussianSieve(((1,2),(2,3)))
        r=quotient_holonomy(s,1)
        self.assertTrue(r.confined)
        self.assertEqual(r.rank,0)
        self.assertEqual(r.hermite_basis,())
        self.assertEqual(r.surviving_residues,2304)
        self.assertEqual(r.largest_finite_quotient_component,580)
        self.assertIsNone(r.nonzero_cycle)

    def test_sixteen_spanning_tree_and_signed_dart_check(self):
        # This path is a real 7-step SUCC loop mod 5 and is source-valid.
        s=GaussianSieve(((1,2),))
        path=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
        path.verify(s,1)
        self.assertEqual(path.displacement,(5,0))
        self.assertEqual(path.points[-1],(5,1))

    def test_one_new_13_factor_kills_repeat_at_index_one(self):
        s=GaussianSieve(((1,2),))
        path=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
        kill=certify_single_loop_elimination(s,path,1,(2,3))
        self.assertEqual(kill.norm,13)
        self.assertEqual(kill.forbidden_repetition_index,1)
        self.assertEqual(kill.cycle_length,7)
        self.assertEqual(kill.maximum_completed_cycles_before_forbidden,0)

    def test_new_17_factor_kills_old_template_but_leaves_other_escape(self):
        old=GaussianSieve(((1,2),))
        path=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
        kill=certify_single_loop_elimination(old,path,1,(1,4))
        self.assertEqual(kill.forbidden_repetition_index,6)
        self.assertEqual(kill.maximum_completed_cycles_before_forbidden,5)
        self.assertFalse(quotient_holonomy(GaussianSieve(((1,2),(1,4))),1).confined)

    def test_finite_catalogue_can_be_killed_simultaneously(self):
        s=GaussianSieve(((1,2),))
        r=quotient_holonomy(s,1)
        a=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
        b=r.nonzero_cycle
        kills=certify_simultaneous_elimination(s,(a,b),1,(1,4))
        self.assertEqual(len(kills),2)
        self.assertTrue(all(0<=x.forbidden_repetition_index<x.norm for x in kills))

    def test_projection_commutes_only_for_true_nested_source(self):
        coarse=GaussianSieve(((1,2),))
        fine=GaussianSieve(((1,2),(2,3)))
        a,b=(0,1),(1,1)
        self.assertTrue(fine.allowed(a) and fine.allowed(b))
        self.assertTrue(verify_refinement_commutes(coarse,fine,(a,b),1)['covariant'])
        with self.assertRaises(HolonomyError):
            verify_refinement_commutes(fine,coarse,(a,b),1)
        with self.assertRaises(HolonomyError):
            verify_refinement_commutes(coarse,fine,((0,0),(1,0)),1)
        with self.assertRaises(HolonomyError):
            verify_refinement_commutes(coarse,fine,(a,(2,1)),1)

    def test_nonprime_false_duplicate_and_resource_mutations(self):
        for factors in (((3,4),),((1,1),),((3,0),),((1,2),(2,1)),((1,2),(1,2))):
            with self.assertRaises(HolonomyError): GaussianSieve(factors)
        with self.assertRaisesRegex(HolonomyError,'budget'):
            GaussianSieve(((1,2),(1,4))).allowed_residues(max_cells=7000)
        with self.assertRaises(HolonomyError): quotient_holonomy(GaussianSieve(()),0)

    def test_reject_false_loop_and_new_factor_dividing_h(self):
        s=GaussianSieve(((1,2),))
        loop=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
        with self.assertRaises(HolonomyError): loop.verify(s,0)
        with self.assertRaises(HolonomyError): certify_single_loop_elimination(s,loop,1,(1,2))
        with self.assertRaises(HolonomyError): certify_single_loop_elimination(s,loop,1,(3,4))
        with self.assertRaises(HolonomyError): certify_simultaneous_elimination(s,(),1,(1,4))

    def test_nonzero_holonomy_survives_finite_expanding_moduli(self):
        z=limit_holonomy_warning((2,4,8,16))
        self.assertTrue(z['all_finite_stages_escaping'])
        self.assertIn('UNVERIFIED',z['intersection_zero_if_periods_unbounded'])
        with self.assertRaises(HolonomyError): limit_holonomy_warning((2,3))

    def test_extended_gcd_with_negative_offsets(self):
        for a in range(1,20):
            for b in range(-15,16):
                g,s,t=_bezout(a,b)
                self.assertEqual(g,gcd(a,b))
                self.assertEqual(s*a+t*b,g)

    def test_true_fucc_primality_does_not_equal_sieve_membership(self):
        for z,expected in [((2,1),True),((-1,2),True),((1,1),True),
                           ((0,3),True),((3,0),True),((0,7),True),
                           ((0,5),False),((3,4),False),((0,0),False),
                           ((2,2),False),((1,0),False)]:
            self.assertEqual(gaussian_prime(z),expected)
        sieve=GaussianSieve(((1,2),))
        r=fucc_path_observations(sieve,((1,2),(2,1),(3,0),(3,4)))
        self.assertTrue(r[0]['exceptional_prime'])
        self.assertTrue(r[1]['exceptional_prime'])
        self.assertFalse(r[2]['exceptional_prime'])
        self.assertFalse(r[3]['gaussian_prime'])
        with self.assertRaises(HolonomyError):gaussian_prime((2.2,1))

    def test_hermite_index_vs_independent_pairwise_minors(self):
        rng=random.Random(97431)
        for _ in range(280):
            v=[(rng.randint(-8,8),rng.randint(-8,8)) for i in range(rng.randint(1,8))]
            l=_LatticeHNF()
            for h in v:l.add(h)
            determinants=[abs(x[0]*y[1]-x[1]*y[0]) for x,y in combinations(v,2)]
            g=0
            for det in determinants:g=gcd(g,det)
            if g:
                self.assertEqual(l.rank,2)
                self.assertEqual(l.index,g)
                self.assertEqual(abs(l.basis[0][0]*l.basis[1][1]),g)
            elif any(x!=(0,0) for x in v):
                self.assertEqual(l.rank,1)
                self.assertIsNone(l.index)
            else:
                self.assertEqual(l.rank,0)


if __name__=='__main__':
    unittest.main()
