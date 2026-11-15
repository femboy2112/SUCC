"""Focused exact rational positive, negative, and mutation tests for Gamma genesis."""
import unittest
import random
from fractions import Fraction as F
from math import factorial

from observational_succ.gamma_genesis import (
    forcing, forcing_factored, beta_integer, oily_positive_moment_bounds,
    refined_oily_moment_bounds, green_tail_bounds, oily_gamma_total_variation_bound, gamma_delay_pmf,
    gamma_poisson_mixture_pmf, convolution_coefficient,
    laplace_integer_shape, gamma_partition_integer_shape,
    gauge_compensated_partition, causal_gamma_filter, signed_mean_gap
)


class GammaGenesisTests(unittest.TestCase):
    def test_four_original_signed_poles_and_factored_source(self):
        for n in range(1,85):
            self.assertEqual(forcing(n),forcing_factored(n))
            self.assertGreater(forcing(n),0)
        self.assertTrue(all(forcing(n)>forcing(n+1) for n in range(1,60)))

    def test_original_source_green_and_oily_moment_rational_brackets(self):
        for n in range(0,30):
            m=8*n
            lo,hi=oily_positive_moment_bounds(m)
            tl,th=green_tail_bounds(n,20)
            self.assertLess(tl,hi)
            self.assertGreater(th,lo)
            self.assertLess(tl,th)
            if n>=1:
                self.assertGreater(lo,0)
                # The very narrow source sum brackets fit wholly inside
                # independently derived Beta/endpoint bounds.
                self.assertLessEqual(lo,tl)
                self.assertLessEqual(th,hi)

    def test_rational_beta_closed_forms(self):
        for m in range(21):
            for k in range(6):
                expect=F(factorial(m)*factorial(k),factorial(m+k+1))
                self.assertEqual(beta_integer(m,k),expect)

    def test_moment_refined_upper_lower_and_asymptotic(self):
        for m in [8,16,32,64,128,256,1024]:
            coarse=oily_positive_moment_bounds(m)
            fine=refined_oily_moment_bounds(m)
            self.assertGreaterEqual(fine[1],coarse[0])
            self.assertLessEqual(fine[1],coarse[1])
            self.assertLessEqual(fine[0],fine[1])
            tl,th=green_tail_bounds(m//8,35)
            self.assertLessEqual(fine[0],tl)
            self.assertLessEqual(th,fine[1])
        m=100_000
        lo,hi=refined_oily_moment_bounds(m)
        self.assertLess(hi-lo,F(500,m**5))
        self.assertLess(abs(F(1)-m*m*lo),F(8,m))
        self.assertLess(abs(F(1)-m*m*hi),F(8,m))

    def test_source_conditional_gamma_tv_convergence_is_quantitative(self):
        for m in (8,16,24,32,64,128,256,1024):
            b=oily_gamma_total_variation_bound(m)
            lo,hi=green_tail_bounds(m//8,30)
            # Actual 1-m^2 I_m is enclosed by independent Green source.
            self.assertLessEqual(1-m*m*lo,b)
            self.assertLess(b,F(7,m))
            self.assertGreaterEqual(b,0)
        with self.assertRaises(ValueError):
            oily_gamma_total_variation_bound(0)

    def test_oily_endpoint_is_exact_two_stage_discrete_gamma(self):
        for j in range(0,50):
            self.assertEqual(gamma_delay_pmf(2,j),F(j+1,2**(j+2)))
            self.assertEqual(gamma_poisson_mixture_pmf(2,j),gamma_delay_pmf(2,j))

    def test_normalization_characteristic_and_mean_by_pgf(self):
        # G_alpha(z)=(2-z)^(-alpha), G(1)=1, derivative G'(1)=alpha.
        for a in range(0,9):
            self.assertEqual(laplace_integer_shape(a,F(0)),1)
            self.assertEqual(gamma_delay_pmf(a,0),F(1,2**a))
            if a>0:
                self.assertEqual(gamma_delay_pmf(a,1),F(a,2**(a+1)))

    def test_gamma_origin_impulse_is_convolution_identity(self):
        for a in range(0,7):
            for j in range(0,19):
                self.assertEqual(convolution_coefficient(0,a,j),gamma_delay_pmf(a,j))
                self.assertEqual(convolution_coefficient(a,0,j),gamma_delay_pmf(a,j))

    def test_independence_is_not_free_from_matching_marginals(self):
        # If the two Exp(1) stages are identical random variables, their
        # sum is 2*Exp(1), not Gamma(2,1). Compare exact Laplace at q=1.
        dependent_transform=F(1,3)
        independent_transform=laplace_integer_shape(2,F(1))
        self.assertEqual(independent_transform,F(1,4))
        self.assertNotEqual(dependent_transform,independent_transform)

    def test_discrete_gamma_semigroup_all_small_compositions(self):
        for a in range(0,7):
            for b in range(0,7):
                for j in range(0,16):
                    self.assertEqual(convolution_coefficient(a,b,j),gamma_delay_pmf(a+b,j))

    def test_independent_poisson_gamma_bridge(self):
        for a in range(1,9):
            for j in range(0,25):
                self.assertEqual(gamma_poisson_mixture_pmf(a,j),gamma_delay_pmf(a,j))

    def test_gamma_multiplicative_clock_gauge(self):
        for a in (1,2,3,5):
            for rate in (F(1),F(3,7),F(11,6)):
                for rescale in (F(1),F(2),F(5,3)):
                    u,v=gauge_compensated_partition(a,rate,rescale)
                    self.assertEqual(u,v)
                    self.assertEqual(u,factorial(a-1))

    def test_wrong_clock_rate_without_compensation_is_not_gauge(self):
        self.assertNotEqual(gamma_partition_integer_shape(2,F(1)),
                            gamma_partition_integer_shape(2,F(2)))

    def test_causal_delay_compulsory_two_steps(self):
        f=(F(1),F(0),F(0),F(0),F(0),F(0),F(0))
        y=causal_gamma_filter(f,2,delay=2)
        self.assertEqual(y[:2],(F(0),F(0)))
        self.assertEqual(y[2],F(1,4))
        self.assertEqual(y[3],F(1,4))
        self.assertEqual(y[4],F(3,16))

    def test_signed_universal_boundary_gap_130_seeded(self):
        rng=random.Random(16028)
        for _ in range(130):
            n=rng.randint(1,30)
            f=tuple(F(rng.randint(-5,5),rng.randint(1,5)) for _ in range(n))
            a=rng.randint(0,8); d=rng.randint(0,5)
            gap,bound=signed_mean_gap(f,a,d)
            self.assertLessEqual(gap,bound)
            if a==0 and d==0:self.assertEqual(gap,0)

    def test_coherent_constant_control_survives_gamma_smoothing(self):
        # A constant (nonnormal) signed phase is NOT canceled by an
        # ordinary normalized fixed-depth causal observer kernel.
        a=2; n=180
        f=(F(1),)*n
        y=causal_gamma_filter(f,a,2)
        self.assertGreater(sum(y,F(0)), n-4)
        self.assertLessEqual(abs(sum(y,F(0))-n),4)

    def test_zero_seeded_rational_carrier_signed_observer_transport(self):
        # Literal U_0=0 and the original four signed poles. This exact
        # integer-lift sign is a control, NOT the complex Weyl criterion.
        u=F(0)
        f=[]
        for n in range(0,52):
            if n:
                u=16*u+forcing(n)
            f.append(F(1 if (u.numerator//u.denominator)%2==0 else -1))
        gap,bound=signed_mean_gap(tuple(f),2,2)
        self.assertLessEqual(gap,bound)
        self.assertEqual(bound,4)

    def test_moving_depth_can_fake_cancellation_on_constant_phase(self):
        # Do not infer a source-selected Weyl saving from an observer whose
        # Gamma depth grows faster than the observation horizon.
        for n in (8,12,20):
            alpha=n*n
            f=(F(1),)*n
            y=causal_gamma_filter(f,alpha)
            avg=sum(y,F(0))/n
            chernoff=F(2)**n * F(2,3)**alpha
            self.assertLessEqual(avg,chernoff)
            self.assertLess(avg,F(1,100))

    def test_alternating_phase_and_sign_do_not_follow_from_grade(self):
        # Same positive weights, incompatible extra signed channels.
        w=gamma_delay_pmf(2,3)
        self.assertNotEqual(w, F(0))
        self.assertNotEqual(w*F(1),w*F(0))
        self.assertEqual((w*F(1)+w*F(-1))/2,0)

    def test_first_order_nonuniversal_endpoint_shapes(self):
        # Different positive endpoint germs share the SAME Gamma(2) leading
        # coefficient (L(1)=1); their m^-3 corrections differ.
        for m in (8,20,60):
            base=beta_integer(m,1)
            mutant=base+beta_integer(m,2)
            self.assertNotEqual(base,mutant)
            self.assertEqual((m*m*base).limit_denominator(10**20) > 0,True)
            self.assertGreater(mutant-base,0)

    def test_input_validation_and_no_invented_realization(self):
        for fn,args in ((forcing,(0,)),(beta_integer,(-1,2)),
                        (oily_positive_moment_bounds,(-1,)),
                        (green_tail_bounds,(1,0)),(gamma_delay_pmf,(-1,3)),
                        (gamma_poisson_mixture_pmf,(0,3)),
                        (gamma_partition_integer_shape,(1,0)),
                        (causal_gamma_filter,((F(1),),1,-1))):
            with self.assertRaises(ValueError):fn(*args)
        with self.assertRaises(ValueError):gamma_delay_pmf(1.5,3)
        with self.assertRaises(TypeError):causal_gamma_filter((0.3,),2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
