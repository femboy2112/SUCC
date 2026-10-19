"""Exact ALL-DIRECTIONS 2x2 source Schur sign oracle for interval-rank-one savings.

Given rational signed source quadratic Q(x,y)=[x y] A [x y]^T and
interval-constrained true source moment rows (m1,m2) +/- (e1,e2),
a source-rigorous lower has form:
 Q(x,y)+Σ λ_j (|m1*x+m2*y|-e1|x|-e2|y|)_+².

This decision procedure checks every real direction (x,y), not a finite
angular grid. Set x=1, y=t and separately x=0. For t>=0 and t<=0,
each positive-part absolute-linear feature is the MAX of 3 exact affine
functions. Partition the real line at their finitely many intersections;
the lower is a rational quadratic on every interval. Check finite
endpoints, exact interior vertices and both unbounded tails.

A NEGATIVE checked lower does NOT imply a negative original source.
A NONNEGATIVE bound DOES imply the full signed source block positive
under the separately authenticated source form hypotheses.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations


class ExactConeError(ValueError):
    pass


def _q(z):
    if type(z) not in (int,F):
        raise ExactConeError("only exact int/Fraction angular certificates")
    return F(z)


def _affines(feature,sign):
    m1,m2,e1,e2,weight=feature
    return ((F(0),F(0)),
            (m1-e1,m2-sign*e2),
            (-m1-e1,-m2-sign*e2))


def _evaluate_affine(a,t):
    return a[0]+a[1]*t


def _intersection(f,g):
    if f[1]==g[1]:return None
    return (g[0]-f[0])/(f[1]-g[1])


def _inside(t,left,right):
    return (left is None or t>=left) and (right is None or t<=right)


def _minimum_quadratic_on_interval(a,b,c,left,right):
    """Exact min lower and a finite rational minimizing witness if attained."""
    if left is None and right is None:
        raise ExactConeError("one semiaxis at a time required")
    if left is None:
        # t -> -inf. If c<0, negative infinity; if c=0 and b>0 idem.
        if c<0 or (c==0 and b>0):return False,None
    if right is None:
        if c<0 or (c==0 and b<0):return False,None
    xs=[]
    if left is not None:xs.append(left)
    if right is not None:xs.append(right)
    if c>0:
        vertex=-b/(2*c)
        if _inside(vertex,left,right):xs.append(vertex)
    if not xs:
        # e.g. zero linear part with a finite boundary is never here.
        raise ExactConeError("unbounded quadratic without finite boundary")
    vals=tuple((a+b*t+c*t*t,t) for t in xs)
    minval,x=min(vals,key=lambda v:v[0])
    return minval>=0,(minval,x)


def exact_nonnegative_two_dimensional_source_cone(A,features):
    """Prove or refute positivity of the DECLARED robust lower on R².

    A is exact symmetric 2x2. features iterable of (m1,m2,e1,e2,λ),
    e_i>=0, λ>=0. The returned result does not identify source.
    """
    try:
        A=tuple(tuple(_q(v) for v in row) for row in A)
        feats=tuple(tuple(_q(v) for v in row) for row in features)
    except (TypeError,ValueError) as exc:
        raise ExactConeError("exact quadratic and source interval features required") from exc
    if len(A)!=2 or any(len(row)!=2 for row in A) or A[0][1]!=A[1][0]:
        raise ExactConeError("symmetric rational 2x2 source low block required")
    if any(len(f)!=5 or min(f[2],f[3],f[4])<0 for f in feats):
        raise ExactConeError("source feature is (m1,m2,e1>=0,e2>=0,lambda>=0)")
    # Vertical direction x=0, y=1 is the point at infinity after x=1,t.
    infinity=A[1][1]+sum((w*max(F(0),abs(m2)-e2)**2
                           for m1,m2,e1,e2,w in feats),F(0))
    details=[]
    proved=infinity>=0
    first_failure=None if proved else {"kind":"vertical_direction","x":(F(0),F(1)),
                                       "lower":infinity}
    for sign in (-1,+1):
        low=None if sign==-1 else F(0)
        high=F(0) if sign==-1 else None
        cut={F(0)}
        for feature in feats:
            af=_affines(feature,sign)
            for u,v in combinations(af,2):
                point=_intersection(u,v)
                if point is not None and _inside(point,low,high):
                    cut.add(point)
        sorted_cut=sorted(cut)
        points=[None]+sorted_cut if sign==-1 else sorted_cut+[None]
        for left,right in zip(points,points[1:]):
            if left is None:sample=right-F(1)
            elif right is None:sample=left+F(1)
            else:sample=(left+right)/2
            qa=A[0][0];qb=2*A[0][1];qc=A[1][1]
            chosen=[]
            for feature in feats:
                af=_affines(feature,sign)
                winner=max(af,key=lambda z:_evaluate_affine(z,sample))
                chosen.append(winner)
                m,n=winner
                weight=feature[4]
                qa+=weight*m*m
                qb+=2*weight*m*n
                qc+=weight*n*n
            good,witness=_minimum_quadratic_on_interval(qa,qb,qc,left,right)
            details.append({
                "halfline":sign,
                "range":(left,right),
                "quadratic":(qa,qb,qc),
                "minimum_nonnegative":good,
                "minimum_witness":witness,
            })
            if not good and first_failure is None:
                first_failure={"kind":"computed_lower_negative_on_interval",
                               "halfline":sign,"range":(left,right),
                               "minimum_witness":witness,
                               "this_is_NOT_a_negative_original_Weil_witness":True}
            proved=proved and good
    return {
        "robust_lower_nonnegative_for_ALL_real_directions":proved,
        "source_form_is_not_supplied_or_authenticated_here":True,
        "tested_unbounded_tails":True,
        "tested_vertical_direction":True,
        "piecewise_exact_intervals":tuple(details),
        "first_failure_of_LOWER_only":first_failure,
        "RH_proved":False,
    }
