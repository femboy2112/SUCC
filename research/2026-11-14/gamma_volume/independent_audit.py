#!/usr/bin/env python3
"""Independent, bounded Gamma-volume audit; no production-module imports.

Run from any directory with Python, SymPy and mpmath installed:
    python research/2026-11-14/gamma_volume/independent_audit.py

Exact checks reconstruct the positive source from the original signed polynomial
P=4-2*x**3-x**4-x**5.  The geometric expansion of 16*P/(16-x**8)
gives the direct four-pole BBP series.  Its positive tail is bounded above by
64/[15*(8*N+1)*16**N], since each bracket is at most 4/(8*k+1).
This rational enclosure, rather than a floating-point value of pi, certifies
the finite Hankel determinant signs.

Numerical quadratures and fractional-coefficient holdouts are diagnostics only.
They do not prove general semigroup, conjugation, or transform identities.
The current production implementation and its tests were not read to select
the numerical parameters.  Mathematical-source overlap remains explicit:
method separation here means separate code and decompositions, not a new
independent mathematical source or independent model family.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import time

import mpmath as mp
import sympy as sp


DPS = 70
TOLERANCE = "1e-32"
MUTATION_FLOOR = "1e-8"
BBP_TERMS = 24
MAX_MOMENT = 8
MAX_HANKEL = 5
MAX_GRADE = 12


def rational(value: sp.Expr | int) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def mpq(value: str | Fraction) -> mp.mpf:
    value = Fraction(value)
    return mp.mpf(value.numerator) / value.denominator


def number(value: mp.mpf) -> str:
    return mp.nstr(value, 55)


def complex_number(value: mp.mpc) -> dict[str, str]:
    return {"real": number(mp.re(value)), "imag": number(mp.im(value))}


def polynomial_product(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    """Ascending coefficients; deliberately separate from SymPy algebra."""
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def fraction_determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Exact elimination, independently checking SymPy's affine determinants."""
    matrix = [row[:] for row in matrix]
    result = Fraction(1)
    for col in range(len(matrix)):
        pivot = next((row for row in range(col, len(matrix)) if matrix[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            result = -result
        entry = matrix[col][col]
        result *= entry
        for row in range(col + 1, len(matrix)):
            multiplier = matrix[row][col] / entry
            for index in range(col + 1, len(matrix)):
                matrix[row][index] -= multiplier * matrix[col][index]
            matrix[row][col] = Fraction(0)
    return result


class Audit:
    def __init__(self) -> None:
        self.checks: list[dict[str, object]] = []

    def exact(self, name: str, condition: bool) -> None:
        passed = bool(condition)
        self.checks.append({"name": name, "kind": "exact", "passed": passed})
        if not passed:
            raise AssertionError(name)

    def close(self, name: str, left: mp.mpf | mp.mpc, right: mp.mpf | mp.mpc) -> mp.mpf:
        error = abs(left - right)
        passed = bool(mp.isfinite(error) and error <= mp.mpf(TOLERANCE))
        self.checks.append({
            "name": name, "kind": "numerical_identity", "passed": passed,
            "absolute_error": number(error), "tolerance": TOLERANCE,
        })
        if not passed:
            raise AssertionError(f"{name}: absolute error {number(error)}")
        return error

    def separates(self, name: str, correct: mp.mpf, mutation: mp.mpf) -> mp.mpf:
        gap = abs(correct - mutation)
        passed = bool(mp.isfinite(gap) and gap >= mp.mpf(MUTATION_FLOOR))
        self.checks.append({
            "name": name, "kind": "mutation_separation", "passed": passed,
            "absolute_gap": number(gap), "required_gap": MUTATION_FLOOR,
        })
        if not passed:
            raise AssertionError(f"{name}: mutation gap {number(gap)}")
        return gap


def exact_source_audit(audit: Audit) -> dict[str, object]:
    x = sp.Symbol("x", real=True)
    pi_parameter = sp.Symbol("p")
    source_p = 4 - 2*x**3 - x**4 - x**5
    source_r = source_p / (16 - x**8)
    denominator = (2 - x**2) * (x**2 - 2*x + 2)
    u = x - x**2 / 2
    v = x**2 / 2
    a = sp.expand((1 - u) * (1 - v))
    audit.exact("signed_source_positive_factorization", sp.expand(
        source_p - (1-x)*(x*x+2)*(x*x+2*x+2)) == 0)
    audit.exact("original_source_cancellation", sp.cancel(
        source_r - (1-x)/denominator) == 0)
    audit.exact("source_a_equals_denominator_over_four", sp.expand(a-denominator/4) == 0)

    partial_fractions = -x/(4*(2-x*x)) + (2-x)/(4*(x*x-2*x+2))
    primitive = 2*sp.log(2-x*x) - 2*sp.log(x*x-2*x+2) + 4*sp.atan(x-1)
    audit.exact("partial_fraction_identity", sp.cancel(source_r-partial_fractions) == 0)
    audit.exact("elementary_antiderivative", sp.simplify(sp.diff(primitive, x)-16*source_r) == 0)
    integral_value = sp.simplify(primitive.subs(x, 1)-primitive.subs(x, 0))
    audit.exact("exact_pi_integral", integral_value == sp.pi)

    # Independent rational-polynomial route from (1-u)(1-v), not SymPy output.
    a_fraction = polynomial_product(
        [Fraction(1), Fraction(-1), Fraction(1, 2)],
        [Fraction(1), Fraction(0), Fraction(-1, 2)],
    )
    audit.exact("two_polynomial_routes_for_a", all(
        rational(sp.expand(a).coeff(x, k)) == c for k, c in enumerate(a_fraction)))
    power = [Fraction(1)]
    moments: dict[int, Fraction] = {}
    moment_rows = []
    for n in range(1, MAX_MOMENT + 1):
        integrand = sp.cancel(16*source_r*a**n)
        sympy_value = rational(sp.integrate(integrand, (x, 0, 1)))
        coefficients = polynomial_product([Fraction(4), Fraction(-4)], power)
        fraction_value = sum((c/Fraction(k+1) for k, c in enumerate(coefficients)), Fraction(0))
        audit.exact(f"moment_c{n}_two_exact_routes", sympy_value == fraction_value)
        moments[n] = sympy_value
        moment_rows.append({
            "n": n, "c_n": str(sympy_value), "moment_m_n": f"({sympy_value})/pi",
            "polynomial_integrand": str(sp.expand(integrand)),
        })
        power = polynomial_product(power, a_fraction)
    audit.exact("moment_c1_anchor", moments[1] == 2)
    audit.exact("moment_c2_anchor", moments[2] == Fraction(7, 5))

    bbp_terms = []
    for k in range(BBP_TERMS):
        bracket = (Fraction(4, 8*k+1) - Fraction(2, 8*k+4)
                   - Fraction(1, 8*k+5) - Fraction(1, 8*k+6))
        audit.exact(f"bbp_retained_bracket_positive_{k}", bracket > 0)
        bbp_terms.append(bracket/Fraction(16**k))
    pi_lower = sum(bbp_terms, Fraction(0))
    tail_bound = Fraction(64, 15*(8*BBP_TERMS+1)*16**BBP_TERMS)
    pi_upper = pi_lower + tail_bound
    audit.exact("bbp_enclosure_has_positive_width", 0 < pi_lower < pi_upper)

    hankel_rows = []
    for dimension in range(1, MAX_HANKEL + 1):
        # pi*H has pi only at (0,0), because m_0=1 and m_n=c_n/pi for n>0.
        matrix = sp.Matrix(dimension, dimension, lambda i, j:
                           pi_parameter if i+j == 0 else sp.Rational(moments[i+j]))
        determinant = sp.Poly(sp.expand(matrix.det(method="domain-ge")), pi_parameter)
        audit.exact(f"hankel_{dimension}_affine_numerator", determinant.degree() <= 1)
        slope = rational(determinant.nth(1))
        intercept = rational(determinant.nth(0))
        endpoint_values = []
        for label, endpoint in (("lower", pi_lower), ("upper", pi_upper)):
            plain_matrix = [[endpoint if i+j == 0 else moments[i+j]
                             for j in range(dimension)] for i in range(dimension)]
            independent = fraction_determinant(plain_matrix)
            affine = slope*endpoint + intercept
            audit.exact(f"hankel_{dimension}_{label}_independent_determinant", independent == affine)
            endpoint_values.append(affine)
        numerator_lower = min(endpoint_values)
        numerator_upper = max(endpoint_values)
        audit.exact(f"hankel_{dimension}_strict_positive_sign", numerator_lower > 0)
        hankel_rows.append({
            "dimension": dimension,
            "determinant_formula": "(slope*pi+intercept)/pi**dimension",
            "slope": str(slope), "intercept": str(intercept),
            "numerator_lower": str(numerator_lower), "numerator_upper": str(numerator_upper),
            "determinant_lower": str(numerator_lower/pi_upper**dimension),
            "determinant_upper": str(numerator_upper/pi_lower**dimension),
        })

    variance = sp.factor(sp.Rational(moments[2])/pi_parameter
                         - (sp.Rational(moments[1])/pi_parameter)**2)
    audit.exact("source_variance_formula", sp.cancel(
        variance-(7*pi_parameter-20)/(5*pi_parameter**2)) == 0)
    variance_lower = (7*pi_lower-20)/(5*pi_upper*pi_upper)
    audit.exact("source_variance_strict_positive_from_bbp", variance_lower > 0)
    fixed_x = Fraction(5, 13)
    fixed_a = sum((coefficient*fixed_x**i for i, coefficient in enumerate(a_fraction)), Fraction(0))
    fixed_covariance = fixed_a**2 - fixed_a*fixed_a
    audit.exact("fixed_latent_zero_covariance", fixed_covariance == 0)
    for dimension in range(2, MAX_HANKEL+1):
        fixed_hankel = [[fixed_a**(i+j) for j in range(dimension)] for i in range(dimension)]
        audit.exact(f"fixed_latent_hankel_{dimension}_zero", fraction_determinant(fixed_hankel) == 0)

    return {
        "status": "EXACT_FINITE_SYMBOLIC_AND_RATIONAL",
        "source_polynomial": str(source_p), "source_original": str(source_r),
        "source_cancelled": str(sp.cancel(source_r)), "u": str(u), "v": str(v), "a": str(a),
        "partial_fractions": str(partial_fractions), "antiderivative_of_16R": str(primitive),
        "integral_16R_0_1": str(integral_value),
        "moments": moment_rows,
        "pi_enclosure": {
            "method": "direct four-pole BBP sum; positive tail bounded by a geometric majorant",
            "terms": BBP_TERMS, "retained_terms": [str(term) for term in bbp_terms],
            "lower": str(pi_lower), "upper": str(pi_upper), "width": str(tail_bound),
            "tail_bound_formula": "64/(15*(8*N+1)*16**N)",
            "floating_pi_used_for_signs": False,
        },
        "hankel": hankel_rows,
        "source_covariance": {"formula": str(variance), "strict_positive_lower": str(variance_lower)},
        "fixed_latent_control": {"x": str(fixed_x), "a": str(fixed_a), "covariance": str(fixed_covariance)},
    }


def conditional_coefficients(x: mp.mpf, depth: mp.mpf, maximum: int) -> list[mp.mpf]:
    if depth == 0:
        return [mp.mpf(1)] + [mp.mpf(0)]*maximum
    u, v = x-x*x/2, x*x/2
    normalizer = ((1-u)*(1-v))**depth
    return [normalizer*mp.fsum(
        mp.rf(depth, j)*mp.rf(depth, k-j)*u**j*v**(k-j)
        /(mp.factorial(j)*mp.factorial(k-j)) for j in range(k+1)
    ) for k in range(maximum+1)]


def fractional_holdouts(audit: Audit) -> dict[str, object]:
    parameters = [
        ("2/7", "3/7", "5/9"), ("5/11", "9/8", "7/10"),
        ("17/19", "11/6", "4/5"), ("23/29", "13/11", "17/13"),
    ]
    rows = []
    for case, (x_text, alpha_text, beta_text) in enumerate(parameters):
        x, alpha, beta = map(mpq, (x_text, alpha_text, beta_text))
        left = conditional_coefficients(x, alpha, MAX_GRADE)
        right = conditional_coefficients(x, beta, MAX_GRADE)
        target = conditional_coefficients(x, alpha+beta, MAX_GRADE)
        product = [mp.fsum(left[j]*right[k-j] for j in range(k+1)) for k in range(MAX_GRADE+1)]
        errors = [audit.close(f"fractional_case_{case}_grade_{k}", product[k], target[k])
                  for k in range(MAX_GRADE+1)]
        rows.append({
            "x": x_text, "alpha": alpha_text, "beta": beta_text,
            "grades": [0, MAX_GRADE], "convolved_coefficients": [number(q) for q in product],
            "direct_sum_depth_coefficients": [number(q) for q in target],
            "max_absolute_error": number(max(errors)),
        })
    for label, x, alpha in (("zero_depth", mpq("11/17"), mp.mpf(0)),
                             ("zero_x", mp.mpf(0), mpq("3/7"))):
        coefficients = conditional_coefficients(x, alpha, MAX_GRADE)
        for k, value in enumerate(coefficients):
            audit.close(f"fractional_{label}_{k}", value, mp.mpf(int(k == 0)))
    return {"status": "NUMERICAL_DIAGNOSTIC_ONLY", "cases": rows,
            "null_controls": ["zero depth gives delta_0", "x=0 gives delta_0"]}


def direct_tempered(alpha: mp.mpf, rate: mp.mpf, origin: mp.mpf, end: mp.mpf, function) -> mp.mpf:
    """Direct kernel, regularized by delay=(end-origin)*r**(1/alpha)."""
    gap = end-origin
    return gap**alpha/mp.gamma(alpha+1)*mp.quad(
        lambda r: mp.exp(-rate*gap*r**(1/alpha))*function(end-gap*r**(1/alpha)), [0, 1])


def conjugated_tempered(alpha: mp.mpf, rate: mp.mpf, origin: mp.mpf,
                       end: mp.mpf, function, outer_sign: int = -1) -> mp.mpf:
    """Untempered integral of exp(rate*y)*f(y), then an outer multiplier."""
    gap = end-origin
    integral = mp.quad(lambda s: s**(alpha-1)*mp.exp(rate*(end-gap*s))*function(end-gap*s),
                       [0, mp.mpf("0.25"), 1])
    return mp.exp(outer_sign*rate*end)*gap**alpha/mp.gamma(alpha)*integral


def tempered_holdouts(audit: Audit) -> dict[str, object]:
    parameters = [
        ("3/5", "2/5", "-7/5", "9/7"),
        ("7/4", "7/6", "3/8", "11/10"),
        ("11/8", "5/7", "5/3", "4/9"),
    ]
    function = lambda y: 1+y*y/5+mp.sin(y)/7
    rows = []
    for case, (alpha_text, rate_text, origin_text, gap_text) in enumerate(parameters):
        alpha, rate, origin, gap = map(mpq, (alpha_text, rate_text, origin_text, gap_text))
        end = origin+gap
        direct = direct_tempered(alpha, rate, origin, end, function)
        conjugated = conjugated_tempered(alpha, rate, origin, end, function)
        error = audit.close(f"tempered_case_{case}_conjugation", direct, conjugated)
        constant = direct_tempered(alpha, rate, origin, end, lambda y: mp.mpf(1))
        constant_reference = mp.gammainc(alpha, 0, rate*gap)/(rate**alpha*mp.gamma(alpha))
        audit.close(f"tempered_case_{case}_constant", constant, constant_reference)
        untempered = direct_tempered(alpha, mp.mpf(0), origin, end, lambda y: mp.mpf(1))
        audit.close(f"tempered_case_{case}_untempered_volume", untempered, gap**alpha/mp.gamma(alpha+1))
        wrong_sign = conjugated_tempered(alpha, rate, origin, end, function, outer_sign=1)
        sign_gap = audit.separates(f"tempered_case_{case}_wrong_outer_sign", direct, wrong_sign)
        wrong_power = mp.quad(lambda delay: delay**alpha*mp.exp(-rate*delay)*function(end-delay),
                              [0, gap])/mp.gamma(alpha)
        power_gap = audit.separates(f"tempered_case_{case}_wrong_kernel_exponent", direct, wrong_power)
        rows.append({
            "alpha": alpha_text, "rate": rate_text, "origin": origin_text, "gap": gap_text,
            "function": "1+y**2/5+sin(y)/7", "direct_kernel": number(direct),
            "conjugated_integral": number(conjugated), "absolute_error": number(error),
            "constant_value": number(constant), "constant_reference": number(constant_reference),
            "untempered_constant": number(untempered),
            "wrong_outer_sign_value": number(wrong_sign), "wrong_outer_sign_gap": number(sign_gap),
            "wrong_kernel_exponent_value": number(wrong_power), "wrong_kernel_exponent_gap": number(power_gap),
        })
    alpha, rate, origin, gap = map(mpq, parameters[0])
    audit.close("tempered_zero_function_direct", direct_tempered(alpha, rate, origin, origin+gap, lambda y: mp.mpf(0)), mp.mpf(0))
    audit.close("tempered_zero_function_conjugated", conjugated_tempered(alpha, rate, origin, origin+gap, lambda y: mp.mpf(0)), mp.mpf(0))
    return {"status": "NUMERICAL_DIAGNOSTIC_ONLY", "cases": rows,
            "null_control": "zero function at the first nonzero origin",
            "constant_boundary": "finite causal interval has incomplete-Gamma mass, not unit mass"}


def mellin_holdouts(audit: Audit) -> dict[str, object]:
    parameters = [("5/4", "7/6", "13/10"), ("7/3", "2/5", "-8/7"),
                  ("3/4", "11/8", "7/3"), ("5/4", "7/6", "0")]
    log_breaks = [-120, -40, -16, -8, -4, 0, 2, 4, 6]
    rows = []
    for case, (shape_text, rate_text, frequency_text) in enumerate(parameters):
        shape, rate, frequency = map(mpq, (shape_text, rate_text, frequency_text))
        scale = rate**shape/mp.gamma(shape)
        direct = scale*mp.quad(lambda r: r**(shape-1)*mp.exp(-rate*r)
                               *mp.exp(1j*frequency*mp.log(r)), [0, 1, mp.inf])
        log_fourier = scale*mp.quad(lambda y: mp.exp(shape*y-rate*mp.exp(y))
                                    *mp.exp(1j*frequency*y), log_breaks)
        reference = mp.gamma(shape+1j*frequency)/(mp.gamma(shape)*rate**(1j*frequency))
        errors = [
            audit.close(f"mellin_case_{case}_direct_gamma", direct, reference),
            audit.close(f"mellin_case_{case}_log_fourier_gamma", log_fourier, reference),
            audit.close(f"mellin_case_{case}_two_integrals", direct, log_fourier),
        ]
        left_tail = scale*mp.exp(shape*log_breaks[0])/shape
        right_tail = mp.gammainc(shape, rate*mp.exp(log_breaks[-1]), mp.inf)/mp.gamma(shape)
        if frequency == 0:
            audit.close("mellin_zero_frequency_normalization", direct, mp.mpf(1))
        rows.append({
            "shape": shape_text, "rate": rate_text, "frequency": frequency_text,
            "direct_mellin": complex_number(direct), "log_fourier": complex_number(log_fourier),
            "gamma_reference": complex_number(reference), "max_absolute_error": number(max(errors)),
            "log_left_tail_bound_evaluated_numerically": number(left_tail),
            "log_right_tail_bound_evaluated_numerically": number(right_tail),
        })
    return {"status": "NUMERICAL_DIAGNOSTIC_ONLY", "cases": rows,
            "log_quadrature_breaks": log_breaks,
            "tail_note": "The tail formulas use |phase|=1; their rounded evaluations are not interval certificates."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent/"receipts"/"independent.json")
    args = parser.parse_args()
    started = time.perf_counter()
    script = Path(__file__).resolve()
    mp.mp.dps = DPS
    audit = Audit()
    receipt: dict[str, object] = {
        "schema": "succ.gamma_volume.independent_audit.v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "versions": {"python": platform.python_version(), "sympy": sp.__version__, "mpmath": mp.__version__},
        "working_decimal_digits": DPS,
        "production_modules_imported": [],
        "parameters_chosen_without_reading_current_production_or_tests": True,
        "scope": "Exact finite symbolic identities and rational determinant signs; finite numerical diagnostics, not universal numerical proofs.",
    }
    try:
        receipt["repo_head"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=script.parent, text=True,
            stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        # Git provenance is useful metadata, not a mathematical dependency.
        receipt["repo_head"] = None
    try:
        receipt["exact"] = exact_source_audit(audit)
        receipt["fractional_oily"] = fractional_holdouts(audit)
        receipt["tempered_integrals"] = tempered_holdouts(audit)
        receipt["mellin_log_fourier"] = mellin_holdouts(audit)
        receipt["status"] = "PASS"
    except Exception as error:
        receipt["status"] = "FAIL"
        receipt["error"] = {"type": type(error).__name__, "message": str(error)}
    identities = [item for item in audit.checks if item["kind"] == "numerical_identity"]
    mutations = [item for item in audit.checks if item["kind"] == "mutation_separation"]
    receipt["checks"] = audit.checks
    receipt["counts"] = {
        "exact": sum(item["kind"] == "exact" for item in audit.checks),
        "numerical_identities": len(identities), "mutation_separations": len(mutations),
        "failed": sum(not item["passed"] for item in audit.checks),
    }
    receipt["max_numerical_identity_absolute_error"] = number(max(
        (mp.mpf(item["absolute_error"]) for item in identities), default=mp.mpf(0)))
    receipt["minimum_mutation_absolute_gap"] = (number(min(
        mp.mpf(item["absolute_gap"]) for item in mutations)) if mutations else None)
    receipt["elapsed_seconds"] = round(time.perf_counter()-started, 6)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False)+"\n")
    print(json.dumps({"status": receipt["status"], "receipt": str(args.output.resolve()),
                      "counts": receipt["counts"], "elapsed_seconds": receipt["elapsed_seconds"],
                      "max_numerical_identity_absolute_error": receipt["max_numerical_identity_absolute_error"],
                      "minimum_mutation_absolute_gap": receipt["minimum_mutation_absolute_gap"],
                      "error": receipt.get("error")}, sort_keys=True))
    return int(receipt["status"] != "PASS")


if __name__ == "__main__":
    raise SystemExit(main())
