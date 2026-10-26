"""Ladder contraction probe (forward instrument; PROVES NOTHING by itself).

The Main XII no-go (SK2-A1) showed a fixed positive-proportion relative block loss is
insufficient for S_N(h)=o(N); sufficiency needs a full relative loss c_N -> 1, reachable
via the multiplicative x16 frequency ladder e(hU_{n+1}) = e(16h U_n) e(h r(n+1)).  This
module exposes the two forward quantities for the next round:

  * `ladder_identity_residual` -- the EXACT, forcing-agnostic identity
        {U_{n+1}} == {16 {U_n} + r(n+1)}     (residual == 0 for ANY forcing),
    the only CERTAIN output here (a deterministic receipt, Q[Q/Z] exact);

  * `ladder_ratio` -- the OBSERVED contraction factor lambda_N(h)=|a_N(16h)|/|a_N(h)|
    with a_N(h)=(1/N) sum_{n<=N} e(hU_n).  A proof of limsup_h lambda_N(h) < 1 for the
    AUTHENTIC orbit (while FAILING on the hard controls) would give the power saving
    N^{-gamma}; this module does NOT prove it and MUST NOT be read as doing so.

pi base-16 normality: OPEN.  RH: OPEN.  lambda_N(h) is a numerical diagnostic, never a
certificate; the only proved output is the identity residual.
"""
from fractions import Fraction as Q

from . import succ_internal_matrix_walk as mw
from .signed_pushforward import authentic_states

# --- grep-able honest status flags (firewall) ---
ladder_contraction_proved = False   # limsup_h lambda_N(h) < 1 is UNVERIFIED / OPEN
pi_normality_proved = False


def ladder_identity_residual(states):
    """[{U_{n+1}} - {16 {U_n} + r(n+1)}]_n : all EXACTLY Q(0) (forcing-agnostic)."""
    out = []
    for n in range(1, len(states)):
        lhs = mw.circle(states[n])                                   # {U_{n+1}}
        rhs = mw.circle(16 * mw.circle(states[n - 1]) + mw.authentic_r(n + 1))
        out.append(lhs - rhs)
    return out


def mean_phasor_abs(states, h, precision=60):
    """|a_N(h)| = |(1/N) sum_n e(hU_n)|  (OBSERVED, evaluated -- not a certificate)."""
    N = len(states)
    s = mw.PhasePoly.zero()
    for u in states:
        s = s + mw.formal_character(h, u)
    return abs(complex((s / N).evaluation(precision=precision)))


def ladder_ratio(states, h, precision=60):
    """OBSERVED lambda_N(h) = |a_N(16h)| / |a_N(h)|  (diagnostic only)."""
    lo = mean_phasor_abs(states, h, precision)
    hi = mean_phasor_abs(states, 16 * h, precision)
    return (hi / lo) if lo > 0 else float("inf")


def report(N=64, hs=(1, 2, 3)):
    """Human-readable forward report.  Prints the honest status line."""
    states = authentic_states(N)
    resid = ladder_identity_residual(states)
    identity_exact = all(r == 0 for r in resid)
    lines = [
        f"ladder identity {{U_n+1}}=={{16{{U_n}}+r}} exact (all residuals 0): {identity_exact}",
        "OBSERVED lambda_N(h)=|a_N(16h)|/|a_N(h)| (NOT a certificate):",
    ]
    for h in hs:
        lines.append(f"    h={h}: lambda_N={ladder_ratio(states, h):.4f}")
    lines.append("pi normality OPEN; ladder contraction UNVERIFIED; identity EXACT")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
