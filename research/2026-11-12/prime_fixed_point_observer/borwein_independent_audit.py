"""Exact geometric controls for the Borwein ratchet construction.

This audit is independent of the legacy CDF's inclusion-exclusion algorithm:
its primary oracle clips a two-dimensional rectangle by rational half-planes
and computes the resulting polygon area. The legacy CDF is a comparator.
Finite checks calibrate the derivations in reviews/borwein_adversary_audit.md;
they do not prove the infinite probabilistic or operator statements.

Run from any directory. The deterministic JSON is printed to stdout; this
script writes no receipt or other artifact by itself.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from observational_succ.borwein_prime_clock import borwein_window_mass


Point = tuple[F, F]
HalfPlane = tuple[F, F, F]


def clip_polygon(vertices: list[Point], plane: HalfPlane) -> list[Point]:
    """Intersect a convex polygon with alpha*x + beta*y <= bound."""
    if not vertices:
        return []
    alpha, beta, bound = plane
    output: list[Point] = []
    previous = vertices[-1]
    previous_excess = alpha * previous[0] + beta * previous[1] - bound
    for current in vertices:
        current_excess = alpha * current[0] + beta * current[1] - bound
        previous_inside = previous_excess <= 0
        current_inside = current_excess <= 0
        if previous_inside != current_inside:
            fraction = previous_excess / (previous_excess - current_excess)
            output.append((
                previous[0] + fraction * (current[0] - previous[0]),
                previous[1] + fraction * (current[1] - previous[1]),
            ))
        if current_inside:
            output.append(current)
        previous = current
        previous_excess = current_excess
    return output


def polygon_area(vertices: list[Point]) -> F:
    if len(vertices) < 3:
        return F(0)
    twice_signed = sum((
        first[0] * second[1] - second[0] * first[1]
        for first, second in zip(vertices, vertices[1:] + vertices[:1])
    ), F(0))
    return abs(twice_signed) / 2


def box_probability(a: F, b: F, constraints: tuple[HalfPlane, ...]) -> F:
    """Exact probability for independent uniforms in [-a,a] x [-b,b]."""
    if a <= 0 or b <= 0:
        raise ValueError("positive widths required")
    vertices = [(-a, -b), (a, -b), (a, b), (-a, b)]
    for constraint in constraints:
        vertices = clip_polygon(vertices, constraint)
    return polygon_area(vertices) / (4 * a * b)


def sum_interval_probability(a: F, b: F, lower: F, upper: F) -> F:
    return box_probability(a, b, (
        (F(1), F(1), upper),
        (F(-1), F(-1), -lower),
    ))


def one_uniform_interval(a: F, lower: F, upper: F) -> F:
    if a <= 0:
        raise ValueError("positive width required")
    return max(F(0), min(a, upper) - max(-a, lower)) / (2 * a)


def run_audit() -> dict[str, object]:
    checks: dict[str, int] = {}

    def equal(group: str, actual: object, expected: object) -> None:
        if actual != expected:
            raise AssertionError((group, actual, expected))
        checks[group] = checks.get(group, 0) + 1

    def true(group: str, condition: bool) -> None:
        equal(group, condition, True)

    # Calibrate the geometry oracle with all-space, empty, half and quarter boxes.
    for a, b in ((F(1), F(1)), (F(2, 3), F(7, 5)), (F(1, 101), F(3))):
        equal("geometry_controls", box_probability(a, b, ()), F(1))
        equal("geometry_controls", box_probability(a, b, ((F(1), F(0), -2*a),)), F(0))
        equal("geometry_controls", box_probability(a, b, ((F(1), F(0), F(0)),)), F(1, 2))
        equal("geometry_controls", box_probability(a, b, (
            (F(1), F(0), F(0)), (F(0), F(1), F(0)),
        )), F(1, 4))

    pairs = (
        (F(1, 4), F(1, 4)), (F(1, 3), F(2, 3)),
        (F(1), F(1, 2)), (F(2), F(2)),
        (F(3, 2), F(2, 3)), (F(1, 100), F(101, 100)),
        (F(3), F(1, 7)),
    )
    shifts = tuple(map(F, (-4, -3, -2, -1, 0, 1, 2, 3, 4))) + (F(-1, 2), F(1, 2))
    for a, b in pairs:
        for shift in shifts:
            geometric = sum_interval_probability(a, b, -1-shift, 1-shift)
            equal("legacy_cdf_vs_independent_polygon", borwein_window_mass((a, b), shift), geometric)

    for a in (F(1, 100), F(1, 3), F(1), F(3, 2), F(2), F(3)):
        for shift in shifts:
            equal("legacy_cdf_vs_independent_interval", borwein_window_mass((a,), shift),
                  one_uniform_interval(a, -1-shift, 1-shift))

    # The exact charge filter, including the support-equality boundary A=1.
    charge_values: dict[str, str] = {}
    for a, b in ((F(1, 4), F(1, 4)), (F(1, 3), F(2, 3)), (F(1, 100), F(99, 100))):
        for charge in range(-8, 9):
            expected = F(1) if charge == 0 else F(1, 2) if abs(charge) == 1 else F(0)
            actual = sum_interval_probability(a, b, F(-1-charge), F(1-charge))
            equal("integer_charge_filter", actual, expected)
            charge_values[str(charge)] = str(actual)
    # Repetition is a different operation from adding shrinking sinc widths.
    for repetitions in (1, 2, 3, 7, 16):
        for charge in range(9):
            value = sum_interval_probability(F(1, 3), F(2, 3), F(-1-charge), F(1-charge))
            expected = F(1) if charge == 0 else F(1, 2**repetitions) if charge == 1 else F(0)
            equal("repeated_filter", value**repetitions, expected)

    # Width a=3: normalizing by the central mass incorrectly fixes two composite charges.
    broad_masses = [one_uniform_interval(F(3), F(-1-c), F(1-c)) for c in range(5)]
    equal("broad_window_mutation", broad_masses,
          [F(1, 3), F(1, 3), F(1, 3), F(1, 6), F(0)])
    equal("broad_window_mutation", [value / broad_masses[0] for value in broad_masses],
          [F(1), F(1), F(1), F(1, 2), F(0)])

    # Endpoint mass differs from path survival; the latter imposes an extra slab.
    endpoint = sum_interval_probability(F(2), F(2), F(-1), F(1))
    survival = box_probability(F(2), F(2), (
        (F(1), F(1), F(1)), (F(-1), F(-1), F(1)),
        (F(1), F(0), F(1)), (F(-1), F(0), F(1)),
    ))
    equal("endpoint_vs_survival", endpoint, F(7, 16))
    equal("endpoint_vs_survival", survival, F(1, 4))
    true("endpoint_vs_survival", endpoint != survival)

    # Wrapping U[-1,1] mod 2 is uniform and adding another independent jump
    # preserves that circular law. Check eight cells by exact lifted polygons.
    circular_cells: list[str] = []
    for cell in range(8):
        lower, upper = F(cell, 4), F(cell+1, 4)
        before = sum((one_uniform_interval(F(1), lower+2*k, upper+2*k)
                      for k in range(-2, 3)), F(0))
        after = sum((sum_interval_probability(F(1), F(1, 2), lower+2*k, upper+2*k)
                     for k in range(-2, 3)), F(0))
        equal("periodization_mutation", before, F(1, 8))
        equal("periodization_mutation", after, before)
        circular_cells.append(str(after))
    line_mass = sum_interval_probability(F(1), F(1, 2), F(-1), F(1))
    equal("periodization_mutation", line_mass, F(7, 8))

    # Every stage has positive overflow, but the leak probabilities are summable.
    leaks: list[dict[str, object]] = []
    for stage in range(1, 13):
        epsilon = F(1, 2**stage)
        a = (1+epsilon)/2
        leak = 1-sum_interval_probability(a, a, F(-1), F(1))
        equal("summable_positive_leak_mutation", leak, F(1, (2**stage+1)**2))
        true("summable_positive_leak_mutation", F(0) < leak <= F(1, 4**stage))
        leaks.append({"stage": stage, "each_width": str(a), "leak": str(leak)})

    # The mixture law of max(U[-a,a],0) gives exact first and second moments.
    moments: list[dict[str, str]] = []
    for a in (F(1, 3), F(1), F(2), F(7, 4)):
        mean = F(1, 2) * a/2
        second = F(1, 2) * a*a/3
        variance = second-mean*mean
        equal("rectification_moments", mean, a/4)
        equal("rectification_moments", variance, 5*a*a/48)
        equal("rectification_moments", one_uniform_interval(a, a/2, a), F(1, 4))
        moments.append({"width": str(a), "mean": str(mean), "variance": str(variance)})

    # A common uniform Z makes all rectified increments vanish on Z<=0.
    # This exact event has probability 1/2, independent of how many widths are used.
    equal("correlated_increment_mutation", one_uniform_interval(F(1), F(-1), F(0)), F(1, 2))

    # Rational lower-bound certificate for the odd-width charge-one sinc product.
    # The analytic inequality sinc(x)>=1-x^2/6 (0<=x<=1/3) is proved in the note.
    square_sum = F(0)
    rational_product_lower_bound = F(1)
    for stage in range(1, 25):
        a = F(1, 2*stage+1)
        square_sum += a*a
        rational_product_lower_bound *= 1-a*a/6
        telescoping = F(stage, 4*(stage+1))
        true("shrinking_sinc_lower_bound", square_sum < telescoping)
        true("shrinking_sinc_lower_bound", rational_product_lower_bound >= 1-square_sum/6)
        true("shrinking_sinc_lower_bound", rational_product_lower_bound > F(23, 24))

    return {
        "schema": "succ.borwein.independent-audit.v1",
        "status": "PASS",
        "total_checks": sum(checks.values()),
        "checks_by_group": checks,
        "method": "Exact Fraction polygon clipping, interval lengths, and rational identities; no numerical quadrature or random sampling.",
        "dependency": "The legacy inclusion-exclusion CDF is only a comparator. The geometric oracle does not call it.",
        "scope": "Finite calibration of stated proofs and countermodels; no finite output certifies an infinite theorem.",
        "raw_controls": {
            "integer_charge_filter": charge_values,
            "a3_window_masses_c0_through_c4": list(map(str, broad_masses)),
            "a3_normalized_masses": [str(value/broad_masses[0]) for value in broad_masses],
            "endpoint_mass_width2_width2": str(endpoint),
            "two_stage_survival_mass": str(survival),
            "period2_eight_equal_cells_before_and_after": circular_cells,
            "line_mass_after_adding_width_half": str(line_mass),
            "summable_positive_leaks": leaks,
            "rectification_moments": moments,
            "correlated_common_uniform_stall_probability": "1/2",
            "all_odd_width_sinc_products_charge_one_lower_bound": "23/24 (strict for finite products)",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
