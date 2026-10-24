"""Independent exact-integer and analytic controls for N-internal BBP."""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_natural_carrier import (
    ORIGIN, NaturalBBPState, forcing_numerator, forcing_denominator,
    exact_forcing, machine_step, orbit_state, orbit_prefix,
    cantor_pair, cantor_unpair, encode_state, decode_state,
    encoded_machine_step, dyadic_view, dyadic_observer_step,
    rational_partial_alpha, alpha_enclosure, source_tail_enclosure,
)
from observational_succ.pi_joint_prime_carrier import (
    forcing as independent_four_poles,
    states as independent_source,
    local_primary, joint_circle, dyadic_integral,
)


def arctan_interval(unit_inv, terms):
    """Exact alternating rational bounds: arctan(1/q)."""
    x = Q(1, unit_inv)
    s = sum(((-1)**j * x**(2*j+1) / (2*j+1) for j in range(terms)), Q())
    err = (-1)**terms * x**(2*terms+1) / (2*terms+1)
    return min(s, s+err), max(s, s+err)


def machin_alpha_interval(terms=65):
    """pi/16 = arctan(1/5) - (1/4) arctan(1/239)."""
    a,b=arctan_interval(5,terms)
    c,d=arctan_interval(239,terms)
    return a - d/4, b - c/4


class NaturalCarrierTests(unittest.TestCase):
    def test_polynomials_are_exactly_original_four_poles(self):
        for j in range(1,101):
            self.assertEqual(
                exact_forcing(j),
                Q(4,8*j-7)-Q(2,8*j-4)-Q(1,8*j-3)-Q(1,8*j-2))
            self.assertEqual(exact_forcing(j), independent_four_poles(j))

    def test_positivity_oddness_and_polynomial_bound(self):
        # n=t+1: P=120t^2+151t+47; 8D-n^2P has *positive*
        # coefficients (3976, 7801, 5227, 1307, 73) in t>=0.
        for j in range(1,180):
            self.assertGreater(forcing_numerator(j),0)
            self.assertEqual(forcing_denominator(j)%2,1)
            self.assertGreater(8*forcing_denominator(j),j*j*forcing_numerator(j))
            if j<179:
                self.assertGreater(exact_forcing(j),exact_forcing(j+1))

    def test_origin_and_actual_orbit(self):
        vals = independent_source(64)
        self.assertEqual(ORIGIN, NaturalBBPState(0,0,0))
        for j,s in enumerate(orbit_prefix(64)):
            self.assertEqual(s.time,j)
            self.assertEqual(s.rational,vals[j])
            self.assertEqual(s.denominator%2,1)
            self.assertEqual(machine_step(s).rational,16*s.rational+independent_four_poles(j+1))
        self.assertEqual(orbit_state(1).rational,Q(47,15))

    def test_total_noncanonical_state_transition(self):
        for n in (0,1,2,17,31):
            for a in (0,1,7,41):
                for t in (0,1,11,89):
                    state=NaturalBBPState(n,a,t)
                    nxt=machine_step(state)
                    self.assertEqual(nxt.time,n+1)
                    self.assertEqual(nxt.rational,16*state.rational+exact_forcing(n+1))
                    self.assertEqual(nxt.denominator%2,1)

    def test_section_is_a_genuine_successor_morphism(self):
        for n in range(35):
            self.assertEqual(machine_step(orbit_state(n)), orbit_state(n+1))

    def test_cantor_product_code_roundtrip(self):
        for a in (0,1,2,15,173,2**64):
            for b in (0,1,3,99,2**80):
                self.assertEqual(cantor_unpair(cantor_pair(a,b)),(a,b))
        for s in orbit_prefix(30):
            self.assertEqual(decode_state(encode_state(s)),s)
            self.assertEqual(encoded_machine_step(encode_state(s)),encode_state(machine_step(s)))
        for n in (0,2,50):
            for a in (0,17):
                for t in (0,19):
                    s=NaturalBBPState(n,a,t)
                    self.assertEqual(encoded_machine_step(encode_state(s)),encode_state(machine_step(s)))

    def test_dyadic_factor_commutes_on_all_states(self):
        for n in (0,1,2,9):
            for a,t in ((0,0),(1,0),(7,13),(29,21)):
                s=NaturalBBPState(n,a,t)
                nxt=machine_step(s)
                for bits in (1,2,4,7,12):
                    self.assertEqual(dyadic_view(nxt,bits),
                                     dyadic_observer_step(n,dyadic_view(s,bits),bits))
                    self.assertEqual(dyadic_view(s,bits),dyadic_integral(s.rational,bits))

    def test_prime_torsion_views_are_synchronized_factors(self):
        for s in orbit_prefix(12):
            nxt=machine_step(s)
            for p in (2,3,5,7,11,13,17,19):
                self.assertEqual(local_primary(nxt.rational,p),
                                 (16*local_primary(s.rational,p)+
                                  local_primary(exact_forcing(s.time+1),p))%1)
                if p==2:
                    self.assertEqual(local_primary(s.rational,p),Q())
        for s in orbit_prefix(10):
            self.assertEqual(joint_circle(s.rational),s.rational%1)

    def test_integer_lift_matters_to_rational_filter(self):
        u=Q(1,7);v=u+1
        self.assertEqual(u%1,v%1)
        self.assertNotEqual((u/5)%1,(v/5)%1)
        self.assertNotEqual(ORIGIN.rational%1,machine_step(ORIGIN).rational%1)
        self.assertNotEqual((16*ORIGIN.rational)%1,machine_step(ORIGIN).rational%1)

    def test_pascal_trace_internal_to_natural_orbit(self):
        seq=orbit_prefix(19)
        for degree in range(19):
            expected=sum(((-1)**(degree-j)*comb(degree,j)*seq[j].rational
                          for j in range(degree+1)),Q())
            self.assertEqual(expected, sum(((-1)**(degree-j)*comb(degree,j)*
                                            independent_source(degree+1)[j]
                                            for j in range(degree+1)),Q()))

    def test_rational_pi_lower_approximants(self):
        assert ORIGIN.rational==0
        for n in range(26):
            self.assertEqual(rational_partial_alpha(n),orbit_state(n).rational/16**n)
            if n:
                self.assertLess(rational_partial_alpha(n-1),rational_partial_alpha(n))

    def test_exact_enclosures_against_independent_machin_oracle(self):
        low,high=machin_alpha_interval(70)
        self.assertLess(low,high)
        for n in (0,1,2,3,5,8,13,21,35):
            a,b=alpha_enclosure(n)
            self.assertLess(a,high)
            self.assertGreater(b,low)
            self.assertGreater(a if n>0 else Q(0),Q(-1))
            self.assertLess(b-a,Q(8,15*(n+1)**2*16**n)+Q(1,16**(n+200)))

    def test_tail_intervals_are_strict_and_nested(self):
        for n in (0,1,3,19):
            previous=None
            for terms in (1,2,4,8,12):
                a,b=source_tail_enclosure(n,terms)
                self.assertLess(a,b)
                self.assertLess(b-a,Q(8,15*(n+terms+1)**2*16**terms))
                if previous:
                    self.assertLess(previous[0],a)
                    self.assertLess(b,previous[1])
                previous=(a,b)
            self.assertLess(b,Q(8,15*(n+1)**2))

    def test_backward_not_total_on_2integral_space(self):
        # An arbitrary 2-integral state cannot be reversed by /16,
        # although the special source graph extends arithmetically.
        fake_next=Q(0)
        prev=(fake_next-exact_forcing(1))/16
        self.assertEqual(prev.denominator%2,0)
        authentic_next=orbit_state(1).rational
        self.assertEqual((authentic_next-exact_forcing(1))/16,Q(0))

    def test_input_validation(self):
        for bad in (-1,True,0.4):
            with self.assertRaises((ValueError,TypeError)):
                orbit_state(bad)
            with self.assertRaises((ValueError,TypeError)):
                decode_state(bad)
            with self.assertRaises((ValueError,TypeError)):
                forcing_denominator(bad)
        with self.assertRaises(ValueError):
            NaturalBBPState(0,0,-1)
        with self.assertRaises(ValueError):
            source_tail_enclosure(0,0)
        with self.assertRaises(ValueError):
            dyadic_view(ORIGIN,0)


if __name__=='__main__':
    unittest.main()

class DigitCertificateTests(unittest.TestCase):
    def test_first_hexadecimal_digits_certified_without_pi_float(self):
        from observational_succ.bbp_natural_carrier import certified_hex_digit
        # pi's fixed hexadecimal prefix is a display-only regression; the
        # oracle below computes pi by a DIFFERENT (Machin) rational series.
        expected = "3243F6A8885A308D313198A2E0370734"
        self.assertEqual(''.join(format(certified_hex_digit(n)[0],'X')
                                 for n in range(len(expected))), expected)

    def test_fresh_indices_against_independent_machin_bounds(self):
        from observational_succ.bbp_natural_carrier import certified_hex_digit
        low, high = machin_alpha_interval(160)
        for n in (0, 1, 2, 3, 8, 19, 31, 52, 64, 73, 89, 100):
            result = certified_hex_digit(n, 90)
            self.assertIsNotNone(result)
            digit, terms = result
            a, b = 16**(n+1)*low, 16**(n+1)*high
            da, db = a.numerator//a.denominator, b.numerator//b.denominator
            self.assertEqual(da, db)
            self.assertEqual(digit, da % 16)
            self.assertGreaterEqual(terms, 1)

    def test_budget_is_explicit_and_low_budget_may_not_certify(self):
        from observational_succ.bbp_natural_carrier import certified_hex_digit
        # Budget=1 happens to certify the authentic first digit. A test
        # must NOT manufacture an ambiguity absent from the source.
        self.assertEqual(certified_hex_digit(0, 1), (3, 1))
        with self.assertRaises(ValueError):
            certified_hex_digit(0, 0)
