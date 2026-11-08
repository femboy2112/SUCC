"""Two-tone pin-bed: source-conditioned Fourier realization diagnostics.

Research-only. Exact Q(i) heterodyning and BBP rational plaquettes are sound
finite checks; analytic trigonometric floats are NOT proof certificates.
See research/2026-11-07/pinbed_yoneda_oscillators/ for derivations.
"""
from __future__ import annotations

import cmath
from fractions import Fraction
from math import cos, isfinite, pi, sin


def aperture_factor(a: float, h: int) -> complex:
    """Fourier coefficient of normalized modulated arc before mode shift."""
    if not isinstance(a, (float, int)) or not 0 < a < 1 or type(h) is not int:
        raise ValueError("require aperture 0<a<1 and integral harmonic")
    if h == 0:
        return 1 + 0j
    return cmath.exp(-1j*pi*h*a) * (sin(pi*h*a)/(pi*h*a))


def mode_vector(a: float, h: int, coefficient: complex) -> tuple[complex, complex]:
    """Two coherently referenced output modes at harmonic h!=0."""
    if type(h) is not int or h == 0:
        raise ValueError("centered surface has zero mode by definition")
    return (aperture_factor(a,h)*coefficient,
            aperture_factor(a,h-1)*coefficient)


def mode_weight(a: float, h: int) -> float:
    """The >0 sum of squared two-tone gains; numeric diagnostic."""
    if type(h) is not int or h == 0:
        raise ValueError("require nonzero harmonic")
    return abs(aperture_factor(a,h))**2 + abs(aperture_factor(a,h-1))**2


def mode_recovery_and_defect(a: float, h: int,
                             readings: tuple[complex, complex]) -> tuple[complex,float]:
    """Least-squares carrier mode, and squared distance to lawful response line.

    If defect>calibrated_noise_budget, the pair cannot be source-realizable
    under the declared pin calibration. Small defect is NOT positivity or
    source authentication. This function uses ordinary floating complex.
    """
    if len(readings) != 2:
        raise ValueError("two actual channel readings required")
    x, y = readings
    g, q = aperture_factor(a,h), aperture_factor(a,h-1)
    w = mode_weight(a,h)
    recovered = (g.conjugate()*x + q.conjugate()*y)/w
    transverse_squared = abs(q*x-g*y)**2/w
    return recovered, transverse_squared


def evolve_mode(a: float, h: int, b: int, source_shift: float,
                input_at_bh: tuple[complex, complex], *,
                defect_squared_budget: float) -> tuple[complex, complex]:
    """D_(b,t) on a coherent input, via only two observed input responses.

    A noncoherent input must be REJECTED, never silently repaired via this
    projection. An explicit calibrated squared-error budget is mandatory;
    the numerical check is not an exact or physical realization certificate.
    Same mathematical rule works on wrong seeds: no normality.
    """
    if type(b) is not int or b < 1 or not isinstance(source_shift,(float,int)) or not isfinite(source_shift):
        raise ValueError("source action must be known integer multiplier and finite shift")
    if (type(defect_squared_budget) not in (float,int)
            or not isfinite(defect_squared_budget) or defect_squared_budget < 0):
        raise ValueError("explicit finite nonnegative defect budget required")
    coeff, defect = mode_recovery_and_defect(a,b*h,input_at_bh)
    if defect > defect_squared_budget:
        raise ValueError("observed channel defect exceeds declared budget")
    return mode_vector(a,h,cmath.exp(-2j*pi*h*source_shift)*coeff)


def heterodyne_qi(x: int | Fraction, y: int | Fraction) -> tuple[Fraction,Fraction,Fraction]:
    """Exact measured |z|^2, |z+1|^2, |z+i|^2 for z=x+i*y in Q(i)."""
    if type(x) not in (int,Fraction) or type(y) not in (int,Fraction):
        raise TypeError("rational quadratures required")
    x,y=Fraction(x),Fraction(y)
    return (x*x+y*y, (x+1)**2+y*y, x*x+(y+1)**2)


def heterodyne_decode(values: tuple[int|Fraction,int|Fraction,int|Fraction]) -> tuple[Fraction,Fraction]:
    """Exact pair of signed quadratures; requires independently known references."""
    if len(values)!=3 or any(type(v) not in (int,Fraction) or v<0 for v in values):
        raise ValueError("three nonnegative rational intensities required")
    v,w,z = map(Fraction,values)
    x,y=(w-v-1)/2,(z-v-1)/2
    if heterodyne_qi(x,y)!=tuple(map(Fraction,values)):
        raise ValueError("inconsistent intensity triple")
    return x,y


def two_tone_frame_constants(a: float) -> tuple[float,float]:
    """H^-1 lower and upper weight constants; proved in theorem dossier."""
    if not isinstance(a,(float,int)) or not 0<a<1:
        raise ValueError("0<a<1 required")
    alpha=(1-abs(cos(pi*a)))/(pi*pi*a*a)
    beta=max(8.,18/(pi*pi*a*a))
    return alpha,beta


def energy_pair(phases: tuple[Fraction,...], a: float) -> float:
    """Finite two-tone positive-energy pair kernel (numeric, NOT certified)."""
    if not phases or any(type(x) not in (Fraction,int) for x in phases) or not 0<a<1:
        raise ValueError("nonempty exact-rational phase list and valid aperture required")
    x=[float(Fraction(v)%1) for v in phases]
    N=len(x)
    total=0.
    for u in x:
        for v in x:
            d=(u-v)%1
            overlap=max(0.,a-d)+max(0.,a-(1-d))
            total += overlap*(1+cos(2*pi*d))
    return total/(a*a*N*N)-1-(sin(pi*a)/(pi*a))**2


def energy_transfer_bound(a: float, A: int) -> float:
    """Original BBP zero-seed -> completed pi, unsquared energy difference."""
    if not isinstance(a,(float,int)) or not 0<a<1 or type(A) is not int or A<1:
        raise ValueError("0<a<1, A>=1 required")
    return (2/(a*a)+2*pi/a)/(15*A*A)


def four_pole(n: int) -> Fraction:
    """Independently specified original SUCC BBP forcing; do not mutate."""
    if type(n) is not int or n<1:
        raise ValueError("n>=1 required")
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def source_history(count: int, seed: Fraction | int = 0) -> tuple[Fraction,...]:
    """Exact circle histories for original forcing at true and hostile seeds."""
    if type(count) is not int or not 0<=count<=500 or type(seed) not in (Fraction,int):
        raise ValueError("count 0..500 and rational seed required")
    result=[Fraction(seed)%1]
    for n in range(1,count+1):
        result.append((16*result[-1]+four_pole(n))%1)
    return tuple(result)


def local_plaquette(states: tuple[Fraction,...], n: int) -> Fraction:
    """Zero for ALL seeds; exact cocycle consistency is not π normality."""
    if type(n) is not int or not 0<=n<len(states)-1:
        raise ValueError("consecutive states required")
    return (Fraction(states[n+1])-16*Fraction(states[n])-four_pole(n+1))%1
