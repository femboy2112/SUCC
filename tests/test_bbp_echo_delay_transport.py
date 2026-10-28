"""Exact Green/delay transport, independent algebraic and hostile checks."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ import bbp_echo_delay_transport as t


def independent_four_pole(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def phase(x):
    # Reduce exact rational mod 1 BEFORE conversion: giant BBP states are safe.
    f = float(x % 1)
    return complex(math.cos(2*math.pi*f), math.sin(2*math.pi*f))


class EchoExactTransport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w = t.exact_window(100)

    def test_source_identity_positive_sum_and_quadratic_decay(self):
        self.assertEqual(self.w.forcing[1], Q(47, 15))
        for n in range(1, 101):
            self.assertEqual(self.w.forcing[n], independent_four_pole(n))
            self.assertGreater(self.w.forcing[n], 0)
            if n >= 2:
                self.assertLess(self.w.forcing[n], Q(1, n*n))

    def test_finite_green_identity_all_ages(self):
        for n in range(0, 101):
            scale = (Q(1, 16) if n == 0 else Q(16**(n-1)))
            self.assertEqual(self.w.states[n]+self.w.tails[n], scale*self.w.pi_prefix)
        for n in range(1, 100):
            self.assertLess(self.w.tails[n], t.tail_upper(n))

    def test_filter_exact_future_and_independent_source_division(self):
        filters = [(-16, 1), (-15, 1), (-1, 1), (1, -2, 1),
                   (17, -33, 16), (2, 0, -3, 1), (0, 0, 1), (1,)]
        for coefficients in filters:
            symbol, q = t.division_by_characteristic(coefficients)
            self.assertEqual(symbol, t.filter_symbol(coefficients))
            for n in (1, 2, 7, 19, 71):
                self.assertEqual(t.exact_transport_residual(self.w, n, coefficients),
                                 -t.filtered_tail(self.w, n, coefficients))
                self.assertEqual(t.filtered_state(self.w, n, coefficients),
                                 t.source_only_filter(self.w, n, coefficients))
            for x in (0, 1, 3, 16, -2):
                p = sum(c*x**j for j,c in enumerate(coefficients))
                qx = sum(c*x**j for j,c in enumerate(q))
                self.assertEqual(p, symbol+(x-16)*qx)

    def test_annihilating_and_nonannihilating_mutation(self):
        self.assertEqual(t.filter_symbol((-16, 1)), 0)
        self.assertEqual(t.filter_symbol((-15, 1)), 1)
        for n in range(1, 95):
            self.assertEqual(t.filtered_state(self.w, n, (-16,1)), self.w.forcing[n+1])
            self.assertEqual(t.filtered_state(self.w, n, (-15,1)),
                             self.w.states[n]+self.w.forcing[n+1])

    def test_weighted_multiple_lag_phase_budget(self):
        # Test at finite cutoff; the exact finite tail gives a stronger bound
        # than the universal pi/15 budget. Delays include 24-step echo paths.
        cases = [((-16,1),1), ((-1,0,0,1),2), ((1,0,0,-2,0,1),3),
                 ((2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1),1)]
        for coefficients,h in cases:
            count = 70
            errs = []
            exact_bound = Q(0)
            for n in range(1, count+1):
                observed = t.filtered_state(self.w,n,coefficients)
                ideal = Q(t.filter_symbol(coefficients)*16**(n-1))*self.w.pi_prefix
                errs.append(phase(Q(h)*observed)-phase(Q(h)*ideal))
                exact_bound += sum((abs(c)*self.w.tails[n+j]
                                    for j,c in enumerate(coefficients)),Q(0))
            # Arbitrary deterministic complex unit-weight modulation.
            weights = [cmath.exp(2j*math.pi*(n%7)/7) for n in range(count)]
            signed = sum(w*z for w,z in zip(weights,errs))
            self.assertLessEqual(abs(signed),
                                 2*math.pi*abs(h)*float(exact_bound)+1e-9)
            self.assertLessEqual(float(exact_bound),
                                 sum(map(abs,coefficients))/15)
            self.assertEqual(t.phase_difference_budget_pi_units(h,coefficients),
                             Q(2*abs(h)*sum(map(abs,coefficients)),15))

    def test_hostile_rational_nonnormal_same_leading_decay(self):
        alpha=Q(15,64)
        prev=Q(0)
        for n in range(1,60):
            forcing,tail,state=t.nonnormal_decay_control(n)
            self.assertGreater(forcing,0)
            self.assertEqual(state,16*prev+forcing)
            self.assertEqual(state+tail,16**(n-1)*alpha)
            self.assertLess(tail,Q(1,n*n))
            if n>=3:
                self.assertEqual((state+tail).denominator,1)
                # Sequence approaches an integer orbit rather than Haar.
                self.assertLess(abs(phase(state)-1),2*math.pi*float(tail)+1e-10)
            prev=state
        # Matched leading n^-2 coefficient, NOT matched authentic BBP source.
        self.assertNotEqual(t.nonnormal_decay_control(1)[0],self.w.forcing[1])

    def test_total_future_tail_mass_and_digamma_source_sum(self):
        # Exact finite Fubini: sum T_(n,M)=(sum r(1..M)-pi_M)/15.
        source_sum = sum(self.w.forcing[1:], Q(0))
        self.assertEqual(sum(self.w.tails[1:], Q(0)),
                         (source_sum-self.w.pi_prefix)/15)
        # Independent high-precision formula is established on paper from
        # the digamma identity; a finite prefix can only CHECK its enclosure.
        root2 = math.sqrt(2)
        predicted = (math.pi/4 + 5*root2*math.pi/16 +
                     5*math.log(2)/8 + 5*root2*math.log(1+root2)/8)
        remainder = predicted - float(source_sum)
        self.assertGreater(remainder, 0)
        self.assertLess(remainder, 1/self.w.cutoff)

    def test_invalid_inputs_and_zero_frequency(self):
        for bad in ([], (), [1, 2.0], [True]):
            with self.assertRaises((TypeError,ValueError)):
                t.filter_symbol(bad)
        with self.assertRaises(ValueError):
            t.phase_difference_budget_pi_units(0,(1,))
        with self.assertRaises(ValueError):
            t.filtered_state(self.w,100,(1,1))


if __name__=='__main__':
    unittest.main()
