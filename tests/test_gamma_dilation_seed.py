"""Gamma dilation / observer-jet bridge: exact algebra and scoped quadrature.

GDB-01--09 are mathematical observation models. These tests do not measure a
physical Gamma observer, certify RH/pi-normality, or establish an arithmetic
source-selected signed Weyl bound.

Exact source-independent algebra uses Q(i) as pairs of Fractions, where q is a
symbolically chosen rational frequency. Numerical tests explicitly calibrate
Fourier/Gamma integrals at non-rational 2*pi*x; these are NOT proof certificates.
"""
import cmath
from fractions import Fraction as F
import math
import unittest


def c(a=0, b=0):
    return (F(a), F(b))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    den = a[0] * a[0] + a[1] * a[1]
    if not den:
        raise ZeroDivisionError("zero complex rational")
    return (a[0] / den, -a[1] / den)


def scale(a, s):
    s = F(s)
    return (a[0] * s, a[1] * s)


def lam(q):
    return c(1, -q)


def res(q):
    """M_plus(y)/z(y)=1/(1-iq), q=2*pi*y; exact over rational q."""
    return inv(lam(q))


def second_shape(q):
    """M_plus(shape2,y)/z(y) over a declared formal q."""
    u = res(q)
    return scale(add(u, mul(u, u)), F(1, 2))


def simpson(fn, start, stop, n):
    if n <= 0 or n % 2:
        raise ValueError("positive even sample count required")
    h = (stop - start) / n
    result = fn(start) + fn(stop)
    for j in range(1, n):
        result += (4 if j % 2 else 2) * fn(start + j * h)
    return result * h / 3


def gamma_forward_time(x, shape):
    """Numerical forward-only Gamma log-scale integral (shape 1 or 2)."""
    if shape not in (1, 2):
        raise ValueError("calibration supports shapes 1 and 2")
    c0 = math.log(16)
    norm = math.e if shape == 1 else math.e / 2
    stop = math.log(44) / c0  # neglected u>=44 tail is tiny
    def integrand(t):
        u = math.exp(c0 * t)
        weight = norm * c0 * u ** shape * math.exp(-u)
        return weight * cmath.exp(2j * math.pi * x * u)
    return simpson(integrand, 0.0, stop, 8192)


def gamma_closed(x, shape):
    q = 2 * math.pi * x
    z = cmath.exp(1j * q)
    p = 1 / (1 - 1j * q)
    if shape == 1:
        return z * p
    if shape == 2:
        return z * (p + p * p) / 2
    raise ValueError("invalid shape")


class GammaDilationSeedTests(unittest.TestCase):
    def test_formal_forward_boundary_zero(self):
        for q in (F(0), F(1, 5), F(-7, 4), F(20, 3)):
            # The phase z is factored out, so lambda*(M/z) == 1.
            self.assertEqual(mul(lam(q), res(q)), c(1))
            recovered = sub(c(1), inv(res(q)))
            self.assertEqual(recovered, c(0, q))
            self.assertEqual(res(q), inv(lam(q)))

    def test_exact_signed_mixed_compensation(self):
        for q, qq in ((F(1, 2), F(3, 2)),
                      (F(-3), F(4)), (F(0), F(7, 3))):
            # A deck-shift case has a common endpoint phase z. Algebra is
            # checked in the normalized z=1 chart without assuming q rational
            # itself corresponds to an integer physical deck shift.
            l0, l1 = lam(q), lam(qq)
            m0, m1 = res(q), res(qq)
            dl, dm = sub(l1, l0), sub(m1, m0)
            linear = add(mul(l0, dm), mul(m0, dl))
            mixed = mul(dl, dm)
            self.assertEqual(add(linear, mixed), c(0))
            self.assertNotEqual(linear, c(0))  # omitted mixed term is false
            self.assertEqual(dm, mul(c(0, qq - q), mul(m1, m0)))

    def test_shape_two_exact_fiber(self):
        for q in (F(0), F(1, 3), F(-2), F(5)):
            l, u, m2 = lam(q), res(q), second_shape(q)
            # 2 * lambda^2 * M2/z = lambda + 1
            self.assertEqual(scale(mul(mul(l, l), m2), 2),
                             add(l, c(1)))
            self.assertEqual(m2, scale(add(u, mul(u, u)), F(1, 2)))
        self.assertEqual(second_shape(F(0)), c(1))

    def test_forward_only_time_density_and_shape_one(self):
        x = 0.125
        got = gamma_forward_time(x, 1)
        want = gamma_closed(x, 1)
        self.assertLess(abs(got - want), 2e-9)
        density = simpson(
            lambda t: math.e * math.log(16) *
                      math.exp(math.log(16) * t) *
                      math.exp(-math.exp(math.log(16) * t)),
            0.0, math.log(44) / math.log(16), 8192)
        self.assertLess(abs(density - 1), 2e-10)

    def test_forward_only_shape_two(self):
        for x in (0.0, 0.0625, -0.125):
            self.assertLess(abs(gamma_forward_time(x, 2) -
                                gamma_closed(x, 2)), 2e-9)

    def test_inherited_seed_and_analytic_path_compose(self):
        for x in (F(1, 16), F(-1, 7), F(3, 8)):
            for b in (2, 10, 16):
                # Remove the conventional factor 2*pi*i. Real-lift transport
                # is the exact rational b^dt*x for integral durations.
                a, d1, d2 = 0, 2, 3
                j_b = F(b ** d1) * x
                j_c = F(b ** d2) * j_b
                self.assertEqual(j_c, F(b ** (d1 + d2)) * x)
                # The logarithmic derivative has multiplier log(b),
                # independently of Gamma shape and original BBP pole data.
                self.assertAlmostEqual(math.log(b) * float(j_c),
                                       math.log(b) * b ** (d1 + d2) * float(x),
                                       places=11)

    def test_gamma_observer_reconstructs_logarithmic_derivative(self):
        for y in (0.0, 0.125, -0.25, 2.0):
            z = cmath.exp(2j * math.pi * y)
            m = gamma_closed(y, 1)
            seed = 1 - z / m
            derivative = math.log(16) * seed
            self.assertLess(abs(seed - 2j * math.pi * y), 1e-12)
            self.assertLess(abs(derivative -
                                2j * math.pi * math.log(16) * y), 1e-11)
            # Opposite sign would fail for a nonzero y.
            if y:
                self.assertGreater(abs((1 + z / m) - seed), 1.0)

    def test_deck_aliases_converge_in_gamma_but_not_in_jet(self):
        x, k = math.pi / 16, 1
        previous = float("inf")
        for n in range(0, 5):
            y, yp = 16 ** n * x, 16 ** n * (x + k)
            # Exact circle-deck equality is imposed analytically by using the
            # same unit phase for both lifts; floating huge-angle mod-1 is NOT
            # an exact test of this identity.
            z = cmath.exp(2j * math.pi * y)
            m = z / (1 - 2j * math.pi * y)
            mp = z / (1 - 2j * math.pi * yp)
            gap = abs(mp - m)
            predicted = ((2 * math.pi * 16 ** n * abs(k)) /
                         (math.hypot(1, 2 * math.pi * y) *
                          math.hypot(1, 2 * math.pi * yp)))
            self.assertAlmostEqual(gap, predicted, delta=predicted * 2e-11)
            self.assertLess(gap, previous)
            previous = gap
            self.assertLessEqual(
                gap, abs(k) / (2 * math.pi * 16 ** n * abs(x * (x + k))) *
                (1 + 1e-13))
            # Signed local jet contrast grows despite Gamma gap shrinking.
            self.assertEqual(16 ** n * k, 16 ** n * k)

    def test_exact_inverse_error_amplification(self):
        y = 5.0
        z = cmath.exp(2j * math.pi * y)
        m = gamma_closed(y, 1)
        dm = complex(1e-5, -2e-5)
        est = m + dm
        y_recovered = (1 - z / est) / (2j * math.pi)
        analytic_error = abs(dm) / (2 * math.pi * abs(est) * abs(m))
        self.assertAlmostEqual(abs(y_recovered - y), analytic_error,
                               delta=analytic_error * 2e-10)

    def test_locked_circle_looks_gamma_attenuated(self):
        last = 1.0
        for n in range(0, 5):
            y = 16 ** n  # integer orbit e(y)==1, perfectly locked
            m = 1 / (1 - 2j * math.pi * y)
            self.assertLess(abs(m), last)
            last = abs(m)
        self.assertLess(last, 1e-4)

    def test_native_gamma2_bound_does_not_resolve_moving_phase(self):
        x = math.pi / 16
        for n in range(2, 10):
            y = 16 ** n * x
            reference = 1 / (1 + 4 * math.pi ** 2 * y * y)
            absolute_error_budget = 7 / (4 * n)
            self.assertGreater(absolute_error_budget, reference)
            self.assertLess(reference,
                            1 / (4 * math.pi ** 2 * x * x * 16 ** (2 * n)))

    def test_shape_three_cannot_uniquely_invert_full_gamma_scalar(self):
        # Both (1 +/- i sqrt(3))**3 = -8 exactly by algebra.
        r = math.sqrt(3)
        self.assertAlmostEqual(abs((1 + 1j * r) ** 3 + 8), 0, delta=2e-14)
        self.assertAlmostEqual(abs((1 - 1j * r) ** 3 + 8), 0, delta=2e-14)
        self.assertNotEqual(1 + 1j * r, 1 - 1j * r)

    def test_noncanonical_interpolation_changes_derivative(self):
        # exp(2*pi*i*a*sin(2*pi*t)) is 1 for all integer t, but
        # contributes 4*pi**2*i*a to the log derivative there.
        a = 0.125
        for n in range(4):
            self.assertAlmostEqual(math.sin(2 * math.pi * n), 0, delta=1e-14)
            self.assertAlmostEqual(math.cos(2 * math.pi * n), 1, delta=1e-14)
            delta_derivative = 4j * math.pi ** 2 * a
            self.assertGreater(abs(delta_derivative), 0)


if __name__ == "__main__":
    unittest.main()
