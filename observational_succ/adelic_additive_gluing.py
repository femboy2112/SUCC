"""Exact additive adelic phases and source-scale holonomy for the original BBP.

Research instrument only: all-place phase reconstruction is classical and
DOES NOT imply base-16 normality of pi or any selected signed Fourier decay.
The original source and literal zero seed are imported, never modified.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt, lcm

from observational_succ.duck_bbp import forcing


def _nat(x: int, name: str, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return x


def primes_upto(limit: int) -> tuple[int, ...]:
    _nat(limit, "limit")
    if limit < 2:
        return ()
    composite = bytearray(limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if not composite[p]:
            for n in range(p * p, limit + 1, p):
                composite[n] = 1
    return tuple(i for i in range(2, limit + 1) if not composite[i])


def factor_with_bound(denominator: int, maximum_prime: int) -> dict[int, int]:
    """Prove exact factor support; rejects an insufficient declared cutoff."""
    _nat(denominator, "denominator", 1)
    _nat(maximum_prime, "maximum_prime", 2)
    remaining = denominator
    factors: dict[int, int] = {}
    for p in primes_upto(maximum_prime):
        if remaining % p == 0:
            e = 0
            while remaining % p == 0:
                remaining //= p
                e += 1
            factors[p] = e
        if remaining == 1:
            break
    if remaining != 1:
        raise ValueError("denominator has prime support outside declared source cutoff")
    return factors


def local_additive_fraction(value: Fraction, prime: int) -> Fraction:
    """The standard Q_p fractional part of rational value, in [0,1)."""
    if not isinstance(value, Fraction):
        raise TypeError("an exact rational Fraction is required")
    _nat(prime, "prime", 2)
    if prime not in primes_upto(prime):
        raise ValueError("prime argument is composite")
    d = value.denominator
    pe = 1
    while d % (pe * prime) == 0:
        pe *= prime
    if pe == 1:
        return Fraction(0)
    unit = d // pe
    residue = (value.numerator * pow(unit, -1, pe)) % pe
    return Fraction(residue, pe)


def additive_prime_parts(value: Fraction, maximum_prime: int) -> dict[int, Fraction]:
    """All nontrivial p-adic fractions; factorization certified by cutoff."""
    if not isinstance(value, Fraction):
        raise TypeError("exact Fraction required")
    return {p: local_additive_fraction(value, p)
            for p in factor_with_bound(value.denominator, maximum_prime)}


def real_phase_from_all_places(value: Fraction, maximum_prime: int) -> Fraction:
    """Classical additive adelic product formula, EXACT in Q/Z.

    Returns sum_p {value}_p mod1, equal to value mod1.
    No exponential or floating-point evaluation is used.
    """
    return sum(additive_prime_parts(value, maximum_prime).values(), Fraction()) % 1


def orbit_states(horizon: int) -> tuple[Fraction, ...]:
    """Original zero-selected unwrapped rational BBP states."""
    _nat(horizon, "horizon")
    states = [Fraction(0)]
    for n in range(1, horizon + 1):
        states.append(16 * states[-1] + forcing(n))
    return tuple(states)


def original_phase_parts(n: int, *, states: tuple[Fraction, ...] | None = None) -> dict[int, Fraction]:
    """All p-adic additive phase factors of U_n; d_n is odd, p<=8n-3."""
    _nat(n, "n", 1)
    u = orbit_states(n)[-1] if states is None else states[n]
    return additive_prime_parts(u, 8*n - 3)


def finite_phase_cocycle(n: int, prime: int, *, states: tuple[Fraction, ...] | None = None) -> tuple[Fraction, Fraction]:
    """Compatibility of p-adic additive character with ×16 and frozen forcing.

    Returns equal elements of Q/Z, not an assertion of probabilistic mixing.
    """
    _nat(n, "n")
    states = orbit_states(n + 1) if states is None else states
    lhs = local_additive_fraction(states[n + 1], prime)
    rhs = (16*local_additive_fraction(states[n],prime)
           +local_additive_fraction(forcing(n+1),prime))%1
    return lhs, rhs


def source_defect(start: int, steps: int) -> Fraction:
    """Exact F_(start,steps): identical to ASG-01 of PR #556."""
    _nat(start, "start")
    _nat(steps, "steps", 1)
    return sum((16**(steps-j)*forcing(start+j)
                for j in range(1,steps+1)), Fraction())


def holonomy_exponent(epoch: int, steps: int) -> Fraction:
    """Unwrapped exponent Theta_(A,k) = sum_(A<=n<2A) F_(n,k)."""
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return sum((source_defect(n, steps) for n in range(epoch,2*epoch)), Fraction())


def holonomy_center(epoch: int, steps: int) -> Fraction:
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return Fraction(16**steps-1,128*epoch)


def holonomy_error_bound(epoch: int, steps: int) -> Fraction:
    """Absolute |Theta-(16^k-1)/(128 A)| <= 14 c_k/A², all A,k>=1.

    Derived from ASG-02 uniform 298/(25n²) bound and the integral test.
    """
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return Fraction(7*(16**steps-1),32*epoch*epoch)


def critical_steps(epoch: int) -> int:
    """Natural first open scale k=max(1,ceil(log_16(A))); no floats."""
    _nat(epoch, "epoch", 2)
    k = 0
    pow16 = 1
    while pow16 < epoch:
        pow16 *= 16
        k += 1
    return max(1,k)


def critical_arc_halfwidth(minimum_epoch: int) -> Fraction:
    """All Theta_(A,ceil log16 A) for A>=M lie in [17/256 +/- width].

    For M>=32, width <1/4 turn, so ANY convex average of their
    phase characters has strictly positive rotated real part.
    """
    _nat(minimum_epoch, "minimum_epoch", 32)
    return Fraction(15,256) + Fraction(449,128*minimum_epoch)


def coboundary(n: int) -> Fraction:
    """Source-preserving null g_n from draft #555; g_0=0."""
    _nat(n, "n")
    return Fraction(n,257*(2*n+1)**3)


def coboundary_defect_delta(epoch: int, steps: int) -> Fraction:
    """Theta' - Theta for source r'=r+g_n-16g_(n-1)."""
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return sum((coboundary(n+steps)-16**steps*coboundary(n)
                for n in range(epoch,2*epoch)), Fraction())


def coboundary_delta_center(epoch: int, steps: int) -> Fraction:
    """Theta' - Theta = -16^k/(4112 A) + explicit error."""
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return -Fraction(16**steps,4112*epoch)


def coboundary_delta_error(epoch: int, steps: int) -> Fraction:
    _nat(epoch, "epoch", 1)
    _nat(steps, "steps", 1)
    return Fraction(9*16**steps,8224*epoch*epoch) + Fraction(1,2056*epoch)


def source_prime_injection(prime: int, n: int) -> int:
    """J_(p,n) = p*r(n) mod p provided p*r(n) is p-integral.

    Only valid before any p² pole. Detects each real original pole birth.
    """
    _nat(prime, "prime", 2)
    _nat(n, "n", 1)
    if prime not in primes_upto(prime):
        raise ValueError("prime required")
    q = prime * forcing(n)
    if q.denominator % prime == 0:
        raise ValueError("p² pole or nonintegral source at the requested time")
    return (q.numerator * pow(q.denominator,-1,prime)) % prime


def source_p_history(prime: int, horizon: int) -> tuple[int, ...]:
    """First-shell p-primary labels C_p(n) on exact original source."""
    _nat(horizon, "horizon")
    values = [0]
    for n in range(1,horizon+1):
        values.append((16*values[-1]+source_prime_injection(prime,n))%prime)
    return tuple(values)


def compensated_real_driver(n: int, prime: int) -> Fraction:
    """r(n) - J_(p,n)/p, the exact analytic complement driver."""
    return forcing(n)-Fraction(source_prime_injection(prime,n),prime)


def balanced_complement_cocycle(n: int, prime: int, *, states: tuple[Fraction, ...] | None=None) -> tuple[Fraction, Fraction]:
    """In Q/Z, b_(n+1) = b_n^16 e(h (r-J/p)) for h=1.

    b_n is e(U_n-C_p(n)/p); for h integer multiply both phases by h.
    """
    states = orbit_states(n+1) if states is None else states
    C = source_p_history(prime,n+1)
    lhs=(states[n+1]-Fraction(C[n+1],prime))%1
    rhs=(16*(states[n]-Fraction(C[n],prime)) +compensated_real_driver(n+1,prime))%1
    return lhs,rhs


def epoch_conductor_and_support(epoch: int) -> tuple[int, int, int]:
    """CRT observer Q=lcm den(U_n), #distinct residues, #observations."""
    _nat(epoch, "epoch", 1)
    states=orbit_states(2*epoch-1)
    sub=states[epoch:2*epoch]
    q=lcm(*(u.denominator for u in sub))
    support=len(set((u%1 for u in sub)))
    return q,support,epoch


def exact_crt_tv_from_haar(epoch: int) -> Fraction:
    """When Q>=A, exact TV is 1 - (#distinct)/Q, far from Haar."""
    q,s,A=epoch_conductor_and_support(epoch)
    if q<A:
        raise ValueError("Q>=A required for closed TV formula")
    return 1-Fraction(s,q)


def full_crt_spectral_energy(epoch: int) -> Fraction:
    """Exact all-character Parseval excess over the common CRT conductor.

    sum_(h=1)^(Q-1) |(1/A)sum_n e(h*U_n)|²
    = Q/A² * sum_(x modQ) count(x)² - 1 >= Q/A - 1.
    Computed by integer/rational multiplicities, without complex floats.
    Huge full-spectrum energy is compatible with fixed-h cancellation.
    """
    _nat(epoch, "epoch", 1)
    states=orbit_states(2*epoch-1)
    q=lcm(*(u.denominator for u in states[epoch:2*epoch]))
    counts: dict[int,int]={}
    for u in states[epoch:2*epoch]:
        address=int(q * (u%1))  # Q is multiple of every reduced denominator.
        if Fraction(address,1)!=q*(u%1):
            raise ArithmeticError("inexact common-conductor address")
        counts[address]=counts.get(address,0)+1
    return Fraction(q*sum(c*c for c in counts.values()),epoch*epoch)-1
