"""Replay exact Gamma-response and source prime-gap checks.

The universal claims have paper proofs in GAMMA_PRIME.md. This finite probe does
not test or certify R0 or normality. SymPy is used for symbolic rational algebra
and prime enumeration; original BBP states use fractions.Fraction.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import pairwise
import json
from pathlib import Path

import sympy as S


RECEIPT = Path(__file__).with_name("GAMMA_RESULTS.json")


def log_two_interval(terms: int = 8) -> tuple[F, F]:
    """Exact 2*atanh(1/3) series with a positive geometric remainder bound."""
    y = F(1, 3)
    lower = 2 * sum(y ** (2*k+1) / (2*k+1) for k in range(terms))
    error = 2 * y ** (2*terms+1) / ((2*terms+1) * (1-y*y))
    return lower, lower + error


def run() -> dict:
    z, s, t = S.symbols("z s t")
    f = (z+S.Rational(1, 8))**4 / (
        (z+S.Rational(1, 2))**2
        * (z+S.Rational(5, 8)) * (z+S.Rational(3, 4)))

    def source(q):
        return 4/(8*q-7)-2/(8*q-4)-1/(8*q-3)-1/(8*q-2)

    assert S.cancel(S.diff(f, z)/(8*f)-source(z+1)) == 0
    # Mutation: omit one unit of the authentic first-pole coefficient.
    assert S.cancel(S.diff(f, z)/(8*f)-(source(z+1)-1/(8*z+1))) != 0
    symbolic_cases = 2
    for n in range(1, 8):
        lhs = sum(16**(n-j) * S.diff(f.subs(z, z+j-1), z)
                  / (8*f.subs(z, z+j-1)) for j in range(1, n+1))
        rhs = sum(16**(n-j)*source(z+j) for j in range(1, n+1))
        assert S.cancel(lhs-rhs) == 0
        symbolic_cases += 1
    seed_log_ratio = 8*16**7*(s-t)*z
    assert S.diff(seed_log_ratio, z) == 8*16**7*(s-t)
    assert S.diff(seed_log_ratio, z, 2) == 0
    symbolic_cases += 1

    sequences = [[8*k+a for k in range(100) for a in residues]
                 for residues in [(1, 4, 5, 6), (2, 3, 4, 7)]]
    gaps = [p for seq in sequences for p in pairwise(seq)]
    expected = [(F(1, 4), F(1301, 252)), (F(1, 3), F(4951, 945)),
                (F(3, 7), F(2405, 441)), (F(1, 2), F(79, 14)),
                (F(3, 4), F(27, 4)), (F(1), F(8))]
    envelopes = []
    for x, wanted in expected:
        inherited = 4*sum(max(F(1, a)-(1+x)/b, 0) for a, b in gaps)
        assert 6*x+inherited == wanted
        active = [(a, b) for a, b in gaps if F(1, a) > (1+x)/b]
        # Every possible omitted gap has a>=800 and length<=3; it cannot
        # contribute at any of these x>=1/4. This is a finite completeness bound.
        assert all(a < 3/x for a, b in active)
        assert 3/x < 800
        if x == F(1, 2):
            assert active == [(1, 4), (4, 7)]
        envelopes.append({"x": str(x), "rational_part": str(wanted),
                          "inherited_before_loss": str(inherited),
                          "log16_coefficient": str(-x),
                          "active_gaps": [list(p) for p in active]})

    # The root-agent strengthening truncates only inherited-prime loss at zero.
    log2_lower, log2_upper = log_two_interval()
    truncation_cases = []
    for x in (F(1, 4), F(1, 2), F(3, 4), F(1)):
        inherited = 4*sum(max(F(1, a)-(1+x)/b, 0) for a, b in gaps)
        inherited_lower = inherited - 4*x*log2_upper
        inherited_upper = inherited - 4*x*log2_lower
        if x < 1:
            assert inherited_lower > 0
            branch = "retain_inherited"
        else:
            assert inherited_upper < 0
            branch = "fresh_only"
        truncation_cases.append({"x": str(x), "branch": branch,
                                 "fresh_mass": str(6*x),
                                 "inherited_interval": [str(inherited_lower),
                                                        str(inherited_upper)]})

    # Raw pole enumeration is independent of the multiplier gap lists above.
    ends = [(127, 158), (191, 254), (257, 385), (311, 622)]
    orbit = [F(0)]
    for n in range(1, 623):
        orbit.append(16*orbit[-1]+F(4, 8*n-7)-F(2, 8*n-4)
                     -F(1, 8*n-3)-F(1, 8*n-2))
    prime_rows = []
    for n, t in ends:
        fresh = inherited = 0
        for p in S.primerange(7, 8*t):
            if p*p <= 8*t:
                continue
            born = [j for j in range(1, t+1)
                    if any((8*j-c) % p == 0 for c in (7, 4, 3, 2))]
            if not born:
                continue
            if born[0] > n and orbit[t].denominator % p == 0:
                assert (orbit[t]-orbit[n]).denominator % p == 0
                fresh += 1
            elif born[0] <= n and not any(j > n for j in born):
                if orbit[n].denominator % p == 0 and pow(16, t-n, p) != 1:
                    assert (orbit[t]-orbit[n]).denominator % p == 0
                    inherited += 1
        prime_rows.append({"n": n, "t": t, "fresh": fresh,
                           "inherited_no_injection": inherited})
    prime_checks = sum(row["fresh"]+row["inherited_no_injection"]
                       for row in prime_rows)
    assert prime_checks == 751
    return {
        "schema": "SUCC-leah-gamma-prime-v1",
        "base_commit": "db9fb4b84672050efa79b13377f1e73364598a14",
        "status": "PASS",
        "scope": "Exact finite algebra; no R0 or normality certificate",
        "symbolic_check_cases": symbolic_cases,
        "original_envelope_check_cases": len(envelopes),
        "root_strengthening_check_cases": len(truncation_cases),
        "direct_prime_implications": prime_checks,
        "envelopes": envelopes,
        "log2_interval": [str(log2_lower), str(log2_upper)],
        "root_strengthening": truncation_cases,
        "direct_prime_rows": prime_rows,
        "mutation_control": "Wrong first-pole coefficient rejected",
        "preregistration_scope": (
            "Symbolic and original envelope cases predeclared in GAMMA_PRIME.md; "
            "direct-prime checks and root strengthening are non-blind regression checks")
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="Refresh the deterministic checked JSON receipt")
    args = parser.parse_args()
    result = run()
    if args.write:
        RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    else:
        expected = json.loads(RECEIPT.read_text())
        assert result == expected, "Receipt differs; inspect before refreshing"
    print(json.dumps({"status": result["status"],
                      "symbolic_and_envelope_cases": (
                          result["symbolic_check_cases"]
                          + result["original_envelope_check_cases"]
                          + result["root_strengthening_check_cases"]),
                      "direct_prime_implications": result["direct_prime_implications"],
                      "receipt_action": "written" if args.write else "verified"},
                     sort_keys=True))


if __name__ == "__main__":
    main()
