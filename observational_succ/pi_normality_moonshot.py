"""π-normality moonshot: the Fejér energy instrument and the circularity check.

Two exact/verified facts, both reproducible here:

1. The Fejér (chord-energy) instrument.  For base b, x in R/Z, band M, horizon N,
       E(M,N) = 1 + 2 Σ_{h=1..M} (1 - h/(M+1)) |A_{h,N}(x)|²,
   with A the Weyl sum.  This module computes E exactly-in-the-limit-shape using
   mpmath at a precision that actually resolves frac(b^j x) (dps > j*log10(b)).

2. The chord-polynomial circularity.  With d(z)=|1-z|² and K_M the Fejér kernel
   expressed in X = d, we verify symbolically that
       Σ_{j,k} d_{jk}^m = N² Σ_h (-1)^h C(2m,m+h) |A_{h,N}|²,
   i.e. the chord energy IS the Fourier energy.  This is the proof that the
   chord-polynomial route consumes no new information.

NOTE ON PRECISION (a real bug this repo hit): resolving frac(b^j x) for j < N
requires mp.mp.dps > N*log10(b).  At fixed dps the phases are garbage past
j ≈ dps/log10(b), and the chord mean spuriously "decays" like 1/N.  Every
function here sets precision from N; use `_dps_for`.

No claim about π normality.  No zero coordinates.
"""
from __future__ import annotations

import math
from fractions import Fraction as F


class MoonShotError(ValueError):
    pass


def _dps_for(base: int, n_terms: int) -> int:
    """Decimal digits needed to resolve frac(base^j * x) for j < n_terms."""
    if type(base) is not int or base < 2:
        raise MoonShotError("base >= 2 integer")
    if type(n_terms) is not int or n_terms < 1:
        raise MoonShotError("n_terms >= 1 integer")
    return int(math.ceil(n_terms * math.log10(base))) + 60


def phases(x, base: int, n_terms: int):
    """[frac(base^j * x) for j < n_terms], at a precision that resolves them.

    The value x MUST be re-read from its source string under the high-precision
    context: an mpf created by the caller carries only the caller's precision,
    so multiplying it by base^j loses the fractional part once base^j exceeds
    that precision.  Callers may pass a string (e.g. mp.nstr(mp.pi, D)) or a
    float; floats are re-read as their decimal repr, which is exact intent for
    a 17-digit value but is NOT enough for large j -- prefer strings.
    """
    import mpmath as mp
    dps = _dps_for(base, n_terms)
    with mp.workdps(dps):
        # Convert to a string at full working precision BEFORE entering the
        # loop, so the multiplication sees every digit.
        if isinstance(x, str):
            xx = mp.mpf(x)
        else:
            # Re-evaluate the source at this precision when it is a known
            # constant-like object; otherwise take its exact decimal.
            try:
                xx = mp.mpf(mp.nstr(x, dps))
            except Exception:
                xx = mp.mpf(x)
        out = []
        for j in range(n_terms):
            out.append(mp.frac(mp.mpf(base) ** j * xx))
        return out


def phases_for_pi(base: int, n_terms: int):
    """frac(base^j * pi) for j < n_terms, computed from pi at full precision.

    This is the ONLY reliable entry point for the constant pi: the value of pi
    must be generated inside the high-precision context, never passed in from
    an mpf that was created at the caller's precision.
    """
    import mpmath as mp
    dps = _dps_for(base, n_terms)
    with mp.workdps(dps):
        pi = +mp.pi                      # evaluated at dps
        out = []
        for j in range(n_terms):
            out.append(mp.frac(mp.mpf(base) ** j * pi))
        return out


def _phases_dispatch(x, base: int, n_terms: int):
    """Use phases_for_pi for the pi sentinel; else the generic path."""
    if x == "pi":
        return phases_for_pi(base, n_terms)
    return phases(x, base, n_terms)


def weyl_sum(x, base: int, h: int, n_terms: int):
    """A_{h,N}(x) = (1/N) Σ_{j<N} exp(2πi h base^j x).

    Pass x="pi" for the constant pi (computed at full precision internally);
    any other exact value must be supplied as a string with enough digits.
    """
    import mpmath as mp
    if type(h) is not int or h == 0:
        raise MoonShotError("h must be a nonzero integer")
    with mp.workdps(_dps_for(base, n_terms)):
        acc = mp.mpc(0)
        for t in _phases_dispatch(x, base, n_terms):
            acc += mp.expjpi(2 * h * t)
        return acc / n_terms


def fejer_energy(x, base: int, band: int, n_terms: int):
    """E(M,N) - 1 = 2 Σ_{h=1..M} (1 - h/(M+1)) |A_{h,N}|².  Returns a float."""
    if type(band) is not int or band < 1:
        raise MoonShotError("band >= 1 integer")
    total = 0.0
    for h in range(1, band + 1):
        a = abs(weyl_sum(x, base, h, n_terms))
        total += 2.0 * (1.0 - h / (band + 1)) * float(a) ** 2
    return total


def chord_mean(x, base: int, n_terms: int):
    """Empirical mean of d(z_j) = |1 - exp(2πi frac(base^j x))|².

    Haar target is exactly 2 (i.e. binom(2,1)).  Requires correct precision;
    see the module note.
    """
    import mpmath as mp
    with mp.workdps(_dps_for(base, n_terms)):
        tot = mp.mpf(0)
        for t in _phases_dispatch(x, base, n_terms):
            tot += abs(1 - mp.expjpi(2 * t)) ** 2
        return tot / n_terms


def chord_energy_identity_check(m: int, n_terms: int, base: int = 2, x=None):
    """Verify Σ_{j,k} d_{jk}^m = N² Σ_h (-1)^h C(2m,m+h) |A_{h,N}|².

    This is the circularity witness: the chord polynomial of degree m is
    exactly the Fourier energy truncated at |h| <= m.  Returns
    (lhs, rhs, relative_gap).
    """
    import mpmath as mp
    if type(m) is not int or m < 1:
        raise MoonShotError("m >= 1 integer")
    if x is None:
        x = "pi"
    with mp.workdps(_dps_for(base, n_terms) + 20):
        ph = [mp.expjpi(2 * t) for t in _phases_dispatch(x, base, n_terms)]
        # lhs: (1/N^2) sum_{j,k} |z_j - z_k|^{2m}
        lhs = mp.mpf(0)
        for j in range(n_terms):
            for k in range(n_terms):
                lhs += abs(ph[j] - ph[k]) ** (2 * m)
        lhs /= n_terms ** 2
        # rhs: sum_{|h|<=m} (-1)^h C(2m,m+h) |A_hN|^2
        rhs = mp.mpf(0)
        for h in range(-m, m + 1):
            coeff = (-1) ** h * math.comb(2 * m, m + h)
            a = abs(weyl_sum(x, base, h, n_terms)) ** 2 if h != 0 else mp.mpf(1)
            rhs += coeff * a
        gap = abs(lhs - rhs) / max(abs(rhs), mp.mpf(1))
        return lhs, rhs, gap


__all__ = ["MoonShotError", "phases", "phases_for_pi", "weyl_sum", "fejer_energy", "chord_mean",
           "chord_energy_identity_check", "_dps_for"]
