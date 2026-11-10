"""Exact tests for the signed covariance decomposition (Front F)."""
import unittest
from fractions import Fraction as Q

from observational_succ import signed_covariance_decomposition as scd
from observational_succ import duck_bbp


class SignedCovarianceTests(unittest.TestCase):
    def _frozen_rows(self):
        # Reconstruct TFH-05 / HOLDOUT_512 2x2 counts (pp,pm,mp,mm)=(133,121,125,133).
        rows = []
        for _ in range(133): rows.append(scd.SignedSample(0, 1, 1, 1, 0))
        for _ in range(121): rows.append(scd.SignedSample(0, 1, -1, -1, 0))
        for _ in range(125): rows.append(scd.SignedSample(0, -1, 1, -1, 0))
        for _ in range(133): rows.append(scd.SignedSample(0, -1, -1, 1, 0))
        return rows

    def test_covariance_matches_frozen_holdout(self):
        rows = self._frozen_rows()
        self.assertEqual(scd.covariance(rows), Q(641, 16384))

    def test_tfh01_identity(self):
        # Cov(a,b) = (1-m^2)*beta exactly.
        rows = self._frozen_rows()
        t = scd.two_fiber_table(rows)
        self.assertEqual(scd.covariance(rows), (1 - t['m']**2) * t['beta'])
        self.assertEqual(t['beta'], Q(641, 16383))

    def test_decomposition_identity_exact(self):
        # Cov(a,b) = Cov(a, b*eps) + Cov(a, b*(1-eps)) exactly.
        rows = self._frozen_rows()
        d = scd.check_decomposition_identity(rows)
        self.assertTrue(d['matches_direct'])

    def test_tail_budget_small(self):
        # T_n <= r(n+1)/15 < 1/16 for n large enough that r(n+1) < 15/16.
        for n in (10, 100, 1000):
            lo, hi = duck_bbp.tail_interval(n, 4)
            self.assertLessEqual(hi, duck_bbp.forcing(n + 1) / 15 + Q(1, 10**6))

    def test_eps_is_carry_bit(self):
        # eps_n = floor({U_n} + T_n) is the tail carry into the digit;
        # the tail is < 1/16 for large n so eps_n in {0,1}.
        for n in (50, 100, 200):
            tail_hi = duck_bbp.tail_interval(n, 3)[1]
            self.assertLess(tail_hi, Q(1, 16))


if __name__ == '__main__':
    unittest.main()
