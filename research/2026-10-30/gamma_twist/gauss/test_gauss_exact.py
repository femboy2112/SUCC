import unittest
from fractions import Fraction

from gauss_exact import (AUTH, MUTATION, OFFSETS, Cyclo, Field, GaussSystem,
    cofiber, gamma_mod, gk_exponent, gk_unit_mod, orbit, source,
    valuation, verify_gk_unit_power)


PRIMES = (3, 5, 7, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 71, 73, 89)


class ExactGaussTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.systems = {p: GaussSystem(p) for p in PRIMES}

    def test_field_orders_and_frobenius(self):
        for p, system in self.systems.items():
            field = system.field
            self.assertEqual(len(set(field.powers)), field.q-1)
            for x in field.powers:
                self.assertEqual(field.power(x, field.q), x)
                xp = field.power(x, p)
                self.assertEqual(field.trace(xp), field.trace(x))

    def test_cyclotomic_relations(self):
        for p in PRIMES:
            self.assertEqual(Cyclo.monomial(p, 4), Cyclo.monomial(p, scalar=-1))
            self.assertEqual(Cyclo.monomial(p, j=p), Cyclo.monomial(p))
            self.assertEqual(sum((Cyclo.monomial(p, j=j) for j in range(p)),
                                 Cyclo.monomial(p, scalar=0)), Cyclo.monomial(p, scalar=0))

    def test_all_gauss_norms(self):
        for p, system in self.systems.items():
            for d in range(1, 8):
                self.assertEqual(system.sums[d]*system.sums[d].conjugate(),
                                 Cyclo.monomial(p, scalar=system.field.q))

    def test_exact_frobenius_permutations(self):
        for p, system in self.systems.items():
            for d in range(1, 8):
                self.assertEqual(system.sums[d], system.sums[p*d % 8])

    def test_both_quadratic_davenport_hasse_identities(self):
        for system in self.systems.values():
            g = system.sums
            self.assertEqual(g[1]*g[5], system.character(4, -1)*g[2]*g[4])
            self.assertEqual(g[2]*g[6], system.character(4, -2)*g[4].power(2))

    def test_complete_mutant_blindness(self):
        for p, system in self.systems.items():
            ratio = system.weighted(MUTATION)
            self.assertEqual(ratio, system.character(2, 2))
            self.assertEqual(ratio.power(2), Cyclo.monomial(p))
            mutant = tuple(a+2*b for a, b in zip(AUTH, MUTATION))
            self.assertEqual(system.weighted(mutant), system.weighted())
            for k in (5, 9, 13, 17):
                self.assertEqual(ratio.power(2**(k+2)), Cyclo.monomial(p))

    def test_full_unit_power_checks(self):
        for system in self.systems.values():
            verify_gk_unit_power(system, 3)

    def test_gamma_modular_continuity_and_recurrence(self):
        for p in (3, 5, 13, 19, 73):
            for d in OFFSETS:
                x = Fraction(d, 8)
                self.assertEqual(gamma_mod(p, 3, x) % p**2, gamma_mod(p, 2, x))
                residue = x.numerator*pow(x.denominator, -1, p**2) % p**2
                step = -residue if residue % p else -1
                self.assertEqual(gamma_mod(p, 2, x+1),
                    gamma_mod(p, 2, x)*step % p**2)

    def test_negative_coefficient_sum_keeps_exact_integer_unit(self):
        value = gk_unit_mod(17, 3, (-1, 0, 0, 0))
        self.assertIsInstance(value, int)
        self.assertEqual(value, -pow(gamma_mod(17, 3, Fraction(1, 8)), -1, 17**3) % 17**3)

    def test_units_also_blind_to_large_positive_mutants(self):
        for p in (13, 17, 19, 29, 43, 47, 73):
            authentic = gk_unit_mod(p, 3)
            for k in (5, 9, 13, 17):
                mutant = tuple(a+2**(k+2)*b for a, b in zip(AUTH, MUTATION))
                self.assertEqual(gk_unit_mod(p, 3, mutant), authentic)
                self.assertEqual(gk_exponent(p, mutant), gk_exponent(p))

    def test_radix_source_still_distinguishes_mutants(self):
        for k in (5, 9, 13, 17):
            t = 2**(k+2)
            mutant = tuple(a+t*b for a, b in zip(AUTH, MUTATION))
            for n in (1, 2, 7, 23, 53):
                self.assertEqual(valuation(source(n, mutant)-source(n), 2), k)
                self.assertEqual(valuation(orbit(n, mutant)-orbit(n), 2), k)
            difference = 13*(orbit(2, mutant)-orbit(2))
            self.assertEqual(difference.numerator*pow(difference.denominator, -1, 13) % 13,
                             t % 13)

    def test_original_conductor_cancellations_and_returns(self):
        for n in range(10, 17):
            self.assertGreaterEqual(valuation(orbit(n), 19), 0)
        self.assertEqual(valuation(orbit(9), 19), -1)
        self.assertEqual(valuation(orbit(17), 19), -1)
        self.assertEqual(valuation(orbit(274), 73), 0)
        self.assertEqual(valuation(orbit(273), 73), -1)

    def test_cofiber_foreign_conductors(self):
        a, P, v = cofiber(orbit(2), 13)
        self.assertEqual((a, P, v), (12, 13, Fraction(107, 315)))
        for p, n in ((19, 5), (19, 10), (19, 17), (73, 10), (73, 274),
                     (17, 3), (29, 4), (43, 11), (47, 12)):
            _, _, v = cofiber(orbit(n), p)
            self.assertEqual(v.denominator % 2, 1)
            self.assertEqual(v.denominator % p == 0, False)
            self.assertGreater(v.denominator, 1)

    def test_class_seven_exact_semiprimitive_product(self):
        for p in (7, 23, 31, 47, 71):
            self.assertEqual(self.systems[p].weighted(),
                             Cyclo.monomial(p, scalar=(-1)**((p+1)//8)))

    def test_wrong_ratio_and_same_ratio_controls_are_not_forced_blind(self):
        system = self.systems[13]
        for mutant in ((5, -2, -1, -1), (8, -4, -2, -2)):
            self.assertNotEqual(system.weighted(mutant), system.weighted())


if __name__ == "__main__":
    unittest.main()
