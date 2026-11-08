"""Predeclared coefficient-sensitive source clock vs index-only control.

Research-only finite audit of SOURCE_CLOCK_PREREG.md committed before evaluation.
A source clock is not a source-uniqueness certificate or a pi-normality proof.
"""
from __future__ import annotations
import json
import math
from fractions import Fraction
from joint_entropy import (
    four_pole, certified_source_digits, pole_clock, mealy_run,
    decode_reversible_observer, block_entropy,
)

PREREG_COMMIT = "a0289b84295b4fdef3a7f3678d6c3cfdd5ea881c"


def denominator(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("n>=1 integer required")
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def numerator(n: int) -> int:
    """The original FOUR-pole source cleared by its exact denominator."""
    if type(n) is not int or n < 1:
        raise ValueError("n>=1 integer required")
    return 120*n*n-89*n+16


def index_clock(n: int) -> int:
    return pole_clock(n, 7)


def coefficient_clock(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 integer required")
    return numerator(n+1) % 7


def mutant_numerator(n: int) -> int:
    """Weight mutation 4 -> 5 on the (8*n-7) first signed pole."""
    return numerator(n) + (2*n-1)*(4*n-1)*(8*n-3)


def mutant_clock(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 integer required")
    return mutant_numerator(n+1) % 7


def verified_source_clock() -> bool:
    """Check formula equality for many exact Fraction indices and two mutants."""
    for n in range(1, 201):
        if denominator(n)*four_pole(n) != numerator(n):
            return False
        mutated = four_pole(n) + Fraction(1,8*n-7)
        if denominator(n)*mutated != mutant_numerator(n):
            return False
    return True


def verdict(a: float, b: float) -> str:
    """Finite diagnostic: compare output deficit a vs input deficit b."""
    return "worse" if a > b + 1e-12 else "better" if a < b - 1e-12 else "equal"


def run() -> dict:
    assert verified_source_clock(), "exact four-pole clearing failed"
    assert all(coefficient_clock(i+7) == coefficient_clock(i) for i in range(77))
    assert all(mutant_clock(i+7) == mutant_clock(i) for i in range(77))
    first_mismatch = next(i for i in range(77) if coefficient_clock(i) != mutant_clock(i))
    digits, _ = certified_source_digits(1536)
    table = []
    for N in (384,768,1536):
        d = digits[:N]
        old_tape = tuple(index_clock(i) for i in range(N))
        authentic_tape = tuple(coefficient_clock(i) for i in range(N))
        mutant_tape = tuple(mutant_clock(i) for i in range(N))
        o_old,_ = mealy_run(d, old_tape)
        o_auth,_ = mealy_run(d, authentic_tape)
        o_mut,_ = mealy_run(d, mutant_tape)
        assert decode_reversible_observer(o_auth,authentic_tape) == d
        assert decode_reversible_observer(o_mut,mutant_tape) == d
        assert decode_reversible_observer(o_old,old_tape) == d
        assert o_auth != o_mut
        assert decode_reversible_observer(o_auth,mutant_tape) != d
        rows = {}
        for k in (1,2):
            input_debt=k*math.log(16)-block_entropy(d,k)
            old_debt=k*math.log(16)-block_entropy(o_old,k)
            authentic_debt=k*math.log(16)-block_entropy(o_auth,k)
            mutant_debt=k*math.log(16)-block_entropy(o_mut,k)
            rows[f"k_{k}"] = {
                "input_deficit_nats_float":round(input_debt,12),
                "index_only_deficit_nats_float":round(old_debt,12),
                "coefficient_clock_deficit_nats_float":round(authentic_debt,12),
                "mutant_clock_deficit_nats_float":round(mutant_debt,12),
                "coefficient_vs_input":verdict(authentic_debt,input_debt),
                "coefficient_vs_index":verdict(authentic_debt,old_debt),
            }
        table.append({"N":N,**rows})
    return {
        "status":"OBSERVED-FINITE", "pi_normality":"OPEN",
        "preregistration_head_before_measurement":PREREG_COMMIT,
        "exact_original_four_pole_checks":200,
        "clock_period":7,
        "original_clock_first_period":[coefficient_clock(i) for i in range(7)],
        "index_clock_first_period":[index_clock(i) for i in range(7)],
        "mutant_clock_first_period":[mutant_clock(i) for i in range(7)],
        "mutant_first_clock_mismatch_n":first_mismatch,
        "reversibility_for_all_3_clocks":True,
        "wrong_clock_replay_rejects_original":True,
        "finite_entropy_measurements":table,
        "entropy_float_diagnostic_not_rigorous_signed_saving":True,
        "source_clock_alone_does_not_uniquely_identify_source":True,
    }

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
