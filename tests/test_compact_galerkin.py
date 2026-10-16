"""Exact finite controls; universal analytic proofs live in the dossier."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import unittest

from observational_succ import compact_galerkin as C


def multiply(a, x):
    return tuple(sum((v*w for v, w in zip(row, x)), F()) for row in a)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F())


def inverse_two(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if det <= 0:
        raise ValueError('positive block determinant required')
    return ((a[1][1]/det, -a[0][1]/det),
            (-a[1][0]/det, a[0][0]/det))


class CompactProjectionControls(unittest.TestCase):
    def test_noncompact_identity_has_exact_unit_obstruction(self):
        for n in (1, 2, 10, 1000):
            r = C.diagonal_compression_control(n, 0)
            self.assertEqual(r['operator_norm_error'], 1)
            self.assertFalse(r['compact_iff_exponent_positive'])
            self.assertEqual(r['witness_index'], n+1)

    def test_compact_diagonal_tail_uses_first_omitted_coordinate(self):
        for p in (1, 2, 5):
            for n in (1, 3, 12):
                r = C.diagonal_compression_control(n, p)
                tail = [F(1, j**p) for j in range(n+1, n+30)]
                self.assertEqual(r['operator_norm_error'], max(tail))
                self.assertEqual(r['norm_I_minus_projection'], 1)

    def test_weighted_legendre_tail_equality_on_first_omitted_mode(self):
        for n in range(9):
            r = C.polynomial_legendre_tail([0]*(n+1)+[1], n)
            self.assertEqual(r['tail_squared'], r['tail_squared_upper'])
            self.assertEqual(r['tail_squared'], F(1, 2*n+3))

    def test_weighted_legendre_sum_independently_integrates_mixed_modes(self):
        for n in (0, 2, 4, 8):
            cs = tuple(F((-1)**j, j+1) for j in range(11))
            r = C.polynomial_legendre_tail(cs, n)
            self.assertEqual(r['weighted_derivative_squared'], r['spectral_sum'])
            self.assertLessEqual(r['tail_squared'], r['tail_squared_upper'])

    def test_wrong_first_omitted_eigenvalue_is_detected(self):
        # Replacing (N+1)(N+2) by a larger next weight is a false bound.
        r = C.polynomial_legendre_tail((0, 0, 0, 1), 2)
        self.assertGreater(r['tail_squared'], r['weighted_derivative_squared']/20)

    def test_constant_has_zero_derivative_and_zero_tail(self):
        r = C.polynomial_legendre_tail((F(7, 3),), 0)
        self.assertEqual(r['tail_squared'], 0)
        self.assertEqual(r['weighted_derivative_squared'], 0)

    def test_only_exact_valid_parameters_admitted(self):
        for bad in (True, 3.0, 0, -1):
            with self.assertRaises(C.CompactGalerkinError):
                C.source_legendre_bound(bad)
        for bad in (True, 0.5, '1/2'):
            with self.assertRaises(C.CompactGalerkinError):
                C.polynomial_legendre_tail((bad,), 0)
        with self.assertRaises(C.CompactGalerkinError):
            C.polynomial_legendre_tail((), 1)


class SourceCompressionControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bound = C.source_legendre_bound(20, 64)

    def test_authentic_source_and_sharp_budget_replayed(self):
        r = self.bound
        self.assertEqual(r['source']['source_git_blob'],
                         '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertLess(r['gprime_L1_strict_upper'], F(11, 40))
        self.assertLess(r['gprime_L2_squared_strict_upper'], F(4, 25))
        self.assertEqual(r['first_omitted_eigenvalue'], 21*22)

    def test_live_source_hashes_match_previous_round_receipt(self):
        root = Path(__file__).resolve().parents[1]
        old = json.loads((root/'research/2026-10-15/proof_teeth_receipts/'
                         'schur-declared-environment.json').read_text())
        for name, value in C.source_snapshot()['sha256'].items():
            # New adapter was in own_code_sha256 in the inherited receipt.
            previous = old['source']['sha256'].get(name, old['own_code_sha256'].get(name))
            self.assertEqual(value, previous, name)
            self.assertEqual(value, sha256((root/name).read_bytes()).hexdigest())

    def test_error_budget_decreases_and_keeps_gamma_tail_separate(self):
        a, b = self.bound, C.source_legendre_bound(40, 64)
        self.assertLess(b['operator_error_squared_strict_upper'],
                        a['operator_error_squared_strict_upper'])
        self.assertEqual(a['positive_gamma_tail_operator_upper'],
                         F(2, 257**2)+F(16, 257**3))
        self.assertEqual(a['compressed_GJ_total_error_strict_upper'],
                         a['operator_error_rational_strict_upper']+
                         a['positive_gamma_tail_operator_upper'])
        self.assertEqual(C.source_legendre_bound(20)['positive_gamma_tail_operator_upper'], 0)

    def test_no_inverse_or_sign_promotion_from_compactness(self):
        self.assertFalse(self.bound['inverse_or_zero_shift_error_certified'])
        self.assertEqual(self.bound['original_S0_sign'], 'OPEN')
        self.assertFalse(self.bound['RH_PROVED'])
        self.assertTrue(self.bound['requires_exact_compression_or_separate_matrix_entry_error'])


class ZeroShiftControls(unittest.TestCase):
    def test_norm_small_perturbation_has_fixed_short_sign_change(self):
        for m in (1, 2, 7, 64):
            r = C.zero_shift_discontinuity(m)
            g = ((F(1, 2), F(1, m)), (F(1, m), F(1, m*m)))
            v = r['negative_vector_low_high']
            self.assertEqual(dot(v, multiply(g, v)), r['negative_energy'])
            self.assertEqual(r['response_zero_shift'], 1)
            self.assertLess(r['short'], 0)
            self.assertGreater(r['limit_short'], 0)
            self.assertFalse(r['authentic_weil_source'])

    def test_regularized_responses_converge_at_each_fixed_positive_shift(self):
        a = C.zero_shift_discontinuity(4, F(1, 100))
        b = C.zero_shift_discontinuity(40, F(1, 100))
        self.assertGreater(a['positive_shift_response'], b['positive_shift_response'])
        self.assertEqual(a['response_zero_shift'], b['response_zero_shift'])
        for shift in (0, -1, 0.1, True):
            with self.assertRaises(C.CompactGalerkinError):
                C.zero_shift_discontinuity(4, shift)

    def test_regularized_perturbation_bound_on_independent_scalar_models(self):
        for d, e, b, c, lam in ((1, 2, 3, 4, F(1, 7)),
                               (F(1, 100), F(1, 10), F(1, 4), 0, F(1, 5))):
            bound = C.positive_shift_response_error(abs(d-e), abs(b-c), abs(b), abs(c), lam)
            actual = abs(F(b*b)/(d+lam)-F(c*c)/(e+lam))
            self.assertLessEqual(actual, bound['conditional_response_error_upper'])
            self.assertIsNone(bound['zero_shift_bound'])


class RelativeGraphControls(unittest.TestCase):
    def test_independent_two_by_two_algebra_confirms_every_block(self):
        for j in range(1, 12):
            r = C.graph_failure_block(j)
            d, k, b, u = r['D'], r['K_scalar'], r['b'], r['partial_Galerkin_u']
            dk = ((d[0][0]-k, d[0][1]), (d[1][0], d[1][1]-k))
            self.assertGreater(dk[0][0], 0)
            self.assertEqual(dk[0][0]*dk[1][1]-dk[0][1]*dk[1][0], r['det_D_minus_K'])
            self.assertGreater(r['det_D_minus_K'], 0)
            residual = tuple(a-c for a, c in zip(b, multiply(d, u)))
            self.assertEqual(residual, r['partial_residual'])
            self.assertEqual(residual[0], 0)
            self.assertEqual(dot(residual, residual)/k, F(1, 2))
            exact = multiply(inverse_two(d), b)
            self.assertEqual(exact, r['exact_response_vector'])
            self.assertEqual(dot(b, exact), r['block_response'])
            self.assertEqual(2*dot(b, u)-dot(u, multiply(d, u)), r['partial_response'])
            self.assertEqual(sum((v*v for row in d for v in row), F())/k,
                             r['relative_map_HS_squared'])

    def test_infinite_stage_formulas_match_independent_finite_sum_and_exact_tail(self):
        for j in range(1, 8):
            for complete in (False, True):
                r = C.graph_failure_stage(j, complete)
                response = F()
                for i in range(1, j+1):
                    block = C.graph_failure_block(i)
                    if i < j or complete:
                        response += dot(block['b'], multiply(inverse_two(block['D']), block['b']))
                    else:
                        response += dot(block['b'], block['partial_Galerkin_u'])
                future_relative = sum((2*F(1, 4**i) for i in range(j+1, j+9)), F())
                future_relative += F(2, 3*4**(j+8))
                self.assertEqual(response, r['Galerkin_response'])
                self.assertEqual(future_relative+(0 if complete else F(1, 2)),
                                 r['full_K_relative_residual_squared'])
                self.assertEqual(r['R0']-response, r['true_D_relative_residual_squared'])

    def test_residual_failure_survives_compact_hilbert_schmidt_relative_map(self):
        a, b = C.graph_failure_block(1), C.graph_failure_block(8)
        self.assertLess(b['relative_map_HS_squared'], a['relative_map_HS_squared'])
        self.assertEqual(a['partial_K_residual_squared'], b['partial_K_residual_squared'])
        partial = C.graph_failure_stage(8)
        complete = C.graph_failure_stage(8, True)
        self.assertGreater(partial['full_K_relative_residual_squared'], F(1, 2))
        self.assertLess(complete['full_K_relative_residual_squared'], F(1, 10000))
        self.assertLess(partial['true_D_relative_residual_squared'], F(1, 10000))

    def test_negative_sufficient_lower_is_not_negative_original_short(self):
        for j in range(1, 10):
            r = C.graph_failure_stage(j)
            self.assertLess(r['sufficient_lower'], 0)
            self.assertGreater(r['true_short'], 0)
            self.assertGreater(r['upper_short'], r['true_short'])

    def test_no_bool_or_float_alias_for_graph_family(self):
        for bad in (True, 1.0, 0, 129):
            with self.assertRaises(C.CompactGalerkinError):
                C.graph_failure_block(bad)
        with self.assertRaises(C.CompactGalerkinError):
            C.graph_failure_stage(1, 1)


class RangeGapAndGammaControls(unittest.TestCase):
    def test_clamped_source_constant_and_exact_polynomial_controls(self):
        # C1=t²(1-t)²/24; its fourth derivative is identically one.
        r = C.clamped_polynomial_control((0, 0, F(1, 24), -F(1, 12), F(1, 24)))
        self.assertEqual(r['high_u_equals_fourth_derivative'], (F(1),))
        self.assertEqual(r['mean_second_derivative'], 0)
        self.assertEqual(r['first_moment_second_derivative'], 0)
        self.assertEqual(r['K_relative_residual_squared'], 1+r['ddf_squared'])
        self.assertGreater(r['true_S0'], 0)
        self.assertLessEqual(r['sufficient_lower'], -F(4, 5))

    def test_clamped_range_gap_survives_signed_and_higher_degree_trials(self):
        for scale in (-100, -1, 0, F(1, 7), 1, 10):
            for shift in (0, 1, 2, 5):
                f = (0,)*shift+(0, 0, scale, -2*scale, scale)
                r = C.clamped_polynomial_control(f)
                self.assertGreaterEqual(r['K_relative_residual_squared'], 1)
                self.assertLessEqual(r['sufficient_lower'], -F(4, 5))

    def test_dirichlet_poisson_maximizer_is_not_a_clamped_trial(self):
        with self.assertRaises(C.CompactGalerkinError):
            C.clamped_polynomial_control((0, F(1, 2), -F(1, 2)))
        # Direct energy of f*=t(1-t)/2 is 1/12, but f*' has nonzero endpoints.
        self.assertEqual(2*(F(1, 4)-F(1, 6))-(F(1, 4)-F(1, 2)+F(1, 3)), F(1, 12))

    def test_gamma_tail_controls_independent_finite_sum_and_exact_integral_tail(self):
        for j in (1, 4, 64):
            r = C.gamma_residual_gram_upper(((1,),), ((1,),), j)
            eta = r['derivative_tail_L1_upper']
            d = 4*j+1
            self.assertEqual(eta, F(8, d*d)+F(2, d))
            partial = sum((F(8, (4*k+1)**2) for k in range(j, j+50)), F())
            self.assertLess(partial+F(2, 4*(j+50)+1), eta)
            self.assertEqual(r['upper'], ((2+2*eta*eta,),))

    def test_matrix_gram_upper_retains_cross_terms(self):
        # A=[[1,2],[-1,3]], E=eta*I. W=I bounds ||E x||²/eta².
        cj = ((F(2), -F(1)), (-F(1), F(13)))
        r = C.gamma_residual_gram_upper(cj, ((1, 0), (0, 1)), 3, F(1, 3))
        eta = r['derivative_tail_L1_upper']
        a = ((1+eta, F(2)), (-F(1), 3+eta))
        for x in ((F(1), F(0)), (F(0), F(1)), (F(2), -F(3)), (-F(5), F(7))):
            self.assertLessEqual(dot(multiply(a, x), multiply(a, x)),
                                 dot(x, multiply(r['upper'], x)))
        self.assertFalse(r['source_identification_inferred_from_PSD'])

    def test_wrong_gram_and_zero_epsilon_rejected(self):
        for cj, w, eps in ((((1,),), ((1,),), 0),
                           (((-1,),), ((1,),), 1),
                           (((1, 0), (0, 1)), ((1,),), 1)):
            with self.assertRaises(ValueError):
                C.gamma_residual_gram_upper(cj, w, 3, eps)


if __name__ == '__main__':
    unittest.main()
