import unittest
from fractions import Fraction as Q

from observational_succ.oily_signed_certificate import (
    Interval, authentic_signed_certificate, character_enclosure,
    machin_pi_enclosure, signed_sum_enclosure, squared_modulus_enclosure)
from observational_succ.bbp_resonance_controls import exact_forced_history


class SignedCertificateTests(unittest.TestCase):
    def test_pi_machin_rational_calibration(self):
        bounds = machin_pi_enclosure()
        self.assertGreater(bounds.lower, Q(3141592653589793238462643383279,10**30))
        self.assertLess(bounds.upper, Q(3141592653589793238462643383280,10**30))
        self.assertLess(bounds.upper-bounds.lower, Q(1,10**40))
        self.assertEqual((Q(120,119)-Q(1,239))/(1+Q(120,119)*Q(1,239)), 1)

    def test_quarter_circle_and_periodicity(self):
        for q, pair in [(Q(0),(1,0)),(Q(1,4),(0,1)),(Q(1,2),(-1,0)),(Q(3,4),(0,-1))]:
            r,i = character_enclosure(q)
            self.assertEqual((r.lower,r.upper),(pair[0],pair[0]))
            self.assertEqual((i.lower,i.upper),(pair[1],pair[1]))
            self.assertEqual(character_enclosure(q+137), (r,i))

    def test_exact_algebraic_character(self):
        r,i = character_enclosure(Q(1,3))
        self.assertTrue(r.contains(Q(-1,2)))
        self.assertLessEqual(i.lower**2,Q(3,4))
        self.assertGreaterEqual(i.upper**2,Q(3,4))

    def test_complete_grid_null_and_coherent_positive_controls(self):
        grid = signed_sum_enclosure(tuple(Q(j,17) for j in range(17)))
        self.assertTrue(grid[0].contains(0))
        self.assertTrue(grid[1].contains(0))
        self.assertLess(squared_modulus_enclosure(grid).upper,Q(1,10**20))
        constant = signed_sum_enclosure((Q(0),)*17)
        self.assertEqual(squared_modulus_enclosure(constant),Interval(289,289))

    def test_source_adapter_independent_unwrapped_recurrence(self):
        # Different existing adapter: unwrapped states vs local literal carries.
        h = exact_forced_history(37)
        report = authentic_signed_certificate(37,3,7)
        manual = signed_sum_enclosure(h[1:],3)
        self.assertEqual((report['real'],report['imag']),manual)
        self.assertEqual(report['squared_modulus'],squared_modulus_enclosure(manual))
        self.assertFalse(report['infinite_cancellation_proved'])

    def test_signed_cross_block_is_not_diagonal_energy(self):
        # Two one-point blocks at opposite phases: full energy 0, cross -2.
        a = signed_sum_enclosure((Q(0),Q(1,2)))
        full = squared_modulus_enclosure(a)
        cross = full-Interval(2,2)
        self.assertEqual(full,Interval(0,0))
        self.assertEqual(cross,Interval(-2,-2))
        # Deliberately dropping cross terms is rejected by this exact witness.
        self.assertNotEqual(full,Interval(2,2))

    def test_hostile_endpoint_and_precision_holdouts(self):
        import mpmath as mp
        with mp.workdps(90):
            for q in (Q(-999,2000),Q(1,997),Q(412,997),Q(473,1009)):
                r,i=character_enclosure(q)
                phase=mp.mpf(q.numerator)/q.denominator
                value=mp.exp(2j*mp.pi*phase)
                for bounds, scalar in ((r,mp.re(value)),(i,mp.im(value))):
                    lo=mp.mpf(bounds.lower.numerator)/bounds.lower.denominator
                    hi=mp.mpf(bounds.upper.numerator)/bounds.upper.denominator
                    self.assertLessEqual(lo,scalar)
                    self.assertGreaterEqual(hi,scalar)

    def test_invalid_inputs_and_mutation(self):
        character_enclosure(Q(1,4))
        with self.assertRaises(ValueError): character_enclosure(0.25)
        machin_pi_enclosure(1)
        with self.assertRaises(ValueError): machin_pi_enclosure(True)
        with self.assertRaises(ValueError): character_enclosure(0.1)
        with self.assertRaises(ValueError): authentic_signed_certificate(8,0)
        with self.assertRaises(ValueError): Interval(1,0)
        with self.assertRaises(ValueError): character_enclosure(Q(1,3),bits=2)
        r,_=character_enclosure(Q(1,3))
        mutant=Interval(r.lower+1,r.upper+1)
        self.assertFalse(mutant.contains(Q(-1,2)))


if __name__ == '__main__':
    unittest.main()
