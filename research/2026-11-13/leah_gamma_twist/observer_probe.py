"""Exact, source-labelled affine observer controls for the Leah--Gamma round.

Words are listed in chronological application order.  The symbol x in
LinearX means the fixed source constant pi/16, not a sampled seed.  No
floating point computation or asserted all-shell phase estimate is used.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial, prod
import json


def integer(value, name, minimum=None):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer, not a boolean")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def rational(value, name="value"):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Fraction(value)


def scale16(exponent):
    integer(exponent, "exponent")
    return Fraction(16 ** exponent) if exponent >= 0 else Fraction(1, 16 ** -exponent)


def source(n):
    integer(n, "source index", 1)
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def tail_upper(n):
    """Existing four-pole bound, not an inferred phase cancellation bound."""
    integer(n, "clock", 0)
    return Fraction(47, 225 * (n + 1)**2)


@dataclass(frozen=True)
class LinearX:
    """Exact a*x+b, with the immutable x=pi/16 kept symbolic."""

    a: Fraction
    b: Fraction

    def __post_init__(self):
        object.__setattr__(self, "a", rational(self.a, "x coefficient"))
        object.__setattr__(self, "b", rational(self.b, "constant"))

    def __add__(self, other):
        if not isinstance(other, LinearX):
            other = LinearX(0, rational(other))
        return LinearX(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return LinearX(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, LinearX) else -rational(other))

    def __mul__(self, scalar):
        scalar = rational(scalar, "scalar")
        return LinearX(self.a*scalar, self.b*scalar)

    __rmul__ = __mul__


@dataclass(frozen=True)
class Affine:
    net_scale: int
    offset: Fraction

    @property
    def slope(self):
        return scale16(self.net_scale)

    def apply(self, state):
        if isinstance(state, LinearX):
            return state*self.slope + self.offset
        return self.slope*rational(state, "state") + self.offset


def checked_word(word):
    result = []
    for letter in word:
        if not isinstance(letter, (tuple, list)) or len(letter) != 2:
            raise ValueError("each letter is (positive source index, direction)")
        n, direction = letter
        integer(n, "source index", 1)
        integer(direction, "direction")
        if direction not in (-1, 1):
            raise ValueError("direction must be +1 or -1")
        result.append((n, direction))
    return tuple(result)


def compile_word(word):
    net, offset = 0, Fraction(0)
    for n, direction in checked_word(word):
        if direction == 1:
            offset = 16*offset + source(n)
        else:
            offset = (offset-source(n))/16
        net += direction
    return Affine(net, offset)


def iterate_word(word, state):
    """Independent sequential interpreter; does not call compile_word."""
    value = state if isinstance(state, LinearX) else rational(state, "state")
    for n, direction in checked_word(word):
        value = value*16 + source(n) if direction == 1 else (value-source(n))*Fraction(1, 16)
    return value


def inverse_word(word):
    return tuple((n, -direction) for n, direction in reversed(checked_word(word)))


def state_at(n, seed=0):
    integer(n, "clock", 0)
    value = seed if isinstance(seed, LinearX) else rational(seed, "seed")
    for j in range(1, n+1):
        value = value*16 + source(j)
    return value


def seed_pin(n, state):
    integer(n, "clock", 0)
    return state*scale16(-n) - state_at(n)*scale16(-n)


def symbolic_tail(n):
    """T_n=16^n*x-U_n(0), retained before any completed-phase comparison."""
    integer(n, "clock", 0)
    return LinearX(scale16(n), -state_at(n))


def completed_word(xi, present_clock, word):
    """Same forcing, explicitly WRONG seed s=xi-x, actual tail retained.

    The final absolute clock must be nonnegative.  This never treats a
    fractional frequency of an unlifted circle point as a character.
    """
    xi = rational(xi, "completed initial phase")
    integer(present_clock, "present clock", 0)
    action = compile_word(word)
    final_clock = present_clock + action.net_scale
    if final_clock < 0:
        raise ValueError("the final absolute clock must be nonnegative")
    state = state_at(present_clock, LinearX(-1, xi))
    return (action.apply(state) + symbolic_tail(present_clock)*action.slope
            - action.offset)


def phase(value):
    return rational(value, "phase") % 1


def relative_frequency(h, first_clock, second_clock):
    integer(h, "character")
    integer(first_clock, "first clock", 0)
    integer(second_clock, "second clock", 0)
    return h*(16**first_clock - 16**second_clock)


def neutral_phase(xi, clocks, charges):
    xi = rational(xi, "completed initial phase")
    if len(clocks) != len(charges) or not clocks:
        raise ValueError("nonempty clocks and charges must have equal lengths")
    for clock in clocks:
        integer(clock, "clock", 0)
    for charge in charges:
        integer(charge, "charge")
    if sum(charges) != 0:
        raise ValueError("a relative probe must have total charge zero")
    return phase(xi*sum(a*16**m for a, m in zip(charges, clocks)))


def swap_defect(first, second):
    integer(first, "first source index", 1)
    integer(second, "second source index", 1)
    return 15*(source(first)-source(second))


def finite_difference(n, order):
    integer(n, "source index", 1)
    integer(order, "difference order", 0)
    return sum(((-1)**j * comb(order, j) * source(n+j)
                for j in range(order+1)), Fraction(0))


def moment_difference(n, order):
    """Separate route: expand g(z)*(1-z^8)^order, then integrate monomials."""
    integer(n, "source index", 1)
    integer(order, "difference order", 0)
    polynomial = {}
    for degree, coefficient in ((0, 4), (3, -2), (4, -1), (5, -1)):
        for j in range(order+1):
            power = degree + 8*j
            polynomial[power] = polynomial.get(power, 0) + coefficient*(-1)**j*comb(order, j)
    return sum((Fraction(coefficient, 8*n-7+power)
                for power, coefficient in polynomial.items()), Fraction(0))


def difference_bounds(n, order):
    integer(n, "source index", 1)
    integer(order, "difference order", 0)
    numerator = 15 * 8**order * factorial(order+1)
    lower = Fraction(numerator, prod(8*n-3+7*order+j for j in range(order+2)))
    upper = Fraction(numerator, prod(8*n-7+j for j in range(order+2)))
    return lower, upper


def gamma_limit(order):
    integer(order, "difference order", 0)
    return Fraction(15*factorial(order+1), 64)


def difference_word(n, order):
    integer(n, "source index", 1)
    integer(order, "difference order", 1)
    word = []
    for j in range(order):
        coefficient = (-1)**j*comb(order-1, j)
        edge = ((n+j, 1), (n+j+1, -1))
        if coefficient < 0:
            edge = inverse_word(edge)
        word.extend(edge * abs(coefficient))
    return tuple(word)


def relative_tail_budget(clock, frequency):
    """Rational upper bound for |g(qU_n)-g(qY_n)|, using 2*pi<44/7."""
    integer(frequency, "frequency")
    return Fraction(44, 7)*abs(frequency)*tail_upper(clock)


def build_report():
    grid = []
    for n in (1, 2, 5, 17, 64):
        for order in range(6):
            direct, moment = finite_difference(n, order), moment_difference(n, order)
            lower, upper = difference_bounds(n, order)
            grid.append({"n": n, "order": order, "direct": str(direct),
                         "moment": str(moment), "lower": str(lower), "upper": str(upper),
                         "routes_agree": direct == moment, "bounds_hold": lower <= direct <= upper,
                         "scaled_gamma_limit": str(gamma_limit(order))})
    patterns = (((0, 1), (-1, 1)), ((0, 1, 2), (1, -2, 1)),
                ((0, 1, 2, 3), (1, -1, 2, -2)),
                ((0, 1, 2, 3, 4), (1, 1, 1, 1, -4)))
    torsion = []
    for j in range(15):
        xi = Fraction(j, 15)
        present = 3
        initial_state = state_at(present, LinearX(-1, xi))
        tail = symbolic_tail(present)
        torsion.append({"j": j, "seed": f"{xi} - pi/16 (wrong seed)",
                        "literal_zero_seed_authenticated": False,
                        "present_clock": present,
                        "state_linear_x": [str(initial_state.a), str(initial_state.b)],
                        "tail_linear_x": [str(tail.a), str(tail.b)],
                        "completed_linear_x": [str((initial_state+tail).a), str((initial_state+tail).b)],
                        "neutral_phase_keys": [str(neutral_phase(xi, clocks, charges)) for clocks, charges in patterns],
                        "absolute_phase_key": str(phase(xi)),
                        "R0_gap": "0" if j == 0 else f"1-cos(2*pi*{j}/15)>0"})
    loop = ((2, 1), (5, 1), (2, -1), (5, -1))
    action = compile_word(loop)
    return {"baseline": "db9fb4b84672050efa79b13377f1e73364598a14",
            "status": "exact finite calibration; universal claims require the accompanying proofs",
            "source": {"r": "4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)",
                       "authentic_seed": "0", "x": "pi/16", "base": 16},
            "difference_grid": grid,
            "closed_commutator": {"chronological_word": loop, "net_scale": action.net_scale,
                                  "offset": str(action.offset),
                                  "formula": str(Fraction(15, 256)*(source(2)-source(5)))},
            "same_forcing_wrong_seed_controls": torsion,
            "neutral_patterns": [{"clocks": c, "charges": a} for c, a in patterns],
            "unproved": ["all-shell positive relative energy on the authentic zero-seed path",
                         "R0 for the authentic zero-seed path", "pi normality"],
            "independence": "two exact algebraic implementations; same source and same model, not independent external witnesses"}


if __name__ == "__main__":
    print(json.dumps(build_report(), indent=2, sort_keys=True))
