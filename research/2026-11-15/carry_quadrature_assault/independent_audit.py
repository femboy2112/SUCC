#!/usr/bin/env python3
"""Independent exact calibration for the carry-quadrature dossier.

Standard library only; no observational_succ imports or pi approximations.
Run directly to print a deterministic JSON receipt.  An optional --output
path also saves that same receipt.  Finite checks do not prove the authentic
positive-density gate, analyticity of an infinite Mahler series, or a limiting
endpoint.  The associated documents supply the universal arguments.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys


SOURCE_LAST = 256
MAHLER_LAST = 48
LOOP_LAST_START = 16
LOOP_LAST_DEPTH = 8
TM_FIRST = 5
TM_LAST = 128
TM_PREFIX = 160
TAIL_DEPTH = 12
EXTRA_PULSES = (512, 1024, 4096, 65536)


class AuditFailure(Exception):
    def __init__(self, label: str, context: dict):
        self.label = label
        self.context = context
        super().__init__(label)


class Checks:
    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()

    def require(self, condition: bool, label: str, **context: object) -> None:
        self.counts[label] += 1
        if not condition:
            raise AuditFailure(label, context)


def floor_q(x: Q) -> int:
    return x.numerator // x.denominator


def nearest_q(x: Q) -> int:
    """Nearest integer, with exact ties rounded toward positive infinity."""
    return floor_q(x + Q(1, 2))


def source_four_poles(n: int) -> Q:
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def source_combined(n: int) -> Q:
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def residue(x: Q, modulus: int) -> int:
    if x.denominator % 2 == 0:
        raise ValueError("The residue map requires an odd reduced denominator")
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def v2_integer(n: int) -> int | None:
    """None denotes infinite valuation at zero."""
    n = abs(n)
    return None if n == 0 else (n & -n).bit_length() - 1


def difference_v2(a: Q, b: Q) -> int | None:
    if a.denominator % 2 == 0 or b.denominator % 2 == 0:
        raise ValueError("This comparison requires two 2-integral rationals")
    # The denominator is odd, so no gcd or rational reduction is needed.
    return v2_integer(a.numerator*b.denominator - b.numerator*a.denominator)


def divisible_at_least(x: Q, exponent: int) -> bool:
    return x.denominator % 2 == 1 and x.numerator % (1 << exponent) == 0


def lag(n: int) -> int:
    m = 0
    while 16**m < n*n:
        m += 1
    return m


def rational_digest(values: list[Q]) -> str:
    serial = "\n".join(f"{x.numerator}/{x.denominator}" for x in values)
    return sha256(serial.encode("ascii")).hexdigest()


def polynomial_trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def polynomial_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return polynomial_trim(out)


def polynomial_sub(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, y in enumerate(b):
        out[i] -= y
    return polynomial_trim(out)


def polynomial_shift_one(a: list[int]) -> list[int]:
    """Coefficients of P(t+1), in ascending powers."""
    out = [0] * len(a)
    for degree, value in enumerate(a):
        for power in range(degree+1):
            out[power] += value * comb(degree, power)
    return polynomial_trim(out)


def polynomial_certificates(checks: Checks) -> dict:
    numerator = [16, -89, 120]
    denominator = [1]
    for factor in ([-1, 2], [-1, 4], [-7, 8], [-3, 8]):
        denominator = polynomial_mul(denominator, factor)
    lower = polynomial_sub([0, 0] + [64*x for x in numerator],
                           [15*x for x in denominator])
    upper = polynomial_sub(
        [15*x for x in denominator],
        [64*x for x in polynomial_mul([1, -2, 1], numerator)],
    )
    lower_shift = polynomial_shift_one(lower)
    upper_shift = polynomial_shift_one(upper)
    checks.require(lower == [-315, 3090, -9656, 9664],
                   "polynomial.lower_identity")
    checks.require(upper_shift == [225, 2910, 7672, 5696],
                   "polynomial.upper_identity")
    checks.require(lower_shift == [2783, 12770, 19336, 9664],
                   "polynomial.lower_shift_identity")
    checks.require(all(x > 0 for x in lower_shift + upper_shift),
                   "polynomial.positive_shift_coefficients")
    return {
        "coefficient_order": "ascending powers of t; n=t+1",
        "lower_shift_coefficients": lower_shift,
        "upper_shift_coefficients": upper_shift,
        "scope": "exact symbolic identities used in the documented tail proof",
    }


# Finite group algebra of Q/Z.  A dictionary represents a formal sum of
# circle characters e(exponent).  Identities are checked exactly, with no
# floating-point sine, complex numbers, or transcendental comparisons.
def character(exponent: Q) -> dict[Q, int]:
    return {exponent % 1: 1}


def character_add(a: dict[Q, int], b: dict[Q, int],
                  scale: int = 1) -> dict[Q, int]:
    out = a.copy()
    for exponent, value in b.items():
        out[exponent] = out.get(exponent, 0) + scale*value
    return {exponent: value for exponent, value in out.items() if value}


def character_mul(a: dict[Q, int], b: dict[Q, int]) -> dict[Q, int]:
    out: dict[Q, int] = {}
    for x, u in a.items():
        for y, v in b.items():
            key = (x+y) % 1
            out[key] = out.get(key, 0) + u*v
    return {exponent: value for exponent, value in out.items() if value}


def character_conjugate(a: dict[Q, int]) -> dict[Q, int]:
    return {(-exponent) % 1: value for exponent, value in a.items()}


def source_audit(checks: Checks) -> tuple[dict, list[Q]]:
    horizon = max(SOURCE_LAST + lag(SOURCE_LAST),
                  LOOP_LAST_START + 2**LOOP_LAST_DEPTH)
    states = [Q(0)]
    for n in range(1, horizon+1):
        states.append(16*states[-1] + source_four_poles(n))

    for n in range(1, SOURCE_LAST+1):
        r = source_four_poles(n)
        checks.require(r == source_combined(n),
                       "source.expanded_four_pole_identity", n=n)
        checks.require(r > Q(15, 64*n*n), "source.lower_bound", n=n)
        if n >= 2:
            checks.require(r < Q(15, 64*(n-1)**2),
                           "source.upper_bound", n=n)

    hits = 0
    for n in range(SOURCE_LAST+1):
        u = states[n]
        carry = floor_q(u)
        y = u-carry
        checks.require(u.denominator % 2 == 1 and y.denominator % 2 == 1,
                       "source.odd_denominators", n=n)
        checks.require(residue(u, 16) == (2*(n % 2)-n) % 16,
                       "source.spatial_nibble", n=n)
        checks.require(residue(u, 4) == n % 4,
                       "source.fourth_root_clock", n=n)
        checks.require((n+residue(-y, 4)) % 4 == carry % 4,
                       "source.carry_cofactor_phase", n=n)
        if n:
            previous = states[n-1]
            local = floor_q(16*(previous-floor_q(previous))+source_four_poles(n))
            checks.require(carry-16*floor_q(previous) == local,
                           "source.literal_carry_recurrence", n=n)
            hits += carry % 4 in (1, 2)

    for b in range(1, SOURCE_LAST+1):
        for a in range(b):
            checks.require(difference_v2(states[b], states[a]) == v2_integer(b-a),
                           "source.all_pair_isometry", a=a, b=b)

    for k in range(LOOP_LAST_DEPTH+1):
        modulus = 2**(k+1)
        for n in range(LOOP_LAST_START+1):
            t = n+2**k
            delta = states[t]-states[n]
            checks.require(residue(delta, modulus) == 2**k,
                           "source.dyadic_next_bit_flip", n=n, k=k)
            c_delta = floor_q(states[t])-floor_q(states[n])
            y_delta = (states[t]-floor_q(states[t]))-(states[n]-floor_q(states[n]))
            checks.require(c_delta % modulus ==
                           (2**k+residue(-y_delta, modulus)) % modulus,
                           "source.dyadic_carry_transport", n=n, k=k)

    return {
        "original_zero_seed": True,
        "source_identity_indices": [1, SOURCE_LAST],
        "state_identity_indices": [0, SOURCE_LAST],
        "all_pair_state_isometries": SOURCE_LAST*(SOURCE_LAST+1)//2,
        "loop_start_indices": [0, LOOP_LAST_START],
        "loop_depths": [0, LOOP_LAST_DEPTH],
        "extra_states_for_echoes_and_loops": horizon-SOURCE_LAST,
        "finite_target_hits": hits,
        "target_hit_index_range": [1, SOURCE_LAST],
        "first_two_nonzero_states": [str(states[1]), str(states[2])],
        "states_sha256": rational_digest(states[:SOURCE_LAST+1]),
        "positive_density_inferred": False,
    }, states


def excitation_audit(checks: Checks, states: list[Q]) -> dict:
    for n in list(range(4, SOURCE_LAST+1)) + list(EXTRA_PULSES):
        m = lag(n)
        q = 16**m
        echo = sum((16**(m-j)*source_four_poles(n+j)
                    for j in range(1, m+1)), Q(0))
        checks.require(n*n <= q < 16*n*n, "echo.amplification_scale", n=n)
        checks.require(Q(1, 128) < echo < Q(1, 4),
                       "echo.uniform_rational_interval", n=n)
        lower = Q(15*n*n, 1024*(n+1)**2)-Q(1, 64*n*n)
        checks.require(lower >= Q(43, 5120) > Q(1, 128),
                       "echo.documented_lower_bound", n=n)
        if n > SOURCE_LAST:
            continue
        later = n+m
        checks.require(states[later]-q*states[n] == echo,
                       "echo.finite_source_identity", n=n)
        for theta in (Q(1), Q(1, 4)):
            delta = character_add(character(theta*states[later]),
                                  character(theta*q*states[n]), -1)
            reference = character_add(character(Q(0)),
                                      character(-theta*echo), -1)
            norm = character_mul(reference, character_conjugate(reference))
            product = character_mul(delta, character_conjugate(reference))
            expected = character_mul(character(theta*states[later]), norm)
            checks.require(product == expected, "echo.reference_decoder",
                           n=n, theta=str(theta))
            checks.require(Q(0) < theta*echo < 1,
                           "echo.reference_nonzero_exponent",
                           n=n, theta=str(theta))
            if theta == Q(1, 4):
                c = floor_q(states[later])
                y = states[later]-c
                actual = character_mul(product, character(-y/4))
                target = character_mul(character(Q(c, 4)), norm)
                checks.require(actual == target, "echo.quarter_carry_decoder", n=n)
    for b in range(4, SOURCE_LAST+1):
        shifted = {n+lag(n) for n in range(b, 2*b)}
        original = set(range(b, 2*b))
        checks.require(len(shifted) == b and
                       len(shifted ^ original) <= 2*lag(2*b),
                       "echo.sampling_symmetric_difference", B=b)
    return {
        "echo_indices": [4, SOURCE_LAST],
        "additional_echo_indices": list(EXTRA_PULSES),
        "exact_echo_interval": ["1/128", "1/4"],
        "readout_thetas": ["1", "1/4"],
        "complex_identity_method": "finite exact group algebra of Q/Z",
        "trigonometric_numerics_used": False,
        "uniform_norm_bounds": {
            "theta_1": "|J| > 2 sin(pi/128)",
            "theta_1_over_4": "|J| > 2 sin(pi/512)",
            "authority": "documented analytic sine bound; not evaluated numerically",
        },
        "signed_density_bound_inferred": False,
    }


def tau(n: int) -> Q:
    return Q(n+1, (2*n+1)*(4*n+1)*(8*n+1))


def mahler_control(checks: Checks, source: list[Q],
                   endpoint: Q, low_bits: int) -> dict:
    coefficients = [Q(0)]
    values = [Q(0)]
    errors = [Q(0)]
    maximum_odd_q_bits = 0
    label = f"L{low_bits}_a{endpoint.numerator}_{endpoint.denominator}"
    for n in range(1, MAHLER_LAST+1):
        f_n = 16**n*endpoint-tau(n)
        delta = tau(n)/Q(100*(n+1))
        prior = sum((coefficients[k]*comb(n, k) for k in range(1, n)), Q(0))
        target = f_n-source[n]-prior
        exponent = 2*n+low_bits
        step = 2**exponent
        threshold = Q(step)/(2*delta)
        odd_q = floor_q(threshold)+1
        if odd_q % 2 == 0:
            odd_q += 1
        p = nearest_q(target*odd_q/step)
        coefficient = Q(step*p, odd_q)
        coefficients.append(coefficient)
        value = source[n]+prior+coefficient
        values.append(value)
        error = value-f_n
        errors.append(error)
        maximum_odd_q_bits = max(maximum_odd_q_bits, odd_q.bit_length())
        checks.require(odd_q % 2 == 1 and Q(odd_q) > threshold,
                       "mahler.odd_grid_resolution", control=label, n=n)
        checks.require(divisible_at_least(coefficient, exponent),
                       "mahler.coefficient_divisibility", control=label, n=n)
        checks.require(abs(coefficient-target) <= Q(step, 2*odd_q) < delta,
                       "mahler.rounding_bound", control=label, n=n)
        checks.require(abs(error) < delta,
                       "mahler.real_approximation", control=label, n=n)
        recomputed = source[n]+sum(
            (coefficients[k]*comb(n, k) for k in range(1, n+1)), Q(0))
        checks.require(value == recomputed, "mahler.finite_interpolation",
                       control=label, n=n)
        checks.require(value.denominator % 2 == 1,
                       "mahler.odd_diagonal_state", control=label, n=n)
        checks.require(residue(value, 2**low_bits) ==
                       residue(source[n], 2**low_bits),
                       "mahler.authentic_low_bits", control=label, n=n)
        checks.require(divisible_at_least(value-source[n], low_bits+2),
                       "mahler.strong_correction_divisibility", control=label, n=n)
        expected_floor = (16**n-1 if endpoint == 1 else (16**n-1)//5)
        checks.require(floor_q(value) == expected_floor and expected_floor % 4 == 3,
                       "mahler.locked_carry_floor", control=label, n=n)
        remaining = 16**n*endpoint-value
        upper = Q(1) if endpoint == 1 else Q(1, 5)
        checks.require(Q(0) < remaining < upper,
                       "mahler.positive_completed_tail", control=label, n=n)

    checks.require(values[0] == source[0] == 0,
                   "mahler.exact_origin", control=label)
    forcing = [values[n]-16*values[n-1] for n in range(1, MAHLER_LAST+1)]
    for n, r_new in enumerate(forcing, 1):
        checks.require(r_new > 0 and r_new.denominator % 2 == 1,
                       "mahler.positive_odd_source", control=label, n=n)
        checks.require(residue(r_new, 2**low_bits) ==
                       residue(source_four_poles(n), 2**low_bits),
                       "mahler.authentic_low_source_bits", control=label, n=n)
        if n >= 2:
            baseline = 16*tau(n-1)-tau(n)
            checks.require(r_new-baseline == errors[n]-16*errors[n-1],
                           "mahler.source_error_identity", control=label, n=n)
    checks.require(any(forcing[n-1] != source_four_poles(n)
                       for n in range(1, MAHLER_LAST+1)),
                   "mahler.changed_literal_source", control=label)
    for b in range(1, MAHLER_LAST+1):
        for a in range(b):
            expected = v2_integer(b-a)
            checks.require(difference_v2(values[b], values[a]) == expected,
                           "mahler.all_pair_state_isometry",
                           control=label, a=a, b=b)
            contraction = difference_v2(values[b]-source[b], values[a]-source[a])
            checks.require(contraction is None or
                           contraction >= expected+low_bits+2,
                           "mahler.all_pair_correction_contraction",
                           control=label, a=a, b=b)
    for b in range(1, MAHLER_LAST):
        for a in range(b):
            checks.require(difference_v2(forcing[b], forcing[a]) == v2_integer(b-a),
                           "mahler.all_pair_source_isometry",
                           control=label, source_a=a+1, source_b=b+1)
    return {
        "control": label,
        "prescribed_endpoint": str(endpoint),
        "retained_authentic_bits_L": low_bits,
        "state_indices": [0, MAHLER_LAST],
        "coefficient_indices": [1, MAHLER_LAST],
        "source_indices": [1, MAHLER_LAST],
        "state_pair_count": MAHLER_LAST*(MAHLER_LAST+1)//2,
        "source_pair_count": MAHLER_LAST*(MAHLER_LAST-1)//2,
        "target_events": 0,
        "carry_residue_at_every_positive_checked_index": 3,
        "literal_four_pole_source_preserved": False,
        "maximum_rounding_denominator_bits": maximum_odd_q_bits,
        "coefficient_samples": {str(k): str(coefficients[k])
                                for k in (1, 2, MAHLER_LAST)},
        "coefficients_sha256": rational_digest(coefficients),
        "states_sha256": rational_digest(values),
        "scope": "finite calibration of the fixed-L analytic construction",
        "infinite_analyticity_or_endpoint_inferred_from_checks": False,
    }


def thue_morse(k: int) -> int:
    return k.bit_count() % 2


def tm_audit(checks: Checks) -> dict:
    beta_lo = sum((Q(3*thue_morse(k), 16**k)
                   for k in range(1, TM_PREFIX+1)), Q(0))
    beta_hi = beta_lo+Q(1, 5*16**TM_PREFIX)
    prefixes = [0]
    for n in range(1, TM_LAST+1):
        prefixes.append(16*prefixes[-1]+3*thue_morse(n))
    certified: dict[int, int] = {}
    for n in range(TM_FIRST, TM_LAST+1):
        tail_lo = sum((source_four_poles(n+j)/16**j
                       for j in range(1, TAIL_DEPTH+1)), Q(0))
        tail_hi = tail_lo+Q(1, 16**TAIL_DEPTH*64*(n+TAIL_DEPTH)**2)
        value_lo = 16**n*beta_lo-tail_hi
        value_hi = 16**n*beta_hi-tail_lo
        expected = prefixes[n]
        checks.require(0 < tail_lo < tail_hi < Q(1, 64*n*n) < Q(3, 4096),
                       "tm.tail_enclosure_separation", n=n)
        checks.require(value_lo <= value_hi and
                       floor_q(value_lo) == floor_q(value_hi) == expected,
                       "tm.interval_floor_certificate", n=n)
        checks.require(nearest_q(value_lo) == nearest_q(value_hi) == expected,
                       "tm.interval_nearest_certificate", n=n)
        checks.require(0 < value_lo-expected <= value_hi-expected < Q(1, 5),
                       "tm.fractional_interval_certificate", n=n)
        checks.require(expected % 4 in (0, 3),
                       "tm.no_target_event", n=n)
        certified[n] = expected
    nonzero = 0
    for n in range(TM_FIRST, TM_LAST):
        packet = certified[n+1]-16*certified[n]
        checks.require(packet == 3*thue_morse(n+1),
                       "tm.exact_winding_certificate", n=n)
        nonzero += packet != 0
    for b in range(TM_FIRST, TM_LAST//2+1):
        count = sum(thue_morse(n+1) for n in range(b, 2*b))
        checks.require(abs(2*count-b) <= 2, "tm.shell_packet_balance", B=b)
    return {
        "completed_endpoint_digit_set": [0, 3],
        "prefix_length": TM_PREFIX,
        "endpoint_enclosure_width": f"1/(5*16^{TM_PREFIX})",
        "tail_terms": TAIL_DEPTH,
        "tail_remainder_bound": "16^(-12)/(64*(n+12)^2)",
        "state_index_range": [TM_FIRST, TM_LAST],
        "floor_certificates": len(certified),
        "nearest_integer_certificates": len(certified),
        "winding_certificates": TM_LAST-TM_FIRST,
        "nonzero_positive_packets": nonzero,
        "target_events": 0,
        "original_four_pole_forcing_preserved": True,
        "original_zero_seed_preserved": False,
        "enclosure_authority": "digit tail bound and documented n^-2 source-tail theorem",
        "irrationality_exponent_tested_or_inferred": False,
        "scope": "finite rational interval certificates; universal proof is in WINDING_PACKETS.md",
    }


def run_audit(checks: Checks) -> dict:
    polynomial = polynomial_certificates(checks)
    source_result, states = source_audit(checks)
    excitation = excitation_audit(checks, states)
    controls = [mahler_control(checks, states, endpoint, low_bits)
                for low_bits in (2, 8) for endpoint in (Q(1), Q(1, 5))]
    tm_result = tm_audit(checks)
    return {
        "status": "PASS",
        "audit_version": 1,
        "method": "standalone Python standard library exact arithmetic",
        "observational_succ_imports": False,
        "floating_point_used": False,
        "rounding_convention": "nearest integer; exact ties toward positive infinity",
        "claims": {
            "finite_calibration_passed": True,
            "authentic_positive_shell_density_proved": False,
            "pi_normality_proved": False,
            "finite_computation_used_as_infinite_proof": False,
        },
        "polynomial_certificates": polynomial,
        "authentic_source": source_result,
        "source_excitation": excitation,
        "fixed_L_mahler_controls": controls,
        "thue_morse_control": tm_result,
        "total_exact_assertions": sum(checks.counts.values()),
        "check_counts": dict(sorted(checks.counts.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="also save the deterministic JSON receipt at this path")
    args = parser.parse_args()
    checks = Checks()
    try:
        receipt = run_audit(checks)
        code = 0
    except AuditFailure as exc:
        receipt = {
            "status": "FAIL",
            "failed_check": exc.label,
            "context": exc.context,
            "checks_attempted": sum(checks.counts.values()),
            "check_counts": dict(sorted(checks.counts.items())),
        }
        code = 1
    receipt["audit_file_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(receipt, indent=2, sort_keys=True, default=str)+"\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    sys.stdout.write(payload)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
