"""Source-indexed logistic-map observer trees, with exact finite certificates.

The logistic map f(x)=4*x*(1-x) is conjugate to the full tent map
T(theta)=2*theta (theta<=1/2), 2-2*theta (theta>=1/2) through
h(theta)=sin(pi*theta/2)**2.  T and its inverse branches are exact over Q;
the equal-weight logistic inverse transfer operator maps Q[x] -> Q[x].

No claims of empirical source authentication, prediction of individual chaotic
orbits from a stationary law, universal chaos elimination or RH consequences.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb
from itertools import product
from typing import Iterable, Sequence


class ObserverTreeError(ValueError):
    """Malformed or incompatible source, path, parameter or observer report."""


def rational(value: int | F) -> F:
    """Accept exact integers/Fractions; float input is not an exact certificate."""
    if isinstance(value, bool) or not isinstance(value, (int, F)):
        raise ObserverTreeError("Exact integer/Fraction required; float is not a certificate")
    return F(value)


def _bits(bits: Iterable[int]) -> tuple[int, ...]:
    result = tuple(bits)
    if any(type(b) is not int or b not in (0, 1) for b in result):
        raise ObserverTreeError("Each inverse-branch/chronological itinerary bit is 0 or 1")
    return result


def logistic(x: int | F) -> F:
    x = rational(x)
    if not 0 <= x <= 1:
        raise ObserverTreeError("Logistic source state must be in [0,1]")
    return 4 * x * (1 - x)


def tent(theta: int | F) -> F:
    theta = rational(theta)
    if not 0 <= theta <= 1:
        raise ObserverTreeError("Tent source state must be in [0,1]")
    return 2*theta if theta <= F(1,2) else 2*(1-theta)


def inverse_tent_branch(bit: int, y: int | F) -> F:
    if type(bit) is not int or bit not in (0, 1):
        raise ObserverTreeError("Inverse branch must be 0 or 1")
    y = rational(y)
    if not 0 <= y <= 1:
        raise ObserverTreeError("Inverse endpoint must be in [0,1]")
    return y/2 if bit == 0 else 1-y/2


def cylinder(bits: Iterable[int]) -> tuple[F, F]:
    """Full tent itinerary cylinder; endpoints are overlapping measure-zero ties.

    A chronological word s_0 ... s_(n-1) describes the sides of T^i(theta).
    The inverse composition is b_(s0) o ... o b_(sn-1)([0,1]).
    """
    bs = _bits(bits)
    a, b = F(0), F(1)
    for bit in reversed(bs):
        a, b = inverse_tent_branch(bit,a), inverse_tent_branch(bit,b)
    return min(a,b), max(a,b)


def symbolic_path(theta: int | F, depth: int) -> tuple[int, ...]:
    """Actual forward itinerary, excluding ambiguous critical-point ties."""
    x = rational(theta)
    if not 0 <= x <= 1 or type(depth) is not int or depth < 0:
        raise ObserverTreeError("Valid source angle and nonnegative depth required")
    result = []
    for _ in range(depth):
        if x == F(1,2):
            raise ObserverTreeError("Critical boundary itinerary is convention-dependent")
        result.append(int(x > F(1,2)))
        x = tent(x)
    return tuple(result)


def inverse_word(bits: Iterable[int], endpoint: int | F) -> F:
    bs = _bits(bits)
    value = rational(endpoint)
    if not 0 <= value <= 1:
        raise ObserverTreeError("Endpoint must be in [0,1]")
    for bit in reversed(bs):
        value = inverse_tent_branch(bit, value)
    return value


def forward_uncertainty(bits: Iterable[int], steps: int) -> tuple[F, F]:
    """Exact forward image of a whole n-cylinder: all of [0,1] by step n."""
    bs = _bits(bits)
    if type(steps) is not int or steps < 0:
        raise ObserverTreeError("Nonnegative integer time required")
    return cylinder(bs[steps:])


def cylinder_mass(bits: Iterable[int]) -> F:
    return F(1, 2**len(_bits(bits)))


def cylinders_at(depth: int) -> tuple[tuple[tuple[int, ...], tuple[F, F]], ...]:
    if type(depth) is not int or not 0 <= depth <= 14:
        raise ObserverTreeError("Enumeration depth must be 0..14")
    return tuple((bits,cylinder(bits)) for bits in product((0,1),repeat=depth))


@dataclass(frozen=True)
class Source:
    name: str
    version: int

    def __post_init__(self) -> None:
        if not self.name or type(self.version) is not int or self.version < 0:
            raise ObserverTreeError("Original-source identifier and nonnegative version required")


@dataclass(frozen=True)
class PrefixReceipt:
    source: Source
    chronology: tuple[int, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self,"chronology",_bits(self.chronology))


@dataclass(frozen=True)
class TerminalReceipt:
    source: Source
    step: int
    theta: F

    def __post_init__(self) -> None:
        if type(self.step) is not int or self.step < 0:
            raise ObserverTreeError("Endpoint time must be nonnegative")
        x = rational(self.theta)
        if not 0 < x < 1:
            raise ObserverTreeError("Interior endpoint required to avoid critical ties")
        object.__setattr__(self,"theta",x)


def join_observers(prefix: PrefixReceipt, terminal: TerminalReceipt) -> dict:
    """A formally source-typed dual E/E'' join; no claimed physical attestation.

    Prefix bits alone isolate one 2^-n cylinder, while the n-step endpoint
    alone admits 2^n inverse branches. Their join determines theta_0 exactly.
    """
    if prefix.source != terminal.source or len(prefix.chronology) != terminal.step:
        raise ObserverTreeError("Source/version or causal endpoint-time mismatch")
    initial = inverse_word(prefix.chronology,terminal.theta)
    orbit = (initial,)
    for _ in prefix.chronology:
        orbit += (tent(orbit[-1]),)
    if orbit[-1] != terminal.theta:
        raise AssertionError("Causal forward reconstruction failed")
    if symbolic_path(initial,terminal.step) != prefix.chronology:
        raise AssertionError("Source path and endpoint do not glue")
    return {
        "source":prefix.source,
        "depth":terminal.step,
        "theta_initial":initial,
        "orbit":orbit,
        "endpoint":terminal.theta,
        "cylinder":cylinder(prefix.chronology),
        "actual_physical_source_authenticated":False,
    }


def join_interval(prefix: PrefixReceipt, source: Source, step: int,
                  endpoint_low: int | F, endpoint_high: int | F) -> tuple[F,F]:
    """Dual join with bounded endpoint precision; exact uncertainty width.

    This is a complete *interval report*, not a claim that a device attests it.
    """
    a,b = rational(endpoint_low),rational(endpoint_high)
    if prefix.source != source or type(step) is not int or step != len(prefix.chronology):
        raise ObserverTreeError("Source/version or time mismatch")
    if not 0 < a <= b < 1:
        raise ObserverTreeError("Valid interior terminal interval required")
    x,y = inverse_word(prefix.chronology,a),inverse_word(prefix.chronology,b)
    return min(x,y),max(x,y)


# Exact inverse-tree transfer on Q[x]. Ascending-power polynomial coordinates.
def _canonical(values: Sequence[F | int]) -> tuple[F, ...]:
    result = [rational(c) for c in values]
    if not result:
        raise ObserverTreeError("A polynomial needs at least a zero coefficient")
    while len(result)>1 and result[-1]==0:
        result.pop()
    return tuple(result)


def _add(a: tuple[F,...], b: tuple[F,...], scale: F = F(1)) -> tuple[F,...]:
    n=max(len(a),len(b))
    return _canonical([(a[i] if i<len(a) else 0) + scale*(b[i] if i<len(b) else 0)
                       for i in range(n)])


def _multiply(a: tuple[F,...], b: tuple[F,...]) -> tuple[F,...]:
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return _canonical(c)


def transfer_polynomial(coefficients: Sequence[int|F]) -> tuple[F,...]:
    """(Lg)(y)=[g((1-sqrt(1-y))/2)+g((1+sqrt(1-y))/2)]/2.

    Roots u+v=1, u*v=y/4; power sums S_0=2, S_1=1,
    S_k=S_(k-1)-(y/4)*S_(k-2). Every coefficient is an exact Fraction.
    """
    p = _canonical(coefficients)
    powers=[(F(2),)]
    if len(p)>1:
        powers.append((F(1),))
    for k in range(2,len(p)):
        prev=powers[k-1]
        shifted=(F(0),)+tuple(v/4 for v in powers[k-2])
        powers.append(_add(prev,shifted,F(-1)))
    result=(F(0),)
    for coefficient, power in zip(p,powers):
        result=_add(result,power,coefficient/2)
    return result


def transfer_depth(coefficients: Sequence[int|F], depth: int) -> tuple[F,...]:
    if type(depth) is not int or depth < 0:
        raise ObserverTreeError("Nonnegative transfer depth required")
    result=_canonical(coefficients)
    for _ in range(depth):
        result=transfer_polynomial(result)
    return result


def arcsine_moment(power: int) -> F:
    if type(power) is not int or power < 0:
        raise ObserverTreeError("Moment order must be nonnegative")
    return F(comb(2*power,power),4**power)


def equilibrium_mean(coefficients: Sequence[int|F]) -> F:
    p=_canonical(coefficients)
    return sum((coef*arcsine_moment(k) for k,coef in enumerate(p)), F(0))


def exact_completion_depth(coefficients: Sequence[int|F]) -> int:
    """Sufficient universal depth: 2**n exceeds the degree of the polynomial."""
    p=_canonical(coefficients)
    return (len(p)-1).bit_length()


def chebyshev_mode(order: int) -> tuple[F,...]:
    """T_order(1-2*x), for transfer eigen-chain/halving identity."""
    if type(order) is not int or order < 0:
        raise ObserverTreeError("Chebyshev order must be nonnegative")
    if order==0:
        return (F(1),)
    z=(F(1),F(-2))
    if order==1:
        return z
    a,b=(F(1),),z
    for _ in range(2,order+1):
        a,b=b,_add(_multiply((F(2),F(-4)),b),a,F(-1))
    return b


def report_information(depth: int, retained_bits: int) -> dict:
    """Exact combinatorial cost of an n-word quotient retaining k bits.

    NOT a time-equivariant deterministic dynamical factor of f_4.
    """
    if (type(depth) is not int or type(retained_bits) is not int
        or depth < 0 or retained_bits < 0 or retained_bits > depth):
        raise ObserverTreeError("0 <= retained_bits <= depth required")
    return {
       "possible_source_histories":2**depth,
       "distinct_reports":2**retained_bits,
       "maximum_fiber":2**(depth-retained_bits),
       "source_history_entropy_bits":depth,
       "report_entropy_bits":retained_bits,
       "unresolved_history_bits":depth-retained_bits,
       "zero_entropy_dynamical_factor_proved":False,
    }


def zero_lag_one_covariance_receipt() -> dict:
    """Uncorrelated adjacent x values can be exactly functionally dependent."""
    m=[arcsine_moment(k) for k in range(4)]
    ex=m[1]
    ex2=m[2]
    ex_next=4*(m[1]-m[2])
    ex_xnext=4*(m[2]-m[3])
    return {"E_x":ex,"E_x_squared":ex2,"E_x_cubed":m[3],
            "E_next":ex_next,"E_x_times_next":ex_xnext,
            "covariance":ex_xnext-ex*ex_next,
            "deterministic_relation":"x_next=4*x*(1-x)",
            "statistical_independence_inferred":False}


def lipschitz_uniform_bound_pi_coefficient(depth: int, source_lipschitz: int | F) -> F:
    """Exact coefficient C in sup_y |L^n g(y)-mu(g)| <= C*pi.

    Requires a certified Lipschitz constant L for g on [0,1]. The proof
    transports g through h(theta) (Lipschitz pi*L/2) and couples each
    depth-n inverse branch to a uniform point in its 2^-n tent cylinder.
    This supplies a theorem-bound, not a floating-point interval certificate.
    """
    if type(depth) is not int or depth < 0:
        raise ObserverTreeError("Nonnegative depth required")
    L = rational(source_lipschitz)
    if L < 0:
        raise ObserverTreeError("Lipschitz constant must be nonnegative")
    return L / (2**(depth+2))


def period_two_bifurcation_receipt(r: int | F) -> dict:
    """Exact algebraic 2-cycle for rational logistic 3 < r <= 4.

    x_+/-=(r+1 +/- sqrt((r-3)(r+1)))/(2*r).  The two elements
    swap, verified through Q[s]/(s^2-a). This does not establish the
    full parameter-space bifurcation diagram or natural measure.
    """
    rate=rational(r)
    if not 3 < rate <= 4:
        raise ObserverTreeError("Nondegenerate real 2-cycle requires 3<r<=4")
    center=(rate+1)/(2*rate)
    radius_square=((rate-3)*(rate+1))/(4*rate**2)
    mapped_center=rate*(center-center**2-radius_square)
    mapped_slope=rate*(1-2*center)
    multiplier=-rate**2+2*rate+4
    if mapped_center != center or mapped_slope != -1:
        raise AssertionError("Two-cycle radical relation failed")
    return {
        "rate":rate,"center":center,"radius_square":radius_square,
        "coefficient_of_sqrt_in_forward_swap":mapped_slope,
        "period_two_derivative_multiplier":multiplier,
        "period_two_attracting":abs(multiplier)<1,
        "validates_all_parameter_windows":False,
    }


def forward_pullback_polynomial(coefficients: Sequence[int|F], steps: int) -> tuple[F,...]:
    """Koopman pullback U^n(g)=g(f_4^n(x)) on exact polynomials.

    Unlike fixed-degree observables, this target changes at every forward SUCC.
    The exact identity L^n U^n g = g leaves a nonconstant residual.
    """
    if type(steps) is not int or steps < 0:
        raise ObserverTreeError("Nonnegative moving-target steps required")
    result=_canonical(coefficients)
    f=(F(0),F(4),F(-4))
    for _ in range(steps):
        next_result=(F(0),)
        for c in reversed(result):
            next_result=_add(_multiply(next_result,f),(c,))
        result=next_result
    return result
