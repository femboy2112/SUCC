"""Five-channel Jacobian observatory: exact BBP source, local rank repair,
objective/conditional phase agreement and preregistered rational R0 probes.

Research-only: no asymptotic signed cancellation, R0 or normality proved.
Standard-library arithmetic. Run this file to print an auditable finite receipt.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import cos, pi, sin

BETA = (7, 4, 3, 2)
AUTHENTIC_COEFFICIENTS = (4, -2, -1, -1)
FIBONACCI_TIMES = (55, 89, 144, 233)
REPAIRED_CHRONOLOGY = (55, 89, 144, 146, 147, 233)
PRIME_CHANNELS = (3, 5, 7, 11, 29)
# Locked before finite-shell results are inspected. No response-adaptive cherry-picking.
WEYL_PROBES = ((1, 1), (4, 11), (6, 7))  # (ell, h)
SIGNED_FREQUENCIES = (1, 2, 15)
SHIFT_BANK = (0, 1, 5, 6, 21, 22, 55, 56)


def forcing(n: int, coefficients=AUTHENTIC_COEFFICIENTS) -> Fraction:
    if n < 1:
        raise ValueError("forcing clocks must be >= 1")
    return sum((Fraction(a, 8*n-b) for a, b in zip(coefficients, BETA)), Fraction())


def zero_seed_history(last_n: int, coefficients=AUTHENTIC_COEFFICIENTS) -> list[Fraction]:
    u = [Fraction(0)]
    for n in range(1, last_n + 1):
        u.append(16*u[-1] + forcing(n, coefficients))
    return u


def finite_completed_seed(depth: int, coefficients=AUTHENTIC_COEFFICIENTS) -> Fraction:
    return sum((forcing(n, coefficients) * Fraction(1, 16**n)
                for n in range(1, depth+1)), Fraction())


def source_row(n: int) -> tuple[Fraction, ...]:
    return tuple(Fraction(1, 8*n-b) for b in BETA)


def det_exact(matrix) -> Fraction:
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("square matrix required")
    d = Fraction(1)
    for j in range(n):
        piv = next((i for i in range(j, n) if a[i][j]), None)
        if piv is None:
            return Fraction(0)
        if piv != j:
            a[piv], a[j] = a[j], a[piv]
            d = -d
        v = a[j][j]
        d *= v
        for i in range(j+1, n):
            z = a[i][j] / v
            for k in range(j+1, n):
                a[i][k] -= z*a[j][k]
            a[i][j] = Fraction(0)
    return d


def cauchy_det(times) -> Fraction:
    times = tuple(times)
    if len(times) != 4 or len(set(times)) != 4:
        raise ValueError("exactly four distinct clocks required")
    top = 1
    for i, j in combinations(range(4), 2):
        top *= 8*(times[j] - times[i]) * (BETA[i] - BETA[j])
    bottom = 1
    for t in times:
        for b in BETA:
            bottom *= (8*t - b)
    return Fraction(top, bottom)


def five_channel_jacobian(times, depth: int = 16):
    times = tuple(times)
    if len(times) != 4:
        raise ValueError("four source innovations plus one anchor")
    rows = [source_row(t) + (Fraction(0),) for t in times]
    anchor = tuple(sum((Fraction(1, 16**n*(8*n-b))
                        for n in range(1, depth+1)), Fraction()) for b in BETA)
    return rows + [anchor + (Fraction(1),)]


def vp_nonzero(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("valuation infinity for zero")
    n = abs(n)
    k = 0
    while n % p == 0:
        k += 1
        n //= p
    return k


def vp_fraction(x: Fraction, p: int) -> int:
    if not x:
        raise ValueError("zero valuation not finite")
    return vp_nonzero(x.numerator, p) - vp_nonzero(x.denominator, p)


def normalized_prime_row(n: int, p: int):
    """Return minimal p^scale clearing row's negative valuations, mod-p row.

    Scale is recorded, never passed off as an unscaled p-adic measurement.
    """
    row = source_row(n)
    scale = max(0, -min(vp_fraction(x, p) for x in row))
    integral = [x*p**scale for x in row]
    assert all(x.denominator % p != 0 for x in integral)
    reduced = tuple(x.numerator*pow(x.denominator, -1, p) % p for x in integral)
    return scale, reduced


def rank_modp(rows, p: int) -> int:
    a = [[x % p for x in row] for row in rows]
    if not a:
        return 0
    n, m = len(a), len(a[0]); r = 0
    for col in range(m):
        piv = next((i for i in range(r, n) if a[i][col]), None)
        if piv is None:
            continue
        a[piv], a[r] = a[r], a[piv]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x*inv) % p for x in a[r]]
        for i in range(n):
            if i != r:
                z = a[i][col]
                a[i] = [(x - z*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def prime_schedule_report(times, primes=PRIME_CHANNELS):
    report = {}
    for p in primes:
        rows = [normalized_prime_row(t, p) for t in times]
        report[p] = {"rank": rank_modp([r for _, r in rows], p),
                     "scales": tuple(s for s, _ in rows),
                     "rows": tuple(r for _, r in rows)}
    return report


def admissible_next_clock(history, prime: int, candidates):
    """A predeclared, rank-only policy. Does not read any actual Weyl phase.

    Candidate must advance chronological time; observations are never deleted.
    """
    old_rank = prime_schedule_report(history, (prime,))[prime]["rank"]
    for n in candidates:
        if n <= history[-1]:
            continue
        new_rank = prime_schedule_report(tuple(history)+(n,), (prime,))[prime]["rank"]
        if new_rank > old_rank:
            return n
    return None


def fracmod1(x: Fraction) -> Fraction:
    return x - (x.numerator // x.denominator)


def phase(x: Fraction, h=1) -> complex:
    theta = float(fracmod1(h*x))
    return complex(cos(2*pi*theta), sin(2*pi*theta))


def shell_phase_partition(states, B: int, h: int = 1, bins: int = 16):
    """Finite rational-source proxy for the objective observer partition.

    Group assignment is based only on U_n mod 1; relative phase is frequency h.
    """
    groups = defaultdict(list)
    for n in range(B, 2*B):
        theta = fracmod1(states[n])
        a = (bins*theta.numerator) // theta.denominator
        groups[a].append(phase(states[n], h))
    m = {a: sum(z)/len(z) for a, z in groups.items()}
    weights = {a: len(z)/B for a, z in groups.items()}
    W = sum(weights[a]*m[a] for a in m)
    within = sum(weights[a]*(1-abs(m[a])**2) for a in m)
    between = sum(weights[a]*weights[b]*abs(m[a]-m[b])**2
                  for a, b in combinations(m, 2))
    return {"W": W, "within": within, "between": between,
            "variance": 1-abs(W)**2,
            "bins_nonempty": len(groups),
            "min_local_coherence": min(abs(x) for x in m.values()),
            "weights": weights, "means": m}


def uniform_grid_control(size=32, h=1):
    """All local cells perfectly locked, objective phase mean cancels for h<size."""
    z = [complex(cos(2*pi*h*j/size), sin(2*pi*h*j/size)) for j in range(size)]
    W = sum(z)/size
    between = sum(abs(z[i]-z[j])**2 for i in range(size) for j in range(i+1,size))/size**2
    return W, between


def torus_sq(x: Fraction) -> Fraction:
    theta = fracmod1(x)
    d = min(theta, 1-theta)
    return d*d


def holonomy(states, B: int, ell: int, h: int) -> Fraction:
    """Fully rational source-corrected R0 gate, no completed pi digits needed."""
    K = h*(16**ell-1)
    assert len(states) > 2*B+ell-1
    for n in range(B, 2*B):
        drift = sum((16**(ell-j)*forcing(n+j) for j in range(1,ell+1)), Fraction())
        assert states[n+ell]-states[n]-drift == (16**ell-1)*states[n]
    return sum((torus_sq(K*states[n]) for n in range(B,2*B)), Fraction())/B


def r0_lower_certificate(states, B: int, ell: int, h: int):
    H = holonomy(states, B, ell, h)
    K = h*(16**ell-1)
    correction = (2*pi/15)*float(forcing(B+1))
    return H, 8*float(H)/(K*K)-correction


def source_tail_bound(n):
    """T_n < r(n+1)/15; source proof is the positive monotone BBP kernel."""
    return forcing(n+1)/15



def signed_lag(states, B: int, ell: int, h: int) -> complex:
    """Genuine real-circle signed BBP relative phase at a fixed source lag."""
    assert len(states) >= 2*B + ell
    return sum((phase(states[n+ell]-states[n], h)
                for n in range(B, 2*B)), complex(0))/B


def signed_shift_gram(states, B: int, h: int, shifts=SHIFT_BANK):
    """Signed, chronological Gram energy, with all relative cross terms kept."""
    assert shifts[0] == 0 and tuple(sorted(set(shifts))) == tuple(shifts)
    assert len(states) >= 2*B + shifts[-1]
    m = len(shifts)
    wave = [sum((phase(states[n+t],h) for t in shifts),complex(0))/m
            for n in range(B,2*B)]
    energy = sum(abs(z)**2 for z in wave)/B
    signed_cross = sum((sum((phase(states[n+v]-states[n+u],h)
                             for n in range(B,2*B)),complex(0)).real/B
                        for u,v in combinations(shifts,2)))
    reconstructed = 1/m + 2*signed_cross/(m*m)
    return energy,reconstructed


def shifted_weyl_upper(states, B: int, h: int, shifts=SHIFT_BANK) -> float:
    """Source-certified upper bound on the genuine completed |W_B^pi(h)|.

    This is conditional on the actual BBP finite-source theorem T_n<1/(64n^2).
    No mixing assertion follows from the inequality itself.
    """
    energy,_ = signed_shift_gram(states,B,h,shifts)
    return energy**0.5 + 2*shifts[-1]/B + pi*abs(h)/(32*B**2)


def truncated_authentic_tail(n: int, depth=16) -> Fraction:
    """The wrong-seed, same-forcing state is -T_n, here approximated rationally."""
    return sum((Fraction(1,16**j)*forcing(n+j)
                for j in range(1,depth+1)),Fraction())


def locked_same_forcing_gram(B: int, h=1, shifts=SHIFT_BANK, depth=16) -> float:
    """Numerical control for exact wrong seed s*=-pi/16, whose state is -T_n."""
    top = 2*B + shifts[-1]
    faux = [-truncated_authentic_tail(n,depth) for n in range(top+1)]
    return signed_shift_gram(faux,B,h,shifts)[0]


def run_receipt():
    initial = prime_schedule_report(FIBONACCI_TIMES)
    repaired = prime_schedule_report(REPAIRED_CHRONOLOGY)
    assert all(repaired[p]["rank"] == 4 for p in PRIME_CHANNELS)
    assert initial[3]["rank"] == initial[11]["rank"] == 3
    assert admissible_next_clock((55,89,144), 3, (145,146,147)) == 146
    assert admissible_next_clock((55,89,144,146), 11, (147,148)) == 147
    ca = det_exact([source_row(n) for n in FIBONACCI_TIMES]); cb = cauchy_det(FIBONACCI_TIMES)
    assert ca == cb and ca != 0
    assert det_exact(five_channel_jacobian(FIBONACCI_TIMES, 16)) == ca
    states = zero_seed_history(2*256 + SHIFT_BANK[-1])
    print('Baseline ranks:', {p:initial[p]['rank'] for p in PRIME_CHANNELS})
    print('Repaired ranks:', {p:repaired[p]['rank'] for p in PRIME_CHANNELS})
    print('Maximum precision scales:', {p:max(repaired[p]['scales']) for p in PRIME_CHANNELS})
    print('Five-channel Jacobian determinant equals source Cauchy determinant: PASS')
    for B in (64, 128, 256):
        report = shell_phase_partition(states, B, bins=16)
        assert abs(report['within'] + report['between'] - report['variance']) < 1e-12
        assert report['min_local_coherence'] >= cos(pi/16)-1e-12
        print('Shell', B, 'rational BBP |W_1|', round(abs(report['W']),6),
              'within',round(report['within'],6),'between',round(report['between'],6),
              'local_min',round(report['min_local_coherence'],6))
        for h in SIGNED_FREQUENCIES:
            E, E_cross = signed_shift_gram(states, B, h)
            assert abs(E-E_cross) < 1e-12
            print('  signed Gram h',h,'energy',round(E,6),'upper completed Weyl',round(shifted_weyl_upper(states,B,h),6))
        for ell,h in WEYL_PROBES:
            H, lb = r0_lower_certificate(states, B, ell, h)
            assert Fraction(0) <= H <= Fraction(1,4)
            print('  gate', (ell,h), 'H',round(float(H),6),'R0_lb',round(lb,12))
    W,D = uniform_grid_control(32,1)
    assert abs(W) < 1e-12 and abs(D-1) < 1e-12
    print('Uniform root-grid: all observers locally locked, global W=0: PASS')
    print('Same-forcing wrong-seed Gram B=128, h=1:',round(locked_same_forcing_gram(128),6))
    print('Finite data NOT a proof of any asymptotic BBP bound.')


if __name__ == '__main__':
    run_receipt()
