"""Exact geometry, lost-coordinate and lost-precision carry controls."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import unittest

from observational_succ.prime_base_carry import (
    CoverPoint,
    carry_cocycle,
    circle_carry,
    inverse_candidates_without_q_coordinate,
    invert_with_q_coordinate,
    reduce_cover,
    transport_cover,
)


class PrimeBaseCarryTests(unittest.TestCase):
    def test_exact_geometry_instead_of_only_label_formula(self):
        roots = (Q(0), Q(1, 16), Q(1, 3), Q(2, 3), Q(15, 16), Q(256, 257))
        for modulus, q, root in product((1, 2, 4, 8, 9, 16, 25, 27),
                                        (2, 3, 5, 7, 11, 13), roots):
            for label in range(modulus):
                point = CoverPoint(root, label, modulus)
                image = transport_cover(point, q)
                self.assertEqual(image.circle_point, (q*point.circle_point) % 1)
                self.assertEqual((modulus*image.circle_point) % 1, (q*root) % 1)

    def test_fibre_permutation_iff_coprime(self):
        for modulus, q in product(range(1, 49), range(1, 17)):
            for root in (Q(0), Q(2, 5), Q(11, 13)):
                labels = {transport_cover(CoverPoint(root, a, modulus), q).label
                          for a in range(modulus)}
                self.assertEqual(len(labels), modulus//gcd(q, modulus))
                self.assertEqual(len(labels) == modulus, gcd(q, modulus) == 1)

    def test_bounded_carry_including_exact_boundary(self):
        for q in range(1, 18):
            for k in range(q):
                self.assertEqual(circle_carry(Q(k, q), q), (Q(0), k))
                x = Q(k, q)+Q(1, 2*q)
                self.assertEqual(circle_carry(x, q), (Q(1, 2), k))

    def test_carry_cocycle_and_commuting_actual_maps(self):
        for q, r, root in product((2, 3, 4, 5, 7, 16),
                                   (2, 3, 4, 5, 7, 16),
                                   (Q(0), Q(1, 3), Q(3, 7), Q(15, 16))):
            point = CoverPoint(root, 29, 48)
            direct = transport_cover(point, q*r)
            self.assertEqual(transport_cover(transport_cover(point, r), q), direct)
            self.assertEqual(transport_cover(transport_cover(point, q), r), direct)
            carries = carry_cocycle(root, q, r)
            self.assertEqual(carries, ((q*r*root).__floor__(),)*3)

    def test_factor_base_and_depth_reductions_are_coherent(self):
        for root, label, q in product((Q(1, 5), Q(2, 3)), range(16), (3, 5, 7)):
            point = CoverPoint(root, label, 16)
            self.assertEqual(reduce_cover(reduce_cover(point, 4), 2),
                             reduce_cover(point, 2))
            for divisor in (1, 2, 4, 8, 16):
                projected = reduce_cover(point, divisor)
                self.assertEqual(projected.circle_point,
                                 ((16//divisor)*point.circle_point) % 1)
                self.assertEqual(reduce_cover(transport_cover(point, q), divisor),
                                 transport_cover(projected, q))

    def test_one_integer_carry_serves_distinct_prime_coordinates(self):
        # The joint 2^4 * 3^2 * 5 cover supplies compatible CRT projections.
        for root, label, q in product((Q(3, 7), Q(8, 9)), (0, 1, 42, 719),
                                      (2, 3, 5, 7, 13)):
            point = CoverPoint(root, label, 720)
            root_after, shared_carry = circle_carry(root, q)
            image = transport_cover(point, q)
            for modulus in (16, 9, 5):
                part = transport_cover(reduce_cover(point, modulus), q)
                self.assertEqual(part, reduce_cover(image, modulus))
                self.assertEqual(part.root, root_after)
                self.assertEqual(part.label, (q*label+shared_carry) % modulus)

    def test_inverse_spends_one_factor_of_q_precision(self):
        for q, lower_modulus, root in product((2, 3, 5, 7), (1, 2, 9, 16),
                                               (Q(0), Q(2, 7), Q(15, 16))):
            modulus = q*lower_modulus
            for label in range(modulus):
                source = CoverPoint(root, label, modulus)
                image = transport_cover(source, q)
                recovered = invert_with_q_coordinate(image, q)
                self.assertEqual(recovered, reduce_cover(source, lower_modulus))
                self.assertEqual(recovered.modulus, lower_modulus)

    def test_extra_finite_precision_really_is_ambiguous(self):
        q, lower_modulus = 3, 16
        sources = tuple(CoverPoint(Q(2, 5), 7+j*lower_modulus,
                                   q*lower_modulus) for j in range(q))
        images = tuple(transport_cover(source, q) for source in sources)
        self.assertEqual(len(set(sources)), q)
        self.assertEqual(len(set(images)), 1)
        recovered = invert_with_q_coordinate(images[0], q)
        self.assertEqual(recovered, CoverPoint(Q(2, 5), 7, lower_modulus))
        # A mutant reporting the original cover degree would falsely choose
        # one of q indistinguishable labels.
        self.assertNotEqual(recovered.modulus, sources[0].modulus)

    def test_inverse_reads_the_higher_cover_coordinate_directly(self):
        for q, lower_modulus, root in product((2, 3, 5), (1, 4, 9, 16),
                                               (Q(1, 7), Q(2, 3))):
            for label in range(q*lower_modulus):
                image = CoverPoint(root, label, q*lower_modulus)
                recovered = invert_with_q_coordinate(image, q)
                # Multiplication by q shifts inverse-cover coordinates:
                # the image's q*m coordinate IS the source's m coordinate.
                self.assertEqual(recovered.circle_point, image.circle_point)
                self.assertEqual(transport_cover(recovered, q),
                                 reduce_cover(image, lower_modulus))

    def test_missing_q_coordinate_preserves_all_q_candidates(self):
        for modulus, q, root in product((1, 2, 4, 16, 25), (3, 7),
                                        (Q(0), Q(1, 7), Q(8, 9))):
            for label in range(modulus):
                image = CoverPoint(root, label, modulus)
                candidates = inverse_candidates_without_q_coordinate(image, q)
                self.assertEqual(len(set(candidates)), q)
                self.assertEqual({c.root for c in candidates},
                                 {(root+k)/q for k in range(q)})
                for candidate in candidates:
                    self.assertEqual(transport_cover(candidate, q), image)

    def test_missing_coordinate_candidates_match_all_lifted_images(self):
        image = CoverPoint(Q(1, 7), 5, 16)
        candidates = inverse_candidates_without_q_coordinate(image, 3)
        lifted_images = (CoverPoint(image.root, image.label+16*j, 48)
                         for j in range(3))
        inverses = {invert_with_q_coordinate(lifted, 3) for lifted in lifted_images}
        self.assertEqual(inverses, set(candidates))

    def test_dropping_carry_fails_geometric_oracle(self):
        source = CoverPoint(Q(2, 5), 0, 16)
        actual = transport_cover(source, 3)
        wrong = CoverPoint((3*source.root) % 1, (3*source.label) % 16, 16)
        self.assertEqual(actual.circle_point, (3*source.circle_point) % 1)
        self.assertNotEqual(wrong.circle_point, (3*source.circle_point) % 1)
        self.assertEqual(actual.label-wrong.label, 1)

    def test_carry_relabeling_does_not_uniformize_weights(self):
        # An affine bijection sends a point mass to a point mass.  Structural
        # branch transport cannot itself provide a 1/16 probability bound.
        points = tuple(CoverPoint(Q(2, 5), a, 16) for a in range(16))
        weights = {point: Q(int(point.label == 7)) for point in points}
        image_weights = {transport_cover(point, 3): weight
                         for point, weight in weights.items()}
        self.assertEqual(sum(weight*weight for weight in image_weights.values()), 1)
        self.assertNotEqual(set(image_weights.values()), {Q(1, 16)})

    def test_invalid_inputs_cannot_hide_domain_or_precision_errors(self):
        for args in ((Q(1), 0, 16), (Q(-1, 5), 0, 16), (0.5, 0, 16),
                     (True, 0, 16), (Q(0), 16, 16), (Q(0), -1, 16),
                     (Q(0), 0, 0), (Q(0), 0, True)):
            with self.assertRaises(ValueError):
                CoverPoint(*args)
        point = CoverPoint(Q(2, 5), 7, 16)
        for q in (0, -1, True, Q(3), 3.0):
            with self.assertRaises(ValueError):
                transport_cover(point, q)
        with self.assertRaises(ValueError):
            reduce_cover(point, 3)
        with self.assertRaises(ValueError):
            invert_with_q_coordinate(point, 3)
        with self.assertRaises(ValueError):
            inverse_candidates_without_q_coordinate(point, 2)
        with self.assertRaises(ValueError):
            inverse_candidates_without_q_coordinate(CoverPoint(Q(0), 0, 2), 6)


if __name__ == "__main__":
    unittest.main()
