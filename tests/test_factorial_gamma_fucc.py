"""Exact SUCC×FUCC factorial/Gamma controls; mpmath only for oracle tests."""
import unittest
import json
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial

import mpmath as mp

from observational_succ.factorial_gamma_fucc import (
    FactorialGammaGateError, bareiss_determinant, beta_gamma_backward_moment,
    binomial_cocycle, clock_characteristic, complex_binomial_cocycle,
    counterfeit_hankel, counterfeit_two_atom_moment,
    factorial_hankel, factorial_hankel_certificate, factorial_pascal_factor,
    finite_exponential_clock_band_certificate, finite_source_countermodel_certificate,
    fucc_factorial_dilation_certificate, fucc_succ_square,
    gamma_characteristic, gamma_recurrence_conjugacy, gamma_twist_mutant,
    laguerre_orthogonality_certificate, monic_laguerre_coefficients,
    primes_through, spiral_dynamics,
    archimedean_clock_ratio, archimedean_ratio_oracle,
    beta_product_moment_certificate, scaled_order_statistic_cdf_certificate,
    ordered_uniform_beta_isomorphism,
)


class TestPinnedResearchReceipt(unittest.TestCase):
    def test_receipt_matches_recomputed_exact_source(self):
        from scripts.factorial_gamma_fucc_probe import exact_receipt
        root=Path(__file__).resolve().parents[1]
        target=root/'research/2026-10-16/FACTORIAL_GAMMA_FUCC_RECEIPT.json'
        self.assertEqual(json.loads(target.read_text(encoding='utf-8')),
                         exact_receipt())


class TestFactorialPascalHankel(unittest.TestCase):
    def test_exact_hankel_pascal_through_8(self):
        for size in range(1,9):
            with self.subTest(size=size):
                c=factorial_hankel_certificate(size)
                self.assertEqual(c['H'], factorial_hankel(size))
                self.assertTrue(c['positive_definite'])
                self.assertEqual(c['determinant'],
                                 bareiss_determinant(c['H']))
                self.assertFalse(c['RH_proved'])

    def test_factorial_pascal_succ_recurrence(self):
        a=factorial_pascal_factor(11)
        for n in range(10):
            for k in range(11):
                lhs=a[n+1][k]
                rhs=(n+1)*(a[n][k]+(a[n][k-1] if k else 0))
                self.assertEqual(lhs,rhs)

    def test_first_factorial_values(self):
        self.assertEqual(factorial_hankel(3),((1,1,2),(1,2,6),(2,6,24)))
        self.assertEqual(factorial_pascal_factor(3),((1,0,0),(1,1,0),(2,4,2)))
        self.assertEqual(bareiss_determinant(factorial_hankel(3)),4)

    def test_exact_matrix_rejects_malformed(self):
        with self.assertRaises(FactorialGammaGateError):
            bareiss_determinant(((1,2),))
        with self.assertRaises(FactorialGammaGateError):
            bareiss_determinant(((1,1),(1,0.5)))
        for n in (0,-1,True,2.0,26):
            with self.assertRaises(FactorialGammaGateError):
                factorial_hankel(n)


class TestMomentUniquenessAndCountermodels(unittest.TestCase):
    def test_laguerre_orthogonal_moment_polynomials(self):
        for m in range(1,10):
            with self.subTest(degree=m):
                c=laguerre_orthogonality_certificate(m)
                self.assertEqual(c['lower_orthogonality'],(0,)*m)
                self.assertEqual(c['squared_norm'],factorial(m)**2)
                self.assertEqual(c['first_missing_moment'],2*m)

    def test_historical_gauss2_exact_construction(self):
        self.assertEqual(monic_laguerre_coefficients(2),(2,-4,1))
        expected=(1,1,2,6,20,68,232,792)
        self.assertEqual(tuple(counterfeit_two_atom_moment(k) for k in range(8)),expected)
        cert=finite_source_countermodel_certificate()
        self.assertEqual(cert['agree_through'],3)
        self.assertEqual(cert['first_discrepancy'],4)
        self.assertEqual(cert['genuine_hankel_3_det'],4)
        self.assertEqual(cert['atomic_hankel_3_det'],0)
        self.assertEqual(counterfeit_hankel(3)[2][2],20)

    def test_gauss_laguerre_three_atom_fresh_holdout(self):
        # Independent mpmath quadrature; implementation does not use node-finding.
        with mp.workdps(70):
            xs, ws=mp.gauss_quadrature(3,'laguerre')
            self.assertEqual(len(xs),3)
            self.assertTrue(all(x>0 for x in xs))
            self.assertTrue(all(w>0 for w in ws))
            for k in range(6):
                observed=mp.fsum(ws[i]*xs[i]**k for i in range(3))
                self.assertLess(abs(observed-mp.factorial(k)),mp.mpf('1e-55'))
            missing=mp.fsum(ws[i]*xs[i]**6 for i in range(3))
            self.assertLess(abs(mp.factorial(6)-missing-36),mp.mpf('1e-50'))

    def test_two_atom_fourier_not_gamma_or_decaying(self):
        with mp.workdps(65):
            a=mp.sqrt(2)
            wm=(2+a)/4;wp=(2-a)/4
            xm=2-a;xp=2+a
            t=mp.mpf('1.73')
            mimic=wm*mp.exp(1j*t*mp.log(xm))+wp*mp.exp(1j*t*mp.log(xp))
            gamma=mp.gamma(1+1j*t)
            self.assertGreater(abs(mimic-gamma),mp.mpf('0.01'))
            # Exact resonance at every integer multiple of period from log-node ratio.
            period=2*mp.pi/mp.log(xp/xm)
            phase=wm*mp.exp(1j*period*mp.log(xm))+wp*mp.exp(1j*period*mp.log(xp))
            self.assertLess(abs(abs(phase)-1),mp.mpf('1e-55'))

    def test_hankel_rank_negative_control(self):
        for size in (3,4,5,6):
            self.assertEqual(bareiss_determinant(counterfeit_hankel(size)),0)
            self.assertGreater(bareiss_determinant(factorial_hankel(size)),0)


class TestFuccInterleaving(unittest.TestCase):
    def test_primes_are_authenticated(self):
        self.assertEqual(primes_through(12),(2,3,5,7,11))
        for p in (4,6,9,25,1,True,3.0):
            with self.assertRaises(FactorialGammaGateError):
                fucc_succ_square(p,2)

    def test_affine_succ_fucc_square(self):
        for p in (2,3,5,7,11):
            for n in (0,1,2,11):
                c=fucc_succ_square(p,n)
                self.assertEqual(c['V_after_S'],c['S_power_p_after_V'])
                self.assertNotEqual(c['V_after_S'],c['false_S_after_V'])
                self.assertTrue(c['flat_commuting_square'])

    def test_multinomial_prime_carries(self):
        for p in (2,3,5,7,11):
            for n in (1,2,3,5,9):
                c=fucc_factorial_dilation_certificate(p,n)
                self.assertEqual(c['dilation_multinomial'],
                                 factorial(p*n)//factorial(n)**p)
                self.assertEqual(c['prime_factor_reconstruction'],c['dilation_multinomial'])
                self.assertFalse(c['square_has_nontrivial_holonomy'])

    def test_nonzero_carries_control(self):
        c=fucc_factorial_dilation_certificate(2,1)
        self.assertEqual(c['dilation_multinomial'],2)
        self.assertEqual(c['q_adic_carries'],{2:1})
        c=fucc_factorial_dilation_certificate(3,2)
        self.assertEqual(c['dilation_multinomial'],90)
        self.assertEqual(c['q_adic_carries'],{2:1,3:2,5:1})

    def test_cocycle_on_nat(self):
        for a in (0,1,2,5,7):
            for b in (0,1,4):
                for c in (0,3,8):
                    x=binomial_cocycle(a,b,c)
                    self.assertTrue(x['equal'])
                    self.assertEqual(x['left'],x['right'])

    def test_analytic_cocycle_holdout(self):
        values=(0.13+0.67j,1.1-0.27j,0.3+0.04j)
        c=complex_binomial_cocycle(*values, dps=65)
        self.assertLess(abs(c['error']),mp.mpf('1e-55'))

    def test_beta_gamma_backward_rational_moments(self):
        for n in range(9):
            for r in range(8):
                x=beta_gamma_backward_moment(n,r)
                self.assertEqual(x['beta_r_moment']*x['next_shape_moment'],x['previous_shape_moment'])
                self.assertEqual(x['backward_log_delay_rate'],n+1)


class TestFiniteUniformBetaPoissonSource(unittest.TestCase):
    def test_all_finite_positive_beta_product_moments(self):
        for n in (0,1,3,10):
            for M in (30,100,300):
                for r in (0,1,2,5,9):
                    with self.subTest(n=n,M=M,r=r):
                        x=beta_product_moment_certificate(n,M,r)
                        expected=F(factorial(n+r),factorial(n))
                        factor=F(M**r*factorial(M),factorial(M+r))
                        self.assertEqual(x['limiting_Gamma_shape_moment'],expected)
                        self.assertEqual(x['finite_factorial_correction'],factor)
                        self.assertEqual(x['finite_positive_Beta_product_moment'],factor*expected)
                        self.assertGreaterEqual(x['positive_moment_deficit'],0)
                        self.assertLessEqual(x['positive_moment_deficit'],x['rational_deficit_upper'])

    def test_scaled_minimum_is_exact_finite_beta_source(self):
        # Minimum of M uniform points has CDF 1-(1-x/M)^M.
        for M in (6,20,120):
            for x in (F(1,2),F(2),F(4)):
                c=scaled_order_statistic_cdf_certificate(0,M,x)
                self.assertEqual(c['finite_uniform_order_statistic_cdf'],1-(1-x/M)**M)
                self.assertLessEqual(c['rational_CDF_error_upper'],x*x/M)

    def test_poisson_gamma_threshold_quantitative_holdouts(self):
        with mp.workdps(75):
            for n,M,x in ((0,100,F(1,3)),(0,200,F(2)),(2,80,F(3)),
                          (3,250,F(5,2)),(6,140,F(8))):
                c=scaled_order_statistic_cdf_certificate(n,M,x)
                threshold=mp.mpf(x.numerator)/x.denominator
                target=1-mp.exp(-threshold)*mp.fsum(threshold**k/mp.factorial(k)
                                                    for k in range(n+1))
                q=c['finite_uniform_order_statistic_cdf']
                exact=mp.mpf(q.numerator)/q.denominator
                err=abs(exact-target)
                b=c['rational_CDF_error_upper']
                self.assertLess(err,mp.mpf(b.numerator)/b.denominator)

    def test_finite_beta_product_is_order_statistic_distribution(self):
        # Independent oracle: mpmath beta distribution moment integral.
        with mp.workdps(60):
            n,M=2,15
            a,b=n+1,M-n
            for r in range(7):
                expected=mp.beta(a+r,b)/mp.beta(a,b)*M**r
                c=beta_product_moment_certificate(n,M,r)
                q=c['finite_positive_Beta_product_moment']
                self.assertLess(abs(expected-mp.mpf(q.numerator)/q.denominator),mp.mpf('1e-52'))

    def test_exact_joint_order_statistics_beta_map(self):
        for coords in ((F(1,2),), (F(1,2),F(2,3)),
                       (F(1,4),F(3,5),F(5,7),F(7,8)),
                       (F(2,7),F(4,9),F(3,10),F(8,11),F(10,13))):
            c=ordered_uniform_beta_isomorphism(coords)
            self.assertEqual(c['recovered_beta_coordinates'],coords)
            self.assertEqual(c['input_joint_beta_density'],
                             factorial(len(coords))*c['absolute_jacobian'])
            self.assertTrue(c['source_map_invertible_on_open_simplex'])
            self.assertTrue(all(c['ordered_uniform_coordinates'][j]
                                < c['ordered_uniform_coordinates'][j+1]
                                for j in range(len(coords)-1)))

    def test_independent_symbolic_jacobian(self):
        # Fully independent symbolic differentiation, not reusing the module's
        # asserted product-Jacobian identity.
        import sympy as sp
        for M in (1,2,3,4,5):
            bs=sp.symbols('b0:'+str(M),positive=True)
            ordered=[sp.prod(bs[k:M]) for k in range(M)]
            matrix=sp.Matrix([[sp.diff(x,b) for b in bs] for x in ordered])
            actual=sp.factor(matrix.det())
            expected=sp.prod(bs[k]**k for k in range(M))
            self.assertEqual(sp.simplify(actual-expected),0)

    def test_order_statistic_beta_cdf_independent_oracle(self):
        # Independent Beta-density integration against the exact Binomial tail.
        with mp.workdps(65):
            n,M,x=2,45,F(7,3)
            c=scaled_order_statistic_cdf_certificate(n,M,x)
            scaled=mp.mpf(x.numerator)/x.denominator/M
            oracle=mp.betainc(n+1,M-n,0,scaled,regularized=True)
            frac=c['finite_uniform_order_statistic_cdf']
            exact=mp.mpf(frac.numerator)/frac.denominator
            self.assertLess(abs(exact-oracle),mp.mpf('1e-55'))

    def test_exact_probability_simplex_source_rejects_mutations(self):
        for coords in ((F(1,2),F(0)),(F(1,3),F(1)),
                       (F(1,2),0.2),[],(F(-1,2),)):
            with self.assertRaises(FactorialGammaGateError):
                ordered_uniform_beta_isomorphism(coords)

    def test_source_grammar_invalid(self):
        for n,M,x in ((5,5,F(1)),(0,6,F(7)),(0,6,F(-1)),
                      (True,6,F(1)),(0,6,0.1)):
            with self.assertRaises(FactorialGammaGateError):
                scaled_order_statistic_cdf_certificate(n,M,x)
        for n,M,r in ((3,3,1),(0,5,-1),(0,5,True),(0,5,2.0)):
            with self.assertRaises(FactorialGammaGateError):
                beta_product_moment_certificate(n,M,r)


class TestStochasticGammaFiniteClock(unittest.TestCase):
    def test_clock_approaches_gamma_independently(self):
        with mp.workdps(85):
            for n,t in ((0,0.3),(0,2.0),(2,-1.35),(5,3.2)):
                errors=[]
                for M in (60,250,1000):
                    observed=clock_characteristic(n,M,t,dps=80)
                    expected=gamma_characteristic(n,t,dps=80)
                    errors.append(abs(observed-expected))
                self.assertLess(errors[-1],errors[0])
                self.assertLess(errors[-1],mp.mpf('0.02'))

    def test_uniform_rational_bounds_standalone(self):
        c=finite_exponential_clock_band_certificate(3,400,F(4))
        self.assertIsInstance(c['log_ratio_bound'],F)
        self.assertIsInstance(c['uniform_absolute_error_upper'],F)
        self.assertLess(c['uniform_absolute_error_upper'],F(1,20))
        self.assertFalse(c['gamma_values_used_to_build_approximant'])
        self.assertFalse(c['RH_proved'])
        for M in (100,400,1600):
            c=finite_exponential_clock_band_certificate(0,M,F(3))
            with mp.workdps(60):
                for t in (-3,-2,0,1.5,3):
                    actual=abs(clock_characteristic(0,M,t,dps=65)-gamma_characteristic(0,t,dps=65))
                    self.assertLess(actual,mp.mpf(c['uniform_absolute_error_upper'].numerator)
                                               /c['uniform_absolute_error_upper'].denominator)

    def test_bound_monotonic_and_jensen_independent(self):
        cs=[finite_exponential_clock_band_certificate(0,M,F(3)) for M in (100,400,1600)]
        self.assertGreater(cs[0]['uniform_absolute_error_upper'],cs[1]['uniform_absolute_error_upper'])
        self.assertGreater(cs[1]['uniform_absolute_error_upper'],cs[2]['uniform_absolute_error_upper'])
        for c in cs:
            self.assertGreater(c['independent_coupling_error_upper'],c['uniform_absolute_error_upper'])

    def test_clock_refuses_outside_claim_domain(self):
        for n,M,T in ((0,0,F(1)),(3,3,F(1)),(0,10,F(11)),(0,2,F(3)),
                       (0,10,F(-1)),(0,10,0.2),(True,10,F(1))):
            with self.assertRaises(FactorialGammaGateError):
                finite_exponential_clock_band_certificate(n,M,T)

    def test_integer_gamma_recurrence_conjugacy(self):
        for n,t in ((0,0),(1,2),(4,-0.7),(8,6)):
            c=gamma_recurrence_conjugacy(n,t,dps=75)
            self.assertLess(c['absolute_defect'],mp.mpf('1e-60'))

    def test_spiral_strict_radial_direction_and_angle_n_positive(self):
        for n in (1,2,5):
            before=spiral_dynamics(n,-1.0,dps=70)
            middle=spiral_dynamics(n,0,dps=70)
            after=spiral_dynamics(n,1.0,dps=70)
            self.assertGreater(before['radial_log_slope'],0)
            self.assertLess(after['radial_log_slope'],0)
            self.assertLess(abs(middle['radial_log_slope']),mp.mpf('1e-60'))
            self.assertGreater(middle['unwrapped_angle_slope'],0)
            self.assertGreater(before['unwrapped_angle_slope'],0)
            self.assertGreater(after['unwrapped_angle_slope'],0)
            self.assertEqual(middle['expected_radius_direction'],'stationary')

    def test_periodic_gauge_preserves_modulus_while_spoofing_phase(self):
        x=gamma_twist_mutant(3,0.45,F(1,3),dps=80)
        self.assertLess(x['radial_difference'],mp.mpf('1e-65'))
        self.assertGreater(abs(x['mutant']-x['genuine']),mp.mpf('0.1'))
        self.assertFalse(x['positive_Mellin_source_authenticated'])
        y=gamma_twist_mutant(3,0,4,dps=80)
        self.assertLess(abs(y['mutant']-factorial(3)),mp.mpf('1e-65'))

    def test_archimedean_real_place_phase_transport(self):
        # Fresh target: Γ_R(2n+2+2it)/Γ_R(2n+2), not ordinary Γ(s).
        for n,t in ((0,0.75),(2,-1.6),(5,2.5)):
            with mp.workdps(75):
                actual=archimedean_clock_ratio(n,800,t,dps=75)
                oracle=archimedean_ratio_oracle(n,t,dps=75)
                rational=finite_exponential_clock_band_certificate(n,800,F(3))[
                    'uniform_absolute_error_upper']
                self.assertLess(abs(actual-oracle),
                                mp.mpf(rational.numerator)/rational.denominator)
                self.assertGreater(abs(clock_characteristic(n,800,t,dps=75)-oracle),
                                   mp.mpf('0.01'))

    def test_archimedean_direct_dirac_and_exponential_source_agree(self):
        # Third, genuinely different numerical evaluation from PR #141's
        # finite Gaussian Dirac comb. This is a check, not a rigorous interval.
        with mp.workdps(70):
            n,t=2,mp.mpf('0.7')
            h=mp.mpf('0.125')
            def real_gamma_comb(tau):
                s=2*n+2+2j*tau
                return h*mp.fsum(mp.exp(s*(h*k)/2-mp.pi*mp.exp(h*k))
                                 for k in range(-400,80))
            dirac_ratio=real_gamma_comb(t)/real_gamma_comb(mp.mpf(0))
            gamma_r_oracle=archimedean_ratio_oracle(n,t,dps=70)
            exp_clock=archimedean_clock_ratio(n,1000,t,dps=70)
            self.assertLess(abs(dirac_ratio-gamma_r_oracle),mp.mpf('1e-22'))
            self.assertLess(abs(exp_clock-gamma_r_oracle),mp.mpf('0.02'))

    def test_clock_factor_is_not_prime_euler_multiplicative(self):
        with mp.workdps(70):
            t=mp.mpf('2.5')
            local=lambda k: k/(k+1j*t)
            self.assertGreater(abs(local(6)-local(2)*local(3)),mp.mpf('0.01'))


if __name__ == '__main__':
    unittest.main()
