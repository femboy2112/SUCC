import sys
from pathlib import Path
from fractions import Fraction as Q
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
import innovation_oracle as io


class InnovationTests(unittest.TestCase):
    def test_complete_finite_character_compiler(self):
        rows=io.exact_cases()
        self.assertEqual(len(rows),28)
        self.assertTrue(all(r['exact_innovation_checks']>0 for r in rows))

    def test_common_factor_interval_and_bound(self):
        self.assertEqual(len(io.interval_cases()),18)

    def test_integer_lift_common_transport(self):
        self.assertEqual(io.source_compression_cases(),612)

    def test_exact_mode_covariance_and_conjugation(self):
        self.assertEqual(io.mode_covariance_cases(),288)

    def test_literal_digit_tail_constant(self):
        for b in (2,4,16):
            averages=[Q(sum(abs(d-c) for c in range(b)),b) for d in range(b+1)]
            self.assertEqual(max(averages),Q(b+1,2))
            self.assertEqual(max(averages[:-1]),Q(b-1,2))
            for k in range(1,8):
                for R in range(1,k+1):
                    # Coefficient pi*|h| deliberately factored out.
                    tail=sum((Q(b+1,b**l) for l in range(R+1,k+1)),Q(0))
                    self.assertEqual(tail,Q(b+1,b-1)*(Q(1,b**R)-Q(1,b**k)))


if __name__=='__main__':unittest.main()
