"""Exact finite tests of the scoped SUCC–Scott–Omega source weld."""
import unittest
from fractions import Fraction as Q
from math import floor
from pathlib import Path
import importlib.util

# Test also works directly from repository root under unittest discovery.
MODULE = Path(__file__).resolve().parents[0] / 'scott_omega_source_weld.py'
if not MODULE.exists():
    MODULE = Path(__file__).resolve().parents[1] / 'observational_succ' / 'scott_omega_source_weld.py'
spec = importlib.util.spec_from_file_location('scott_omega_source_weld', MODULE)
import sys
weld = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = weld
spec.loader.exec_module(weld)


class SourceWeldTests(unittest.TestCase):
    def test_known_source(self):
        self.assertEqual(weld.bbp_forcing(1), Q(47,15))
        self.assertEqual(weld.selected_state(0), 0)
        for j in range(1,40):
            self.assertEqual(weld.selected_state(j),16*weld.selected_state(j-1)+weld.bbp_forcing(j))
            self.assertGreater(weld.bbp_forcing(j),0)
            self.assertLess(weld.bbp_forcing(j),Q(4,j*j))

    def test_naturality_of_finite_source_square(self):
        for L in [2,3,7,13,23]:
            p = weld.prefix_pi_over_16(L)
            for n in range(L+1):
                self.assertEqual(weld.selected_state(n)+weld.finite_green_tail(n,L),16**n*p)
                self.assertEqual(weld.completed_interval(n,L),weld.completed_interval(0,L).scaled(16**n))

    def test_nested_rational_information(self):
        for n in range(12):
            for L in range(max(1,n),20):
                a=weld.completed_interval(n,L)
                b=weld.completed_interval(n,L+1)
                self.assertTrue(b.below(a), (n,L))
                self.assertGreater(a.width,0)
                self.assertLess(b.width,a.width)

    def test_circle_phase_and_lift_not_identical(self):
        for n in range(1,25):
            a,b=weld.seam_pair(n)
            self.assertNotEqual(weld.circle_arcs(a),weld.circle_arcs(b))
            self.assertEqual(weld.circular_point_distance(a.lo,b.lo),Q(1,16**n))
            self.assertEqual(weld.circle_arcs(weld.RationalInterval(1,1)),((Q(0),Q(0)),))
            self.assertEqual(weld.circle_arcs(weld.RationalInterval(0,0)),((Q(0),Q(0)),))

    def test_source_alias(self):
        for n in range(1,12):
            original=weld.selected_state(n)
            wrong=original + Q(16**(n-1))
            self.assertEqual(weld.circular_point_distance(original,wrong),0)
        self.assertNotEqual(Q(0),Q(1,16))

    def test_omega_growth_is_syntax_not_geometry(self):
        for k in range(2,9):
            trace=weld.trace_omega_k(k,20)
            self.assertEqual(trace[0],2)
            self.assertEqual({v-u for u,v in zip(trace,trace[1:])},{k-2})

    def test_circle_arcs_seams(self):
        self.assertEqual(weld.circle_arcs(weld.RationalInterval(Q(15,16),Q(17,16))),
                         ((Q(0),Q(1,16)),(Q(15,16),Q(1))))
        self.assertEqual(weld.circle_arcs(weld.RationalInterval(0,2)),((Q(0),Q(1)),))
        self.assertEqual(weld.circle_arcs(weld.RationalInterval(Q(1,3),Q(1,2))),((Q(1,3),Q(1,2)),))

    def test_finite_digit_certificate(self):
        # Certified entirely from four-pole rational source and strict error bound.
        observed = []
        for n in range(10):
            dig = None
            for horizon in range(max(1,n),n+32):
                dig=weld.digit_if_certified(n,horizon)
                if dig is not None:break
            self.assertIsNotNone(dig,n)
            observed.append(dig)
        self.assertEqual(observed[:6],[3,2,4,3,15,6]) # 3.243F6... base 16

    def test_weyl_transport_is_only_precision(self):
        for h in [-13,-1,0,1,7]:
            for n in [0,1,3,9]:
                B=weld.source_weyl_error_over_pi_bound(h,n,max(1,n+4))
                self.assertGreaterEqual(B,0)
                if h==0:self.assertEqual(B,0)
                else:self.assertGreater(B,0)

    def test_validation(self):
        for invalid in (-2,-1,1.2):
            with self.assertRaises(ValueError): weld.bbp_forcing(invalid)
        with self.assertRaises(ValueError):weld.completed_interval(3,2)
        with self.assertRaises(ValueError):weld.trace_omega_k(1,3)
        with self.assertRaises(ValueError):weld.RationalInterval(1,0)


if __name__=='__main__': unittest.main()