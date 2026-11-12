"""Exact finite audit of the return-path family; emits a JSON receipt.

The direct oracle executes multiply, individual successor steps, and partial
division.  It does not use the implementation's gcd-normal-form evaluator.
Proofs, rather than the finite sweep, justify the universal statements.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import return_paths as rp


def literal_return(n: int, a: int, label: int) -> int | None:
    current = a * label
    for _ in range(n - a):
        current += 1
    return current // n if current % n == 0 else None


def literal_adjoint(n: int, a: int, label: int) -> int | None:
    current = n * label
    for _ in range(n - a):
        current -= 1
        if current < 1:
            return None
    return current // a if current % a == 0 else None


def trial_prime(n: int) -> bool:
    return n >= 2 and all(n % divisor for divisor in range(2, isqrt(n) + 1))


def totient_by_units(n: int) -> int:
    return sum(gcd(n, residue) == 1 for residue in range(1, n + 1))


def fraction_text(value: Q) -> str:
    return str(value)


def main() -> None:
    checks: Counter[str] = Counter()

    def check(condition: bool, family: str) -> None:
        if not condition:
            raise AssertionError(f"failed check in {family}")
        checks[family] += 1

    # All return channels, including the explicitly separate identity control.
    for n in range(2, 25):
        for a in range(1, n + 1):
            path = rp.ReturnPath(n, a)
            for label in range(1, 61):
                direct = literal_return(n, a, label)
                direct_adjoint = literal_adjoint(n, a, label)
                check(path.basis(label) == direct, "literal_return_vs_gcd")
                check(path.adjoint_basis(label) == direct_adjoint, "literal_adjoint_vs_gcd")
                check(rp.evaluate_word(label, path.word) == direct, "typed_word_vs_direct")
                if direct is not None:
                    check(path.adjoint_basis(direct) == label, "partial_inverse")
                if direct_adjoint is not None:
                    check(path.basis(direct_adjoint) == label, "partial_inverse")
            check(path.basis(1) == 1, "unit_anchor")
            check(path.forward(1) == n, "forward_arrival")
            if a == n:
                check(all(path.basis(m) == m for m in (1, 2, 19, 101)),
                      "identity_exclusion_control")
            else:
                check(path.initial_period > path.range_period >= 1,
                      "strict_pointed_contraction")

    for n in range(2, 81):
        literal_domains = Counter()
        for a in range(1, n):
            # The first non-unit admitted label gives the pointed period.
            first = next(m for m in range(2, n + 2)
                         if literal_return(n, a, m) is not None)
            literal_domains[first - 1] += 1
        check(dict(sorted(literal_domains.items())) == rp.domain_multiplicities(n),
              "domain_profile_vs_first_admitted_label")
        expected = {q: totient_by_units(q) for q in range(2, n + 1) if n % q == 0}
        check(rp.domain_multiplicities(n) == expected, "domain_totient_multiplicity")

    # Full finite periods for small n; the independent oracle counts the
    # actual divisibility tests rather than applying the gcd identity.
    for n in range(2, 129):
        projection = True
        for label in range(1, n + 2):
            count = sum((a * label + (n - a)) % n == 0 for a in range(1, n))
            check(count == rp.family_eigenvalue(n, label), "gram_vs_literal_domain_count")
            check(rp.family_eigenvalue(n, label + n) == count, "periodicity")
            normalized = Q(count, n - 1)
            projection = projection and normalized * normalized == normalized
            check(0 <= normalized <= 1, "normalized_gram_bounds")
        check(projection == trial_prime(n), "projection_vs_trial_division")

    holdouts = (137, 169, 221, 257, 289, 331, 437, 509, 667, 1009)
    holdout_receipts = []
    for n in holdouts:
        selected_a = sorted({1, 2, 3, n // 2, n - 1, n} |
                            {d for d in range(2, isqrt(n) + 1) if n % d == 0})
        labels = sorted({1, 2, 3, n, n + 1, 2*n + 1, n*n + 1, 10007} |
                        {1 + d for d in range(2, isqrt(n) + 1) if n % d == 0})
        for a in selected_a:
            path = rp.ReturnPath(n, a)
            for label in labels:
                check(path.basis(label) == literal_return(n, a, label),
                      "fresh_literal_return_holdout")
                check(path.adjoint_basis(label) == literal_adjoint(n, a, label),
                      "fresh_adjoint_holdout")
        defects = []
        for label in range(1, n + 1):
            count = sum((a * label + (n - a)) % n == 0 for a in range(1, n))
            check(count == rp.family_eigenvalue(n, label), "fresh_full_period_gram_holdout")
            if count not in (0, n - 1):
                defects.append((label, count))
        check((not defects) == trial_prime(n), "fresh_prime_projection_holdout")
        holdout_receipts.append({
            "n": n,
            "trial_prime": trial_prime(n),
            "normalized_gram_is_projection": not defects,
            "first_fractional_eigenvalue": None if not defects else {
                "basis_label": defects[0][0],
                "eigenvalue": fraction_text(Q(defects[0][1], n - 1)),
            },
        })

    non_norm_witnesses = []
    for n, a in ((3, 1), (5, 2), (6, 4), (9, 6), (15, 6), (37, 17)):
        path = rp.ReturnPath(n, a)
        for rounds in range(0, 7):
            for label in range(1, 101):
                image = label
                inverse_image = label
                for _ in range(rounds):
                    if image is not None:
                        image = literal_return(n, a, image)
                    if inverse_image is not None:
                        inverse_image = literal_adjoint(n, a, inverse_image)
                check(path.power_basis(label, rounds) == image, "iterated_word_vs_power")
                check(path.power_basis(label, rounds, adjoint=True) == inverse_image,
                      "iterated_adjoint_vs_power")
            if rounds:
                source = 1 + path.initial_period**rounds
                target = 1 + path.range_period**rounds
                check(path.power_basis(source, rounds) == target and target != 1,
                      "non_norm_convergence_witness")
                non_norm_witnesses.append({"n": n, "a": a, "rounds": rounds,
                                           "source": source, "target": target,
                                           "squared_error_on_unit_vector": 1})

    state = {1: Q(1, 3), 6: Q(1, 2), 11: Q(-2, 5), 26: Q(3, 7),
             126: Q(-5, 11), 626: Q(7, 13)}
    for n, a in ((3, 1), (5, 2), (6, 4), (15, 6)):
        path = rp.ReturnPath(n, a)
        for rounds in range(7):
            image = path.apply(state, rounds=rounds)
            image.pop(1, None)
            tail = sum((amplitude**2 for label, amplitude in state.items()
                        if label > 1 and (label - 1) % path.initial_period**rounds == 0), Q(0))
            check(rp.norm_squared(image) == tail, "finite_state_tail_identity")

    # Typed affine maps and their composition.  Counting hom(1,n) alone is
    # not a Yoneda naturality check, so pullback/associativity is explicit.
    for source in range(1, 8):
        for middle in range(source, 9):
            for target in range(middle, 11):
                for first in rp.affine_hom(source, middle):
                    for second in rp.affine_hom(middle, target):
                        composite = second.after(first)
                        check(composite in rp.affine_hom(source, target),
                              "typed_affine_composition")
                        check(composite(source) == target, "affine_endpoint")
                        for probe in (1, 2, 19):
                            check(composite(probe) == second(first(probe)),
                                  "affine_action_composition")
    affine_samples = (rp.Affine(1), rp.Affine(1, 1), rp.Affine(2),
                      rp.Affine(3, 2), rp.Affine(5, 4))
    for left in affine_samples:
        for middle in affine_samples:
            for right in affine_samples:
                check(left.after(middle).after(right) == left.after(middle.after(right)),
                      "affine_associativity")

    s, v = rp.Affine(1, 1), rp.Affine(2)
    route_s, route_v = s.after(v).after(s), s.after(v).after(v)
    check(route_s(1) == route_v(1) == 5, "same_vertex_trace_control")
    check((route_s(2), route_v(2)) == (7, 9), "parallel_label_discriminator")
    check(s.after(v).after(s) == rp.Affine(1, 3).after(v),
          "distinct_histories_equal_affine_map")

    plus, minus = {1: Q(1, 2), 2: Q(1, 2)}, {1: Q(1, 2), 2: Q(-1, 2)}
    interference = []
    for name, vector, expected in (
        ("unit", {1: 1}, (Q(1), Q(0), Q(1, 2))),
        ("orthogonal_outputs", {6: 1}, (Q(1, 2), Q(1, 2), Q(1, 2))),
        ("overlapping_nonunit_outputs", {6: 1, 11: 1}, (Q(3, 2), Q(1, 2), Q(1))),
    ):
        positive = rp.norm_squared(rp.coherent_sum(5, plus, vector))
        negative = rp.norm_squared(rp.coherent_sum(5, minus, vector))
        separate = rp.separate_intensity(5, plus, vector)
        check((positive, negative, separate) == expected, "coherent_interference_controls")
        check(rp.separate_intensity(5, minus, vector) == separate,
              "separate_intensity_sign_invariance")
        interference.append({"name": name, "input_squared_norm": fraction_text(rp.norm_squared(vector)),
                             "plus_coherent_intensity": fraction_text(positive),
                             "minus_coherent_intensity": fraction_text(negative),
                             "separate_intensity": fraction_text(separate)})

    offset_mutations_rejected = sum(
        rp.family_eigenvalue(n, label) != gcd(n, label) - 1
        for n in (3, 5, 6, 9, 37, 49) for label in range(1, 101))
    check(offset_mutations_rejected > 0, "missing_pointed_offset_mutation")
    check(literal_return(6, 3, 3) == 2 and literal_return(6, 1, 3) is None,
          "composite_common_domain_mutation")
    check(rp.ReturnPath(5, 5).basis(2) == 2 and
          all(path.basis(2) is None for path in rp.return_family(5)),
          "identity_channel_contamination_mutation")

    directory = Path(__file__).resolve().parent
    files = ("return_paths.py", "test_return_paths.py", "return_paths_probe.py")
    report = {
        "schema_version": 1,
        "status": "PASS",
        "finite_scope": "Exact integer/Fraction controls; no finite sweep proves the all-n theorem or strong limit.",
        "checks": dict(sorted(checks.items())),
        "total_checks": sum(checks.values()),
        "failures": 0,
        "implementation": "gcd normal form; exact finite rational states",
        "differential_oracle": "literal multiplication, repeated successor, partial division; independently written here",
        "initial_grid": {"n": [2, 24], "a": "1..n including identity control", "labels": [1, 60]},
        "full_gram_period_grid": {"n": [2, 128], "labels": "1..n+1"},
        "holdouts": holdout_receipts,
        "five": {"domain_multiplicities": rp.domain_multiplicities(5),
                 "outputs_from_e6": [path.basis(6) for path in rp.return_family(5)],
                 "normalized_gram_first_period": [fraction_text(rp.normalized_eigenvalue(5, m))
                                                  for m in range(1, 6)]},
        "six": {"domain_multiplicities": rp.domain_multiplicities(6),
                "normalized_gram_first_period": [fraction_text(rp.normalized_eigenvalue(6, m))
                                                 for m in range(1, 7)]},
        "non_norm_witnesses": non_norm_witnesses,
        "interference": interference,
        "parallel_arrow_control": {"root_trace": [1, 2, 4, 5],
                                   "affine_maps": [{"a": route_s.a, "b": route_s.b},
                                                   {"a": route_v.a, "b": route_v.b}],
                                   "outputs_at_source_2": [route_s(2), route_v(2)]},
        "mutation_controls": {"missing_m_minus_1_rejected_cases": offset_mutations_rejected,
                              "composite_common_domain_refuted": True,
                              "identity_contamination_detected": True},
        "source_sha256": {name: sha256((directory / name).read_bytes()).hexdigest() for name in files},
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
