#!/usr/bin/env python3
"""Independent Gamma--Laguerre mode audit; no project-module imports.

The exact Fraction checks certify finite polynomial identities only. All
mpmath checks and CDF values are 50-digit, noninterval diagnostics. Analytic
tail bounds are derived in the companion theorem dossier, not from the scan.
No infinite numerical sum, pi-normality test, or physical interpretation is
used. Run directly; the only written artifact is the requested JSON receipt.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp


HERE = Path(__file__).resolve().parent
PRECISION = 50


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def decimal(value: object) -> str:
    return mp.nstr(value, 45)


def complex_json(value: mp.mpc) -> dict[str, str]:
    return {"real": decimal(mp.re(value)), "imag": decimal(mp.im(value))}


def laguerre_polynomial(degree: int, shape: mp.mpf, value: mp.mpf) -> mp.mpf:
    """Finite polynomial, avoiding mpmath's hypergeometric Laguerre evaluator."""
    return mp.fsum(
        (-1) ** j
        * mp.binomial(degree + shape - 1, degree - j)
        * value**j
        / math.factorial(j)
        for j in range(degree + 1)
    )


def basis(degree: int, shape: mp.mpf, value: mp.mpf) -> mp.mpf:
    return mp.sqrt(mp.factorial(degree) / mp.rf(shape, degree)) * laguerre_polynomial(
        degree, shape, value
    )


def gamma_weight(shape: mp.mpf, value: mp.mpf) -> mp.mpf:
    return value ** (shape - 1) * mp.exp(-value) / mp.gamma(shape)


def character(omega: mp.mpf, value: mp.mpf) -> mp.mpc:
    return mp.exp(1j * omega * mp.log(value))


def quadrature(function: object) -> object:
    return mp.quad(function, [0, 1, 4, mp.inf])


def direct_coefficient(shape: mp.mpf, omega: mp.mpf, degree: int) -> mp.mpc:
    return (
        mp.gamma(shape + 1j * omega)
        / mp.gamma(shape)
        * mp.rf(-1j * omega, degree)
        / mp.sqrt(mp.factorial(degree) * mp.rf(shape, degree))
    )


def finite_weights(omega: mp.mpf, cutoff: int) -> list[mp.mpf]:
    """Finite recurrence, separate from the direct Pochhammer coefficient path."""
    beta = omega * omega
    weights = [abs(mp.gamma(2 + 1j * omega)) ** 2]
    for degree in range(cutoff):
        weights.append(
            weights[-1] * (degree * degree + beta) / ((degree + 1) * (degree + 2))
        )
    return weights


def tail_bounds(omega: Fraction, cutoff: int) -> tuple[Fraction, Fraction]:
    """Exact rational bounds for the analytically proved omitted mode energy."""
    if cutoff < 1:
        raise ValueError("The rational tail bounds require cutoff >= 1")
    beta = omega * omega
    constant = beta * (1 + beta)
    lower = constant * max(Fraction(0), 1 - beta / cutoff) / (
        2 * (cutoff + 1) * (cutoff + 2)
    )
    upper = min(
        Fraction(1), beta / (cutoff + 1), constant / (2 * cutoff * (cutoff + 1))
    )
    return lower, upper


class Audit:
    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()
        self.failures: list[dict[str, str]] = []

    def check(self, category: str, label: str, passed: bool, detail: str = "") -> None:
        self.counts[category] += 1
        if not passed:
            self.failures.append({"category": category, "label": label, "detail": detail})

    def close(self, category: str, label: str, actual: object, expected: object) -> mp.mpf:
        error = abs(actual - expected)
        tolerance = mp.mpf("1e-36") * max(1, abs(expected))
        self.check(category, label, error <= tolerance, decimal(error))
        return error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "receipts" / "mode_audit.json")
    args = parser.parse_args()
    mp.mp.dps = PRECISION
    started = time.monotonic()
    audit = Audit()

    # Exact Gamma(2) polynomial orthogonality, with no transcendental arithmetic.
    polynomial_rows = [
        tuple(Fraction((-1) ** j * math.comb(m + 1, j + 1), math.factorial(j)) for j in range(m + 1))
        for m in range(9)
    ]
    for left in range(9):
        for right in range(9):
            integral = sum(
                (u * v * math.factorial(j + k + 1)
                 for j, u in enumerate(polynomial_rows[left])
                 for k, v in enumerate(polynomial_rows[right])),
                Fraction(0),
            )
            expected = Fraction(left + 1 if left == right else 0)
            audit.check("exact_polynomial_orthogonality", f"{left},{right}", integral == expected)

    coefficient_rows = []
    quadrature_values: dict[tuple[str, str, int], mp.mpc] = {}
    cases = [(Fraction(2), Fraction(0)), (Fraction(2), Fraction(1, 3)),
             (Fraction(2), Fraction(1)), (Fraction(2), Fraction(3)),
             (Fraction(7, 2), Fraction(-3, 4))]
    for shape_q, omega_q in cases:
        shape, omega = mp_fraction(shape_q), mp_fraction(omega_q)
        for degree in range(6):
            value = quadrature(
                lambda t: character(omega, t) * basis(degree, shape, t) * gamma_weight(shape, t)
            )
            expected = direct_coefficient(shape, omega, degree)
            error = audit.close("coefficient_quadrature", f"{shape_q},{omega_q},{degree}", value, expected)
            key = (str(shape_q), str(omega_q), degree)
            quadrature_values[key] = value
            coefficient_rows.append({
                "shape": str(shape_q), "omega": str(omega_q), "degree": degree,
                "quadrature": complex_json(value), "closed_form": complex_json(expected),
                "absolute_error": decimal(error),
            })

    # Reflection identity and finite Euler products provide two different
    # checks on the vacuum weight. Product endpoints are exact Fractions;
    # comparison to the Gamma value is still a noninterval numeric diagnostic.
    product_rows = []
    for omega_q in [Fraction(0), Fraction(1, 4), Fraction(1), Fraction(3, 2), Fraction(5)]:
        omega = mp_fraction(omega_q)
        vacuum = abs(mp.gamma(2 + 1j * omega)) ** 2
        reflection = (1 + omega**2) * mp.pi * omega / mp.sinh(mp.pi * omega) if omega else mp.mpf(1)
        audit.close("vacuum_reflection", str(omega_q), vacuum, reflection)
        for last_factor in [32, 64, 256]:
            finite_product = Fraction(1)
            for j in range(2, last_factor + 1):
                finite_product /= 1 + omega_q**2 / (j * j)
            lower = finite_product * max(Fraction(0), 1 - omega_q**2 / last_factor)
            upper = finite_product
            audit.check("gamma_product_enclosure", f"lower:{omega_q},{last_factor}",
                        vacuum >= mp_fraction(lower) - mp.mpf("1e-40"))
            audit.check("gamma_product_enclosure", f"upper:{omega_q},{last_factor}",
                        vacuum <= mp_fraction(upper) + mp.mpf("1e-40"))
            product_rows.append({"omega": str(omega_q), "last_factor": last_factor,
                                 "lower": str(lower), "upper": str(upper),
                                 "gamma_value": decimal(vacuum)})

    tail_rows = []
    for omega_q in [Fraction(0), Fraction(1, 4), Fraction(1), Fraction(3, 2), Fraction(5)]:
        omega = mp_fraction(omega_q)
        for cutoff in [1, 2, 5, 17, 50, 200, 1000]:
            weights = finite_weights(omega, cutoff)
            captured = mp.fsum(weights)
            omitted = 1 - captured
            truncated_mean = mp.fsum(m * p for m, p in enumerate(weights))
            lower, upper = tail_bounds(omega_q, cutoff)
            audit.check("finite_tail_enclosure", f"lower:{omega_q},{cutoff}",
                        omitted >= mp_fraction(lower) - mp.mpf("1e-38"))
            audit.check("finite_tail_enclosure", f"upper:{omega_q},{cutoff}",
                        omitted <= mp_fraction(upper) + mp.mpf("1e-38"))
            audit.check("finite_degree_mean", f"{omega_q},{cutoff}",
                        -mp.mpf("1e-38") <= truncated_mean <= omega**2 + mp.mpf("1e-38"))
            tail_rows.append({"omega": str(omega_q), "cutoff": cutoff,
                              "captured_energy": decimal(captured), "omitted_energy": decimal(omitted),
                              "rational_lower": str(lower), "rational_upper": str(upper),
                              "truncated_mean_degree": decimal(truncated_mean), "full_mean_degree": str(omega_q**2)})

    direct_weight_rows = []
    for omega_q in [Fraction(1, 4), Fraction(1), Fraction(3, 2), Fraction(5)]:
        omega = mp_fraction(omega_q)
        constant = omega**2 * (1 + omega**2)
        weights = finite_weights(omega, 19)
        for degree in [1, 2, 3, 5, 11, 19]:
            coefficient_weight = abs(direct_coefficient(mp.mpf(2), omega, degree)) ** 2
            gamma_ratio_weight = constant * abs(mp.gamma(degree + 1j * omega) / mp.gamma(degree)) ** 2 / (
                degree * degree * (degree + 1)
            )
            error_one = audit.close("direct_weight_identity", f"ratio:{omega_q},{degree}", coefficient_weight, gamma_ratio_weight)
            error_two = audit.close("direct_weight_identity", f"recurrence:{omega_q},{degree}", coefficient_weight, weights[degree])
            direct_weight_rows.append({"omega": str(omega_q), "degree": degree,
                                       "coefficient_weight": decimal(coefficient_weight),
                                       "gamma_ratio_error": decimal(error_one), "recurrence_error": decimal(error_two)})

    reconstruction_rows = []
    for cutoff in [0, 1, 5]:
        omega = mp.mpf(1)
        coefficients = [direct_coefficient(mp.mpf(2), omega, m) for m in range(cutoff + 1)]
        norm_error_squared = quadrature(
            lambda t: abs(character(omega, t) - mp.fsum(coefficients[m] * basis(m, mp.mpf(2), t)
                                                     for m in range(cutoff + 1))) ** 2 * t * mp.exp(-t)
        )
        omitted = 1 - mp.fsum(abs(c) ** 2 for c in coefficients)
        error = audit.close("direct_reconstruction_norm", str(cutoff), norm_error_squared, omitted)
        reconstruction_rows.append({"omega": "1", "cutoff": cutoff,
                                    "direct_squared_norm": decimal(norm_error_squared),
                                    "coefficient_tail": decimal(omitted), "absolute_error": decimal(error)})

    # This law is deliberately a transparent finite-atom control, not an
    # assertion that authentic BBP's residual label has this distribution.
    atom_labels = [Fraction(0), Fraction(1), Fraction(4)]
    atom_probabilities = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
    audit.check("exact_control_law", "probability_mass", sum(atom_probabilities) == 1)
    tensor_rows = []
    for omega_q in [Fraction(0), Fraction(1, 2), Fraction(2)]:
        omega = mp_fraction(omega_q)
        phi = mp.gamma(2 + 1j * omega)
        phi_integral = quadrature(lambda t: character(omega, t) * t * mp.exp(-t))
        gamma_residual = quadrature(lambda t: abs(character(omega, t) - phi) ** 2 * t * mp.exp(-t))
        audit.close("tensor_gamma_projection", f"coefficient:{omega_q}", phi_integral, phi)
        audit.close("tensor_gamma_projection", f"residual:{omega_q}", gamma_residual, 1 - abs(phi) ** 2)
        for scale_q in [Fraction(1), Fraction(3), Fraction(17)]:
            scale = mp_fraction(scale_q)
            labels = [mp.exp(1j * omega * mp.log(scale / (scale + mp_fraction(b)))) for b in atom_labels]
            psi = mp.fsum(mp_fraction(p) * v for p, v in zip(atom_probabilities, labels))
            source_residual = mp.fsum(mp_fraction(p) * abs(phi * (v - psi)) ** 2
                                     for p, v in zip(atom_probabilities, labels))
            scalar_energy = abs(phi_integral * psi) ** 2
            total = gamma_residual + source_residual + scalar_energy
            audit.close("tensor_energy", f"total:{scale_q},{omega_q}", total, mp.mpf(1))
            audit.close("tensor_energy", f"source:{scale_q},{omega_q}", source_residual, abs(phi) ** 2 * (1 - abs(psi) ** 2))
            inner_source_constant = mp.fsum(mp_fraction(p) * phi * (v - psi) * mp.conj(phi * psi)
                                           for p, v in zip(atom_probabilities, labels))
            inner_gamma_source = (phi_integral - phi) * mp.fsum(
                mp_fraction(p) * v * mp.conj(phi * (v - psi)) for p, v in zip(atom_probabilities, labels)
            )
            audit.close("tensor_orthogonality", f"source_constant:{scale_q},{omega_q}", inner_source_constant, 0)
            audit.close("tensor_orthogonality", f"gamma_source:{scale_q},{omega_q}", inner_gamma_source, 0)
            tensor_rows.append({"scale": str(scale_q), "omega": str(omega_q),
                                "gamma_residual_energy": decimal(gamma_residual),
                                "source_residual_energy": decimal(source_residual),
                                "scalar_energy": decimal(scalar_energy), "total": decimal(total),
                                "source_constant_inner_product": complex_json(inner_source_constant),
                                "gamma_source_inner_product": complex_json(inner_gamma_source)})

    # Diagnostics deliberately preserve every signed error, including possible
    # nonmonotone convergence. No asymptotic error threshold is asserted here.
    scaling_rows = []
    for omega_integer in [5, 10, 20, 40, 80]:
        omega = mp.mpf(omega_integer)
        beta = omega_integer * omega_integer
        levels = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]
        cutoffs = {int(level * beta): level for level in levels}
        weights = finite_weights(omega, max(cutoffs))
        captured = mp.mpf(0)
        previous = mp.mpf(0)
        for degree, weight in enumerate(weights):
            captured += weight
            if degree not in cutoffs:
                continue
            level_q = cutoffs[degree]
            level = mp_fraction(level_q)
            limit = (1 + 1 / level) * mp.exp(-1 / level)
            audit.check("cdf_diagnostic_range", f"{omega_integer},{level_q}", 0 <= captured <= 1 + mp.mpf("1e-38"))
            audit.check("cdf_diagnostic_order", f"{omega_integer},{level_q}", captured >= previous)
            previous = captured
            scaling_rows.append({"omega": omega_integer, "scaled_cutoff": str(level_q),
                                 "integer_cutoff": degree, "finite_cdf": decimal(captured),
                                 "inverse_gamma_limit_cdf": decimal(limit),
                                 "signed_error": decimal(captured - limit), "absolute_error": decimal(abs(captured - limit))})

    mutations = []
    correct = quadrature_values[("2", "1", 1)]
    reversed_sign = mp.gamma(2 + 1j) * mp.rf(1j, 1) / mp.sqrt(2)
    gap = abs(correct - reversed_sign)
    audit.check("mutation_detection", "reversed_coefficient_sign", gap > mp.mpf("0.5"))
    mutations.append({"name": "reversed_coefficient_sign", "gap": decimal(gap), "detected": bool(gap > mp.mpf("0.5"))})

    correct = quadrature_values[("2", "1", 3)]
    omitted_factorial = mp.gamma(2 + 1j) * mp.rf(-1j, 3) / mp.sqrt(mp.rf(2, 3))
    gap = abs(correct - omitted_factorial)
    audit.check("mutation_detection", "omitted_factorial", gap > mp.mpf("0.1"))
    mutations.append({"name": "omitted_factorial", "gap": decimal(gap), "detected": bool(gap > mp.mpf("0.1"))})

    correct = quadrature_values[("2", "1", 0)]
    wrong_shape = mp.gamma(1 + 1j)
    gap = abs(correct - wrong_shape)
    audit.check("mutation_detection", "shape_one_in_place_of_two", gap > mp.mpf("0.1"))
    mutations.append({"name": "shape_one_in_place_of_two", "gap": decimal(gap), "detected": bool(gap > mp.mpf("0.1"))})

    retained = mp.fsum(finite_weights(mp.mpf(3), 1))
    renormalized_sum = mp.fsum(p / retained for p in finite_weights(mp.mpf(3), 1))
    hidden_loss = 1 - retained
    audit.close("mutation_calibration", "renormalized_prefix_sums_to_one", renormalized_sum, 1)
    audit.check("mutation_detection", "renormalizing_truncation_masks_loss", hidden_loss > mp.mpf("0.5"))
    mutations.append({"name": "renormalizing_truncation_masks_loss", "omega": "3", "cutoff": 1,
                      "true_retained_energy": decimal(retained), "renormalized_reported_energy": decimal(renormalized_sum),
                      "hidden_omitted_energy": decimal(hidden_loss), "detected": bool(hidden_loss > mp.mpf("0.5"))})

    receipt = {
        "schema": "succ.gamma_phase_disintegration.independent_mode_audit.v1",
        "status": "PASS" if not audit.failures else "FAIL",
        "scope": "Exact finite rational identities plus noninterval numerical diagnostics; no universal inference from finite tests.",
        "numerical_diagnostics_are_interval_certificates": False,
        "project_module_imports": [],
        "infinite_numeric_summation_used": False,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(), "mpmath_version": mp.__version__, "decimal_precision": PRECISION,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "assertions": sum(audit.counts.values()), "assertions_by_category": dict(sorted(audit.counts.items())),
        "failures": audit.failures,
        "exact_polynomial_scope": "All 81 pairs of L_m^1,L_n^1 for m,n=0..8; integral weight t*exp(-t).",
        "coefficient_quadrature": coefficient_rows, "gamma_product_enclosures": product_rows,
        "finite_tail_enclosures": tail_rows, "direct_weight_identities": direct_weight_rows,
        "direct_reconstruction_norms": reconstruction_rows,
        "tensor_control": {"source_status": "Synthetic finite-atom control; not authentic BBP residual law.",
                           "atoms": [str(b) for b in atom_labels], "probabilities": [str(p) for p in atom_probabilities],
                           "rows": tensor_rows},
        "actual_bbp_residual_joint_audit": "Not run in this independent mode script; no temporal joining asserted.",
        "double_scaling_diagnostics": scaling_rows,
        "double_scaling_validation_rule": "Record signed errors; check finite CDF range/order only. No monotone error or finite asymptotic threshold claimed.",
        "mutations": mutations,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "assertions": receipt["assertions"],
                      "assertions_by_category": receipt["assertions_by_category"],
                      "failures": audit.failures, "receipt": str(args.output),
                      "elapsed_seconds": receipt["elapsed_seconds"]}, indent=2))
    return 1 if audit.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
