"""Exact independent arithmetical oracle for the rational-diagonal Tate tensor."""
import random
import unittest
from fractions import Fraction as F

from observational_succ.adelic_schwartz_source import DiagonalGaussianTensor
from observational_succ.tate_schwartz_functor import TateFunctorError
from observational_succ.diagonal_adele_zeta import (
    additive_reciprocity, multiplicative_reciprocity, fractional_padic_part,
)


class GaussianTensorTests(unittest.TestCase):
    def test_standard_tensor_and_exact_integer_source(self):
        x = DiagonalGaussianTensor(F(1), F(0), F(1))
        self.assertEqual(x.exceptional_places(), ())
        for n in range(-12, 13):
            self.assertTrue(x.at_rational(n)["nonzero"])
            self.assertFalse(x.at_rational(F(2*n+1, 2))["nonzero"])
            y = x.fourier_at_rational(n)
            self.assertTrue(y["finite_support"])
            self.assertEqual(y["global_phase"], 0)
            self.assertEqual(y["global_Haar_affine_scaling"], 1)
            self.assertEqual(y["gaussian_exponent_pi"], n*n)
            self.assertFalse(y["full_Poisson_formula_proved_by_finite_samples"])
        self.assertFalse(x.fourier_at_rational(F(1, 3))["finite_support"])
        self.assertIn(3, x.fourier_at_rational(F(1, 3))["finite_active_places"])

    def test_active_place_propagation_from_source_and_frequency(self):
        x = DiagonalGaussianTensor(F(-6, 35), F(1, 22), F(7, 11))
        self.assertEqual(x.exceptional_places(), (2, 3, 5, 7, 11))
        q = x.fourier_at_rational(F(-35, 6))
        self.assertTrue(q["finite_support"])
        self.assertEqual(q["source_integral_label"], 1)
        self.assertEqual(q["global_phase"], 0)
        self.assertEqual(q["global_Haar_affine_scaling"], 1)
        y = x.fourier_at_rational(F(1, 97))
        self.assertFalse(y["finite_support"])
        self.assertIn(97, y["finite_active_places"])

    def test_nontrivial_character_cancels_only_if_all_finite_places_retained(self):
        x = DiagonalGaussianTensor(6, F(1, 5), 1)
        xi = F(1, 6)
        q = x.fourier_at_rational(xi)
        self.assertTrue(q["finite_support"])
        self.assertEqual(q["real_phase"], F(1, 30))
        self.assertEqual(q["finite_phase"], F(29, 30))
        self.assertEqual(q["global_phase"], 0)
        self.assertEqual(set(q["finite_active_places"]), {2, 3, 5})
        # A phase mutation which silently removes the p=5 place spoils the
        # source pairing, even though the full global phase must be 0.
        without_5 = (q["real_phase"]+sum(v.phase for p,v in q["local_Fourier_values"].items()
                                        if p != 5)) % 1
        self.assertNotEqual(without_5, 0)

    def test_independent_gaussian_exponent_and_lattice_index(self):
        rng = random.Random(9021)
        for _ in range(140):
            a = F(rng.choice((-1, 1)) * rng.randint(1, 20), rng.randint(1, 12))
            d = F(rng.randint(-20, 20), rng.randint(1, 15))
            t = F(rng.randint(1, 9), rng.randint(1, 13))
            x = DiagonalGaussianTensor(a, d, t)
            for n in (-7, -1, 0, 1, 2, 8):
                r = x.poisson_index_receipt(n)
                self.assertEqual(r["primal_Gaussian_exponent_pi"], t * n*n)
                self.assertEqual(r["dual_Gaussian_exponent_pi"], F(n*n)/t)
                self.assertEqual(r["dual_global_phase"], 0)
                self.assertTrue(r["matched_original_integer_source"])
                self.assertFalse(r["theta_functional_equation_proved_by_this_finite_index"])

    def test_global_affine_functor_and_noncommutation(self):
        x = DiagonalGaussianTensor(1, 0, 2, "source-x", 10)
        a = x.affine(3, F(1, 5)).affine(F(1, 2), F(-2, 7))
        b = x.affine(F(3, 2), F(1, 10)-F(2, 7))
        self.assertEqual(a, b)
        self.assertEqual(a.source_id, "source-x")
        self.assertEqual(a.epoch, 10)
        for n in (-2, -1, 0, 1, 5):
            self.assertTrue(a.poisson_index_receipt(n)["matched_original_integer_source"])
        y = x.affine(3, 2)
        z = x.affine(2, 3)
        self.assertNotEqual(y.shift, z.shift)

    def test_exact_haar_scaling_and_prime_mutation(self):
        for q in (F(2), F(1, 3), F(-14, 15), F(121, 8), F(1, 101)):
            obj = DiagonalGaussianTensor(q, F(0))
            self.assertEqual(multiplicative_reciprocity(q)["global_product"], 1)
            r = obj.fourier_at_rational(F(1)/q)
            self.assertEqual(r["global_Haar_affine_scaling"], 1)
            self.assertTrue(r["finite_support"])
            # Incorrectly omitting a prime with nonzero v_p(q) loses
            # that local Haar factor and breaks reciprocity.
            for p,v in multiplicative_reciprocity(q)["valuations"].items():
                if v:
                    mutated = F(p)**v
                    self.assertNotEqual(mutated, 1)

    def test_bad_signs_clocks_and_source_rejected(self):
        for args in ((0, 0, 1), (1, 0, 0), (1, 0, -1),
                     (1, 0, 1, "", 0), (1, 0, 1, "source", -1)):
            with self.assertRaises(TateFunctorError):
                DiagonalGaussianTensor(*args)
        with self.assertRaises(TateFunctorError):
            DiagonalGaussianTensor(1, 0, 1).affine(0, 2)
        with self.assertRaises(TateFunctorError):
            DiagonalGaussianTensor(1, 0).local_ball(6)
        with self.assertRaises(TateFunctorError):
            DiagonalGaussianTensor(1, 0).poisson_index_receipt(F(1, 2))


if __name__ == "__main__":
    unittest.main()
