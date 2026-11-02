"""Exact verification of the f_m decomposition and f_4 pole-isolation (Round 2).

PROVED: r(n) = 2 f_3(n) + f_4(n) + f_5(n), f_m(n) = 1/(8n-7) - 1/(8n-7+m);
the -1/p pole (p=5 mod 8) is carried exclusively by f_4(a_p).

stdlib Fraction only. No normality claim.
"""
from fractions import Fraction


def f(n, m):
    return Fraction(1, 8*n-7) - Fraction(1, 8*n-7+m)


def r(n):
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def U(n):
    u = Fraction(0)
    for j in range(1, n+1):
        u = 16*u + r(j)
    return u


def U_part(n, m, coeff):
    """sum_{j<=n} 16^{n-j} * coeff * f_m(j), via the recurrence."""
    u = Fraction(0)
    for j in range(1, n+1):
        u = 16*u + coeff*f(j, m)
    return u


def main():
    # (1) pointwise decomposition r = 2 f_3 + f_4 + f_5
    for j in range(1, 30):
        assert 2*f(j, 3) + f(j, 4) + f(j, 5) == r(j), j
    print("(1) r(n) = 2 f_3(n) + f_4(n) + f_5(n)  exact for n=1..29  PASS")

    # (2) U_n = 2 U^{(3)} + U^{(4)} + U^{(5)}
    for n in range(1, 15):
        lhs = U_part(n, 3, 2) + U_part(n, 4, 1) + U_part(n, 5, 1)
        assert lhs == U(n), n
    print("(2) U_n = 2U^{(3)}_n + U^{(4)}_n + U^{(5)}_n  exact for n=1..14  PASS")

    # (3) f_4 pole isolation: for p=5 mod 8, the -1/p is exclusively in f_4(a_p)
    print("(3) f_4 pole isolation:")
    for p in [13, 29, 37, 53, 61, 101, 149, 197]:
        if p % 8 != 5:
            continue
        a = (p+3)//8
        assert 8*a - 3 == p  # p = 8a_p - 3
        # f_4(a_p) = 1/(p-4) - 1/p  carries the -1/p
        assert f(a, 4) == Fraction(1, p-4) - Fraction(1, p)
        # f_3(a_p), f_5(a_p) are p-free
        assert f(a, 3).denominator % p != 0
        assert f(a, 5).denominator % p != 0
        # the pole of U^{(4)} at a_p has v_p = -1; the others are p-free
        print(f"  p={p}: a_p={a}, f_4(a_p)={f(a,4)} carries -1/p; f_3,f_5 p-free  PASS")

    # (4) cofactor V_{p,n} via f_m decomposition equals SPP-01 cofactor
    print("(4) cofactor identity V_{p,n} = 2U^{(3)} + U^{(5)} + (U^{(4)} + 16^{n-a_p}/p):")
    for p in [13, 29, 37]:
        if p % 8 != 5:
            continue
        a = (p+3)//8
        b = (p+1)//2
        for n in range(a, b):
            Un = U(n)
            clock = -Fraction(16**(n-a), p)   # c_p = -1
            V_spp = Un - clock                 # SPP-01 cofactor
            V_fm = (U_part(n, 3, 2) + U_part(n, 5, 1)
                    + (U_part(n, 4, 1) + Fraction(16**(n-a), p)))
            assert V_fm == V_spp, (p, n, V_fm, V_spp)
            assert V_spp.denominator % p != 0  # p-free
        print(f"  p={p}: V (f_m) == V (SPP-01), p-free, for all n in window  PASS")

    print("\nAll exact structural checks passed.")


if __name__ == "__main__":
    main()
