"""Exact regressions and hostile controls for the recursive-carrier dossier.

These finite tests check instruments; analytic universal claims have paper
proofs.  Raw moments, direct word products, and native source histories serve
as independent computational representations.  No test asserts normality.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
import unittest

from observational_succ import recursive_carrier_triangle as t
from observational_succ import oily_macaroni_transfer as old
from observational_succ.succ_internal_matrix_walk import authentic_r as native_r


HOLDOUT_A = (F(1, 17), F(23, 11), F(1001, 7), F(8*37-7),
             F(8*61-7), F(8*97-7))


def direct_moments(a, depth):
    coefficients = ((4, 0), (-2, 3), (-1, 4), (-1, 5))
    normalizer = sum((F(c)/(a+d) for c, d in coefficients), F())
    return [factorial(k)*sum((F(c)/(a+d)**(k+1) for c, d in coefficients), F())
            /normalizer for k in range(depth+1)]


def moment_cumulants(moments):
    cumulants = [F()]
    for k in range(1, len(moments)):
        cumulants.append(moments[k]-sum((comb(k-1, j-1)*cumulants[j]*moments[k-j]
                                        for j in range(1, k)), F()))
    return cumulants


def matrix_product(a, b):
    return tuple(tuple(sum((x*y for x, y in zip(row, column)), F())
                       for column in zip(*b)) for row in a)


class AuthenticSourceTests(unittest.TestCase):
    def test_source_authentication_beyond_initial_grid(self):
        for n in (1, 2, 3, 37, 61, 97, 1001):
            self.assertEqual(t.source_factorization(8*n-7), native_r(n))
        self.assertEqual(t.source_factorization(1), F(47, 15))

    def test_atomic_transform_and_integer_convolution_roots(self):
        for a, s in product(HOLDOUT_A, (F(), F(1, 13), F(7, 5), F(8), F(19))):
            normalizer = old.r_at_a(a+s)/old.r_at_a(a)
            self.assertEqual(t.atomic_laplace(a, s), normalizer)
            self.assertEqual(t.atomic_laplace(a, s)**5,
                             t.atomic_laplace(a, s)**2*t.atomic_laplace(a, s)**3)
            # Independent normalized tilt of the fivefold convolution transform.
            z = F(11, 7)
            self.assertEqual((old.r_at_a(a+s+z)/old.r_at_a(a))**5/normalizer**5,
                             t.atomic_laplace(a+s, z)**5)

    def test_all_cumulants_against_independent_moment_recursion(self):
        for a in HOLDOUT_A:
            independent = moment_cumulants(direct_moments(a, 12))
            for k in range(1, 13):
                self.assertEqual(t.source_cumulant(a, k), independent[k])
                lower, upper = t.cumulant_bounds(a, k)
                self.assertLess(lower, independent[k])
                self.assertLess(independent[k], upper)

    def test_source_time_update_keeps_every_original_signed_pole(self):
        for n in (1, 2, 17, 37, 61, 97):
            self.assertEqual(t.tilt_normalizer(8*n-7, 8), native_r(n+1)/native_r(n))

    def test_complete_factorial_interaction_signs(self):
        for a in HOLDOUT_A:
            for order in range(1, 7):
                steps = tuple((F(1, 13), F(7, 5), F(8), F(19))[j % 4]
                              for j in range(order))
                ratio = t.interaction_ratio(a, steps)
                self.assertGreater(ratio, 1) if order % 2 == 0 else self.assertLess(ratio, 1)

    def test_zero_direction_is_an_exact_null(self):
        for order in range(1, 7):
            self.assertEqual(t.interaction_ratio(F(23, 11), (0,)+(8,)*(order-1)), 1)

    def test_triangle_cocycle_all_parenthesizations(self):
        for a, s, u in product(HOLDOUT_A, (F(1, 13), F(8)), (F(7, 5), F(19))):
            v = F(11, 7)
            c = lambda x, y: t.interaction_ratio(a, (x, y))
            self.assertEqual(c(s, u)*c(s+u, v), c(u, v)*c(s, u+v))
            self.assertEqual(t.tilt_normalizer(a, s+u),
                             t.tilt_normalizer(a, s)*t.tilt_normalizer(a+s, u))

    def test_exact_pair_and_cubic_original_clock_receipts(self):
        self.assertEqual(t.interaction_ratio(1, (8, 8)), F(414839061, 52528300))
        self.assertEqual(t.interaction_ratio(1, (8, 8, 8)),
                         F(61527533661959200, 322441778977512831))

    def test_pair_bounds_against_direct_source_ratios(self):
        for a, s, u in product(HOLDOUT_A, (F(1, 13), F(8)), (F(7, 5), F(19))):
            lower, upper = t.pair_ratio_bounds(a, s, u)
            actual = old.r_at_a(a+s+u)*old.r_at_a(a)/(old.r_at_a(a+s)*old.r_at_a(a+u))
            self.assertLess(lower, actual)
            self.assertLess(actual, upper)

    def test_linear_gauge_cancels_but_cubic_does_not(self):
        # An exact multiplicative linear gauge g(a)=2^a on integer clocks.
        def gauged(a):
            return old.r_at_a(a)*2**a
        pair = gauged(17)*gauged(1)/gauged(9)**2
        self.assertEqual(pair, t.interaction_ratio(1, (8, 8)))
        self.assertNotEqual(t.interaction_ratio(1, (8, 8, 8)), 1)


class GeometryAndTransportTests(unittest.TestCase):
    def test_overlap_square_and_strict_squeezes(self):
        for a, b in product(HOLDOUT_A, repeat=2):
            actual = old.r_at_a((a+b)/2)**2/(old.r_at_a(a)*old.r_at_a(b))
            self.assertEqual(actual, t.overlap_square(a, b))
            lower, upper = t.overlap_square_bounds(a, b)
            if a == b:
                self.assertEqual((actual, lower, upper), (F(1), F(1), F(1)))
            else:
                self.assertLess(lower, actual)
                self.assertLess(actual, upper)
            self.assertGreaterEqual(actual, (1-t.overlap_deficit_bound(a, b))**2)

    def test_cube_root_boundaries_without_float_rounding(self):
        for j in (0, 1, 2, 3, 11, 97, 10**6):
            for n in {max(0, j**3-1), j**3, j**3+1}:
                c = t.integer_cuberoot(n)
                self.assertLessEqual(c**3, n)
                self.assertGreater((c+1)**3, n)

    def test_uniform_block_budget_controls_every_exact_overlap(self):
        for horizon, size in ((1, 1), (27, 3), (343, 7), (1000, 13)):
            manual, blocks = F(), 0
            for start in range(1, horizon+1, size):
                stop = min(horizon, start+size-1)
                endpoint = t.overlap_deficit_bound(8*start-7, 8*stop-7)
                for n in range(start, stop+1):
                    # Nonnegative lower bound, so squaring is sound.
                    self.assertGreaterEqual(t.overlap_square(8*start-7, 8*n-7), (1-endpoint)**2)
                manual += (stop-start+1)*endpoint
                blocks += 1
            report = t.block_transport_budget(horizon, size)
            self.assertEqual(manual/horizon, report['absolute_mean_error_upper'])
            self.assertLessEqual(manual/horizon, report['simple_upper'])
            self.assertEqual(blocks, report['blocks'])

    def test_cubic_blocks_cover_all_times_and_have_exact_budget(self):
        for n in (1, 2, 7, 8, 9, 26, 27, 28, 343, 1000, 4096):
            report = t.cubic_transport_budget(n)
            indices, budget = [], F()
            for j in range(report['blocks']):
                start, stop = 1+j**3, min(n, (j+1)**3)
                indices.extend(range(start, stop+1))
                deficit = (stop-start+1)*t.overlap_deficit_bound(8*start-7, 8*stop-7)
                if j:
                    self.assertLess(deficit, F(27, 4))
                else:
                    self.assertEqual(deficit, 0)
                budget += deficit
            self.assertEqual(indices, list(range(1, n+1)))
            self.assertEqual(budget/n, report['absolute_mean_error_upper'])
            self.assertLessEqual(budget/n, report['simple_upper'])
            self.assertEqual(report['discarded'], 0)

    def test_cubic_transport_polynomial_positive_certificate(self):
        for j in range(1, 40):
            left = 3*(2*j*j+3*j+3)**2-4*(3*j*j+3*j+1)*(j+1)**2
            self.assertEqual(left, 23*j*j+34*j+23)
            self.assertGreater(left, 0)

    def test_better_transport_does_not_become_a_fourier_estimate(self):
        n = 4096
        report = t.cubic_transport_budget(n)
        previous = old.multiscale_hilbert_transport_budget(n)
        self.assertLess(report['absolute_mean_error_upper'], previous['absolute_mean_error_upper'])
        self.assertLess(report['blocks'], n//16)
        self.assertFalse(report['signed_cancellation_proved'])
        # Choosing z_n=1 gives A_N=1 for every horizon and satisfies all
        # phase-independent carrier hypotheses, irrespective of this saving.
        self.assertEqual(sum(F(1) for _ in range(n))/n, 1)


class RecursivePathTests(unittest.TestCase):
    def test_normalized_transfer_composes_with_retained_mass(self):
        mu = (F(1, 2), F(1, 2))
        a = ((F(1, 2), F(1, 2)), (F(0), F(1, 2)))
        b = ((F(1, 2), F(0)), (F(1, 2), F(1, 2)))
        first, z1 = t.posterior_transport(mu, a)
        final, z2 = t.posterior_transport(first, b)
        direct, total = t.posterior_transport(mu, matrix_product(a, b))
        self.assertEqual(final, direct)
        self.assertEqual(total, z1*z2)
        self.assertEqual((direct, total), ((F(3, 5), F(2, 5)), F(5, 8)))
        reverse, reverse_total = t.posterior_transport(mu, matrix_product(b, a))
        self.assertEqual(total, reverse_total)
        self.assertEqual(reverse, (F(2, 5), F(3, 5)))
        self.assertNotEqual(direct, reverse)

    def test_stokes_for_three_independent_probability_laws(self):
        laws = (t.polya_left, t.exponential_left,
                lambda l, r: t.harmonic_left(l, r, length=9))
        for law in laws:
            for length in range(8):
                for letters in product('LR', repeat=length):
                    word = ''.join(letters)
                    canonical = 'L'*word.count('L')+'R'*word.count('R')
                    ratio = t.word_probability(word, law)/t.word_probability(canonical, law)
                    self.assertEqual(ratio, t.word_sheet_ratio(word, law))

    def test_flat_reinforcement_can_have_nonzero_reset_interaction(self):
        for left, right in product(range(5), repeat=2):
            self.assertEqual(t.diamond_ratio(left, right, t.polya_left), 1)
        self.assertEqual(t.word_probability('LL', t.polya_left), F(1, 3))
        self.assertEqual(t.word_probability('L', t.polya_left)**2, F(1, 4))

    def test_field_curvature_recovers_inherited_three_quarters(self):
        self.assertEqual(t.diamond_ratio(1, 0, t.harmonic_left), F(3, 4))
        self.assertEqual(t.word_probability('LLR', t.harmonic_left)
                         / t.word_probability('LRL', t.harmonic_left), F(3, 4))

    def test_nonflat_exponential_feedback_has_coherent_infinite_atom(self):
        self.assertEqual(t.diamond_ratio(1, 0, t.exponential_left), F(4, 5))
        self.assertEqual(t.all_left_atom_lower_bound(3), F(1, 5))
        for horizon in (3, 7, 19, 61):
            self.assertGreater(t.word_probability('L'*horizon, t.exponential_left), F(1, 5))
        # Exact ensemble cancellation of last-letter phase, despite that atom.
        for horizon in range(1, 9):
            signed = total = F()
            for letters in product('LR', repeat=horizon):
                word = ''.join(letters)
                p = t.word_probability(word, t.exponential_left)
                total += p
                signed += p*(1 if word[-1] == 'L' else -1)
            self.assertEqual(total, 1)
            self.assertEqual(signed, 0)

    def test_original_affine_phase_rectangle_is_exactly_flat(self):
        for horizon in (1, 7, 19, 37):
            original = [native_r(n) for n in range(1, horizon+1)]
            f = [F(1, 8*n-7) for n in range(1, horizon+1)]
            g = [F(-1, 8*n-3) for n in range(1, horizon+1)]
            self.assertEqual(t.affine_phase_rectangle(original, f, g, F(7, 5), F(-3, 11)),
                             (F(),)*(horizon+1))
            direct = [F()]
            for forcing in original:
                direct.append(16*direct[-1]+forcing)
            self.assertEqual(tuple(direct), t.authentic_history(horizon))


class FailClosedInputsAndMutationTests(unittest.TestCase):
    def test_domain_and_instrument_budget_fail_closed(self):
        for bad in (True, 1.0, '1', 0, -1):
            with self.assertRaises(ValueError): t.source_factorization(bad)
        for bad in (-1, True, F(1, 2)):
            with self.assertRaises(ValueError): t.integer_cuberoot(bad)
        with self.assertRaises(ValueError): t.interaction_ratio(1, ())
        with self.assertRaises(ValueError): t.interaction_ratio(1, (1,)*13)
        with self.assertRaises(ValueError): t.tilt_normalizer(1, -1)
        with self.assertRaises(ValueError): t.block_transport_budget(5, 6)
        with self.assertRaises(ValueError): t.word_probability('LX', t.polya_left)
        with self.assertRaises(ValueError): t.harmonic_left(3, 0)
        with self.assertRaises(ValueError): t.diamond_ratio(0, 0, lambda l, r: F(1))
        with self.assertRaises(ValueError): t.affine_phase_rectangle([1], [], [1])

    def test_zero_evidence_has_no_normalized_posterior(self):
        with self.assertRaises(ValueError): t.posterior_transport((F(1),), ((F(0),),))
        with self.assertRaises(ValueError): t.posterior_transport((F(1, 2),), ((F(1),),))
        with self.assertRaises(ValueError): t.posterior_transport((F(1),), ((-1,),))

    def test_false_models_have_explicit_separating_witnesses(self):
        authentic = native_r(1)
        wrong_pole = F(4)-F(1, 4)-F(1, 5)-F(1, 6)  # -2 changed to -1
        self.assertNotEqual(authentic, wrong_pole)
        self.assertNotEqual(t.tilt_normalizer(1, 16), t.tilt_normalizer(1, 8)**2)
        self.assertNotEqual(t.interaction_ratio(1, (8, 8, 8)), 1)
        self.assertNotEqual(t.diamond_ratio(1, 0, t.exponential_left), 1)
        self.assertNotEqual(t.posterior_transport((F(1, 2), F(1, 2)), ((1, 1), (0, 1)))[0],
                            (F(1, 2), F(1)))  # omitted normalization


if __name__ == '__main__':
    unittest.main()
