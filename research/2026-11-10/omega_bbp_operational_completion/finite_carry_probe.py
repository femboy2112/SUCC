"""Finite exact calibration of productive BBP tail / carry cocycle.

Structural identities do not prove a limiting digit distribution. All arithmetic
uses fractions; no pi oracle or floating-point comparisons are involved.
"""
from fractions import Fraction
from math import floor


def bbp_source(n: int) -> Fraction:
    assert n >= 1
    return (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
            - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))


def finite_orbit(horizon: int, seed: Fraction, forcing=bbp_source):
    assert isinstance(seed, Fraction) and horizon >= 1
    p = [Fraction(0)]
    u = [seed]
    for j in range(1, horizon + 1):
        p.append(p[-1] + forcing(j) / (16**j))
        u.append(16*u[-1] + forcing(j))
    completed = [16**j * (seed + p[horizon]) for j in range(horizon + 1)]
    tails = [completed[j] - u[j] for j in range(horizon + 1)]
    crossings = [floor(u[j] - floor(u[j]) + tails[j]) for j in range(horizon + 1)]
    return u, tails, completed, crossings


def check(horizon: int, seed: Fraction, forcing=bbp_source) -> int:
    u, t, y, eps = finite_orbit(horizon, seed, forcing)
    assert all(0 <= value < 1 for value in t)  # valid for these controls
    assert all(value in (0, 1) for value in eps)
    for n in range(horizon):
        assert t[n+1] == 16*t[n] - forcing(n+1)
        assert y[n+1] == 16*y[n]
        kappa = floor(u[n+1]) - 16*floor(u[n])
        digit = floor(y[n+1]) - 16*floor(y[n])
        assert 0 <= digit < 16
        assert digit == kappa + eps[n+1] - 16*eps[n]
        assert (digit - kappa - eps[n+1]) % 2 == 0
    return horizon


def run() -> None:
    count = 0
    for horizon in (1, 2, 3, 7, 11, 14, 16, 32, 64):
        for seed in (Fraction(0), Fraction(1, 16), Fraction(-3, 100)):
            count += check(horizon, seed)
    horizon, target = 14, 7
    u, t, _, _ = finite_orbit(horizon, Fraction(0))
    # A rational seed deliberately positions finite U_target inside the
    # next tail-boundary strip; an exhaustive carry identity must survive it.
    adversarial_seed = (1 - t[target]/2 - u[target]) / 16**target
    _, _, _, crossings = finite_orbit(horizon, adversarial_seed)
    assert crossings[target] == 1
    count += check(horizon, adversarial_seed)
    count += check(14, Fraction(0), lambda n: Fraction(0))
    # The same structural laws hold for zero forcing, whose digits are all 0.
    _, _, completion, _ = finite_orbit(14, Fraction(0), lambda n: Fraction(0))
    assert all(value == 0 for value in completion)
    # The backward tail operator contracts by 1/16 in supremum norm.
    # An exact finite truncation of depth k has error bounded by 4/(15*16**k).
    for n in (0, 1, 3, 8):
        for k in (1, 2, 4, 10):
            approx = sum((bbp_source(n+j) / 16**j for j in range(1, k+1)), Fraction(0))
            longer = sum((bbp_source(n+j) / 16**j for j in range(1, k+101)), Fraction(0))
            assert 0 < longer - approx < Fraction(4, 15*16**k)
    print(f"PASS: {count} exact finite arrow squares + 16 strict tail enclosures; "
          "one forced boundary crossing; zero-forcing negative control")


if __name__ == '__main__':
    run()
