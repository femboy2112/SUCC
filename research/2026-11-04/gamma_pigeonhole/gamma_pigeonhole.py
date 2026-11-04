"""Original BBP Gamma-prime pigeonhole: exact p-local/real source window census.

All finite arithmetic uses Fraction, no pi digits, no numerical claims about
normality.  Euler finite-part windows use alternating rational log enclosures.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import ceil, floor, gcd, isqrt, lcm


def prime(p: int) -> bool:
    return type(p) is int and p > 1 and all(p % d for d in range(2, isqrt(p) + 1))


def forcing(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("n>=1 required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def gamma_delta_bounds(p: int, K: int = 16) -> tuple[F, F]:
    """Exact enclosures of delta(p)=1/p-log(1+1/p), S_K/S_(K+1)."""
    if type(p) is not int or p < 2 or type(K) is not int or K < 2:
        raise ValueError("p>=2, K>=2")
    s=sum((F((-1)**k, k*p**k) for k in range(2, K+1)), F(0))
    t=s+F((-1)**(K+1), (K+1)*p**(K+1))
    lo,hi=min(s,t),max(s,t)
    assert F(1, 2*p*(p+1)) < lo < hi < F(1, 2*p*p)
    return lo,hi


def source_prime(n: int) -> int:
    if type(n) is not int or n < 2:
        raise ValueError("n>=2 required")
    p=8*n-7
    if p <= 5 or not prime(p):
        raise ValueError("newborn 8n-7 must be prime>5")
    return p


def pole_split(n: int) -> dict:
    """r(n)=4/p+beta with exactly reduced denominator p*C."""
    p=source_prime(n)
    beta=-F(2,p+3)-F(1,p+4)-F(1,p+5)
    C=(p+3)*(p+4)*(p+5)//8
    r=forcing(n)
    assert beta.denominator == C
    assert r == F(4,p)+beta and r.denominator == p*C and gcd(p,C) == 1
    assert r.numerator*pow(C,-1,p)%p == 4
    assert F(2,p*p) < r < F(15,p*(p+1))
    lo,hi=gamma_delta_bounds(p)
    assert r < 30*lo
    return {"n":n,"p":p,"r":r,"beta":beta,"C_force":C,
            "gamma_lower":30*lo,"gamma_upper":30*hi,
            "lower_candidates":floor(C*30*lo),
            "upper_candidates":ceil(C*30*hi)}


def clock_state(n: int) -> tuple[int,int,int]:
    """Unwrapped original rational U_n=A_n/Q_n with SOURCE lcm clock."""
    if type(n) is not int or n<0:
        raise ValueError("n>=0 required")
    Q,A=1,0
    for j in range(1,n+1):
        r=forcing(j)
        N=lcm(Q,r.denominator)
        A=16*(N//Q)*A+(N//r.denominator)*r.numerator
        Q=N
    return A,Q,n


def birth_register(n: int) -> dict:
    p=source_prime(n)
    _,Qprev,_=clock_state(n-1)
    A,Q,_=clock_state(n)
    C=Q//p
    assert Q%p==0 and Q%(p*p)!=0 and Qprev%p!=0 and C%p!=0
    assert (A-4*C)%p==0
    old=(A-4*C)//p
    assert F(A,Q)==F(4,p)+F(old,C)
    return {"n":n,"p":p,"A":A,"Q":Q,"Q_prev":Qprev,
            "C_state":C,"p_residue":A*pow(C,-1,p)%p,
            "old_cofactor_address":old%C}


def coset_count(Q: int,M: int,residue: int,start:F,width:F) -> int:
    """Exact half-open circular arc count for numerator class A= res (mod M)."""
    if any(type(x) is not int for x in (Q,M,residue)) or Q<1 or M<1 or Q%M:
        raise ValueError("exact M|Q required")
    start,width=F(start),F(width)
    if not 0<=width<=1:
        raise ValueError("window length in [0,1]")
    C=Q//M
    t=F(residue,Q)
    return ceil(C*(start+width-t))-ceil(C*(start-t))


def count_certificates(Q:int,M:int,wlo:F,whi:F)->tuple[int,int]:
    if Q<1 or M<1 or Q%M:
        raise ValueError("M must divide Q")
    if not 0<=wlo<=whi<=1:
        raise ValueError("valid positive window enclosure required")
    C=Q//M
    return floor(C*wlo),ceil(C*whi)


def pair_exclusion_possible(L:int,M:int,q:int)->bool:
    """Necessary, never sufficient, for congruence-only near-pair exclusion."""
    if any(type(x) is not int for x in (L,M,q)) or q<=2 or L<1 or M<1 or L%M:
        raise ValueError("q>2 and M|L required")
    return 2*(L//M)<q


def gamma_corrected_pin(n:int,K:int=4)->dict:
    """Provably unique rational in newborn p-coset using four Gamma-jet terms."""
    s=pole_split(n)
    p,C=s["p"],s["C_force"]
    if p<41:
        raise ValueError("uniform uniqueness certified for p>=41 only")
    if type(K) is not int or K<4:
        raise ValueError("at least four alternating log terms required")
    dlo,dhi=gamma_delta_bounds(p,K)
    left=30*dlo-F(49,p**3)
    right=30*dhi-F(49,p**3)+F(236,p**4)
    assert 0<left<s["r"]<right<1
    width=right-left
    assert C*width<1
    Q=p*C
    assert coset_count(Q,p,4*C,left,width)==1
    k=ceil(C*(left-F(4,p)))
    candidate=(F(4,p)+F(k,C))%1
    assert left<=candidate<right and candidate==s["r"]
    return {"n":n,"p":p,"C":C,"source":s["r"],
            "window_lo":left,"window_hi":right,"window_width":width,
            "candidate":candidate,"cofactor_address":k%C,
            "scaled_width":C*width,"unique":True}


def false_neighbor(n:int)->dict:
    """Wrong cofactor, same newborn residue: coarse Gamma passes; jet rejects."""
    s=pole_split(n)
    pin=gamma_corrected_pin(n)
    p,C=s["p"],s["C_force"]
    neighbor=s["r"]+F(1,C)
    assert 0<neighbor<30*gamma_delta_bounds(p,16)[0]
    assert (p*neighbor).numerator*pow((p*neighbor).denominator,-1,p)%p==4
    assert not(pin["window_lo"]<=neighbor<pin["window_hi"])
    return {"n":n,"p":p,"neighbor":neighbor,"coarse":True,"refined":False}


def source_native_seed(A:int)->tuple[F,int]:
    if type(A) is not int or A<2:
        raise ValueError("A>=2")
    B=clock_state(A)[1]
    alpha=sum((forcing(j)/16**j for j in range(1,2*A+1)),F(0))
    y=-B*alpha
    nearest=(2*y.numerator+y.denominator)//(2*y.denominator)
    s=F(nearest,B)
    assert B%s.denominator==0 and abs(s+alpha)<=F(1,2*B)
    return s,B


def old_seed_same_newprime(A:int,n:int)->dict:
    """The coherent source-native wrong seed shares every NEW post-A p passport."""
    if type(A) is not int or not A<n<2*A:
        raise ValueError("A<n<2A required")
    p=source_prime(n)
    s,B=source_native_seed(A)
    assert B%p!=0 and s!=0
    a,Q,_=clock_state(n)
    original=F(a,Q)
    other=original+16**n*s
    def local(x):
        z=p*x
        assert z.denominator%p!=0
        return z.numerator*pow(z.denominator,-1,p)%p
    assert local(original)==local(other)==4
    return {"A":A,"n":n,"p":p,"same_passport":True,
            "changed_seed":s,"old_clock":B}
