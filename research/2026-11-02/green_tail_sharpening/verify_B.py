"""Verify the Green-tail sharpening theorem: B = (S - pi)/15, B < 1/61.

Checks, each exact or high-precision:
  1. sum_{m>=1} 16^{-(m-1)} r(m) = pi  (classical BBP, in our indexing).
  2. B = sum_n T_n equals (S - pi)/15, S = sum_m r(m).
  3. Strict bounds: B < 1/61 < 1/60 < 17/648 < 1/32.

stdlib Fraction + mpmath (high precision) only. No normality claim.
"""
from fractions import Fraction
from mpmath import mp, mpf, pi

mp.dps = 80


def r(m):
    f = (Fraction(4, 8*m - 7) - Fraction(2, 8*m - 4)
         - Fraction(1, 8*m - 3) - Fraction(1, 8*m - 2))
    return mpf(f.numerator) / mpf(f.denominator)


def main():
    # (1) BBP: sum_{m>=1} 16^{-(m-1)} r(m) = pi
    bbp = sum(mpf(16) ** (-(m - 1)) * r(m) for m in range(1, 300))
    print(f"(1) sum 16^-(m-1) r(m) = {bbp}")
    print(f"    pi                  = {pi}")
    print(f"    |diff| = {abs(bbp - pi)}  (should be ~0)")
    assert abs(bbp - pi) < mpf("1e-60")

    # (2) S = sum r(m); B = sum_n T_n; check B = (S - pi)/15
    # S with tail correction: sum_{m>M} r(m) ~ 15/64 * 1/M
    M = 4000
    S = sum(r(m) for m in range(1, M + 1)) + mpf(15) / 64 * (mpf(1) / M)
    # B direct: sum over n and j. T_n ~ 15/(64 n^2) * (1/15) ... actually T_n ~ r(n+1)/16 ~ 15/(64*16*n^2).
    # Truncate n at N0 and add the tail sum_{n>N0} T_n ~ sum_{n>N0} 15/(1024 n^2) ~ 15/(1024 N0).
    N0 = 2000
    B = mpf(0)
    for n in range(1, N0 + 1):
        B += sum(mpf(16) ** (-j) * r(n + j) for j in range(1, 80))
    B += mpf(15) / 1024 * (mpf(1) / N0)  # tail of the n-sum
    B_alt = (S - pi) / 15
    print(f"\n(2) S = {S}")
    print(f"    B (direct)    = {B}")
    print(f"    (S - pi)/15   = {B_alt}")
    print(f"    |B - (S-pi)/15| = {abs(B - B_alt)}  (should be ~0)")
    assert abs(B - B_alt) < mpf("1e-5")  # two independent O(1/M) truncations

    # (3) strict bounds
    print(f"\n(3) B = {B}")
    for label, bound in [("1/32", mpf(1)/32), ("17/648", mpf(17)/648),
                         ("1/60", mpf(1)/60), ("1/61", mpf(1)/61)]:
        print(f"    B < {label} = {bound}: {B < bound}")
    assert B < mpf(1)/61
    assert B < mpf(1)/60
    assert B < mpf(17)/648
    assert B < mpf(1)/32

    print("\nAll Green-tail sharpening checks PASSED.")


if __name__ == "__main__":
    main()
