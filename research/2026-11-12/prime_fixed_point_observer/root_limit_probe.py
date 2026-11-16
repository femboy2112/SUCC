"""Exact finite controls for the centered common root and limit topology.

This standalone oracle does not import return_paths.  It uses the l2(N_0)
basis epsilon_k and executes centered partial divisions directly.
For coprime q > r >= 1, T(q,r) epsilon_(q*k) = epsilon_(r*k), otherwise 0.
All coefficients, moments, and interior-disk evaluations are rational.

The common fixed-line and strong-limit assertions require the analytic tail
proof.  These finite controls calibrate identities and explicit failures;
they do not measure proof hardness or establish a universal eigenvector for
operators outside the declared family.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


def integer(value: int, name: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def parameters(q: int, r: int) -> None:
    integer(q, "q", 2)
    integer(r, "r", 1)
    if r >= q or gcd(q, r) != 1:
        raise ValueError("require coprime q > r >= 1")


def step(q: int, r: int, label: int) -> int | None:
    """One centered return; None denotes the zero vector, not epsilon_0."""
    parameters(q, r)
    integer(label, "basis label")
    return r * (label // q) if label % q == 0 else None


def repeat_step(q: int, r: int, label: int, rounds: int) -> int | None:
    """Literal iteration, independent of the closed q**rounds formula."""
    parameters(q, r)
    integer(label, "basis label")
    integer(rounds, "rounds")
    result = label
    for _ in range(rounds):
        result = step(q, r, result)
        if result is None:
            break
    return result


def closed_power(q: int, r: int, label: int, rounds: int) -> int | None:
    parameters(q, r)
    integer(label, "basis label")
    integer(rounds, "rounds")
    quotient, remainder = divmod(label, q**rounds)
    return None if remainder else r**rounds * quotient


def state(values: dict[int, int | Q]) -> dict[int, Q]:
    result = {}
    for label, value in values.items():
        integer(label, "basis label")
        if isinstance(value, bool) or not isinstance(value, (int, Q)):
            raise TypeError("coefficients must be exact integers or Fractions")
        if value:
            result[label] = Q(value)
    return result


def apply(q: int, r: int, values: dict[int, int | Q], rounds: int = 1) -> dict[int, Q]:
    parameters(q, r)
    integer(rounds, "rounds")
    output = {}
    for label, value in state(values).items():
        image = repeat_step(q, r, label, rounds)
        if image is not None:
            output[image] = output.get(image, Q(0)) + value
    return {label: value for label, value in output.items() if value}


def square_norm(values: dict[int, int | Q]) -> Q:
    return sum((value**2 for value in state(values).values()), Q(0))


def polynomial(values: dict[int, int | Q], z: Q) -> Q:
    if not isinstance(z, Q):
        raise TypeError("evaluation point must be an exact Fraction")
    return sum((value * z**label for label, value in state(values).items()), Q(0))


def valuation(q: int, label: int) -> int:
    integer(q, "q", 2)
    integer(label, "nonzero label", 1)
    depth = 0
    while label % q == 0:
        label //= q
        depth += 1
    return depth


def report() -> dict:
    checks: Counter[str] = Counter()

    def verify(condition: bool, family: str) -> None:
        if not condition:
            raise AssertionError(f"failed check: {family}")
        checks[family] += 1

    pairs = tuple((q, r) for q in range(2, 10) for r in range(1, q)
                  if gcd(q, r) == 1)
    for q, r in pairs:
        verify(step(q, r, 0) == 0, "common_root")
        for label in range(101):
            verify(step(q, r, label) == label if label == 0
                   else step(q, r, label) != label, "basis_fixed_points")
            for rounds in range(6):
                verify(repeat_step(q, r, label, rounds) ==
                       closed_power(q, r, label, rounds), "literal_vs_closed_power")

    # J e_(k+1)=epsilon_k.  Original dilation and pointed dilation must not
    # be confused after this unitary relabeling of the orthonormal basis.
    for label in range(101):
        original = label + 1
        verify((original + 1) - 1 == label + 1, "recentered_successor")
        for d in range(1, 11):
            verify(d * original - 1 == d * label + d - 1,
                   "recentered_original_dilation_affine_offset")
            verify((1 + d * (original - 1)) - 1 == d * label,
                   "recentered_pointed_dilation")
    verify(2 * (0 + 1) - 1 != 2 * 0, "dropped_d_minus_1_mutation")

    # Sparse commutator [S,E0]=S E0-E0 S, checked on a complete finite basis
    # window.  The formula has a separate all-label derivation in the note.
    def shift(values):
        return {label + 1: value for label, value in state(values).items()}

    def root_projection(values):
        values = state(values)
        return {0: values[0]} if 0 in values else {}

    for label in range(101):
        unit = {label: Q(1)}
        first = shift(root_projection(unit))
        second = root_projection(shift(unit))
        commutator = dict(first)
        for target, coefficient in second.items():
            commutator[target] = commutator.get(target, Q(0)) - coefficient
        commutator = {target: coefficient for target, coefficient in commutator.items()
                      if coefficient}
        verify(commutator == ({1: Q(1)} if label == 0 else {}),
               "successor_root_commutator")
    verify(shift({0: 1}) != {0: Q(1)}, "root_not_fixed_by_successor")

    window_cases = 0
    strict_boundary_witnesses = []
    for q, r in pairs:
        for rounds in range(1, 5):
            cutoff = q**rounds
            # Use both a short ordinary prefix and the largest permitted
            # basis label, without building giant finite matrices.
            for maximum in sorted({0, 1, min(30, cutoff - 1), cutoff - 1}):
                if maximum >= cutoff:
                    continue
                labels = sorted(set(range(min(maximum, 40) + 1)) | {maximum})
                for label in labels:
                    verify(repeat_step(q, r, label, rounds) == (0 if label == 0 else None),
                           "finite_window_exactness")
                window_cases += 1
            image = repeat_step(q, r, cutoff, rounds)
            verify(image == r**rounds and image != 0, "strict_window_threshold")
            verify(square_norm(apply(q, r, {cutoff: 1}, rounds)) == 1,
                   "norm_one_escaping_witness")
            if (q, r) in ((2, 1), (3, 2), (5, 3)):
                strict_boundary_witnesses.append({
                    "q": q, "r": r, "rounds": rounds,
                    "input_label": cutoff, "output_label": image,
                    "squared_error_after_root_projection": 1,
                })

    # Coefficient tails and moment budgets are exact finite fixtures.  C^2
    # is recorded directly so no irrational square-root rounding is needed.
    fixtures = (
        {0: Q(2, 3), 1: Q(1, 5), 2: Q(-2, 7), 4: Q(3, 11), 8: Q(-4, 13)},
        {0: Q(-1, 2), 3: Q(2, 5), 9: Q(-3, 7), 27: Q(4, 11), 81: Q(-5, 13)},
        {0: Q(1), 5: Q(1, 3), 25: Q(2, 9), 125: Q(-4, 27), 625: Q(5, 81)},
        {1: Q(3, 5), 6: Q(4, 5), 17: Q(-5, 12), 49: Q(7, 15)},
    )
    moment_examples = []
    for index, fixture in enumerate(fixtures):
        for q, r in ((2, 1), (3, 2), (5, 2), (5, 3), (7, 4)):
            for rounds in range(6):
                image = apply(q, r, fixture, rounds)
                constant = image.pop(0, Q(0))
                verify(constant == fixture.get(0, Q(0)), "root_coefficient_preserved")
                actual_error_squared = square_norm(image)
                direct_tail = sum((value**2 for label, value in fixture.items()
                                   if label > 0 and label % q**rounds == 0), Q(0))
                verify(actual_error_squared == direct_tail, "exact_tail_identity")
                for s in (1, 2):
                    moment_squared = sum((Q(label)**(2*s) * value**2
                                          for label, value in fixture.items() if label > 0), Q(0))
                    error_bound_squared = moment_squared / Q(q)**(2*s*rounds)
                    verify(actual_error_squared <= error_bound_squared,
                           "weighted_moment_bound")
                    if index == 1 and (q, r, rounds, s) == (3, 2, 2, 1):
                        moment_examples.append({
                            "fixture": index, "q": q, "r": r, "rounds": rounds, "s": s,
                            "C_squared": str(moment_squared),
                            "error_squared": str(actual_error_squared),
                            "bound_squared": str(error_bound_squared),
                        })

    # Hardy H2 identification epsilon_k <-> z^k.  Evaluating finite
    # polynomials at rational real z exercises the coefficient identity
    # without making unsupported assertions about numerical boundary limits.
    for fixture in fixtures:
        for q, r in ((2, 1), (3, 2), (5, 3)):
            for rounds in range(5):
                expected_coefficients = {
                    r**rounds * (label // q**rounds): coefficient
                    for label, coefficient in fixture.items() if label % q**rounds == 0
                }
                image = apply(q, r, fixture, rounds)
                verify(image == expected_coefficients, "hardy_coefficient_extraction")
                for rho in (Q(1, 2), Q(3, 4), Q(-2, 3)):
                    direct = sum((coefficient * rho**(r**rounds * (label // q**rounds))
                                  for label, coefficient in fixture.items()
                                  if label % q**rounds == 0), Q(0))
                    verify(polynomial(image, rho) == direct, "hardy_rational_evaluation")

    escaping_analytic_witnesses = []
    for rho in (Q(1, 2), Q(3, 4)):
        previous_value = Q(1)
        for rounds in range(1, 7):
            q, r = 3, 2
            image = apply(q, r, {q**rounds: 1}, rounds)
            value = polynomial(image, rho)
            verify(image == {r**rounds: Q(1)}, "escaping_hardy_monomial")
            verify(square_norm(image) == 1, "escaping_hardy_norm")
            verify(value == rho**(r**rounds), "interior_disk_supremum_value")
            verify(0 < value < previous_value and value <= rho**rounds,
                   "interior_disk_decay_exact")
            previous_value = value
            escaping_analytic_witnesses.append({
                "q": q, "r": r, "rounds": rounds,
                "input_exponent": q**rounds, "output_exponent": r**rounds,
                "radius": str(rho), "disk_supremum": str(value), "H2_norm_squared": 1,
            })
    # The stated analytic escape requires r>1.  With r=1 the output is
    # always z, and the compact-disk norm need not tend to zero.
    for rounds in range(1, 7):
        image = apply(2, 1, {2**rounds: 1}, rounds)
        verify(image == {1: Q(1)} and polynomial(image, Q(1, 2)) == Q(1, 2),
               "r_equals_one_nondecay_control")

    # A declared sup-norm observation interface on |z|<=rho attenuates the
    # coefficient of z^N by rho^N.  Its two worst-case error balls overlap
    # at the midpoint once 2*epsilon >= rho^N.  This is an interface
    # conditioning statement, not a lower bound on proof or computation.
    coefficient_conditioning = []
    for rho in (Q(1, 2), Q(2, 3)):
        for exponent in (1, 2, 5, 20):
            monomial = {exponent: Q(1)}
            midpoint = {exponent: Q(1, 2)}
            distance = rho**exponent
            overlap_error = distance / 2
            separating_error = distance / 3
            amplification = 1 / distance
            verify(square_norm(monomial) == 1, "conditioning_H2_norm")
            verify(polynomial(monomial, rho) == distance,
                   "conditioning_sup_disk_norm")
            # Each difference from the midpoint is +/-z^N/2, whose exact
            # supremum on this disk is distance/2.
            midpoint_to_zero = polynomial(midpoint, rho)
            midpoint_to_monomial = polynomial(monomial, rho) - polynomial(midpoint, rho)
            verify(midpoint_to_zero == overlap_error,
                   "conditioning_midpoint_zero_hypothesis")
            verify(midpoint_to_monomial == overlap_error,
                   "conditioning_midpoint_monomial_hypothesis")
            verify(2 * overlap_error == distance,
                   "conditioning_error_balls_touch")
            verify(distance - 2 * separating_error == distance / 3 > 0,
                   "conditioning_error_balls_disjoint")
            verify(amplification * distance == 1,
                   "conditioning_coefficient_amplification")
            coefficient_conditioning.append({
                "radius": str(rho), "exponent": exponent,
                "H2_norm_squared": 1, "sup_disk_distance": str(distance),
                "midpoint_observation": "z^N/2",
                "overlap_error": str(overlap_error),
                "separating_error": str(separating_error),
                "separation_gap": str(distance - 2 * separating_error),
                "coefficient_error_amplification": str(amplification),
            })

    depth_receipts = []
    for label in (8, 9):
        depth = valuation(2, label)
        history = [repeat_step(2, 1, label, rounds) for rounds in range(depth + 2)]
        verify(history[depth] is not None and history[depth + 1] is None,
               "valuation_survival_depth")
        depth_receipts.append({"label": label, "v2": depth,
                               "iterations_until_rejection": depth + 1,
                               "history": history})
    verify(8 < 9 and valuation(2, 8) > valuation(2, 9), "label_order_not_depth_order")

    invalid_cases = ((1, 1), (2, 2), (4, 2), (3, 0))
    for q, r in invalid_cases:
        rejected = False
        try:
            step(q, r, 0)
        except (TypeError, ValueError):
            rejected = True
        verify(rejected, "invalid_parameter_control")
    # Noncoprime (q,r)=(4,2) kills the claimed q**j formula: at j=2,
    # label8 maps 8->4->2, even though16 does not divide8.
    noncoprime_literal = 2 * ((2 * (8 // 4)) // 4)
    verify(noncoprime_literal == 2 and 8 % (4**2) != 0, "coprimality_is_load_bearing")

    return {
        "schema": "succ-centered-root-limit-v1",
        "status": "PASS", "total_checks": sum(checks.values()), "failures": 0,
        "checks": dict(sorted(checks.items())),
        "finite_scope": {
            "coprime_pairs": [list(pair) for pair in pairs],
            "initial_labels": [0, 100], "power_rounds": [0, 5],
            "finite_window_cases": window_cases,
            "window_sampling": "All labels through min(M,40), plus M; universal equality has a separate proof.",
            "amplitudes": "exact real rational", "moment_orders": [1, 2],
            "analytic_fixture_radii": ["1/2", "3/4", "-2/3"],
        },
        "centering": {
            "unitary": "J e_(k+1)=epsilon_k",
            "successor": "k -> k+1",
            "original_dilation": "k -> d*k+d-1",
            "pointed_dilation": "k -> d*k",
            "common_return_fixed_line": "C epsilon_0, proved by the single T_(2,1) tail argument",
            "successor_commutator": "[S,E0]=|1><0|",
            "scope": "epsilon_0 is not fixed by successor; the claim is relative to the return family",
        },
        "tail_identity": "||(T_(q,r)^j-E0)x||^2=sum_(k>=1)|x_(q^j*k)|^2",
        "moment_bound": "error^2 <= C^2*q^(-2*s*j) when sum_(k>=1) k^(2*s)|x_k|^2 <= C^2",
        "moment_examples": moment_examples,
        "strict_threshold_witnesses": strict_boundary_witnesses,
        "hardy_coefficient_formula": "T^j f(z)=sum_(k>=0)c_(q^j*k) z^(r^j*k)",
        "escaping_analytic_witnesses": escaping_analytic_witnesses,
        "coefficient_conditioning": {
            "case_count": len(coefficient_conditioning),
            "observation_interface": "The entire function on |z|<=rho, with worst-case sup-norm error <=epsilon",
            "hypotheses": "0 versus z^N",
            "uniform_distinguishability": "2*epsilon < rho^N; otherwise the midpoint z^N/2 fits both hypotheses",
            "coefficient_error_amplification": "rho^(-N)",
            "scope": "measurement-interface conditioning, not proof/computational lower bound",
            "cases": coefficient_conditioning,
        },
        "depth_counterexample": depth_receipts,
        "proof_boundary": "Finite controls certify only their declared exact cases. Common fixed space, strong convergence, "
                          "and universal moment bounds require the displayed proofs. Uniform H2 operator convergence "
                          "fails. No universal proof-hardness measure is defined or inferred.",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
