"""Exact structure of C_A: verify the near-collision / spacing analysis.

C_A = (1/A) sum_i v_i(A)^2, v_i(A) = #{A<=n<2A: floor(A{U_n})=i}.
U_n exact rational (Fraction).  Verifies:
  (1) C_A empirically bounded (random-pair signature);
  (2) colliding pairs have spacing ~1/A^2, NOT 1/(Q_n Q_m) ~ exp(-12A);
  (3) no exact-integer-difference or exact-equal-frac pairs.
"""
from fractions import Fraction as Q
from collections import defaultdict


def r(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def states(N):
    U = [Q(0)]
    for n in range(1, N+1):
        U.append(16*U[-1] + r(n))
    return U


def frac(u):
    return u - Q(u.numerator // u.denominator)


def collision(A, U):
    cnt = defaultdict(list)
    for n in range(A, 2*A):
        cnt[int(frac(U[n])*A)].append(n)
    v = [len(ns) for ns in cnt.values()]
    return sum(x*x for x in v) / A, cnt


def main():
    U = states(4096)
    print("=== C_A profile (exact Fraction) ===")
    for A in [16, 32, 64, 128, 256, 512, 1024, 2048]:
        cA, _ = collision(A, U)
        print("A=%5d  C_A=%.6f" % (A, cA))

    A = 256
    import mpmath as mp
    mp.mp.dps = 60
    cA, cnt = collision(A, U)
    dists = []
    exact_int = 0
    exact_eq = 0
    for b, ns in cnt.items():
        for i in range(len(ns)):
            for j in range(i+1, len(ns)):
                n, m = ns[i], ns[j]
                fd = frac(U[n]) - frac(U[m])   # tiny rational in (-1,1)
                num = abs(fd.numerator)
                ln = float(mp.log(num) - mp.log(fd.denominator))
                dists.append(ln)
                if (U[n]-U[m]).denominator == 1:
                    exact_int += 1
                if frac(U[n]) == frac(U[m]):
                    exact_eq += 1
    dists.sort()
    print("\n=== A=%d collision structure ===" % A)
    print("same-bin pairs: %d" % len(dists))
    print("exact-integer-difference pairs: %d" % exact_int)
    print("exact-equal-fractional-part pairs: %d" % exact_eq)
    print("spacing exponents log10||{U_n}-{U_m}|| (smallest 5), vs 1/A=10^%.2f, 1/A^2=10^%.2f:"
          % (mp.log10(1/A), mp.log10(1/(A*A))))
    for ln in dists[:5]:
        print("  10^%.2f" % (ln/mp.log(10)))


if __name__ == '__main__':
    main()
