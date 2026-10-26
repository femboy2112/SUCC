"""Tests for observational_succ.signed_pushforward.

Verifies the signed K -> P K P^* adapter as a NEGATIVE theorem + firewall
sharpening: conservation/coarsening invariance, signed base change <=> cartesian,
the ghost-faithfulness-is-insufficient control, signed-blindness, the source-blind
positive-Gram rotation countermodel, and the occupancy-baseline trap (phase-blind
(H-1)/N is NOT the Weyl gate).  All exact over Q[Q/Z] unless marked OBSERVED.
"""
import unittest
from fractions import Fraction as Q

import observational_succ.beck_chevalley_source as bc
import observational_succ.signed_pushforward as sp
from observational_succ import mobius_signed_contrasts as MSC
from observational_succ.succ_internal_matrix_walk import PhasePoly as PP, authentic_r, circle

e = lambda th: PP.monomial(Q(th))


def _carry_labels(states):
    cs, u = [], Q(0)
    for n in range(1, len(states) + 1):
        c = (16 * circle(u) + authentic_r(n)).__floor__()
        u = states[n - 1]
        cs.append(c)
    return cs


def _poledepth(n):
    return tuple(min(2, max(0, -MSC.valuation(authentic_r(n), p))) for p in (3, 5, 7))


class SignedBaseChangeFirewall(unittest.TestCase):
    def test_amplitude_base_change_iff_cartesian(self):
        # cartesian clock square: holds for a nontrivial amplitude, and is_cartesian True
        sq = bc.clock_quotient_square(12, 3, 6)
        z = {s: e(Q(s, 12)) for s in sq.S}
        self.assertTrue(bc.is_cartesian(sq))
        self.assertTrue(sp.amplitude_base_change_holds(sq, z))
        self.assertTrue(sp.quadratic_base_change_holds(sq, z))
        # both failure modes: non-cartesian => base change fails == is_cartesian False
        sqg, _ = bc.firewall_square()
        self.assertFalse(bc.is_cartesian(sqg))
        self.assertFalse(sp.amplitude_base_change_holds(sqg, {"s0": e(0), "s1": e(Q(1, 2))}))
        sqr = bc.realization_faithful_noncartesian_square()
        self.assertFalse(bc.is_cartesian(sqr))
        self.assertFalse(sp.amplitude_base_change_holds(sqr, {"s0": e(Q(1, 3))}))

    def test_ghost_firewall_fires(self):  # NC1
        sqg, _ = bc.firewall_square()
        rep = sp.signed_firewall_report(sqg, {"s0": e(0), "s1": e(Q(1, 2))})
        self.assertTrue(rep["ghost_firewall_breaks"])
        self.assertFalse(rep["amplitude_bc"])
        self.assertEqual(rep["amplitude_defect"], {"p0": e(Q(1, 2))})

    def test_ghost_faithful_square_still_breaks_signed_base_change(self):  # NC2 (keeper)
        # The one new product: no ghost + Prop-BC-for-all, yet signed base change FAILS.
        sqr = bc.realization_faithful_noncartesian_square()
        rep = sp.signed_firewall_report(sqr, {"s0": e(Q(1, 3))})
        self.assertFalse(rep["ghost_firewall_breaks"])   # realization-faithful
        self.assertTrue(rep["prop_bc_all"])              # Prop base change holds for all F
        self.assertFalse(rep["amplitude_bc"])            # ... yet signed transport breaks
        self.assertFalse(rep["cartesian"])               # correct firewall is is_cartesian

    def test_signed_blindness(self):  # NC3
        sq = bc.clock_quotient_square(12, 3, 6)
        z_coh = {s: e(0) for s in sq.S}
        z_can = {s: e(Q(s % 2, 2)) for s in sq.S}
        r_coh = sp.signed_firewall_report(sq, z_coh)
        r_can = sp.signed_firewall_report(sq, z_can)
        keys = ("cartesian", "comparison_surjective", "ghost_firewall_breaks", "prop_bc_all")
        self.assertTrue(all(r_coh[k] == r_can[k] for k in keys))  # identical categorical report
        self.assertNotEqual(sp.amp_pushforward(sq.q, z_coh),
                            sp.amp_pushforward(sq.q, z_can))        # different signed energy


class ConservationAndTrap(unittest.TestCase):
    def setUp(self):
        self.states = sp.authentic_states(32)
        self.h = 1

    def test_conservation_coarsening_invariant(self):
        cs = _carry_labels(self.states)
        labs = {
            "singleton": lambda n, u: ("s", n),
            "carry": lambda n, u: ("c", cs[n - 1]),
            "pole": lambda n, u: ("p", _poledepth(n)),
            "both": lambda n, u: ("b", cs[n - 1], _poledepth(n)),
        }
        for name, lab in labs.items():
            self.assertTrue(sp.conservation_holds(self.states, lab, self.h), name)
        # functoriality: coarsen (carry x pole) -> carry; cell moments must merge
        fine = sp.cell_moments(self.states, labs["both"], self.h)
        coarse = sp.cell_moments(self.states, labs["carry"], self.h)
        merged = {}
        for (_, c, _pd), (cnt, s) in fine.items():
            k = ("c", c)
            cnt0, s0 = merged.get(k, (0, PP.zero()))
            merged[k] = (cnt0 + cnt, s0 + s)
        for k in coarse:
            self.assertEqual(merged[k][1], coarse[k][1])
            self.assertEqual(merged[k][0], coarse[k][0])

    def test_rotation_countermodel_positive_gram_blind(self):  # NC1 (B-side)
        cs = _carry_labels(self.states)
        lab = lambda n, u: ("b", cs[n - 1], _poledepth(n))
        cells = sp.cell_moments(self.states, lab, self.h)
        keys = sorted(cells, key=str)
        theta = {k: Q(i, len(keys)) for i, k in enumerate(keys)}
        rot = sp.rotate_cells(cells, theta)
        # within-cell diagonal energies and sizes INVARIANT (exact Q[Q/Z])
        self.assertEqual(sp.within_cell_energy(cells), sp.within_cell_energy(rot))
        self.assertTrue(all(cells[k][0] == rot[k][0] for k in keys))
        # ... yet |sum_A S_A|^2 CHANGES: positive diagonal cannot determine the gate
        self.assertNotEqual(sp.ones_contraction(cells), sp.ones_contraction(rot))

    def test_exact_345_witness(self):
        # identical diagonal 50, |S|^2 ranges 16..144 under an exact half-turn rotation
        hte = MSC.half_turn_evaluation
        cA, cB, cC = PP.monomial(0, 3), PP.monomial(0, 4), PP.monomial(0, 5)
        half = PP.monomial(Q(1, 2))
        diag = cA * cA.star() + cB * cB.star() + cC * cC.star()
        aligned = (cA + cB + cC)
        anti = (cA + half * cB + cC)
        self.assertEqual(hte(diag), 50)
        self.assertEqual(hte(aligned * aligned.star()), 144)
        self.assertEqual(hte(anti * anti.star()), 16)

    def test_occupancy_baseline_phase_blind_not_gate(self):
        for (N, H, h) in [(8, 3, 1), (20, 4, 1), (40, 5, 3)]:
            auth = sp.authentic_states(N)
            seed = tuple(MSC.coherent_seed_control(N, start=max(1, N // 4))["states"])
            cf = tuple(MSC.counterfeit_states(N))
            base = Q(H - 1, N)
            # occupancy baseline is EXACTLY (H-1)/N and identical across all three orbits
            self.assertEqual(sp.occupancy_baseline(auth, H, h), base)
            self.assertEqual(sp.occupancy_baseline(seed, H, h), base)
            self.assertEqual(sp.occupancy_baseline(cf, H, h), base)
            # the REAL (evaluated) gate separates authentic from counterfeit (OBSERVED)
            g_auth = sp.weyl_gate_value(auth, H, h)
            g_seed = sp.weyl_gate_value(seed, H, h)
            g_cf = sp.weyl_gate_value(cf, H, h)
            self.assertLess(g_auth, 1.0)      # authentic ~0.15-0.20
            self.assertGreater(g_seed, 1.0)   # counterfeits sit near the trivial max H-1
            self.assertGreater(g_cf, 1.0)

    def test_firewall_flags(self):
        self.assertFalse(sp.signed_saving_proved)
        self.assertFalse(sp.pi_normality_proved)
        self.assertFalse(sp.occupancy_baseline_is_the_gate)
        self.assertFalse(sp.introduces_new_theorem)


if __name__ == "__main__":
    unittest.main()
