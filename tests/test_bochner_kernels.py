"""Tests for observational_succ.bochner_kernels (Rigidity Forge, Part VI).

Every assertion is exact (sympy Rational / symbolic). No float is used as a
certificate.
"""
import unittest

import sympy as sp

from observational_succ.bochner_kernels import (
    BochnerKernelError,
    characteristic_coefficients,
    four_way_spectral_report,
    is_positive_definite_exact,
    is_psd_exact,
    kernel_gram,
    leading_principal_minors,
    levy_khintchine_benchmarks,
    levy_khintchine_verify,
    one_minus_cos_feature,
    one_minus_cos_gram_from_circle_points,
    one_minus_cos_positive_benchmark,
    schoenberg_contract,
    schoenberg_polarization_check,
    summary,
    t4_negative_benchmark,
    verify_one_minus_cos_identity,
)


class TestExactPSDPrimitive(unittest.TestCase):
    def test_identity_is_psd_and_pd(self):
        M = sp.Matrix([[2, 0], [0, 2]])
        self.assertTrue(is_psd_exact(M))
        self.assertTrue(is_positive_definite_exact(M))

    def test_indefinite_rejected(self):
        M = sp.Matrix([[2, -14], [-14, 2]])
        self.assertFalse(is_psd_exact(M))
        self.assertFalse(is_positive_definite_exact(M))

    def test_psd_but_not_pd(self):
        # eigenvalues 0 and 2: PSD, not PD.
        M = sp.Matrix([[1, 1], [1, 1]])
        self.assertTrue(is_psd_exact(M))
        self.assertFalse(is_positive_definite_exact(M))

    def test_sylvester_gotcha_is_caught_by_psd_test(self):
        # Leading principal minors are 0 and 0 -- Sylvester-leading cannot reject,
        # but the matrix is indefinite (eigenvalues 0, -1). is_psd_exact must say NO.
        M = sp.Matrix([[0, 0], [0, -1]])
        self.assertEqual([sp.Integer(0), sp.Integer(0)], leading_principal_minors(M))
        self.assertFalse(is_psd_exact(M))

    def test_charpoly_coeffs(self):
        M = sp.Matrix([[2, -14], [-14, 2]])
        self.assertEqual([sp.Integer(1), sp.Integer(-4), sp.Integer(-192)],
                         characteristic_coefficients(M))

    def test_nonsymmetric_rejected(self):
        with self.assertRaises(BochnerKernelError):
            is_psd_exact(sp.Matrix([[1, 2], [3, 1]]))

    def test_float_is_not_a_certificate(self):
        with self.assertRaises(BochnerKernelError):
            kernel_gram(lambda t: t ** 2, [0.5, 1.0])

    def test_surd_matrix_psd_decided_exactly(self):
        # Genuine surd entries sqrt(2); eigenvalues 2 +/- sqrt(2), both > 0, so
        # PSD, and the sign of every charpoly coefficient is still decided exactly.
        M = sp.Matrix([[2, sp.sqrt(2)], [sp.sqrt(2), 2]])
        self.assertFalse(all(v.is_rational for v in M))
        self.assertTrue(is_psd_exact(M))

    def test_surd_matrix_indefinite_decided_exactly(self):
        # eigenvalues 1 +/- sqrt(2): 1 - sqrt(2) < 0, so NOT PSD, decided exactly.
        M = sp.Matrix([[1, sp.sqrt(2)], [sp.sqrt(2), 1]])
        self.assertFalse(is_psd_exact(M))


class TestNegativeBenchmark(unittest.TestCase):
    def test_t4_gram_det_minus_192_not_psd(self):
        r = t4_negative_benchmark()
        self.assertEqual(sp.Matrix([[2, -14], [-14, 2]]), r["gram"])
        self.assertEqual(sp.Integer(-192), r["determinant"])
        self.assertFalse(r["is_psd"])
        self.assertFalse(r["conditionally_negative_definite"])
        self.assertEqual("REFUTED", r["status"])
        self.assertFalse(r["RH_proved"])

    def test_t4_gram_via_kernel_gram(self):
        G = kernel_gram(lambda t: t ** 4, [-1, 1])
        self.assertEqual(sp.Matrix([[2, -14], [-14, 2]]), G)


class TestPositiveBenchmark(unittest.TestCase):
    def test_feature_identity_holds_for_all_s_t(self):
        self.assertTrue(verify_one_minus_cos_identity())

    def test_feature_map_shape(self):
        phi = one_minus_cos_feature(sp.pi / 3)
        # cos(pi/3)=1/2, sin(pi/3)=sqrt(3)/2
        self.assertEqual(sp.Rational(1, 2), sp.simplify(phi[0]))
        self.assertEqual(sp.sqrt(3) / 2, sp.simplify(phi[1]))

    def test_rational_circle_point_gram_is_psd(self):
        pts = [(1, 0), (sp.Rational(3, 5), sp.Rational(4, 5)),
               (sp.Rational(5, 13), sp.Rational(12, 13))]
        G = one_minus_cos_gram_from_circle_points(pts)
        # fully rational Gram
        self.assertTrue(all(v.is_rational for v in G))
        self.assertTrue(is_psd_exact(G))

    def test_gram_equals_feature_gram(self):
        pts = [(1, 0), (sp.Rational(3, 5), sp.Rational(4, 5)),
               (sp.Rational(-7, 25), sp.Rational(24, 25))]
        G = one_minus_cos_gram_from_circle_points(pts)
        Phi = sp.Matrix([[1 - a, b] for a, b in pts])
        self.assertEqual(sp.zeros(3, 3), sp.simplify(G - Phi * Phi.T))

    def test_non_circle_point_rejected(self):
        with self.assertRaises(BochnerKernelError):
            one_minus_cos_gram_from_circle_points([(1, 1)])

    def test_benchmark_rollup_all_psd(self):
        r = one_minus_cos_positive_benchmark()
        self.assertTrue(r["symbolic_identity_K_equals_inner_product"])
        self.assertTrue(r["global_psd"])
        self.assertTrue(r["conditionally_negative_definite"])
        self.assertEqual("PROVED LOCAL", r["status"])
        for g in r["rational_point_grams"]:
            self.assertTrue(g["is_psd"])
            self.assertTrue(g["equals_feature_gram"])
        self.assertFalse(r["RH_proved"])


class TestLevyKhintchine(unittest.TestCase):
    def test_one_minus_cos_has_delta_1(self):
        self.assertTrue(levy_khintchine_verify(lambda x: 1 - sp.cos(x), 0, [(1, 1)]))

    def test_one_minus_cos_scaled(self):
        # 1 - cos(2x) has Levy measure delta_2
        self.assertTrue(levy_khintchine_verify(lambda x: 1 - sp.cos(2 * x), 0, [(2, 1)]))

    def test_t_squared_is_gaussian_term(self):
        self.assertTrue(levy_khintchine_verify(lambda x: x ** 2, 1, []))

    def test_negative_mass_rejected(self):
        self.assertFalse(levy_khintchine_verify(lambda x: 1 - sp.cos(x), 0, [(1, -1)]))

    def test_negative_c_rejected(self):
        self.assertFalse(levy_khintchine_verify(lambda x: -(x ** 2), -1, []))

    def test_benchmarks(self):
        lk = levy_khintchine_benchmarks()
        self.assertTrue(lk["one_minus_cos"]["positive_measure"])
        self.assertTrue(lk["t_squared"]["positive_measure"])
        self.assertFalse(lk["t_fourth"]["positive_measure"])
        self.assertEqual(sp.Integer(-192), lk["t_fourth"]["finite_witness_det"])


class TestSchoenbergPolarization(unittest.TestCase):
    def test_identity_holds_general_coeffs(self):
        r = schoenberg_polarization_check(lambda t: t ** 2, [0, 1, 2], [3, -1, 5])
        self.assertTrue(r["identity_holds"])

    def test_zero_sum_hyperplane_reduction(self):
        # coeffs sum to 0: quadratic form = - sum c_i c_j Psi(t_i - t_j)
        r = schoenberg_polarization_check(lambda t: t ** 4, [-1, 0, 1], [1, -2, 1])
        self.assertTrue(r["identity_holds"])
        self.assertTrue(r["on_zero_sum_hyperplane"])
        self.assertTrue(r["equals_minus_diff_form_on_hyperplane"])


class TestFourWayDistinction(unittest.TestCase):
    def test_one_minus_cos_passes_i_ii_iii_fails_iv(self):
        r = four_way_spectral_report("1 - cos t")
        self.assertTrue(r["i_finite_psd"])
        self.assertTrue(r["ii_global_pd_kernel"])
        self.assertTrue(r["iii_positive_spectral_measure"])
        self.assertIsNone(r["iv_source_identified_signed_weil"])
        self.assertTrue(r["negative_control"])
        self.assertFalse(r["RH_proved"])
        self.assertFalse(r["Weil_PSD_proved"])
        self.assertFalse(r["source_authentic"])

    def test_t4_fails_all_four(self):
        r = four_way_spectral_report("t^4")
        self.assertFalse(r["i_finite_psd"])
        self.assertFalse(r["ii_global_pd_kernel"])
        self.assertFalse(r["iii_positive_spectral_measure"])
        self.assertIsNone(r["iv_source_identified_signed_weil"])
        self.assertFalse(r["RH_proved"])

    def test_iv_never_identified(self):
        for name in ("1 - cos t", "t^4"):
            self.assertIsNone(
                four_way_spectral_report(name)["iv_source_identified_signed_weil"]
            )


class TestContractAndFirewall(unittest.TestCase):
    def test_contract_is_classical_and_not_source_authentic(self):
        c = schoenberg_contract()
        self.assertEqual("CLASSICAL", c.status)
        self.assertFalse(c.source_authentic)
        self.assertTrue(any("signed Weil" in o for o in c.open_obligations))
        self.assertTrue(any("RH remains OPEN" in o for o in c.open_obligations))

    def test_summary_runs_and_keeps_rh_open(self):
        s = summary()
        self.assertFalse(s["negative_benchmark_t4"]["RH_proved"])
        self.assertFalse(s["positive_benchmark_1_minus_cos"]["RH_proved"])
        self.assertFalse(s["four_way_1_minus_cos"]["RH_proved"])
        self.assertIsNone(s["four_way_1_minus_cos"]["iv_source_identified_signed_weil"])


if __name__ == "__main__":
    unittest.main()
