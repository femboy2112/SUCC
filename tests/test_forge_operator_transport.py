"""Independent exact receipts; infinite statements are proved in Paper B."""

from fractions import Fraction
from itertools import combinations, product
from math import prod
import unittest

from observational_succ.forge_operator_transport import (
    PrimeShell, cylinder_atomic_lift, cylinder_norm_squared,
    forward_cylinder_bound_squared, geometric_orbit_mass,
    good_cylinder_primes, multiplication_pullback, prime_set,
    project_atomic_masses,
)


class ForgeOperatorTransportTests(unittest.TestCase):
    def test_shell_formula_against_independent_residue_count(self):
        for size in range(5):
            for primes in combinations((2, 3, 5, 7), size):
                for n in (1, 2, 5, 12, 25, 49, 77):
                    shell = PrimeShell(primes, n)
                    self.assertEqual(shell.counted_mass(), shell.mass)
        # Held-out primes and a factor deliberately outside the selected set.
        for n in (17, 2 ** 3 * 11 * 17, 13 ** 2 * 19):
            shell = PrimeShell((2, 11, 13), n)
            self.assertEqual(shell.counted_mass(), shell.mass)

    def test_unselected_factor_and_nonexact_valuation_mutations(self):
        shell = PrimeShell((2, 3), 5)
        self.assertEqual(shell.mass, Fraction(1, 3))
        self.assertNotEqual(shell.mass, shell.unit_mass / shell.n)
        shell = PrimeShell((2, 3), 12)
        only_divisible = Fraction(sum(r % 12 == 0 for r in range(shell.modulus)), shell.modulus)
        self.assertNotEqual(only_divisible, shell.mass)

    def test_normalized_shell_coefficient_bound_is_sharp(self):
        for shell in (PrimeShell((2, 3), 5), PrimeShell((5, 11), 25)):
            for values in ((1,), (2, -3, 4, 1), (0, 1, -2, 5, 3, -1, 4)):
                integral = shell.cylinder_integral(values)
                # f = 1_K/sqrt(mu(K)) has norm one; square its pairing.
                pairing_squared = integral ** 2 / shell.mass
                self.assertLessEqual(pairing_squared, max(abs(x) for x in values) ** 2 * shell.mass)
            self.assertEqual(shell.cylinder_integral((1,)) ** 2 / shell.mass, shell.mass)

    def test_forward_test_permutations_and_bad_prime_mutation(self):
        values = (Fraction(2), Fraction(-1), Fraction(3, 7), Fraction(4), Fraction(-3), Fraction(5))
        for p in (5, 7, 11, 13):
            self.assertEqual(cylinder_norm_squared(multiplication_pullback(values, p)), cylinder_norm_squared(values))
        self.assertNotEqual(cylinder_norm_squared(multiplication_pullback(values, 2)), cylinder_norm_squared(values))
        self.assertEqual(good_cylinder_primes((2, 3, 5, 11), 6), (5, 11))
        self.assertEqual(forward_cylinder_bound_squared((2, 3, 5, 11), 55, 6), Fraction(48, 605))
        self.assertEqual(
            multiplication_pullback(multiplication_pullback(values, 5), 11),
            multiplication_pullback(multiplication_pullback(values, 11), 5),
        )

    def test_geometric_norm_blowup_against_direct_exponent_enumeration(self):
        for primes in ((2,), (2, 3), (5, 11, 13)):
            alpha = PrimeShell(primes, 1).unit_mass
            previous = Fraction(0)
            for depth in range(6):
                direct = sum((Fraction(1, prod(p ** a for p, a in zip(primes, exponents)))
                              for exponents in product(range(depth + 1), repeat=len(primes))), start=Fraction(0))
                observed = geometric_orbit_mass(primes, depth)
                self.assertEqual(observed, direct)
                self.assertGreater(observed, previous)
                self.assertEqual(observed * alpha, prod((1 - Fraction(1, p ** (depth + 1)) for p in primes), start=Fraction(1)))
                previous = observed

    def test_distribution_interpolation_and_coarser_compatibility(self):
        masses = tuple(Fraction((-1) ** r * (r + 1), 7) for r in range(12))
        atoms = cylinder_atomic_lift(masses)
        self.assertEqual(project_atomic_masses(atoms, 12), masses)
        for modulus in (1, 2, 3, 4, 6):
            expected = tuple(sum(masses[r] for r in range(12) if r % modulus == s) for s in range(modulus))
            self.assertEqual(project_atomic_masses(atoms, modulus), expected)
        # Omitting the source sqrt(n) normalization changes the cylinder mass.
        square_atoms = {1: Fraction(1), 4: Fraction(2), 9: Fraction(3)}
        self.assertEqual(project_atomic_masses(square_atoms, 5), (0, 1, 0, 0, 5))
        self.assertNotEqual(project_atomic_masses(square_atoms, 5), project_atomic_masses({1: 1, 4: 1, 9: 1}, 5))

    def test_domain_guards(self):
        for bad in ((4,), (2, 2), (True,), (2.0,)):
            with self.assertRaises(ValueError):
                prime_set(bad)
        with self.assertRaises(ValueError):
            PrimeShell((2,), 0)
        with self.assertRaises(ValueError):
            PrimeShell((2,), 2 ** 20).counted_mass()
        with self.assertRaises(ValueError):
            cylinder_atomic_lift((0.5,))
        with self.assertRaises(ValueError):
            forward_cylinder_bound_squared((2,), 1, 3, -1)


if __name__ == "__main__":
    unittest.main()
