"""Independent bounded exact checks for the RAD/RIS research chart."""
import unittest
from fractions import Fraction
from math import gcd, prod

from observational_succ.rad_ris_transport import (
    ABCSnapshot, RadRis, RadRisError, abc_snapshot, crt_successor_valuations,
    from_radical_layers, gibbs_prime_moments, is_prime, joint_rad_ris_local_factor,
    prime_powers, prime_window_successor_witness, rad,
    radical_layers, ris, successor_balance,
)


def oracle_factors(n):
    """Independent reference by scanning *every* candidate divisor."""
    found = []
    for p in range(2, n + 1):
        if n % p == 0 and all(p % q for q, _ in found):
            power = 0
            while n % p == 0:
                n //= p
                power += 1
            found.append((p, power))
        if n == 1:
            break
    return tuple(found)


def oracle_valuation(n, p):
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


class RadRisTransportTest(unittest.TestCase):
    def test_oracle_and_roundtrip_exhaustive(self):
        for n in range(1, 2001):
            factors = oracle_factors(n)
            support = prod(p for p, e in factors)
            self.assertEqual(prime_powers(n), factors)
            self.assertEqual(rad(n), support)
            self.assertEqual(ris(n), n // support)
            self.assertEqual(RadRis.from_integer(n).value, n)
            layers = radical_layers(n)
            self.assertEqual(from_radical_layers(layers), n)
            self.assertEqual(prod(layers), n)
            self.assertTrue(all(layers[i] % layers[i + 1] == 0
                                for i in range(len(layers) - 1)))

    def test_examples_and_prime_gate(self):
        self.assertEqual(radical_layers(1008), (42, 6, 2, 2))
        self.assertEqual(RadRis.from_integer(1008), RadRis(42, 24))
        state = RadRis.from_integer(1)
        for p, lane in ((2, "support"), (2, "multiplicity"),
                        (3, "support"), (2, "multiplicity")):
            observed_lane, state = state.prime_step(p)
            self.assertEqual(observed_lane, lane)
        self.assertEqual(state, RadRis.from_integer(24))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(91))

    def test_multiplication_and_associativity(self):
        for n in range(1, 61):
            for m in range(1, 61):
                a, b = RadRis.from_integer(n), RadRis.from_integer(m)
                self.assertEqual(a.multiply(b), RadRis.from_integer(n * m))
                overlap = gcd(a.radical, b.radical)
                self.assertEqual(a.multiply(b).radical, a.radical * b.radical // overlap)
                self.assertEqual(a.multiply(b).residual, a.residual * b.residual * overlap)
        for x, y, z in ((12, 18, 20), (49, 21, 4), (3, 25, 8)):
            a, b, c = (RadRis.from_integer(t) for t in (x, y, z))
            self.assertEqual(a.multiply(b).multiply(c), a.multiply(b.multiply(c)))

    def test_discrete_balances_are_signed(self):
        self.assertEqual(successor_balance(128), (8128, -8127))
        # Two very large opposing terms can cancel to a unit.
        for n in range(1, 3000):
            left, right = successor_balance(n)
            self.assertEqual(left + right, 1)
            self.assertEqual(gcd(rad(n), rad(n + 1)), 1)

    def test_abc_quality_exact_threshold(self):
        triple = abc_snapshot(3, 125)
        self.assertIsInstance(triple, ABCSnapshot)
        self.assertEqual(triple.c, 128)
        self.assertEqual(triple.excess_ratio, Fraction(64, 15))
        self.assertTrue(triple.quality_above_one)
        for a in range(1, 80):
            for b in range(1, 80):
                if gcd(a, b) == 1:
                    d = abc_snapshot(a, b)
                    self.assertEqual(d.quality_above_one, d.c > d.radical_abc)
                    self.assertEqual(d.radical_abc, rad(a * b * d.c))
                    self.assertEqual(d.excess_ratio,
                                     Fraction(ris(d.c), rad(a) * rad(b)))

    def test_crt_exhaustive_independent_oracle(self):
        for left, right in (({}, {}), ({2: 1}, {}), ({}, {3: 1}),
                            ({2: 1}, {3: 1}), ({3: 2}, {2: 1}),
                            ({2: 2}, {3: 1, 5: 1}), ({5: 1}, {7: 1})):
            sig = crt_successor_valuations(left, right)
            self.assertEqual(len(sig.residues),
                             prod(p - 1 for p in (*left, *right)))
            self.assertEqual(sig.modulus,
                             prod(p ** (e + 1) for p, e in (*left.items(), *right.items())))
            brute_count = 0
            for n in range(1, 10001):
                oracle_match = all(oracle_valuation(n, p) == e for p, e in left.items()) \
                    and all(oracle_valuation(n + 1, p) == e for p, e in right.items())
                self.assertEqual(sig.matches(n), oracle_match, (left, right, n))
                brute_count += oracle_match
            self.assertEqual(sig.count_up_to(10000), brute_count)
            self.assertLessEqual(abs(Fraction(brute_count) - 10000 * sig.density),
                                 len(sig.residues))

    def test_finite_prime_window_cannot_reconstruct_successor(self):
        for primes, outsider in (((2, 3, 5), 7), ((3, 5), 2),
                                 ((2, 7), 3), ((2, 3, 5, 7), 11), ((), 2)):
            hit, miss = prime_window_successor_witness(primes, outsider)
            self.assertNotEqual(hit, miss)
            self.assertTrue(all(oracle_valuation(hit, p) == oracle_valuation(miss, p) == 0
                                for p in primes))
            self.assertEqual((hit + 1) % outsider, 0)
            self.assertNotEqual((miss + 1) % outsider, 0)
            self.assertEqual(rad(hit + 1) % outsider, 0)
            self.assertNotEqual(rad(miss + 1) % outsider, 0)
        self.assertEqual(prime_window_successor_witness((2, 3, 5), 7), (181, 91))

    def test_exact_bivariate_dirichlet_prime_factors(self):
        for p in (2, 3, 5, 7):
            self.assertEqual(joint_rad_ris_local_factor(p, 2, 2),
                             Fraction(p * p, p * p - 1))
            for s, u in ((2, 1), (3, 2)):
                exact = joint_rad_ris_local_factor(p, s, u)
                prefix = 1 + sum((Fraction(1, p ** (s + u * (k - 1)))
                                  for k in range(1, 6)), Fraction())
                tail = Fraction(1, p ** (s + 5 * u)) / (1 - Fraction(1, p ** u))
                self.assertEqual(prefix + tail, exact)

    def test_hostile_input_mutations(self):
        for n in (0, -1, True, 1.5, 1000001):
            with self.assertRaises(RadRisError):
                rad(n)
        for invalid in ((1, 2), (4, 1), (6, 5), (6, 7), (2, 3)):
            with self.assertRaises(RadRisError):
                RadRis(*invalid)
        for invalid_layers in ((1,), (6, 10), (4, 2), (2, 1), [2, 2]):
            with self.assertRaises(RadRisError):
                from_radical_layers(invalid_layers)
        for p in (1, 4, 9, True):
            with self.assertRaises(RadRisError):
                RadRis.from_integer(5).prime_step(p)
        for left, right in (({2: 1}, {2: 1}), ({4: 1}, {}),
                            ({2: True}, {}), ({3: 0}, {}), ({3: 100}, {})):
            with self.assertRaises(RadRisError):
                crt_successor_valuations(left, right)
        for p_window, outsider in (((2, 3), 3), ((2, 6), 7), ((3, 2), 7),
                                    ((2,), 4), ((2, 3, 5, 7), 999983)):
            with self.assertRaises(RadRisError):
                prime_window_successor_witness(p_window, outsider)
        with self.assertRaises(RadRisError):
            joint_rad_ris_local_factor(6, 2, 1)
        with self.assertRaises(RadRisError):
            joint_rad_ris_local_factor(2, 1, 1)
        for a, b in ((2, 2), (0, 5), (True, 5), (999999, 2)):
            with self.assertRaises(RadRisError):
                abc_snapshot(a, b)
        for primes, beta in (((2, 6), 2), ((3, 2), 2), ((2, 2), 2),
                             ((2,), 1), ((2,), True)):
            with self.assertRaises(RadRisError):
                gibbs_prime_moments(primes, beta)

    def test_finite_gibbs_prime_moments(self):
        rows = gibbs_prime_moments((2, 3, 5, 7), 2)
        for p, support, residual_mean, covariance in rows:
            q = Fraction(1, p * p)
            self.assertEqual(support, q)
            self.assertEqual(residual_mean, q * q / (1 - q))
            self.assertEqual(covariance, q * q)
            self.assertEqual(covariance, (1 - support) * residual_mean)
        self.assertEqual(rows[0],
                         (2, Fraction(1, 4), Fraction(1, 12), Fraction(1, 16)))

    def test_vacuous_circuit_does_not_certify_prime_support(self):
        for n in range(1, 500):
            fake_r, fake_t = 1, n
            fake_next_r, fake_next_t = 1, n + 1
            self.assertEqual(fake_r * fake_t, n)
            self.assertEqual(fake_t * (fake_next_r - fake_r)
                             + fake_next_r * (fake_next_t - fake_t), 1)
        self.assertNotEqual(1, rad(2))
        self.assertNotEqual((1, 2), (rad(2), ris(2)))


if __name__ == "__main__":
    unittest.main()
