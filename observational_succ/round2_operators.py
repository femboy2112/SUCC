"""Exact finite controls for forward disjointness and normalized GCD Grams.

Infinite claims are paper proofs in ROUND2_OPERATORS.md. No float eigenvalue,
finite sieve, or successful control is treated as an infinite theorem.
"""
from collections import deque
from fractions import Fraction as Q
from math import gcd, isqrt


def integer(value, lower=1, upper=20000):
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError("integer outside bounded exact domain")
    return value


def prime_family(values):
    if type(values) is not tuple or len(set(values)) != len(values):
        raise ValueError("distinct tuple of primes required")
    for p in values:
        integer(p, 2, 1000)
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            raise ValueError("composite generator is not a prime")
    return values


def semigroup_prefix(primes, limit):
    primes = prime_family(primes)
    integer(limit)
    answer = []
    for n in range(1, limit + 1):
        remaining = n
        for p in primes:
            while remaining % p == 0:
                remaining //= p
        if remaining == 1:
            answer.append(n)
    return tuple(answer)


def residue_transport(primes, modulus, limit):
    """Finite-group inverse representatives and exact harmonic transport.

    Every residue in the generated subgroup has a fixed positive monoid
    representative. Its inverse representative transports that entire class
    into residue 1. The overlap multiplicity is at most the subgroup order.
    """
    primes = prime_family(primes)
    integer(modulus, 1, 64)
    integer(limit)
    if any(gcd(p, modulus) != 1 for p in primes):
        raise ValueError("remove generators dividing the character modulus")
    identity = 1 % modulus
    reps = {identity: 1}
    queue = deque([identity])
    while queue:
        residue = queue.popleft()
        for p in primes:
            following = residue * p % modulus
            if following not in reps:
                reps[following] = reps[residue] * p
                queue.append(following)
    inverse = {r: reps[next(s for s in reps if r*s % modulus == identity)] for r in reps}
    prefix = semigroup_prefix(primes, limit)
    total = sum((Q(1, n) for n in prefix), Q())
    images = [inverse[n % modulus] * n for n in prefix]
    transported = sum((Q(1, n) for n in images), Q())
    distinct = sum((Q(1, n) for n in set(images)), Q())
    h, maximum = len(reps), max(inverse.values())
    assert all(n % modulus == identity for n in images)
    assert total / maximum <= transported <= h * distinct
    return dict(modulus=modulus, primes=primes, limit=limit,
                subgroup_representatives=reps, inverse_multipliers=inverse,
                subgroup_order=h, maximum_multiplier=maximum,
                monoid_prefix_mass=total, transported_mass_with_multiplicity=transported,
                identity_image_mass=distinct, certified_identity_mass_lower=total/(h*maximum),
                maximum_image=max(images), authority="EXACT_FINITE_CONTROL")


def character_polynomial(values, frequency):
    """DFT in Q[X]/(X^q-1); evaluation at exp(2pi i/q) gives the pairing."""
    if type(values) is not tuple or not values or any(type(v) not in (int, Q) for v in values):
        raise ValueError("nonempty exact rational cylinder required")
    q = integer(len(values), 1, 64)
    if type(frequency) is not int:
        raise ValueError("integer frequency required")
    out = [Q(0)] * q
    for x, value in enumerate(values):
        out[(-frequency*x) % q] += Q(value, q)
    return tuple(out)


def scaled_cutoff_character_polynomial(values, n, frequency):
    """Direct finite residue integral for sqrt(n)<U_n f,chi_frequency/q>."""
    character_polynomial(values, frequency)
    integer(n, 1, 256)
    q = len(values)
    out = [Q(0)] * q
    for x in range(n*q):
        if x % n == 0:
            # The factor n cancels the Haar period n*q exactly.
            out[(-frequency*x) % q] += Q(values[(x//n) % q], q)
    return tuple(out)


def harmonic(n):
    integer(n)
    return sum((Q(1, k) for k in range(1, n + 1)), Q())


def totient(n):
    integer(n)
    return sum(gcd(n, k) == 1 for k in range(1, n + 1))


def gcd_matrix(n):
    integer(n, 1, 64)
    return tuple(tuple(gcd(i, j) for j in range(1, n + 1)) for i in range(1, n + 1))


def determinant(matrix):
    """Independent exact elimination, including singular controls."""
    rows = [list(map(Q, row)) for row in matrix]
    n = len(rows)
    if not n or any(len(row) != n for row in rows):
        raise ValueError("nonempty square matrix required")
    det = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            rows[pivot], rows[j] = rows[j], rows[pivot]
            det = -det
        diagonal = rows[j][j]
        det *= diagonal
        for i in range(j + 1, n):
            scale = rows[i][j] / diagonal
            for k in range(j + 1, n):
                rows[i][k] -= scale * rows[j][k]
            rows[i][j] = Q(0)
    return det


def spectral_certificate(n, iterations=4):
    """Rational Rayleigh/weighted-Schur brackets for ||T_N||^2=lambda_max(K).

    L_ij=gcd(i,j)/j is diagonally similar to K_ij=gcd(i,j)/sqrt(ij).
    x>0 corresponds to v_i=x_i/sqrt(i); no radical arithmetic is needed.
    """
    integer(n, 1, 64)
    integer(iterations, 0, 8)
    B = gcd_matrix(n)
    x = tuple(Q(1) for _ in range(n))
    history = []
    for step in range(iterations + 1):
        image = tuple(sum((Q(B[i][j], j+1)*x[j] for j in range(n)), Q()) for i in range(n))
        denominator = sum((x[i]**2 / (i+1) for i in range(n)), Q())
        rayleigh = sum((x[i]*image[i]/(i+1) for i in range(n)), Q()) / denominator
        upper = max(image[i]/x[i] for i in range(n))
        history.append(dict(iteration=step, rayleigh_lower=rayleigh, weighted_Schur_upper=upper))
        if step != iterations:
            x = tuple(y / image[0] for y in image)
    H = harmonic(n)
    divisor_lower = sum((Q(totient(d), d*d)*harmonic(n//d)**2 for d in range(1, n+1)), Q()) / H
    assert divisor_lower == history[0]["rayleigh_lower"] >= H
    lower = max(row["rayleigh_lower"] for row in history)
    upper = min(row["weighted_Schur_upper"] for row in history)
    assert H <= lower <= upper <= n
    return dict(N=n, harmonic_lower=H, divisor_Rayleigh_lower=divisor_lower,
                lower_squared_operator_norm=lower, upper_squared_operator_norm=upper,
                final_positive_weights=x, iterations=iterations, history=history,
                authority="EXACT_RATIONAL_SPECTRAL_ENCLOSURE")
