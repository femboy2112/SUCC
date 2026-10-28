#!/usr/bin/env python3
"""Standalone exact finite certificates for three Round-2 arithmetic lemmas.

Only Python standard-library arithmetic; no repository import, numerical phase,
normality claim, or infinite theorem inferred from finite enumeration.
Run from any directory: python scripts/pi_prime7_exact_theorem_probe.py [--output PATH].
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json

POLES=((2,-1),(4,-1),(8,-7),(8,-3))
def A(x):return 120*x*x-89*x+16
def D(x):
 ans=1
 for a,b in POLES:ans*=a*x+b
 return ans

def cyclotomic_remainder(counts,p,L):
 """Exact integer reduction modulo Phi_(p^L)=sum_j X^(j*p^(L-1))."""
 q=p**L;step=q//p
 assert len(counts)==q
 out=counts[:]
 for u in range(step):
  top=out[u+(p-1)*step]
  for j in range(p):out[u+j*step]-=top
 assert not any(out[(p-1)*step:])
 return out[:(p-1)*step]

def sparse(vec):return {str(i):v for i,v in enumerate(vec) if v}
def residue_hist(exponents,q):
 out=[0]*q
 for n in exponents:out[n%q]+=1
 return out

def prime7_character_certificates():
 rows=[];p=7
 for L in range(1,5):
  q=p**L;c=89*pow(120,-1,q)%q;step=q//p
  R={x:A(x)*pow(D(x),-1,q)%q for x in range(q) if D(x)%p}
  regular_mirror=[x for x in R if (c-x)%q in R]
  assert regular_mirror==list(range(6,q,p))
  fibers=defaultdict(list)
  for x in R:fibers[A(x)%q].append(x)
  singleton=[f for f in fibers.values() if f[0]%p in (1,5)]
  central=[f for f in fibers.values() if f[0]%p==6]
  assert all(len(f)==1 for f in singleton)
  assert len(singleton)==2*q//p
  assert all(all(x%p==6 for x in f) for f in central)
  translation_checks=0
  if L>=2:
   for x in regular_mirror:
    t=(x+step)%q
    assert A(t)%q==A(x)%q
    assert (R[t]-R[x])%q==step
    fx=(R[x]-R[(c-x)%q])%q
    ft=(R[t]-R[(c-t)%q])%q
    assert (ft-fx)%q==2*step
    translation_checks+=1
  for a in (1,2,3,6):
   mirror_counts=residue_hist((a*(R[x]-R[(c-x)%q]) for x in regular_mirror),q)
   mirror_rem=cyclotomic_remainder(mirror_counts,p,L)
   central_rem=[cyclotomic_remainder(residue_hist((a*R[x] for x in f),q),p,L) for f in central]
   # Direct expansion of every fiber squared modulus gives an integer group-ring polynomial.
   energy_counts=residue_hist((a*(R[x]-R[y]) for f in fibers.values() for x in f for y in f),q)
   energy_rem=cyclotomic_remainder(energy_counts,p,L)
   expected=3 if L==1 else 2*q//p
   assert energy_rem==[expected]+[0]*(len(energy_rem)-1)
   if L==1:
    assert mirror_rem==[1]+[0]*(len(mirror_rem)-1)
    assert sum(not any(v) for v in central_rem)==0
    assert Q(expected,q)==Q(3,7)!=Q(2,7)
   else:
    assert not any(mirror_rem)
    assert all(not any(v) for v in central_rem)
    assert Q(expected,q)==Q(2,7)
   rows.append({'p':p,'L':L,'q':q,'character_multiplier':a,
    'regular_input_count':len(R),'regular_mirror_input_count':len(regular_mirror),
    'singleton_regular_fiber_count':len(singleton),'central_regular_fiber_count':len(central),
    'zero_central_character_fibers':sum(not any(v) for v in central_rem),
    'mirror_cyclotomic_remainder':sparse(mirror_rem),
    'fiber_energy_cyclotomic_remainder':sparse(energy_rem),
    'normalized_fiber_energy':str(Q(expected,q)),
    'translation_checks':translation_checks,
    'L1_false_extension_rejected':L==1})
 return rows

def zadd(a,b):return a[0]+b[0],a[1]+b[1]
def zsub(a,b):return a[0]-b[0],a[1]-b[1]
def norm(a):return a[0]*a[0]+a[1]*a[1]
def integer_gaussian_phases(N,variant):
 roots=((1,0),(0,1),(-1,0),(0,-1))
 return [roots[(n*n+3*n+(n//3 if variant else n//5)+variant)%4] for n in range(N)]
def binned_sums(phases,q,kind):
 out=[(0,0)]*q
 for n,z in enumerate(phases):
  key=(A(n) if kind=='A' else n)%q
  out[key]=zadd(out[key],z)
 return out

def refinement_certificates():
 rows=[]
 for p in (7,11):
  for L in (1,2):
   q=p**L;fine=p*q
   # Every chosen N is incomplete at fine depth, including N<q and N>fine.
   for N in (1,q-1,q+3,fine+5,2*fine-1):
    assert N%fine
    for kind in ('A','time'):
     for variant in (0,1):
      z=integer_gaussian_phases(N,variant)
      coarse=binned_sums(z,q,kind);children=binned_sums(z,fine,kind)
      assert all(coarse[b]==tuple(sum(children[b+j*q][k] for j in range(p)) for k in range(2)) for b in range(q))
      C=Q(q,N*N)*sum(map(norm,coarse))
      Cfine=Q(fine,N*N)*sum(map(norm,children))
      debt=Q(q,N*N)*sum(norm(zsub(children[b+i*q],children[b+j*q])) for b in range(q) for i in range(p) for j in range(i+1,p))
      assert Cfine-C==debt>=0
      rows.append({'p':p,'L':L,'q':q,'N':N,'partition':kind,'phase_variant':variant,
       'coarse_energy':str(C),'fine_energy':str(Cfine),'child_difference_energy':str(debt),
       'incomplete_N':True,'identity_exact':True})
 return rows

def vp(n,p,L):
 if n%p**L==0:return L
 out=0
 while n%p==0:out+=1;n//=p
 return out

def truncated_kernel_certificates():
 rows=[]
 for p in (7,11):
  for L in (1,2,3,4):
   q=p**L;b=89*pow(240,-1,q)%q
   fibers=defaultdict(list)
   for x in range(q):fibers[A(x)%q].append(x)
   # Every occupied fiber is wholly regular of one center valuation s, or is the critical fiber.
   classification=[]
   for value,cell in fibers.items():
    vals={vp((x-b)%q,p,L) for x in cell}
    if min(vals)*2>=L:
     assert len(cell)==p**(L//2)
     classification.append(('critical',None,cell))
    else:
     assert len(vals)==1
     s=next(iter(vals));assert 2*s<L and len(cell)==2*p**s
     classification.append(('regular',s,cell))
   assert sum(kind=='critical' for kind,s,cell in classification)==1
   regular_counts=Counter(s for kind,s,cell in classification if kind=='regular')
   assert dict(regular_counts)=={s:(p-1)*p**(L-2*s-1)//2 for s in range((L-1)//2+1)}
   for S in range((L-1)//2+1):
    selected=[cell for kind,s,cell in classification if kind=='regular' and s<=S]
    trace=sum(map(len,selected));opnorm=max(map(len,selected))
    row_sum_max=opnorm;frobenius_sq=sum(len(cell)**2 for cell in selected)
    assert trace==q-Q(q,p**(S+1))
    assert opnorm==2*p**S
    assert Q(frobenius_sq,q)==2*(S+1)*Q(p-1,p)
    # Build the full action without a dense q-by-q matrix, then verify norm attainment.
    largest=next(cell for cell in selected if len(cell)==opnorm)
    v={x for x in largest}
    Kv=[0]*q
    for cell in selected:
     scalar=sum(x in v for x in cell)
     for x in cell:Kv[x]=scalar
    assert sum(t*t for t in Kv)==opnorm*opnorm*len(v)
    assert sum(x!=0 for x in Kv)==len(v)
    # On arbitrary Gaussian input, verify a direct blockwise counting-measure norm bound.
    w=[((n*n+3*n)%7-3,(2*n*n+n)%11-5) for n in range(q)]
    Kwnorm=0;wnorm=sum(map(norm,w))
    for cell in selected:
     sw=(sum(w[x][0] for x in cell),sum(w[x][1] for x in cell))
     Kwnorm+=len(cell)*norm(sw)
    assert Kwnorm<=opnorm**2*wnorm
    rows.append({'p':p,'L':L,'q':q,'S':S,'selected_fibers':len(selected),
     'regular_fiber_classification':{str(s):{'fiber_size':2*p**s,'fiber_count':v} for s,v in sorted(regular_counts.items())},
     'critical_fiber_size':p**(L//2),'trace':trace,'trace_over_q':str(Q(trace,q)),
     'operator_norm':opnorm,'maximum_row_sum':row_sum_max,
     'positive_spectrum_multiplicities':dict(sorted(Counter(map(len,selected)).items())),
     'nullity':q-len(selected),'b_S':str(Q(frobenius_sq,q)),
     'norm_attainment_exact':True,'whole_fibers_retained':True,
     'critical_fiber_excluded':True,'gaussian_vector_norm_bound_exact':True})
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('pi_prime7_exact_theorem_receipt.json'));args=ap.parse_args()
 report={'status':'PASS: exact finite certificates; infinite proofs remain separate; pi normality OPEN',
 'arithmetic':'Python standard library integers and Fraction; no floats, no repository imports',
 'instrument_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'predeclared_domains':{'modular_source':{'p':7,'L':[1,2,3,4],'unit_multipliers':[1,2,3,6]},
 'refinement':{'p':[7,11],'L':[1,2],'partitions':['A','time'],'phases':'Gaussian units; incomplete N'},
 'truncation':{'p':[7,11],'L':[1,2,3,4],'S':'all S>=0 with 2S<L'}},
 'prime7_modular_source':prime7_character_certificates(),
 'incomplete_N_refinement':refinement_certificates(),
 'truncated_K_S':truncated_kernel_certificates()}
 args.output.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'status':'PASS','output':str(args.output),'rows':{key:len(report[key]) for key in ('prime7_modular_source','incomplete_N_refinement','truncated_K_S')},'instrument_sha256':report['instrument_sha256']},indent=2))
if __name__=='__main__':main()
