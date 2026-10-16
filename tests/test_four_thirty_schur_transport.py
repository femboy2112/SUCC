"""Four-mode vs thirty-mode Schur transport: exact finite-model regressions."""
import unittest
from fractions import Fraction as F

from observational_succ.four_thirty_schur_transport import (
    short_to, haynsworth_transitivity_holds, coercivity_does_not_transport_example,
    demo, KAPPA_4, KAPPA_30,
)


class TransitivityTests(unittest.TestCase):
    def test_short_to_matches_2x2_schur(self):
        G = ((F(2), F(1)), (F(1), F(2)))
        self.assertEqual(short_to(G, (0,)), ((F(2) - F(1, 2),),))  # 2 - 1*1/2*1

    def test_haynsworth_transitivity_exact(self):
        G = (
            (F(3),   F(0),   F(1,2), F(0),   F(1,5), F(0)  ),
            (F(0),   F(2),   F(0),   F(1,3), F(0),   F(1,7)),
            (F(1,2), F(0),   F(-1),  F(0),   F(1,4), F(0)  ),
            (F(0),   F(1,3), F(0),   F(2),   F(0),   F(1,6)),
            (F(1,5), F(0),   F(1,4), F(0),   F(5),   F(0)  ),
            (F(0),   F(1,7), F(0),   F(1,6), F(0),   F(4)  ),
        )
        res = haynsworth_transitivity_holds(G, low=(0, 1), mid=(2, 3))
        self.assertTrue(res["equal"])
        self.assertEqual(res["direct"], res["nested"])  # S_4 == Short_F4(S_30)


class CoercivityNoGoTests(unittest.TestCase):
    def test_high_coercivity_does_not_transport(self):
        out = coercivity_does_not_transport_example(eps=F(1, 10), b=F(1))
        self.assertTrue(out["high_coercivity_cannot_rescue_four_mode_sign"])
        self.assertTrue(out["four_mode_schur_independent_of_high_coercivity_c"])
        for row in out["sweep"]:
            self.assertEqual(row["four_mode_schur_[0,0]"], str(F(1) - F(1) / F(1, 10)))  # -9
            self.assertTrue(row["four_mode_schur_not_psd"])

    def test_positive_when_coupling_small_enough(self):
        # b^2 < eps  ->  four-mode Schur stays positive (sanity: the mechanism is real)
        out = coercivity_does_not_transport_example(eps=F(1, 2), b=F(1, 10))
        self.assertFalse(out["high_coercivity_cannot_rescue_four_mode_sign"])

    def test_kappa_ordering(self):
        self.assertEqual(KAPPA_4, F(1, 50))
        self.assertEqual(KAPPA_30, F(369, 10000))
        self.assertGreater(KAPPA_30, KAPPA_4)   # 30-mode is MORE coercive, yet does not transport

    def test_demo(self):
        d = demo()
        self.assertTrue(d["transitivity_equal"])
        self.assertTrue(d["coercivity_transport_nogo"])
        self.assertFalse(d["RH_proved"])


if __name__ == "__main__":
    unittest.main()
