"""Independent, import-free exact arithmetic audit of SUCC YM/QM bridge.

No import of observational_succ, no fitting, no statement that this is a
blind external referee. These calculations check results via different
formulae and data decompositions in standard-library Fraction arithmetic.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q
from itertools import permutations, product


def audit() -> dict:
    # 1. Independently construct the 16x16 Kogut-Susskind-style matrix on Z2 links.
    states=tuple(product((0,1), repeat=4))
    parity=lambda x:sum(x)%2
    cls={p:tuple(x for x in states if parity(x)==p) for p in (0,1)}
    H={}
    for x in states:
        for y in states:
            electric=4*int(x==y)-sum(int(tuple(1-z if i==e else z for i,z in enumerate(y))==x) for e in range(4))
            magnet=2*parity(x)*int(x==y)
            H[x,y]=Q(electric+magnet)
    M=tuple(tuple(sum((H[x,y] for x in cls[i] for y in cls[j]),Q()) / 8
                  for j in (0,1)) for i in (0,1))
    assert M==((Q(4),Q(-4)),(Q(-4),Q(6)))
    tr=M[0][0]+M[1][1]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert (tr,det)==(10,8)
    # 2. Construct S3 using the *opposite* representation: permutation tuples
    # and direct conjugacy orbit classes, without importing SUCC's S3.
    S=tuple(permutations(range(3)))
    def mul(a,b):return tuple(a[b[i]] for i in range(3))
    def inv(a):return tuple(a.index(i) for i in range(3))
    def conj(k,a):return mul(mul(k,a),inv(k))
    remain=set(product(S,repeat=2));orbits=0
    while remain:
        a,b=min(remain)
        orb={(conj(k,a),conj(k,b)) for k in S}
        assert orb<=remain
        remain-=orb
        orbits+=1
    assert orbits==11
    # 3. Independent finite projection over internal Z3 gauge orbits.
    q=3
    F={(a,b):Q((7*a+5*b+1)%11) for a,b in product(range(q),repeat=2)}
    p={}
    for a,b in F:
        p[a,b]=sum((F[(a-k)%q,(k+b)%q] for k in range(q)),Q())/q
        direct=sum((F[t,(a+b-t)%q] for t in range(q)),Q())/q
        assert p[a,b]==direct
    assert all(p[a,b]==p[(a-k)%q,(b+k)%q] for a,b in F for k in range(q))
    # 4. Haar conditional energy identity, by direct independent 4-cell table.
    cells=(Q(1,10),Q(2,10),Q(3,10),Q(4,10))
    coarse=(cells[0]+cells[1],cells[2]+cells[3])
    e1=4*sum(x*x for x in cells)-1
    e0=2*sum(x*x for x in coarse)-1
    detail=4*sum((cells[2*i+j]-coarse[i]/2)**2 for i in (0,1) for j in (0,1))
    assert (e0,e1,detail)==(Q(4,25),Q(1,5),Q(1,25))
    # 5. Exact Wilson source transport through a two-factor sign product.
    weight={1:Q(3),-1:Q(1)}
    Z=sum(weight.values(),Q())
    raw={s:weight[s]/Z for s in (1,-1)}
    pushed={s:sum((raw[a]*raw[b] for a,b in product((1,-1),repeat=2) if a*b==s),Q())
            for s in (1,-1)}
    assert (pushed[1],pushed[-1])==(Q(5,8),Q(3,8))
    tv=sum((abs(raw[s]-pushed[s]) for s in raw),Q())/2
    assert tv==Q(1,8)
    # 6. Gauge-odd state and gauge-invariant density, independent of projector.
    psi={(a,b):Q(1 if a==0 else -1,2) for a,b in product((0,1),repeat=2)}
    transformed={(a,b):psi[((a+1)%2,(b+1)%2)] for a,b in psi}
    assert all(transformed[x]==-psi[x] for x in psi)
    assert all(transformed[x]*transformed[y]==psi[x]*psi[y] for x,y in product(psi,repeat=2))
    # All failures are explicit assertions in a finite exact model; no mass gap.
    return {'status':'INDEPENDENT ALGORITHMIC DECOMPOSITIONS; SAME-MODEL FINITE AUDIT',
            'graph_projected_H':[[str(z) for z in row] for row in M],
            'graph_characteristic_trace':str(tr),'graph_characteristic_det':str(det),
            'S3_simultaneous_two_loop_orbits':orbits,
            'internal_Z3_gauge_projection_exact':True,
            'haar_word_detail_4_cells':str(detail),
            'interacting_Wilson_pushforward_TV':str(tv),
            'gauge_odd_density_twirl_invariant':True,
            'YM_mass_gap':'OPEN'}


if __name__=='__main__':
    print(json.dumps(audit(),sort_keys=True,indent=2))
