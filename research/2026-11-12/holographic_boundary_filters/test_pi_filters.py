"""Independent source/rounding and adversarial controls for PI_FILTERS.md."""
from copy import deepcopy
from fractions import Fraction as F
import unittest

import pi_filters as p


class PiFilterTests(unittest.TestCase):
    def test_combined_source_equals_four_poles(self):
        for n in range(1, 129):
            direct = F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            self.assertEqual(p.forcing(n), direct)
            self.assertGreater(direct, 0)
            self.assertLessEqual(direct, F(47,15*n*n))

    def test_interval_vs_independent_fraction_source(self):
        exact = F()
        for n, low, width, scale in p.raw_intervals(40, 13):
            if n:
                r = F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
                exact = (16*exact+r) % 1
            self.assertTrue(p.contains_circle(exact, low, width, scale))
            self.assertLessEqual(width, (16**n-1)//15)
            self.assertLess(F(width,scale), F(1,15*2**13))

    def test_cell_lower_at_all_rational_grid_samples(self):
        for q in (3, 7, 16):
            for a in range(q):
                for j in range(17):
                    x = F(16*a+j,16*q)
                    d = min(x, 1-x)
                    self.assertLessEqual(p.cell_minorant(a,q), 8*d*d)

    def test_lipschitz_tail_payment(self):
        for i in range(41):
            x = F(i,40)
            for j in range(-10,11):
                t = F(j,100)
                y = (x+t) % 1
                d0 = min(x,1-x)
                d1 = min(y,1-y)
                self.assertLessEqual(abs(d0*d0-d1*d1), abs(t))

    def test_resolution_monotonicity(self):
        result = p.run_shells((16,37), (8,16,32), 20)
        for b in (16,37):
            a = [F(x["signed_gap_lower"]) for x in result["entries"] if x["shell"]==b]
            self.assertEqual(a, sorted(a))

    def test_count_verifier_rejects_mutation(self):
        result = p.run_shells((9,), (8,), 12)
        self.assertTrue(p.verify_receipt(result))
        for field, value in (("seed","1"), ("source","mutant"), ("uniform_R0_proved",True)):
            mutant = deepcopy(result); mutant[field] = value
            self.assertFalse(p.verify_receipt(mutant))
        mutant = deepcopy(result)
        mutant["entries"][0]["counts"][0] += 1
        self.assertFalse(p.verify_receipt(mutant))
        mutant = deepcopy(result)
        mutant["entries"][0]["tail_payment"] = "0"
        self.assertFalse(p.verify_receipt(mutant))
        mutant = deepcopy(result)
        mutant["last_index"] = float(mutant["last_index"])
        self.assertFalse(p.verify_receipt(mutant))
        # Python's True==1 is not equality of an exact-count packet schema.
        small = p.run_shells((1,), (2,), 12)
        mutant = deepcopy(small)
        index = mutant["entries"][0]["counts"].index(1)
        mutant["entries"][0]["counts"][index] = True
        self.assertFalse(p.verify_receipt(mutant))

    def test_periodic_uniform_grid_is_not_universal_normality(self):
        # One period may have balanced cells; the atomic repeated grid is still
        # non-Haar. This test certifies only a finite minorant, no limit.
        out = p.gap_from_counts([4]*16, 0, 64)
        self.assertEqual(F(out["raw_minorant"]), F(35,64))
        self.assertGreater(F(out["signed_gap_lower"]), 0)

    def test_fixed_zero_and_unknown_controls(self):
        for counts, ambiguous in (([64]+[0]*15,0), ([0]*16,64)):
            self.assertEqual(F(p.gap_from_counts(counts,ambiguous,64)["signed_gap_lower"]),0)
        self.assertIsNone(p.certified_cell(99,2,100,16))
        self.assertIsNone(p.certified_cell(0,100,100,16))
        self.assertEqual(p.certified_cell(0,0,100,16),0)

    def test_guard_and_source_type_errors(self):
        for last in (-1, True, 1.5):
            with self.assertRaises(ValueError): list(p.raw_intervals(last))
        with self.assertRaises(ValueError): list(p.raw_intervals(5,0))
        with self.assertRaises(ValueError): p.forcing(0)
        with self.assertRaises(ValueError): p.gap_from_counts([1,2],0,4)
        with self.assertRaises(ValueError): p.gap_from_counts([True,1],0,2)
        with self.assertRaises(ValueError): p.run_shells((3,3))


if __name__ == "__main__":
    unittest.main()
