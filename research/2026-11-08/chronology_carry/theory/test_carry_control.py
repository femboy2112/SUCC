from fractions import Fraction as Q
from itertools import product
import unittest

from carry_control import (
    ZERO, add, append_operator, conditional_l2_identity, mean, norm_squared,
    literal_occupation_identity, occupation_identity, padded_vdc, poisson_compile, states, sub,
    transient_literal_poisson_compile,
    integer_lift_poisson_compile,
)


class CarryControlTests(unittest.TestCase):
    def test_poisson_all_small_tables_and_native_depth_two(self):
        for base, depth in [(2, 1), (2, 2), (3, 2), (16, 1), (16, 2)]:
            support = states(base, depth)
            for shift in range(4):
                table = {w: (Q((i + shift) % 7 - 3, 8), Q((i * 3 + shift) % 5 - 2, 16))
                         for i, w in enumerate(support)}
                compiled = poisson_compile(table, base, depth)
                evolved = table
                for _ in range(depth):
                    evolved = append_operator(evolved, base, depth)
                self.assertEqual(set(evolved.values()), {compiled["mean"]})
                self.assertTrue(all(sub(compiled["potential"][w],
                                        compiled["reference_potential"][w])
                                    == sub(table[w], compiled["mean"]) for w in support))

    def test_all_small_causal_paths_have_exact_occupation_identity(self):
        base, depth = 2, 2
        table = {w: (Q(i, 5), Q(i * i, 7)) for i, w in enumerate(states(base, depth))}
        for digits in product(range(base), repeat=8):
            path = tuple(tuple(digits[i:i + depth]) for i in range(len(digits) - depth + 1))
            result = occupation_identity(table, path, base, depth)
            self.assertEqual(result["actual"], add(result["mean"],
                             add(result["boundary"], result["innovation"])))

    def test_nonuniform_rows_can_have_zero_signed_innovation(self):
        table = {(0,): (Q(1), Q(0)), (1,): (Q(-1), Q(0))}
        path = tuple((i % 2,) for i in range(21))
        result = occupation_identity(table, path, 2, 1)
        self.assertEqual(result["innovation"], ZERO)
        self.assertEqual(result["boundary"], ZERO)
        # Both conditional rows are deterministic, TV=1/2 from uniform.
        self.assertEqual(Q(1, 2), sum(abs(q - Q(1, 2)) for q in [Q(0), Q(1)]) / 2)

    def test_padded_vdc_independent_exact_gram_routes(self):
        roots = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1))]
        for n in range(1, 12):
            values = tuple(roots[(i * i + 3 * i + n) % 4] for i in range(n))
            for horizon in range(1, n + 1):
                result = padded_vdc(values, horizon)
                self.assertGreaterEqual(result["upper_squared"], result["actual_mean_squared"])
        values = tuple((Q((-1) ** n), Q(0)) for n in range(100))
        result = padded_vdc(values, 20)
        self.assertEqual(sum(norm_squared(z) for z in values) / len(values), 1)
        self.assertLess(result["upper_squared"], Q(1, 500))

    def test_coherent_residual_cannot_disappear(self):
        values = ((Q(1), Q(0)),) * 50
        for horizon in [1, 2, 10, 25, 50]:
            self.assertGreaterEqual(padded_vdc(values, horizon)["upper_squared"], 1)

    def test_transferred_table_mismatch_is_not_training_risk(self):
        roots = [(Q(1), Q(0)), (Q(-1), Q(0)), (Q(0), Q(1)), (Q(0), Q(-1))]
        path = tuple((i % 3,) for i in range(12))
        values = tuple(roots[i % 4] for i in range(12))
        zero_table = {(i,): ZERO for i in range(3)}
        result = conditional_l2_identity(values, path, zero_table)
        self.assertEqual(result["risk"], 1)
        self.assertEqual(result["empirical_optimum"], 1)
        bad = {(i,): (Q(1, 2), Q(0)) for i in range(3)}
        result = conditional_l2_identity(values, path, bad)
        self.assertEqual(result["risk"], Q(5, 4))
        self.assertEqual(result["transferred_table_mismatch"], Q(1, 4))

    def test_invalid_input_is_rejected(self):
        with self.assertRaises(ValueError):
            poisson_compile({(0,): (1.0, 0.0)}, 2, 1)
        table = {w: ZERO for w in states(2, 2)}
        with self.assertRaises(ValueError):
            occupation_identity(table, [(0, 0), (1, 1)], 2, 2)
        for horizon in [0, 2, True]:
            with self.assertRaises(ValueError):
                padded_vdc([(Q(1), Q(0))], horizon)

    def test_original_four_pole_carry_completion_algebra(self):
        # A finite terminal-zero Green completion verifies the exact algebra;
        # this does not approximate an infinite normality claim.
        forcing = [Q(0)] + [Q(4, 8*n-7) - Q(2, 8*n-4)
                             - Q(1, 8*n-3) - Q(1, 8*n-2)
                             for n in range(1, 82)]
        states = [Q(0)]
        for r in forcing[1:]:
            states.append(16*states[-1] + r)
        tails = [Q(0)] * len(states)
        for n in range(len(states)-2, -1, -1):
            tails[n] = (tails[n+1] + forcing[n+1])/16
        y = [(u+t) % 1 for u, t in zip(states, tails)]
        j = [int(v<t) for v, t in zip(y, tails)]
        for n in range(1, len(states)):
            c = states[n].__floor__() - 16*states[n-1].__floor__()
            a = (16*y[n-1]).__floor__()
            self.assertEqual(c, a + 16*j[n-1] - j[n])
            self.assertEqual((states[n] % 1), y[n]-tails[n]+j[n])

    def test_literal_carry_spill_is_charged(self):
        table = {w: (Q(sum(w), 4), Q(w[0]-w[1], 8))
                 for w in product(range(3), repeat=2)}
        digits = [0, 1, 2, 0, 1, 1, 0]
        path = tuple(tuple(digits[i:i+2]) for i in range(len(digits)-1))
        result = literal_occupation_identity(table, path, base=2, depth=2)
        self.assertEqual(result["exceptional_words"], 2)
        self.assertNotEqual(result["literal_correction"], ZERO)
        self.assertEqual(result["literal_mean"],
                         add(result["actual"], result["literal_correction"]))

    def test_original_source_retrodictive_phase_identity_and_error(self):
        forcing = [Q(0)] + [Q(4, 8*n-7)-Q(2, 8*n-4)
                             -Q(1, 8*n-3)-Q(1, 8*n-2)
                             for n in range(1, 101)]
        x, carries = [Q(0)], [0]
        for r in forcing[1:]:
            value = 16*x[-1]+r
            carries.append(value.__floor__())
            x.append(value % 1)
        for n in [10, 23, 47, 80, 100]:
            for depth in range(1, 7):
                q = 16**depth
                k = sum(16**(depth-j)*carries[n-depth+j] for j in range(1, depth+1))
                f = sum((16**(depth-j)*forcing[n-depth+j]
                         for j in range(1, depth+1)), Q(0))
                self.assertEqual(q*x[n-depth], k-f+x[n])
                self.assertLessEqual(abs(Q(2*k+1, 2*q)-x[n-depth]), Q(1, 2*q)+f/q)
                self.assertLess(f/q, Q(1, 64*(n-depth)**2))

    def test_retrodictive_difference_has_paid_window_energy(self):
        roots = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1))]
        for n in [20, 40]:
            for depth in [1, 3, 7]:
                phases = [roots[(j*j+3*j+5) % 4] for j in range(n+depth)]
                difference = [sub(phases[j+depth], phases[j]) for j in range(n)]
                self.assertLessEqual(norm_squared(mean(difference)), Q(2*depth, n)**2)
                for horizon in [1, 2, 8, 16]:
                    v = padded_vdc(difference, horizon)["upper_squared"]
                    bound = Q(2*depth, horizon)*(1+Q(horizon-1, n))
                    self.assertLessEqual(v, bound*bound)

    def test_literal_transient_kernel_keeps_exceptional_states(self):
        for base, depth in [(2, 1), (2, 3), (16, 1), (16, 2)]:
            table = {w: (Q(sum(w), 7), Q(sum((j+1)*d for j, d in enumerate(w)), 11))
                     for w in states(base+1, depth)}
            compiled = transient_literal_poisson_compile(table, base, depth)
            ordinary_mean = mean(table[w] for w in states(base, depth))
            self.assertEqual(compiled["mean"], ordinary_mean)
            self.assertNotEqual(ordinary_mean, mean(table.values()))
            self.assertEqual(set(compiled["potential"]), set(table))
            for w in table:
                self.assertEqual(sub(compiled["potential"][w], compiled["reference_potential"][w]),
                                 sub(table[w], ordinary_mean))

    def test_integer_lift_quotient_preserves_literal_carry_and_potential(self):
        for base, depth in [(2, 3), (16, 2)]:
            q = base**depth
            def quotient(word):
                return sum(base**(depth-j-1)*d for j, d in enumerate(word)) % q
            values = [(Q(i % 7, 9), Q((i*i) % 5, 13)) for i in range(q)]
            literal = {w: values[quotient(w)] for w in states(base+1, depth)}
            large = transient_literal_poisson_compile(literal, base, depth)
            small = integer_lift_poisson_compile(values, base, depth)
            self.assertEqual(large["mean"], small["mean"])
            for w in literal:
                self.assertEqual(large["potential"][w], small["potential"][quotient(w)])
                for c in range(base+1):
                    self.assertEqual(quotient(w[1:]+(c,)), (base*quotient(w)+c) % q)
        # Independent symbol reduction would erase a genuine higher carry.
        self.assertEqual(quotient((0, 16)), 16)
        self.assertEqual(quotient((0, 0)), 0)


if __name__ == "__main__":
    unittest.main()
