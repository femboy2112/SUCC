"""Independent exact countermodel oracles for NO_GHOST/GLUING_REPAIR.md.

These enumerate finite fixtures; general claims have paper proofs in the dossier.
No imported solver is used to verify its own certificates.
"""

from fractions import Fraction
from itertools import permutations, product
import unittest


class NoGhostGluingExamples(unittest.TestCase):
    def test_destructive_shared_original_is_not_joint_execution(self):
        def a(state):
            x, y = state
            return x, (x, 0)

        def b(state):
            x, y = state
            return y, (0, y)

        self.assertEqual(a((1, 1))[0], 1)
        self.assertEqual(b((1, 1))[0], 1)
        for first, second in ((a, b), (b, a)):
            receipt1, state = first((1, 1))
            receipt2, _ = second(state)
            self.assertEqual((receipt1, receipt2), (1, 0))

    def test_projected_boundary_has_no_private_glue(self):
        left, right = {0}, {1}
        quotient = lambda _private: "same public interface"
        self.assertEqual(set(map(quotient, left)), set(map(quotient, right)))
        self.assertEqual(left & right, set())

    def test_parity_dual_inequality(self):
        equal = {(0, 0), (1, 1)}
        different = {(0, 1), (1, 0)}
        for support in (equal, different):
            self.assertEqual({x for x, _ in support}, {0, 1})
            self.assertEqual({y for _, y in support}, {0, 1})
        scores = []
        lawful = []
        for x, y, z in product(range(2), repeat=3):
            score = int(x == y) + int(y == z) + int(x != z)
            scores.append(score)
            if (x, y) in equal and (y, z) in equal and (x, z) in different:
                lawful.append((x, y, z))
        self.assertEqual(lawful, [])
        self.assertEqual(max(scores), 2)
        requested_expectation = Fraction(1) + Fraction(1) + Fraction(1)
        self.assertGreater(requested_expectation, max(scores))

    def test_nonregular_deck_invariance_does_not_descend(self):
        # Vertices and fiber values are 0,1,2; monodromies generate S3.
        red, blue = (1, 0, 2), (0, 2, 1)

        def compose(p, q):
            return tuple(p[q[i]] for i in range(3))

        deck = [
            p for p in permutations(range(3))
            if compose(p, red) == compose(red, p)
            and compose(p, blue) == compose(blue, p)
        ]
        self.assertEqual(deck, [(0, 1, 2)])
        lifted_section = (0, 1, 2)
        for monodromy in (red, blue):
            for i in range(3):
                self.assertEqual(lifted_section[monodromy[i]], monodromy[lifted_section[i]])
        self.assertEqual([x for x in range(3) if red[x] == x and blue[x] == x], [])

    def test_fixed_fair_coin_rejects_supported_point_mass(self):
        support = {0, 1}
        proposed = {0: Fraction(1), 1: Fraction(0)}
        actual = {0: Fraction(1, 2), 1: Fraction(1, 2)}
        self.assertTrue(all(x in support for x, mass in proposed.items() if mass))
        self.assertNotEqual(proposed, actual)

    def test_source_prior_and_private_flow_do_not_prevent_hidden_oracle(self):
        oracle = {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)}
        self.assertEqual(sum(oracle.values()), 1)
        self.assertEqual(sum(m for (source, _), m in oracle.items() if source == 0), Fraction(1, 2))
        self.assertEqual(sum(m for (source, guess), m in oracle.items() if source == guess), 1)
        for numerator in range(9):
            q = Fraction(numerator, 8)
            operational = {
                (source, guess): Fraction(1, 2) * (q if guess == 0 else 1 - q)
                for source, guess in product(range(2), repeat=2)
            }
            success = sum(m for (source, guess), m in operational.items() if source == guess)
            self.assertEqual(success, Fraction(1, 2))

    def test_join_tree_conditional_product_on_lawful_atoms(self):
        # x-y and y-z are a tree. All atoms require x=y; z remains random.
        mu_xy = {(0, 0): Fraction(1, 3), (1, 1): Fraction(2, 3)}
        mu_yz = {(0, 0): Fraction(1, 6), (0, 1): Fraction(1, 6),
                 (1, 0): Fraction(1, 2), (1, 1): Fraction(1, 6)}
        nu_y = {y: sum(m for (_, yy), m in mu_xy.items() if yy == y) for y in range(2)}
        coupling = {}
        for x, y, z in product(range(2), repeat=3):
            coupling[x, y, z] = mu_xy.get((x, y), 0) * mu_yz.get((y, z), 0) / nu_y[y]
        self.assertEqual(sum(coupling.values()), 1)
        self.assertTrue(all(x == y for (x, y, _), m in coupling.items() if m))
        for xy, mass in mu_xy.items():
            self.assertEqual(sum(m for (x, y, _), m in coupling.items() if (x, y) == xy), mass)
        for yz, mass in mu_yz.items():
            self.assertEqual(sum(m for (_, y, z), m in coupling.items() if (y, z) == yz), mass)

    def test_incomparable_exact_legal_sensor_repairs(self):
        # Adequacy asks to separate states 0 and 2, with state 1 unspecified.
        sensors = {"baseline": (0, 0, 0), "A": (0, 1, 1), "B": (0, 0, 1)}

        def refines(fine, coarse):
            return all(fine[i] != fine[j] or coarse[i] == coarse[j]
                       for i, j in product(range(3), repeat=2))

        adequate = {name for name, q in sensors.items() if q[0] != q[2]}
        self.assertEqual(adequate, {"A", "B"})
        self.assertFalse(refines(sensors["A"], sensors["B"]))
        self.assertFalse(refines(sensors["B"], sensors["A"]))
        least = [name for name in adequate if all(refines(sensors[other], sensors[name])
                                                for other in adequate)]
        self.assertEqual(least, [])


if __name__ == "__main__":
    unittest.main()
