"""Authenticated Suzuki prime-power diagonal hinge quadtree with Hilbert order."""
import unittest
from fractions import Fraction as Q
from observational_succ import hilbert_prime_wavefront as w
from observational_succ import source_weil_hierarchy as orig

class PrimeHingeHilbertTests(unittest.TestCase):
    def test_first_no_prime_window_has_single_smooth_leaf(self):
        for k in (1,2,3,5,7):
            p=w.adaptive_profile(Q(1,4),k)
            self.assertEqual(p["active_true_prime_powers"],())
            self.assertEqual(p["adaptive_leaf_count"],1)
            self.assertEqual(p["original_square_area"],Q(1,4))
            self.assertEqual(p["wavefront_transition_finest_cells"],0)

    def test_true_first_prime_two_wavefront(self):
        for k in (2,3,4,5,6):
            p=w.adaptive_profile(Q(1,2),k)
            self.assertEqual(p["active_true_prime_powers"],((2,2),))
            self.assertGreater(p["wavefront_transition_finest_cells"],0)
            self.assertLessEqual(p["wavefront_transition_finest_cells"],8*2**k)
            self.assertLess(p["adaptive_leaf_count"],4**k)
            self.assertEqual(p["original_square_area"],Q(1))
            self.assertFalse(p["signed_Weil_positive_proved"])

    def test_multilevel_source_wavefront_never_adds_fake_six(self):
        out=w.adaptive_profile(Q(1),5)
        self.assertEqual(out["active_true_prime_powers"],
                         ((2,2),(3,3),(4,2),(5,5),(7,7)))
        self.assertNotIn((6,6),out["active_true_prime_powers"])
        self.assertTrue(out["exact_hilbert_prefix_partition"])

    def test_exact_wavefront_inequalities(self):
        a=Q(1,2)
        self.assertEqual(w.hinge_status(a,3,0,0,2),"INACTIVE")
        self.assertEqual(w.hinge_status(a,3,0,7,2),"ACTIVE")
        statuses={w.hinge_status(a,4,i,j,2)
                  for i in range(16) for j in range(16)}
        self.assertEqual(statuses,{"INACTIVE","ACTIVE","TRANSITION"})

    def test_adaptive_hilbert_cylinders_partition_without_ghost(self):
        for a in (Q(1,4),Q(1,2),Q(3,4)):
            for k in (2,3,5):
                p=w.adaptive_profile(a,k)
                pos=0
                for leaf in p["hilbert_ordered_leaves"]:
                    self.assertEqual(leaf.hilbert_start,pos)
                    pos+=leaf.hilbert_span
                    self.assertEqual(leaf.hilbert_span,4**(k-leaf.depth))
                self.assertEqual(pos,4**k)

    def test_wavefront_codimension_one_growth(self):
        # Empirical finite exact checks plus a separate paper geometric proof.
        for k in (3,4,5,6,7):
            n=2**k
            p=w.adaptive_profile(Q(1,2),k)
            self.assertLessEqual(p["wavefront_transition_finest_cells"],8*n)
            self.assertLess(p["adaptive_leaf_count"],n*n)
            self.assertGreater(p["adaptive_leaf_count"],1)

    def test_fake_euler_source_and_precision_type_rejected(self):
        for fn in (
            lambda:w.hinge_status(Q(1,2),2,0,3,6),
            lambda:w.hinge_status(Q(1,2),2,0,3,9),
            lambda:w.adaptive_profile(0.5,3),
            lambda:w.adaptive_profile(Q(1,2),0),
            lambda:w.adaptive_profile(Q(1,2),9),
            lambda:w.hinge_status(Q(1,2),3,8,0,2),
        ):
            with self.assertRaises((w.PrimeWavefrontError,w.HilbertCarrierError)):fn()
        with self.assertRaises(orig.WeilHierarchyError):
            orig.assert_original_source_tape(orig.AUTHENTIC_TAPE+((6,6),))

if __name__=="__main__":
    unittest.main()
