"""Independent exact-source tests for backward clock/Haar arithmetic bridge."""
import unittest
from fractions import Fraction as F
from math import gcd
from observational_succ.bidirectional_cut import (
    SourcePassport, CutSourceError, bernoulli_clock_covariance,
    clock_lcm, clock_period_integral, clock_tail_optimum,
    certified_cut_residual, forward_fractional_value,
    gcd_square_kernel, inverted_clock_value, jordan_two,
    log_one_plus_one_over, mobius, phi, reflected_fractional_value,
    signed_coefficients, square_root_tail_energy)


class ExactArithmeticBridge(unittest.TestCase):
    def test_mobius_jordan_inversions(self):
        for n in range(1,51):
            self.assertEqual(sum(mobius(n//d)*d*d for d in range(1,n+1) if n%d==0),jordan_two(n))
            self.assertEqual(sum(jordan_two(d) for d in range(1,n+1) if n%d==0),n*n)
            self.assertGreater(jordan_two(n),0)
            self.assertEqual(sum(phi(d) for d in range(1,n+1) if n%d==0),n)

    def test_basel_covariance_one_clock(self):
        self.assertEqual(bernoulli_clock_covariance(1,1),F(1,3))
        self.assertEqual(bernoulli_clock_covariance(1,2),F(7,24))
        self.assertEqual(bernoulli_clock_covariance(2,3),F(19,72))
        self.assertEqual(gcd_square_kernel(2,3),F(1,6))

    def test_periodic_hilbert_covariance_independent_cell_integrals(self):
        for coeffs in [
            (F(0),), (F(3,2),), (F(1),F(-2)),
            (F(2),F(3),F(-1)), (F(1,2),F(-2,3),F(7,5),F(1,4)),
        ]:
            closed=square_root_tail_energy(coeffs)['value']
            direct=clock_period_integral(coeffs)['mean_square']
            self.assertEqual(closed,direct)

    def test_pairwise_bernoulli_covariance_from_cell_source(self):
        # E[{x/m}{x/n}] from independent direct integration on the lcm-clock.
        for m in range(1,8):
            for n in range(1,8):
                L=clock_lcm((m,n))
                out=F(0)
                for k in range(L):
                    # {x/m}= (x-midpoint)/m+ mid_remainder, over one unit cell.
                    a=F(2*k+1,2*m)-k//m
                    b=F(2*k+1,2*n)-k//n
                    out+=a*b+F(1,12*m*n)
                self.assertEqual(out/L,bernoulli_clock_covariance(m,n))

    def test_arithmetic_jordan_square_factor(self):
        for N in range(1,9):
            c=tuple(F((-1)**j,j+2) for j in range(N))
            e=square_root_tail_energy(c)
            self.assertEqual(e['value'],clock_period_integral(c)['mean_square'])
            self.assertGreater(e['value'],0)
            self.assertEqual(e['value'], e['bias']**2+sum(e['nonnegative_squares']))

    def test_min_tail_closed_form_and_exact_optimizer(self):
        expected=(F(1,4),F(1,5),F(2,13),F(2,15),F(2,19),F(1,10))
        for N,x in enumerate(expected,1):
            result=clock_tail_optimum(N)
            self.assertEqual(result['minimum'],x)
            self.assertEqual(result['minimum'],clock_period_integral(result['coefficients'])['mean_square'])
            self.assertEqual(sum((v/n for n,v in enumerate(result['coefficients'],1)),F(0)),6*x)
            self.assertEqual(sum(result['coefficients']),2*(1-x))

    def test_tail_optimisation_does_not_minimise_full_L2(self):
        # N=1 tail optimal coefficient c=3/2 has source residual norm
        # on (0,1) alone =9/4>||h||^2=1. Thus cannot be the full minimizer.
        result=clock_tail_optimum(1)
        self.assertEqual(result['coefficients'],(F(3,2),))
        certificate=certified_cut_residual(result['coefficients'],R=12)
        self.assertGreaterEqual(certificate['lower'],F(9,4))
        self.assertGreater(certificate['lower'],1)
        self.assertEqual(certified_cut_residual((F(0),),R=12)['upper'],F(1))

    def test_cut_residual_outward_certificate(self):
        for c in [(F(0),),(F(1),),(F(1),F(-1)),(F(2,3),F(-1,5),F(1,2))]:
            r=certified_cut_residual(c,R=23,terms=14)
            self.assertLessEqual(r['lower'],r['upper'])
            self.assertGreaterEqual(r['lower'],r['unit_interval_obstruction'])
            self.assertTrue(r['tail_lower']<=r['tail_upper'])
            self.assertEqual(r['tail_Haar_alpha'],square_root_tail_energy(c)['value'])
            self.assertFalse(r['optimal_projection_certified'])

    def test_independent_log_interval_vs_basic_inequalities(self):
        for k in range(1,40):
            lo,hi=log_one_plus_one_over(k,terms=14)
            self.assertTrue(F(1,k+1)<=lo<hi<=F(1,k))

    def test_forward_backward_fractional_involution(self):
        for n in range(1,9):
            for x in [F(1,5),F(2,3),F(7,4),F(13,3),F(41,2)]:
                self.assertEqual(reflected_fractional_value(n,x),inverted_clock_value(n,x))
                self.assertEqual(forward_fractional_value(n,1/x)/x,inverted_clock_value(n,x))

    def test_source_passport_is_not_implicit_completion(self):
        source=SourcePassport('finite-observer',3,tuple(range(1,8)))
        self.assertTrue(source.require_prefix(7))
        with self.assertRaises(CutSourceError): source.require_prefix(8)
        with self.assertRaises(CutSourceError): SourcePassport('bad',0,(1,3)) .require_prefix(2)

    def test_mutant_source_or_bad_types_are_rejected(self):
        for cb in [lambda: signed_coefficients((1.0,)),
                   lambda: signed_coefficients(tuple()),
                   lambda: bernoulli_clock_covariance(0,2),
                   lambda: certified_cut_residual((1,),R=1),
                   lambda: log_one_plus_one_over(1,terms=1),
                   lambda: SourcePassport('',1,(1,))]:
            with self.assertRaises(CutSourceError): cb()


if __name__=='__main__':
    unittest.main()
