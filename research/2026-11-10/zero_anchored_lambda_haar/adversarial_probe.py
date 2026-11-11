#!/usr/bin/env python3
"""Exact adversarial replay for the zero-anchored Lambda–Haar research.

Run from any directory. A failed check raises an exception and exits nonzero.
The JSON receipt reports finite calibrations, not asymptotic normality evidence.
The universal statements are proved separately in ADVERSARIAL.md.
"""
from __future__ import annotations

from dataclasses import replace
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


REPOSITORY = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY))

from observational_succ import c_monoid_succ_embedding as lc
from observational_succ import zero_anchored_lambda as z
from observational_succ.duck_bbp import forcing, tail_interval
from observational_succ.recursive_haar_pinbed import (
    canonical_law,
    digit_averaging_law,
    interval_w1,
    interval_w1_haar,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def prefix(n: int) -> F:
    return sum((forcing(j) / 16**j for j in range(1, n + 1)), F())


def finite_tail(n: int) -> F:
    return sum((forcing(n + j) / 16**j for j in range(1, n + 1)), F())


def altered_source(n: int, prefix_length: int) -> F:
    if n <= prefix_length:
        return forcing(n)
    return (forcing(n) - forcing(2*n - 1) / 16**(n - 1)
            - forcing(2*n) / 16**n)


def altered_source_probe() -> dict:
    cases = completions = 0
    lengths = (1, 2, 3, 7, 16)
    for length in lengths:
        alpha = prefix(2*length)
        require(alpha == prefix(length) + finite_tail(length) / 16**length,
                "finite rational completion target changed")
        state = F()
        for n in range(1, 41):
            value = altered_source(n, length)
            require(value > 0, "altered source lost positivity")
            require((value == forcing(n)) == (n <= length),
                    "altered source did not match exactly its declared prefix")
            state = 16*state + value
            if n >= length:
                require(state + finite_tail(n) == 16**n * alpha,
                        "altered source finite completion did not telescope")
                completions += 1
            cases += 1
    return {
        "passed": True,
        "source_cases": cases,
        "completion_identity_cases": completions,
        "prefix_lengths": list(lengths),
        "clock_range_inclusive": [1, 40],
        "universal_claims_proved_by_this_probe": False,
    }


def floor(value: F) -> int:
    return value.numerator // value.denominator


def rational_shadow_probe() -> dict:
    length, horizon, margin = 4, 64, 3
    source_terms = horizon + margin + 4
    lower, upper = tail_interval(0, source_terms)
    scale = 16**length
    require(floor(lower*scale) == floor(upper*scale),
            "source interval did not certify the requested prefix")
    radix_prefix = F(floor(lower*scale), scale)
    target_width = F(1, 16**(horizon + margin))
    require(upper - lower < target_width,
            "source interval too wide to construct the rational shadow")
    seed = radix_prefix + target_width/2 - (lower + upper)/2
    require(radix_prefix < lower + seed <= upper + seed
            < radix_prefix + target_width,
            "rational seed did not certify the terminating-orbit shadow")
    require(seed < 0 and abs(seed) < F(1, scale),
            "rational shadow seed is not the claimed small nonzero seed")
    phase_cases = 0
    for n in range(length, horizon + 1):
        phase_lower = 16**n * (lower + seed - radix_prefix)
        phase_upper = 16**n * (upper + seed - radix_prefix)
        require(0 < phase_lower <= phase_upper < F(1, 16**margin),
                "a certified shadow phase escaped the claimed zero-tail window")
        phase_cases += 1
    state = z.SourceState(length, 16**length * (seed + prefix(length)), seed)
    certificate = z.certify_state(state, require_zero=False)
    require(z.verify_source_certificate(certificate), "nonzero source replay failed")
    require(not certificate.original_zero, "nonzero seed was mislabeled original-zero")
    try:
        z.certify_state(state)
    except z.CompilerError:
        zero_rejected = True
    else:
        raise AssertionError("original-zero gate admitted the finite rational shadow")
    return {
        "passed": True,
        "prefix_length": length,
        "horizon": horizon,
        "margin": margin,
        "source_terms": source_terms,
        "certified_phase_windows": phase_cases,
        "exact_zero_gate_rejected_shadow": zero_rejected,
        "infinite_statistics_asserted": False,
    }


def quantization_probe() -> dict:
    starts = (F(), F(1, 3), F(1, 17), F(7, 31),
              F(1, 16), F(15, 16), F(137, 991))
    cases = 0
    for start in starts:
        phase = start
        points = []
        for count in range(1, 65):
            points.append(phase)
            phase = (16*phase) % 1
            law = canonical_law(points)
            distance = interval_w1_haar(law)
            defect = interval_w1(law, digit_averaging_law(law))
            require(distance >= F(1, 4*count), "empirical quantization floor failed")
            require(defect >= F(11, 64*count), "actual-orbit defect floor failed")
            cases += 1
    return {
        "passed": True,
        "cases": cases,
        "initial_phases": [str(value) for value in starts],
        "window_range_inclusive": [1, 64],
        "independent_wasserstein_implementation": False,
    }


class PretendEqual(str):
    """The exact hostile equality mechanism found in the initial compiler."""

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    __hash__ = str.__hash__


def compiler_forgery_probe() -> dict:
    certificate = z.certify_state(z.SourceState(0, F()))
    require(z.verify_source_certificate(certificate), "valid source certificate rejected")
    forged_certificate = replace(certificate, status=PretendEqual("NORMALITY_PROVED"))
    program = z.compile_term(z.Literal(F(5)))
    require(z.run(program).value == F(5), "valid literal program changed denotation")
    forged_program = replace(program, code=lc.CONST(PretendEqual("q:0/1")))
    rejected = {}
    for name, operation in (
        ("status_equality_spoof", lambda: z.verify_source_certificate(forged_certificate)),
        ("wrong_denotation_equality_spoof", lambda: z.run(forged_program)),
    ):
        try:
            operation()
        except z.CompilerError:
            rejected[name] = True
        else:
            raise AssertionError(f"compiler forgery accepted: {name}")
    return {"passed": True, "cases": len(rejected), "rejected": rejected,
            "valid_controls_passed": True}


def main() -> None:
    receipt = {
        "status": "FINITE_ADVERSARIAL_REPLAY_PASSED",
        "arithmetic": "fractions.Fraction",
        "altered_source": altered_source_probe(),
        "rational_seed_shadow": rational_shadow_probe(),
        "quantization_and_defect_floor": quantization_probe(),
        "compiler_equality_forgery": compiler_forgery_probe(),
        "normality_proved": False,
        "general_original_zero_contraction_proved": False,
    }
    bound_files = (
        "observational_succ/zero_anchored_lambda.py",
        "observational_succ/c_monoid_succ_embedding.py",
        "observational_succ/duck_bbp.py",
        "observational_succ/recursive_haar_pinbed.py",
    )
    receipt["implementation_sha256"] = {
        path: sha256((REPOSITORY / path).read_bytes()).hexdigest()
        for path in bound_files
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
