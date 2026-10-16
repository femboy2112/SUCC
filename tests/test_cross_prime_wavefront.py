import unittest
from fractions import Fraction as F

from observational_succ import cross_prime_wavefront as C
from observational_succ import suzuki_legendre_source as L
from observational_succ import source_weil_hierarchy as S
from observational_succ.tate_suzuki_shorting import rational_psd


class CrossPrimeWavefrontTests(unittest.TestCase):
    def test_genuine_transition(self):
        self.assertEqual(C.active_wavefronts(F(1, 2)), ((2, 2),))
        self.assertEqual(C.active_wavefronts(F(9, 16)), ((2, 2), (3, 3)))
        self.assertEqual(C.active_wavefronts(F(11, 16)), ((2, 2), (3, 3)))
        self.assertEqual(C.active_wavefronts(F(7, 10)), ((2, 2), (3, 3), (4, 2)))

    def test_inactive_and_fake_composite(self):
        self.assertEqual(C.hinge_entry(1, 1, F(1, 2), 3), S.iv(0))
        with self.assertRaises(C.WavefrontTransportError):
            C.hinge_entry(1, 1, F(1), 6)

    def test_prime_square_parent(self):
        a = F(7, 10)
        poly = L.prime_hinge_integral_polynomial(1, 1, a)
        base = L.polynomial_interval(poly, S.log_iv(4))*S.log_iv(2)*S.sqrt_inverse(4)
        self.assertEqual(C.hinge_entry(1, 1, a, 4), base)
        wrong = L.polynomial_interval(poly, S.log_iv(4))*S.log_iv(4)*S.sqrt_inverse(4)
        self.assertTrue(base.hi < wrong.lo or wrong.hi < base.lo)

    def test_first_window_source_agreement(self):
        for i, j in ((1, 1), (1, 3), (2, 4), (2, 2)):
            got = C.source_partial_entry(i, j, F(1, 2), 8)
            old = L.authentic_full_low_entry(i, j, F(1, 2), 8)
            self.assertLessEqual(got.lo, old.hi)
            self.assertLessEqual(old.lo, got.hi)

    def test_parity_and_symmetry_beyond_prime2(self):
        r = C.transported_low_bracket(F(9, 16), 8)
        for key in ('lower_form', 'upper_form'):
            m = r[key]
            self.assertEqual(m, tuple(zip(*m)))
            self.assertTrue(all(m[i][j] == 0 for i in range(4) for j in range(4) if (i-j) % 2))
        self.assertFalse(r['high_coercivity_transferred'])
        self.assertFalse(r['Schur_sign_proved'])

    def test_loewner_bracket_is_ordered(self):
        r = C.transported_low_bracket(F(7, 10), 8)
        gap = tuple(tuple(r['upper_form'][i][j]-r['lower_form'][i][j] for j in range(4)) for i in range(4))
        self.assertTrue(rational_psd(gap))

    def test_unitary_normalization(self):
        a = F(9, 16)
        r = C.transported_low_bracket(a, 8)
        z = C.source_partial_entry(1, 3, a, 8)/(2*a)
        self.assertEqual(r['partial_entry_intervals'][0][2], (z.lo, z.hi))
        self.assertEqual(r['reference_metric_diagonal'], (F(1, 3), F(1, 5), F(1, 7), F(1, 9)))
        self.assertEqual(C.primitive_transport_scale(a)['inverse_Neumann'], F(81, 64))

    def test_continuity_bound(self):
        a, b = F(1, 2), F(9, 16)
        self.assertEqual(C.radius_continuity_bound(a, a), 0)
        self.assertEqual(C.radius_continuity_bound(a, b), C.radius_continuity_bound(b, a))
        self.assertGreater(C.radius_continuity_bound(a, b), 0)

    def test_product_formula_menu_obstruction(self):
        r = C.product_formula_observation(F(7, 12), (2, 3))
        self.assertEqual(r['partial_norm_product'], 7)
        self.assertEqual(r['full_norm_product'], 1)
        self.assertEqual(r['missing_nontrivial_places'], (7,))
        self.assertFalse(r['spectral_tail_bound_obtained'])

    def test_fixed_rational_complete_menu(self):
        r = C.product_formula_observation(F(-7, 12), (2, 3, 7))
        self.assertEqual(r['partial_norm_product'], 1)
        self.assertEqual(r['missing_nontrivial_places'], ())
        self.assertIsInstance(r['additive_reciprocity_integer_defect'], int)

    def test_invalid_domains(self):
        for a in (True, 0, F(3, 2), 0.5):
            with self.assertRaises(ValueError):
                C.active_wavefronts(a)
        with self.assertRaises(ValueError):
            C.product_formula_observation(0, (2,))
        with self.assertRaises(ValueError):
            C.source_partial_entry(1, 2, F(1, 2), 0)


if __name__ == '__main__':
    unittest.main()
