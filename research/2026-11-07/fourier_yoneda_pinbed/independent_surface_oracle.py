#!/usr/bin/env python3
"""Independent exact oracle for the continuous quadratic pin surface.

This file intentionally imports no SUCC implementation.  Its primary oracle
integrates two piecewise quadratic polynomials over their actual common
breakpoints using fractions.Fraction.  The Bernoulli B4 closed form and affine
pin dynamics are the *claims under test*, not ingredients in that integrator.

Run directly; the complete deterministic receipt is emitted as JSON.  This is
finite algebraic calibration.  The all-parameter proofs live in the accompanying
research note, and no output claims pi normality or source equidistribution.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path


ZERO = Q(0)
ONE = Q(1)


def mod_one(x: Q) -> Q:
    """Exact representative in [0, 1), including negative integer lifts."""
    x = Q(x)
    return x - x.numerator // x.denominator


def b2(t: Q) -> Q:
    t = mod_one(t)
    return t * t - t + Q(1, 6)


def b4_polynomial(t: Q) -> Q:
    """Nonperiodic polynomial, evaluated only on a declared representative."""
    t = Q(t)
    return t**4 - 2 * t**3 + t * t - Q(1, 30)


def polynomial_product(a: tuple[Q, ...], b: tuple[Q, ...]) -> tuple[Q, ...]:
    result = [ZERO] * (len(a) + len(b) - 1)
    for j, left in enumerate(a):
        for k, right in enumerate(b):
            result[j + k] += left * right
    return tuple(result)


def polynomial_integral(coefficients: tuple[Q, ...], lo: Q, hi: Q) -> Q:
    return sum(
        (value * (hi ** (degree + 1) - lo ** (degree + 1)) / (degree + 1)
         for degree, value in enumerate(coefficients)),
        ZERO,
    )


def local_centered_quadratic(shift: Q) -> tuple[Q, Q, Q]:
    """Coefficients of B2(t+shift) within one uninterrupted polynomial piece."""
    return (shift * shift - shift + Q(1, 6), 2 * shift - 1, ONE)


@lru_cache(maxsize=None)
def direct_covariance(x: Q, y: Q) -> Q:
    """Integrate B2({t-x}) B2({t-y}) by splitting at both actual seams.

    No Fourier series, B4 identity, translation reduction, or SUCC function is
    used here.  Midpoints select the correct polynomial on each open interval;
    individual endpoints do not affect the integral.
    """
    x, y = mod_one(x), mod_one(y)
    cuts = sorted({ZERO, ONE, x, y})
    answer = ZERO
    for lo, hi in zip(cuts, cuts[1:]):
        midpoint = (lo + hi) / 2
        x_shift = -x + (1 if midpoint < x else 0)
        y_shift = -y + (1 if midpoint < y else 0)
        product = polynomial_product(
            local_centered_quadratic(x_shift),
            local_centered_quadratic(y_shift),
        )
        answer += polynomial_integral(product, lo, hi)
    return answer


def surface(measure: tuple[tuple[Q, Q], ...], t: Q) -> Q:
    """Pointwise surface evaluation for a finite rational signed measure."""
    return sum((weight * b2(t - x) for x, weight in measure), ZERO)


def pushed(measure: tuple[tuple[Q, Q], ...], radix: int, shift: Q
           ) -> tuple[tuple[Q, Q], ...]:
    return tuple((mod_one(radix * x + shift), weight) for x, weight in measure)


def branch_average(measure: tuple[tuple[Q, Q], ...], radix: int,
                   shift: Q, t: Q) -> Q:
    return sum((surface(measure, (t - shift + j) / radix)
                for j in range(radix)), ZERO) / radix


def direct_energy(measure: tuple[tuple[Q, Q], ...]) -> Q:
    return sum((wx * wy * direct_covariance(x, y)
                for x, wx in measure for y, wy in measure), ZERO)


def uniform_grid(q: int, phase: Q = ZERO) -> tuple[tuple[Q, Q], ...]:
    return tuple((mod_one(Q(j, q) + phase), Q(1, q)) for j in range(q))


def difference(left: tuple[tuple[Q, Q], ...], right: tuple[tuple[Q, Q], ...]
               ) -> tuple[tuple[Q, Q], ...]:
    return left + tuple((x, -weight) for x, weight in right)


def original_bbp_forcing(n: int) -> Q:
    """Frozen four-fraction expression; no pi digit or imported oracle input."""
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def combined_bbp_forcing(n: int) -> Q:
    return Q(120 * n * n - 89 * n + 16,
             (2 * n - 1) * (4 * n - 1) * (8 * n - 7) * (8 * n - 3))


def require_equal(left: Q, right: Q, context: str) -> None:
    if left != right:
        raise AssertionError(f"{context}: {left} != {right}")


def run() -> dict:
    counts: dict[str, int] = {}
    witnesses: dict[str, object] = {}

    # Deliberately excludes the reserved fresh 17, 31, 61, 127 regions.
    points = tuple(map(Q, [0, 1, -1, 2])) + (
        Q(1, 2), Q(1, 3), Q(2, 3), Q(1, 4), Q(3, 4),
        Q(1, 5), Q(2, 5), Q(4, 5), Q(1, 7), Q(3, 7), Q(6, 7),
        Q(-2, 3), Q(8, 5), Q(-9, 7),
    )
    counts["direct_covariance_identity"] = 0
    counts["exact_dirac_distance"] = 0
    for x in points:
        for y in points:
            observed = direct_covariance(x, y)
            claimed = -b4_polynomial(mod_one(x - y)) / 6
            require_equal(observed, claimed, f"covariance at {x}, {y}")
            counts["direct_covariance_identity"] += 1
            d = mod_one(x - y)
            d = min(d, 1 - d)
            distance_squared = (direct_covariance(x, x) + direct_covariance(y, y)
                                - 2 * direct_covariance(x, y))
            require_equal(distance_squared, d * d * (1 - d)**2 / 3,
                          f"Dirac distance at {x}, {y}")
            counts["exact_dirac_distance"] += 1

    witnesses["covariance_samples"] = [
        {"x": x, "y": y, "direct_integral": direct_covariance(x, y),
         "claimed_closed_form": -b4_polynomial(mod_one(x - y)) / 6}
        for x, y in ((ZERO, ZERO), (ZERO, Q(1, 2)), (Q(2, 5), Q(-2, 3)))
    ]

    grids = []
    for q in (1, 2, 3, 4, 5, 7, 8, 9, 11, 13):
        measured = direct_energy(uniform_grid(q))
        expected = Q(1, 180 * q**4)
        require_equal(measured, expected, f"grid energy q={q}")
        grids.append({"q": q, "direct_energy": measured, "expected": expected})
    counts["uniform_grid_energies"] = len(grids)
    witnesses["grid_energies"] = grids

    measures = (
        ((ZERO, ONE),),
        ((Q(1, 3), ONE),),
        ((ZERO, Q(1, 3)), (Q(2, 5), Q(2, 3))),
        ((Q(-2, 3), Q(1, 7)), (Q(1, 4), Q(2, 7)), (Q(4, 5), Q(4, 7))),
        # A zero-total-mass signed difference tests the linear extension.
        ((ZERO, ONE), (Q(1, 3), -ONE)),
    )
    radices = (2, 3, 4, 16)
    shifts = (ZERO, Q(1, 7), Q(5, 6), Q(-2, 5), Q(8, 3))
    counts["affine_naturality"] = 0
    seam_case_count = 0
    for measure in measures:
        for radix in radices:
            for shift in shifts:
                image = pushed(measure, radix, shift)
                seams = {mod_one(radix * x + shift) for x, _ in measure}
                locations = set(points) | seams | {s + 1 for s in seams}
                for t in locations:
                    left = surface(image, t)
                    right = radix**2 * branch_average(measure, radix, shift, t)
                    require_equal(left, right,
                                  f"naturality b={radix}, a={shift}, t={t}")
                    counts["affine_naturality"] += 1
                    if mod_one(t) in seams:
                        seam_case_count += 1

    # Saturation of the b^2 L2 operator norm using bona fide finite probability
    # measures, instead of Fourier-space test vectors or trigonometric densities.
    norm_witnesses = []
    for radix in radices:
        for displacement in (Q(1, 3), Q(1, 5)):
            left = uniform_grid(radix)
            right = uniform_grid(radix, displacement / radix)
            delta = difference(left, right)
            input_squared = direct_energy(delta)
            output_squared = direct_energy(pushed(delta, radix, Q(1, 7)))
            if input_squared <= 0:
                raise AssertionError("Operator-norm witness must be nonzero")
            require_equal(output_squared, radix**4 * input_squared,
                          f"operator-norm saturation b={radix}, d={displacement}")
            norm_witnesses.append({"radix": radix, "displacement": displacement,
                                   "input_norm_squared": input_squared,
                                   "output_norm_squared": output_squared,
                                   "squared_ratio": output_squared / input_squared})
    counts["exact_operator_norm_saturation"] = len(norm_witnesses)
    witnesses["operator_norm_saturation"] = norm_witnesses

    # Original zero-seed source replay: only the designated tiny calibration
    # indices 1..5, and two independently written forcing expressions.
    source_states = []
    state = ZERO
    source_naturality_count = 0
    for n in range(1, 6):
        forcing = original_bbp_forcing(n)
        require_equal(forcing, combined_bbp_forcing(n), f"original BBP forcing n={n}")
        previous = state
        state = 16 * state + forcing
        source_measure = ((mod_one(previous), ONE),)
        for t in (ZERO, Q(1, 2), mod_one(state), mod_one(state) + 1):
            left = b2(t - state)
            right = 16**2 * branch_average(source_measure, 16, forcing, t)
            require_equal(left, right, f"source-specific BBP naturality n={n}, t={t}")
            source_naturality_count += 1
        source_states.append({"n": n, "forcing": forcing,
                              "unwrapped_state": state, "phase": mod_one(state)})
    require_equal(original_bbp_forcing(1), Q(47, 15), "BBP initial calibration")
    counts["bbp_initial_value_calibration"] = 1
    counts["original_bbp_forcing_crosscheck"] = 5
    counts["source_specific_bbp_naturality"] = source_naturality_count
    witnesses["bbp_zero_seed_states"] = source_states

    # Preregistered hostile mutations: each false rule must actually lose.
    mutation_results = []

    def reject_mutation(name: str, actual: Q, mutated: Q) -> None:
        if actual == mutated:
            raise AssertionError(f"Mutation survived its declared witness: {name}")
        mutation_results.append({"mutation": name, "rejected": True,
                                 "actual": actual, "mutated_prediction": mutated})

    reject_mutation("wrong_covariance_sign", direct_covariance(ZERO, ZERO),
                    b4_polynomial(ZERO) / 6)
    reject_mutation("omit_B4_constant", direct_covariance(ZERO, ZERO), ZERO)
    sample = ((Q(1, 3), ONE),)
    radix, shift, t = 3, Q(1, 7), Q(2, 5)
    actual = surface(pushed(sample, radix, shift), t)
    average = branch_average(sample, radix, shift, t)
    reject_mutation("omit_b_squared", actual, average)
    reject_mutation("use_b_instead_of_b_squared", actual, radix * average)
    wrong_shift = radix**2 * branch_average(sample, radix, -shift, t)
    reject_mutation("reverse_translation_sign", actual, wrong_shift)
    # Uncentered kappa=B2+1/12 cannot obey the same homogeneous b^2 rule.
    reject_mutation("forget_centering", actual + Q(1, 12),
                    radix**2 * (average + Q(1, 12)))
    norm_sample = norm_witnesses[0]
    reject_mutation("claim_nonexpansion", norm_sample["output_norm_squared"],
                    norm_sample["input_norm_squared"])
    n = 3
    wrong_forcing = (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
                     - Q(1, 8 * n - 3) + Q(1, 8 * n - 2))
    reject_mutation("flip_last_BBP_pole_sign", original_bbp_forcing(n), wrong_forcing)
    counts["hostile_mutations_rejected"] = len(mutation_results)
    witnesses["mutations"] = mutation_results

    return {
        "oracle": "independent_piecewise_quadratic_pin_surface",
        "oracle_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "status": "PASS",
        "arithmetic": "stdlib fractions.Fraction; exact polynomial integration",
        "imports_succ_implementation": False,
        "primary_method": "split at both source seams, multiply local polynomials, integrate exactly",
        "normalization": "circle Haar mass 1; B2(t)=t^2-t+1/6; centered surface",
        "counts": counts,
        "total_asserted_checks": sum(counts.values()),
        "coverage_subcategories": {
            "affine_naturality_cases_at_source_seam": seam_case_count,
            "subcategory_counts_added_to_total": False,
        },
        "witnesses": witnesses,
        "scope": {
            "source_indices": [1, 2, 3, 4, 5],
            "reserved_fresh_regions_used": [],
            "finite_calibration_only": True,
            "pi_normality": "OPEN",
            "all_parameter_proof_claimed_by_computation": False,
        },
    }


def encode(value: object) -> str:
    if isinstance(value, Q):
        return str(value)
    raise TypeError(f"Cannot JSON-encode {type(value).__name__}")


if __name__ == "__main__":
    print(json.dumps(run(), default=encode, indent=2, sort_keys=True))
