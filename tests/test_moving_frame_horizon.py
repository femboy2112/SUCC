"""Exact finite controls for BBP moving-frame and observer horizon.

Only the authentic four-pole zero-seeded rational source is used for numerical
BBP certificates. Haar entropy is a separate artificial prior on all digits.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import unittest


def r(n):
    if n < 1:
        raise ValueError('n >= 1')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


@lru_cache(maxsize=2)
def states(end):
    u = F(0)
    d = {}
    for n in range(1, end+1):
        u = 16*u + r(n)
        d[n] = (u, r(n+1)/15)
    return d


def circle_d(q):
    frac = F(q) % 1
    return min(frac, 1-frac)


def step_lower(n, data):
    u, beta = data[n]
    return max(F(0), circle_d(15*u)-15*beta)


def certified_speed(B, data):
    return F(16, B) * sum((step_lower(n,data)**2 for n in range(B, 2*B)),F(0))


def anchor_lower(B,data):
    return F(8, B) * sum((max(F(0),circle_d(data[n][0])-data[n][1])**2
                             for n in range(B, 2*B)), F(0))


def shift_digits(digits,n,k):
    return tuple(digits[n:n+k])


def unknown_future_digits(m,n,k):
    return min(k,max(0,n+k-m))


class MovingFrameHorizonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=states(512)

    def test_exact_zero_seed_and_direct_prefix(self):
        self.assertEqual(self.data[1][0],r(1))
        for n in (1,2,5,32,64,257,512):
            prefix=sum((r(j)/16**j for j in range(1,n+1)), F(0))
            self.assertEqual(self.data[n][0],16**n * prefix)
            self.assertGreater(r(n),0)

    def test_strict_positive_finite_tail_envelope(self):
        for n in (1,2,5,32,64,128,256,512):
            beta = self.data[n][1]
            self.assertEqual(beta,r(n+1)/15)
            self.assertGreater(beta,0)
            self.assertLess(beta,F(1,30))
            self.assertLess(beta,F(1,n*n*3))

    def test_exact_moving_chart_commutes_with_source(self):
        # Work additively in R/Z, avoiding numerical complex phases.
        for n in (1,2,10,32,64):
            un=self.data[n][0]
            rn1=r(n+1)
            un1=16*un+rn1
            self.assertEqual(self.data[n+1][0],un1)
            for z in (F(0),F(1,7),F(1,3),F(4,5),F(10,3)):
                lhs=(16*z-un1)%1
                rhs=(-rn1+16*(z-un))%1
                self.assertEqual(lhs,rhs)

    def test_phase_relative_motion_exact_and_not_same_as_tail(self):
        for n in (1,2,16,64,256):
            un=self.data[n][0]
            self.assertEqual((self.data[n+1][0]-self.data[n][0]),
                             15*un+r(n+1))
            self.assertGreaterEqual(step_lower(n,self.data),0)
            self.assertLessEqual(step_lower(n,self.data),F(1,2))

    def test_finite_source_speed_certificates(self):
        for B in (16,32,64,128,256):
            s=certified_speed(B,self.data)
            self.assertGreater(s,F(1))
            if B>=32:
                self.assertGreater(s,F(6,5))
            self.assertLess(s,F(4))

    def test_finite_R0_margin_from_speed(self):
        for B in (32,64,128,256):
            s=certified_speed(B,self.data)
            eta=s/8-F(1,B)
            self.assertGreater(eta,F(1,10))
            self.assertLess(eta,F(2))
            # This is a conditional lower bound on 1-Re W_B for those
            # *finite* shells, not a bound valid at all later B.

    def test_independent_anchor_rational_certificate(self):
        for B in (16,32,64,128,256):
            a=anchor_lower(B,self.data)
            self.assertGreater(a,F(0))
            self.assertLess(a,F(2))

    def test_correct_temporal_error_does_not_replace_signed_budget(self):
        for n in (1,2,16,128):
            # For coherent counterseed s=-x the true rational-state part
            # would be -T_n, with 0<T_n<beta_n, hence its step bound is 0.
            beta=self.data[n][1]
            fake_t=beta/2 # just an admissible interval point, not true T_n
            self.assertEqual(max(F(0),circle_d(-15*fake_t)-15*beta),0)
        # Locked example: x=1 yields z_n=1, zero absolute and relative motion.
        self.assertEqual((15*16**100*F(1))%1,0)
        # Different fixed but nonunit phase: x=1/15, has R0 but speed zero.
        for n in (1,2,8):
            self.assertEqual((15*16**n*F(1,15))%1,0)
            self.assertEqual((16**n*F(1,15))%1,F(1,15))

    def test_horizon_digit_knowledge_minimal(self):
        # A prefix of length m can determine future k digits iff m >= n+k,
        # over the unrestricted 16-symbol full-shift source class.
        for m in range(1,5):
            for n in range(0,4):
                for k in range(1,4):
                    unknown=unknown_future_digits(m,n,k)
                    self.assertEqual(unknown, min(k, max(0,n+k-m)))
                    if m >= n+k:
                        self.assertEqual(unknown,0)
                    if n >= m:
                        self.assertEqual(unknown,k)

    def test_Haar_entropy_is_prior_relative_not_BBP(self):
        # Enumerate independent uniform base16 digits, fixing m-prefix.
        # Count distinct possible k-digit outcomes, not pi-digit entropy.
        for m,n,k in ((1,0,2),(2,1,2),(2,2,2),(4,2,2),(4,3,2)):
            L=max(m,n+k)
            suffix_len=L-m
            self.assertLessEqual(suffix_len,3)
            possible=set()
            prefix=(7,)*m
            for suffix in product(range(16),repeat=suffix_len):
                digits=prefix+suffix
                possible.add(shift_digits(digits,n,k))
            unknown=unknown_future_digits(m,n,k)
            self.assertEqual(len(possible), 16**unknown)
            # With equal-weight Haar branches, Shannon entropy (bits)
            # is exactly log2(count)=4 * unknown, not k_B*T or joules.
            self.assertEqual(4*unknown, (len(possible).bit_length()-1))

    def test_horizon_nonnecessity_controls(self):
        # The full state is fixed if the source is *known* (e.g. BBP), so
        # the Haar full-shift cylinder growth is not source identification.
        # An observer with enough prefix digits for a single target can
        # know it exactly, contradicting an unrestricted impossibility.
        self.assertEqual(unknown_future_digits(20,5,4),0)
        self.assertEqual(unknown_future_digits(3,25,2),2)


if __name__ == '__main__':
    unittest.main()
