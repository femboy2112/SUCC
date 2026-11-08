"""Dyadic source-selected Fourier energy-gap diagnostics, float only."""
import json
from fractions import Fraction
from math import pi,sin,cos,log
from random import Random
from prime_certificate import source

def source_phases(N):
 x=Fraction(0);out=[x]
 for n in range(1,N):
  step=16*x+source(n);x=step-(step.numerator//step.denominator);out.append(x)
 return out

def unit_phases(x,h):
 return [complex(cos(2*pi*h*float(t)),sin(2*pi*h*float(t))) for t in x]

def details(seq):
 N=len(seq);m=N.bit_length()-1;assert 2**m==N
 energies=[]
 for k in range(m+1):
  Q=1<<k;M=N//Q
  val=sum(abs(sum(seq[j+t*Q] for t in range(M))/M)**2 for j in range(Q))/Q
  energies.append(val)
 assert abs(energies[-1]-1)<1e-11
 assert all(energies[k+1]+1e-10>=energies[k] for k in range(m))
 ratios=[]
 for k in range(m):
  den=energies[k+1]
  ratios.append(max(0.0,min(1.0,(energies[k+1]-energies[k])/den)) if den>1e-14 else None)
 return energies,ratios

def run():
 out=[]
 for N in (128,256,512,1024):
  xs=source_phases(N); rng=Random(537111+N)
  other={
    'original_zero_BBP':xs,
    'isometric_H_shadow':[Fraction(n,(2*n-1)**4) for n in range(N)],
    'periodic_beta_1_17':[Fraction(pow(16,n,17),17) for n in range(N)],
    'synthetic_iid_seed':[rng.random() for _ in range(N)]}
  for key,x in other.items():
   for h in (1,2,3):
    e,g=details(unit_phases(x,h))
    gap_mass=sum(v for v in g if v is not None)
    count_ge_1_4=sum(v>=0.25 for v in g if v is not None)
    out.append({'N':N,'h':h,'sequence':key,'weyl_abs2_float':round(e[0],12),
                'gap_mass_sum_float':round(gap_mass,9),'levels_with_gap_at_least_quarter':count_ge_1_4,
                'level_count':len(g), 'gap_ratios_float':[round(v,5) if v is not None else None for v in g]})
 return {'label':'OBSERVED FINITE FLOAT DIAGNOSTIC, not proof',
         'original_source':True,'literal_U0':'0',
         'missing_infinite_source_selected_gap':'OPEN','rows':out}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
