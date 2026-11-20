"""Source-typed exact rational arithmetic and declared observer instruments.

Research-only: original BBP forcing and literal zero seed remain invariant.
Neither Gaussian L2 norms nor p-adic valuations are physical energies.
No all-shell anti-lock assertion is made.
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, exp, isqrt, pi, sin, sqrt


def r(n: int) -> Fraction:
    if not isinstance(n, int) or n < 1:
        raise ValueError('clock n must be an integer >= 1')
    return (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
            - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))


def r_mutant(n: int) -> Fraction:
    """Matched-jet but SOURCE-INVALID Q* = Q + (1-t)^2."""
    if not isinstance(n, int) or n < 1:
        raise ValueError('clock n must be an integer >= 1')
    a = 8*n - 7
    return r(n) + Fraction(2, a*(a+1)*(a+2))


def prefix(M: int) -> Fraction:
    if not isinstance(M, int) or M < 0:
        raise ValueError('terminal M must be an integer >= 0')
    return sum((r(j)/16**j for j in range(1, M+1)), Fraction(0))


def state(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    if not isinstance(n, int) or n < 0:
        raise ValueError('clock n must be an integer >= 0')
    v = Fraction(seed)
    for j in range(1, n+1):
        v = 16*v + r(j)
    return v


def terminal_tail(n: int, M: int) -> Fraction:
    if not (isinstance(n, int) and isinstance(M, int) and 0 <= n <= M):
        raise ValueError('require integers 0 <= n <= M')
    return sum((r(j)/16**(j-n) for j in range(n+1, M+1)), Fraction(0))


def terminal_completed(n: int, M: int, seed: Fraction = Fraction(0)) -> Fraction:
    if not (isinstance(n, int) and isinstance(M, int) and 0 <= n <= M):
        raise ValueError('require integers 0 <= n <= M')
    return state(n, seed) + terminal_tail(n, M)


def primary(q: Fraction, p: int) -> Fraction:
    """Canonical p-primary component of q modulo Z, no factorization oracle.

    If p^k || denominator b, write b=p^k b' and choose
    c=a*(b')^{-1} mod p^k, then return c/p^k in [0,1).
    """
    q = Fraction(q)
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('p must be a prime >= 2')
    b = q.denominator
    m = 1
    while b % p == 0:
        m *= p
        b //= p
    if m == 1:
        return Fraction(0)
    return Fraction((q.numerator * pow(b, -1, m)) % m, m)


def prime_factors(n: int) -> tuple[int, ...]:
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return tuple(out)


def all_primary(q: Fraction) -> dict[int, Fraction]:
    q = Fraction(q)
    return {p: primary(q, p) for p in prime_factors(q.denominator)}


def fractional(q: Fraction) -> Fraction:
    q = Fraction(q)
    return Fraction(q.numerator % q.denominator, q.denominator)


def canonical_reassembly(q: Fraction) -> bool:
    return fractional(q - sum(all_primary(q).values(), Fraction(0))) == 0


def character(q: Fraction, h: int = 1) -> complex:
    t = float(fractional(Fraction(q) * h))
    return complex(cos(2*pi*t), sin(2*pi*t))


def signed_phase_split(q: Fraction, completed_addition: Fraction,
                       places: tuple[int, ...], h: int = 1) -> tuple[complex, complex]:
    """a: selected rational p-primary character. b: full complementary
    character including the terminal tail and (optionally) a seed shift.
    The returned product is exactly e(h*(q+completed_addition)), up to float
    rounding in the complex number representation.
    """
    selected = sum((primary(q, p) for p in places), Fraction(0))
    return character(selected, h), character(q-selected+Fraction(completed_addition), h)


def p2_clock(p: int) -> int:
    if type(p) is not int or p < 7 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('expected odd prime >= 7')
    return (p*p-1)//8


def v_p_fraction(q: Fraction, p: int) -> int:
    q = Fraction(q)
    if q == 0:
        raise ValueError('valuation at zero is infinite')
    a, b, v = abs(q.numerator), q.denominator, 0
    while a % p == 0:
        v += 1
        a //= p
    while b % p == 0:
        v -= 1
        b //= p
    return v


def residue_mod_p(q: Fraction, p: int) -> int:
    q = Fraction(q)
    if q.denominator % p == 0:
        raise ValueError('requires p-integral rational')
    return (q.numerator * pow(q.denominator, -1, p)) % p


def event_signature(p: int, mutant: bool = False) -> tuple[int, int]:
    """At clock (p^2+7)/8, return v_p(r) and residue p^2*r mod p."""
    n = p2_clock(p) + 1
    q = r_mutant(n) if mutant else r(n)
    return v_p_fraction(q, p), residue_mod_p(p*p*q, p)


def gaussian_displacement(theta: Fraction | float, lam: float = 1., H: int = 20) -> float:
    if lam <= 0 or H < 1:
        raise ValueError('lambda > 0 and H >= 1 required')
    t = float(theta % 1) if isinstance(theta, Fraction) else theta
    return 4*sum(exp(-lam*k*k)*(1-cos(2*pi*k*t)) for k in range(1, H+1))


def gaussian_form_defect(lam: float = 1., radix: int = 16, H: int = 30) -> float:
    """Exact L2-defect represented as a certified-convergent series,
    numerically truncated at H. Theta-independent for a point carrier.
    """
    if lam <= 0 or radix < 2 or H < 1:
        raise ValueError('lambda > 0, radix >= 2, H >= 1')
    return 2*sum((exp(-lam*k*k/2)-exp(-radix**2*lam*k*k/2))**2
                 for k in range(1, H+1))


def form_defect_small_width_coefficient(radix: int = 16) -> float:
    """S_lambda ~ sqrt(pi/lambda)*coefficient as lambda down to zero."""
    return 1 + 1/radix - 2*sqrt(2/(1+radix*radix))


def gaussian_signed_interference(u: Fraction, t: Fraction, lam: float = 1.,
                                 H: int = 20) -> tuple[float, float, float, float]:
    """Gaussian L2 ledger: completed, source, compensator, signed cross.
    For each k, v=(e(k*u)-1)+e(k*u)*(e(k*t)-1).
    """
    total = source = boundary = cross = 0.0
    for k in range(1, H+1):
        w = 2*exp(-lam*k*k)
        a = character(u, k)
        b = character(t, k)
        va = a-1
        vb = a*(b-1)
        total += w*abs(a*b-1)**2
        source += w*abs(va)**2
        boundary += w*abs(vb)**2
        cross += 2*w*(va*vb.conjugate()).real
    return total, source, boundary, cross


def shell_pulse_count(B: int) -> int:
    """Upper bound count: p^2 event clocks <= 2B, ignoring primality."""
    return isqrt(16*B+1)


def sparse_pulse_mass_upper(B: int, duration: int, observable_bound: float = 1.) -> float:
    """Conservative upper bound for a bounded witness supported during
    at most `duration` forward steps per prime-square clock <= 2B."""
    if B < 1 or duration < 0 or observable_bound < 0:
        raise ValueError('invalid bound inputs')
    return observable_bound*min(1., duration*shell_pulse_count(B)/B)


def feedback_history(s: int, policy, steps: int, actuated: bool = True) -> tuple[int, ...]:
    """Declared toy carrier; tests possibility, not physical realization."""
    hist = [s]
    for n in range(steps):
        action = policy(n, s)
        s = s + (action if actuated else 1)
        hist.append(s)
    return tuple(hist)


def rational_place_product(q: Fraction) -> Fraction:
    """Exact elementary product formula |q|_infty prod_p |q|_p=1.
    Not a physical energy conservation law. Intended for small rational tests.
    """
    q=Fraction(q)
    if q==0:
        raise ValueError('product formula requires q != 0')
    product=abs(q)
    for p in sorted(set(prime_factors(abs(q.numerator))) | set(prime_factors(q.denominator))):
        v=v_p_fraction(q,p)
        product *= Fraction(p**(-v),1) if v<0 else Fraction(1,p**v)
    return product
