"""Optional exact certificate regeneration/check using SymPy; never overwrites files."""
import sympy as S,json,time
from pathlib import Path
x,y,s,p=S.symbols('x y s p')
A=lambda z:(8*z-7)**4;D=lambda z:(8*z-4)**2*(8*z-3)*(8*z-2)
f=S.Poly(S.cancel((A(x)*D(y)-A(y)*D(x))/(x-y)),x,y).primitive()[1].as_expr()
fsp=S.symmetrize(f,[x,y],formal=True);print('symmetrization',fsp,flush=True)
fs=fsp[0].subs({fsp[2][0][0]:s,fsp[2][1][0]:p});assert fsp[1]==0
f0=S.expand(fs);f1=S.expand(fs.subs({s:s+2,p:p+s+1},simultaneous=True));f2=S.expand(fs.subs({s:s+4,p:p+2*s+4},simultaneous=True));polys=[f0,f1,f2]
print('fs=',fs,flush=True)
g2=S.groebner(polys[:2],p,s);print('g2 degrees',[(S.degree(g,p),S.degree(g,s)) for g in g2],flush=True)
print('g2 factor last',S.factor(g2.polys[-1].as_expr()),flush=True)
for degree in range(0,6):
    monoms=[s**i*p**j for i in range(degree+1) for j in range(degree+1-i)]
    columns=[S.Poly(a*b,s,p) for a in polys for b in monoms]
    allmon=sorted(set().union(*(set(c.monoms()) for c in columns)),reverse=True)
    M=S.Matrix([[c.coeff_monomial(mon) for c in columns] for mon in allmon]);rhs=S.Matrix([int(mon==(0,0)) for mon in allmon])
    t=time.time()
    try: sol,params=M.gauss_jordan_solve(rhs)
    except ValueError: print('no degree',degree,'time',time.time()-t,flush=True);continue
    sol=sol.subs({symbol:0 for symbol in params});den=S.ilcm(*(S.denom(c) for c in sol));ints=[int(c*den) for c in sol]
    h=[S.expand(sum(ints[k*len(monoms)+i]*monoms[i] for i in range(len(monoms)))) for k in range(3)]
    assert S.expand(sum(a*b for a,b in zip(h,polys)))==den
    print('CERT DEG',degree,'constant digits',len(str(den)),'terms',[len(S.Poly(g,s,p).terms()) for g in h],flush=True)
    break
# infinity value u=1: gcd(A-D, shifted A-D)=1; extended Euclid.
q0=A(x)-D(x);q1=q0.subs(x,x+1)
i0,i1,ig=S.gcdex(q0,q1,x);assert ig==1
iden=S.ilcm(*(S.denom(c) for z in (i0,i1) for c in S.Poly(z,x).all_coeffs()))
I=[S.expand(z*iden) for z in (i0,i1)]
# Immersion: source ramification includes the double pole at 1/2.
c0=(8*x-7)*(2*x-1)*(120*x*x-89*x+16);c1=c0.subs(x,x+1)
e0,e1,eg=S.gcdex(c0,c1,x);assert eg==1
eDen=S.ilcm(*(S.denom(c) for z in (e0,e1) for c in S.Poly(z,x).all_coeffs()));E=[S.expand(z*eDen) for z in (e0,e1)]
def bt(poly):return [[int(i),int(j),int(c)] for (i,j),c in S.Poly(poly,s,p).terms()]
def ut(poly):return [int(c) for c in reversed(S.Poly(poly,x).all_coeffs())]
result={'collision_f':bt(fs),'multipliers':[bt(a) for a in h],'constant':int(den),
        'infinity_multipliers':[ut(z) for z in I],'infinity_constant':int(iden),
        'immersion_multipliers':[ut(z) for z in E],'immersion_constant':int(eDen),
        'two_frame_groebner':[str(g) for g in g2],
        'scope':'exact polynomial identities; global complex three-frame embedding certificate'}
stored=json.loads((Path(__file__).resolve().parent/'GLOBAL_DELAY_CERTIFICATE.json').read_text())
assert result==stored, 'regenerated certificate differs from the committed certificate'
print('EXACT_CERTIFICATE_REGENERATION_PASS',flush=True)
print('Infinity/immersion certificates',len(str(iden)),len(str(eDen)),flush=True)
