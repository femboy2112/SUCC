"""Exact source-derived Gaussian finite-sieve Haar coverage calibration.

The source law is UNIFORM on the periodic sieve survivors, not the time
law of a Gaussian-prime bounded-step walk. Chinese remainder theory
justifies the closed forms; enumerations are finite positive controls.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import prod
from typing import Sequence

from .coverage_lower_bounds import (CoverageError, gaussian_coordinate,
                                    gaussian_frame, is_prime, lattice_snake)


def gaussian_sieve_crt_certificate(factor_pairs: Sequence[tuple[int, int]],
                                   *, max_period: int = 300) -> dict:
    """Prove by CRT, and independently count, split-prime residue floors.

    Each pair (a,b) means the conjugate factors a+bi and a-bi, with
    p=a*a+b*b an authentic DISTINCT rational split prime. Resource cap
    applies only to the finite auditor, not to the mathematical theorem.
    """
    pairs = tuple(factor_pairs)
    if not pairs:
        raise CoverageError("At least one true split Gaussian pair required")
    primes = []
    for a, b in pairs:
        if type(a) is not int or type(b) is not int or a <= 0 or b <= 0:
            raise CoverageError("Require positive integral Gaussian coordinates")
        p = a*a + b*b
        if not is_prime(p) or p % 4 != 1 or p in primes:
            raise CoverageError("Duplicate, composite, inert or ramified source norm")
        primes.append(p)
    q = prod(primes)
    if type(max_period) is not int or q > max_period:
        raise CoverageError("Finite enumeration resource cap; not an arithmetic no-go")
    factors = tuple(f for a, b in pairs for f in ((a,b),(a,-b)))
    sample = tuple(pt for pt in lattice_snake(q)
                   if all(gaussian_coordinate(pt, fac) != 0 for fac in factors))
    expected = F(q*q) * prod(F(p-1, p)**2 for p in primes)
    if expected.denominator != 1 or len(sample) != expected:
        raise AssertionError("Source count contradicts independent CRT theorem")
    details = []
    for fac in factors:
        p = fac[0]**2+fac[1]**2
        frame = gaussian_frame(sample, fac, f"CRT period {q} sieve Haar")
        if frame.masses != (F(0),) + (F(1, p-1),) * (p-1):
            raise AssertionError("CRT Gaussian coordinate is not uniform over units")
        if frame.chi2 != F(1,p-1):
            raise AssertionError("CRT collision index mismatch")
        report = frame.bound(F(1,4))
        if report['exception_count'] != 1 or report['good_mass'] != F(p-1,p):
            raise AssertionError("Wrong exact low-atom coverage")
        details.append({'factor':fac,'norm':p,'chi2':frame.chi2,
                        'good_mass':report['good_mass'],'bad_count':1})
    return {'period':q,'sieve_survivors':len(sample),
            'expected_survivors':expected,'factors':tuple(details),
            'source_type':'uniform CRT sieve survivor, NOT Gaussian-prime walk'}

def split_sieve_mixing_debt(frame) -> dict:
    """Exact irreducible zero-exclusion debt + variable walk-mixing debt.

    Applicable only to uniform-p reference with exactly zero mass at 0;
    this source restriction must be justified independently.
    """
    p=len(frame.atoms)
    if p<2 or frame.atoms != tuple(range(p)) or frame.reference != (F(1,p),)*p:
        raise CoverageError("Need fully declared Haar residue frame")
    if frame.masses[0] != 0:
        raise CoverageError("Zero residue is not forbidden in this source")
    base=F(1,p-1)
    deviation=F(p)*sum((frame.masses[u]-F(1,p-1))**2 for u in range(1,p))
    if frame.chi2 != base+deviation:
        raise AssertionError("Exact Gaussian sieve mixing-debt identity failed")
    return {'irreducible_zero_cost':base,'path_mixing_debt':deviation,
            'total_chi2':frame.chi2}
