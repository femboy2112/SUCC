"""Independent high-precision numerical boundary-Gram oracle.

This uses mpmath's pi directly, never the rational BBP certificate backend.
The output is NUMERICAL OBSERVATION, not a rigorous enclosure or proof.
The finite cases were declared before this oracle was executed.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp


def decimal(value):
    return mp.nstr(value, 65)


def gram_case(start, degree, source="pi_over_16"):
    precision = max(160, 2 * (2 * start + degree) + 80)
    if source == "near_rational_irrational":
        # Resolve very small singular values of the intentionally clustered
        # columns; ordinary working precision would report noise near zero.
        precision = max(700, precision)
    with mp.workdps(precision):
        if source == "pi_over_16":
            x = mp.pi / 16
        elif source == "completed_zero":
            x = mp.mpf(0)
        elif source == "fixed_1_over_15":
            x = mp.mpf(1) / 15
        elif source == "period_two_1_over_17":
            x = mp.mpf(1) / 17
        elif source == "near_rational_irrational":
            x = mp.mpf(1) / 15 + mp.sqrt(2) * mp.power(16, -(2 * start + degree + 40))
        else:
            raise ValueError(source)

        # Direct orbit values are constructed independently at each index.
        # In particular, no floating recurrence is repeatedly amplified.
        phases = [mp.frac(mp.power(16, n) * x)
                  for n in range(start, 2 * start + degree)]
        values = [mp.exp(2j * mp.pi * t) for t in phases]
        matrix = mp.matrix(degree + 1)
        for j in range(degree + 1):
            matrix[j, j] = 1
            for k in range(j + 1, degree + 1):
                entry = mp.fsum(mp.conj(values[n + j]) * values[n + k]
                                for n in range(start)) / start
                matrix[j, k] = entry
                matrix[k, j] = mp.conj(entry)

        eigenvalues = mp.eighe(matrix, eigvals_only=True)
        modulus_margin = min(1 - mp.fsum(abs(matrix[j, k])
                                        for k in range(degree + 1) if k != j)
                             for j in range(degree + 1))
        box_l1_margin = min(1 - mp.fsum(abs(mp.re(matrix[j, k])) + abs(mp.im(matrix[j, k]))
                                       for k in range(degree + 1) if k != j)
                            for j in range(degree + 1))
        # Differential check: the Hankel Gram equals a Weyl-difference sum.
        differential = mp.mpf(0)
        for j in range(degree + 1):
            for k in range(j + 1, degree + 1):
                frequency = 16 ** k - 16 ** j
                direct = mp.fsum(mp.exp(2j * mp.pi * mp.frac(frequency * mp.power(16, n) * x))
                                 for n in range(start, 2 * start)) / start
                differential = max(differential, abs(matrix[j, k] - direct))
        assert differential < mp.mpf("1e-65")

        exact_rank = None
        if source in ("completed_zero", "fixed_1_over_15"):
            exact_rank = 1
        elif source == "period_two_1_over_17":
            exact_rank = min(2, degree + 1)
        return {
            "start": start,
            "length": start,
            "degree": degree,
            "source": source,
            "decimal_precision": precision,
            "eigenvalues_numerical": [decimal(v) for v in eigenvalues],
            "gershgorin_modulus_lower_numerical": decimal(modulus_margin),
            "gershgorin_box_l1_lower_numerical": decimal(box_l1_margin),
            "gram": [[{"real": decimal(mp.re(matrix[j, k])),
                        "imag": decimal(mp.im(matrix[j, k]))}
                       for k in range(degree + 1)] for j in range(degree + 1)],
            "differential_error": decimal(differential),
            "control_rank_from_paper_argument": exact_rank,
        }


def main():
    cases = [gram_case(a, d) for a in (17, 37, 73) for d in range(1, 5)]
    cases.append(gram_case(109, 4))
    controls = [gram_case(17, 4, source) for source in (
        "completed_zero", "fixed_1_over_15", "period_two_1_over_17",
        "near_rational_irrational")]
    receipt = {
        "status": "NUMERICAL OBSERVATION ONLY",
        "scope": "Finite high-precision cross-check, not interval certification or an asymptotic estimate",
        "implementation": "mpmath direct pi, direct orbit powers, Hermitian eigenvalue solver",
        "provenance": "Separate implementation within the same model family; no external independence claim",
        "preregistered_shell_starts": [17, 37, 73],
        "preregistered_holdout": {"start": 109, "degree": 4},
        "cases": cases,
        "controls": controls,
    }
    target = Path(__file__).with_name("receipts") / "oracle.json"
    target.write_text(json.dumps(receipt, indent=2) + "\n")
    for case in cases + controls:
        print(case["source"], "A=", case["start"], "d=", case["degree"],
              "lambda_min=", case["eigenvalues_numerical"][0],
              "Gershgorin=", case["gershgorin_modulus_lower_numerical"])
    print("Wrote", target)


if __name__ == "__main__":
    main()
