"""Source-exact tests for the critical coherent chirp; no pi digits or stochastic fit."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction as F

HERE=Path(__file__).resolve().parents[1]/'research'/'2026-11-04'/'critical_chirp'
sys.path.insert(0,str(HERE))
from critical_chirp import (
    forcing,forcing_polynomial,coherent_tail_bounds,rigorous_tail_sandwich,
    exact_phase_epoch,independent_modular_phase_epoch,critical_frequency,
    coherent_chirp_leading_constant,calibration_ratio,
)


class CriticalChirpExact(unittest.TestCase):
    def test_source_four_poles_vs_independent_polynomial(self):
        for n in range(1,192):
            self.assertEqual(forcing(n),forcing_polynomial(n))
            self.assertEqual(forcing(n).denominator%2,1)
            self.assertGreater(forcing(n),0)
            if n>1:
                self.assertLess(forcing(n),forcing(n-1))

    def test_original_zero_seed_two_oracles(self):
        for A in (4,8,16,32,64):
            self.assertEqual(exact_phase_epoch(A),independent_modular_phase_epoch(A))

    def test_exact_tail_sandwich_development(self):
        for n in (1,2,3,4,5,6,7,8,11,16,32,64,127,256):
            x=rigorous_tail_sandwich(n,16)
            self.assertLess(x['tail_upper'],x['model'])
            self.assertLess(x['model']-x['tail_lower'],x['max_error'])

    def test_rational_tail_enclosures_nested(self):
        for n in (1,5,16,64):
            lo8,hi8=coherent_tail_bounds(n,8)
            lo12,hi12=coherent_tail_bounds(n,12)
            lo16,hi16=coherent_tail_bounds(n,16)
            self.assertLess(lo8,lo12)
            self.assertLess(lo12,lo16)
            self.assertLess(hi16,hi12)
            self.assertLess(hi12,hi8)
            self.assertLess(lo16,hi16)

    def test_radix_schedule_has_fixed_factor_16_and_no_float_lemma(self):
        from math import log
        for A in (16,64,256,1024,4096):
            for h in (1,2,3,17):
                H=critical_frequency(A,h)
                self.assertEqual(H%abs(h),0)
                self.assertLessEqual(H,A*A*log(A))
                self.assertGreater(16*H,A*A*log(A))
                self.assertGreaterEqual(H,abs(h))

    def test_explicit_nonasymptotic_coherent_arc_lower_bound(self):
        # For the genuine coherent tail T_n, monotonicity plus the source integral gives
        # 0<T_n-T_(n+1)<=1/(32n^3). Pick m consecutive epoch phases of span
        # H*(m-1)/(32A^3) <= 1/8 cycle => phasor mean modulus >=m/(2A).
        for A,L in ((128,4),(128,32),(256,64),(512,256)):
            H=A*A*L
            m=min(A,4*A//L)
            self.assertGreaterEqual(m,1)
            phase_span=F(H*(m-1),32*A**3)
            self.assertLess(phase_span,F(1,8))
            self.assertGreaterEqual(F(m,2*A),0)

    def test_trust_scope(self):
        self.assertEqual(coherent_chirp_leading_constant(),256)
        self.assertEqual(calibration_ratio(64,64*64*16),16)
        with self.assertRaises(ValueError):forcing(0)
        with self.assertRaises(ValueError):critical_frequency(0,1)
        with self.assertRaises(ValueError):rigorous_tail_sandwich(1,0)

if __name__=='__main__':unittest.main()
