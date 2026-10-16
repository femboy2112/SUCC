"""Exact finite cyclic Poisson calibration against independent SUCC DFT.

This is the finite abelian prototype of Tate adelic Poisson summation.
It is NOT a proof that Fourier analysis of the full adele ring, Gamma
completion or Weil positivity has been implemented. The proof uses
character orthogonality, with explicit source and normalization contracts.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .finite_fourier_carrier import (
    CyclotomicElement, exact_dft, exact_idft
)
from .pontryagin_source_duality import (
    PontryaginSourceError, FiniteCyclicCharacter
)


def finite_poisson_coset(
    values: tuple[int|F, ...], subgroup_step: int, offset: int = 0,
    *,
    source_id: str = "Z-integer-modular-source", epoch: int = 0,
) -> dict:
    """For H=d Z/n, compare sum_(x in a+H) f(x) with dual H^perp Fourier sum.

    SUCC's exact_dft uses the POSITIVE exponential convention:
         Fplus(k)=sum_x f(x)*exp(2pi*i*k*x/n).
    Fourier inversion has NEGATIVE phase, yielding
         sum_(x in a+H) f(x)
            = |H|/n * sum_(k in H^perp) Fplus(k)*exp(-2pi*i*k*a/n).
    """
    if type(values) is not tuple or not 2 <= len(values) <= 36:
        raise PontryaginSourceError("One bounded original finite cyclic source tuple required")
    if any(type(x) not in (int,F) for x in values):
        raise PontryaginSourceError("Only exact integer/rational source coefficients")
    n=len(values)
    if type(subgroup_step) is not int or not 1 <= subgroup_step <= n or n%subgroup_step:
        raise PontryaginSourceError("H=dZ/n needs a positive divisor d of n")
    if type(offset) is not int:
        raise PontryaginSourceError("An exact original coset offset is required")
    if type(source_id) is not str or not source_id.strip() or type(epoch) is not int or epoch < 0:
        raise PontryaginSourceError("Original source ID and epoch must be declared")
    d=subgroup_step
    size=n//d
    original=tuple(F(x) for x in values)
    direct=sum((original[(offset+d*j)%n] for j in range(size)),F(0))
    spectrum=exact_dft(original)
    rhs=CyclotomicElement.scalar(n,0)
    for j in range(d):
        k=j*size
        phase=FiniteCyclicCharacter(n,k,source_id,epoch).character_root(-offset)
        rhs=rhs + spectrum[k]*phase
    rhs=rhs.scale(F(size,n))
    if rhs != CyclotomicElement.scalar(n,direct):
        raise AssertionError("Poisson subgroup Fourier dual fails original source sum")
    # Independent inversion: guard against an implementation whose DFT and
    # dual "proof" simply agree on a shared wrong normalization.
    rebuilt=exact_idft(spectrum)
    if rebuilt != tuple(CyclotomicElement.scalar(n,x) for x in original):
        raise AssertionError("Source reconstruction from full finite spectrum failed")
    return {
        "modulus":n,"source_id":source_id,"epoch":epoch,
        "subgroup_step":d,"offset":offset%n,
        "subgroup_size":size,
        "annihilator_frequencies":tuple(j*size for j in range(d)),
        "direct_source_sum":direct,
        "dual_sum_exact_polynomial":rhs.polynomial,
        "dual_source_provenance":"pre-existing exact cyclotomic DFT",
        "fourier_positive_sign":True,
        "inverse_negative_sign":True,
        "finite_poisson_exact":True,
        "adelic_poisson_proved_by_finite_examples":False,
        "RH_proved":False,
    }


def exact_cyclic_annihilator(n: int, step: int) -> dict:
    """Brute finite orthogonality oracle for subgroup H=dZ/n."""
    if type(n) is not int or not 2 <= n <= 100 or type(step) is not int or not 1 <= step <= n or n%step:
        raise PontryaginSourceError("Valid bounded cyclic subgroup needed")
    source=tuple((j*step)%n for j in range(n//step))
    dual=tuple(
        k for k in range(n)
        if all((k*x)%n==0 for x in source)
    )
    expected=tuple(j*(n//step) for j in range(step))
    if dual!=expected:
        raise AssertionError("Independent finite source orthogonality contradicted dual formula")
    return {"modulus":n,"subgroup":source,"annihilator":dual,
            "size_product":len(source)*len(dual),
            "size_product_equals_n":len(source)*len(dual)==n,
            "two_independent_calculations_agree":True,
            "RH_proved":False}


def wrong_coset_phase_witness() -> dict:
    """Incorrect sign turns a translated source coset into the wrong one."""
    n, a, d=7, 1, 7
    original=tuple(F(1 if x==a else 0) for x in range(n))
    good=finite_poisson_coset(original,d,a)
    spectrum=exact_dft(original)
    bad=CyclotomicElement.scalar(n,0)
    for k in good["annihilator_frequencies"]:
        bad=bad+spectrum[k]*CyclotomicElement.root(n,+k*a)  # wrong inverse sign
    bad=bad.scale(F(1,n))
    if bad==CyclotomicElement.scalar(n,good["direct_source_sum"]):
        raise AssertionError("Mutated coset sign unexpectedly retained source")
    return {"n":n,"a":a,"correct_source_sum":good["direct_source_sum"],
            "wrong_sign_Fourier_sum":bad.polynomial,
            "sign_mutation_detected":True,"RH_proved":False}
