"""Verify the exact asymptotic series of T_n = sum_{j>=1} 16^{-j} r(n+j).

Checks the exact rational coefficients 1/64, -7/512, 55/4096, -595/32768, 8551/262144
against direct high-precision computation, to ~1e-20.

stdlib Fraction + mpmath only. No normality claim.
"""
from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 80


def r(n):
    f = (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
         - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))
    return mpf(f.numerator) / mpf(f.denominator)


def T(n):
    return sum(mpf(16) ** (-j) * r(n + j) for j in range(1, 90))


# exact rational coefficients c_2..c_6
coeff = {2: Fraction(1, 64), 3: Fraction(-7, 512), 4: Fraction(55, 4096),
         5: Fraction(-595, 32768), 6: Fraction(8551, 262144)}


def main():
    print("Exact T_n asymptotic coefficients:")
    for m, c in sorted(coeff.items()):
        print(f"  c_{m} = {c} = {float(c)}")

    print("\nVerification (T_n vs partial sums of the asymptotic series):")
    ok = True
    for n in [1000, 5000, 20000]:
        Tn = T(n)
        partial = sum(mpf(c.numerator) / mpf(c.denominator) / mpf(n) ** m
                      for m, c in sorted(coeff.items()))
        diff = Tn - partial
        print(f"  n={n}: |T_n - partial(2..6)| = {float(abs(diff)):.3e}")
        ok = ok and abs(diff) < mpf(10) ** (-20)
    assert ok, "coefficients failed to match"

    # two-sided bound check: 1/(64n^2) - 7/(512n^3) < T_n < 1/(64n^2) for large n
    print("\nTwo-sided bound check (for n >= 100):")
    for n in [100, 500, 2000]:
        Tn = T(n)
        lo = mpf(1) / (64 * mpf(n)**2) - mpf(7) / (512 * mpf(n)**3)
        hi = mpf(1) / (64 * mpf(n)**2)
        assert lo < Tn < hi, (n, Tn, lo, hi)
        print(f"  n={n}: {float(lo):.3e} < T_n={float(Tn):.3e} < {float(hi):.3e}  OK")

    print("\nAll T_n asymptotic-series checks PASSED.")


if __name__ == "__main__":
    main()
