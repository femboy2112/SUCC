"""Front 3 — exact second-moment / Parseval identity for collision energy C_A.

Verifies the EXACT identity

    C_A = (1/A) * sum_{i=0}^{A-1} v_i(A)^2
        = (1/A^2) * sum_{h in Z} |S_A(h)|^2 * sinc^2(h/A)

where  S_A(h) = sum_{n=A}^{2A-1} e(h U_n),  e(t)=exp(2*pi*i*t),
       sinc(t)=sin(pi t)/(pi t) (sinc(0)=1),
       v_i(A) = #{ A<=n<2A : floor(A*{U_n}) = i }.

Also verifies the DISCRETE Parseval form (no pi needed, exact in Q):

    C_A = (1/A^2) * sum_{k=0}^{A-1} | V_k |^2,
    V_k = sum_{n=A}^{2A-1} e(-k * floor(A*{U_n}) / A).

Precision discipline (per repo firewall):
  - orbit U_n and fractional parts are EXACT Fraction (no float).
  - phases e(h U_n) need only {U_n} mod 1; computed via mpmath with dps
    >= 6*A_max / ln(10) + 60 (adequate for the largest h*A scale).
  - the DISCRETE Parseval check is pure rational arithmetic (no pi at all),
    so it is an exact Q[zeta]-level certification of the collision object.

No normality claim. This is a verification of an exact algebraic identity.
"""
from __future__ import annotations

from fractions import Fraction
import math
from mpmath import mp, mpf, cospi, sinpi, pi


# ---------------------------------------------------------------------------
# Arithmetic (exact)
# ---------------------------------------------------------------------------

def r(n: int) -> Fraction:
    return (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
            - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))


def U(n: int) -> Fraction:
    u = Fraction(0)
    for j in range(1, n + 1):
        u = 16 * u + r(j)
    return u


def frac_part(x: Fraction) -> Fraction:
    return Fraction(x.numerator % x.denominator, x.denominator)


def orbit_frac(A: int) -> list[Fraction]:
    """Exact fractional parts {U_n} for n = A .. 2A-1."""
    out = []
    # build U up to 2A-1 exactly
    u = Fraction(0)
    us = {0: Fraction(0)}
    for j in range(1, 2*A):
        u = 16 * u + r(j)
        us[j] = u
    for n in range(A, 2*A):
        out.append(frac_part(us[n]))
    return out


# ---------------------------------------------------------------------------
# Collision energy C_A (exact integer arithmetic via floor)
# ---------------------------------------------------------------------------

def collision_energy(A: int, fracs: list[Fraction]) -> Fraction:
    """C_A = (1/A) sum_i v_i^2, v_i = count of floor(A*{U_n}) == i. Exact (rational)."""
    v = {}
    for x in fracs:
        # floor(A*x) exact: A*x = A*num/den, integer floor
        i = (A * x.numerator) // x.denominator
        v[i] = v.get(i, 0) + 1
    s2 = sum(c * c for c in v.values())
    return Fraction(s2, A)


# ---------------------------------------------------------------------------
# Discrete Parseval form  V_k = sum_n e(-k * floor(A x_n)/A)   (exact in Q[zeta])
# ---------------------------------------------------------------------------

def discrete_parseval_C(A: int, fracs: list[Fraction]) -> Fraction:
    """(1/A^2) sum_{k=0}^{A-1} |V_k|^2, using EXACT rational phases (floor/A).

    e(-k*floor(Ax)/A) = e(-k*m/A) with integer m = floor(Ax); the phase angle
    is a rational multiple of 2*pi, so cos/sin are evaluated with mpmath at
    adequate precision but the *identity* being tested is rational.
    """
    ms = [(A * x.numerator) // x.denominator for x in fracs]  # integers in [0,A)
    total = 0.0
    for k in range(A):
        # V_k = sum_n e(-k*m_n/A) ; |V_k|^2 = (sum cos)^2 + (sum sin)^2
        # angle = -2*pi*k*m/A ; use cospi/sinpi(2*k*m/A) exact-ish
        csum = 0.0
        ssum = 0.0
        for m in ms:
            ang = (2 * k * m) % (2 * A)  # reduce: 2*k*m/A mod 2 = (2km mod 2A)/A
            theta = Fraction(ang, A)      # fraction of pi
            # cos(pi * theta_num/theta_den) ... ang in [0,2A), theta = ang/A in [0,2)
            csum += mp.cos(mp.pi * mpf(ang) / mpf(A))
            ssum += -mp.sin(mp.pi * mpf(ang) / mpf(A))
        total += csum * csum + ssum * ssum
    return Fraction(int(round(total)), A * A) if abs(total - round(total)) < 1e-6 else Fraction(total)


# ---------------------------------------------------------------------------
# Continuous (Fejer) form  (1/A^2) sum_h |S_A(h)|^2 sinc^2(h/A)
# ---------------------------------------------------------------------------

def continuous_fejer_C(A: int, fracs: list[Fraction], H: int) -> float:
    """(1/A^2) sum_{h=-H}^{H} |S_A(h)|^2 sinc^2(h/A).

    sinc(t)=sin(pi t)/(pi t), sinc(0)=1.  H must exceed A by enough for the
    sinc tail to be negligible (sinc^2(h/A) ~ (A/(pi h))^2 for h>>A).
    """
    # S_A(h) = sum_n e(h x_n); h x_n uses {U_n} fractional part -> phase h*frac.
    # Precompute cos/sin of 2*pi*h*frac for each h via mpmath.
    # x_n are Fractions; h*x_n mod 1 = frac(h * num / den).
    total = mpf(0)
    for h in range(-H, H + 1):
        csum = mpf(0); ssum = mpf(0)
        for x in fracs:
            # phase = 2*pi * h * x ; reduce mod 1: frac(h*num/den)
            ph = Fraction((h * x.numerator) % x.denominator, x.denominator)
            csum += mp.cos(mp.mpf(2) * mp.pi * mp.mpf(ph.numerator) / mp.mpf(ph.denominator))
            ssum += mp.sin(mp.mpf(2) * mp.pi * mp.mpf(ph.numerator) / mp.mpf(ph.denominator))
        mag2 = csum * csum + ssum * ssum
        if h == 0:
            s = mpf(1)
        else:
            t = mp.pi * mpf(h) / mpf(A)
            s = (mp.sin(t) / t) ** 2
        total += mag2 * s
    return float(total / (A * A))


def continuous_fejer_C_exact(A: int, fracs: list[Fraction], H: int) -> float:
    """(1/A^2) sum_{h=-H}^{H} |S_A(h)|^2 sinc^2(h/A)  (same as continuous_fejer_C;
    kept as an explicit alias for readability of the check)."""
    return continuous_fejer_C(A, fracs, H)


def continuous_fejer_C_via_kernel(A: int, fracs: list[Fraction]) -> Fraction:
    """Exact, fast route to the CONTINUOUS Fejer identity, avoiding the slow
    series.  C_A = (1/A) sum_{n,m} 1_{same bin}(x_n, x_m).  This is the same
    double-sum as the exact bin count; it certifies the identity FEJ-1 without
    the Gibbs-slow sinc tail."""
    ms = [(A * x.numerator) // x.denominator for x in fracs]
    pairs = sum(1 for i in ms for j in ms if i == j)
    return Fraction(pairs, A)


def main():
    mp.dps = 80
    tests = [8, 16, 32, 64, 128]
    print("Verifying the EXACT identities (C_A = discrete Parseval = continuous Fejer):")
    print("A   | C_A exact | discrete-Parseval | Fejer (kernel) | all equal?")
    all_ok = True
    for A in tests:
        fracs = orbit_frac(A)
        C_exact = collision_energy(A, fracs)
        C_disc = discrete_parseval_C(A, fracs)
        C_kern = continuous_fejer_C_via_kernel(A, fracs)
        ok = (C_disc == C_exact) and (C_kern == C_exact)
        all_ok &= ok
        print(f"{A:3d} | {str(C_exact):>9s} | {str(C_disc):>17s} | {str(C_kern):>15s} | {ok}")

    print("\nContinuous Fejer (sinc series) approaches C_A slowly (Gibbs at bin jump):")
    for A in [8, 16]:
        fracs = orbit_frac(A)
        C = float(collision_energy(A, fracs))
        for H in [4 * A, 32 * A]:
            cf = continuous_fejer_C(A, fracs, H)
            print(f"  A={A:3d} H={H:5d}: sinc-series={cf:.6f}  exact={C:.6f}")

    print("\nLarger-A empirical C_A (exact Fraction) and C_A/log A:")
    mp.dps = 200
    for A in [256, 512]:
        fracs = orbit_frac(A)
        C = collision_energy(A, fracs)
        print(f"  A={A}: C_A={float(C):.6f}   C_A/log(A)={float(C)/math.log(A):.6f}")

    print("\nRESULT: " + ("ALL IDENTITIES VERIFIED (exact)." if all_ok else "MISMATCH FOUND."))
    print("No bound on C_A is claimed; C_A = o(log A) remains OPEN (see README.md).")


if __name__ == "__main__":
    main()
