"""Exact cofiber recurrence and certified source-only lag-energy minimization.

No selected cancellation is assumed. Integer interval trigonometry is imported
from the already pinned PR399 finite-circle instrument; arithmetic is direct.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
from math import isqrt

_path = Path(__file__).resolve().parents[2] / 'arithmetic_barrier' / 'finite_circle.py'
_spec = importlib.util.spec_from_file_location('inherited_finite_circle', _path)
fc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fc)

AUTH = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)


def forcing(n, coefficients=AUTH, offsets=OFFSETS):
    if n < 1:
        raise ValueError('n must be positive')
    return sum((F(c, 8*n-8+d) for c, d in zip(coefficients, offsets)), F())


def orbit(end, seed=F(), coefficients=AUTH, offsets=OFFSETS):
    values = [F(seed) % 1]
    for n in range(1, end+1):
        values.append((16*values[-1]+forcing(n, coefficients, offsets)) % 1)
    return values


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def order16(p):
    if not is_prime(p) or p == 2:
        raise ValueError('odd prime required')
    x, k = 16 % p, 1
    while x != 1:
        x, k = x*16 % p, k+1
    return k


def birth(p):
    if not is_prime(p) or p <= 5:
        raise ValueError('prime greater than 5 required')
    if p % 8 == 1:
        return (p+7)//8
    if p % 8 == 5:
        return (p+3)//8
    return (p+1)//4


def split_primary(q, p):
    """Return primary and complementary elements of Q/Z, both in [0,1)."""
    if not is_prime(p):
        raise ValueError('prime required')
    q = F(q) % 1
    denominator, power = q.denominator, 1
    while denominator % p == 0:
        denominator //= p
        power *= p
    a = q.numerator*pow(denominator, -1, power) % power if power > 1 else 0
    primary = F(a, power)
    complement = (q-primary) % 1
    assert complement.denominator % p
    return primary, complement


def projected_history(end, p, coefficients=AUTH):
    """Rebuild both histories from projected forcing, retaining zero seed."""
    primary = [F()]
    cofiber = [F()]
    for n in range(1, end+1):
        a, v = split_primary(forcing(n, coefficients), p)
        primary.append((16*primary[-1]+a) % 1)
        cofiber.append((16*cofiber[-1]+v) % 1)
    return primary, cofiber


def energy_interval(phases, h=1):
    """Unnormalized adjacent energy; exact integer interval endpoints."""
    low = high = 0
    for x, y in zip(phases, phases[1:]):
        (cl, ch), _ = fc.character(h*(y-x))
        low += fc.SCALE-ch
        high += fc.SCALE-cl
    return F(low, fc.SCALE), F(high, fc.SCALE)


def phase_energy_interval(turns):
    low = high = 0
    for turn in turns:
        (cl, ch), _ = fc.character(turn)
        low += fc.SCALE-ch
        high += fc.SCALE-cl
    return F(low, fc.SCALE), F(high, fc.SCALE)


def tail_interval(n, terms=32):
    partial = sum((forcing(n+j)/16**j for j in range(1, terms+1)), F())
    remainder = F(1, 16**terms*(8*(n+terms)+1)**2)
    return partial, partial+remainder


def tail_difference_interval(n, terms=32):
    # The omitted difference tail is positive and less than the omitted tail.
    partial = sum(((forcing(n+j)-forcing(n+j+1))/16**j
                   for j in range(1, terms+1)), F())
    remainder = F(1, 16**terms*(8*(n+terms)+1)**2)
    return partial, partial+remainder


def energy_of_intervals(turns):
    """Chord Lipschitz enclosure, used only for small Green remainder widths."""
    lo = hi = F()
    for a, b in turns:
        (cl, ch), _ = fc.character((a+b)/2)
        error = fc.PI_HI*(b-a)
        lo += 1-F(ch, fc.SCALE)-error
        hi += 1-F(cl, fc.SCALE)+error
    return max(F(), lo), hi


def minimum_energy_certificate(A, L, h=1, terms=32):
    """Rigorous enclosure of inf_s sum of L lag-one energies.

    The certificate proves small-branch unwrapping, then bounds the exact
    quadratic projection and Taylor error. No numerical optimizer is trusted.
    """
    if A < 1 or L < 2 or h == 0:
        raise ValueError('A>=1, L>=2, h nonzero required')
    h = abs(h)
    D = [(h*a, h*b) for a, b in (tail_difference_interval(n, terms)
                                for n in range(A, A+L))]
    coherent = energy_of_intervals(D)
    M = coherent[1]
    # Every centered minimizer phase satisfies u_j² <= M/8.
    # Thus |u_(j+1)-16u_j| < 1/2; the source difference is <1/2.
    max_source = max(abs(h*(forcing(n+2)-forcing(n+1)))
                     for n in range(A, A+L-1))
    unwrap = F(17**2, 8)*M < F(1, 4) and max_source < F(1, 2)
    if not unwrap:
        raise ValueError('small-branch criterion not certified')
    a = [F(1, 16**(L-1-j)) for j in range(L)]
    aa = sum((x*x for x in a), F())
    lo2 = sum((d[0]**2 for d in D), F())
    hi2 = sum((d[1]**2 for d in D), F())
    ad_lo = sum((x*d[0] for x, d in zip(a, D)), F())
    ad_hi = sum((x*d[1] for x, d in zip(a, D)), F())
    Qlo = max(F(), lo2-ad_hi**2/aa)
    Qhi = hi2-ad_lo**2/aa
    # Candidate tau comes from midpoint D, so this is a realizable orbit.
    tau = -(ad_lo+ad_hi)/(2*aa)
    candidate = [(d[0]+x*tau, d[1]+x*tau) for x, d in zip(a, D)]
    candidate_bound = energy_of_intervals(candidate)
    factor = 1-fc.PI_HI**2*M/24
    lower = max(F(), 2*fc.PI_LO**2*factor*Qlo)
    upper = candidate_bound[1]
    if lower > upper:
        raise AssertionError('inconsistent minimum enclosure')
    return {'A': A, 'L': L, 'h': h, 'terms': terms, 'unwrap': unwrap,
            'mean_minimum': (lower/L, upper/L),
            'mean_coherent': (coherent[0]/L, coherent[1]/L),
            'quadratic_minimum': (Qlo, Qhi), 'tau': tau,
            'asymptotic_reference': sum((F(1, n**6) for n in range(A, A+L)), F())/L,
            'max_source_difference': max_source}


def universal_floor_certificate(values, A, L, h=1):
    energy = energy_interval(values[A:A+L+1], h)
    source_turns = [h*(forcing(n+2)-forcing(n+1))
                    for n in range(A, A+L-1)]
    floor = phase_energy_interval(source_turns)
    return energy, (floor[0]/289, floor[1]/289)


def decimal_bracket(pair, digits=18):
    scale = 10**digits
    lo, hi = pair
    return [str(F((lo*scale).__floor__(), scale)),
            str(F((hi*scale).__ceil__(), scale))]


def rational_pair(pair):
    return [str(x) for x in pair]
