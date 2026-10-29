"""Cross-check imported local Hopf source against SUCC Main XIII rank-two code.

When run on a complete SUCC worktree this test must exercise the real
main code. It skips only when the source module is genuinely unavailable
in an isolated local scratch copy.
"""
from fractions import Fraction as F
import unittest
from observational_succ.hopf_source_exact import (
    t_iter,SOURCE_ORIGIN,source_tap,source_moment,
    unwrapped_zero_seed,pole_quaternion,
)
try:
    from observational_succ import rank_two_chiral_towers as main_rank
except ImportError:
    main_rank=None

class PinnedMainSourceBridge(unittest.TestCase):
    @unittest.skipIf(main_rank is None,"complete SUCC source unavailable in isolated local scratch copy")
    def test_chiral_successor_matches_real_main(self):
        for n in range(0,66):
            state=main_rank.iterate(main_rank.ORIGIN,n)
            q=t_iter(SOURCE_ORIGIN,n)
            self.assertEqual((state.left.re,state.left.im,state.right.re,state.right.im),tuple(q))
            self.assertEqual(main_rank.source_readout(state),source_tap(q))

    @unittest.skipIf(main_rank is None,"complete SUCC source unavailable in isolated local scratch copy")
    def test_source_moments_zero_seed_and_original_four_poles(self):
        for n in range(1,65):
            self.assertEqual(main_rank.source_moment(n),source_moment(n))
            self.assertEqual(main_rank.authentic_four_poles(n),sum(tuple(pole_quaternion(n)),F(0)))
        for n in range(0,40):
            self.assertEqual(main_rank.original_zero_seed_prefix(n),unwrapped_zero_seed(n))
