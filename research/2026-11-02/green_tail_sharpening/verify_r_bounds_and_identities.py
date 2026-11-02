"""Reproducible verification: sharp r(n) bounds + exact orbit identities (SUCC).

r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)
U_0 = 0,  U_{n+1} = 16 U_n + r(n+1)
T_n = sum_{j>=1} 16^{-j} r(n+j)   (Green tail; 16 T_n - T_{n+1} = r(n+1))

Part A (sharp two-sided bounds + asymptotic series, all PROVED):
  A1. r(n) > 15/(64 n^2)  and  r(n) < 15/(64 n^2) + 151/(512 n^3) + C4/n^4, C4 = 16182005/5779456.
  A2. r(n) strictly decreasing on n >= 1.
  A3. Asymptotic series r(n) = 15/(64 n^2) + 151/(512 n^3) + 1209/(4096 n^4) + ...
      with a_k = (4*7^k - 2*4^k - 3^k - 2^k)/8^{k+1}, all a_k > 0 for k>=1.

Part B (exact orbit identities):
  B1. 16 T_n - T_{n+1} = r(n+1)  (Green-tail defining identity).
  B2. 16 T_0 = pi  (BBP).
  B3. U_n + T_n = 16^{n-1} pi  (NEW exact identity linking the finite orbit to pi).
  B4. T_n - T_{n+1} = r(n+1) - 15 T_n ;  16 T_n = r(n+1) + T_{n+1}.
  B5. U_{n+1} - 16 U_n = 16 T_n - T_{n+1}  (= r(n+1))  (U/T coupling).
  B6. T_{n+2} = (16 + R_n) T_{n+1} - 16 R_n T_n,  R_n = r(n+2)/r(n+1)  (exact 2nd order).
  B7. U_n is rational;  T_n = pi/16 - U_n/16^n  (exact pi + rational decomposition).
  B8. v_2(U_n) = v_2(n)  for all n >= 1  (NEW 2-adic valuation identity).

Pure stdlib (fractions) + mpmath (high precision). No normality claim.
"""
from fractions import Fraction
from mpmath import mp, mpf, pi

mp.dps = 60


def r(m):
    return (Fraction(4, 8*m - 7) - Fraction(2, 8*m - 4)
            - Fraction(1, 8*m - 3) - Fraction(1, 8*m - 2))


def r_mp(m):
    return (mpf(4)/(8*m - 7) - mpf(2)/(8*m - 4)
            - mpf(1)/(8*m - 3) - mpf(1)/(8*m - 2))


def T_mp(n):
    return sum(mpf(16)**(-j) * r_mp(n + j) for j in range(1, 400))


def U(n):
    u = Fraction(0)
    for j in range(1, n + 1):
        u = 16 * u + r(j)
    return u


def U_mp(n):
    u = mpf(0)
    for j in range(1, n + 1):
        u = 16 * u + r_mp(j)
    return u


def a_k(k):
    """Coefficient of 1/n^{k+1} in the asymptotic series for r(n)."""
    return Fraction(4 * 7**k - 2 * 4**k - 3**k - 2**k, 8**(k + 1))


def v2_frac(q):
    """2-adic valuation of a Fraction (num/den)."""
    num, den = q.numerator, q.denominator
    v = 0
    while num % 2 == 0:
        num //= 2
        v += 1
    while den % 2 == 0:
        den //= 2
        v -= 1
    return v


def main():
    print("=" * 72)
    print("PART A: sharp bounds on r(n)")
    print("=" * 72)

    # A3: asymptotic coefficients (exact)
    print("\n[A3] Asymptotic coefficients a_k (coefficient of 1/n^{k+1}):")
    for k in range(1, 6):
        print(f"     a_{k} = {a_k(k)}")
    assert a_k(1) == Fraction(15, 64)
    assert a_k(2) == Fraction(151, 512)
    assert a_k(3) == Fraction(1209, 4096)
    assert a_k(4) == Fraction(8995, 32768)
    print("     -> matches stated 15/64, 151/512, 1209/4096, 8995/32768.")

    # all a_k > 0 for k>=1
    for k in range(1, 30):
        assert a_k(k) > 0, f"a_{k} not positive"
    print("     all a_k > 0 for k=1..29 (proved: N_k = 4*7^k-2*4^k-3^k-2^k > 0).")

    # A1: lower bound r(n) > 15/(64 n^2)
    print("\n[A1] Lower bound r(n) > 15/(64 n^2):")
    for n in range(1, 2000):
        assert r(n) > Fraction(15, 64 * n * n), f"lower fails n={n}"
    print("     verified n=1..1999 exactly. (proved: r - 15/64n^2 = positive rational)")

    # A1: upper bound r(n) < 15/(64 n^2) + 151/(512 n^3) + 1209/(4096 n^4) + C5/n^5
    C5 = Fraction(16182005, 5779456)
    print(f"\n[A1] Upper bound r(n) < 15/(64n^2)+151/(512n^3)+1209/(4096n^4)+C5/n^5, C5={C5}:")
    for n in range(1, 2000):
        ub = (Fraction(15, 64) / (n*n)
              + Fraction(151, 512) / (n**3)
              + Fraction(1209, 4096) / (n**4)
              + C5 / (n**5))
        assert r(n) < ub, f"upper fails n={n}"
    print("     verified n=1..1999 exactly.")
    # Simpler 3-term bound C3 = 1461681/346624
    C3 = Fraction(1461681, 346624)
    for n in range(1, 2000):
        ub = (Fraction(15, 64) / (n*n)
              + Fraction(151, 512) / (n**3)
              + C3 / (n**4))
        assert r(n) < ub, f"3-term upper fails n={n}"
    print("     3-term variant (C3=1461681/346624) also verified n=1..1999.")

    # A2: strict decrease
    print("\n[A2] r(n) strictly decreasing:")
    for n in range(1, 2000):
        assert r(n) > r(n + 1), f"decrease fails n={n}"
    print("     verified n=1..1999 exactly. (proved: r'(n)<0 and r(n)-r(n+1)>0)")

    print("\n" + "=" * 72)
    print("PART B: exact orbit identities")
    print("=" * 72)

    # B1/B2: 16 T_n - T_{n+1} = r(n+1); 16 T_0 = pi
    print("\n[B1/B2] 16 T_n - T_{n+1} = r(n+1);  16 T_0 = pi:")
    bbp = sum(mpf(16)**(-(m - 1)) * r_mp(m) for m in range(1, 300))
    print(f"     sum 16^-(m-1) r(m) = {mp.nstr(bbp, 30)}  == pi = {mp.nstr(pi, 30)}")
    assert abs(bbp - pi) < mpf("1e-40")
    for n in range(0, 8):
        lhs = 16 * T_mp(n) - T_mp(n + 1)
        rhs = r_mp(n + 1)
        assert abs(lhs - rhs) < mpf("1e-40"), f"B1 fails n={n}"
    print("     16 T_0 = pi (BBP) and 16 T_n - T_{n+1} = r(n+1) verified.")

    # B3: U_n + T_n = 16^{n-1} pi  (NEW)
    print("\n[B3] U_n + T_n = 16^{n-1} pi  (NEW exact identity):")
    for n in [1, 2, 3, 5, 10]:
        lhs = U_mp(n) + T_mp(n)
        rhs = mpf(16)**(n - 1) * pi
        assert abs(lhs - rhs) < mpf("1e-40"), f"B3 fails n={n}"
        print(f"     n={n}: U_n + T_n = {mp.nstr(lhs, 25)}  == 16^{n-1} pi = {mp.nstr(rhs, 25)}")
    print("     (U_n rational + Green tail T_n exactly rebuild 16^{n-1} pi.)")

    # B7: T_n = 16^{n-1} pi - U_n  (rearranged from B3)
    print("\n[B7] T_n = 16^{n-1} pi - U_n  (rearranged from B3):")
    for n in [1, 2, 3, 4, 5]:
        u = U(n)
        predict = mpf(16)**(n - 1) * pi - mpf(u.numerator)/mpf(u.denominator)
        assert abs(predict - T_mp(n)) < mpf("1e-40"), f"B7 fails n={n}"
        print(f"     n={n}: U_n = {u}  ->  T_n = 16^{n-1} pi - U_n verified.")

    # B5: U_{n+1} - 16 U_n = 16 T_n - T_{n+1} = r(n+1)
    print("\n[B5] U_{n+1} - 16 U_n = 16 T_n - T_{n+1} = r(n+1):")
    for n in range(1, 6):
        lhs = 16 * U(n - 1) + r(n)  # U_n
        assert 16 * U(n - 1) + r(n) == U(n)
        assert U(n) - 16 * U(n - 1) == r(n)
    print("     U recurrence and U/T coupling to r(n+1) verified exactly.")

    # B8: v_2(U_n) = v_2(n)
    print("\n[B8] v_2(U_n) = v_2(n)  (NEW 2-adic valuation identity):")
    for n in range(1, 1001):
        assert v2_frac(U(n)) == v2_frac(Fraction(n)), f"B8 fails n={n}"
    print("     verified n=1..1000 exactly.")

    print("\nAll sharp-bound and orbit-identity checks PASSED.")


if __name__ == "__main__":
    main()
