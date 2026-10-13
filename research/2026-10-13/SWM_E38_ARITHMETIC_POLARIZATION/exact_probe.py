#!/usr/bin/env python3
"""E38 bounded exact witnesses; no zero data, integrations, or third-party code.

Finite polynomial Dirichlet algebra corroborates the dossier's separately
proved universal statements. It does not certify a completed positive form.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from math import factorial, isqrt
import json


N = 16
SOURCE_PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
IMPORT_PARENT = "ba075348b7bcc66d938b3e0ca96c26e95bba340a"


def convolution(left, right):
    out = [Q(0)] * (N + 1)
    for d in range(1, N + 1):
        for k in range(1, N // d + 1):
            out[d * k] += left[d] * right[k]
    return out


def exponential(tape):
    assert tape[1] == 0
    unit = [Q(0)] * (N + 1)
    unit[1] = Q(1)
    out, power = unit[:], unit[:]
    for r in range(1, N.bit_length()):
        power = convolution(power, tape)
        out = [u + v / factorial(r) for u, v in zip(out, power)]
    return out


def logarithm(source):
    assert source[1] == 1
    h = source[:]
    h[1] = Q(0)
    out, power = [Q(0)] * (N + 1), h[:]
    for r in range(1, N.bit_length()):
        out = [u + Q((-1) ** (r + 1), r) * v
               for u, v in zip(out, power)]
        power = convolution(power, h)
    return out


def prime_power(n):
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        m, k = n, 0
        while m % p == 0:
            m //= p
            k += 1
        if m == 1:
            return p, k
    return None


def gram(tape, vectors):
    return [[sum((tape[n] ** 2 * x[n] * y[n]
                  for n in range(2, N + 1)), Q(0))
             for y in vectors] for x in vectors]


def gaussian_mul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def gaussian_sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def polynomial_product(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i+j] += x*y
    return out


def shifted(vector, multiplier):
    return {multiplier * n: value for n, value in vector.items()}


def difference_norm_squared(left, right):
    return sum((left.get(k, Q(0)) - right.get(k, Q(0)))**2
               for k in set(left) | set(right))


def polynomial(t):
    return t**8 - 16*t**6 + 46*t**4 - 16*t**2 + 1


def log_integer(n, terms=16):
    """Rational series bounds; x=(n-1)/(n+1) is in (0,1)."""
    x = Q(n - 1, n + 1)
    lower = sum((Q(2, 2*j + 1) * x**(2*j + 1)
                 for j in range(terms)), Q(0))
    tail = Q(2, 2*terms + 1) * x**(2*terms + 1) / (1 - x*x)
    return lower, lower + tail


def fraction(x):
    return str(x)


def main():
    source = [Q(0)] + [Q(1)] * N
    genuine = logarithm(source)
    for n in range(2, N + 1):
        pp = prime_power(n)
        assert genuine[n] == (Q(1, pp[1]) if pp else Q(0))
    assert exponential(genuine) == source

    plus, minus = genuine[:], genuine[:]
    plus[6], minus[6] = Q(1), Q(-1)
    a_plus, a_minus = exponential(plus), exponential(minus)
    assert logarithm(a_plus) == plus and logarithm(a_minus) == minus
    assert a_plus[6] == 2 and a_minus[6] == 0
    assert all(v >= 0 for v in a_plus[1:] + a_minus[1:])
    weight_mutant = genuine[:]
    weight_mutant[2] *= 2
    assert logarithm(exponential(weight_mutant))[2] == 2
    vectors = [[Q(0)] * (N + 1) for _ in range(3)]
    vectors[0][6] = 1
    vectors[1][2] = vectors[1][6] = 1
    vectors[2][3], vectors[2][6] = 1, -1
    witness = gram(plus, vectors)
    assert witness == gram(minus, vectors)
    assert witness == [[1, 1, -1], [1, 2, -1], [-1, -1, 2]]
    # Exact LDL factorization also records a positive control, not an RH gate.
    assert witness[0][0] == 1
    assert witness[1][1] - witness[1][0]**2 == 1
    assert witness[2][2] - witness[2][0]**2 == 1
    assert witness[1][2] - witness[1][0] * witness[0][2] == 0

    lo, hi = log_integer(6)
    scale = 10**6
    sqrt_floor = isqrt(6 * scale**2)
    inv_lo, inv_hi = Q(scale, sqrt_floor + 1), Q(scale, sqrt_floor)
    # Normalize the smooth bump to ||eta||_2=1, analytically in the dossier.
    delta_lower, delta_upper = -4 * hi * inv_hi, -4 * lo * inv_lo
    assert delta_lower <= delta_upper < 0

    chi = {0: (Q(0), Q(0)), 1: (Q(1), Q(0)),
           2: (Q(0), Q(1)), 3: (Q(0), Q(-1)), 4: (Q(-1), Q(0))}
    for x in range(5):
        for y in range(5):
            assert chi[(x*y) % 5] == gaussian_mul(chi[x], chi[y])
    chi_b6 = gaussian_sub(chi[1], gaussian_mul(chi[2], chi[3]))
    phase_b6 = gaussian_sub(chi[1], gaussian_mul((Q(0), Q(-1)), chi[3]))
    assert chi_b6 == (0, 0) and phase_b6 == (2, 0)

    # DH t is the unique root of P in (1/4,1/3); P'<0 throughout.
    left, right = Q(1, 4), Q(1, 3)
    derivative_bracket_upper = right**6 + 23*right**2 - 4
    assert polynomial(left) > 0 > polynomial(right)
    assert derivative_bracket_upper < 0
    dh_b6_bounds = (1 + left**2, 1 + right**2)
    assert dh_b6_bounds[0] > 0
    dh_product = polynomial_product((Q(0), Q(1)), (Q(0), Q(-1)))
    dh_b6 = [Q(1) - dh_product[0], -dh_product[1], -dh_product[2]]
    assert dh_b6 == [1, 0, 1]

    # Exact amplitude convention at square 4: b(4)log(4)/sqrt(4).
    assert genuine[4] * Q(1, 2) == Q(1, 4)
    assert genuine[4] * Q(1) == Q(1, 2)
    # omega=pi/log(2): canonical e^(i omega log(2))=-1;
    # doubled clock e^(i omega 2log(2))=+1, without numeric pi/log.
    phase_pair = tuple((-1)**clock_multiple for clock_multiple in (1, 2))
    assert phase_pair[0] != phase_pair[1]

    # Proper-isometry defect: V_2* e_1=0, (I-V_2 V_2*)e_1=e_1.
    e1 = {Q(1): Q(1)}
    adjoint = {n // 2: value for n, value in e1.items() if n % 2 == 0}
    defect_squared = difference_norm_squared(e1, shifted(adjoint, Q(2)))
    assert defect_squared == 1
    regular_shift_controls = []
    for m in range(2, 8):
        q = Q(m + 1, m)
        assert q != 1
        norm_squared = difference_norm_squared(shifted(e1, q), e1)
        assert norm_squared == 2
        regular_shift_controls.append({"q": str(q), "norm_squared": str(norm_squared)})

    receipt = {
        "schema": "succ.swm.e38.exact-controls.v1",
        "source_parent": SOURCE_PARENT,
        "import_origin": IMPORT_PARENT,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "horizon": N,
        "arithmetic": "Python Fraction; no floating-point integrations",
        "genuine_log_support_verified_through": N,
        "sign_tape_sources_a6": {"plus": "2", "minus": "0"},
        "prime_weight_mutation": {"n": 2, "genuine_b": "1", "mutated_b": "2"},
        "same_gram": [[str(v) for v in row] for row in witness],
        "gram_ldl_pivots": ["1", "1", "1"],
        "weil_delta": {
            "formula": "-4*log(6)/sqrt(6) for ||eta||_2=1",
            "certified_rational_interval": [str(delta_lower), str(delta_upper)],
            "strictly_negative": True,
            "arch_gamma_and_poles": "unchanged and cancel in delta",
        },
        "matched_q5_odd_controls": {
            "chi_b6": [str(v) for v in chi_b6],
            "single_prime_phase_mutant_b6": [str(v) for v in phase_b6],
            "dh_b6": "1+t^2",
            "dh_b6_polynomial_coefficients": [str(v) for v in dh_b6],
            "dh_t_polynomial": "t^8-16*t^6+46*t^4-16*t^2+1",
            "dh_t_interval": [str(left), str(right)],
            "endpoint_polynomial_values": [str(polynomial(left)), str(polynomial(right))],
            "derivative_bracket_upper": str(derivative_bracket_upper),
            "dh_b6_strict_bounds": [str(v) for v in dh_b6_bounds],
            "gamma": "(5/pi)^((s+1)/2)*Gamma((s+1)/2)",
            "poles": "none",
            "dh_root_number": "+1",
            "evaluation_scope": "source algebra and exact parameter selection, no completed DH sign evaluation",
        },
        "half_density_n4_log4_coefficients": ["1/4", "1/2"],
        "clock_phase_control": list(phase_pair),
        "V2_defect_norm_squared": str(defect_squared),
        "discrete_q_regular_shift_controls": regular_shift_controls,
        "completed_weil_positivity_certified": False,
        "nontrivial_zero_locations_read_or_used": False,
        "RH_PROVED": False,
        "exit_status": 0,
        "status": "EXACT_BOUNDED_CONTROLS_PASS",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
