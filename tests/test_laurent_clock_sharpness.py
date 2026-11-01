"""Root-discoverable exact Fraction controls for Laurent-clock sharpness."""
import importlib.util
from pathlib import Path
from fractions import Fraction as F
import unittest

SOURCE=Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'laurent_clock_sharpness'/'sharpness.py'
spec=importlib.util.spec_from_file_location('succ_lcs_independent_exact', SOURCE)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)


class ExactSourceClocks(unittest.TestCase):
    def test_original_source_values(self):
        self.assertEqual(s.source(1),F(47,15))
        self.assertEqual(s.source(2),F(106,819))

    def test_moment_independent_first_values(self):
        for d,val in [(0,F(1,15)),(1,F(16,225)),(2,F(272,3375)),
                      (3,F(1712,16875)),(4,F(37808,253125))]:
            with self.subTest(d=d):self.assertEqual(s.moment(d),val)

    def test_exact_laurent_leading_coefficients(self):
        expected=(F(1,64),-F(7,512),F(55,4096),-F(595,32768),F(8551,262144))
        for d,x in enumerate(expected,1):
            with self.subTest(d=d):self.assertEqual(s.infinite_leading(d),x)

    def test_strict_pole_sign_for_all_calibrated_shifts(self):
        for d in range(1,11):
            for j in range(1,15):
                with self.subTest(d=d,j=j):
                    self.assertGreater((-1)**(d+1)*s.original_coefficient(j,d),0)

    def test_strict_weighted_sign_for_all_orders(self):
        for d in range(1,14):
            self.assertGreater((-1)**(d+1)*s.infinite_leading(d),0)
            for k in (1,2,5,10):
                self.assertGreater((-1)**(d+1)*s.finite_leading(k,d),0)
                self.assertLessEqual(abs(s.finite_leading(k,d)),s.moment(d))

    def test_geometric_remainder_second_oracle(self):
        for n,k in [(1,1),(5,3),(31,5),(113,7),(301,11)]:
            for d in range(1,7):
                with self.subTest(n=n,k=k,d=d):
                    self.assertEqual(s.residual(n,k,d),s.independent_residual(n,k,d))

    def test_explicit_all_time_value_bound(self):
        for n,k in [(1,1),(2,4),(9,5),(53,8),(131,12),(307,17)]:
            for d in range(1,9):
                with self.subTest(n=n,k=k,d=d):
                    c=s.finite_leading(k,d)
                    lhs=abs(s.residual(n,k,d)/16**k-c/F(n)**(d+1))
                    self.assertLessEqual(lhs,s.moment(d+1)/F(n)**(d+2))

    def test_first_and_second_derivative_bounds(self):
        for n,k in [(F(3,2),2),(F(9,4),3),(F(117,5),6),(F(121),9)]:
            for d in range(1,8):
                with self.subTest(n=n,k=k,d=d):
                    C=s.derivative_certificate(n,k,d)
                    for x in ('value','first','second'):
                        self.assertLessEqual(C[x+'_error'],C[x+'_bound'])

    def test_derivative_sign_on_bulk_holdouts(self):
        for n,k in [(512,7),(1024,8),(2048,9)]:
            for d in (1,2,3,4):
                with self.subTest(n=n,k=k,d=d):
                    _,f1,f2=s.scaled_derivatives(n,k,d)
                    self.assertGreater((-1)**d*f1,0)
                    self.assertGreater((-1)**(d+1)*f2,0)

    def test_earlier_d1_profile_recovered(self):
        a,r,g=s.limiting_profile(1,F(5,2))
        self.assertEqual((a,r,g),(F(4,5),F(24,25),F(1,25)))

    def test_new_d2_coherent_profile(self):
        a,r,g=s.limiting_profile(2,F(7,2))
        self.assertEqual((a,r,g),(F(6,7),F(48,49),F(1,49)))

    def test_new_d3_coherent_profile(self):
        a,r,g=s.limiting_profile(3,F(9,2))
        self.assertEqual((a,r,g),(F(8,9),F(80,81),F(1,81)))

    def test_gap_is_strict_and_sums_one(self):
        for d in range(1,9):
            c=F(2*d+3,2)
            a,red,gap=s.limiting_profile(d,c)
            self.assertEqual(red+gap,1)
            self.assertGreater(gap,0)
            self.assertLess(red,1)

    def test_wrong_positive_source_fails(self):
        self.assertTrue(s.mutation_fails_source_contract(10000,1,2))
        self.assertTrue(s.mutation_fails_source_contract(10000,2,3))

    def test_invalid_inputs_fail_closed(self):
        for d in (0,-1,25,False):
            with self.assertRaises(ValueError):s.infinite_leading(d)
        for c in (F(3),F(4),F(6)):
            with self.assertRaises(ValueError):s.limiting_profile(2,c)
        with self.assertRaises(ValueError):s.source(F(1,2))
        with self.assertRaises(ValueError):s.moment(-1)


if __name__=='__main__':unittest.main()
