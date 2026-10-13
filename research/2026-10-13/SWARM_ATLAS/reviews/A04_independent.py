import itertools,json,sys
from pathlib import Path
G=tuple(itertools.permutations(range(3)));E=(0,1,2)
def mul(g,h):return tuple(g[h[i]] for i in range(3))
def inv(g):return tuple(g.index(i) for i in range(3))
def subgroup(k):return E in k and all(mul(g,h) in k for g in k for h in k)
subs=[frozenset(g for g,b in zip(G,bits) if b) for bits in itertools.product((0,1),repeat=6)]
subs=[k for k in subs if subgroup(k)]
def core(k):return frozenset.intersection(*(frozenset(mul(mul(g,h),inv(g)) for h in k) for g in G))
a=(1,0,2);b=(0,2,1)
deck=[d for d in G if mul(d,a)==mul(a,d) and mul(d,b)==mul(b,d)]
sections=[f for f in itertools.product(range(3),repeat=3) if all(f[g[y]]==g[f[y]] for g in (a,b) for y in range(3))]
assert deck==[E] and sections==[E]
assert any(sections[0][i]!=sections[0][j] for i in range(3) for j in range(3))
for mode in ['natural3','natural3+sign2']:
 X=range(3 if mode=='natural3' else 5)
 def action(g,x):
  parity=sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))%2
  return g[x] if x<3 else 3+(x-3+parity)%2
 stabilizers=[frozenset(g for g in G if action(g,x)==x) for x in X]
 predicted=min(6//len(k) for k in stabilizers)
 regular_predicted=min(6//len(core(k)) for k in stabilizers)
 actual=min(6//len(k) for k in subs if any(all(action(g,x)==x for g in k) for x in X))
 regular_actual=min(6//len(k) for k in subs if core(k)==k and any(all(action(g,x)==x for g in k) for x in X))
 assert (predicted,regular_predicted)==(actual,regular_actual)
 assert (actual,regular_actual)==((3,6) if mode=='natural3' else (2,2))
r={'reviewer':'/root distinct from /root/a04','S3_subgroups':len(subs),'deck_group_size':len(deck),'lawful_sections':sections,'non_descending_deck_invariant_witness':True,'natural3_minima':[3,6,6],'natural3_plus_sign2_minima':[2,2,6],'all_checks_passed':True,'helper_imports':False,'verdict':'paper orbit/core/subgroup proof survives; no kernel promotion'}
t=json.dumps(r,indent=2)+'\n'
if len(sys.argv)>1:Path(sys.argv[1]).write_text(t)
print(t)
