"""Exact finite carrier probes for the BBP edge law and seed-response tomography.

All computations are finite integers/Fractions; no normality claim is made.
The infinite proofs and the counterfactual-seed firewall are in PROOFS.md.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import isqrt

BASE = 16
SINGER_MODULUS = 73


def forcing(n: int) -> Fraction:
    """The ORIGINAL four signed BBP poles; n>=1."""
    if n < 1:
        raise ValueError("n>=1 required")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def original_states(N: int, seed: Fraction = Fraction(0)) -> tuple[Fraction, ...]:
    """Return U_0..U_N, with exact rational seed. Default is authentic U_0=0."""
    if N < 0:
        raise ValueError("N>=0 required")
    out = [Fraction(seed)]
    for n in range(1, N+1):
        out.append(BASE*out[-1] + forcing(n))
    return tuple(out)


def edge_data(N: int) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    """(U_(n+1)-U_n, 15 U_n, r(n+1)), 1<=n<=N, authentic seed."""
    u = original_states(N+1)
    return tuple((u[n+1]-u[n], 15*u[n], forcing(n+1)) for n in range(1, N+1))


def edge_error_certificate(N: int) -> Fraction:
    """Exact total forcing shift in edge vs 15*vertex character, n=1..N."""
    if N < 0:
        raise ValueError("N>=0")
    return sum((forcing(n+1) for n in range(1, N+1)), Fraction(0))


def circle_distance(t: Fraction) -> Fraction:
    """Exact distance from rational t to Z (in [0,1/2])."""
    x=Fraction(t)%1
    return min(x,1-x)


def edge_phase_mismatch(N: int, h: int=1) -> Fraction:
    """Exact rational sum dist(h*r(n+1), Z), a signed-comparison bound."""
    if N < 0 or h == 0:
        raise ValueError("N>=0 and h!=0 required")
    return sum((circle_distance(h*forcing(n+1)) for n in range(1,N+1)), Fraction(0))


def bbp_constant_prefix(K: int) -> Fraction:
    """c_K=sum_(j=1)^K 16^-j r(j), with true infinite c=pi/16."""
    if K < 0:
        raise ValueError("K>=0")
    return sum((forcing(k)/16**k for k in range(1, K+1)), Fraction(0))


def bbp_tail_upper(K: int) -> Fraction:
    """Rigorous 0<c-c_K<=16^-K / ((8K+1)(8K+2)); K>=0."""
    if K < 0:
        raise ValueError("K>=0")
    return Fraction(1, 16**K*(8*K+1)*(8*K+2))


def truncation_seed_error(K: int, n: int) -> Fraction:
    """Bound |U_n(-c_K)+T_n|=16^n(c-c_K), for 0<=n<=K."""
    if not 0 <= n <= K:
        raise ValueError("0<=n<=K required")
    return 16**n * bbp_tail_upper(K)


def pair_difference_labels(N: int, h: int=1, base: int=BASE) -> dict[int, tuple[int,int]]:
    """Ordered off-diagonal lacunary differences; injective over integers."""
    if N < 2 or h == 0 or base < 3:
        raise ValueError("N>=2, h!=0, base>=3 required")
    labels: dict[int, tuple[int,int]] = {}
    for n in range(1, N+1):
        for m in range(1, N+1):
            if n == m:
                continue
            label = h*(base**n-base**m)
            if label in labels:
                raise ArithmeticError("unexpected integer Fourier collision")
            labels[label] = (n,m)
    return labels


def aliases(N: int, modulus: int, h: int=1, base: int=BASE) -> dict[int, list[tuple[int,int]]]:
    """Off-diagonal frequency classes including diagonal represented by (0,0)."""
    if modulus < 2:
        raise ValueError("modulus>=2")
    result: dict[int, list[tuple[int,int]]] = {0: [(0,0)]}
    for label, pair in pair_difference_labels(N,h,base).items():
        result.setdefault(label % modulus, []).append(pair)
    return result


def is_alias_free(N: int, modulus: int, h: int=1, base: int=BASE) -> bool:
    a = aliases(N,modulus,h,base)
    return len(a) == 1+N*(N-1) and all(len(v)==1 for v in a.values())


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for k in range(2,isqrt(n)+1):
        if n%k == 0:
            return False
    return True


def first_alias_free_prime(N: int, h: int=1, base: int=BASE, cap: int=100_000) -> int:
    """Finite search. The proof of eventual existence uses infinitude of primes."""
    if cap < 2:
        raise ValueError("cap too small")
    for p in range(max(2,N*(N-1)+1),cap+1):
        if is_prime(p) and is_alias_free(N,p,h,base):
            return p
    raise LookupError("no alias-free prime <= cap; NOT proof of nonexistence")


def difference_set_73() -> tuple[int,...]:
    """A cyclic (73,9,1) difference set: nine radix16 time modes."""
    return tuple(sorted({pow(BASE,n,SINGER_MODULUS) for n in range(1,10)}))


def diff_multiplicity(D: tuple[int,...], modulus: int) -> Counter:
    return Counter((a-b)%modulus for a in D for b in D if a!=b)


def singer_lines() -> tuple[frozenset[int],...]:
    D=difference_set_73()
    return tuple(frozenset((x+d)%SINGER_MODULUS for d in D) for x in range(SINGER_MODULUS))


def exact_source_tomogram(N: int, modulus: int, h: int=1, seed: Fraction=Fraction(0)) -> dict[int, tuple[tuple[int,int],Fraction] | None]:
    """Formal DFT of seed-response intensity. A label carries e(2πi*phase).

    Phase is a Fraction mod 1, NOT a floating-point complex approximation.
    The coefficient at residue 0 equals scalar N and is represented by None.
    Only use when *every* spectral label is distinct mod modulus.
    """
    if not is_alias_free(N,modulus,h):
        raise ValueError("aliased Fourier carrier: intensity is not injective")
    u=original_states(N,seed)
    result: dict[int, tuple[tuple[int,int],Fraction] | None] = {0:None}
    for frequency,(n,m) in pair_difference_labels(N,h).items():
        result[frequency%modulus] = ((n,m), (h*(u[n]-u[m]))%1)
    return result


def fourth_moment(N: int) -> int:
    """Exact seed integral of |sum z_n e(h16^n s)|^4, |z_n|=1."""
    if N < 1:
        raise ValueError("N>=1 required")
    return 2*N*N-N


def cylinder_moment_tail(N: int,k: int) -> tuple[int,int]:
    """For radix-16 cylinder depth k, late indices n>=max(1,k)."""
    if N < 1 or not 0 <= k <= N:
        raise ValueError("N>=1, 0<=k<=N")
    start=max(1,k)
    M=N-start+1
    return M, 2*M*M-M


def selection_lipschitz_budget(N: int,h: int=1) -> int:
    """|F_N(s)-F_N(t)| <= 2*pi*B*|s-t|, B exact integer."""
    if N < 0 or h == 0:
        raise ValueError("N>=0, h!=0")
    return abs(h)*sum(16**n for n in range(1,N+1))


if __name__ == '__main__':
    for N in range(2,15):
        p=first_alias_free_prime(N)
        print(f'N={N:2d}: {1+N*(N-1):3d} pair channels, alias-free prime p={p}')
    D=difference_set_73()
    assert D==(1,2,4,8,16,32,37,55,64)
    assert set(diff_multiplicity(D,73).values())=={1}
    print('73-point projective carrier VERIFIED, all 72 nonzero differences appear once')
