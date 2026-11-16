"""Exact-source and finite-probe validation; no normality proof."""
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.pi_resonant_interferometer import (
    forcing, forcing_leading_bounds, state, source_innovation,
    innovation_leading, critical_lag, same_mode_lag_phase, compensated_phase,
    pi_interval, click_phase_interval, click_interval, shell_click_interval,
    inverse_propensity_expectation, collision_phase_table,
    source_click_probability_rational_control, gamma_depth_two_one_sided_factor,
)

class ExactSource(unittest.TestCase):
    def test_original_first_pole(self):
        self.assertEqual(forcing(1),F(47,15))
    def test_invalid_source_time(self):
        with self.assertRaises(ValueError):forcing(0)
    def test_unique_pointed_origin(self):
        self.assertEqual(state(0),0)
    def test_recurrence(self):
        for n in range(20):self.assertEqual(state(n+1),16*state(n)+forcing(n+1))
    def test_rational_forcing_rewrite(self):
        for n in range(1,41):
            self.assertEqual(forcing(n),F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
    def test_strict_leading_difference(self):
        for n in range(2,91):
            actual,lead,err=forcing_leading_bounds(n)
            self.assertEqual(err,actual-lead)
            self.assertGreater(err,0)
            self.assertLess(err,F(1,n**3))
    def test_innovation_recurrence(self):
        for n in range(2,12):
            for ell in range(1,9):
                self.assertEqual(state(n+ell)-16**ell*state(n),source_innovation(n,ell))
    def test_resonant_error(self):
        for n in range(2,31):
            for ell in range(1,10):
                actual,lead,cap=innovation_leading(n,ell)
                self.assertLessEqual(abs(actual-lead),cap)
    def test_critical_band(self):
        for n in (2,3,4,5,10,11,25,100,1000,100000):
            ell=critical_lag(n)
            x=F(16**ell,64*n*n)
            self.assertLessEqual(F(1,4),x)
            self.assertLessEqual(x,F(4))
    def test_seed_blind_compensated(self):
        for n in range(2,7):
            for ell in (1,2,4):
                self.assertEqual(compensated_phase(n,ell,3,F(0)),compensated_phase(n,ell,3,F(1,17)))
    def test_uncompensated_retains_seed(self):
        n,ell,h=4,2,1
        x=same_mode_lag_phase(n,ell,h,F(0))
        y=same_mode_lag_phase(n,ell,h,F(1,19))
        self.assertNotEqual(x,y)
        self.assertEqual((y-x)%1,(h*(16**ell-1)*16**n*F(1,19))%1)
    def test_lag_has_rational_alias_despite_history(self):
        n,ell=4,2
        self.assertEqual(same_mode_lag_phase(n,ell,1,F(0)),
                         same_mode_lag_phase(n,ell,1,F(1,17)))

    def test_direct_lag(self):
        for n in (0,2,4):
            self.assertEqual(same_mode_lag_phase(n,3,1),(state(n+3)-state(n))%1)

class FiniteClicks(unittest.TestCase):
    def test_pi_enclosure_positive(self):
        for depth in (3,5,8,12):
            lo,hi=pi_interval(depth)
            self.assertLess(lo,F(22,7));self.assertGreater(hi,F(3));self.assertLess(lo,hi)
    def test_coherent_zero_no_click(self):
        self.assertEqual(click_phase_interval(F(0)),(F(0),F(0)))
        self.assertEqual(click_phase_interval(F(1)),(F(0),F(0)))
    def test_symmetry(self):
        for v in (F(1,15),F(17,32),F(3,7)):
            self.assertEqual(click_phase_interval(v),click_phase_interval(-v))
    def test_finite_source_clicks_valid(self):
        for n in range(1,15):
            lo,hi=click_interval(n,1,completed=False)
            self.assertLessEqual(F(0),lo);self.assertLessEqual(lo,hi);self.assertLessEqual(hi,F(1))
    def test_completed_contains_uncompleted(self):
        for n in range(1,12):
            lo,hi=click_interval(n,1,completed=False)
            a,b=click_interval(n,1,completed=True)
            self.assertLessEqual(a,lo);self.assertGreaterEqual(b,hi)
    def test_shell_interval(self):
        a,b=shell_click_interval(4,1,completed=True)
        self.assertGreater(a,0);self.assertLess(b,1)
    def test_rational_periodic_clicks_false_normality(self):
        lo,hi=source_click_probability_rational_control(F(1,15))
        self.assertGreater(lo,0)
        self.assertLess(hi,F(1))
        self.assertTrue(all((16**n*F(1,15))%1==F(1,15) for n in range(1,15)))
    def test_bad_harmonic(self):
        with self.assertRaises(ValueError):click_interval(3,h=0)
    def test_actual_pi_value_inside(self):
        import mpmath as mp
        with mp.workdps(80):
            for n in range(1,12):
                lo,hi=click_interval(n,h=1,completed=True)
                actual=mp.sin(mp.pi*(16**n*mp.pi/16))**2
                a=mp.mpf(lo.numerator)/lo.denominator
                b=mp.mpf(hi.numerator)/hi.denominator
                self.assertLessEqual(a,actual)
                self.assertLessEqual(actual,b)
    def test_rational_U_click_value_inside(self):
        import mpmath as mp
        with mp.workdps(80):
            for n in range(1,12):
                lo,hi=click_interval(n,h=1,completed=False)
                q=state(n)%1
                actual=mp.sin(mp.pi*mp.mpf(q.numerator)/q.denominator)**2
                self.assertLessEqual(mp.mpf(lo.numerator)/lo.denominator,actual)
                self.assertLessEqual(actual,mp.mpf(hi.numerator)/hi.denominator)

class UnbiasedProbeChoice(unittest.TestCase):
    def test_horvitz_thompson(self):
        p=(F(3,4),F(1,4))
        q=(F(3,4),F(1,4))
        self.assertEqual(inverse_propensity_expectation(p,q),F(1,2))
        self.assertNotEqual(sum((x*y for x,y in zip(p,q)),F(0)),F(1,2))
    def test_pathological_policy_rejected(self):
        with self.assertRaises(ValueError):inverse_propensity_expectation((F(1),F(0)),(F(1),F(0)))
    def test_non_normal_periodic_has_perfect_pair_energy(self):
        periods=tuple((16**n*F(1,15))%1 for n in range(10))
        table=collision_phase_table(periods)
        self.assertTrue(all(x==0 for row in table for x in row))
    def test_pair_symmetry(self):
        p=tuple(state(n)%1 for n in range(2,9))
        tab=collision_phase_table(p)
        self.assertTrue(all(tab[i][j]==(-tab[j][i])%1 for i in range(len(tab)) for j in range(len(tab))))
    def test_exact_pair_energy_as_complex(self):
        import mpmath as mp
        p=tuple(state(n)%1 for n in range(2,9))
        table=collision_phase_table(p)
        with mp.workdps(60):
            def ch(q):return mp.exp(2j*mp.pi*mp.mpf(q.numerator)/q.denominator)
            direct=abs(sum((ch(x) for x in p)))**2/len(p)**2
            pair=sum((ch(d) for row in table for d in row))/len(p)**2
            self.assertLess(abs(direct-pair),mp.mpf('1e-55'))
            self.assertLess(abs(mp.im(pair)),mp.mpf('1e-55'))
    def test_gamma_dephasing_coherent_false_click(self):
        # one-sided Gamma(2,1) phase factor at omega=1: 0 - i/2.
        re,im=gamma_depth_two_one_sided_factor()
        self.assertEqual((re,im),(F(0),-F(1,2)))
        self.assertEqual((1-re)/2,F(1,2)) # spurious baseline click from phi=0
        self.assertEqual(click_phase_interval(F(0)),(0,0))

if __name__=='__main__':unittest.main()
