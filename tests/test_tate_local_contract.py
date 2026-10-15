"""Exact Tate local certificates; floating comparisons are supplementary only."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.tate_local_contract import (
    TateContractError, QRootMinus3, DELTA, ZETA3, chi_mod3,
    unramified_ball_pair, gauss_sum_mod3, ramified_mod3_coset_pair,
    coarse_ramified_unit_zeta, finite_twisted_log_jets,
    fake_composite_local_factor, symmetric_offline_mutant,
)


class UnramifiedTateContractTests(unittest.TestCase):
    def test_all_exact_tate_ball_shifts_and_unramified_signs(self):
        count = 0
        for p, a, s, omega in product((2, 3, 5, 7, 11), range(-3, 4),
                                      (2, 3, 4), (-1, 1)):
            pair = unramified_ball_pair(p, a, s, omega)
            self.assertEqual(pair.zeta,
                             (omega if a % 2 else 1) * Q(p) ** (-a*s) /
                             (1 - omega*Q(p)**(-s)))
            self.assertEqual(pair.zeta, pair.forward_over_dual*pair.dual_zeta)
            self.assertEqual(pair.forward_over_dual*pair.inverse_tate_gamma, 1)
            # Scaling the additive Fourier measure by p would break this law.
            self.assertNotEqual(pair.zeta,
                                pair.forward_over_dual * p * pair.dual_zeta)
            count += 1
        self.assertEqual(count, 210)

    def test_wrong_prime_and_untyped_character_rejected(self):
        for p in (0, 1, 4, 6, 9, -3, 2.0, True):
            with self.subTest(p=p), self.assertRaises(TateContractError):
                unramified_ball_pair(p, 1, 3)
        for a, s, omega in ((0.2, 2, 1), (1, 1, 1), (0, 2, 0),
                            (0, 2, 2), (True, 2, 1)):
            with self.assertRaises(TateContractError):
                unramified_ball_pair(3, a, s, omega)

    def test_real_and_mutant_euler_sources(self):
        for s in (2, 3, 4, 5):
            fake, real = fake_composite_local_factor(s)
            self.assertNotEqual(fake, real)
            self.assertEqual(real,
                             unramified_ball_pair(2, 0, s).zeta *
                             unramified_ball_pair(3, 0, s).zeta)


class RamifiedConductorTests(unittest.TestCase):
    def test_exact_cyclotomic_algebra_and_gauss(self):
        self.assertEqual(DELTA**2, QRootMinus3(-3))
        self.assertEqual(ZETA3**3, QRootMinus3(1))
        self.assertEqual(ZETA3+ZETA3**2, QRootMinus3(-1))
        self.assertEqual(gauss_sum_mod3(1), DELTA)
        self.assertEqual(gauss_sum_mod3(2), -DELTA)
        self.assertEqual(gauss_sum_mod3(-1), -DELTA)
        self.assertEqual(gauss_sum_mod3(1).norm(), 3)
        self.assertEqual(DELTA * (1/DELTA), QRootMinus3(1))

    def test_primitive_character_is_multiplicative(self):
        for a in range(-15, 16):
            for b in range(-15, 16):
                self.assertEqual(chi_mod3(a*b), chi_mod3(a)*chi_mod3(b))

    def test_ramified_tate_coset_exact_fe(self):
        for unit, s in product((1, 2, 4, 5, -1, -2), (2, 3, 4, 7)):
            pair = ramified_mod3_coset_pair(unit, s)
            self.assertEqual(pair.zeta, Q(chi_mod3(unit), 2))
            self.assertEqual(pair.dual_zeta,
                             gauss_sum_mod3(unit) * Q(1, 2 * 3**s))
            self.assertEqual(QRootMinus3(pair.zeta),
                             pair.forward_over_dual * pair.dual_zeta)
            self.assertEqual(pair.forward_over_dual,
                             QRootMinus3(0, -(3**(s-1))))
        for bad in (0, 3, 6, -3):
            with self.assertRaises(TateContractError):
                ramified_mod3_coset_pair(bad, 2)

    def test_coarse_unit_observer_erases_character(self):
        self.assertEqual(coarse_ramified_unit_zeta(), 0)
        self.assertEqual(ramified_mod3_coset_pair(1, 2).zeta, Q(1, 2))
        self.assertEqual(ramified_mod3_coset_pair(2, 2).zeta, Q(-1, 2))
        self.assertEqual(coarse_ramified_unit_zeta(),
                         (ramified_mod3_coset_pair(1, 2).zeta
                          +ramified_mod3_coset_pair(2, 2).zeta))
        # Chi_3 cannot be reconstructed from a single coarse unit observation.
        self.assertNotEqual(gauss_sum_mod3(1), gauss_sum_mod3(2))

    def test_unramified_unit_ball_is_not_ramified_character_probe(self):
        self.assertNotEqual(unramified_ball_pair(3, 0, 2).zeta,
                            coarse_ramified_unit_zeta())
        with self.assertRaises(TateContractError):
            gauss_sum_mod3(3)


class SourceAndLogicControls(unittest.TestCase):
    def test_exact_twisted_prime_jets(self):
        primes = (2, 3, 5, 7, 11, 13)
        for s, d in product((2, 3), (1, 2, 5)):
            jets = finite_twisted_log_jets(primes, d, s, "chi3")
            self.assertNotIn(3, jets)  # local ramification suppresses Euler factor
            for p, val in jets.items():
                direct = sum((Q(chi_mod3(p**k), (p**k)**s)
                              for k in range(1, d+1)), Q(0))
                self.assertEqual(val, direct)
            self.assertNotEqual(jets[2],
                                finite_twisted_log_jets(primes,d,s,"trivial")[2])

    def test_false_places_and_fake_characters_fail_closed(self):
        for ps in ((6,), (2, 2), (3, 2), (2.0,), (1,), (4,)):
            with self.assertRaises(TateContractError):
                finite_twisted_log_jets(ps, 2, 3)
        for bad in ("fakechi", "chi4", "", None):
            with self.assertRaises(TateContractError):
                finite_twisted_log_jets((2,3), 2, 3, bad)

    def test_symmetric_completion_mutant_refutes_fe_implies_rh(self):
        P = symmetric_offline_mutant
        for s in (Q(-3, 2), 0, Q(1, 7), Q(1, 2), 1, Q(17, 9)):
            self.assertEqual(P(s), P(1-Q(s)))
        self.assertEqual(P(0), 1)
        self.assertEqual(P(1), 1)
        self.assertEqual(P(Q(1, 4)), 0)
        self.assertEqual(P(Q(3, 4)), 0)
        self.assertEqual(P(Q(1, 2)), Q(-1, 3))
        # The extra zeros are OFF the critical line, even though FE/poles survive.


class CompletedChi3TateTests(unittest.TestCase):
    def test_theta_poisson_odd_character_against_independent_halves(self):
        import mpmath as mp
        from observational_succ.tate_local_contract import chi3_odd_theta
        for tt in (Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(3, 2), Q(3)):
            left = chi3_odd_theta(tt, 26, 80)
            right = mp.power(mp.mpf(tt.denominator)/tt.numerator, mp.mpf(3)/2) * chi3_odd_theta(1/tt, 26, 80)
            self.assertLess(abs(left-right), mp.mpf('1e-50'))

    def test_completed_chi3_source_vs_independent_hurwitz(self):
        import mpmath as mp
        from observational_succ.tate_local_contract import (chi3_completed_theta,
                                                              chi3_strip_tail_rational)
        ss = (mp.mpc('0.125', '3'), mp.mpc('0.5', '13'), mp.mpc('0.9', '20'))
        for s in ss:
            N = 7
            source = chi3_completed_theta(s, N, 80)
            mp.mp.dps = 80
            L = mp.power(3, -s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
            oracle = mp.power(3/mp.pi, (s+1)/2)*mp.gamma((s+1)/2)*L
            bound = chi3_strip_tail_rational(N, 60)
            rigorous_bound_eval = mp.mpf(bound.numerator)/bound.denominator
            self.assertLess(abs(source-oracle), rigorous_bound_eval)
            self.assertLess(abs(source-chi3_completed_theta(1-s, N, 80)),
                            mp.mpf('1e-60'))

    def test_tail_contract_is_exact_and_improves(self):
        from observational_succ.tate_local_contract import chi3_strip_tail_rational
        for N in (2,3,4,6):
            self.assertGreater(chi3_strip_tail_rational(N), 0)
            self.assertLess(chi3_strip_tail_rational(N+1),
                            chi3_strip_tail_rational(N))
            self.assertLess(chi3_strip_tail_rational(N, 45),
                            chi3_strip_tail_rational(N, 15))
        self.assertLess(chi3_strip_tail_rational(7, 55), Q(1,10**16))

    def test_non_ramified_mutant_does_not_inherit_chi_completion(self):
        from observational_succ.tate_local_contract import chi3_completed_theta
        import mpmath as mp
        s=mp.mpc('0.5', '7')
        genuine=chi3_completed_theta(s,8,70)
        mutant=genuine * mp.mpf('0.95')
        self.assertGreater(abs(mutant-genuine), mp.mpf('1e-5'))


if __name__ == "__main__":
    unittest.main()
