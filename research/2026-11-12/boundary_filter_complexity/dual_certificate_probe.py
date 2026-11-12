"""Exact finite calibrations for the dynamic dual-certificate budget.

This is a finite graph verifier, not a universal BBP or trigonometric prover.
All values and error budgets are exact rationals. A declared domain is part
of the input; excluding a hostile state is never inferred by this verifier.
"""

from fractions import Fraction


def _q(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("certificate values must be exact integers or Fractions")
    return Fraction(value)


def verify_local(transitions, costs, potentials, credits, errors):
    """Check g_n(x) >= c_n + V_(n+1)(F_n x) - V_n(x) - eps_n.

    Each transition row lists every state in that step's claimed domain.
    Return the exact smallest slack, rejecting any malformed/false claim.
    """
    steps = len(transitions)
    if not steps or len(costs) != steps or len(potentials) != steps + 1:
        raise ValueError("inconsistent or empty horizon")
    if len(credits) != steps or len(errors) != steps:
        raise ValueError("inconsistent budget horizon")
    slacks = []
    for n, row in enumerate(transitions):
        if not row or set(row) != set(costs[n]) or set(row) != set(potentials[n]):
            raise ValueError("transition, cost, and potential domains must agree")
        credit, error = _q(credits[n]), _q(errors[n])
        if error < 0:
            raise ValueError("error must be nonnegative")
        for state, target in row.items():
            if target not in potentials[n + 1]:
                raise ValueError("next potential is undefined on the transition")
            slack = (_q(costs[n][state]) - credit
                     - _q(potentials[n + 1][target])
                     + _q(potentials[n][state]) + error)
            if slack < 0:
                raise ValueError("false local inequality")
            slacks.append(slack)
    return min(slacks)


def lower_bound(path, potentials, credits, errors):
    """Evaluate the telescoping lower bound; local validity is separate."""
    if len(path) != len(credits) + 1 or len(potentials) != len(path):
        raise ValueError("inconsistent path horizon")
    if len(errors) != len(credits):
        raise ValueError("inconsistent error horizon")
    return (sum((_q(c) - _q(e) for c, e in zip(credits, errors)), Fraction())
            + _q(potentials[-1][path[-1]]) - _q(potentials[0][path[0]]))


def oscillation(potential):
    values = [_q(value) for value in potential.values()]
    if not values:
        raise ValueError("empty potential domain")
    return max(values) - min(values)


def grid_extension_debt(lipschitz, denominator):
    """Worst off-grid deficit from a Lipschitz residual nonnegative on Γ_Q."""
    if type(denominator) is not int or denominator < 1:
        raise ValueError("positive integer grid denominator required")
    lipschitz = _q(lipschitz)
    if lipschitz < 0:
        raise ValueError("Lipschitz bound must be nonnegative")
    return lipschitz / (2 * denominator)


def smooth_grid_extension_debt(second_derivative_bound, denominator):
    """C² residual deficit between grid endpoints with a paid |R''| bound."""
    if type(denominator) is not int or denominator < 1:
        raise ValueError("positive integer grid denominator required")
    curvature = _q(second_derivative_bound)
    if curvature < 0:
        raise ValueError("second derivative bound must be nonnegative")
    return curvature / (8 * denominator ** 2)


def fixed_point_calibration(start, stop):
    """T(x)=16x mod 1 restricted to the fixed states 0 and 1/3.

    g(0)=0 and g(1/3)=3/2 exactly. V_n(0)=-3n/2, V_n(1/3)=0.
    The local inequality is equality on both states; no pi input is used.
    """
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (start, stop)):
        raise TypeError("integer times required")
    if not 0 <= start < stop:
        raise ValueError("require 0 <= start < stop")
    a, b, eta = Fraction(0), Fraction(1, 3), Fraction(3, 2)
    steps = stop - start
    transitions = [{a: a, b: b} for _ in range(steps)]
    costs = [{a: Fraction(), b: eta} for _ in range(steps)]
    potentials = [{a: -eta * n, b: Fraction()} for n in range(start, stop + 1)]
    return transitions, costs, potentials, [eta] * steps, [Fraction()] * steps
