"""Exact controls for the superexponentially matched, radix-locked source.

This constructs a changed rational-valued sequence, NEVER the original BBP
source. No float or pi oracle is used. It is a countermodel, not a normality
proof. All source values and comparison certificates are Fractions.
"""

from fractions import Fraction as Q
from functools import lru_cache
import json
import unittest


@lru_cache(None)
def r(n):
    assert n >= 1
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def gap(n):
    return r(n) - r(n+1)


def eps(n):
    assert n >= 0
    return gap(n+1) / (1024 * 16**((n+1)**2))


def ceilq(x):
    return -((-x.numerator)//x.denominator)


def tail_partial(n, length):
    result = Q(0)
    for j in range(length, 0, -1):
        result = (result + r(n+j))/16
    return result


def trunc_error_bound(n, length):
    return r(n+length+1)/(15*16**length)


class FlatLock:
    def __init__(self, prefix):
        assert prefix >= 0
        self.prefix = prefix
        self.cutoff = prefix
        while 16**prefix * trunc_error_bound(0, self.cutoff) >= eps(prefix)/4:
            self.cutoff += 1
        self.depth = prefix
        while Q(16**prefix, 16**self.depth) >= eps(prefix)/4:
            self.depth += 1
        self.source_prefix = tail_partial(0, prefix)
        upper_grid = ceilq(16**self.depth * tail_partial(0, self.cutoff))
        self.endpoint = Q(upper_grid, 16**self.depth)
        self.lengths = {}

    @lru_cache(None)
    def g(self, n):
        assert n >= self.prefix
        if n == self.prefix:
            return 16**n * (self.endpoint - self.source_prefix)
        length = max(1, (n+1)**2)
        while trunc_error_bound(n, length) >= eps(n):
            length += 1
        self.lengths[n] = length
        return tail_partial(n, length)

    def forcing(self, n):
        if n <= self.prefix:
            return r(n)
        return 16*self.g(n-1)-self.g(n)

    def perturbation(self, n):
        return self.forcing(n)-r(n)

    def endpoint_tail_bound(self, n):
        assert n > self.prefix
        self.g(n)
        return trunc_error_bound(n, self.lengths[n])


class Tests(unittest.TestCase):
    def test_source_gap_calibration(self):
        for n in range(1, 200):
            self.assertGreater(r(n), 0)
            self.assertGreater(gap(n), gap(n+1))
            self.assertLess(eps(n), r(n+1)/1024)

    def test_exact_finite_prefix_and_radix_endpoint(self):
        for m in (0, 1, 3, 7):
            f = FlatLock(m)
            self.assertEqual((16**f.depth*f.endpoint).denominator, 1)
            for n in range(1, m+1):
                self.assertEqual(f.forcing(n), r(n))
            self.assertGreater(f.g(m), 0)
            self.assertEqual(16**m*f.endpoint-f.g(m), 16**m*f.source_prefix)
            self.assertLess(16**m*trunc_error_bound(0, f.cutoff), eps(m)/4)
            self.assertLess(Q(16**m, 16**f.depth), eps(m)/4)

    def test_superexponential_bound_and_monotonicity(self):
        for m in (0, 1, 3, 7):
            f = FlatLock(m)
            for n in range(max(1, m), 21):
                self.assertGreater(f.forcing(n), Q(1007, 1024)*r(n))
                self.assertGreater(f.forcing(n)-f.forcing(n+1), Q(495, 512)*gap(n))
                self.assertLess(abs(f.perturbation(n)), Q(17, 1024)*Q(1,16**(n*n))*gap(n))
                if n>m:
                    self.assertLess(f.endpoint_tail_bound(n), eps(n))

    def test_exact_forward_history_and_tail_telescope(self):
        for m in (0, 1, 3):
            f = FlatLock(m)
            state = Q(0)
            weighted = Q(0)
            for n in range(1, 23):
                state = 16*state+f.forcing(n)
                weighted += f.forcing(n)/16**n
                if n>=m:
                    self.assertEqual(state, 16**n*f.endpoint-f.g(n))
                    self.assertEqual(f.endpoint-weighted, f.g(n)/16**n)

    def test_locked_terminal_all_F_and_exact_norm(self):
        f = FlatLock(0)
        for B in (f.depth, f.depth+1, f.depth+3):
            terminal = 16**(2*B)*f.endpoint-f.g(2*B)
            C = terminal.numerator//terminal.denominator
            self.assertEqual(C % 16**B, 16**B-1)
            norm=Q(0)
            for k in range(1, B+1):
                z=terminal/16**k
                z-=z.numerator//z.denominator
                norm+=min(z,1-z)**2/B
            self.assertEqual(norm, f.g(2*B)**2*(1-Q(1,16**(2*B)))/(255*B))
            self.assertEqual((16**B*f.endpoint).denominator, 1)

    def test_mutations_are_detected(self):
        f=FlatLock(1)
        n=4
        wrong=15*f.g(n-1)-f.g(n)
        self.assertNotEqual(wrong, f.forcing(n))
        self.assertGreater(abs(wrong-r(n)), Q(17,1024)*Q(1,16**(n*n))*gap(n))
        coarse_q=f.endpoint+Q(1,16**f.prefix)
        self.assertGreater(abs(16**f.prefix*(coarse_q-f.endpoint)), eps(f.prefix))

    def test_exact_high_order_complete_monotonicity_failure(self):
        # A bound on all k+1 terms, not a rounded finite-difference sum.
        # The proof bounds the j>=2 perturbation tail geometrically.
        f=FlatLock(0)
        k=100_000_000
        ratio=Q(k,3*16**11)
        self.assertLess(ratio,Q(1,2))
        authentic_upper=Q(1,2*(k+1)*(k+2))
        correction_tail=k*(k-1)*Q(17,1024)*gap(5)/16**25
        upper=(authentic_upper+f.perturbation(3)
               +k*abs(f.perturbation(4))+correction_tail)
        self.assertLess(upper,-Q(1,10**15))


def receipts():
    rows=[]
    for m in (0, 1, 3, 7):
        f=FlatLock(m)
        rows.append({"prefix":m,"source_cutoff":f.cutoff,"radix_depth":f.depth,
                     "locked_endpoint":str(f.endpoint),
                     "first_changed_forcing_ratio":str(f.forcing(m+1)/r(m+1))})
    print(json.dumps({"scope":"finite exact controls only", "rows":rows},indent=2))


if __name__ == "__main__":
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    receipts()
    raise SystemExit(not result.wasSuccessful())
