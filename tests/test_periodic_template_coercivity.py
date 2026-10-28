"""Exact independent and hostile controls for periodic-template coercivity."""
import unittest
from fractions import Fraction as Q

from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.periodic_template_coercivity import (
    approximation_coefficient_bound, authentic_forcing_parameters,
    conditional_periodic_budget, diophantine_scale_comparison,
    inverse_periodic_certificate, periodic_branch_parameters,
    periodic_integer_solution, periodic_lift_witness, residue_transition_counts,
    uniform_threshold_comparison,
)


def literal_r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


class PeriodicFiniteCore(unittest.TestCase):
    def test_modular_transition_endpoints_against_enumeration(self):
        for t, p in ((2, 1), (23, 5), (31, 3), (20003, 7), (17, 23)):
            expected = tuple(sum(n % p == s for n in range(t)) for s in range(p))
            self.assertEqual(residue_transition_counts(t, p), expected)
            self.assertEqual(min(expected), t//p)

    def test_whole_block_quiet_count_in_each_residue(self):
        params = periodic_branch_parameters(60002, 3, Q(15, 4096))
        self.assertEqual(params.minimum_residue_count, 20000)
        self.assertEqual(params.nonperiodic_loss_lower-Q(1, 14),
                         Q(9907077909, 19243046273024))
        with self.assertRaises(ValueError):
            periodic_branch_parameters(59999, 3, 0)

    def test_periodic_integer_fixed_point_independent_polynomial_formula(self):
        for pattern in ((3,), (1, -2), (7, 0, -3), (1, 5, -9, 2, 11)):
            values = periodic_integer_solution(pattern)
            p = len(pattern)
            independent = -sum(k*16**(p-1-t) for t, k in enumerate(pattern))
            self.assertEqual(values[0], Q(independent, 16**p-1))
            for t, k in enumerate(pattern):
                self.assertEqual(values[(t+1) % p], 16*values[t]+k)
                self.assertEqual(((16**p-1)*values[t]).denominator, 1)

    def test_arbitrary_rational_templates_cancel_on_congruent_indices(self):
        pattern = (2, -7, 4)
        f = periodic_integer_solution(pattern)
        # The rational periodic lift f is represented with an arbitrary
        # center; theta repeats exactly, q=0, and no theta enters f's carrier.
        center = Q(2, 37)
        template = tuple(x-center for x in f)
        witness = periodic_lift_witness((Q(),)*24, (Q(),)*23,
                                         template, -5, center)
        self.assertIsNone(witness.incompatible_branch_pair)
        self.assertEqual(witness.branches, tuple(pattern[t % 3] for t in range(23)))
        self.assertEqual(witness.energy, 0)
        mutated = list(template)
        mutated[1] += Q(1, 17)
        with self.assertRaises(ValueError):
            periodic_lift_witness((Q(),)*24, (Q(),)*23, mutated, -5, center)

    def test_nonperiodic_branch_event_and_quiet_class_witness(self):
        offsets = (Q(1, 16),)+(Q(),)*60000
        witness = periodic_lift_witness(offsets, (Q(),)*60000, (0, 0, 0))
        self.assertEqual(witness.incompatible_branch_pair, (3, 0))
        self.assertEqual(witness.branches[0], -1)
        self.assertTrue(all(k == 0 for k in witness.branches[1:]))
        self.assertEqual(witness.quiet_transition_indices, (3, 1, 2))
        self.assertEqual(witness.energy, Q(1, 256))

    def test_endpoint_p_step_identity_with_nondividing_terminal_index(self):
        pattern = (2, -7, 4, 1, -8)
        periodic = periodic_integer_solution(pattern)
        t = 23
        forcing = tuple(Q((-1)**j*(j+2), 3*j+7) for j in range(1, t+1))
        state = Q(5, 31)
        states = [state]
        for j, r in enumerate(forcing):
            state = 16*state+r+pattern[j % 5]
            states.append(state)
        p = len(pattern)
        z = tuple(states[j]-periodic[j % p] for j in range(t+1))
        last = sum((16**(p-j)*forcing[t-p+j-1] for j in range(1, p+1)), Q())
        self.assertEqual(z[t], 16**p*z[t-p]+last)
        self.assertEqual(z[t], (16**p*(z[t]-z[t-p])-last)/(16**p-1))
        ordered = sum((r/Q(16**j) for j, r in enumerate(forcing, 1)), Q())
        self.assertEqual(z[0]+ordered, z[t]/Q(16**t))

    def test_generic_inverse_preserves_periodic_exact_control_and_rejects_excursion(self):
        forcing = (Q(),)*40000
        periodic = inverse_periodic_certificate(Q(1, 255), forcing, 2, -7)
        excursion = inverse_periodic_certificate(Q(1, 16), forcing, 2, 1)
        self.assertFalse(periodic.outside_arcs)
        self.assertEqual(periodic.center_denominator, 7*255)
        self.assertTrue(excursion.outside_arcs)
        self.assertEqual(excursion.arc_radius, Q(256, 1275*16**40000))
        self.assertEqual(excursion.distance_to_centers, Q(1, 4080))

    def test_constant_forcing_order_and_last_period_weight(self):
        forcing = (Q(1, 13),)*40000
        result = inverse_periodic_certificate(-Q(1, 195), forcing, 2, 1)
        self.assertEqual(result.terminal_period_forcing, Q(17, 13))
        self.assertEqual(result.weighted_source, Q(1, 195)*(1-Q(1, 16**40000)))
        self.assertFalse(result.outside_arcs)


class SourceAndSimultaneousBudgets(unittest.TestCase):
    def test_large_literal_source_holdouts_and_period_boundary(self):
        for m, p, h in ((4096, 1, 1), (8193, 2, -31),
                        (12317, 3, 12317**2//64), (32771, 7, 101)):
            result = authentic_forcing_parameters(m, p, h)
            self.assertEqual(result.forcing_span,
                             abs(h)*(literal_r(m+2)-literal_r(8*m)))
            self.assertEqual(result.minimum_residue_count, (7*m-1)//p)
            self.assertGreaterEqual(result.minimum_residue_count, 20000)
        with self.assertRaises(ValueError):
            authentic_forcing_parameters(8191, 2)

    def test_denominator_factor_mutation_and_conditional_onset(self):
        # At p=2 the conductor is255, not15. Supplied C is never certified.
        m, p, h = 32, 2, 1
        c = Q(15**8, 16**16)
        self.assertGreater(c*c*16**m, 15**15)
        self.assertFalse(diophantine_scale_comparison(m, p, h, c))
        self.assertTrue(uniform_threshold_comparison(4096, Q(1, 1000)))
        for m, p, h in ((1, 1, 1), (17, 17, -3), (8192, 2, 97)):
            self.assertLess(approximation_coefficient_bound(m, p, h), 4)

    def test_all_N_count_with_independently_enumerated_period_and_frequency_gates(self):
        for n in (1, 8**5-1, 8**5, 8**8+11):
            for p in (1, 2, 8, 9, 65):
                for h in (1, 64**3+1):
                    budget = conditional_periodic_budget(n, p, h, 4)
                    expected = sum(8**(j+1) <= n and j >= 4
                                   and 8**j >= 4096*p and (8**j)**2 >= 64*h
                                   for j in range(12))
                    self.assertEqual(budget.eligible_blocks, expected)
                    self.assertEqual(budget.residue_modulus_sum_upper, Q(n)-Q(expected, 14))
                    self.assertFalse(budget.numerical_onset_certified)

    def test_untwisted_cancellation_does_not_control_periodic_template_supremum(self):
        # A genuine period-three x ->16x circle orbit with conductor9.
        phases = tuple(pow(16, n, 9) for n in range(1, 4))
        untwisted = CyclotomicElement.scalar(9, 0)
        matched = CyclotomicElement.scalar(9, 0)
        for a in phases:
            untwisted += CyclotomicElement.root(9, a)
            matched += CyclotomicElement.root(9, a)*CyclotomicElement.root(9, -a)
        self.assertEqual(untwisted, CyclotomicElement.scalar(9, 0))
        self.assertEqual(matched, CyclotomicElement.scalar(9, 3))

    def test_type_and_passport_inputs_are_not_silently_coerced(self):
        for call in (lambda: periodic_integer_solution((True,)),
                     lambda: periodic_branch_parameters(40000, 2, 0.0),
                     lambda: inverse_periodic_certificate(0, (0, 0), 0),
                     lambda: authentic_forcing_parameters(4096, 1, 0),
                     lambda: conditional_periodic_budget(10, 1, 1, 3),
                     lambda: diophantine_scale_comparison(20, 2, 1, 0)):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
