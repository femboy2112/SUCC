import unittest
import sympy as sp
from fractions import Fraction as F
from gamma_all_places import (
    DELTAS,AUTH,FAKE,AGE_KERNEL,RANK2_2ADIC_FAKE_PLUS,RANK2_2ADIC_FAKE_MINUS,
    source,orbit,local_ratio,local_regular,local_polar,two_adic_defect,
    two_integrality_condition,v_p_fraction,ages,coeff_deform,tail,
    partial_total_tail,total_source_partial,total_pi_partial,sum_tail_rhs_partial,
    time_weighted_gamma
)

class AllPlaceTests(unittest.TestCase):
    def test_real_gamma_logarithmic_derivative_original(self):
        t=sp.symbols('t')
        H=sp.prod((8*t+d)**c for d,c in zip(DELTAS,AUTH))
        R=sp.Add(*[sp.Rational(c)/(8*t+d) for d,c in zip(DELTAS,AUTH)])
        self.assertEqual(sp.cancel(sp.diff(H,t)/(8*H)-R),0)
    def test_all_prime_local_ratio_recurrence(self):
        # This is the algebraic one-step Morita quotient, not numerical Gamma_p.
        for p in (2,3,5,7,11,13,17,23,29):
            for n in range(1,35):
                t=n-1
                oracle=sp.Rational(1)
                for d,c in zip(DELTAS,AUTH):
                    z=8*t+d
                    oracle *= sp.Integer(-z if z%p else -1)**c
                self.assertEqual(F(oracle),local_ratio(n,p))
                self.assertEqual(local_regular(n,p)+local_polar(n,p),source(n))
    def test_polar_support_exact_exceptional_primes(self):
        for p in (7,11,13,17,19,23,29,31,37,41):
            for n in range(1,1+5*p):
                self.assertLessEqual(sum(((8*(n-1)+d)%p==0) for d in DELTAS),1)
    def test_2_polar_defect_closed_formula(self):
        for n in range(1,110):
            self.assertEqual(local_polar(n,2),two_adic_defect(n))
            self.assertEqual(two_adic_defect(n),-F(3*n-1,(2*n-1)*(4*n-1)))
            self.assertGreaterEqual(v_p_fraction(source(n),2),0)
            self.assertEqual(source(n).numerator%2, n%2)
    def test_integrality_condition_exact_integer_vectors(self):
        for A in (-2,-1,0,2):
            for B in (-5,-3,-2,-1,0,1,2,3,4):
                for C in (-1,1):
                    for D in (-3,-2,-1,0,1,2,3):
                        co=(A,B,C,D)
                        verdict=two_integrality_condition(co)
                        self.assertEqual(all(v_p_fraction(source(n,co),2)>=0 or source(n,co)==0 for n in range(1,11)),verdict)
    def test_ages_and_2adic_filter_does_not_identify_source(self):
        for t in (-4,0,4,8):
            c=coeff_deform(t)
            self.assertEqual(ages(c),ages(AUTH))
            self.assertTrue(two_integrality_condition(c))
        self.assertEqual(ages(AUTH),ages(FAKE))
        self.assertFalse(two_integrality_condition(FAKE))
        self.assertNotEqual(source(2,RANK2_2ADIC_FAKE_PLUS),source(2,AUTH))
    def test_positive_matched_mutant_factorization(self):
        q=sp.symbols('q')
        K=1-3*q**3+q**4+q**5
        self.assertEqual(sp.factor(K),(q-1)**2*(q**3+3*q**2+2*q+1))
        Q=4-2*q**3-q**4-q**5
        for t in (0,4):
            self.assertTrue(all(float((Q+t*K).subs(q,sp.Rational(i,40)))>0 for i in range(0,40)))
        # exact nonnegative for all 0<=q<=1, as K>=0 and original Q>0 there.
        self.assertEqual(sp.diff(K,q).subs(q,1),0)
        self.assertEqual(sp.diff(K,q,2).subs(q,1),14)
    def test_even_prime_distinguishes_age_twin_but_not_all(self):
        self.assertEqual(v_p_fraction(source(1,FAKE),2),-2)
        for n in range(1,80):
            self.assertGreaterEqual(v_p_fraction(source(n,RANK2_2ADIC_FAKE_PLUS),2),0)
    def test_first_birth_13_rejects_2adically_integral_twin(self):
        for c in (AUTH,RANK2_2ADIC_FAKE_PLUS):
            u=orbit(2,c)
            self.assertEqual(v_p_fraction(u,13),-1)
        self.assertNotEqual((13*orbit(2,AUTH)).numerator*pow((13*orbit(2,AUTH)).denominator,-1,13)%13,
                            (13*orbit(2,RANK2_2ADIC_FAKE_PLUS)).numerator*pow((13*orbit(2,RANK2_2ADIC_FAKE_PLUS)).denominator,-1,13)%13)
    def test_finite_green_double_sum_identity(self):
        for N in (2,3,6,14,20):
            lhs=sum((source(n+j)*F(1,16**j) for n in range(1,N) for j in range(1,N-n+1)),F())
            self.assertEqual(lhs,sum_tail_rhs_partial(N))
    def test_direct_positive_tail(self):
        for n in range(1,25):
            t=tail(n,16)
            self.assertGreater(t,0)
            self.assertLess(t,F(1,(8*n+1)**2))
    def test_analytic_source_gamma_convergence(self):
        d=(1,4,5,6)
        digamma=-sum(F(c,8)*sp.digamma(sp.Rational(x,8)) for x,c in zip(d,AUTH))
        value=float(sp.N(digamma,40))
        for N in (100,500,1000):
            s=float(total_source_partial(N))
            self.assertGreater(value,s)
            self.assertLess(value-s,1/N)
    def test_pi_and_total_tail_holonomy(self):
        import mpmath as mp
        mp.mp.dps=70
        sg=-sum(mp.mpf(c)/8*mp.digamma(mp.mpf(d)/8) for d,c in zip(DELTAS,AUTH))
        B=(sg-mp.pi)/15
        self.assertTrue(mp.mpf('0.016')< B <mp.mpf('0.017'))
        S=partial_total_tail(70,140)
        sv=mp.mpf(S.numerator)/S.denominator
        self.assertGreater(B,sv)
        self.assertLess(B-sv,1/mp.mpf(8*(8*70+1)))
        # The phase-holonomy budget is 2pi times the exact positive sum.
        self.assertLess(2*mp.pi*B, mp.mpf('0.103'))
    def test_complex_selected_phase_bound_finite(self):
        import mpmath as mp
        mp.mp.dps=85
        sg=-sum(mp.mpf(c)/8*mp.digamma(mp.mpf(d)/8) for d,c in zip(DELTAS,AUTH))
        cost=2*mp.pi*(sg-mp.pi)/15
        for h in (1,3,7):
            diff=mp.mpc(0)
            for n in range(1,41):
                u=orbit(n)
                um=mp.mpf(u.numerator)/u.denominator
                diff += mp.exp(2j*mp.pi*h*um) - mp.exp(2j*mp.pi*h*16**(n-1)*mp.pi)
            self.assertLess(abs(diff),h*cost)
    def test_coherent_seed_same_gamma_data(self):
        for n in (1,2,4,10):
            self.assertEqual(orbit(n,AUTH,F(1,16))-orbit(n),16**(n-1))
            self.assertEqual(local_ratio(n,2),local_ratio(n,2,AUTH))

if __name__=='__main__':unittest.main(verbosity=2)

class AllHorizon2AdicControls(unittest.TestCase):
    def test_age_kernel_has_exact_valuation_minus_two_all_times(self):
        for n in range(1,401):
            self.assertEqual(v_p_fraction(source(n,AGE_KERNEL),2),-2)

    def test_arbitrary_fixed_precision_all_horizon_mutants(self):
        # Every n is included in the analytic proof; finite sample is just a mutation test.
        for k in (1,2,4,8,12,16):
            t=2**(k+2)
            c=coeff_deform(t)
            self.assertEqual(ages(c),ages(AUTH))
            self.assertTrue(two_integrality_condition(c))
            for n in range(1,31):
                self.assertEqual(v_p_fraction(source(n,c)-source(n),2),k)
                self.assertEqual(v_p_fraction(orbit(n,c)-orbit(n),2),k)
            # odd-prime snapshot DOES discriminate the entire tower.
            assert (13*orbit(2,c)).denominator % 13
            assert (13*orbit(2)).denominator % 13
            def mod13(x):return x.numerator*pow(x.denominator,-1,13)%13
            self.assertNotEqual(mod13(13*orbit(2,c)),mod13(13*orbit(2)))

    def test_even_snapshots_cannot_be_source_selection(self):
        # Fixed finite 2-adic resolutions see identical source/orbit for all times,
        # but the exact 2-adic source and its real BBP constant are distinct.
        self.assertNotEqual(source(3,coeff_deform(64)),source(3))
        self.assertEqual(v_p_fraction(source(3,coeff_deform(64))-source(3),2),4)

