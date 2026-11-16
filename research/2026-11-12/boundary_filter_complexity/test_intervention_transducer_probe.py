import unittest
from fractions import Fraction as Q

from intervention_transducer_probe import (
    G, adjoint, bloch_density, controlled_rotation, effective_effect,
    evolved_pair, eye, inverse_coordinate, matrix, multiply,
    partial_trace_first, partial_trace_last, scaled, tensor, trace,
)


class InterventionTransducerTests(unittest.TestCase):
    c, s = Q(3, 5), Q(4, 5)
    p0, p1 = matrix([[1, 0], [0, 0]]), matrix([[0, 0], [0, 1]])

    def test_unitary_and_passive_dark_port(self):
        u = controlled_rotation(self.c, self.s)
        self.assertEqual(multiply(adjoint(u), u), eye(4))
        self.assertEqual(effective_effect(eye(4), self.p1), matrix([[0, 0], [0, 0]]))

    def test_effective_click_effect(self):
        effect = effective_effect(controlled_rotation(self.c, self.s), self.p1)
        self.assertEqual(effect, scaled(self.p1, self.s*self.s))
        for xyz in ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
                    (Q(1, 3), Q(-1, 4), Q(2, 5))):
            rho = bloch_density(*xyz)
            pair = evolved_pair(rho, self.c, self.s)
            meter = partial_trace_first(pair, 2, 2)
            self.assertEqual(meter[1][1], trace(multiply(rho, effect)))

    def test_channel_disturbance_and_energy_preservation(self):
        z = matrix([[1, 0], [0, -1]])
        for xyz in ((1, 0, 0), (0, 1, 0), (Q(1, 3), Q(-1, 4), Q(2, 5))):
            rho = bloch_density(*xyz)
            output = partial_trace_last(evolved_pair(rho, self.c, self.s), 2, 2)
            expected = matrix([[rho[0][0], self.c*rho[0][1]],
                               [self.c*rho[1][0], rho[1][1]]])
            self.assertEqual(output, expected)
            self.assertEqual(trace(multiply(output, z)), trace(multiply(rho, z)))
        plus = bloch_density(1, 0, 0)
        output = partial_trace_last(evolved_pair(plus, self.c, self.s), 2, 2)
        self.assertNotEqual(output, plus)

    def test_full_meter_still_blind_to_source_coherence(self):
        plus, minus = bloch_density(1, 0, 0), bloch_density(-1, 0, 0)
        meter_plus = partial_trace_first(evolved_pair(plus, self.c, self.s), 2, 2)
        meter_minus = partial_trace_first(evolved_pair(minus, self.c, self.s), 2, 2)
        self.assertEqual(meter_plus, meter_minus)

    def test_record_distinguishability_and_visibility(self):
        a = partial_trace_first(evolved_pair(self.p0, self.c, self.s), 2, 2)
        b = partial_trace_first(evolved_pair(self.p1, self.c, self.s), 2, 2)
        difference = matrix([[a[i][j]-b[i][j] for j in range(2)] for i in range(2)])
        self.assertEqual(trace(difference), G())
        self.assertEqual(multiply(difference, difference), scaled(eye(2), self.s*self.s))
        self.assertEqual(self.c*self.c + self.s*self.s, 1)
        # The specific click probabilities separate by s², not by optimal D=s.
        self.assertEqual(b[1][1] - a[1][1], G(self.s*self.s))

    def test_three_calibrated_axes_reconstruct_fresh_state(self):
        click = scaled(self.p1, self.s*self.s)
        # R=G/sqrt(2), so R*click R is computed without irrational rounding.
        gx = matrix([[1, 1], [1, -1]])
        gy = matrix([[1, G(0, -1)], [1, G(0, 1)]])
        rotations = (gx, gy)
        for rotation in rotations:
            self.assertEqual(multiply(adjoint(rotation), rotation), scaled(eye(2), 2))
        effects = [scaled(multiply(multiply(adjoint(r), click), r), Q(1, 2))
                   for r in rotations] + [click]
        xyz = (Q(1, 3), Q(-1, 4), Q(2, 5))
        rho = bloch_density(*xyz)
        recovered = []
        for effect in effects:
            probability = trace(multiply(rho, effect))
            self.assertEqual(probability.imag, 0)
            recovered.append(inverse_coordinate(probability.real, self.s))
        self.assertEqual(tuple(recovered), xyz)

    def test_inverse_error_is_exact_and_zero_coupling_rejected(self):
        probability = self.s*self.s/2
        error = self.s*self.s/20
        difference = inverse_coordinate(probability+error, self.s) - inverse_coordinate(probability, self.s)
        self.assertEqual(abs(difference), 2*error/(self.s*self.s))
        with self.assertRaises(ValueError):
            inverse_coordinate(Q(), 0)

    def test_known_background_can_be_cancelled(self):
        u = controlled_rotation(self.c, self.s)
        background = tensor(eye(2), matrix([[0, 1], [1, 0]]))
        total = multiply(background, u)
        self.assertNotEqual(effective_effect(total, self.p1), effective_effect(u, self.p1))
        restored = multiply(adjoint(background), total)
        self.assertEqual(effective_effect(restored, self.p1), effective_effect(u, self.p1))

    def test_unitary_calibration_error_bounds_effect_error(self):
        c, s, epsilon = Q(99, 101), Q(20, 101), Q(1, 5)
        u = controlled_rotation(c, s)
        difference = matrix([[u[i][j] - eye(4)[i][j] for j in range(4)] for i in range(4)])
        squared = multiply(adjoint(difference), difference)
        self.assertEqual(squared, matrix([[0, 0, 0, 0], [0, 0, 0, 0],
                                         [0, 0, 2-2*c, 0], [0, 0, 0, 2-2*c]]))
        self.assertLessEqual(2-2*c, epsilon*epsilon)
        plus_effect = bloch_density(1, 0, 0)
        e, ehat = effective_effect(u, plus_effect), effective_effect(eye(4), plus_effect)
        effect_difference = matrix([[e[i][j] - ehat[i][j] for j in range(2)] for i in range(2)])
        self.assertEqual(effect_difference, matrix([[0, 0], [0, c*s]]))
        self.assertLessEqual(c*s, 2*epsilon)

    def test_copying_record_prevents_naive_uncompute(self):
        u = tensor(controlled_rotation(self.c, self.s), eye(2))
        # Registers are system, meter, copy. CNOT copies the meter's basis label.
        copy = [[0]*8 for _ in range(8)]
        for source in range(8):
            system, meter, record = source//4, (source//2)%2, source%2
            target = 4*system + 2*meter + (record ^ meter)
            copy[target][source] = 1
        copy = matrix(copy)
        plus = bloch_density(1, 0, 0)
        initial = tensor(plus, tensor(self.p0, self.p0))
        restored_unitary = multiply(adjoint(u), u)
        self.assertEqual(multiply(multiply(restored_unitary, initial), adjoint(restored_unitary)), initial)
        with_copy = multiply(multiply(adjoint(u), copy), u)
        output = multiply(multiply(with_copy, initial), adjoint(with_copy))
        retained = partial_trace_last(output, 2, 4)
        self.assertEqual(retained[0][1], G(self.c*self.c/2))
        self.assertNotEqual(retained, plus)

    def test_invalid_coupling_and_state_rejected(self):
        with self.assertRaises(ValueError):
            controlled_rotation(Q(1, 2), Q(1, 2))
        with self.assertRaises(TypeError):
            controlled_rotation(0.6, self.s)
        with self.assertRaises(ValueError):
            bloch_density(1, 1, 1)


if __name__ == "__main__":
    unittest.main()
