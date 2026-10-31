"""Exact, typed finite carriers; no probabilistic law is assigned to BBP."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import factorial


@dataclass(frozen=True)
class Slot:
    label: str
    colour: str


@dataclass(frozen=True)
class Object:
    slots: tuple[Slot, ...] = ()

    def __post_init__(self):
        if len({s.label for s in self.slots}) != len(self.slots):
            raise ValueError("labels must be distinct")

    @property
    def rank(self):
        return len(self.slots)


@dataclass(frozen=True)
class Path:
    source: Object
    added: tuple[Slot, ...]
    bits: tuple[int, ...]

    def __post_init__(self):
        if len(self.added) != len(self.bits) or any(b not in (0, 1) for b in self.bits):
            raise ValueError("one binary choice is required per slot")
        Object(self.source.slots + self.added)

    @property
    def target(self):
        return Object(self.source.slots + self.added)

    @property
    def grade(self):
        return sum(self.bits)

    def then(self, other: Path):
        if self.target != other.source:
            raise ValueError("middle carrier objects do not match")
        return Path(self.source, self.added + other.added, self.bits + other.bits)

    def split(self, position: int):
        if not 0 <= position <= len(self.bits):
            raise ValueError("split outside path")
        left = Path(self.source, self.added[:position], self.bits[:position])
        right = Path(left.target, self.added[position:], self.bits[position:])
        return left, right

    @staticmethod
    def identity(obj: Object):
        return Path(obj, (), ())


@dataclass(frozen=True)
class SignedRank:
    """A representative (positive, negative); equivalent is the quotient relation."""
    positive: int
    negative: int

    def __post_init__(self):
        if self.positive < 0 or self.negative < 0:
            raise ValueError("representative counts must be nonnegative")

    @property
    def value(self):
        return self.positive - self.negative

    def equivalent(self, other):
        return self.positive + other.negative == other.positive + self.negative

    def __add__(self, other):
        return SignedRank(self.positive + other.positive, self.negative + other.negative)

    def __neg__(self):
        return SignedRank(self.negative, self.positive)

    def __mul__(self, other):
        return SignedRank(self.positive*other.positive + self.negative*other.negative,
                          self.positive*other.negative + self.negative*other.positive)


def binomial(x: int | Q, k: int) -> Q:
    if k < 0:
        return Q(0)
    result = Q(1)
    for j in range(k):
        result *= Q(x-j, j+1)
    return result


def polarized_product(a: int, b: int) -> Q:
    return binomial(a+b, 2)-binomial(a, 2)-binomial(b, 2)


@dataclass(frozen=True)
class Matrix:
    a: Q
    b: Q
    c: Q
    d: Q

    def __post_init__(self):
        for name in ("a", "b", "c", "d"):
            object.__setattr__(self, name, Q(getattr(self, name)))

    def __add__(self, other):
        return Matrix(*(x+y for x, y in zip(self.entries(), other.entries())))

    def __neg__(self):
        return Matrix(*(-x for x in self.entries()))

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return Matrix(*(x*other for x in self.entries()))
        return Matrix(self.a*other.a+self.b*other.c, self.a*other.b+self.b*other.d,
                      self.c*other.a+self.d*other.c, self.c*other.b+self.d*other.d)

    def apply(self, v):
        return (self.a*v[0]+self.b*v[1], self.c*v[0]+self.d*v[1])

    def entries(self):
        return (self.a, self.b, self.c, self.d)

    def norm(self):
        return max(abs(self.a)+abs(self.b), abs(self.c)+abs(self.d))


ZERO = Matrix(0, 0, 0, 0)
ONE = Matrix(1, 0, 0, 1)


def matrix_sum(items):
    result = ZERO
    for item in items:
        result = result+item
    return result


def power_coeff_to_newton(coeff):
    """J(sum a_k*x^k) = sum k!*a_k*binomial(x,k), ordered coefficients."""
    return tuple(a*factorial(k) for k, a in enumerate(coeff))


def newton_eval(coeff, x):
    return matrix_sum(a*binomial(x, k) for k, a in enumerate(coeff))


def newton_product(left, right, transported=False):
    """Ordinary product or transported star product, in the Newton basis."""
    result = [ZERO]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            for overlap in range(1 if transported else min(i, j)+1):
                k = i+j-overlap
                multiplicity = factorial(k)//(factorial(overlap)*factorial(i-overlap)*factorial(j-overlap))
                result[k] = result[k]+(a*b)*multiplicity
    return tuple(result)


def transport(bits, edge, start=(0, 0)):
    """Chronological linear maps act on column vectors on the left."""
    n, k = start
    result = ONE
    for bit in bits:
        result = edge(n, k, bit)*result
        n, k = n+1, k+bit
    return result


def diamond(edge, n, k):
    """Weight(01)-Weight(10)."""
    return edge(n+1, k, 1)*edge(n, k, 0)-edge(n+1, k+1, 0)*edge(n, k, 1)


def swap_telescope(bits, edge, start=(0, 0)):
    """Sort 10 -> 01; return exact transported defects old minus new."""
    word = list(bits)
    defects = []
    while True:
        hit = next((i for i in range(len(word)-1) if word[i:i+2] == [1, 0]), None)
        if hit is None:
            break
        i = hit
        n, k = start[0]+i, start[1]+sum(word[:i])
        prefix = transport(word[:i], edge, start)
        suffix = transport(word[i+2:], edge, (n+2, k+1))
        defects.append(suffix*(-diamond(edge, n, k))*prefix)
        word[i:i+2] = [0, 1]
    return tuple(word), tuple(defects)


def endpoint_states(edge, n, initial=(Q(1), Q(0))):
    result = {}
    for bits in product((0, 1), repeat=n):
        result.setdefault(sum(bits), set()).add(transport(bits, edge).apply(initial))
    return result


def bbp_source(n: int) -> Q:
    if n < 1:
        raise ValueError("native source begins at n=1")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def affine_matrix(radix, source):
    return Matrix(radix, source, 0, 1)


def source_order_lift(order, seed=Q(0), radix=16):
    u = Q(seed)
    for n in order:
        u = radix*u+bbp_source(n)
    return u
