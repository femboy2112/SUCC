"""Independent arithmetic checks: cyclic group basis and frequency collision counts.

This does not import seed_superposition. It calculates the finite group
character sums using the cyclotomic antipodal quotient, not any shortcut
from the test module. Mathematical truth about arbitrary N remains in proofs.
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from math import factorial


def independent_cyclic_grid(order: int, exponent: int) -> tuple[int,...]:
    """Polynomial sum_(j=0)^(order-1) X^(exponent*j) mod X^(order/2)+1.

    The returned zero vector iff exact evaluation at primitive order-th
    complex root is zero. Here order is a power of 16.
    """
    if order < 2 or order & (order-1):raise ValueError("power-of-two order")
    a=[0]*(order//2)
    for j in range(order):
        r=(exponent*j)%order
        a[r%(order//2)]+=(1 if r<order//2 else -1)
    return tuple(a)


def direct_equal_count_collisions(k: int, r: int) -> tuple[int,int]:
    """Enumerate count-vectors rather than r-tuples; independent from prior DP.

    Returns (distinct weights, pairs of distinct vectors with same power sum).
    """
    if not 1<=k<=6 or not 0<=r<=20:
        raise ValueError("k=1..6, r=0..20")
    freq=Counter()
    def recurse(j, remaining, total):
        if j==k-1:
            freq[total+remaining*16**j]+=1
            return
        for c in range(remaining+1):
            recurse(j+1,remaining-c,total+c*16**j)
    recurse(0,r,0)
    return len(freq), sum(c*(c-1)//2 for c in freq.values())


def direct_haar_moment_tuples(k: int, r: int) -> int:
    """Full 2r sample moments without using multinomial-composition formula."""
    if k<1 or r<0 or k**r>200_000:
        raise ValueError("oracle limited to <=200000 tuples")
    raw=Counter(sum(16**i for i in word)
                for word in product(range(k),repeat=r))
    return sum(n*n for n in raw.values())


if __name__=="__main__":
    print({"roots_256_f_1":independent_cyclic_grid(256,1),
        "roots_256_f_256":independent_cyclic_grid(256,256),
        "r16":direct_equal_count_collisions(3,16),
        "r17":direct_equal_count_collisions(3,17),
        "moment_k3_r4":direct_haar_moment_tuples(3,4)})
