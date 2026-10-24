"""Independent source-clock minimization and no-alias finite certificates."""
import unittest
from math import comb,gcd
from observational_succ.minimal_moment_clock import minimum_moment_clock
from observational_succ.minimal_circle_carry import exact_origin_moment

class MinimalMomentClock(unittest.TestCase):
    def test_unit_clock_minima(self):
        for b,N,k,q in ((16,3,2,7),(16,3,3,13),(16,3,4,23),
                        (16,3,16,277),(16,4,2,19),(16,4,3,47),
                        (16,4,5,173)):
            m,count=minimum_moment_clock(b,N,k,require_unit=True)
            self.assertEqual((m,count),(q,comb(N+k-1,k)))
            self.assertEqual(gcd(m,b),1)
            self.assertLess(m,k*b**(N-1)+1)
            self.assertEqual(exact_origin_moment(b,N,k,modulus=m),
                             exact_origin_moment(b,N,k))

    def test_nonunit_grid_is_not_cyclic_multiplier_clock(self):
        self.assertEqual(minimum_moment_clock(16,3,16),(274,153))
        with self.assertRaises(ValueError):
            minimum_moment_clock(16,3,16,require_unit=True,max_modulus=276)

    def test_independent_multiset_alias_oracle(self):
        b,N,k,m=16,3,2,7
        sums=[b**i+b**j for i in range(N) for j in range(i,N)]
        self.assertEqual(len({x%m for x in sums}),len(sums))
        self.assertLess(len({x%6 for x in sums}),len(sums))

if __name__=="__main__":
    unittest.main()
