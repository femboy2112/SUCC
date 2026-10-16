"""Hostile tests for the original signed zeta Weil source on a rational B-spline grammar."""
import unittest
from fractions import Fraction as Q
from random import Random
from observational_succ.prime_active_weil_splines import (
    WeilSplineGate, Iv, exp_minus, exp_any, log_int, pi_interval,
    euler_gamma_interval, zeta_contact, central_bspline7_at_rational,
    completed_weil_bspline_entry, genuine_prime_tape,
    two_spline_prime_active_gram, gamma_tail_error,
    original_legendre_spline_projection, contact_neumann_gram,
    contact_mutant_gram, fake6_source_probe,
    cubic_spline_derivative_segments, _poly_integral,
    _prime_label, pole_integral,
)

class IntervalControls(unittest.TestCase):
    def test_arithmetic_interval_contains_exact_rationals(self):
        r=Random(1337)
        for _ in range(100):
            x=Q(r.randint(-100,100),r.randint(1,70))
            y=Q(r.randint(-100,100),r.randint(1,70))
            xx,yy=Iv.q(x),Iv.q(y)
            for operation,value in ((xx+yy,x+y),(xx-yy,x-y),(xx*yy,x*y),(xx*Q(7,19),x*Q(7,19))):
                self.assertLessEqual(operation.lower,value)
                self.assertGreaterEqual(operation.upper,value)

    def test_exp_log_pi_gamma_controls_against_independent_mpmath(self):
        import mpmath as mp
        mp.mp.dps=75
        for q in (Q(0),Q(1,17),Q(1,2),Q(7,4),Q(137,2),Q(501)):
            r=exp_minus(q)
            value=mp.exp(-mp.mpf(q.numerator)/q.denominator)
            self.assertLessEqual(mp.mpf(r.lo)/10**55,value)
            self.assertGreaterEqual(mp.mpf(r.hi)/10**55,value)
        for q in (Q(-7,3),Q(0),Q(2,7),Q(7,3)):
            r=exp_any(q)
            v=mp.exp(mp.mpf(q.numerator)/q.denominator)
            self.assertLessEqual(mp.mpf(r.lo)/10**55,v)
            self.assertGreaterEqual(mp.mpf(r.hi)/10**55,v)
        for n in (2,3,4,6,9,27):
            r=log_int(n)
            self.assertLessEqual(mp.mpf(r.lo)/10**55,mp.log(n))
            self.assertGreaterEqual(mp.mpf(r.hi)/10**55,mp.log(n))
        p=pi_interval()
        g=euler_gamma_interval()
        c=zeta_contact()
        for v,z in ((p,mp.pi),(g,mp.euler),(c,-mp.euler-mp.log(4*mp.pi))):
            self.assertLessEqual(mp.mpf(v.lo)/10**55,z)
            self.assertGreaterEqual(mp.mpf(v.hi)/10**55,z)

    def test_bad_inputs_and_forged_labels(self):
        for bad in (0,-1,True,0.2):
            with self.assertRaises(WeilSplineGate):
                completed_weil_bspline_entry(bad,Q(0))
        for n in (6,10,12,15,18,30,36,42):
            self.assertIsNone(_prime_label(n))
        for n,p in ((2,2),(4,2),(8,2),(9,3),(25,5),(27,3)):
            self.assertEqual(_prime_label(n),p)
        with self.assertRaises(WeilSplineGate):
            completed_weil_bspline_entry(Q(1,5),Q(0),tape=((2,2),(6,6)))
        with self.assertRaises(WeilSplineGate):
            completed_weil_bspline_entry(Q(1,5),Q(1,10),tape=())

class SourceGeometry(unittest.TestCase):
    def test_g_is_exact_bspline_convolution(self):
        self.assertEqual(central_bspline7_at_rational(Q(0)),Q(151,315))
        self.assertEqual(central_bspline7_at_rational(Q(4)),0)
        self.assertEqual(central_bspline7_at_rational(Q(1,2)),Q(259723,645120))
        # Integrated B3 spline is the fourfold uniform density. B7 is eightfold.
        # For centered autocorrelation scaling h=1/5, contact Gram is exact.
        k=contact_neumann_gram()
        self.assertEqual(k['diag'],Q(151,63))
        self.assertEqual(k['cross'],Q(259723,129024))
        self.assertGreater(k['eigenvalues'][1],0)

    def test_first_prime_active_and_spoofed_source(self):
        self.assertEqual(genuine_prime_tape(Q(1,5),Q(0)),((2,2),))
        self.assertEqual(genuine_prime_tape(Q(1,5),Q(1,10)),((2,2),))
        self.assertLess(Q(9,10),log_int(6).lower)
        r=fake6_source_probe()
        self.assertTrue(r['strictly_negative'])
        self.assertLess(r['fake6_signed_effect'].upper,0)
        with self.assertRaises(WeilSplineGate):
            completed_weil_bspline_entry(Q(1,2),Q(0),tape=((2,2),(3,3),(6,6)))

    def test_exact_pole_laplace_formula_against_independent_quadrature(self):
        import mpmath as mp
        mp.mp.dps=65
        from math import comb
        def bs7(x):
            return mp.fsum((-1)**j*comb(8,j)*max(x+4-j,0)**7 for j in range(9))/5040
        h=mp.mpf(1)/5; d=mp.mpf(1)/10
        g=lambda x: bs7((x-d)/h)/h
        knots=sorted({d+(j-4)*h for j in range(9)})
        val=mp.fsum(mp.quad(lambda x:g(x)*(mp.exp(x/2)+mp.exp(-x/2)),[a,b])
                    for a,b in zip(knots[:-1],knots[1:]))
        interval=pole_integral(Q(1,5),Q(1,10))
        self.assertLessEqual(mp.mpf(interval.lo)/10**55,val)
        self.assertGreaterEqual(mp.mpf(interval.hi)/10**55,val)

    def test_legendre_P30_source_leakage_is_positive(self):
        for t in (Q(0),Q(1,10)):
            z=original_legendre_spline_projection(t=t,rank=30)
            self.assertEqual(z['full_L2_norm_squared'],Q(250,3))
            self.assertEqual(z['first_mode_integrals'][0],0)
            self.assertTrue(z['high_residual_nonzero'])
            self.assertGreater(z['high_residual_norm_squared'],0)
            self.assertLess(z['high_residual_norm_squared'],Q(1,100))
            self.assertFalse(z['low_Schur_sign_proved'])
        # Compare polynomial primitive antiderivative over each segment.
        for t in (Q(0),Q(1,10)):
            s=cubic_spline_derivative_segments(Q(1,5),t)
            self.assertEqual(sum((_poly_integral(c,lo,hi) for lo,hi,c in s),Q(0)),0)

class OriginalWeilCertificate(unittest.TestCase):
    def test_analytic_tail_decreases(self):
        self.assertGreater(gamma_tail_error(Q(1,5),16),gamma_tail_error(Q(1,5),32))
        self.assertGreater(gamma_tail_error(Q(1,5),32),gamma_tail_error(Q(1,5),64))

    def test_original_prime_active_matrix_strictly_psd(self):
        z=two_spline_prime_active_gram(J=64)
        self.assertEqual(z['Suzuki_radius'],Q(1,2))
        self.assertTrue(z['is_positive_certified'])
        self.assertGreater(z['smallest_eigenvalue_lower'],Q(1,16))
        self.assertTrue(z['certified_relative_neumann_coercive'])
        self.assertGreater(z['source_relative_neumann_lower'],Q(1,50))
        self.assertFalse(z['original_low_schur_sign_verified'])
        self.assertFalse(z['all_a_or_RH_proved'])
        for x in ('diag','cross'):
            c=z[x]
            self.assertEqual(c['source_tape'],((2,2),))
            self.assertEqual(c['conductor'],1)
            self.assertEqual(c['parity'],0)
            self.assertEqual(c['half_density'],Q(1,2))
            self.assertEqual(c['poles'],(0,1))
            self.assertLess(c['prime'].upper,0)

    def test_raw_analytic_numerical_holdout_inside_rational_enclosures(self):
        import mpmath as mp
        mp.mp.dps=50
        from math import comb
        h=mp.mpf(1)/5
        def b7(x):
            return mp.fsum((-1)**j*comb(8,j)*max(x+4-j,0)**7 for j in range(9))/5040
        for d_r in (Q(0),Q(1,10)):
            d=mp.mpf(d_r.numerator)/d_r.denominator
            gg=lambda u: b7((u-d)/h)/h
            r=4*h+abs(d)
            knots=sorted({mp.mpf(0),r}|{abs(d+(j-4)*h) for j in range(9)})
            pp=mp.fsum(mp.quad(lambda u:gg(u)*(mp.exp(u/2)+mp.exp(-u/2)),[u,v])
                       for u,v in zip(sorted({d+(j-4)*h for j in range(9)})[:-1],sorted({d+(j-4)*h for j in range(9)})[1:]))
            def arch(u):
                if not u: return mp.mpf(0)
                dg=gg(u)+gg(-u)-2*mp.exp(-u/2)*gg(0)
                return mp.exp(-u/2)*dg/(-mp.expm1(-2*u))
            aa=mp.fsum(mp.quad(arch,[u,v]) for u,v in zip(knots[:-1],knots[1:]))+mp.quad(arch,[r,mp.inf])
            prime=mp.log(2)/mp.sqrt(2)*(gg(mp.log(2))+gg(-mp.log(2)))
            true=pp+(-mp.euler-mp.log(4*mp.pi))*gg(0)-aa-prime
            cert=completed_weil_bspline_entry(Q(1,5),d_r,J=64)['value']
            self.assertLessEqual(mp.mpf(cert.lo)/10**55,true)
            self.assertGreaterEqual(mp.mpf(cert.hi)/10**55,true)

    def test_genuine_source_contact_mutation_goes_strictly_negative(self):
        mutant=contact_mutant_gram(Q(-1,8),64)
        self.assertTrue(mutant['mutant_has_certified_negative'])
        self.assertLess(mutant['positive_vector_branch'][1],0)
        self.assertFalse(mutant['RH_disproved'])

if __name__=='__main__': unittest.main()

class FiniteWitnessClosure(unittest.TestCase):
    def test_hidden_positive_fake_non_euler_source_has_offcritical_roots(self):
        import mpmath as mp
        mp.mp.dps=80
        from observational_succ.prime_active_weil_splines import arbitrarily_hidden_positive_non_euler_source
        for m in (1,3,8):
            z=arbitrarily_hidden_positive_non_euler_source(m)
            self.assertEqual(z['offcritical_zero_real_part'],Q(3,4))
            self.assertTrue(z['all_coefficients_positive'])
            self.assertFalse(z['Euler_prime_source_authenticated'])
            self.assertFalse(z['functional_equation_authenticated'])
            N=z['N']; A=z['positive_dirichlet_weight']
            self.assertEqual(Q(A,6**(5*m)),z['uniform_multiplier_error_on_Re_s_at_least_5_over_4'])
            # Same function at its analytically prescribed offcritical zero.
            s=mp.mpf(3)/4+1j*mp.pi/mp.log(N)
            defect=1+mp.mpf(A)*mp.exp(-s*mp.log(N))
            self.assertLess(abs(defect),mp.mpf('1e-70'))
        self.assertLess(arbitrarily_hidden_positive_non_euler_source(8)['uniform_multiplier_error_on_Re_s_at_least_5_over_4'],Q(1,10**12))

    def test_continuity_budget_is_typed_not_automatically_certified(self):
        from observational_succ.prime_active_weil_splines import normalized_test_continuity_budget
        b=normalized_test_continuity_budget(Q(1,2),1,1,Q(1,1000),Q(1,1000))
        self.assertGreater(b,0)
        self.assertLess(b,1)
        with self.assertRaises(WeilSplineGate):
            normalized_test_continuity_budget(Q(1,2),1,1,Q(-1,1000),Q(1,1000))
        with self.assertRaises(WeilSplineGate):
            normalized_test_continuity_budget(Q(1,2),1,1,.001,.001)

    def test_rank4_leakage_is_large_despite_rank30_smallness(self):
        # The existing WB4 theorem reduces the hard low sector to P1..P4,
        # not P1..P30. These exact rational ratios block an invalid transfer.
        for t,ratio in ((Q(0),Q(2809,6250)),(Q(1,10),Q(869,3125))):
            r=original_legendre_spline_projection(t=t,rank=4)
            self.assertEqual(r['high_residual_norm_squared']/r['full_L2_norm_squared'],ratio)
            self.assertGreater(ratio,Q(1,4))
            self.assertFalse(r['low_Schur_sign_proved'])

    def test_30_legendre_leakage_is_small_but_not_zero(self):
        for t in (Q(0),Q(1,10)):
            r=original_legendre_spline_projection(t=t,rank=30)
            self.assertGreater(r['high_residual_norm_squared'],0)
            self.assertLess(r['high_residual_norm_squared']/r['full_L2_norm_squared'],Q(1,60000))


class SchurBoundaryNegativeControl(unittest.TestCase):
    def test_positive_finite_probes_do_not_fix_original_low_schur(self):
        # F=span(e1,e2,e3), Hhigh=span(e4) with D=1>0.
        # Even perfect positivity on span(e1,e2) leaves the e3 direction negative.
        from fractions import Fraction as R
        low_A=(R(1),R(1),R(-1))
        high_D=R(1)
        self.assertGreater(high_D,0)
        for x in ((1,0,0),(0,1,0),(1,1,0)):
            self.assertGreater(sum(low_A[i]*x[i]*x[i] for i in range(3)),0)
        negative=(0,0,1)
        self.assertLess(sum(low_A[i]*negative[i]*negative[i] for i in range(3)),0)
        # B=0 so the exact low Schur equals A, and remains indefinite.

class AuthenticLowLegendreBlock(unittest.TestCase):
    def test_actual_original_P1_P2_low_A_is_strictly_positive(self):
        from observational_succ.prime_active_weil_splines import original_two_mode_low_block
        x=original_two_mode_low_block(J=64)
        self.assertEqual(x['offdiag'],0)  # parity, not numerical fitting
        self.assertTrue(x['original_low_A_on_span_P1_P2_positive'])
        self.assertGreater(x['low_A11']['interval'].lower,Q(1,10000))
        self.assertGreater(x['low_A22']['interval'].lower,Q(1,5000))
        for tag in ('low_A11','low_A22'):
            self.assertEqual(x[tag]['source'],((2,2),))
            self.assertTrue(x[tag]['original_low_A_positive_certified'])
            self.assertFalse(x[tag]['original_low_Schur_S0_positive'])
        self.assertFalse(x['source_zero_shift_R0_computed'])
        self.assertFalse(x['Schur_S0_proved'])

    def test_full_completed_low_entries_against_independent_mpmath(self):
        import mpmath as mp
        from observational_succ.prime_active_weil_splines import genuine_original_low_legendre_diagonal
        mp.mp.dps=70
        coeffs={1:[Q(1,30),Q(0),Q(-1,6),Q(1,6),Q(0),Q(-1,30)],
                2:[Q(1,210),Q(0),Q(-1,10),Q(1,6),Q(0),Q(-1,10),Q(0),Q(1,35)]}
        for mode in (1,2):
            def gg(x):
                if not 0<=x<=1:return mp.mpf(0)
                return mp.fsum((mp.mpf(q.numerator)/q.denominator)*x**i
                               for i,q in enumerate(coeffs[mode]))
            g0=gg(mp.mpf(0))
            pole=2*mp.quad(lambda x:(mp.exp(x/2)+mp.exp(-x/2))*gg(x),[0,1])
            def arch_kern(x):
                if not x:return mp.mpf(0)
                return (mp.exp(-x/2)*(2*gg(x)-2*mp.exp(-x/2)*g0)
                        /(-mp.expm1(-2*x)))
            arch=(-mp.euler-mp.log(4*mp.pi))*g0-mp.quad(arch_kern,[0,1,mp.inf])
            prime=-2*mp.log(2)/mp.sqrt(2)*gg(mp.log(2))
            val=pole+arch+prime
            cert=genuine_original_low_legendre_diagonal(mode,64)['interval']
            self.assertLessEqual(mp.mpf(cert.lo)/10**55,val)
            self.assertGreaterEqual(mp.mpf(cert.hi)/10**55,val)

    def test_positive_A_does_not_automatically_dominate_high_short(self):
        from observational_succ.prime_active_weil_splines import original_two_mode_low_block
        x=original_two_mode_low_block(64)
        A1=x['low_A11']['interval']
        # Two positive candidate residuals compatible with R0>=0 but
        # having different low-Schur signs; neither is claimed as TRUE source.
        assert A1.lower>0
        R0_zero=Q(0)
        R0_toy=Q(1,5000)
        self.assertGreater(A1.lower-R0_zero,0)
        self.assertLess(A1.upper-R0_toy,0)
