"""BBP critical Fejer: exact rational source/majorants, real floating probes.
No claim about all-horizon pi normality. Pure Python stdlib.
"""
from __future__ import annotations
from fractions import Fraction
from math import cos, sin, pi, sqrt
from random import Random
import json


def r_exact(n:int)->Fraction:
    assert n>=1
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def r_four_poles(n:int)->Fraction:
    assert n>=1
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def original(N:int)->list[Fraction]:
    assert N>=1
    x=Fraction(0); out=[x]
    for n in range(1,N):
        v=16*x+r_exact(n)
        x=v-v.numerator//v.denominator
        out.append(x)
    return out


def rational_tail(n:int,J:int=14)->Fraction:
    assert n>=0 and J>=2
    return sum((r_exact(n+j)/16**j for j in range(1,J+1)),Fraction(0))


def fejer_weighted_spectrum(phases:list[float],H:int)->float:
    N=len(phases)
    assert N>0 and H>=1
    E=1.0
    for h in range(1,H+1):
        cr=si=0.0
        for x in phases:
            a=2*pi*h*x
            cr+=cos(a);si+=sin(a)
        E+=2*(1-h/(H+1))*(cr*cr+si*si)/(N*N)
    return E


def fejer_pair_float(phases:list[float],H:int)->float:
    from math import sin
    N=len(phases);t=float(N*(H+1))
    acc=N*(H+1.0)
    for i in range(N):
        for j in range(i):
            d=(phases[i]-phases[j])%1
            if d>0.5: d=1-d
            if d<1e-13:
                f=H+1.0
            else:
                v=sin(pi*d)
                f=sin(pi*(H+1)*d)**2/((H+1)*v*v)
            acc+=2*f
    return acc/(N*N)


def exact_majorant_quantized(xs:list[Fraction],H:int,unit:int=1000000)->dict:
    """Exact rational upper bound from kernel envelope; quantize each pair UP."""
    N=len(xs);L=H+1
    assert N>0 and H>=1 and unit>=1
    total=N*L*unit
    nonzero=0; min_space=None
    for i in range(N):
        for j in range(i):
            d=abs(xs[i]-xs[j]);d=min(d,1-d)
            if d==0:
                upper=Fraction(L)
            else:
                nonzero+=1
                if min_space is None or d<min_space: min_space=d
                bound=Fraction(1,4*L*d*d)
                upper=min(Fraction(L),bound)
            upint=(upper.numerator*unit + upper.denominator-1)//upper.denominator
            total+=2*upint
    return {'N':N,'H':H,'unit':unit,'integer_upward_sum':total,
            'bound_numerator':total,'bound_denominator':unit*N*N,
            'upper_decimal':round(total/(unit*N*N),10),
            'distinct_pairs':nonzero==N*(N-1)//2,
            'min_gap_float_diagnostic':float(min_space) if min_space else None}


def near_pair_count(xs:list[Fraction],H:int)->int:
    """Exact *ordered* circular pairs with ||xi-xj||<=1/H incl diagonal."""
    N=len(xs);d=Fraction(1,H)
    assert H>=3
    s=sorted(xs)
    y=s+[x+1 for x in s]
    count=0; j=0
    for i in range(N):
        j=max(j,i+1)
        while j<i+N and y[j]-y[i]<=d:
            j+=1
        count+=j-(i+1)
    return N+2*count


def probe(N:int,H:int,do_majorant:bool=False)->dict:
    xs=original(N)
    xf=[float(x) for x in xs]
    zf=[float((x+rational_tail(n))%1) for n,x in enumerate(xs)]
    cx=fejer_weighted_spectrum(xf,H)
    cz=fejer_weighted_spectrum(zf,H)
    B=4*sqrt(H*(H+1))/N
    out={'N':N,'H':H,'original_C_float':round(cx,11),
         'completed_C_float':round(cz,11),
         'sqrt_energy_distance_float':round(abs(sqrt(cx)-sqrt(cz)),12),
         'proved_Hilbert_radius':round(B,9),
         'near_pairs_at_1_over_H':near_pair_count(xs,H),
         'near_pairs_density_normalized_float':round(near_pair_count(xs,H)*H/(N*N),8)}
    if do_majorant:out['certified_rational_upper']=exact_majorant_quantized(xs,H)
    return out


def run()->dict:
    assert all(r_exact(n)==r_four_poles(n) for n in range(1,513))
    cases=[(32,8),(64,8),(64,16),(128,16),(128,32),
           (128,64),(128,128),(256,256)]
    out=[]
    for N,H in cases:
        v=probe(N,H,do_majorant=N<=128 or (N==256 and H==256))
        assert v['sqrt_energy_distance_float']<=v['proved_Hilbert_radius']+1e-8
        out.append(v)
    pairs=fejer_pair_float([float(x) for x in original(32)],8)
    spec=fejer_weighted_spectrum([float(x) for x in original(32)],8)
    assert abs(pairs-spec)<1e-8
    models=[]
    for N in (128,256):
        H=N
        for kind,xx in [('H_isometric_nonnormal_shadow',[Fraction(n,(2*n-1)**4) for n in range(N)]),
                        ('periodic_1_over_17',[Fraction(pow(16,n,17),17) for n in range(N)])]:
            models.append({'N':N,'H':H,'type':kind,
                           'fejer_energy_float':round(fejer_weighted_spectrum([float(x) for x in xx],H),9),
                           'near_pairs_exact':near_pair_count(xx,H)})
    return {'scope':'EXACT finite rational source/Fejer majorants; FLOAT Fourier energies only',
            'preregistration':'1714487e01759cf0cc43afca3b9454af04cba261',
            'analytical_unconditional':'|sqrt(Cz)-sqrt(Cx)|<=4sqrt(H(H+1))/N',
            'infinite_source_collision_bound':'OPEN',
            'pi_normality':'OPEN',
            'cases':out,'hostile_models':models,
            'pair_vs_fourier_float_delta':abs(pairs-spec)}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
