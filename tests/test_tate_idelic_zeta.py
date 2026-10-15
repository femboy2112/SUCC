"""Exact finite witnesses plus diagnostic quadrature, never a numeric RH proof."""
import itertools
import unittest
from fractions import Fraction as Q

import mpmath as mp

from observational_succ.tate_idelic_zeta import (
    IdeleClassChart, RationalChartIdele, StandardTateSource, TateIdelicError,
    TateZeroModes, euler_exhaustion_bound, finite_euler_stage,
    log_derivative_tail_bound, multiplicative_shell_mass,
    omitted_place_witness, real_gamma_even_integer,
)


class IdelicSourceTests(unittest.TestCase):
    def test_general_rational_chart_normalization_and_reconstruction(self):
        for real in (Q(-5, 8), Q(1, 3), Q(14)):
            for a, b in itertools.product((Q(1, 2), Q(-3), Q(8, 9)), repeat=2):
                x = RationalChartIdele(real, Q(5, 7), ((2, a), (3, b)))
                chart = x.quotient()
                self.assertEqual(chart.reconstruct(), x)
                self.assertEqual(chart.representative.real, x.norm)
                self.assertEqual(chart.representative.finite_valuations(), ())
                for p in (2, 3, 5, 7, 11):
                    self.assertNotEqual(chart.unit_residue(p, 3) % p, 0)

    def test_quotient_commutes_with_diagonal_rational_action(self):
        x = RationalChartIdele(Q(-7, 15), Q(9, 14), ((2, Q(8)), (5, Q(3, 25))))
        base = x.quotient()
        for a in (Q(-1), Q(3, 8), Q(-11, 49)):
            moved = x.diagonal_action(a).quotient()
            self.assertEqual(moved.representative, base.representative)
            self.assertEqual(moved.rational_multiplier, a * base.rational_multiplier)
            self.assertEqual(x.diagonal_action(a).norm, x.norm)

    def test_idelic_validation_is_not_adelic_nonzero_validation(self):
        # Every coordinate must be nonzero; composite and duplicate places fail.
        for args in ((0,), (1, 0), (1, 1, ((6, Q(1)),)), (1, 1, ((2, Q(0)),)),
                     (1, 1, ((2, Q(1)), (2, Q(2))))):
            with self.subTest(args=args), self.assertRaises(TateIdelicError):
                RationalChartIdele(*args)

    def test_invalid_quotient_representatives_rejected(self):
        for x in (RationalChartIdele(-1), RationalChartIdele(1, 2)):
            with self.assertRaises(TateIdelicError):
                IdeleClassChart(Q(1), x)

    def test_source_to_poisson_and_local_fourier_interfaces(self):
        src = StandardTateSource("source-A", 4)
        gen = src.poisson_generator()
        self.assertEqual((gen.coset.shift, gen.coset.scale, gen.heat), (0, 1, 1))
        for p in (2, 3, 7):
            ball = src.local_test(p)
            self.assertEqual((ball.source_id, ball.epoch), ("source-A", 4))
            for x in (Q(0), Q(1), Q(p), Q(1, p)):
                self.assertEqual(ball.fourier(x).amplitude, int(ball.contains(x)))
                self.assertEqual(ball.fourier(x).phase, 0)

    def test_orbit_support_exactly_integers_for_nontrivial_unit_chart(self):
        src = StandardTateSource()
        unit = RationalChartIdele(Q(7, 3), Q(1), ((2, Q(3)), (3, Q(2))))
        for num in range(-12, 13):
            if num == 0:
                continue
            for den in range(1, 9):
                q = Q(num, den)
                result = src.rational_orbit_exponent(unit, q)
                self.assertEqual(result is not None, q.denominator == 1)
                if q.denominator == 1:
                    self.assertEqual(result, (q * Q(7, 3)) ** 2)

    def test_source_identity_and_epoch_are_not_silently_joined(self):
        src = StandardTateSource("A", 2)
        for x in (RationalChartIdele(1, source_id="B", epoch=2),
                  RationalChartIdele(1, source_id="A", epoch=3)):
            with self.assertRaises(TateIdelicError):
                src.evaluate_exponent(x)

    def test_multiplicative_haar_shells_from_additive_measures(self):
        for p in (2, 3, 5, 13):
            for k in range(-4, 5):
                self.assertEqual(multiplicative_shell_mass(p, k), 1)
                # Omitting the normalization (1-p^-1)^-1 gives the wrong mass.
                self.assertNotEqual(1 - Q(1, p), multiplicative_shell_mass(p, k))

    def test_euler_stage_agrees_with_direct_valuation_tuple_enumeration(self):
        for ps in ((), (2,), (2, 3), (2, 3, 5)):
            depth = 4
            stage = finite_euler_stage(ps, 2, depth)
            direct = Q(0)
            for valuations in itertools.product(range(depth), repeat=len(ps)):
                n = 1
                for p, k in zip(ps, valuations):
                    n *= p ** k
                direct += Q(1, n ** 2)
            self.assertEqual(stage["finite_shell_product"], direct)
            self.assertEqual(direct + stage["exact_shell_tail"], stage["complete_finite_place_product"])

    def test_prime_exhaustion_bound_has_exact_missing_coefficient_support(self):
        receipt = euler_exhaustion_bound(11, 3)
        self.assertEqual(receipt["primes"], (2, 3, 5, 7, 11))
        self.assertEqual(receipt["absolute_error_bound"], Q(1, 242))
        missing = Q(0)
        for n in range(1, 100):
            a = n
            for p in receipt["primes"]:
                while a % p == 0:
                    a //= p
            if a != 1:
                self.assertGreater(n, 11)
                missing += Q(1, n ** 3)
        self.assertLess(missing, receipt["absolute_error_bound"])

    def test_fake_composite_euler_place_rejected(self):
        for bad in (6, 9, 1):
            with self.assertRaises(TateIdelicError):
                StandardTateSource().local_test(bad)
            with self.assertRaises(TateIdelicError):
                finite_euler_stage((bad,), 2)

    def test_omitted_prime_is_a_finite_exact_source_witness(self):
        for p in (2, 7, 101):
            witness = omitted_place_witness(p)
            self.assertEqual(witness["first_changed_integer_coefficient"], p)
            self.assertNotEqual(witness["genuine_coefficient"], witness["mutant_coefficient"])
            self.assertEqual(witness["mutant_to_true_Euler_ratio_at_s"], Q(p * p - 1, p * p))

    def test_real_gamma_and_the_sign_factor_normalization(self):
        # Integral over both components R^times: Gamma_R(2)=1/pi.
        self.assertEqual(real_gamma_even_integer(2), (1, -1))
        self.assertEqual(real_gamma_even_integer(6), (2, -3))
        self.assertNotEqual(real_gamma_even_integer(6), (120, -3))  # Gamma(s), same pi exponent
        self.assertNotEqual(real_gamma_even_integer(2), (Q(1, 2), -1))
        self.assertNotEqual(real_gamma_even_integer(2), (1, -2))
        # Quotient Haar has mass 1 on norm-one units. The sign multiplicity
        # belongs in the rational orbit, and cancels dr/r=dt/(2t).
        source = StandardTateSource()
        rep = RationalChartIdele(1)
        orbit = [source.rational_orbit_exponent(rep, n) for n in range(-3, 4) if n]
        positive_sign_count = orbit.count(Q(1))
        self.assertEqual(positive_sign_count, 2)
        heat_jacobian, quotient_mass = Q(1, 2), 1
        self.assertEqual(positive_sign_count * heat_jacobian * quotient_mass, 1)
        self.assertNotEqual(positive_sign_count * heat_jacobian * 2, 1)

    def test_zero_mode_residues_and_fourier_exchange(self):
        for zero, dual in ((Q(1), Q(1)), (Q(3, 2), Q(-2))):
            modes = TateZeroModes(zero, dual)
            self.assertEqual(modes.residues, (-zero, dual))
            for s in (Q(2), Q(-3, 7), Q(1, 3)):
                self.assertEqual(modes.pole_term(s), modes.fourier_exchange().pole_term(1 - s))
        self.assertEqual(TateZeroModes().pole_term(2), Q(1, 2))

    def test_fixed_gamma_bound_on_unbounded_halfplane_is_refuted(self):
        numerator, power = real_gamma_even_integer(20)
        base, base_power = real_gamma_even_integer(2)
        self.assertEqual((numerator // base, power - base_power), (362880, -9))
        # pi<4 gives Gamma_R(20)/Gamma_R(2)>9!/4^9>1.
        self.assertGreater(Q(numerator, base * 4 ** (base_power - power)), 1)

    def test_omitted_or_wrong_pole_terms_fail_exactly(self):
        modes = TateZeroModes()
        self.assertNotEqual(modes.residues, (0, 0))
        self.assertNotEqual(modes.residues, (1, 1))
        self.assertNotEqual(modes.pole_term(2), Q(-1, 2))
        for s in (0, 1):
            with self.assertRaises(TateIdelicError):
                modes.pole_term(s)

    def test_true_log_derivative_tape_not_an_euler_dirichlet_tape(self):
        result = StandardTateSource().logarithmic_coefficients(30)
        labels = dict(result["prime_power_labels"])
        self.assertEqual(labels[8], 2)
        self.assertEqual(labels[9], 3)
        for non_power in (6, 10, 12, 15, 30):
            self.assertNotIn(non_power, labels)
        # 6 DOES have Dirichlet zeta coefficient 1; its log coefficient is 0.
        self.assertNotEqual(labels.get(6, 0), 1)

    def test_rational_log_tail_bound_against_looser_exact_majorant(self):
        # log(n) <= ceil(log2(n)), a completely rational validation prefix.
        N, sigma = 20, 3
        finite_majorant = sum((Q((n - 1).bit_length(), n ** sigma) for n in range(N + 1, 150)), Q(0))
        # This particular looser prefix remains below the independently proved
        # integral bound; that observation is not its universal proof.
        self.assertLess(finite_majorant, log_derivative_tail_bound(N, sigma))

    def test_theta_truncation_bound_is_positive_and_decreases(self):
        src = StandardTateSource()
        bounds = [src.tail_bound(N, 4) for N in (3, 4, 5)]
        self.assertGreater(bounds[-1], 0)
        self.assertGreater(bounds[0], bounds[1])
        self.assertGreater(bounds[1], bounds[2])


class TateAnalyticDiagnosticTests(unittest.TestCase):
    def test_idelic_norm_integral_matches_inherited_heat_integral(self):
        src = StandardTateSource()
        with mp.workdps(35):
            z = mp.mpc("0.3", "2.1")
            N = 4
            # Independent quadrature in r, rather than incomplete Gamma in t.
            integral = 2 * mp.quad(lambda r: sum(mp.exp(-mp.pi * n * n * r * r)
                                  for n in range(1, N + 1)) * (r ** z + r ** (1 - z)) / r,
                                  [1, 2, 4, mp.inf])
            direct = 1 / (z * (z - 1)) + integral
            self.assertLess(abs(direct - src.completed(z, N, 35)), mp.mpf("1e-29"))

    def test_absolute_half_plane_and_functional_equation_diagnostics(self):
        src = StandardTateSource()
        with mp.workdps(40):
            for z in (mp.mpc(2, 0), mp.mpc("2.7", "1.2")):
                reference = mp.pi ** (-z / 2) * mp.gamma(z / 2) * mp.zeta(z)
                self.assertLess(abs(src.completed(z, 6, 40) - reference), mp.mpf("1e-32"))
            z = mp.mpc("-1.7", "3.4")
            self.assertLess(abs(src.completed(z, 6, 40) - src.completed(1 - z, 6, 40)), mp.mpf("1e-32"))


if __name__ == "__main__":
    unittest.main()
