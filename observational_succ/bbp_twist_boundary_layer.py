"""Certified boundary-layer observable for a finite sign-flipped BBP seam.

These are changed-initial trajectories. A finite seam is not a cyclic forcing
law. The paper limit is m*(1-|mean phase|) -> C_h/3, whereas the differently
tuned PRK controls have m^-4 deficit. No authentic cancellation is claimed.
"""
from fractions import Fraction as Q

from .bbp_resonance_controls import exact_forced_history
from .bbp_source_memory import tail_interval, source_tail_beta_bracket
from .bbp_prime_window_signed_intervals import box_phase


def _integer(n, lower=1):
    if type(n) is not int or n < lower:
        raise ValueError("integer in the stated domain required")
    return n


def _frequency(h):
    if type(h) is not int:
        raise ValueError("integer frequency required")
    return h


def twisted_window(m):
    """Exact states n=m+1,...,4m satisfying X_(4m)=-X_0."""
    _integer(m)
    original = exact_forced_history(4*m)
    initial = -original[-1]/(16**(4*m)+1)
    return initial, tuple(original[n]+16**n*initial
                          for n in range(m+1,4*m+1))


def edge_loss_interval(h=1, depth=10, source_depth=14, phase_terms=12):
    """Rational enclosure of C_h=sum_j>=0 (1-cos(2*pi*h*alpha*16^-j)).

    alpha is enclosed by the authentic positive source sum, never supplied
    pi digits. Character boxes use the independent Machin pi enclosure.
    Each omitted term is <=2*pi^2*h^2*alpha^2*16^(-2j).
    """
    _frequency(h); _integer(depth); _integer(source_depth); _integer(phase_terms)
    if h == 0:
        return Q(), Q()
    lo, hi = tail_interval(0, source_depth)
    mid = (lo+hi)/2
    lower = upper = Q()
    for j in range(depth):
        box = box_phase(h*mid/16**j, terms=phase_terms)
        # cosine is 2*pi-Lipschitz in circle coordinates.
        error = Q(44,7)*abs(h)*(hi-lo)/(2*16**j)
        lower += max(Q(), 1-box[1]-error)
        upper += min(Q(2), 1-box[0]+error)
    upper += 2*Q(22,7)**2*h*h*hi*hi*Q(1,16**(2*depth))/Q(255,256)
    return lower, upper


def edge_complex_error(m, h=1, source_depth=14):
    """Bound |sum_window(e(hX_n)-1)-sum_j>=0(e(h alpha/16^j)-1)|.

    Uses sum_(n>m) T_n<1/(64m), exact geometric edge transport,
    and the inherited uniform source-tail bracket. Bound tends to zero.
    """
    _integer(m); _frequency(h); _integer(source_depth)
    alpha_upper = tail_interval(0, source_depth)[1]
    terminal_tail = source_tail_beta_bracket(4*m)[1]
    edge_error = terminal_tail+alpha_upper/16**(4*m)
    missing_edge = alpha_upper/16**(3*m)
    return Q(44,7)*abs(h)*(Q(1,64*m)+Q(16,15)*(edge_error+missing_edge))


def scaled_deficit_budget(m, h=1, source_depth=14):
    """Bound |m*(1-|mean e(hX)|)-C_h/3| by an explicit O_h(1/m).

    The check below enforces Re(mean)>=1/2, used in converting real-part
    loss to modulus loss. A failed check means enlarge m, not a false theorem.
    """
    _integer(m); _frequency(h); _integer(source_depth)
    alpha_upper = tail_interval(0, source_depth)[1]
    error = edge_complex_error(m,h,source_depth)
    total_bound = Q(44,7)*abs(h)*alpha_upper*Q(16,15)+error
    if 2*total_bound > 3*m:
        raise ValueError("enlarge m to certify positive mean real part")
    return error/3+total_bound*total_bound/(9*m)


def edge_loss_power_coefficient(k):
    """Coefficient of (2*pi*h*alpha)^(2k) in the entire edge-loss series.

    C_h= sum_k>=1 (-1)^(k+1)*(2*pi*h*alpha)^(2k)
                       /[(2k)!*(1-16^(-2k))].
    """
    from math import factorial
    _integer(k)
    return Q((-1)**(k+1),factorial(2*k))/(1-Q(1,16**(2*k)))
