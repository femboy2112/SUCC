"""Exact, source-faithful finite probes for the SUCC selected-boundary slip theorem.

Do not treat finite probes as proofs of the asymptotic theorem in THEOREMS.md.
All BBP states and their lag-phase turns are rational Fractions.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd

DELTAS = (1, 4, 5, 6)
COEFFS = (4, -2, -1, -1)


def forcing(n: int, coeffs=COEFFS) -> F:
    if n < 1:
        raise ValueError('n>=1 required')
    return sum((F(c, 8 * (n-1) + d) for c, d in zip(coeffs, DELTAS)), F())


def states(stop: int, seed=F(0), coeffs=COEFFS):
    """U_0,...,U_stop; exact Fractions."""
    vals = [F(seed)]
    for n in range(1, stop + 1):
        vals.append(16 * vals[-1] + forcing(n, coeffs))
    return vals


def dist_to_integer(z) -> F:
    z = F(z)
    t = z - (z.numerator // z.denominator)
    return min(t, 1-t)


def slip_distances(start: int, stop: int, h: int=1, seed=F(0)):
    if start < 1 or stop < start or not h:
        raise ValueError('1<=start<=stop, h!=0')
    u = states(stop+1, seed=seed)
    return [dist_to_integer(h * (u[n+1] - u[n]))
            for n in range(start, stop+1)]


def slip_stats(start: int, stop: int, h: int=1, delta=F(1,20)):
    distances = slip_distances(start, stop, h)
    good = [(start+i,d) for i,d in enumerate(distances) if d >= delta]
    longest = 0
    current = 0
    for d in distances:
        if d < delta:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return {'start':start,'stop':stop,'h':h,'threshold':str(delta),
            'slips':len(good),'longest_coherent_run':longest,
            'first_slips':[i for i,_ in good[:12]],
            'min_distance':float(min(distances)),
            'max_distance':float(max(distances))}


def forced_approximation(q: int, initial_residual: F, run_length: int,
                         max_radius=F(1,18)):
    """Arithmetic lemma: if all signed residues at 16^j*x have abs<max_radius,
    they must be 16^j times the first residue. This does not assume pi.
    Input q is an irrelevant label of the rational denominator under study.
    """
    if 17*max_radius >= 1 or run_length<1:
        raise ValueError('radius must be <1/17 and length >=1')
    eps = F(initial_residual)
    values = []
    for _ in range(run_length):
        vals = eps - (eps.numerator // eps.denominator)
        signed = vals if vals <= F(1,2) else vals-1
        if abs(signed) >= max_radius:
            return {'all_near':False, 'length':len(values), 'values':values}
        values.append(signed)
        eps *= 16
    return {'all_near':True, 'length':len(values), 'values':values,
            'first_residual_bound':max_radius * F(1,16**(run_length-1))}


def rational_phase_window(alpha: F, start: int, length: int, h=1):
    """Model-only pure-radix lag distances at rational alpha (not pi)."""
    alpha = F(alpha)
    if start<1 or length<1: raise ValueError('positive start and length')
    return [dist_to_integer(15*h*(16**(n-1))*alpha)
            for n in range(start,start+length)]


if __name__ == '__main__':
    for h in (1,3,7):
        print(slip_stats(1,256,h))
