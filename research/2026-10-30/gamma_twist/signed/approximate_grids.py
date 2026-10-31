"""Exact translated-grid minimax search and Stoneham multiplicity calibration."""
from fractions import Fraction as F
import json
from signed_transport import orbit,birth,order16,decimal_bracket


def optimal_radius(phases,q):
    if q<1 or not phases:raise ValueError('nonempty phases and q>=1 required')
    residues=sorted(set((q*x)%1 for x in phases))
    gaps=[b-a for a,b in zip(residues,residues[1:])]
    gaps.append(1+residues[0]-residues[-1])
    return (1-max(gaps))/(2*q)


def source_case(p):
    b,L=birth(p),order16(p)
    phases=orbit(b+L-1)[b:]
    radii=[optimal_radius(phases,q) for q in range(1,L+1)]
    best=min(range(1,L+1),key=lambda q:radii[q-1])
    eps=F(1,p*p)
    return {'p':p,'birth':b,'L':L,'q_min':1,'q_max':L,'allowed_error':str(eps),
            'best_q':best,'best_radius':decimal_bracket((radii[best-1],radii[best-1]),30),
            'passing_q':[q for q,r in enumerate(radii,1) if r<=eps],
            'all_q_excluded':all(r>eps for r in radii),
            'minimum_radius_over_allowed_error':decimal_bracket((min(radii)/eps,min(radii)/eps),20)}


def stoneham(c,j):
    q=c**j
    A=q
    L=(c-1)*q
    alpha=sum((F(1,c**k*16**(c**k)) for k in range(1,j+1)),F())
    phases=[(16**n*alpha)%1 for n in range(A,A+L)]
    labels=[(q*x).numerator for x in phases]
    assert all((q*x).denominator==1 for x in phases)
    counts={x:labels.count(x) for x in set(labels)}
    radius=optimal_radius(phases,q)
    assert radius==0
    if c in (3,5):
        assert len(counts)==q//c
        assert set(counts.values())=={c*(c-1)}
    else:
        # The newest term is initially 1/2^j; it becomes an integer after
        # ceil(j/4) radix steps. Keep that finite transient rather than
        # pretending the whole stage starts at zero.
        transient=(j+3)//4
        assert counts.get(0)==q-transient
        assert max(counts.values())==q-transient
    return {'c':c,'j':j,'q':q,'A':A,'L':L,'exact_truncated_grid_radius':'0',
            'distinct_cells':len(counts),'maximum_cell_multiplicity':max(counts.values()),
            'complete_constant_tail_error_bound':str(F(1,16*(c-1)*q)),
            'bounded_multiplicity_mechanism':c in (3,5)}


def main():
    rows=[source_case(p) for p in (701,709,733)]
    print(json.dumps({'status':'EXACT_FINITE_SEARCH','source':'authentic U0=0',
        'criterion':'max_n distance(U_n,theta+Z/q)<=1/p^2, q<=L',
        'BBP_cases':rows,'Stoneham_controls':[stoneham(c,j) for c,j in ((3,3),(5,2),(2,5))],
        'boundary':'excludes only stated finite q/error/window classes; no all-horizon approximate-grid no-go'},indent=2))


if __name__=='__main__':main()
