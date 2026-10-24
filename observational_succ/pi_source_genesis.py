"""Exact finite instruments for the pi source-genesis paper theorems.

No decimal digits of pi are inputs. BBP supplies the selected orbit;
independent Machin arctangents supply certified angles. Bounds on transport
errors are not bounds on cancellation. Infinite claims live in the dossiers.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial

from .bbp_source_memory import forcing, tail_interval


def _nat(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"expected integer >= {minimum}")
    return value


def _integer(value):
    if type(value) is not int:
        raise ValueError("expected integer")
    return value


def _exact(value):
    if type(value) not in (int, Q):
        raise ValueError("expected exact integer or Fraction")
    return Q(value)


@lru_cache(None)
def endpoint_coefficients(order):
    """a_k=h^(k)(1)/k!: h(1+s)=1/(1-2s-2s^3-s^4)."""
    _nat(order)
    out = []
    for k in range(order + 1):
        out.append(1 if k == 0 else sum(
            c*out[k-j] for j, c in ((1, 2), (3, 2), (4, 1)) if j <= k))
    return tuple(out)


def beta_integer(a, b):
    """Integral t^(a-1)(1-t)^(b-1) dt on [0,1], integer a,b>=1."""
    _nat(a, 1); _nat(b, 1)
    product = 1
    for j in range(b):
        product *= a+j
    return Q(factorial(b-1), product)


def tail_beta_interval(n, order):
    """Signed Taylor remainder: T_n lies between P_order and P_(order+1).

    P_K=sum_(k<K)(-1)^k a_k B(8n+1,k+2). Valid for EVERY finite
    order K>=0. This does not assert convergence as K tends to infinity.
    """
    _nat(n); _nat(order)
    a = endpoint_coefficients(order)
    p = sum(((-1)**k*a[k]*beta_integer(8*n+1, k+2)
             for k in range(order)), Q())
    next_p = p + (-1)**order*a[order]*beta_integer(8*n+1, order+2)
    return min(p, next_p), max(p, next_p)


def forced_states(length, initial=Q(0)):
    """BBP circle recurrence, including y_0 and all states through y_length."""
    _nat(length)
    states = [_exact(initial) % 1]
    for n in range(1, length+1):
        states.append((16*states[-1]+forcing(n)) % 1)
    return tuple(states)


def lag_tail_mass_interval(start, length, lag, terms=12):
    """Enclose sum_(j<length)(T_(start+j)-T_(start+j+lag)).

    start>=1. Telescoping leaves min(length,lag) pairs at the boundaries;
    no exponentially large lag frequency multiplies this error.
    """
    _nat(start, 1); _nat(length); _nat(lag); _nat(terms, 1)
    overlap = min(length, lag)
    shift = max(length, lag)
    low = high = Q()
    for j in range(overlap):
        a, b = tail_interval(start+j, terms)
        c, d = tail_interval(start+shift+j, terms)
        low += a-d
        high += b-c
    return max(Q(), low), high


def lag_transport_budget(h, start, length, lag):
    """Rational all-horizon bound on |C-D|, using 2pi<8 and beta tails.

    sum_(n>=s)T_n < sum 1/((8n+1)(8n+2)) < 1/(8(8s-6)).
    A sharper telescoping beta bound gives 2|h|/(16*start-5).
    Four finite Green enclosures additionally certify sum_(n>=1)T_n<1/60.
    """
    _integer(h); _nat(start, 1); _nat(length); _nat(lag)
    if lag == 0 or length == 0 or h == 0:
        return Q()
    boundary = sum((Q(1, (8*n+1)*(8*n+2))
                    for n in range(start, start+min(length, lag))), Q())
    return min(Q(2*length), 8*abs(h)*boundary,
               Q(2*abs(h), 16*start-5), Q(2*abs(h), 15))


def corrected_lag_transport_budget(h, start, order):
    """All-length/all-lag error after signed beta correction P_order.

    E_K(n)=(-1)^K(T_n-P_K(n)) is a positive Hausdorff moment sequence.
    Its tail sum is <=a_K/8*B(8*start-6,K+1); multiply by 2pi|h|<8|h|.
    """
    _integer(h); _nat(start, 1); _nat(order)
    return abs(h)*endpoint_coefficients(order)[-1]*beta_integer(8*start-6, order+1)


def window_pi_interval(horizon, lookahead=0):
    """P_M<pi<P_M+16^(1-M)T_M upper bound, M=N+lookahead.

    Enough precision for simultaneous two-time phases through time N-1.
    Numerator and denominator remain exact and reduced by Fraction.
    """
    _nat(horizon, 1); _nat(lookahead)
    m = horizon+lookahead
    partial = sum((forcing(k)/16**(k-1) for k in range(1, m+1)), Q())
    error = Q(1, 16**(m-1)*(8*m+1)*(8*m+2))
    return partial, partial+error


def window_lag_transport_budget(h, horizon, lag, lookahead=0):
    """|C_d(N;pi)-C_d(N;P_(N+K))| <= 128|h|/(15*16^K)*B_(N+K).

    Holds simultaneously for 0<=d<N. This controls approximation only;
    no complete-period cancellation is substituted for an incomplete sum.
    """
    _integer(h); _nat(horizon, 1); _nat(lag); _nat(lookahead)
    if lag >= horizon:
        raise ValueError("lag must be smaller than horizon")
    if lag == 0:
        return Q()
    m = horizon+lookahead
    return Q(128*abs(h), 15*16**lookahead*(8*m+1)*(8*m+2))


def _atan_interval(q, terms):
    total = sum((Q((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), Q())
    other = total+Q((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(total, other), max(total, other)


@lru_cache(None)
def machin_pi_interval(terms=80):
    """Classical Machin identity, alternating-series rational remainder."""
    _nat(terms, 1)
    a, b = _atan_interval(5, terms)
    c, d = _atan_interval(239, terms)
    return 16*a-4*d, 16*b-4*c


def dyadic_enclosure(low, high, bits=100):
    low, high = _exact(low), _exact(high)
    _nat(bits, 1)
    if low > high:
        raise ValueError("reversed interval")
    scale = 2**bits
    return Q(low*scale // 1, scale), Q(-((-high*scale) // 1), scale)


@dataclass(frozen=True)
class ComplexBox:
    real_low: Q
    real_high: Q
    imag_low: Q
    imag_high: Q

    def __add__(self, other):
        return ComplexBox(self.real_low+other.real_low,
                          self.real_high+other.real_high,
                          self.imag_low+other.imag_low,
                          self.imag_high+other.imag_high)

    def __sub__(self, other):
        return ComplexBox(self.real_low-other.real_high,
                          self.real_high-other.real_low,
                          self.imag_low-other.imag_high,
                          self.imag_high-other.imag_low)

    def l1_upper(self):
        return (max(abs(self.real_low), abs(self.real_high))
                + max(abs(self.imag_low), abs(self.imag_high)))

    def modulus_squared_upper(self):
        return (max(abs(self.real_low), abs(self.real_high))**2
                + max(abs(self.imag_low), abs(self.imag_high))**2)

    def outward(self, bits=60):
        return ComplexBox(*dyadic_enclosure(self.real_low, self.real_high, bits),
                          *dyadic_enclosure(self.imag_low, self.imag_high, bits))


def character_interval(low, high, *, pi_bounds=None, order=28, bits=120):
    """Certified exp(2*pi*i*x) box for x in [low,high].

    Real Taylor with derivative bound 1 and Lipschitz phase transport.
    The interval may cross an integer; the same integer is subtracted from
    its entire lift, so modulo discontinuities never invalidate enclosure.
    The default Machin bounds enclose actual pi. If pi_bounds is supplied,
    the caller must prove it contains pi; the (3,4) check is only a domain
    guard, not authentication of that external source premise.
    """
    _nat(order, 1)
    low, high = dyadic_enclosure(low, high, bits)
    pl, pu = dyadic_enclosure(*(machin_pi_interval() if pi_bounds is None
                                else pi_bounds), bits)
    if not (3 < pl < pu < 4):
        raise ValueError("pi enclosure must lie strictly inside (3,4)")
    center, radius = (low+high)/2, (high-low)/2
    center -= (center+Q(1, 2)) // 1
    x = (pl+pu)*center
    angle_error = 2*pu*radius+(pu-pl)*abs(center)
    sin_value = sum(((-1)**k*x**(2*k+1)/factorial(2*k+1)
                     for k in range(order)), Q())
    cos_value = sum(((-1)**k*x**(2*k)/factorial(2*k)
                     for k in range(order)), Q())
    error = abs(x)**(2*order)/factorial(2*order)+angle_error
    return ComplexBox(max(Q(-1), cos_value-error), min(Q(1), cos_value+error),
                      max(Q(-1), sin_value-error), min(Q(1), sin_value+error))


def signed_sum_interval(phases, *, pi_bounds=None):
    total = ComplexBox(Q(), Q(), Q(), Q())
    for low, high in phases:
        total += character_interval(low, high, pi_bounds=pi_bounds).outward(100)
    return total


def correlation_interval(h, horizon, lag, *, source="bbp", lookahead=12):
    """Finite signed lag C_d or rational forced D_d; no digits as proof inputs."""
    _integer(h); _nat(horizon, 1); _nat(lag); _nat(lookahead)
    if lag >= horizon:
        raise ValueError("lag must be smaller than horizon")
    length = horizon-lag
    if source == "forced":
        states = forced_states(horizon)
        phases = [(h*(states[j+lag+1]-states[j+1]),)*2 for j in range(length)]
    else:
        if source == "bbp":
            low, high = window_pi_interval(horizon, lookahead)
        elif source == "machin":
            low, high = machin_pi_interval(2*horizon+40)
        elif source == "partial":
            low = high = window_pi_interval(horizon, lookahead)[0]
        else:
            raise ValueError("unknown source")
        phases = []
        for j in range(length):
            k = h*(16**lag-1)*16**j
            phases.append((min(k*low, k*high), max(k*low, k*high)))
    return signed_sum_interval(phases)
