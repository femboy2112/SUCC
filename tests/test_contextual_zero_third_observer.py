"""Exact controls for the contextual-zero / third-observer research extension.

This finite algebra is not a physical measurement, entropy production result,
or a source-specific arithmetic estimate.
"""

from fractions import Fraction
import unittest


def product(left, right):
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix shapes")
    return tuple(tuple(sum((Fraction(a) * Fraction(b) for a, b in
                            zip(left_row, col)), Fraction(0))
                       for col in zip(*right)) for left_row in left)


def add(left, right):
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("incompatible matrix shapes")
    return tuple(tuple(Fraction(a) + Fraction(b) for a, b in zip(ra, rb))
                 for ra, rb in zip(left, right))


def neg(a):
    return tuple(tuple(-Fraction(x) for x in row) for row in a)


def sub(a, b):
    return add(a, neg(b))


def output(row, vector):
    return sum((Fraction(x) * Fraction(y) for x, y in zip(row, vector)), Fraction(0))


class ContextualZeroThirdObserver(unittest.TestCase):
    def test_two_polynomial_zeros_are_not_equal_as_forms(self):
        f = lambda x: x
        g = lambda x: x * x
        self.assertEqual((f(0), g(0)), (0, 0))
        self.assertEqual((f(2), g(2)), (2, 4))
        self.assertNotEqual(f(2), g(2))

    def test_third_reference_separates_a_zero_fiber(self):
        a, b = (0, 1, 0), (0, 0, 1)
        initial_window = (1, 0, 0)
        new_window = (0, 1, -1)
        redundant_window = (2, 0, 0)
        self.assertEqual((output(initial_window, a), output(initial_window, b)), (0, 0))
        self.assertEqual((output(new_window, a), output(new_window, b)), (1, -1))
        self.assertEqual((output(redundant_window, a), output(redundant_window, b)), (0, 0))

    def test_fixed_readout_boundary_defect_is_signed_probe_response(self):
        u = Fraction(3, 2)
        identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        ku = ((1, 0, u), (0, 1, -u), (0, 0, 1))
        ps = ((1, 0, 0),)
        bt = ((1,),)
        d0 = sub(product(ps, identity), product(bt, ps))
        du = sub(product(ps, ku), product(bt, ps))
        delta = product(ps, sub(ku, identity))
        self.assertEqual(d0, ((0, 0, 0),))
        self.assertEqual(du, ((0, 0, u),))
        self.assertEqual(sub(du, d0), delta)
        self.assertEqual(output(du[0], (3, 7, 1)), u)

    def test_energy_ledger_changes_distribution_not_total(self):
        u = Fraction(3, 2)
        ku = ((1, 0, u), (0, 1, -u), (0, 0, 1))
        e_total = ((1, 1, 0),)
        self.assertEqual(product(e_total, ku), e_total)
        before = (Fraction(2), Fraction(4), Fraction(1))
        after = tuple(output(row, before) for row in ku)
        self.assertEqual(after, (Fraction(7, 2), Fraction(5, 2), Fraction(1)))
        self.assertEqual(output(e_total[0], before), output(e_total[0], after))
        self.assertEqual(sub(product(e_total, ku), e_total), ((0, 0, 0),))
        self.assertGreater(u, 0)  # A paid energy transfer may have zero total-report defect.

    def test_zero_energy_transfer_can_leave_nonzero_passive_model_error(self):
        # No controlled probe is applied, but the x-only model omits the y -> x coupling.
        k = ((1, 1, 0), (0, 1, 0), (0, 0, 1))
        p = ((1, 0, 0),)
        self.assertEqual(sub(product(p, k), p), ((0, 1, 0),))
        self.assertEqual(output((0, 1, 0), (0, 3, 1)), 3)

    def test_full_mixed_chart_probing_defect_identity_and_mutant(self):
        p0 = ((1, 1), (0, 1))
        k0 = ((1, 2), (3, 4))
        b0 = ((2, 1), (0, 1))
        dp = ((0, 1), (1, 0))
        dk = ((1, 0), (0, 0))
        db = ((1, 0), (0, 0))
        pu, ku, bu = add(p0, dp), add(k0, dk), add(b0, db)
        e0 = sub(product(p0, k0), product(b0, p0))
        eu = sub(product(pu, ku), product(bu, pu))
        terms = (product(p0, dk), product(dp, k0), product(dp, dk),
                 neg(product(b0, dp)), neg(product(db, p0)), neg(product(db, dp)))
        rhs = ((0, 0), (0, 0))
        for t in terms:
            rhs = add(rhs, t)
        self.assertEqual(sub(eu, e0), rhs)
        mutant_without_cross_terms = ((0, 0), (0, 0))
        for i in (0, 1, 3, 4):
            mutant_without_cross_terms = add(mutant_without_cross_terms, terms[i])
        self.assertNotEqual(sub(eu, e0), mutant_without_cross_terms)

    def test_nonnegative_probe_cost_is_not_entropy(self):
        def cost(x, y):
            return (x + y) ** 2 + x ** 2 + y ** 2
        for x in range(-3, 4):
            for y in range(-3, 4):
                self.assertGreaterEqual(cost(x, y), 0)
                self.assertEqual(cost(x, y) == 0, (x, y) == (0, 0))
        # For an equiprobable binary hypothesis, a deterministic constant report
        # yields 0 bits, while an injective two-outcome report yields 1 bit.
        a, b = (0, 1, 0), (0, 0, 1)
        constant = (1, 0, 0)
        discriminating = (0, 1, -1)
        outcomes_constant = (output(constant, a), output(constant, b))
        outcomes_separating = (output(discriminating, a), output(discriminating, b))
        self.assertEqual(int(outcomes_constant[0] != outcomes_constant[1]), 0)
        self.assertEqual(int(outcomes_separating[0] != outcomes_separating[1]), 1)
        # A positive resource cost alone does not create information.
        self.assertGreater(cost(1, 0), 0)


if __name__ == "__main__":
    unittest.main()
