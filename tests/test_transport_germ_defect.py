"""Exact finite controls: source-typed analytic seed and transported observer defect.

Paper theorem scope: a declared boost/chart/ODE law. The tests do not establish
a physical observer, a prime analytic-time flow, or pi normality.
"""
from fractions import Fraction as F
import unittest


ZETA_MINUS_ONE = -F(1, 12)


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))


def prime_inventory_seed(primes):
    """True finite Euler/Hurwitz inventory state, with an oriented boost jet."""
    if len(primes) != len(set(primes)) or not all(is_prime(p) for p in primes):
        raise ValueError("source passport must contain distinct genuine primes")
    e = F(1)
    for p in primes:
        e /= F(1 - p)
    r = ZETA_MINUS_ONE / e
    u = (e + r) / 2
    q = -(e - r) / 2  # du/dt in the declared auxiliary boost clock
    return u, q


def exact_prime_step(jet, p):
    """Discrete genuine-prime step: sign parity plus hyperbolic boost."""
    if not is_prime(p):
        raise ValueError("only a genuine new prime step may be passed")
    u, q = map(F, jet)
    m = F(p - 1)
    ch, sh = (m + 1 / m) / 2, (m - 1 / m) / 2
    return (-ch * u - sh * q, -sh * u - ch * q)


def source_U(t, s):
    """Polynomial propagator for nilpotent K=[[0,1],[0,0]]."""
    h = F(t) - F(s)
    return ((F(1), h), (F(0), F(1)))


def row_times(row, mat):
    return tuple(sum((F(row[i]) * F(mat[i][j]) for i in range(2)), F(0))
                 for j in range(2))


def row_sub(a, b):
    return tuple(F(x) - F(y) for x, y in zip(a, b))


def row_add(a, b):
    return tuple(F(x) + F(y) for x, y in zip(a, b))


def readout(t):
    return (F(t), F(1))


def interval_defect(t, s):
    return row_sub(row_times(readout(t), source_U(t, s)), readout(s))


def integrated_defect(t, s):
    """Exact integral of E(r)U(r,s), with E(r)=(1,r)."""
    t, s = F(t), F(s)
    return (t - s, t * (t - s))


class TransportedGermDefectTests(unittest.TestCase):
    def test_true_prime_inventory_alias_has_opposite_differential(self):
        a = prime_inventory_seed((3,))
        b = prime_inventory_seed((2, 7))
        self.assertEqual(a, (F(-1, 6), F(1, 3)))
        self.assertEqual(b, (F(-1, 6), F(-1, 3)))
        self.assertEqual(a[0], b[0])
        self.assertNotEqual(a[1], b[1])
        self.assertEqual(a[0] ** 2 - a[1] ** 2, ZETA_MINUS_ONE)
        self.assertEqual(b[0] ** 2 - b[1] ** 2, ZETA_MINUS_ONE)

    def test_transferred_differential_predicts_distinct_future(self):
        a = exact_prime_step(prime_inventory_seed((3,)), 5)
        b = exact_prime_step(prime_inventory_seed((2, 7)), 5)
        self.assertEqual(a[0], F(-13, 48))
        self.assertEqual(b[0], F(47, 48))
        self.assertEqual(b[0] - a[0], F(5, 4))
        self.assertEqual((b[0] - a[0]) / 2, F(5, 8))
        self.assertEqual(a, prime_inventory_seed((3, 5)))
        self.assertEqual(b, prime_inventory_seed((2, 7, 5)))
        wrong_sign = exact_prime_step((F(-1, 6), F(-1, 3)), 5)
        self.assertNotEqual(a[0], wrong_sign[0])

    def test_composition_and_source_passport(self):
        base = prime_inventory_seed(())
        first = exact_prime_step(exact_prime_step(base, 3), 5)
        second = exact_prime_step(exact_prime_step(base, 5), 3)
        self.assertEqual(first, second)
        self.assertEqual(first, prime_inventory_seed((3, 5)))
        self.assertEqual(exact_prime_step(base, 2), tuple(-v for v in base))
        self.assertEqual(exact_prime_step(base, 2), prime_inventory_seed((2,)))
        for fake in (1, 4, 6, 9):
            with self.assertRaises(ValueError):
                exact_prime_step(base, fake)
        with self.assertRaises(ValueError):
            prime_inventory_seed((2, 3, 6))
        with self.assertRaises(ValueError):
            prime_inventory_seed((3, 3))

    def test_moving_chart_differential_and_integrated_defect(self):
        for a, b in ((F(0), F(3, 2)), (F(1, 2), F(4, 3)),
                     (F(-1, 2), F(5, 4))):
            # P'=(1,0); P K=(0,t). Omitting P' loses the first coordinate.
            self.assertEqual(interval_defect(b, a), integrated_defect(b, a))
            self.assertEqual(interval_defect(b, a)[0], b - a)
            self.assertNotEqual(interval_defect(b, a)[0], F(0))

    def test_signed_intermediate_defect_transport(self):
        for a, b, c in ((F(0), F(1, 2), F(3, 2)),
                        (F(1, 7), F(2, 3), F(7, 4))):
            direct = interval_defect(c, a)
            staged = row_add(row_times(interval_defect(c, b), source_U(b, a)),
                             interval_defect(b, a))  # observer L(c,b)=I
            self.assertEqual(direct, staged)

    def test_unrestricted_finite_jet_cannot_continue_an_arbitrary_germ(self):
        # 0 and t^(m+1) agree through derivative m at t=0, disagree at t=1.
        for m in range(0, 7):
            # coefficient of t^k for 0<=k<=m is zero in both polynomials
            coeffs_f = [F(0)] * (m + 2)
            coeffs_g = [F(0)] * (m + 1) + [F(1)]
            self.assertEqual(coeffs_f[:m + 1], coeffs_g[:m + 1])
            self.assertNotEqual(sum(coeffs_f), sum(coeffs_g))

    def test_real_lift_derivative_detects_integer_deck_alias(self):
        # The log-derivative divided by 2*pi*i*log(16) is 16^n*x.
        # No floating exp/pi or invented numerical derivative is evaluated.
        x = F(1, 16)
        for n in range(0, 9):
            for k in (-16, -1, 1, 16):
                log_d_x = 16 ** n * x
                log_d_xk = 16 ** n * (x + k)
                self.assertEqual(log_d_xk - log_d_x, k * 16 ** n)
                self.assertEqual((k * 16 ** n).denominator if isinstance(
                    k * 16 ** n, F) else 1, 1)
                self.assertEqual(15 * k * 16 ** n,
                                 k * (16 ** (n + 1) - 16 ** n))


if __name__ == "__main__":
    unittest.main()
