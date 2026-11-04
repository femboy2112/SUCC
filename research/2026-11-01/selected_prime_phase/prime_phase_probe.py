"""Exact original source receipts + separately labeled float-only signed diagnostics.

Run: python research/2026-11-01/selected_prime_phase/prime_phase_probe.py
No external data, pi digits, Monte Carlo, or p-value extrapolation.
"""
from __future__ import annotations

import cmath
import json
from fractions import Fraction
from math import isqrt, pi
from pathlib import Path

from prime_phase import (state,source,horizon_primes,birth,phase_split,
                         trace_factor,source_mass_certificate)
from independent_oracle import u_convolution,verify_horizon


def finite_exact_receipt():
    results=[]
    for N in (2,3,4,5,8,16,32,64,100):
        u=state(N)
        assert u==u_convolution(N)
        ps=horizon_primes(N)
        v,parts=phase_split(u,ps)
        for p in ps:verify_horizon(N,p)
        trace=trace_factor(parts,1)
        results.append({
            'N':N,'prime_count':len(ps),'prime_list':ps,
            'denominator_digits':len(str(u.denominator)),
            'relative_trace_abs_numerator':abs(trace.numerator),
            'relative_trace_abs_denominator':trace.denominator,
            'first_residues':[{'prime':p,'a':a} for p,a in parts[:4]],
            'p_free_cofactor_denominator_digits':len(str(v.denominator)),
            'verified_all_primes':True
        })
    part,cap=source_mass_certificate()
    return {
        'source':'original four signed BBP poles; exact U0=0',
        'authority':'exact stdlib Fraction + independent combined-rational oracle',
        'not_a_pi_normality_proof':True,
        'mass_2_through_16':str(part),'mass_2_to_infinity_upper':str(cap),
        'rational_simpler_upper':'65/256',
        'n3_sample':{'U':'615863723/765765','P':221,
                     'parts':[[13,10],[17,4]],'cofactor':'2783233/3465',
                     'trace_multiplier':'1/192'},
        'p257_primary_period':4,'p257_primary_complete_cycle_mean_lower':'49/100',
        'horizons':results
    }


def finite_signed_diagnostics():
    """Float-only diagnostics: NOT sound intervals or infinite proofs."""
    results=[]
    for N in (64,128,256,512):
        p=next(p for p in horizon_primes(N) if p>2*N and p<3*N)
        b=birth(p)
        us=[];u=Fraction(0)
        for j in range(1,N+1):
            u=16*u+source(j)
            if j>=b.n:us.append((j,u))
        for h in (1,3,5):
            primary=0j;cofactor=0j;joint=0j
            for j,u in us:
                a=(b.coefficient*pow(16,j-b.n,p))%p
                v=(u-Fraction(a,p))%1
                primary+=cmath.exp(2j*pi*h*a/p)
                cofactor+=cmath.exp(2j*pi*h*float(v))
                joint+=cmath.exp(2j*pi*h*float(u%1))
            L=len(us)
            results.append({
                'N':N,'h':h,'p':p,'birth':b.n,'length':L,
                'primary_mean_modulus':format(abs(primary/L),'.12g'),
                'p_free_cofactor_mean_modulus':format(abs(cofactor/L),'.12g'),
                'ACTUAL_joint_mean_modulus':format(abs(joint/L),'.12g'),
                'normalized_Galois_trace_modulus':format(1/(p-1),'.12g'),
            })
    return {'status':'NUMERICAL_DIAGNOSTIC_ONLY','method':'exact fractional states, float complex exponential','results':results}


if __name__=='__main__':
    folder=Path(__file__).resolve().parent
    exact=finite_exact_receipt()
    signed=finite_signed_diagnostics()
    (folder/'FINITE_EXACT_RECEIPT.json').write_text(json.dumps(exact,sort_keys=True,indent=2)+'\n')
    (folder/'SIGNED_DIAGNOSTICS.json').write_text(json.dumps(signed,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'exact_horizons':len(exact['horizons']),
          'signed_diagnostic_cases':len(signed['results']),
          'example_N3':exact['n3_sample'],'N128_h1':next(x for x in signed['results'] if x['N']==128 and x['h']==1),
          'all_exact_checks':True},indent=2))
