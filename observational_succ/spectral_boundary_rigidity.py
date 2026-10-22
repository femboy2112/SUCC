"""Exact source-relative boundary spectral rigidity for finite positive RC chains.

CLASSICAL IMPORT: finite Jacobi Weyl-m-function inverse theory, continued
fractions, controllability/observability, and rational interpolation.

Original SUCC question: when do source-authenticated boundary RETURN HISTORIES
determine an interior realization, not merely select a fitted scalar?

This module establishes the finite chain model ONLY, not arbitrary graph
inverse problems, physical constants, real experiments or gravitational ER=EPR.
Exact Fraction arithmetic; no SymPy, NumPy or floats in proof or tests.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import prod


class SpectralSourceError(ValueError):
    """Malformed source, inactive boundary channel or overclaimed inverse."""


def number(x):
    if type(x) not in (int, F):
        raise SpectralSourceError("Fraction or exact integer required, not float/bool")
    return F(x)


def poly(values):
    if type(values) not in (tuple, list) or not values:
        raise SpectralSourceError("nonempty polynomial coefficients required")
    out=[number(v) for v in values]
    while len(out)>1 and not out[-1]:
        out.pop()
    return tuple(out)


def pa(a,b):
    a=poly(a);b=poly(b)
    return poly([(a[i] if i<len(a) else F())+
                 (b[i] if i<len(b) else F())
                 for i in range(max(len(a),len(b)))])


def ps(a,c):
    return poly([number(c)*v for v in poly(a)])


def pm(a,b):
    a=poly(a);b=poly(b)
    out=[F()]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j]+=v*w
    return poly(out)


def pd(a,b):
    a=poly(a);b=poly(b)
    if b==(F(),):
        raise SpectralSourceError("division by zero polynomial")
    r=list(a)
    q=[F()]*max(1,len(a)-len(b)+1)
    while len(r)>=len(b) and (len(r)>1 or r[0]):
        i=len(r)-len(b);v=r[-1]/b[-1]
        q[i]+=v
        for j,c in enumerate(b):
            r[i+j]-=v*c
        r=list(poly(r))
    return poly(q),poly(r)


def pgcd(a,b):
    a=poly(a);b=poly(b)
    while b!=(F(),):
        a,b=b,pd(a,b)[1]
    return ps(a,1/a[-1])


def rational_response(numerator,denominator):
    n=poly(numerator);d=poly(denominator)
    if d==(F(),):
        raise SpectralSourceError("zero response denominator")
    if n==(F(),):
        return ((F(),),(F(1),))
    g=pgcd(n,d)
    n,rem=pd(n,g)
    if rem!=(F(),):
        raise ArithmeticError("polynomial gcd numerator not exact")
    d,rem=pd(d,g)
    if rem!=(F(),):
        raise ArithmeticError("polynomial gcd denominator not exact")
    lc=d[-1]
    return ps(n,1/lc),ps(d,1/lc)


def evaluate_poly(coeffs,s):
    s=number(s)
    return sum((v*s**j for j,v in enumerate(poly(coeffs))),F())


def response_at(response,s):
    n,d=rational_response(*response)
    denominator=evaluate_poly(d,s)
    if denominator==0:
        raise SpectralSourceError("probe at a pole of rational response")
    return evaluate_poly(n,s)/denominator


def _conductances(g):
    if type(g) not in (tuple,list) or not 1<=len(g)<=9:
        raise SpectralSourceError("1..9 strictly positive source conductances")
    out=tuple(number(x) for x in g)
    if any(x<=0 for x in out):
        raise SpectralSourceError("all source conductances strictly positive")
    return out


def chain_jacobi(g):
    """Interior Jacobi A: diagonal g_(i-1)+g_i, offdiagonal -g_i."""
    g=_conductances(g)
    n=len(g)-1
    return tuple(tuple(
        g[i]+g[i+1] if i==j else
        -g[min(i,j)+1] if abs(i-j)==1 else F()
        for j in range(n)) for i in range(n))


def chain_response(g):
    """Laplace one-port Y(s) for g0..gn, grounded endpoint, unit C on interiors.

    n=0: direct resistor to ground.
    n>=1: Y(s)=g0-g0^2 [(sI+A)^-1]_(1,1).
    """
    g=_conductances(g)
    n=len(g)-1
    if n==0:
        return rational_response((g[0],),(F(1),))
    d_next=(F(1),)
    d_after=(F(),)
    d_two=None
    for i in reversed(range(n)):
        term=pm((g[i]+g[i+1],F(1)),d_next)
        correction=ps(d_after,g[i+1]**2 if i<n-1 else F())
        current=pa(term,ps(correction,-1))
        if i==1:
            d_two=current
        d_next,d_after=current,d_next
    d_one=d_next
    if d_two is None:
        d_two=(F(1),)
    return rational_response(
        pa(ps(d_one,g[0]),ps(d_two,-g[0]**2)),d_one)


def chain_moments(g,how_many):
    """mu_k=<e1,A^k e1>; each coefficient is a weighted closed walk."""
    g=_conductances(g)
    if len(g)<2:
        raise SpectralSourceError("boundary moments require hidden node")
    if type(how_many) is not int or not 1<=how_many<=50:
        raise SpectralSourceError("bounded finite exact moment count 1..50")
    A=chain_jacobi(g);n=len(A)
    v=[F(1)]+[F()]*(n-1);result=[]
    for _ in range(how_many):
        result.append(v[0])
        v=[sum((A[i][j]*v[j] for j in range(n)),F()) for i in range(n)]
    return tuple(result)


def round_trip_new_depth(g,new_terminal):
    """First newly visible moment for an extra unit-capacitance hidden node.

    Old terminal resistor g[-1] is *reconnected* to a new hidden node.
    New terminal resistor is independently declared new_terminal>0.
    """
    g=_conductances(g)
    if len(g)<2:
        raise SpectralSourceError("at least one original hidden node required")
    last=number(new_terminal)
    if last<=0:
        raise SpectralSourceError("new ground edge must be positive")
    r=len(g)-1
    old=chain_moments(g,2*r+1)
    newer=chain_moments(g+(last,),2*r+1)
    expected=prod(v*v for v in g[1:])
    if old[:2*r]!=newer[:2*r] or newer[2*r]-old[2*r]!=expected:
        raise ArithmeticError("round-trip depth identity contradicted")
    return {"depth":r,"first_distinguishing_moment":2*r,
            "difference":expected,"moments_before":old,
            "moments_after":newer}


def recover_positive_chain(response):
    """Exact inverse Jacobi continued fraction with physical source checks.

    It determines g0 by high-frequency response, then recursively recovers
    a_i and b_i^2 from 1/m(s), and forces g_i=a_i-g_(i-1),
    b_i^2=g_i^2. No positive disconnected/ghost modes admitted.
    """
    P,Q=rational_response(*response)
    if len(P)!=len(Q):
        raise SpectralSourceError("boundary response not finite passive RC form")
    g0=P[-1]/Q[-1]
    if g0<=0:
        raise SpectralSourceError("nonpositive high-frequency boundary weight")
    if len(Q)==1:
        return (g0,)
    m=rational_response(pa(ps(Q,g0),ps(P,-1)),ps(Q,g0*g0))
    result=[g0]
    for _ in range(8):
        N,D=m
        if N==(F(),):
            raise SpectralSourceError("invisible or cancelled boundary dynamics")
        quo,rem=pd(D,N)
        if len(quo)!=2 or quo[-1]!=1:
            raise SpectralSourceError("Weyl continued-fraction quotient invalid")
        gnew=quo[0]-result[-1]
        if gnew<=0:
            raise SpectralSourceError("recovered edge is not a positive source")
        result.append(gnew)
        if rem==(F(),):
            break
        b2=-rem[-1]
        if b2!=gnew*gnew:
            raise SpectralSourceError("inconsistent Jacobi offdiagonal source")
        m=rational_response(ps(rem,-1),ps(N,b2))
    else:
        raise SpectralSourceError("more than 8 hidden nodes not in finite budget")
    if chain_response(result)!=(P,Q):
        raise ArithmeticError("independent forward replay does not match inverse")
    return tuple(result)


def exact_linear_unique(rows,targets):
    """Overdetermined exact rational Gauss-Jordan; None if no unique solution."""
    if not rows or not targets or len(rows)!=len(targets):
        raise SpectralSourceError("matching nonempty finite linear system")
    m=len(rows);n=len(rows[0])
    if n==0 or any(len(row)!=n for row in rows):
        raise SpectralSourceError("nonrectangular linear system")
    a=[[number(x) for x in row]+[number(y)] for row,y in zip(rows,targets)]
    pivots=[];r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if a[i][col]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][col]
        a[r]=[v/z for v in a[r]]
        for i in range(m):
            if i!=r and a[i][col]:
                q=a[i][col]
                a[i]=[v-q*w for v,w in zip(a[i],a[r])]
        pivots.append(col);r+=1
        if r==m:break
    if any(all(x==0 for x in row[:n]) and row[n]!=0 for row in a):
        return None
    if r!=n:
        return None
    x=[F()]*n
    for i,j in enumerate(pivots):
        x[j]=a[i][-1]
    return tuple(x)


def interpolate_response(samples,maximum_hidden_nodes):
    """2d+1 rational frequency readings determine proper response of degree<=d.

    Values must be exact; no experimental precision inference is made.
    Rational model order n is recovered by least possible denominator degree.
    """
    if type(maximum_hidden_nodes) is not int or not 0<=maximum_hidden_nodes<=8:
        raise SpectralSourceError("finite complexity prior 0..8 required")
    if type(samples) not in (tuple,list) or len(samples)<2*maximum_hidden_nodes+1:
        raise SpectralSourceError("need at least 2d+1 distinct source frequencies")
    obs=tuple((number(s),number(y)) for s,y in samples)
    if len({s for s,_ in obs})!=len(obs):
        raise SpectralSourceError("frequency probes must be distinct")
    for n in range(maximum_hidden_nodes+1):
        rows=[];targets=[]
        for s,y in obs:
            rows.append(tuple(s**j for j in range(n+1))+
                        tuple(-y*s**j for j in range(n)))
            targets.append(y*s**n)
        solution=exact_linear_unique(rows,targets)
        if solution is None:continue
        response=rational_response(solution[:n+1],solution[n+1:]+(F(1),))
        if all(response_at(response,s)==y for s,y in obs):
            return response
    raise SpectralSourceError("exact data inconsistent with complexity bound")


def finite_response_identity(first,second,freqs,degree_bound):
    """Sufficient finite exact certification under checked rational degree bound."""
    if type(degree_bound) is not int or degree_bound<0 or degree_bound>8:
        raise SpectralSourceError("declared finite McMillan order bound required")
    a=rational_response(*first);b=rational_response(*second)
    if max(len(a[0])-1,len(a[1])-1,len(b[0])-1,len(b[1])-1)>degree_bound:
        raise SpectralSourceError("one source exceeds prior rational complexity")
    if len(freqs)<2*degree_bound+1:
        raise SpectralSourceError("insufficient complete verification frequencies")
    freq=tuple(number(s) for s in freqs)
    if len(set(freq))!=len(freq):
        raise SpectralSourceError("repeated observations not new frequencies")
    matches=all(response_at(a,s)==response_at(b,s) for s in freq)
    if matches and a!=b:
        raise ArithmeticError("degree-bound rational identity theorem violated")
    return matches


def boundary_krylov_top_coefficient(g):
    """Coefficient of deepest site in A^(n-1)e1; exact minimality certificate."""
    g=_conductances(g);n=len(g)-1
    if n<1:raise SpectralSourceError("hidden chain required")
    return F(-1)**(n-1)*prod(g[1:n])


def approximate_hidden_mode_pair(coupling):
    """Different-length, arbitrarily close responses as coupling -> 0+."""
    eps=number(coupling)
    if not 0<eps<1:
        raise SpectralSourceError("strictly positive weak coupling <1 required")
    return chain_response((1,eps)),chain_response((1,eps,1))
