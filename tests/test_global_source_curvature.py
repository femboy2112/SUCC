"""Exact holdouts and falsifiers for paid moving-frequency source bounds."""
from fractions import Fraction as Q
import unittest

from observational_succ import global_source_curvature as c
from observational_succ.pi_succ_character_intervals import fourier_squared_interval


def independent_r(n):
    # Regrouped odd-denominator formula, independent of the production adapter.
    return Q(4, 8*n-7)-Q(1, 4*n-2)-Q(1, 8*n-3)-Q(1, 2*(4*n-1))


class SourceCurvatureTests(unittest.TestCase):
    def test_source_and_both_derivative_margins(self):
        for n in (1, 2, 3, 17, 31, 129, 997, 10007):
            r = independent_r(n+1)
            d = r-independent_r(n+2)
            self.assertEqual(c.source_derivative(n), d)
            self.assertTrue(0 < Q(15,64)-n*n*r < Q(7,5*n))
            self.assertTrue(0 < Q(15,32)-n**3*d < Q(3,n))
            self.assertGreater(d, c.source_derivative(n+1))

    def test_cubic_boundaries_and_independent_holdouts(self):
        for m in (16, 17, 33, 64, 79, 257):
            for h in (m**3, -(16*m**3//15)):
                out = c.cubic_source_certificate(m, h)
                self.assertLess(out['increment_max'], Q(1,2))
                self.assertGreater(out['increment_min'], Q(1,32))
                self.assertEqual(out['selected_sum_upper'],
                                 m-Q(max(0,m-33),289))

    def test_quadratic_disjoint_pairs_and_rounding(self):
        for m in (128, 129, 130, 131, 257):
            for h in (m*m, -2*m*m):
                out = c.quadratic_source_certificate(m, h)
                self.assertEqual(out['pairs'], m//4)
                self.assertGreater(out['gap_min'], Q(1,16))
                self.assertLess(out['gap_max'], Q(1,2))

    def test_native_zero_source_and_wrong_seed_rejection(self):
        for m in (7, 19, 37):
            state = Q()
            all_states = []
            for n in range(1, 2*m+1):
                state = 16*state+independent_r(n)
                all_states.append(state)
            actual = tuple(all_states[m:])
            self.assertEqual(c.source_window(m), actual)
            c.authenticate_window(actual, m)
            # Retains every interior recurrence; fails the zero selector.
            mutant = tuple(x+Q(16**n,3) for n,x in
                           enumerate(actual, start=m+1))
            with self.assertRaises(ValueError): c.authenticate_window(mutant,m)
            wrong_pole = tuple(x+1 for x in actual)
            with self.assertRaises(ValueError): c.authenticate_window(wrong_pole,m)

    def test_finite_signed_interval_holdouts(self):
        for m,h,bound in ((41,41**3,c.cubic_band_bound),
                          (67,-(16*67**3//15),c.cubic_band_bound),
                          (129,2*129**2,c.quadratic_band_bound)):
            phases = c.source_window(m)
            _, upper = fourier_squared_interval(phases,h)
            self.assertLessEqual(upper, (bound(m,h)/m)**2)

    def test_real_core_endpoints_and_false_constant(self):
        u = tuple(Q(i%7,11) for i in range(41))
        w = tuple(u[i+1]+16*u[i] for i in range(40))
        left,boundary,full = c.energy_transport(u,w)
        self.assertLessEqual(left,boundary)
        self.assertEqual(full-boundary,17*u[0]**2+272*u[-1]**2)
        # Uniform u makes weighted Cauchy exact; constant 288 fails for T>288.
        u = (Q(1),)*290
        w = (Q(17),)*289
        left,boundary,full = c.energy_transport(u,w)
        self.assertEqual(left,boundary)
        self.assertGreater(left,288*sum(x*x for x in u))
        with self.assertRaises(ValueError):c.energy_transport((Q(0),Q(0)),(Q(1),))

    def test_changed_green_highband_does_not_establish_fixed_mode(self):
        out = c.changed_green_control(1024,1024**3)
        self.assertEqual(out['moving_sum_upper'],512)
        self.assertEqual(out['fixed_nonzero_frequency_limit'],1)
        self.assertFalse(out['zero_selector'])
        self.assertTrue(out['same_four_poles'])

    def test_domain_and_frequency_mutations_fail(self):
        for bad in (True,16.0,Q(16),0,-1):
            with self.assertRaises(ValueError): c.cubic_band_bound(bad,4096)
        for h in (0,4095,16*16**3//15+1,True):
            with self.assertRaises(ValueError): c.cubic_band_bound(16,h)
        with self.assertRaises(ValueError): c.quadratic_band_bound(127,127**2)
        with self.assertRaises(ValueError): c.quadratic_band_bound(128,128**2-1)
        with self.assertRaises(ValueError): c.source_window(2001)


if __name__ == '__main__':
    unittest.main()
