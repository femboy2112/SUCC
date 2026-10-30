"""Exact rational checks for the SUCC human T-action snapshot dossier.

These tests certify finite identities in a declared model, not pi normality,
physical impulses, a new uniqueness theorem, or RH.
"""
from fractions import Fraction
import unittest


def action(x, base=16):
    """Digit plus recentered state; x must be in [0,1)."""
    if not (isinstance(x, Fraction) and 0 <= x < 1 and isinstance(base, int) and base >= 2):
        raise ValueError("requires rational x in [0,1), integer base >=2")
    scaled = base * x
    digit = scaled.numerator // scaled.denominator
    return digit, scaled - digit


def reconstruct(digit, residual, base=16):
    if not (isinstance(digit, int) and 0 <= digit < base
            and isinstance(base, int) and base >= 2
            and isinstance(residual, Fraction) and 0 <= residual < 1):
        raise ValueError("invalid digit / residual")
    return (digit + residual) / base


def orbit(x, steps, base=16):
    for _ in range(steps):
        digit, recentered = action(x, base)
        yield x, digit, recentered
        x = recentered


class HumanTActionSnapshotTests(unittest.TestCase):
    def test_reversible_if_digit_is_retained(self):
        for base in (2, 3, 16):
            for digit in range(base):
                for residual in (Fraction(0), Fraction(1, 7), Fraction(4, 5)):
                    x = reconstruct(digit, residual, base)
                    self.assertEqual(action(x, base), (digit, residual))

    def test_losing_digit_is_base_to_one(self):
        r = Fraction(2, 7)
        for base in (2, 3, 16):
            origins = [reconstruct(d, r, base) for d in range(base)]
            self.assertEqual(len(set(origins)), base)
            self.assertEqual({action(x, base)[1] for x in origins}, {r})

    def test_exact_reset_jump(self):
        for base in (2, 3, 16):
            for x in (Fraction(0), Fraction(1, 9), Fraction(8, 17)):
                for before, digit, after in orbit(x, 9, base):
                    # The chosen between-frame lift reaches base*before.
                    self.assertEqual(after - base * before, -digit)

    def test_distributional_jump_identity_exact_pairing(self):
        # Pick a=1 and an affine between-frame lift q(n+s)=x_n(1+(b-1)s).
        # On (0,M), Dq=(b-1)x_n dt - sum d_n delta_(n+1).
        # Test against phi(t)=t(M-t), exactly, using Fraction arithmetic.
        for base in (2, 3, 16):
            for seed in (Fraction(0), Fraction(3, 17), Fraction(11, 29)):
                M = 6
                history = list(orbit(seed, M, base))
                lhs = Fraction(0)
                regular = Fraction(0)
                atoms = Fraction(0)
                for n, (x, digit, _) in enumerate(history):
                    A = M - 2 * n
                    # - integral_0^1 x[1+(b-1)s] * (A-2s) ds
                    lhs -= x * (A - 1 + (base - 1) * (Fraction(A, 2) - Fraction(2, 3)))
                    # integral_0^1 (b-1)x * (n+s)(M-n-s) ds
                    regular += (base - 1) * x * (
                        n * (M - n) + Fraction(M - 2 * n, 2) - Fraction(1, 3)
                    )
                    atoms -= digit * (n + 1) * (M - n - 1)
                self.assertEqual(lhs, regular + atoms)

    def test_reversed_delta_sign_is_detected(self):
        base = 16
        seed = Fraction(3, 17)
        M = 5
        history = list(orbit(seed, M, base))
        lhs = regular = atoms = Fraction(0)
        for n, (x, digit, _) in enumerate(history):
            A = M - 2 * n
            lhs -= x * (A - 1 + (base - 1) * (Fraction(A, 2) - Fraction(2, 3)))
            regular += (base - 1) * x * (
                n * (M - n) + Fraction(M - 2 * n, 2) - Fraction(1, 3)
            )
            atoms -= digit * (n + 1) * (M - n - 1)
        self.assertNotEqual(atoms, 0)
        self.assertEqual(lhs, regular + atoms)
        self.assertNotEqual(lhs, regular - atoms)

    def test_exact_finite_haar_partition_grid(self):
        for base in (2, 3, 16):
            q = 7
            tally = {(d, Fraction(j, q)): 0 for d in range(base) for j in range(q)}
            for j in range(base * q):
                d, r = action(Fraction(j, base * q), base)
                tally[d, r] += 1
            self.assertEqual(set(tally.values()), {1})

    def test_finite_snapshots_do_not_fix_future(self):
        for base in (2, 3, 16):
            for N in range(1, 8):
                # Both sequences start with N zero digits, but then differ.
                a = Fraction(0)
                c = Fraction(1, base ** (N + 1))
                da = [d for _, d, _ in orbit(a, N + 1, base)]
                dc = [d for _, d, _ in orbit(c, N + 1, base)]
                self.assertEqual(da[:N], dc[:N])
                self.assertNotEqual(da[N], dc[N])

    def test_temporal_aliasing_with_distinct_midframe_phase(self):
        f = Fraction(1, 7)
        f_alias = f + 1
        for n in range(20):
            self.assertEqual((f * n) % 1, (f_alias * n) % 1)
        self.assertNotEqual((f * Fraction(1, 2)) % 1,
                            (f_alias * Fraction(1, 2)) % 1)

    def test_continuous_chart_does_not_force_delta(self):
        # A different interpolation q(n+s)=(1-s)x_n+s*x_(n+1)
        # is continuous at every boundary. Same exact snapshots, no jumps.
        history = list(orbit(Fraction(3, 17), 8))
        for n in range(len(history) - 1):
            _, _, after = history[n]
            next_before, _, _ = history[n + 1]
            self.assertEqual(after, next_before)

    def test_zero_orbit_stays_nonnormal(self):
        history = list(orbit(Fraction(0), 32))
        self.assertEqual([digit for _, digit, _ in history], [0] * 32)


if __name__ == "__main__":
    unittest.main()
