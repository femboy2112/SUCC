"""Original-BBP lag-flow/alias-valve finite exact rational instrument.

Research only. Not a pi normality proof. All sampled arithmetic is Fraction,
including chronology and phase comparisons. No pi digits are ever inputs.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import lcm


def force(n: int) -> F:
    if not isinstance(n, int) or n < 1:
        raise ValueError("BBP source time n>=1 required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def force_closed(n: int) -> F:
    if not isinstance(n, int) or n < 1:
        raise ValueError("BBP source time n>=1 required")
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def orbit(N: int, seed: F = F(0)) -> tuple[F,...]:
    if not isinstance(N,int) or N<0:
        raise ValueError("nonnegative N")
    x=F(seed)%1
    states=[x]
    for n in range(1,N+1):
        x=(16*x+force(n))%1
        states.append(x)
    return tuple(states)


def modular_orbit(N: int) -> tuple[F,...]:
    if not isinstance(N,int) or N<0: raise ValueError("nonnegative N")
    D=1
    for n in range(1,N+1): D=lcm(D,force_closed(n).denominator)
    if D%2!=1: raise AssertionError("original source denominator not odd")
    x=0; states=[F(0)]
    for n in range(1,N+1):
        y=force_closed(n)
        x=(16*x+y.numerator*(D//y.denominator))%D
        states.append(F(x,D))
    return tuple(states)


def circ_dist(x: F) -> F:
    y=F(x)%1
    return min(y,1-y)


def tent(x: F, q: int) -> F:
    if not isinstance(q,int) or q<2: raise ValueError("q integer >=2")
    return max(F(0),1-q*circ_dist(x))


def lateral(x: F, q: int) -> F:
    return sum((tent(x-F(j,16),16*q) for j in range(1,16)), F(0))


def leakage(x: F, q: int) -> F:
    return tent(x,q)-tent(x,16*q)


def shear(n: int,d:int)->F:
    if n<1 or d<1: raise ValueError("n,d positive")
    return force(n+1)-force(n+d+1)


def shear_cap(n:int,d:int)->F:
    if n<1 or d<1: raise ValueError("n,d positive")
    return F(240*d,(8*n+1)*(8*n+2)*(8*n+3))


def signed_shear_flux(x:F,n:int,d:int,q:int)->F:
    return tent(16*x-shear(n,d),q)-tent(16*x,q)


def flux(A:int,q:int,seed:F=F(0))->dict:
    if not isinstance(A,int) or A<2: raise ValueError("A>=2")
    if not isinstance(q,int) or q<2: raise ValueError("q>=2")
    xs=orbit(2*A-1,seed)
    leak=side=drift=src_shear=endpoint=F(0)
    for d in range(1,A):
        end=2*A-d-1
        endpoint+=tent(xs[A+d]-xs[A],q)-tent(xs[end+d]-xs[end],q)
        for n in range(A,end):
            delta=xs[n+d]-xs[n]
            delta_next=xs[n+d+1]-xs[n+1]
            s=shear(n,d)
            if s<=0 or s>=shear_cap(n,d): raise AssertionError("source shear bound")
            if circ_dist(delta_next-(16*delta-s))!=0: raise AssertionError("lag recurrence")
            l=leakage(delta,q)
            i=lateral(delta,q)
            if tent(16*delta,q)!=tent(delta,16*q)+i: raise AssertionError("16-alias")
            leak+=l; side+=i; drift+=signed_shear_flux(delta,n,d,q)
            src_shear+=s
    if leak-side!=endpoint+drift: raise AssertionError("valve balance")
    if abs(drift)>q*src_shear: raise AssertionError("signed flux magnitude")
    cap=F(15*A*(A-1),2*(8*A+1)*(8*A+2))
    if src_shear>=cap: raise AssertionError("source total shear cap")
    if abs(leak-side)>A-1+q*cap: raise AssertionError("epoch normalized cap")
    return dict(A=A,q=q,leak=leak,injection=side,signed_source_flux=drift,
                boundary=endpoint,positive_source_shear=src_shear,
                source_shear_cap=cap,normalized_imbalance=F(q,A*A)*(leak-side),
                normalized_cap=F(q,A*A)*(A-1+q*cap))


def source_conductor(N:int)->int:
    if N<0: raise ValueError("N>=0")
    D=1
    for j in range(1,N+1): D=lcm(D,force(j).denominator)
    return D


def escape_depth(D:int,q:int)->int:
    if D<1 or q<2: raise ValueError("D>=1,q>=2")
    k=0; v=q
    while v<D:
        k+=1; v*=16
    return k


def pair_energy(phases:tuple[F,...],q:int)->F:
    if not phases: raise ValueError("need phases")
    N=len(phases)
    return F(q,N*N)*sum((tent(x-y,q) for x in phases for y in phases),F(0))


def escape_receipt(phases:tuple[F,...],q:int,J:int)->dict:
    if not phases or J<0: raise ValueError("nonempty phases, J>=0")
    z=[x-y for x in phases for y in phases]
    N=len(phases)
    flux=sum((sum((leakage(delta,q*16**j) for j in range(J)),F(0)) for delta in z),F(0))
    rem=sum((tent(delta,q*16**J) for delta in z),F(0))
    total=F(q,N*N)*(flux+rem)
    if total!=pair_energy(phases,q): raise AssertionError("telescoping")
    D=lcm(*(F(x).denominator for x in phases))
    assert D%2==1
    L=escape_depth(D,q)
    survivors=sum((circ_dist(delta)==0 for delta in z))
    if q*16**L < D: raise AssertionError("depth too small")
    assert all(tent(delta,q*16**L)==(1 if circ_dist(delta)==0 else 0) for delta in z)
    return dict(q=q,J=J,total=total,release_at_J=F(q,N*N)*flux,
                unresolved_at_J=F(q,N*N)*rem,exact_collision_pairs=survivors,
                conductor=D,terminal_depth=L,terminal_residue=F(q*survivors,N*N))


def bbp_prefix(M:int)->F:
    if M<1: raise ValueError("M>=1")
    return sum((force(j)/16**j for j in range(1,M+1)),F(0))


def nearest_integer(y:F)->int:
    y=F(y)
    return (2*y.numerator+y.denominator)//(2*y.denominator)


def coherent_odd_seed(A:int)->tuple[F,int,F]:
    """Epoch-dependent odd-denominator counterseed; NOT actual U_0=0."""
    if A<2: raise ValueError("A>=2")
    M=2*A
    alpha=bbp_prefix(M)
    Q=512*A*A*16**M+1  # odd; 16^M/(2Q) < 1/(1024 A^2)
    s=F(nearest_integer(-Q*alpha),Q)
    assert s.denominator%2==1
    assert abs(s+alpha)<=F(1,2*Q)
    return s,M,alpha


def coherent_odd_receipt(A:int,q:int)->dict:
    seed,M,alpha=coherent_odd_seed(A)
    xs=orbit(M,seed)
    selected=xs[A:2*A]
    assert all(x.denominator%2==1 for x in xs)
    real_unwrapped=[]
    un=seed
    for n in range(M+1):
        if n: un=16*un+force(n)
        if A<=n<2*A:
            R=sum((force(j)/16**(j-n) for j in range(n+1,M+1)),F(0))
            assert 0<R<F(1,64*n*n)
            assert un==16**n*(seed+alpha)-R
            real_unwrapped.append(un)
    width=max(real_unwrapped)-min(real_unwrapped)
    assert width<F(9,512*A*A)
    E=pair_energy(selected,q)
    assert E>=q*(1-F(9*q,512*A*A))
    return dict(A=A,q=q,seed_denominator_bits=seed.denominator.bit_length(),
                width=width,J=E,lower_bound=F(q)*(1-F(9*q,512*A*A)),
                seed_is_original=False,odd_denominators=True)
