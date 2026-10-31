"""Exact original BBP two-adic × three-adic time-clock and tripling probes.

All computations are rational/integer; analytic/global theorems are in PROOF.md.
Normality, RH and the Furstenberg zero-entropy conjecture remain OPEN.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction

def bbp_r(n: int) -> Fraction:
    if type(n) is not int or n < 1: raise ValueError("positive integer n required")
    return Fraction(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def original_states(N: int) -> tuple[Fraction,...]:
    if type(N) is not int or N < 0: raise ValueError("N must be >= 0")
    u=Fraction(0); seq=[u]
    for n in range(1,N+1):
        u=16*u+bbp_r(n); seq.append(u)
    return tuple(seq)

def two_mod_states(N: int, a: int) -> tuple[int,...]:
    """Original zero-seeded U_0..U_N mod 2^a; all reduced denominators odd."""
    if type(N) is not int or N<0 or type(a) is not int or not 1<=a<=20:
        raise ValueError("invalid source horizon or dyadic depth")
    q=2**a; u=0; seq=[0]
    for n in range(1,N+1):
        A=120*n*n-89*n+16
        D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        assert D&1
        u=(16*u+A*pow(D,-1,q))%q; seq.append(u)
    return tuple(seq)

def rational_mod_two(x: Fraction,a:int)->int:
    x=Fraction(x);q=2**a
    if x.denominator%2==0:raise ValueError("not a two-adic integer")
    return x.numerator*pow(x.denominator,-1,q)%q

def three_clock(t:int,b:int)->int:
    if type(t) is not int or t<0 or type(b) is not int or not 1<=b<=20:
        raise ValueError("invalid nonnegative time or 3-adic level")
    return pow(16,t,3**b)

def clock_period(b:int)->int:
    if type(b) is not int or not 1<=b<=20:raise ValueError("b in 1..20")
    return 3**(b-1)

def clock_modulus(a:int,b:int)->int:
    if type(a) is not int or a<1 or type(b) is not int or b<1:
        raise ValueError("positive levels required")
    return 2**a * 3**(b-1)

def joint_clock_counts(a:int,b:int,start:int=0,cycles:int=1):
    """Exact CRT joint product histogram; every cell visited once per period."""
    if type(start) is not int or start<0 or type(cycles) is not int or cycles<1:
        raise ValueError("nonnegative start and positive cycles")
    q=2**a; L=clock_period(b); M=q*L
    states=two_mod_states(start+cycles*M,a)
    counts=Counter((states[t],three_clock(t,b)) for t in range(start,start+cycles*M))
    units={three_clock(t,b) for t in range(L)}
    return dict(q=q,level=b,period=M,counts=counts,distinct=len(counts),
                expected_cells=q*L,all_equal=(len(counts)==q*L
                and set(counts.values())=={cycles}),expected_units=units)

def local_character_histogram(a:int,b:int,r:int,s:int):
    """Exact frequency-index distribution, not a floating complex evaluation."""
    q=2**a;L=clock_period(b);M=q*L
    states=two_mod_states(M,a); hist=Counter()
    for t in range(M):
        hist[(Fraction(r*states[t],q)+Fraction(s*t,L))%1]+=1
    d=len(hist)
    roots={Fraction(j,d) for j in range(d)}
    return dict(hist=hist,period=M,uniform_roots=(set(hist)==roots and
                set(hist.values())=={M//d}),zero_mean=(d==1 and
                next(iter(hist))==0) if r%q==0 and s%L==0 else
                (d>1 and set(hist)==roots and set(hist.values())=={M//d}))

def hats(x:Fraction,q:int)->dict[int,Fraction]:
    if type(q) is not int or q<2:raise ValueError("q>=2")
    y=(Fraction(x)%1)*q
    j=y.numerator//y.denominator;t=y-j
    return {i:v for i,v in ((j,1-t),((j+1)%q,t)) if v}

def empirical_hats(xs,q):
    xs=tuple(xs)
    if not xs:raise ValueError("nonempty orbit required")
    a=[Fraction(0)]*q
    for x in xs:
        for j,v in hats(x,q).items():a[j]+=v
    return tuple(v/len(xs) for v in a)

def tripling_refine_hat(x:Fraction,q:int)->bool:
    """phi_(q,j)(3x) equals three sibling hats at level 3q."""
    coarse=hats(3*x,q);fine=hats(x,3*q)
    return all(coarse.get(j,0)==sum(fine.get(j+t*q,0) for t in range(3))
               for j in range(q))

def tripling_carry(x:Fraction,q:int):
    """Exact real fractional base-q digit transport: d_3=(3d+c) mod q."""
    y=Fraction(x)%1;t=q*y
    d=t.numerator//t.denominator
    z=3*(t-d);c=z.numerator//z.denominator
    out=(q*((3*y)%1));d3=out.numerator//out.denominator
    if d3!=(3*d+c)%q:raise AssertionError("failed carry")
    return (d,c,d3)

def tripling_hat_defect(N:int,q:int):
    if type(N) is not int or N<1:raise ValueError("N positive")
    u=original_states(N)[1:]
    a=empirical_hats(u,q);b=empirical_hats((3*x for x in u),q)
    return tuple(y-x for x,y in zip(a,b))

def green_tail_bracket(n:int,terms:int=40):
    if type(n) is not int or n<1 or type(terms) is not int or terms<1:
        raise ValueError("positive n and terms required")
    low=sum((bbp_r(n+j)/16**j for j in range(1,terms+1)),Fraction(0))
    return low,low+bbp_r(n+terms+1)/(15*16**terms)

def certified_selected_tripling_carry(n:int,q:int,terms:int=48):
    """Certify π's n-th selected digit and 3x carry, rejecting seam ambiguity."""
    u=original_states(n)[-1];lo,hi=green_tail_bracket(n,terms)
    low=q*(u+lo);high=q*(u+hi)
    d=low.numerator//low.denominator; e=high.numerator//high.denominator
    a=3*low;c=3*high
    f=a.numerator//a.denominator;g=c.numerator//c.denominator
    if d!=e or f!=g:raise ArithmeticError("certification crosses a seam")
    return dict(digit=d%q,carry=f-3*d,tripled_digit=f%q,
                strict_width=high-low,selected_zero_seed=True)

def tripling_transport_certificate(N:int,q:int,terms:int=32):
    """Original selected hat Δ_3(U) transfers to Δ_3(y) at L1 < q/(4N)."""
    u=original_states(N)[1:]
    tails=tuple(green_tail_bracket(n,terms) for n in range(1,N+1))
    approx=tuple(x+lo for x,(lo,hi) in zip(u,tails))
    d_u=tripling_hat_defect(N,q)
    p=empirical_hats(approx,q);z=empirical_hats((3*x for x in approx),q)
    d_approx=tuple(a-b for a,b in zip(z,p))
    obs=sum((abs(x-y) for x,y in zip(d_u,d_approx)),Fraction(0))
    return dict(observed=obs,
         certified_bound=Fraction(8*q,N)*sum((hi for lo,hi in tails),Fraction(0)),
         missing_tail_upper=Fraction(8*q,N)*sum((hi-lo for lo,hi in tails),Fraction(0)),
         universal_upper=Fraction(q,4*N))

def v_p_rational(x:Fraction,p:int)->int:
    x=Fraction(x)
    if x==0:raise ValueError("valuation at zero undefined")
    def v(k):
        k=abs(k);a=0
        while k%p==0:k//=p;a+=1
        return a
    return v(x.numerator)-v(x.denominator)

def rational_circle_phase(mode:int,N:int,x:Fraction)->Fraction:
    """Pontryagin character of R/NZ is indexed by EVERY integer mode."""
    if type(N) is not int or N<1 or type(mode) is not int:
        raise ValueError("invalid mode/N")
    return Fraction(mode,N)*Fraction(x)%1

def periodic_character_control(alpha:Fraction,period:int)->bool:
    """Finite check for period dividing a given positive integer."""
    if type(period) is not int or period<1:raise ValueError("period positive")
    a=Fraction(alpha)%1
    return ((16**period-1)*a).denominator==1


def independent_backward_f2_residue(t:int,a:int)->int:
    """Independent finite 2-adic Green F₂(t), not the forward BBP recurrence.

    F₂(t)=sum_(j>=0)16^j r(t-j), with r on arbitrary integer indices.
    All terms 4j>=a vanish mod 2^a. F₂(0)=0 is a separate analytic theorem.
    """
    if type(t) is not int or type(a) is not int or not 1<=a<=20:
        raise ValueError("integer time and dyadic precision 1..20 required")
    q=2**a;total=0
    for j in range((a+3)//4):
        n=t-j;A=120*n*n-89*n+16
        D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        total=(total+pow(16,j,q)*A*pow(D,-1,q))%q
    return total


def exceptional_integer_orbit_phase(n:int,alpha:Fraction)->Fraction:
    """The integer-orbit branch of a Borel-equivariant null-orbit decoder.

    Outside diagonal integers in Z₂×Z₃ set f(t)=0. This Borel map
    is Haar-almost-everywhere zero despite f(0)=alpha; only this exact
    countable branch is executable from rational alpha in finite code.
    """
    if type(n) is not int:raise ValueError("integer time required")
    a=Fraction(alpha)%1
    return (a*16**n)%1 if n>=0 else (a/Fraction(16**(-n)))%1
