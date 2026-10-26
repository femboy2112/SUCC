"""Historical Fourier-ratio instrument, with the source-time shift audit.

A fixed proportional block loss is insufficient for S_N(h)=o(N). The original
proposal to compound these frequency ratios into a power saving was not valid:
frequency multiplication by 16 is a source-time shift with a bounded defect.
See ladder_shift_audit.py and the 2026-10-26 source-bridge dossier. This module
retains its numerical diagnostic and its exact finite identity:

  * `ladder_identity_residual` -- the EXACT authentic-forcing identity
        {U_{n+1}} == {16 {U_n} + r(n+1)}     (residual == 0 for any seed),
    the only CERTAIN output here (a deterministic receipt, Q[Q/Z] exact);

  * `ladder_ratio` -- the OBSERVED contraction factor lambda_N(h)=|a_N(16h)|/|a_N(h)|
    with a_N(h)=(1/N) sum_{n<=N} e(hU_n).  At fixed N, the literal unbounded-h
    contraction is REFUTED by the authentic common denominator: both averages
    equal 1 at its multiples. At fixed h, a uniform ratio q<1 would already
    imply O_h(1/N) normalized sums. It is a strong missing cancellation premise,
    not an independently proved mechanism that can simply be iterated.

pi base-16 normality: OPEN.  RH: OPEN.  lambda_N(h) is a numerical diagnostic, never a
certificate; the only proved output is the identity residual.
"""
from fractions import Fraction as Q

from . import succ_internal_matrix_walk as mw
from .signed_pushforward import authentic_states

# --- grep-able honest status flags (firewall) ---
ladder_contraction_proved = False   # prescribed-band/selected-source saving is unproved
unbounded_frequency_contraction_refuted = True
pi_normality_proved = False


def ladder_identity_residual(states):
    """Exact zero residual for authentic-forcing histories, with any initial seed.

    This instrument uses mw.authentic_r. For a general declared forcing use
    ladder_shift_audit, whose identity takes that forcing as an input.
    """
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
    lines.append("pi normality OPEN; band-restricted contraction UNVERIFIED; "
                 "unbounded-h contraction REFUTED; identity EXACT")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
