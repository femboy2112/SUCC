"""Source-specific critical-scale epoch Fejer energy, research-only.

No claim of pi normality. Full source is the original SUCC BBP four poles with U0=0.
"""
from __future__ import annotations
import cmath
import math
from fractions import Fraction


def original_r(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("integer source index >=1 required")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def combined_r(n: int) -> Fraction:
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def circle_states(N: int) -> tuple[Fraction, ...]:
    if type(N) is not int or N < 1:
        raise ValueError("N>=1 required")
    v = [Fraction(0)]
    for n in range(1, N):
        v.append((16*v[-1] + original_r(n)) % 1)
    return tuple(v)


def tail_interval(n: int, depth: int=20) -> tuple[Fraction,Fraction]:
    if n<1 or depth<0:
        raise ValueError("tail bound requires n>=1, depth>=0")
    lo = sum((Fraction(1,16**j)*original_r(n+j)
              for j in range(1,depth+1)), Fraction(0))
    hi = lo + Fraction(1,15*16**depth*(n+depth+1)**2)
    return lo,hi


def mean_tail_upper(A: int) -> Fraction:
    if A<1: raise ValueError("A>=1")
    return sum((Fraction(1,15*(n+1)**2) for n in range(A,2*A)),Fraction(0))/A


def hilbert_transport_bound(A: int, H: int) -> float:
    if A<1 or H<1: raise ValueError("A,H>=1")
    return (math.pi/(15*A*A))*math.sqrt(H*(H+1)*(H+2)/6)


def weight_square_sum(H: int) -> Fraction:
    return 2*sum((Fraction(H+1-h,H+1)*h*h for h in range(1,H+1)),Fraction(0))


def fourier_energy(pts: tuple[Fraction,...] | list[float], H: int) -> float:
    if not pts or H<1: raise ValueError("nonempty points and H>=1 required")
    N = len(pts)
    u = [float(t) for t in pts]
    ans = 1.0
    for h in range(1,H+1):
        w = 1-h/(H+1)
        c = sum((cmath.exp(2j*math.pi*h*x) for x in u),0j)/N
        ans += 2*w*abs(c)**2
    return ans


def epoch_pair_count(pts: tuple[Fraction,...], delta: Fraction) -> int:
    if not (0<=delta<=Fraction(1,2)):
        raise ValueError("delta must be in [0,1/2]")
    return sum(1 for a in pts for b in pts
               if min(abs(a-b), 1-abs(a-b))<=delta)


def window_epoch(A: int, depth: int=20) -> dict[str,float]:
    states = circle_states(2*A)[A:]
    completed = []
    for n,x in enumerate(states,start=A):
        lo,hi = tail_interval(n,depth)
        completed.append((x+(lo+hi)/2)%1)
    cx = fourier_energy(states,A)
    cz = fourier_energy(completed,A)
    observed = abs(math.sqrt(cz)-math.sqrt(cx))
    bound = hilbert_transport_bound(A,A)
    return dict(A=A,C_rational=cx,C_completed=cz,observed_hilbert_shift=observed,
                rigorous_upper=bound,pass_float_check=observed<=bound+1e-10,
                roundoff_not_certified=True)
