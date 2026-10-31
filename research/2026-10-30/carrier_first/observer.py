"""Exact finite observer instruments; no distributional assumption on BBP."""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import log


def floor(x):
    return x.numerator // x.denominator


def frac(x):
    return x-floor(x)


def source(n):
    if n < 1:
        raise ValueError('positive source clock required')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


@dataclass(frozen=True)
class ArithmeticState:
    clock: int = 0
    lift: Q = Q(0)
    carries: tuple = ()
    source_id: str = 'original-four-pole'

    def __post_init__(self):
        if self.source_id!='original-four-pole':
            raise ValueError('this realization supports only the original four-pole source')
        if self.clock<0 or len(self.carries)!=self.clock:
            raise ValueError('clock and full carry history must agree')

    def step(self):
        r=source(self.clock+1)
        y=16*self.lift+r
        carry=floor(16*frac(self.lift)+r)
        return ArithmeticState(self.clock+1,y,self.carries+(carry,),self.source_id)


def rational_orbit(x,N,b=16):
    x=frac(Q(x)); result=[]
    for _ in range(N):
        result.append(x); x=frac(b*x)
    return result


def word_counts(word,N,k,b=16):
    if N<1 or k<0 or len(word)<N+k or any(not 0<=d<b for d in word):
        raise ValueError('need N+k valid digits')
    counts=Counter()
    for n in range(N):
        v=0
        for d in word[n+1:n+k+1]: v=b*v+d
        counts[word[n],v]+=1
    return counts


def branch_cost(counts,b=16):
    N=sum(counts.values())
    totals=Counter()
    for (d,v),c in counts.items(): totals[v]+=c
    cost=Q(0);tv=Q(0);deficiency=0.;sampling_floor=0.
    for v,total in totals.items():
        acc=0
        for d in range(b):
            c=counts.get((d,v),0)
            tv+=abs(Q(c)-Q(total,b))
            if c: deficiency+=c/N*log(b*c/total)
            acc+=c
            if d<b-1: cost+=abs(Q(acc)-Q((d+1)*total,b))
        sampling_floor+=total/N*log(b/min(b,total))
    return dict(rho=cost/(b*N),tv=tv/(2*N),deficiency=deficiency,
                sampling_floor=sampling_floor,occupied_futures=len(totals),N=N)


def transport_bound(counts,k,b=16):
    r=branch_cost(counts,b)
    return (b*r['rho']+Q(1,b**k)+Q(1,r['N']))/(b-1)


def w1_uniform(points):
    """Exact integral of empirical quantile distance from uniform quantile."""
    N=len(points);total=Q(0)
    for i,x in enumerate(sorted(points)):
        a=Q(i,N)-x;z=Q(i+1,N)-x
        total+=(z*abs(z)-a*abs(a))/2
    return total


def minimal_states(word):
    if not word: return 0
    N=len(word);best=N;witness=(N-1,1)
    for p in range(1,N+1):
        last=next((i for i in range(N-1,p-1,-1) if word[i]!=word[i-p]),p-1)
        S=max(p,last+1)
        if S<best:best=S;witness=(S-p,p)
    return best,witness


def completed_bbp_word(L):
    """First L digits of {pi}, from original zero-seed source only.

    Positive decreasing source bounds the omitted alpha=pi/16 series.
    Raises at an unresolved boundary; never guesses a digit.
    """
    R=L+12
    a=sum((source(j)/16**j for j in range(1,R+1)),Q(0))
    err=source(R+1)/(15*16**R)
    lo=floor(16**(L+1)*a);hi=floor(16**(L+1)*(a+err))
    if lo!=hi:raise ArithmeticError('increase tail precision')
    z=lo%16**L
    return tuple((z//16**(L-1-i))%16 for i in range(L))


def debruijn(b,k):
    """Classical necklace recursion, used only as a hostile periodic control."""
    a=[0]*(b*k);seq=[]
    def db(t,p):
        if t>k:
            if k%p==0:seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p];db(t+1,p)
            for j in range(a[t-p]+1,b):a[t]=j;db(t+1,t)
    db(1,1)
    return tuple(seq)


def periodic_value(word,b):
    z=0
    for d in word:z=b*z+d
    return Q(z,b**len(word)-1)
