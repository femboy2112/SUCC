"""Focused original-source Gamma-window controls; no all-time normality claim."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import unittest
from fractions import Fraction
import mpmath as mp
mp.mp.dps=70
from gamma_phase import (source_r,original_Q,source_g,K,green_integral,green_series,
    fractional_window,window_asymptotic,four_time_window,four_time_limit,
    scale_log_character,gamma_log_target,tv_budget)

class SourceAlgebra(unittest.TestCase):
    def test_four_poles(self):
        for n in range(1,25):
            expected=Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(source_r(n),expected)

    def test_zero_seed(self):
        U=Fraction(0)
        for n in range(1,20):
            U=16*U+source_r(n)
            P=sum((source_r(j)/16**j for j in range(1,n+1)),Fraction(0))
            self.assertEqual(U,16**n*P)

    def test_original_factorization(self):
        for t in [mp.mpf(i)/32 for i in range(33)]:
            self.assertTrue(mp.almosteq(original_Q(t), (1-t)*(2+t*t)*(2+2*t+t*t)))

    def test_source_density_identity(self):
        for t in [mp.mpf(i)/32 for i in range(33)]:
            self.assertTrue(mp.almosteq(source_g(t),original_Q(t)/(16-t**8)))

    def test_density_upper(self):
        for t in [mp.mpf(i)/32 for i in range(33)]:
            self.assertGreaterEqual(source_g(t),0)
            self.assertLessEqual(source_g(t),1-t)

    def test_K_upper_pointwise(self):
        for v in [mp.mpf(i)/17 for i in range(150)]:
            self.assertGreaterEqual(K(v),0)
            self.assertLessEqual(K(v),v/64+mp.mpf('1e-45'))

    def test_green_source_rational_bounds(self):
        for n in (2,8,16):
            lo=green_series(n,18)
            hi=lo + source_r(n+19)/(15*16**18)
            target=green_integral(n,45)
            self.assertLess(mp.mpf(lo.numerator)/lo.denominator,mp.re(target))
            self.assertGreater(mp.mpf(hi.numerator)/hi.denominator,mp.re(target))

    def test_pi_value_is_imported_identity(self):
        # Finite high-precision diagnostic only; does not prove BBP identity.
        self.assertLess(abs(green_integral(0,55)-mp.pi/16),mp.mpf('1e-15'))

    def test_positive_moment(self):
        self.assertGreater(green_integral(20,50),0)
        self.assertLess(green_integral(60,50),green_integral(20,50))

class GammaWindows(unittest.TestCase):
    def test_beta0_equals_green(self):
        for n in (3,19):
            self.assertLess(abs(fractional_window(n,0,0,45)-green_integral(n,45)),mp.mpf('1e-40'))

    def test_complex_conjugate(self):
        a=fractional_window(23,.6,.4+.8j,45)
        b=fractional_window(23,-.6,.4-.8j,45)
        self.assertLess(abs(a-b.conjugate()),mp.mpf('1e-36'))

    def test_zero_twist_real_positive(self):
        v=fractional_window(24,0,1,45)
        self.assertAlmostEqual(float(mp.im(v)),0)
        self.assertGreater(mp.re(v),0)

    def test_first_order_source_correction(self):
        n=100
        exact=fractional_window(n,.6,.4+.7j,45)
        a0=window_asymptotic(n,.6,.4+.7j,0,45)
        a1=window_asymptotic(n,.6,.4+.7j,1,45)
        self.assertLess(abs(a1-exact),abs(a0-exact)/5)

    def test_second_order_source_correction(self):
        n=100
        exact=fractional_window(n,.6,.4+.7j,45)
        a1=window_asymptotic(n,.6,.4+.7j,1,45)
        a2=window_asymptotic(n,.6,.4+.7j,2,45)
        self.assertLess(abs(a2-exact),abs(a1-exact)/10)

    def test_exact_fractional_successor_square(self):
        # Complex frequency is transported as xi -> n*xi/(n+1), since the
        # *additive* Laplace coordinate z=n(1+i xi) advances by exactly one.
        n=13;xi=mp.mpf('0.75');beta=mp.mpc('0.6','0.4')
        lhs=fractional_window(n,xi,beta+1,60)
        rhs=(fractional_window(n,xi,beta,60)
             -fractional_window(n+1,n*xi/(n+1),beta,60))
        self.assertLess(abs(lhs-rhs),mp.mpf('1e-53'))

    def test_original_forcing_successor_square(self):
        # Exact r(n+1)=(16-S)T_n, verified without a pi oracle.
        n=9
        rhs=16*green_integral(n,55)-green_integral(n+1,55)
        rr=source_r(n+1)
        self.assertLess(abs(rhs-mp.mpf(rr.numerator)/rr.denominator),mp.mpf('1e-50'))

    def test_source_fixed_beta_complex(self):
        n=250;beta=.3+1.2j
        v=fractional_window(n,-.3,beta,45)
        asym=window_asymptotic(n,-.3,beta,2,45)
        self.assertLess(abs(v-asym)/abs(v),mp.mpf('1e-4'))

    def test_wrong_source_gamma_marginal_blind(self):
        # Coherent wrong seed changes completed circle phases to constant 0;
        # it does NOT change the forcing-only Green or Gamma windows.
        n=11
        original=fractional_window(n,.5,1j*.7,45)
        self.assertEqual(original,fractional_window(n,.5,1j*.7,45))
        self.assertGreater(green_integral(n,40),0)

    def test_invalid_beta_guard(self):
        with self.assertRaises(ValueError):
            fractional_window(10,0,-2)

class FourTime(unittest.TestCase):
    def test_four_time_positive(self):
        for n,q in ((8,4),(18,18),(32,256)):
            v=four_time_window(n,q,2,0,0,45)
            self.assertGreater(mp.re(v),0)
            self.assertLess(abs(mp.im(v)),mp.mpf('1e-39'))

    def test_four_time_source_finite_difference(self):
        n,q=13,5
        expected=(green_integral(n,50)-green_integral(n+q,50)
                  -green_integral(n+2,50)+green_integral(n+q+2,50))
        self.assertLess(abs(expected-four_time_window(n,q,2,0,0,50)),mp.mpf('1e-43'))

    def test_saturated_cubic(self):
        n=250;q=n*n
        value=four_time_window(n,q,2,0,0,45)
        prediction=four_time_limit(n,q,2,0,0,'saturated',45)
        self.assertLess(abs(value/prediction-1),mp.mpf('.025'))

    def test_proportional_cubic(self):
        n=250;q=n
        v=four_time_window(n,q,2,0,0,45)
        expected=four_time_limit(n,q,2,0,0,'proportional',45)
        self.assertLess(abs(v/expected-1),mp.mpf('.025'))

    def test_fixed_q_quartic(self):
        n=250;q=4
        v=four_time_window(n,q,2,0,0,45)
        expected=four_time_limit(n,q,2,0,0,'sublinear',45)
        self.assertLess(abs(v/expected-1),mp.mpf('.06'))

    def test_complex_saturated(self):
        n=350;q=n*n;beta=.3+.7j;xi=.7
        v=four_time_window(n,q,2,xi,beta,45)
        expected=four_time_limit(n,q,2,xi,beta,'saturated',45)
        self.assertLess(abs(v/expected-1),mp.mpf('.022'))

class TransportedPhases(unittest.TestCase):
    def test_mass_deficit_bound(self):
        for n in (1,8,16,64):
            deficit,budget=tv_budget(n,45)
            self.assertGreaterEqual(deficit,0)
            self.assertLessEqual(deficit,budget+mp.mpf('1e-35'))

    def test_uniform_two_phase_bound(self):
        n=16
        deficit,budget=tv_budget(n,45)
        for xi,omega in ((0,0),(1,0),(0,3),(2,7),(-3,11)):
            observed=scale_log_character(n,xi,omega,45)
            gamma=gamma_log_target(xi,omega,45)
            self.assertLessEqual(abs(observed-gamma),2*deficit+mp.mpf('1e-30'))
            self.assertLessEqual(abs(observed-gamma),2*budget+mp.mpf('1e-30'))

    def test_gamma_frequency_nonzero(self):
        self.assertGreater(abs(gamma_log_target(0,2,45)),0)
        self.assertLess(abs(gamma_log_target(0,2,45)),1)

    def test_gamma_two_phase_conjugacy(self):
        v=gamma_log_target(.6,1.2,45)
        w=gamma_log_target(-.6,-1.2,45)
        self.assertLess(abs(v-mp.conj(w)),mp.mpf('1e-38'))

    def test_invalid_n_and_gamma(self):
        with self.assertRaises(ValueError): tv_budget(0)
        with self.assertRaises(ValueError): four_time_window(1,0)

from gamma_signed_shell import tail_rational,tail_interval,positive_step_difference,shell_response,limiting_integral

class SourceHighFrequency(unittest.TestCase):
    def test_source_positive_differences(self):
        for k in range(4):
            for n in (8,18):
                lo,hi=positive_step_difference(n,k,2,45)
                self.assertGreater(lo,0)
                self.assertGreater(hi,lo)

    def test_true_green_interval(self):
        for n in (3,23):
            lo,hi=tail_interval(n,30)
            target=green_integral(n,60)
            self.assertLess(mp.mpf(lo.numerator)/lo.denominator,mp.re(target))
            self.assertGreater(mp.mpf(hi.numerator)/hi.denominator,mp.re(target))

    def test_fixed_finite_signed_shell_against_limit(self):
        for k in (0,1,2):
            r=shell_response(64,k,2,0.5,45,60)
            l=limiting_integral(64,k,2,0.5,60)
            self.assertLess(abs(r['value']-l),mp.mpf('0.085'))
            self.assertLess(r['max_phase_halfwidth_bound'],mp.mpf('1e-35'))

    def test_signed_phase_error_bound_is_positive(self):
        r=shell_response(16,1,2,0.5,45,60)
        self.assertGreater(r['max_phase_halfwidth_bound'],0)
        self.assertLess(r['max_phase_halfwidth_bound'],mp.mpf('1e-32'))

if __name__=="__main__":
    unittest.main(verbosity=2)
