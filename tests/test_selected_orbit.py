"""Shared selected-orbit framework (Main XX) and the exact carry–interval identity CB-1.

No π-normality claim: every number checked here is a finite exact receipt.
"""
import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from observational_succ import duck_bbp
from observational_succ import selected_orbit as so


def one_pole_mutant(n):
    return so.four_pole_forcing(n, weights=(5, -2, -1, -1))


class SourceAndStates(unittest.TestCase):
    def test_closed_form_equals_four_pole_form(self):
        for n in range(1, 400):
            self.assertEqual(so.original_forcing(n), so.four_pole_forcing(n))

    def test_states_match_formal_core_and_zero_seed(self):
        orb = so.SelectedOrbit()
        self.assertEqual(orb.state(0), 0)
        for n in (1, 2, 7, 33, 60):
            self.assertEqual(orb.state(n), duck_bbp.forced_orbit(n))

    def test_source_sum_transports_states(self):
        orb = so.SelectedOrbit()
        for n in (5, 40, 90):
            for k in (1, 2, 5):
                self.assertEqual((16 ** k * orb.state(n) + orb.source_sum(k, n)) % 1, orb.state(n + k))

    def test_green_tail_enclosure_and_recursion(self):
        for n in (3, 50, 400):
            lo, hi = so.green_tail_interval(n)
            lo1, hi1 = so.green_tail_interval(n + 1)
            self.assertLess(lo, hi)
            r = so.original_forcing(n + 1)
            self.assertLessEqual(16 * lo - hi1, r)  # 16T_n - T_(n+1) = r(n+1)
            self.assertGreaterEqual(16 * hi - lo1, r)
            self.assertLess(abs(64 * n * n * lo - 1), Fraction(1, n))  # T_n ~ 1/(64 n^2)


class CarryIntervalIdentity(unittest.TestCase):
    """CB-1: b_{n,m,k} = 1[S_m(n+k) <= x_{n+d} < S_d(n)], δ = S_d(n) - S_m(n+k)."""

    def _check(self, orb, A):
        if orb.forcing is so.original_forcing:
            depths = so.critical_depths(A)
        else:  # mutant forcings have their own scale (e.g. a nonzero 1/n moment)
            depths = [d for d in range(2, 12)
                      if all(orb.source_sum(d, n) < 1 for n in range(A, 2 * A))]
        self.assertTrue(depths)
        checked = 0
        for d in depths:
            for m in range(1, d):
                k = d - m
                for n in range(A, 2 * A):
                    self.assertEqual(orb.carry_by_definition(n, m, k), orb.carry_by_window(n, m, k))
                    checked += 1
        return checked

    def test_zero_seed_preregistered_epochs(self):
        orb = so.SelectedOrbit()
        self.assertGreater(self._check(orb, 64) + self._check(orb, 173), 1000)

    def test_identity_is_generic_not_a_fingerprint(self):
        # rational seed (a rotation, 16≡1 mod 5) and a one-pole mutant obey it too
        self._check(so.SelectedOrbit(seed=Fraction(1, 5)), 64)
        self._check(so.SelectedOrbit(forcing=one_pole_mutant), 64)

    def test_innovation_two_paths_agree_exactly(self):
        orb = so.SelectedOrbit()
        d = so.critical_depths(64)[-1]
        for m in (1, d - 1):
            self.assertEqual(orb.innovation(64, m, d - m, by="window"),
                             orb.innovation(64, m, d - m, by="definition"))

    def test_admissibility_depends_on_depth_and_is_monotone(self):
        ds = so.critical_depths(173)
        self.assertEqual(ds, list(range(2, ds[-1] + 1)))
        self.assertFalse(so.admissible(173, 1, ds[-1]))


class FrameworkHygiene(unittest.TestCase):
    def test_weyl_coefficient_does_not_leak_precision(self):
        saved = mp.mp.dps
        try:
            mp.mp.dps = 15
            c = so.SelectedOrbit().weyl_coefficient(16, 1, dps=50)
            self.assertEqual(mp.mp.dps, 15)
            self.assertLessEqual(abs(c), 1)
        finally:
            mp.mp.dps = saved

    def test_receipt_is_deterministic_and_rejects_unknown_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            dep = Path(tmp) / "dep.txt"
            dep.write_text("x")
            out = Path(tmp) / "r.json"
            args = dict(claims={"CB-1": "PROVED"}, depends_on=["dep.txt"], root=tmp)
            so.write_receipt(out, {"J": Fraction(-3, 7)}, **args)
            first = out.read_bytes()
            so.write_receipt(out, {"J": Fraction(-3, 7)}, **args)
            self.assertEqual(first, out.read_bytes())
            doc = json.loads(first)
            self.assertEqual(doc["payload"]["J"], "-3/7")
            self.assertEqual(doc["pi_normality"], "OPEN")
            with self.assertRaises(ValueError):
                so.write_receipt(out, {}, claims={"X": "PROVED-BY-VIBES"})


if __name__ == "__main__":
    unittest.main()
