"""Exact small controls for TD-W4/W5 using rational Fourier--Motzkin elimination."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
import json


def row(coeffs, bound):
    if any(type(v) not in (int, Q) for v in (*coeffs, bound)):
        raise TypeError('exact rational coefficients required')
    return tuple(map(Q, coeffs)), Q(bound)


def eliminate(rows, j):
    """Existentially eliminate one real coordinate from closed inequalities."""
    pos, neg, keep = [], [], []
    for a, b in rows:
        p = a[j]
        rest = a[:j] + a[j+1:]
        if p > 0:
            pos.append((p, rest, b))
        elif p < 0:
            neg.append((p, rest, b))
        else:
            keep.append((rest, b))
    for p, ap, bp in pos:
        for n, an, bn in neg:
            keep.append((tuple(-n*x+p*y for x,y in zip(ap,an)), -n*bp+p*bn))
    return list(dict.fromkeys(keep))


def accepts(rows, pt):
    return all(sum(a*x for a,x in zip(coeff,pt)) <= bound for coeff,bound in rows)


def witness(rows, n):
    if n == 0:
        return () if accepts(rows, ()) else None
    tail = witness(eliminate(rows, 0), n-1)
    if tail is None:
        return None
    lower, upper = [], []
    for a, b in rows:
        residual = b - sum(v*x for v,x in zip(a[1:],tail))
        if a[0] > 0:
            upper.append(residual/a[0])
        elif a[0] < 0:
            lower.append(residual/a[0])
    first = max(lower) if lower else min(upper) if upper else Q(0)
    result = (first, *tail)
    assert accepts(rows, result)
    return result


def deadline():
    # Joint source/current prior s=x in [-1,1].
    initial=[row((1,0),1),row((-1,0),1),row((1,-1),0),row((-1,1),0)]
    unit=[row((1,),1),row((-1,),1)]
    def command(extrema):
        rows=list(unit)
        for s in extrema:
            rows.extend((row((1,),s+Q(1,2)),row((-1,),Q(1,2)-s)))
        return witness(rows,1)
    assert command((Q(-1),Q(1))) is None
    received={}
    for o in (-1,1):
        before=[row((*a,0),b) for a,b in initial]
        # Both reports are possible at x=0; x' is destructively reset to zero.
        graph=[row((0,-o,0),0),row((0,0,1),0),row((0,0,-1),0)]
        joined=eliminate(before+graph,1)
        endpoints=(Q(-1),Q(0)) if o==-1 else (Q(0),Q(1))
        assert all(accepts(joined,(s,Q(0))) for s in endpoints)
        assert all(accepts(joined,(s,Q(0))) == (endpoints[0]<=s<=endpoints[1])
                   for s in (Q(i,7) for i in range(-10,11)))
        assert accepts(joined,(Q(0),Q(0))) and not accepts(joined,(Q(0),Q(1)))
        # Polytope equality by mutual containment, via pointed support bounds:
        # unrestricted source projection is [-1,0] or [0,1], x'=0 always.
        projected=eliminate(joined,1)
        lo=max(b/a[0] for a,b in projected if a[0]<0)
        hi=min(b/a[0] for a,b in projected if a[0]>0)
        assert (lo,hi)==endpoints
        current=eliminate(joined,0)
        assert max(b/a[0] for a,b in current if a[0]<0)==0
        assert min(b/a[0] for a,b in current if a[0]>0)==0
        c=command(endpoints)
        assert c==(Q(o,2),)
        received[str(o)]=str(c[0])
    # Move negative branch domain to u>=0: boundary label cannot be discarded.
    assert witness(unit+[row((-1,),0),row((1,),-Q(1,2))],1) is None
    # Nonconvex source components cannot be replaced by a filled interval for legality.
    allowed=lambda x: x<=-Q(1,2) or x>=Q(1,2)
    assert all(allowed(x) for x in (Q(-1),Q(1))) and not allowed(Q(0))
    return received


def helly():
    cases=0
    size=[]
    for m in range(1,6):
        # u_1,...,u_m >=0, u_0=1-sum u_i>=0 in nonredundant coordinates.
        base=[row(tuple(-int(i==j) for j in range(m)),0) for i in range(m)]
        base.append(row((1,)*m,1))
        facets=[row((-1,)*m,-1)]+[row(tuple(int(i==j) for j in range(m)),0) for i in range(m)]
        assert witness(base+facets,m) is None
        for i in range(m+1):
            assert witness(base+facets[:i]+facets[i+1:],m) is not None
        size.append(m+1)
        cases+=m+2
    grid=[tuple(Q(i,5) for i in s) for s in product(range(6),repeat=3) if sum(s)==5]
    pairs=0
    for s,t in combinations_with_replacement(grid,2):
        caps=[1-max(a,b) for a,b in zip(s,t)]
        # Exact rational LP for a common command on the encoded triangle.
        rows=[row((-1,0),0),row((0,-1),0),row((1,1),1),
              row((-1,-1),caps[0]-1),row((1,0),caps[1]),row((0,1),caps[2])]
        assert witness(rows,2) is not None
        pairs+=1
    assert witness([row((0,),-1)],1) is None  # empty command set, one case suffices
    # Unbounded hidden x': every sampled finite subset admits max x' as a control.
    for k in range(1,11):
        assert witness([row((-1,),-j) for j in range(k+1)],1)==(Q(k),)
    return {'infeasible_simplex_sizes':size,'simplex_LPs':cases,'triangle_pair_LPs':pairs}


if __name__=='__main__':
    print(json.dumps({'status':'EXACT_RATIONAL_CONTROLS','commands_after_destructive_bit':deadline(),
                      'helly':helly()},sort_keys=True))
