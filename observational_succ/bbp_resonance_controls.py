"""Exact hostile controls for BBP prime-window resonance estimates.

These are explicitly CHANGED-INITIAL-STATE or CHANGED-RECURRENCE controls,
never substitutes for the authentic zero-initial BBP source. The odd-denominator
same-forcing control attains a normalized modulus deficit O_h(m^-4), showing
the order limitation of bounds uniform over rational initial states.
See research/2026-10-25/BBP_RESONANCE_OBSTRUCTIONS.md for proofs and provenance.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd

from .bbp_cyclotomic_birth import first_window_residues, p_primary_phase
from .bbp_prime_window_projection import window_parameters
from .bbp_source_memory import forcing, source_tail_beta_bracket


def _integer(value: int, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("integer in the declared domain required")
    return value


def _exact(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def nearest_grid_point(value: Q, denominator: int) -> Q:
    """A nearest a/q, with ties resolved toward +infinity; entirely rational."""
    value = _exact(value)
    _integer(denominator, 1)
    scaled = denominator * value
    numerator = (2 * scaled.numerator + scaled.denominator) // (2 * scaled.denominator)
    return Q(numerator, denominator)


def exact_forced_history(count: int, initial: Q = Q()) -> tuple[Q, ...]:
    """UNWRAPPED rational states, including initial; original four-pole forcing."""
    _integer(count, 0)
    state = _exact(initial)
    result = [state]
    for n in range(1, count + 1):
        state = 16 * state + forcing(n)
        result.append(state)
    return tuple(result)


def authentic_history_failures(history: tuple[Q, ...]) -> tuple[str, ...]:
    """Finite authentication checks U0=0 AND every supplied four-pole step.

    Passing authenticates only the supplied finite history. A source-name
    string, p-primary agreement, or rational denominator parity is not enough.
    """
    if not history:
        raise ValueError("history must include the initial state")
    states = tuple(_exact(value) for value in history)
    failures = []
    if states[0] != 0:
        failures.append("initial-state")
    for n in range(1, len(states)):
        if states[n] - 16 * states[n - 1] != forcing(n):
            failures.append("forcing-step-%d" % n)
    return tuple(failures)


def pointwise_pfree_antiphase(p: int, denominator: int, h: int = 1) -> dict:
    """Odd p-free, L-periodic anti-phases with O_h(q^-2) modulus deficit.

    Rounds each -a_t/p independently to the q-grid. This preserves period L
    but does NOT preserve the authentic forcing. The recurrence defect is
    an explicit measured quantity, not silently discarded.
    """
    _integer(denominator, 1)
    _integer(h)
    m, length, delta, blocks = window_parameters(p)
    if denominator % 2 == 0 or gcd(denominator, p) != 1:
        raise ValueError("odd denominator coprime to p required")
    primary = tuple(Q(a, p) for a in first_window_residues(p))
    complement = tuple(nearest_grid_point(-a, denominator) for a in primary)
    errors = tuple(a + w for a, w in zip(primary, complement))
    if any(abs(x) > Q(1, 2 * denominator) for x in errors):
        raise AssertionError("nearest-grid error bound failed")
    defects = tuple((complement[t + 1] - 16 * complement[t]) % 1
                    for t in range(delta - 1))
    return {"source": "pointwise-pfree-antiphase-control", "p": p, "m": m,
            "L": length, "delta": delta, "blocks": blocks, "h": h,
            "denominator": denominator, "primary": primary,
            "complement": complement, "errors": errors,
            "homogeneous_recurrence_defects": defects,
            "real_mean_lower": Q(1) - Q(242 * h * h, 49 * denominator**2),
            "authentic_source": False}


def same_forcing_odd_control(p: int, h: int = 1) -> dict:
    """Same BBP forcing, same p-primary birth, near-maximal signed window.

    N=4m, q=2*p*m^2*16^N+1. Round -U_N/16^N to an initial c in (1/q)Z.
    For n=m+1,...,4m, |X_n|<1/(32*m^2), giving
      |sum e(h X_n)/(3m)| > 1 - 121*h^2/(6272*m^4),  h != 0.
    Every operation selecting c is finite rational arithmetic. No pi digit
    or irrational Green tail is an input. The sole authentic-history failure
    is U0=c != 0. A DIFFERENT c is selected for each p-window.
    """
    _integer(h)
    m, length, delta, blocks = window_parameters(p)
    horizon = 4 * m
    denominator = 2 * p * m * m * 16**horizon + 1
    original = exact_forced_history(horizon)
    terminal_alpha = original[-1] / 16**horizon
    initial = nearest_grid_point(-terminal_alpha, denominator)
    epsilon = initial + terminal_alpha
    history = exact_forced_history(horizon, initial)
    states = history[m + 1:]
    primary = tuple(Q(a, p) for a in first_window_residues(p))
    complement = tuple((state - a) % 1 for state, a in zip(states, primary))
    budgets = tuple(source_tail_beta_bracket(n)[1] + Q(16**n, 2 * denominator)
                    for n in range(m + 1, horizon + 1))
    if abs(epsilon) > Q(1, 2 * denominator):
        raise AssertionError("rational initial-state approximation failed")
    if any(abs(state) >= bound or bound >= Q(1, 32 * m*m)
           for state, bound in zip(states, budgets)):
        raise AssertionError("backward source-tail certificate failed")
    if any(w.denominator % p == 0 or w.denominator % 2 == 0 for w in complement):
        raise AssertionError("odd p-free complement type was not preserved")
    if tuple(p_primary_phase(state, p) for state in states) != first_window_residues(p):
        raise AssertionError("authentic p-primary clock was changed")
    failures = authentic_history_failures(history)
    if failures != ("initial-state",):
        raise AssertionError("control must change exactly the initial source selector")
    squared_budget = sum((bound * bound for bound in budgets), Q()) / delta
    return {"source": "same-forcing-odd-initial-control", "p": p, "m": m,
            "L": length, "delta": delta, "blocks": blocks, "h": h,
            "horizon": horizon, "denominator": denominator, "initial": initial,
            "terminal_alpha": terminal_alpha, "initial_error": epsilon,
            "history": history, "states": states, "primary": primary,
            "complement": complement, "phase_budgets": budgets,
            "real_mean_lower": Q(1) - Q(968, 49) * h*h * squared_budget,
            "modulus_deficit_upper": Q(121 * h*h, 6272 * m**4),
            "authentic_failures": failures, "authentic_source": False}


def one_impulse_control(p: int, preserved_steps: int = 0) -> dict:
    """U0=0, exact first K steps, then one explicit nonauthentic forcing impulse.

    K+1 is required to precede the p-birth. After that impulse the trajectory
    equals same_forcing_odd_control, so its p-window remains coherent. This
    preserves the entire forcing tail and its asymptotic expansion, but fails
    the exact four-pole law at one recorded index. No source mutation is hidden.
    """
    _integer(preserved_steps, 0)
    data = same_forcing_odd_control(p)
    if preserved_steps >= data["m"]:
        raise ValueError("the mutated impulse must precede the first p-birth")
    impulse_index = preserved_steps + 1
    impulse = 16**impulse_index * data["initial"]
    state = Q()
    history = [state]
    for n in range(1, data["horizon"] + 1):
        state = 16 * state + forcing(n) + (impulse if n == impulse_index else 0)
        history.append(state)
    if tuple(history[impulse_index:]) != data["history"][impulse_index:]:
        raise AssertionError("single impulse did not realize the changed selector")
    return {"source": "one-impulse-control", "p": p, "preserved_steps": preserved_steps,
            "impulse_index": impulse_index, "impulse": impulse,
            "history": tuple(history), "authentic_source": False,
            "authentic_failures": authentic_history_failures(tuple(history))}


def homogeneous_denominator_lower(p: int, count: int, radius: Q) -> Q:
    """Necessary q >= 16^(count-1)/(p*radius) for homogeneous coherence.

    Hypotheses: x=a/p+b/q has nonzero p-primary component, gcd(p,q)=1;
    every 16^t*x has centered lift of absolute value <= radius for t<count;
    0<radius<1/17. Then successive centered lifts cannot wrap and grow by 16.
    This bound does NOT apply to the inhomogeneous BBP recurrence.
    """
    window_parameters(p)
    _integer(count, 1)
    radius = _exact(radius)
    if not Q() < radius < Q(1, 17):
        raise ValueError("requires 0 < radius < 1/17")
    return Q(16**(count - 1), p) / radius


def inverse_source_window_arcs(p: int, angular_radius: Q, h: int = 1) -> dict:
    """Explicit rational seeds forced by near-maximal prime-window coherence.

    Set D=3m and T=D-1. If the selected Fourier modulus deficit is at most
    8*a^2/D, and 34*a+|h|*(max forcing-min forcing)<1, its starting phase
    must lie in 15*|h| arcs centered j/(15*|h|)-sum_(k=1)^T16^-k*r(n0+k).
    The returned radius is 16^-T*(32*a+|h|*r(n0+T))/(15*|h|).

    This constructs a CONDITIONAL inverse theorem, not an assertion that
    authentic BBP satisfies its coherence hypothesis. Membership is exact;
    it is necessary, not sufficient, for the displayed deficit threshold.
    """
    _integer(h)
    if h == 0:
        raise ValueError("nonzero Fourier frequency required")
    angular_radius = _exact(angular_radius)
    if angular_radius <= 0:
        raise ValueError("positive rational angular radius required")
    m, length, delta, blocks = window_parameters(p)
    start = m+1
    steps = delta-1
    first_forcing, last_forcing = forcing(start+1), forcing(start+steps)
    spread = first_forcing-last_forcing
    if 34*angular_radius+abs(h)*spread >= 1:
        raise ValueError("single-integer unwrapping condition must be strict")
    source_sum = sum((forcing(start+k)/16**k for k in range(1, steps+1)), Q())
    radius = (32*angular_radius+abs(h)*abs(last_forcing))/(15*abs(h)*16**steps)
    return {"source": "authentic-bbp-conditional-inverse-arcs", "p": p, "m": m,
            "L": length, "delta": delta, "blocks": blocks, "h": h,
            "start_index": start, "steps": steps, "angular_radius": angular_radius,
            "forcing_spread": spread, "finite_source_sum": source_sum,
            "arc_count": 15*abs(h), "arc_radius": radius,
            "deficit_threshold": 8*angular_radius**2/delta,
            "coherence_hypothesis_established": False}


def inverse_arc_membership(p: int, phase: Q, angular_radius: Q, h: int = 1) -> dict:
    """Exact nearest-arc check; an outside authentic start gives a deficit lower bound.

    The caller supplies the actual starting phase. Source authentication and
    the finite inverse theorem are separate from mere membership in these arcs.
    """
    phase = _exact(phase)
    data = inverse_source_window_arcs(p, angular_radius, h)
    shifted = (phase+data["finite_source_sum"]) % 1
    grid_point = nearest_grid_point(shifted, data["arc_count"])
    displacement = (shifted-grid_point) % 1
    distance = min(displacement, 1-displacement)
    index = int(grid_point*data["arc_count"]) % data["arc_count"]
    return {"p": p, "h": h, "cell_index": index,
            "center": (Q(index, data["arc_count"])-data["finite_source_sum"]) % 1,
            "distance": distance, "radius": data["arc_radius"],
            "inside": distance <= data["arc_radius"],
            "deficit_threshold": data["deficit_threshold"]}
