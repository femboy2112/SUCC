"""Source/gauge/rank controls; does not test an infinite normality assertion."""
from fractions import Fraction as Q
import unittest
from observational_succ.seed_source_rank import (
    AffineSeed,G_PI,forcing,partial,state,h_moment,change_source_gauge,
    source_gauge_check,rational_shadow_seed,shadow_state,shadow_upper,
    shell_lock_bound
)

class SeedSourceRankTests(unittest.TestCase):
    def test_four_poles_exact_source(self):
        for n in range(1,34):
            expected=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            self.assertEqual(forcing(n),expected)
        self.assertEqual(forcing(1),Q(47,15))

    def test_strict_rational_prefix_increase(self):
        self.assertEqual(partial(0),0)
        for n in range(1,45):
            self.assertGreater(forcing(n),0)
            self.assertGreater(partial(n),partial(n-1))
            self.assertLess(forcing(n+1),forcing(n))

    def test_seed_recurrence_is_source_typed(self):
        for seed in (Q(0),Q(1,16),Q(-3,5),Q(17,97)):
            for n in range(1,12):
                self.assertEqual(state(n,seed),16*state(n-1,seed)+forcing(n))
                self.assertEqual(Q(state(n,seed),16**n)-partial(n),seed)

    def test_symbolic_counterseed_is_nonrational_finite_state(self):
        wrong=AffineSeed(Q(0),Q(-1))
        self.assertEqual(wrong.completed_coefficients,(Q(0),Q(0)))
        self.assertEqual(wrong.normality_class,"RATIONAL_NONNORMAL")
        for n in range(9):
            coeff=wrong.raw_state_coefficients(n)
            self.assertEqual(coeff[1],-16**n)
            # Assumes x irrational, so nonzero coefficient means irrational.
            self.assertNotEqual(coeff[1],0)

    def test_rational_seeds_never_on_rank_collapse(self):
        for a in (Q(0),Q(-1,16),Q(1,5),Q(100,19)):
            x=AffineSeed(a,Q(0))
            self.assertEqual(x.completed_coefficients,(a,Q(1)))
            self.assertEqual(x.normality_class,"EQUIVALENT_TO_PI_BASE16_NORMALITY")

    def test_full_rank_locus_exact(self):
        for a in (Q(-2,3),Q(0),Q(5,7)):
            for b in (Q(-3),Q(-1),Q(-1,2),Q(0),Q(1,3),Q(2)):
                x=AffineSeed(a,b)
                self.assertEqual(x.normality_class=="RATIONAL_NONNORMAL",b==-1)
                self.assertEqual(x.completed_coefficients[1],1+b)

    def test_rational_alias_of_completed_circle(self):
        seed=Q(1,16)
        for n in range(1,11):
            self.assertEqual(16**n*seed%1,0)
        self.assertNotEqual(state(0,seed),state(0,Q(0)))

    def test_rational_source_gauge_shift_full_equivalence(self):
        for h in ((Q(1,2),), (Q(0),Q(1),Q(-3,4)),(Q(7,9),Q(-1,3))):
            self.assertTrue(source_gauge_check(G_PI,Q(0),h,20))
            g2,s2=change_source_gauge(G_PI,Q(0),h)
            self.assertEqual(s2,h_moment(0,h))
            self.assertNotEqual(g2,G_PI)
            self.assertNotEqual(s2,Q(0))

    def test_fixed_forcing_seed_shift_not_same_gauge(self):
        h=(Q(3,4),)
        g2,s2=change_source_gauge(G_PI,Q(0),h)
        self.assertEqual(s2,Q(3,4))
        for n in range(0,7):
            self.assertEqual(state(n,s2,g2)-state(n,Q(0),G_PI),h_moment(n,h))
            # At n=0 both values equal the seed shift; after one step
            # fixed forcing grows it by 16 instead of a_h(n).
            if n>=1:
                self.assertNotEqual(state(n,s2,G_PI)-state(n,Q(0),G_PI),h_moment(n,h))

    def test_future_shadow_has_exact_zero_at_horizon(self):
        for N in (4,8,16,32,48):
            self.assertEqual(shadow_state(N,N),0)
            for n in range(N):
                got=shadow_state(N,n)
                direct=-sum((Q(forcing(j),16**(j-n)) for j in range(n+1,N+1)),Q(0))
                self.assertEqual(got,direct)
                self.assertLess(got,0)
                self.assertGreater(got,-shadow_upper(n))

    def test_shell_anti_lock_rational_moving_seed(self):
        for B in (3,6,12,24,48):
            N=2*B
            self.assertLess(shell_lock_bound(B),Q(1))
            self.assertTrue(all(-shadow_upper(B)<shadow_state(N,n)<=0
                                for n in range(B,2*B)))
            if B>=6:
                self.assertLess(shell_lock_bound(B),shell_lock_bound(B//2))

    def test_nonzero_shadow_seed_not_authenticated_origin(self):
        for N in (1,2,8,20):
            seed=rational_shadow_seed(N)
            self.assertLess(seed,0)
            self.assertNotEqual(seed,Q(0))
            self.assertEqual(state(0,seed),seed)

    def test_input_types_fail_closed(self):
        with self.assertRaises(TypeError):AffineSeed(.5,Q(0))
        with self.assertRaises(TypeError):forcing(2,(.5,))
        with self.assertRaises(ValueError):forcing(0)
        with self.assertRaises(ValueError):shadow_state(4,5)
        with self.assertRaises(ValueError):shell_lock_bound(0)
        with self.assertRaises(TypeError):state(4,seed=.1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
