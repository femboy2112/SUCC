"""Independent SymPy construction; no imports from adic_transduction.

Confirms finite symbolic claims and held-out prime events, not universal
quantifiers or external refereeing. Exits nonzero on an assertion failure.
"""
from __future__ import annotations
import json
from sympy import symbols, expand, simplify, Rational, Matrix, eye, factor, diff

n,t,p=symbols('n t p', integer=True, positive=True)
Q=4-2*t**3-t**4-t**5
H=4+4*t+4*t*t+2*t**3+t**4
Qstar=Q+(1-t)**2
Hstar=H+(1-t)
assert expand(Q-(1-t)*H)==0
assert expand(Qstar-(1-t)*Hstar)==0
assert Q.subs(t,1)==Qstar.subs(t,1)==0
assert diff(Q,t).subs(t,1)==diff(Qstar,t).subs(t,1)==-15
M=Matrix([[0,1],[1,-1]])
I=eye(2)
def poly_matrix(pol,matrix):
    f=pol.as_poly(t)
    return sum((coef*matrix**power for (power,),coef in f.terms()),Matrix.zeros(2))
assert poly_matrix(H,M)==8*I+M
assert poly_matrix(Hstar,M)==9*I
assert poly_matrix(H,M).det()==55
assert poly_matrix(Hstar,M).det()==81

original=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
source_native=Rational(120)*n*n-89*n+16
source_native /= (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
assert simplify(original-source_native)==0
mutation=1/(8*n-7)-2/(8*n-6)+1/(8*n-5)
assert simplify(mutation - 2/((8*n-7)*(8*n-6)*(8*n-5)))==0

square_clock=(p*p+7)/8
at_clock=simplify(original.subs(n,square_clock))
mutant_clock=simplify((original+mutation).subs(n,square_clock))
assert simplify(at_clock-(4/p**2 - 2/(p**2+3)-1/(p**2+4)-1/(p**2+5)))==0
assert simplify(p**6*(mutant_clock-at_clock)-2*p**4/((p*p+1)*(p*p+2)))==0

# Laurent jets at infinity: substitute p=1/z and expand near z=0.
z=symbols('z',positive=True)
jet=at_clock.subs(p,1/z).series(z,0,7)
mutant_jet=mutant_clock.subs(p,1/z).series(z,0,7)
assert simplify(jet.removeO().coeff(z,4)-15)==0
assert simplify(mutant_jet.removeO().coeff(z,4)-15)==0
assert simplify((mutant_jet-jet).removeO().coeff(z,6)-2)==0

checks=0
for prime in [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,127,151,173,199]:
    assert (prime*prime-1)%8==0
    P2=prime*prime
    for mutated, expected in [(False,4),(True,5)]:
        rr=(mutant_clock if mutated else at_clock).subs(p,prime)
        rr=Rational(rr)
        num,den=rr.p,rr.q
        v=0
        while num%prime==0:
            num//=prime;v+=1
        while den%prime==0:
            den//=prime;v-=1
        assert v==-2
        xx=P2*rr
        assert xx.q%prime
        assert (xx.p*pow(int(xx.q),-1,prime))%prime==expected
        checks+=1

print(json.dumps({
  'source':'unchanged original four-pole BBP forcing',
  'Qfactor_and_first_jet':'PASS',
  'source_matrix_original_det':55,
  'source_matrix_mutant_det':81,
  'independent_native_source_formula':'PASS',
  'p_square_jet_original':str(jet),
  'p_square_jet_mutant':str(mutant_jet),
  'heldout_p_square_residue_cases':checks,
  'verdict':'PASS',
},indent=2))
