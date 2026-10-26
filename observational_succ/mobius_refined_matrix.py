"""Möbius-refined, source-labelled internal Fourier Gram walk.

Finite Q[Q/Z] identities; PSD only after cyclotomic evaluation.
Authentic source = unchanged four-pole BBP, U_0 = 0.
No pi digit, selected cancellation or normality inference.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import isqrt

from .succ_internal_matrix_walk import PhasePoly, authentic_r, circle

SOURCE = "Q:Coherent-Main-X-four-pole-BBP"


def integer(x, low=0, high=100000):
    if type(x) is not int or not low <= x <= high:
        raise ValueError("bounded ordinary integer required")
    return x


def primes_checked(primes):
    P = tuple(primes)
    if len(P) > 4 or P != tuple(sorted(set(P))):
        raise ValueError("sorted distinct primes, at most four")
    for p in P:
        integer(p, 2, 101)
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            raise ValueError("prime required")
    return P


def valuation(n, p):
    integer(p, 2, 101)
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


@dataclass(frozen=True)
class Point:
    n: int
    state: Q
    forcing: Q
    carry: int


@dataclass(frozen=True)
class Trace:
    points: tuple[Point, ...]
    source_id: str
    authenticated: bool

    def prefix(self, n):
        integer(n, 0, len(self.points))
        return Trace(self.points[:n], self.source_id, self.authenticated)

    def validate(self):
        u = Q(0)
        for n, pt in enumerate(self.points, 1):
            if pt.n != n or type(pt.state) is not Q or type(pt.forcing) is not Q:
                return False
            if type(pt.carry) is not int or pt.carry != (16*circle(u)+pt.forcing).__floor__():
                return False
            if self.authenticated and pt.forcing != authentic_r(n):
                return False
            if pt.state != 16*u+pt.forcing:
                return False
            u = pt.state
        return self.source_id == SOURCE if self.authenticated else self.source_id.startswith("CONTROL:")


def from_forcing(forces, source_id="CONTROL:other"):
    if not source_id.startswith("CONTROL:"):
        raise ValueError("untrusted forcing requires CONTROL: label")
    forces = tuple(forces)
    integer(len(forces), 0, 128)
    pts, u = [], Q(0)
    for n, r in enumerate(forces, 1):
        if type(r) is not Q:
            raise ValueError("exact Fraction forcing only")
        c = (16*circle(u)+r).__floor__()
        u = 16*u+r
        pts.append(Point(n,u,r,c))
    out = Trace(tuple(pts),source_id,False)
    assert out.validate()
    return out


def authentic(N):
    integer(N,0,128)
    control = from_forcing(tuple(authentic_r(n) for n in range(1,N+1)))
    out = Trace(control.points,SOURCE,True)
    if not out.validate():
        raise ArithmeticError("source authentication")
    return out


def label(pt, P, k):
    integer(k,0,4)
    return (pt.carry,tuple((pt.n % p**k,
             min(k,valuation(pt.forcing.denominator,p)),
             min(k,valuation(pt.state.denominator,p))) for p in P))


def zero(H):
    z=PhasePoly.zero()
    return tuple(tuple(z for _ in range(H)) for _ in range(H))


def plus(A,B):
    return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))


def matrix(points,H):
    out=zero(H)
    for pt in points:
        out=plus(out,tuple(tuple(PhasePoly.monomial((i-j)*pt.state)
                     for j in range(H)) for i in range(H)))
    return out


@dataclass(frozen=True)
class Snapshot:
    trace: Trace
    width: int
    primes: tuple[int,...]
    depth: int
    blocks: dict
    counts: dict

    def total(self):
        out=zero(self.width)
        for B in self.blocks.values():
            out=plus(out,B)
        return out


def build(trace,H=3,P=(3,5),k=1):
    if not isinstance(trace,Trace) or not trace.validate():
        raise ValueError("verified source-typed trace needed")
    integer(H,1,8)
    P=primes_checked(P)
    integer(k,0,4)
    groups={}
    for pt in trace.points:
        groups.setdefault(label(pt,P,k),[]).append(pt)
    return Snapshot(trace,H,P,k,
        {a:matrix(pts,H) for a,pts in groups.items()},
        {a:len(pts) for a,pts in groups.items()})


def project_label(a,from_P,to_P,k):
    carry,local=a
    return (carry,tuple((local[from_P.index(p)][0]%p**k,
        min(k,local[from_P.index(p)][1]),
        min(k,local[from_P.index(p)][2])) for p in to_P))


def coarsen(fine,H,P,k):
    integer(H,1,fine.width)
    P=primes_checked(P)
    integer(k,0,fine.depth)
    if not set(P).issubset(fine.primes):
        raise ValueError("unseen prime")
    blocks,counts={},{}
    for a,B in fine.blocks.items():
        b=project_label(a,fine.primes,P,k)
        crop=tuple(tuple(row[:H]) for row in B[:H])
        blocks[b]=plus(blocks.get(b,zero(H)),crop)
        counts[b]=counts.get(b,0)+fine.counts[a]
    return Snapshot(fine.trace,H,P,k,blocks,counts)


def cumulative(s,a,thresholds):
    carry,local=a
    chosen=[pt for pt in s.trace.points if pt.carry==carry and all(
        pt.n%p**s.depth==loc[0] and
        valuation(pt.forcing.denominator,p)>=lower[0] and
        valuation(pt.state.denominator,p)>=lower[1]
        for p,loc,lower in zip(s.primes,local,thresholds))]
    return matrix(chosen,s.width)


def invert_atom(s,a):
    """Exact product-of-chains Möbius inversion; recovered atom Gram is PSD."""
    if a not in s.blocks:
        raise ValueError("observed atom required")
    floors=tuple((x[1],x[2]) for x in a[1])
    free=tuple((p,t) for p,coords in enumerate(a[1])
               for t in (0,1) if coords[t+1]<s.depth)
    result=zero(s.width)
    for bits in product((0,1),repeat=len(free)):
        levels=[list(x) for x in floors]
        for bit,(p,t) in zip(bits,free):
            levels[p][t]+=bit
        B=cumulative(s,a,tuple(tuple(x) for x in levels))
        result=plus(result,tuple(tuple((-1)**sum(bits)*x for x in row)
                                 for row in B))
    return result


def moment(s,a,h=1):
    integer(abs(h),1,10000)
    if a not in s.blocks:
        raise ValueError("observed atom required")
    return sum((PhasePoly.monomial(h*pt.state) for pt in s.trace.points
        if label(pt,s.primes,s.depth)==a),PhasePoly.zero())


def energies(s,h=1):
    """Global |S|^2/N, conditional sum_a |S_a|^2/|a|."""
    N=len(s.trace.points)
    if N==0:
        raise ValueError("nonempty trace required")
    z={a:moment(s,a,h) for a in s.blocks}
    S=sum(z.values(),PhasePoly.zero())
    return (S*S.star()/N,
        sum((q*q.star()/s.counts[a] for a,q in z.items()),PhasePoly.zero()))


def variance(fine,coarse,h=1):
    """Refining conditional energy is a nonnegative *-sum of squares."""
    if fine.trace!=coarse.trace or coarsen(fine,coarse.width,
                                          coarse.primes,coarse.depth)!=coarse:
        raise ValueError("exact common trace/marginal required")
    acc=PhasePoly.zero()
    for a,m in coarse.counts.items():
        za=moment(coarse,a,h)
        for b,sz in fine.counts.items():
            if project_label(b,fine.primes,coarse.primes,coarse.depth)==a:
                residual=moment(fine,b,h)-Q(sz,m)*za
                acc+=residual*residual.star()/sz
    if energies(fine,h)[1]-energies(coarse,h)[1]!=acc:
        raise ArithmeticError("ANOVA identity")
    return acc


def cross_interference(s,h=1):
    z=[moment(s,a,h) for a in s.blocks]
    S=sum(z,PhasePoly.zero())
    return S*S.star()-sum((a*a.star() for a in z),PhasePoly.zero())


def fejer(delta,H):
    integer(H,1,8)
    value=PhasePoly.monomial(0,H)
    for j in range(1,H):
        value+=(PhasePoly.monomial(j*delta)+PhasePoly.monomial(-j*delta))*(H-j)
    return value


def conditioned_innovation(trace,H,P,k):
    """Source-typed q_(m,H) = sum_a |a|/m q_(m,H|a), no independence."""
    if not trace.validate() or len(trace.points)<2:
        raise ValueError(">=2 valid source observations")
    past=trace.prefix(len(trace.points)-1)
    s=build(past,H,P,k)
    arrival=trace.points[-1]
    q={}
    for a in s.blocks:
        q[a]=sum((fejer(arrival.state-pt.state,H) for pt in past.points
                  if label(pt,s.primes,s.depth)==a),PhasePoly.zero())/s.counts[a]
    return (sum((s.counts[a]*z for a,z in q.items()),PhasePoly.zero())/
            len(past.points),q)


def pole_classes(p):
    primes_checked((p,))
    if p<7:
        raise ValueError("3 and 5 are exceptional pole overlaps")
    return tuple(n for n in range(p)
        if ((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))%p==0)


def pole_count(N,p):
    """For p>=7: count(p|den r(n)) = 4*floor(N/p)+tail, |error|<=4."""
    integer(N,1,100000)
    roots=pole_classes(p)
    if len(roots)!=4:
        raise ArithmeticError("four pole roots")
    q,r=divmod(N,p)
    count=4*q+sum(1 for a in roots if 1<=a<=r)
    if N<=128 and count!=sum(authentic_r(n).denominator%p==0
                            for n in range(1,N+1)):
        raise ArithmeticError("exact pole denominator law")
    return count,Q(count)-Q(4*N,p),roots


def pole_crt_sieve(N,P):
    """Prime-labeled source count, NOT phase independence or cancellation.

    For P>=7, M=prod(P), survivors per complete M block = prod(p-4).
    Deleting other cells changes any selected Weyl sum by <= deleted count.
    """
    integer(N,1,100000)
    P=primes_checked(P)
    if not P or any(p<7 for p in P):
        raise ValueError("nonempty P with p>=7")
    M,per=1,1
    roots={p:set(pole_classes(p)) for p in P}
    for p in P:
        M*=p
        per*=p-4
    if M>250000:
        raise ValueError("declared CRT budget")
    q,r=divmod(N,M)
    keep=q*per+sum(all(n%p not in roots[p] for p in P)
                   for n in range(1,r+1))
    if N<=128 and keep!=sum(all(authentic_r(n).denominator%p
                     for p in P) for n in range(1,N+1)):
        raise ArithmeticError("CRT/source mismatch")
    return {"source":SOURCE,"N":N,"primes":P,"period":M,
            "survivors_per_period":per,"survivors":keep,"deleted":N-keep,
            "max_deleted_weyl_modulus":N-keep,"normality_proved":False}
