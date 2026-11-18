"""Original BBP future-tail complete monotonicity and locked-source falsifier."""
import unittest
from fractions import Fraction as F
from math import factorial
from observational_succ.borwein_quantitative_certificate import source_r,U
from observational_succ.bbp_tail_impulse import (
  source_difference,tail_impulse_rational_bounds,gamma_leading_constant,
  locked_source_difference,locked_source_r,locked_positive_mellin_kernel,
)

class CausalTailImpulseTests(unittest.TestCase):
    def test_original_forcing_unchanged_and_genuine_zero_seed(self):
        self.assertEqual(U(0),0)
        self.assertEqual(source_r(1),F(47,15))
        for n in (1,2,13):
            self.assertEqual(U(n),16*U(n-1)+source_r(n))

    def test_signed_all_order_original_source_differences_positive(self):
        for n in (1,2,3,8,32,128):
            for k in range(9):
                self.assertGreater(source_difference(n,k),0)

    def test_strict_monotone_for_every_tested_k_and_n(self):
        for n in (1,2,5,10,50):
            for k in range(7):
                self.assertGreater(source_difference(n,k),source_difference(n+1,k))

    def test_all_fraction_tail_bounds_enclose_positive_source_tail(self):
        for N in (0,1,2,16,100):
            for k in (0,1,2,3,5):
                a,b=tail_impulse_rational_bounds(N,k,12)
                self.assertGreater(a,0)
                self.assertGreater(b,a)
                smaller=tail_impulse_rational_bounds(N,k,8)
                self.assertLess(smaller[0],a)
                self.assertLess(b,smaller[1])

    def test_delta_reconstruction_of_source_tail_differences(self):
        N=5;M=8
        def tail_trunc(n):
            return sum((source_r(n+j)/16**j for j in range(1,M+1)),F(0))
        from math import comb
        for k in range(6):
            transformed=sum((F((-1)**j*comb(k,j))*tail_trunc(N+j)
                             for j in range(k+1)),F(0))
            a,b=tail_impulse_rational_bounds(N,k,M)
            self.assertEqual(transformed,a)
            self.assertLess(a,b)

    def test_gamma_asymptotic_matches_rational_control_intervals(self):
        for k in range(5):
            N=500
            lo,hi=tail_impulse_rational_bounds(N,k,24)
            scaled_lo=lo*N**(k+2)
            scaled_hi=hi*N**(k+2)
            gamma=gamma_leading_constant(k)
            self.assertGreater(gamma,0)
            # Finite N need not equal the asymptotic constant.
            self.assertLess(abs(float((scaled_lo+scaled_hi)/2/gamma)-1),F(1,10))

    def test_positive_locked_source_has_same_moment_hierarchy(self):
        self.assertEqual(F(5,2)-F(4,2)+F(3,6),1)
        for n in (1,2,3,16,100):
            for k in range(6):
                self.assertGreater(locked_source_difference(n,k),0)
            self.assertGreater(locked_source_r(n),locked_source_r(n+1))
        for t in (F(0),F(1,4),F(1,2),F(3,4)):
            self.assertGreater(locked_positive_mellin_kernel(t),0)
        self.assertEqual(locked_positive_mellin_kernel(1),0)

    def test_negative_source_mutant_violates_positive_differences(self):
        self.assertLess(-source_difference(3,2),0)
        with self.assertRaises(ValueError): source_difference(0,1)
        with self.assertRaises(ValueError): tail_impulse_rational_bounds(0,-1,4)

if __name__=='__main__':unittest.main()

class PascalKnowledgeVolumeTests(unittest.TestCase):
    def test_exact_rational_pascal_recursion(self):
        from observational_succ.bbp_tail_impulse import tail_impulse_rational_bounds
        for M in (2,4,8,16):
            for n in (0,1,2,8):
                for k in range(7):
                    a=tail_impulse_rational_bounds(n,k,M)[0]
                    b=tail_impulse_rational_bounds(n+1,k,M)[0]
                    c=tail_impulse_rational_bounds(n,k+1,M)[0]
                    self.assertEqual(a,b+c)
                    self.assertGreater(b,0)
                    self.assertGreater(c,0)

    def test_binomial_pascal_mass_is_exact_source_endpoint(self):
        from observational_succ.bbp_tail_impulse import (finite_source_endpoint,
           pascal_source_layer, tail_impulse_rational_bounds)
        from math import comb
        for M in (2,6,12):
            p=finite_source_endpoint(M)
            self.assertGreater(p,0)
            for level in (0,1,2,4,8):
                layer=pascal_source_layer(M,level)
                self.assertEqual(sum(layer,F(0)),1)
                self.assertTrue(all(x>0 for x in layer))
                raw=sum((F(comb(level,n))*tail_impulse_rational_bounds(n,level-n,M)[0]
                         for n in range(level+1)),F(0))
                self.assertEqual(raw,p)

    def test_bernstein_first_two_moments_exact(self):
        from observational_succ.bbp_tail_impulse import (pascal_source_layer,source_moment_y)
        for M in (3,8,16):
            first=source_moment_y(M,1)
            second=source_moment_y(M,2)
            self.assertTrue(F(0)<second<first<F(1))
            for level in (1,2,4,8):
                p=pascal_source_layer(M,level)
                mean=sum((F(n,level)*p[n] for n in range(level+1)),F(0))
                quad=sum((F(n*n,level*level)*p[n] for n in range(level+1)),F(0))
                self.assertEqual(mean,first)
                self.assertEqual(quad,second+(first-second)/level)

    def test_certified_transport_error_decreases_in_both_axes(self):
        from observational_succ.bbp_tail_impulse import certified_source_lift_error
        for M in (4,8,16):
            tail,cap=certified_source_lift_error(M,64)
            self.assertGreater(tail,0)
            self.assertLess(tail,cap)
            more_tail,more_cap=certified_source_lift_error(M+4,64)
            self.assertLess(more_tail,tail)
            self.assertLess(more_cap,cap)
            _,taller=certified_source_lift_error(M,256)
            self.assertLess(taller,cap)

    def test_order_limit_dual_gamma_asymptotic_numerical_controls(self):
        # Numeric probes are finite diagnostics; the universal asymptotics
        # follow from endpoint Laplace/Beta estimates in the theorem note.
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest("optional mpmath not installed; exact rational and paper tests still run")
        mp.mp.dps=55
        def K(t):return (1-t)/((2-t*t)*(t*t-2*t+2))
        for N in (0,1):
            for k in (100,300):
                val=mp.quad(lambda t:t**(8*N)*(1-t**8)**k*K(t),[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1])
                base=mp.gamma(N+mp.mpf(1)/8)/(32*k**(N+mp.mpf(1)/8))
                self.assertLess(abs(val/base-1),mp.mpf('.2'))
