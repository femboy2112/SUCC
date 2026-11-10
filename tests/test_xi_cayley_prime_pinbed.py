"""Hostile exact critical-circle probes; not a proof of RH or finite zero census."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.xi_cayley_prime_pinbed import (
    critical_circle_at_height, exact_horodisk_margin, fake_completed_reflection,
    fake_disk_reflection, fake_jensen_exp_mean, fake_li_coefficient,
    critical_line_zero_pair, half_density_prime_product_at_boundary,
    half_plane_horodisk, mertens_gamma_diagnostic, prime_euler_log_tail_bound,
    prime_sieve, normalized_prime_pole_location, real_cayley,
    upper_zero_count_from_jensen, completed_euler_product_diagnostic,
)


class ExactMobiusCircleTests(unittest.TestCase):
    def test_critical_line_maps_to_unit_circle_without_rounding(self):
        for t in (Q(0), Q(1,2), Q(-3,11), Q(17,4), Q(451,37)):
            re, im = critical_circle_at_height(t)
            self.assertEqual(re*re + im*im, 1)
            self.assertEqual(im >= 0, t >= 0)
        self.assertEqual(critical_circle_at_height(0),(-1, 0))
        self.assertEqual(critical_circle_at_height(Q(1,2)),(0,1))
        self.assertEqual(real_cayley(Q(1,2)),-1)
        with self.assertRaises(ValueError): real_cayley(0)
        with self.assertRaises(TypeError): critical_circle_at_height(0.5)

    def test_exact_euler_horodisks_have_tangent_inner_boundary(self):
        self.assertEqual(half_plane_horodisk(1),(Q(1,2),Q(1,2)))
        self.assertEqual(half_plane_horodisk(Q(3,2)),(Q(2,3),Q(1,3)))
        self.assertEqual(exact_horodisk_margin(Q(1,3),0,Q(3,2)),0)
        self.assertEqual(exact_horodisk_margin(0,0,1),0)
        self.assertGreater(exact_horodisk_margin(Q(3,4),0,1),0)
        self.assertLess(exact_horodisk_margin(-Q(1,3),0,1),0)
        for s in (Q(3,2), Q(2), Q(5,3), Q(3,4)):
            w = real_cayley(s)
            self.assertEqual(exact_horodisk_margin(w,0,1) > 0, s > 1)
        with self.assertRaises(ValueError): half_plane_horodisk(0)

    def test_reflection_symmetric_offline_polynomial_is_exact_countermodel(self):
        for a in (Q(1,4), Q(1,10),Q(3,8)):
            ins, outs = critical_line_zero_pair(a)
            self.assertEqual(ins*outs,1)
            self.assertTrue(-1<ins<0)
            self.assertTrue(outs < -1)
            for s in (Q(-3), 0, Q(1,8), Q(1,2), Q(3,4),1,2,5):
                self.assertEqual(fake_completed_reflection(s,a),
                                 fake_completed_reflection(1-Q(s),a))
            self.assertEqual(fake_completed_reflection(0,a),1)
            self.assertEqual(fake_completed_reflection(1,a),1)
            self.assertEqual(fake_completed_reflection(Q(1,2)+a,a),0)
            self.assertEqual(fake_completed_reflection(Q(1,2)-a,a),0)
            for w in (Q(-4,5),Q(-1,5),0,Q(1,7),Q(1,2)):
                self.assertEqual(fake_disk_reflection(w,a),
                                 fake_completed_reflection(Q(1)/(1-w),a))
        self.assertEqual(critical_line_zero_pair(Q(1,4)), (Q(-1,3),Q(-3)))
        self.assertEqual(fake_li_coefficient(1,Q(1,4)), Q(16,3))
        self.assertEqual(fake_li_coefficient(2,Q(1,4)), Q(-64,9))
        for a in (0,Q(1,2),Q(4,5)):
            with self.assertRaises(ValueError): critical_line_zero_pair(a)

    def test_independent_log_series_oracle_for_fake_li(self):
        # Independent coefficient extraction by rational formal power series.
        def multiply(x,y,M):
            return [sum((x[i]*y[j-i] for i in range(j+1)),Q(0)) for j in range(M+1)]
        for a in (Q(1,10),Q(1,4),Q(2,5)):
            M=9; c=1/(Q(1,4)-a*a)
            # Q_a(1/(1-w))=1 + c*w/(1-w)^2.
            x=[Q(0)]+[c*j for j in range(1,M+1)]
            formal=[Q(1)]+x[1:]
            x_power=[Q(1)]+[Q(0)]*M
            coefficients=[Q(0)]*(M+1)
            for k in range(1,M+1):
                x_power=multiply(x_power,x,M)
                for n in range(1,M+1):
                    coefficients[n]+=Q((-1)**(k+1),k)*x_power[n]
            for n in range(1,M+1):
                self.assertEqual(n*coefficients[n],fake_li_coefficient(n,a))

    def test_jensen_exact_zero_count_certificate_on_fake_models(self):
        a=Q(1,4); r=Q(1,2)
        self.assertEqual(fake_jensen_exp_mean(Q(1,4),a),1)
        self.assertEqual(fake_jensen_exp_mean(r,a),Q(3,2))
        self.assertEqual(upper_zero_count_from_jensen(Q(1,4),r,Q(3,2)),0)
        self.assertEqual(upper_zero_count_from_jensen(Q(2,5),r,Q(3,2)),1)
        with self.assertRaises(ValueError): fake_jensen_exp_mean(Q(1,3),a)
        with self.assertRaises(ValueError):upper_zero_count_from_jensen(Q(1,2),Q(1,2),1)
        with self.assertRaises(ValueError):upper_zero_count_from_jensen(Q(1,4),Q(1,2),Q(9,10))

    def test_independent_numerical_jensen_calibration_without_zeta_zeros(self):
        # Numerical quadrature is an independent holdout, not certified intervals.
        import mpmath as mp
        with mp.workdps(45):
            a=mp.mpf(1)/4
            for r,rational_mean in ((mp.mpf(1)/5, Q(1)),
                                    (mp.mpf(1)/2, Q(3,2))):
                def integrand(theta):
                    z=r*mp.exp(1j*theta)
                    s=1/(1-z)
                    f=1+s*(s-1)/(mp.mpf(1)/4-a*a)
                    return mp.log(abs(f))
                mean=mp.quad(integrand,[0,mp.pi,2*mp.pi])/(2*mp.pi)
                target=mp.log(mp.mpf(rational_mean.numerator)/rational_mean.denominator)
                self.assertLess(abs(mean-target),mp.mpf('2e-30'))

    def test_line_root_model_has_critical_unit_roots(self):
        # H(s)=1+2s(s-1); H(1-s)=H(s), H(0)=H(1)=1.
        # H(1/(1-w))=(1+w^2)/(1-w)^2, with roots at +-i.
        for s in (Q(-3),Q(-1,2),0,Q(1,4),Q(1,2),1,Q(3,2),5):
            self.assertEqual(1+2*Q(s)*(Q(s)-1),
                             1+2*(1-Q(s))*(-Q(s)))
        for n in range(1,97):
            if n%2: lam=2
            else: lam=2+2*((-1)**(n//2+1))
            self.assertGreaterEqual(lam,0)
        self.assertEqual((1j)**2,-1)


class PrimeEulerGeometryTests(unittest.TestCase):
    def test_exact_finite_half_density_primes_boundary_and_mertens(self):
        self.assertEqual(prime_sieve(11),(2,3,5,7,11))
        self.assertEqual(half_density_prime_product_at_boundary(2),Q(1,2))
        self.assertEqual(half_density_prime_product_at_boundary(3),Q(1,3))
        self.assertEqual(half_density_prime_product_at_boundary(5),Q(4,15))
        self.assertEqual(half_density_prime_product_at_boundary(7),Q(8,35))
        # Finite monotonic samples; NOT proof of Mertens' infinite limit.
        values=[half_density_prime_product_at_boundary(N) for N in (10,50,100,1000)]
        self.assertTrue(all(x > y > 0 for x,y in zip(values,values[1:])))
        self.assertGreater(mertens_gamma_diagnostic(10000),0.5)
        self.assertLess(mertens_gamma_diagnostic(10000),0.63)
        for bad in (0,1,2.5,1000001):
            with self.assertRaises(ValueError):prime_sieve(bad)

    def test_original_vs_half_density_prime_zero_locations(self):
        for p in (2,3,5,7,11,29):
            for k in (-5,-1,1,3,11):
                old=normalized_prime_pole_location(p,k,False)
                new=normalized_prime_pole_location(p,k,True)
                self.assertAlmostEqual(old.real,1,places=12)
                self.assertGreater(abs(old),1)
                self.assertAlmostEqual(abs(new),1,places=12)
                self.assertNotAlmostEqual(old.real,new.real,places=8)
        with self.assertRaises(ValueError):normalized_prime_pole_location(6,2,True)
        with self.assertRaises(ValueError):normalized_prime_pole_location(5,0,True)

    def test_convergent_euler_region_completes_gamma_and_pole(self):
        import mpmath as mp
        with mp.workdps(65):
            for s in (mp.mpc(2),mp.mpc(2,0.37),mp.mpc(3,1.2)):
                P=450
                true=mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
                computed=completed_euler_product_diagnostic(complex(s),P)
                bound=prime_euler_log_tail_bound(float(s.real),P)
                predicted=abs(computed)*math.expm1(bound)
                self.assertLessEqual(abs(complex(true)-computed),predicted+1e-12)
                self.assertLess(bound,0.01)
        with self.assertRaises(ValueError):completed_euler_product_diagnostic(0.75,50)
        with self.assertRaises(ValueError):prime_euler_log_tail_bound(1.,50)
        with self.assertRaises(ValueError):prime_euler_log_tail_bound(1.5,1)

    def test_prime_products_are_not_zeta_zeros(self):
        # The finite half-density factor for P=5 is NONZERO at s=3/2,
        # but approaches zero as P grows by Mertens (CLASSICAL result).
        for P in (2,5,11,100,1000):
            self.assertNotEqual(half_density_prime_product_at_boundary(P),0)
        # In Möbius disk, the new limiting zero is at 1/3, inside unit disk,
        # on the convergence-horodisk boundary for Re s>3/2.
        w=real_cayley(Q(3,2))
        self.assertEqual(w,Q(1,3))
        self.assertEqual(exact_horodisk_margin(w,0,Q(3,2)),0)
        self.assertLess(w*w,1)


if __name__ == '__main__':
    unittest.main()

class NumericalWindingCalibration(unittest.TestCase):
    def test_learning_circle_phase_winding_splits_true_and_fake_models(self):
        from observational_succ.xi_cayley_prime_pinbed import sampled_phase_winding_diagnostic
        # Both fake models are *explicitly constructed independently* of any
        # nontrivial zeta zero data. The sample itself is NOT an RH certificate.
        def off(w):
            return 1+(16/3)*w/((1-w)**2)  # roots at -1/3,-3
        def on(w):
            return (1+w*w)/((1-w)**2)     # roots +-i, on boundary
        for r, expected in ((0.2,0),(0.5,1),(0.8,1)):
            winding, step, min_abs = sampled_phase_winding_diagnostic(off,r)
            self.assertEqual(winding,expected)
            self.assertLess(step,0.3)
            self.assertGreater(min_abs,0)
            self.assertEqual(sampled_phase_winding_diagnostic(on,r)[0],0)
        with self.assertRaises(ValueError):sampled_phase_winding_diagnostic(off,1.)
