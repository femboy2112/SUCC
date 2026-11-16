"""Finite exact interfaces for the forward odometer suspension, Gamma clocks,
and Euler-Hasse forward-difference zeta values.

These are declared mathematical carriers, NOT physics, a full analytic
continuation certificate, or an RH/normality result. Uses no negative seed.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd
from cmath import exp, pi

Q = Fraction


def natural(n: int, *, minimum: int = 0):
    if type(n) is not int or n < minimum:
        raise ValueError(f"expected integer >= {minimum}")
    return n


def lcm_clock(n: int) -> int:
    """Period of the least synchronized forward clock C_1,...,C_n."""
    natural(n, minimum=1)
    period = 1
    for j in range(1, n + 1):
        period = period // gcd(period, j) * j
    return period


def clock_thread(value: int, depth: int) -> tuple[int, ...]:
    """Consistent, ordinary signed integer under all finite clock quotients.

    A negative value is a REQUESTED TARGET, not a starting source seed.
    """
    if type(value) is not int:
        raise ValueError("integer target required")
    natural(depth, minimum=1)
    return tuple(value % lcm_clock(n) for n in range(1, depth + 1))


def forward_winding(steps: int, depth: int) -> tuple[int, ...]:
    """From origin, m positive suspension cycles hit -m in each clock."""
    natural(steps)
    natural(depth, minimum=1)
    return tuple((-steps) % lcm_clock(n) for n in range(1, depth + 1))


def suspension_circle(length: int, clock_state: int, phase: Q) -> Q:
    """(a,u) maps to a-u mod L; seam (a,1) ~ (a-1,0)."""
    natural(length, minimum=1)
    if type(clock_state) is not int or type(phase) not in (int,Q):
        raise ValueError("clock state integer, phase exact rational")
    phase = Q(phase)
    if not 0 <= phase <= 1:
        raise ValueError("phase in closed unit interval")
    return (Q(clock_state) - phase) % length


def forward_phase(length: int, elapsed: Q) -> Q:
    """Continuous forward path from (a,u)=(0,0) at rational elapsed t>=0."""
    natural(length, minimum=1)
    if type(elapsed) not in (int,Q) or elapsed < 0:
        raise ValueError("nonnegative rational elapsed time required")
    return (-Q(elapsed)) % length


def consistent_thread(residues: tuple[int, ...]) -> bool:
    """Check bonding maps between all adjacent finite synchronized clocks."""
    return all(type(r) is int and 0 <= r < lcm_clock(i + 1) for i,r in enumerate(residues)) and all(
        residues[i] % lcm_clock(i) == residues[i-1]
        for i in range(1,len(residues))
    )


def gamma_latency_moments(steps: int, rate: int) -> tuple[Q, Q]:
    """km independent Exp(k) steps: total T~Gamma(km, rate=k)."""
    natural(steps, minimum=1)
    natural(rate, minimum=1)
    return Q(steps), Q(steps,rate)


def gamma_laplace_of_forward_clock(steps: int, rate: int, q: Q) -> Q:
    """Exact Laplace E exp(-qT), T~Gamma(km,k), q>=0 rational."""
    natural(steps, minimum=1)
    natural(rate, minimum=1)
    if type(q) not in (int, Q) or q < 0:
        raise ValueError("nonnegative exact Laplace parameter")
    q = Q(q)
    return (Q(rate)/(Q(rate)+q))**(steps*rate)


def gamma_mean_transport_error_lipschitz(steps: int, rate: int, bound: Q) -> float:
    """Rigorous analytic expression L sqrt(m/k), returned as float for display.

    For a certificate use: |E f(phi_T x)-f(phi_m x)|^2 <= L^2*m/k.
    """
    natural(steps, minimum=1)
    natural(rate, minimum=1)
    if type(bound) not in (int,Q) or bound < 0:
        raise ValueError("nonnegative exact Lipschitz bound")
    return float(Q(bound)) * (steps/rate)**0.5


def gamma_clock_fourier(steps: int, rate: int, length: int, harmonic: int=1) -> complex:
    """Exact closed formula in C, numerically represented with complex powers:

    E exp(-2pi i h T/L)=(1+2pi i h/(kL))^(-km).
    Do not regard machine floats as a theorem certificate.
    """
    natural(steps, minimum=1)
    natural(rate, minimum=1)
    natural(length, minimum=1)
    if type(harmonic) is not int:
        raise ValueError("integer harmonic")
    return (1 + 2j*pi*harmonic/(rate*length))**(-steps*rate)


def clock_fourier_limit(steps: int, length: int, harmonic: int=1) -> complex:
    natural(steps)
    natural(length, minimum=1)
    if type(harmonic) is not int:
        raise ValueError("integer harmonic")
    return exp(-2j*pi*harmonic*steps/length)


def positive_power_difference(moment: int, order: int) -> int:
    """Only positive values (j+1)^m, signed by the finite Pascal face.

    sum_{j=0}^n (-1)^j binom(n,j)(j+1)^m = (-1)^n Delta^n x^m |_{x=1}.
    """
    natural(moment)
    natural(order)
    return sum((-1)**j * comb(order,j) * (j+1)**moment for j in range(order+1))


def eta_negative_euler(moment: int) -> Q:
    """Sondow/Hasse Euler-transformed eta(-m); finite since Delta^(m+1) x^m=0.

    Uses positive source coordinates 1,2,...,m+1 only. Analytic
    identification with eta(-m) depends on the classical continuation theorem.
    """
    natural(moment)
    return sum((Q(positive_power_difference(moment,n),2**(n+1))
                for n in range(moment+1)), Q(0))


def eta_negative_recurrence(moment: int) -> Q:
    """Independent recurrence: E(t)=e^t/(1+e^t), (1+e^t)E=e^t.

    a_m = (1-sum_{j=1}^m C(m,j)a_{m-j})/2.
    """
    natural(moment)
    a = []
    for m in range(moment+1):
        prior = sum((comb(m,j)*a[m-j] for j in range(1,m+1)),Q(0))
        a.append((Q(1)-prior)/2)
    return a[moment]


def zeta_negative_euler(moment: int) -> Q:
    """Zeta(-m) via analytic eta(s)=(1-2^(1-s))zeta(s); NOT divergent sum."""
    natural(moment)
    return eta_negative_euler(moment)/Q(1-2**(moment+1))


def prospective_even_zero(moment: int) -> bool:
    """Finite computational witness; proof from parity of e^t/(1+e^t)."""
    natural(moment, minimum=1)
    return zeta_negative_euler(2*moment) == 0


def negative_gamma_distribution_coefficients(order: int) -> tuple[int, ...]:
    """Distribution g_{-m}=(1+D)^m delta_0; coefficients of delta^(j).

    Laplace g_{-m}=(1+p)^m. This is a signed generalized distribution,
    not a normalized positive measure or physical negative travel time.
    """
    natural(order)
    return tuple(comb(order,j) for j in range(order+1))


def negative_gamma_laplace_symbol(order: int, p: Q) -> Q:
    """Laplace action of distribution on exp(-p t), evaluated exactly."""
    natural(order)
    if type(p) not in (int,Q) or p < 0:
        raise ValueError("nonnegative rational p required")
    return sum((Q(c)*Q(p)**j for j,c in enumerate(
        negative_gamma_distribution_coefficients(order))),Q(0))


def gamma_inverse_volume_identity(order: int, p: Q) -> Q:
    """g_m*g_{-m}=delta_0 in Laplace coordinate, hence symbol 1."""
    natural(order)
    if type(p) not in (int,Q) or p < 0:
        raise ValueError("nonnegative rational p required")
    forward=(Q(1)/(Q(1)+Q(p)))**order
    inverse=negative_gamma_laplace_symbol(order,p)
    return forward*inverse


def noninteger_crt_thread(depth: int) -> tuple[int, ...]:
    """Profinite CRT phantom: 2-adic component =1, every odd p-adic =0.

    Each finite L_N coordinate has a positive representative, but no single
    ordinary integer has all the coordinates. Hence no finite suspension
    path from the origin reaches this transverse point.
    """
    natural(depth, minimum=1)
    vals = []
    for n in range(1,depth+1):
        length = lcm_clock(n)
        power2 = length & -length
        odd = length // power2
        if power2 == 1:
            residue = 0
        else:
            residue = (odd * pow(odd,-1,power2)) % length
        vals.append(residue)
    assert consistent_thread(tuple(vals))
    return tuple(vals)
