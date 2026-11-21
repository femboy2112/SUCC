"""Source-faithful finite computations for a causal-journal / analytic-seam research dossier.

NO computation here certifies pi normality, physical randomness, or a quantum
carrier. Finite tests are illustrations of independent paper proofs.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt, lcm
from typing import Callable, Hashable, Iterable, Sequence


def prime(n: int) -> bool:
    if type(n) is not int:
        raise TypeError("integer expected")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def seam_clock(p: int) -> int:
    """Clock j_p where 8*j_p-7=p^2, p an actual prime >=7."""
    if type(p) is not int or p < 7 or not prime(p):
        raise ValueError("prime p >= 7 required")
    assert (p*p+7)%8 == 0
    return (p*p+7)//8


def first_pole_seam(n: int, tag: int = 4) -> int:
    """Canonical p^2-amplified mark, zero unless 8n-7 is prime-square.

    tag=4: BBP first-pole p-primary fraction; tag=5: declared
    matched-first-jet mutant Q+(1-t)^2.
    """
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if type(tag) is not int:
        raise TypeError("integer tag")
    m = 8*n-7
    if m < 49:
        return 0
    p = isqrt(m)
    return tag if p*p == m and p >= 7 and prime(p) else 0


def consecutive_prime_gap(p: int, q: int) -> int:
    if type(p) is not int or type(q) is not int or not (p >= 7 and p < q):
        raise ValueError("ordered primes >=7 required")
    if not prime(p) or not prime(q) or any(prime(r) for r in range(p+1, q)):
        raise ValueError("arguments must be consecutive primes")
    return seam_clock(q) - seam_clock(p)


def gap_hankel(p: int, q: int, tag: int=4) -> tuple[tuple[int, ...], ...]:
    """H[a,b]=mark(j_p+1+a+b), 0<=a,b<L, L=j_q-j_p."""
    L = consecutive_prime_gap(p,q)
    t = seam_clock(p)+1
    return tuple(tuple(first_pole_seam(t+i+j,tag) for j in range(L))
                 for i in range(L))


def predicted_hankel_det(p: int, q: int, tag: int=4) -> int:
    L = consecutive_prime_gap(p,q)
    return (-1 if ((L*(L-1)//2)%2) else 1)*tag**L


def bareiss_det(matrix: Sequence[Sequence[int]]) -> int:
    """Independent integer determinant implementation, with exact divisions."""
    n=len(matrix)
    if not n:
        return 1
    if any(len(row)!=n for row in matrix):
        raise ValueError("square matrix required")
    common=lcm(*(Fraction(z).denominator for row in matrix for z in row))
    if common != 1:
        integer_matrix=[[int(Fraction(z)*common) for z in row] for row in matrix]
        return Fraction(bareiss_det(integer_matrix),common**n)
    a=[list(map(int,row)) for row in matrix]
    sign=1
    denom=1
    for k in range(n-1):
        if a[k][k]==0:
            q=next((i for i in range(k+1,n) if a[i][k]),None)
            if q is None: return 0
            a[k],a[q]=a[q],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                if num%denom: raise ArithmeticError("nonexact Bareiss division")
                a[i][j]=num//denom
        for i in range(k+1,n): a[i][k]=0
        denom=pivot
    return sign*a[-1][-1]


def bbp_forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("forcing clock must be >=1")
    return (Fraction(4,8*n-7) - Fraction(2,8*n-4)
            - Fraction(1,8*n-3) - Fraction(1,8*n-2))


def bbp_mutant_forcing(n: int) -> Fraction:
    """Exact Mellin Q+(1-t)^2 mutation; NOT the authentic four-pole source."""
    return bbp_forcing(n) + Fraction(2,(8*n-7)*(8*n-6)*(8*n-5))


def p_primary_fraction(x: Fraction, p: int) -> Fraction:
    """Canonical p-primary fractional part in [0,1), not an untyped norm."""
    if type(x) is not Fraction or not prime(p):
        raise ValueError("rational x and prime p required")
    denom=x.denominator
    pp=1
    while denom % p == 0:
        denom//=p
        pp*=p
    if pp == 1: return Fraction()
    numerator=(x.numerator*pow(denom,-1,pp))%pp
    return Fraction(numerator,pp)


def source_atom(n: int) -> Fraction:
    return bbp_forcing(n)/16**n


def source_prefix(n: int) -> Fraction:
    if type(n) is not int or n<0: raise ValueError("n >= 0")
    return sum((source_atom(j) for j in range(1,n+1)),Fraction())


def source_tail_upper(n: int) -> Fraction:
    """Exact positive upper bound for sum_{j>n} c_j, via decreasing r."""
    if type(n) is not int or n <0: raise ValueError("n >=0")
    return bbp_forcing(n+1)/ (15*16**n)


def truncated_germ(n: int, end: int) -> tuple[Fraction, ...]:
    """Coefficients of G_n^[end](z)=sum_{k>=0}c_(n+k+1) z^k."""
    if type(n) is not int or type(end) is not int or not (0<=n<=end):
        raise ValueError("0 <= n <= end")
    return tuple(source_atom(j) for j in range(n+1,end+1))


def backward_shift(coefficients: Sequence[Fraction]) -> tuple[Fraction,...]:
    return tuple(coefficients[1:])


def eval_germ(coefficients: Sequence[Fraction], z: Fraction|int=1) -> Fraction:
    z=Fraction(z)
    return sum((Fraction(c)*z**j for j,c in enumerate(coefficients)),Fraction())


def terminal_seam(n: int, M: int) -> tuple[Fraction,Fraction,Fraction]:
    """P_n, G_n^[M](1), P_M with P_n+G_n^[M](1)=P_M exactly."""
    P=source_prefix(n)
    G=eval_germ(truncated_germ(n,M))
    return P,G,source_prefix(M)


def alias_upper(j: int, modulus: int) -> Fraction:
    """Exact bound for root-of-unity alias: sum_{k>=1}c_(j+kM)."""
    if type(j) is not int or type(modulus) is not int or not 1<=j<=modulus:
        raise ValueError("1 <= j <= modulus")
    return (bbp_forcing(j+modulus)
            / (16**(j+modulus) * (1-Fraction(1,16**modulus))))


def aliased_prefix(j: int, modulus: int, end: int) -> Fraction:
    """Residue-class source weights through a finite end clock."""
    if not 1<=j<=modulus or end<j:
        raise ValueError("invalid alias arguments")
    return sum((source_atom(n) for n in range(j,end+1,modulus)),Fraction())


def finite_journal(T: Callable, readout: Callable, state, count: int):
    if type(count) is not int or count<0: raise ValueError("count >=0")
    results=[]
    for _ in range(count):
        results.append(readout(state))
        state=T(state)
    return tuple(results)


def finite_observational_quotient(states: Iterable[Hashable], T: Callable, readout: Callable):
    """Exact future-safe Moore quotient for a finite CLOSED state set.

    Returns class labels as frozensets of ORIGINAL states; these encode the
    full forward journal up to the stable partition, not a spurious quotient.
    """
    states=tuple(states)
    S=set(states)
    if len(S)!=len(states) or any(T(s) not in S for s in states):
        raise ValueError("distinct states and closed action required")
    signatures={s:(readout(s),) for s in states}
    partition=None
    for _ in range(len(states)+1):
        classes={}
        for s in states:
            classes.setdefault(signatures[s],set()).add(s)
        newpartition=frozenset(frozenset(x) for x in classes.values())
        if newpartition==partition:
            break
        partition=newpartition
        signatures={s:(readout(s),signatures[T(s)]) for s in states}
    else:
        raise AssertionError("finite Moore partition did not stabilize")
    class_of={s:cl for cl in partition for s in cl}
    for cl in partition:
        if len({readout(s) for s in cl})!=1 or len({class_of[T(s)] for s in cl})!=1:
            raise AssertionError("quotient not causally closed")
    return class_of


def policy_feedback_step(state, update_carrier: Callable, observe: Callable, policy: Callable):
    """Fold observer memory back into the carrier: (x,m) -> (T_policy(m)x, m||observation)."""
    x,m=state
    action=policy(m)
    return (update_carrier(x,action), tuple(m)+(observe(x),))


def p_primary_seam(n: int, mutant: bool=False, radix_weight: bool=False) -> Fraction:
    """Exact source-selected first-pole p-primary mark at prime-square seams.

    At j_p, canonical p-primary fractional part is 4/p² for original
    r, and 5/p² for Q+(1-t)^2. It is 0 at other clocks by DECLARED
    first-pole projection, not by taking p-primary of an arbitrary r(n).
    """
    m = 8*n-7
    if n<0: raise ValueError("nonnegative clock")
    p=isqrt(m) if m >= 49 else 0
    result=Fraction(5 if mutant else 4,p*p) if p>=7 and p*p==m and prime(p) else Fraction()
    return result/16**n if radix_weight else result


def general_seam_hankel(p: int, q: int, *, mutant: bool=False,
                        radix_weight: bool=False) -> tuple[tuple[Fraction,...],...]:
    L=consecutive_prime_gap(p,q)
    t=seam_clock(p)+1
    return tuple(tuple(p_primary_seam(t+i+j,mutant,radix_weight) for j in range(L))
                 for i in range(L))


def general_seam_hankel_det(p: int, q: int, *, mutant: bool=False,
                            radix_weight: bool=False) -> Fraction:
    L=consecutive_prime_gap(p,q)
    mark=Fraction(5 if mutant else 4,q*q)
    if radix_weight: mark/=16**seam_clock(q)
    return (-1 if (L*(L-1)//2)%2 else 1)*mark**L



def origami_step(memory: tuple, future: tuple) -> tuple[tuple,tuple]:
    """Chronological head-tail seam; lossless when source atom is logged.

    This is an exact finite-prefix fixture of the infinite stream coalgebra,
    not an assertion that an embedded observer physically holds infinity.
    """
    if not isinstance(memory,tuple) or not isinstance(future,tuple) or not future:
        raise ValueError("tuple memory and nonempty future required")
    return memory+(future[0],), future[1:]


def origami_unstep(memory: tuple, future: tuple) -> tuple[tuple,tuple]:
    """Algebraic inverse on the image of origami_step; no reverse physical time."""
    if not isinstance(memory,tuple) or not isinstance(future,tuple) or not memory:
        raise ValueError("tuple memory and nonempty logged history required")
    return memory[:-1], (memory[-1],)+future
