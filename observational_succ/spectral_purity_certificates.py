"""Outward rational certificates for selected Fejer innovations.

The source path is the original four-pole BBP recurrence, with its full lift.
Character evaluation uses a separately derived Machin/Taylor enclosure. A
Galois trace and the selected complex embedding are deliberately distinct.
"""
from fractions import Fraction as Q

from .pi_source_genesis import character_interval, dyadic_enclosure
from .succ_internal_matrix_walk import authentic_r


def _int(value, minimum, maximum):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError("ordinary integer outside declared finite budget")
    return value


def authentic_prefix(count):
    """Return U_1,...,U_count without discarding any integer carries."""
    _int(count, 1, 2000)
    state = Q()
    result = []
    for n in range(1, count + 1):
        state = 16 * state + authentic_r(n)
        result.append(state)
    return tuple(result)


def innovation_interval(history, arrival, width, *, bits=60):
    """Enclose q by its real cosine polynomial, with rational outward errors.

    This generic evaluator does not attach an authentic-source label to
    caller-supplied phases. Formal group-algebra nonzero is not used as a
    test for nonzero complex evaluation.
    """
    _int(width, 1, 64)
    _int(bits, 16, 120)
    history = tuple(history)
    if (not history or len(history) > 2000 or type(arrival) is not Q
            or any(type(x) is not Q for x in history)):
        raise ValueError("nonempty exact rational history and arrival required")
    low = high = Q(width)
    for previous in history:
        for k in range(1, width):
            phase = (k * (arrival - previous)) % 1
            box = character_interval(phase, phase).outward(bits)
            weight = Q(2 * (width - k), len(history))
            low += weight * box.real_low
            high += weight * box.real_high
    low, high = dyadic_enclosure(low, high, bits)
    return max(Q(), low), min(Q(width * width), high)


def authentic_innovation_interval(arrival_index, width, *, bits=60):
    _int(arrival_index, 2, 2000)
    path = authentic_prefix(arrival_index)
    return innovation_interval(path[:-1], path[-1], width, bits=bits)


def selected_trace_counterexample():
    """Actual arrival n=2, H=3, new 3^2 layer: trace q=3 but q>5.

    The two exact lifted states are checked against an independent reduced
    rational forcing formula. The relative Galois identity is proved in
    SPECTRAL_PURITY_ARITHMETIC.md; this evaluates the selected embedding.
    """
    path = authentic_prefix(2)
    reduced = lambda n: Q(120*n*n - 89*n + 16,
                          (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    if path != (reduced(1), 16*reduced(1) + reduced(2)):
        raise ArithmeticError("original four-pole source mismatch")
    # U_1 has 3-depth 1; U_2 has 3-depth 2. Other primes remain fixed
    # in this relative Galois average. Width 3 sees no nonzero multiple of 3.
    def depth(den):
        result = 0
        while den % 3 == 0:
            result += 1
            den //= 3
        return result
    if (depth(path[0].denominator), depth(path[1].denominator)) != (1, 2):
        raise ArithmeticError("new authentic 3-power layer missing")
    bounds = innovation_interval(path[:-1], path[-1], 3)
    if bounds[0] <= 5:
        raise ArithmeticError("selected embedding failed the strict counterexample")
    return {"arrival_index": 2, "innovation_index": 1, "width": 3,
            "prime": 3, "prior_depth": 1, "arrival_depth": 2,
            "source_states": path, "selected_q_interval": bounds,
            "relative_galois_mean_q": Q(3),
            "pointwise_trace_bound_refuted": True}
