"""Exact regressions for the additive two/three causal transport dossier."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "research/2026-11-18/two_three_causal_transport/probe.py"
SPEC = importlib.util.spec_from_file_location("two_three_causal_probe", PATH)
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


def matrix_polynomial(coefficients, matrix):
    size = len(matrix)
    out = [[0]*size for _ in range(size)]
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    for c in coefficients:
        out = [[out[i][j]+c*power[i][j] for j in range(size)] for i in range(size)]
        power = p.matmul(power, matrix)
    return out


class CausalTransportTests(unittest.TestCase):
    def test_actual_fibonacci_module_exposes_ternary_complement(self):
        m = [[0, 1], [1, -1]]
        self.assertEqual(matrix_polynomial(p.H, m), [[8, 1], [1, 7]])
        self.assertEqual(matrix_polynomial(p.K, m), [[0, 3], [3, -3]])
        self.assertEqual(matrix_polynomial(p.Q, m), [[7, -6], [-6, 13]])
        self.assertEqual(p.determinant(matrix_polynomial(p.H, m)), 55)
        self.assertEqual(p.determinant(matrix_polynomial(p.Q, m)), 55)
        for a in range(-8, 9):
            for b in range(-8, 9):
                initial = max(p.local_norm(a, 3), p.local_norm(b, 3))
                image = (3*b, 3*(a-b))
                self.assertEqual(max(p.local_norm(x, 3) for x in image), initial/3)
        # Keep the full constant-channel discrepancy in the pentagonal map.
        s = p.cyclic_matrix((0, 1), 5)
        st = [list(row) for row in zip(*s)]
        b = [[s[i][j]+st[i][j] for j in range(5)] for i in range(5)]
        d = [[int(i == 2*j % 5) for j in range(5)] for i in range(5)]
        dt = [list(row) for row in zip(*d)]
        h = p.cyclic_matrix(p.H, 5)
        gram = p.matmul([list(row) for row in zip(*h)], h)
        transported = p.matmul(p.matmul(d, matrix_polynomial(p.Q, b)), dt)
        self.assertEqual([[gram[i][j]-transported[i][j] for j in range(5)]
                          for i in range(5)], [[57]*5 for _ in range(5)])
        self.assertTrue(all(sum(row) == 225 for row in gram))

    def test_declared_quartic_fibonacci_lift_and_sign_control(self):
        a4 = [[1, 4, 6, 4, 1], [1, 3, 3, 1, 0], [1, 2, 1, 0, 0],
              [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
        lift = lambda a, b: [[a**(4-j)*b**j] for j in range(5)]
        for a in range(-12, 13):
            for b in range(-12, 13):
                self.assertEqual(p.matmul(a4, lift(a, b)), lift(a+b, a))
                self.assertEqual(lift(a, b), lift(-a, -b))
        char = p.poly_mul(p.poly_mul((-1, 1), (1, 3, 1)), (1, -7, 1))
        self.assertEqual(matrix_polynomial(char, a4), [[0]*5 for _ in range(5)])
        self.assertEqual(p.determinant(a4), 1)  # five channels do not force a 5-adic defect

    def test_literal_source_cycle_retains_free_constant_and_torsion(self):
        for blocks in (1, 2, 3):
            n, d = 8*blocks, 16**blocks-1
            a = p.cyclic_matrix(p.Q, n)
            self.assertTrue(all(sum(row) == 0 for row in a))
            self.assertTrue(all(sum(col) == 0 for col in zip(*a)))
            cofactor = [row[1:] for row in a[1:]]
            self.assertEqual(p.determinant(cofactor), d**4//15)
            # Forgetting (1-t) would incorrectly remove this free constant channel.
            self.assertNotEqual(p.determinant(p.cyclic_matrix(p.H, n)), 0)

    def test_all_block_boundary_smith_certificate(self):
        for blocks in range(1, 5):
            n = 8*blocks
            coeff = p.block_complement(blocks)
            self.assertEqual(p.poly_mul(p.H, coeff), (16**blocks,)+(0,)*(n-1)+(-1,))
            for matrix_builder, denominator in ((p.cyclic_matrix, 16**blocks-1),
                                                (p.causal_matrix, 16**blocks)):
                a = matrix_builder(p.H, n)
                b = matrix_builder(coeff, n)
                self.assertEqual(p.matmul(a, b), [[denominator*int(i == j) for j in range(n)] for i in range(n)])
                self.assertEqual(p.determinant(a), denominator**4)
                minor = [row[:n-4] for row in a[4:]]
                self.assertEqual(p.determinant(minor), 1)
            self.assertEqual(p.vp_integer(16**blocks-1, 3), 1+p.vp_integer(blocks, 3))
            self.assertEqual(p.vp_integer(16**blocks-1, 5), 1+p.vp_integer(blocks, 5))

    def test_radix_factor_and_causal_inverse(self):
        self.assertEqual(p.poly_mul(p.H, p.K), (16, 0, 0, 0, 0, 0, 0, 0, -1))
        for n in range(1, 34):
            a = p.causal_matrix(p.H, n)
            inv = p.causal_matrix(p.causal_inverse_coefficients(n), n)
            self.assertEqual(p.matmul(a, inv), [[int(i == j) for j in range(n)] for i in range(n)])
            self.assertEqual(p.determinant(a), 4**n)
            q, r = divmod(n-1, 8)
            loss = 4*q+2+int(r >= 3)+int(r >= 4)
            self.assertEqual(max(p.local_norm(x, 2) for x in inv[-1]), 2**loss)
            self.assertLessEqual(sum(abs(x) for x in inv[-1]), Fraction(11, 15))
        self.assertEqual(p.matmul(p.cyclic_matrix(p.H, 8), p.cyclic_matrix(p.K, 8)),
                         [[15*int(i == j) for j in range(8)] for i in range(8)])
        self.assertEqual(p.matmul(p.causal_matrix(p.H, 8), p.causal_matrix(p.K, 8)),
                         [[16*int(i == j) for j in range(8)] for i in range(8)])

    def test_causal_hidden_tail_bits(self):
        for n in range(1, 20):
            for coefficients in (p.H, p.Q):
                a = p.causal_matrix(coefficients, n)
                self.assertEqual(p.determinant(a), 4**n)
                for j in range(n):
                    image = [a[i][j] % 2 for i in range(n)]
                    self.assertEqual(any(image), j+4 < n)
            # Explicit positive control: the oldest input appears after four samples.
            if n >= 5:
                self.assertEqual(p.causal_matrix(p.H, n)[4][0] % 2, 1)

    def test_compact_ternary_height_and_signed_mutation(self):
        states = p.bbp_states(1536)
        for n in range(1, len(states)):
            height, scale, modulus, unit = p.ternary_height_certificate(n)
            self.assertEqual(p.local_norm(states[n], 3), height)
            self.assertEqual(p.residue(scale*states[n], modulus), unit)
            self.assertGreater(9*height, 4*n)
            self.assertLessEqual(height, 8*n)
        mutant = p.forcing(1)+Fraction(2, 6)
        self.assertEqual(p.local_norm(mutant, 3), 3)  # height alone misses it
        self.assertNotEqual(p.residue(3*mutant, 3), 1)

    def test_snapshot_period_obstruction_and_close_shadow_control(self):
        for depth in range(1, 16):
            denominator = 3**depth
            period = 3**(depth-1)
            self.assertEqual(pow(16, period, denominator), 1)
            if depth > 1:
                self.assertNotEqual(pow(16, period//3, denominator), 1)
            # Increasing exact period still permits real distance to zero tending to zero.
            self.assertLessEqual(Fraction(1, denominator), Fraction(1, 3))
        # The forced continuation differs from the autonomous orbit of a snapshot.
        states = p.bbp_states(2)
        self.assertEqual((16*states[1]-states[1]).denominator, 1)
        self.assertNotEqual((states[2]-16*states[1]).denominator, 1)

    def test_full_exact_certificate(self):
        result = p.finite_certificate()
        self.assertEqual(result["positive_odd_valuation_words"], 5460)
        self.assertEqual(result["terminal_memory_identities"], 30948)

    def test_source_mutation_is_detected(self):
        mutant = (4, 4, 4, 2, 2)
        self.assertNotEqual(p.poly_mul((1, -1), mutant), p.Q)
        self.assertNotEqual(p.determinant(p.cyclic_matrix(mutant, 5)), 825)

    def test_cyclic_closure_cannot_replace_mellin_boundary(self):
        # Q(t) mod(t^5-1) = 3-2t^3-t^4. Its deleted term has source-sized mass.
        reduced = (3, 0, 0, -2, -1)
        for n in (1, 2, 7, 31, 257, 1025):
            loss = p.forcing(n)-p.moment(reduced, 8*n-8)
            self.assertEqual(loss, Fraction(5, (8*n-7)*(8*n-2)))
            self.assertGreater(loss, 0)
        for m, (d, g, j) in p.INVERSES.items():
            defect = list(p.poly_mul(p.H, g))
            defect[0] -= d
            for exponent in (0, 8, 80, 800):
                self.assertNotEqual(p.moment(defect, exponent), 0)

    def test_inverse_precision_loss_is_sharp(self):
        for m, (d, g, _) in p.INVERSES.items():
            for prime in (2, 3, 5, 11):
                loss = p.vp_integer(d, prime)
                self.assertEqual(min(p.vp_integer(c, prime) for c in g if c), 0)
                product = p.matmul(p.cyclic_matrix(p.H, m), [[c] for c in g])
                self.assertEqual(product, [[d]]+[[0]]*(m-1))
                if loss:
                    self.assertTrue(all(row[0] % prime**loss == 0 for row in product))
                    self.assertTrue(any(c % prime != 0 for c in g))

    def test_order_is_not_total_valuation(self):
        left, w1 = p.syracuse_trace(11, 2)
        right, w2 = p.syracuse_trace(9, 2)
        self.assertEqual(w1, (1, 2))
        self.assertEqual(w2, (2, 1))
        self.assertEqual(sum(w1), sum(w2))
        self.assertNotEqual(left[-1] % 9, right[-1] % 9)

    def test_local_slopes_satisfy_product_formula(self):
        for word in ((1,), (2,), (1, 2), (2, 1), (1, 3, 2, 4)):
            slope = Fraction(3**len(word), 2**sum(word))
            self.assertEqual(slope*p.local_norm(slope, 2)*p.local_norm(slope, 3), 1)
        for length in range(1, 20):
            slope = Fraction(16**length)
            self.assertEqual(slope*p.local_norm(slope, 2)*p.local_norm(slope, 3), 1)
            self.assertEqual(p.local_norm(slope, 3), 1)

    def test_mod_three_newest_binary_division_parity(self):
        for n in range(1, 2000, 2):
            trace, word = p.syracuse_trace(n, 1)
            self.assertEqual(trace[-1] % 3, pow(2, word[0], 3))

    def test_rational_seed_local_alias_and_mutations(self):
        # This confirms local indistinguishability, not a changed normality theorem.
        seed = Fraction(2**7*3**4*17, 5**8)
        for n in range(40):
            difference = 16**n*seed
            self.assertGreaterEqual(p.vp(difference, 2), 7)
            self.assertGreaterEqual(p.vp(difference, 3), 4)
        self.assertLess(p.vp(seed/Fraction(3), 3), 4)
        with self.assertRaises(ValueError):
            p.terminal_ternary((1, 2), 3)
        with self.assertRaises(ValueError):
            p.recent_window(3, 4)
        with self.assertRaises(ValueError):
            p.residue(Fraction(1, 3), 9)


if __name__ == "__main__":
    unittest.main()
