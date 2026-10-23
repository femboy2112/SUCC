"""Independent exact adversaries for boundary identifiability.

The determinant oracle below is the permutation formula, independent of the
production Gaussian elimination and continued-fraction implementations.
These are mathematical synthetic models, not physical observations.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import prod
import unittest

from observational_succ.boundary_realization_selection import (
    FiniteNetwork, boundary_response,
)
from observational_succ.spectral_boundary_rigidity import (
    approximate_hidden_mode_pair, response_at, chain_jacobi, chain_moments,
)


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), Q())
                       for col in transpose(b)) for row in a)


def determinant(a):
    n = len(a)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(n)
                           for j in range(i + 1, n))
                * prod(a[i][p[i]] for i in range(n))
                for p in permutations(range(n))), Q())


def diagonal_resolvent(a, s, at=0):
    shifted = tuple(tuple(Q(x) + (s if i == j else 0)
                          for j, x in enumerate(row))
                    for i, row in enumerate(a))
    minor = tuple(tuple(x for j, x in enumerate(row) if j != at)
                  for i, row in enumerate(shifted) if i != at)
    return determinant(minor) / determinant(shifted)


def moments(a, count):
    v = tuple(Q(i == 0) for i in range(len(a)))
    out = []
    for _ in range(count):
        out.append(v[0])
        v = tuple(sum((x * y for x, y in zip(row, v)), Q()) for row in a)
    return tuple(out)


def krylov_determinant(a):
    v = tuple(Q(i == 0) for i in range(len(a)))
    cols = []
    for _ in a:
        cols.append(v)
        v = tuple(sum((x * y for x, y in zip(row, v)), Q()) for row in a)
    return determinant(transpose(cols))


PATH = ((Q(4), Q(-1), Q(0)),
        (Q(-1), Q(4), Q(-1)),
        (Q(0), Q(-1), Q(4)))
ROTATION = ((Q(1), Q(0), Q(0)),
            (Q(0), Q(4, 5), Q(-3, 5)),
            (Q(0), Q(3, 5), Q(4, 5)))
TRIANGLE = ((Q(4), Q(-4, 5), Q(-3, 5)),
            (Q(-4, 5), Q(124, 25), Q(-7, 25)),
            (Q(-3, 5), Q(-7, 25), Q(76, 25)))


def grounded_network(a):
    """Port 0, interiors 1..3, reference ground 4, all interior C=1."""
    edges = [(0, 1, Q(1))]
    for i in range(3):
        for j in range(i + 1, 3):
            if a[i][j]:
                edges.append((i + 1, j + 1, -a[i][j]))
        grounding = sum(a[i], Q()) - Q(i == 0)
        if grounding <= 0:
            raise ValueError("positive independent grounding required")
        edges.append((i + 1, 4, grounding))
    return FiniteNetwork(5, (0, 4), tuple(edges),
                         tuple((i, Q(1)) for i in (1, 2, 3)))


def finite_stieltjes_alias(probes):
    """Explicit normalized positive spectral weights agreeing at all probes.

    r=k+2 poles; residues of prod(s-probe)/prod(s+pole) sum to zero.
    This is deliberately independent of production rational interpolation.
    """
    probes = tuple(Q(s) for s in probes)
    if len(set(probes)) != len(probes) or any(s < 0 for s in probes):
        raise ValueError("distinct nonnegative Laplace probes required")
    r = len(probes) + 2
    poles = tuple(Q(j + 2) for j in range(r))
    residues = tuple(prod(-a - s for s in probes)
                     / prod(b - a for b in poles if b != a)
                     for a in poles)
    delta = Q(1, 2 * r) / max(abs(c) for c in residues)
    left = tuple(Q(1, r) + delta * c for c in residues)
    right = tuple(Q(1, r) - delta * c for c in residues)
    return poles, left, right, residues, delta


def stieltjes(poles, weights, s):
    return sum((w / (s + a) for a, w in zip(poles, weights)), Q())


class RealityPinHostileTests(unittest.TestCase):
    def test_nonpermutation_boundary_gauge_preserves_operator_pair(self):
        eye = tuple(tuple(Q(i == j) for j in range(3)) for i in range(3))
        self.assertEqual(multiply(ROTATION, transpose(ROTATION)), eye)
        self.assertEqual(multiply(multiply(ROTATION, PATH),
                                  transpose(ROTATION)), TRIANGLE)
        self.assertEqual(tuple(row[0] for row in ROTATION), (1, 0, 0))
        self.assertTrue(any(x not in (0, 1) for row in ROTATION for x in row))

    def test_both_nonisomorphic_interiors_are_cyclic_positive_rc_sources(self):
        for a, edge_count in ((PATH, 2), (TRIANGLE, 3)):
            self.assertEqual(sum(a[i][j] < 0 for i in range(3)
                                 for j in range(i + 1, 3)), edge_count)
            self.assertEqual(krylov_determinant(a), Q(-1))
            self.assertTrue(all(sum(row, Q()) - Q(i == 0) > 0
                                for i, row in enumerate(a)))
            grounded_network(a)  # verifies positive actual edge realization
            for k in (1, 2, 3):
                self.assertGreater(determinant(tuple(row[:k] for row in a[:k])), 0)

    def test_full_response_alias_checked_by_independent_graph_and_cofactors(self):
        for s in (Q(0), Q(1, 13), Q(1), Q(7, 3), Q(101)):
            expected_m = ((s + 4) ** 2 - 1) / ((s + 4) * ((s + 4) ** 2 - 2))
            for a in (PATH, TRIANGLE):
                self.assertEqual(diagonal_resolvent(a, s), expected_m)
                self.assertEqual(boundary_response(grounded_network(a), s)[0][0],
                                 1 - expected_m)
        self.assertEqual(moments(PATH, 16), moments(TRIANGLE, 16))

    def test_new_authenticated_interior_probe_splits_full_scalar_alias(self):
        # Accessing node 2 is extra observational authority, not inferred from Y.
        self.assertNotEqual(PATH[1][1], TRIANGLE[1][1])
        self.assertNotEqual(diagonal_resolvent(PATH, Q(1), at=1),
                            diagonal_resolvent(TRIANGLE, Q(1), at=1))

    def test_any_finite_probe_list_has_positive_normalized_cyclic_aliases(self):
        for probes in ((), (Q(0),), (Q(1, 3), Q(2)),
                       tuple(map(Q, range(7))),
                       (Q(1, 101), Q(5, 7), Q(19, 2), Q(1000))):
            poles, left, right, residues, delta = finite_stieltjes_alias(probes)
            self.assertEqual(sum(residues), 0)
            self.assertEqual(sum(left), 1)
            self.assertEqual(sum(right), 1)
            self.assertTrue(all(w > 0 for w in left + right))
            self.assertNotEqual(left, right)
            for s in probes:
                self.assertEqual(stieltjes(poles, left, s),
                                 stieltjes(poles, right, s))
            s = max(probes, default=Q(0)) + 1
            predicted = 2 * delta * prod(s - x for x in probes) / prod(s + a for a in poles)
            self.assertEqual(stieltjes(poles, left, s) - stieltjes(poles, right, s), predicted)
            self.assertNotEqual(predicted, 0)
            # Positive weights at distinct positive poles imply no dark mode.
            # Weighted Vandermonde Gram determinant is strictly positive.
            for weights in (left, right):
                gram_det = prod(weights) * prod((poles[j] - poles[i]) ** 2
                          for i in range(len(poles)) for j in range(i + 1, len(poles)))
                self.assertGreater(gram_det, 0)

    def test_alias_probe_detects_mutated_nonannihilating_weight_change(self):
        poles, left, right, _, _ = finite_stieltjes_alias((Q(0), Q(1)))
        mutated = list(right)
        change = min(right) / 2
        mutated[0] += change
        mutated[1] -= change
        self.assertEqual(sum(mutated), 1)
        for s in (Q(0), Q(1)):
            self.assertNotEqual(stieltjes(poles, left, s), stieltjes(poles, mutated, s))

    def test_first_return_2r_requires_preservation_of_old_principal_block(self):
        old = chain_jacobi((2, 3, 5))
        # Attach new edge 5 while RETAINING the old ground resistor 5.
        # The old depth-two diagonal changes, so detection is at 2r-1=3.
        attached = ((Q(5), Q(-3), Q(0)),
                    (Q(-3), Q(13), Q(-5)),
                    (Q(0), Q(-5), Q(12)))
        before, after = moments(old, 5), moments(attached, 5)
        self.assertEqual(before[:3], after[:3])
        self.assertEqual(after[3] - before[3], Q(45))
        self.assertEqual(before, chain_moments((2, 3, 5), 5))

    def test_weak_coupling_global_formula_and_noise_adversary(self):
        for eps in (Q(1, 2), Q(1, 17), Q(1, 1000)):
            short, long = approximate_hidden_mode_pair(eps)
            for s in (Q(0), Q(1, 7), Q(2), Q(10000)):
                gap = abs(response_at(short, s) - response_at(long, s))
                a = s + 1 + eps
                self.assertEqual(gap, eps ** 2 / (a * (a * a - eps * eps)))
                self.assertLess(gap, eps ** 2)
                midpoint = (response_at(short, s) + response_at(long, s)) / 2
                # The same observation with error eps²/2 fits either topology.
                self.assertLess(abs(midpoint - response_at(short, s)), eps ** 2 / 2)
                self.assertLess(abs(midpoint - response_at(long, s)), eps ** 2 / 2)


if __name__ == "__main__":
    unittest.main()
