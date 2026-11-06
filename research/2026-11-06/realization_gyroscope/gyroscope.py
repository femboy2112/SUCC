"""SUCC research-only recursive observer gyroscope and encoding-gauge probes.

Exact Fraction arithmetic, original four signed BBP poles, U_0 = 0. This module
is an instrument, not a pi normality theorem, Lean certification, or quantum model.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable

Forcing = Callable[[int], Fraction]


def forcing(n: int) -> Fraction:
    """The actual four-pole source: r(n), n >= 1."""
    if type(n) is not int or n < 1:
        raise ValueError("source index must be an integer >= 1")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def circle(x: Fraction | int) -> Fraction:
    return Fraction(x) % 1


def prefix(x: Fraction | int, base: int, width: int) -> tuple[int, ...]:
    """First `width` base-`base` digits, canonical terminating convention."""
    if type(base) is not int or base < 2 or type(width) is not int or width < 0:
        raise ValueError("base >= 2; width a nonnegative integer")
    y = circle(x)
    out = []
    for _ in range(width):
        y *= base
        d = y.numerator // y.denominator
        out.append(d)
        y -= d
    return tuple(out)


def source_state(n: int, seed: Fraction | int = 0, r: Forcing = forcing) -> Fraction:
    """Exact circular SUCC state U_n(seed), with no digit oracle."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    x = circle(seed)
    for k in range(1, n+1):
        x = circle(16*x + r(k))
    return x


def tail_interval(n: int, depth: int = 12) -> tuple[Fraction, Fraction]:
    """Rigorous enclosure of T_n for n>=1, using r(k) < 1/k^2 (k>=2)."""
    if type(n) is not int or n < 1 or type(depth) is not int or depth < 0:
        raise ValueError("require integer n>=1 and depth>=0")
    partial = sum((Fraction(1, 16**j)*forcing(n+j)
                   for j in range(1, depth+1)), Fraction(0))
    # Remainder = 16^-depth T_(n+depth); T_m < 1/[15(m+1)^2].
    remainder_bound = Fraction(1, 16**depth * 15 * (n+depth+1)**2)
    return partial, partial + remainder_bound


def model_policy(observer: 'Observer') -> int:
    """Self-dependent probe resolution: predicted phase and last event affect action."""
    predicted_first_digit = (16*observer.model_world).numerator // (16*observer.model_world).denominator
    return 1 + ((observer.last_cell + predicted_first_digit + observer.time) % 2)


@dataclass(frozen=True)
class Observer:
    """Actual physical/mathematical observer memory, including its own model."""
    model_world: Fraction
    last_cell: int = 0
    time: int = 0
    transcript: tuple[tuple[int,int], ...] = ()


@dataclass(frozen=True)
class Carrier:
    """State (realized arithmetic world, realized observer). No external oracle."""
    world: Fraction
    observer: Observer


def initialize(seed: Fraction | int = 0, *, model_seed: Fraction | int | None = None) -> Carrier:
    s = circle(seed)
    return Carrier(world=s, observer=Observer(
        model_world=s if model_seed is None else circle(model_seed)))


def advance(g: Carrier, *, physical_source: Forcing = forcing,
            internal_source: Forcing = forcing,
            policy: Callable[[Observer], int] = model_policy) -> Carrier:
    """One carrier tick, including model computation, sensing and feedback.

    The observer's action changes *what is measured*, never the BBP source.
    The actual carrier realizes the internal calculation as part of the state.
    """
    o = g.observer
    depth = policy(o)
    if type(depth) is not int or depth < 1:
        raise ValueError("policy must return a positive integer depth")
    cell = sum(d*16**(depth-1-i) for i, d in enumerate(prefix(g.world, 16, depth)))
    new_observer = Observer(
        model_world=circle(16*o.model_world + internal_source(o.time+1)),
        last_cell=cell,
        time=o.time+1,
        transcript=o.transcript + ((depth,cell),))
    new_world = circle(16*g.world + physical_source(o.time+1))
    return Carrier(world=new_world, observer=new_observer)


def exact_replay(seed: Fraction | int, ticks: int,
                 *, physical_source: Forcing = forcing,
                 internal_source: Forcing = forcing,
                 policy: Callable[[Observer], int] = model_policy) -> Carrier:
    g = initialize(seed)
    for _ in range(ticks):
        g = advance(g, physical_source=physical_source,
                    internal_source=internal_source, policy=policy)
    return g


def phase_orbit(beta: Fraction | int, length: int, base: int = 16) -> tuple[Fraction,...]:
    """Exact completed orbit {base^n beta}, for a declared rational beta."""
    if type(length) is not int or length < 0 or type(base) is not int or base < 2:
        raise ValueError("length >= 0 and integer base >=2 required")
    x = circle(beta)
    out = []
    for _ in range(length):
        out.append(x)
        x = circle(base*x)
    return tuple(out)


def interleave_phase(beta: Fraction | int, blocks: int) -> tuple[Fraction,...]:
    """Four phase observations of a x16 orbit, exactly the corresponding x2 orbit."""
    original = phase_orbit(beta, blocks, 16)
    return tuple(circle(2**j*x) for x in original for j in range(4))


def source_bound_polynomial(t: int) -> int:
    """D(n)-n^2 A(n), n=t+2, as an independent integer-polynomial witness."""
    if type(t) is not int or t < 0:
        raise ValueError("t >= 0")
    return 392*t**4+2201*t**3+4494*t**2+3902*t+1185


def decode_gauge(observed: Fraction | int, action_shift: Fraction | int) -> Fraction:
    """Recover x from a *logged exact* rotational chart y = x + action_shift."""
    return circle(Fraction(observed)-Fraction(action_shift))


def joint_weyl(observed: tuple[Fraction,...],
               action_shifts: tuple[Fraction,...], h: int) -> complex:
    """Gauge-invariant Fourier witness of the decoded original carrier orbit.

    Caller must attest that observed[n] = x[n] + action_shift[n] mod 1;
    the function cannot authenticate that assertion or establish cancellation.
    """
    import cmath
    import math
    if len(observed) != len(action_shifts) or not observed:
        raise ValueError("nonempty, equally sized observation/action logs required")
    if type(h) is not int:
        raise ValueError("integer Fourier mode required")
    return sum(cmath.exp(2j*math.pi*h*float(decode_gauge(y,a)))
               for y,a in zip(observed,action_shifts))/len(observed)