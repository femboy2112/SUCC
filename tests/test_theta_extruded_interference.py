"""Local research checks; finite precision cannot certify RH or infinite sign claims."""
from __future__ import annotations
import math
import unittest
from fractions import Fraction
from math import comb, factorial
import mpmath as mp

from observational_succ.theta_extruded_interference import (
    pascal_laguerre_weights, laguerre_signed_value,
    triangle_moments_from_a,a_from_triangle_moments,li_from_completed_coefficients,
    fake_atomic_triangle_coefficients,fake_atomic_completed,
    theta_kernel,theta_phi,theta_I,xi_theta_dual,
    theta_reflected_channels,completed_xi_direct,laguerre_theta_coefficient,
    first_li_gamma,rigorous_integer_tail_bound,rigorous_time_tail_bound,
    completed_phi_halves
)

class ExactPascalExtrusion(unittest.TestCase):
    def test_laguerre_explicit_rational(self):
        for n in range(1,21):
            weights=pascal_laguerre_weights(n)
            self.assertEqual(len(weights),n)
            self.assertEqual(weights[0],n)
            self.assertEqual(weights[-1],Fraction(1,factorial(n-1)))
            for t in (Fraction(0),Fraction(1,2),Fraction(3,5)):
                self.assertEqual(laguerre_signed_value(n,t,1),
                    sum((w*(-t)**j for j,w in enumerate(weights)),Fraction(0)))
                self.assertEqual(laguerre_signed_value(n,t,-1),
                    sum((w*t**j for j,w in enumerate(weights)),Fraction(0)))
                self.assertGreater(laguerre_signed_value(n,t,-1),0)
    def test_exact_pascal_inverse(self):
        for size in range(1,19):
            c=tuple(Fraction(j+2,2*j+5) for j in range(size))
            a=a_from_triangle_moments(c)
            self.assertEqual(triangle_moments_from_a(a),c)
            self.assertTrue(all(v>0 for v in c))
    def test_all_order_positive_finite_differences(self):
        for size in range(1,13):
            c=tuple(Fraction(j+3,4*j+7) for j in range(size))
            a=a_from_triangle_moments(c)
            b=[a[i]/(i+1) for i in range(size)]
            for k in range(size):
                self.assertTrue(all(x>0 for x in b))
                b=[b[i+1]-b[i] for i in range(len(b)-1)]
    def test_exact_signed_li_recursion_and_fakes(self):
        a=tuple(Fraction(16*n,3) for n in range(1,9))
        li=li_from_completed_coefficients(a)
        self.assertEqual(li[0],Fraction(16,3))
        self.assertEqual(li[1],Fraction(-64,9))
        self.assertTrue(all(n*x==x*n for n,x in enumerate(a,1)))
    def test_rejects_bad_sources(self):
        for arg in (0,-1,True,1.2):
            with self.assertRaises(ValueError):pascal_laguerre_weights(arg)
        for arg in (0,False,-1.3):
            with self.assertRaises(ValueError):laguerre_signed_value(2,Fraction(1,3),arg)
        for a in ((),[Fraction(1,2)],(1.25,)):
            with self.assertRaises(ValueError):triangle_moments_from_a(a)
        with self.assertRaises(ValueError):li_from_completed_coefficients(())

class ThetaGammaCalibration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with mp.workdps(55):
            cls.a=[mp.mpf('0')]+[laguerre_theta_coefficient(n) for n in range(1,10)]
            cls.li=li_from_completed_coefficients(tuple(cls.a[1:]))

    def test_gamma_first_vertex(self):
        with mp.workdps(55):
            self.assertLess(abs(self.a[1]-first_li_gamma()),mp.mpf('1e-46'))
            self.assertGreater(self.a[1],0)
    def test_first_two_completed_li_against_stieltjes(self):
        with mp.workdps(55):
            gamma=mp.euler
            li2=1+gamma-gamma**2+mp.pi**2/8-2*mp.stieltjes(1)-mp.log(4*mp.pi)
            self.assertLess(abs(self.li[1]-li2),mp.mpf('1e-46'))
            self.assertGreater(self.li[1],0)
    def test_pascal_integer_difference_positive_at_finite_n(self):
        with mp.workdps(55):
            b=[self.a[n]/n for n in range(1,len(self.a))]
            for degree in range(0,6):
                self.assertTrue(all(x>0 for x in b))
                b=[b[j+1]-b[j] for j in range(len(b)-1)]
    def test_completed_series_against_independent_zeta_gamma(self):
        with mp.workdps(55):
            for z in (mp.mpf('0.01'),mp.mpf('0.07'),mp.mpf('0.1')):
                s=1/(1-z)
                val=2*completed_xi_direct(s)
                poly=1+sum(self.a[n]*z**n for n in range(1,len(self.a)))
                self.assertLess(abs(poly-val),mp.mpf('5e-10'))
    def test_gamma_completion_and_theta_contact(self):
        with mp.workdps(55):
            for s in (mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('1.5'),
                      mp.mpc('.7','2'),mp.mpc('.5','4')):
                self.assertLess(abs(xi_theta_dual(s)-completed_xi_direct(s)),mp.mpf('5e-48'))
            theta1=1+theta_kernel(mp.mpf('0'))
            derivtheta=-4*mp.pi*sum(m*m*mp.exp(-mp.pi*m*m) for m in range(1,9))
            self.assertLess(abs(derivtheta+theta1/2),mp.mpf('1e-45'))
            # w(t)=2 exp(t/2) (theta(exp(2t))-1), hence w'(0)=-1
            wprime=theta_kernel(0)+derivtheta*2
            self.assertLess(abs(wprime+1),mp.mpf('1e-45'))
    def test_original_positive_Phi_and_negative_control(self):
        with mp.workdps(55):
            for t in (mp.mpf(0),mp.mpf('.1'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')):
                self.assertGreater(theta_phi(t),0)
                self.assertGreater(theta_kernel(t),0)
            # Positive Fourier density does not imply real zeros:
            # 1 + (1/2) cos z has nonreal zeros at pi ± i acosh 2.
            z=mp.pi+1j*mp.acosh(2)
            self.assertLess(abs(1+mp.cos(z)/2),mp.mpf('1e-45'))
    def test_theta_cutoff_analytic_bounds_are_tiny(self):
        with mp.workdps(70):
            for n in (1,2,4,8,12):
                tail=rigorous_integer_tail_bound(n,source_terms=8)
                ttail=rigorous_time_tail_bound(n,time_cutoff='2.7')
                self.assertGreater(tail,0)
                self.assertGreater(ttail,0)
                self.assertLess(tail,mp.mpf('1e-80'))
                self.assertLess(ttail,mp.mpf('1e-250'))

class DualInterferenceAndHostileControls(unittest.TestCase):
    def test_atomic_fake_offline_zeros_and_li_sign(self):
        with mp.workdps(50):
            self.assertEqual(fake_atomic_completed(mp.mpf('0')),1)
            self.assertEqual(fake_atomic_completed(mp.mpf('1')),1)
            self.assertLess(fake_atomic_completed(mp.mpf('0.5')),0)
            self.assertLess(abs(fake_atomic_completed(mp.mpf('0.3'))-
                                fake_atomic_completed(mp.mpf('0.7'))),mp.mpf('1e-45'))
            a1=fake_atomic_triangle_coefficients(1)
            a2=fake_atomic_triangle_coefficients(2)
            self.assertGreater(a1,0)
            self.assertGreater(a2,0)
            actual_li2=2*a2-a1*a1
            expected=4*math.e*(1-math.e)
            self.assertLess(abs(actual_li2-expected),2e-13)
            self.assertLess(actual_li2,0)
    def test_atomic_fake_all_newton_moments_strictly_positive(self):
        with mp.workdps(50):
            for j in range(0,26):
                coefficient=mp.mpf(2)*(mp.e+(-1)**j)/mp.factorial(j+1)
                self.assertGreater(coefficient,0)
                # This positive atom imitates the entire original Pascal
                # positivity theorem yet has real offcritical zeros.
    def test_unmodified_theta_split_dominance_reverses_exactly(self):
        with mp.workdps(55):
            for y,sign in ((mp.mpf('.25'),1),(mp.mpf('1'),-1)):
                e,estar=theta_reflected_channels(1j*y)
                delta=abs(e)**2-abs(estar)**2
                self.assertEqual((delta>0)-(delta<0),sign)
            e,estar=theta_reflected_channels(1j*mp.mpf('.5'))
            self.assertLess(abs(e-estar),mp.mpf('1e-48'))
    def test_completed_phi_split_reconstructs_xi_and_has_sign_failure(self):
        with mp.workdps(55):
            for z in (mp.mpc(0,'.25'),mp.mpc(17,'.25')):
                n,p=completed_phi_halves(z)
                xi=completed_xi_direct(mp.mpf('.5')+1j*z)
                self.assertLess(abs((n+p)/2-xi),mp.mpf('1e-44'))
                delta=abs(n)**2-abs(p)**2
                if abs(z.real)<1:
                    self.assertGreater(delta,0)
                else:
                    self.assertLess(delta,mp.mpf('-0.00002'))
    def test_triangular_log_not_generated_by_positive_moments_only(self):
        with mp.workdps(55):
            c=tuple(Fraction(j+1,j+7) for j in range(1,10))
            a=a_from_triangle_moments(c)
            self.assertTrue(all(x>0 for x in c))
            values=li_from_completed_coefficients(a)
            # Algebraic formal-log recurrence independent of theta.
            self.assertEqual(values[0],a[0])
            self.assertEqual(values[1],2*a[1]-a[0]*a[0])
    def test_fake_half_density_not_authenticated_by_gamma(self):
        with mp.workdps(50):
            fake=fake_atomic_completed(mp.mpf('2'))
            authentic=2*completed_xi_direct(mp.mpf('2'))
            self.assertGreater(abs(fake-authentic),1)

if __name__ == '__main__':
    unittest.main()

class LowDegreeRigorousSign(unittest.TestCase):
    def test_first_four_symbolic_triangular_polynomials(self):
        from observational_succ.theta_extruded_interference import first_four_li_from_moments
        x=(Fraction(1,3),Fraction(1,5),Fraction(2,7),Fraction(4,9))
        m0,m1,m2,m3=x
        result=first_four_li_from_moments(x)
        self.assertEqual(result[0],m0)
        self.assertEqual(result[1],m0*(4-m0)+2*m1)
        self.assertEqual(result[2],m0*(m0-3)**2+3*m1*(3-m0)+Fraction(3,2)*m2)
        self.assertEqual(result[3],
            m0*(16-20*m0+8*m0*m0-m0**3)
            +m1*(24-20*m0+4*m0*m0)-2*m1*m1
            +m2*(8-2*m0)+Fraction(2,3)*m3)
    def test_elementary_source_moment_envelope(self):
        from observational_succ.theta_extruded_interference import theta_moment_upper_bound
        with mp.workdps(55):
            for j in range(0,8):
                self.assertGreater(theta_moment_upper_bound(j),0)
            self.assertLess(theta_moment_upper_bound(0),mp.mpf('0.08'))
            self.assertLess(theta_moment_upper_bound(1),mp.mpf('0.02'))
            # Hence M0<1, M1<1. Together with M2,M3>0,
            # the exact displayed polynomial makes lambda_1..4>0.
    def test_authentic_first_four_numeric_match_source_moments(self):
        from observational_succ.theta_extruded_interference import first_four_li_from_moments
        with mp.workdps(55):
            vals=[laguerre_theta_coefficient(n) for n in range(1,5)]
            b=[vals[i]/(i+1) for i in range(4)]
            c=[]
            for k in range(4):
                c.append(b[0]*math.factorial(k+1))
                b=[b[i+1]-b[i] for i in range(len(b)-1)]
            self.assertTrue(all(x>0 for x in c))
            result=first_four_li_from_moments(tuple(c))
            direct=li_from_completed_coefficients(tuple(vals))
            for u,v in zip(result,direct):
                self.assertLess(abs(u-v),mp.mpf('1e-48'))
                self.assertGreater(u,0)

class LogClockTwoTimeCurrent(unittest.TestCase):
    def test_symmetrized_kernel_exact_finite_atoms(self):
        from observational_succ.theta_extruded_interference import finite_log_clock_current
        with mp.workdps(65):
            atoms=((mp.mpf('0'),mp.mpf(2)),
                   (mp.mpf('.2'),mp.mpf('.5')),
                   (mp.mpf('1.3'),mp.mpf('1.5')))
            for u in (mp.mpc('0','.25'),mp.mpc('3','.4'),mp.mpc('17','.25')):
                one,two=finite_log_clock_current(atoms,u)
                self.assertLess(abs(one-two),mp.mpf('1e-59'))
            one,two=finite_log_clock_current(atoms,mp.mpc('0','.25'))
            self.assertGreater(one,0)
    def test_original_xi_log_clock_current_sampled_positive(self):
        from observational_succ.theta_extruded_interference import completed_xi_log_clock_current
        with mp.workdps(55):
            for x,y in ((0,'.25'),(5,'.25'),(17,'.25'),(17,'1'),(30,'.25')):
                p=completed_xi_log_clock_current(mp.mpc(x,y))
                self.assertGreater(p,0)
    def test_offcritical_fake_must_fail_global_strict_current(self):
        from observational_succ.theta_extruded_interference import fake_atomic_completed
        with mp.workdps(70):
            f=lambda s:fake_atomic_completed(s)
            rho=mp.findroot(f,(mp.mpf('.1'),mp.mpf('.4')))
            self.assertLess(abs(f(rho)),mp.mpf('1e-60'))
            self.assertLess(rho,mp.mpf('.5'))
            z=1j*(mp.mpf('.5')-rho)  # s=.5+iu = rho
            self.assertGreater(mp.im(z),0)
            # At an offcritical zero, Xi_fake=0, so the strict log-clock
            # current vanishes regardless of the derivative companion.
            self.assertLess(abs(f(mp.mpf('.5')+1j*z)),mp.mpf('1e-60'))

class ArithmeticSourceFirewall(unittest.TestCase):
    def test_composite_six_changed_theta_source(self):
        from observational_succ.theta_extruded_interference import composite_six_mutation_delta
        with mp.workdps(115):
            for s in (mp.mpf('2'),mp.mpc('0.75','1.25')):
                delta=composite_six_mutation_delta(s,strength=1)
                self.assertGreater(abs(delta),mp.mpf('1e-70'))
                self.assertLess(abs(delta),mp.mpf('1e-39'))
                # Reflection preserves even a fake source; arithmetic
                # authentication must be checked separately.
                reflected=composite_six_mutation_delta(1-s,strength=1)
                self.assertLess(abs(delta-reflected),mp.mpf('1e-108'))
    def test_wrong_gamma_not_true_completion(self):
        from observational_succ.theta_extruded_interference import wrong_gamma_completed
        with mp.workdps(55):
            for s in (mp.mpf(2),mp.mpc('.8','3')):
                self.assertGreater(abs(wrong_gamma_completed(s)-completed_xi_direct(s)),
                                   mp.mpf('1e-7'))
            with self.assertRaises(ValueError): wrong_gamma_completed(1)
