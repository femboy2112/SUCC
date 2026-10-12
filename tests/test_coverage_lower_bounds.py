"""Exact adversarial finite controls. Universal proofs are in the research dossier."""
import sys
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.coverage_lower_bounds import (
    CoverageError, CoverageFrame, uniform_frame, collision_index,
    independent_product, translation_audit, gaussian_coordinate,
    gaussian_frame, lattice_snake, bernoulli_succ_block,
    amplify_minorization, cyclic_convolution, block_coverage_audit,
    batch_coverage_lower_bound, signed_succ_block,
)


class CoverageLowerBoundTests(unittest.TestCase):
    def test_uniform_source_has_full_coverage_at_any_allowed_threshold(self):
        for q in range(2, 18):
            frame = uniform_frame('exact source', 'readout', (F(1, q),) * q)
            self.assertEqual(frame.chi2, 0)
            for tau in (F(1, 4), F(1, 2), F(9, 10)):
                report = frame.bound(tau)
                self.assertEqual(report['lower_mass'], 1)
                self.assertEqual(report['good_mass'], 1)
                self.assertEqual(report['exception_count'], 0)

    def test_every_small_exact_rational_law_passes_sharp_coverage(self):
        for q in (2, 3, 4):
            for weights in product(range(5), repeat=q):
                if not sum(weights):
                    continue
                frame = uniform_frame('complete-small-law', 'clock',
                                      tuple(F(t, sum(weights)) for t in weights))
                for tau in (F(1, 4), F(1, 2), F(3, 4)):
                    receipt = frame.bound(tau)
                    self.assertGreaterEqual(receipt['good_mass'], receipt['lower_mass'])
                    self.assertEqual(receipt['exception_count'],
                                     sum(p < tau / q for p in frame.masses))

    def test_nonuniform_reference_full_exhaustion(self):
        for refs in product(range(1, 5), repeat=3):
            pi = tuple(F(t, sum(refs)) for t in refs)
            for weights in product(range(3), repeat=3):
                if not sum(weights):
                    continue
                p = tuple(F(t, sum(weights)) for t in weights)
                frame = CoverageFrame('origin', 'mixed', (0, 1, 2), p, pi)
                self.assertGreaterEqual(frame.bound(F(1, 2))['good_mass'],
                                        frame.bound(F(1, 2))['lower_mass'])

    def test_two_level_bound_is_sharp_in_limit(self):
        # One residue is JUST below tau*pi; the others compensate equally.
        lower = F(4, 5)
        for delta in (F(1, 100), F(1, 10000), F(1, 1000000)):
            p0 = F(1, 10) - delta
            frame = uniform_frame('sharpness', 'five',
                                  (p0,) + ((1 - p0) / 4,) * 4)
            receipt = frame.bound(F(1, 2))
            self.assertEqual(receipt['good_mass'], lower)
            self.assertEqual(receipt['exception_count'], 1)
        self.assertLess(receipt['good_mass'] - receipt['lower_mass'], F(1, 100000))

    def test_chi_square_is_exactly_independent_pair_collision(self):
        for weights in product(range(4), repeat=3):
            if not sum(weights):
                continue
            n = sum(weights)
            manual = sum(F(a * a, n * n) for a in weights)
            self.assertEqual(collision_index(weights), 3 * manual - 1)
            self.assertEqual(uniform_frame('pair', 'mod3',
                tuple(F(w, n) for w in weights)).chi2, collision_index(weights))

    def test_markov_data_processing_for_every_binary_rational_kernel(self):
        for r in range(1, 5):
            for a in range(1, r):
                pi = (F(a, r), 1 - F(a, r))
                for k in range(5):
                    p = (F(k, 4), 1 - F(k, 4))
                    frame = CoverageFrame('source', 'prior', ('a', 'b'), p, pi)
                    for t, u in product(range(4), repeat=2):
                        rows = ((F(t, 3), 1 - F(t, 3)),
                                (F(u, 3), 1 - F(u, 3)))
                        got = frame.push(('left', 'right'), rows, 'after')
                        self.assertLessEqual(got.chi2, frame.chi2)
                        got.bound(F(3, 4))

    def test_composing_observers_matches_single_composite_channel(self):
        start = uniform_frame('S1', 'fine', (F(1, 5), F(2, 5), F(2, 5)))
        k = ((F(1, 2), F(1, 2)), (F(0), F(1)), (F(1), F(0)))
        j = ((F(1, 3), F(2, 3)), (F(2, 5), F(3, 5)))
        staged = start.push(('x', 'y'), k, 'medium').push(('u', 'v'), j, 'coarse')
        composed = tuple(tuple(sum(k[i][z] * j[z][w] for z in range(2))
                               for w in range(2)) for i in range(3))
        direct = start.push(('u', 'v'), composed, 'direct')
        self.assertEqual(staged.masses, direct.masses)
        self.assertEqual(staged.reference, direct.reference)
        self.assertEqual(staged.chi2, direct.chi2)
        self.assertEqual(staged.epoch, 2)
        self.assertEqual(direct.epoch, 1)
        self.assertEqual(start.source_id, staged.source_id)

    def test_coarse_reference_must_be_pushed_not_fabricated_uniform(self):
        start = uniform_frame('provenance', 'source', (F(1, 4),) * 4)
        coarse = start.push(('majority', 'minority'),
            ((F(1), F(0)), (F(1), F(0)),
             (F(1), F(0)), (F(0), F(1))), 'true quotient')
        self.assertEqual(coarse.reference, (F(3, 4), F(1, 4)))
        self.assertEqual(coarse.masses, coarse.reference)
        self.assertEqual(coarse.bound(F(3, 4))['good_mass'], 1)
        counterfeit = uniform_frame('provenance', 'falsely Haar', coarse.masses)
        self.assertNotEqual(counterfeit.chi2, coarse.chi2)
        self.assertNotEqual(counterfeit.bound(F(3, 4))['good_mass'], 1)

    def test_degenerate_kernel_and_mutations_rejected(self):
        frame = uniform_frame('source', 'fine', (F(1, 2), F(1, 2)))
        with self.assertRaises(CoverageError):
            uniform_frame('', 'fine', (F(1, 2), F(1, 2)))
        with self.assertRaises(CoverageError):
            uniform_frame('valid', 'fine', (0.5, 0.5))
        with self.assertRaises(CoverageError):
            CoverageFrame('valid', 'fine', ('x', 'x'), (F(1, 2),)*2, (F(1, 2),)*2)
        with self.assertRaises(CoverageError):
            frame.bound(F(1))
        with self.assertRaises(CoverageError):
            frame.push(('x', 'y'), ((F(3, 2), F(-1, 2)), (F(0), F(1))), 'invalid')

    def test_independent_tensor_identity_and_missing_independence_refusal(self):
        a = uniform_frame('A', 'a', (F(3, 4), F(1, 4)))
        b = uniform_frame('B', 'b', (F(1, 3), F(1, 3), F(1, 3)))
        with self.assertRaises(CoverageError):
            independent_product(a, b)
        prod = independent_product(a, b, declared_independent=True)
        self.assertEqual(1 + prod.chi2, (1 + a.chi2) * (1 + b.chi2))
        prod.bound(F(1, 2))

    def test_correlated_translation_collapse_refutes_free_coverage_transport(self):
        q = 5
        collapsed = translation_audit(tuple((x, (-x) % q, F(1, q))
                                           for x in range(q)), q, 'original')
        self.assertEqual(collapsed['source'].chi2, 0)
        self.assertEqual(collapsed['terminal'].chi2, 4)
        self.assertEqual(collapsed['conditional_energy'], 4)
        self.assertFalse(collapsed['independent_update'])
        self.assertEqual(collapsed['terminal'].bound(F(1, 2))['exception_count'], 4)

    def test_independent_translation_contracts_energy_exactly(self):
        for q in (3, 5):
            joint = tuple((x, u, F((x + 1) * (u + 1),
                (q * (q + 1) // 2) ** 2)) for x in range(q) for u in range(q))
            audit = translation_audit(joint, q, 'independent-source')
            self.assertTrue(audit['independent_update'])
            self.assertLessEqual(audit['terminal'].chi2, audit['source'].chi2)
            self.assertEqual(audit['conditional_energy'], audit['source'].chi2)

    def test_gaussian_factor_is_true_source_not_fake_composite(self):
        self.assertEqual(gaussian_coordinate((1, 2), (1, 2)), 0)
        self.assertEqual(gaussian_coordinate((1, -2), (1, -2)), 0)
        for fake in ((3, 4), (3, 0), (1, 1)):
            with self.assertRaises(CoverageError):
                gaussian_coordinate((0, 0), fake)

    def test_exact_uniform_gaussian_coverage_from_full_grid_snake(self):
        path = lattice_snake(65)
        self.assertEqual(len(set(path)), 65 ** 2)
        self.assertTrue(all(abs(x2 - x1) + abs(y2 - y1) == 1
            for (x1, y1), (x2, y2) in zip(path, path[1:])))
        for factor in ((1, 2), (1, -2), (2, 3), (2, -3)):
            frame = gaussian_frame(path, factor, 'full-grid source, NOT Gaussian primes')
            self.assertEqual(frame.chi2, 0)
            self.assertEqual(frame.bound(F(1, 4))['exception_count'], 0)

    def test_short_prime_norm_window_has_exact_coverage_obstruction(self):
        path = tuple((n, 0) for n in range(4))
        # Every difference has norm < 13; projection modulo pi (norm 13)
        # is injective but four observed positions cannot cover 13 residues.
        self.assertTrue(all((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 < 13
                         for x in path for y in path))
        report = gaussian_frame(path, (2, 3), 'short path').bound(F(1, 4))
        self.assertEqual(report['exception_count'], 9)
        self.assertEqual(report['good_mass'], F(4, 13))

    def test_bernoulli_succ_primitive_coverage_formula(self):
        for q in range(2, 13):
            frame, alpha = bernoulli_succ_block(q)
            self.assertEqual(min(frame.masses), F(1, 2**(q-1)))
            self.assertEqual(alpha, F(q, 2**(q-1)))
            for z in frame.atoms:
                self.assertGreaterEqual(frame.masses[z], alpha / q)
        with self.assertRaises(CoverageError):
            bernoulli_succ_block(5, F(1))

    def test_nonzero_signed_succ_generator_coverage(self):
        for q in (3, 5, 7, 11, 13):
            frame, alpha = signed_succ_block(q)
            self.assertEqual(min(frame.masses), F(1, 2**(q-1)))
            self.assertEqual(alpha, F(q, 2**(q-1)))
            self.assertGreaterEqual(min(frame.masses), alpha / q)
            if q <= 5:
                self.assertEqual(frame.bound(F(1, 4))['exception_count'], 0)
        with self.assertRaises(CoverageError):
            signed_succ_block(4)

    def test_bernoulli_biased_clock_and_minoration(self):
        for bias in (F(1, 3), F(2, 3), F(1, 4)):
            q = 5
            frame, alpha = bernoulli_succ_block(q, bias)
            self.assertEqual(min(frame.masses), min(bias, 1-bias) ** 4)
            self.assertEqual(alpha, q * min(frame.masses))

    def test_covered_mass_amplifies_under_independent_blocks(self):
        for q in (3, 5, 7):
            for blocks in (1, 2, 3):
                audit = block_coverage_audit(q, blocks)
                self.assertEqual(audit['tau'], 1 - (1 - audit['alpha']) ** blocks)
                self.assertGreaterEqual(min(audit['law']), audit['tau'] / q)
                self.assertLessEqual(audit['frame'].chi2,
                    block_coverage_audit(q, 1)['frame'].chi2)
        self.assertEqual(amplify_minorization(F(1), 20), 1)
        with self.assertRaises(CoverageError):
            amplify_minorization(F(1, 2), 0)

    def test_joint_collision_budget_proves_many_good_coordinates_without_independence(self):
        zero = uniform_frame('same source', 'uniform', (F(1, 5),) * 5)
        one = uniform_frame('same source', 'one missing',
                            (F(0), F(1, 4), F(1, 4), F(1, 4), F(1, 4)))
        frames = (zero,) * 99 + (one,)
        audit = batch_coverage_lower_bound(frames, F(1, 2), F(1, 5))
        self.assertEqual(audit['mean_chi2'], F(1, 400))
        self.assertEqual(audit['coordinate_fraction_lower'], F(24, 25))
        self.assertEqual(audit['coordinate_fraction_observed'], F(99, 100))
        self.assertEqual(audit['actual_bad_coordinates'], 1)
        # All coordinates can share the same source bit; independence is not used.
        with self.assertRaises(CoverageError):
            batch_coverage_lower_bound(frames +
                (uniform_frame('different source', 'forged', (F(1, 5),) * 5),),
                F(1, 2), F(1, 5))
        with self.assertRaises(CoverageError):
            batch_coverage_lower_bound((zero, zero.push(('x',), ((F(1),),)*5, 'changed')),
                                       F(1, 2), F(1, 5))

    def test_cyclic_convolution_exact_reference_and_nontrivial_shift(self):
        a = (F(1, 2), F(1, 2), F(0))
        delta = (F(0), F(1), F(0))
        self.assertEqual(cyclic_convolution(a, delta), (F(0), F(1, 2), F(1, 2)))
        with self.assertRaises(CoverageError):
            cyclic_convolution(a, (F(1), F(0)))


if __name__ == '__main__':
    unittest.main()
