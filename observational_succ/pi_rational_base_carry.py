"""Exact rational-base digit carries and authentic BBP source Pascal bridges.

Source: Akiyama--Frougny--Sakarovitch integer p/q algorithm (classical).
No result here establishes pi normality or selected real-circle cancellation.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd


def base_pair(p: int, q: int) -> tuple[int, int]:
    if type(p) is not int or type(q) is not int or p <= q or q < 1 or gcd(p, q) != 1:
        raise ValueError('require coprime integers p>q>=1')
    return p, q


def rational_base_digits(N: int, p: int, q: int) -> tuple[int, ...]:
    """Least significant digits first; zero has the empty representation."""
    base_pair(p, q)
    if type(N) is not int or N < 0:
        raise ValueError('nonnegative integer N required')
    digits = []
    while N:
        N, digit = divmod(q * N, p)
        digits.append(digit)
    return tuple(digits)


def rational_base_value(digits: tuple[int, ...], p: int, q: int) -> Fraction:
    base_pair(p, q)
    if not isinstance(digits, tuple) or any(type(a) is not int or a < 0 or a >= p for a in digits):
        raise ValueError('digits must be a tuple of base-p integer digits')
    return sum((Fraction(a, q) * Fraction(p, q)**i for i, a in enumerate(digits)), Fraction())


def prefix_from_residue(N: int, p: int, q: int, depth: int) -> tuple[int, ...]:
    """Return exactly the first depth digits; N can be any integer via p-adic residue."""
    base_pair(p, q)
    if type(N) is not int or type(depth) is not int or depth < 0:
        raise ValueError('integer N and nonnegative integer depth required')
    N %= p**depth
    digits = []
    for _ in range(depth):
        N, a = divmod(q * N, p)
        digits.append(a)
    return tuple(digits)


def residue_from_prefix(digits: tuple[int, ...], p: int, q: int) -> int:
    """Inverse bijection to Z/(p^L), including padded leading zeros."""
    base_pair(p, q)
    if not isinstance(digits, tuple) or any(type(a) is not int or a < 0 or a >= p for a in digits):
        raise ValueError('invalid finite digit word')
    L = len(digits)
    mod = p**L
    if mod == 1:
        return 0
    numerator = sum(a * p**i * q**(L-1-i) for i, a in enumerate(digits))
    return numerator * pow(q**L, -1, mod) % mod


def pascal_additive_terms(digits: tuple[int, ...], p: int, q: int) -> tuple[Fraction, ...]:
    """For p=q+1, N= sum_j q^(-j-1) sum_i>=j comb(i,j)*a_i."""
    base_pair(p, q)
    if p != q + 1:
        raise ValueError('this binomial expansion requires p=q+1')
    if any(type(a) is not int or a < 0 or a >= p for a in digits):
        raise ValueError('invalid digit')
    return tuple(Fraction(sum(comb(i, j)*digits[i] for i in range(j, len(digits))), q**(j+1))
                 for j in range(len(digits)))


def bbp_forcing(n: int) -> Fraction:
    if type(n) is not int or n <= 0:
        raise ValueError('positive index required')
    return (Fraction(4, 8*n-7)-Fraction(2, 8*n-4)
            -Fraction(1, 8*n-3)-Fraction(1, 8*n-2))


def bbp_source_states(N: int) -> tuple[tuple[Fraction, ...], tuple[int, ...]]:
    """Fractional states y_0..y_N and literal integer lifts C_0..C_N."""
    if type(N) is not int or N < 0:
        raise ValueError('N>=0 required')
    phases = [Fraction()]
    carries = [0]
    for n in range(1, N+1):
        step = 16*phases[-1] + bbp_forcing(n)
        carry = step.numerator // step.denominator
        phases.append(step-carry)
        carries.append(16*carries[-1]+carry)
    return tuple(phases), tuple(carries)


def bbp_newton_coefficient(k: int) -> Fraction:
    """A_k=Delta^k U_0, computed from the rational forcing."""
    if type(k) is not int or k < 0:
        raise ValueError('nonnegative order required')
    if k == 0:
        return Fraction()
    a = Fraction()
    differences = [bbp_forcing(i) for i in range(1, k+1)]
    for order in range(1, k+1):
        a = 15*a + differences[0]
        differences = [differences[i+1]-differences[i] for i in range(len(differences)-1)]
    return a


def successor_pascal_source(k: int, q: int) -> Fraction:
    """((H_(q+1)-I)^k U)_0=(q/15)^k Delta^k U_0.

    Its real target is q^k*pi/16; error <=(q/15)^k*pi/16 for 1<=q<15.
    """
    if type(q) is not int or q < 1 or q > 15:
        raise ValueError('integer 1<=q<=15 required')
    return Fraction(q, 15)**k * bbp_newton_coefficient(k)


def centered_phase(x: Fraction) -> Fraction:
    x %= 1
    return x if x < Fraction(1, 2) else x - 1


def binary_source_carry_stat(phases: tuple[Fraction, ...],
                             indices: range, modulus: int = 11) -> dict:
    """Exact finite source marginal/joint counts, never an asymptotic estimate."""
    if type(modulus) is not int or modulus < 2:
        raise ValueError('modulus>=2 required')
    C = 0
    joint = {}
    residue = [0]*modulus
    octants = [0]*16
    for n in range(1, max(indices, default=0)+1):
        x = 16*phases[n-1]+bbp_forcing(n)
        C = 16*C + x.numerator//x.denominator
        if n in indices:
            a = C % modulus
            b = (16*phases[n]).numerator//(16*phases[n]).denominator
            residue[a] += 1
            octants[b] += 1
            joint[(a,b)] = joint.get((a,b),0)+1
    d = len(indices)
    tv = sum((abs(Fraction(c,d)-Fraction(1,modulus)) for c in residue),Fraction())/2 if d else Fraction()
    # Exact distance between empirical joint and product of empirical marginals.
    joint_tv = (sum((abs(Fraction(joint.get((a,b),0),d)-Fraction(residue[a]*octants[b],d*d))
                     for a in range(modulus) for b in range(16)), Fraction())/2 if d else Fraction())
    return {'size':d,'residue':tuple(residue),'sixteen_cells':tuple(octants),
            'residue_tv':tv,'joint_vs_product_tv':joint_tv}
