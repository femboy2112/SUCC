"""Exact golden/Oily clock passports and matched-jet arithmetic controls."""
from fractions import Fraction as F
from math import comb
import json
import sympy as sp
import spectral_probe as s

x,z=sp.symbols('x z')
Q=4-2*sp.exp(-3*x)-sp.exp(-4*x)-sp.exp(-5*x)
Qmut=Q+(1-sp.exp(-x))**4
jets=[sp.diff(Q,x,j).subs(x,0) for j in range(5)]
mutjets=[sp.diff(Qmut,x,j).subs(x,0) for j in range(5)]
assert jets[:4]==mutjets[:4]
assert mutjets[4]-jets[4]==24
q=(3-sp.sqrt(5))/2
q3=(5-sp.sqrt(21))/6
assert sp.simplify((2-q)**(-2)-q)==0
assert sp.simplify((4-3*q3)**(-2)-q3)==0
assert sp.simplify((4-3*q)**(-2)-q)!=0
# Independent coefficient formula shared by every kernel with the same first3 jets.
A=(7+sp.Rational(-59,2)/15)/8
B=(sp.Rational(49,2)+7*sp.Rational(-59,2)/15+sp.Rational(81,2)/15)/64
D=z*(1-z)/2; E=-z*(1-z)*(2*z-1)/6; d=2-z
N1=2*A/d**3+6*D/d**4
N2=6*B/d**4+24*(A*D+E)/d**5+60*D**2/d**6
G1=sp.factor(N1-2*A/d**2)
G2=sp.factor(N2-2*A*N1+(4*A*A-6*B)/d**2)
alpha=sp.simplify(G1.subs(z,q)/(1-2/(2-q)**3))
beta=sp.simplify((3*alpha**2/(2-q)**4+sp.diff(G1,z).subs(z,q)*alpha+G2.subs(z,q))/(1-2/(2-q)**3))
assert sp.simplify(beta-(sp.Rational(6031,80)-sp.Rational(12139211,360000)*sp.sqrt(5)))==0
log_second=sp.simplify(5*B-2*A*A-sp.Rational(49,128))
assert log_second==sp.Rational(-3601,28800)
oily_second=sp.simplify(log_second-beta)

original=F(0); mutant=F(0); rows=[]
for n in range(1,32):
    a=8*n-7
    extra=sum((F((-1)**j*comb(4,j),a+j) for j in range(5)),F(0))
    assert extra>0
    original=16*original+s.r(n)
    mutant=16*mutant+s.r(n)+extra
    if n in (1,2,7,17,31):
        assert (mutant-original)%1!=0
        rows.append({"n":n,"source_extra":s.dump_fraction(extra),"phase_difference":s.dump_fraction((mutant-original)%1)})

# The coherent same-original-forcing seed has the same marks/geometry but
# lag energy bounded by2*pi^2*h^2*D_n^2. This is a rigorous source-only
# contrast; its irrational seed is not submitted to rational CRT reduction.
pl,pu=s.pi_interval()
coherent=[]
for A,N in ((61,127),(113,257),(229,509)):
    for h in (1,3,7):
        upper=2*pu*pu*h*h*F(256,(8*A+1)**6)
        assert upper<F(1,4)
        coherent.append({"A":A,"N":N,"h":h,"mean_energy_upper":s.dump_fraction(upper),"decimal_upper":float(upper)})

out={"status":"PASS exact source geometry and typed countermodels; no new selected saving",
     "author_provenance":"Leah / femboy2112; Harmonic Numbers, Golden Ratio, Euler-Mascheroni and Oily-Macaroni",
     "source_jets":[str(y) for y in jets],"quartic_mutant_jets":[str(y) for y in mutjets],
     "golden_clock1":str(q),"clock3":str(q3),"second_golden_coefficient":str(beta),
     "second_oily_coefficient":str(oily_second),"distinct_exact_mutant_phases":rows,
     "same_source_same_geometry_coherent_energy_bounds":coherent}
with open('geometry_control_receipt.json','x') as f:json.dump(out,f,indent=2)
print('PASS 5 jet levels, 2 clock roots, golden/Oily second coefficients, 5 exact mutant phases, 9 coherent bounds')
