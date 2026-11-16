#!/usr/bin/env python3
"""Bounded numerical diagnostic of the original-source face limit.

No production module is imported.  Two positive-kernel quadratures use
different coordinates and different algebraic expressions for the source:

  t route: q(t) is a positive sum of three exponential differences;
  y route: y=u**8 removes y**(1/8-1)'s endpoint singularity, and the
           original source numerator is evaluated in factored form.

The tested k and s lists are fixed.  The output is a raw numerical receipt,
not an interval certificate, an all-k error bound, a monotonicity claim,
or a proof of locally uniform convergence.  At the tested negative
integers the exact rising-factorial zero is used instead of a numerical
division by Gamma at a pole.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp


DEPTHS = (8, 32, 128, 512, 2048)
POINTS = (
    ("1/2", "0"),
    ("2", "0"),
    ("-1/2", "0"),
    ("-3/2", "0"),
    ("1/2", "3/4"),
    ("-1/2", "5/4"),
    ("-1", "0"),
    ("-2", "0"),
)
DPS = 40


def scalar(text: str):
    if "/" in text:
        numerator, denominator = text.split("/")
        return mp.mpf(numerator) / mp.mpf(denominator)
    return mp.mpf(text)


def encode(value):
    value = mp.mpc(value)
    return {"real": mp.nstr(value.real, DPS), "imag": mp.nstr(value.imag, DPS)}


def heat_t(t, depth):
    if t == 0 or mp.isinf(t):
        return mp.mpf(0)
    q = (2 * (-mp.expm1(-3 * t))
         - mp.expm1(-4 * t) - mp.expm1(-5 * t))
    return (mp.exp(-t) * q / (1 - mp.exp(-8 * t) / 16)
            * (-mp.expm1(-8 * t)) ** depth)


def heat_y_regularized(u, depth):
    # y=u**8 makes w(y)*y**(1/8-1)*dy = q(u)/(1-u**8/16)*du.
    if u == 0:
        return mp.mpf(4)
    if u == 1:
        return mp.mpf(0)
    q = (1 - u) * (u * u + 2) * (u * u + 2 * u + 2)
    return q * (1 - u ** 8) ** depth / (1 - u ** 8 / 16)


def t_integral(depth, s, center):
    def integrand(t):
        if t == 0 or mp.isinf(t):
            return mp.mpf(0)
        return mp.power(t, s - 1) * heat_t(t, depth)

    points = [mp.mpf(0), center / 2, center, 2 * center,
              4 * center, max(mp.mpf(8), 8 * center), mp.inf]
    return mp.quad(integrand, points)


def y_integral(depth, s, center):
    def integrand(u):
        if u == 0 or u == 1:
            # The value at a single endpoint does not change the integral.
            return mp.mpf(0)
        return mp.power(-mp.log(u), s - 1) * heat_y_regularized(u, depth)

    points = sorted({mp.mpf(0), mp.exp(-4 * center), mp.exp(-2 * center),
                     mp.exp(-center), mp.exp(-center / 2), mp.mpf(1)})
    return mp.quad(integrand, points)


def run():
    started = time.monotonic()
    rows = []
    normalizations = []
    max_coordinate_difference = mp.mpf(0)
    max_normalization_difference = mp.mpf(0)
    with mp.workdps(DPS):
        for depth in DEPTHS:
            center = mp.log(depth) / 8
            z_t = t_integral(depth, mp.mpf(1), center)
            z_y = y_integral(depth, mp.mpf(1), center)
            max_normalization_difference = max(max_normalization_difference, abs(z_t-z_y))
            normalizations.append({
                "k": depth,
                "A_k": mp.nstr(center, DPS),
                "Z_k_t": encode(z_t),
                "Z_k_y_regularized": encode(z_y),
                "absolute_coordinate_difference": mp.nstr(abs(z_t-z_y), DPS),
                "ratio_to_Gamma_1_8_over_2k_1_8": encode(
                    z_t * 2 * mp.power(depth, mp.mpf(1)/8) / mp.gamma(mp.mpf(1)/8)),
            })
            for real_text, imag_text in POINTS:
                s = mp.mpc(scalar(real_text), scalar(imag_text))
                row = {"k": depth, "s_real_exact": real_text, "s_imag_exact": imag_text}
                if s.imag == 0 and s.real <= 0 and s.real == int(s.real):
                    m = -int(s.real)
                    if m > depth:
                        raise ValueError("declared exact-zero branch requires m <= k")
                    row.update({
                        "status": "exact_analytic_rising_factorial_zero",
                        "C_k": {"real": "0", "imag": "0"},
                        "reciprocal_Gamma": {"real": "0", "imag": "0"},
                        "explanation": "s is one of 0,-1,...,-k; (s)_(k+1)=0",
                    })
                else:
                    if s.real <= -depth-1:
                        raise ValueError("quadrature point outside ordinary Mellin convergence domain")
                    raw_t = t_integral(depth, s, center)
                    raw_y = y_integral(depth, s, center)
                    factor = mp.power(center, 1-s) * mp.rgamma(s)
                    value_t = factor * raw_t / z_t
                    value_y = factor * raw_y / z_y
                    target = mp.rgamma(s)
                    difference = abs(value_t-value_y)
                    max_coordinate_difference = max(max_coordinate_difference, difference)
                    row.update({
                        "status": "numerical_diagnostic_only",
                        "Mellin_integral_t": encode(raw_t),
                        "Mellin_integral_y_regularized": encode(raw_y),
                        "C_k_t": encode(value_t),
                        "C_k_y_regularized": encode(value_y),
                        "reciprocal_Gamma": encode(target),
                        "absolute_coordinate_difference": mp.nstr(difference, DPS),
                        "absolute_difference_from_reciprocal_Gamma": mp.nstr(abs(value_t-target), DPS),
                    })
                rows.append(row)
        result = {
            "schema": "succ-causal-face-limit-diagnostic-v1",
            "source": "q(t)=4-2exp(-3t)-exp(-4t)-exp(-5t), native radix regulator 1/16",
            "definition": "C_k(s)=((log k)/8)^(1-s)*B_(1/16,k)(s)/B_(1/16,k)(1)",
            "classification": "finite numerical diagnostic supplemented by labelled exact zeros",
            "interval_certificate": False,
            "universal_convergence_inferred_from_numerics": False,
            "monotonicity_or_all_k_error_bound_asserted": False,
            "imports_production_modules": False,
            "python_version": platform.python_version(),
            "mpmath_version": mp.__version__,
            "working_decimal_digits": DPS,
            "depths": list(DEPTHS),
            "numerical_rows": sum(r["status"] == "numerical_diagnostic_only" for r in rows),
            "exact_zero_rows": sum(r["status"] == "exact_analytic_rising_factorial_zero" for r in rows),
            "max_C_coordinate_difference": mp.nstr(max_coordinate_difference, DPS),
            "max_Z_coordinate_difference": mp.nstr(max_normalization_difference, DPS),
            "normalizations": normalizations,
            "rows": rows,
            "elapsed_seconds": round(time.monotonic()-started, 3),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON receipt path; otherwise stdout")
    args = parser.parse_args()
    receipt = run()
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.output is None:
        print(serialized, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({key: receipt[key] for key in (
            "numerical_rows", "exact_zero_rows", "max_C_coordinate_difference",
            "max_Z_coordinate_difference", "elapsed_seconds", "script_sha256")}, indent=2))
