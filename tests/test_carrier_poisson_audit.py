"""Exact receipts for the independent carrier/Poisson audit.

These check finite identities and explicit mutants, not infinite Poisson
summation, effective access to every adele, or RH positivity.
"""
import unittest
from fractions import Fraction as F
from math import lcm

from observational_succ.adelic_poisson_reconstruction import RationalCoset
from observational_succ.edge_carrier_reconstruction import ProfiniteProgram, RationalSpan
from observational_succ.finite_adele_localization import FiniteAdeleSpan
from observational_succ.finite_adelic_character_bridge import (
    finite_adele_phase, finite_principal_parts,
)
from observational_succ.finite_fourier_carrier import (
    CyclotomicElement, exact_dft, exact_idft,
)


def _diagonal(q):
    q = F(q)
    return FiniteAdeleSpan.diagonal_rational(RationalSpan(q.numerator, q.denominator))


def _member(point, coset):
    scaled = point.add(_diagonal(-coset.shift)).multiply(_diagonal(1 / coset.scale))
    return finite_adele_phase(scaled) == 0


class CarrierPoissonAuditTests(unittest.TestCase):
    def test_integer_scale_refinement_on_nonrational_source_points(self):
        points = [_diagonal(F(k, d)) for d in (1, 2, 3, 5) for k in range(-4, 5)]
        for p in (2, 3, 5):
            points.extend(FiniteAdeleSpan(ProfiniteProgram.projector(p), d)
                          for d in (1, 2, 3, 6))
        for scale in (F(1, 2), F(2, 3), F(3, 5), F(5, 2), F(6, 7)):
            for shift in (F(0), F(1, 3), F(-2, 5)):
                parent = RationalCoset(shift, scale)
                a, b = scale.numerator, scale.denominator
                pieces = [RationalCoset(shift + scale * j, F(a)) for j in range(b)]
                self.assertEqual(sum((x.additive_haar_volume for x in pieces), F(0)),
                                 parent.additive_haar_volume)
                for point in points:
                    with self.subTest(scale=scale, shift=shift, point=point):
                        self.assertEqual(sum(_member(point, x) for x in pieces),
                                         int(_member(point, parent)))

    def test_refinement_commutes_with_exact_fourier_at_rational_frequencies(self):
        # Root arithmetic tests cancellation outside the coarser annihilator.
        for scale in (F(1, 2), F(2, 3), F(3, 4), F(5, 2)):
            for shift in (F(0), F(1, 3)):
                parent = RationalCoset(shift, scale)
                a, b = scale.numerator, scale.denominator
                pieces = [RationalCoset(shift + scale * j, F(a)) for j in range(b)]
                for m in range(-7, 8):
                    frequency = F(m, a)
                    transforms = [piece.dual_diagonal(frequency) for piece in pieces]
                    expected = parent.dual_diagonal(frequency)
                    phases = [t['finite_character_phase'] for t in transforms]
                    phases.append(expected['finite_character_phase'])
                    modulus = lcm(*(x.denominator for x in phases))
                    total = CyclotomicElement.scalar(modulus, 0)
                    for transform in transforms:
                        exponent = int(modulus * transform['finite_character_phase'])
                        total += CyclotomicElement.root(modulus, exponent).scale(
                            transform['finite_haar_amplitude'])
                    target = CyclotomicElement.root(
                        modulus, int(modulus * expected['finite_character_phase'])).scale(
                            expected['finite_haar_amplitude'])
                    self.assertEqual(total, target)

    def test_positive_forward_requires_negative_inverse(self):
        n = 5
        original = (0, 1, 0, 0, 0)
        spectrum = exact_dft(original)
        expected = tuple(CyclotomicElement.scalar(n, x) for x in original)
        self.assertEqual(exact_idft(spectrum), expected)
        wrong = []
        for x in range(n):
            value = CyclotomicElement.scalar(n, 0)
            for k, coefficient in enumerate(spectrum):
                value += coefficient * CyclotomicElement.root(n, k * x)
            wrong.append(value.scale(F(1, n)))
        self.assertNotEqual(tuple(wrong), expected)
        self.assertEqual(tuple(wrong), tuple(expected[(-x) % n] for x in range(n)))
        self.assertEqual(wrong[1], CyclotomicElement.scalar(n, 0))
        self.assertEqual(wrong[4], CyclotomicElement.scalar(n, 1))

    def test_single_place_phase_and_missing_place_have_exact_witness(self):
        q = F(1, 3)
        parts = finite_principal_parts(_diagonal(q))
        self.assertEqual(parts, {3: F(1, 3)})
        finite = sum(parts.values(), F(0))
        self.assertEqual((q - finite) % 1, 0)
        self.assertEqual((q + finite) % 1, F(2, 3))
        omitted = sum((x for p, x in parts.items() if p != 3), F(0))
        self.assertEqual((q - omitted) % 1, F(1, 3))

    def test_inverse_annihilator_scale_is_essential(self):
        coset = RationalCoset(0, 2)
        frequency = F(1, 2)
        self.assertTrue(coset.dual_diagonal(frequency)['dual_within_finite_support'])
        self.assertFalse(coset.primal_diagonal(frequency)['within_finite_compact_open_support'])
        self.assertEqual(coset.dual_diagonal(frequency)['finite_haar_amplitude'], F(1, 2))

    def test_fresh_prime_projector_evades_declared_finite_horizon(self):
        projector = ProfiniteProgram.projector(7)
        for modulus in (2, 4, 8, 3, 9, 5, 25, 30):
            self.assertEqual(projector.residue(modulus), 0)
        self.assertEqual(projector.residue(7), 1)
        self.assertEqual(finite_adele_phase(FiniteAdeleSpan(projector, 7)), F(1, 7))


if __name__ == '__main__':
    unittest.main()
