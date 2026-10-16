#!/usr/bin/env python3
"""Replay scoped proof-access examples; paper authority is kept explicit."""
import json
import sys
from dataclasses import asdict
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.minimal_observation import (
    FiniteObservation, compile_factorization, replay_factorization,
    chi4_observation, polynomial_descent,
)
from observational_succ.minimal_weil_window import minimum_arithmetic_window, autocorrelation_atom_witness


def main():
    positive = FiniteObservation("finite-whole-source", 0, (0, 0, 1), (2, 2, 3))
    negative = FiniteObservation("finite-whole-source", 0, (0, 0), (0, 1))
    capsules = [compile_factorization(p) for p in (positive, negative)]
    assert all(replay_factorization(p, c) for p, c in zip((positive, negative), capsules))
    report = {"finite_certificates": [asdict(c) for c in capsules],
              "chi4": [chi4_observation(n) for n in (1, 2, 3, 4, 8, 10)],
              "false_binomial_descent": polynomial_descent((0, 0, 1), 2),
              "first_prime_window": minimum_arithmetic_window(Fraction(1, 2)),
              "smooth_autocorrelation_witness": autocorrelation_atom_witness(Fraction(1, 2), 2),
              "RH_proved": False, "Lean_verification_performed_by_this_probe": False}
    print(json.dumps(report, indent=2, default=str, sort_keys=True))


if __name__ == "__main__":
    main()
