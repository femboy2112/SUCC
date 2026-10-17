"""PDQ megaswarm audit: reproduce the exact positivity-threshold obstruction.

Independent of the sibling branch's modules for the *threshold* computation:
this script rebuilds the certified lower bracket from the authenticated source
block alone and bisects the scalar cap at which positivity begins, then shows
that neither the published Young cap nor the improved coercivity kappa' reaches
it.  It is an obstruction instrument, not a sign verdict.

Run:  python scripts/pdq_threshold_obstruction.py
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main() -> int:
    from observational_succ.certified_four_schur_trial import (
        GPRIME_L1_UPPER, KAPPA, _g_block, _loewner_radius, _mat_sub,
        _parity_block_min_eig, _scale, _scalar_shift, legendre_L2_norm2,
    )

    RANK, J = 12, 64
    Gblk = _g_block(RANK, J)
    A4_mid = tuple(tuple((Gblk[i][j].lo + Gblk[i][j].hi) / 2 for j in range(4))
                   for i in range(4))
    A4_rad = _loewner_radius(tuple(tuple((Gblk[i][j].hi - Gblk[i][j].lo) / 2
                                         for j in range(4)) for i in range(4)))
    A4_lo = _scalar_shift(A4_mid, A4_rad)
    Wl = tuple(tuple(legendre_L2_norm2(i + 1) if i == j else F(0)
                     for j in range(4)) for i in range(4))
    _, a4_min = _parity_block_min_eig(A4_lo)

    print("=== PDQ threshold obstruction (independent reproduction) ===")
    print(f"A4 interval-lower min eig  = {float(a4_min):.10e}")
    print(f"W_L2(low) diag             = {[str(Wl[i][i]) for i in range(4)]}")

    # ---- EXACT even/odd-block generalized-eigenvalue threshold ----
    # A4_lo is EXACTLY parity-block-diagonal (cross entries vanish), so the true
    # threshold tau* = sup{tau : A4_lo - tau*W_low >= 0} = smallest generalized
    # eigenvalue of the pair (A4_lo, W_low) IN THE W_low (Legendre-mass) METRIC
    # decouples into two 2x2 blocks. For a block [[p,q],[q,r]] with W=diag(w1,w2),
    #   det(block - tau*W) = (w1 w2) tau^2 - (p w2 + r w1) tau + (p r - q^2),
    # a quadratic in tau with rational coefficients whose smallest root is that
    # block's threshold; tau* is the min over the two blocks. This is the exact
    # algebraic threshold, NOT a dyadic bisection endpoint.
    from math import isqrt

    def _sqrt_bracket(delta, D=10 ** 18):
        # rational s_lo, s_hi with s_lo**2 <= delta <= s_hi**2 (certified)
        n = isqrt((delta.numerator * D * D) // delta.denominator)
        return F(n, D), F(n + 1, D)

    def _block_threshold_bracket(i0, i1):
        p, r, q = A4_lo[i0][i0], A4_lo[i1][i1], A4_lo[i0][i1]
        w1, w2 = Wl[i0][i0], Wl[i1][i1]
        A_c = w1 * w2
        B = p * w2 + r * w1
        C = p * r - q * q
        disc = B * B - 4 * A_c * C
        if disc < 0:
            raise ArithmeticError("complex generalized eigenvalue")
        s_lo, s_hi = _sqrt_bracket(disc)
        # smallest root = (B - sqrt(disc)) / (2 A_c); larger sqrt -> smaller root
        return (B - s_hi) / (2 * A_c), (B - s_lo) / (2 * A_c), (A_c, B, C)

    odd_lo, odd_hi, _odd_q = _block_threshold_bracket(0, 2)
    even_lo, even_hi, even_q = _block_threshold_bracket(1, 3)
    tau_lo, tau_hi = min(odd_lo, even_lo), min(odd_hi, even_hi)
    binding = "even (modes 2,4)" if even_lo <= odd_lo else "odd (modes 1,3)"
    print()
    print("exact generalized-eigenvalue threshold tau* (W_low Legendre-mass metric):")
    print(f"  odd  block (modes 1,3): tau in ({float(odd_lo):.10e}, {float(odd_hi):.10e})")
    print(f"  even block (modes 2,4): tau in ({float(even_lo):.12e}, {float(even_hi):.12e})")
    print(f"  tau* (binding = {binding}) in ({float(tau_lo):.12e}, {float(tau_hi):.12e})")
    print(f"  even-block exact quadratic coeffs (A*t^2 - B*t + C): {even_q}")

    # Conservative DYADIC lower witness (min_eig_lower bisection). NOT the threshold:
    # the inner min_eig_lower is a conservative lower bound on lambda_min, so this
    # halts just BELOW tau*. Retained only to exhibit a cap where positivity
    # provably still holds.
    lo, hi = F(0), F(1)
    for _ in range(80):
        mid = (lo + hi) / 2
        _, m = _parity_block_min_eig(_mat_sub(A4_lo, _scale(Wl, mid)))
        if m > 0:
            lo = mid
        else:
            hi = mid
    tau_dyadic = lo
    print(f"conservative dyadic lower witness (NOT the threshold) = {float(tau_dyadic):.12e}")
    print(f"  provably PD here; lies ~{float(tau_lo - tau_dyadic):.2e} below tau*")

    young = GPRIME_L1_UPPER ** 2 / KAPPA
    print(f"present Young cap 121/32    = {float(young):.5f}")
    print(f"required improvement factor = {float(young / tau_hi):.6e}")

    print()
    print("kappa sweep (each still negative):")
    for label, kp in (("1/50 (published)", F(1, 50)),
                      ("0.021420 (WB4 exact m4)", F(21420, 10**6)),
                      ("0.038983 (audit)", F(389832818322773, 10**16))):
        cap = GPRIME_L1_UPPER ** 2 / kp
        _, m = _parity_block_min_eig(_mat_sub(A4_lo, _scale(Wl, cap)))
        print(f"  kappa={label:26s} cap={float(cap):9.5f} "
              f"min_eig={float(m):+.6e} "
              f"{'POSITIVE' if m > 0 else 'negative'}")

    print()
    print("CONCLUSION: the Young channel is ~6.3e6 too loose; the binding")
    print("constraint is the derivative-energy/moment channel (margin O(1e-8)),")
    print("not coercivity. S4 sign remains AMBIGUOUS. RH NOT proved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
