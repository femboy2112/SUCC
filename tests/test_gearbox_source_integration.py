"""Cross-branch integration: the SUCC gears meshing on ONE authentic source.

This suite is not another per-module test. It connects independently authored
branches of the 2026-10-24 pi frontier and asserts that they agree about the
*same* authenticated four-pole BBP source, on common source times.

Ground-truth discipline (AGENTS.md / integration prompt): no assertion here is
allowed to use an implementation under test as its own oracle. The reference for
every digit/value claim is an INDEPENDENT Machin-type rational computation of pi
(no BBP, no floating point) or exact rational algebra. The carriers are only ever
compared *to that external reference* or *to each other*.

Authentic source law (fixed, not to be altered):
    r(n) = (120 n^2 - 89 n + 16) / ((2n-1)(4n-1)(8n-7)(8n-3)),  n >= 1
    U_0 = 0,  U_{n+1} = 16 U_n + r(n+1),   alpha = pi/16 = lim U_n / 16^n.

What this suite does NOT establish: any frequency, equidistribution, or
normality statement. pi normality remains OPEN.
"""
from __future__ import annotations

import unittest
from fractions import Fraction

from observational_succ import bbp_natural_carrier as NC
from observational_succ import integer_bbp_carrier as IC


# --- independent reference: Machin pi, exact rationals, no BBP, no float ------
def _arctan_inv(x: int, terms: int) -> Fraction:
    return sum((Fraction((-1) ** k, (2 * k + 1) * x ** (2 * k + 1))
                for k in range(terms)), Fraction(0))


# 4 arctan(1/5) - arctan(1/239); term counts give >> 40 correct hex digits.
PI = 4 * (4 * _arctan_inv(5, 200) - _arctan_inv(239, 120))


def _hex_digits(frac: Fraction, count: int) -> list[int]:
    f = frac - int(frac)
    out = []
    for _ in range(count):
        f *= 16
        d = int(f)
        out.append(d)
        f -= d
    return out


PI_HEX = _hex_digits(PI - 3, 40)       # {pi}  : 2,4,3,F,6,A,8,8,8,5,...
PI16_HEX = _hex_digits(PI / 16, 40)    # pi/16 : 3,2,4,3,F,6,A,8,...


class ReferenceCalibration(unittest.TestCase):
    """Calibrate the instrument before trusting any reading (Instrument rule)."""

    def test_machin_oracle_matches_known_pi_hex(self):
        # Known expansion pi = 3.243F6A8885A308D3... (base 16).
        self.assertEqual(
            "".join("%X" % d for d in PI_HEX[:16]), "243F6A8885A308D3")

    def test_pi_over_16_is_a_hex_shift_of_pi(self):
        self.assertEqual(PI16_HEX[0], 3)
        self.assertTrue(all(PI16_HEX[i] == PI_HEX[i - 1] for i in range(1, 30)))


class SingleSourceTwoCarriers(unittest.TestCase):
    """Gear #1: the N-successor carrier (#281) and the integer carrier (#282)
    are two representations of ONE source; their unwrapped rationals coincide."""

    def test_identical_unwrapped_rationals(self):
        for n in range(60):
            un_281 = NC.orbit_state(n).rational
            st = IC.source_states(n)[-1]
            un_282 = Fraction(st.numerator, st.conductor)
            self.assertEqual(un_281, un_282, f"carriers disagree on U_{n}")

    def test_forcing_law_agrees_both_carriers(self):
        # #282 returns reduced a/b; #281 returns the raw product form; as exact
        # rationals they are the same r(n), and the denominator stays odd.
        for n in range(1, 40):
            a, b = IC.forcing_pair(n)
            self.assertEqual(Fraction(a, b), NC.exact_forcing(n))
            self.assertEqual(b % 2, 1)
            self.assertEqual(NC.forcing_denominator(n) % 2, 1)

    def test_tail_enclosures_bracket_the_true_alpha(self):
        # The external reference alpha = pi/16 must sit inside both carriers'
        # exact rational enclosures at every tested index -- oracle, not self.
        alpha = PI / 16
        for n in range(0, 24):
            lo281, hi281 = NC.alpha_enclosure(n)
            self.assertLessEqual(lo281, alpha)
            self.assertLess(alpha, hi281)
            lo282, hi282 = IC.tail_bounds(n, 12)
            u = NC.orbit_state(n).rational / 16 ** n  # U_n/16^n
            self.assertLessEqual(u + lo282 / 16 ** n, alpha)
            self.assertLess(alpha, u + hi282 / 16 ** n)


class CertifiedDigitsAgreeWithOracle(unittest.TestCase):
    """Gear #8: certified hex digits from BOTH carriers match the independent
    Machin oracle, each at its documented convention."""

    def test_integer_carrier_digits_are_pi_hex(self):
        for n in range(1, 31):
            st = IC.source_states(n)[-1]
            digit, _depth = IC.hexadecimal_digit(st)
            self.assertEqual(digit, PI_HEX[n - 1], f"#282 digit {n}")

    def test_natural_carrier_digits_are_pi_over_16_hex(self):
        for i in range(0, 30):
            got = NC.certified_hex_digit(i)
            self.assertIsNotNone(got, f"#281 failed to certify digit {i}")
            self.assertEqual(got[0], PI16_HEX[i], f"#281 digit {i}")

    def test_two_carriers_agree_on_shared_digits(self):
        # pi/16 digit i (natural carrier) == pi digit i-1 (integer carrier),
        # routed only through the external oracle's shift identity.
        for i in range(1, 30):
            d_nat = NC.certified_hex_digit(i)[0]
            d_int, _ = IC.hexadecimal_digit(IC.source_states(i)[-1])
            self.assertEqual(d_nat, d_int, f"carriers disagree at shared digit {i}")


class DyadicObserverFactorsThroughSource(unittest.TestCase):
    """Gear #4: the 2-adic observation is a genuine quotient of the one source,
    identical across carriers, and its local step commutes with the machine."""

    def test_cross_branch_dyadic_reduction_matches(self):
        for n in range(40):
            nc = NC.orbit_state(n)
            ic = IC.source_states(n)[-1]
            u = nc.rational
            for k in (4, 8, 16, 32):
                m = 1 << k
                independent = (u.numerator * pow(u.denominator, -1, m)) % m
                self.assertEqual(NC.dyadic_view(nc, k), independent)
                self.assertEqual(
                    (ic.numerator * pow(ic.conductor, -1, m)) % m, independent)

    def test_local_dyadic_step_commutes_with_source(self):
        for k in (4, 8, 16):
            residue = 0
            for n in range(30):
                self.assertEqual(NC.dyadic_view(NC.orbit_state(n), k), residue)
                residue = NC.dyadic_observer_step(n, residue, k)


class HostileControls(unittest.TestCase):
    """Negative controls: things that look source-like but are not the source.
    A test suite that only confirms the happy path certifies nothing."""

    def test_changed_initial_state_is_not_the_authentic_orbit(self):
        alt = NC.NaturalBBPState(0, 1, 0)  # U_0 = 1 instead of 0
        for _ in range(5):
            alt = NC.machine_step(alt)
        self.assertNotEqual(alt.rational, NC.orbit_state(5).rational)

    def test_one_third_counterfeit_is_not_pi(self):
        # A different positive, odd-denominator source of the same leading
        # shape. Its orbit tends to 1/3, not pi/16 -- so "positive odd source"
        # is not by itself evidence of the authentic circle.
        u = Fraction(0)
        for n in range(1, 25):
            u = 16 * u + IC.odd_rational_counterfeit_forcing(n)
            self.assertNotEqual(IC.odd_rational_counterfeit_forcing(n),
                                NC.exact_forcing(n))
        limit_proxy = u / 16 ** 24
        self.assertNotEqual(limit_proxy, PI / 16)
        self.assertLess(abs(limit_proxy - Fraction(1, 3)), Fraction(1, 16 ** 20))

    def test_dropped_forcing_mutant_never_reaches_pi(self):
        # Drop the forcing term entirely: U_{n+1} = 16 U_n. Orbit stays 0.
        u = Fraction(0)
        for _ in range(10):
            u = 16 * u
            self.assertEqual(u, 0)

    def test_integer_carrier_rejects_non_source_digit_readout(self):
        # A hand-built state that is not the zero-initial authenticated source
        # must be refused, not silently decoded.
        bogus = IC.IntegerState(5, IC.conductor_at(5), 123456789)
        with self.assertRaises(ValueError):
            IC.hexadecimal_digit(bogus)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
