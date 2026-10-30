#!/usr/bin/env python3
"""Independent exact finite oracle for the inertial-information boundary.

No import of observational_succ.inertial_information_boundary is permitted.
The declared codec is reconstructed with a separate bit algorithm; preparation
words are composed as affine matrices; eventual phase kernels use prime
valuations rather than the production gcd loop.  All phase tests compare exact
rational exponents modulo one.  No logarithm or trigonometric approximation
certifies a result.  Universal statements require the accompanying paper proofs.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.succ_internal_matrix_walk import authentic_r


PARENT = "b6a3815ceb505de0b1f570eae3ff5be75cdbe99c"
FORBIDDEN = "observational_succ.inertial_information_boundary"
BASES = (2, 3, 10, 16, 27)
FREQUENCIES = (-7, 1, 5)
SEEDS = (Q(-16), Q(-1), Q(0), Q(1), Q(1, 16), Q(1, 256), Q(1, 3), Q(-7, 40))
STARTS = (0, 1, 2, 5)
SOURCE_HOLDOUTS = (37, 61, 97)
COUNTS: Counter[str] = Counter()


def check(condition, group: str, context: str = "") -> None:
    if not condition:
        raise AssertionError(f"{group}: {context}")
    COUNTS[group] += 1


def encode_integer(value: int) -> str:
    """Independent divmod bit construction of the declared signed gamma code."""
    if type(value) is not int:
        raise ValueError("integer required")
    if value == 0:
        return "0"
    quotient = abs(value)
    reverse_bits = []
    while quotient:
        quotient, remainder = divmod(quotient, 2)
        reverse_bits.append(str(remainder))
    magnitude_bits = "".join(reversed(reverse_bits))
    return "1" + ("1" if value < 0 else "0") + "0" * (len(reverse_bits) - 1) + magnitude_bits


def decode_integer(word: str) -> int:
    """Cursor parser, rejecting truncation and data after one complete word."""
    if not isinstance(word, str) or not word or set(word) - {"0", "1"}:
        raise ValueError("nonempty binary word required")
    if word[0] == "0":
        if len(word) != 1:
            raise ValueError("trailing bits")
        return 0
    if len(word) < 3:
        raise ValueError("missing signed gamma payload")
    negative = word[1] == "1"
    cursor = 2
    payload_width = 1
    while cursor < len(word) and word[cursor] == "0":
        payload_width += 1
        cursor += 1
    if cursor + payload_width != len(word):
        raise ValueError("invalid gamma payload length")
    value = 0
    for digit in word[cursor:]:
        value = 2 * value + (digit == "1")
    if value == 0:
        raise ValueError("nonzero magnitude required")
    return -value if negative else value


def prefix_free(words) -> bool:
    """Trie implementation independent of the production sorted-neighbor test."""
    root = {}
    terminal = object()
    for word in words:
        branch = root
        if terminal in branch:
            return False
        for bit in word:
            if terminal in branch:
                return False
            branch = branch.setdefault(bit, {})
        if branch:
            return False
        branch[terminal] = True
    return True


def factor_integer(value: int) -> dict[int, int]:
    factors = {}
    trial = 2
    while trial * trial <= value:
        while value % trial == 0:
            factors[trial] = factors.get(trial, 0) + 1
            value //= trial
        trial += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def valuation_start(offset: Q, base: int, frequency: int) -> int | None:
    denominator_factors = factor_integer((frequency * offset).denominator)
    base_factors = factor_integer(base)
    if set(denominator_factors) - set(base_factors):
        return None
    return max(((power + base_factors[prime] - 1) // base_factors[prime]
                for prime, power in denominator_factors.items()), default=0)


def iterate(forcing, seed: Q, base: int) -> tuple[Q, ...]:
    state = seed
    result = [state]
    for value in forcing:
        state = base * state + value
        result.append(state)
    return tuple(result)


def direct_green(forcing, seed: Q, base: int, time: int) -> Q:
    return base ** time * seed + sum(
        (base ** (time - k) * forcing[k - 1] for k in range(1, time + 1)), Q(0))


def rational_source(n: int) -> Q:
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def source_extension(a: Q) -> Q:
    return 4 / a - 2 / (a + 3) - 1 / (a + 4) - 1 / (a + 5)


def hostile_source(n: int, shift: Q) -> Q:
    return 16 / (8 * n - 7 + shift) ** 2 - 1 / (8 * n + 1 + shift) ** 2


def hostile_closed(time: int, shift: Q) -> Q:
    return Q(16) ** time / (shift + 1) ** 2 - 1 / (8 * time + shift + 1) ** 2


def source_passport(states) -> bool:
    if not states or states[0] != 0:
        return False
    return all(states[n] - 16 * states[n - 1] == rational_source(n)
               for n in range(1, len(states)))


def affine_program(word: str, base: int) -> tuple[int, int, int]:
    """Compose affine maps (multiplier,offset); retain paid displacement count."""
    operators = {"R": (base, 0, 0), "N": (-1, 0, 0),
                 "+": (1, 1, 1), "-": (1, -1, 1)}
    multiplier, offset, cost = 1, 0, 0
    for symbol in word:
        a, c, k = operators[symbol]
        multiplier, offset, cost = a * multiplier, a * offset + c, cost + k
    return multiplier, offset, cost


def run() -> dict:
    check(FORBIDDEN not in sys.modules, "production_module_not_imported")

    # Declared code: the ranking belongs to this protocol, not every codebook.
    expected = {0: "0", 1: "101", -1: "111", -16: "11000010000"}
    for integer, word in expected.items():
        check(encode_integer(integer) == word and decode_integer(word) == integer,
              "exact_code_examples")
    integer_domain = sorted(set(range(-257, 258))
                            | {sign * 2 ** power for sign in (-1, 1) for power in range(17)})
    codebook = {n: encode_integer(n) for n in integer_domain}
    for integer, word in codebook.items():
        check(decode_integer(word) == integer, "independent_codec_roundtrips", str(integer))
        magnitude, exponent = abs(integer), 0
        while magnitude >= 2:
            magnitude //= 2
            exponent += 1
        expected_length = 1 if integer == 0 else 2 * exponent + 3
        check(len(word) == expected_length, "independent_code_lengths", str(integer))
    check(prefix_free(codebook.values()), "trie_prefix_free_codebook")
    for first, second in combinations(codebook.values(), 2):
        check(not first.startswith(second) and not second.startswith(first),
              "pairwise_prefix_comparisons")
    for bound in (0, 1, 2, 3, 7, 16, 31, 257):
        word_mass = sum((Q(1, 2 ** len(encode_integer(n)))
                         for n in range(-bound, bound + 1)), Q(0))
        # Count magnitudes by a direct finite sum, independently of constructing words.
        length_mass = Q(1, 2)
        for n in range(1, bound + 1):
            power = 0
            while 2 ** (power + 1) <= n:
                power += 1
            length_mass += Q(1, 2 ** (2 * power + 2))
        check(word_mass == length_mass and word_mass < 1, "exact_partial_kraft_sums")
    for level in range(17):
        shell_mass = Q(1, 2) + sum((Q(1, 2 ** (k + 2)) for k in range(level + 1)), Q(0))
        check(shell_mass == 1 - Q(1, 2 ** (level + 2)), "exact_full_shell_kraft_sums")
    counter_codebook = {n: encode_integer({0: -1, -1: 0}.get(n, n)) for n in integer_domain}
    check(prefix_free(counter_codebook.values()), "valid_prefix_countercode")
    check(len(counter_codebook[-1]) < len(counter_codebook[0]), "countercode_reversed_ranking")
    check(prefix_free([""]) and not prefix_free(["", "1"]), "empty_codeword_control")
    rejected_words = []
    for invalid in ("", "1", "10", "11", "100", "110", "00", "0101", "1010", "11x"):
        try:
            decode_integer(invalid)
        except ValueError:
            rejected_words.append(invalid)
        else:
            raise AssertionError("decoder accepted invalid word " + repr(invalid))
        COUNTS["invalid_codewords_rejected"] += 1

    # Independent resource semantics: a free operation fixes actualized zero.
    for base in BASES:
        for length in range(6):
            for symbols in product("RN+-", repeat=length):
                word = "".join(symbols)
                multiplier, state, cost = affine_program(word, base)
                sequential, sequential_cost = 0, 0
                for symbol in word:
                    if symbol == "R":
                        sequential *= base
                    elif symbol == "N":
                        sequential = -sequential
                    else:
                        sequential += 1 if symbol == "+" else -1
                        sequential_cost += 1
                check((state, cost) == (sequential, sequential_cost), "preparation_matrix_vs_execution")
                check((cost > 0 or state == 0) and (state == 0 or cost >= 1),
                      "positive_intervention_boundary")
        check(affine_program("-", base)[1:] == (-1, 1), "unit_displacement_resource")
        check(affine_program("-R", base)[1:] == (-base, 1), "free_radix_after_paid_displacement")

    # A finite rich neutral fiber is compatible with a fixed actualized zero.
    virtual_distribution = {v: Q(1, 7) for v in range(7)}
    for shift, orientation in product(range(7), (-1, 1)):
        pushed = {(orientation * v + shift) % 7: mass for v, mass in virtual_distribution.items()}
        check(pushed == virtual_distribution and len(pushed) == 7,
              "nonempty_neutral_virtual_fiber")

    # Independent same-forcing histories test the phase quotient formulas.
    control_forcing = tuple(Q((-1) ** n * (n + 1), 2 * n + 3) for n in range(1, 15))
    quotient_examples = []
    for base in BASES:
        zero_history = iterate(control_forcing, Q(0), base)
        for seed in SEEDS:
            history = iterate(control_forcing, seed, base)
            for n in STARTS:
                check(history[n] == direct_green(control_forcing, seed, base, n),
                      "recurrence_vs_green")
            for frequency in FREQUENCIES:
                first_absolute = valuation_start(seed, base, frequency)
                first_relative = valuation_start((base - 1) * seed, base, frequency)
                if first_absolute is not None:
                    check((frequency * base ** first_absolute * seed).denominator == 1,
                          "valuation_absolute_threshold")
                    if first_absolute:
                        check((frequency * base ** (first_absolute - 1) * seed).denominator != 1,
                              "valuation_threshold_minimality")
                else:
                    external = set(factor_integer((frequency * seed).denominator)) - set(factor_integer(base))
                    check(bool(external), "valuation_external_prime_obstruction")
                for start in STARTS:
                    actual = (frequency * (history[start] - zero_history[start])) % 1
                    formula = (frequency * base ** start * seed) % 1
                    check(actual == formula, "same_source_phase_ratio")
                    criterion = (frequency * base ** start * seed).denominator == 1
                    valuation_criterion = first_absolute is not None and first_absolute <= start
                    literal = all((frequency * (history[n] - zero_history[n])) % 1 == 0
                                  for n in range(start, start + 9))
                    check(literal == criterion == valuation_criterion,
                          "absolute_phase_quotient")
                    relative_criterion = (frequency * (base - 1) * base ** start * seed).denominator == 1
                    relative_literal = all(
                        (frequency * ((history[n] - zero_history[n])
                                      - (history[start] - zero_history[start]))) % 1 == 0
                        for n in range(start, start + 9))
                    check(relative_literal == relative_criterion
                          == (first_relative is not None and first_relative <= start),
                          "relative_phase_quotient")
                quotient_examples.append({"base": base, "frequency": frequency, "offset": str(seed),
                                          "absolute_start": first_absolute, "relative_start": first_relative})
    for frequency in FREQUENCIES:
        for n in (0, 1, 2, 5, 37, 61, 97):
            check((frequency * 16 ** n * Q(1, 15)) % 1 == Q(frequency, 15) % 1,
                  "one_fifteenth_constant_phase_rotation")
    for base, frequency, power in product(BASES, FREQUENCIES, (0, 1, 2, 5, 12)):
        delta = Q(1, 2 * frequency * base ** power)
        check((frequency * base ** power * delta) % 1 == Q(1, 2),
              "tiny_seed_exact_antipodal_horizon")
        expected_after = Q(0) if base % 2 == 0 else Q(1, 2)
        for n in (power + 1, power + 2, power + 5):
            check((frequency * base ** n * delta) % 1 == expected_after,
                  "even_alias_odd_antipodal_tail")
        check(min(Q(2), 8 * abs(frequency * base ** power * delta)) == 2,
              "rational_chord_bound_on_exact_antipodal_control")

    # A finite collection of observations uses the gcd of its coefficients.
    for coefficients in ((1, 16, 256), (3, 6, 18), (12, 18, 30), (5, 80, 1280), (-7, 21, 63)):
        divisor = 0
        for coefficient in coefficients:
            divisor = gcd(divisor, abs(coefficient))
        for delta in SEEDS + (Q(1, divisor), Q(1, divisor + 1)):
            check(all((coefficient * delta).denominator == 1 for coefficient in coefficients)
                  == ((divisor * delta).denominator == 1), "finite_observer_gcd_kernel")

    # Original source authentication and full-state recovery retain more than phases.
    forcing = tuple(rational_source(n) for n in range(1, 101))
    for n in (1, 2) + SOURCE_HOLDOUTS:
        check(forcing[n - 1] == authentic_r(n), "original_four_pole_authentication")
    for seed in SEEDS:
        history = iterate(forcing, seed, 16)
        for n in (0, 1, 2, 5) + SOURCE_HOLDOUTS:
            recovered = history[n] / 16 ** n - sum(
                (forcing[k - 1] / 16 ** k for k in range(1, n + 1)), Q(0))
            check(recovered == seed, "full_real_state_seed_recovery")
        check(source_passport(history) == (seed == 0), "zero_seed_full_source_passport")

    # Finite advanced endpoint conditions expose actual future-input dependence.
    for base, prefix in product(BASES, (0, 1, 2, 5, 37, 61, 97)):
        horizon = prefix + 3
        first = forcing[:horizon]
        second = list(first)
        pulse = Q(5, 7)
        second[prefix] += pulse
        first_retarded = iterate(first, Q(0), base)
        second_retarded = iterate(second, Q(0), base)
        check(first_retarded[:prefix + 1] == second_retarded[:prefix + 1],
              "retarded_prefix_nonanticipation")
        advanced_first = -sum((value / base ** k for k, value in enumerate(first, 1)), Q(0))
        advanced_second = -sum((value / base ** k for k, value in enumerate(second, 1)), Q(0))
        check(advanced_second - advanced_first == -pulse / base ** (prefix + 1),
              "advanced_seed_future_pulse")
        history_first = iterate(first, advanced_first, base)
        history_second = iterate(second, advanced_second, base)
        check(history_first[-1] == history_second[-1] == 0, "finite_advanced_terminal_boundary")
        for n in (0, prefix):
            check(history_second[n] - history_first[n] == -pulse * Q(base) ** (n - prefix - 1),
                  "advanced_past_changes_under_future_pulse")

    # Positive zero-seeded counterfeit sources, kept explicitly distinct from original.
    for shift in (Q(0), Q(3), Q(4), Q(7, 5)):
        modified = tuple(hostile_source(n, shift) for n in range(1, 98))
        computed = iterate(modified, Q(0), 16)
        check(not source_passport(computed), "changed_source_passport_rejection")
        mode = (1 / (shift + 1) ** 2).denominator
        for n, value in enumerate(computed):
            check(value == hostile_closed(n, shift), "coherent_closed_form_vs_recurrence")
            if n:
                check(modified[n - 1] > 0, "coherent_source_positivity")
            tail = 1 / (8 * n + shift + 1) ** 2
            check((mode * (value + tail)).denominator == 1, "coherent_mode_exact_tail")
        for n in SOURCE_HOLDOUTS:
            check(modified[n - 1] != authentic_r(n), "coherent_source_is_not_original")
            if shift == 4:
                check(computed[n].denominator % 2 == modified[n - 1].denominator % 2 == 1,
                      "odd_denominator_coherent_control")
                check((25 * computed[n] + Q(25, (8 * n + 5) ** 2)).denominator == 1,
                      "fixed_mode_25_coherence")
    for a in (Q(1, 7), Q(1), Q(9), Q(17), Q(8 * 37 - 7), Q(8 * 61 - 7), Q(8 * 97 - 7)):
        r3 = 16 / (a + 3) ** 2 - 1 / (a + 11) ** 2
        r4 = 16 / (a + 4) ** 2 - 1 / (a + 12) ** 2
        polynomial_difference = (15 * a ** 4 + 729 * a ** 3 + 9809 * a ** 2 + 50263 * a + 87120) / (
            a * (a + 3) ** 2 * (a + 4) * (a + 5) * (a + 11) ** 2)
        check(source_extension(a) - r3 == polynomial_difference > 0,
              "strictly_smaller_forcing_identity")
        check(0 < r4 < r3 < source_extension(a), "smaller_forcing_order")

    # Exact likelihood factorization behind binary coarse-graining, without evaluating logs.
    for epsilon, mass, positive_fraction in product((Q(1, 10), Q(1, 100), Q(1, 1000)),
                                                   (Q(1, 7), Q(1, 2), Q(6, 7)),
                                                   (Q(1, 3), Q(2, 5))):
        reference = (1 - epsilon, epsilon / 2, epsilon / 2)
        selected = (1 - mass, mass * positive_fraction, mass * (1 - positive_fraction))
        for index in (1, 2):
            check(selected[index] / reference[index]
                  == mass / epsilon * (selected[index] / mass) / (reference[index] / epsilon),
                  "exact_kl_coarse_graining_ratio_factorization")

    mutations = []

    def reject(name: str, observed, false_prediction, reason: str) -> None:
        check(observed != false_prediction, "false_mutations_rejected", name)
        mutations.append({"name": name, "status": "rejected", "exact_observed": str(observed),
                          "false_prediction": str(false_prediction), "reason": reason})

    reject("empty_word_multiclass_prefix_code", prefix_free(["", "1"]), True,
           "An empty codeword prefixes every other word; framing cannot be omitted.")
    reject("universal_zero_shortest_code", len(counter_codebook[-1]) < len(counter_codebook[0]), False,
           "A valid relabeled prefix code gives -1 the shortest codeword.")
    free_bootstrap = (1, 1, 0)
    reject("zero_cost_bootstrap", free_bootstrap[1] == 0, True,
           "A zero-cost affine instruction with offset one does not preserve neutral zero.")
    reject("resource_cost_equals_instruction_count", affine_program("-R", 16)[2], len("-R"),
           "The declared radix instruction is free; resource cost and message length differ.")
    reject("reciprocal_phase_clock", (16 * Q(1, 16)) % 1, (Q(1, 16) / 16) % 1,
           "The homogeneous seed difference expands by b^n, not b^(-n).")
    reject("phase_clock_off_by_one", (16 * Q(1, 256)) % 1, (256 * Q(1, 256)) % 1,
           "The seed 1/256 is first absolutely invisible at time two, not time one.")
    reject("phase_ratio_orientation", Q(1, 3) % 1, Q(-1, 3) % 1,
           "Reversing c-d conjugates a nonreal ratio and changes the declared observation.")
    reject("relative_quotient_omits_b_minus_one", (15 * Q(1, 15)).denominator == 1,
           Q(1, 15).denominator == 1,
           "A constant phase rotation need not be the identity rotation.")
    reject("integer_seed_changes_visible_phase", (16 ** 97 * Q(-16)) % 1, Q(1, 2),
           "Integer seed offsets are exact phase aliases, not an opposite-phase control.")
    n = 37
    reject("original_source_wrong_coefficient", rational_source(n), rational_source(n) + Q(1, 8 * n - 4),
           "Changing -2 to -1 in the second signed pole violates the original source passport.")
    reject("original_source_clock_shift", rational_source(n), source_extension(Q(8 * n - 6)),
           "The authentic source clock is a_n=8n-7, not 8n-6.")
    reject("coherent_source_tail_shift", hostile_source(n, Q(4)),
           Q(16, (8 * n - 3) ** 2) - Q(1, (8 * n + 4) ** 2),
           "Changing the tail denominator breaks the advertised zero-seeded closed form.")
    reject("advanced_rule_is_nonanticipatory", -Q(5, 7 * 16 ** 6), Q(0),
           "A pulse after the five-term observed prefix changes the advanced initial seed.")

    check(FORBIDDEN not in sys.modules, "production_module_not_imported")
    return {
        "schema": "succ.inertial-information-boundary.independent-oracle.v1",
        "status": "passed",
        "parent_commit": PARENT,
        "implementation": {
            "python": platform.python_version(),
            "arithmetic": "fractions.Fraction and exact integers only",
            "new_production_module_imported": False,
            "independence_scope": "separate codebook parser, affine composition, valuation algorithm, and source reconstruction; shared native source passport",
        },
        "predeclared_grids": {
            "bases": list(BASES), "frequencies": list(FREQUENCIES),
            "seeds": [str(value) for value in SEEDS], "observation_starts": list(STARTS),
            "source_holdouts": list(SOURCE_HOLDOUTS),
            "integer_codebook": "-257..257 plus signed powers of two through 2^16",
            "codebook_symbols": len(codebook),
            "preparation_alphabet": "RN+-", "maximum_preparation_word_length": 5,
            "tiny_offset_horizons": [0, 1, 2, 5, 12],
            "coherent_source_shifts": ["0", "3", "4", "7/5"],
            "coherent_source_horizon": 97,
        },
        "exact_checks": dict(sorted(COUNTS.items())),
        "exact_check_total": sum(COUNTS.values()),
        "quotient_finite_cases": quotient_examples,
        "mutations": {"rejected_count": len(mutations), "witnesses": mutations},
        "exact_examples": {
            "zero_code": "0", "negative_one_code": "111", "negative_sixteen_code": "11000010000",
            "negative_one_preparation_cost": 1, "negative_sixteen_preparation_cost": 1,
            "base16_absolute_start_for_1_over_256": 2,
            "base16_relative_start_for_1_over_15": 0,
            "base16_absolute_start_for_1_over_15": None,
            "odd_denominator_coherent_mode": 25,
            "invalid_codewords_rejected": rejected_words,
        },
        "numerical_diagnostics": {
            "evaluations": 0, "floating_point_certificates": False,
            "kl_logarithms_evaluated": False, "trigonometric_values_evaluated": False,
        },
        "scope": {
            "finite_checks": "VERIFIED_FINITE",
            "all_parameter_results": "paper proofs required; no universal lift from this grid",
            "original_BBP_signed_cancellation": "OPEN",
            "pi_normality": "OPEN",
            "physical_or_human_cognition_model": "NOT CLAIMED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path for the JSON also printed to stdout")
    arguments = parser.parse_args()
    try:
        result = run()
        exit_code = 0
    except Exception as error:
        result = {"schema": "succ.inertial-information-boundary.independent-oracle.v1",
                  "status": "failed", "error_type": type(error).__name__, "error": str(error),
                  "completed_exact_checks": dict(sorted(COUNTS.items())),
                  "numerical_diagnostics": {"evaluations": 0, "floating_point_certificates": False}}
        exit_code = 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
