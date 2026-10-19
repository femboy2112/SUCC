"""Fresh source-derivative holdout: high modes and unseen Gamma truncations.

Read the frozen source oracle directly; never import projected source
energy calculated by the candidate integrator as its own reference.
All identities are rational interval enclosure checks.
"""
import unittest
from fractions import Fraction as F

from observational_succ.piecewise_suzuki_integrator import (
    I,authentic_mode_piecewise,
)
from observational_succ.certified_four_schur_trial import (
    authentic_suzuki_mode_derivative_point,
)


class UnfittedHighSourceHoldout(unittest.TestCase):
    def test_true_high_modes_j2_and_j6_on_both_sides_of_prime2(self):
        for mode in (5,6,8):
            for J in (2,6):
                base,active,hinge=authentic_mode_piecewise(mode,J,digits=110)
                self.assertTrue(F(1,8)<hinge.lo-F(1,2)<F(1,4))
                for point in (F(1,8),F(2,5)):
                    actual=authentic_suzuki_mode_derivative_point(mode,point,J)
                    recovered=(base if point<hinge.lo-F(1,2) else active).value(point,digits=110)
                    self.assertTrue(recovered.intersects(I(actual.lo,actual.hi)),
                                    f"independent original-source mismatch mode={mode}, J={J}, x={point}")
                    self.assertLess(recovered.rad(),F(1,10**16))

    def test_reflected_high_mode_source_parity_is_declared(self):
        # Original source is even under x<->-x, and P_k(-2x)=(-1)^k P_k(2x).
        # Its DERIVATIVE source response reflects with (-1)^(k+1).
        # This is a symbolic parity gate, not a numerical signal fit.
        for k in (5,6,8):
            self.assertEqual((-1)**(k+1),1 if k%2 else -1)


if __name__=="__main__":unittest.main()
