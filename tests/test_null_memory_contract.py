"""Exact memory-neutral null controls and higher-order source-coupling calibrations.

All finite probabilities use Fractions. The stochastic source sign is a test
hypothesis class, NOT a probabilistic claim about deterministic pi digits.
"""
import unittest
from fractions import Fraction as Q
from itertools import product

SIGNS = (-1, 1)


def independent_sign_law():
    return {(theta, r): Q(1, 4) for theta, r in product(SIGNS, repeat=2)}


def source_mask_law():
    # Theta and R independent; observer already remembers M=R; Z=Theta*R.
    return {(theta, r, theta*r): Q(1, 4) for theta, r in product(SIGNS, repeat=2)}


def probability(law, predicate):
    return sum((v for row, v in law.items() if predicate(row)), Q())


def conditional(law, predicate, condition):
    den = probability(law, condition)
    if den == 0:
        raise ZeroDivisionError
    return probability(law, lambda row: condition(row) and predicate(row))/den


def mask_future_joint(reuse):
    # Stored R is currently independent of Theta. Future sensor may reuse
    # R or instead use a new independent R'. Distinguish them exactly.
    law = {}
    for theta, r, fresh in product(SIGNS, repeat=3):
        y = theta*(r if reuse else fresh)
        row = (theta, r, y)
        law[row] = law.get(row, Q()) + Q(1, 8)
    return law


def intervention_law(p):
    # A=R; B=Theta*(R if share else R'), exactly finite signed masks.
    p = Q(p)
    if not 0 <= p <= 1:
        raise ValueError
    law = {}
    for theta, r, fresh in product(SIGNS, repeat=3):
        for shared, ps in ((True, p), (False, 1-p)):
            row = (theta, r, theta*(r if shared else fresh))
            law[row] = law.get(row, Q()) + ps/Q(8)
    return law


class MemoryNullControlTests(unittest.TestCase):
    def test_unconditional_null_can_have_one_bit_conditional_information(self):
        law = source_mask_law()
        for theta, z in product(SIGNS, repeat=2):
            self.assertEqual(conditional(
                law, lambda v: v[2] == z, lambda v: v[0] == theta), Q(1, 2))
        for m, z in product(SIGNS, repeat=2):
            self.assertEqual(conditional(
                law, lambda v: v[0] == m*z,
                lambda v: v[1] == m and v[2] == z), 1)

    def test_fresh_independent_mask_preserves_current_posterior_given_memory(self):
        law = {(theta, m, z):Q(1,8)
               for theta, m, z in product(SIGNS, repeat=3)}
        for m, z, theta in product(SIGNS, repeat=3):
            post = conditional(law, lambda v: v[0] == theta,
                               lambda v: v[1] == m and v[2] == z)
            prior = conditional(law, lambda v: v[0] == theta,
                                lambda v: v[1] == m)
            self.assertEqual(post, prior)
            self.assertEqual(post, Q(1,2))

    def test_presently_null_mask_can_be_future_informative_if_reused(self):
        for reuse in (True, False):
            law = mask_future_joint(reuse)
            for theta, r in product(SIGNS, repeat=2):
                self.assertEqual(conditional(
                    law, lambda v: v[1] == r, lambda v: v[0] == theta),
                    Q(1,2))
            for r, y in product(SIGNS, repeat=2):
                p = conditional(law, lambda v: v[0] == r*y,
                                lambda v: v[1] == r and v[2] == y)
                self.assertEqual(p, Q(1) if reuse else Q(1,2))

    def test_source_independent_randomization_can_change_probe_selection(self):
        # Baseline always selects q_star; a source-blind fair coin
        # changing the decision policy reduces its selection rate.
        baseline = Q(1)
        coin_policy = sum((Q(1,2) for r in SIGNS if r == 1), Q())
        self.assertEqual(coin_policy, Q(1,2))
        self.assertNotEqual(baseline, coin_policy)

    def test_controllable_correlation_and_source_blind_single_channel(self):
        for p in (Q(0), Q(1,4), Q(1,2), Q(1)):
            law = intervention_law(p)
            self.assertEqual(sum(law.values()), 1)
            for theta in SIGNS:
                for channel in (1, 2):
                    for value in SIGNS:
                        self.assertEqual(conditional(
                            law, lambda row: row[channel] == value,
                            lambda row: row[0] == theta), Q(1,2))
                corr = conditional(
                    law, lambda row: row[1]*row[2] == theta,
                    lambda row: row[0] == theta)
                # Expectation theta*A*B = p; event +1 prob (1+p)/2.
                self.assertEqual(2*corr-1, p)

    def test_null_intervention_appears_source_blind_as_joint(self):
        law = intervention_law(0)
        for theta, a, b in product(SIGNS, repeat=3):
            self.assertEqual(conditional(
                law, lambda row: row[1] == a and row[2] == b,
                lambda row: row[0] == theta), Q(1,4))

    def test_retraction_keeps_memory_and_sources_separate(self):
        state = (("four_poles", "zero_seed", "prior_probe"), ("q1","q2"), 7)
        extended = (state, "fresh_source_independent_bit")
        self.assertEqual(extended[0],state)
        erased = ((), state[1], state[2])
        self.assertNotEqual(erased,state)

    def test_old_memory_conditioning_is_mandatory_not_decorative(self):
        law = source_mask_law()
        # Marginal likelihood of Z independent of theta, but joint
        # with retained M differs between hypotheses.
        for theta in SIGNS:
            self.assertEqual(conditional(
                law, lambda row: row[2] == 1,
                lambda row: row[0] == theta), Q(1,2))
            self.assertEqual(conditional(
                law, lambda row: row[1] == 1 and row[2] == theta,
                lambda row: row[0] == theta), Q(1,2))
            self.assertEqual(conditional(
                law, lambda row: row[1] == 1 and row[2] == -theta,
                lambda row: row[0] == theta), Q(0))


if __name__ == "__main__":
    unittest.main()
