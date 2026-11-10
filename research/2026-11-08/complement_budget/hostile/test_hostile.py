import unittest
from fractions import Fraction as F
from oracle import ambiguity_counts, cycle, eligible, factor_identity


class HostileTests(unittest.TestCase):
    def test_exact_nonresonant_reconstruction(self):
        self.assertEqual(ambiguity_counts(73,3,1),9)
        self.assertEqual(ambiguity_counts(97,1,3),12)

    def test_two_replicas_are_eligible(self):
        self.assertTrue(eligible(4409))
        self.assertEqual(len(cycle(4409)),551)
        self.assertEqual((4409-1)//4,2*len(cycle(4409)))

    def test_even_radix_factor(self):
        self.assertEqual(factor_identity(),17)

    def test_synthetic_control_needs_forcing_cost(self):
        self.assertNotEqual((-1)**16,-1)
        self.assertEqual((-1)**17,-1)
        self.assertEqual((-1)**16*(-1),-1)

    def test_invalid_clock(self):
        for p,xi in ((2,1),(9,1),(17,0)):
            with self.assertRaises(ValueError):
                cycle(p,xi)

    def test_deterministic_q2_floor_positive(self):
        p=4409;m=551;n0=(p-1)//4+1
        for h in (1,3):
            lower=F(m-1,17*m)*(1-F(330*h,7*(8*n0+1)**2))
            self.assertGreater(lower,F(58,1000))
            self.assertLess(lower,F(1,17))


if __name__=="__main__":
    unittest.main()
