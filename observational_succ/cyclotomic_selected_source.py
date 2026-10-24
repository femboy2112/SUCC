"""Exact selected-source instruments; no asymptotic cancellation is assumed.

The BBP recurrence comes from common ancestor #252. Prime-window definitions
from sibling #256 are independently reconstructed here, not imported as a
merged dependency. Complex certificates use rational Taylor enclosures.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt

from .bbp_source_memory import forcing
from .pi_source_genesis import (ComplexBox, character_interval, forced_states,
                               machin_pi_interval, signed_sum_interval,
                               beta_integer, endpoint_coefficients)


def _int(n, lo=0):
    if type(n) is not int or n < lo:
        raise ValueError(f"integer >= {lo} required")
    return n


def _harmonic(h):
    if type(h) is not int or h == 0:
        raise ValueError("nonzero integer harmonic required")
    return h


def _rational(x):
    if type(x) not in (int, Q):
        raise ValueError("exact rational required")
    return Q(x)


def prime(p):
    _int(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError("genuine prime required")
    return p


def primary_component(x, p):
    """Canonical p-power component of an exact rational in Q/Z."""
    prime(p)
    x = _rational(x)
    other, power = x.denominator, 1
    while other % p == 0:
        other //= p
        power *= p
    if power == 1:
        return Q()
    return Q((x.numerator*pow(other, -1, power)) % power, power)


def order(base, modulus):
    """Unit order, with the declared convention ord_1(base)=1."""
    _int(base, 2); _int(modulus, 1)
    if gcd(base, modulus) != 1:
        raise ValueError("unit base required")
    if modulus == 1:
        return 1
    value = base % modulus
    k = 1
    while value != 1:
        value = value*base % modulus
        k += 1
    return k


@dataclass(frozen=True)
class PrimeWindow:
    p: int
    m: int
    period: int
    initial: Q
    states: tuple[Q, ...]
    local: tuple[Q, ...]
    complement: tuple[Q, ...]


def prime_window(p, initial=Q()):
    """Exact forcing, with a p-integral initial state explicitly recorded.

    Only initial%1=0 authenticates the original selected source. Other allowed
    states preserve this p-clock but are labelled changed-source controls.
    """
    prime(p)
    initial = _rational(initial)
    if p % 8 != 1 or initial.denominator % p == 0:
        raise ValueError("p=1 mod8 and p-integral initial state required")
    m = (p-1)//8
    period = order(16, p)
    if m % period:
        raise ArithmeticError("eighth-power clock invariant failed")
    values = forced_states(4*m, initial)[m+1:]
    local = tuple(Q(4*pow(16, t, p) % p, p) for t in range(3*m))
    complement = tuple((y-u) % 1 for y, u in zip(values, local))
    if any(v.denominator % p == 0 for v in complement):
        raise ArithmeticError("source p-primary split failed")
    return PrimeWindow(p, m, period, initial, values, local, complement)


def box_scale(box, scale):
    scale = _rational(scale)
    a, b = sorted((scale*box.real_low, scale*box.real_high))
    c, d = sorted((scale*box.imag_low, scale*box.imag_high))
    return ComplexBox(a, b, c, d)


def sqrt_upper(x, bits=55):
    """Outward rational square-root bound, by integer arithmetic."""
    x = _rational(x); _int(bits, 1)
    if x < 0:
        raise ValueError("nonnegative radicand required")
    scale = 2**bits
    target = (x.numerator*scale*scale+x.denominator-1)//x.denominator
    result = isqrt(target)
    if result*result < target:
        result += 1
    return Q(result, scale)


def character_mean(phases):
    phases = tuple(phases)
    if not phases:
        raise ValueError("nonempty phase sequence required")
    return box_scale(signed_sum_interval(((x, x) for x in phases)), Q(1, len(phases)))


def interference_interval(window, h=1):
    """Actual signed I_p as full phases minus block-anchored phases."""
    _harmonic(h)
    L = window.period
    full = character_mean(h*y for y in window.states)
    anchor = character_mean(h*(window.local[t % L]+window.complement[(t//L)*L])
                            for t in range(3*window.m))
    return full-anchor


def complement_spectrum(window, h=1):
    """Normalized DFT of the averaged, block-centered complement weights."""
    _harmonic(h)
    L, delta = window.period, 3*window.m
    anchor = character_mean(h*window.complement[t] for t in range(0, delta, L))
    result = []
    for k in range(L):
        value = character_mean(h*w-Q(k*(t % L), L)
                               for t, w in enumerate(window.complement))
        result.append(value-anchor if k == 0 else value)
    return tuple(result)


def twisted_clock_certificate(p, h=1):
    """Finite certified twisted bounds from exact nonzero lag sums.

    No numerical BGK exponent is invented. For each prime the actual lag
    sums give epsilon; the paper applies the external asymptotic theorem.
    """
    prime(p); _harmonic(h)
    if p % 8 != 1 or h % p == 0:
        raise ValueError("nonresonant eighth-power prime clock required")
    L = order(16, p)
    phases = tuple(Q(4*h*pow(16, s, p), p) for s in range(L))
    gauss = character_mean(phases)
    eps0 = min(Q(1), sqrt_upper(gauss.modulus_squared_upper()))
    epsilon = Q()
    for d in range(1, L):
        a = 4*h*(pow(16, d, p)-1)
        lag = character_mean(Q(a*pow(16, t, p), p) for t in range(L))
        epsilon = max(epsilon, min(Q(1), sqrt_upper(lag.modulus_squared_upper())))
    delta_sq = Q(1, L)+Q(L-1, L)*epsilon
    twisted = tuple(character_mean(phases[s]-Q(k*s, L) for s in range(L))
                    for k in range(L))
    return {"period": L, "epsilon": epsilon, "zero_mode_upper": eps0,
            "twist_upper_squared": delta_sq, "twisted": twisted}


def spectral_interference_certificate(window, h=1):
    clock = twisted_clock_certificate(window.p, h)
    spectrum = complement_spectrum(window, h)
    mass = tuple(sqrt_upper(z.modulus_squared_upper()) for z in spectrum)
    bound = (clock["zero_mode_upper"]*mass[0]
             + sqrt_upper(clock["twist_upper_squared"])*sum(mass[1:], Q()))
    return {"clock": clock, "spectrum": spectrum, "wiener_upper": sum(mass, Q()),
            "interference_upper": bound, "actual": interference_interval(window, h)}


def dyadic_initial_control(depth):
    """Source-certified nearest c/16^depth to -pi/16; no pi digits input.

    Machin alternating-series intervals certify selection. The returned
    interval and error refer to the signed lift, before taking mod1.
    """
    _int(depth, 1)
    scale = 16**depth
    terms = 2*depth+20
    while True:
        pl, pu = machin_pi_interval(terms)
        low, high = -pu/16, -pl/16
        c0, c1 = (scale*low+Q(1, 2))//1, (scale*high+Q(1, 2))//1
        if c0 == c1:
            initial = Q(c0, scale)
            error = max(abs(initial-low), abs(initial-high))
            if error <= Q(1, 2*scale):
                return {"initial": initial, "depth": depth, "pi_interval": (pl, pu),
                        "error_upper": error, "machin_terms": terms}
        terms *= 2


def coherent_window_error(p, depth, h=1, initial_error=None):
    """Upper bound on |mean full changed-state phases - 1|, exact rational.

    The initial state must satisfy |initial+T_0| <= initial_error (or the
    default nearest-dyadic budget). This function checks the size of that
    supplied budget, not its source membership; dyadic_initial_control
    constructs a state and independently certifies the required premise.
    """
    prime(p); _harmonic(h); _int(depth, 1)
    if p % 8 != 1:
        raise ValueError("eighth-power source window required")
    m = (p-1)//8
    if depth < 4*m:
        raise ValueError("control depth must cover the whole source window")
    error = Q(1, 2*16**depth) if initial_error is None else _rational(initial_error)
    if not 0 <= error <= Q(1, 2*16**depth):
        raise ValueError("certified nearest-dyadic error budget required")
    beta = Q(1, (8*m+9)*(8*m+10))
    expansion = error*Q(16**(4*m+1)-16**(m+1), 45*m)
    return Q(44, 7)*abs(h)*(beta+expansion)


def coalescence_depth(initial):
    """First n with 16^n initial integer, or None if an odd denominator remains."""
    initial = _rational(initial)
    den, exponent = initial.denominator, 0
    while den % 2 == 0:
        den //= 2
        exponent += 1
    return (exponent+3)//4 if den == 1 else None


def clock_profile(base, h, modulus):
    """Exact transient/period of h*base^j mod modulus, retaining all prime powers."""
    _int(base, 2); _harmonic(h); _int(modulus, 1)
    reduced = modulus//gcd(modulus, abs(h))
    unit, transient = reduced, 0
    while gcd(unit, base) > 1:
        unit //= gcd(unit, base)
        transient += 1
    period = order(base, unit)
    return {"reduced_modulus": reduced, "unit_modulus": unit,
            "transient": transient, "period": period,
            "first_repeat_index": transient+period}


def ternary_tomography_clock(h, horizon):
    """Linear-size base16 second-moment clock; no fourth-moment claim."""
    _harmonic(h); _int(horizon, 1)
    v, power = abs(h), 1
    while v % 3 == 0:
        power *= 3
        v //= 3
    size = 1
    while size < horizon:
        size *= 3
    return 3*power*size


def fourth_alias_polynomial(base, h, horizon, modulus):
    """Integer Laurent exponents of the N^4-scaled grid fourth mean.

    Returns coefficients c_q such that grid mean |G_x|^4 =
    N^-4 sum_q c_q e(q*x). A zero-only polynomial is source-independent.
    """
    _int(base, 2); _harmonic(h); _int(horizon, 1); _int(modulus, 1)
    groups = {}
    for j in range(horizon):
        for k in range(horizon):
            frequency = h*(base**j+base**k)
            groups.setdefault(frequency % modulus, []).append(frequency)
    coefficients = {}
    for values in groups.values():
        for a in values:
            for b in values:
                coefficients[a-b] = coefficients.get(a-b, 0)+1
    return coefficients


def inverse_observer_delay(base, depth, cutoff):
    """First forward time at which a cutoff-H Fourier observer can see root x."""
    _int(base, 2); _int(depth); _int(cutoff, 1)
    level, power = 0, 1
    while power*base <= cutoff:
        level += 1
        power *= base
    return max(0, depth-level)


def pell_tail_approximation(n, order):
    """Exact A_K(n); the analytic signed remainder is an inherited theorem."""
    _int(n); _int(order)
    a = endpoint_coefficients(order)
    return sum(((-1)**j*a[j]*beta_integer(8*n+1, j+2)
                for j in range(order)), Q())


def corrected_carry_defect(n, lag, order):
    """Rational lift of the first phase-sensitive base16 equal-count carry.

    For q_n=y_n+A_K(n), this lift equals
    16*q_n+q_(n+d+1)-q_(n+1)-16*q_(n+d) modulo1.
    Its signed negative (-1)^(K+1)*lift is a strict positive Hausdorff
    moment sequence in n, by the paper's remainder-measure proof.
    """
    _int(n); _int(lag, 1); _int(order)
    A = lambda j: pell_tail_approximation(j, order)
    return (-forcing(n+1)+forcing(n+lag+1)
            +16*A(n)+A(n+lag+1)-A(n+1)-16*A(n+lag))


def corrected_carry_upper(n, lag, order):
    """Strict rational upper for absolute lifted carry defect, not cancellation."""
    _int(n); _int(lag, 1); _int(order)
    a = endpoint_coefficients(order)[-1]
    return a*min(16*beta_integer(8*n+1, order+2),
                 128*lag*beta_integer(8*n+1, order+3))


def corrected_origin_l2_squared_upper(h, start, length, order):
    """Rational upper for Haar L2 difference of actual and corrected responses.

    start is the first forced-state index>=1; the response has length terms.
    The same clock frequencies are used for both responses. This compares
    responses; each individual second/fourth moment remains source-blind.
    """
    _harmonic(h); _int(start, 1); _int(length, 1); _int(order)
    a = endpoint_coefficients(order)[-1]
    return (Q(44*abs(h)*a, 7*length)**2
            *beta_integer(8*start+1, order+2)
            *beta_integer(8*start-6, order+1)/8)
