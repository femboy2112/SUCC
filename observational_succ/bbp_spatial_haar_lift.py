"""Source-specific BBP spatial Haar lift; NOT a proof of real pi digit normality.

Inherited from SUCC #527: the exact 2-adic source solution V with V(0)=0,
V(n)=U_n for nonnegative n. This module computes its explicit nibble lifts.
SUCC #558/#562 supply the all-prime real phase and literal carry interface.
The only source imported here is the frozen four-pole duck_bbp.forcing.
"""
from __future__ import annotations
from fractions import Fraction
from observational_succ.duck_bbp import forcing


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def first_spatial_digit(n: int) -> int:
    """V(n) mod16 = (2*(n mod2)-n) mod16. NOT pi's real nth digit."""
    _nat(n)
    return (2 * (n & 1) - n) % 16


def derivative_slope(n: int) -> int:
    """r'(n) mod16 = 10+(2n-1)^(-2), i.e. 11 or 3, always odd."""
    _nat(n)
    return (10 + pow(2*n - 1, -2, 16)) % 16


def modular_source(n: int, modulus: int) -> int:
    """r(n) in Z/(16^k) from canonical odd-denominator combined source."""
    _nat(n, 1)
    if type(modulus) is not int or modulus < 16:
        raise ValueError("modulus must be a positive power of 16")
    q=modulus
    while q % 16 == 0:
        q//=16
    if q != 1:
        raise ValueError("modulus must be a power of 16")
    f=forcing(n)
    if f.denominator % 2 == 0:
        raise ArithmeticError("original source must be 2-adically integral")
    return f.numerator * pow(f.denominator, -1, modulus) % modulus


def source_spatial_states(horizon: int, modulus: int) -> tuple[int, ...]:
    """Original U0=0 finite exact integer source residues U_0,...,U_horizon."""
    _nat(horizon)
    seq=[0]
    for n in range(1,horizon+1):
        seq.append((16*seq[-1]+modular_source(n,modulus))%modulus)
    return tuple(seq)


def affine_lift(a: int, t: int, k: int, state_a: int) -> int:
    """V(a+16^k*t) mod16^(k+1), k>=1, via SOURCE derivative.

    This is a spatial precision lift. A temporal successor is different.
    """
    _nat(a);_nat(t);_nat(k,1);_nat(state_a)
    if t>=16:
        raise ValueError("one refinement nibble required")
    return (state_a + 16**k*t*derivative_slope(a)) % 16**(k+1)


def two_spatial_digits_from_first(first: int, t: int) -> tuple[int,int]:
    """Explicit Haar-preserving 1->2 SPATIAL map with extra clock nibble t.

    a=f(first) since f is involutive. Output (first, b_a+t*s_a mod16)
    traverses all 256 pairs once as first,t traverse Z16^2.
    """
    _nat(first);_nat(t)
    if first>=16 or t>=16:
        raise ValueError("digits must be 0..15")
    a=first_spatial_digit(first)
    v=source_spatial_states(a,256)[a]
    return first, (v//16+t*derivative_slope(a))%16


def next_temporal_spatial_digit(d: int) -> int:
    """The low spatial nibble at NEXT TIME, NOT the second precision digit."""
    _nat(d)
    if d>=16:raise ValueError("digit must be 0..15")
    return (d+1 if d%2==0 else d-3)%16


def complete_source_states(horizon: int) -> tuple[Fraction,...]:
    """Original unwrapped zero-seeded rational BBP states, exact."""
    _nat(horizon)
    vals=[Fraction(0)]
    for j in range(1,horizon+1):
        vals.append(16*vals[-1]+forcing(j))
    return tuple(vals)


def tail_interval(n: int, depth: int) -> tuple[Fraction,Fraction]:
    """Rigorous future T_n enclosure, positive decreasing original source."""
    _nat(n,1);_nat(depth)
    partial=sum((forcing(n+j)/16**j for j in range(1,depth+1)), Fraction())
    return partial, partial+forcing(n+depth+1)/(15*16**depth)


def completed_real_word(n: int, width: int = 2, depth: int = 8,
                        states: tuple[Fraction,...] | None = None) -> int:
    """Exactly certify REAL pi's next width hex digits after 16^(n-1)pi.

    Unlike two_spatial_digits_from_first, this pays the analytic Green tail.
    """
    _nat(n,1);_nat(width,1);_nat(depth)
    if width>8:raise ValueError("certification scope width<=8")
    u=states[n] if states is not None else complete_source_states(n)[n]
    lo,hi=tail_interval(n,depth)
    cell=16**width
    left=int(((u%1)+lo)*cell)
    right=int(((u%1)+hi)*cell)
    if left!=right:
        raise ArithmeticError("ambiguous real digit boundary; increase depth")
    return left%cell


def word_counts(digits: str, cyclic: bool = False) -> tuple[tuple[int,...],...]:
    """16x16 chronological transition counts (no wrap unless explicit)."""
    if type(digits) is not str or len(digits)<2:
        raise ValueError("nonempty hexadecimal path required")
    ds=[int(x,16) for x in digits]
    out=[[0]*16 for _ in range(16)]
    for j in range(len(ds) if cyclic else len(ds)-1):
        out[ds[j]][ds[(j+1)%len(ds)]]+=1
    return tuple(tuple(x) for x in out)


def two_digit_energies(counts: tuple[tuple[int,...],...]) -> tuple[Fraction,...]:
    """E2=Erow+Ecol+225 mixed modes, exact rational finite Parseval."""
    if len(counts)!=16 or any(len(r)!=16 for r in counts):
        raise ValueError("16x16 count table required")
    N=sum(sum(row) for row in counts)
    if N<=0:raise ValueError("empty")
    row=[sum(r) for r in counts]
    col=[sum(counts[a][b] for a in range(16)) for b in range(16)]
    er=Fraction(16*sum(v*v for v in row),N*N)-1
    ec=Fraction(16*sum(v*v for v in col),N*N)-1
    e2=Fraction(256*sum(v*v for r in counts for v in r),N*N)-1
    mixed=e2-er-ec
    if mixed<0:raise AssertionError("mixed projected norm must be nonnegative")
    return er,ec,e2,mixed


def bulk_pi_hex_digits(length: int, guard: int = 24) -> str:
    """Finite ORIGINAL four-pole BBP outward INTEGER enclosure, no pi oracle.

    pi=sum_(j>=1)16^(1-j)r(j). For K=N+guard and S=16^K,
    L=sum_(j<=K) floor(S 16^(1-j)r(j)) has L <= S*pi < L+K+1.
    Hence matching N-hex cells certify the finite prefix. Not normality.
    """
    _nat(length,2);_nat(guard,8)
    K=length+guard
    power=1<<(4*K)
    L=0
    for j in range(1,K+1):
        frac=forcing(j)
        L+=(power*frac.numerator)//frac.denominator
        power//=16
    assert power==1
    left=L>>(4*guard)
    right=(L+K+1)>>(4*guard)
    if left!=right:raise ArithmeticError("increase guard; ambiguous interval")
    return format(left%(16**length),'X').zfill(length)
