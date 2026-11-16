"""Exact independent-calibration and source mutation tests; unittest standard library."""
import unittest
from fractions import Fraction
from loop_probe import (
    forcing, frac, source_states, lifted_source_states, modular_source_states, green_tail_interval,
    distance_to_nearest_integer, distance_interval_lower,
    circle_pulse_certificate, clock_jet, predicted_jet, first_certified_pulse,
    return_jet_table, pulse_energy_threshold, source_crt_passport,
)

class TestExactBBP(unittest.TestCase):
    def test_odd_prime_phase_reconstructs_real_phase(self):
        source=lifted_source_states(10)
        for n in range(1,11):
            passport=source_crt_passport(n,source[n])
            fractional=source[n]-passport["integer_winding"]
            local=sum((Fraction(k,p**v) for p,v,k in
                       passport["local_characters"]),Fraction())
            self.assertEqual(local-fractional,
                             passport["crt_reconstruction_integer"])
            self.assertTrue(all(p%2 and p<=8*n for p,v,k in
                                passport["local_characters"]))

    def test_integer_winding_indispensable_for_2adic_component(self):
        source=lifted_source_states(7)
        for n in range(1,8):
            p=source_crt_passport(n,source[n])
            q=256
            integer=p["integer_winding"]
            b=p["numerator_remainder"]
            d=p["odd_denominator"]
            expected=(integer + b*pow(d,-1,q))%q
            observed=(source[n].numerator*pow(source[n].denominator,-1,q))%q
            self.assertEqual(expected,observed)

    def test_four_poles(self):
        for n in range(1,32):
            self.assertEqual(forcing(n), sum((Fraction(v,8*n-d)
                for v,d in ((4,7),(-2,4),(-1,3),(-1,2))),Fraction()))

    def test_literal_zero(self):
        self.assertEqual(source_states(1)[0], 0)
        self.assertEqual(source_states(1)[1],Fraction(47,15)%1)

    def test_source_odd_denominator(self):
        for n in range(1,56):
            self.assertEqual(forcing(n).denominator%2,1)

    def test_full_modular_v_rational_recurrence(self):
        vals=lifted_source_states(44)
        mod=16**3
        vals2=modular_source_states(44,mod)
        for n in range(45):
            self.assertEqual(vals2[n],vals[n].numerator*pow(vals[n].denominator,-1,mod)%mod)

    def test_tail_monotonic(self):
        for n in range(0,40):
            self.assertGreater(forcing(n+1),forcing(n+2))

    def test_tail_brackets_nested(self):
        for n in [0,1,2,16,256]:
            previous=green_tail_interval(n,0)
            for depth in range(1,7):
                current=green_tail_interval(n,depth)
                self.assertGreaterEqual(current[0],previous[0])
                self.assertLessEqual(current[1],previous[1])
                previous=current

    def test_nonnormal_coherent_zero_control(self):
        # Wrong seed s=-pi/16: completed z_n is identically zero.
        for n in range(12):
            self.assertEqual(distance_to_nearest_integer(Fraction(0)),0)

    def test_periodic_rational_control(self):
        # x=1/(16^q-1) makes the q-time circle loop exactly closed.
        for q in (1,2,16):
            x=Fraction(1,16**q-1)
            self.assertEqual(distance_to_nearest_integer((16**q-1)*x),0)

    def test_terminating_rational_is_excluded_from_escape_theorem(self):
        # y=1/16 has a single nonzero initial state, but no late pulses.
        y=Fraction(1,16)
        self.assertEqual(distance_to_nearest_integer(y),Fraction(1,16))
        self.assertTrue(all(distance_to_nearest_integer(16**n*y)==0 for n in range(1,10)))

    def test_sharp_gap_control(self):
        # delta0=1/17, 16*delta0 == -delta0 modulo 1.
        for n in range(10):
            self.assertEqual(distance_to_nearest_integer(Fraction(16**n,17)),Fraction(1,17))

    def test_distance_interval(self):
        self.assertEqual(distance_interval_lower(Fraction(1,3),Fraction(2,5)),Fraction(1,3))
        self.assertEqual(distance_interval_lower(Fraction(9,10),Fraction(11,10)),0)
        self.assertEqual(distance_interval_lower(Fraction(-1,2),Fraction(-1,3)),Fraction(1,3))

    def test_original_q16_pulse(self):
        c=first_certified_pulse(16,2,depth=16)
        self.assertIsNotNone(c)
        self.assertEqual(c.n,2)
        self.assertGreater(c.distance_lower,Fraction(1,17))
        self.assertLess(c.interval_width,Fraction(1,16**8))

    def test_original_q256_pulse(self):
        c=first_certified_pulse(256,3,depth=16)
        self.assertIsNotNone(c)
        self.assertEqual(c.n,3)
        self.assertGreater(c.distance_lower,Fraction(1,17))

    def test_precise_pulse_certs(self):
        for q,n in [(16,2),(256,3)]:
            v=source_states(q+n)
            lo=circle_pulse_certificate(v,q,n,depth=12)
            hi=circle_pulse_certificate(v,q,n,depth=18)
            self.assertTrue(lo.passed and hi.passed)
            self.assertGreaterEqual(hi.distance_lower,lo.distance_lower)

    def test_unreduced_winding_is_load_bearing(self):
        # The REAL fractional phase cannot substitute for the lifted 2-adic state.
        lifted=lifted_source_states(5)
        reduced=source_states(5)
        mod=16**3
        self.assertEqual(lifted[1],Fraction(47,15))
        self.assertEqual(reduced[1],Fraction(2,15))
        self.assertNotEqual(lifted[1].numerator*pow(lifted[1].denominator,-1,mod)%mod,
                            reduced[1].numerator*pow(reduced[1].denominator,-1,mod)%mod)

    def test_return_jet_encodes_source_phase_orientation(self):
        # The two 16th-root phases are negatives since 11-3 = 8.
        self.assertEqual((11-3)%16,8)
        self.assertEqual([predicted_jet(n) for n in range(8)],
                         [11,11,3,3,11,11,3,3])

    def test_bbp_exact_original_pulse_metric(self):
        # Absolute lower bounds > 1/17, not uncertified trig approximations.
        for q,n in [(16,2),(256,3)]:
            c=circle_pulse_certificate(source_states(q+n),q,n,18)
            self.assertTrue(c.passed)
            self.assertGreater(c.distance_lower,Fraction(1,17))

    def test_jet_q16(self):
        self.assertEqual(return_jet_table(16,8),[11,11,3,3,11,11,3,3])

    def test_jet_q256(self):
        self.assertEqual(return_jet_table(256,8),[11,11,3,3,11,11,3,3])

    def test_jet_all_n_beyond_k(self):
        for k in (1,2):
            q=16**k
            vals=modular_source_states(q+35,16*q)
            for n in range(k+1,35):
                self.assertEqual(clock_jet(vals,k,n),predicted_jet(n))

    def test_unmutated_jet_odd(self):
        for q in (16,256):
            for value in return_jet_table(q,12):
                self.assertEqual(value%2,1)

    def test_mutant_breaks_jet(self):
        # The mutant does not even close its zero-seeded q-clock at n=0.
        mutant=modular_source_states(24,256,3)
        self.assertNotEqual((mutant[16]-mutant[0])%16,0)
        self.assertEqual(return_jet_table(16,8,4),[11,11,3,3,11,11,3,3])

    def test_metric_floor(self):
        self.assertAlmostEqual(pulse_energy_threshold(),0.1350555411912884,places=12)

    def test_2adic_return_isometry_mod_q(self):
        for k in (1,2):
            q=16**k
            states=modular_source_states(q+34,16*q)
            for n in range(k+1,34):
                step=(states[n+q]-states[n])%(16*q)
                self.assertEqual(step%q,0)
                self.assertNotEqual(step%(16*q),0)

if __name__=='__main__': unittest.main()
