"""Cross-front contracts: compare independent source and observer implementations."""
from dataclasses import replace
from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import sys
import unittest

from observational_succ.duck_bbp import forcing
from observational_succ import zero_anchored_lambda as compiler
from observational_succ.zero_anchored_haar import grid_haar_defect, signed_block_overlap


def research_module(name, relative):
    path = Path(__file__).resolve().parents[1] / "research/2026-11-10" / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


z = research_module("_xxiv_zero_anchor", "circle_line_lr_observer/zero_anchor_identity/zero_anchor.py")
fiber = research_module("_xxiv_fiber", "basel_crt_omega_phasebridge/ratio_fiber_joinings/certified_fiber.py")
shield = research_module("_xxiv_shield", "circle_line_lr_observer/height_shield/farey_height_shield.py")


class CrossFrontContracts(unittest.TestCase):
    def test_all_source_clocks_match_frozen_contract(self):
        # These implementations all use the one-indexed recurrence clock.
        for n in (*range(1, 65), 257, 1021, 4099):
            expected = forcing(n)
            self.assertEqual(z.r(n), expected)
            self.assertEqual(fiber.bbp_r(n), expected)
            self.assertEqual(shield.four_pole(n), expected)

    def test_rational_seed_passports_agree_and_alias_is_rejected(self):
        for seed in (Q(), Q(1,16), Q(-3,7)):
            for n in (0, 1, 3, 11):
                symbolic = z.state(n, z.AffineX(seed, Q()))
                state = compiler.SourceState(n, symbolic.const, seed)
                receipt = compiler.certify_state(state, require_zero=False)
                self.assertEqual(receipt.prefix_seed, z.recovered_seed(n, symbolic).const)
                if seed:
                    with self.assertRaises(compiler.CompilerError):
                        compiler.certify_state(state)
                else:
                    self.assertTrue(receipt.original_zero)
                with self.assertRaises(compiler.CompilerError):
                    compiler.certify_state(replace(state, value=state.value+Q(1,16)), require_zero=False)
        # An irrational symbolic seed remains outside the rational compiler API.
        with self.assertRaises((TypeError, ValueError)):
            compiler.SourceState(0, z.COHERENT_WRONG, Q())

    def test_signed_cdf_backends_match_on_same_chart_rational_points(self):
        for early, late, denominator in [((0,0),(0,0),16), ((0,0),(15,15),16),
                                         ((1,7,13),(2,8,14),32)]:
            result = signed_block_overlap(early, late, denominator)
            a = tuple(Q(x, denominator) for x in early)
            b = tuple(Q(x, denominator) for x in late)
            self.assertEqual(result.early, z.haar_defect(a))
            self.assertEqual(result.late, z.haar_defect(b))
            self.assertEqual(result.combined, z.haar_defect(a+b))
            self.assertEqual(result.overlap, (z.haar_defect(a)+z.haar_defect(b))/2-z.haar_defect(a+b))
            self.assertEqual(grid_haar_defect(early+late, denominator), result.combined)

    def test_two_source_farey_paths_and_bounded_denominator_margin(self):
        a = shield.certify_height(1000, "circle_beta")
        b = shield.certify_height(1000, "bbp_four_pole")
        self.assertTrue(shield.verify_height_certificate(a))
        self.assertTrue(shield.verify_height_certificate(b))
        self.assertEqual(a.final, b.final)
        self.assertEqual(a.steps, b.steps)
        for cert in (a, b):
            # Direct rational probes are separate from the Farey-neighbor argument.
            for denominator in range(1, 41):
                for numerator in range(3*denominator, 4*denominator+1):
                    q = Q(numerator, denominator)
                    distance = max(cert.final_source_lo-q, q-cert.final_source_hi)
                    self.assertGreater(distance, cert.uniform_margin)


if __name__ == "__main__":
    unittest.main()
