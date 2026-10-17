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

    # Bisect the scalar cap tau: positivity begins at the largest tau with
    # (A4_lo - tau*Wl) still strictly PD.
    lo, hi = F(0), F(1)
    for _ in range(80):
        mid = (lo + hi) / 2
        _, m = _parity_block_min_eig(_mat_sub(A4_lo, _scale(Wl, mid)))
        if m > 0:
            lo = mid
        else:
            hi = mid
    tau_star = lo
    print(f"positivity-threshold cap   = {float(tau_star):.10e}")
    print(f"  exact                     = {tau_star}")

    young = GPRIME_L1_UPPER ** 2 / KAPPA
    print(f"present Young cap 121/32    = {float(young):.5f}")
    print(f"required improvement factor = {float(young / tau_star):.6e}")

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
