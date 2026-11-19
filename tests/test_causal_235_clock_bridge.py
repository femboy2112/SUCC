"""Independent finite checks of the original-source/forward-clock observer."""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import comb, factorial, gcd
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/2026-11-18/causal_235_local_dynamics/clock_bridge.py"
SPEC = spec_from_file_location("causal235_clock_bridge", PATH)
bridge = module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


def literal_r(n):
    return sum((Fraction(w,8*n-c) for w,c in ((4,7),(-2,4),(-1,3),(-1,2))), Fraction(0))


class TestCausal235ClockBridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states = [Fraction(0)]
        for n in range(1,513):
            cls.states.append(16*cls.states[-1]+literal_r(n))

    def test_authentic_labels_against_literal_forward_states(self):
        for n, state in enumerate(self.states):
            for a,b in ((1,1),(3,2),(4,2),(7,4),(9,5)):
                label2 = state.numerator*pow(state.denominator,-1,2**a) % 2**a
                label3 = (120*n*n-89*n+16) % 3**b
                self.assertEqual(bridge.source_labels(n,a,b),(label2,label3))
        self.assertEqual(bridge.source_states(64),self.states[:65])

    def test_complete_clock_map_and_forward_wraparound(self):
        for a,b in ((1,1),(4,2),(5,3)):
            modulus = 2**a*3**b
            reports = set()
            for n in range(modulus+1):
                labels = bridge.source_labels(n,a,b)
                self.assertEqual(bridge.clock_from_bbp_labels(*labels,a,b),n%modulus)
                observed = bridge.observer_from_bbp_labels(*labels,a,b)
                f,g = bridge.fibonacci_pair(2*n)
                self.assertEqual(observed,(bridge.quartic(g,f,2**a),bridge.quartic(g,f,3**b)))
                if n < modulus:
                    reports.add(labels)
                next_reports = bridge.observer_from_bbp_labels(*bridge.source_labels(n+1,a,b),a,b)
                for old,new,mod in zip(observed,next_reports,(2**a,3**b)):
                    step = tuple(sum(x*y for x,y in zip(row,old))%mod for row in bridge.T)
                    self.assertEqual(step,new)
            self.assertEqual(len(reports),modulus)

    def test_resolution_compatibility_and_forgotten_clock_mutant(self):
        for n in (0,1,2,5,17,71,137,211,507):
            fine = bridge.observer_from_bbp_labels(*bridge.source_labels(n,9,5),9,5)
            coarse = bridge.observer_from_bbp_labels(*bridge.source_labels(n,4,2),4,2)
            self.assertEqual(tuple(x%16 for x in fine[0]),coarse[0])
            self.assertEqual(tuple(x%9 for x in fine[1]),coarse[1])
        # Both individual phase values exist, but this pair has no shared clock.
        self.assertFalse(bridge.local_pair_compatibility(0,1,4,2))
        self.assertNotEqual(bridge.predicted_quartic(1,9),bridge.predicted_quartic(2,9))

    def test_compatible_phase_pairs_have_exact_shared_clock_count(self):
        for a,b in ((1,1),(4,2),(5,3),(7,4)):
            p2,p3,joint = bridge.periods(a,b)
            actual = {(n%p2,n%p3) for n in range(joint)}
            compatible = {(u,v) for u,v in product(range(p2),range(p3))
                          if bridge.local_pair_compatibility(u,v,a,b)}
            self.assertEqual(actual,compatible)
            self.assertEqual(len(actual),joint)
            if a>=4 and b>=2:
                self.assertEqual(6*len(actual),p2*p3)

    def test_delayed_null_against_independent_partial_fraction_product(self):
        history = [None]+[literal_r(n) for n in range(1,180)]
        for n,k,d in product((1,3,11),(0,1,2,4),(1,2,6,7)):
            now=n+k*d
            expected=Fraction(0)
            for w,c in ((4,7),(-2,4),(-1,3),(-1,2)):
                denominator=1
                for j in range(k+1):
                    denominator*=8*(n+j*d)-c
                expected+=Fraction(w*factorial(k)*(8*d)**k,denominator)
            self.assertEqual(bridge.delayed_null(history[:now+1],now,k,d),expected)
            self.assertGreater(expected,0)
            if k:
                with self.assertRaises(ValueError):
                    bridge.delayed_null(history[:now],now,k,d)
        with self.assertRaises(ValueError):
            bridge.delayed_null(history,2,2,1)

    def test_rational_phase_bounds_cross_wraps_and_detect_lock(self):
        for state,allowance in ((Fraction(999,1000),Fraction(1,100)),
                                (Fraction(-1,1000),Fraction(1,100)),
                                (Fraction(1,2),Fraction(1,20)),
                                (Fraction(0),Fraction(1,1000))):
            lo,hi=bridge.phase_distance_squared_bounds(state,allowance)
            for j in range(41):
                x=state+allowance*j/40
                frac=x-x.numerator//x.denominator
                exact=min(frac,1-frac)**2
                self.assertLessEqual(lo,exact)
                self.assertGreaterEqual(hi,exact)
        self.assertEqual(bridge.phase_distance_squared_bounds(0,0),(0,0))
        with self.assertRaises(ValueError):
            bridge.phase_distance_squared_bounds(0,-1)

    def test_finite_source_energy_intervals_are_nonvacuous(self):
        # Existing source range: calibration only, expressly not a fresh holdout.
        for B in (16,32,64,128,256):
            lo,hi=bridge.source_shell_certificate(self.states,B)
            self.assertGreater(lo,0)
            self.assertLess(hi,Fraction(1,4))
            sample=Fraction(0)
            for n in range(B,2*B):
                partial_tail=sum((literal_r(n+j)/16**j for j in range(1,17)),Fraction(0))
                y=self.states[n]+partial_tail
                frac=y-y.numerator//y.denominator
                sample+=min(frac,1-frac)**2
            self.assertLessEqual(lo,sample/B)
            self.assertGreaterEqual(hi,sample/B)

    def test_invalid_local_domains_rejected(self):
        for a,b in ((0,1),(1,0),(33,1),(1,16),(True,2)):
            with self.assertRaises(ValueError):
                bridge.clock_from_bbp_labels(0,0,a,b)
        with self.assertRaises(ValueError):
            bridge.power(-1,2)
        with self.assertRaises(ValueError):
            bridge.clock_from_bbp_labels(16,0,4,2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
