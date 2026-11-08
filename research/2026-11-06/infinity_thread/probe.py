"""Finite probes for conditional INFINITY THREAD theorem. Source-original and zero-seeded.
All complex exponentials are FLOAT DIAGNOSTICS ONLY, not interval-certified asymptotics.
The exact all-prefix gluing inequality and its proof are in THEOREM.md.
"""
from __future__ import annotations
from fractions import Fraction
from math import cos, sin, pi
from random import Random
import json


def authentic_r(n: int) -> Fraction:
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def independent_four_poles(n: int) -> Fraction:
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def original_fractions(count: int) -> list[Fraction]:
    x=Fraction(0)
    states=[x]
    for n in range(1,count):
        v=16*x+authentic_r(n)
        x=v-v.numerator//v.denominator
        states.append(x)
    return states


def to_complex(xs: list[Fraction | float], h: int) -> list[complex]:
    return [complex(cos(2*pi*h*float(x)),sin(2*pi*h*float(x))) for x in xs]


def horizon_parameters(A: int) -> tuple[int,int,int,int]:
    if A<16: raise ValueError('A>=16')
    Q=1<<((A.bit_length()-1)//2)
    m0=(A+Q-1)//Q
    m1=2*A//Q
    return Q,m0,m1,m1-m0+1


def averaged_energy(seq: list[complex], A: int) -> float:
    Q,m0,m1,L=horizon_parameters(A)
    if len(seq)<2*A: raise ValueError('insufficient sequence')
    sums=[0j]*Q
    acc=0.
    for m in range(1,m1+1):
        for j in range(Q):
            sums[j]+=seq[j+(m-1)*Q]
        if m0<=m<=m1:
            acc+=sum(abs(s/m)**2 for s in sums)/Q
    return acc/L


def prefix_max(seq: list[complex], A: int) -> float:
    if len(seq)<2*A: raise ValueError('insufficient sequence')
    total=0j;maximum=0.
    for n,v in enumerate(seq[:2*A],1):
        total+=v
        if A<=n<=2*A:
            maximum=max(maximum,abs(total)/n)
    return maximum


def gluing_upper(A: int, E: float) -> float:
    Q,*_=horizon_parameters(A)
    return 18*Q/A+(64*E/3)**(1/3)


def poiss_half(xs: list[Fraction | float], A: int, max_h: int=12):
    Q,m0,m1,L=horizon_parameters(A)
    energies=[]
    for h in range(1,max_h+1):
        e=averaged_energy(to_complex(xs[:2*A],h),A)
        assert 0<=e<=1+1e-10
        energies.append(e)
    p=2*sum(2**(-h)*e for h,e in enumerate(energies,1))
    tail=2**(1-max_h)  # exact: Σ_|h|>H 2^-|h| = 2^(1-H)
    assert 0<=p<=2 and tail>=0
    sup=prefix_max(to_complex(xs[:2*A],1),A)
    bound=gluing_upper(A,energies[0])
    assert sup <= bound+1e-10
    return {'A':A,'Q':Q,'M_min':m0,'M_max':m1,'M_count':L,
            'h1_to_h3_avg_R_float':[round(v,12) for v in energies[:3]],
            'poisson_half_h1_to_h12_float':round(p,12),
            'uncomputed_poisson_tail_at_most':f'1/{2**(max_h-1)}',
            'h1_prefix_shell_sup_float':round(sup,12),
            'h1_gluing_bound_float':round(bound,12)}


def run():
    # Froze A and sample controls before first new numerical execution on the PR.
    assert all(authentic_r(n)==independent_four_poles(n) for n in range(1,257))
    states=original_fractions(8192)
    assert states[0]==0
    out=[]
    for A in (2048,4096):
        cases={
            'original_zero_four_pole':states[:2*A],
            'isometric_nonnormal_H_shadow':[Fraction(n,(2*n-1)**4) for n in range(2*A)],
            'periodic_rational_beta_1_17':[Fraction(pow(16,n,17),17) for n in range(2*A)],
        }
        rng=Random(316783+A)
        cases['synthetic_iid_real_seed']=[rng.random() for _ in range(2*A)]
        for kind,xs in cases.items():
            data=poiss_half(xs,A,12)
            data['kind']=kind
            if kind=='isometric_nonnormal_H_shadow':
                assert all(v>.99 for v in data['h1_to_h3_avg_R_float'])
            if kind=='periodic_rational_beta_1_17':
                assert all(abs(v-1)<1e-10 for v in data['h1_to_h3_avg_R_float'])
            out.append(data)
    return {'scope':'OBSERVED FINITE FLOAT DIAGNOSTICS only',
            'source_original':True,'source_seed':'literal U0=0',
            'preregistration_before_new_holdouts':True,
            'A_holdouts':[2048,4096],
            't_poisson':'1/2','fourier_h_truncation':12,
            'normality':'OPEN','infinite_source_contraction':'OPEN',
            'rows':out}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
