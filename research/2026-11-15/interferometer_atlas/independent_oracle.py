"""Independent rational/computational oracle for SUCC instrument atlas.

Never imports observational_succ.interferometer_atlas. Exact rational grids,
independent digit generators and a clearly noncertificate mpmath smoke.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json
import mpmath as mp


def oily_weight(h):return Q(h+1,3*2**h)


def full_kernel_re(x):
    return {0:Q(1),1:Q(-13,75),2:Q(-5,27),3:Q(-13,75)}[x%4]


def direct_quarter_grid_exact(samples):
    n=len(samples)
    return sum((full_kernel_re(x-y) for x in samples for y in samples),Q(0))/n**2


def finite_quarter_energy(samples,H):
    n=len(samples)
    return sum((oily_weight(h)*Q(sum((1,0,-1,0)[(h*(x-y))%4]
                                         for x in samples for y in samples),n*n)
                for h in range(1,H+1)),Q(0))


def direct_haar_pair(words,k):
    n=len(words)
    return sum((Q(0) if x[:k]!=y[:k] else Q(1) if x[k]==y[k] else Q(-1,15)
                for x in words for y in words),Q(0))/n**2


def direct_haar_count(words,k):
    n=len(words)
    return Q(16*sum(v*v for v in Counter(x[:k+1] for x in words).values())
             -sum(v*v for v in Counter(x[:k] for x in words).values()),15*n*n)


def exact_source_digits(D):
    P=Q(0)
    for n in range(1,D+81):
        forcing=lambda j: Q(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
        P+=forcing(n)/16**n
        upper=P+forcing(n+1)/(15*16**n)
        xlo=(16**D*P).__floor__()
        if xlo==(16**D*upper).__floor__():
            return tuple((xlo//16**j)%16 for j in range(D-1,-1,-1))
    raise ArithmeticError('insufficient independently implemented exact source precision')


def source_shell(B,K):
    d=exact_source_digits(2*B+K)
    return tuple(tuple(d[n:n+K]) for n in range(B,2*B))


def tail(H):return Q(H+3,3*2**H)


def pi_phase_smoke(B,H=16):
    # NOT a proof certificate: uses floating pi; rigorous source-bound is paper proof.
    with mp.workdps(90):
        x=mp.pi/16
        phases_pi=[mp.frac(mp.power(16,n)*x) for n in range(B,2*B)]
        phases_U=[]
        U=Q(0)
        for j in range(1,2*B):
            r=Q(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))
            U=16*U+r
            if j>=B:
                u=U%1
                phases_U.append(mp.mpf(u.numerator)/u.denominator)
        def energy(xs):
            return mp.fsum([mp.mpf(h+1)/(3*2**h)*
                    abs(mp.fsum([mp.exp(2j*mp.pi*h*t) for t in xs])/B)**2
                    for h in range(1,H+1)])
        e_pi,e_u=energy(phases_pi),energy(phases_U)
        b=Q(7,12*B*B)
        return {"B":B,"harmonics":H,"pi_complete":mp.nstr(e_pi,19),
                "rational_source":mp.nstr(e_u,19),"difference":mp.nstr(abs(e_pi-e_u),18),
                "proved_budget":f"{b.numerator}/{b.denominator}",
                "within_budget_smoke":abs(e_pi-e_u)<mp.mpf(b.numerator)/b.denominator}


def run():
    samples_checked=0;radix_word_cases=0;source_checks=0
    # Entire infinite H Oily kernel, compared against finite exact sums + tail.
    for size in range(1,6):
        for samples in product(range(4),repeat=size):
            ideal=direct_quarter_grid_exact(samples)
            for H in (1,2,4,8,14):
                partial=finite_quarter_energy(samples,H)
                assert 0<=partial<=ideal<=partial+tail(H),(samples,H,ideal,partial)
                samples_checked+=1
    # Direct pair-vs-histogram Haar in independent code, source digits too.
    for size in range(1,5):
        for base in product(range(3),repeat=size):
            words=tuple((x,(x+1)%3,(x+2)%3) for x in base)
            for k in range(3):
                assert direct_haar_pair(words,k)==direct_haar_count(words,k)
                radix_word_cases+=1
    source_prefixes={}
    for B in (2,3,4,7,12,24):
        ws=source_shell(B,8)
        source_prefixes[str(B)]=["".join('0123456789abcdef'[x] for x in v) for v in ws[:3]]
        for k in range(8):
            assert direct_haar_pair(ws,k)==direct_haar_count(ws,k)
            source_checks+=1
    calibration = []
    for B in (1,2,4,8,16):
        calibration.append(pi_phase_smoke(B))
        assert calibration[-1]['within_budget_smoke']
    out={"oily_full_kernel_vs_rational_truncation":samples_checked,
         "haar_direct_vs_histogram":radix_word_cases,
         "authentic_zero_BBP_haar":source_checks,
         "rational_pi_digit_samples":source_prefixes,
         "pi_phase_smoke_not_certificate":calibration,
         "synthetic_independent_uniform_null_expected_energy":
            {str(B):f"1/{B}" for B in (2,3,4,8,16)},
         "all_exact_checks_pass":True,
         "pi_normality":"OPEN","RH":"OPEN"}
    print(json.dumps(out,indent=2));return out

if __name__=='__main__':run()
