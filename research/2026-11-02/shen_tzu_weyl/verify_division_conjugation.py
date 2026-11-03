"""Verify the division/conjugation obstruction and the Cayley separation.

1. Circle conjugation z->1/z (theta->-theta) maps under Cayley w=-i(z-1)/(z+1)
   to LINE NEGATION w->-w, NOT to line division w->1/w.
2. The BBP orbit {16^{n-1} pi} has no digit-complement pair (not closed under conjugation).
"""
import mpmath as mp
from fractions import Fraction as Q


def cayley(z):
    return -1j*(z-1)/(z+1)


def r(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def main():
    mp.mp.dps = 60
    print("=== Cayley: circle conjugation -> line negation (not 1/w) ===")
    for th in [0.3, 1.0, 2.0]:
        z = mp.exp(1j*th)
        w = cayley(z)
        w_inv = cayley(1/z)  # image of conjugation
        # check w_inv == -w (negation), not 1/w
        is_negation = abs(w_inv + w) < 1e-12
        is_division = abs(w_inv - (1/w if abs(w) > 1e-12 else 0)) < 1e-12
        print("  theta=%.3f: cayley(1/z)=%+.4f vs -w=%+.4f (negation=%s, division=%s)"
              % (th, w_inv.real, (-w).real, is_negation, is_division))

    print("\n=== Orbit digit-complement check (conjugation-symmetry) ===")
    digits = []
    x = mp.frac(mp.pi)
    for i in range(64):
        digits.append(int(mp.floor(16*x)))
        x = mp.frac(16*x)
    found = False
    for n in range(40):
        for m in range(40):
            if n == m:
                continue
            comp = tuple(15-d for d in digits[n:n+8])
            if tuple(digits[m:m+8]) == comp:
                found = True
                print("  complement pair n=%d m=%d" % (n, m))
    print("  digit-complement (conjugation) pairs: %s" % ("YES" if found else "NONE"))


if __name__ == '__main__':
    main()
