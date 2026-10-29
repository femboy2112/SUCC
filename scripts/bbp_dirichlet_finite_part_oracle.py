"""Independent exact+numeric oracle: authentic 4-pole BBP Dirichlet response.

Proof is in the accompanying dossier.  SymPy gives independent exact
partial fractions, asymptotic coefficients and rational digamma reduction.
High-precision mpmath numerics cross-check, not a proof of continuation.
"""
import json
from pathlib import Path
import sympy as s
import mpmath as mp

n,t=s.symbols('n t',integer=True,positive=True)
A=120*n*n-89*n+16
D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert s.factor(r-A/D)==0

# Compute source coefficients symbolically, no fitting.
asy=s.series(r.subs(n,1/t),t,0,7).removeO()
a2=s.expand(asy).coeff(t,2)
a3=s.expand(asy).coeff(t,3)
a4=s.expand(asy).coeff(t,4)
assert (a2,a3,a4)==(s.Rational(15,64),s.Rational(151,512),s.Rational(1209,4096))

B=[(s.Rational(7,16),s.Rational(1,8)),(-s.Rational(1,8),s.Rational(1,2)),(-s.Rational(3,64),s.Rational(5,8)),(-s.Rational(1,32),s.Rational(3,4))]
assert s.factor(n*r-sum(b/(n-(1-z)) for b,z in B))==0
assert sum((b for b,_ in B),s.Rational(0))==a2

finite_part=-sum((b*s.digamma(z) for b,z in B),s.Rational(0))
closed=(s.Rational(15,64)*s.EulerGamma
        + (27+31*s.sqrt(2))*s.pi/128
        + s.Rational(39,32)*s.log(2)
        + 31*s.sqrt(2)*s.log(1+s.sqrt(2))/64)
# SymPy may retain a logarithm of 2±sqrt(2); reduce via the explicit
# positive-real identity (2+sqrt2)/(2-sqrt2)=(1+sqrt2)^2.
expanded=(s.Rational(15,64)*s.EulerGamma
         + s.Rational(27,128)*s.pi
         + 31*s.sqrt(2)*s.pi/128
         + s.Rational(39,32)*s.log(2)
         + 31*s.sqrt(2)*(s.log(2+s.sqrt(2))-s.log(2-s.sqrt(2)))/128)
assert s.simplify(s.expand_func(finite_part)-expanded)==0
assert s.simplify((2+s.sqrt(2))/(2-s.sqrt(2))-(1+s.sqrt(2))**2)==0

mp.mp.dps=60
mpB=[(mp.mpf(int(b.p))/int(b.q),mp.mpf(int(z.p))/int(z.q)) for b,z in B]
Cdig=-sum(b*mp.digamma(z) for b,z in mpB)
Cclosed=mp.mpf(15)/64*mp.euler + (27+31*mp.sqrt(2))*mp.pi/128 + mp.mpf(39)/32*mp.log(2) + 31*mp.sqrt(2)/64*mp.log(1+mp.sqrt(2))
assert abs(Cclosed-Cdig)<mp.mpf('1e-55')

# A finite original-source sum vs infinite digamma value, with a sound
# (though conservative) tail bound based on exact B_a partial fractions.
N=4000
partial=mp.mpf(15)/64*mp.euler
for ni in range(1,N+1):
    partial+=sum(b*(1/(ni-(1-z))-1/mp.mpf(ni)) for b,z in mpB)
# |sum_(n>N) δ_n| <= (sum |B_a| a_a)*8/N for n>=1.
const=sum((abs(b)*(1-z) for b,z in B),s.Rational(0))
tail_upper=mp.mpf(int(const.p))/int(const.q)*8/N
assert abs(partial-Cdig)<tail_upper

out={
 'source_r(n)':'4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)',
 'a2':str(a2),'a3':str(a3),'a4':str(a4),
 'convergent_halfplane':'Re s > -1',
 'meromorphic_continuation':'C, possible simple poles s=1-k for integers k>=2 with residues a_k',
 'principal_pole':'s=-1; residue 15/64',
 'finite_part_digamma':str(finite_part),
 'finite_part_closed':str(closed),
 'finite_part_value_50digits':mp.nstr(Cdig,51),
 'numerical_finite_partial_n':N,
 'rigorous_partial_error_bound':mp.nstr(tail_upper,18),
 'independent_sympy_closed_form_equality':True,
 'status':'PAPER_PROVED via source partial fractions and classical digamma; no RH/normality consequence'
}
p=Path(__file__).resolve().parent.parent/'research/2026-10-28/ORIGINAL_BBP_DIRICHLET_FINITE_PART_RECEIPT.json'
p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS independent exact SymPy and 60-digit mpmath finite-part oracle; finite-sum tail bound checked. Closed C =',mp.nstr(Cdig,30))
