import unittest
from fractions import Fraction as F
from math import factorial
from observational_succ import oily_macaroni_transfer as o
from observational_succ.succ_internal_matrix_walk import authentic_r as canonical_r


class ExactSource(unittest.TestCase):
    def test_source(self):
        self.assertEqual(tuple(o.source_taylor_moment(i) for i in range(4)),(0,15,-59,243))
        for n in range(1,50):
            self.assertEqual(o.authentic_r(n),F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
            self.assertGreater(o.authentic_r(n),0)
            self.assertEqual(o.authentic_r(n),canonical_r(n))
            self.assertEqual(o.source_moment(n,0),1)
    def test_fib(self):
        self.assertEqual(tuple(o.fibonacci_ratio(k) for k in range(1,6)),(F(1),F(1,2),F(2,3),F(3,5),F(5,8)))
    def test_gamma_two_moments(self):
        self.assertAlmostEqual(float(o.source_moment(1000,1)),2,delta=.002)
        self.assertAlmostEqual(float(o.source_moment(1000,2)),6,delta=.012)
    def test_finite_SUCC_jet(self):
        import mpmath as m
        lo,hi=o.finite_first_jet_bounds(256,16)
        v=o.golden(m)-m.euler
        self.assertLess(float(lo),float(v))
        # H_N-logN gamma over-estimates gamma, first jet below limit for m large
        self.assertLess(lo,hi)
        self.assertGreater(float(lo),float(v)-.01)
    def test_mutant_unchanged_jets(self):
        self.assertGreater(o.mutant_r(1,F(1,2)),o.authentic_r(1))
        for n in (16,64,256):
            a=o.source_a(n)
            extra=o.mutant_r(n,F(1))-o.authentic_r(n)
            self.assertGreater(extra,0)
            self.assertLess(extra,6*F(1,a**4))
    def test_frullani_exact(self):
        for n in (1,2,16):
            const,terms=o.frullani_square_log_weights(n)
            self.assertEqual(const,-1)
            self.assertEqual(sum(c for _,c in terms),0)
            self.assertIn(0,tuple(s for s,_ in terms))
        self.assertEqual(o.chi_square_limit_coefficient(),F(3481,450))
    def test_no_false_claims(self):
        receipt=o.source_rank_and_claims()
        for key in ('golden_unique_for_bbp','source_selected_weyl_saving','pi_normality_proved','RH_proved'):
            self.assertFalse(receipt[key])
    def test_green_intervals(self):
        for n in (1,8,64):
            low,high=o.green_tail_bounds(n,12)
            deeper_low,deeper_high=o.green_tail_bounds(n,24)
            self.assertLess(low,deeper_low)
            self.assertLessEqual(deeper_high,high)
            self.assertLess(high-low,F(1,16**12))

    def test_overlap(self):
        for n in (1,3,16,64):
            self.assertEqual(o.unweighted_overlap_square(n,n),F(1))
        for n,m in ((1,2),(3,9),(16,32),(32,256)):
            self.assertGreater(o.unweighted_overlap_square(n,m),0)
            self.assertLess(o.unweighted_overlap_square(n,m),1)


class AnalyticComplex(unittest.TestCase):
    def test_moment_identity(self):
        import mpmath as m
        for n in (1,16,64):
            for k in (0,1,2):
                got=o.complex_joint_mellin(n,k,0)
                expv=o.source_moment(n,k)
                with m.workdps(70):
                    self.assertLess(abs(got-m.mpf(expv.numerator)/expv.denominator),m.mpf('1e-60'))
    def test_independent_complex_integral_oracle(self):
        import mpmath as mp
        with mp.workdps(45):
            n=2
            a=o.source_a(n)
            z=mp.mpc('0.3','0.15')
            s=mp.mpc('0.15','-0.2')
            r=mp.mpf(o.authentic_r(n).numerator)/o.authentic_r(n).denominator
            Q=lambda x: 4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)
            val=mp.quad(lambda x: mp.exp(-a*(1+s)*x)*Q(x)*(a*x)**z/r,[0,1,mp.inf])
            got=o.complex_joint_mellin(n,z,s,precision=75)
            self.assertLess(abs(got-val),mp.mpf('1e-35'))

    def test_char_normalized(self):
        for n in (1,16,64):
            self.assertAlmostEqual(abs(o.source_oily_character(n,0)-1),0,delta=1e-35)
    def test_defect_asymptotic(self):
        import mpmath as m
        target=F(59,30)*(1+o.golden(m))
        for n,bound in ((16,.11),(64,.03),(256,.01)):
            self.assertLess(abs(o.source_a(n)*o.oily_defect_no_gamma(n)-float(target)),bound)
    def test_chi2_limit(self):
        target=float(o.chi_square_limit_coefficient())
        for n,bound in ((16,.6),(64,.15),(256,.04)):
            chi=float(o.chi_square_observed(n))
            self.assertGreater(chi,0)
            self.assertLess(abs(o.source_a(n)**2*chi-target),bound)
    def test_signed_complex_correction(self):
        for t in (.4,1.2,2.1):
            errors=[]
            for n in (16,64,256):
                got=o.source_oily_character(n,t)
                ref=o.gamma2_oily_character(t)
                corr=o.first_complex_correction(n,t)
                errors.append(abs(got-ref-corr)*o.source_a(n)**2)
                self.assertLess(abs(got-ref),.10)
            self.assertLess(float(errors[-1]),float(errors[0])*1.5)
    def test_overlap_symmetry(self):
        for n,m,h,t in ((2,3,1,.5),(4,9,2,1.3)):
            x=o.complex_time_kernel(n,m,h,t)
            y=o.complex_time_kernel(m,n,h,t)
            with __import__("mpmath").workdps(70):
                self.assertLess(abs(x-y.conjugate()),1e-45)
            self.assertLessEqual(abs(x),1+1e-30)
            with __import__("mpmath").workdps(70):
                self.assertLess(abs(o.complex_time_kernel(n,n,h,t)-1),1e-45)
    def test_log_kernel_limit(self):
        self.assertAlmostEqual(float(o.limiting_log_scale_kernel(2,0).real),8/9)
        x=o.limiting_log_scale_kernel(3,1)
        y=o.limiting_log_scale_kernel(F(1,3),1)
        with __import__("mpmath").workdps(70):
                self.assertLess(abs(x-y.conjugate()),1e-45)
    def test_uniform_complex_error(self):
        for n in (3,16,64):
            a=o.source_a(n)
            for t in (0.0, .3, 1.5, 10.0, 50.0):
                got=o.source_oily_character(n,t)
                ref=o.gamma2_oily_character(t)
                first=o.first_complex_correction(n,t)
                self.assertLess(abs(got-ref-first),64/a**2)
    def test_source_kernel_unweighted_overlap(self):
        import mpmath as m
        for n,k in ((2,4),(8,16),(16,64)):
            overlap=o.complex_time_kernel(n,k,0,0)
            with m.workdps(70):
                self.assertLess(abs(abs(overlap)**2-m.mpf(o.unweighted_overlap_square(n,k).numerator)/o.unweighted_overlap_square(n,k).denominator),m.mpf('1e-60'))

    def test_gamma2_not_golden_fixed(self):
        import mpmath as m
        lam=o.golden(m)
        self.assertGreater(abs(lam-(1+lam)**-2),.20)

if __name__=='__main__':unittest.main(verbosity=2)
