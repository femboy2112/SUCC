"""Exact source, metric, inverse, observable and horizon controls."""

from dataclasses import replace
from fractions import Fraction as Q
import unittest

from observational_succ.carry_safe_polyphase import polyphase_succ, tensor_unitary
from observational_succ.ym_haar_bridge import (
    WeightedHaarPacket, WeightedSplit, haar_analyze, haar_synthesize,
    polyphase_pack, polyphase_unpack, weighted_energy, z2_wilson_weights,
)


def apply(matrix, vector):
    return tuple(sum((a*b for a, b in zip(row, vector)), Q()) for row in matrix)


class WeightedHaarTests(unittest.TestCase):
    def test_binary_exact_inverse_and_energy(self):
        for p, q in ((Q(1, 2), Q(1, 2)), (Q(2, 7), Q(5, 7)), (Q(7), Q(11, 3))):
            split = WeightedSplit(p, q)
            for original in ((Q(1), Q(-1)), (Q(19, 7), Q(-23, 11)), (Q(4), Q(4))):
                coefficients = split.analyze(*original)
                self.assertEqual(split.synthesize(*coefficients), original)
                self.assertEqual(weighted_energy(original, (p, q)),
                                 weighted_energy(coefficients, split.coefficient_weights))

    def test_uniform_haar_has_expected_multiscale_order(self):
        packet = haar_analyze((1, 2, 3, 4), (1, 1, 1, 1))
        self.assertEqual(packet.coefficients, (Q(5, 2), -2, -1, -1))
        self.assertEqual(packet.coefficient_weights, (4, 1, Q(1, 2), Q(1, 2)))
        self.assertEqual(packet.energy, 30)
        self.assertEqual(haar_synthesize(packet), (1, 2, 3, 4))

    def test_fresh_weighted_trees_reconstruct_every_detail(self):
        for size in (1, 2, 8, 32):
            weights = tuple(Q(j + 2, j + 3) for j in range(size))
            values = tuple(Q((-1)**j * (3*j + 1), 2*j + 5) for j in range(size))
            packet = haar_analyze(values, weights)
            self.assertEqual(haar_synthesize(packet), values)
            self.assertEqual(packet.energy, weighted_energy(values, weights))
            self.assertEqual(packet.coefficients[0],
                             sum((v*w for v, w in zip(values, weights)), Q()) / sum(weights))

    def test_detail_deletion_loses_energy_and_information(self):
        packet = haar_analyze((1, -1), (1, 1))
        coarse_only = replace(packet, coefficients=(packet.coefficients[0], Q()))
        self.assertEqual(packet.energy, 2)
        self.assertEqual(coarse_only.energy, 0)
        self.assertEqual(haar_synthesize(coarse_only), (0, 0))
        with self.assertRaises(ValueError):
            WeightedHaarPacket((Q(1), Q(1)), (Q(0),))

    def test_transport_observable_not_only_state_vector(self):
        split = WeightedSplit(Q(2, 7), Q(5, 7))
        values, observable = (Q(11, 5), Q(-7, 3)), (Q(-2), Q(5))
        matrix = split.multiplication_matrix(*observable)
        transformed_product = split.analyze(*(f*x for f, x in zip(values, observable)))
        self.assertEqual(apply(matrix, split.analyze(*values)), transformed_product)
        metric = split.coefficient_weights
        self.assertEqual(metric[0] * matrix[0][1], metric[1] * matrix[1][0])

    def test_adapted_vacuum_equality_does_not_erase_source(self):
        fair = WeightedSplit(*z2_wilson_weights(Q(0)))
        biased = WeightedSplit(*z2_wilson_weights(Q(3, 5)))
        self.assertEqual(fair.analyze(1, 1), (1, 0))
        self.assertEqual(biased.analyze(1, 1), (1, 0))
        fair_observable = fair.multiplication_matrix(1, -1)
        biased_observable = biased.multiplication_matrix(1, -1)
        self.assertEqual(fair_observable[0][0], 0)
        self.assertEqual(biased_observable[0][0], Q(3, 5))
        self.assertNotEqual(fair_observable, biased_observable)

    def test_uniform_weight_substitution_mutates_wilson_expectation(self):
        data = (1, -1)
        true_weights = z2_wilson_weights(Q(3, 5))
        self.assertEqual(haar_analyze(data, true_weights).coefficients[0], Q(3, 5))
        self.assertEqual(haar_analyze(data, (Q(1, 2), Q(1, 2))).coefficients[0], 0)

    def test_exact_domain_controls(self):
        with self.assertRaises(TypeError):
            WeightedSplit(0.5, 0.5)
        with self.assertRaises(ValueError):
            WeightedSplit(0, 1)
        with self.assertRaises(ValueError):
            haar_analyze((1, 2, 3), (1, 1, 1))
        with self.assertRaises(ValueError):
            z2_wilson_weights(1)


class ExistingPolyphaseBridgeTests(unittest.TestCase):
    def test_existing_coordinate_map_and_controlled_carry(self):
        packet = polyphase_pack(tuple(range(1, 9)), 4)
        self.assertEqual(packet.blocks, ((1, 2, 3, 4), (5, 6, 7, 8)))
        self.assertEqual(polyphase_unpack(packet), tuple(range(1, 9)))
        self.assertEqual(polyphase_succ(1, 3, 4), (2, 0))
        self.assertTrue(tensor_unitary(8, 4).onto)

    def test_partial_horizon_isometry_has_explicit_unhit_slots(self):
        source = (Q(1, 2), Q(2, 3), Q(-3, 5), Q(7, 11), Q(-13, 17))
        packet = polyphase_pack(source, 4)
        layout = tensor_unitary(5, 4)
        self.assertFalse(layout.onto)
        self.assertEqual(layout.unhit, ((2, 1), (2, 2), (2, 3)))
        self.assertEqual(polyphase_unpack(packet), source)
        self.assertEqual(sum((v*v for row in packet.blocks for v in row), Q()),
                         sum((v*v for v in source), Q()))
        mutant = replace(packet, blocks=(packet.blocks[0], (packet.blocks[1][0], Q(1), Q(), Q())))
        with self.assertRaisesRegex(ValueError, "horizon"):
            polyphase_unpack(mutant)


if __name__ == "__main__":
    unittest.main()
