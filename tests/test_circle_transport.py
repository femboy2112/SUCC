"""Exact finite-to-Archimedean-circle torsion duality tests, zero free."""
from fractions import Fraction as Q
import unittest
import json
import subprocess
import sys

from observational_succ.core import BudgetExceeded, DomainError
from observational_succ.arithmetic import conductor_growth
from observational_succ.circle_transport import (
    FiniteClock, FiniteDualRefinement, CyclicOneObjectCategory,
    verify_refinement_tower, conductor_birth_2_to_6, mod1)


class CircleTransportTests(unittest.TestCase):
    def test_real_circle_torsion_embedding_and_successor(self):
        for m in [2,3,4,6,10,31]:
            c=FiniteClock(m)
            for j in range(m):
                self.assertEqual(c.torsion(j), Q(j,m))
                self.assertEqual(mod1(m*c.torsion(j)), Q(0))
                self.assertEqual(c.torsion(c.succ(j)),mod1(c.torsion(j)+Q(1,m)))
            self.assertEqual(c.succ(m-1),0)

    def test_exact_character_phase_addition(self):
        for m in [2,3,5,6,11,20]:
            c=FiniteClock(m)
            for j in range(m):
                for k in range(m):
                    self.assertEqual(c.phase(k+1,j),mod1(c.phase(k,j)+c.torsion(j)))

    def test_projection_dual_inclusion(self):
        for m,n in [(2,6),(3,12),(4,12),(5,10),(6,30)]:
            bridge=FiniteDualRefinement(m,n)
            report=bridge.verify_exhaustive()
            self.assertEqual(report['phase_checks'],m*n)
            for k in range(n):
                for j in range(m):
                    self.assertTrue(bridge.verify_phase(k,j))

    def test_clock_refinement_functor_directions(self):
        bridge=FiniteDualRefinement(2,6)
        p,d=bridge.functors()
        self.assertTrue(p.verify()['composable_pairs_checked']>0)
        self.assertTrue(d.verify()['composable_pairs_checked']>0)
        self.assertTrue(p.hom_faithfulness()['full'])
        self.assertFalse(p.hom_faithfulness()['faithful'])
        self.assertTrue(d.hom_faithfulness()['faithful'])
        self.assertFalse(d.hom_faithfulness()['full'])

    def test_exact_2_to_6_conductor_birth(self):
        result=conductor_birth_2_to_6()
        self.assertEqual(result['old_dual_indices'],[0,3])
        self.assertEqual(result['new_dimension'],4)
        self.assertEqual(result['new_exact_conductor_modes'],{3:[2,4],6:[1,5]})
        self.assertEqual(result['new_dimension'],conductor_growth(3)['innovation_rank'])

    def test_inverse_and_direct_towers(self):
        for m,n,r in [(2,6,30),(3,12,60),(2,4,12),(3,9,45)]:
            self.assertEqual(verify_refinement_tower(m,n,r)['status'],'verified_dual_tower')

    def test_false_character_inclusion_does_not_preserve_phases(self):
        bridge=FiniteDualRefinement(2,6)
        j=1
        k=1
        lhs=FiniteClock(2).phase(bridge.project(k),j)
        rhs=FiniteClock(6).phase(k,j)   # wrong: should be 3*j
        self.assertNotEqual(lhs,rhs)
        self.assertEqual(lhs,FiniteClock(6).phase(k,bridge.include_character(j)))

    def test_out_of_domain_or_resource_budget(self):
        with self.assertRaises(DomainError):
            FiniteDualRefinement(2,5)
        with self.assertRaises(BudgetExceeded):
            FiniteClock(10001)
        with self.assertRaises(BudgetExceeded):
            FiniteDualRefinement(30,300).verify_exhaustive(max_cells=100)
        with self.assertRaises(DomainError):
            FiniteClock(6).mod(Q(1,2))
        with self.assertRaises(DomainError):
            CyclicOneObjectCategory(6).hom('false','*')

    def test_public_cli_circle_transport(self):
        result=subprocess.run([sys.executable,'-m','observational_succ','circle-demo'],
                              text=True,capture_output=True,timeout=45)
        self.assertEqual(result.returncode,0,result.stderr)
        data=json.loads(result.stdout)
        self.assertEqual(data['conductor_birth']['new_dimension'],4)
        self.assertEqual(data['dual_tower']['status'],'verified_dual_tower')
        with self.assertRaises(BudgetExceeded):
            FiniteDualRefinement(2,1000).functors()

    def test_circle_angle_is_not_unrestricted_real_place(self):
        c=FiniteClock(6)
        self.assertTrue(c.torsion(1) in (Q(1,6),))
        # m-torsion is finite/countable, not the whole R/Z and has no Gamma.
        self.assertEqual({c.torsion(j) for j in range(6)},
                         {Q(j,6) for j in range(6)})
        self.assertFalse(hasattr(c,'gamma_factor'))


if __name__=="__main__":
    unittest.main()
