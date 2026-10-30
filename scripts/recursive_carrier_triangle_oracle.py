#!/usr/bin/env python3
"""Independent exact finite oracle for the recursive-carrier triangle campaign.

Run from a checkout with SymPy available, for example:
    PYTHONPATH=/tmp/succ_triangle_deps python scripts/recursive_carrier_triangle_oracle.py

This script deliberately does not import observational_succ.recursive_carrier_triangle.
It reconstructs the source by partial fractions, the atoms in Q(sqrt(241)),
cumulants from raw moments and symbolic differentiation, and path sheets by
independent word enumeration.  Finite checks do not prove the all-parameter
paper theorems.  No selected BBP normality, physical field, or cognitive claim
is inferred.  Numerical diagnostics are absent: all verdicts use exact arithmetic.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, factorial
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from observational_succ.succ_internal_matrix_walk import authentic_r


BASELINE = "ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc"
FORBIDDEN_MODULE = "observational_succ.recursive_carrier_triangle"
COUNTS: Counter[str] = Counter()

# These grids are fixed in source before execution, not adapted to its answers.
SOURCE_INDICES = tuple(range(1, 33)) + (63, 127)
PARAMETERS = (Q(1, 7), Q(1, 3), Q(1), Q(5, 2), Q(9), Q(17), Q(65))
ATOM_SHIFTS = (Q(0), Q(1, 5), Q(1), Q(8), Q(16), Q(33, 2))
FINITE_DIFFERENCE_PARAMETERS = (Q(1, 5), Q(1), Q(9), Q(17), Q(65))
FINITE_DIFFERENCE_ORDERS = tuple(range(1, 9))
SYMBOLIC_CUMULANT_ORDERS = tuple(range(1, 7))
RAW_CUMULANT_ORDERS = tuple(range(1, 13))


def require(condition: bool, group: str, detail: str = "") -> None:
    if not condition:
        raise AssertionError(f"{group}: {detail}")
    COUNTS[group] += 1


def source(a: Q) -> Q:
    """The signed partial-fraction source; no factorization used."""
    return 4 / a - 2 / (a + 3) - 1 / (a + 4) - 1 / (a + 5)


@dataclass(frozen=True)
class Quadratic:
    """Exact x+y*sqrt(241), with independent arithmetic and sign comparison."""

    x: Q
    y: Q = Q(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", Q(self.x))
        object.__setattr__(self, "y", Q(self.y))

    @staticmethod
    def coerce(other: object) -> "Quadratic":
        return other if isinstance(other, Quadratic) else Quadratic(Q(other))

    def __add__(self, other: object) -> "Quadratic":
        z = self.coerce(other)
        return Quadratic(self.x + z.x, self.y + z.y)

    __radd__ = __add__

    def __neg__(self) -> "Quadratic":
        return Quadratic(-self.x, -self.y)

    def __sub__(self, other: object) -> "Quadratic":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "Quadratic":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "Quadratic":
        z = self.coerce(other)
        return Quadratic(self.x * z.x + 241 * self.y * z.y,
                         self.x * z.y + self.y * z.x)

    __rmul__ = __mul__

    def inverse(self) -> "Quadratic":
        norm = self.x * self.x - 241 * self.y * self.y
        if not norm:
            raise ZeroDivisionError("zero quadratic-field element")
        return Quadratic(self.x / norm, -self.y / norm)

    def __truediv__(self, other: object) -> "Quadratic":
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other: object) -> "Quadratic":
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> "Quadratic":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result, base = Quadratic(1), self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def sign(self) -> int:
        sign = lambda z: (z > 0) - (z < 0)
        if not self.y:
            return sign(self.x)
        if not self.x or sign(self.x) == sign(self.y):
            return sign(self.y)
        comparison = sign(self.x * self.x - 241 * self.y * self.y)
        return comparison if self.x > 0 else -comparison

    def as_sympy(self) -> sp.Expr:
        return (sp.Rational(self.x.numerator, self.x.denominator)
                + sp.Rational(self.y.numerator, self.y.denominator) * sp.sqrt(241))


ALPHA = Quadratic(Q(121, 30), Q(-1, 30))
BETA = Quadratic(Q(121, 30), Q(1, 30))


def raw_moment(a: Q, order: int) -> Q:
    return factorial(order) * (
        4 / a ** (order + 1)
        - 2 / (a + 3) ** (order + 1)
        - 1 / (a + 4) ** (order + 1)
        - 1 / (a + 5) ** (order + 1)
    ) / source(a)


def moment_cumulants(a: Q, maximum: int) -> tuple[Q, ...]:
    moments = tuple(raw_moment(a, n) for n in range(maximum + 1))
    cumulants = [Q(0)]
    for n in range(1, maximum + 1):
        cumulants.append(moments[n] - sum(
            (comb(n - 1, k - 1) * cumulants[k] * moments[n - k]
             for k in range(1, n)), Q(0)))
    return tuple(cumulants)


def algebraic_cumulant(a: Q, order: int) -> Quadratic:
    poles = sum((1 / (a + c) ** order for c in (0, 3, 4, 5)), Q(0))
    return factorial(order - 1) * (
        Quadratic(poles) - (a + ALPHA) ** (-order) - (a + BETA) ** (-order))


def complete_factorial_ratio(a: Q, shifts: tuple[Q, ...]) -> Q:
    """Exponentiate the complete mixed difference of log R using every cell."""
    value = Q(1)
    for chosen in product((0, 1), repeat=len(shifts)):
        offset = sum((shift for shift, use in zip(shifts, chosen) if use), Q(0))
        corner = source(a + offset)
        if (len(shifts) - sum(chosen)) % 2:
            value /= corner
        else:
            value *= corner
    return value


def pair_ratio(a: Q, s: Q, t: Q) -> Q:
    return source(a + s + t) * source(a) / (source(a + s) * source(a + t))


def word_mass(word: str, probability) -> Q:
    l = r = 0
    mass = Q(1)
    for symbol in word:
        left = probability(l, r)
        mass *= left if symbol == "L" else 1 - left
        l += symbol == "L"
        r += symbol == "R"
    return mass


def sheet_mass_ratio(word: str, cell_ratio) -> Q:
    """Area product from explicit closed-form cells, not transition products."""
    l = r = 0
    result = Q(1)
    for symbol in word:
        if symbol == "L":
            for j in range(r):
                result /= cell_ratio(l, j)
            l += 1
        else:
            r += 1
    return result


def row_times_matrix(row, matrix) -> tuple[Q, ...]:
    return tuple(sum((row[i] * matrix[i][j] for i in range(len(row))), Q(0))
                 for j in range(len(matrix[0])))


def normalize(row) -> tuple[tuple[Q, ...], Q]:
    total = sum(row, Q(0))
    return tuple(entry / total for entry in row), total


def source_green(values: tuple[Q, ...], seed: Q) -> tuple[Q, ...]:
    """Direct finite convolution, independent of production's recursive update."""
    return tuple(16 ** n * seed + sum(
        (16 ** (n - k) * values[k - 1] for k in range(1, n + 1)), Q(0))
        for n in range(len(values) + 1))


def run() -> dict:
    require(FORBIDDEN_MODULE not in sys.modules, "implementation_independence")
    a_symbol = sp.Symbol("a", positive=True)
    r_symbol = (4 / a_symbol - 2 / (a_symbol + 3)
                - 1 / (a_symbol + 4) - 1 / (a_symbol + 5))
    factor_symbol = ((15 * a_symbol ** 2 + 121 * a_symbol + 240)
                     / (a_symbol * (a_symbol + 3) * (a_symbol + 4) * (a_symbol + 5)))
    require(sp.cancel(r_symbol - factor_symbol) == 0, "symbolic_source_factorization")
    require(sp.expand(15 * (a_symbol + ALPHA.as_sympy())
                      * (a_symbol + BETA.as_sympy()))
            == 15 * a_symbol ** 2 + 121 * a_symbol + 240,
            "symbolic_source_factorization")
    for n in SOURCE_INDICES:
        require(source(Q(8 * n - 7)) == authentic_r(n), "native_source_authentication",
                f"n={n}")

    # Calibrate the quadratic field itself against SymPy's separate representation.
    field_elements = (Quadratic(2, 3), Quadratic(Q(-2, 7), Q(1, 3)), ALPHA, BETA)
    for x, y in product(field_elements, repeat=2):
        for result, expression in (
            (x + y, x.as_sympy() + y.as_sympy()),
            (x * y, x.as_sympy() * y.as_sympy()),
            (x / y, x.as_sympy() / y.as_sympy()),
        ):
            require(sp.simplify(result.as_sympy() - expression) == 0,
                    "quadratic_field_calibration")
    for positive in (ALPHA - 3, 4 - ALPHA, BETA - 4, 5 - BETA):
        require(positive.sign() == 1, "exact_interlacing")
    for value, expected in ((Quadratic(16, -1), 1), (Quadratic(-16, 1), -1),
                            (Quadratic(15, -1), -1), (Quadratic(-15, 1), 1),
                            (Quadratic(0), 0)):
        require(value.sign() == expected, "quadratic_sign_calibration")

    for a in PARAMETERS:
        p_alpha = (ALPHA - 3) / (a + ALPHA)
        p_beta = (BETA - 4) / (a + BETA)
        require(p_alpha.sign() > 0 and (1 - p_alpha).sign() > 0,
                "bernoulli_atom_probabilities")
        require(p_beta.sign() > 0 and (1 - p_beta).sign() > 0,
                "bernoulli_atom_probabilities")
        for s in ATOM_SHIFTS:
            left_gate = 1 - p_alpha + p_alpha * (a + 3) / (a + 3 + s)
            right_gate = 1 - p_beta + p_beta * (a + 4) / (a + 4 + s)
            atom_product = a / (a + s) * (a + 5) / (a + 5 + s) * left_gate * right_gate
            require(atom_product.y == 0 and atom_product.x == source(a + s) / source(a),
                    "independent_atomic_laplace_products", f"a={a}, s={s}")

    derivative = sp.cancel(sp.diff(sp.log(r_symbol), a_symbol))
    symbolic_derivatives = {}
    for order in SYMBOLIC_CUMULANT_ORDERS:
        symbolic_derivatives[order] = derivative
        if order != SYMBOLIC_CUMULANT_ORDERS[-1]:
            derivative = sp.cancel(sp.diff(derivative, a_symbol))
    for a in PARAMETERS:
        cumulants = moment_cumulants(a, RAW_CUMULANT_ORDERS[-1])
        require(raw_moment(a, 0) == 1, "raw_moment_normalization")
        for order in RAW_CUMULANT_ORDERS:
            atom_cumulant = algebraic_cumulant(a, order)
            require(atom_cumulant.y == 0 and atom_cumulant.x == cumulants[order],
                    "raw_moment_vs_algebraic_cumulants", f"a={a}, order={order}")
            low = factorial(order - 1) * (1 / a ** order + 1 / (a + 5) ** order)
            high = factorial(order - 1) * (1 / a ** order + 1 / (a + 3) ** order)
            require(0 < low < cumulants[order] < high, "strict_cumulant_bounds",
                    f"a={a}, order={order}")
            if order in symbolic_derivatives:
                exact_symbolic = (-1) ** order * symbolic_derivatives[order].subs(
                    a_symbol, sp.Rational(a.numerator, a.denominator))
                require(exact_symbolic == sp.Rational(cumulants[order].numerator,
                                                      cumulants[order].denominator),
                        "log_derivative_vs_raw_moment_cumulants", f"a={a}, order={order}")

    for a in FINITE_DIFFERENCE_PARAMETERS:
        for order in FINITE_DIFFERENCE_ORDERS:
            patterns = ((Q(1),) * order, (Q(8),) * order,
                        tuple(Q(j + 1, 3) for j in range(order)))
            for shifts in patterns:
                ratio = complete_factorial_ratio(a, shifts)
                correct_sign = ratio > 1 if order % 2 == 0 else 0 < ratio < 1
                require(correct_sign, "complete_factorial_strict_signs",
                        f"a={a}, order={order}, shifts={shifts}")
            zero_shifts = (Q(0),) + (Q(8),) * (order - 1)
            require(complete_factorial_ratio(a, zero_shifts) == 1,
                    "complete_factorial_zero_controls")

    cocycle_steps = (Q(0), Q(1, 3), Q(1), Q(8))
    for a in (Q(1, 5), Q(1), Q(17)):
        for s, t, u in product(cocycle_steps, repeat=3):
            require(source(a + s + t) / source(a)
                    == source(a + s) / source(a) * source(a + s + t) / source(a + s),
                    "source_tilt_updated_field_composition")
            require(pair_ratio(a, s, t) * pair_ratio(a, s + t, u)
                    == pair_ratio(a, t, u) * pair_ratio(a, s, t + u),
                    "interaction_cocycle")

    # Noncommuting observed-event kernels: identical total mass, different posteriors.
    initial = (Q(1, 2), Q(1, 2))
    kernel_k = ((Q(1, 2), Q(1, 2)), (Q(0), Q(1, 2)))
    kernel_l = ((Q(1, 2), Q(0)), (Q(1, 2), Q(1, 2)))
    p_k, z_k = normalize(row_times_matrix(initial, kernel_k))
    p_l, z_l = normalize(row_times_matrix(initial, kernel_l))
    p_kl, z_l_after_k = normalize(row_times_matrix(p_k, kernel_l))
    p_lk, z_k_after_l = normalize(row_times_matrix(p_l, kernel_k))
    raw_kl = row_times_matrix(row_times_matrix(initial, kernel_k), kernel_l)
    raw_lk = row_times_matrix(row_times_matrix(initial, kernel_l), kernel_k)
    require(normalize(raw_kl) == (p_kl, z_k * z_l_after_k), "posterior_mass_composition")
    require(normalize(raw_lk) == (p_lk, z_l * z_k_after_l), "posterior_mass_composition")
    require(p_kl == (Q(3, 5), Q(2, 5)) and p_lk == (Q(2, 5), Q(3, 5)),
            "noncommuting_posterior_control")
    require(sum(raw_kl) == sum(raw_lk) == Q(5, 8), "equal_mass_distinct_field_control")

    # Harmonic fields: every complete path remains inside the declared live rectangle.
    for length in range(3, 10):
        probability = lambda l, r, length=length: Q(length - r, 2 * length - l - r)
        cell = lambda l, r, length=length: Q((length - r) * (length - l - 1),
                                            (length - l) * (length - r - 1))
        for n in range(1, min(9, 2 * length - 1)):
            for letters in product("LR", repeat=n):
                word = "".join(letters)
                l, r = word.count("L"), word.count("R")
                if max(l, r) >= length:
                    continue
                reference = "L" * l + "R" * r
                require(word_mass(word, probability) / word_mass(reference, probability)
                        == sheet_mass_ratio(word, cell), "harmonic_discrete_stokes")

    exponential = lambda l, r: Q(2 ** l, 2 ** l + 2 ** r)
    exp_cell = lambda l, r: Q(2 ** l + 2 ** (r + 1), 2 ** (l + 1) + 2 ** r)
    polya = lambda l, r: (Q(3, 2) + l) / (Q(3, 2) + Q(2, 3) + l + r)
    for n in range(0, 10):
        total = signed = Q(0)
        for letters in product("LR", repeat=n):
            word = "".join(letters)
            l, r = word.count("L"), word.count("R")
            reference = "L" * l + "R" * r
            mass = word_mass(word, exponential)
            require(mass / word_mass(reference, exponential)
                    == sheet_mass_ratio(word, exp_cell), "exponential_discrete_stokes")
            require(word_mass(word, polya) == word_mass(reference, polya),
                    "polya_flatness_control")
            total += mass
            signed += mass * (0 if not word else 1 if word[-1] == "L" else -1)
        require(total == 1 and signed == 0, "ensemble_mass_and_zero_phase")

    previous_bound = Q(0)
    for n in range(3, 65):
        prefix_probability = Q(1)
        for k in range(n):
            prefix_probability *= Q(2 ** k, 2 ** k + 1)
        rational_tail_bound = prefix_probability * (1 - Q(1, 2 ** (n - 1)))
        require(prefix_probability > Q(1, 5) and rational_tail_bound >= Q(1, 5),
                "all_left_rational_atom_bound")
        require(rational_tail_bound > previous_bound, "all_left_bound_monotonicity")
        previous_bound = rational_tail_bound

    forcing = tuple(authentic_r(n) for n in range(1, 25))
    first = tuple(Q(1, 8 * n - 4) for n in range(1, 25))
    second = tuple(Q(1, 8 * n - 3) for n in range(1, 25))
    for seed in (Q(0), Q(1, 15), Q(-2, 7)):
        for alpha, beta in ((Q(1), Q(1)), (Q(2, 3), Q(-3, 5)), (Q(-1, 2), Q(7, 4))):
            streams = [tuple(r + i * alpha * f + j * beta * g
                             for r, f, g in zip(forcing, first, second))
                       for i, j in ((0, 0), (1, 0), (0, 1), (1, 1))]
            u00, u10, u01, u11 = (source_green(stream, seed) for stream in streams)
            for n, corners in enumerate(zip(u00, u10, u01, u11)):
                b00, b10, b01, b11 = corners
                residual = b11 + b00 - b10 - b01
                require(residual == 0, "affine_source_rectangle", f"n={n}, seed={seed}")
                for frequency in (0, 1, -3, 8):
                    require((frequency * residual) % 1 == 0, "exact_phase_rectangle")

    mutations = []

    def reject(name: str, observed, false_value, reason: str) -> None:
        require(observed != false_value, "false_mutations_rejected", name)
        mutations.append({"name": name, "status": "rejected", "reason": reason,
                          "exact_observed": str(observed), "false_prediction": str(false_value)})

    reject("source_pole_coefficient", source(Q(1)),
           Q(4) - Q(1, 4) - Q(1, 5) - Q(1, 6),
           "Changing the authentic second pole coefficient from -2 to -1 changes R(1).")
    reject("omitted_posterior_normalizer", sum(row_times_matrix(initial, kernel_k)), Q(1),
           "The unnormalized observed-event row has mass 3/4 and is not a posterior.")
    reject("reset_field_cocycle", sum(raw_kl), z_k * z_l,
           "The second normalization must use the posterior after the first kernel.")
    reject("source_reset_tilt_cocycle", source(Q(17)) / source(Q(1)),
           (source(Q(9)) / source(Q(1))) ** 2,
           "Two source-clock tilts do not equal two independent resets to a=1.")
    reject("pairwise_log_truncation", complete_factorial_ratio(Q(1), (Q(8),) * 3), Q(1),
           "The complete cubic factorial ratio is strictly below one on the authentic clock.")
    reject("flat_curvature_assumption", exp_cell(1, 0), Q(1),
           "The exponentially reinforced carrier has nontrivial local route odds.")
    true_interaction = complete_factorial_ratio(Q(1), (Q(1), Q(8)))
    wrong_mobius_sign = true_interaction / source(Q(1)) ** 2
    reject("fake_interaction_exponent", true_interaction, wrong_mobius_sign,
           "Flipping the empty-corner exponent corrupts the complete mixed difference.")
    # A fake cross forcing inserted only at corner (1,1) violates the affine phase passport.
    fake_phase_exponent = (first[0] * second[0]) % 1
    reject("invented_affine_cross_forcing", fake_phase_exponent, Q(0),
           "An alpha*beta*f*g source term creates a nonzero mixed phase and changes the source family.")

    require(FORBIDDEN_MODULE not in sys.modules, "implementation_independence")
    return {
        "schema": "succ.recursive-carrier-triangle.independent-oracle.v1",
        "status": "passed",
        "baseline_commit": BASELINE,
        "implementation": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "native_source": "observational_succ.succ_internal_matrix_walk.authentic_r",
            "production_triangle_module_imported": False,
            "independence_scope": "separate algebra and enumeration; same authenticated original source",
        },
        "preregistered_finite_grids": {
            "source_indices": list(SOURCE_INDICES),
            "positive_parameters": [str(x) for x in PARAMETERS],
            "atom_shifts": [str(x) for x in ATOM_SHIFTS],
            "symbolic_cumulant_orders": list(SYMBOLIC_CUMULANT_ORDERS),
            "raw_cumulant_orders": list(RAW_CUMULANT_ORDERS),
            "factorial_difference_parameters": [str(x) for x in FINITE_DIFFERENCE_PARAMETERS],
            "factorial_difference_orders": list(FINITE_DIFFERENCE_ORDERS),
            "factorial_shift_patterns": ["all 1", "all 8", "(1/3,2/3,...,order/3)"],
            "zero_direction_control": "one zero followed by order-1 shifts of 8",
            "harmonic_lengths": [3, 4, 5, 6, 7, 8, 9],
            "exponential_and_polya_max_word_length": 9,
            "all_left_prefix_range": [3, 64],
            "affine_horizon": 24,
            "affine_seeds": ["0", "1/15", "-2/7"],
        },
        "exact_checks": dict(sorted(COUNTS.items())),
        "exact_check_total": sum(COUNTS.values()),
        "mutations": {"rejected_count": len(mutations), "witnesses": mutations},
        "exact_examples": {
            "authentic_clock_pair_ratio": str(pair_ratio(Q(1), Q(8), Q(8))),
            "authentic_clock_cubic_ratio": str(complete_factorial_ratio(Q(1), (Q(8),) * 3)),
            "exponential_diamond_1_0": str(exp_cell(1, 0)),
            "all_left_atom_proved_lower_bound": "1/5",
            "both_constant_paths_proved_mass_lower_bound": "2/5",
            "kernel_composed_mass": str(sum(raw_kl)),
            "kernel_reset_mass": str(z_k * z_l),
        },
        "numerical_diagnostics": {
            "executed": False,
            "count": 0,
            "reason": "No floating-point approximation enters an oracle verdict.",
        },
        "claims": {
            "finite_exact_checks": "VERIFIED_FINITE",
            "universal_theorems": "paper proofs required; not certified by this finite grid",
            "selected_BBP_cancellation": "OPEN",
            "pi_normality": "OPEN",
            "physical_or_cognitive_source_identification": "NOT CLAIMED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional destination for the same JSON printed on stdout")
    args = parser.parse_args()
    try:
        result = run()
        code = 0
    except Exception as error:
        result = {"schema": "succ.recursive-carrier-triangle.independent-oracle.v1",
                  "status": "failed", "error_type": type(error).__name__,
                  "error": str(error), "completed_exact_checks": dict(sorted(COUNTS.items())),
                  "numerical_diagnostics": {"executed": False, "count": 0}}
        code = 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
