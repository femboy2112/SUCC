"""Hostile tests for the original-source BBP coupled finite oracle."""
from __future__ import annotations

import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ import duck_bbp
from observational_succ.bbp_coupled_oracle import (
    OracleError, RootPrefixCertificate, UnresolvedAtPrecision,
    certify_root, certify_square, closed_root_enclosure,
    pure_gauge_holonomy, refinement_energy, snapshot, verify_green_transport,
    finite_prefix_signal, temporal_energy,
)


class CoupledOracleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = certify_root(32, 17)

    def test_source_contract_four_signed_poles(self):
        for n in range(1, 35):
            expected = 4*Q(1,8*n-7)-2*Q(1,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            self.assertEqual(duck_bbp.forcing(n), expected)

    def test_green_interval_naturality_all_endpoints(self):
        for n in range(0, 14):
            for depth in range(0, 12):
                lo, hi = verify_green_transport(n, depth)
                self.assertLess(lo, hi)

    def test_global_root_prefix_certifies_each_orbit_cell(self):
        cert = self.root
        for n in range(1, 13):
            for k in (1, 2, 3):
                claimed = cert.word(n, k)
                u = duck_bbp.lifted_orbit(n)
                tlo, thi = duck_bbp.tail_interval(n, 32-n)
                self.assertEqual((16**k*(u+tlo)).numerator // (16**k*(u+tlo)).denominator % (16**k), claimed)
                self.assertEqual((16**k*(u+thi)).numerator // (16**k*(u+thi)).denominator % (16**k), claimed)

    def test_root_authenticity_and_no_guessing(self):
        with self.assertRaises(UnresolvedAtPrecision):
            certify_root(0, 3)
        with self.assertRaises(UnresolvedAtPrecision):
            self.root.word(17, 1)
        with self.assertRaises(OracleError):
            replace(self.root, prefix=self.root.prefix + 1)
        with self.assertRaises(OracleError):
            replace(self.root, source_id='forged-source')
        with self.assertRaises(OracleError):
            replace(self.root, upper=self.root.upper + Q(1, 16**30))
        with self.assertRaises(OracleError):
            certify_root(True, 5)

    def test_square_energy_and_word_path_commute(self):
        for N in range(1, 10):
            for k in (1, 2, 3):
                receipt = certify_square(self.root, N, k)
                self.assertTrue(receipt.exact_word_square_commutes)
                self.assertEqual(receipt.square_energy_commutator, 0)
                self.assertGreaterEqual(receipt.horizontal_refinement_N, 0)
                self.assertGreaterEqual(receipt.horizontal_refinement_N1, 0)

    def test_source_locked_signed_time_edge(self):
        old = snapshot(self.root, 5, 1)
        new = snapshot(self.root, 6, 1)
        w = self.root.word(6, 1)
        self.assertEqual(temporal_energy(old, new, w), new.energy-old.energy)
        with self.assertRaises(OracleError):
            temporal_energy(old, new, (w+1)%16)
        with self.assertRaises(OracleError):
            temporal_energy(replace(old, energy=Q(0)), new, w)

    def test_exact_tv_energy_and_universal_coverage_ceiling(self):
        for k in (1, 2, 3):
            snap = snapshot(self.root, 9, k)
            M, N = 16**k, 9
            d = Q(1, 2)*(
                sum((abs(Q(c,N)-Q(1,M)) for _,c in snap.counts), Q())
                + Q(M-len(snap.counts), M))
            self.assertEqual(snap.variation, d)
            self.assertEqual(snap.energy, Q(M*sum(c*c for _,c in snap.counts),N*N)-1)
            self.assertGreaterEqual(snap.variation, snap.coverage_lower)
            self.assertGreaterEqual(snap.energy, Q(M,N)-1)

    def test_time_energy_can_increase_or_decrease(self):
        # A universal time-monotonic signal would be false: even on the
        # selected BBP prefix, adding a sample changes collision energies.
        changes = []
        for N in range(1, 12):
            changes.append(snapshot(self.root,N+1,1).energy - snapshot(self.root,N,1).energy)
        self.assertTrue(any(x < 0 for x in changes))
        self.assertTrue(any(x > 0 for x in changes))

    def test_certified_knowledge_signal_is_monotone_but_not_normality(self):
        values = [finite_prefix_signal(depth, budget=25).certified_digits
                  for depth in range(36)]
        self.assertEqual(values, sorted(values))
        self.assertGreaterEqual(values[-1], 17)
        self.assertFalse(finite_prefix_signal(0, 25).budget_saturated)
        self.assertTrue(finite_prefix_signal(32, 10).budget_saturated)

    def test_pure_gauge_is_flat_not_source_curvature(self):
        for n in range(0, 20):
            for h in (-7, -1, 0, 1, 4, 16):
                self.assertEqual(pure_gauge_holonomy(n, h), 0)

    def test_coherent_prefix_allows_nonnormal_counterfeit(self):
        # Counterfeit rational shares the exact 17-digit certified prefix,
        # but then has a repeating zero hexadecimal tail: nonnormal.
        cert = self.root
        beta = Q(2*cert.prefix+1, 2*16**cert.digits)
        self.assertEqual((16**cert.digits * beta).numerator // (16**cert.digits*beta).denominator, cert.prefix)
        for n in range(1, 11):
            for k in (1,2,3):
                self.assertEqual((16**k*beta*16**n).numerator // (16**k*beta*16**n).denominator %16**k, cert.word(n,k))
        self.assertEqual(((16**(cert.digits+5)*beta) % 1),0)
        # This fake beta has no authenticated BBP/zero-seed law.

    def test_invalid_cross_source_refinement_rejected(self):
        parent = snapshot(self.root, 7, 1)
        child = snapshot(self.root, 7, 2)
        self.assertGreaterEqual(refinement_energy(parent, child),0)
        with self.assertRaises(OracleError):
            refinement_energy(replace(parent, source_id='fake'),child)
        with self.assertRaises(OracleError):
            refinement_energy(parent, replace(child, n_samples=8))
        with self.assertRaises(OracleError):
            refinement_energy(parent, replace(child, counts=((0,7),)))
        with self.assertRaises(OracleError):
            refinement_energy(parent, replace(child, energy=Q(0)))
        with self.assertRaises(OracleError):
            refinement_energy(replace(parent, source_id='fake'),replace(child, source_id='fake'))

    def test_source_interval_shrinks_and_zero_seed_is_explicit(self):
        previous = closed_root_enclosure(0)
        for depth in range(1, 16):
            current = closed_root_enclosure(depth)
            self.assertGreater(current[0], previous[0])
            self.assertLess(current[1], previous[1])
            self.assertEqual(current[0] * 16**depth, duck_bbp.lifted_orbit(depth))
            previous = current


if __name__ == '__main__':
    unittest.main()
