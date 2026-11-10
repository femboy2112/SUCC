"""Outward integer rectangles; finite certificates, never asymptotic claims.

All endpoints have denominator SCALE. Range reduction uses exact rational
turns; Taylor evaluation is outward at every operation. No float enters.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from observational_succ.pi_succ_character_intervals import machin_pi_interval

BITS = 80
SCALE = 1 << BITS


def ceildiv(a, b):
    return -((-a) // b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int or self.lo > self.hi:
            raise ValueError("ordered integer endpoints required")

    @classmethod
    def ratio(cls, numerator, denominator=1):
        if type(numerator) is not int or type(denominator) is not int or denominator <= 0:
            raise ValueError("integer ratio with positive denominator required")
        return cls(numerator*SCALE//denominator, ceildiv(numerator*SCALE, denominator))

    def __add__(self, other):
        return Interval(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        corners = (self.lo*other.lo, self.lo*other.hi,
                   self.hi*other.lo, self.hi*other.hi)
        return Interval(min(corners)//SCALE, ceildiv(max(corners), SCALE))

    def divide(self, positive_integer):
        if type(positive_integer) is not int or positive_integer <= 0:
            raise ValueError("positive integer divisor required")
        return Interval(self.lo//positive_integer, ceildiv(self.hi, positive_integer))

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo, self.hi*self.hi)
        high = max(self.lo*self.lo, self.hi*self.hi)
        return Interval(low//SCALE, ceildiv(high, SCALE))

    def overlaps(self, other):
        return max(self.lo, other.lo) <= min(self.hi, other.hi)

    def as_list(self):
        return [self.lo, self.hi]


ZERO = Interval(0, 0)
ONE = Interval(SCALE, SCALE)


@dataclass(frozen=True)
class Box:
    re: Interval = ZERO
    im: Interval = ZERO

    def __add__(self, other):
        return Box(self.re+other.re, self.im+other.im)

    def __neg__(self):
        return Box(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Box(self.re*other.re-self.im*other.im,
                   self.re*other.im+self.im*other.re)

    def conjugate(self):
        return Box(self.re, -self.im)

    def divide(self, n):
        return Box(self.re.divide(n), self.im.divide(n))

    def norm_squared(self):
        return self.re.square()+self.im.square()

    def as_dict(self):
        return {"re": self.re.as_list(), "im": self.im.as_list(),
                "abs_squared": self.norm_squared().as_list()}


@lru_cache(None)
def pi_box():
    lo, hi = machin_pi_interval(20)
    return Interval(lo.numerator*SCALE//lo.denominator,
                    ceildiv(hi.numerator*SCALE, hi.denominator))


def phase(numerator, denominator=1):
    """Enclose e(numerator/denominator), using exact quadrant transport."""
    if type(numerator) is not int or type(denominator) is not int or denominator <= 0:
        raise ValueError("exact integer phase pair required")
    n = numerator % denominator
    quadrant = (8*n+denominator)//(2*denominator)
    # t = n/d - quadrant/4 belongs to [-1/8,1/8].
    x = Interval.ratio(4*n-quadrant*denominator, 2*denominator)*pi_box()
    assert -SCALE < x.lo <= x.hi < SCALE
    minus_x2 = -(x*x)
    c = Interval.ratio((-1)**13, factorial(26))
    s = Interval.ratio((-1)**13, factorial(27))
    # Horner with x², coefficients already have their alternating signs.
    x2 = -minus_x2
    for j in range(12, -1, -1):
        c = c*x2+Interval.ratio((-1)**j, factorial(2*j))
        s = s*x2+Interval.ratio((-1)**j, factorial(2*j+1))
    s = s*x
    # cos polynomial is also Taylor degree27; sin is Taylor degree28.
    ec, es = ceildiv(SCALE, factorial(28)), ceildiv(SCALE, factorial(29))
    c = c+Interval(-ec, ec)
    s = s+Interval(-es, es)
    rotation = quadrant % 4
    return (Box(c, s), Box(-s, c), Box(-c, -s), Box(s, -c))[rotation]


def mean(boxes):
    values = list(boxes)
    if not values:
        raise ValueError("nonempty sequence required")
    total = Box()
    for value in values:
        total = total+value
    return total.divide(len(values))


def contains_rational(interval, value):
    value = Q(value)
    return interval.lo*value.denominator <= value.numerator*SCALE <= interval.hi*value.denominator
