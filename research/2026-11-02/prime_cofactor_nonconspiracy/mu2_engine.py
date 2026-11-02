"""MEGAROUND3-MU2: exact mu_2(h) engine.

mu_2(h) = (1/(L-1)) * sum_{r=0}^{L-2} sin^2(pi * h * delta_{p,r} / 2)   [task normalization]
         = (1/(L-1)) * sum_{r=0}^{L-2} sin^2(pi * h * delta_{p,r})       [engine/PCN-03 normalization]

Wait -- resolve the normalization below by direct Parseval match.

The task states:  sum_ell |D_hat|^2 = (1/L) sum_r |D_{p,h}(r)|^2 = (4/L) sum_r sin^2(pi h delta/2),
with |D|^2 = 4 sin^2(pi h delta/2).  So the task's sin^2 argument is (pi h delta / 2).

The PCN-03 engine uses  |D_{p,h}(r)|^2 = 4 sin^2(pi h delta_{p,r}/2)  [same], and its
`mu2_sum` accumulates  sin(pi * h * delta % 1)^2  -- i.e. WITHOUT the /2 inside, which would be
a DIFFERENT object (sin^2(pi h delta) vs sin^2(pi h delta/2)).

We compute BOTH and label them unambiguously:
   mu2_half(h) = (1/(L-1)) sum_r sin^2(pi h delta_{p,r} / 2)   [task's mu_2]
   mu2_full(h) = (1/(L-1)) sum_r sin^2(pi h delta_{p,r})       [PCN-03 engine's mu2_sum]

The task's delta is  delta_{p,r} = 15 W_{p,b_p+r} + r(b_p+r+1) + kappa_{p,b_p+r}
which equals W_{p,b_p+r+1} - W_{p,b_p+r} (verified: W_{j+1}-W_j = 15 W_j + r(j+1) + kappa_j).

Two independent methods:
  METHOD A: recurrence delta (W_{j+1} - W_j) with W = U_j - a_{p,j}/p, exact Fraction.
  METHOD B: closed form 15 W_j + r(j+1) + kappa_j, exact Fraction.
Both feed mpmath sin^2 at dps >= 6*Nmax/2.3 (Nmax = max ord_p(16) over the prime set).
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt

from mpmath import mp, mpf, mpc, pi, sin, sqrt


# ---------------------------------------------------------------------------
# exact integer / rational primitives (independent of mega_round_engine.py)
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d <= isqrt(n):
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def primes_range(lo: int, hi: int) -> list[int]:
    return [p for p in range(lo, hi + 1) if is_prime(p)]


def ord_p(base: int, p: int) -> int:
    cur = base % p
    o = 1
    while cur != 1:
        cur = (cur * base) % p
        o += 1
    return o


def r_bbp(n: int) -> Fraction:
    return (Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4)
            - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2))


def orbit(horizon: int) -> list[Fraction]:
    st = [Fraction(0)]
    cur = Fraction(0)
    for n in range(1, horizon + 1):
        cur = 16 * cur + r_bbp(n)
        st.append(cur)
    return st


def birth_step(p: int) -> int:
    return (p + 7) // 8 if p % 8 == 1 else (p + 3) // 8


def c_p(p: int) -> int:
    return 4 if p % 8 == 1 else p - 1


def a_pj(p: int, j: int, bp: int, cp: int) -> int:
    return (cp * pow(16, j - bp, p)) % p


# ---------------------------------------------------------------------------
# delta / mu_2 computation
# ---------------------------------------------------------------------------

def compute_mu2(p: int, h: int, dps: int):
    """Return exact-phase mu_2(h) via two methods, plus delta diagnostics.

    Returns dict with:
      mu2_half_A, mu2_full_A   (method A: W_{j+1}-W_j)
      mu2_half_B, mu2_full_B   (method B: 15 W_j + r + kappa)
      L, b_p, c_p, kappa_histogram, min/max sin^2 values, etc.
    """
    mp.dps = dps
    L = ord_p(16, p)
    bp = birth_step(p)
    cp = c_p(p)
    # full window j in [bp, bp+L-1]; increments r in [0, L-2]
    hor = bp + L - 1
    orb = orbit(hor)

    def frac(x: Fraction):
        return x - (x.numerator // x.denominator)

    sA_half = mpf(0)
    sA_full = mpf(0)
    sB_half = mpf(0)
    sB_full = mpf(0)
    kappas: dict[int, int] = {}
    delta_fracs: list[Fraction] = []
    max_sin = mpf(0)
    min_sin = mpf(1)

    for r in range(L - 1):
        j = bp + r
        a_j = a_pj(p, j, bp, cp)
        a_n = a_pj(p, j + 1, bp, cp)
        kappa = (16 * a_j) // p
        kappas[kappa] = kappas.get(kappa, 0) + 1

        w_j = orb[j] - Fraction(a_j, p)
        w_n = orb[j + 1] - Fraction(a_n, p)

        # METHOD A
        dA = frac(w_n - w_j)
        # METHOD B
        dB = frac(15 * w_j + r_bbp(j + 1) + kappa)

        assert dA == dB, (p, r, dA, dB)
        delta_fracs.append(dA)

        # task sin^2(pi h delta / 2)
        sA_half += sin(pi * h * mpf(dA.numerator) / mpf(dA.denominator) / 2) ** 2
        sB_half += sin(pi * h * mpf(dB.numerator) / mpf(dB.denominator) / 2) ** 2
        # PCN-03 sin^2(pi h delta)
        sA_full += sin(pi * h * mpf(dA.numerator) / mpf(dA.denominator)) ** 2
        sB_full += sin(pi * h * mpf(dB.numerator) / mpf(dB.denominator)) ** 2

        sv = sin(pi * h * mpf(dA.numerator) / mpf(dA.denominator) / 2) ** 2
        if sv > max_sin:
            max_sin = sv
        if sv < min_sin:
            min_sin = sv

    n = L - 1
    return {
        "p": p, "mod8": p % 8, "L": L, "b_p": bp, "c_p": cp,
        "mu2_half_A": float(sA_half / n),
        "mu2_full_A": float(sA_full / n),
        "mu2_half_B": float(sB_half / n),
        "mu2_full_B": float(sB_full / n),
        "kappa_hist": dict(sorted(kappas.items())),
        "max_sin2": float(max_sin),
        "min_sin2": float(min_sin),
    }


if __name__ == "__main__":
    import json
    # quick smoke on p=17, h=1
    print(json.dumps(compute_mu2(17, 1, 60), indent=2, default=str))
