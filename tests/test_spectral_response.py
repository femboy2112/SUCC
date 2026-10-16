"""Exact finite controls and counterexamples; paper proofs are in the dossier."""
from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ import spectral_response as S
from observational_succ.recursive_operator_gluing import inverse, product as mm, transpose, psd


def add(a, b, sign=1):
    return tuple(tuple(x+sign*y for x, y in zip(r, s)) for r, s in zip(a, b))


def quadratic(a, x):
    return sum((x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x))), F())


class SpectralMeasureTests(unittest.TestCase):
    def setUp(self):
        self.d = (F(1, 16), F(1, 4), F(1))
        self.b = ((F(1, 4), F(-1, 2)), (F(1, 3), F(2, 3)), (F(-1, 5), F(1, 5)))
        self.measure = S.SpectralMeasure.from_diagonal(self.d, self.b)

    def test_response_matches_rotated_full_matrix_inverse(self):
        # A rational Householder basis changes the representation and mixes D.
        v = (1, 2, 2)
        q = tuple(tuple(F(int(i == j))-F(2*v[i]*v[j], 9) for j in range(3)) for i in range(3))
        diag = tuple(tuple(self.d[i] if i == j else F() for j in range(3)) for i in range(3))
        d, b = mm(mm(q, diag), transpose(q)), mm(q, self.b)
        for shift in (F(), F(1, 100), F(2, 3), F(10)):
            shifted = tuple(tuple(d[i][j]+shift*(i == j) for j in range(3)) for i in range(3))
            direct = mm(transpose(b), mm(inverse(shifted), b))
            self.assertEqual(direct, self.measure.response(shift))

    def test_scalar_quadratic_measure_is_sum_of_squared_couplings(self):
        for x in product((-2, 0, 1), repeat=2):
            expected = sum((sum((r[i]*x[i] for i in range(2)), F())**2/d
                            for d, r in zip(self.d, self.b)), F())
            self.assertEqual(quadratic(self.measure.response(), x), expected)

    def test_signed_off_diagonal_weights_are_retained(self):
        self.assertLess(self.measure.atoms[0][1][0][1], 0)
        self.assertTrue(psd(self.measure.atoms[0][1]))
        self.assertEqual(self.measure.atoms[0][1][0][1], -F(1, 8))

    def test_repeated_eigenvalues_and_unsorted_input(self):
        m = S.SpectralMeasure.from_diagonal((1, F(1, 2), 1), ((1, 2), (2, -1), (3, 1)))
        self.assertEqual(m.weak_mass(F(3, 4)), ((4, -2), (-2, 1)))
        self.assertEqual(m.moment(0), ((14, 3), (3, 6)))
        self.assertEqual(len(m.atoms), 3)

    def test_zero_atom_not_silently_pseudoinverted(self):
        m = S.SpectralMeasure.from_diagonal((0, 1), ((1,), (2,)))
        self.assertEqual(m.response(F(1, 2)), ((F(14, 3),),))
        self.assertEqual(m.zero_mass(), ((1,),))
        self.assertEqual(m.moment(0), ((5,),))
        for operation in (lambda: m.response(), lambda: m.inverse_tail(1),
                          lambda: m.shift_gap(1), lambda: m.completion_gap(1),
                          lambda: m.fractional_range_gram(1),
                          lambda: m.stieltjes_tail_parts(1),
                          lambda: m.weak_mass_bound(1, ((10,),), 1)):
            with self.assertRaises(S.SpectralResponseError):
                operation()

    def test_uncoupled_kernel_and_all_zero_measure_are_lawful(self):
        m = S.SpectralMeasure.from_diagonal((0, 2), ((0,), (2,)))
        self.assertEqual(m.response(), ((2,),))
        z = S.SpectralMeasure.from_diagonal((0,), ((0,),))
        self.assertEqual(z.response(), ((0,),))
        self.assertEqual(z.fractional_bounds(F(1, 2), 1, 1)['shift_upper'], ((0,),))

    def test_exact_stieltjes_identity_with_boundary_atom(self):
        for eps in (F(1, 32), F(1, 16), F(1, 4), F(3, 4), F(1), F(2)):
            boundary, integral = self.measure.stieltjes_tail_parts(eps)
            # Independent step-function integration, interval by interval.
            knots = sorted({d for d in self.d if d < eps}) + [eps]
            direct = ((F(), F()), (F(), F()))
            for a, b in zip(knots, knots[1:]):
                mass = self.measure.weak_mass(a)
                direct = add(direct, tuple(tuple(x*(1/a-1/b) for x in row) for row in mass))
            self.assertEqual(direct, integral)
            self.assertEqual(add(boundary, integral), self.measure.inverse_tail(eps))

    def test_shift_and_trial_gap_are_distinct_positive_matrices(self):
        for lam in (F(1, 16), F(1, 3), F(2)):
            delta, trial = self.measure.shift_gap(lam), self.measure.completion_gap(lam)
            self.assertEqual(delta, add(self.measure.response(), self.measure.response(lam), -1))
            self.assertTrue(psd(delta))
            self.assertTrue(psd(trial))
            self.assertTrue(psd(add(delta, trial, -1)))
            self.assertNotEqual(delta, trial)

    def test_completion_gap_matches_original_signed_block_energy(self):
        a = ((F(-2), F(1, 3)), (F(1, 3), F(1)))  # Whole G is not assumed PSD.
        for lam in (F(1, 16), F(1, 2), F(3)):
            s0 = add(a, self.measure.response(), -1)
            for x in product((-1, 1, 2), repeat=2):
                bx = [sum((r[i]*x[i] for i in range(2)), F()) for r in self.b]
                h = [-y/(d+lam) for d, y in zip(self.d, bx)]
                energy = quadratic(a, x)+sum((2*y*z+d*z*z for d, y, z in zip(self.d, bx, h)), F())
                self.assertEqual(energy-quadratic(s0, x), quadratic(self.measure.completion_gap(lam), x))

    def test_response_is_loewner_monotone_and_completely_monotone(self):
        values = [self.measure.response(F(j, 8)) for j in range(1, 8)]
        for order in range(1, 6):
            values = [add(a, b, -1) for a, b in zip(values, values[1:])]
            for delta in values:
                self.assertTrue(psd(delta), order)


class FractionalAndWeakBoundsTests(unittest.TestCase):
    def test_weak_mass_gate_checks_all_jumps_and_matrix_order(self):
        m = S.SpectralMeasure.from_diagonal((F(1, 4), F(1, 2), 1),
                                          ((F(1, 4), 0), (0, F(1, 2)), (F(1, 2), F(1, 2))))
        upper = m.weak_mass_bound(1, ((2, 0), (0, 2)), 1)
        self.assertTrue(psd(add(upper, m.inverse_tail(1), -1)))
        with self.assertRaises(S.SpectralResponseError):
            m.weak_mass_bound(1, ((F(1, 2), 0), (0, F(1, 2))), 1)

    def test_weak_mass_certificate_must_cover_intermediate_small_jump(self):
        # Endpoint F(1)<=1 is true but F(1/16)<=(1/16)^2 is false.
        m = S.SpectralMeasure(((F(1, 16), ((F(1, 2),),)),))
        self.assertLessEqual(m.weak_mass(1)[0][0], 1)
        with self.assertRaises(S.SpectralResponseError):
            m.weak_mass_bound(1, ((1,),), 1)

    def test_fractional_bounds_half_power_with_noncommuting_weights(self):
        m = S.SpectralMeasure.from_diagonal((F(1, 16), F(1, 4), 1),
                                          ((1, -1), (2, 1), (-1, 3)))
        # Rational squares keep half-power constants exactly representable.
        for lam in (F(1, 16), F(1, 4), F(4)):
            gram = m.fractional_range_gram(F(1, 2))
            maximum = S.scalar_filter_maximum(F(1, 2), lam, 1)
            upper = tuple(tuple(maximum*x for x in row) for row in gram)
            self.assertTrue(psd(add(upper, m.shift_gap(lam), -1)))
        bounds = m.fractional_bounds(F(1, 2), 4, F(1, 4))
        self.assertTrue(psd(add(bounds['tail_upper'], m.inverse_tail(F(1, 4)), -1)))
        # The order-two peak lam/3 need not have a rational square root;
        # that API refuses irrational constants, rather than issuing a certificate.
        with self.assertRaises(S.SpectralResponseError):
            m.fractional_bounds(F(1, 2), F(1, 16), F(1, 4))

    def test_integer_fractional_grams_and_bounds(self):
        m = S.slow_tail_prefix(4)
        for alpha in (1, 2, 3):
            for lam in (F(1, 16), F(1), F(10)):
                b = m.fractional_bounds(alpha, lam, F(1, 16))
                self.assertGreaterEqual(b['tail_upper'][0][0], m.inverse_tail(F(1, 16))[0][0])
                self.assertGreaterEqual(b['shift_upper'][0][0], m.shift_gap(lam)[0][0])
                self.assertGreaterEqual(b['completion_upper'][0][0], m.completion_gap(lam)[0][0])

    def test_sharp_scalar_constants_and_finite_support_cap(self):
        self.assertEqual(S.scalar_filter_maximum(F(1, 2), 1, 10), F(1, 2))
        self.assertEqual(S.scalar_filter_maximum(1, 1, 10, 2), F(1, 4))
        self.assertEqual(S.scalar_filter_maximum(1, 1, F(1, 2), 2), F(2, 9))
        self.assertEqual(S.scalar_filter_maximum(2, 1, 10), F(100, 11))
        self.assertEqual(S.scalar_filter_maximum(2, 1, 10, 2), F(100, 121))

    def test_single_atom_attains_response_and_completion_constants(self):
        m = S.SpectralMeasure.from_diagonal((1,), ((1,),))
        self.assertEqual(m.shift_gap(1)[0][0], S.scalar_filter_maximum(F(1, 2), 1, 2))
        self.assertEqual(m.completion_gap(1)[0][0], S.scalar_filter_maximum(1, 1, 2, 2))

    def test_rational_power_exact_or_rejected(self):
        self.assertEqual(S.rational_power(F(1, 16), -F(3, 2)), 64)
        self.assertEqual(S.rational_power(F(27, 8), F(2, 3)), F(9, 4))
        with self.assertRaises(S.SpectralResponseError):
            S.rational_power(2, F(1, 2))


class CounterexampleTests(unittest.TestCase):
    def test_slow_tail_prefix_inverse_weights_are_one_over_j_squared(self):
        for n in (1, 4, 16, 64):
            expected = sum((F(1, j*j) for j in range(1, n+1)), F())
            self.assertEqual(S.slow_tail_prefix(n).response(), ((expected,),))

    def test_infinite_enclosures_contain_larger_prefix_plus_its_tail(self):
        for shift in (F(1, 4), F(1, 4**12), F(1, 4**30)):
            small, large = S.slow_tail_enclosure(16, shift), S.slow_tail_enclosure(64, shift)
            for key in ('response', 'shift_gap', 'completion_gap'):
                self.assertLessEqual(small[key][0], large[key][0])
                self.assertGreaterEqual(small[key][1], large[key][1])

    def test_no_power_lower_bounds_at_dyadic_shifts(self):
        for n in (1, 2, 8, 16, 32):
            enclosure = S.slow_tail_enclosure(64, F(1, 4**n))
            self.assertGreaterEqual(enclosure['shift_gap'][0], F(1, 2*n))
            self.assertGreaterEqual(enclosure['completion_gap'][0], F(1, 4*n))

    def test_positive_moments_converge_while_fractional_range_grams_grow(self):
        small, large = S.slow_tail_prefix(8), S.slow_tail_prefix(32)
        for order in range(6):
            self.assertLessEqual(large.moment(order)[0][0], F(1, 4**(order+1)-1))
        self.assertGreater(large.fractional_range_gram(F(1, 2))[0][0],
                           1000*small.fractional_range_gram(F(1, 2))[0][0])

    def test_fixed_exact_moment_aliases_have_unbounded_inverse_family(self):
        for order in range(9):
            previous_base = None
            for scale in (4, 32, 4096):
                eps = F(1, (order+1)*scale)
                base, alternative = S.matched_moment_measures(order, eps)
                if previous_base is not None:
                    self.assertEqual(base, previous_base)
                previous_base = base
                for k in range(order+1):
                    self.assertEqual(base.moment(k), alternative.moment(k))
                self.assertTrue(all(w[0][0] > 0 for _, w in alternative.atoms))
                self.assertGreaterEqual(alternative.response()[0][0], 1/eps)
                self.assertNotEqual(base.response(), alternative.response())
                self.assertNotEqual(base.response(eps), alternative.response(eps))

    def test_tiny_perturbation_flips_short_and_has_original_negative_witness(self):
        for n in (1, 8, 32, 128):
            r = S.tiny_coupling_counterexample(n)
            self.assertEqual(r['R0'], 1)
            self.assertEqual(r['S0'], -F(1, 2))
            self.assertEqual(r['original_energy'], -F(1, 2))
            self.assertEqual(r['limit_S0'], F(1, 2))
            self.assertEqual(r['operator_perturbation_norm'], F(1, 2**n))
            self.assertEqual(r['response_at_shift_one'], F(1, 4**n+1))


class ContractTests(unittest.TestCase):
    def test_bad_atoms_and_shape_are_rejected(self):
        bad = [(), ((-1, ((1,),)),), ((1, ((-1,),)),),
               ((1, ((1, 2), (0, 1))),), ((1, ((1, 2), (2, 1))),),
               ((1, ((1,),)), (2, ((1, 0), (0, 1)))),
               ((1, ((True,),)),), ((1.0, ((1,),)),), ((1, ((1.0,),)),),
               tuple((1, ((1,),)) for _ in range(129))]
        for atoms in bad:
            with self.subTest(atoms=str(atoms)[:80]):
                with self.assertRaises(S.SpectralResponseError):
                    S.SpectralMeasure(atoms)

    def test_bad_diagonal_inputs_are_rejected(self):
        for d, b in (((), ()), ((1,), ((1,), (2,))), ((1, 2), ((1,), (1, 2))),
                     ((True,), ((1,),)), ((1,), ((False,),)), ((1,), ((),))):
            with self.assertRaises(S.SpectralResponseError):
                S.SpectralMeasure.from_diagonal(d, b)

    def test_bad_domains_and_budgets_are_rejected(self):
        m = S.slow_tail_prefix(1)
        for action in (lambda: m.response(-1), lambda: m.response(True),
                       lambda: m.shift_gap(0), lambda: m.inverse_tail(0),
                       lambda: m.moment(-1), lambda: m.moment(True),
                       lambda: m.fractional_range_gram(0),
                       lambda: m.weak_mass_bound(0, ((1,),), 1),
                       lambda: m.weak_mass_bound(1, ((1, 0), (0, 1)), 1),
                       lambda: S.slow_tail_prefix(129),
                       lambda: S.slow_tail_enclosure(True, 1),
                       lambda: S.matched_moment_measures(2, F(1, 3)),
                       lambda: S.matched_moment_measures(17, F(1, 100)),
                       lambda: S.scalar_filter_maximum(1, 1, 1, 3),
                       lambda: S.rational_power(2, 33),
                       lambda: S.tiny_coupling_counterexample(0)):
            with self.assertRaises(S.SpectralResponseError):
                action()


if __name__ == '__main__':
    unittest.main()
