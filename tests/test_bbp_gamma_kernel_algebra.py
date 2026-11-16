"""Independent exact checks for the source Gamma convolution algebra.

The global polynomial oracle and the direct convolution-jet oracle do
not use the production Laurent-expansion algorithm.  Optional SymPy
checks provide an additional, separately implemented partial fraction
calculation; the required checks have no third-party dependency.
"""

from dataclasses import FrozenInstanceError
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ import bbp_gamma_kernel_algebra as g


# Keep literal source data independent of the production constants.
SHIFTS = (0, 3, 4, 5)
RESIDUES = (4, -2, -1, -1)


def multiply(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return tuple(out)


def polynomial_power(polynomial, power):
    out = (Q(1),)
    for _ in range(power):
        out = multiply(out, polynomial)
    return out


def sum_polynomials(polynomials):
    polynomials = tuple(polynomials)
    out = [Q(0)] * max(map(len, polynomials))
    for polynomial in polynomials:
        for i, coefficient in enumerate(polynomial):
            out[i] += coefficient
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def cleared_term(shift, order, coefficient, power):
    """Multiply C/(a+d)**k by product_e(a+e)**power directly."""
    out = (Q(coefficient),)
    for d in SHIFTS:
        out = multiply(out, polynomial_power((Q(d), Q(1)),
                                            power - order if d == shift else power))
    return out


def original_numerator():
    return sum_polynomials(cleared_term(d, 1, c, 1)
                           for d, c in zip(SHIFTS, RESIDUES))


def original_jets(through, residues=RESIDUES):
    return tuple(sum((Q(c * (-d) ** m, factorial(m))
                      for d, c in zip(SHIFTS, residues)), Q(0))
                 for m in range(through + 1))


def convolve_jets(left, right, through):
    """Integrate monomials by the Beta identity, independently of poles."""
    out = [Q(0)] * (through + 1)
    for m, a in enumerate(left):
        for n in range(min(len(right), through - m)):
            out[m + n + 1] += (a * right[n]
                               * Q(factorial(m) * factorial(n), factorial(m + n + 1)))
    return tuple(out)


class SourceGammaKernelAlgebra(unittest.TestCase):
    def test_authentic_source_and_known_first_two_powers(self):
        self.assertEqual(g.SOURCE_SHIFTS, SHIFTS)
        self.assertEqual(g.SOURCE_RESIDUES, RESIDUES)
        self.assertEqual(original_numerator(), (Q(240), Q(121), Q(15)))
        self.assertEqual(tuple((t.shift, t.order, t.coefficient)
                               for t in g.source_kernel_power(1).terms),
                         tuple((d, 1, Q(c)) for d, c in zip(SHIFTS, RESIDUES)))
        self.assertEqual(tuple((t.shift, t.order, t.coefficient)
                               for t in g.source_kernel_power(2).terms),
                         ((0, 1, Q(-134, 15)), (0, 2, Q(16)),
                          (3, 1, Q(34, 3)), (3, 2, Q(4)),
                          (4, 1, Q(0)), (4, 2, Q(1)),
                          (5, 1, Q(-12, 5)), (5, 2, Q(1))))
        for term in g.source_kernel_power(2).terms:
            self.assertEqual(term.kernel_degree, term.order - 1)
            self.assertEqual(term.kernel_coefficient,
                             term.coefficient / factorial(term.order - 1))

    def test_all_budgeted_powers_by_global_rational_polynomial_identity(self):
        numerator = original_numerator()
        for power in range(1, g.MAX_POWER + 1):
            with self.subTest(power=power):
                kernel = g.source_kernel_power(power)
                cleared = sum_polynomials(
                    cleared_term(t.shift, t.order, t.coefficient, power)
                    for t in kernel.terms)
                self.assertEqual(cleared, polynomial_power(numerator, power))
                self.assertEqual(len(kernel.terms), 4 * power)
                self.assertEqual(tuple((t.shift, t.order) for t in kernel.terms),
                                 tuple((d, k) for d in SHIFTS for k in range(1, power + 1)))
                self.assertEqual(tuple(t.coefficient for t in kernel.terms
                                       if t.order == power),
                                 tuple(Q(c ** power) for c in RESIDUES))

    def test_exact_laplace_at_positive_rational_holdouts(self):
        for a in (Q(1, 13), Q(2, 7), Q(1), Q(5, 3), Q(17), Q(1001, 9)):
            source = Q(240 + 121 * a + 15 * a * a) / (a * (a+3) * (a+4) * (a+5))
            self.assertEqual(g.source_laplace(a), source)
            for power in range(1, g.MAX_POWER + 1):
                with self.subTest(a=a, power=power):
                    self.assertEqual(g.source_kernel_power(power).laplace(a), source ** power)

    def test_all_powers_against_direct_beta_convolution_jets(self):
        through = 2 * g.MAX_POWER + 4
        source = original_jets(through)
        jets = source
        for power in range(1, g.MAX_POWER + 1):
            with self.subTest(power=power):
                kernel = g.source_kernel_power(power)
                self.assertEqual(kernel.taylor_coefficients(through), jets)
                self.assertEqual(jets[:2 * power - 1], (Q(0),) * (2 * power - 1))
                self.assertEqual(jets[2 * power - 1],
                                 Q(15 ** power, factorial(2 * power - 1)))
                # The next coefficient is a second, independent source-moment check.
                self.assertEqual(jets[2 * power],
                                 Q(-59 * power * 15 ** (power - 1), factorial(2 * power)))
            jets = convolve_jets(jets, source, through)

    def test_high_taylor_degree_and_integer_laplace(self):
        kernel = g.source_kernel_power(1)
        self.assertEqual(kernel.taylor_coefficient(g.MAX_TAYLOR_DEGREE),
                         original_jets(g.MAX_TAYLOR_DEGREE)[-1])
        self.assertEqual(g.source_laplace(1), Q(47, 15))
        self.assertEqual(kernel.laplace(1), Q(47, 15))

    def test_hostile_sign_pole_and_collision_controls(self):
        authentic = g.source_kernel_power(2)
        # Turning every residue positive destroys the endpoint cancellation.
        wrong_source = original_jets(5, tuple(abs(c) for c in RESIDUES))
        wrong_squared = convolve_jets(wrong_source, wrong_source, 5)
        self.assertEqual(wrong_source[0], 8)
        self.assertEqual(wrong_squared[1], 64)
        self.assertNotEqual(wrong_squared, authentic.taylor_coefficients(5))
        # A misplaced pole is rejected by the global polynomial identity.
        bad_terms = list(authentic.terms)
        bad_terms[1] = g.PoleTerm(3, 2, bad_terms[1].coefficient)
        wrong_cleared = sum_polynomials(cleared_term(t.shift, t.order, t.coefficient, 2)
                                       for t in bad_terms)
        self.assertNotEqual(wrong_cleared, polynomial_power(original_numerator(), 2))
        # Pointwise kernel powers and convolution powers have different jets.
        pointwise = multiply(original_jets(5), original_jets(5))[:6]
        self.assertEqual(pointwise[2], 225)
        self.assertEqual(authentic.taylor_coefficient(2), 0)

    def test_guarded_budgets_exact_types_and_immutable_source(self):
        for bad in (0, -1, g.MAX_POWER + 1, True, False, 1.0, Q(1), "2", None):
            with self.subTest(power=bad):
                with self.assertRaises(ValueError):
                    g.source_kernel_power(bad)
                with self.assertRaises(ValueError):
                    g.GammaKernelPower(bad)
        kernel = g.source_kernel_power(1)
        for bad in (-1, g.MAX_TAYLOR_DEGREE + 1, True, 1.0, Q(1), "1", None):
            with self.subTest(degree=bad):
                with self.assertRaises(ValueError):
                    kernel.taylor_coefficient(bad)
                with self.assertRaises(ValueError):
                    kernel.taylor_coefficients(bad)
        for bad in (0, -1, Q(-1, 3), True, 1.0, "1", None):
            with self.subTest(a=bad):
                with self.assertRaises(ValueError):
                    g.source_laplace(bad)
                with self.assertRaises(ValueError):
                    kernel.laplace(bad)
        for args in ((1, 1, Q(1)), (True, 1, Q(1)), (0, 0, Q(1)),
                     (0, True, Q(1)), (0, 1, 1.0)):
            with self.assertRaises(ValueError):
                g.PoleTerm(*args)
        with self.assertRaises(FrozenInstanceError):
            kernel.terms = ()
        with self.assertRaises(FrozenInstanceError):
            kernel.terms[0].coefficient = Q(0)
        with self.assertRaises(TypeError):
            g.GammaKernelPower(1, terms=())

    def test_optional_sympy_partial_fraction_oracle(self):
        try:
            import sympy as sp
        except ImportError:
            self.skipTest("optional independent SymPy partial-fraction oracle unavailable")
        a = sp.Symbol("a")
        source = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5)
        for power in (1, 2, 3, 5):
            with self.subTest(power=power):
                independent = sp.apart(source ** power, a)
                production = sum(sp.Rational(t.coefficient.numerator,
                                             t.coefficient.denominator)
                                 / (a + t.shift) ** t.order
                                 for t in g.source_kernel_power(power).terms)
                self.assertEqual(sp.expand(independent - production), 0)


if __name__ == "__main__":
    unittest.main()
