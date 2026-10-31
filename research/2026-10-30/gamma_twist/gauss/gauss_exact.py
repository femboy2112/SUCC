"""Exact order-eight Gauss sums and explicitly normalized GK unit probes.

Standard library only. Q(zeta_8,zeta_p) basis is zeta_8^i zeta_p^j,
0<=i<4, 0<=j<p-1. Finite fields use a declared quadratic nonsquare.
No floating-point number participates in an algebraic certificate.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from math import gcd

OFFSETS = (1, 4, 5, 6)
AUTH = (4, -2, -1, -1)
MUTATION = (1, -3, 1, 1)


def prime_divisors(n):
    out, d = [], 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


class Field:
    def __init__(self, p):
        if p < 3 or prime_divisors(p) != [p]:
            raise ValueError("odd prime required")
        self.p = p
        self.f = 1 if p % 8 == 1 else 2
        self.q = p**self.f
        self.d = 0 if self.f == 1 else next(
            x for x in range(2, p) if pow(x, (p-1)//2, p) == p-1)
        factors = prime_divisors(self.q-1)
        self.generator = next(
            self.decode(i) for i in range(2, self.q)
            if all(self.power(self.decode(i), (self.q-1)//ell) != (1, 0)
                   for ell in factors))
        self.powers, self.logs = [], {}
        x = (1, 0)
        for j in range(self.q-1):
            self.powers.append(x)
            self.logs[x] = j
            x = self.mul(x, self.generator)
        assert x == (1, 0) and len(self.logs) == self.q-1

    def decode(self, i):
        return i % self.p, i // self.p

    def mul(self, x, y, modulus=None):
        m = self.p if modulus is None else modulus
        a, b = x
        c, d = y
        return (a*c+self.d*b*d) % m, (a*d+b*c) % m

    def power(self, x, n, modulus=None):
        if n < 0:
            raise ValueError("nonnegative exponent required")
        z = (1, 0)
        while n:
            if n & 1:
                z = self.mul(z, x, modulus)
            x = self.mul(x, x, modulus)
            n >>= 1
        return z

    def trace(self, x):
        return (self.f*x[0]) % self.p


@dataclass(frozen=True)
class Cyclo:
    p: int
    coeff: tuple
    denominator: int = 1

    @staticmethod
    def make(p, coeff, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        coeff = tuple(coeff)
        assert len(coeff) == 4*(p-1)
        if denominator < 0:
            denominator = -denominator
            coeff = tuple(-x for x in coeff)
        common = reduce(gcd, coeff, denominator)
        return Cyclo(p, tuple(x//common for x in coeff), denominator//common)

    @staticmethod
    def monomial(p, i=0, j=0, scalar=1):
        a = [0]*(4*(p-1))
        i %= 8
        if i >= 4:
            scalar, i = -scalar, i-4
        j %= p
        if j == p-1:
            for t in range(p-1):
                a[i*(p-1)+t] -= scalar
        else:
            a[i*(p-1)+j] += scalar
        return Cyclo.make(p, a)

    def scale(self, numerator, denominator=1):
        return Cyclo.make(self.p, (numerator*x for x in self.coeff),
                          self.denominator*denominator)

    def __add__(self, other):
        assert self.p == other.p
        return Cyclo.make(self.p,
            (a*other.denominator+b*self.denominator
             for a, b in zip(self.coeff, other.coeff)),
            self.denominator*other.denominator)

    def __sub__(self, other):
        return self+other.scale(-1)

    def __mul__(self, other):
        assert self.p == other.p
        p, size = self.p, self.p-1
        raw = [0]*(4*p)
        aa = [(i//size, i % size, a) for i, a in enumerate(self.coeff) if a]
        bb = [(i//size, i % size, a) for i, a in enumerate(other.coeff) if a]
        for i, j, a in aa:
            for k, ell, b in bb:
                row = i+k
                sign = 1 if row < 4 else -1
                raw[(row % 4)*p+(j+ell) % p] += sign*a*b
        result = []
        for i in range(4):
            top = raw[i*p+p-1]
            result.extend(raw[i*p+j]-top for j in range(size))
        return Cyclo.make(p, result, self.denominator*other.denominator)

    def power(self, exponent):
        if exponent < 0:
            raise ValueError("negative Cyclo powers require declared inverse")
        out, x = Cyclo.monomial(self.p), self
        while exponent:
            if exponent & 1:
                out = out*x
            x = x*x
            exponent >>= 1
        return out

    def conjugate(self):
        out = Cyclo.monomial(self.p, scalar=0)
        for index, a in enumerate(self.coeff):
            if a:
                i, j = divmod(index, self.p-1)
                out = out+Cyclo.monomial(self.p, -i, -j, a)
        return out.scale(1, self.denominator)

    def zeta8_coefficients(self):
        size = self.p-1
        assert all(a == 0 for i, a in enumerate(self.coeff) if i % size != 0)
        return tuple(self.coeff[i*size] for i in range(4)), self.denominator

    def record(self):
        return {"basis":"zeta8^i*zeta_p^j; 0<=i<4,0<=j<p-1",
                "numerators":list(self.coeff), "denominator":self.denominator}


class GaussSystem:
    def __init__(self, p):
        self.field = Field(p)
        self.p = p
        self.sums = {}
        for delta in range(1, 8):
            raw = [0]*(4*p)
            for j, x in enumerate(self.field.powers):
                i = (-delta*j) % 8
                raw[(i % 4)*p+self.field.trace(x)] += 1 if i < 4 else -1
            self.sums[delta] = Cyclo.make(p,
                [raw[i*p+j]-raw[i*p+p-1] for i in range(4) for j in range(p-1)])

    def character(self, value, power=1):
        return Cyclo.monomial(self.p, -power*self.field.logs[(value % self.p, 0)])

    def weighted(self, coefficients=AUTH):
        out = Cyclo.monomial(self.p)
        for delta, coefficient in zip(OFFSETS, coefficients):
            if coefficient >= 0:
                out = out*self.sums[delta].power(coefficient)
            else:
                sign = (-1)**(delta*((self.field.q-1)//8))
                inverse = self.sums[8-delta].scale(sign, self.field.q)
                out = out*inverse.power(-coefficient)
        return out


def gk_exponent(p, coefficients=AUTH):
    f = 1 if p % 8 == 1 else 2
    valuation = sum((Fraction((delta*p**i) % 8, 8)*c
        for i in range(f) for delta, c in zip(OFFSETS, coefficients)), Fraction())
    exponent = (p-1)*valuation
    assert exponent.denominator == 1
    return int(exponent), valuation


def gamma_mod(p, precision, argument):
    """Morita Gamma at rational p-integral argument, exactly modulo p^precision."""
    modulus = p**precision
    argument = Fraction(argument)
    n = argument.numerator*pow(argument.denominator, -1, modulus) % modulus
    if n == 0:
        n = modulus
    out = -1 if n % 2 else 1
    for j in range(1, n):
        if j % p:
            out = out*j % modulus
    return out % modulus


def gk_unit_mod(p, precision, coefficients=AUTH):
    modulus = p**precision
    out = -1 if sum(coefficients) % 2 else 1
    f = 1 if p % 8 == 1 else 2
    for i in range(f):
        for delta, coefficient in zip(OFFSETS, coefficients):
            out = out*pow(gamma_mod(p, precision, Fraction(delta*p**i % 8, 8)),
                          coefficient, modulus) % modulus
    return out


def verify_gk_unit_power(system, precision=3):
    """Exact full-unit power verification in an unramified local embedding.

    This independently checks U^m, not the choice among m roots of unity.
    The root choice for U is exactly the published GK normalization.
    """
    field, p = system.field, system.p
    m = 8 if field.f == 1 else 8//gcd(8, p+1)
    exponent, valuation = gk_exponent(p)
    mv = m*valuation
    assert mv.denominator == 1 and mv <= 0
    normalized = system.weighted().power(m).scale((-p)**(-int(mv)))
    coeff, denominator = normalized.zeta8_coefficients()
    D, leftover = 0, denominator
    while leftover % p == 0:
        leftover //= p
        D += 1
    assert leftover == 1
    modulus = p**(precision+D)
    residue = field.power(field.generator, (field.q-1)//8)
    lift = field.power(residue, field.q**(precision+D), modulus)
    assert field.power(lift, 8, modulus) == (1, 0)
    numerator = (0, 0)
    for i, a in enumerate(coeff):
        term = field.power(lift, i, modulus)
        numerator = ((numerator[0]+a*term[0]) % modulus,
                     (numerator[1]+a*term[1]) % modulus)
    assert numerator[0] % denominator == numerator[1] % denominator == 0
    evaluated = tuple(x//denominator for x in numerator)
    unit = gk_unit_mod(p, precision)
    assert evaluated == (pow(unit, m, p**precision), 0)
    return {"precision":precision,"unit_mod_p_power":unit,
        "unit_power_exponent":m,"independent_cyclotomic_power_value":list(evaluated),
        "gk_uniformizer_exponent":exponent,"valuation":str(valuation),
        "teichmuller_zeta8_residue":list(residue),
        "normalization":"pi_p^(p-1)=-p; pi_p congruent zeta_p-1 mod (zeta_p-1)^2",
        "boundary":"power check is independent; root choice uses classical GK"}


def source(n, coefficients=AUTH):
    return sum((Fraction(c, 8*n-8+d) for c, d in zip(coefficients, OFFSETS)), Fraction())


def orbit(n, coefficients=AUTH):
    out = Fraction()
    for j in range(1, n+1):
        out = 16*out+source(j, coefficients)
    return out


def cofiber(value, p):
    P, D = 1, value.denominator
    while D % p == 0:
        P *= p
        D //= p
    a = value.numerator*pow(D, -1, P) % P if P > 1 else 0
    v = value-Fraction(a, P)
    v -= v.numerator//v.denominator
    assert v.denominator % p
    return a, P, v


def valuation(value, p):
    if value == 0:
        return None
    n, d, v = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v
