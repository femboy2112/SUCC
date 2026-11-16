#!/usr/bin/env python3
"""Exact, independent finite audit of AL-01 in ABSOLUTE_LAGS.md.

Uses no production module, floating arithmetic, or transcendental oracle.
The deterministic sign vectors calibrate the finite formulas; they do not
certify any infinite-statistical premise about the BBP source.
"""

from fractions import Fraction
from hashlib import sha256
import json
from random import Random


SEED = 20261113
LENGTHS = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
TRIALS = 6


def run_audit():
    rng = Random(SEED)
    tensor_checks = 0
    weighted_cauchy_checks = 0
    vectors = []

    for n in LENGTHS:
        for trial in range(TRIALS):
            vector = [rng.choice((-1, 1)) for _ in range(n)]
            vectors.append(vector)
            correlation = [
                Fraction(sum(vector[i + lag] * vector[i]
                             for i in range(n - lag)), n)
                for lag in range(n)
            ]

            def gamma(length):
                return Fraction(1, length) + Fraction(2, length) * sum(
                    (1 - Fraction(lag, length)) * correlation[lag] ** 2
                    for lag in range(1, min(length, n))
                )

            windows = sorted({1, 2, 3, 5, n, max(1, n // 2), n + 3, 2 * n + 1})
            for window in windows:
                gamma_h = gamma(window)
                absolute_h = Fraction(2, window) * sum(
                    (1 - Fraction(lag, window)) * abs(correlation[lag])
                    for lag in range(1, min(window, n))
                )
                assert absolute_h ** 2 <= (
                    (1 - Fraction(1, window)) *
                    (gamma_h - Fraction(1, window))
                ), ("AL2", n, trial, window)
                weighted_cauchy_checks += 1

                subdivisions = sorted({
                    1, max(1, window // 3), max(1, window // 2), window
                })
                for short in subdivisions:
                    quotient, remainder = divmod(window, short)
                    a = Fraction(quotient * short, window) ** 2 * gamma(short)
                    b = Fraction(remainder, window) ** 2
                    residual = gamma_h - a - b
                    # sqrt(gamma_h) <= sqrt(a) + sqrt(b), checked rationally.
                    assert residual <= 0 or residual ** 2 <= 4 * a * b, (
                        "AL1", n, trial, window, short
                    )
                    tensor_checks += 1

    # This array has no common positive-definite autocorrelation realization.
    # Its square violates AL1 at a divisible pair, so the mutation must fail.
    large, short = 100, 10
    mutated = [Fraction(1) if lag == 0 or lag >= short else Fraction(0)
               for lag in range(large)]

    def mutated_gamma(length):
        return Fraction(1, length) + Fraction(2, length) * sum(
            (1 - Fraction(lag, length)) * mutated[lag] ** 2
            for lag in range(1, length)
        )

    assert large % short == 0
    mutation_rejected = mutated_gamma(large) > mutated_gamma(short)
    assert mutation_rejected
    assert tensor_checks == 1164

    vector_payload = json.dumps(vectors, separators=(",", ":")).encode("ascii")
    return {
        "status": "PASS",
        "scope": "Finite exact formula audit; no BBP statistical claim",
        "implementation": "Independent fractions.Fraction implementation",
        "random_seed": SEED,
        "lengths": list(LENGTHS),
        "trials_per_length": TRIALS,
        "vectors": len(vectors),
        "vector_payload_sha256": sha256(vector_payload).hexdigest(),
        "AL1_tensor_inequality_checks": tensor_checks,
        "AL2_weighted_cauchy_checks": weighted_cauchy_checks,
        "mutation": {
            "kind": "Non-positive-definite triangular correlation array",
            "H": large,
            "J": short,
            "G_H": str(mutated_gamma(large)),
            "G_J": str(mutated_gamma(short)),
            "rejected": mutation_rejected,
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
