"""Exact finite-prime *joint* readout of the authentic rational BBP source.

Q/Z local primary components differ from full Q_p coordinates. Every circle
phase is reconstructed from all prime torsion projections for each rational
source state, but this gives no estimate of the source-selected time average.

No floating point, π digits, or unproved distribution assumptions occur here.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from math import comb, isqrt, lcm
from typing import Iterable


def _nat(n: int, name: str, lower: int = 0) -> int:
    if type(n) is not int or n < lower:
        raise ValueError(f"{name} must be an integer >= {lower}")
    return n


def primes_through(cap: int) -> tuple[int, ...]:
    _nat(cap, 'cap')
    if cap < 2:
        return ()
    sieve = bytearray(b'\x01') * (cap + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(cap) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00' * ((cap - p*p)//p + 1)
    return tuple(p for p in range(2, cap + 1) if sieve[p])


def _prime(p: int) -> int:
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError('prime p required')
    return p


def _q(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError('exact int/Fraction required')
    return Q(value)


def forcing(n: int) -> Q:
    """Original four-pole BBP forcing; no decimal π input."""
    _nat(n, 'n', 1)
    return Q(4, 8*n - 7) - Q(2, 8*n - 4) - Q(1, 8*n - 3) - Q(1, 8*n - 2)


def forcing_odd(n: int) -> Q:
    """Algebraically equal three-term form with strictly odd denominators."""
    _nat(n, 'n', 1)
    return Q(4, 8*n - 7) - Q(1, 8*n - 3) - Q(3*n - 1, (2*n - 1)*(4*n - 1))


def states(count: int) -> tuple[Q, ...]:
    _nat(count, 'count', 1)
    result = [Q(0)]
    for n in range(1, count):
        result.append(16 * result[-1] + forcing(n))
    return tuple(result)


def denominator_primes(den: int, candidate_primes: Iterable[int] | None = None) -> dict[int, int]:
    _nat(den, 'den', 1)
    d = den
    factors: dict[int, int] = {}
    if candidate_primes is None:
        trial = 2
        while trial * trial <= d:
            if d % trial == 0:
                v = 0
                while d % trial == 0:
                    d //= trial
                    v += 1
                factors[trial] = v
            trial = 3 if trial == 2 else trial + 2
        if d > 1:
            factors[d] = 1
    else:
        for p in candidate_primes:
            _prime(p)
            if d % p:
                continue
            v = 0
            while d % p == 0:
                d //= p
                v += 1
            factors[p] = v
            if d == 1:
                break
        if d != 1:
            raise ValueError('insufficient prime candidate set to factor denominator')
    return factors


def local_primary(value: Q | int, p: int) -> Q:
    """Standard p-primary component of [value] in Q/Z, in [0,1)."""
    x = _q(value)
    p = _prime(p)
    d = x.denominator
    pv = 1
    while d % p == 0:
        d //= p
        pv *= p
    if pv == 1:
        return Q(0)
    # x=a/(p^v * d) with d unit in Z_p. Component c/p^v.
    c = (x.numerator * pow(d, -1, pv)) % pv
    return Q(c, pv)


def joint_primary(value: Q | int, candidates: Iterable[int] | None = None) -> tuple[tuple[int, Q], ...]:
    x = _q(value)
    return tuple((p, local_primary(x, p)) for p in sorted(denominator_primes(x.denominator, candidates)))


def joint_circle(value: Q | int, candidates: Iterable[int] | None = None) -> Q:
    """Global circle phase reconstructed from a *joint* finite prime family."""
    return sum((x for _, x in joint_primary(value, candidates)), Q(0)) % 1


def primary_window_phase(value: Q | int, primes: Iterable[int]) -> Q:
    return sum((local_primary(value, p) for p in primes), Q(0)) % 1


def dyadic_integral(value: Q | int, depth: int) -> int:
    """Full integral 2-adic residue. NOT the 2-primary Q/Z torsion."""
    _nat(depth, 'depth')
    x = _q(value)
    if x.denominator % 2 == 0:
        raise ValueError('not integral in Z_2')
    modulus = 2**depth
    if modulus == 1:
        return 0
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def source_prime_bound(index: int) -> int:
    """At time n, denominators divide integers <= max(5,8n-3)."""
    _nat(index, 'index')
    return max(0, 8*index - 3)


def source_torsion(index: int, values: tuple[Q, ...] | None = None) -> tuple[tuple[int, Q], ...]:
    _nat(index, 'index')
    if values is None:
        values = states(index + 1)
    if index >= len(values):
        raise ValueError('missing source state')
    return joint_primary(values[index], primes_through(source_prime_bound(index)))


def pascal_difference(values: Iterable[Q | int], order: int) -> Q:
    """Signed Newton/Pascal difference at source index zero."""
    _nat(order, 'order')
    values = tuple(map(_q, values))
    if len(values) <= order:
        raise ValueError('need at least order+1 values')
    return sum(((-1)**(order-j) * comb(order, j) * values[j] for j in range(order + 1)), Q(0))


def local_pascal_difference(values: Iterable[Q | int], order: int, p: int) -> Q:
    """True additive p-primary projection commutes with integer Pascal rows."""
    _nat(order, 'order'); _prime(p)
    seq = tuple(map(_q, values))
    return sum(((-1)**(order-j) * comb(order,j) * local_primary(seq[j],p)
                for j in range(order+1)), Q(0)) % 1


def known_tail_upper(index: int) -> Q:
    """Inherited BBP-positive-kernel bound 0<T_n<1/((8n+1)(8n+2))."""
    _nat(index, 'index')
    return Q(1, (8*index + 1)*(8*index + 2))


def floor_hex_digit(value: Q | int) -> int:
    phase = _q(value) % 1
    return (16 * phase.numerator)//phase.denominator


def certified_hex_digit(index: int, value: Q | int) -> int | None:
    """Guaranteed digit for {16^n*pi/16}, or None if enclosure crosses a gate.

    Uses 0 < T_n < known_tail_upper(n), n>=0; positive interval endpoints.
    """
    _nat(index, 'index')
    x = _q(value)
    lo = floor_hex_digit(x)
    # Entire open upper interval must stay within same floor 16 * fractional.
    # Treat boundary conservatively (None) even if exact endpoint equality.
    right = x + known_tail_upper(index)
    return lo if floor_hex_digit(right) == lo and (16*(right%1)).denominator != 1 else None


def conditional_squared_residual(values: Iterable[Q | int], primes: Iterable[int],
                                 gate_digit: int = 0) -> Q:
    """L2 projection residual for an explicitly declared finite empirical source.

    Group by *joint* primary torsion observations; no assumption of prime independence.
    The source here is the exactly supplied rational finite sample, not Haar.
    """
    values = tuple(map(_q, values))
    if not values:
        raise ValueError('nonempty sample required')
    if type(gate_digit) is not int or not 0 <= gate_digit < 16:
        raise ValueError('hexadecimal digit 0..15 required')
    chosen = tuple(primes)
    for p in chosen:
        _prime(p)
    buckets: dict[tuple[Q, ...], list[int]] = defaultdict(list)
    for value in values:
        buckets[tuple(local_primary(value, p) for p in chosen)].append(
            int(floor_hex_digit(value) == gate_digit))
    n = len(values)
    return sum((Q(sum(v)*(len(v)-sum(v)), len(v)*n) for v in buckets.values()), Q(0))


def four_gate_interaction(values: Iterable[Q | int], p: int, q: int, digit: int = 0) -> Q:
    """Full factorial two-place synergy: R(p)+R(q)-R(empty)-R(p,q)."""
    values = tuple(values)
    return (conditional_squared_residual(values, (p,), digit)
          + conditional_squared_residual(values, (q,), digit)
          - conditional_squared_residual(values, (), digit)
          - conditional_squared_residual(values, (p, q), digit))


def six_phase_control() -> tuple[Q, ...]:
    """All 2x3 primary coordinates once: exact joint observability witness."""
    return tuple((Q(a,2) + Q(b,3)) % 1 for a in range(2) for b in range(3))


def correlated_six_phase_control() -> tuple[Q, ...]:
    """Both active prime characters average zero; their product does not."""
    return (Q(0), Q(0), Q(1, 3), Q(5, 6), Q(1, 6), Q(1, 6))


def hidden_prime_halfway(q: int) -> Q:
    """q-primary only; real fraction tends to 1/2 as odd prime q increases."""
    _prime(q)
    if q == 2:
        raise ValueError('odd prime required')
    return Q(q - 1, 2*q)


def height_unique_threshold(common_denominator: int, real_bound: int) -> int:
    """If M exceeds this, joint congruences of B*x determine x in [-R,R]."""
    _nat(common_denominator,'common_denominator',1)
    _nat(real_bound,'real_bound',1)
    return 2*common_denominator*real_bound


def common_bbp_denominator(count: int) -> int:
    """Optional expensive exact common denominator for the first count states."""
    _nat(count, 'count', 1)
    b = 1
    for n in range(1, count):
        for d in (8*n-7, 8*n-3, 2*n-1, 4*n-1):
            b = lcm(b, d)
    return b


def _high_prime(p: int) -> int:
    _prime(p)
    if p < 7:
        raise ValueError('separate-pole theorem requires prime p>=7')
    return p


def valuation_rational(value: Q | int, p: int) -> int:
    """v_p(x) for nonzero exact rational x."""
    x = _q(value);_prime(p)
    if x == 0:
        raise ValueError('valuation of zero is infinite')
    def v(a: int) -> int:
        a=abs(a); k=0
        while a%p==0:
            a//=p;k+=1
        return k
    return v(x.numerator)-v(x.denominator)


def four_pole_residues(p: int, order: int = 1) -> tuple[int, ...]:
    """Exactly four DISTINCT pole residues mod p**order for p>=7."""
    _high_prime(p);_nat(order,'order',1)
    modulus=p**order
    residues=tuple(sorted({(c*pow(a,-1,modulus))%modulus
                           for a,c in ((8,7),(8,3),(2,1),(4,1))}))
    if len(residues)!=4:
        raise AssertionError('four disjoint source poles expected for p>=7')
    return residues


def pole_event(n: int, p: int, order: int = 1) -> bool:
    """v_p(r(n)) <= -order, exactly a union of 4 classes mod p**order."""
    _nat(n,'n',1)
    return n%(p**order) in four_pole_residues(p,order)


def first_prime_birth(p: int) -> int:
    """First time p-primary innovation is nontrivial, for p>=7."""
    _high_prime(p)
    residues=four_pole_residues(p)
    return min(r if r else p for r in residues)


def crt_pole_joint_period(prime_powers: Iterable[tuple[int, int]]) -> tuple[int, int]:
    """Period M and EXACT count of n mod M with all pole events active.

    Inputs have distinct primes >=7, depths >=1. CRT gives 4**len(states).
    This is a forcing-activation count, not a real carry/phase frequency.
    """
    items=tuple(prime_powers)
    if len({p for p,_ in items})!=len(items):
        raise ValueError('distinct prime labels required')
    modulus=1
    for p,k in items:
        _high_prime(p);_nat(k,'order',1)
        modulus*=p**k
    return (modulus,4**len(items))


def forcing_numerator(n: int) -> int:
    """120*n^2 - 89*n + 16; discriminant 241 (not a normality invariant)."""
    _nat(n, 'n')
    return 120*n*n - 89*n + 16


def forcing_product_form(n: int) -> Q:
    _nat(n,'n',1)
    return Q(forcing_numerator(n),
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def exceptional_numerator_root(p: int, depth: int) -> int:
    """Unique p-adic Hensel root of N(t) congruent to -1 mod p, p=3,5."""
    if p not in (3,5) or type(p) is not int:
        raise ValueError('exceptional prime must be 3 or 5')
    _nat(depth,'depth',1)
    ans=p-1
    modulus=p
    for _ in range(2,depth+1):
        possibilities=[ans+j*modulus for j in range(p)
                       if forcing_numerator(ans+j*modulus)%(p*modulus)==0]
        if len(possibilities)!=1:
            raise AssertionError('simple Hensel root must lift uniquely')
        ans=possibilities[0]
        modulus*=p
    return ans


def sixteen_clock_order(p: int, depth: int) -> int:
    """Exact multiplicative transport period of 16 mod p^depth, odd p.

    Finite exact calculation (not an analytic claim of source normality).
    For the long-period protocol use a factorization-based order algorithm.
    """
    _prime(p);_nat(depth,'depth',1)
    if p==2:
        raise ValueError('16 is not a unit at p=2')
    modulus=p**depth
    current=16%modulus
    period=1
    while current!=1:
        current=current*16%modulus
        period+=1
    return period


def source_innovation_poles(n: int) -> tuple[int, ...]:
    """Distinct p>=7 where authentic forcing r(n) has negative valuation."""
    _nat(n,'n',1)
    source_denominators=(8*n-7,8*n-3,2*n-1,4*n-1)
    candidates=set()
    for d in source_denominators:
        candidates.update(denominator_primes(d))
    return tuple(sorted(p for p in candidates if p>=7))
