"""Independent symbolic oracle for the new four-pole nine research.

Rebuilds the source and operator identities directly in SymPy, not by
importing observational_succ.four_pole_nine. Writes deterministic JSON.
No floating-point inference is treated as proof authority.
"""
from itertools import combinations
import json
from pathlib import Path
import sympy as S

A,B = S.symbols('a b', positive=True)
shifts=(0,3,4,5)
cs=(4,-2,-1,-1)
P=S.eye(4)-S.ones(4)/4
D=lambda x:S.diag(*[(x+t)/(x+t+8) for t in shifts])
M=lambda x:P*D(x)*P

# 1. Two independent representations of the actual signed source.
R=lambda x:sum((S.Rational(c)/(x+t) for c,t in zip(cs,shifts)),S.Integer(0))
positive=sum((S.Rational(w)*d/(A*(A+d)) for d,w in [(3,2),(4,1),(5,1)]),S.Integer(0))
assert S.cancel(R(A)-positive)==0
Q=S.symbols('x')
Qf=4-2*S.exp(-3*Q)-S.exp(-4*Q)-S.exp(-5*Q)
jets=[S.diff(Qf,Q,k).subs(Q,0) for k in (1,2,3)]
assert jets==[15,-59,243]

# The source-mutated positive kernel changes higher jets without changing the first two.
Qmut=Qf+S.exp(-6*Q)*(1-S.exp(-Q))**3
assert S.diff(Qmut,Q).subs(Q,0)==jets[0]
assert S.diff(Qmut,Q,2).subs(Q,0)==jets[1]
assert S.diff(Qmut,Q,3).subs(Q,0)==jets[2]+6

# 2. Rigid original poles (2,1,1) with the original two moments.
solution=[]
for x in range(1,20):
    for y in range(1,20):
        for z in range(y,20):
            if 2*x+y+z==15 and 2*x*x+y*y+z*z==59:
                solution.append((x,y,z))
assert solution==[(3,4,5)]

# 3. Completely independent symbolic construction of projected clock commutator.
C=S.simplify(M(A)*M(B)-M(B)*M(A))
ua=P*S.Matrix([(A+t)/(A+t+8) for t in shifts])
ub=P*S.Matrix([(B+t)/(B+t+8) for t in shifts])
C2=-S.Rational(1,4)*(ua*ub.T-ub*ua.T)
assert all(S.cancel(C[i,j]-C2[i,j])==0 for i in range(4) for j in range(4))

# 4. Vandermonde route from 3x3 Cauchy-Binet, independently of square root norms.
op2=S.cancel(-S.trace(C*C)/2)
vd=S.Integer(0)
for i,j,k in combinations(shifts,3):
    V=(j-i)*(k-i)*(k-j)
    den=S.prod((A+8+t)**2*(B+8+t)**2 for t in (i,j,k))
    vd+=S.Integer(V*V)/den
claim=64*(A-B)**2*vd
assert S.cancel(op2-claim)==0
assert S.factor(op2.subs({A:1,B:9})) == S.Rational(11541128,258600651534225)
assert S.factor(C[0,1].subs({A:1,B:9})) == -S.Rational(283,2297295)

# 5. The explicit curvature coefficient for consecutive clock steps.
lead=S.simplify(S.limit(A**6*C.subs(B,A+8)[0,1],A,S.oo))
assert lead==-1344
p=P*S.Matrix(shifts)
q=P*S.Matrix([t*t for t in shifts])
asym=-128*(p*q.T-q*p.T)
assert asym[0,1]==-1344
# Other exact symbolic limits check the full antisymmetric matrix, not just one entry.
for i in range(4):
    for j in range(4):
        assert S.simplify(S.limit(A**6*C.subs(B,A+8)[i,j],A,S.oo)-asym[i,j])==0
Gram=S.simplify((p.dot(p))*(q.dot(q))-(p.dot(q))**2)
assert Gram==362
assert S.limit(A**12*op2.subs(B,A+8),A,S.oo)==S.Integer(128**2*362)

# 6. Cauchy determinant channel identifiability from source moments.
x0,x1,x2=S.Integer(1),S.Integer(9),S.Integer(17)
rows=S.Matrix([[d/(x*(x+d)) for d in (3,4,5)] for x in (x0,x1,x2)])
v=S.Matrix([R(x) for x in (x0,x1,x2)])
assert rows.det()!=0
assert rows.inv()*v==S.Matrix([2,1,1])

# 7. Check the three-positive channels are a genuine probability mixture.
mu = [S.factor(S.Rational(w)*d/(A*(A+d))/R(A)) for d,w in [(3,2),(4,1),(5,1)]]
assert S.simplify(sum(mu))==1
assert [S.limit(x,A,S.oo) for x in mu]==[S.Rational(6,15),S.Rational(4,15),S.Rational(5,15)]

# 8. New exact two-adic pairing proof, independent n-symbol algebra.
n=S.symbols('n',positive=True,integer=True)
an=8*n-7
r3=S.Rational(6)/(an*(an+3))
r4=S.Rational(4)/(an*(an+4))
r5=S.Rational(5)/(an*(an+5))
assert S.cancel(r3-S.Rational(3)/(2*an*(2*n-1)))==0
assert S.cancel(r5-S.Rational(5)/(2*an*(4*n-1)))==0
assert S.cancel(r3+r5-(11*n-4)/(an*(2*n-1)*(4*n-1)))==0
assert S.cancel(r3+r4+r5-(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*an*(an+4)))==0

# 9. Source-conditioned golden fixed-point drift, symbolic implicit derivative.
lam=(S.sqrt(5)-1)/2
q0=lam**2
z,t=S.symbols('z t')
# R((2-z)/t)/R(1/t) as a rational expression in t.
g=S.factor(R((2-z)/t)/R(1/t))
g0=(2-z)**(-2)
beta=S.Rational(59,15)
g1=S.factor(g0*beta*(1-1/(2-z)))
assert S.simplify(S.limit(g,z,S.Rational(1,2))-g.subs(z,S.Rational(1,2)))==0
assert S.simplify(S.limit(g,t,0)-g0)==0
assert S.simplify(S.limit((g-g0)/t,t,0)-g1)==0
Fprime=S.diff(g0,z).subs(z,q0)
drift=S.simplify(g1.subs(z,q0)/(1-Fprime))
assert S.simplify(drift-S.Rational(59,15)*(5-S.sqrt(5))/10)==0

receipt={
 'status':'INDEPENDENT_EXACT_SYMBOLIC_REPLAY',
 'source':'four signed pole coefficient and offset arrays reproduced from scratch',
 'original_jets':[str(x) for x in jets],
 'rigid_pole_offset_solutions':solution,
 'source_channel_multiplicities':[2,1,1],
 'channel_mixture_asymptotic_weights':['2/5','4/15','1/3'],
 'cauchy_source_sampling_determinant':str(S.factor(rows.det())),
 'clock_commutator_1_9_entry_01':str(C[0,1].subs({A:1,B:9})),
 'clock_commutator_1_9_operator_norm_sq':str(op2.subs({A:1,B:9})),
 'clock_commutator_consecutive_asymptotic_mat':[[str(asym[i,j]) for j in range(4)] for i in range(4)],
 'clock_commutator_limit_a12_norm_sq':str(S.Integer(128**2*362)),
 'all_16_symbolic_commutator_entries_verified':True,
 'all_16_symbolic_asymptotic_matrix_entries_verified':True,
 'exact_vandermonde_norm_verified':True,
 'source_2adic_pairing_symbolically_verified':True,
 'positive_mixed_poisson_fixed_point_shift':str(drift),
 'positive_mixed_poisson_universal_root':str(S.simplify(q0)),
 'complete_pgf_first_jet_symbolically_verified':True,
 'higher_jet_mutant_preserves_first_two_jets':True,
 'uses_unsourced_normality_claim':False,
}
if __name__=='__main__':
    import sys
    if '--out' in sys.argv:
        out=Path(sys.argv[sys.argv.index('--out')+1]);out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(receipt,indent=2,sort_keys=True))
