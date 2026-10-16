"""Independent finite oracles: indicator ranks, cyclic sums and root sums.

The oracle code does not call the conductor/sector formulas it is checking.
All arithmetic is standard-library Fraction or the existing cyclotomic field.
"""
import unittest
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd, lcm

from observational_succ.collective_modular import (
    BoundedCylinder, CollectiveModularError, affine_character,
    affine_norm_squared, affine_pullback, collective_sectors,
    compatible_crt_image, conditional_expectation, conductor_projector,
    conductor_six_basis, fucc_pullback, linear_pool_projector,
    minimum_target_portfolio, missing_joint_projector, succ_pullback,
    target_pair_cover,
)
from observational_succ.consensus_lambda import Candidate, World
from observational_succ.classical_haar_clock import (
    PrimeHaarClock, condition, multiply_observable, succ_observable,
)
from observational_succ.dynamic_fourier_tower import sum_fibers
from observational_succ.finite_fourier_carrier import CyclotomicElement as C
from observational_succ.pascal_rotated_transport import matmul, matrix_apply
from observational_succ.source_lambda import Atlas, Join, Passport, Read, execute


def rank(rows):
    """Test-only rational elimination on raw observable value vectors."""
    if not rows:
        return 0
    a = [list(map(Q, row)) for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        divisor = a[pivot][col]
        a[pivot] = [v/divisor for v in a[pivot]]
        for i in range(pivot+1, len(a)):
            scale = a[i][col]
            a[i] = [v-scale*w for v, w in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def indicators(n, m):
    return [tuple(Q(x % m == r) for x in range(n)) for r in range(m)]


def cyclic_average(values, m):
    # Translation by m, not the matrix's congruence-entry construction.
    n = len(values)
    return tuple(sum((values[(x+k*m) % n] for k in range(n//m)), Q())/(n//m)
                 for x in range(n))


def zero(n):
    return tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))


class CollectiveModularTests(unittest.TestCase):
    def test_expectation_composition_against_cyclic_orbit_oracle(self):
        count = 0
        for n in range(1, 19):
            ds = [d for d in range(1, n+1) if n % d == 0]
            for m, q in product(ds, repeat=2):
                actual = matmul(conditional_expectation(n, m), conditional_expectation(n, q))
                expected_columns = []
                for j in range(n):
                    unit = tuple(Q(x == j) for x in range(n))
                    expected_columns.append(cyclic_average(unit, gcd(m, q)))
                self.assertEqual(actual, tuple(zip(*expected_columns)))
                count += 1
        self.assertEqual(count, 224)

    def test_projection_self_adjoint_and_rank(self):
        for n, m in ((1, 1), (6, 2), (12, 4), (18, 6), (20, 5)):
            e = conditional_expectation(n, m)
            self.assertEqual(e, tuple(zip(*e)))
            self.assertEqual(matmul(e, e), e)
            self.assertEqual(rank(e), m)
            self.assertTrue(all(type(v) is Q for row in e for v in row))

    def test_primitive_projectors_against_exact_character_sums(self):
        for n in range(1, 13):
            for d in range(1, n+1):
                if n % d:
                    continue
                p = conductor_projector(n, d)
                labels = [k for k in range(n) if n//gcd(k, n) == d]
                roots = [sum((C.root(n, k*t) for k in labels), C.scalar(n, 0)).scale(Q(1, n))
                         for t in range(n)]
                for x, y in product(range(n), repeat=2):
                    self.assertEqual(C.scalar(n, p[x][y]), roots[(x-y) % n])
                self.assertEqual(rank(p), len(labels))

    def test_primitive_orthogonal_resolution(self):
        n = 12
        ps = [conductor_projector(n, d) for d in (1, 2, 3, 4, 6, 12)]
        for i, j in product(range(len(ps)), repeat=2):
            self.assertEqual(matmul(ps[i], ps[j]), ps[i] if i == j else zero(n))
        self.assertEqual(tuple(tuple(sum(p[x][y] for p in ps) for y in range(n))
                               for x in range(n)), conditional_expectation(n, n))

    def test_crt_actual_image_and_incompatible_tuples(self):
        for ms in ((2, 3), (4, 6), (4, 6, 9), (1, 3), (3, 3)):
            image = compatible_crt_image(ms)
            compatible = {rs for rs in product(*(range(m) for m in ms))
                          if all((rs[i]-rs[j]) % gcd(ms[i], ms[j]) == 0
                                 for i, j in combinations(range(len(ms)), 2))}
            self.assertEqual(set(image), compatible)
            self.assertEqual(len(image), lcm(*ms))
        self.assertNotIn((0, 1), compatible_crt_image((4, 6)))
        self.assertEqual(len(compatible_crt_image((4, 6))), 12)

    def test_crt_source_lambda_join_integration(self):
        p = Passport("modular-integration", 0)
        for x in range(12):
            result = execute(Join(Read(4), Read(6)), Atlas.from_integer(p, x, (4, 6)))
            self.assertEqual((result.value.modulus, result.value.value), (12, x))

    def test_linear_rank_vs_joint_product_rank(self):
        for ms in ((2, 3), (4, 6), (2, 3, 5), (6, 10, 15), (2, 2, 4), (1,)):
            n = lcm(*ms)
            linear = [v for m in ms for v in indicators(n, m)]
            joint = [tuple(Q(all(x % m == r for m, r in zip(ms, rs))) for x in range(n))
                     for rs in product(*(range(m) for m in ms))]
            sectors = collective_sectors(n, ms)
            self.assertEqual(rank(linear), sectors.linear_dimension)
            self.assertEqual(rank(joint), sectors.joint_dimension)
            if len(ms) == 2:
                self.assertEqual(sectors.missing_dimension, n-sum(ms)+gcd(*ms))

    def test_joint_sector_depths(self):
        data = collective_sectors(30, (2, 3, 5))
        self.assertEqual((data.linear_dimension, data.missing_dimension), (8, 22))
        self.assertEqual(data.missing_conductors, (6, 10, 15, 30))
        self.assertEqual({s.conductor: s.minimum_joint_menus for s in data.sectors},
                         {1: 0, 2: 1, 3: 1, 5: 1, 6: 2, 10: 2, 15: 2, 30: 3})
        other = collective_sectors(30, (6, 10, 15))
        self.assertEqual((other.linear_dimension, other.missing_dimension), (22, 8))
        self.assertEqual(other.sectors[-1].minimum_joint_menus, 2)

    def test_interaction_order_against_partial_product_ranks(self):
        for ms in ((2, 3, 5), (4, 6, 3)):
            n = lcm(*ms)
            sectors = collective_sectors(n, ms)
            rows = [(Q(1),)*n]
            for order in range(len(ms)+1):
                if order:
                    for subset in combinations(ms, order):
                        rows.extend(tuple(Q(all(x % m == r for m, r in zip(subset, rs)))
                                          for x in range(n))
                                    for rs in product(*(range(m) for m in subset)))
                self.assertEqual(rank(rows), sum(s.dimension for s in sectors.sectors
                                                  if s.minimum_joint_menus <= order))

    def test_linear_projector_and_missing_ambient_boundary(self):
        n = 12
        pool = linear_pool_projector(n, (2, 3))
        missing = missing_joint_projector(n, (2, 3))
        self.assertEqual(rank(pool), 4)
        self.assertEqual(rank(missing), 2)  # Other six ambient dimensions excluded.
        self.assertEqual(matmul(pool, missing), zero(n))
        self.assertEqual(matmul(pool, pool), pool)
        self.assertEqual(tuple(tuple(a+b for a, b in zip(r, s)) for r, s in zip(pool, missing)),
                         conditional_expectation(n, 6))
        for m in (2, 3):
            for v in indicators(n, m):
                self.assertEqual(matrix_apply(pool, v), v)

    def test_conductor_six_basis_and_multiplication(self):
        u, v = conductor_six_basis()
        self.assertEqual(rank([u, v]), 2)
        for w in (u, v):
            self.assertEqual(matrix_apply(conductor_projector(6, 6), w), w)
            for m in (2, 3):
                self.assertEqual(cyclic_average(w, m), (Q(0),)*6)
        self.assertEqual(sum(a*b for a, b in zip(u, v)), 0)
        self.assertEqual(sum(a*a for a in u)/6, 2)
        self.assertEqual(sum(a*a for a in v)/6, Q(2, 3))
        self.assertEqual(tuple((-1)**x * (2, -1, -1)[x % 3] for x in range(6)), u)
        self.assertNotEqual(matrix_apply(linear_pool_projector(6, (2, 3)), u), u)

    def test_six_character_basis_in_one_field(self):
        u, v = conductor_six_basis()
        imaginary = C.root(6, 1) + C.scalar(6, Q(-1, 2))
        for x in range(6):
            self.assertEqual(C.root(6, x), C.scalar(6, u[x]/2) + imaginary.scale(v[x]))
            self.assertEqual(C.root(6, -x), C.scalar(6, u[x]/2) + imaginary.scale(-v[x]))
        # Composite conductor is generated by existing 2/3 characters.
        self.assertEqual(C.root(6, 3)*C.root(6, 4), C.root(6, 1))

    def test_affine_character_covariance_including_nonunits(self):
        for n in (1, 6, 10):
            for a, b, k in product((0, 2, -3, 5), (-1, 0, 1), range(n)):
                phase, ch = affine_character(n, k, a, b)
                for x in range(n):
                    self.assertEqual(C.root(n, k*(a*x+b)), phase*ch.character_root(x))
                conductor = n//gcd(k, n)
                self.assertEqual(ch.rational_frequency.denominator, conductor//gcd(conductor, a))

    def test_affine_nonunit_rank_norm_and_phase_mutation(self):
        for n, a, b in ((6, 2, 1), (12, 6, 5), (6, 0, 3), (10, -3, 2)):
            u = affine_pullback(n, a, b)
            fibers = [sum((a*x+b) % n == y for x in range(n)) for y in range(n)]
            self.assertEqual(rank(u), len([c for c in fibers if c]))
            self.assertEqual(affine_norm_squared(n, a), max(fibers))
            atom = tuple(Q(i == b % n) for i in range(n))
            pulled = matrix_apply(u, atom)
            self.assertEqual(sum(v*v for v in pulled), max(fibers))
        phase, _ = affine_character(6, 1, 2, 1)
        self.assertNotEqual(phase, C.scalar(6, 1))
        self.assertNotEqual(fucc_pullback(6, 2), affine_pullback(6, 2, 0))

    def test_affine_unit_commutes_and_nonunit_does_not_always(self):
        e = conditional_expectation(6, 2)
        unit = affine_pullback(6, 5, 1)
        self.assertEqual(matmul(e, unit), matmul(unit, e))
        nonunit = affine_pullback(6, 2, 1)
        # E_1 is not preserved: averaging f(2x+1) samples only odd outputs.
        e1 = conditional_expectation(6, 1)
        self.assertNotEqual(matmul(e1, nonunit), matmul(nonunit, e1))

    def test_existing_prime_clock_and_tower_integration(self):
        for chart in ("n_minus_one", "one_minus_n"):
            low, high = PrimeHaarClock(2, 2, chart), PrimeHaarClock(2, 3, chart)
            values = tuple(Q(x*x-3*x, 7) for x in range(8))
            self.assertEqual(matrix_apply(succ_pullback(8, 2, chart), values),
                             succ_observable(high, values, 2))
            self.assertEqual(matrix_apply(fucc_pullback(8, 2, chart), values),
                             multiply_observable(high, values, 2))
            expected = condition(high, low, values)
            self.assertEqual(matrix_apply(conditional_expectation(8, 4), values), expected*2)
            self.assertEqual(tuple(v/2 for v in sum_fibers(values, 4)), expected)

    def test_nonuniform_measure_breaks_gcd_identity(self):
        # Independent weighted conditional expectations on a correlated CRT pair.
        weights = tuple(map(Q, (2, 1, 1, 1, 1, 1)))
        def weighted(m):
            return tuple(tuple(weights[y]/sum(weights[z] for z in range(6) if z % m == x % m)
                               if x % m == y % m else Q(0) for y in range(6)) for x in range(6))
        self.assertNotEqual(matmul(weighted(2), weighted(3)), weighted(1))

    def test_minimum_portfolio_against_all_subset_decoders(self):
        p = Passport("finite-targets", 0)
        for targets in (("0", "1", "2", "3", "4", "5"),
                        ("even", "odd")*3, ("same",)*6):
            world = World(p, tuple(Candidate(str(x), x, targets[x]) for x in range(6)))
            for ms in ((2, 3), (2, 3, 6), (2,), (1,), (), (2, 2, 3)):
                valid_sizes = []
                for size in range(len(ms)+1):
                    for subset in combinations(ms, size):
                        cells = {}
                        for c in world.candidates:
                            cells.setdefault(tuple(c.integer % m for m in subset), set()).add(c.target)
                        if all(len(labels) == 1 for labels in cells.values()):
                            valid_sizes.append(size)
                actual = minimum_target_portfolio(world, ms)
                if valid_sizes:
                    self.assertEqual(actual.status, "MODEL_TARGET_SEPARATING_PORTFOLIO")
                    self.assertEqual(len(actual.selected), min(valid_sizes))
                else:
                    self.assertEqual(actual.status, "DARK_WITH_THIS_ACCESSIBLE_PORT_FAMILY")

    def test_hidden_source_collision_and_finite_alias(self):
        p = Passport("hidden-target", 0)
        hidden = World(p, (Candidate("a", 7, "left"), Candidate("b", 7, "right")))
        self.assertEqual(target_pair_cover(hidden, (2, 3, 5)), (("a", "b", ()),))
        self.assertEqual(minimum_target_portfolio(hidden, (2, 3, 5)).uncovered_pairs, (("a", "b"),))
        finite = World(p, (Candidate("a", 0, "left"), Candidate("b", 6, "right")))
        self.assertEqual(minimum_target_portfolio(finite, (2, 3)).uncovered_pairs, (("a", "b"),))
        self.assertEqual(len(minimum_target_portfolio(finite, (2, 3, 5)).selected), 1)

    def test_cylinder_algebra_and_compatible_refinements(self):
        f, g = BoundedCylinder((1, -1)), BoundedCylinder((2, -1, -1))
        self.assertEqual(f.multiply(g).values, conductor_six_basis()[0])
        self.assertEqual(f.refine(12), f.refine(6).refine(12))
        self.assertEqual(f.refine(6).sup_norm, f.sup_norm)
        self.assertEqual(f.multiply(g).refine(12), f.refine(12).multiply(g.refine(12)))
        self.assertEqual(f.add(g).refine(12), f.refine(12).add(g.refine(12)))

    def test_fail_closed_on_wrong_carriers_and_inexact_inputs(self):
        for n, m in ((0, 1), (101, 1), (6, 4), (True, 1), (6, 2.0), (6, 0)):
            with self.assertRaises(CollectiveModularError):
                conditional_expectation(n, m)
        for ms in ((), (2,)*13, (7, 16), (True,)):
            with self.assertRaises(CollectiveModularError):
                compatible_crt_image(ms)
        for values in ((), (0.1,), (True,), [1, 2]):
            with self.assertRaises(CollectiveModularError):
                BoundedCylinder(values)
        with self.assertRaises(CollectiveModularError):
            BoundedCylinder((1, 2)).refine(3)
        with self.assertRaises(CollectiveModularError):
            affine_pullback(6, 2.0, 1)
        with self.assertRaises(CollectiveModularError):
            BoundedCylinder((0,)*7).multiply(BoundedCylinder((0,)*16))


if __name__ == "__main__":
    unittest.main()
