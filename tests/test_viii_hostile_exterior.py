"""Independent exact holdouts for PR #214; these are not universal proofs.

Oracles use permutation determinants, recursive positive compositions,
finite group images and direct occupation enumeration.  None uses the
production determinant, stars-and-bars formula or coin-change recurrence.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd, prod
import random
import unittest

from observational_succ import exterior_cofactor_ascent as subject


def permutation_det(rows):
    n = len(rows)
    answer = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        answer += (-1) ** inversions * prod(rows[i][p[i]] for i in range(n))
    return answer


def compositions(total, slots):
    if slots == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - slots + 2):
        for rest in compositions(total - first, slots - 1):
            yield (first,) + rest


def direct_weight_count(budget, weights):
    return sum(sum(w * n for w, n in zip(weights, occupations)) <= budget
               for occupations in product(*(range(budget // w + 1) for w in weights)))


class ExteriorIndependentHoldouts(unittest.TestCase):
    def test_cofactor_identity_and_amgm_without_sampling_divisor_weights(self):
        for m in range(2, 6):
            for total in range(m, 15):
                for summands in compositions(total, m):
                    values = summands + (total,)
                    # Two extreme selections plus a mixed one, retaining every slot.
                    selections = ((1,) * (m + 1), values,
                                  tuple(x if i % 2 else 1 for i, x in enumerate(values)))
                    for ds in selections:
                        us = tuple(x // d for x, d in zip(values, ds))
                        cert = subject.cofactor_certificate(ds, us, Fraction(2 * total + 1, 2))
                        self.assertEqual(cert['D'] * cert['U'], prod(values))
                        self.assertLessEqual(prod(values) * m**m, total**(m + 1))
                        if cert['high_divisor']:
                            self.assertLess(cert['U'], Fraction(2 * total + 1, 2 * m**m))
        # Small cofactors alone do not imply high divisor product.
        cert = subject.cofactor_certificate((1, 8, 9), (1, 1, 1), 9)
        self.assertLess(cert['U'], Fraction(9, 4))
        self.assertFalse(cert['high_divisor'])

    def test_bareiss_against_leibniz_with_pivots_and_deep_coefficients(self):
        rng = random.Random(21420261021)
        for n in range(1, 6):
            for trial in range(70):
                rows = [[rng.randrange(-5, 6) for _ in range(n)] for _ in range(n)]
                if trial % 3 == 0:
                    rows[0][0] = 0
                if trial % 5 == 0 and n > 1:
                    rows[-1] = rows[0][:]
                if trial % 7 == 0:
                    rows[-1] = [v * 10**40 for v in rows[-1]]
                self.assertEqual(subject.determinant(rows), permutation_det(rows))

    def test_shared_modulus_by_finite_group_image(self):
        # L = diag(d_i) ker(sum d_i*u_i mod q).  Its index is
        # product(d_i) times the image size, independently of row replacement.
        for m in (2, 3):
            for ds in product(range(1, 5), repeat=m):
                for q in range(1, 6):
                    image = {sum(d * u for d, u in zip(ds, us)) % q
                             for us in product(range(q), repeat=m)}
                    self.assertEqual(subject.effective_exterior_modulus(ds + (q,)),
                                     prod(ds) * len(image))

    def test_shared_prime_source_configurations(self):
        configurations = 0
        for ds in product(range(1, 5), repeat=4):
            points = []
            for us in product(range(1, 5), repeat=3):
                xs = tuple(d * u for d, u in zip(ds[:-1], us))
                if sum(xs) % ds[-1] == 0:
                    points.append(xs + (sum(xs),))
            for start in range(min(4, max(0, len(points) - 2))):
                chosen = points[start:start + 3]
                height = max(p[-1] for p in chosen)
                cert = subject.general_exterior_certificate(ds, chosen, height)
                delta = permutation_det([[p[i] for p in chosen] for i in range(3)])
                self.assertEqual(cert['determinant'], delta)
                self.assertEqual(delta % cert['E'], 0)
                self.assertLessEqual(abs(delta), height**3)
                if any(gcd(*p[:-1]) == 1 for p in chosen):
                    self.assertEqual(cert['E'], prod(ds))
                configurations += 1
        self.assertGreater(configurations, 500)

    def test_effective_divisor_is_needed_and_one_primitive_point_suffices(self):
        pts = ((2, 2, 2, 6), (4, 2, 2, 8), (2, 4, 2, 8))
        cert = subject.general_exterior_certificate((2, 2, 2, 2), pts, 8)
        self.assertEqual(abs(cert['determinant']), 8)
        self.assertEqual(cert['E'], 8)
        self.assertNotEqual(cert['determinant'] % cert['D'], 0)
        mixed = ((2, 2, 5, 9), (4, 4, 10, 18), (2, 4, 3, 9))
        cert = subject.general_exterior_certificate((2, 2, 1, 3), mixed, 18)
        self.assertFalse(cert['globally_primitive'])  # metadata says ALL points
        self.assertEqual(cert['E'], cert['D'])        # one point already suffices

    def test_unbounded_rank_two_counterfamily_without_family_constructor(self):
        for K in (3, 4, 7, 12):
            odd_factor = prod(j for j in range(3, K, 2))
            n = odd_factor * (24 * K**3 + 1)
            ds = (n, n + 1, 2 * n + 1, 3 * n + 2)
            X = K * ds[-1]
            points = [((k - 1) * n, (2 * k - 1) * (n + 1), 2 * n + 1,
                       k * (3 * n + 2)) for k in range(2, K + 1)]
            self.assertTrue(all(gcd(a, b) == 1 for a, b in combinations(ds, 2)))
            self.assertGreater(prod(ds), X**3)
            self.assertEqual(len(set(points)), K - 1)
            for point in points:
                self.assertEqual(sum(point[:-1]), point[-1])
                self.assertEqual(gcd(*point[:-1]), 1)
                self.assertTrue(all(x % d == 0 for x, d in zip(point, ds)))
            # First two are independent; every three columns have zero determinant.
            self.assertNotEqual(points[0][0] * points[1][2] -
                                points[1][0] * points[0][2], 0)
            for triple in combinations(points, 3):
                self.assertEqual(permutation_det([[p[i] for p in triple]
                                                  for i in range(3)]), 0)

    def test_simplex_counts_from_positive_compositions_and_fractional_cutoffs(self):
        for m in range(1, 5):
            for W in range(1, 4):
                rows = list(product(range(W), repeat=m))
                for N in range(0, 13):
                    counts = Counter(tuple(x % W for x in xs)
                                     for total in range(m, N + 1)
                                     for xs in compositions(total, m))
                    for X in (Fraction(N), Fraction(3 * N + 2, 3)):
                        for row in rows:
                            actual = subject.residue_simplex_count(m, W, X, [row])
                            self.assertEqual(actual, counts[row])
                            volume = (X / W)**m / factorial(m)
                            self.assertLessEqual(abs(actual - volume),
                                subject.simplex_error_bound(m, W, X, 1))
                        chosen = rows[::2]
                        actual = subject.residue_simplex_count(m, W, X, chosen)
                        self.assertEqual(actual, sum(counts[r] for r in chosen))
                        self.assertLessEqual(abs(actual - len(chosen) * (X/W)**m / factorial(m)),
                            subject.simplex_error_bound(m, W, X, len(chosen)))

    def test_dimension_growth_and_empty_positive_simplex(self):
        self.assertEqual(subject.unrestricted_simplex_count(11, 10), 0)
        # Exact obstruction to a dimension-free negligible relative boundary.
        for N, m in ((100, 10), (400, 20), (1600, 40)):
            ratio = Fraction(subject.unrestricted_simplex_count(m, N) * factorial(m), N**m)
            self.assertLess(ratio, Fraction(3, 4))
            self.assertGreater(ratio, Fraction(1, 2))
        self.assertEqual(subject.residue_simplex_count(4, 3, 0, []), 0)
        self.assertEqual(subject.simplex_error_bound(4, 3, 0, 0), 0)

    def test_local_laws_count_summands_and_exclude_total(self):
        for m in range(1, 6):
            for p in (2, 3, 5):
                points = list(product(range(p), repeat=m))
                primitive = sum(any(x != 0 for x in row) for row in points)
                pairwise = sum(sum(x == 0 for x in row) <= 1 for row in points)
                factors = subject.local_prime_clock_factors(m, p)
                self.assertEqual(factors['primitive_gcd'], Fraction(primitive, p**m))
                self.assertEqual(factors['pairwise_summands'], Fraction(pairwise, p**m))
        # m=3, p=3: (1,1,1) has no zero summands and a zero total; adding
        # another zero summand yields a real exclusion only when m>=4.
        row = (0, 1, 1, 1)
        self.assertEqual(sum(x == 0 for x in row), 1)
        self.assertEqual(sum(row) % 3, 0)
        self.assertEqual(sum(x == 0 for x in row + (sum(row) % 3,)), 2)

    def test_carrier_modes_are_labeled_and_all_affordable_modes_are_required(self):
        for weights in ((1,), (1, 1), (1, 2), (2, 2, 3), (1, 3, 5), (5, 9)):
            for budget in range(9):
                self.assertEqual(subject.weighted_infinite_count(budget, weights),
                                 direct_weight_count(budget, weights))
        self.assertEqual(subject.weighted_infinite_count(1, (1, 1, 1)), 4)
        self.assertEqual(subject.weighted_infinite_count(1, (1,)), 2)
        # Distinct finite carriers; the function does not authenticate an
        # arbitrary infinite source or certify completeness of its input.

    def test_exact_domains_reject_silent_numeric_coercions(self):
        for bad in (True, False, 2.0, Fraction(2), '2'):
            with self.assertRaises(subject.ExteriorAscentError):
                subject.effective_exterior_modulus((1, 1, bad))
            with self.assertRaises(subject.ExteriorAscentError):
                subject.local_prime_clock_factors(2, bad)
        for bad in (True, False, 2.0, '2'):
            with self.assertRaises(subject.ExteriorAscentError):
                subject.residue_simplex_count(2, 1, bad, [(0, 0)])
        for p in (1, 4, 9, 25, 49):
            with self.assertRaises(subject.ExteriorAscentError):
                subject.local_prime_clock_factors(3, p)


if __name__ == '__main__':
    unittest.main()
