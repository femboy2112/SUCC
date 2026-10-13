"""Independent exact SWM-X08 probes for affine clocks and arithmetic audits.

The universal statements and proofs are in X08.md and X08_REVIEW.md. These
finite algorithms use no imported repair or arithmetic-log implementation.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import gcd, isqrt
import random


def partitions(size):
    """Each set partition once, as a restricted-growth word."""
    if type(size) is not int or size < 1:
        raise ValueError("Positive finite carrier size required")

    def extend(prefix):
        if len(prefix) == size:
            yield prefix
        else:
            for value in range(max(prefix) + 2):
                yield from extend(prefix + (value,))

    yield from extend((0,))


def canonical(values):
    ids = {}
    return tuple(ids.setdefault(value, len(ids)) for value in values)


def stable(labels, action):
    if len(labels) != len(action) or any(type(x) is not int or not 0 <= x < len(labels)
                                        for x in action):
        raise ValueError("Complete same-carrier action required")
    return all(labels[x] != labels[y] or labels[action[x]] == labels[action[y]]
               for x in range(len(labels)) for y in range(len(labels)))


def fixed_point_repair(labels, actions):
    """Independent forward signature refinement, all actions at each round."""
    current = canonical(labels)
    for action in actions:
        stable(current, action)  # type and domain validation
    while True:
        following = canonical(tuple((current[x],) + tuple(current[a[x]] for a in actions)
                                    for x in range(len(current))))
        if following == current:
            return current
        current = following


def cyclic_word_kernel(labels):
    """Independent all-successor-word oracle: m shifts suffice on C_m."""
    size = len(labels)
    return canonical(tuple(tuple(labels[(x + k) % size] for k in range(size))
                           for x in range(size)))


def least_report_period(labels):
    """Least positive cyclic period. No primality or action closure is assumed."""
    if not labels:
        raise ValueError("Nonempty complete report required")
    size = len(labels)
    return next(d for d in range(1, size + 1)
                if all(labels[(x + d) % size] == labels[x] for x in range(size)))


def valuation_report(prime, exponent):
    if type(prime) is not int or prime < 2 or any(prime % d == 0
                                                for d in range(2, isqrt(prime) + 1)):
        raise ValueError("Prime required")
    if type(exponent) is not int or exponent < 1:
        raise ValueError("Positive truncation exponent required")
    size = prime**exponent
    result = []
    for x in range(size):
        depth = 0
        while depth < exponent and x % (prime ** (depth + 1)) == 0:
            depth += 1
        result.append(depth)
    return tuple(result)


def convolution(left, right):
    if len(left) != len(right):
        raise ValueError("Equal supplied horizons required")
    return tuple(Fraction(0) if n == 0 else
                 sum((left[d] * right[n // d] for d in range(1, n + 1) if n % d == 0),
                     Fraction(0)) for n in range(len(left)))


def direct_log(source):
    """Literal locally finite convolution-power logarithm over Q."""
    if len(source) < 2 or source[1] != 1:
        raise ValueError("Normalized complete prefix required")
    horizon = len(source) - 1
    increment = tuple(Fraction(0) if n <= 1 else Fraction(source[n])
                      for n in range(horizon + 1))
    power = increment
    result = [Fraction(0)] * (horizon + 1)
    degree = 1
    while 2**degree <= horizon:
        for n in range(2, horizon + 1):
            result[n] += Fraction((-1)**(degree + 1), degree) * power[n]
        power = convolution(power, increment)
        degree += 1
    return tuple(result)


def prime_power(n):
    if n < 2:
        return False
    d = next((d for d in range(2, n + 1) if n % d == 0), n)
    while n % d == 0:
        n //= d
    return n == 1


def coprime_multiplicative(source):
    horizon = len(source) - 1
    return all(source[u*v] == source[u]*source[v]
               for u in range(1, horizon + 1) for v in range(1, horizon//u + 1)
               if gcd(u, v) == 1)


def pair_covariance(weights, features):
    """Independent pair-difference covariance formula, all exact rational."""
    if len(weights) != len(features) or not weights or sum(weights) <= 0:
        raise ValueError("Matched positive-mass weighted feature family required")
    dimension = len(features[0])
    if any(w < 0 for w in weights) or any(len(v) != dimension for v in features):
        raise ValueError("Nonnegative weights and a fixed feature dimension required")
    mass = sum(weights)
    return tuple(tuple(sum((weights[i]*weights[j]*(features[i][a]-features[j][a])
                            *(features[i][b]-features[j][b])
                            for i in range(len(weights)) for j in range(len(weights))),
                           Fraction(0))/(2*mass*mass)
                       for b in range(dimension)) for a in range(dimension))


def x08_receipt():
    """Finite independent oracles plus explicit cross-checks of cohort code."""
    from .swarm_arithmetic import cyclic_frame_offsets, dirichlet_log, valuation_covariance

    partition_count = 0
    stable_counts = {}
    for size in range(1, 9):
        successor = tuple((x + 1) % size for x in range(size))
        dilations = tuple(tuple(a*x % size for x in range(size)) for a in (2, 3, 5))
        stable_count = 0
        congruences = {tuple(x % d for x in range(size))
                      for d in range(1, size + 1) if size % d == 0}
        for labels in partitions(size):
            partition_count += 1
            is_stable = stable(labels, successor)
            assert is_stable == (labels in congruences)
            stable_count += is_stable
            period = least_report_period(labels)
            predicted = tuple(x % period for x in range(size))
            assert size % period == 0
            assert cyclic_word_kernel(labels) == predicted
            assert fixed_point_repair(labels, (successor,) + dilations) == predicted
            # Both repair orders are absorbed by successor repair.
            assert fixed_point_repair(fixed_point_repair(labels, dilations),
                                      (successor,)) == predicted
            assert fixed_point_repair(predicted, dilations) == predicted
        stable_counts[str(size)] = stable_count

    frame_cases = 0
    permutation_count = 0
    for size in range(1, 9):
        successor_commutants = []
        for frame in permutations(range(size)):
            permutation_count += 1
            if all(frame[(x + 1) % size] == (frame[x] + 1) % size for x in range(size)):
                successor_commutants.append(frame)
        for slopes in ((), (1,), (2,), (3,), (5,), (3, 5), (4, 7)):
            frames = tuple(frame for frame in successor_commutants
                           if all(frame[a*x % size] == a*frame[x] % size
                                  for a in slopes for x in range(size)))
            predicted_offsets = cyclic_frame_offsets(size, slopes)
            assert {frame[0] for frame in frames} == set(predicted_offsets)
            frame_cases += 1

    commutation_cases = 0
    quotient_squares = 0
    for size in range(1, 65):
        for slope in range(16):
            commute = all((slope*(x+1)) % size == (slope*x+1) % size
                          for x in range(size))
            assert commute == ((slope - 1) % size == 0)
            commutation_cases += 1
            for divisor in range(1, size + 1):
                if size % divisor == 0:
                    for offset in (0, 1, 7):
                        assert all(((slope*x+offset) % size) % divisor
                                   == (slope*(x % divisor)+offset) % divisor
                                   for x in range(size))
                        quotient_squares += 1

    valuation_cases = []
    for prime, exponents in ((2, range(1, 7)), (3, range(1, 5)),
                             (5, range(1, 3)), (7, range(1, 3))):
        for exponent in exponents:
            labels = valuation_report(prime, exponent)
            size = len(labels)
            successor = tuple((x+1) % size for x in range(size))
            assert all(stable(labels, tuple(a*x % size for x in range(size)))
                       for a in range(16))
            assert least_report_period(labels) == size
            assert fixed_point_repair(labels, (successor,)) == tuple(range(size))
            valuation_cases.append([prime, exponent, size, len(set(labels))])

    log_cases = 0
    for tail in product((0, 1), repeat=11):
        source = (0, 1) + tail
        logarithm = direct_log(source)
        assert all(logarithm[n] == 0 for n in range(2, 13) if not prime_power(n)) \
            == coprime_multiplicative(source)
        production = dirichlet_log(dict(enumerate(source[1:], 1)), 12)
        assert all(production[n].re == logarithm[n] and production[n].im == 0
                   for n in range(2, 13))
        log_cases += 1
    rng = random.Random(800836)
    for _ in range(128):
        source = (0, 1) + tuple(Fraction(rng.randrange(-3, 4), rng.randrange(1, 5))
                                for _ in range(29))
        logarithm = direct_log(source)
        production = dirichlet_log(dict(enumerate(source[1:], 1)), 30)
        assert all(production[n].re == logarithm[n] and production[n].im == 0
                   for n in range(2, 31))
        assert all(logarithm[n] == 0 for n in range(2, 31) if not prime_power(n)) \
            == coprime_multiplicative(source)
        log_cases += 1

    authentic = {n: 1 for n in range(1, 7)}
    mutant = dict(authentic)
    mutant[6] = -1
    weights = tuple(Fraction(1, n) for n in range(1, 7))
    features = ((0, 0), (1, 0), (0, 1), (2, 0), (0, 0), (1, 1))
    covariance = pair_covariance(weights, features)
    assert covariance == valuation_covariance(authentic, 6, (2, 3))
    assert covariance == valuation_covariance(mutant, 6, (2, 3))
    determinant = covariance[0][0]*covariance[1][1]-covariance[0][1]**2
    assert covariance[0][0] > 0 and determinant > 0
    source_a = tuple([0] + [authentic[n] for n in range(1, 7)])
    source_b = tuple([0] + [mutant[n] for n in range(1, 7)])
    assert direct_log(source_a)[6] == 0 and direct_log(source_b)[6] == -2

    nonlinear = (0, 0, 1, 0)
    parity = (0, 1, 0, 1)
    successor4 = (1, 2, 3, 0)
    assert stable(parity, successor4) and not stable(parity, nonlinear)
    assert fixed_point_repair(parity, (successor4, nonlinear)) == (0, 1, 2, 3)
    # Arithmetic-specific failure of central-holonomy extrapolation. Product
    # D S D^-1 S^-1 is evaluated right to left; D = D^-1 on C_3.
    shift3, dilation2 = (1, 2, 0), (0, 2, 1)
    inverse_shift3 = (2, 0, 1)
    commutator = tuple(dilation2[shift3[dilation2[inverse_shift3[x]]]] for x in range(3))
    assert commutator == shift3
    assert tuple(dilation2[commutator[x]] for x in range(3)) \
        != tuple(commutator[dilation2[x]] for x in range(3))
    return {
        "mission": "SWM-X08", "base_commit": "a4fa7c372662f7c17502c58ea78121ec864c22b2",
        "status": "PROVED LOCAL (paper); exact controls passed; three Nat affine-stability Lean lemmas",
        "clock_partition_cases": partition_count,
        "successor_stable_partition_counts": stable_counts,
        "frame_permutations_examined": permutation_count, "frame_family_cases": frame_cases,
        "noncommutation_cases": commutation_cases, "affine_quotient_squares": quotient_squares,
        "valuation_cases_p_k_size_initial_blocks": valuation_cases,
        "independent_log_source_cases": log_cases, "rational_source_seed": 800836,
        "phase_covariance": [[str(x) for x in row] for row in covariance],
        "phase_covariance_determinant": str(determinant), "phase_log6": ["0", "-2"],
        "valuation_successor_counterexample": {"modulus": 3, "prime": 3,
            "reports": [1, 0, 0], "original_pair": [1, 2], "after_successor": [2, 0],
            "after_reports": [0, 1]},
        "nonlinear_mutation": {"modulus": 4, "report": list(parity),
            "action": list(nonlinear), "same_report_pair": [0, 2],
            "after_reports": [0, 1], "joint_repair": [0, 1, 2, 3]},
        "affine_holonomy_mutation": {"modulus": 3, "successor": list(shift3),
            "prime_dilation": list(dilation2), "D_S_Dinv_Sinv": list(commutator),
            "commutator_central": False},
        "global_RH_or_Weil_claim": False, "nontrivial_zero_inputs": False,
    }
