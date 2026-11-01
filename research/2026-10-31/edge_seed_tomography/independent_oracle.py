"""Separate brute-force check of moments, cyclic incidence, and Fourier aliasing.

Does not import the main research module; exact integer/rational algorithms.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def brute_fourth_collision(n: int, base: int=16) -> int:
    if not 1<=n<=12:
        raise ValueError("oracle n range 1..12")
    freq=[base**j for j in range(1,n+1)]
    return sum(a+b==c+d for a,b,c,d in product(freq,repeat=4))


def brute_73_difference_set() -> dict:
    seq=[pow(16,n,73) for n in range(1,10)]
    labels=[(a-b)%73 for i,a in enumerate(seq) for j,b in enumerate(seq) if i!=j]
    counts=Counter(labels)
    assert len(seq)==len(set(seq))==9
    assert sorted(labels)==list(range(1,73))
    assert len(counts)==72 and all(c==1 for c in counts.values())
    lines=[{(t+d)%73 for d in seq} for t in range(73)]
    assert all(len(line)==9 for line in lines)
    assert all(len(a&b)==1 for i,a in enumerate(lines) for b in lines[i+1:])
    point_pair_count=Counter(tuple(sorted((a,b))) for line in lines for a in line for b in line if a<b)
    assert len(point_pair_count)==73*72//2
    assert all(value==1 for value in point_pair_count.values())
    return {'residues':tuple(sorted(seq)),'ordered_differences':72,
            'lines':len(lines),'point_pairs':len(point_pair_count)}


def brute_phase_response(N:int,h:int,modulus:int,seed:Fraction=Fraction(0)) -> dict:
    """Symbolic group-ring response: integer Fourier labels -> rational phase modulo 1.

    Source via explicit finite convolution, not recurrent U_n implementation.
    """
    if N<2 or h==0 or modulus<2:raise ValueError('invalid input')
    def force(n:int)->Fraction:
        # alternate grouped four-pole formula (integral of P(t))
        k=8*n-8
        return Fraction(4,k+1)-Fraction(2,k+4)-Fraction(1,k+5)-Fraction(1,k+6)
    u=[seed]
    for n in range(1,N+1):
        u.append(16**n*seed+sum((16**(n-k)*force(k) for k in range(1,n+1)),Fraction(0)))
    labels=Counter((h*(16**n-16**m))%modulus for n in range(1,N+1) for m in range(1,N+1) if n!=m)
    if 0 in labels or len(labels)!=N*(N-1) or any(value!=1 for value in labels.values()):
        raise ValueError('intensity group ring contains collisions')
    return {(h*(16**n-16**m))%modulus: (h*(u[n]-u[m]))%1
            for n in range(1,N+1) for m in range(1,N+1) if n!=m}


def discrete_fourth_collision(n:int,modulus:int)->int:
    """Exact group-ring discrete fourth moment (no floating-point roots)."""
    if n<1 or modulus<2:raise ValueError('n>=1, modulus>=2')
    xs=[pow(16,j,modulus) for j in range(1,n+1)]
    sums=Counter((a+b)%modulus for a,b in product(xs,repeat=2))
    return sum(c*c for c in sums.values())


def brute_fourth_cylinder(N:int,k:int)->int:
    """All pair-of-pairs identities for frequencies 16^(n-k), n>=max(k,1)."""
    from itertools import product
    freq=[16**(n-k) for n in range(max(1,k),N+1)]
    return sum(a+b==c+d for a,b,c,d in product(freq,repeat=4))

if __name__=='__main__':
    print(brute_73_difference_set())
    print('fourth moments',[(i,brute_fourth_collision(i)) for i in range(1,10)])
