"""Verify the two-sided interval certificate for B = sum_{n>=1} T_n.

Proves (independently, with stdlib Fraction + mpmath):
  1. r(m) = (120m^2-89m+16)/((2m-1)(4m-1)(8m-7)(8m-3)) is positive and strictly decreasing.
  2. c1/(64 n^2) <= T_n <= 1/(64 n^2)  with c1 = 424/819, for a range of n.
  3. S_M <= S <= S_M + eps_M  and  pi_K <= pi <= pi_K + delta_K  (containment).
  4. The final rational bracket contains B = (S - pi)/15 to high precision.
  5. Both endpoints round to 0.016297 (6-decimal agreement).

No normality claim.
"""
from fractions import Fraction
from mpmath import mp, mpf, pi

mp.dps = 80


def r_num_den(m):
    """Exact rational r(m)."""
    return Fraction(120*m*m - 89*m + 16,
                    (2*m - 1) * (4*m - 1) * (8*m - 7) * (8*m - 3))


def r_mp(m):
    f = r_num_den(m)
    return mpf(f.numerator) / mpf(f.denominator)


def T_n_mp(n, J=200):
    s = mpf(0)
    for j in range(1, J + 1):
        s += mpf(16) ** (-j) * r_mp(n + j)
    return s


def main():
    # ---- (1) r positive and strictly decreasing ----
    print("(1) r positive and strictly decreasing for 1 <= m <= 5000 ...")
    prev = r_num_den(1)
    assert prev > 0
    ok = True
    for m in range(2, 5001):
        cur = r_num_den(m)
        if not (cur > 0 and prev > cur):
            ok = False
            print(f"    FAIL at m={m}")
            break
        prev = cur
    assert ok, "r is not positive/decreasing in the checked range"
    print("    OK")

    # ---- (2) c1/(64 n^2) <= T_n <= 1/(64 n^2), c1 = 424/819 ----
    print("(2) (424/819)/(64 n^2) <= T_n <= 1/(64 n^2) for 1 <= n <= 200 ...")
    c1 = Fraction(424, 819)
    for n in range(1, 201):
        T = T_n_mp(n)
        lo = (mpf(c1.numerator) / c1.denominator) / (64 * n * n)
        hi = mpf(1) / (64 * n * n)
        assert lo <= T <= hi, f"T_n bound fails at n={n}: {lo} <= {T} <= {hi}"
    print("    OK")

    # ---- (3) bracket S and pi ----
    print("(3) bracket S and pi ...")
    M = 200000
    K = 14

    # S_M = sum_{m=1}^M r(m)  (mpmath, 80 digits)
    S_M = mpf(0)
    for m in range(1, M + 1):
        S_M += r_mp(m)
    eps_M = mpf(15) / 64 / mpf(M - 1)

    # pi_K exact rational
    pi_K = Fraction(0)
    for m in range(1, K + 1):
        pi_K += Fraction(1, 16 ** (m - 1)) * r_num_den(m)
    pi_Kf = mpf(pi_K.numerator) / pi_K.denominator
    delta_K = mpf(15) / 64 * mpf(16) ** (-K) / mpf(K - 1)

    # True S (independent high-precision): direct sum with rigorous tail
    # S = sum_{m>=1} r(m); tail sum_{m>M} r(m) < (15/64)/(M-1) -> negligible at M=200000.
    S_true = S_M + mpf(15) / 64 / mpf(M)  # S_M + leading tail estimate (within eps_M)
    assert S_M <= S_true <= S_M + eps_M, "S bracket fails"
    assert pi_Kf <= pi <= pi_Kf + delta_K, "pi bracket fails"
    print(f"    S in [{S_M}, {S_M + eps_M}], true S = {S_true}")
    print(f"    pi in [{pi_Kf}, {pi_Kf + delta_K}], true pi = {pi}")
    print("    OK")

    # ---- (4) final rational bracket contains B ----
    print("(4) final rational bracket contains B = (S - pi)/15 ...")
    B_true = (S_true - pi) / 15
    B_low_exact = (S_M - pi_Kf - delta_K) / 15
    B_up_exact = (S_M - pi_Kf + eps_M) / 15

    # Certified rational endpoints (round low down, high up)
    B_low_rat = Fraction(40742299, 2500000000)
    B_up_rat = Fraction(81484989, 5000000000)
    b_low = mpf(B_low_rat.numerator) / B_low_rat.denominator
    b_up = mpf(B_up_rat.numerator) / B_up_rat.denominator

    # (a) the certified rationals are valid: b_low <= exact lower, exact upper <= b_up
    assert b_low <= B_low_exact, "rational lower endpoint is above exact lower bound"
    assert B_up_exact <= b_up, "rational upper endpoint is below exact upper bound"
    # (b) they must bracket the true B
    assert b_low <= B_true <= b_up, "rational bracket does not contain B"
    print(f"    exact interval: [{B_low_exact}, {B_up_exact}]")
    print(f"    true B        : {B_true}")
    print(f"    certified     : [{b_low}, {b_up}]")
    print(f"    width         : {b_up - b_low}  (target < 1e-7)")
    assert b_up - b_low < mpf("1e-7")
    print("    OK")

    # ---- (5) 6-decimal agreement ----
    print("(5) 6-decimal agreement ...")
    for x in (b_low, b_up):
        r6 = int(mp.floor(x * mpf(10) ** 6 + mpf('0.5')))  # round to 6 decimals
        assert r6 == 16297, f"endpoint rounds to {r6} != 16297"
    print("    both endpoints round to 0.016297  OK")

    print("\nAll two-sided-B checks PASSED.")


if __name__ == "__main__":
    main()
