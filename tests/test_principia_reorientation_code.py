import unittest
from dataclasses import replace
from observational_succ.principia_reorientation import (
    ring_with_beacon,ring_with_unknown_heading,homogeneous_ring,ReorientationError
)
from observational_succ.principia_reorientation_code import (
    make_local_code,verify_local_code,guaranteed_error_budget,
    decode_with_bounded_errors,hamming
)


class RobustReorientationTests(unittest.TestCase):
    def test_a_complete_clock_lap_separates_known_positions(self):
        n=6; task=ring_with_beacon(n)
        c=make_local_code(task,('forward',)*n)
        self.assertEqual(c.min_target_distance,2)
        self.assertEqual(guaranteed_error_budget(task,c),0)

    def test_two_laps_correct_one_adversarial_false_report(self):
        for n in (4,5,6,8):
            task=ring_with_beacon(n)
            code=make_local_code(task,('forward',)*(2*n))
            self.assertEqual(code.min_target_distance,4)
            self.assertEqual(guaranteed_error_budget(task,code),1)
            for w,target,word in code.signatures:
                self.assertEqual(decode_with_bounded_errors(task,code,word,1),target)
                for i in range(len(word)):
                    flipped=tuple(('beacon' if y=='dark' else 'dark') if j==i else y
                                  for j,y in enumerate(word))
                    self.assertEqual(decode_with_bounded_errors(task,code,flipped,1),target)

    def test_e_plus_one_full_laps_correct_e_errors(self):
        for e in (0,1,2,3):
            n=5; task=ring_with_beacon(n)
            code=make_local_code(task,('forward',)*(n*(e+1)))
            self.assertGreaterEqual(code.min_target_distance,2*e+1)
            self.assertGreaterEqual(guaranteed_error_budget(task,code),e)

    def test_one_lap_has_overlapping_one_error_balls(self):
        task=ring_with_beacon(6)
        code=make_local_code(task,('forward',)*6)
        a,b=next((a,b) for a in code.signatures for b in code.signatures
                 if a[0]!=b[0] and hamming(a[2],b[2])==2)
        differences=[i for i,(x,y) in enumerate(zip(a[2],b[2])) if x!=y]
        self.assertEqual(len(differences),2)
        midpoint=list(a[2]);midpoint[differences[0]]=b[2][differences[0]]
        self.assertEqual(hamming(a[2],midpoint),1)
        self.assertEqual(hamming(b[2],midpoint),1)
        with self.assertRaises(ReorientationError):
            decode_with_bounded_errors(task,code,tuple(midpoint),1)

    def test_reflection_gauge_cannot_be_repaired_by_more_redundancy(self):
        task=ring_with_unknown_heading(5,side_marker=False,coordinate='pose')
        for laps in (1,2,3):
            c=make_local_code(task,('forward',)*(5*laps))
            self.assertEqual(c.min_target_distance,0)
            self.assertEqual(guaranteed_error_budget(task,c),-1)

    def test_asymmetric_landmark_breaks_gauge_with_enough_data(self):
        task=ring_with_unknown_heading(5,side_marker=True,coordinate='pose')
        for laps in (2,4):
            c=make_local_code(task,('forward',)*(5*laps))
            self.assertGreaterEqual(c.min_target_distance,2)
        c=make_local_code(task,('forward',)*20)
        self.assertGreaterEqual(guaranteed_error_budget(task,c),1)

    def test_reset_discards_original_origin_but_locates_current(self):
        task=homogeneous_ring(6,reset=True,mode='current')
        c=make_local_code(task,('reset',))
        self.assertIsNone(c.min_target_distance)
        self.assertIsNone(guaranteed_error_budget(task,c))
        self.assertEqual(decode_with_bounded_errors(task,c,('dark','dark'),0),'x0')
        original=homogeneous_ring(6,reset=True,mode='initial')
        c2=make_local_code(original,('reset',))
        self.assertEqual(c2.min_target_distance,0)

    def test_wrong_source_and_insufficient_report_declined(self):
        task=ring_with_beacon(5)
        c=make_local_code(task,('forward',)*10)
        with self.assertRaises(ReorientationError):verify_local_code(task,replace(c,source='fake'))
        with self.assertRaises(ReorientationError):decode_with_bounded_errors(task,c,('beacon',),1)
        with self.assertRaises(ReorientationError):decode_with_bounded_errors(task,c,('unknown',)*11,0)


if __name__=='__main__':unittest.main()
