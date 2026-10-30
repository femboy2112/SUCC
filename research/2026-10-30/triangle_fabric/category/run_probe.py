from pathlib import Path
from fractions import Fraction as F
import json
import arrow_probe as p

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

rows=[];word_count=0
for a in (17,41,97,233):
    for m in (3,4,6,8):
        authentic=[p.word_probability(a,w) for w in p.all_words(m)]
        mutant=[p.word_probability(a,w,True) for w in p.all_words(m)]
        assert min(mutant)>0 and sum(mutant)==1
        grades=[sum(p.word_probability(a,w,True) for w in p.all_words(m) if w.count('1')==k) for k in range(m+1)]
        assert grades==p.endpoint(a,m)
        word_count+=2**m
        rows.append({'a':a,'m':m,'endpoint':grades,'minimum_word_mass':min(mutant),'total_variation':sum(abs(x-y) for x,y in zip(authentic,mutant))/2})

cycles=[]
for a,m,d in [(17,2,2),(41,3,4),(97,5,3),(233,7,2)]:
    j=p.native_joint(a,m,d)
    assert p.margins(j)==(p.endpoint(a,m),p.endpoint(a,m+d))
    edges=p.edge_support(m,d)
    dim=len(edges)-p.rank(p.incidence(m,d))
    assert dim==m*(d-1)
    basis=p.cycle_basis(m,d)
    assert p.rank([[z[i][k] for i,k in edges] for z in basis])==dim
    cycles.append({'a':a,'m':m,'d':d,'dimension':dim,'joint':j})

recon=[]
for a,m,d in [(17,2,2),(41,3,2),(97,4,3)]:
    j=p.native_joint(a,m,d)
    left=list(range(1,m+2));right=list(range(2,m+d+3))
    observed,recovered,gain=p.tomography(j,left,right)
    assert j==recovered
    recon.append({'a':a,'m':m,'d':d,'left':left,'right':right,'observed':observed,'joint':j,'max_norm_error_gain':gain})

z,design_rank=p.matched_arrow_direction(4,4)
assert p.harmonic_golden_moments(z)==[0]*7
matched=[]
for a in (17,97,233):
    j=p.native_joint(a,4,4);epsilon=p.power_moment(a,8,8)/2
    mutant=p.perturb(j,z,epsilon)
    assert min(v for row in mutant for v in row)>=0
    assert p.margins(j)==p.margins(mutant)
    assert p.harmonic_golden_moments(j)==p.harmonic_golden_moments(mutant)
    c=p.cauchy(range(1,6),range(5));d=p.cauchy(range(2,11),range(9))
    defect=p.matmul(p.matmul(c,z),p.transpose(d))
    nonzero=next((i,k,v*epsilon) for i,row in enumerate(defect) for k,v in enumerate(row) if v)
    matched.append({'a':a,'epsilon':epsilon,'joint':j,'mutant':mutant,'witness_resolvent_defect':nonzero})

out={'status':'PASS exact finite instruments; universal claims require the dossier proofs',
     'source':{'poles':p.POLES,'parent':'6cf5050ff2cfd92e7a0c8876da5233be6ff117f5','sensor_mutation_not_bbp_mutation':True},
     'snapshot_aliases':rows,'enumerated_word_pairs':word_count,'cycles':cycles,
     'tomography':recon,'triangle_matched_direction':z,'triangle_design_rank':design_rank,
     'triangle_matched_couplings':matched}
path=Path(__file__).parent/'receipts'/'probe.json'
with path.open('x') as f:json.dump(encode(out),f,indent=2)
print(f'PASS {len(rows)} all-horizon-alias finite rows, {word_count} word pairs, {len(cycles)} cycle ranks, {len(recon)} exact tomographies, {len(matched)} fully triangle-matched arrows; design rank {design_rank}/12')
