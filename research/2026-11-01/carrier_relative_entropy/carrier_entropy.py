"""Exact finite carrier-relative digit statistics for the original BBP zero seed.

This module implements observables, not a pi-normality proof. Every state and
partition count is exact Fraction/integer; logarithmic entropy is a diagnostic
only. The genuine asymptotic signed/collision saving remains open.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from collections import Counter
from math import log, sqrt, isqrt
from typing import Iterable

B = 16


def source(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('source time must be positive int')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def source_combined(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('source time must be positive int')
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def selected_states(n: int) -> tuple[Fraction, ...]:
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative int horizon required')
    x=Fraction(0)
    out=[]
    for j in range(1,n+1):
        x=B*x+source(j)
        out.append(x)
    return tuple(out)


def cell(value: Fraction | int, depth: int, base: int = B) -> int:
    if type(depth) is not int or depth < 0 or type(base) is not int or base < 2:
        raise ValueError('valid integer resolution and base required')
    if type(value) not in (int, Fraction):
        raise ValueError('exact fractional input required')
    f=Fraction(value)
    return (base**depth * (f.numerator % f.denominator)) // f.denominator


def counts(values: Iterable[Fraction | int], depth: int, base: int=B) -> dict[int,int]:
    return dict(Counter(cell(value,depth,base) for value in values))


def prefix_project(index: int, from_depth: int, to_depth: int, base: int=B) -> int:
    if not (type(from_depth) is type(to_depth) is int and 0 <= to_depth <= from_depth
            and type(base) is int and base >= 2 and type(index) is int
            and 0 <= index < base**from_depth):
        raise ValueError('invalid prefix projection')
    return index // base**(from_depth-to_depth)


def consistent_refinement(fine: dict[int,int], fine_depth: int, coarse: dict[int,int], base:int=B) -> bool:
    image=Counter()
    for w,v in fine.items():
        if type(v) is not int or v < 0:
            raise ValueError('counts must be nonnegative integers')
        image[prefix_project(w,fine_depth,fine_depth-1,base)]+=v
    return {k:v for k,v in image.items() if v} == {k:v for k,v in coarse.items() if v}


def collision_defect_from_counts(c: dict[int,int], n:int, depth:int, base:int=B)->Fraction:
    if type(n) is not int or n<=0 or type(depth) is not int or depth<0 or type(base) is not int or base<2:
        raise ValueError('nonempty sample and valid carrier required')
    m=base**depth
    if sum(c.values())!=n or any(type(x) is not int or x<0 or x>=m or type(v) is not int or v<0 for x,v in c.items()):
        raise ValueError('invalid carrier counts')
    return Fraction(m*sum(t*t for t in c.values()),n*n)-1


def signed_collision_excess(c: dict[int,int], n:int, depth:int, base:int=B)->Fraction:
    m=base**depth
    _=collision_defect_from_counts(c,n,depth,base)
    off=sum(t*(t-1) for t in c.values())
    return Fraction(off,1)-Fraction(n*(n-1),m)


def collision_decomposition(c:dict[int,int],n:int,depth:int,base:int=B)->tuple[Fraction,Fraction,Fraction]:
    m=base**depth
    q=collision_defect_from_counts(c,n,depth,base)
    diagonal=Fraction(m-1,n)
    off=Fraction(m,n*n)*signed_collision_excess(c,n,depth,base)
    if q!=diagonal+off:
        raise AssertionError('signed collision identity failed')
    return q,diagonal,off


def entropy_from_counts(c:dict[int,int],n:int)->float:
    if type(n) is not int or n<=0 or sum(c.values())!=n or any(type(x) is not int or x<0 for x in c.values()):
        raise ValueError('nonempty sample counts required')
    return log(n) - sum(v*log(v) for v in c.values() if v)/n


def kl_from_counts(c:dict[int,int],n:int,depth:int,base:int=B)->float:
    _=collision_defect_from_counts(c,n,depth,base)
    return depth*log(base)-entropy_from_counts(c,n)


def conditional_entropy_increment(coarse:dict[int,int],fine:dict[int,int],n:int,depth:int,base:int=B)->float:
    if not consistent_refinement(fine,depth+1,coarse,base):
        raise ValueError('not a lawful observation refinement')
    return entropy_from_counts(fine,n)-entropy_from_counts(coarse,n)


def conditional_defect(coarse:dict[int,int],fine:dict[int,int],n:int,depth:int,base:int=B)->float:
    return log(base)-conditional_entropy_increment(coarse,fine,n,depth,base)


def empirical_profile(values:tuple[Fraction,...],max_depth:int,base:int=B)->dict:
    if not values or type(max_depth) is not int or max_depth < 1:
        raise ValueError('nonempty sample and positive depth required')
    n=len(values)
    out=[]
    prev={0:n}
    for k in range(1,max_depth+1):
        c=counts(values,k,base)
        q,diag,off=collision_decomposition(c,n,k,base)
        out.append({'depth':k,'occupied':len(c),'cells':base**k,
                    'entropy_nats':entropy_from_counts(c,n),
                    'kl_nats':kl_from_counts(c,n,k,base),
                    'conditional_deficit_nats':conditional_defect(prev,c,n,k-1,base),
                    'collision_defect':str(q),'diagonal':str(diag),
                    'centered_offdiagonal':str(off)})
        prev=c
    return {'horizon':n,'base':base,'profile':out}


def rational_sqrt_upper(x: Fraction, digits: int=30) -> Fraction:
    """Outward rational sqrt bound, not a floating approximation."""
    q=Fraction(x)
    if q<0 or type(digits) is not int or not 1<=digits<=120:
        raise ValueError('nonnegative rational and bounded precision required')
    den=10**digits
    floor=isqrt((q.numerator*den*den)//q.denominator)
    lo=Fraction(floor,den)
    if lo*lo==q:return lo
    return Fraction(floor+1,den)


def certified_weyl_ceiling(c:dict[int,int],n:int,depth:int,h:int,base:int=B,digits:int=30)->Fraction:
    """Exact rational upper bound for the ORIGINAL selected real Fourier mean.

    Under 0<|h|<M the discrete M-clock character has zero uniform mean.
    DFT Parseval + cell Lipschitz, 2pi<44/7:
       |A_N(h)| <= sqrt(Q_N,k)+44|h|/(7M).
    Only the square-root ceiling is rounded; the final output is rational.
    This proves NO signed cancellation unless the actual cell Q tends to 0.
    """
    if type(h) is not int or not 0<abs(h)<base**depth:
        raise ValueError('harmonic must be nonzero and below carrier modulus')
    return rational_sqrt_upper(collision_defect_from_counts(c,n,depth,base),digits)+Fraction(44*abs(h),7*base**depth)


def collision_weyl_bound(c:dict[int,int],n:int,depth:int,h:int,base:int=B)->float:
    """Rigorous theorem bound |A_N(h)| <= sqrt(Q)+44|h|/(7 b^k).

    Uses pi<22/7 and exact Q. For h divisible by b**k this is NOT a
    meaningful nonzero-DFT-character bound; reject instead of false certainty.
    Returned float is only a display approximation; compare squared rational
    inequalities for certified conclusions.
    """
    if type(h) is not int or h==0 or h % (base**depth)==0:
        raise ValueError('need a nontrivial finite group character')
    q=collision_defect_from_counts(c,n,depth,base)
    return sqrt(q.numerator/q.denominator)+Fraction(44*abs(h),7*base**depth).__float__()


def conditional_path_surprisal(depth:int,base:int=B)->float:
    """Uniform virtual prior: SAME surprisal for every realized prefix.

    Not a test of normality and not a claim about external physical backaction.
    """
    if type(depth) is not int or depth<0 or type(base) is not int or base<2:
        raise ValueError('invalid virtual prior')
    return depth*log(base)


def debruijn_cycle(base:int=B,depth:int=2)->tuple[int,...]:
    """Standard exact FKM recursion for an alphabet's cyclic de Bruijn word."""
    if type(base) is not int or not 2<=base<=16 or type(depth) is not int or not 1<=depth<=5:
        raise ValueError('bounded exact de Bruijn control required')
    a=[0]*(base*depth+1)
    sequence=[]
    def db(t:int,p:int):
        if t>depth:
            if depth%p==0:
                sequence.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,base):
                a[t]=j
                db(t+1,t)
    db(1,1)
    if len(sequence)!=base**depth:
        raise ArithmeticError('de Bruijn construction failure')
    return tuple(sequence)


def cyclic_word_counts(cycle:tuple[int,...],depth:int,base:int=B)->dict[int,int]:
    if type(depth) is not int or depth<0 or not cycle or any(type(d) is not int or not 0<=d<base for d in cycle):
        raise ValueError('valid word and depth required')
    n=len(cycle)
    out=Counter()
    for s in range(n):
        w=0
        for i in range(depth):
            w=base*w+cycle[(s+i)%n]
        out[w]+=1
    return dict(out)


def rational_completed_counterfeit(n:int)->Fraction:
    """Rational completion of a positive, decreasing after-N source mutant.

    Identical original first n forcing values; for later j>n use
    r'(j)=r(n)*2**(-(j-n)). Completed alpha' is rational/non-normal.
    This source MUTATES the original four poles after the finite prefix.
    """
    if type(n) is not int or n<1:
        raise ValueError('finite prefix required')
    alpha=sum((source(j)/B**j for j in range(1,n+1)),Fraction(0))
    return alpha+Fraction(1,B**n)*source(n)/31


def source_stationarity_budget(n:int, sup_norm:Fraction|int=1, lipschitz:Fraction|int=1)->Fraction:
    """For x_n=U_n mod1, n=1..N: |avg f(16x_n)-avg f(x_n)|.

    Upper bound (2||f||infty + L sum_(n=1)^N r(n+1))/N;
    the source sum is exact rational. Applies to circle Lipschitz f.
    """
    if type(n) is not int or n<1:
        raise ValueError('positive horizon required')
    s=Fraction(sup_norm);l=Fraction(lipschitz)
    if s<0 or l<0:
        raise ValueError('nonnegative norm bounds required')
    return (2*s+l*sum((source(j+1) for j in range(1,n+1)),Fraction(0)))/n


def exact_resolution_ceiling(n:int, depth:int, base:int=B)->Fraction:
    """For uniform cell support ≤n: KL >= log(base**depth/n) when M>n.

    Returns exact ratio M/n; entropy inequality is asserted in proof file.
    This is carrier-only and does not use any BBP data.
    """
    if type(n) is not int or n<=0 or type(depth) is not int or depth<0:
        raise ValueError('nonempty valid resolution required')
    return Fraction(base**depth,n)
