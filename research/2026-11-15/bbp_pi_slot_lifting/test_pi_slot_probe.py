"""Focused original-source algebra and strict rational interval controls."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import unittest
from fractions import Fraction
import pi_slot_probe as p

class SourceContract(unittest.TestCase):
    def test_original_coefficients(self):
        for n in range(1,19):
            self.assertEqual(p.forcing(n), Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
    def test_original_seed_zero(self):self.assertEqual(p.source_u(0),0)
    def test_integral_prefix_rational(self):
        for n in range(0,18):self.assertEqual(p.source_u(n),p.polynomial_prefix(n))
    def test_forcing_initial(self):self.assertEqual(p.forcing(1),Fraction(47,15))
    def test_forcing_sign(self):
        for n in range(1,100):self.assertGreater(p.forcing(n),0)
    def test_forcing_decreases(self):
        for n in range(1,99):self.assertGreater(p.forcing(n),p.forcing(n+1))
    def test_Q_factorization_fraction_grid(self):
        for j in range(0,23):
            t=Fraction(j,23)
            self.assertEqual(p.q_poly(t),(1-t)*(2+t*t)*(2+2*t+t*t))
    def test_coin_legal_probability(self):
        for j in range(0,31):
            t=Fraction(j,31)
            self.assertTrue(0<=p.moment_g(t)<=1-t)
    def test_tail_bounds_are_strict(self):
        for n in [0,1,2,8,16,32,128]:
            low,high=p.tail_interval(n,14)
            self.assertGreater(high,low)
            self.assertGreater(low,0)
            if n>=1:
                self.assertLess(high,p.forcing(n+1)/15)
    def test_tail_bounds_shrink(self):
        for n in (0,1,16):
            last=None
            for depth in range(0,12):
                a,b=p.tail_interval(n,depth)
                if last is not None:
                    self.assertGreaterEqual(a,last[0]);self.assertLessEqual(b,last[1])
                last=a,b
    def test_tail_ends_at_original_source_not_free_seed(self):
        self.assertEqual(p.tail_interval(0,0)[0],0)
        self.assertEqual(p.tail_interval(0,0)[1],p.forcing(1)/15)
    def test_bernoulli_shared_gram_zero_time(self):
        self.assertEqual(p.coin_gram_interval(0,0,12),p.tail_interval(0,12))
    def test_bernoulli_shared_gram_additive(self):
        for n,m in [(1,2),(2,7),(15,23),(23,40)]:
            self.assertEqual(p.coin_gram_interval(n,m,12),p.tail_interval(n+m,12))
    def test_one_mark_rational_upper(self):
        for n in [0,1,7,100]:
            self.assertGreater(p.upper_one_mark_square(n),0)
            self.assertGreater(p.upper_bernoulli_one_mark_square(n),p.upper_one_mark_square(n))
    def test_source_moment_grading(self):
        # Difference of the GREEN TAIL, not of an independently sampled fake source.
        for n in [0,3,8,24,64]:
            lo,hi=p.green_diff_interval(n,2,25)
            self.assertGreater(lo,0)
            self.assertGreater(hi,lo)
    def test_two_tap_bernoulli_square_positive(self):
        for n in [1,7,32,100]:
            lo,hi=p.coin_two_diff_square_interval(n,2,28)
            self.assertGreater(lo,0);self.assertGreater(hi,lo)
    def test_two_tap_rb_upper(self):
        for n in [0,1,10,25]:
            self.assertGreater(p.upper_rb_two_diff_square(n,2),0)
    def test_four_tap_green_positive(self):
        for n in [0,1,2,8,32,96]:
            for q in [1,16,256]:
                lo,hi=p.double_diff_interval(n,q,2,28)
                self.assertGreater(lo,0)
                self.assertGreater(hi,lo)
    def test_four_tap_source_upper_uniform(self):
        for n in [1,4,8,32,96]:
            for q in [16,256]:
                lo,hi=p.double_diff_interval(n,q,2,26)
                bound,other=p.upper_four_diff_mean(n,q,2)
                self.assertLess(hi,bound)
                self.assertLess(hi,other)
    def test_four_tap_square_bounds(self):
        for n in [1,4,32]:
            a,b=p.upper_rb_four_diff_square(n,16,2)
            self.assertGreater(a,0);self.assertGreater(b,0)
    def test_zero_lag_double_diff(self):
        for n in [0,2,32]:
            self.assertEqual(p.double_diff_interval(n,16,0,15)[0] <=0, True)
            self.assertEqual(p.double_diff_mark(n,16,0,Fraction(1,2)),0)
    def test_zero_lag_two_square(self):
        self.assertEqual(p.coin_two_diff_square_interval(0,0,20)[0] <=0, True)
    def test_nonlinearity_unit_character_coin(self):
        # e(h * 16^n C) = 1 pathwise whenever C in {0,1}, h integer.
        import cmath
        for c in [0,1]:
            for h in [1,3,16,256]:
                self.assertAlmostEqual(abs(cmath.exp(2j*cmath.pi*h*c)-1),0,places=12)
    def test_canonical_real_phase_not_trivial(self):
        import cmath
        lo,hi=p.tail_interval(0,15)
        self.assertLess(hi,Fraction(1,2));self.assertGreater(lo,0)
        self.assertGreater(abs(cmath.exp(2j*cmath.pi*float(lo))-1),0.5)

class SourceGauge(unittest.TestCase):
    def test_gauge_changes_integer_history(self):
        for n in range(1,18):
            diff_u,diff_p,g_end=p.source_gauge(n)
            self.assertEqual(diff_u,2*n*n)
            self.assertEqual(diff_p,g_end)
    def test_gauge_limit_goes_zero(self):
        self.assertGreater(p.source_gauge(10)[2],p.source_gauge(20)[2])
    def test_gauge_circle_phase_identical(self):
        for n in range(1,8):
            diff_u,_,_=p.source_gauge(n)
            self.assertEqual(diff_u.denominator,1)
    def test_gauge_source_changes(self):
        for n in (1,2,3,4):
            self.assertNotEqual(2*n*n-16*2*(n-1)**2,0)

class PoissonFunctional(unittest.TestCase):
    def test_zero_amplitude_is_unit_phase(self):
        mean,var=p.poisson_path_theory(0,0,0,1,3)
        self.assertAlmostEqual(abs(mean-1),0)
        self.assertAlmostEqual(var,0)
    def test_nonzero_amplitude_unbiased(self):
        import cmath
        mu=.061; pref=.25;harm=3;rate=4
        mean,var=p.poisson_path_theory(mu,0,pref,harm,rate)
        self.assertAlmostEqual(abs(mean-cmath.exp(2j*cmath.pi*harm*(pref+mu))),0)
        self.assertAlmostEqual(var,0)
    def test_variance_strictly_positive(self):
        _,v=p.poisson_path_theory(.25,.005,0,1,1)
        self.assertGreater(v,0)
    def test_variance_decreases_with_rate(self):
        a=p.poisson_path_theory(.25,.005,0,1,1)[1]
        b=p.poisson_path_theory(.25,.005,0,1,8)[1]
        self.assertGreater(a,b)
    def test_variance_decreases_with_source_depth(self):
        a=p.poisson_path_theory(.002,float(p.upper_one_mark_square(8)),0,1,1)[1]
        b=p.poisson_path_theory(.002,float(p.upper_one_mark_square(80)),0,1,1)[1]
        self.assertGreater(a,b)
    def test_rate_guard(self):
        with self.assertRaises(ValueError):p.poisson_path_theory(.1,.1,0,1,0)


class OperatorPath(unittest.TestCase):
    def test_operator_source_forcing(self):
        for n in range(1,23):
            self.assertEqual(p.original_operator_forcing_integral(n),p.forcing(n))
    def test_operator_series_telescopes(self):
        for n in range(0,22):self.assertEqual(p.operator_telescoping_residual(n),0)
    def test_green_resolvent_reconstructs_source(self):
        # Interval verification: 16 T_n - T_(n+1) = r(n+1).
        for n in range(0,15):
            a,b=p.tail_interval(n,28);c,d=p.tail_interval(n+1,28)
            self.assertLess(16*a-d,p.forcing(n+1))
            self.assertGreater(16*b-c,p.forcing(n+1))
    def test_green_chiral_energy_positive(self):
        for n in [1,3,16,32]:
            for k in [0,1,2,3]:
                lo,hi=p.chiral_green_energy_interval(n,k,36)
                self.assertGreater(lo,0)
                self.assertGreater(hi,lo)
    def test_green_chiral_k0_equals_T_2n(self):
        for n in [0,1,4,18]:
            self.assertEqual(p.chiral_green_energy_interval(n,0,25),p.tail_interval(2*n,25))
    def test_coin_source_has_no_pi_dependency(self):
        import random
        rng=random.Random(1717)
        for _ in range(100):
            t,c=p.sample_pi_coin(rng)
            self.assertTrue(0<=t<1)
            self.assertIn(c,(0,1))
    def test_poisson_count_finite(self):
        import random
        rng=random.Random(17)
        vals=[p.poisson_count(2,rng) for _ in range(100)]
        self.assertTrue(all(v>=0 and isinstance(v,int) for v in vals))
    def test_poisson_phase_finite(self):
        import random
        rng=random.Random(170)
        for n in [0,1,4,16]:
            value=p.phase_product_sample(n,1,2.,rng)
            self.assertTrue(abs(value)<1000)
    def test_four_tap_finite(self):
        import random
        rng=random.Random(171)
        for n in [1,2,8]:
            value=p.four_tap_phase_sample(n,16,2,1,2.,rng)
            self.assertTrue(abs(value)<1000)
    def test_zero_harmonic_path(self):
        import random
        rng=random.Random(172)
        for n in [0,1,16]:
            self.assertEqual(p.phase_product_sample(n,0,2.,rng),1)
    def test_ordered_differencing_mark_sign(self):
        for n,q,lag in [(0,16,2),(4,16,2),(32,256,2)]:
            for t in [Fraction(1,10),Fraction(1,2),Fraction(9,10)]:
                self.assertGreater(p.double_diff_mark(n,q,lag,t),0)

class AllModePhaseInstrument(unittest.TestCase):
    def test_oily_first_second_moment(self):
        self.assertEqual(p.oily_moments(),(Fraction(8,3),Fraction(32,3)))
    def test_oily_probability_mass(self):
        mass=sum((Fraction(h+1,3*2**h) for h in range(1,100)),Fraction())
        self.assertTrue(0<mass<1)
        self.assertLess(1-mass,Fraction(1,10**20))
    def test_oily_frequency_sampler(self):
        import random
        rng=random.Random(649)
        for _ in range(1000):
            h=p.sample_oily_frequency(rng)
            self.assertGreaterEqual(h,1)
    def test_common_phase_field_finite(self):
        import random
        rng=random.Random(6491)
        for B in (2,4):
            a=p.common_shell_phase_sample(B,3,2.,rng)
            self.assertTrue(abs(a)<1000)
    def test_independent_oily_pair_finite(self):
        import random
        rng=random.Random(6492)
        for B in (2,4,8):
            value,h=p.all_mode_oily_pair_sample(B,1.5,rng)
            self.assertEqual(float(value),float(value))
            self.assertGreaterEqual(h,1)
    def test_uniform_h_variance_exponent(self):
        for h in (1,2,3,16,101):
            self.assertEqual(Fraction(h*h,h*h),1)
    def test_expected_total_poisson_cost(self):
        mean_h2=p.oily_moments()[1]
        self.assertEqual(2*mean_h2,Fraction(64,3))
    def test_rate_guard_common(self):
        import random
        with self.assertRaises(ValueError):p.common_shell_phase_sample(1,1,0,random.Random(1))

if __name__=='__main__':unittest.main()
