"""Exact specimens and mutation controls; paper proofs carry all quantifiers."""
from fractions import Fraction as Q
from math import gcd
import unittest

from observational_succ.classical_haar_clock import (
    PrimeHaarClock, condition, haar_inner, multiply_observable, pullback, succ_observable,
)
from observational_succ.dynamic_fourier_tower import lift_character, sum_fibers
from observational_succ.finite_fourier_carrier import CyclotomicElement as C, exact_dft
from observational_succ.finite_quotient_retract import FiniteQuotientRetract
from observational_succ.pontryagin_source_duality import RationalCircleCharacter
from observational_succ.profinite_hilbert import (
    HaarCylinder, ProfiniteHilbertError, conjugate, finite_commutation_witness,
    norm_obstruction, profinite_hilbert_probe,
)


def scalar_values(cylinder):
    if any(len(z.polynomial) != 1 for z in cylinder.values):
        raise AssertionError("Expected real rational specimen")
    return tuple(z.polynomial[0] for z in cylinder.values)


class ProfiniteHilbertTests(unittest.TestCase):
    def test_haar_isometry_adjoint_and_counting_mutant(self):
        for n, m in ((1, 3), (2, 6), (3, 12), (4, 12), (5, 10)):
            with self.subTest(n=n, m=m):
                f = HaarCylinder(n, tuple(Q(x-2, 3) for x in range(n)))
                g = HaarCylinder(m, tuple(Q((5*x) % 7-3, 2) for x in range(m)))
                self.assertEqual(f.norm_squared().polynomial, f.refine(m).norm_squared().polynomial)
                self.assertEqual(f.refine(m).inner(g), f.inner(g.condition(n)))
                self.assertTrue(f.refine(m).condition(n).equivalent(f))
                p = g.project(n)
                self.assertTrue(p.project(n).equivalent(p))
                # Explicit residual checks orthogonality and Pythagoras.
                r = HaarCylinder(m, tuple(a + b.scale(-1) for a, b in zip(g.values, p.values)))
                self.assertEqual(p.inner(r).polynomial, (Q(0),))
                self.assertEqual(g.norm_squared(), p.norm_squared() + r.norm_squared())
                raw_low = sum(v*v for v in scalar_values(f))
                raw_high = sum(v*v for v in scalar_values(f.refine(m)))
                self.assertEqual(raw_high, (m//n)*raw_low)
                self.assertNotEqual(raw_high, raw_low)

    def test_existing_prime_clocks_and_both_source_charts(self):
        for p, r in ((2, 1), (2, 2), (3, 1), (5, 1)):
            for chart in ("n_minus_one", "one_minus_n"):
                low, high = PrimeHaarClock(p, r, chart), PrimeHaarClock(p, r+1, chart)
                f = tuple(Q(x-1, 3) for x in range(low.size))
                g = tuple(Q((3*x) % 7-2, 5) for x in range(high.size))
                a, b = HaarCylinder(low.size, f), HaarCylinder(high.size, g)
                self.assertEqual(scalar_values(a.refine(high.size)), pullback(low, high, f))
                self.assertEqual(scalar_values(b.condition(low.size)), condition(high, low, g))
                self.assertEqual(b.norm_squared().polynomial, (haar_inner(high, g, g),))
                for m in (1, 2, 3, 6):
                    self.assertEqual(scalar_values(b.source_multiply(m, chart)),
                                     multiply_observable(high, g, m))
                self.assertEqual(scalar_values(b.source_successor(3, chart)),
                                 succ_observable(high, g, 3))

    def test_source_affine_offset_cannot_be_silently_dropped(self):
        delta = HaarCylinder(4, (0, 1, 0, 0))
        self.assertEqual(scalar_values(delta.source_multiply(2)), (Q(1), Q(0), Q(1), Q(0)))
        self.assertEqual(scalar_values(delta.multiply(2)), (Q(0),)*4)
        for chart in ("n_minus_one", "one_minus_n"):
            self.assertTrue(delta.source_multiply(2, chart).source_successor(1, chart).equivalent(
                delta.source_successor(2, chart).source_multiply(2, chart)))

    def test_coherent_tower_and_incomparable_projection_intersection(self):
        g = HaarCylinder(24, tuple(Q(x % 7-3, 2) for x in range(24)))
        self.assertTrue(g.condition(12).condition(3).equivalent(g.condition(3)))
        f = HaarCylinder(3, (1, -2, 4))
        self.assertTrue(f.refine(6).refine(24).equivalent(f.refine(24)))
        for n, m in ((4, 6), (3, 8), (2, 6), (1, 8)):
            self.assertTrue(g.project(n).project(m).equivalent(g.project(gcd(n, m))))
        self.assertTrue(f.refine(3).equivalent(f))
        self.assertTrue(f.condition(3).equivalent(f))

    def test_complex_sesquilinear_and_coefficient_field_survives_averaging(self):
        zeta = C.root(3, 1)
        f = HaarCylinder(6, (zeta,)*6)
        a = f.condition(2)
        self.assertEqual(a.field, 6)
        self.assertTrue(a.equivalent(HaarCylinder(1, (zeta,))))
        one = HaarCylinder(1, (1,))
        self.assertEqual(f.inner(one), lift_character(zeta, 6))
        self.assertEqual(one.inner(f), conjugate(f.inner(one)))
        self.assertEqual(f.norm_squared().polynomial, (Q(1),))
        self.assertTrue(HaarCylinder.from_fourier(a.fourier()).equivalent(a))

    def test_fourier_inversion_parseval_and_wrong_sign_mutation(self):
        for n in (1, 2, 3, 4, 6, 8, 9, 12):
            f = HaarCylinder(n, tuple(Q((7*x) % 5-2, 3) for x in range(n)))
            spectrum = f.fourier()
            self.assertTrue(HaarCylinder.from_fourier(spectrum).equivalent(f))
            energy = C.scalar(f.field, 0)
            for c in spectrum:
                energy = energy + c*conjugate(c)
            self.assertEqual(energy, f.norm_squared())
        zeta = C.root(5, 1)
        mixed = HaarCylinder(2, (C.scalar(5, 1) + zeta, zeta.scale(2)))
        mixed_spectrum = mixed.fourier()
        self.assertTrue(HaarCylinder.from_fourier(mixed_spectrum).equivalent(mixed))
        self.assertEqual(mixed.norm_squared(), sum(
            (z*conjugate(z) for z in mixed_spectrum), C.scalar(10, 0)))
        char = HaarCylinder.character(RationalCircleCharacter(Q(1, 3)))
        coefficients = char.fourier()
        self.assertEqual([z.polynomial for z in coefficients], [(Q(0),), (Q(1),), (Q(0),)])
        # Unmodified PLUS-phase analysis would put this character at -1/3.
        plus_at_one = C.scalar(3, 0)
        for x, value in enumerate(char.values):
            plus_at_one = plus_at_one + value*C.root(3, x)
        self.assertNotEqual(plus_at_one.scale(Q(1, 3)), coefficients[1])

    def test_fourier_naturality_and_counting_normalization_bridge(self):
        for n, m in ((2, 6), (3, 6), (3, 12), (4, 12), (5, 10)):
            f = HaarCylinder(n, tuple(Q(x-2, 3) for x in range(n)))
            sf, lifted = f.fourier(), f.refine(m).fourier()
            k = m//n
            for b in range(m):
                want = lift_character(sf[b//k], m) if b % k == 0 else C.scalar(m, 0)
                self.assertEqual(lifted[b], want)
            g = HaarCylinder(m, tuple(Q(x % 5-2, 3) for x in range(m)))
            fine, coarse = g.fourier(), g.condition(n).fourier()
            self.assertEqual(coarse, tuple(fine[k*a] for a in range(n)))
            raw = sum_fibers(scalar_values(g), n)
            self.assertEqual(scalar_values(g.condition(n)), tuple(x/k for x in raw))
            self.assertNotEqual(raw, scalar_values(g.condition(n)))
            dft = exact_dft(scalar_values(f))
            self.assertEqual(sf, tuple(dft[-a % n].scale(Q(1, n)) for a in range(n)))
            self.assertEqual(scalar_values(g.project(n)), FiniteQuotientRetract(m, n).project(scalar_values(g)))

    def test_character_labels_lift_and_wrong_label_is_detected(self):
        char = RationalCircleCharacter(Q(1, 3), "source", 9)
        low, high = HaarCylinder.character(char), HaarCylinder.character(char, 12)
        self.assertTrue(low.refine(12).equivalent(high))
        wrong = HaarCylinder.character(RationalCircleCharacter(Q(1, 12), "source", 9))
        self.assertFalse(high.equivalent(wrong))
        self.assertEqual(char.on_finite_clock(3).lift(12).label, 4)

    def test_translation_commutes_on_basis_and_has_correct_phase(self):
        for n, m in ((1, 4), (2, 6), (3, 12)):
            for j in range(m):
                f = HaarCylinder(m, tuple(int(x == j) for x in range(m)))
                for t in (-3, 0, 1, 5):
                    self.assertTrue(f.translate(t).condition(n).equivalent(f.condition(n).translate(t)))
        chi = HaarCylinder.character(RationalCircleCharacter(Q(1, 6)))
        moved = chi.translate(2).fourier()
        self.assertEqual(moved[1], C.root(6, 2))
        self.assertEqual(sum(z.polynomial != (Q(0),) for z in moved), 1)

    def test_exact_multiplier_commutation_criterion_with_nonunit_positive_control(self):
        for n, m in ((1, 4), (2, 4), (2, 6), (3, 6), (3, 9), (4, 12)):
            for multiplier in range(1, 7):
                for offset in (-1, 0, 1):
                    expected = gcd(multiplier, m//n) == 1
                    observed = True
                    # Exhaust all coordinate vectors: an independent finite matrix check.
                    for j in range(m):
                        f = HaarCylinder(m, tuple(int(x == j) for x in range(m)))
                        observed &= f.multiply(multiplier, offset).condition(n).equivalent(
                            f.condition(n).multiply(multiplier, offset))
                    self.assertEqual(observed, expected)
                    receipt = finite_commutation_witness(m, n, multiplier, offset)
                    self.assertEqual(receipt['commutes_for_all_vectors_by_PH_06'], expected)
        positive = finite_commutation_witness(6, 2, 2, 1)
        self.assertTrue(positive['commutes_for_all_vectors_by_PH_06'])
        bad = finite_commutation_witness(4, 2, 2, 1)
        self.assertEqual(bad['average_after_multiply'], (Q(1), Q(0)))
        self.assertEqual(bad['multiply_after_average'], (Q(1, 2), Q(1, 2)))

    def test_nonunit_pullback_still_intertwines_and_norm_fiber_identity(self):
        for n, m in ((2, 4), (2, 6), (3, 9)):
            f = HaarCylinder(n, tuple(range(n)))
            g = HaarCylinder(m, tuple(Q(x-2, 3) for x in range(m)))
            for multiplier in (1, 2, 3, 6):
                self.assertTrue(f.multiply(multiplier, 1).refine(m).equivalent(
                    f.refine(m).multiply(multiplier, 1)))
                image = {(multiplier*x+1) % m for x in range(m)}
                masked_energy = sum(scalar_values(g)[x]**2 for x in image)/m
                self.assertEqual(g.multiply(multiplier, 1).norm_squared().polynomial,
                                 (gcd(multiplier, m)*masked_energy,))

    def test_global_nonunit_character_counterexample(self):
        for n, multiplier in ((1, 2), (2, 2), (3, 2), (4, 3), (5, 2)):
            f = HaarCylinder.character(RationalCircleCharacter(Q(1, n*multiplier)))
            left = f.multiply(multiplier, multiplier-1).project(n)
            right = f.project(n).multiply(multiplier, multiplier-1)
            self.assertEqual(left.norm_squared().polynomial, (Q(1),))
            self.assertEqual(right.norm_squared().polynomial, (Q(0),))

    def test_strong_vs_norm_and_noncofinal_tower_controls(self):
        fixed = HaarCylinder.character(RationalCircleCharacter(Q(1, 6)))
        for n in (6, 12, 24):
            self.assertTrue(fixed.project(n).equivalent(fixed))
        for n in (1, 2, 3, 6, 12):
            self.assertEqual(norm_obstruction(n)['error_norm_squared'], Q(1))
        other_prime = HaarCylinder.character(RationalCircleCharacter(Q(1, 3)))
        for n in (2, 4, 8):
            self.assertEqual(other_prime.project(n).norm_squared().polynomial, (Q(0),))

    def test_compatible_evaluation_cone_has_unbounded_norm_witness_family(self):
        # These are specimens of PH-04's paper family, not a finite proof of divergence.
        for n in (1, 2, 4, 8, 16):
            delta = HaarCylinder(n, (1,) + (0,)*(n-1))
            self.assertEqual(delta.norm_squared().polynomial, (Q(1, n),))
            self.assertEqual(scalar_values(delta)[0], 1)
            self.assertEqual(scalar_values(delta.refine(2*n))[0], 1)
            self.assertEqual(Q(1) / delta.norm_squared().polynomial[0], n)

    def test_source_and_exactness_guards(self):
        for n, values in ((True, (1,)), (0, ()), (101, (1,)*101), (2, (1,)),
                          (2, (True, 1)), (2, (1.0, 1)), (2, (1j, 1))):
            with self.assertRaises(ProfiniteHilbertError):
                HaarCylinder(n, values)
        for source, epoch in ((" ", 0), ("s", -1), ("s", True)):
            with self.assertRaises(ProfiniteHilbertError):
                HaarCylinder(1, (1,), source, epoch)
        a = HaarCylinder(2, (1, 0), "s", 7)
        for other in (HaarCylinder(2, (1, 0), "other", 7), HaarCylinder(2, (1, 0), "s", 8)):
            with self.assertRaises(ProfiniteHilbertError):
                a.inner(other)
            with self.assertRaises(ProfiniteHilbertError):
                a.equivalent(other)
        for operation in (lambda: a.refine(3), lambda: a.condition(3), lambda: a.refine(102),
                          lambda: a.translate(True), lambda: a.multiply(0), lambda: a.multiply(1.5),
                          lambda: a.multiply(2, True),
                          lambda: HaarCylinder(11, (C.root(13, 1),)*11)):
            with self.assertRaises(ProfiniteHilbertError):
                operation()

    def test_probe_boundaries_and_counterexamples(self):
        receipt = profinite_hilbert_probe()
        self.assertFalse(receipt['universal_theorems_proved_by_finite_tests'])
        self.assertFalse(receipt['physical_source_authenticated'])
        self.assertFalse(receipt['RH_proved'])
        self.assertEqual(receipt['chi_one_third_energy_after_levels_2_4_8'], [Q(0)]*3)


if __name__ == '__main__':
    unittest.main()
