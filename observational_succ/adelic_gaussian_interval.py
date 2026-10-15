"""Rational outward interval sanity probes for Gaussian adelic Poisson.

Separate mathematical roles:
1. The adelic Poisson theorem follows ON PAPER from real Schwartz Poisson
   plus the source-rational compact-open spanning lemma (classical).
2. Finite Gaussian sums are independently enclosed using exact rational
   bounds on pi and e^{-x}. The omitted tails get a PROVED rational
   bound from e^x>=x^2/2 and pi>3.
3. Overlap of intervals is only an adversarial CONSISTENCY test. It is
   NOT the proof of the infinite identity, nor of Weil positivity.

Only trivial/half-period Fourier phases are allowed so all finite signed
terms are real and the exact interval arithmetic is straightforward.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

from .adelic_poisson_reconstruction import (
    AdelicPoissonError, RationalCoset, GaussianPoissonGenerator
)
from .source_weil_hierarchy import (
    I, exp_neg, pi_iv, iv
)


def _square_root_fraction(value:F)->F:
    if value<=0:
        raise AdelicPoissonError("A positive square heat required")
    a=isqrt(value.numerator)
    b=isqrt(value.denominator)
    if a*a!=value.numerator or b*b!=value.denominator:
        raise AdelicPoissonError("Gaussian certified amplitude requires rational sqrt(heat)")
    return F(a,b)


def _gaussian_exp_pi_upper_lower(r:F)->I:
    if r<0:
        raise AdelicPoissonError("Gaussian exponent must be nonnegative")
    pi=pi_iv()
    if pi.lo<=3 or pi.lo*r<0 or pi.hi*r>128:
        raise AdelicPoissonError("Exact interval routine lacks the requested exp/pi domain")
    # exp(-pi r) decreases in pi. Inputs to exp_neg are exact rational
    # outward pi endpoints, not a floating representation of pi.
    low=exp_neg(pi.hi*r).lo
    high=exp_neg(pi.lo*r).hi
    return I(low,high)


def certified_gaussian_poisson_probe(
    scale:int|F, heat:int|F, offset_half:bool, N:int
)->dict:
    """Exact rational truncation and absolute remainder bounds.

    Original coset is 0+D Zhat. Arch Gaussian centred at 0 or D/2.
    Fourier phase is 1 or (-1)^m. Test t must have rational square root.
    Finite identity:
      sum_n exp(-pi*t*(D*n-a)^2)
       = 1/(D*sqrt(t)) sum_m exp(-pi*m^2/(D^2*t)) exp(2pi*i*a*m/D).

    The omitted primal tail |n|>N is bounded by
      4 / [27 (t D^2)^2 (N-|a|/D)^3].
    The omitted dual tail |m|>N is bounded by
      4 D^3 t^(3/2) / (27 N^3).
    Proof: pi>3, e^{-x}<=2/x^2, integral comparison for sum 1/n^4.
    """
    if type(scale) not in (int,F) or type(heat) not in (int,F):
        raise AdelicPoissonError("Exact rational scale/heat required")
    if type(offset_half) is not bool or type(N) is not int or not 2<=N<=16:
        raise AdelicPoissonError("Only Boolean half-shift and integer truncation budget")
    D,t=F(scale),F(heat)
    if D<=0 or t<=0:
        raise AdelicPoissonError("Positive rational scale/heat")
    sq=_square_root_fraction(t)
    shift=F(1,2) if offset_half else F(0)
    generator=GaussianPoissonGenerator(RationalCoset(0,D),D*shift,t)

    primal=iv(0)
    dual=iv(0)
    for n in range(-N,N+1):
        source=generator.primal_integer(n)
        primal=primal+_gaussian_exp_pi_upper_lower(
            source["Gaussian_exponent_coefficient_of_pi"]
        )
    for m in range(-N,N+1):
        source=generator.dual_integer(m)
        term=_gaussian_exp_pi_upper_lower(
            source["Gaussian_exponent_coefficient_of_pi"]
        )
        if source["global_Fourier_phase"] not in (F(0),F(1,2)):
            raise AssertionError("Unsupported complex phase in a real-only rigorous interval")
        if source["global_Fourier_phase"]==F(1,2):
            term=-term
        dual=dual+term
    amplitude=F(1)/(D*sq)
    dual=dual*amplitude

    # Support/normalization error bound, all rational with no
    # use of the desired infinite Poisson identity.
    b=t*D*D
    if N<=abs(shift):
        raise AdelicPoissonError("Insufficient truncation beyond Gaussian translation")
    primal_tail=F(4,27)/(b*b*(N-abs(shift))**3)
    dual_tail=F(4,27)*D**3*sq**3/N**3
    primal_global=I(primal.lo-primal_tail,primal.hi+primal_tail)
    dual_global=I(dual.lo-dual_tail,dual.hi+dual_tail)
    compatible=not (primal_global.hi<dual_global.lo or
                    dual_global.hi<primal_global.lo)
    if not compatible:
        raise AssertionError("Rigorous Gaussian bounds falsify declared Poisson normalization")
    return {
        "D":D,"heat":t,"square_root_heat":sq,
        "center":D*shift,"offset_half":offset_half,"truncation":N,
        "primal_finite_interval":(primal.lo,primal.hi),
        "dual_finite_interval":(dual.lo,dual.hi),
        "primal_tail_bound":primal_tail,"dual_tail_bound":dual_tail,
        "primal_global_enclosure":(primal_global.lo,primal_global.hi),
        "dual_global_enclosure":(dual_global.lo,dual_global.hi),
        "rigorous_intervals_overlap":True,
        "wrong_haar_multiplier_detectable_if_intervals_disjoint":None,
        "infinite_identity_proved_by_finite_intervals":False,
        "full_analytic_Poisson_theorem_from_classical_real_Poisson":True,
        "RH_proved":False,
    }


def wrong_haar_amplitude_witness()->dict:
    """At D=2, missing finite Haar 1/D factor is strictly falsified.

    For t=1, 0 shift, N=3, bound direct theta and the incorrect dual
    expression with DOUBLE amplitude, using only rational enclosures.
    """
    good=certified_gaussian_poisson_probe(2,1,False,3)
    dual=good["dual_global_enclosure"]
    primal=good["primal_global_enclosure"]
    # Correct dual has amplitude 1/2; omitted finite Haar gives 2x.
    wrong=(2*dual[0],2*dual[1])
    if not (wrong[0]>primal[1] or wrong[1]<primal[0]):
        raise AssertionError("Haar source mutation not separated by rigorous intervals")
    return {
        "correct_primal_global_enclosure":primal,
        "wrong_mutated_dual_global_enclosure":wrong,
        "mutant_wrong_Haar_refuted_with_rational_bounds":True,
        "no_float_sign_assumptions":True,
        "underlying_full_poisson_already_classical":True,
        "RH_proved":False,
    }
