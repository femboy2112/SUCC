"""Exact research probes for prime charges, Pisot support and source fidelity.

Research-only; not imported by SUCC production code. No zeta-zero coordinates
are inputs. Analytic statements are proved separately in RESEARCH.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import isqrt
from typing import Iterable, Sequence


def positive_int(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("expected a positive integer")
    return n


def factor(n: int) -> dict[int, int]:
    n = positive_int(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n: int) -> bool:
    return n >= 2 and factor(n) == {n: 1}


def require_prime(p: int) -> int:
    positive_int(p)
    if not is_prime(p):
        raise ValueError("primitive channel must be a genuine prime")
    return p


def primes_upto(n: int) -> list[int]:
    positive_int(n)
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(2, n+1) if sieve[p]]


def omega(n: int) -> int:
    return sum(factor(n).values())


def divisor_count(n: int) -> int:
    ans = 1
    for e in factor(n).values():
        ans *= e + 1
    return ans


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        ds = [d*p**k for d in ds for k in range(e+1)]
    return sorted(ds)


def local_profile(n: int, channels: Iterable[int]) -> tuple[int, ...]:
    fs = factor(n)
    return tuple(fs.get(require_prime(p), 0) for p in channels)


def prime_fidelity(n: int, p: int) -> F:
    j = factor(n).get(require_prime(p), 0)
    return F(j+1, j+2)


def charge_successor_jump(n: int, p: int) -> int:
    """Coefficient of [N_p,S]|n> in the |n+1> direction."""
    positive_int(n)
    require_prime(p)
    return factor(n+1).get(p, 0) - factor(n).get(p, 0)


def polya_laplacian(m: int) -> list[list[F]]:
    """PCR-02 leakage matrix, dimension m, including the m=1 vacuum."""
    positive_int(m)
    a = [[F(0) for _ in range(m)] for _ in range(m)]
    for j in range(1, m):
        w = F(j*(m-j), m*(m+1))
        a[j-1][j-1] += w
        a[j][j] += w
        a[j-1][j] -= w
        a[j][j-1] -= w
    return a


def fiber_laplacian(n: int) -> list[list[F]]:
    """Tensor sum of prime-local PCR-02 leakage on the actual divisor fiber."""
    dims = [e+1 for e in factor(n).values()]
    states = list(product(*(range(m) for m in dims)))
    index = {s: i for i, s in enumerate(states)}
    a = [[F(0) for _ in states] for _ in states]
    for slot, m in enumerate(dims):
        local = polya_laplacian(m)
        for st in states:
            i = index[st]
            for k in range(m):
                to = st[:slot] + (k,) + st[slot+1:]
                a[i][index[to]] += local[st[slot]][k]
    return a


def rank(a: Sequence[Sequence[F]]) -> int:
    """Rational Gaussian elimination, independent of the symbolic oracle."""
    b = [[F(x) for x in row] for row in a]
    if not b:
        return 0
    r = 0
    for c in range(len(b[0])):
        pivot = next((j for j in range(r, len(b)) if b[j][c]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        q = b[r][c]
        b[r] = [x/q for x in b[r]]
        for j in range(len(b)):
            if j != r and b[j][c]:
                q = b[j][c]
                b[j] = [x-q*y for x, y in zip(b[j], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def dconv(a: Sequence[F], b: Sequence[F]) -> list[F]:
    if len(a) != len(b):
        raise ValueError("coefficient cutoffs must agree")
    n = len(a)-1
    c = [F(0)]*(n+1)
    for i in range(1, n+1):
        if a[i]:
            for j in range(1, n//i+1):
                c[i*j] += a[i]*b[j]
    return c


def dirichlet_log(a: Sequence[F]) -> list[F]:
    """Formal Dirichlet logarithm: exact for all coefficients within cutoff."""
    if len(a) < 2 or a[1] != 1:
        raise ValueError("constant coefficient must be 1")
    n = len(a)-1
    b = [F(x) for x in a]
    b[1] = F(0)
    power = b[:]
    out = [F(0)]*(n+1)
    for k in range(1, n.bit_length()):
        sign = F((-1)**(k+1), k)
        out = [x+sign*y for x, y in zip(out, power)]
        power = dconv(power, b)
    return out


def mobius(n: int) -> int:
    fs = factor(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)


def extract_primitives(log_coeffs: Sequence[F]) -> list[F]:
    """Coefficients of sum_k mu(k)/k * log Z(ks), not arbitrary prime detection."""
    n = len(log_coeffs)-1
    out = [F(0)]*(n+1)
    for k in range(1, n.bit_length()):
        weight = F(mobius(k), k)
        if weight:
            for m in range(2, n+1):
                v = m**k
                if v > n:
                    break
                out[v] += weight*log_coeffs[m]
    return out


def generator_coeffs(n: int, generators: Sequence[int]) -> list[F]:
    """Counts formal multisets; composite generators intentionally allowed as controls."""
    positive_int(n)
    if len(set(generators)) != len(generators) or any(g < 2 for g in generators):
        raise ValueError("distinct integer generators >= 2 required")
    a = [F(0)]*(n+1)
    a[1] = F(1)
    for g in generators:
        for k in range(1, n//g+1):
            a[g*k] += a[k]
    return a


@dataclass(frozen=True)
class Quad:
    """a+b*beta in Q(beta), beta^2=m*beta+1. Exact, no floating roots."""
    m: int
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self) -> None:
        positive_int(self.m)
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    def _coerce(self, x: Quad | int | F) -> Quad:
        if isinstance(x, Quad):
            if x.m != self.m:
                raise ValueError("no implicit transport between quadratic fields")
            return x
        return Quad(self.m, F(x))

    def __add__(self, x: Quad | int | F) -> Quad:
        x = self._coerce(x)
        return Quad(self.m, self.a+x.a, self.b+x.b)

    __radd__ = __add__

    def __neg__(self) -> Quad:
        return Quad(self.m, -self.a, -self.b)

    def __sub__(self, x: Quad | int | F) -> Quad:
        return self + (-self._coerce(x))

    def __rsub__(self, x: Quad | int | F) -> Quad:
        return self._coerce(x) + (-self)

    def __mul__(self, x: Quad | int | F) -> Quad:
        x = self._coerce(x)
        return Quad(self.m, self.a*x.a+self.b*x.b,
                    self.a*x.b+self.b*x.a+self.m*self.b*x.b)

    __rmul__ = __mul__

    def conjugate(self) -> Quad:
        return Quad(self.m, self.a+self.m*self.b, -self.b)

    def inverse(self) -> Quad:
        norm = self.a*self.a+self.m*self.a*self.b-self.b*self.b
        if norm == 0:
            raise ZeroDivisionError("zero quadratic element")
        q = self.conjugate()
        return Quad(self.m, q.a/norm, q.b/norm)

    def __truediv__(self, x: Quad | int | F) -> Quad:
        return self * self._coerce(x).inverse()

    def __rtruediv__(self, x: Quad | int | F) -> Quad:
        return self._coerce(x) * self.inverse()

    def __pow__(self, k: int) -> Quad:
        if isinstance(k, bool) or not isinstance(k, int):
            raise ValueError("integer exponent required")
        if k < 0:
            return self.inverse()**(-k)
        v, ans = self, Quad(self.m, 1)
        while k:
            if k & 1:
                ans = ans*v
            v, k = v*v, k//2
        return ans

    def trace(self) -> F:
        return 2*self.a+self.m*self.b


def lucas_trace(m: int, k: int) -> int:
    positive_int(m)
    if not isinstance(k, int) or k < 0:
        raise ValueError("nonnegative integer exponent required")
    a, b = 2, m
    for _ in range(k):
        a, b = b, m*b+a
    return a


def half_strip_clock_tail(cutoff: int, abs_s_upper: F) -> F:
    """Analytic bound for omitted log C(s), Re(s)>=1/2, |s|<=abs_s_upper.

    Uses delta_p < p^-2, 1/(1-2^-1/2)<4 and the integral test.
    It bounds the mathematical tail, NOT floating evaluation roundoff.
    """
    positive_int(cutoff)
    if abs_s_upper <= 0:
        raise ValueError("positive modulus bound required")
    return F(8, 3)*abs_s_upper/isqrt(cutoff)**3
