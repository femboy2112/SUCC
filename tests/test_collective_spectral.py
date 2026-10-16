"""Exact hostile controls for the collective spectral lane (stdlib only)."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from math import comb
import unittest

from observational_succ import collective_spectral as C


class PolarizationTests(unittest.TestCase):
    def test_signed_collective_detection(self):
        form = C.HermitianForm(((1, 2), (2, 1)))
        self.assertEqual(form.quadratic((1, 0)), 1)
        self.assertEqual(form.quadratic((0, 1)), 1)
        self.assertEqual(form.quadratic((1, 1)), 6)
        self.assertEqual(form.quadratic((1, -1)), -2)
        self.assertEqual(C.real_polarization(form.quadratic, (1, 0), (0, 1)), 2)

    def test_complex_linear_first_sign_and_blind_real_probes(self):
        form = C.HermitianForm(((1, C.Gaussian(0, 2)), (C.Gaussian(0, -2), 1)))
        self.assertEqual(C.real_polarization(form.quadratic, (1, 0), (0, 1)), 0)
        self.assertEqual(C.complex_polarization(form.quadratic, (1, 0), (0, 1)), C.Gaussian(0, 2))
        self.assertEqual(form.quadratic((1, C.Gaussian(0, -1))), -2)
        for a, b in product(range(-3, 4), repeat=2):
            self.assertEqual(form.quadratic((a, b)), a*a+b*b)

    def test_exhaustive_gaussian_rational_polarization(self):
        form = C.HermitianForm(((F(1, 3), C.Gaussian(F(2, 5), F(-3, 7))),
                                (C.Gaussian(F(2, 5), F(3, 7)), -F(4, 9))))
        points = tuple(product((C.Gaussian(), C.Gaussian(F(1, 2), F(1, 3)), C.Gaussian(-1, 2)), repeat=2))
        for x, y in product(points, repeat=2):
            self.assertEqual(C.complex_polarization(form.quadratic, x, y), form.pairing(x, y))

    def test_real_apparatus_does_not_supply_imaginary_superpositions(self):
        form = C.HermitianForm(((1, 2), (2, 1)))
        app = C.QuadraticApparatus(form, ((1, 1), (1, -1)))
        self.assertEqual(C.real_polarization(app.measure, (1, 0), (0, 1)), 2)
        with self.assertRaises(C.SpectralError):
            C.complex_polarization(app.measure, (1, 0), (0, 1))

    def test_nonhermitian_and_dimension_errors(self):
        for rows in ((), ((1, 2),), ((1, 2), (0, 1)), ((C.Gaussian(1, 1),),)):
            with self.assertRaises(C.SpectralError):
                C.HermitianForm(rows)
        with self.assertRaises(C.SpectralError):
            C.HermitianForm(((1,),)).quadratic((1, 0))
        with self.assertRaises(C.SpectralError):
            C.combine((1,), (1, 0))

    def test_inexact_inputs_rejected(self):
        for value in (True, 1.0, 1j, '1/2'):
            with self.assertRaises(C.SpectralError):
                C.Gaussian(value)
        with self.assertRaises(C.SpectralError):
            C.real_polarization(lambda _: 1.0, (1,), (1,))


class IntersectionTests(unittest.TestCase):
    def setUp(self):
        self.ctx = C.Coordinates('blob', 'commit', F(1, 2), ('P1', 'P2'),
                                 ('Gamma', 'contact', 'poles', 'prime2'), (F(1, 3), F(1, 5)), 'S0')
        self.a = C.Bound(self.ctx, C.Interval(-2, 3), 'a', frozenset({'source', 'implementation-a'}))
        self.b = C.Bound(self.ctx, C.Interval(-1, 2), 'b', frozenset({'source', 'implementation-b'}))

    def test_shared_source_not_independence(self):
        result = C.intersect_bounds((self.a, self.b))
        self.assertEqual(result['interval'], C.Interval(-1, 2))
        self.assertEqual(result['provenance_components'], (('a', 'b'),))
        self.assertFalse(result['independence_established'])

    def test_bridge_dependency_transitive_closure(self):
        a = replace(self.a, dependencies=frozenset({'x'}))
        b = replace(self.b, dependencies=frozenset({'y'}))
        bridge = replace(self.a, route='c', dependencies=frozenset({'x', 'y'}))
        self.assertEqual(C.intersect_bounds((a, b, bridge))['provenance_components'], (('a', 'b', 'c'),))

    def test_disjoint_labels_still_do_not_prove_independence(self):
        b = replace(self.b, dependencies=frozenset({'other-source'}))
        result = C.intersect_bounds((self.a, b))
        self.assertEqual(len(result['provenance_components']), 2)
        self.assertFalse(result['independence_established'])

    def test_every_source_coordinate_mismatch_rejected(self):
        mutations = dict(source_blob='fake', source_commit='wrong', radius=F(3, 4),
                         basis=('P2', 'P1'), channels=('Gamma', 'contact', 'poles'),
                         metric_diagonal=(F(1), F(1)), target='S-shift', convention='conjugate-first')
        for field, value in mutations.items():
            with self.subTest(field=field), self.assertRaises(C.SpectralError):
                C.intersect_bounds((self.a, replace(self.b, coordinates=replace(self.ctx, **{field: value}))))

    def test_empty_duplicate_and_inconsistent_bounds_rejected(self):
        for bounds in ((), (self.a, self.a), (self.a, replace(self.b, interval=C.Interval(4, 5)))):
            with self.assertRaises(C.SpectralError):
                C.intersect_bounds(bounds)

    def test_touching_bounds_allowed(self):
        result = C.intersect_bounds((self.a, replace(self.b, interval=C.Interval(3, 4))))
        self.assertEqual(result['interval'], C.Interval(3, 3))

    def test_bad_contracts(self):
        for kwargs in ({'radius': F()}, {'channels': ('Gamma', 'Gamma')}, {'basis': ('P1',)},
                       {'metric_diagonal': (F(1), F(-1))}, {'source_blob': ''}):
            with self.assertRaises(C.SpectralError):
                replace(self.ctx, **kwargs)
        with self.assertRaises(C.SpectralError):
            replace(self.a, dependencies=frozenset())
        with self.assertRaises(C.SpectralError):
            C.Interval(2, 1)


class WitnessDepthTests(unittest.TestCase):
    def test_exact_a_priori_degrees(self):
        for d, n in ((F(1, 10), 10), (F(1, 100), 109), (F(1, 1000), 1099)):
            result = C.negative_witness_budget(d)
            self.assertEqual(result['degree'], n)
            self.assertLessEqual(result['compression_error_upper'], d/4)
            self.assertLess(result['rational_quadratic_upper'], -d/2)
            self.assertLess(result['rational_quadratic_upper']+result['certification_error_allowance'], 0)
            self.assertFalse(result['density_rate_assumed'])

    def test_rounding_grid_error_bound(self):
        for d in (F(11, 40), F(1, 13), F(1, 10000)):
            b = C.negative_witness_budget(d)
            self.assertLessEqual(F(b['degree'], 2*b['coefficient_denominator']**2), b['rounding_L2_error_upper']**2)
            radicand = b['coefficient_denominator']**2*(2*b['degree']+1)
            cap = b['integer_numerator_absolute_bound']
            self.assertGreaterEqual((cap-1)**2, radicand)
            self.assertLess((cap-2)**2, radicand)
            base, exponent = b['candidate_count_power']
            self.assertEqual((base, exponent), (2*cap+1, 2*b['degree']))
            self.assertEqual(b['candidate_count_log2_strict_upper'], exponent*base.bit_length())

    def test_witness_budget_invalid_inputs(self):
        for d in (F(), -F(1), F(1), .01, True):
            with self.assertRaises(C.SpectralError):
                C.negative_witness_budget(d)
        for n in (0, -1, 1.0, True):
            with self.assertRaises(C.SpectralError):
                C.compression_error(n)

    def test_hidden_mode_has_fixed_short_but_decaying_full_margin(self):
        for n in (1, 8, 100):
            r = C.hidden_soft_mode(n)
            form = C.HermitianForm(((F(1, 2), r['b_m']), (r['b_m'], r['D_mm'])))
            c = r['witness_high_coefficient']
            self.assertEqual(form.quadratic((1, c)), -F(1, 2))
            self.assertEqual(-form.quadratic((1, c))/(1+c*c), r['unit_witness_negative_margin'])
            self.assertEqual(r['full_short'], -F(1, 2))
            self.assertEqual(r['visible_short'], F(1, 2))
            self.assertEqual(r['square_root_response_norm_squared'], 1)


class ProjectionCertificateTests(unittest.TestCase):
    def samples(self, polynomial, grid=32):
        return tuple((x, polynomial(x), polynomial(x)) for i in range(grid//2)
                     for x in (F(2*i+1, 2*grid),))

    def test_exact_cell_legendre_moments(self):
        for k in range(4):
            total = sum((C.legendre_cell_integral(k, F(i, 8)-F(1, 2), F(i+1, 8)-F(1, 2)) for i in range(8)), F())
            self.assertEqual(total, F(k == 0))

    def test_antisymmetric_correlation_against_independent_square_integrals(self):
        polys = ((F(1),), (F(), F(2)), (-F(1, 2), F(), F(6)),
                 (F(), -F(3), F(), F(20)), (F(3, 8), F(), -F(15), F(), F(70)))
        def monomial(power):
            return (F(1, 2)**(power+1)-(-F(1, 2))**(power+1))/(power+1)
        def moment(k, power):
            return sum((c*monomial(i+power) for i, c in enumerate(polys[k])), F())
        for j, k in product(range(1, 5), range(4)):
            psi = C.derivative_correlation_polynomial(j, k)
            if (j+k) % 2 == 0:
                self.assertEqual(psi, (F(),))
            for p in (1, 3, 5):
                square = sum((comb(p, a)*(-1)**a*moment(k, p-a)*moment(j, a)
                              for a in range(p+1)), F())
                line = sum((c/F(i+p+1) for i, c in enumerate(psi)), F())
                self.assertEqual(line, square)
            # Independent contact derivative sign(x-y): h_j=2 primitive(P_j).
            primitive = (F(),)+tuple(c/F(i+1) for i, c in enumerate(polys[j]))
            left_value = sum((c*(-F(1, 2))**i for i, c in enumerate(primitive)), F())
            contact = 2*sum((a*b*monomial(i+t) for i, a in enumerate(primitive)
                             for t, b in enumerate(polys[k])), F())-2*left_value*moment(k, 0)
            self.assertEqual(sum((c/F(i+1) for i, c in enumerate(psi)), F()), contact)

    def test_exact_moments_sharpen_but_conflicts_reject(self):
        col = C.projected_column_bound(2, self.samples(lambda x: 2*x), 32, 2)
        exact = (C.Interval(0, 0), C.Interval(F(1, 3), F(1, 3)), C.Interval(0, 0), C.Interval(0, 0))
        refined = C.refine_projected_column(col, exact)
        self.assertEqual(refined['removed_polynomial_energy_lower'], F(1, 3))
        self.assertLess(refined['projected_energy_upper'], col['projected_energy_upper'])
        with self.assertRaises(C.SpectralError):
            C.refine_projected_column(col, (C.Interval(1, 1),)+exact[1:])

    def test_constant_column_projection_exact(self):
        c = C.projected_column_bound(1, self.samples(lambda x: F(3)), 32, F())
        self.assertEqual(c['finite_J_energy_upper'], 9)
        self.assertEqual(c['removed_polynomial_energy_lower'], 9)
        self.assertEqual(c['projected_energy_upper'], 0)
        self.assertEqual(c['projection_moment_intervals'], ((F(3), F(3)), (F(), F()), (F(), F()), (F(), F())))

    def test_linear_column_certified_without_sampling_claim(self):
        c = C.projected_column_bound(2, self.samples(lambda x: 2*x), 32, 2)
        self.assertGreaterEqual(c['finite_J_energy_upper'], F(1, 3))
        self.assertGreater(c['removed_polynomial_energy_lower'], 0)
        self.assertLessEqual(c['removed_polynomial_energy_lower'], F(1, 3))
        self.assertGreaterEqual(c['projected_energy_upper'], 0)
        lo, hi = c['projection_moment_intervals'][1]
        self.assertLessEqual(lo, F(1, 3)); self.assertGreaterEqual(hi, F(1, 3))

    def test_cubic_polynomial_true_residual_is_included(self):
        # h(x)=P3(2x) is wholly removed; derivative sup is 12 on the interval.
        c = C.projected_column_bound(2, self.samples(lambda x: 20*x**3-3*x, 128), 128, 12)
        self.assertGreaterEqual(c['projected_energy_upper'], 0)
        self.assertLessEqual(c['removed_polynomial_energy_lower'], F(1, 7))
        lo, hi = c['projection_moment_intervals'][3]
        self.assertLessEqual(lo, F(1, 7)); self.assertGreaterEqual(hi, F(1, 7))

    def test_missing_or_wrong_cells_rejected(self):
        samples = self.samples(lambda x: F(1))
        for bad in (samples[:-1], tuple(reversed(samples)), ((F(), 1, 1),)+samples[1:]):
            with self.assertRaises(C.SpectralError):
                C.projected_column_bound(1, bad, 32, 0)
        with self.assertRaises(C.SpectralError):
            C.projected_column_bound(1, samples, 31, 0)

    def test_derivative_tail_remains_when_finite_part_vanishes(self):
        cols = [C.projected_column_bound(j, self.samples(lambda x: F()), 32, 0) for j in range(1, 5)]
        result = C.projected_response_caps(cols, F(1, 10), F(1, 5))
        self.assertEqual(result['odd']['R0_operator_upper_cap'], F(1, 20))
        with self.assertRaises(C.SpectralError):
            C.projected_response_caps(cols, -F(1), F(1, 5))

    def test_directed_square_root(self):
        for q in (F(), F(1, 9), F(2), F(123, 71)):
            s = C.sqrt_upper(q, 10000)
            self.assertGreaterEqual(s*s, q)
            if s:
                self.assertLess((s-F(1, 10000))**2, q)


if __name__ == '__main__':
    unittest.main()
