"""Exact joint primary observers, real fibers and temporal dependence.

Primary coordinates of Q/Z jointly determine a rational circle point. A
proper subfamily need not approximate it in the real metric. All calculations
below are exact; the changed-source controls do not satisfy the BBP four-pole
forcing and no normality estimate is asserted.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, gcd, isqrt, prod

from .source_path_projector import bbp_circle_carrier

MAX_ENUMERATED_FIBER = 20_000
MAX_INDEPENDENT_PHASE_STATES = 100_000


def _integer(value, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("strict integer in the stated domain required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _prime(value):
    p = _integer(value, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("prime required")
    return p


def _primes(values):
    if type(values) not in (tuple, list):
        raise ValueError("tuple or list of distinct primes required")
    ps = tuple(_prime(p) for p in values)
    if len(set(ps)) != len(ps):
        raise ValueError("duplicate observer prime")
    return ps


def prime_support(value):
    """Distinct prime divisors of a positive integer, by trial division."""
    n = _integer(value, 1)
    result = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return tuple(result)


def _prime_part(n, p):
    part = 1
    while n % p == 0:
        n //= p
        part *= p
    return part


def circle_distance(value):
    value = _rational(value) % 1
    return min(value, 1-value)


def primary_phase(value, prime):
    """p-primary component of [value] in Q/Z, represented in [0,1)."""
    x, p = _rational(value), _prime(prime)
    part = _prime_part(x.denominator, p)
    if part == 1:
        return Q()
    complement = x.denominator // part
    return Q((x.numerator*pow(complement, -1, part)) % part, part)


def joint_primary_phases(value, primes):
    x, ps = _rational(value), _primes(primes)
    return tuple(primary_phase(x, p) for p in ps)


def joint_primary_fiber(modulus, observations):
    """Symbolic full fiber from (prime, primary phase) observations.

    Every allowed point is anchor+j/residual_modulus modulo one. Missing
    prime factors are not silently filled with independent random values.
    """
    D = _integer(modulus, 1)
    if type(observations) not in (tuple, list):
        raise ValueError("tuple or list of observer pairs required")
    pairs = []
    for row in observations:
        if type(row) not in (tuple, list) or len(row) != 2:
            raise ValueError("each observation is (prime, exact phase)")
        p, phase = _prime(row[0]), _rational(row[1]) % 1
        if _prime_part(D, p) % phase.denominator:
            raise ValueError("observed phase is not in the carrier p-part")
        pairs.append((p, phase))
    ps = _primes(tuple(p for p, _ in pairs))
    observed = prod(_prime_part(D, p) for p in ps)
    residual = D // observed
    anchor = sum((phase for _, phase in pairs), Q()) % 1
    return {"modulus": D, "observations": tuple(pairs), "anchor": anchor,
            "observed_modulus": observed, "residual_modulus": residual,
            "fiber_size": residual,
            "optimal_real_radius": Q(residual-1, 2*residual),
            "complete": residual == 1}


def primary_fiber_points(modulus, observations):
    """Enumerate a small fiber; large authentic carriers stay symbolic."""
    data = joint_primary_fiber(modulus, observations)
    R = data["residual_modulus"]
    if R > MAX_ENUMERATED_FIBER:
        raise ValueError("fiber enumeration exceeds explicit budget")
    return tuple(sorted((data["anchor"]+Q(j, R)) % 1 for j in range(R)))


def phase_law(phases):
    if type(phases) not in (tuple, list) or not phases:
        raise ValueError("nonempty exact phase list required")
    counts = Counter(_rational(x) % 1 for x in phases)
    n = len(phases)
    return tuple((x, Q(count, n)) for x, count in sorted(counts.items()))


def _phase_rows(rows):
    if type(rows) not in (tuple, list) or not rows:
        raise ValueError("nonempty list of joint observations required")
    if any(type(row) not in (tuple, list) or not row for row in rows):
        raise ValueError("nonempty observation rows required")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("observation rows have different widths")
    return tuple(tuple(_rational(x) % 1 for x in row) for row in rows)


def temporal_mixed_phase_law(rows):
    """Law of the SUM at the same times; its characters are mixed products."""
    data = _phase_rows(rows)
    return phase_law(tuple(sum(row, Q()) % 1 for row in data))


def independent_marginal_phase_law(rows):
    """Counterfactual product of time marginals, with explicit size guard."""
    data = _phase_rows(rows)
    law = {Q(): Q(1)}
    for j in range(len(data[0])):
        marginal = phase_law(tuple(row[j] for row in data))
        if len(law)*len(marginal) > MAX_INDEPENDENT_PHASE_STATES:
            raise ValueError("independent convolution exceeds explicit budget")
        next_law = Counter()
        for x, px in law.items():
            for y, py in marginal:
                next_law[(x+y) % 1] += px*py
        law = dict(next_law)
    return tuple(sorted(law.items()))


def carrier_sampling_obstruction(phases, modulus):
    """Exact TV and collision at the FULL microscopic carrier resolution."""
    D = _integer(modulus, 1)
    law = phase_law(phases)
    if any(D % x.denominator for x, _ in law):
        raise ValueError("sample phase does not belong to this carrier")
    support = len(law)
    tv = (sum((abs(weight-Q(1, D)) for _, weight in law), Q())
          + Q(D-support, D))/2
    collision = D*sum((weight*weight for _, weight in law), Q())
    n = len(phases)
    return {"modulus": D, "sample_count": n, "support_size": support,
            "total_variation_to_uniform_carrier": tv,
            "support_TV_lower_bound": Q(D-support, D),
            "sample_TV_lower_bound": max(Q(), 1-Q(n, D)),
            "scaled_collision": collision,
            "collision_lower_bound": max(Q(1), Q(D, n)),
            "resolution": "full finite carrier, not real coarse cells"}


def interval_residue_tv(length, modulus):
    """Exact TV of a uniform consecutive interval modulo q vs uniform q."""
    L, q = _integer(length, 1), _integer(modulus, 1)
    r = L % q
    return Q(r*(q-r), L*q)


def short_arc_crt_control(moduli, length):
    """Every proper joint CRT marginal can look uniform while the sum clusters."""
    if type(moduli) not in (tuple, list) or not 2 <= len(moduli) <= 12:
        raise ValueError("two through twelve coprime moduli required")
    qs = tuple(_integer(q, 2) for q in moduli)
    if any(gcd(q, r) != 1 for q, r in combinations(qs, 2)):
        raise ValueError("moduli must be pairwise coprime")
    D, L = prod(qs), _integer(length, 1)
    if L > D:
        raise ValueError("short arc length must not exceed carrier size")
    rows = []
    for k in range(1, len(qs)):
        for indices in combinations(range(len(qs)), k):
            q = prod(qs[i] for i in indices)
            rows.append({"indices": indices, "modulus": q,
                         "TV": interval_residue_tv(L, q),
                         "TV_upper_bound": Q(q, 4*L)})
    return {"moduli": qs, "modulus": D, "length": L,
            "real_arc_length": Q(L, D), "proper_marginals": tuple(rows),
            "all_proper_TV_upper_bound": Q(D//min(qs), 4*L),
            "full_joint_TV": 1-Q(L, D)}


def congruence_separation(modulus, valuation_lower_bounds):
    """Exact grid separation for a CHOSEN rational residual m/D.

    Input v_p(m/D)>=h_p forces a multiple of M in the numerator. Applying
    it to a circular residual requires the same chosen integer carry.
    """
    D = _integer(modulus, 1)
    if type(valuation_lower_bounds) not in (tuple, list):
        raise ValueError("prime/valuation pairs required")
    rows = []
    for row in valuation_lower_bounds:
        if type(row) not in (tuple, list) or len(row) != 2:
            raise ValueError("prime/valuation pair required")
        p, h = _prime(row[0]), _integer(row[1])
        part, exponent = _prime_part(D, p), 0
        while part > 1:
            part //= p
            exponent += 1
        rows.append((p, max(0, h+exponent)))
    _primes(tuple(p for p, _ in rows))
    multiple = prod(p**exponent for p, exponent in rows)
    return {"modulus": D, "numerator_multiple": multiple,
            "nonzero_absolute_separation": Q(multiple, D)}


def escaping_prime_history(constant, horizon, base=16):
    """Finite exact changed-source control; constant is rational here.

    The paper construction allows any real constant. Distinct prime supports
    move with time, forcing is eventually positive O(n^-2), and every fixed
    p-adic state tends to zero, even at increasing absolute local precision.
    This is NOT the authentic fixed rational-function forcing.
    """
    C = _rational(constant)
    nmax, b = _integer(horizon, 1), _integer(base, 2)
    primes = []
    p = 3
    while len(primes) < nmax:
        if all(p % d for d in range(2, isqrt(p)+1)):
            primes.append(p)
        p += 2
    prior = Q()
    rows = []
    for n, p in enumerate(primes, 1):
        q = p
        while q < 32**n:
            q *= p
        depth = (n+1).bit_length()-1
        numerator_multiple = factorial(depth)
        target = b**n*C-Q(1, (n+1)**2)
        scaled = q*target/numerator_multiple
        coefficient = scaled.numerator//scaled.denominator
        if coefficient % p == 0:
            coefficient -= 1
        state = Q(numerator_multiple*coefficient, q)
        tail = b**n*C-state
        rows.append({"n": n, "prime": p, "denominator": q,
                     "factorial_depth": depth,
                     "numerator_multiple": numerator_multiple,
                     "state": state, "phase": state % 1,
                     "forcing": state-b*prior, "tail": tail,
                     "tail_lower": Q(1, (n+1)**2),
                     "tail_upper": Q(1, (n+1)**2)+Q(2*numerator_multiple, q),
                     "uniform_tail_upper": Q(1, (n+1)**2)+Q(1, 16**n)})
        prior = state
    return {"constant": C, "base": b, "rows": tuple(rows),
            "scope": "changed forcing; not the authentic BBP four poles"}


def bbp_joint_primary_certificate(horizon):
    """Exact joint reconstruction of authentic BBP states, not frequencies."""
    data = bbp_circle_carrier(_integer(horizon, 1))
    D = data["modulus"]  # COMMON forcing denominator for the whole prefix.
    ps = prime_support(D)
    states = data["unwrapped_states"][1:]
    phases = data["phases"][1:]
    rows = tuple(joint_primary_phases(x, ps) for x in states)
    reconstructed = tuple(sum(row, Q()) % 1 for row in rows)
    if reconstructed != phases:
        raise AssertionError("joint primary reconstruction changed source phase")
    return {"horizon": horizon, "common_carrier_D_N": D,
            "individual_denominators_d_n": tuple(x.denominator for x in states),
            "prime_support": ps, "reconstructed_phases": reconstructed,
            "source_rows": rows, "initial_state_excluded_from_sample": True,
            "sampling_obstruction": carrier_sampling_obstruction(phases, D),
            "integer_lift": "retained separately by the original source",
            "normality": "OPEN"}


def source_matching_prime_escape(constant, horizon):
    """Changed source matches every authentic supported primary phase.

    At time n the only additional state prime exceeds 16n. Its denominator
    costs exp(o(n)), so scalar logarithmic height asymptotics survive. The
    exact authentic conductor is explicitly VIOLATED. For each fixed prime,
    the full p-adic state and forcing differences tend to zero.
    """
    C, nmax = _rational(constant), _integer(horizon, 1)
    authentic = bbp_circle_carrier(nmax)
    prior, prior_delta = Q(), Q()
    rows = []
    for n in range(1, nmax+1):
        p = 16*n+1
        while any(p % d == 0 for d in range(2, isqrt(p)+1)):
            p += 1
        depth = (n+1).bit_length()-1
        multiple = factorial(depth)
        threshold = 32*n**4*multiple
        q = p
        while q < threshold:
            q *= p
        original = authentic["unwrapped_states"][n]
        target = 16**n*C-Q(1, (n+1)**2)
        scaled = q*(target-original)/multiple
        k = scaled.numerator//scaled.denominator
        if k % p == 0:
            k -= 1
        delta = Q(multiple*k, q)
        state = original+delta
        tail = 16**n*C-state
        forcing = state-16*prior
        forcing_delta = delta-16*prior_delta
        if state.denominator != original.denominator*q:
            raise AssertionError("old and new source denominator factors cancelled")
        if forcing-authentic["forcing"][n-1] != forcing_delta:
            raise AssertionError("perturbed source recurrence did not commute")
        rows.append({"n": n, "prime": p, "new_prime_denominator": q,
                     "factorial_depth": depth, "numerator_multiple": multiple,
                     "original_state": original, "original_forcing": authentic["forcing"][n-1],
                     "original_denominator": original.denominator,
                     "state": state, "phase": state % 1, "state_difference": delta,
                     "forcing": forcing, "forcing_difference": forcing_delta,
                     "tail": tail, "tail_lower": Q(1, (n+1)**2),
                     "tail_upper": Q(1, (n+1)**2)+Q(2*multiple, q),
                     "uniform_tail_upper": Q(1, (n+1)**2)+Q(1, 16*n**4)})
        prior, prior_delta = state, delta
    return {"constant": C, "base": 16, "rows": tuple(rows),
            "scope": "matches authentic primary support; violates exact conductor and four-pole forcing"}
