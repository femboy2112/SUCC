"""Original BBP positive-kick / analytic-completion carry seam.

Research-only exact rational implementation. The authentic forcing is immutable.
The completed source value x=pi/16 uses the classical BBP identity.
No statement about R0, normality, or positive-integer Collatz follows from this module.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import comb


def forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('BBP clock must be a positive integer')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def tail_upper(n: int) -> Fraction:
    if type(n) is not int or n < 0:
        raise ValueError('tail clock must be nonnegative')
    return forcing(n+1)/15


def tail_bounds(n: int, depth: int) -> tuple[Fraction,Fraction]:
    if type(depth) is not int or depth < 0:
        raise ValueError('depth must be nonnegative')
    total=Fraction()
    for k in range(1,depth+1):
        total+=forcing(n+k)/16**k
    return total, total+forcing(n+depth+1)/(15*16**depth)


def prefix_unwrapped(n: int) -> Fraction:
    v=Fraction()
    for j in range(1,n+1):
        v=16*v+forcing(j)
    return v


@dataclass(frozen=True)
class Step:
    clock:int
    raw_digit:int
    kick_carry:int|None
    total_carry:int
    phase:Fraction


def step(phi:Fraction, n:int) -> Step:
    if n<1: raise ValueError('n must be positive')
    v=16*phi+forcing(n)
    base=(16*phi).__floor__()
    carry=v.__floor__()
    e=carry-base if n>=2 else None
    if n>=2 and e not in (0,1):
        raise AssertionError('unexpected forcing charge')
    return Step(n,base,e,carry,v-carry)


def certified_completion_carry(phi: Fraction,n:int, max_depth:int=128)->int:
    # delta= floor(phi+T_n). If interval straddles one, deepen it.
    for depth in [0,1,2,4,8,16,32,64,128]:
        if depth>max_depth:break
        lo,hi=tail_bounds(n,depth)
        if phi+hi<1: return 0
        if phi+lo>1: return 1
    raise ValueError('completion threshold unresolved under precision budget')


def cooldown(B:int)->int:
    """Conservative exact arithmetic event refractory length for every seed."""
    if type(B) is not int or B<2:raise ValueError('B>=2 required')
    rb=forcing(B)
    L=0
    while rb*Fraction(16**(L+2)-1,15)<1:
        L+=1
    # last proven j=L-1 corresponds 16^(L+1), so loop return L
    return L


def moment_difference(n:int,k:int)->Fraction:
    """Return (-1)^k Delta^k r(n), which is strictly positive."""
    if n<1 or k<0:raise ValueError('n>=1,k>=0 required')
    return sum((Fraction((-1)**j*comb(k,j))*forcing(n+j)
               for j in range(k+1)),Fraction())


def trace(nmax:int,seed:Fraction=Fraction(0),check_delta=True)->dict:
    if type(nmax) is not int or nmax<1:raise ValueError('nmax>=1 required')
    phi=seed%1
    e_times=[];delta_times=[];unresolved=[];hex_digits=[];recovered=[]
    previous_delta=0 if seed==0 else None
    for n in range(1,nmax+1):
        st=step(phi,n)
        phi=st.phase
        if st.kick_carry==1:e_times.append(n)
        if check_delta:
            try: delta=certified_completion_carry(phi,n,max_depth=8)
            except ValueError:unresolved.append(n);delta=None
            if delta==1:delta_times.append(n)
            if delta is not None and previous_delta is not None:
                digit=st.total_carry+delta-16*previous_delta
                if not 0<=digit<=15:raise AssertionError((n,digit))
                hex_digits.append(format(digit,'X'))
                recovered.append(digit)
            previous_delta=delta
        phi=st.phase
    word=''.join(hex_digits)
    shells={}
    if len(word)==nmax:
        for B in (128,512,2048,8000):
            if 2*B<=nmax:
                hits=sum(4<=int(char,16)<=11 for char in word[B:2*B])
                shells[str(B)]={'hits':hits,'total':B,'r0_lower_bound':f'{hits}/{B}'}
    return dict(quarter_shells=shells,nmax=nmax, e_times=e_times, delta_times=delta_times,
                unresolved=unresolved, recovered_digits=len(word),
                prefix=word[:32], suffix=word[-32:],
                digit_sha256=sha256(word.encode('ascii')).hexdigest(),
                zero_seed=(seed==0))


def source_phase_reset_bound(n:int)->Fraction:
    """At an extra source-kick carry, theta_n < this rational number."""
    if n<2:raise ValueError('n>=2')
    return forcing(n)+tail_upper(n)


def cofactor_shadow_upper(n:int)->Fraction:
    """At a completion carry, theta_n < T_n < this bound."""
    return tail_upper(n)


if __name__=='__main__':
    import json
    print(json.dumps(trace(4096),indent=2))
