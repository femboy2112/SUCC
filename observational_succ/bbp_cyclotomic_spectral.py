"""Finite signed cyclic-time Fourier ledger for actual BBP prime windows.

DFT computations here use ordinary complex approximations as DIAGNOSTICS.
The underlying finite identities are proved independently in the dossier;
no asymptotic cancellation or pi-normality is inferred from these floats.
"""
from __future__ import annotations
from cmath import exp
from math import pi, sqrt
from fractions import Fraction as Q
from observational_succ.bbp_cyclotomic_birth import (
    _prime, forced_states, first_phase_residue, multiplicative_order_16,
)


def phase(x: Q | float) -> complex:
    return exp(2j*pi*float(x))


def dft(values: tuple[complex, ...]) -> tuple[complex, ...]:
    """Unitarity-free normalized finite DFT, with sign exp(-2pi iks/L)."""
    L=len(values)
    if L==0:raise ValueError('positive clock length required')
    return tuple(sum(values[s]*exp(-2j*pi*k*s/L) for s in range(L))/L
                 for k in range(L))


def single_prime_spectral_ledger(p: int, h: int = 1) -> dict:
    """Source-selected full and complementary Fourier vectors; p=8m+1.

    Computes at all n=m+1..4m. No false Galois ensemble average.
    """
    _prime(p)
    if p%8 !=1:raise ValueError('p ==1 mod 8 required')
    if type(h) is not int or h==0:raise ValueError('nonzero integer frequency')
    m=(p-1)//8;L=multiplicative_order_16(p);B=3*m//L
    assert B*L==3*m
    ys=forced_states(4*m)
    u=tuple(phase(Q((h*first_phase_residue(p)*pow(16,s,p))%p,p)) for s in range(L))
    vs=[]
    for s in range(L):
        vec=[]
        for b in range(B):
            t=b*L+s
            residue=first_phase_residue(p)*pow(16,t,p)%p
            v=(ys[m+t]-Q(residue,p))%1
            assert v.denominator%p
            vec.append(phase(h*v))
        vs.append(sum(vec)/B)
    v=tuple(vs)
    uh=dft(u);vh=dft(v)
    full=sum(u[s]*v[s] for s in range(L))/L
    spectral=sum(uh[(-k)%L]*vh[k] for k in range(L))
    meanpart=uh[0]*vh[0]
    mixed=sum(uh[(-k)%L]*vh[k] for k in range(1,L))
    gvmean=sum(u)/L
    spectral_upper=sqrt(p)/L*sum(abs(vh[k]) for k in range(1,L))
    assert abs(full-spectral)<1e-8
    assert abs(spectral-meanpart-mixed)<1e-8
    assert abs(gvmean-uh[0])<1e-8
    return {"p":p,"h":h,"m":m,"L":L,"blocks":B,
            "full":full,"local_mean":uh[0],"complement_mean":vh[0],
            "zero_mode":meanpart,"mixed":mixed,"fourier_reconstruction":spectral,
            "complement_l1_nonzero":sum(abs(vh[k]) for k in range(1,L)),
            "gauss_upper_nonzero":spectral_upper,
            "u_energy":sum(abs(x)**2 for x in uh),
            "v_energy":sum(abs(x)**2 for x in vh)}


def adversarial_alignment(p: int, h: int = 1) -> tuple[float,float]:
    """u_s cancels locally, v_s=conjugate(u_s) forces global sum exactly 1."""
    _prime(p)
    if p%8!=1:raise ValueError('p==1 mod 8')
    L=multiplicative_order_16(p)
    u=tuple(phase(Q((h*4*pow(16,s,p))%p,p)) for s in range(L))
    return abs(sum(u)/L),abs(sum(t*t.conjugate() for t in u)/L)
