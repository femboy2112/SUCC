from fractions import Fraction as Q
from collections import Counter
import unittest
from cylinder_probe import (
    source,tail_interval,tail_difference_interval,centered,distance,
    classify_interval,digits,word_bound,transitions,bbp_words,
    stoneham_surrogate,stoneham_stage,stoneham_energy_bound_parts,
    walsh_refinement,debruijn,DELTA,
)


class CylinderTests(unittest.TestCase):
    def test_authentic_source_and_threshold_gates(self):
        self.assertEqual(source(1),Q(47,15))
        self.assertEqual(source(2),Q(106,819))
        self.assertLess(DELTA+Q(16,17**3),Q(1,17))
        self.assertLess(Q(15,4096)+Q(16,17**3),DELTA)

    def test_lag_conjugacy_for_truncated_tail(self):
        for n in (1,2,13,47):
            t=tail_interval(n,10)[0]
            tnext=tail_interval(n+1,9)[0]
            self.assertEqual(16*t-tnext,source(n+1))
            u=Q(7,19)
            self.assertEqual(15*u+source(n+1),15*(u+t)+t-tnext)

    def test_safe_interval_threshold_and_seams(self):
        self.assertFalse(classify_interval(Q(99,100),Q(101,100)))
        self.assertTrue(classify_interval(Q(9,20),Q(11,20)))
        self.assertIsNone(classify_interval(DELTA-Q(1,1000),DELTA+Q(1,1000)))

    def test_genuine_source_digits_and_implication(self):
        _,word,slip=bbp_words(128)
        self.assertEqual(word[:8],(2,4,3,15,6,10,8,8))
        for A in range(2,110):
            self.assertLessEqual(transitions(word[A-1:A+15]),2*sum(slip[A-1:A+15]))
            self.assertLessEqual(sum(slip[A-1:A+15]),2*transitions(word[A-1:A+15])+2)

    def test_reverse_inclusion_and_necessary_extra_digits(self):
        self.assertEqual(digits(Q(1,32),1),(0,))
        self.assertGreater(distance(15*Q(1,32)),DELTA)
        for d in range(16):
            y=Q(d*(16**6-1),15*16**6)+Q(9,17*16**6)
            for n in range(2,6):
                lo,hi=tail_difference_interval(n)
                self.assertFalse(classify_interval(15*y+lo,15*y+hi))
                y=16*y % 1

    def test_every_position_period_two_slip(self):
        for n in range(2,70):
            y=Q(1 if n%2 else 16,255)
            lo,hi=tail_difference_interval(n)
            self.assertTrue(classify_interval(15*y+lo,15*y+hi))
            self.assertEqual(distance(15*y),Q(1,17))
            self.assertEqual((17*y) % 1,Q(1,15))

    def test_word_cover_enumeration(self):
        self.assertEqual(word_bound(1,0),16)
        self.assertEqual(word_bound(4,0),16)
        self.assertEqual(word_bound(3,1),16**3)
        self.assertLess(word_bound(10,1),16**10)

    def test_stoneham_actual_grid_and_partial_multiplicity(self):
        for c,p in ((3,3),(5,2)):
            full=stoneham_stage(c,p)
            q=c**p
            self.assertEqual(set(full),{Q(1+c*j,q) for j in range(q//c)})
            for length in (1,7,len(full)//2,len(full)-1):
                self.assertLessEqual(max(Counter(full[:length]).values()),c*(c-1))

    def test_stoneham_two_radix_obstruction(self):
        self.assertNotEqual(len(set(stoneham_stage(2,3))),4)
        with self.assertRaises(ValueError):
            stoneham_energy_bound_parts(2,100,8)

    def test_walsh_all_contexts_and_all_masks(self):
        for cycle in ((0,1),debruijn()):
            for depth in range(6):
                a,b,d,masks=walsh_refinement(cycle,depth)
                self.assertEqual(b-a,d)
                self.assertEqual(masks,15)
        self.assertEqual(walsh_refinement(debruijn(),1)[:2],(1,1))
        self.assertEqual(walsh_refinement(debruijn(),2)[:2],(1,16))


if __name__=='__main__':
    unittest.main(verbosity=2)
