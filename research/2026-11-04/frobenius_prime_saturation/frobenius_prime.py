"""Authentic zero-seeded BBP prime-Frobenius pulse transport (research only).

For every p>5 with p^2>8*N, p-local residue p*U_N is synthesized
from the original four signed poles by universal Q pulse recurrences
indexed by a=p mod8.  This never averages over Galois source choices.

The universal nonzero-pulse sign theorem and conductor asymptotic are
paper theorems in PROOFS.md; finite code tests only finite instances.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from functools import lru_cache

POLES = ((7,4), (4,-2), (3,-1), (2,-1))
ALLOWED_CLASSES=(1,3,5,7)

@lru_cache(maxsize=4096)
def is_prime(n:int)->bool:
    """Exact trial division, only for authenticated finite prime probes."""
    if type(n) is not int or n<2:return False
    if n%2==0:return n==2
    return all(n%q for q in range(3,isqrt(n)+1,2))

def source(n: int)->F:
    if type(n) is not int or n<1:raise ValueError('n>=1 exact integer required')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def dual_source(n: int)->F:
    if type(n) is not int or n<1:raise ValueError('n>=1 exact integer required')
    return F(8,8*n-6)+F(4,8*n-5)+F(4,8*n-4)-F(1,8*n-1)

def source_state(n:int)->F:
    if type(n) is not int or n<0:raise ValueError('n>=0')
    v=F(0)
    for k in range(1,n+1):v=16*v+source(k)
    return v

def dual_state(n:int)->F:
    if type(n) is not int or n<0:raise ValueError('n>=0')
    v=F(0)
    for k in range(1,n+1):v=16*v+dual_source(k)
    return v

def chi_two(a: int)->int:
    if a not in ALLOWED_CLASSES: raise ValueError('a mod8 must be odd')
    return 1 if a in (1,7) else -1

def pulse_events(a: int, max_m:int)->tuple[tuple[int,int,int],...]:
    """m,pole offset c, signed weight w; event time j=(mp+c)/8.

    Condition m*a+c=0 (mod8). All pulses are genuine 8j-c=mp.
    """
    if a not in ALLOWED_CLASSES or type(max_m) is not int or max_m<0:
        raise ValueError('odd class and m cutoff required')
    return tuple((m,c,w) for m in range(1,max_m+1)
                 for c,w in POLES if (m*a+c)%8==0)

def pulse_factor(a:int,old:tuple[int,int,int],new:tuple[int,int,int])->F:
    m0,c0,_=old;m,c,_=new
    if m<=m0 or (m-m0+c-c0)%2:raise ValueError('successive lawful p events required')
    d=m-m0
    return (F(chi_two(a))**d)*(F(2)**((d+c-c0)//2))

def universal_pulse_states(a:int,max_m:int)->tuple[tuple[int,int,int,F],...]:
    """Universal Q normalizers C_a(m); valid mod all sufficiently large p≡a.

    At an event 8j-c=mp: p*U_j ≡ C_a(m) (mod p), assuming
    p^2>8j, p not dividing any rational normalizer's denominator.
    """
    ev=pulse_events(a,max_m)
    C=F(0);old=None;out=[]
    for m,c,w in ev:
        cur=(m,c,w)
        C=F(w,m) if old is None else pulse_factor(a,old,cur)*C+F(w,m)
        out.append((m,c,w,C))
        old=cur
    return tuple(out)

def shell_constant(a:int,n:int)->F:
    """Full four-pole pulse shell (k=n-1); Q source or dual source."""
    if a not in ALLOWED_CLASSES or type(n) is not int or n<1:
        raise ValueError('n>=1, a odd')
    m=8*(n-1)+(6 if a in (1,5) else 7)
    return universal_pulse_states(a,m)[-1][-1]

def full_shell_closed(a:int,n:int)->F:
    if a in (1,5):return source_state(n)
    if a==3:return dual_state(n)
    if a==7:return -4*dual_state(n)
    raise ValueError('odd a mod8')

def pulse_sign(a:int,m:int)->int:
    """Paper-proved nonzero sign at each admissible source pulse m."""
    if a not in ALLOWED_CLASSES or type(m) is not int or m<1:
        raise ValueError('invalid class/event')
    if m not in [z[0] for z in pulse_events(a,m)]:
        raise ValueError('m is not a pulse for class')
    if a==1:return 1
    if a==7:return -1
    if a==3:return (-1 if m%8 in (2,4) else 1)
    if a==5:return (-1 if m%8 in (1,5) else 1)
    raise AssertionError()

def source_pulses_at(p:int,n:int)->tuple[tuple[int,int,int,int],...]:
    """All ACTUAL pole events (m,c,w,j) with j<=n. p prime assumed by caller."""
    if not is_prime(p) or p<=5 or type(n) is not int or n<1:
        raise ValueError('genuine prime p>5 and n>=1')
    ev=[]
    # Largest original linear denominator at j=n is 8n-2, so m*p<=8n.
    for m,c,w in pulse_events(p%8,(8*n)//p+1):
        q=m*p+c
        if q%8==0 and 1<=q//8<=n:
            ev.append((m,c,w,q//8))
    return tuple(ev)

def predicted_p_residue(p:int,n:int)->int:
    """Return genuine p*U_n mod p from universal normalizer.

    Requires p prime>5, p²>8n and all normalized denominators p-units.
    A prime check belongs to caller/test, not a hidden numerical proof.
    """
    if p*p<=8*n:raise ValueError('p²>8n required (simple-pole regime)')
    ev=source_pulses_at(p,n)
    if not ev:return 0
    m,c,w,at=ev[-1]
    C=universal_pulse_states(p%8,m)[-1][-1]
    if C.denominator%p==0:raise ValueError('normalizer not defined modulo p')
    return (C.numerator*pow(C.denominator,-1,p)*pow(16,n-at,p))%p

def integer_lcm_state(n:int)->tuple[int,int,int]:
    """Entire unwrapped BBP state as A/M, with COMMON source LCM M.

    Independent of direct Fraction recursive reduction; source forcing
    fractions are evaluated separately, with all four genuine poles.
    """
    if type(n) is not int or n<0:raise ValueError('n>=0')
    M=1;A=0
    for j in range(1,n+1):
        x=source(j)
        N=lcm(M,x.denominator)
        A=16*(N//M)*A+x.numerator*(N//x.denominator)
        M=N
    return A,M,M//gcd(A,M)

def modular_residue_of_unwrapped(x:F,p:int)->int:
    v=p*x
    if v.denominator%p==0:raise ValueError('valuation below -1')
    return (v.numerator*pow(v.denominator,-1,p))%p

def eligible_source_prime(p:int,n:int)->bool:
    if p<=5 or p%2==0:return False
    if p%4==1:
        return (p+7)//8<=n if p%8==1 else (p+3)//8<=n
    return (p+1)//4<=n
