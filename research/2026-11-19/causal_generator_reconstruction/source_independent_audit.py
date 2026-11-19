"""Independent exact audit of the five-reading acquisition theorem.

No source_acquisition implementation is imported. SymPy propagates the symbolic
raw recurrence, differentiates it for sampling rows, and directly computes the
five-by-five inverse. A separately constructed interval-sum inverse must agree.
Finite checks corroborate implementation; SOURCE_AUDIT.md gives the proof audit.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as S


POLES = (7, 4, 3, 2)
PARAMETERS = S.symbols("s c1 c2 c3 c4")
SCHEDULES = ((4, 9, 21, 44, 67), (8, 13, 21, 34, 55),
             (7, 8, 9, 10, 11), (3, 5, 8, 10, 13))
AUTHENTIC = S.Matrix([4, -2, -1, -1])


def rational_text(value):
    value = S.Rational(value)
    return f"{value.p}/{value.q}"


def exact_digest(matrix):
    """Canonical digest also reproducible using Fraction, without SymPy."""
    payload = [[rational_text(matrix[i, j]) for j in range(matrix.cols)]
               for i in range(matrix.rows)]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def scalar_receipt(value):
    value = S.Rational(value)
    return {"sign": int(S.sign(value)),
            "numerator_bits": abs(int(value.p)).bit_length(),
            "denominator_bits": int(value.q).bit_length(),
            "sha256": sha256(rational_text(value).encode()).hexdigest()}


def symbolic_states(horizon, parameters=PARAMETERS):
    """Evolve raw source states; no normalized cumulative-row formula."""
    states = [S.sympify(parameters[0])]
    for n in range(1, horizon + 1):
        drive = sum(parameters[a + 1] / S.Integer(8*n - pole)
                    for a, pole in enumerate(POLES))
        states.append(S.expand(16*states[-1] + drive))
    return tuple(states)


def raw_rows(states, times):
    return S.Matrix([[S.diff(states[t], parameter) for parameter in PARAMETERS]
                     for t in times])


def interval_block(times):
    """Independent finite-sum expression, not differentiated raw recurrence."""
    return S.Matrix([[sum(S.Rational(1, 16**n*(8*n-pole))
                          for n in range(left + 1, right + 1))
                      for pole in POLES]
                     for left, right in zip(times, times[1:])])


def cauchy_product(clocks):
    numerator = S.Integer(120*8**6)
    for i in range(4):
        for j in range(i + 1, 4):
            numerator *= clocks[j] - clocks[i]
    denominator = S.prod(8*n - pole for n in clocks for pole in POLES)
    return numerator / denominator


def run_audit():
    checks = []

    def require(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    # Row-denominator clearing reduces the Cauchy sign to a small integer
    # polynomial-coefficient determinant, independently of a Cauchy routine.
    z = S.Symbol("z")
    polynomials = [S.Poly(S.prod(z-q for q in POLES if q != pole), z)
                   for pole in POLES]
    coefficients = S.Matrix([[p.nth(k) for p in polynomials] for k in range(4)])
    require("polynomial_coefficient_determinant", coefficients.det() == 120)

    horizon = max(max(t) for t in SCHEDULES) + 7
    states = symbolic_states(horizon)
    x = S.Symbol("x")
    authentic = S.Matrix([0, *AUTHENTIC])
    wrong_seed = S.Matrix([-x, *AUTHENTIC])
    alias_seed = S.Matrix([S.Rational(1, 16), *AUTHENTIC])
    rational_source = S.Matrix([S.Rational(-5, 13), S.Rational(7, 2),
                               S.Rational(-11, 3), S.Rational(13, 5),
                               S.Rational(-17, 7)])
    wrong_states = symbolic_states(horizon, tuple(wrong_seed))
    authentic_states = symbolic_states(horizon, tuple(authentic))
    alias_states = symbolic_states(horizon, tuple(alias_seed))
    schedule_receipts = []

    for times in SCHEDULES:
        label = ",".join(map(str, times))
        raw = raw_rows(states, times)
        direct_inverse = raw.inv(method="DM")
        direct_det = raw.det(method="domain-ge")
        block = interval_block(times)
        block_det = block.det(method="domain-ge")
        normalization = S.diag(*(S.Rational(1, 16**t) for t in times))
        differences = S.eye(5)
        for i in range(1, 5):
            differences[i, i-1] = -1
        anchor = S.Matrix([[sum(S.Rational(1, 16**n*(8*n-pole))
                                for n in range(1, times[0] + 1))
                            for pole in POLES]])
        triangular = S.BlockMatrix([[S.ones(1, 1), anchor],
                                    [S.zeros(4, 1), block]]).as_explicit()
        block_inverse = block.inv(method="DM")
        triangular_inverse = S.BlockMatrix(
            [[S.ones(1, 1), -anchor*block_inverse],
             [S.zeros(4, 1), block_inverse]]).as_explicit()
        via_blocks = triangular_inverse * differences * normalization

        require(label+": raw_to_interval_identity", differences*normalization*raw == triangular)
        require(label+": positive_block_determinant", block_det > 0)
        require(label+": raw_determinant", direct_det == 16**sum(times)*block_det)
        require(label+": direct_and_block_inverse", direct_inverse == via_blocks)
        require(label+": inverse_identity", via_blocks*raw == S.eye(5))
        raw_data = S.Matrix([states[t].subs(dict(zip(PARAMETERS, rational_source)))
                             for t in times])
        recovered = direct_inverse*raw_data
        require(label+": rational_recovery", recovered == rational_source)
        future = times[-1] + 7
        predicted = (raw_rows(states, (future,))*recovered)[0]
        require(label+": future_prediction", predicted == states[future].subs(
            dict(zip(PARAMETERS, rational_source))))

        bad_data = S.Matrix([wrong_states[t] for t in times])
        good_data = S.Matrix([authentic_states[t] for t in times])
        bad_recovery = (direct_inverse*bad_data).applyfunc(S.expand)
        require(label+": symbolic_wrong_seed_recovery", bad_recovery == wrong_seed)
        require(label+": wrong_seed_delta", (bad_data-good_data).applyfunc(S.expand) ==
                S.Matrix([-16**t*x for t in times]))
        # Four normalized innovations cancel the seed. The retained anchor is
        # the actual separating report, not a second coefficient-rank argument.
        require(label+": innovations_ignore_seed",
                ((differences*normalization*(bad_data-good_data))[1:, :]).applyfunc(S.expand)
                == S.zeros(4, 1))

        alias_data = S.Matrix([alias_states[t] for t in times])
        require(label+": rational_alias_lift", alias_data-good_data ==
                S.Matrix([16**(t-1) for t in times]))
        require(label+": wrapped_alias", all(
            S.frac(alias_data[i]) == S.frac(good_data[i]) for i in range(5)))
        require(label+": alias_seed_recovery", direct_inverse*alias_data == alias_seed)

        null_basis = raw[:4, :].nullspace()
        require(label+": four_reading_kernel_dimension", len(null_basis) == 1)
        direction = null_basis[0]
        last_response = (raw[4:5, :]*direction)[0]
        require(label+": fifth_reading_separates_kernel", last_response != 0)
        direction /= last_response
        kernel_states = symbolic_states(times[-1], tuple(direction))
        require(label+": direct_recurrence_kernel_control",
                [kernel_states[t] for t in times] == [0, 0, 0, 0, 1])

        minor_clocks = tuple(t+1 for t in times[:-1])
        minor = S.Matrix([[S.Rational(1, 8*n-pole) for pole in POLES]
                          for n in minor_clocks])
        require(label+": cauchy_minor_sign_and_value",
                minor.det() == cauchy_product(minor_clocks) > 0)
        if all(times[i+1]-times[i] == 1 for i in range(4)):
            require(label+": consecutive_raw_determinant",
                    direct_det == 16**times[0]*cauchy_product(times[1:]))

        schedule_receipts.append({
            "times": list(times), "raw_sampling_matrix_sha256": exact_digest(raw),
            "raw_inverse_sha256": exact_digest(direct_inverse),
            "raw_determinant": scalar_receipt(direct_det),
            "normalized_block_determinant": scalar_receipt(block_det),
            "symbolic_wrong_seed_recovery": [str(v) for v in bad_recovery],
            "rational_alias_seed": "1/16", "wrapped_alias_equal": True,
            "kernel_sha256": exact_digest(direction),
            "kernel_readings": [0, 0, 0, 0, 1], "future_clock": future})

    small_times = SCHEDULES[-1]
    expansion = S.Integer(0)
    term_count = 0
    for clocks in product(*(range(a+1, b+1) for a, b in zip(small_times, small_times[1:]))):
        term = cauchy_product(clocks) / 16**sum(clocks)
        require(f"positive_expansion_term_{term_count}", term > 0)
        expansion += term
        term_count += 1
    require("full_positive_block_expansion", expansion == interval_block(small_times).det())

    offset = S.Symbol("N", nonnegative=True, integer=True)
    consecutive = S.Matrix([[1/(8*(offset+i)-pole) for pole in POLES]
                             for i in range(1, 5)])
    consecutive_inverse = consecutive.inv(method="DM")
    inverse_polynomials = [S.Poly(S.cancel(value), offset) for value in consecutive_inverse]
    require("consecutive_inverse_polynomial_degree", all(p.degree() == 7 for p in inverse_polynomials))
    inverse_leading = consecutive_inverse.applyfunc(
        lambda value: S.Poly(S.cancel(value), offset).LC())
    row_gaps, pole_gaps = (2, 6, 6, 2), (2, 20, 30, 12)
    cofactor_leading = S.Matrix([
        [S.Rational((-1)**(a+i)*8**4*pole_gaps[a]*row_gaps[i], 1440)
         for i in range(4)] for a in range(4)])
    require("consecutive_inverse_cofactor_leading", inverse_leading == cofactor_leading)
    determinant_leading = S.limit(offset**16*consecutive.det(method="domain-ge"), offset, S.oo)
    require("consecutive_determinant_leading", determinant_leading == S.Rational(45, 2**25))
    innovation = S.zeros(4, 5)
    for i in range(4):
        innovation[i, i], innovation[i, i+1] = -16, 1
    coefficient_leading = inverse_leading*innovation
    gain_leading = max(sum(abs(value) for value in coefficient_leading.row(a)) for a in range(4))
    require("consecutive_coefficient_gain_leading", gain_leading == S.Rational(69632, 3))
    require("consecutive_volume_leading", 32/determinant_leading == S.Rational(8**10, 45))

    # A discontinuous clock/stopping policy is allowed in SA-03. These two
    # rational cases exercise different stopping lengths. The universal
    # adversarial-transcript argument is in SOURCE_AUDIT.md, not inferred here.
    def adaptive_transcript(theta):
        trajectory = symbolic_states(20, tuple(theta))
        t, transcript = 1, []
        while len(transcript) < 4:
            y = trajectory[t]
            transcript.append((t, y))
            if len(transcript) >= 3 and y < 0:
                break
            t += 2 if int(S.floor(abs(y))) % 2 == 0 else 3
        return transcript

    adaptive_receipts = []
    for theta in (authentic, S.Matrix([-1, *AUTHENTIC])):
        transcript = adaptive_transcript(theta)
        times = tuple(t for t, _ in transcript)
        observation = raw_rows(states, times)
        invisible = observation.nullspace()[0]
        changed = theta + invisible/S.Integer(17)
        require(f"adaptive_{times}: distinct_sources", changed != theta)
        require(f"adaptive_{times}: identical_transcript", adaptive_transcript(changed) == transcript)
        adaptive_receipts.append({"times": list(times), "readings": len(times),
                                  "different_parameters": True, "identical_transcript": True})

    here = Path(__file__).resolve().parent
    return {
        "status": "PASS", "arithmetic": "exact SymPy rational and polynomial arithmetic",
        "sympy_version": S.__version__, "imports_source_acquisition": False,
        "assertions_passed": len(checks), "schedules": schedule_receipts,
        "cauchy_coefficient_matrix": [list(map(int, coefficients.row(i))) for i in range(4)],
        "cauchy_coefficient_determinant": 120,
        "positive_expansion_terms": term_count, "adaptive_controls": adaptive_receipts,
        "consecutive_asymptotics": {
            "det_C_times_N_power_16_limit": rational_text(determinant_leading),
            "every_inverse_entry_polynomial_degree": 7,
            "inverse_leading_matrix": [[rational_text(inverse_leading[i, j])
                                         for j in range(4)] for i in range(4)],
            "coefficient_infinity_gain_over_N_power_7_limit": rational_text(gain_leading),
            "volume_over_N_power_16_times_16_power_minus_N_times_product_widths_limit":
                rational_text(32/determinant_leading)},
        "source_acquisition_sha256": sha256((here / "source_acquisition.py").read_bytes()).hexdigest(),
        "audit_script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite implementation corroboration; universal claims require the paper proofs."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the same exact JSON receipt to this path")
    arguments = parser.parse_args()
    receipt = json.dumps(run_audit(), indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(receipt)
    print(receipt, end="")
