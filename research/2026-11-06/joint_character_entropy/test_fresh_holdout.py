"""Commit-first 2026-11-06 additive prereg holdout: exact rational controls."""
from __future__ import annotations
import json
import unittest
from fractions import Fraction
from pathlib import Path
from fresh_holdout_probe import main, ADDENDUM_SHA256, GITHUB_COMMIT

class FreshSourceCharacterHoldout(unittest.TestCase):
    def test_fresh_commit_first_original_character_and_controls(self):
        d=main()
        recorded=json.loads(Path(__file__).with_name('FRESH_HOLDOUT_RAW.json').read_text())
        self.assertEqual(d,recorded)
        self.assertEqual(d['prereg_sha256'],ADDENDUM_SHA256)
        self.assertEqual(d['prereg_commit'],GITHUB_COMMIT)
        self.assertEqual([(x['A'],x['h']) for x in d['fresh_epochs_h_3']], [(239,3),(503,3)])
        for row in d['fresh_epochs_h_3']:
            self.assertGreater(Fraction(row['rigorous_lower_floor_12dp']),0)
            self.assertLess(Fraction(row['rigorous_upper_ceil_12dp']),1)
        self.assertLess(Fraction(d['rootgrid_h_3']['rigorous_upper_ceil_12dp']),Fraction(1,10**6))
        self.assertGreater(Fraction(d['periodic_beta_1_5_h_3']['rigorous_lower_floor_12dp']),Fraction(99,100))
