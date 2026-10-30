"""Finite-capacity vs unbounded-contact witnesses for SUCC research.

Finite combinatorial controls only; no randomness or pi normality claimed.
"""
from fractions import Fraction
from itertools import product
from math import comb
import unittest


def min_side_bits(n, grade, internal_bits):
    """Minimum worst-case side bits to reconstruct any observed 2n-word with grade s.

    Grade s is given to the decoder without charge. A valid encoder must
    distinguish comb(2n,s) histories by (internal register, external record).
    """
    total = comb(2*n, grade)
    return max(0, (total - 1).bit_length() - internal_bits)


def possible_transcripts(carrier_sites, schedule):
    """Count distinct observed strings for a *fixed*, deterministic path."""
    return len({tuple(world[i] for i in schedule)
                for world in product((0, 1), repeat=carrier_sites)})


def radix_digits(x, base, length):
    out = []
    for _ in range(length):
        bx = base*x
        digit = bx.numerator // bx.denominator
        out.append(digit)
        x = bx - digit
    return tuple(out)


class InertialContactTests(unittest.TestCase):
    def test_exact_s_one_memory_horizon(self):
        for k in range(2, 8):
            n = 2**(k-1)
            self.assertEqual(min_side_bits(n, 1, k), 0)
            self.assertEqual(min_side_bits(n+1, 1, k), 1)

    def test_grade_zero_has_no_chronology_overhead(self):
        for n in (1, 4, 16, 128):
            self.assertEqual(min_side_bits(n, 0, 0), 0)
            self.assertEqual(min_side_bits(n, 2*n, 0), 0)

    def test_exact_external_record_repairs_collision(self):
        n, k = 32, 4
        histories = list(range(2*n))  # position of the sole 1
        self.assertEqual(min_side_bits(n, 1, k), 2)
        internal = [h % (2**k) for h in histories]
        self.assertLess(len(set(internal)), len(histories))
        joint = [(h % (2**k), h // (2**k)) for h in histories]
        self.assertEqual(len(set(joint)), len(histories))

    def test_static_and_active_frozen_carrier(self):
        T = 6
        self.assertEqual(possible_transcripts(T, [0]*T), 2)
        self.assertEqual(possible_transcripts(T, list(range(T))), 2**T)
        self.assertEqual(possible_transcripts(T, [0,1]*3), 2**2)

    def test_rest_can_receive_dynamic_information(self):
        # A stationary probe of a time-varying field sees fresh data; its
        # address is fixed, but the time index changes the local carrier.
        T = 6
        self.assertEqual(possible_transcripts(T, list(range(T))), 2**T)

    def test_radix_observer_cannot_extrapolate_finite_prefix(self):
        base = 16
        prefix = (3,1,4)
        future = set()
        for d in range(base):
            digits = prefix + (d,0)
            num = sum(v*base**(len(digits)-i-1) for i,v in enumerate(digits))
            x = Fraction(num,base**len(digits))
            observed = radix_digits(x,base,4)
            self.assertEqual(observed[:3],prefix)
            future.add(observed[3])
        self.assertEqual(future,set(range(base)))

    def test_no_bounded_state_can_encode_all_independent_histories(self):
        k = 3
        for m in range(1,8):
            # b=2, m distinct bits: 2^m histories. Outside side channel,
            # no-loss injectivity requires at least m register bits.
            self.assertEqual(2**m <= 2**k,m <= k)


if __name__ == '__main__':
    unittest.main(verbosity=2)
