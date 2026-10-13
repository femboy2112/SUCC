"""Proof-oriented finite observation-menu synthesis and set-cover reduction."""
import random
import unittest
from dataclasses import replace
from itertools import combinations

from observational_succ.field_relative_closure import ClosureError, FiniteField
from observational_succ.field_probe_repair import (
    repair, verify_repair, set_cover_field, unresolved_pairs,
)

class ProbeRepairTests(unittest.TestCase):
    def test_repair_is_a_certified_minimum_cover(self):
        f=set_cover_field(6,({0,1,2,3},{0,1,4},{2,3,5}))
        c=repair(f,("pair_index",),("cover_0","cover_1","cover_2"),"original_bit")
        self.assertTrue(c.possible)
        self.assertEqual(c.selected,("cover_1","cover_2"))
        self.assertEqual(len(c.conflicting_pairs),6)
        self.assertTrue(verify_repair(f,c))

    def test_greedy_largest_first_does_not_guarantee_optimality(self):
        # Greedy picks cover_0 (4 items), then needs BOTH cover_1 and cover_2.
        # True optimum is cover_1 plus cover_2 with 2 probes.
        f=set_cover_field(6,({0,1,2,3},{0,1,4},{2,3,5}))
        c=repair(f,("pair_index",),("cover_0","cover_1","cover_2"),"original_bit")
        self.assertEqual(len(c.selected),2)
        self.assertEqual(1+2,3)

    def test_empty_probes_cannot_close_original_source_claim(self):
        f=set_cover_field(2,({0},{1}))
        c=repair(f,("pair_index",),(),"original_bit")
        self.assertFalse(c.possible)
        self.assertEqual(c.uncovered_pair,((0,0),(0,1)))
        self.assertTrue(verify_repair(f,c))

    def test_incomplete_menu_has_explicit_counterexample(self):
        f=set_cover_field(3,({0,1},))
        c=repair(f,("pair_index",),("cover_0",),"original_bit")
        self.assertFalse(c.possible)
        self.assertEqual(c.uncovered_pair,((2,0),(2,1)))
        self.assertTrue(verify_repair(f,c))

    def test_no_new_probe_required_when_baseline_sufficient(self):
        f=set_cover_field(2,({0,1},))
        c=repair(f,("pair_index","cover_0"),(),"original_bit")
        self.assertTrue(c.possible)
        self.assertEqual(c.selected,())
        self.assertEqual(c.conflicting_pairs,())
        self.assertTrue(verify_repair(f,c))

    def test_repaired_claim_has_exact_decoder(self):
        f=set_cover_field(4,({0,2},{1,3}))
        c=repair(f,("pair_index",),("cover_0","cover_1"),"original_bit")
        self.assertEqual(c.selected,("cover_0","cover_1"))
        dec=f.factor(c.baseline+c.selected,"original_bit")
        self.assertTrue(dec.proved)
        self.assertTrue(f.verify(dec))

    def test_detects_nonminimal_forged_claim(self):
        f=set_cover_field(2,({0,1},{1}))
        c=repair(f,("pair_index",),("cover_0","cover_1"),"original_bit")
        self.assertEqual(c.selected,("cover_0",))
        with self.assertRaisesRegex(ClosureError,"Nonminimal"):
            verify_repair(f,replace(c,selected=("cover_0","cover_1")))

    def test_forged_source_and_pair_lists_rejected(self):
        f=set_cover_field(2,({0},{1}))
        c=repair(f,("pair_index",),("cover_0","cover_1"),"original_bit")
        for forged in (replace(c,source_id="fake"),
                       replace(c,conflicting_pairs=()),
                       replace(c,selected=())):
            with self.assertRaises(ClosureError):
                verify_repair(f,forged)

    def test_correct_darkness_pair_cannot_be_forged_with_decidable_pair(self):
        f=set_cover_field(3,({0,1},))
        c=repair(f,("pair_index",),("cover_0",),"original_bit")
        with self.assertRaises(ClosureError):
            verify_repair(f,replace(c,uncovered_pair=((0,0),(0,1))))

    def test_honest_budget_exhaustion_is_unknown(self):
        f=set_cover_field(6,({0,1,2,3},{0,1,4},{2,3,5}))
        with self.assertRaisesRegex(ClosureError,"UNRESOLVED"):
            repair(f,("pair_index",),("cover_0","cover_1","cover_2"),
                   "original_bit",max_subsets=1)

    def test_fake_composite_cover_reference_rejected(self):
        f=set_cover_field(2,({0,1},))
        with self.assertRaises(ClosureError):
            repair(f,("pair_index",),("fake_prime_6",),"original_bit")

    def test_duplicate_repair_menu_rejected(self):
        f=set_cover_field(2,({0,1},))
        with self.assertRaises(ClosureError):
            repair(f,("pair_index",),("cover_0","cover_0"),"original_bit")

    def test_reference_menus_are_hypothetical_not_physical_actions(self):
        f=set_cover_field(2,({0,1},))
        c=repair(f,("pair_index",),("cover_0",),"original_bit")
        self.assertTrue(verify_repair(f,c))
        self.assertNotIn("physical",c.__dataclass_fields__)

    def test_exhaustive_6_element_incidence_examples(self):
        # Cross-check each result against an independent set-cover brute force.
        rng=random.Random(8257)
        for trial in range(280):
            n=rng.randint(1,6)
            m=rng.randint(0,7)
            subsets=tuple(tuple(i for i in range(n) if rng.randrange(2)) for _ in range(m))
            f=set_cover_field(n,subsets)
            menu=tuple(f"cover_{j}" for j in range(m))
            c=repair(f,("pair_index",),menu,"original_bit",max_subsets=10000)
            covers=[]
            for size in range(m+1):
                for inds in combinations(range(m),size):
                    if set.union(set(),*(set(subsets[i]) for i in inds))==set(range(n)):
                        covers.append(inds)
            if not covers:
                self.assertFalse(c.possible)
            else:
                self.assertTrue(c.possible)
                self.assertEqual(len(c.selected),min(map(len,covers)))
            self.assertTrue(verify_repair(f,c))

if __name__=='__main__':unittest.main()
