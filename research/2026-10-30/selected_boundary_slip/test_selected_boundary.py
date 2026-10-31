"""Independent finite calibrations only; asymptotic proof is in THEOREMS.md."""
import unittest
from fractions import Fraction as F
from math import gcd
from selected_boundary import (forcing,states,dist_to_integer,slip_distances,
                               slip_stats,forced_approximation,rational_phase_window)

class SourceAndBoundaryTests(unittest.TestCase):
    def test_first_source(self):
        self.assertEqual(forcing(1), F(47,15))
        self.assertEqual(forcing(2), F(106,819))
    def test_recursion_exact(self):
        u=states(25)
        for n in range(1,len(u)):
            self.assertEqual(u[n]-16*u[n-1],forcing(n))
    def test_direct_prefix_oracle(self):
        u=states(32)
        for n in (1,2,3,7,17,32):
            direct = sum((16**(n-j)*forcing(j) for j in range(1,n+1)),F())
            self.assertEqual(u[n],direct)
    def test_lag_is_positive_for_source(self):
        u=states(30)
        for n in range(1,30):
            self.assertEqual(u[n+1]-u[n],15*u[n]+forcing(n+1))
    def test_exact_distance(self):
        self.assertEqual(dist_to_integer(F(31,16)),F(1,16))
        self.assertEqual(dist_to_integer(F(-1,16)),F(1,16))
        self.assertEqual(dist_to_integer(F(17,16)),F(1,16))
    def test_first_slips_existence(self):
        for h in (1,2,3,7):
            for a in (8,16,32):
                self.assertTrue(any(x>=F(1,20) for x in slip_distances(a,8*a-1,h)),(a,h))
    def test_late_slip_count(self):
        for h in (1,3,7):
            v=slip_stats(1,256,h)
            self.assertGreater(v['slips'],180)
            self.assertLess(v['longest_coherent_run'],15)
    def test_small_lift_exact(self):
        # a real base-16 orbit near a fixed point has an exactly coherent finite run.
        data=forced_approximation(16**10,F(1,16**12),10)
        self.assertTrue(data['all_near'])
        self.assertEqual(data['values'][9],F(1,16**3))
    def test_expansion_cannot_hide_wrap(self):
        # 17*radius<1 is the exact no-integer-jump threshold.
        with self.assertRaises(ValueError):
            forced_approximation(1,F(0),5,F(1,17))
    def test_counterseed_coherence_rational_pure(self):
        # alpha=0 gives zero energy for every n, demonstrating seed dependence.
        self.assertEqual(rational_phase_window(F(0),1,150),[F(0)]*150)
        # alpha=1/15 is also an exact fixed point for lag h=1.
        self.assertEqual(rational_phase_window(F(1,15),1,150),[F(0)]*150)
    def test_reduced_rational_aliasing(self):
        a=F(1,3)
        # For the pure system 16≡1 mod3, all lag phases are integer.
        self.assertEqual(rational_phase_window(a,1,12),[F(0)]*12)
    def test_liouville_like_sparse_run(self):
        # Finite sparse-digit mimic of a Liouville construction: a very long
        # coherent prefix is possible when no irrationality-exponent input is supplied.
        alpha=F(1,16**300)
        self.assertTrue(all(d<F(1,20) for d in rational_phase_window(alpha,30,200)))

if __name__=='__main__': unittest.main(verbosity=2)
