"""Exact, independent literal-word audit of the return-path construction.

This script imports no return-path implementation. Finite checks validate the
displayed identities on the declared domains; they do not prove universal
claims. Run from any directory. The JSON receipt is written beside this file.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def literal_return(n: int, a: int, m: int) -> int | None:
    """Apply V_a, then n-a successors, then the partial inverse of V_n."""
    if not (n >= 2 and 1 <= a < n and m >= 1):
        raise ValueError("Expected n>=2, 1<=a<n, m>=1")
    at = a * m
    for _ in range(n - a):
        at += 1
    if at % n:
        return None
    return at // n


def literal_adjoint(n: int, a: int, m: int) -> int | None:
    """Reverse the primitive word, including the unilateral-shift boundary."""
    if not (n >= 2 and 1 <= a < n and m >= 1):
        raise ValueError("Expected n>=2, 1<=a<n, m>=1")
    at = n * m
    for _ in range(n - a):
        if at == 1:
            return None
        at -= 1
    if at % a:
        return None
    return at // a


def sparse_apply(n: int, a: int, state: dict[int, Fraction]) -> dict[int, Fraction]:
    output: defaultdict[int, Fraction] = defaultdict(Fraction)
    for m, value in state.items():
        target = literal_return(n, a, m)
        if target is not None:
            output[target] += value
    return {m: value for m, value in output.items() if value}


def norm_squared(state: dict[int, Fraction]) -> Fraction:
    return sum((value * value for value in state.values()), Fraction())


def average(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    result = {m: (left.get(m, Fraction()) + right.get(m, Fraction())) / 2
              for m in left.keys() | right.keys()}
    return {m: value for m, value in result.items() if value}


def prime_by_trial_division(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def hom(m: int, n: int) -> tuple[tuple[int, int], ...]:
    return tuple((a, n - a * m) for a in range(1, n // m + 1))


def compose(f: tuple[int, int], g: tuple[int, int]) -> tuple[int, int]:
    """f after g."""
    a, b = f
    c, d = g
    return a * c, a * d + b


def histories(n: int) -> list[tuple[tuple[str, int], ...]]:
    """All strict-growth primitive histories 1->n; V_1 is excluded."""
    found: list[tuple[tuple[str, int], ...]] = []

    def visit(at: int, word: tuple[tuple[str, int], ...]) -> None:
        if at == n:
            found.append(word)
            return
        visit(at + 1, word + (("S", 1),))
        for d in range(2, n // at + 1):
            visit(d * at, word + (("V", d),))

    visit(1, ())
    return found


def semantics(word: tuple[tuple[str, int], ...]) -> tuple[int, int]:
    result = (1, 0)
    for generator, d in word:
        result = compose((1, 1) if generator == "S" else (d, 0), result)
    return result


def run() -> dict:
    checks = Counter()

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(name)
        checks[name] += 1

    # Prefix is chosen independently of the constructor implementation.
    for n in range(2, 65):
        for m in range(1, 131):
            admitted = []
            for a in range(1, n):
                observed = literal_return(n, a, m)
                g = gcd(n, a)
                numerator, denominator = a // g, n // g
                expected = (1 + numerator * ((m - 1) // denominator)
                            if (m - 1) % denominator == 0 else None)
                check("literal_vs_reduced_fraction", observed == expected)
                if observed is not None:
                    admitted.append(a)
                    check("adjoint_reverses_nonzero_column",
                          literal_adjoint(n, a, observed) == m)
                adjoint = literal_adjoint(n, a, m)
                if adjoint is not None:
                    check("return_reverses_nonzero_adjoint_column",
                          literal_return(n, a, adjoint) == m)
            check("family_diagonal_gcd", len(admitted) == gcd(n, m - 1) - 1)

        eigenvalues = [Fraction(sum(literal_return(n, a, m) is not None
                                    for a in range(1, n)), n - 1)
                       for m in range(1, n + 2)]
        observed_projection = all(value * value == value for value in eigenvalues)
        check("projection_iff_trial_prime", observed_projection == prime_by_trial_division(n))
        for a in range(1, n):
            check("unit_anchor", literal_return(n, a, 1) == 1)
            outputs = [literal_return(n, a, m) for m in range(1, 131)]
            nonzero = [m for m in outputs if m is not None]
            check("finite_columns_orthogonal", len(nonzero) == len(set(nonzero)))

    # Holdouts were not used to formulate the candidate identity.
    holdout_ns = (67, 97, 101, 121, 143, 169, 221, 257)
    for n in holdout_ns:
        for m in (1, 2, n, n + 1, 2 * n + 1, n * n + 1, 10007):
            count = sum(literal_return(n, a, m) is not None for a in range(1, n))
            check("holdout_family_diagonal", count == gcd(n, m - 1) - 1)

    for n in (3, 4, 5, 6, 9, 15):
        for a in range(1, n):
            g = gcd(n, a)
            u, v = a // g, n // g
            for r in range(1, 5):
                for k in range(1, 6):
                    at = 1 + v ** r * k
                    for _ in range(r):
                        at = literal_return(n, a, at)
                        if at is None:
                            raise AssertionError("iteration unexpectedly vanished")
                    check("iteration_and_norm_one_witness", at == 1 + u ** r * k)

    history_counts = {}
    for n in range(1, 11):
        words = histories(n)
        images = set(map(semantics, words))
        history_counts[str(n)] = {"literal_histories": len(words), "affine_maps": len(images)}
        check("history_normal_forms", images == set(hom(1, n)))
    check("five_has_seven_histories", history_counts["5"] == {"literal_histories": 7, "affine_maps": 5})

    for n in range(1, 11):
        for m in range(1, n + 1):
            check("hom_cardinality", len(hom(m, n)) == n // m)
            for f in hom(m, n):
                check("left_identity", compose((1, 0), f) == f)
                check("right_identity", compose(f, (1, 0)) == f)
                for k in range(1, m + 1):
                    for g in hom(k, m):
                        fg = compose(f, g)
                        check("typed_composition", fg in hom(k, n))
                        for j in range(1, k + 1):
                            for h in hom(j, k):
                                check("associativity", compose(fg, h) == compose(f, compose(g, h)))

    # Two histories with the same vertices have distinct typed arrows.
    p = (("S", 1), ("V", 2), ("S", 1))
    q = (("V", 2), ("V", 2), ("S", 1))
    check("same_vertices_distinct_actions", semantics(p) == (2, 3) and semantics(q) == (4, 1))
    check("word_quotient_braid", semantics(p) == semantics((("V", 2), ("S", 1), ("S", 1), ("S", 1))))
    check("word_quotient_multiplication", semantics(q) == semantics((("V", 4), ("S", 1))))

    # The root-restricted presheaf permits a swap which is not natural.
    two_routes = hom(1, 2)
    swap = {two_routes[0]: two_routes[1], two_routes[1]: two_routes[0]}
    identity_two = hom(2, 2)[0]
    for route in two_routes:
        check("root_swap_fails_naturality",
              swap[compose(identity_two, route)] != compose(identity_two, route))
    check("root_restriction_not_full", len(hom(2, 2)) == 1 and len(two_routes) ** len(two_routes) == 4)

    x = {6: Fraction(3, 5), 11: Fraction(4, 5)}
    left, right = sparse_apply(5, 1, x), sparse_apply(5, 2, x)
    altered = {m: (-value if m == 3 else value) for m, value in left.items()}
    intensity = norm_squared(average(left, right))
    altered_intensity = norm_squared(average(altered, right))
    separate = (norm_squared(left) + norm_squared(right)) / 4
    check("phase_control_unit_input", norm_squared(x) == 1)
    check("phase_control_intensities", (intensity, altered_intensity, separate)
          == (Fraction(37, 50), Fraction(13, 50), Fraction(1, 2)))
    check("phase_control_individual_norms", norm_squared(altered) == norm_squared(left) == 1)

    # Mutated claims must fail on named witnesses.
    check("reject_missing_point_offset", gcd(5, 1 - 1) - 1 != gcd(5, 1) - 1)
    check("reject_rounded_partial_inverse", literal_return(5, 1, 2) is None and (2 + 4) // 5 == 1)
    check("reject_identity_in_nontrivial_family", Fraction(5, 4) ** 2 != Fraction(5, 4))
    check("reject_composite_common_domain", literal_return(6, 3, 3) == 2 and literal_return(6, 1, 3) is None)

    output = {
        "status": "PASS",
        "total_checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "independence": "No constructor imports. Literal generator words and sparse finite maps are compared with separately derived gcd and category identities. Same-model review is not an external proof witness.",
        "prefix": {"n": [2, 64], "source_labels": [1, 130]},
        "holdout_ns": list(holdout_ns),
        "history_counts": history_counts,
        "phase_countermodel": {"input": {"6": "3/5", "11": "4/5"},
                               "authentic_coherent_intensity": str(intensity),
                               "altered_coherent_intensity": str(altered_intensity),
                               "separate_intensity": str(separate)},
        "scope": "Finite implementation and counterexample audit only. Universal results are proved in the accompanying mathematical documents.",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = ROOT / "receipts" / "RETURN_PATH_INDEPENDENT_AUDIT.json"
    destination.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    return output


if __name__ == "__main__":
    result = run()
    print(json.dumps({"status": result["status"], "total_checks": result["total_checks"]}, sort_keys=True))
