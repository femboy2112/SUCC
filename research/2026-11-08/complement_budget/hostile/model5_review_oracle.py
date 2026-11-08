"""Independent exact tests of CBM5 escape, rotated arcs and layer cake.

No sibling model implementation is imported. All comparisons below are
rational. These checks supplement the separate universal paper audit.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import random

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]


def clock(p):
    out=[];seen=set();x=4*pow(16,(p-1)//4+1-(p+7)//8,p)%p
    while x not in seen:
        seen.add(x);out.append(x);x=16*x%p
    assert x==out[0]
    return out


def evaluate(P,x,p):
    return sum(c*pow(x,d,p) for d,c in enumerate(P))%p


def cls(P,p):
    a=[c%p for c in P[1:]]
    while a and a[-1]==0:a.pop()
    return tuple(a)


def transformed_cls(P,p):
    return cls(tuple(c*pow(16,d-1,p)%p for d,c in enumerate(P)),p)


def escaping(Ps,p):
    classes={cls(P,p) for P in Ps}
    return [i for i,P in enumerate(Ps) if transformed_cls(P,p) not in classes]


def discrepancy(values):
    """Exact circular interval discrepancy of a finite equal-mass law."""
    counts={}
    for value in values:
        x=value%1;counts[x]=counts.get(x,0)+1
    n=len(values);done=0;left=[];right=[]
    for x,count in sorted(counts.items()):
        left.append(F(done,n)-x);done+=count;right.append(F(done,n)-x)
    return max(right)-min(left)


def run():
    rng=random.Random(202611085)
    escape_checks=0
    for p in (41,73,97,137,193):
        m=len(clock(p))
        for D in (2,3):
            for K in (1,2,3):
                if K*D>=m:continue
                for _ in range(12):
                    Ps=[]
                    while len(Ps)<K:
                        P=tuple(rng.randrange(p) for _ in range(D+1))
                        if P[-1] and P not in Ps:Ps.append(P)
                    assert escaping(Ps,p)
                    escape_checks+=1
    # Distinct polynomials sharing classes modulo constants are allowed.
    assert escaping([(0,0,1),(1,0,1),(0,1,0)],193)
    # Nonhomogeneous affine branches MUST be excluded from CBM5.
    assert not escaping([(1,1)],193)
    rows=[];nonvacuous=0;grid_bound_nonvacuous=0;rotation_checks=0
    for p in (73,193,88001):
        xs=clock(p);m=len(xs)
        for Ps in ([(0,0,1)],[(0,0,1),(2,1,3)]):
            K=len(Ps);D=2
            assert K*D<m
            i=escaping(Ps,p)[0]
            anchors=[F(2*j+1,7+2*j) for j in range(K)]
            distributions=[];rotated=[]
            for j,P in enumerate(Ps):
                values=[F((evaluate(Ps[i],16*x%p,p)-16*evaluate(P,x,p))%p,p) for x in xs]
                distributions.append(values)
                shift=anchors[i]-16*anchors[j]
                translated=[(v+shift)%1 for v in values]
                assert discrepancy(values)==discrepancy(translated)
                rotated.append(translated);rotation_checks+=1
            d=max(discrepancy(v) for v in distributions)
            c=max(F(),1-K*d-F(1,m))
            # The nearest chord is >=4 times nearest circular distance.
            # Zero the final boundary before averaging, as required by CBM5.
            minimum_distances=[min(min(v[r],1-v[r]) for v in rotated) for r in range(m-1)]+[F()]
            lower_distance=4*sum(minimum_distances)/m
            bound=c*c/K
            assert lower_distance>=bound
            nonvacuous+=bound>0
            # Uniform Weil/discrepancy budget, with a rational upper sqrt(p).
            precision=10**12
            sqrt_upper=F(isqrt(p*precision*precision)+1,precision)
            delta=min(F(1),D*sqrt_upper/m)
            harmonic=sum((F(1,k) for k in range(1,(p-1)//2+1)),F())
            d_grid=F(1,p)+delta*harmonic
            assert d<=d_grid
            c_grid=max(F(),1-K*d_grid-F(1,m))
            grid_bound=c_grid*c_grid/K
            assert lower_distance>=grid_bound
            grid_bound_nonvacuous+=grid_bound>0
            rows.append({"p":p,"m":m,"K":K,"D":D,"escaping_branch":i,
                         "exact_discrepancy":str(d),"actual_arc_layer_cake_bound":str(bound),
                         "exact_nearest_distance_lower":str(lower_distance),
                         "PR3_grid_layer_cake_bound_decimal":float(grid_bound),
                         "PR3_grid_discrepancy_upper_decimal":float(d_grid)})
    files=[HERE.parent/'model/THEOREMS.md',Path(__file__)]
    return {"status":"exact finite audit; paper result independently reviewed, no asymptotic test claim",
            "mod_constant_escape_families":escape_checks+1,
            "affine_countermodel_checks":1,"rotated_discrepancy_checks":rotation_checks,
            "nonvacuous_actual_arc_floors":nonvacuous,"nonvacuous_PR3_grid_floors":grid_bound_nonvacuous,
            "rows":rows,"reviewed_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    encoded=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(encoded)
    else:print(encoded,end='')
