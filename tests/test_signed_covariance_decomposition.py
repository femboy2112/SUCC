"""Exact tests for the signed covariance decomposition (Front F)."""
import unittest
from fractions import Fraction as Q
from itertools import product

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
        # PPP-02 uses eps_n=floor({U_n}+T_n) for integer-completed parity.
        # The fractional first-digit parity is PPP's next source index.
        for n in (50, 100, 200):
            tail_hi = duck_bbp.tail_interval(n, 3)[1]
            self.assertLess(tail_hi, Q(1, 16))


class SignedCovarianceHostileTests(unittest.TestCase):
    @staticmethod
    def rows(triples):
        return [scd.SignedSample(i,a,b,a*b,eps)
                for i,(a,b,eps) in enumerate(triples)]

    @staticmethod
    def pair_difference_covariance(a,b):
        # Independent finite covariance identity using pair differences.
        N=len(a)
        return Q(sum((a[i]-a[j])*(b[i]-b[j])
                     for i in range(N) for j in range(N)),2*N*N)

    def test_nondyadic_exactness_and_parity_mean(self):
        rows=self.rows([(1,1,0),(1,-1,1),(-1,1,1)])
        self.assertIs(type(scd.covariance(rows)),Q)
        self.assertEqual(scd.covariance(rows),Q(-4,9))
        table=scd.two_fiber_table(rows)
        self.assertEqual(table['P'],Q(-1,3))
        self.assertEqual(table['complement_mean'],Q(1,3))
        self.assertEqual(scd.tail_boundary_coupling(rows),Q(-4,3))

    def test_all_nondyadic_three_row_sign_and_boundary_models(self):
        types=list(product((-1,1),(-1,1),(0,1)))
        for triples in product(types,repeat=3):
            rows=self.rows(triples)
            a=[r.a for r in rows]
            b=[r.b for r in rows]
            c=[r.b*(-1)**r.eps for r in rows]
            expected=self.pair_difference_covariance(a,b)
            self.assertEqual(scd.covariance(rows),expected)
            split=scd.check_decomposition_identity(rows)
            self.assertIs(type(split['sum']),Q)
            self.assertEqual(split['sum'],expected)
            self.assertTrue(split['matches_direct'])
            difference=expected-self.pair_difference_covariance(a,c)
            self.assertEqual(scd.tail_boundary_coupling(rows),difference)
            if len(set(a))==2:
                table=scd.two_fiber_table(rows)
                self.assertEqual(table['P'],Q(sum(r.s for r in rows),3))
                self.assertEqual(expected,(1-table['m']**2)*table['beta'])

    def test_anticorrelated_signs(self):
        rows=self.rows([(1,-1,0),(1,-1,1),(-1,1,0),(-1,1,1),(1,-1,0)])
        table=scd.two_fiber_table(rows)
        self.assertEqual(table['P'],-1)
        self.assertEqual(table['beta'],-1)
        self.assertEqual(scd.covariance(rows),Q(-24,25))

    def test_sample_domains_and_empty_fibers(self):
        for args in [(0,1,1,-1,0),(0,1,1,1,2),(0,True,1,1,0),(-1,1,1,1,0)]:
            with self.assertRaises(ValueError):
                scd.SignedSample(*args)
        for operation in (scd.covariance,scd.two_fiber_table,
                          scd.tail_boundary_coupling,scd.check_decomposition_identity):
            with self.assertRaises(ValueError):
                operation([])
        with self.assertRaises(ValueError):
            scd.two_fiber_table(self.rows([(1,1,0)]))

    def test_integer_and_fractional_digit_index_shift(self):
        from observational_succ.bbp_parity_pressure import original_zero_parity_states
        from observational_succ.parity_boundary_certificate import certified_source_digit
        states=list(original_zero_parity_states(10))
        signs={state.n:(-1)**state.completed_parity for state in states}
        for n in range(1,10):
            self.assertEqual((-1)**certified_source_digit(n)[0],signs[n+1])
        self.assertEqual(signs[1],-1)  # integer part of pi is 3
        self.assertEqual((-1)**certified_source_digit(1)[0],1)  # next hex digit is 2
        for A in (1,2,3,4):
            old=Q(sum(signs[n] for n in range(A,2*A)),A)
            new=Q(sum((-1)**certified_source_digit(n)[0] for n in range(A,2*A)),A)
            self.assertEqual(new-old,Q(signs[2*A]-signs[A],A))
            self.assertLessEqual(abs(new-old),Q(2,A))


if __name__ == '__main__':
    unittest.main()
