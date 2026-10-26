"""Exact source, rational-carrier and signed-firewall hostile controls."""
import unittest
from fractions import Fraction as Q

from observational_succ import beck_chevalley_source as bc
from observational_succ import signed_pushforward as sp
from observational_succ import selected_branch_operator as op
from observational_succ.lambda_source_duality import (
    Cyclo16, branch_defect, original_history, uniform_inverse_character,
)
from observational_succ.succ_internal_matrix_walk import PhasePoly, circle


class OddInverseTests(unittest.TestCase):
    def test_unique_odd_lift_exhaustive_independent_enumeration(self):
        for q in range(1, 62, 2):
            for a in range(q):
                t = Q(a, q)
                actual = op.exact_odd_inverse(t)
                odd = [((j+t)/16, j) for j in range(16)
                       if ((j+t)/16).denominator % 2]
                self.assertEqual(odd, [(actual.predecessor, actual.digit)])
                self.assertEqual(circle(16*actual.predecessor), t)

    def test_original_source_four_poles_independent_grouping(self):
        # Independently grouped formula proves why the original even poles
        # cancel their two-parts; every remaining denominator is odd.
        states = original_history(83)
        previous = Q()
        for n, state in enumerate(states, 1):
            grouped = Q(4, 8*n-7)-Q(1, 8*n-3)-Q(3*n-1, (2*n-1)*(4*n-1))
            self.assertEqual(state, 16*previous+grouped)
            self.assertEqual(state.denominator % 2, 1)
            x = circle(state)
            self.assertEqual(op.exact_odd_inverse(circle(16*x)).predecessor, x)
            previous = state

    def test_even_carrier_and_pole_mutation_fail_assumption(self):
        for bad in (Q(1, 2), Q(1, 32), Q(1), Q(-1, 3), .2, True):
            with self.assertRaises(ValueError):
                op.exact_odd_inverse(bad)
        # x=1/16 has the same tail as x=0 but has an even denominator.
        self.assertEqual(circle(16*Q(1, 16)), 0)
        self.assertNotEqual(op.exact_odd_inverse(Q()).predecessor, Q(1, 16))
        mutated_force = Q(47, 15)+Q(1, 4)  # omit half the negative second pole.
        self.assertEqual(mutated_force.denominator % 2, 0)

    def test_nearby_tails_have_every_selected_branch(self):
        for center in (Q(), Q(2, 15), Q(1, 2), Q(37, 41)):
            for epsilon in (Q(1, 7), Q(1, 103), Q(1, 10007)):
                for digit in range(16):
                    w = op.odd_tail_near(center, digit, epsilon)
                    self.assertLess(abs(w.tail-center), epsilon)
                    self.assertEqual(w.digit, digit)
                    self.assertEqual(w.predecessor, (digit+w.tail)/16)


class ResolutionTests(unittest.TestCase):
    def test_all_N_source_threshold_without_dense_allocation(self):
        for N in (1, 2, 7, 19, 47, 113):
            states = original_history(N)
            first = op.authentic_resolution_certificate(states)
            for M in (first.conductor, first.conductor+1, 3*first.conductor):
                cert = op.authentic_resolution_certificate(states, M)
                self.assertEqual(cert.chi_squared, 15)
                self.assertTrue(cert.exact_tail_partition)
                self.assertLessEqual(len(cert.counts), N)
                for h in (-17, -8, 0, 1, 4, 8, 15, 16):
                    self.assertEqual(cert.conditional_mode_energy(h), Cyclo16.one())

    def test_coarse_sparse_table_matches_native_dense_independent_code(self):
        states = original_history(67)
        for M in (1, 3, 8, 17, 131):
            sparse = op.authentic_resolution_certificate(states, M)
            dense = branch_defect(states, M)
            self.assertEqual(sparse.chi_squared, dense.chi_squared)
            for h in (1, 4, 8, 13):
                self.assertEqual(sparse.conditional_mode_energy(h),
                                 dense.conditional_mode_energy(h))

    def test_repeated_tails_do_not_require_time_injectivity(self):
        # Synthetic odd states may repeat. Full conditioning still has one
        # digit per tail; no injectivity of authentic source times is claimed.
        states = (Q(2, 15), Q(2, 15), Q(7, 15), Q(7, 15))
        b = branch_defect(states, 15, authenticate=False)
        self.assertEqual(b.chi_squared, 15)
        for h in range(1, 16):
            self.assertEqual(b.conditional_mode_energy(h), Cyclo16.one())

    def test_carrier_support_lower_bound_and_threshold_boundary(self):
        for q in (1, 3, 15, 17, 31, 65):
            values = tuple(Q(a, q) for a in range(q))
            for M in (1, 2, 3, q, q+1):
                d = branch_defect(values, M, authenticate=False)
                self.assertGreaterEqual(d.chi_squared,
                                        op.carrier_resolution_lower(q, M))
        # M<Q can mix selected branches; maximality is not asserted there.
        self.assertLess(branch_defect(tuple(Q(a, 17) for a in range(17)),
                                     1, authenticate=False).chi_squared, 15)

    def test_original_anchor_and_history_mutations_rejected(self):
        authentic = original_history(8)
        altered = tuple(u+Q(16**n, 3) for n, u in enumerate(authentic, 1))
        for history in (altered, authentic[:-1]+(authentic[-1]+1,), ()):
            with self.assertRaises(ValueError):
                op.authentic_resolution_certificate(history)
        for M in (0, True, 1.0):
            with self.assertRaises(ValueError):
                op.authentic_resolution_certificate(authentic, M)


class OperatorFirewallTests(unittest.TestCase):
    def test_affine_odd_carrier_is_permutation_and_exact_norm_isometry(self):
        for q in (1, 3, 9, 15, 17, 35, 105):
            for a in (-2, 0, 1, q+2):
                mapping = op.odd_carrier_affine_map(q, Q(a, q))
                values = {x: Q(i*i-3*i, i+1) for i, x in enumerate(mapping.domain)}
                original = sum(v*v for v in values.values())
                pulled = sum(values[y]**2 for _, y in mapping.pairs)
                self.assertEqual(original, pulled)
                self.assertEqual(set(mapping.table().values()), set(mapping.domain))

    def test_even_carrier_and_foreign_forcing_are_rejected(self):
        for q, r in ((16, Q()), (15, Q(1, 2)), (3, Q(1, 5))):
            with self.assertRaises(ValueError):
                op.odd_carrier_affine_map(q, r)

    def test_actual_odd_fiber_is_not_cartesian_or_uniform_ensemble(self):
        for t in (Q(), Q(2, 15), Q(8, 13)):
            sq = op.selected_fiber_square(t)
            self.assertTrue(bc.is_commutative(sq))
            self.assertFalse(bc.is_cartesian(sq))
            self.assertEqual(len(bc.fiber_product(sq)), 16)
            self.assertEqual(len(sq.S_prime), 1)
            selected = sq.S_prime[0]
            ghost = next(x for x in sq.S if x != selected)
            amp = {x: (PhasePoly.one() if x == ghost else PhasePoly.zero())
                   for x in sq.S}
            self.assertFalse(sp.amplitude_base_change_holds(sq, amp))
            digit = op.exact_odd_inverse(t).digit
            self.assertEqual(uniform_inverse_character(8), Cyclo16.zero())
            self.assertNotEqual(Cyclo16.zeta(8*digit), Cyclo16.zero())

    def test_donor_redundant_realizers_remain_signed_obstruction(self):
        sq = bc.realization_faithful_noncartesian_square()
        self.assertTrue(bc.comparison_is_surjective(sq))
        self.assertTrue(bc.beck_chevalley_holds_all(sq))
        self.assertFalse(bc.is_cartesian(sq))
        self.assertFalse(sp.amplitude_base_change_holds(
            sq, {x: PhasePoly.one() for x in sq.S}))

    def test_status_does_not_claim_cancellation(self):
        self.assertFalse(op.status_flags()["selected_weyl_saving_proved"])
        self.assertFalse(op.status_flags()["pi_base16_normality_proved"])


if __name__ == "__main__":
    unittest.main()
