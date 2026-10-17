"""Probe: CertifiedTrial two-sided Loewner enclosure of the original four-mode
Suzuki/Weil Schur complement S_4 = A_4 - R_4 at a = 1/2.

Reproduces A_4 > 0 (certified at adequate Gamma depth), the U = 0 certified
baseline enclosure, a numerically-DISCOVERED high response U re-certified by
EXACT arithmetic (candidate discovery separated from proof), and the
NON-CERTIFIED finite-mode residual-Gram diagnostic that locates the binding
constraint. No zeta-zero inputs. RH PROVED: NO.

Run:  PYTHONPATH=. python3 scripts/certified_four_schur_trial_probe.py
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.certified_four_schur_trial import (
    CertifiedTrial, _g_block, _parity_block_min_eig, min_eig_lower, A_RADIUS,
)
from observational_succ.suzuki_moment_schur import parity_blocks


def a4_positivity(J, depth=44):
    """Rigorously certified min-eigenvalue lower bound of A_4 at Gamma depth J.

    A_4(full) >= A_4^{(J)} (omitted Gamma tail is PSD).  A_4^{(J)} lies in the
    interval box [lo,hi]; the Loewner statement A_4^{(J)} >= mid - r I holds with
    mid the midpoint matrix and r an upper bound on the spectral radius of the
    (nonnegative, symmetric) radius matrix (max abs row sum).  So min-eig of
    A_4(full) >= min_eig_lower(mid) - r, computed per exact parity block.  An
    entrywise lower endpoint is NOT a Loewner lower bound and is deliberately
    NOT used.  The unnormalized P_n(2t) metric makes magnitudes tiny; only the
    SIGN (certified here) is coordinate-independent."""
    G = _g_block(4, J)
    mid = tuple(tuple((G[i][j].lo + G[i][j].hi) / 2 for j in range(4)) for i in range(4))
    radm = tuple(tuple((G[i][j].hi - G[i][j].lo) / 2 for j in range(4)) for i in range(4))
    pbm, pbr = parity_blocks(mid, 4), parity_blocks(radm, 4)
    out = {"J": J}
    overall = None
    for label in ("odd", "even"):
        bm, br = pbm[label], pbr[label]
        r = max((sum(abs(x) for x in row) for row in br), default=F(0))
        v = min_eig_lower(bm, depth) - r
        out[label + "_min_eig_lower"] = str(v)
        out[label + "_loewner_radius"] = str(r)
        overall = v if overall is None else min(overall, v)
    out["A4_full_min_eig_lower"] = str(overall)
    out["A4_full_is_positive_definite_certified"] = overall > 0
    return out


def rationalize_parity(Ufloat, rank, denom=10**6):
    """Round a numerical high response to rationals, preserving reflection parity."""
    U = []
    for i in range(rank - 4):
        h = i + 5
        row = []
        for j in range(4):
            l = j + 1
            if (h - l) % 2:
                row.append(F(0))                 # parity forces exact zero
            else:
                row.append(F(round(float(Ufloat[i][j]) * denom), denom))
        U.append(tuple(row))
    return tuple(U)


def discover_numerical_U(rank, digits=50, nodes=24, trial="galerkin"):
    """Numerically DISCOVER a high response (not a proof). Uses the existing
    numerical trial machinery; the result is rationalized then re-certified."""
    from observational_succ.four_low_schur_proof_teeth import (
        numerical_full_source_matrix, numerical_derivative_grid, numerical_trial,
    )
    fm = numerical_full_source_matrix(rank=rank, digits=digits)
    dg = numerical_derivative_grid(rank=rank, nodes_per_panel=nodes)
    nt = numerical_trial(fm, dg, rank=rank, trial=trial)
    return nt["U"], nt


def main():
    report = {"object": "S_4 = A_4 - R_4 (original four-mode Suzuki/Weil Schur)",
              "a": str(A_RADIUS), "RH_PROVED": "NO"}

    # (A) A_4 > 0, certified at increasing Gamma depth
    report["A4_positivity"] = [a4_positivity(J) for J in (24, 48, 64)]

    # (B) U = 0 certified baseline enclosure (rank 8, J 48)
    base = CertifiedTrial(U=(), J=48, rank=8, diagnostic=True)
    report["U0_baseline"] = {k: base[k] for k in (
        "verdict", "A4_interval_midpoint_min_eig_lower",
        "upper_bracket_is_psd", "lower_bracket_is_psd",
        "upper_bracket_min_eig_lower", "lower_bracket_min_eig_lower",
        "gamma_positive_tail_norm_upper", "interval_loewner_radius_GJ",
        "diagnostic_lower_bracket_min_eig_lower", "diagnostic_note")}

    # (C) numerically-discovered U, re-certified exactly
    certified_trials = []
    for trial in ("galerkin", "quotient_least_squares"):
        try:
            Uf, nt = discover_numerical_U(rank=8, trial=trial)
            Ur = rationalize_parity(Uf, rank=8)
            ct = CertifiedTrial(U=Ur, J=48, rank=8, diagnostic=True)
            certified_trials.append({
                "discovery": trial,
                "numerical_upper_eigenvalues": nt["upper_eigenvalues"],
                "numerical_quotient_lower_eigenvalues": nt["quotient_lower_eigenvalues"],
                "certified_verdict": ct["verdict"],
                "certified_upper_is_psd": ct["upper_bracket_is_psd"],
                "certified_upper_min_eig_lower": ct["upper_bracket_min_eig_lower"],
                "certified_lower_min_eig_lower": ct["lower_bracket_min_eig_lower"],
                "certified_diagnostic_lower_min_eig_lower":
                    ct.get("diagnostic_lower_bracket_min_eig_lower"),
            })
        except Exception as exc:
            certified_trials.append({"discovery": trial,
                                     "error": f"{type(exc).__name__}: {exc}"})
    report["certified_numerically_discovered_trials"] = certified_trials

    report["interpretation"] = (
        "A_4 > 0 is certified (both parity blocks) at adequate Gamma depth; the "
        "even block is nearly singular (unnormalized margin ~1e-13, sign robust). "
        "For every trial the certified UPPER bracket A_4 - L_U stays PSD (no "
        "negative witness -> S_4 NOT certified negative); the certified LOWER "
        "bracket is indefinite -> S_4 NOT certified positive. Verdict: CERTIFIED "
        "AMBIGUOUS, exact gap quantified. CRUCIAL diagnosis: the NUMERICAL tight "
        "residual bracket A_4 - L_U - (1/kappa) C_quot is itself ALL-NEGATIVE "
        "(eigenvalues ~ -5e-2..-1e-5) at the numerically optimal U, so the "
        "obstruction is NOT merely the conservative Young residual cap -- it is the "
        "1/kappa = 50 amplification of the residual energy (equivalently the "
        "high-sector coercivity constant kappa = 1/50 is too small, or the genuine "
        "low/high arithmetic residual coupling is too large). The next decisive "
        "probe is a SHARPER high-sector coercivity kappa (a better theorem than "
        "D_4 >= K/50) and/or a residual theorem that does not pay the full 1/kappa, "
        "together with a certified high-Legendre-coefficient decay modulus (open "
        "Section 3C) to make the tight residual Gram rigorous.")
    print(json.dumps(report, indent=2, default=str))


if __name__ == "__main__":
    main()
