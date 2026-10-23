"""Exact calibration of the finite carry lane; not proof of infinite limits."""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial, prod
import unittest

from observational_succ import source_faithful_carry as c
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ.reciprocal_succ_fucc import residue_clock, mixed_radix


def inner(a, b):
    return sum((v*b.get(n, 0) for n, v in a.items()), Q())


def add(*vectors):
    result = {}
    for v in vectors:
        for n, x in v.items():
            result[n] = result.get(n, Q())+x
    return {n: x for n, x in result.items() if x}


def oracle_project(v, radix):
    """Dense matrix oracle: (P_a)ij=1/a iff i,j are in the same block."""
    nmax = max(v, default=0)
    stop = ((nmax+radix-1)//radix)*radix
    out = {}
    for i in range(1, stop+1):
        x = sum((Q(v.get(j, 0), radix) for j in range(1, stop+1)
                 if (i-1)//radix == (j-1)//radix), Q())
        if x:
            out[i] = x
    return out


class CarrySourceTests(unittest.TestCase):
    def test_all_small_source_bijections(self):
        for a in (1, 2, 3, 5, 7, 6, 49):
            for n in range(1, 401):
                m, r = c.radix_address(n, a)
                self.assertEqual(c.source_address(m, r, a), n)
                self.assertTrue(0 <= r < a)

    def test_independent_existing_one_based_oracle(self):
        for a in (2, 3, 5, 7):
            for n in range(1, 101):
                self.assertEqual(c.radix_address(n, a), residue_clock(n, a))

    def test_terminal_not_zero_residue_mutation(self):
        for a in (2, 3, 5, 7):
            for n in (1, 2, 19, 101):
                self.assertEqual(c.radix_address(c.multiplier(n, a), a), (n, a-1))
                self.assertNotEqual(c.radix_address(c.multiplier(n, a), a), (n, 0))

    def test_all_carry_iterates_against_source(self):
        for a, n, h in product((2, 3, 5, 7), range(1, 31), range(0, 19)):
            m, r = c.radix_address(n, a)
            self.assertEqual(c.carry_power(m, r, a, h), c.radix_address(n+h, a))

    def test_adjoint_iterates_include_vacuum(self):
        for a, n, h in product((2, 3, 5, 7), range(1, 31), range(0, 19)):
            m, r = c.radix_address(n, a)
            want = c.radix_address(n-h, a) if n > h else None
            self.assertEqual(c.carry_adjoint_power(m, r, a, h), want)
        self.assertIsNone(c.carry_adjoint_power(1, 0, 2))

    def test_forgotten_carry_fails_at_smallest_source(self):
        self.assertEqual(c.radix_address(1, 2)[0], c.radix_address(2, 2)[0])
        self.assertNotEqual(c.radix_address(2, 2)[0], c.radix_address(3, 2)[0])
        self.assertEqual(c.carry_power(1, 1, 2), (2, 0))
        self.assertNotEqual(c.carry_power(1, 1, 2), (1, 0))

    def test_cuntz_isometries_independent_basis_inner_products(self):
        for a in (2, 3, 5, 6, 7):
            vectors = {(n, r): {c.residue_channel(n, a, r): Q(1)}
                       for n in range(1, 7) for r in range(a)}
            for (n, r), (m, s) in product(vectors, repeat=2):
                self.assertEqual(inner(vectors[n, r], vectors[m, s]), int(n == m and r == s))

    def test_cuntz_complete_sum_and_adjoint(self):
        for a, n in product((2, 3, 5, 6, 7), range(1, 100)):
            result = {}
            for r in range(a):
                m = c.residue_adjoint(n, a, r)
                if m is not None:
                    result[c.residue_channel(m, a, r)] = Q(1)
            self.assertEqual(result, {n: Q(1)})

    def test_v_is_terminal_channel_and_nonunit_adjoint_zero(self):
        for a, n in product((2, 3, 5, 6, 7), range(1, 60)):
            self.assertEqual(c.multiplier(n, a), c.residue_channel(n, a, a-1))
            self.assertEqual(c.multiplier_adjoint(n, a), c.residue_adjoint(n, a, a-1))
        self.assertIsNone(c.multiplier_adjoint(1, 2))

    def test_affine_law_and_actual_adjoint_law(self):
        for a, n in product((2, 3, 5, 6, 7), range(1, 60)):
            self.assertEqual(c.multiplier(n+1, a), c.multiplier(n, a)+a)
            vstar = c.multiplier_adjoint(n, a)
            lhs = vstar-1 if vstar is not None and vstar > 1 else None
            rhs = c.multiplier_adjoint(n-a, a) if n > a else None
            self.assertEqual(lhs, rhs)

    def test_extra_reciprocal_law_not_just_formal_adjoint(self):
        for a, n in product((2, 3, 5, 6, 7), range(1, 60)):
            vstar = c.multiplier_adjoint(n, a)
            self.assertEqual(c.multiplier_adjoint(n+a, a),
                             vstar+1 if vstar is not None else None)

    def test_channel_composition(self):
        for a, b in ((2, 3), (3, 2), (2, 2), (5, 7)):
            for r, s, n in product(range(a), range(b), (1, 3, 11)):
                self.assertEqual(c.residue_channel(c.residue_channel(n, b, s), a, r),
                                 c.residue_channel(n, a*b, r+a*s))

    def test_mixed_words_and_empty_word_roundtrip(self):
        for word in ((), (2,), (2, 3), (2, 2, 3), (7, 5, 3), (6, 2)):
            for n in range(1, 201):
                m, ds = c.mixed_address(n, word)
                self.assertEqual(c.mixed_source(m, ds, word), n)

    def test_triple_change_coherence_all_permutations(self):
        words = tuple(permutations((2, 3, 5)))
        for n in range(1, 61):
            m, ds = c.mixed_address(n, words[0])
            for target in words:
                direct = c.rebase_digits(m, ds, words[0], target)
                for middle in words:
                    mm, dd = c.rebase_digits(m, ds, words[0], middle)
                    self.assertEqual(c.rebase_digits(mm, dd, middle, target), direct)

    def test_mixed_radix_existing_oracle_and_not_naive_swap(self):
        for n in range(1, 100):
            x, y = mixed_radix(n, 2, 3)
            m, ds = c.mixed_address(n, (2, 3))
            self.assertEqual((m, ds[1], ds[0]), x)
            m, ds = c.rebase_digits(m, ds, (2, 3), (3, 2))
            self.assertEqual((m, ds[1], ds[0]), y)
        self.assertNotEqual(c.rebase_digits(1, (1, 1), (2, 3), (3, 2)), (1, (1, 1)))

    def test_endpoint_equality_does_not_equal_history(self):
        word_a, word_b = (2, 3), (3, 2)
        self.assertEqual(c.multiplier(c.multiplier(5, 2), 3),
                         c.multiplier(c.multiplier(5, 3), 2))
        self.assertNotEqual(word_a, word_b)

    def test_character_magnitudes_cannot_authenticate_phase(self):
        for a in (2, 3, 5, 7, 25):
            values = [c.multiplier_character(a, k) for k in range(a)]
            self.assertEqual({x[0] for x in values}, {Q(1, a)})
            self.assertEqual(len({x[1] for x in values}), a)

    def test_character_sign_origin_and_conductor(self):
        for a, k in ((6, 2), (9, 3), (7, 0), (7, 2)):
            self.assertEqual(c.character_conductor(a, k), (3 if a in (6, 9) else 1 if k == 0 else 7))
            for r in range(a):
                t = c.character_phase(a, k, r)
                self.assertEqual(c.character_phase(a, k, r, sign=-1), (-t) % 1)
                self.assertEqual(c.character_phase(a, k, r, origin=1), (t-Q(k, a)) % 1)

    def test_refined_fourier_twiddle_identity(self):
        for a, b in ((2, 3), (3, 5), (2, 2), (7, 3)):
            for r, s, k in product(range(a), range(b), range(a*b)):
                full, low, high = c.refined_character_phase(a, b, k, r, s)
                self.assertEqual(full, (low+high) % 1)

    def test_naive_product_character_mutation(self):
        # Both normalized vectors have identical constant entry magnitudes.
        true = c.character_phase(6, 1, 1)
        fake = (c.character_phase(2, 1, 1)+c.character_phase(3, 1, 0)) % 1
        self.assertEqual(true, Q(1, 6))
        self.assertEqual(fake, Q(1, 2))
        self.assertNotEqual(true, fake)

    def test_global_character_invariant_under_authenticated_rebase(self):
        for n in range(1, 31):
            m, (r, s) = c.mixed_address(n, (2, 3))
            mm, (u, t) = c.rebase_digits(m, (r, s), (2, 3), (3, 2))
            for k in range(6):
                self.assertEqual(c.character_phase(6, k, r+2*s),
                                 c.character_phase(6, k, u+3*t))
            self.assertEqual(m, mm)

    def test_block_projection_against_independent_dense_matrix(self):
        v = {1: Q(3, 4), 2: -2, 7: Q(1, 3), 13: 5, 17: -7}
        for a in (1, 2, 3, 5, 7):
            self.assertEqual(c.block_project(v, a), oracle_project(v, a))
            self.assertEqual(c.block_project(c.block_project(v, a), a), c.block_project(v, a))

    def test_coherent_split_norm_orthogonality_and_reconstruction(self):
        for a in (2, 3, 5, 7):
            v = {1: Q(3, 5), 2: Q(-4, 5), 10: Q(2), 29: Q(-2, 7)}
            visible, defect = c.split_visible_defect(v, a)
            self.assertEqual(add(visible, defect), v)
            self.assertEqual(inner(visible, defect), 0)
            self.assertEqual(c.norm_squared(v), c.norm_squared(visible)+c.norm_squared(defect))

    def test_instrument_complement_normalization(self):
        v = {1: Q(3, 5), 7: Q(4, 5)}
        self.assertEqual(c.norm_squared(v), 1)
        for a in (2, 3, 5, 7):
            u, d = c.split_visible_defect(v, a)
            self.assertEqual(c.norm_squared(u)+c.norm_squared(d), 1)

    def test_dephasing_instrument_not_reversible_control(self):
        # e1 and e2 have same postmeasurement P/Q state ensemble for a=2;
        # the sign of the Q component is lost in each rank-one density matrix.
        p1, d1 = c.split_visible_defect({1: Q(1)}, 2)
        p2, d2 = c.split_visible_defect({2: Q(1)}, 2)
        density = lambda v: {(i, j): x*y for i, x in v.items() for j, y in v.items()}
        self.assertEqual(density(p1), density(p2))
        self.assertEqual(density(d1), density(d2))
        self.assertNotEqual(add(p1, d1), add(p2, d2))

    def test_nested_defect_accounting_is_orthogonal(self):
        v = {1: Q(2), 7: Q(-3), 13: Q(1, 4), 21: Q(8, 5)}
        for a, b in ((2, 3), (3, 2), (2, 2), (5, 7)):
            sectors = c.nested_defect_sectors(v, a, b)
            self.assertEqual(add(*sectors), v)
            self.assertEqual(sum((c.norm_squared(x) for x in sectors), Q()), c.norm_squared(v))
            for i, j in ((0, 1), (0, 2), (1, 2)):
                self.assertEqual(inner(sectors[i], sectors[j]), 0)

    def test_v_uniform_sector_exact_all_state_defect(self):
        v = {1: Q(3, 5), 4: Q(-4, 5)}
        for a in (2, 3, 5, 6, 7):
            out = c.source_push(v, lambda n: c.multiplier(n, a))
            visible, defect = c.split_visible_defect(out, a)
            self.assertEqual(c.norm_squared(out), 1)
            self.assertEqual(c.norm_squared(visible), Q(1, a))
            self.assertEqual(c.norm_squared(defect), 1-Q(1, a))

    def test_block_overlap_squared_by_independent_support_count(self):
        for a, m in product((2, 3, 5, 7), (1, 2, 11, 97)):
            support = {a*n for n in range(1, m+1)}
            overlap_squared = Q(len(support & set(range(1, a*m+1)))**2, m*(a*m))
            self.assertEqual(overlap_squared, c.uniform_defect(a)["overlap_squared"])

    def test_compressed_successor_all_h_basis_count(self):
        for a, h in product((2, 3, 5, 7), range(0, 43)):
            # Lift e_m uniformly, apply actual S^h, count coarse blocks.
            m = 4
            counts = {}
            for r in range(a):
                target = (a*(m-1)+r+h)//a+1
                counts[target-m] = counts.get(target-m, Q())+Q(1, a)
            self.assertEqual(c.compressed_successor(h, a), counts)

    def test_compression_does_not_preserve_semigroup_mutation(self):
        for a in (2, 3, 5, 7):
            once = c.compressed_successor(1, a)
            square = {}
            for i, x in once.items():
                for j, y in once.items():
                    square[i+j] = square.get(i+j, Q())+x*y
            direct = c.compressed_successor(2, a)
            difference = {k: direct.get(k, Q())-square.get(k, Q()) for k in (0, 1, 2)}
            self.assertEqual(difference, {0: -Q(1, a*a), 1: Q(2, a*a), 2: -Q(1, a*a)})
            self.assertNotEqual(direct, square)

    def test_half_density_authentication_and_source_endpoint(self):
        for p, r in product((2, 3, 5, 7), range(1, 7)):
            term = c.PrimePowerHalfDensity(p, r)
            self.assertEqual(c.multiplier(term.input_state, p), term.endpoint)
            self.assertEqual(c.radix_address(term.endpoint, term.endpoint), (1, term.endpoint-1))
            self.assertEqual(c.prime_power_at(term.endpoint), term)

    def test_energy_cocycle_domain_and_terminal_channel(self):
        for a, m in product((2, 3, 5, 7), (1, 2, 19, 101)):
            for r in range(a):
                ratio = c.energy_cocycle_ratio(m, r, a)
                self.assertTrue(1 <= ratio <= a)
            self.assertEqual(c.energy_cocycle_ratio(m, a-1, a), a)
            self.assertLess(c.energy_cocycle_ratio(m, 0, a), a)

    def test_energy_cocycle_refinement_not_constant_shift(self):
        for a, b in ((2, 3), (3, 2), (2, 2), (5, 7)):
            for m, r, s in product((1, 5, 17), range(a), range(b)):
                j = b*(m-1)+s+1
                self.assertEqual(c.energy_cocycle_ratio(m, r+a*s, a*b),
                                 c.energy_cocycle_ratio(j, r, a)*c.energy_cocycle_ratio(m, s, b))
        self.assertEqual(c.energy_cocycle_ratio(1, 0, 2), 1)
        self.assertNotEqual(c.energy_cocycle_ratio(1, 0, 2), 2)

    def test_coarse_energy_factorial_identity_and_constant_shift_mutant(self):
        for a, m in product((2, 3, 5, 7), (1, 2, 9)):
            self.assertEqual(c.coarse_energy_product(m, a),
                             Q(factorial(a*m), factorial(a*(m-1))*m**a))
            self.assertNotEqual(c.coarse_energy_product(m, a), a**a)

    def test_fake_composite_passes_geometry_fails_primitive_gate(self):
        self.assertEqual(c.radix_address(c.multiplier(4, 6), 6), (4, 5))
        self.assertEqual(c.uniform_defect(6)["visible_norm_squared"], Q(1, 6))
        self.assertIsNone(c.prime_power_at(6))
        with self.assertRaises(c.CarrySourceError):
            c.PrimePowerHalfDensity(6, 1)
        with self.assertRaises(c.CarrySourceError):
            c.PrimePowerHalfDensity(4, 2)

    def test_dirichlet_log_retains_repeated_primes_rejects_fake_six(self):
        source = GammaInterferometer.from_prefix({n: 1 for n in range(1, 65)}, 64)
        for n in range(2, 65):
            pp = c.prime_power_at(n)
            self.assertEqual(source.connected[n], pp.dirichlet_log_coefficient if pp else 0)
        mutant = {n: 1 for n in range(1, 65)}
        mutant[6] = 2
        fake = GammaInterferometer.from_prefix(mutant, 64)
        self.assertEqual(source.connected[6], 0)
        self.assertEqual(fake.connected[6], 1)

    def test_half_density_intervals_sound_integer_checks(self):
        # Independently established elementary inequalities: 1/2<log2<1,
        # 1<log3<3/2, and exact sqrt(4)=2, sqrt(9)=3.
        for term, lower, upper in ((c.PrimePowerHalfDensity(2, 2), Q(1, 4), Q(1, 2)),
                                   (c.PrimePowerHalfDensity(3, 2), Q(1, 3), Q(1, 2))):
            lo, hi = term.interval()
            self.assertTrue(lower < lo <= hi < upper)
            self.assertLess(hi-lo, Q(1, 10**20))
        for p in (2, 3, 5, 7):
            coarse = c.PrimePowerHalfDensity(p, 3).interval(terms=8, binary_places=16)
            fine = c.PrimePowerHalfDensity(p, 3).interval(terms=32, binary_places=96)
            self.assertTrue(coarse[0] <= fine[0] <= fine[1] <= coarse[1])

    def test_exact_type_and_domain_mutations(self):
        calls = (lambda: c.radix_address(0, 2), lambda: c.radix_address(1, False),
                 lambda: c.radix_address(1, 2.0), lambda: c.source_address(1, 2, 2),
                 lambda: c.carry_power(1, 0, 2, -1), lambda: c.exact_vector({1: 0.5}),
                 lambda: c.character_phase(2, True, 0), lambda: c.character_phase(2, 1, 0, sign=True),
                 lambda: c.rebase_digits(1, (0,), (2,), (3,)),
                 lambda: c.mixed_source(1, (0, 1), (2,)),
                 lambda: c.PrimePowerHalfDensity(2, 0), lambda: c.prime_power_at(True))
        for call in calls:
            with self.assertRaises(c.CarrySourceError):
                call()


if __name__ == "__main__":
    unittest.main()
