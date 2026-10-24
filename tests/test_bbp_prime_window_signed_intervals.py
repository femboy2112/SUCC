"""Certified rational complex phase enclosures of authentic BBP mixed modes.

These are finite-source proofs, not floating-point pi fits or infinite
normality claims. Both an independent Machin alternating interval and a
Taylor remainder are charged before claiming a strict inequality.
"""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_prime_window_projection import (
    additive_clock_partition, source_complement_window,
)
from observational_succ.bbp_prime_window_signed_intervals import (
    machin_pi_interval, box_phase, signed_prime_window_boxes,
    box_modulus_squared_interval,
)


class CertifiedSignedInterference(unittest.TestCase):
    def test_pi_interval_and_periodic_phase_controls(self):
        pl,pu=machin_pi_interval(24)
        self.assertLess(Q(314159,100000),pl)
        self.assertGreater(Q(314160,100000),pu)
        self.assertLess(pu-pl,Q(1,10**27))
        for rational in (Q(),Q(1,7),Q(1,3),Q(1,2),Q(65,17)):
            rect=box_phase(rational,14,24)
            self.assertLessEqual(rect[0],rect[1])
            self.assertLessEqual(rect[2],rect[3])
            actual=cmath.exp(2j*math.pi*float(rational%1))
            self.assertLess(float(rect[0])-1e-12,actual.real)
            self.assertGreater(float(rect[1])+1e-12,actual.real)
            self.assertLess(float(rect[2])-1e-12,actual.imag)
            self.assertGreater(float(rect[3])+1e-12,actual.imag)
        with self.assertRaises(ValueError):
            machin_pi_interval(True)
        with self.assertRaises(ValueError):
            box_phase(Q(1,3),0)

    def test_true_BBP_signed_high_mode_nonzero_finite(self):
        for p,d,full_threshold,j_threshold in (
            (17,1,Q(1,9),Q(1,16)),
            (41,3,Q(1,50),Q(1,100)),
        ):
            out=signed_prime_window_boxes(p,d,1,14,24)
            self.assertGreater(out["full_sq"][0],full_threshold)
            self.assertGreater(out["high_sq"][0],j_threshold)
            self.assertLess(out["low_sq"][1],Q(1,100))
            self.assertLessEqual(out["high_sq"][0],out["high_sq"][1])
            self.assertGreater(out["high_sq"][0],0)
            self.assertEqual(out["full_sq"],
                             box_modulus_squared_interval(out["full"]))
            self.assertEqual(out["low_sq"],
                             box_modulus_squared_interval(out["low"]))
            self.assertEqual(out["high_sq"],
                             box_modulus_squared_interval(out["high"]))

    def test_full_signed_phase_and_projection_independent_numeric_sanity(self):
        for p,d in ((17,1),(41,3)):
            N=additive_clock_partition(p,d)["delta"]
            K=N//d
            w=source_complement_window(p)
            u=[cmath.exp(2j*math.pi*float(Q(4*pow(16,t,p),p)%1))
               for t in range(N)]
            v=[cmath.exp(2j*math.pi*float(w[t]%1)) for t in range(N)]
            normalized=sum(a*b for a,b in zip(u,v))/N
            low=sum(
                (sum(u[r+d*j] for j in range(K))/K)
                *(sum(v[r+d*j] for j in range(K))/K)
                for r in range(d))/d
            high=normalized-low
            boxes=signed_prime_window_boxes(p,d,1,14,24)
            for name,z in (("full",normalized),("low",low),("high",high)):
                rect=boxes[name]
                self.assertLessEqual(float(rect[0])-1e-11,z.real)
                self.assertGreaterEqual(float(rect[1])+1e-11,z.real)
                self.assertLessEqual(float(rect[2])-1e-11,z.imag)
                self.assertGreaterEqual(float(rect[3])+1e-11,z.imag)

    def test_valid_input_and_interval_cost_caps(self):
        with self.assertRaises(ValueError):
            signed_prime_window_boxes(17,4)
        with self.assertRaises(ValueError):
            signed_prime_window_boxes(41,1,1,0,24)
        with self.assertRaises(ValueError):
            signed_prime_window_boxes(257,1)
        with self.assertRaises(ValueError):
            signed_prime_window_boxes(True,1)


if __name__ == "__main__":
    unittest.main()
