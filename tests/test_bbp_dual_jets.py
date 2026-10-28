"""Exact, hostile, source-aware finite checks for dual BBP geometry."""
from fractions import Fraction as Q
from unittest import TestCase
import unittest

from observational_succ import bbp_dual_jets as d


def matrix_sub(a, b):
    return tuple(tuple(x-y for x, y in zip(rowa, rowb))
                 for rowa, rowb in zip(a, b))


def matrix_unit(i, j):
    return tuple(tuple(Q(int(a == i and b == j)) for b in range(4))
                 for a in range(4))


def matrix_direction(x):
    return matrix_sub(d.matmul(x, d.T), d.matmul(d.T, x))


def perturb_return(powers, b):
    return tuple(tuple(sum((d.matmul(d.matmul(powers[7-k], b), powers[k])[i][j]
                            for k in range(8)), Q(0)) for j in range(4))
                 for i in range(4))


def perturb_tap(powers, b, n):
    return sum((d.matmul(d.matmul(d.matmul(d.matmul((d.L,), powers[n-1-k],),
                                    b), powers[k]), tuple((x,) for x in d.B))[0][0]
                for k in range(n)), Q(0))


class ExactDualSource(TestCase):
    def test_dual_product_quotient_and_nilpotent(self):
        x, y = d.Dual(Q(2,3), Q(5,7)), d.Dual(Q(3,5),Q(-2,9))
        self.assertEqual((x*y)/y, x)
        self.assertEqual(d.Dual(0,1)*d.Dual(0,1), d.Dual(0))
        self.assertEqual(d.evaluate((0,0,0,1), d.Dual(4,1)),
                         d.Dual(64,48))
        with self.assertRaises(ZeroDivisionError):
            d.Dual(0,1).inverse()

    def test_original_four_pole_and_chiral_gluing(self):
        for n in (1,2,3,5,11,53,101,997):
            independent = (Q(4,8*n-7)-Q(2,8*n-4)
                           -Q(1,8*n-3)-Q(1,8*n-2))
            self.assertEqual(d.source_jet(n), d.source_rational_jet(n))
            self.assertEqual(d.source_jet(n).value, independent)
            self.assertEqual(d.source_jet(n,d.PLUS)+d.source_jet(n,d.MINUS),
                             d.source_jet(n))
            self.assertNotEqual(d.source_jet(n, d.PLUS),d.source_jet(n))
        with self.assertRaises(ValueError):d.source_jet(0)

    def test_endpoint_zero_is_a_first_order_not_second_order_zero(self):
        self.assertEqual(d.endpoint_jet(), d.Dual(0,-15))
        self.assertEqual(d.endpoint_jet(d.PLUS).value, Q(15,4))
        self.assertEqual(d.endpoint_jet(d.MINUS).value, Q(-15,4))
        self.assertEqual(d.endpoint_jet(d.PLUS)+d.endpoint_jet(d.MINUS),
                         d.endpoint_jet())
        for n in (1000,3000,10000):
            self.assertLess(abs(n*n*d.source_jet(n).value-Q(15,64)),Q(1,100))

    def test_wrongsigned_pole_detected(self):
        mutated = list(d.TOTAL); mutated[3] *= -1
        self.assertNotEqual(d.endpoint_jet(mutated), d.endpoint_jet())
        self.assertNotEqual(d.source_jet(1,mutated), d.source_jet(1))

    def test_exact_rational_derivative_polynomial(self):
        ap = d.derivative(d.A);dp = d.derivative(d.D)
        expected = tuple(x-y for x,y in zip(
            d.multiply_polynomials(ap,d.D)+(0,),
            d.multiply_polynomials(d.A,dp)))
        self.assertEqual(expected,d.W)
        for n in (1,2,3,17):
            self.assertEqual(d.source_jet(n).tangent,
                             Q(d.evaluate(d.W,n),d.evaluate(d.D,n)**2))

    def test_resultants_discriminants_and_new_prime(self):
        self.assertEqual(d.discriminant((1,0,1)),-4)
        self.assertEqual(d.discriminant(d.D),2**24*3**2*5**2)
        self.assertEqual(d.resultant(d.A,d.D),-2**15*3**2*5**2)
        self.assertEqual(d.resultant(d.W,d.D),-2**48*3**4*5**4)
        self.assertEqual(d.discriminant(d.W),
                         2**49*3**5*5**2*d.EXTRA_CRITICAL_PRIME)
        p=d.EXTRA_CRITICAL_PRIME
        self.assertTrue(all(p%q for q in range(2, int(p**0.5)+1)))

    def test_modular_critical_classes_and_higher_jets(self):
        for x, value, second in ((1,5,4),(5,1,1)):
            coeffs=d.field_taylor(d.A,d.D,x,7)
            self.assertEqual(coeffs[:3],(value,0,second))
        with self.assertRaises(ZeroDivisionError):
            d.field_taylor(d.A,d.D,0,7)
        p,x=d.EXTRA_CRITICAL_PRIME,d.EXTRA_CRITICAL_ROOT
        self.assertNotEqual(d.evaluate(d.D,x)%p,0)
        self.assertEqual(d.evaluate(d.W,x)%p,0)
        self.assertEqual(d.evaluate(d.derivative(d.W),x)%p,0)
        self.assertNotEqual(d.evaluate(d.derivative(d.derivative(d.W)),x)%p,0)
        self.assertEqual(d.field_taylor(d.A,d.D,x,p),
                         (34082935,0,0,5987934))

    def test_exact_gain_age_kernel_and_zero_seed(self):
        for n in range(0,13):
            u=sum((16**(n-s)*d.source_jet(s).value
                   for s in range(1,n+1)), Q(0))
            age=sum(((n-s)*16**(n-s-1)*d.source_jet(s).value
                     for s in range(1,n)), Q(0))
            self.assertEqual(d.gain_dual_prefix(n),d.Dual(u,age))
        self.assertEqual(d.gain_dual_prefix(0),d.Dual(0))


class InfinitesimalEightClock(TestCase):
    def test_exact_chiral_matrix_and_return(self):
        powers=d.matrix_powers()
        self.assertEqual(powers[8],tuple(tuple(v/16 for v in row)
                                          for row in d.identity()))
        j=tuple(tuple(Q(-1,4) if i==k and i<2 else
                      Q(1,4) if i==k and i>=2 else Q(0)
                      for k in range(4)) for i in range(4))
        self.assertEqual(powers[4],j)
        self.assertEqual([d.matmul(d.matmul((d.L,),powers[k]),
                                    tuple((x,) for x in d.B))[0][0]
                          for k in range(8)], list(d.TOTAL))

    def test_ranks_holonomy_and_source_constraints(self):
        self.assertEqual(d.tangent_jacobian_ranks(), (4,3,7))
        powers=d.matrix_powers()
        control=tuple(tuple(d.matmul(powers[k],tuple((x,) for x in d.B))[i][0]
                              for k in range(4)) for i in range(4))
        observe=tuple(d.matmul((d.L,),powers[k])[0] for k in range(4))
        self.assertEqual(d.matrix_rank(control),4)
        self.assertEqual(d.matrix_rank(observe),4)

    def test_gauge_is_invisible_but_source_changing_holonomy_is_not(self):
        powers=d.matrix_powers()
        invisible=matrix_direction(matrix_unit(1,1))
        visible=matrix_direction(matrix_unit(0,1))
        z=tuple(tuple(Q(0) for _ in range(4)) for _ in range(4))
        self.assertNotEqual(invisible,z)
        for direction in (invisible,visible):
            self.assertEqual(perturb_return(powers,direction),z)
        self.assertEqual([perturb_tap(powers,invisible,n) for n in range(1,9)],
                         [Q(0)]*8)
        self.assertEqual([perturb_tap(powers,visible,n) for n in range(1,4)],
                         [Q(2),Q(2),Q(1)])
        self.assertNotEqual(perturb_tap(powers,visible,1),Q(0))

    def test_one_jet_does_not_detect_integer_digit_cut(self):
        # x=1/16 +/- t^2 have the SAME value and first derivative at t=0,
        # but their first hexadecimal digits differ for every 0<t<1/4.
        t=Q(1,100)
        below=Q(1,16)-t*t
        above=Q(1,16)+t*t
        self.assertEqual((16*below).numerator//(16*below).denominator,0)
        self.assertEqual((16*above).numerator//(16*above).denominator,1)
        eps=d.Dual(0,1)
        self.assertEqual(d.Dual(Q(1,16))-eps*eps,
                         d.Dual(Q(1,16))+eps*eps)


if __name__=='__main__':
    unittest.main()
