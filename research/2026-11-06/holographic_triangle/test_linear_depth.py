"""Tests frozen in PRE-registered source-window conjecture before new run."""
import unittest
from fractions import Fraction
from math import prod
from hologram import state, forcing
from linear_depth_probe import split_strip, audit

class OriginalPoleStripTests(unittest.TestCase):
    def test_all_six_preregistered_windows(self):
        for n in (8,16,32,64,128,257):
            r=audit(n)
            self.assertGreater(r['gaussian_split_product_bits'],0)
            self.assertGreaterEqual(r['original_denominator_bits'],r['gaussian_split_product_bits'])

    def test_split_and_inert_are_exact(self):
        for n in (8,16,32,64,128,257):
            split,inert=split_strip(n)
            u=state(n)
            for p in split:
                self.assertEqual(u.denominator%p,0)
                self.assertNotEqual(u.denominator%(p*p),0)
            for p in inert:
                self.assertNotEqual(u.denominator%p,0)

    def test_pole_birth_under_factor_removal(self):
        for n in (8,16,32,64):
            um=Fraction()
            for j in range(1,n+1):um=16*um+forcing(j,(0,-2,-1,-1))
            split,_=split_strip(n)
            for p in split:
                self.assertEqual(um.denominator%p==0,p%8==5)

    def test_divisor_census_contrast_with_original(self):
        n=32
        d=state(n).denominator
        split,inert=split_strip(n)
        self.assertEqual(d%prod(split),0)
        self.assertTrue(all(d%p for p in inert))

if __name__=='__main__':unittest.main()
