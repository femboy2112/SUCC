"""Finite exact-receipt probe for the zero-anchored lambda/Haar compiler.

Run from repository root:
  python research/2026-11-10/zero_anchored_lambda_haar/probe.py

Displayed decimal fields are *only* formatted diagnostics. Verdict signs are
computed from rigorous Fraction enclosures; no asymptotic result is inferred.
"""
import json
from fractions import Fraction as Q

from observational_succ import zero_anchored_lambda_haar as z


def sign_interval(pair):
    lo, hi = pair
    return "POSITIVE" if lo > 0 else "NEGATIVE" if hi < 0 else "UNRESOLVED"


def main():
    theta = Q(3, 4)
    true_prefix = z.certified_digits(256, depth=12)
    assert true_prefix[:16] == tuple(int(c,16) for c in "3243F6A8885A308D")
    # Finite-shadow only: a rational seed made from the authenticated source.
    shadow = -z.prefix(100)
    assert shadow and z.recover(z.from_prefix(5,shadow)) == shadow
    assert z.certified_digits(64,shadow,depth=12) == (0,)*64
    rows = []
    for seed_name, seed, sizes in (("original_zero", Q(0), (16,32,64,128,256)),
                                   ("rational_shadow", shadow, (16,32,64))):
        previous = None
        for N in sizes:
            cert = z.certified_haar_defect(N,seed,depth=12)
            digits = z.certified_digits(N,seed,depth=12)
            residual = None if previous is None else sign_interval(
                z.contraction_excess(cert,previous,theta))
            rows.append({
                "seed": seed_name,
                "N": N,
                "parity": str(z.parity_pin(digits)),
                "haar_midpoint_display_only": f"{float(cert.midpoint_defect):.12f}",
                "haar_error_upper_display_only": f"{float(cert.error):.3e}",
                "theta_3_4_excess_sign": residual,
                "zero_anchor": z.authenticate(z.from_prefix(N,seed)),
            })
            previous = cert
    result = {
        "truth_state": "OBSERVED_FINITE; pi normality and asymptotic contraction OPEN",
        "source": "frozen four-pole BBP, original zero seed; rational shadow uses -P_100",
        "tests": "exact rational source, certified completed phases, interval W1",
        "rows": rows,
        "constant_zero_counterorbit": {
            "source_seed": "s_*=-pi/16 (nonrational, symbolic)",
            "haar_defect_exact": "15/32",
            "contraction_excess_theta_3_4_exact": "15/128",
            "claim": "Same forcing and tail fixed point; source-zero authentication fails"
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
