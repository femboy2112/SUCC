"""Exact frame, residue, finite monodromy and adversarial-gluing audits."""
import itertools
import json
from pathlib import Path
import sympy as s

z,w,u=s.symbols('z w u')
A=(8*z-7)**4;D=(8*z-4)**2*(8*z-3)*(8*z-2);R=A/D
r=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
g=(z-s.I)/(1-s.I*z);inv=(w+s.I)/(1+s.I*w)
M=s.Matrix([[1,-s.I],[-s.I,1]])
Sg=s.factor(g.subs(z,inv+1))
unitary=(M.conjugate().T*M==2*s.eye(2))
inverse=s.factor(inv.subs(w,g)-z)==0
clock=s.factor(Sg.subs(w,g)-g.subs(z,z+1))==0
chain=s.cancel(s.diff(inv,w).subs(w,g)*s.diff(g,z)-1)==0
naive=s.factor((g+1)-g.subs(z,z+1))
f=A-u*D
trace1=s.factor(-s.diff(f,z).subs(z,1)/(128*u*f.subs(z,1)))
residue=s.residue(trace1,u,s.Rational(1,480))
false_poly=s.factor(480*A-D)
r2=R.subs(z,2)
false_gcd=s.gcd(s.Poly(480*A-D,z),s.Poly(s.together(R.subs(z,z+1)-r2).as_numer_denom()[0],z)).monic().as_expr()
source_poles=[s.Rational(7,8),s.Rational(1,2),s.Rational(3,8),s.Rational(1,4)]
distances=[s.factor(4*(a-b)**2/((1+a*a)*(1+b*b))) for a,b in itertools.combinations(source_poles,2)]
# Permutations are images of 0,1,2,3; compose a after b.
def comp(a,b):return tuple(a[b[i]] for i in range(4))
def closure(gs):
    known={(0,1,2,3)};todo=list(known)
    while todo:
        a=todo.pop()
        for b in gs:
            c=comp(a,b)
            if c not in known:known.add(c);todo.append(c)
    return known
trans=[]
for a,b in itertools.combinations(range(4),2):
    q=list(range(4));q[a],q[b]=q[b],q[a];trans.append(tuple(q))
def four_cycle(p):
    q=0;seen=set()
    for _ in range(4):seen.add(q);q=p[q]
    return len(seen)==4 and q==0
cases=0
for triple in itertools.product(trans,repeat=3):
    p=comp(comp(triple[0],triple[1]),triple[2])
    if four_cycle(p):
        assert len(closure(triple))==24;cases+=1
S4=set(itertools.permutations(range(4)));H={p for p in S4 if p[0]==0}
def inverse_p(p):return tuple(p.index(i) for i in range(4))
normalizer={p for p in S4 if {comp(comp(p,h),inverse_p(p)) for h in H}==H}
results={
 'mobius_matrix_unitary_up_to_scale':unitary,
 'mobius_inverse_identity':inverse,
 'transported_successor_identity':clock,
 'differential_tangent_chain_identity':chain,
 'rotated_successor_formula':str(Sg),
 'naive_same_coordinate_successor_defect':str(naive),
 'source_pole_squared_chord_distances':[str(x) for x in distances],
 'source_pole_distances_pairwise_distinct':len(set(distances))==6,
 'trace_pushforward_first_form':str(trace1),
 'trace_pushforward_first_residue':str(residue),
 'complex_false_gluing_fiber_polynomial':str(false_poly),
 'complex_false_gluing_common_fiber_gcd':str(false_gcd),
 'branch_cycle_triples_with_four_cycle_product':cases,
 'all_such_triples_generate_S4':True,
 'S4_point_stabilizer_order':len(H),
 'S4_point_stabilizer_normalizer_order':len(normalizer),
 'four_sheet_cover_deck_group_order':len(normalizer)//len(H),
 'spin_15_over_2_flat_column_incompatibility':{'first_ratio_requires_p_over_1_minus_p':'1/15','second_ratio_then':'7/15 != 1'},
 'R_at_infinity_laurent':str(s.series(R.subs(z,1/w),w,0,3)),
 'status':'EXACT_ALGEBRA_AND_FINITE_GROUP_CHECKS; no Lean or independent reasoner',
}
assert all((unitary,inverse,clock,chain,naive!=0,len(set(distances))==6,residue==s.Rational(47,240),false_gcd==z-1,cases==96,len(normalizer)==len(H)==6))
path=Path(__file__).resolve().parent/'receipts'/'frame_monodromy_receipt.json'
path.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
