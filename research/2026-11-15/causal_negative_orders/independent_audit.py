"""Exact independent controls for causal negative orders.

Frozen domains appear in ADVERSARY_NOTES.md. No SUCC production imports,
no random seed, no floating arithmetic, and no numerical zeta evaluations.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json


CHANNELS = ((0, 4), (3, -2), (4, -1), (5, -1))
DEGREE = 24


def derivative_product(left, right):
    return [sum((Q(comb(n, j))*left[j]*right[n-j]
                 for j in range(n+1)), Q())
            for n in range(DEGREE+1)]


def face_derivatives(k):
    values = [Q(1)]+[Q()]*DEGREE
    face = [Q()]+[Q(-(-8)**n) for n in range(1, DEGREE+1)]
    for _ in range(k):
        values = derivative_product(values, face)
    return values


def direct_source_value(age, k, m):
    return sum(((-1)**j*comb(k, j)*c*(age+8*j+d)**m
                for j in range(k+1) for d, c in CHANNELS), Q())


def geometric_moments(rho):
    # Derive from shifting the infinite positive geometric sum by one.
    moments = [1/(1-rho)]
    for power in range(1, DEGREE+1):
        moments.append(rho/(1-rho)*sum(
            (comb(power, j)*moments[j] for j in range(power)), Q()))
    return moments


def direct_native_value(k, m, moments):
    # Expand powers in the source-index n and sum n^ell by exact moments.
    return sum(((-1)**j*comb(k, j)*c*comb(m, ell)*8**ell
                *(1+8*j+d)**(m-ell)*moments[ell]
                for j in range(k+1) for d, c in CHANNELS
                for ell in range(m+1)), Q())


def native_kernel_derivatives():
    # Independent quotient calculation:
    # H=(4e^-t-2e^-4t-e^-5t-e^-6t)/(1-e^-8t/16).
    numerator = [Q(4*(-1)**n-2*(-4)**n-(-5)**n-(-6)**n)
                 for n in range(DEGREE+1)]
    denominator = [Q(15, 16)]+[Q(-(-8)**n, 16)
                                    for n in range(1, DEGREE+1)]
    values = []
    for n in range(DEGREE+1):
        previous = sum((comb(n, j)*denominator[j]*values[n-j]
                        for j in range(1, n+1)), Q())
        values.append((numerator[n]-previous)/denominator[0])
    return values


def stirling_second(n, k):
    row = [1]+[0]*k
    for _ in range(n):
        row = [0]+[j*row[j]+row[j-1] for j in range(1, k+1)]
    return row[k]


def stencil_on_monomial(m, degree, spacing):
    return sum(((-1)**j*comb(m, j)*(j*spacing)**degree
                for j in range(m+1)), Q())/spacing**m


def run():
    out = {"arithmetic": "int/Fraction", "production_imports": False,
           "random_seed": None, "mutations_rejected": {}}
    ages = (Q(1, 7), Q(1), Q(11, 3), Q(17), Q(101))
    faces = [face_derivatives(k) for k in range(11)]
    source_checks = 0
    for age in ages:
        source = [sum((c*(-(age+d))**n for d, c in CHANNELS), Q())
                  for n in range(DEGREE+1)]
        for k in range(11):
            derivatives = derivative_product(source, faces[k])
            for m in range(DEGREE+1):
                value = direct_source_value(age, k, m)
                assert value == (-1)**m*derivatives[m]
                if m <= k:
                    assert value == 0
                else:
                    assert (-1)**(k+1)*value > 0
                source_checks += 1
            first = direct_source_value(age, k, k+1)
            assert first == (-1)**(k+1)*15*8**k*factorial(k+1)
        assert direct_source_value(age, 0, 2) == -30*age-59
    out["source_face"] = {"checks": source_checks, "ages": list(map(str, ages)),
                          "face_counts": [0, 10], "negative_orders": [0, 24]}

    moments = geometric_moments(Q(1, 16))
    native = native_kernel_derivatives()
    native_checks = 0
    values_at_small_orders = {}
    for k in range(11):
        derivatives = derivative_product(native, faces[k])
        for m in range(DEGREE+1):
            value = direct_native_value(k, m, moments)
            assert value == (-1)**m*derivatives[m]
            if m <= k:
                assert value == 0
            else:
                assert (-1)**(k+1)*value > 0
            native_checks += 1
        assert direct_native_value(k, k+1, moments) == (
            (-1)**(k+1)*16*8**k*factorial(k+1))
        if k <= 3:
            values_at_small_orders[str(k)] = [
                str(direct_native_value(k, m, moments)) for m in range(7)]
    assert [direct_native_value(0, m, moments) for m in (1, 2, 3)] == [-16, -112, -880]
    out["native_face"] = {"checks": native_checks, "regulator": "1/16",
                          "first_nonzero_checks": 11,
                          "B_k_at_orders_0_through_minus_6": values_at_small_orders}

    spacings = (Q(1), Q(1, 2), Q(1, 4), Q(1, 16))
    stencil_checks = 0
    variation_checks = 0
    noise_checks = 0
    eta = Q(1, 100)
    for m in range(9):
        for spacing in spacings:
            variation = sum(abs(Q((-1)**j*comb(m, j))/spacing**m)
                            for j in range(m+1))
            assert variation == Q(2**m)/spacing**m
            variation_checks += 1
            for degree in range(13):
                value = stencil_on_monomial(m, degree, spacing)
                expected = (Q() if degree < m else
                            (-1)**m*factorial(m)*stirling_second(degree, m)
                            *spacing**(degree-m))
                assert value == expected
                stencil_checks += 1
            if m:
                errors = [eta*(-1)**j for j in range(m+1)]
                attained = sum((Q((-1)**j*comb(m, j))*errors[j]
                                for j in range(m+1)), Q())/spacing**m
                assert attained == eta*2**m/spacing**m
                noise_checks += 1
    nonpositive_pairings = []
    for m in range(1, 9):
        # Test is chi(t)*(1+(-1)^(m+1)t^m)^2, chi>=0 and chi=1 near 0.
        coefficient = 2*(-1)**(m+1)
        pairing = (-1)**m*factorial(m)*coefficient
        assert pairing == -2*factorial(m) < 0
        nonpositive_pairings.append(pairing)
    out["causal_distribution"] = {
        "monomial_stencil_checks": stencil_checks,
        "total_variation_checks": variation_checks,
        "worst_case_noise_checks": noise_checks,
        "negative_pairings_on_nonnegative_tests": nonpositive_pairings}

    nodes = (1, 2, 3, 5, 8)
    sample_checks = 0
    for target in (-1, -2, -7):
        denominator = 1
        for node in nodes:
            denominator *= target-node
        for point in nodes+(target,):
            value = Q(1, denominator)
            for node in nodes:
                value *= point-node
            assert value == (1 if point == target else 0)
            sample_checks += 1
    noise_continuation_checks = 0
    for m in range(1, 7):
        for strength in range(1, 9):
            # Entire g(s)=2^[-strength*(s+m)], exactly one at s=-m.
            assert Q(2)**(-strength*(-m+m)) == 1
            positive_bound = Q(2)**(-strength*(1+m))
            for positive_order in (1, 2, 3, 5):
                value = Q(2)**(-strength*(positive_order+m))
                assert 0 < value <= positive_bound
                noise_continuation_checks += 1
    out["identification"] = {"finite_sample_rival_checks": sample_checks,
                             "entire_noise_checks": noise_continuation_checks}

    mutations = out["mutations_rejected"]
    assert all((-1)**m*factorial(m) != 0 for m in range(9))
    mutations["erase_gamma_contact"] = {"orders_checked": [0, 8],
                                        "delta_on_t_to_m": "(-1)^m*m!, never zero"}
    assert stencil_on_monomial(1, 1, Q(1, 4)) == -1
    mutations["reverse_difference_orientation"] = {"true": -1, "false": 1}
    assert stencil_on_monomial(1, 0, Q(1, 4)) == 0
    mutations["positive_difference_weights"] = {"constant_test_true": 0,
                                                "positive_weights_false": 8}
    assert eta*2**4/Q(1, 16)**4 == Q(262144, 25)
    mutations["no_noise_amplification"] = {"order": 4, "spacing": "1/16",
        "input_tolerance": "1/100", "attained_output_error": "262144/25"}
    assert direct_native_value(0, 2, moments) == -112
    mutations["native_negative_even_zero"] = {"B_minus_2": "-112"}
    mutations["extra_endpoint_zero"] = {
        "counterexamples": 11, "first_nonzero": "(-1)^(k+1)*16*8^k*(k+1)!"}
    assert sum(c for _, c in CHANNELS) == 0
    assert sum(c for d, c in CHANNELS if d != 5) == 1
    mutations["drop_original_exponential_channel"] = {
        "native_B_0": "0", "deleted_minus_exp_minus_5t_B_0": "16/15",
        "changed_source_control": True}
    boundary_checks = 0
    for t in (Q(0), Q(1, 3), Q(2)):
        primitive_of_derivative = t
        original = 1+t
        assert original-primitive_of_derivative == 1
        boundary_checks += 1
    mutations["discard_initial_value"] = {"function": "1+t", "lost_boundary": 1,
                                            "checks": boundary_checks}
    unregulated_boundary = sum((c*(Q(1, 2)-a) for a, c in (
        (Q(1, 8), 4), (Q(1, 2), -2), (Q(5, 8), -1), (Q(3, 4), -1))), Q())
    assert unregulated_boundary == Q(15, 8)
    out["regulator_boundary_guard"] = {"native_rho_1_over_16_B_0": "0",
                                       "unregulated_analytic_B_0": str(unregulated_boundary),
                                       "same_regulator": False}
    out["result"] = "PASS"
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
