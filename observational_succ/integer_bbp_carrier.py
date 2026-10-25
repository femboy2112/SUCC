"""Integer-native BBP model, lossless odd-conductor transport, exact readouts.

No pi digits or floating-point values enter the source. The state engine and
phase/carry/collision decoders use integers only. Fraction is restricted to
source-tail certificates, not the carrier state. Statistical normality is OPEN.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, lcm


def _nat(x: int, lo: int = 0) -> int:
    if type(x) is not int or x < lo:
        raise ValueError(f"integer >= {lo} required")
    return x


def forcing_pair(n: int) -> tuple[int, int]:
    """Reduced a/b for the authentic four-pole forcing; b is always odd."""
    _nat(n, 1)
    a = 120*n*n - 89*n + 16
    b = (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    d = gcd(a, b)
    return a//d, b//d


@dataclass(frozen=True)
class IntegerState:
    n: int = 0
    conductor: int = 1
    numerator: int = 0

    def __post_init__(self) -> None:
        _nat(self.n); _nat(self.conductor, 1); _nat(self.numerator)
        if self.conductor % 2 == 0:
            raise ValueError("odd-conductor source required")

    @property
    def remainder(self) -> int:
        return self.numerator % self.conductor

    @property
    def integer_part(self) -> int:
        return self.numerator // self.conductor


def step(state: IntegerState) -> tuple[IntegerState, int]:
    """One integer macrostep and its LITERAL forced carry, not a pi digit."""
    n = state.n + 1
    a, b = forcing_pair(n)
    q = lcm(state.conductor, b)
    g, c = q//state.conductor, (q//b)*a
    total = 16*g*state.numerator + c
    literal = (16*g*state.remainder + c)//q
    return IntegerState(n, q, total), literal


def source_states(horizon: int) -> tuple[IntegerState, ...]:
    _nat(horizon)
    states = [IntegerState()]
    for _ in range(horizon):
        states.append(step(states[-1])[0])
    return tuple(states)


@lru_cache(maxsize=None)
def conductor_at(n: int) -> int:
    _nat(n)
    q = 1
    for j in range(1, n+1):
        q = lcm(q, forcing_pair(j)[1])
    return q


def pair(a: int, b: int) -> int:
    _nat(a); _nat(b)
    return (a+b)*(a+b+1)//2 + b


def unpair(code: int) -> tuple[int, int]:
    _nat(code)
    w = (isqrt(8*code+1)-1)//2
    b = code - w*(w+1)//2
    return w-b, b


def coded_step(code: int) -> int:
    """TOTAL INJECTIVE primitive-recursive internal map N -> N.

    code=pair(n,A), with canonical Q_n recomputed from integer source time.
    This is NOT ordinary code+1. n+1 is the external logical clock; running
    the internal arithmetic is not free or a constant-cost physical step.
    """
    n, a = unpair(code)
    out, _ = step(IntegerState(n, conductor_at(n), a))
    return pair(out.n, out.numerator)


def coded_predecessor(code: int) -> int:
    """Exact partial inverse; reject natural numbers outside the program image."""
    n, a = unpair(code)
    if n == 0:
        raise ValueError("no predecessor at the initial time level")
    q0, q = conductor_at(n-1), conductor_at(n)
    rn, rd = forcing_pair(n)
    residual = a - (q//rd)*rn
    multiplier = 16*(q//q0)
    if residual < 0 or residual % multiplier:
        raise ValueError("code is not in the source program image")
    return pair(n-1, residual//multiplier)


def source_level_inverse(n: int, remainder: int) -> int:
    """Recover previous phase on authenticated Q_(n-1) from Q_n output.

    The output must lie in the source-compatible residue coset c_n mod g_n.
    It is not an inverse for the full real-circle covering or arbitrary time.
    """
    _nat(n, 1); _nat(remainder)
    q0, q = conductor_at(n-1), conductor_at(n)
    if remainder >= q:
        raise ValueError("next remainder outside its finite source clock")
    a, b = forcing_pair(n)
    c, g = (q//b)*a, q//q0
    if (remainder-c) % g:
        raise ValueError("remainder is outside the source-compatible image")
    return (((remainder-c)//g)*pow(16, -1, q0)) % q0


def carry_residue16(n: int, next_remainder: int) -> int:
    """Literal carry MODULO16; value16 cannot be distinguished from 0 here."""
    _nat(n, 1); _nat(next_remainder)
    q = conductor_at(n)
    if next_remainder >= q:
        raise ValueError("remainder outside authenticated clock")
    a, b = forcing_pair(n)
    c = (q//b)*a
    return ((c-next_remainder)*pow(q, -1, 16)) % 16


def common_clock(states: tuple[IntegerState, ...]) -> tuple[int, tuple[int, ...]]:
    """One integer modulus retaining ALL phase differences in a finite history."""
    if not states:
        raise ValueError("nonempty observed history required")
    q = lcm(*(s.conductor for s in states))
    return q, tuple((q//s.conductor)*s.remainder for s in states)


def integer_collision_count(states: tuple[IntegerState, ...], mesh: int) -> int:
    """Full ordered near-pair count, diagonals/wrap/endpoints included."""
    _nat(mesh, 3)
    q, addresses = common_clock(states)
    return sum(mesh*min(abs(a-b), q-abs(a-b)) <= q
               for a in addresses for b in addresses)


def tail_bounds(n: int, depth: int) -> tuple[Fraction, Fraction]:
    """Strict rational bounds from authentic source, no supplied pi digits."""
    _nat(n); _nat(depth, 1)
    lo = sum((Fraction(*forcing_pair(n+k))/16**k
              for k in range(1, depth+1)), Fraction())
    # r is positive decreasing; residual < r(n+K+1)/(15*16^K).
    return lo, lo + Fraction(*forcing_pair(n+depth+1))/(15*16**depth)


def hexadecimal_digit(state: IntegerState, max_depth: int = 48) -> tuple[int, int]:
    """Digit after x={16^(n-1)*pi}, n>=1, for the AUTHENTIC state only.

    Returned certificate is (digit, depth). At each finite depth this fails
    closed unless the full outward rational interval has one integer part.
    Irrationality of pi proves eventual termination on the authentic state;
    no uniform depth bound or distribution estimate is implied.
    """
    _nat(state.n, 1); _nat(max_depth, 1)
    if state != source_states(state.n)[-1]:
        raise ValueError("digit readout requires the full zero-initial authenticated source")
    phase = Fraction(state.remainder, state.conductor)
    for depth in range(1, max_depth+1):
        lo, hi = tail_bounds(state.n, depth)
        a, b = 16*(phase+lo), 16*(phase+hi)
        lower, upper = a.numerator//a.denominator, b.numerator//b.denominator
        if lower == upper:
            return lower % 16, depth
    raise ArithmeticError("source precision budget does not certify this digit")


def circle_inverse_discontinuity(k: int) -> tuple[int, int]:
    """16^-1(1/(16k-1))=k/(16k-1)->1/16, not 0."""
    _nat(k, 1)
    q = 16*k-1
    assert pow(16, -1, q) == k
    return k, q


def odd_rational_counterfeit_tail(n: int) -> Fraction:
    """A different positive odd source whose corrected orbit is fixed at 1/3."""
    _nat(n)
    return Fraction(1, (2*n+1)*(2*n+3))


def odd_rational_counterfeit_forcing(n: int) -> Fraction:
    _nat(n, 1)
    return 16*odd_rational_counterfeit_tail(n-1)-odd_rational_counterfeit_tail(n)


def finite_residue_decoder_lower_bound(modulus: int) -> Fraction:
    """Any time-mod-q -> circle decoder has this finite four-time error floor.

    Use actual source times 0,1,q,q+1. With q>=2 the bound exceeds 1/510.
    Letting the last two times be k*q,k*q+1 gives asymptotic lower 1/255
    for worst-case error over ALL n, independently of q. This does not
    obstruct exact discrete-time algorithms or source-adaptive encodings.
    """
    _nat(modulus, 2)
    return (Fraction(2,15)-Fraction(*forcing_pair(modulus+1)))/34
