"""Exact finite two-place *clock* transport, with real complex Fourier diagnostics.
Raw 2-adic residues are exact; DFT is numerical, not an all-horizon estimate.
"""
from fractions import Fraction
from cmath import exp
from math import pi
import json
from experiment import original,r_exact


def original_mod_clock(Q:int)->list[int]:
    assert Q>=2 and Q&(Q-1)==0
    state=0;res=[0]
    for n in range(1,Q):
        r=r_exact(n)
        assert r.denominator%2==1
        state=(16*state+r.numerator*pow(r.denominator,-1,Q))%Q
        res.append(state)
    assert len(set(res))==Q, 'NOT an isometry at this Q'
    return res


def shadow_mod_clock(Q:int)->list[int]:
    assert Q>=2 and Q&(Q-1)==0
    out=[]
    for n in range(Q):
        x=Fraction(n,(2*n-1)**4)
        out.append(x.numerator*pow(x.denominator,-1,Q)%Q)
    assert len(set(out))==Q
    return out


def transformed_character(xs:list[Fraction],mods:list[int],h:int=1)->dict:
    Q=len(xs)
    assert len(mods)==Q and len(set(mods))==Q and Q&(Q-1)==0
    F=[exp(2j*pi*h*float(x)) for x in xs]
    reorder=[None]*Q
    for n,r in enumerate(mods):reorder[r]=F[n]
    spec=[]
    for j in range(Q):
        coef=sum(reorder[r]*exp(-2j*pi*j*r/Q) for r in range(Q))/Q
        spec.append(abs(coef)**2)
    odd=sum(spec[1::2]);all_energy=sum(spec)
    pair=sum(abs(F[n]-F[n+Q//2])**2 for n in range(Q//2))/(2*Q)
    coherent=abs(sum(F)/Q)**2
    assert abs(odd-pair)<1e-9
    assert abs(all_energy-1)<1e-9
    assert abs(spec[0]-coherent)<1e-9
    assert all((mods[n+Q//2]-mods[n])%Q==Q//2 for n in range(Q//2))
    return {'Q':Q,'h':h,'mean_character_energy_float':round(coherent,12),
            'odd_2adic_band_energy_float':round(odd,12),
            'odd_band_direct_real_pair_energy_float':round(pair,12),
            'all_band_energy_float':round(all_energy,12)}


def run()->dict:
    out=[]
    for Q in (64,128,256):
        orig=original(Q)
        shad=[Fraction(n,(2*n-1)**4) for n in range(Q)]
        for name,phas,mods in [('original_zero',orig,original_mod_clock(Q)),
                               ('isometric_H_shadow',shad,shadow_mod_clock(Q))]:
            data=transformed_character(phas,mods)
            data['source']=name
            out.append(data)
    return {'status':'2-adic residues exact; complex DFT observed finite FLOAT ONLY',
            'selected_source_normality':'OPEN',
            'cross_place_common_basis':'clock labels n and source V(n) mod Q, no p-adic real phase equality',
            'rows':out}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
