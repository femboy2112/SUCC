# x3_dimension_repro.py  — FINITE certificates only; no asymptotic proof is claimed.
# Companion to X3_DIMENSION.md (obligation (B) attack, branch research/x3-rigidity-frontier-2026-11-02).
from fractions import Fraction
from math import log
import mpmath as mp


def r(n):  # four-pole BBP forcing (docs/PI_GEARBOX_ATLAS.md source law)
    return Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4) - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2)


def main():
    # --- (i) conductor growth log(Q_n)/n -> 6 ---
    U = Fraction(0, 1)
    rows = []
    for n in range(1, 201):
        U = 16 * U + r(n)
        rows.append((n, U.denominator, log(U.denominator) / n))
    print("[i] conductor log(Q_n)/n (should -> 6):")
    print("    " + ", ".join(f"n={n}:{ratio:.4f}" for n, _, ratio in rows if n in (20, 50, 100, 200)))

    # --- (ii) exact no-exponential-pair denominator bound ---
    U = Fraction(0, 1)
    Un = []
    for n in range(1, 90):
        U = 16 * U + r(n)
        Un.append(U % 1)  # exact fractional part
    best = min((abs(Un[i] - Un[j]), i + 1, j + 1)
               for i in range(len(Un)) for j in range(i + 1, len(Un)))
    print(f"[ii] min |U_n - U_m| over N=90 (exact rational): {float(best[0]):.3e}  pair ({best[1]},{best[2]})")
    QN = rows[88][1]  # Q_89
    import math
    print(f"[ii] denominator bound 1/Q_89^2 ~ e^(-{2 * math.log(QN):.2f})  (lower bound on any pair; log2 Q_89={math.log2(QN):.1f} bits)")
    print(f"[ii] => no pair is closer than 1/(Q_n Q_m); this is exponential e^(-12N), NOT polynomial.")

    # --- (iii) empirical N^{-2} spacing of the true x_n = {16^{n-1} pi} orbit (FINITE) ---
    mp.mp.dps = 400
    pi = mp.pi

    def x(n):
        return mp.fmod(16 ** (n - 1) * pi, 1)

    print("[iii] min spacing of {16^{n-1} pi} (FINITE, high precision):")
    for N in (40, 80, 120, 180, 220):
        xs = [x(n) for n in range(1, N + 1)]
        mn = min(abs(xs[i] - xs[j]) for i in range(N) for j in range(i + 1, N))
        # log(N)/(-log(mn)) ~ 0.5  <=>  mn ~ N^{-2}  (random-pair scaling)
        print(f"    N={N:4d}: min spacing={float(mn):.2e}   log10(N)/(-log10(mn))={log(N) / -log(float(mn)):.3f}")

    # --- (iv) no exact collision (x_84 vs x_85 is a precision artifact) ---
    print(f"[iv] x_84 = {mp.nstr(x(84), 25)}")
    print(f"[iv] x_85 = {mp.nstr(x(85), 25)}")
    print(f"[iv] |x_84 - x_85| = {mp.nstr(abs(x(84) - x(85)), 25)}  (nonzero; exact collision would force pi rational)")


if __name__ == "__main__":
    main()
