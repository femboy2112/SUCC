#!/usr/bin/env python3
"""Independent finite source-fiber receipt. Stdlib exact arithmetic.

Identity pass/fail rules are predefined below; observational sign/size flags
are finite falsification probes, never tests of normality or asymptotics.
Shared primitive: inherited phase_interval (rational Machin/Taylor enclosure).
No floating-point input to any phase calculation. Decimal text is display only.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal, localcontext
import argparse, hashlib, importlib.util, json, time, os
from math import comb

ROOT=Path(__file__).resolve().parents[1]
PRIMITIVE=ROOT/'scripts/pi_signed_cancellation_probe.py'
spec=importlib.util.spec_from_file_location('shared_phase_primitive',PRIMITIVE)
shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)
POLES=((2,-1),(4,-1),(8,-7),(8,-3))
CONFIG={'prime_depths':[(7,1),(11,1),(13,1),(241,1),(7,2),(7,3)],
 'N_multipliers':[2,4,8],'frequencies':[1,2],
 'phase_bits':48,'phase_order':40,'tail_terms':16,
 'identity_checks':'exact source identities, exact Gaussian signed decomposition, interval intersection and Cauchy enclosures',
 'predeclared_falsification_flags':{
  'all_nonpositive_authentic_mirror':'FAIL if any authentic prime off-diagonal lower endpoint > 0',
  'authentic_beats_each_coherent_control':'FAIL rowwise if authentic C lower endpoint exceeds a control C upper endpoint',
  'monotone_authentic_C_on_doubling':'FAIL if later C lower endpoint exceeds prior C upper endpoint',
  'two_sheet_prime_power_formula':'FAIL if omitted mixed-stratum signed interval excludes zero'},
 'interpretation':'All size/sign tests are finite descriptive falsifiers; no universal estimate is certified.'}

def A(n):return 120*n*n-89*n+16
def forcing(n):return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
def fake320_tail(n):return Q(n+1,(2*n+1)*(4*n+1)*(8*n+1))
def authentic_states(N):
 out=[Q(0)]
 for n in range(1,N+1):
  r=forcing(n);assert r==Q(A(n),D(n))
  out.append(16*out[-1]+r)
 return out

def D(n):
 v=1
 for a,b in POLES:v*=a*n+b
 return v

def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def scale(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def sq(a):return shared.square_interval(a)
def dot(z,w):return add(mul(z[0],w[0]),mul(z[1],w[1]))
def sums(zs):
 re=(Q(0),Q(0));im=(Q(0),Q(0))
 for z in zs:re=add(re,z[0]);im=add(im,z[1])
 return re,im
def norm(z):return add(sq(z[0]),sq(z[1]))
def isum(vs):
 ans=(Q(0),Q(0))
 for v in vs:ans=add(ans,v)
 return ans

def interval_json(x):
 lo,hi=shared.outward(*x,40)
 with localcontext() as ctx:
  ctx.prec=18
  disp=[str(Decimal(t.numerator)/Decimal(t.denominator)) for t in (lo,hi)]
 return {'rational':[str(lo),str(hi)],'decimal':disp,'sign':'positive' if lo>0 else 'negative' if hi<0 else 'contains_zero'}
def intersects(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def vp(n,p,L):
 if n==0:return L
 k=0
 while k<L and n%p==0:n//=p;k+=1
 return k

def poly_mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def determinant(M):
 """Bareiss integer determinant with pivoting, independent of resultant formula."""
 a=[r[:] for r in M];n=len(a);sign=1;last=1
 for k in range(n-1):
  if not a[k][k]:
   swap=next(i for i in range(k+1,n) if a[i][k])
   a[k],a[swap]=a[swap],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    val=a[i][j]*pivot-a[i][k]*a[k][j]
    assert val%last==0
    a[i][j]=val//last
   a[i][k]=0
  last=pivot
 return sign*a[-1][-1]

def resultant(a,b):
 # Input ascending coefficients, standard Sylvester row order.
 a=a[::-1];b=b[::-1];m=len(a)-1;n=len(b)-1;mat=[]
 for k in range(n):mat.append([0]*k+a+[0]*(n-1-k))
 for k in range(m):mat.append([0]*k+b+[0]*(m-1-k))
 return determinant(mat)

def poly_reflect(a,c):
 out=[Q(0)]*len(a)
 for i,v in enumerate(a):
  for j in range(i+1):out[j]+=v*comb(i,j)*c**(i-j)*(-1)**j
 return out

def padadd(a,b,sign=1):
 return [(a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def source_algebra():
 den=[1]
 for a,b in POLES:den=poly_mul(den,[b,a])
 nums=[16,-89,120]
 factor_res=[resultant(nums,[b,a]) for a,b in POLES]
 whole=resultant(nums,den)
 derivative=[i*den[i] for i in range(1,len(den))]
 discriminant=resultant(den,derivative)//den[-1]
 # dehomogenize degree-four homogeneous F,G at X=1, independently.
 f=[0,0,120,-89,16];g=[1]
 for a,b in POLES:g=poly_mul(g,[a,b])
 homogeneous=resultant(f,g)
 assert factor_res==[6,20,1920,-32]
 assert whole==-2**15*3**2*5**2
 assert discriminant==2**24*3**2*5**2
 assert homogeneous==-2**33*3**2*5**2
 assert all(forcing(n)==Q(A(n),D(n)) for n in range(1,1000))
 # Independent exact coefficient check, not a sample or symbolic-library oracle.
 reflected=poly_reflect(den,Q(89,120))
 difference=padadd(den,reflected,-1)
 selector=poly_mul([-89,240],[930*16-1243,-930*89,930*120])
 rhs=[-Q(v,50625) for v in selector]+[Q(0)]
 assert difference==rhs
 return {'denominator_mirror_identity':'D(x)-D(89/120-x)=-(240x-89)(930A(x)-1243)/50625',
 'rational_source_cross_product_identity':'A(x)D(89/120-x)-A(89/120-x)D(x)=(240x-89)A(x)(930A(x)-1243)/50625',
 'factor_resultants':factor_res,'resultant_A_D':whole,'discriminant_D':discriminant,'homogeneous_resultant':homogeneous,'denominator_coefficients_ascending':den}

def projective_key(a,b,p,q):
 if b%p:return ('finite',a*pow(b,-1,q)%q)
 assert a%p, 'bad reduction: simultaneous nonunits'
 return ('infinite_chart',b*pow(a,-1,q)%q)

def homogeneous(x,y):
 f=y*y*(120*x*x-89*x*y+16*y*y);g=1
 for a,b in POLES:g*=a*x+b*y
 return f,g

def geometry(p,L):
 q=p**L;fib=defaultdict(list)
 for n in range(q):fib[A(n)%q].append(n)
 pairs=[(r,s) for cell in fib.values() for r in cell for s in cell]
 expected=q+L*(p-1)*p**(L-1)
 assert len(pairs)==expected
 c=89*pow(120,-1,q)%q
 strata=Counter((vp((r-s)%q,p,L),vp((120*(r+s)-89)%q,p,L)) for r,s in pairs)
 assert all(a+b>=L for a,b in strata)
 pole_res=[n for n in range(q) if D(n)%p==0]
 assert all(A(n)%p for n in pole_res)
 projective_domain=[(x,1) for x in range(q)]+[(1,y) for y in range(0,q,p)]
 pfib=Counter(projective_key(*homogeneous(x,y),p,q) for x,y in projective_domain)
 affine_map=Counter(projective_key(A(n),D(n),p,q) for n in range(q))
 # Only denominator-unit points can be compared by an ordinary rational residue.
 regular_pairs=[(r,s) for r,s in pairs if D(r)%p and D(s)%p]
 rational_same=sum(A(r)*D(s)%q==A(s)*D(r)%q for r,s in regular_pairs)
 mirror_break=sum(D(n)%q!=D((c-n)%q)%q for n in range(q))
 return {'p':p,'L':L,'q':q,'numerator_collision_count':len(pairs),'collision_formula':expected,
 'numerator_fiber_size_histogram':dict(sorted(Counter(map(len,fib.values())).items())),
 'pair_valuation_strata':{f'{a},{b}':v for (a,b),v in sorted(strata.items())},
 'D_nonunit_residue_count':len(pole_res),'A_zero_count_mod_q':sum(A(n)%q==0 for n in range(q)),
 'A_D_common_zero_mod_p_count':sum(A(n)%p==0 and D(n)%p==0 for n in range(p)),
 'D_mirror_break_count_mod_q':mirror_break,
 'projective_source_mirror_equal_count':sum((A(n)*D((c-n)%q)-A((c-n)%q)*D(n))%q==0 for n in range(q)),
 'denominator_mirror_equal_residues':[n for n in range(q) if (D(n)-D((c-n)%q))%q==0],
 'regular_A_pairs':len(regular_pairs),'regular_A_pairs_preserving_rational_source':rational_same,
 'affine_projective_source_collision_count':sum(v*v for v in affine_map.values()),
 'full_projective_domain_size':len(projective_domain),'full_projective_source_collision_count':sum(v*v for v in pfib.values()),
 'full_projective_source_fiber_histogram':dict(sorted(Counter(pfib.values()).items()))},pairs

def changed_tail_interval(n):
 # This also covers n=0: the first omitted term has index >=17, so r(m)<1/m² applies.
 terms=CONFIG['tail_terms']
 lo=sum((forcing(n+j)/16**j for j in range(1,terms+1)),Q(0))
 return lo,lo+Q(1,15*16**terms*(n+terms+1)**2)

def phase(q):return shared.phase_interval(q,CONFIG['phase_bits'],CONFIG['phase_order'])
def changed_phase(n,h):
 lo,hi=changed_tail_interval(n);mid=-(lo+hi)/2
 box=phase(h*mid)
 # Each sin/cos derivative in phase variable has magnitude <=2π<44/7.
 debt=Q(44,7)*abs(h)*(hi-lo)/2
 return tuple((max(Q(-1),a-debt),min(Q(1),b+debt)) for a,b in box)

def energy_row(boxes,p,L,pairs):
 N=len(boxes);q=p**L;factor=Q(q,N*N)
 Z=[sums(boxes[r::q]) for r in range(q)]
 fibers=defaultdict(list)
 for r in range(q):fibers[A(r)%q].append(Z[r])
 rawC=isum(norm(sums(vs)) for vs in fibers.values())
 rawE=isum(norm(z) for z in Z)
 rawOff=isum(dot(Z[r],Z[s]) for r,s in pairs if r!=s)
 rawMirror=isum(dot(Z[r],Z[s]) for r,s in pairs if r!=s and (120*(r+s)-89)%q==0)
 rawMixed=isum(dot(Z[r],Z[s]) for r,s in pairs if r!=s and (120*(r+s)-89)%q!=0)
 assert intersects(rawC,add(rawE,rawOff))
 assert intersects(rawOff,add(rawMirror,rawMixed))
 full=scale(norm(sums(boxes)),Q(1,N*N))
 C=scale(rawC,factor);E=scale(rawE,factor)
 # Cauchy gives W<=C (certified enclosures must not prove the contrary).
 assert full[0]<=C[1]
 if L==1:
  b=89*pow(240,-1,q)%q;c=89*pow(120,-1,q)%q
  mirror_all=isum(dot(Z[r],Z[(c-r)%q]) for r in range(q))
  rhs=add(add(rawE,mirror_all),neg(norm(Z[b])))
  assert intersects(rawC,rhs)
 return {'N':N,'q':q,'C':C,'E':E,'offdiag':scale(rawOff,factor),
  'full_mirror_offdiag':scale(rawMirror,factor),'mixed_strata_offdiag':scale(rawMixed,factor),'Weyl_square':full}

def gaussian_identity(p,L,pairs):
 q=p**L
 # Exact rational Gaussian values distinct from PR325's toy phases.
 vals=[(Q((n*n+3*n+2)%7-3,5),Q((2*n*n+n)%11-5,7)) for n in range(5*q)]
 boxes=[((a,a),(b,b)) for a,b in vals]
 row=energy_row(boxes,p,L,pairs)
 assert row['C'][0]==row['C'][1]
 assert row['C'][0]==row['E'][0]+row['offdiag'][0]
 assert row['offdiag'][0]==row['full_mirror_offdiag'][0]+row['mixed_strata_offdiag'][0]
 return {key:str(row[key][0]) for key in ('C','E','offdiag','full_mirror_offdiag','mixed_strata_offdiag')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('pi_prime7_source_fiber_receipt.json'));args=ap.parse_args()
 start=time.time();maxN=max(p**L for p,L in CONFIG['prime_depths'])*max(CONFIG['N_multipliers'])
 report={'status':'FINITE_EXACT_INSTRUMENT; NORMALITY OPEN','config':CONFIG,
 'instrument_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'shared_components':['phase_interval','outward rounding','square_interval'],
 'independent_components':['original signed source recurrence and seed','A/D factor algebra','Bareiss/Sylvester resultants','projective fiber enumeration','signed fiber/mirror/valuation energy assembly','tail-error certification'],
 'shared_primitive_path':str(PRIMITIVE.relative_to(ROOT)),'shared_primitive_sha256':hashlib.sha256(PRIMITIVE.read_bytes()).hexdigest(),
 'source_algebra':source_algebra(),'geometry':[],'gaussian_identity':[],'rows':[],'finite_flags':[]}
 geoms={}
 for p,L in CONFIG['prime_depths']:
  geo,pairs=geometry(p,L);report['geometry'].append(geo);geoms[p,L]=pairs
  report['gaussian_identity'].append({'p':p,'L':L,**gaussian_identity(p,L,pairs)})
 states=authentic_states(maxN-1)
 for h in CONFIG['frequencies']:
  print(f'Preparing certified h={h} boxes through N={maxN}',flush=True)
  controls={'authentic':[phase(h*u) for u in states],
   'coherent_one':[((Q(1),Q(1)),(Q(0),Q(0)))]*maxN,
   'changed_seed_minus_T':[changed_phase(n,h) for n in range(maxN)],
   'pc320_mutant':[phase(-h*fake320_tail(n)) for n in range(maxN)]}
  for p,L in CONFIG['prime_depths']:
   previous=None
   for mult in CONFIG['N_multipliers']:
    N=mult*p**L;rows={name:energy_row(boxes[:N],p,L,geoms[p,L]) for name,boxes in controls.items()}
    auth=rows['authentic']
    report['finite_flags'].append({'p':p,'L':L,'h':h,'N':N,
      'authentic_offdiag_certifiably_positive':auth['offdiag'][0]>0,
      'authentic_offdiag_certifiably_negative':auth['offdiag'][1]<0,
      'authentic_C_certifiably_below_each_control':all(auth['C'][1]<v['C'][0] for k,v in rows.items() if k!='authentic'),
      'authentic_C_certifiably_above_any_control':any(auth['C'][0]>v['C'][1] for k,v in rows.items() if k!='authentic'),
      'authentic_C_certifiably_increased_on_doubling':previous is not None and auth['C'][0]>previous[1],
      'two_sheet_omission_certifiably_nonzero':L>1 and (auth['mixed_strata_offdiag'][0]>0 or auth['mixed_strata_offdiag'][1]<0)})
    previous=auth['C']
    for name,row in rows.items():
     report['rows'].append({'model':name,'p':p,'L':L,'h':h,**{key:interval_json(v) if isinstance(v,tuple) else v for key,v in row.items()}})
    print(f'completed p={p},L={L},h={h},N={N}',flush=True)
 report['elapsed_seconds_display_only']=str(round(time.time()-start,3))
 args.output.write_text(json.dumps(report,indent=2)+'\n')
 print(f'PASS: exact identities and certified enclosures; finite-only receipt {args.output}',flush=True)
if __name__=='__main__':main()
