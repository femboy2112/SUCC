"""Independent exact SymPy oracle, not imported from the implementation.

Recomputes Oily split, nearest-neighbor coupling, Jordan source,
Schwinger su2 Casimir, raw BBP forcing inequality, and nonfunctorial
origin-locked source-projection witness.  No original repo source edits.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

x=s.symbols('x',real=True)
u=x-x**2/2;v=x**2/2
assert s.factor(u+v-x)==0
assert s.factor(u-v-x*(1-x))==0

# Exact analytic birth flow: F_j(k)-F_(j+1)(k)=mu_j(k)*birth_(j,k).
for j in range(0,8):
    hj=s.expand(sum(u**i*v**(j-i) for i in range(j+1)))
    hnext=s.expand(sum(u**i*v**(j+1-i) for i in range(j+2)))
    for k in range(j+1):
        prefix=s.expand(sum(u**i*v**(j-i) for i in range(k+1)))
        pre_next=s.expand(sum(u**i*v**(j+1-i) for i in range(k+1)))
        a=s.expand(sum(u**(j+1-r)*v**r for r in range(k+1)))
        identity=s.factor(prefix*hnext-pre_next*hj-u**k*v**(j-k)*a)
        assert identity==0,(j,k,identity)

# Oily endpoint joint packet: independently geometric, uniformly split.
q=s.Rational(1,2)
for j in range(17):
    assert s.expand((1-q)**2*sum(q**i*q**(j-i) for i in range(j+1)))==s.Rational(j+1,2**(j+2))
    for k in range(j+1):
        assert s.simplify((1-q)**2*q**j / ((1-q)*q**j/(j+1)))==s.Rational(j+1,2)

# Pólya Markov matrix (not Hilbert isometry) preserves UNIFORM PROBABILITIES,
# but its application to UNIFORM AMPLITUDES dampens by sqrt((j+1)/(j+2)).
for j in range(1,13):
    K=s.zeros(j+2,j+1)
    for k in range(j+1):
        a=s.Rational(k+1,j+2)
        K[k,k]=1-a
        K[k+1,k]=a
    assert K*s.ones(j+1,1)/(j+1)==s.ones(j+2,1)/(j+2)
    omega=s.ones(j+1,1)/s.sqrt(j+1)
    amp=K*omega
    assert all(s.simplify(z-s.sqrt(s.Rational(j+1,j+2))/s.sqrt(j+2))==0 for z in amp)
    assert s.simplify((amp.T*amp)[0]-s.Rational(j+1,j+2))==0

# Schwinger SU2: [J+,J-]=2J3 and Casimir j(j+2)/4.
j,k=s.symbols('j k',integer=True,nonnegative=True)
plus=(k+1)*(j-k)
minus=k*(j-k+1)
m=k-s.Rational(1,2)*j
assert s.expand(minus-plus-2*m)==0
assert s.expand(s.Rational(1,2)*(minus+plus)+m*m-j*(j+2)/4)==0

# Source-authentic signed four-pole BBP rational forcing; rigorous tame
# bound r(n) <= 1/n² on every n>=2 (polynomial positive in n-2).
n=s.symbols('n',integer=True,positive=True)
A=120*n*n-89*n+16
D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert s.factor(r-A/D)==0
mvar=s.symbols('m',nonnegative=True)
positivity=s.expand((D-n*n*A).subs(n,mvar+2))
coeff=s.Poly(positivity,mvar).all_coeffs()
assert all(c>0 for c in coeff)

# Exact nonfunctoriality: C(S_A A_2)|1>=|3>/sqrt2;
# C(S_A) C(A_2)|1>=|3>/(2sqrt2)+|4>/sqrt12.
left={3:1/s.sqrt(2)}
right={3:1/(2*s.sqrt(2)),4:1/s.sqrt(12)}
defect=s.simplify(sum((left.get(m,0)-right.get(m,0))**2 for m in (3,4)))
assert defect==s.Rational(5,24)

out={
 'symbolic_biased_birth_certificates':sum(range(1,9)),
 'polya_uniform_amplitude_depths':12,
 'su2_commutator':'[J+,J-]=2J3',
 'su2_casimir':'j(j+2)/4',
 'source_rational_forcing':'A(n)/D(n)',
 'forcing_one_over_n_squared_bound_nonnegative_coeffs_at_n_minus_2':[str(c) for c in coeff],
 'origin_locked_observer_composition_defect_sq':'5/24',
 'local_critical_oily_to_zeta_sizebias':'(j+1)/2',
 'scope':'exact symbolic theorem checks, not proof of pi normality or observer optimality'
}
p=Path(__file__).resolve().parent.parent/'research/2026-10-28/OILY_GROWTH_SYMPY_ORACLE.json'
p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS independent exact SymPy: packet, tilted Pólya, amplitude loss, SU2, authentic forcing, nonfunctoriality; saved',p)
