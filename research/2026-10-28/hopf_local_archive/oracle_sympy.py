"""Independent symbolic derivation from PR #333 source-sector rule.

Optional extra check, requires SymPy. Intentionally does not import the main
implementation when deriving its matrix (only when comparing the final result).
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as S
from hopf_source_exact import T, SOURCE_ORIGIN, t_iter, source_tap, H, hopf


a,b,c,d=S.symbols('a b c d',real=True)
z=a+S.I*b
w=c+S.I*d
u=S.expand((z+S.conjugate(w))/2)
v=S.expand((z-S.conjugate(w))/2)
g=(1+S.I)/2
# Original source rule: even u -> g*u; odd v -> g*conj(v)
new_u=S.expand(g*u)
new_v=S.expand(g*S.conjugate(v))
new_z=S.expand(new_u+new_v)
new_w=S.expand(S.conjugate(new_u)-S.conjugate(new_v))
source_vector=S.Matrix([S.re(new_z),S.im(new_z),S.re(new_w),S.im(new_w)])
T_derived=source_vector.jacobian([a,b,c,d])
T_computed=S.Matrix([[S.Rational(v.numerator,v.denominator) for v in row] for row in T])
assert T_derived==T_computed
assert T_derived.T*T_derived==S.eye(4)/2
assert T_derived.det()==-S.Rational(1,4)
assert T_derived**8==S.eye(4)/16
assert S.expand(T_derived.charpoly().as_expr()-(S.Symbol('lambda')**2-S.Rational(1,2))*(S.Symbol('lambda')**2-S.Symbol('lambda')+S.Rational(1,2)))==0

J=S.Matrix([[0,0,1,0],[0,0,0,-1],[1,0,0,0],[0,-1,0,0]])
assert T_derived**4==-J/4


def qm(q,t):
    A,B,C,D=q;E,F,G,H=t
    return S.Matrix([A*E-B*F-C*G-D*H,A*F+B*E+C*H-D*G,
                     A*G-B*H+C*E+D*F,A*H+B*G-C*F+D*E])

one=S.Matrix([1,0,0,0]);qi=S.Matrix([0,1,0,0]);qj=S.Matrix([0,0,1,0]);qk=S.Matrix([0,0,0,1]);
L=one-qk;R=one+qi
for e in (one,qi,qj,qk):
    assert S.simplify(T_derived*T_derived*e-qm(qm(L,e),R)/4)==S.zeros(4,1)

A=2*T_derived**2
c=A*one
cbar=S.Matrix([c[0],-c[1],-c[2],-c[3]])
M=S.Matrix.hstack(*(qm(A*e,cbar) for e in (one,qi,qj,qk)))
# Match hand-derived quaternion rotation by (1-k) about k axis.
expected=S.Matrix([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
assert M==expected
assert M**4==S.eye(4)

# Compare first-shell signed readout independently, symbolic matrix powers.
readout=S.Matrix([[2,-2,2,-2]])
origin=S.Matrix([2,0,0,0])
expected_taps=[4,0,0,-2,-1,-1,0,0]
assert [(readout*(T_derived**n)*origin)[0] for n in range(8)]==expected_taps

result={
    "PR333_source_sector_derived_T": [[str(T_derived[i,j]) for j in range(4)] for i in range(4)],
    "det_T":str(T_derived.det()),
    "conformal_gram":str(T_derived.T*T_derived),
    "charpoly":str(S.factor(T_derived.charpoly().as_expr())),
    "T4_chirality":True,
    "T8_return":True,
    "T_squared_exact_quaternion_factor":True,
    "induced_even_Hopf_base_action": [[str(M[i,j]) for j in range(4)] for i in range(4)],
    "induced_even_action_order":4,
    "first_eight_source_taps":expected_taps,
    "method":"independent symbolic Gaussian-sector derivation, then comparison with stand-alone Fraction implementation",
}
out=Path(__file__).with_name('oracle_sympy_results.json')
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS independent SymPy derivation: source T, orientation, conformality, cycles, quaternion factor, Hopf rotation')
