"""Independent stdlib-only rational and combinatorial oracle, separate algorithms.

Direct polynomial source and forward convolution are used instead of the
four-pole step recurrence. Pair collision checks do not use aggregated counts.
"""
from fractions import Fraction as F
from collections import Counter


def source_combined_direct(j:int)->F:
    return F(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))


def convolution_states(n:int)->tuple[F,...]:
    # Sum in the opposite computational arrangement from the recurrence.
    return tuple(sum((F(16**(k-j))*source_combined_direct(j)
                       for j in range(1,k+1)),F(0)) for k in range(1,n+1))


def residue_cell(x:F,k:int,base:int=16)->int:
    y=x-F(x.numerator//x.denominator)
    y*=base**k
    return y.numerator//y.denominator


def pair_excess(values:tuple[F,...],k:int,base:int=16)->F:
    words=tuple(residue_cell(x,k,base) for x in values)
    n=len(words)
    off=sum(1 for i in range(n) for j in range(n) if i!=j and words[i]==words[j])
    return F(off)-F(n*(n-1),base**k)


def brute_prefix_consistency(values:tuple[F,...],k:int,base:int=16)->bool:
    a=Counter(residue_cell(x,k,base) for x in values)
    b=Counter(residue_cell(x,k+1,base)//base for x in values)
    return a==b


def cyclic_window_count(word:tuple[int,...],k:int,base:int=16)->dict[int,int]:
    out=Counter()
    for start in range(len(word)):
        val=0
        for j in range(k):val=base*val+word[(start+j)%len(word)]
        out[val]+=1
    return dict(out)


def shifted_successor_error_sum(n:int)->F:
    return sum((source_combined_direct(j+1) for j in range(1,n+1)),F(0))
