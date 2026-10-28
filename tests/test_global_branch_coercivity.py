"""Independent exact and hostile checks for the whole-block inequality."""
import unittest
from fractions import Fraction as Q

from observational_succ.global_branch_coercivity import (
    BLOCK_LOSS, approximation_coefficient_bound, authentic_forcing_parameters,
    boundary_excursion_squared_modulus, conditional_logarithmic_budget,
    diophantine_scale_comparison, inverse_seed_certificate,
    local_cosine_coefficient, machin_pi_interval, quiet_transition_witness,
    uniform_threshold_comparison, whole_block_parameters,
)


def literal_r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


class WholeBlockFiniteProof(unittest.TestCase):
    def test_machin_bounds_with_independent_alternating_sums(self):
        def partial(x, terms):
            return sum(((-1)**k*x**(2*k+1)/Q(2*k+1)
                        for k in range(terms)), Q())
        lower, upper = machin_pi_interval()
        self.assertEqual(lower, 16*partial(Q(1, 5), 2)-4*partial(Q(1, 239), 1))
        self.assertEqual(upper, 16*partial(Q(1, 5), 3)-4*partial(Q(1, 239), 2))
        self.assertGreater(lower, Q(157, 50))
        self.assertLess(upper, Q(22, 7))
        self.assertEqual(local_cosine_coefficient()-19, Q(8725979, 63026250))
        # The stronger local coefficient is not lawful at q=1/2.
        self.assertGreater(19*Q(1, 2)**2, 2)

    def test_exact_long_block_margin_and_rejected_boundary_mutations(self):
        parameters = whole_block_parameters(20000, Q(15, 4096))
        self.assertEqual(parameters.nonconstant_loss_lower-BLOCK_LOSS,
                         Q(9907077909, 19243046273024))
        for args in ((19999, 0), (20000, Q(1, 50)),
                     (20000, 0, Q(1, 101)), (20000, -1)):
            with self.assertRaises(ValueError):
                whole_block_parameters(*args)

    def test_quiet_pair_and_integer_gap_on_independent_boundary_orbit(self):
        offsets = (Q(1, 16),)+(Q(),)*20000
        witness = quiet_transition_witness(offsets, (Q(),)*20000)
        t = witness.quiet_index
        self.assertEqual(t, 1)
        self.assertEqual(witness.other_branch_index, 0)
        self.assertEqual(witness.energy, Q(1, 256))
        self.assertLessEqual(20000*(offsets[t]**2+offsets[t+1]**2), 2*witness.energy)
        gap = abs(witness.transition_values[0]-witness.transition_values[t])
        self.assertGreaterEqual(gap, 1-witness.forcing_span)
        self.assertLessEqual(gap**2, 257*witness.energy*Q(101, 100)**2)

    def test_constant_branch_and_incompatible_source_mutation(self):
        offsets = (Q(1, 32), Q(1, 32), Q(1, 32), Q(1, 32))
        witness = quiet_transition_witness(offsets, (Q(),)*3, -7)
        self.assertIsNone(witness.other_branch_index)
        with self.assertRaises(ValueError):
            quiet_transition_witness(offsets, (Q(), Q(1, 7), Q()), 1)

    def test_inverse_arc_zero_seed_inside_boundary_excursion_outside(self):
        forcing = (Q(),)*20000
        inside = inverse_seed_certificate(0, forcing)
        outside = inverse_seed_certificate(Q(1, 16), forcing)
        self.assertFalse(inside.outside_arcs)
        self.assertTrue(outside.outside_arcs)
        self.assertEqual(outside.distance_to_centers, Q(1, 240))
        self.assertEqual(outside.arc_radius, Q(16, 75*16**20000))

    def test_inverse_source_order_and_independent_backward_telescope(self):
        # Constant nonzero forcing exercises actual source weighting.
        forcing = (Q(1, 13),)*20000
        initial = -Q(1, 195)
        cert = inverse_seed_certificate(initial, forcing, -3)
        self.assertEqual(cert.weighted_source, Q(1, 195)*(1-Q(1, 16**20000)))
        self.assertEqual(initial+cert.weighted_source, initial/Q(16**20000))
        self.assertFalse(cert.outside_arcs)


class AuthenticBandAndConditionalOnset(unittest.TestCase):
    def test_literal_four_poles_on_independent_scale_and_frequency_holdouts(self):
        for m, h in ((4096, 1), (4103, -17), (5003, 5003**2//64), (8191, 101)):
            parameters = authentic_forcing_parameters(m, h)
            self.assertEqual(parameters.forcing_span,
                             abs(h)*(literal_r(m+2)-literal_r(8*m)))
            self.assertEqual(parameters.transitions, 7*m-1)
            self.assertLess(parameters.forcing_span, Q(15, 4096))
            self.assertGreater(parameters.nonconstant_loss_lower, BLOCK_LOSS)
        with self.assertRaises(ValueError):
            authentic_forcing_parameters(4096, 4096**2//64+1)

    def test_inverse_approximation_coefficient_and_factor_sixteen(self):
        self.assertEqual(approximation_coefficient_bound(1, 1), Q(3219739, 940800))
        for m, h in ((1, -1), (17, 3), (4096, 91)):
            self.assertLess(approximation_coefficient_bound(m, h), 4)
        # A supplied C is NOT certified as an irrationality constant for pi.
        c = Q(15**8, 16**16)
        self.assertGreater(c*c*16**32, 15**15)
        self.assertFalse(diophantine_scale_comparison(32, 1, c))
        self.assertTrue(diophantine_scale_comparison(33, 1, c))
        self.assertTrue(uniform_threshold_comparison(4096, Q(1, 1000)))

    def test_all_N_block_count_against_direct_interval_enumeration(self):
        for n in (1, 8**4-1, 8**5, 8**6+17, 8**9-1):
            for h in (1, 64**3, 64**3+1, 64**6+1):
                result = conditional_logarithmic_budget(n, h, 4)
                direct = sum(8**(j+1) <= n and j >= 4 and 64*h <= (8**j)**2
                             for j in range(12))
                self.assertEqual(result.eligible_blocks, direct)
                self.assertEqual(result.modulus_upper, Q(n)-Q(direct, 14))
                self.assertFalse(result.numerical_onset_certified)

    def test_boundary_control_has_smaller_loss_than_one_thirteenth(self):
        # cos(pi/8)=sqrt(2+sqrt(2))/2. The following rational lower
        # certificate uses 239² < 2*169² and has no floating trig input.
        c_lower = Q(9238, 10000)
        self.assertLess(Q(239, 169)**2, 2)
        self.assertLess(4*c_lower*c_lower-2, Q(239, 169))
        self.assertGreater(c_lower, Q(12, 13))
        # For every tested T, |T+e(1/16)|>T+12/13, so D<1/13.
        for t in (2, 73, 20000):
            self.assertGreater(boundary_excursion_squared_modulus(t, c_lower),
                               (Q(t)+Q(12, 13))**2)

    def test_exact_type_and_domain_failures(self):
        for call in (lambda: whole_block_parameters(True, 0),
                     lambda: whole_block_parameters(20000, 0.0),
                     lambda: authentic_forcing_parameters(4095),
                     lambda: authentic_forcing_parameters(4096, 0),
                     lambda: conditional_logarithmic_budget(10, 1, 3),
                     lambda: diophantine_scale_comparison(4, 1, 0)):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
