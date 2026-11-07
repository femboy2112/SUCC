"""Exact arithmetic instruments for the fixed golden aperture, SUCC research only.

No normality assumption. Original four-pole source and literal zero seed.
Every finite energy enclosure uses only rational operations and integer sqrt.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache


def forcing(n:int)->F:
    if not isinstance(n,int) or n<1: raise ValueError('integer n >= 1 required')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def independent_forcing(n:int)->F:
    if not isinstance(n,int) or n<1: raise ValueError('integer n >= 1 required')
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def selected_states(max_n:int)->list[F]:
    """Exact fractions of BBP states U_n modulo 1, from U_0=0."""
    u=F(0); out=[u]
    for n in range(1,max_n+1):
        u=(16*u+forcing(n))%1
        out.append(u)
    return out


def golden_b_bounds(decimals:int=35)->tuple[F,F]:
    """Exact rational bounds on b=(3-sqrt(5))/2 via integer sqrt."""
    if decimals<2: raise ValueError('precision')
    s=10**decimals; r=isqrt(5*s*s)
    lo=(F(3)-F(r+1,s))/2
    hi=(F(3)-F(r,s))/2
    assert 0<lo<hi<F(1,2)
    return lo,hi


def d_less_than_golden_b(d:F)->bool:
    """Rational circular distance 0<=d<=1/2; exact Q(sqrt5) compare."""
    if not F(0)<=d<=F(1,2): raise ValueError('0 <= distance <= 1/2')
    return (3-2*d)**2 >5  # 3-2d is positive


def circle_distance(x:F,y:F)->F:
    d=abs(x-y)
    return min(d,1-d)


def golden_pair_census_bruteforce(points:list[F])->tuple[int,F]:
    """K ordered near pairs (including diagonal), D sum ordered distances, d<b."""
    count=len(points)
    if count<1:raise ValueError('nonempty sample')
    k=count; total_d=F(0)
    for i in range(count):
        assert F(0)<=points[i]<1
        for j in range(i+1,count):
            d=circle_distance(points[i],points[j])
            if d_less_than_golden_b(d):
                k+=2
                total_d+=2*d
    return k,total_d


def golden_pair_census(points:list[F])->tuple[int,F]:
    """Exact O(N log N) pair census: cyclic sorted-window triangle.

    For b<1/2 each unordered nearby pair has exactly one short positive
    circular arc. Duplicate locations still contribute as pairs by index.
    """
    N=len(points)
    if N<1:raise ValueError('nonempty sample')
    ordered=sorted(points)
    if ordered[0]<0 or ordered[-1]>=1:raise ValueError('circle fractions [0,1)')
    y=ordered+[z+1 for z in ordered]
    prefix=[F()]
    for z in y:prefix.append(prefix[-1]+z)
    j=1;pair_count=0;distance_sum=F()
    for i in range(N):
        if j<i+1:j=i+1
        while j<i+N:
            gap=y[j]-y[i]
            if gap>=F(1,2) or not d_less_than_golden_b(gap):break
            j+=1
        count=j-i-1
        pair_count+=count
        distance_sum+=prefix[j]-prefix[i+1]-count*y[i]
    return N+2*pair_count, 2*distance_sum


def golden_aperture_energy_bounds(points:list[F],decimals:int=35)->tuple[F,F,dict]:
    """Rigorous rational lower/upper enclosure of E_a, with a=1/phi, b=a^2."""
    n=len(points); k,dist=golden_pair_census(points)
    blo,bhi=golden_b_bounds(decimals)
    # E_a = K/n^2 - dist/(b n^2) - b ; monotone interval arithmetic
    low=F(k,n*n)-dist/(blo*n*n)-bhi
    high=F(k,n*n)-dist/(bhi*n*n)-blo
    return low,high,{'points':n,'near_ordered_pairs':k,'sum_distances':dist,'b_lo':blo,'b_hi':bhi}


def source_tail_upper(n:int)->F:
    if n<1:raise ValueError('n>=1')
    return F(1,15*(n+1)**2)


def harmonic_epoch_sum(A:int)->F:
    if A<1:raise ValueError('A>=1')
    return sum((F(1,n+1) for n in range(A,2*A)),F())


def transport_bound_approx(A:int)->float:
    """Upper bound on golden sqrt L2 energy transport, display ONLY."""
    import math
    a=(math.sqrt(5)-1)/2
    return math.sqrt(2/15)*float(harmonic_epoch_sum(A))/(a*A)


def epoch_energy(A:int, states:list[F]|None=None,decimals:int=35):
    if states is None:states=selected_states(2*A-1)
    return golden_aperture_energy_bounds(states[A:2*A],decimals)


def golden_bound_float(energy:tuple[F,F,dict]):
    low, high,_=energy
    return float(low),float(high)


def golden_return_energy_bounds(points:list[F],Q:int, decimals:int=35):
    """Golden-aperture spatial collision energy averaged over Q return fibers."""
    N=len(points)
    if Q<1 or Q & (Q-1) or N%Q:raise ValueError('Q must be a power of 2 dividing N')
    M=N//Q
    # For each fiber, E = K/M² - D/(b M²) - b.
    K=0; D=F(0)
    for a in range(Q):
        k,d=golden_pair_census(points[a:N:Q]);K+=k;D+=d
    blo,bhi=golden_b_bounds(decimals)
    base=F(K,Q*M*M)
    lo=base-D/(blo*Q*M*M)-bhi
    hi=base-D/(bhi*Q*M*M)-blo
    return lo,hi,{'Q':Q,'M':M,'near_ordered_pairs':K,'sum_distances':D}


def cutoff_interval_integral(k:int,total_distance:F,n:int,decimals:int=35)->tuple[F,F]:
    """Integrate exact empirical excess B_A(t)-2A²t up to b, then divide bA².

    Direct alternative formula: integral = k*b - total_distance - n²*b².
    """
    blo,bhi=golden_b_bounds(decimals)
    # b interval also enters quadratic; conservative monotone interval operations
    # For E = k/n² - D/(b*n²) - b, as above.
    return F(k,n*n)-total_distance/(blo*n*n)-bhi, F(k,n*n)-total_distance/(bhi*n*n)-blo


def golden_energy_tail_transport_upper(A:int, decimals:int=35)->F:
    """Rigorous |E_gold(pi epoch)-E_gold(original rational epoch)| <= 1/(15*b*A²)."""
    if A<1:raise ValueError('A>=1')
    blo,_=golden_b_bounds(decimals)
    return F(1,15*A*A)/blo


def completed_energy_bounds_from_original(A:int, states:list[F]|None=None,
                                          decimals:int=35)->tuple[F,F]:
    """Rigorous outward bounds on true π completed-orbit golden energy, no π digits."""
    lo,hi,_=epoch_energy(A,states,decimals)
    err=golden_energy_tail_transport_upper(A,decimals)
    return max(F(0),lo-err),hi+err


def partial_future_tail(n:int, depth:int=16)->F:
    if n<1 or depth<1:raise ValueError('n>=1, depth>=1')
    return sum((forcing(n+j)/16**j for j in range(1,depth+1)),F())


def fixedpoint_golden_pair_census(points:list[F],digits:int=28):
    """Certified near-pair count and *interval* for ordered distance sum.

    Fixedpoint sorting is checked for collisions. Every threshold classification
    is certified by integer lower/upper bands or falls back to exact rational.
    O(N log N) with O(N)-sized integers rather than cumulative huge fractions.
    """
    if digits<8:raise ValueError('digits >=8')
    N=len(points)
    if not N:raise ValueError('nonempty sample')
    P=10**digits
    arr=sorted((x.numerator*P//x.denominator,x) for x in points)
    if any(arr[i][0]==arr[i+1][0] for i in range(N-1)):
        raise ValueError('precision collision; increase digits or use exact sweep')
    ys=[a for a,x in arr]
    yy=ys+[a+P for a in ys]
    exact= [x for a,x in arr]
    xx=exact+[x+1 for x in exact]
    pref=[0]
    for v in yy:pref.append(pref[-1]+v)
    blo,bhi=golden_b_bounds(digits+5)
    B_lo=blo.numerator*P//blo.denominator
    B_hi= -((-bhi.numerator*P)//bhi.denominator) # ceil(P*b_hi)
    j=1;near=0;total_fp=0;ambiguous=0
    for i in range(N):
        if j<i+1:j=i+1
        while j<i+N:
            dy=yy[j]-yy[i]
            if dy+1 < B_lo: inside=True
            elif dy-1 > B_hi: inside=False
            else:
                ambiguous+=1
                gap=xx[j]-xx[i]
                inside=gap<F(1,2) and d_less_than_golden_b(gap)
            if not inside:break
            j+=1
        c=j-i-1
        near+=c
        total_fp+=pref[j]-pref[i+1]-c*yy[i]
    # Every selected *short* gap differs from integer fixedpoint difference/P
    # by less than 1/P in absolute value; count both orientations.
    dlo=max(F(),F(2*(total_fp-near),P))
    dhi=F(2*(total_fp+near),P)
    return N+2*near,dlo,dhi,{'digits':digits,'ambiguous_fallbacks':ambiguous,'unique_pairs':near}


def golden_aperture_interval_fast(points:list[F],digits:int=28):
    """Rigorous interval energy computed in O(N logN) and O(N) fixedpoint."""
    N=len(points)
    k,dlo,dhi,diag=fixedpoint_golden_pair_census(points,digits)
    blo,bhi=golden_b_bounds(digits+5)
    lo=F(k,N*N)-dhi/(blo*N*N)-bhi
    hi=F(k,N*N)-dlo/(bhi*N*N)-blo
    return lo,hi,diag|{'near_ordered_pairs':k}


def golden_return_energy_interval_fast(points:list[F],Q:int,digits:int=28):
    """Rigorous fixedpoint triangle-energy interval averaged across Q=2^k fibers."""
    N=len(points)
    if Q<1 or Q & (Q-1) or N%Q: raise ValueError('Q must be power of 2 dividing N')
    M=N//Q
    K=0; Dlow=F(); Dhigh=F(); fallbacks=0
    for a in range(Q):
        k,lo,hi,diag=fixedpoint_golden_pair_census(points[a:N:Q],digits)
        K+=k;Dlow+=lo;Dhigh+=hi;fallbacks+=diag['ambiguous_fallbacks']
    blo,bhi=golden_b_bounds(digits+5)
    lower=F(K,Q*M*M)-Dhigh/(blo*Q*M*M)-bhi
    upper=F(K,Q*M*M)-Dlow/(bhi*Q*M*M)-blo
    return lower,upper,{'Q':Q,'M':M,'ordered_near_pairs':K,'ambiguous_fallbacks':fallbacks}
