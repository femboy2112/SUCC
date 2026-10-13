#!/usr/bin/env python3
"""Independent bounded rational witnesses for E37; no imported SUCC code."""
from fractions import Fraction as Q
from math import comb, factorial, prod
import json


def cutoff(n, q):
    return Q(factorial(n) * n**q, prod(q + j for j in range(n + 1)))


def expanded_mellin(n, q):
    return n**q * sum((Q((-1)**j * comb(n, j), q + j)
                      for j in range(n + 1)), Q(0))


def multiply(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def evaluate(a, x):
    out = Q(0)
    for c in reversed(a):
        out = out * x + c
    return out


def run():
    rows = []
    for n in range(2, 9):
        for q in range(1, 7):
            value = cutoff(n, q)
            ratio = cutoff(n, q + 1) / value
            defect = q - ratio
            assert value == expanded_mellin(n, q)
            assert ratio == Q(n * q, n + q + 1)
            assert defect == Q(q * (q + 1), n + q + 1) > 0
            target = factorial(q - 1)
            # 1-prod_j(1+j/N)^-1 <= sum_j j/N, proved in receipt.
            bound = Q(target * q * (q + 1), 2 * n)
            assert 0 < target - value <= bound
            rows.append({"N": n, "q": q, "mellin": str(value),
                         "ratio": str(ratio), "defect": str(defect),
                         "gamma_error": str(target - value),
                         "proven_error_bound": str(bound)})
    residues = []
    for n in range(2, 9):
        for m in range(n + 1):
            direct = Q(factorial(n), n**m *
                       prod(j - m for j in range(n + 1) if j != m))
            predicted = (-1)**m * Q(comb(n, m), n**m)
            assert direct == predicted
            residues.append({"N": n, "pole": -m, "residue": str(direct)})

    p = (Q(1),)
    nodes = (Q(0), Q(1), Q(2), Q(3), Q(4), Q(-1), Q(-2), Q(-3))
    for a in nodes:
        p = multiply(p, multiply((-a, Q(1)), (-a, Q(1))))
    dp = tuple(i * c for i, c in enumerate(p))[1:]
    for a in nodes:
        assert evaluate(p, a) == evaluate(dp, a) == 0
    for x in (Q(-5), Q(1, 4), Q(1, 2), Q(7, 3), Q(9)):
        assert evaluate(p, x) == evaluate(p, 1 - x)
    holdout = evaluate(p, Q(1, 4))
    assert holdout != 0
    off_line = (Q(3, 16), Q(-1), Q(1))
    assert evaluate(off_line, Q(1, 4)) == evaluate(off_line, Q(3, 4)) == 0
    assert evaluate(off_line, Q(1, 2)) == Q(-1, 16)

    source_controls = []
    for name, a2, a3, a6 in (("zeta", 1, 1, 1),
                            ("non_Euler_six_mutation", 1, 1, 2),
                            ("counterfeit_Euler_base_six", 0, 0, 1)):
        b6 = Q(a6) - Q(a2) * a3
        source_controls.append({"source": name, "a2": a2, "a3": a3,
                                "a6": a6, "connected_b6": str(b6),
                                "same_G2_at_1": str(cutoff(2, 1))})
    assert [r["connected_b6"] for r in source_controls] == ["0", "1", "1"]
    mutant_residues = [{"m": m, "residue_after_dividing_by_pi_power_m":
                       str(Q(2 * (-1)**m * 6**(2*m), factorial(m)))}
                      for m in range(1, 4)]
    return {"status": "TESTED_MODEL_EXACT_RATIONAL", "gamma_rows": rows,
            "finite_residues": residues,
            "sample_polynomial_coefficients_low_to_high": list(map(str, p)),
            "sample_nodes": list(map(str, nodes)),
            "sample_value_and_first_derivative": "all exactly zero",
            "fresh_holdout_at_1_over_4": str(holdout),
            "symmetric_off_line_root_polynomial": list(map(str, off_line)),
            "source_controls": source_controls, "mutant_residues": mutant_residues,
            "RH_proved": False, "completed_source_identified": False,
            "nontrivial_zeta_zero_inputs": False, "floating_point_used": False,
            "universal_analytic_proof_certified_by_script": False}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
