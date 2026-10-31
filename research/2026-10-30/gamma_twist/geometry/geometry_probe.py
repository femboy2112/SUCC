"""Exact finite instruments for the Gamma geometry research dossier.

Authentic source is immutable. Mutants are explicitly named argument values.
No function here asserts normality or an infinite-horizon selected saving.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

AUTH = ((0, F(4)), (3, F(-2)), (4, F(-1)), (5, F(-1)))


def kernel_mutant(order: int, epsilon=F(1)):
    """Q_auth + epsilon*(1-exp(-x))**order, positive for epsilon>=0."""
    if order < 1 or epsilon < 0:
        raise ValueError("positive integer order and nonnegative epsilon required")
    c = dict(AUTH)
    for j in range(order + 1):
        c[j] = c.get(j, F(0)) + epsilon * (-1)**j * comb(order, j)
    return tuple(sorted((j, x) for j, x in c.items() if x))


def age_mutant(t):
    return tuple((d, c + t * e) for (d, c), e in zip(AUTH, (1, -3, 1, 1)))


def source(a, coeffs=AUTH):
    if a <= 0:
        raise ValueError("positive source clock required")
    return sum((c / (F(a) + d) for d, c in coeffs), F(0))


def forcing(n, coeffs=AUTH):
    if n < 1:
        raise ValueError("source time n>=1 required")
    return source(8*n-7, coeffs)


def source_jets(coeffs=AUTH, order=4):
    return [sum((c * (-d)**j for d, c in coeffs), F(0)) for j in range(order+1)]


def orbit(count, seed=F(0), coeffs=AUTH):
    out = [F(seed)]
    for n in range(1, count+1):
        out.append(16*out[-1] + forcing(n, coeffs))
    return out


def phase_and_carry(count, seed=F(0), coeffs=AUTH):
    x = F(seed) % 1
    rows = []
    for n in range(1, count+1):
        raw = 16*x + forcing(n, coeffs)
        carry = raw.numerator // raw.denominator
        x = raw - carry
        rows.append((x, carry))
    return rows


def endpoint_weights(n, coeffs=AUTH):
    """Finite-difference Laplace route; oracle uses Beta rising products."""
    a = 8*n-7
    norm = source(a, coeffs)
    if n < 1 or norm <= 0:
        raise ValueError("positive normalized source required")
    return [F(comb(n,j))*sum(((-1)**ell * comb(j,ell) *
        source(a+8*(n-j+ell), coeffs) for ell in range(j+1)), F(0))/norm
        for j in range(n+1)]


def pgf(weights, z):
    out = F(0)
    for c in reversed(weights):
        out = out*z + c
    return out


def root_interval(n, coeffs=AUTH, bits=72):
    weights = endpoint_weights(n, coeffs)
    mean = sum((j*p for j,p in enumerate(weights)), F(0))
    if mean <= 1:
        return (F(1), F(1))
    lo, hi = F(0), F(1,2)
    while pgf(weights, hi) >= hi:
        hi = (hi+1)/2
    for _ in range(bits):
        mid = (lo+hi)/2
        if pgf(weights, mid) > mid:
            lo = mid
        else:
            hi = mid
    assert pgf(weights, lo) >= lo and pgf(weights, hi) <= hi
    return lo, hi


def pgf_coefficients(z, coeffs=AUTH):
    """0th, 1/n, 1/n^2 coefficients, rank-two finite exponential kernels."""
    jets = source_jets(coeffs, 3)
    if jets[0] != 0 or jets[1] <= 0:
        raise ValueError("rank-two source required")
    c1, c2, c3 = jets[1], jets[2]/2, jets[3]/6
    A = (7+c2/c1)/8
    B = (F(49,2)+7*c2/c1+c3/c1)/64
    d = 2-z
    D = z*(1-z)/2
    E = -z*(1-z)*(2*z-1)/6
    zero = d**-2
    n1 = 2*A/d**3 + 6*D/d**4
    n2 = 6*B/d**4 + 24*(A*D+E)/d**5 + 60*D**2/d**6
    return zero, n1-2*A*zero, n2-2*A*n1+(4*A*A-6*B)*zero


def walsh(mask, label):
    return 1 if (mask & (label % 16)).bit_count() % 2 == 0 else -1


def carry_grade_tensor(n, coeffs=AUTH, seed=F(0)):
    weights = endpoint_weights(n, coeffs)
    rows = phase_and_carry(2*n, seed, coeffs)
    tensor = [[F(0) for _ in range(16)] for _ in range(16)]
    for j,p in enumerate(weights):
        # Arithmetic time n+j, independent of auxiliary posterior grade j.
        carry = rows[n+j-1][1]
        for grade_mask in range(16):
            for carry_mask in range(16):
                tensor[grade_mask][carry_mask] += p*walsh(grade_mask,j)*walsh(carry_mask,carry)
    return tensor


def circle_unit(t):
    """Rational parametrization of a unit complex number as (real,imag)."""
    t=F(t)
    return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def positive_lift_identity(weights, points, target=(F(1), F(0))):
    if any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError("probability weights required")
    if target[0]**2+target[1]**2 != 1:
        raise ValueError("unit target required")
    if any(x*x+y*y != 1 for x,y in points):
        raise ValueError("unit observables required")
    mean = tuple(sum((w*z[k] for w,z in zip(weights,points)), F(0)) for k in (0,1))
    dispersion = sum((w*((z[0]-target[0])**2+(z[1]-target[1])**2)
                      for w,z in zip(weights,points)),F(0))
    exact = 2*(1-mean[0]*target[0]-mean[1]*target[1])
    assert dispersion == exact
    variance = 1-mean[0]**2-mean[1]**2
    assert variance >= 0
    return mean, dispersion, variance


def affine_commutator(i,j,x,coeffs=AUTH):
    """F_i F_j F_i^-1 F_j^-1 on the real lift, no circle quotient."""
    a,b=forcing(i,coeffs),forcing(j,coeffs)
    z=(x-b)/16
    z=(z-a)/16
    z=16*z+b
    z=16*z+a
    return z


def exact_payload():
    holdouts=(17,31,53,89)
    root_rows=[]
    for n in holdouts:
        for label,c in (("authentic",AUTH),("cubic_e1",kernel_mutant(3)),
                        ("cubic_e5",kernel_mutant(3,F(5))),("quartic_e1",kernel_mutant(4))):
            lo,hi=root_interval(n,c,bits=64)
            root_rows.append(dict(n=n,source=label,lower=str(lo),upper=str(hi)))
    tensors={}
    for n in (3,7,17):
        tensors[str(n)]=[[str(x) for x in row] for row in carry_grade_tensor(n)]
    cocycles=[]
    for i,j in ((1,2),(3,7),(17,31),(53,89)):
        delta=15*(forcing(j)-forcing(i))
        for seed in (F(0),F(1,16),F(5,31),F(-7,11)):
            assert affine_commutator(i,j,seed)-seed==delta
        cocycles.append(dict(i=i,j=j,translation=str(delta),seed_trials=4))
    lift_rows=[]
    for t in (F(0),F(1,11),F(1,3),F(1),F(3)):
        mean,disp,var=positive_lift_identity((F(1,2),F(1,2)),(circle_unit(t),circle_unit(-t)))
        lift_rows.append(dict(t=str(t),mean=list(map(str,mean)),dispersion=str(disp),variance=str(var)))
    # Exact factorial four cells: positive source mutation and seed change are
    # separately toggleable; the positive endpoint law ignores the seed.
    source_cells={name:{"source_at_17":str(forcing(17,c)),
                       "q17_zero":str(endpoint_weights(17,c)[0]),
                       "jets":list(map(str,source_jets(c)))}
                  for name,c in (("authentic",AUTH),("age_t128",age_mutant(128)),
                                 ("cubic_e1",kernel_mutant(3)),("quartic_e1",kernel_mutant(4)))}
    return dict(status="PASS",authority="exact finite calibration, paper proofs separate",
                root_enclosures=root_rows,carry_grade_walsh_tensors=tensors,
                affine_commutators=cocycles,positive_lift_controls=lift_rows,
                source_controls=source_cells)


if __name__ == '__main__':
    payload=exact_payload()
    print(json.dumps(payload,indent=2))
