"""Original zero-seeded four-pole BBP: split/inert prime clocks & Gamma correction.

Research only. All exact integers and rational functions preserve the original
forcing; no selected real Weyl asymptotic is presumed. PNT-AP is an external
classical asymptotic theorem, NOT certified by the finite prime sieve.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt, log, pi, ceil


def source(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError('original positive source index required')
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def real_source(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError('original positive source index required')
    return -Q(1, 4*n-3)-Q(1, 4*(2*n-1))-Q(1, 4*(4*n-1))-Q(1, 32*n)


def gaussian_source(n: int) -> Q:
    return source(n)-real_source(n)


def fraction_states(last: int):
    """Yield (n,U_H,U_G,U) exact unwrapped, all literal zero-seeded."""
    if type(last) is not int or last < 0:
        raise ValueError('last nonnegative')
    uh=ug=u=Q(0)
    yield 0,uh,ug,u
    for n in range(1,last+1):
        rh=real_source(n)
        rg=source(n)-rh
        uh=16*uh+rh
        ug=16*ug+rg
        u=16*u+source(n)
        assert uh+ug==u
        yield n,uh,ug,u


def geometric_gamma_tail_interval(s: int | Q, terms: int=80) -> tuple[Q,Q]:
    """Exact rational enclosure of -T_H(s) for positive rational s.

    -T_H(s)=(1/32) sum_{j>=1} 2^-j/(s+j/4).
    The omitted tail is bounded above by 2^-terms/(32*s).
    """
    s=Q(s)
    if s <= 0 or type(terms) is not int or terms < 1:
        raise ValueError('positive rational s and terms>=1 required')
    lo=sum((Q(1,32*(1<<j))/(s+Q(j,4)) for j in range(1,terms+1)),Q(0))
    hi=lo+Q(1,32*(1<<terms))/s
    return lo,hi


def gamma_corrected_tail_interval(s:int | Q, terms:int=80)->tuple[Q,Q]:
    """Enclose R_H(s)=T_H(s)+1/(32s), exact positive O(s^-2)."""
    s=Q(s)
    lo,hi=geometric_gamma_tail_interval(s,terms)
    return Q(1,32*s)-hi, Q(1,32*s)-lo


def uniform_gamma_bound(s:int | Q)->Q:
    s=Q(s)
    if s<=0:raise ValueError('s>0')
    return Q(1,64*s*s)


def mixed_phase_correction(n:int,h:int,k:int)->Q:
    """Add (k-h)/(32n) to h U_H(n)+k U_G(n)."""
    if type(n) is not int or n<1 or type(h) is not int or type(k) is not int:
        raise ValueError('exact integers and n>=1')
    return Q(k-h,32*n)


def mixed_phase_error_bound(n:int,h:int,k:int)->Q:
    """Bound real unwrapped correction error vs 16^n theta_hk.

    theta_hk=k*pi/16+(k-h)*log(2)/8.
    Uses original T_n<1/(64n^2), and 0<R_H(n)<1/(64n^2).
    """
    if type(n) is not int or n<1 or type(h) is not int or type(k) is not int:
        raise ValueError('exact integers and n>=1')
    return Q(abs(k)+abs(k-h),64*n*n)


def phase_sum_chord_upper(h:int,k:int,early:int=1,last:int|None=None)->Q:
    """Exact rational upper on sum of complex phase differences.

    Uses 2pi<44/7, and sum_{n>=early}1/n^2<=1/(early-1)
    for early>1. For early=1 use sum 1/n^2<2.
    """
    if type(early) is not int or early<1:
        raise ValueError('early>=1')
    if type(h) is not int or type(k) is not int:
        raise ValueError('integer frequencies')
    factor=Q(11,112)*(abs(k)+abs(k-h)) # 2pi/64 < 11/112
    if last is not None:
        if type(last) is not int or last<early:
            raise ValueError('last>=early')
        return factor*sum((Q(1,n*n) for n in range(early,last+1)),Q(0))
    return factor*(Q(2) if early==1 else Q(1,early-1))


def is_prime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    for k in range(3,isqrt(n)+1,2):
        if n%k==0:return False
    return True


def primes_up_to(stop:int)->list[bool]:
    if stop<1:raise ValueError('stop>=1')
    p=[True]*(stop+1)
    p[0]=p[1]=False
    for k in range(2,isqrt(stop)+1):
        if p[k]:
            for j in range(k*k,stop+1,k):p[j]=False
    return p


def inert_second_injection_index(k:int)->int:
    """For p=4k-1 prime>5, second p-pole is ceil(3k/2)."""
    if type(k) is not int or k<2 or not is_prime(4*k-1):
        raise ValueError('4k-1 prime>5 required')
    return (3*k+1)//2


def pole_injection_residue(n:int,p:int)->int:
    """p*r(n) modulo p if valuation of r(n) >= -1.

    Uses exact rational fraction; unlike p*U_n this is a local source probe.
    """
    z=p*source(n)
    if z.denominator%p == 0:
        raise ArithmeticError('higher-order p-pole, undefined residue')
    return z.numerator*pow(z.denominator,-1,p)%p


def prime_passports(A:int,c_num:int=4,c_den:int=3)->dict:
    """Original simultaneous clean split/inert clocks on [A,ceil(cA)).

    1<c=c_num/c_den<3/2. The clean inert interval is [k,ceil(3k/2)),
    NOT the tempting but false [k,2k). Source p=4k-1 has composite
    3p pole at its SECOND injection.
    """
    if any(type(z) is not int for z in (A,c_num,c_den)) or A<8 or c_den<1:
        raise ValueError('integer A>=8 and rational c')
    if not c_den<c_num or 2*c_num>=3*c_den:
        raise ValueError('require 1<c<3/2')
    stop=(c_num*A+c_den-1)//c_den
    kminus=(2*c_num*A+3*c_den-1)//(3*c_den)
    sieve=primes_up_to(8*A+1)
    plus=[(8*k+1,k+1) for k in range((A+1)//2,A) if sieve[8*k+1]]
    minus=[(4*k-1,k) for k in range(kminus,A+1) if sieve[4*k-1]]
    assert all(p%8==1 and b<=A and 4*(b-1)>=stop-1 for p,b in plus)
    assert all(p%4==3 and b<=A and inert_second_injection_index(b)>=stop for p,b in minus)
    assert set(p for p,_ in plus).isdisjoint(set(p for p,_ in minus))
    return {'A':A,'stop':stop,'c':[c_num,c_den],
            'split':tuple(plus),'inert':tuple(minus)}


def window_prime_clock(p:int,b:int,n:int,kind:str)->int:
    """p*U_n mod p predicted by original clean pole (not a fitted orbit)."""
    if not is_prime(p) or p<=5 or n<b:
        raise ValueError('generic genuine prime and after birth')
    if kind=='split' and p==8*(b-1)+1 and n<=4*(b-1):
        coeff=4
    elif kind=='inert' and p==4*b-1 and n<inert_second_injection_index(b):
        coeff=-pow(2,-1,p)
    else:
        raise ValueError('outside original clean window')
    return (coeff*pow(16,n-b,p))%p


def exact_prime_mass_profile(A:int,c_num:int=4,c_den:int=3)->dict:
    """Finite certificates, not the PNT-AP asymptotic proof.

    Product comparison uses arbitrary-precision integers, not floating logs.
    """
    from math import prod
    pack=prime_passports(A,c_num,c_den)
    ps=[p for p,_ in pack['split']+pack['inert']]
    product=prod(ps)
    lastlag=pack['stop']-A-1
    alias_counts=[]
    kernel_denominators=[]
    for d in range(1,lastlag+1):
        flags=[pow(16,d,p)==1 for p in ps]
        alias_counts.append(sum(flags))
        # |joint Galois-averaged pair kernel| = 1 / product(p-1 over nonaliases).
        from math import prod
        kernel_denominators.append(prod(p-1 for p,aliased in zip(ps,flags) if not aliased))
    result={
        'A':A,'c':pack['c'],'L':pack['stop']-A,
        'split_primes':len(pack['split']),'inert_primes':len(pack['inert']),
        'min_p':min(ps) if ps else None,
        'log_mass_approx':sum(log(p) for p in ps),
        'threshold_log_approx':lastlag*log(16),
        'exact_mass_dominates_full_window':product>16**lastlag-1,
        'minimum_nonaliases_across_lags':len(ps)-max(alias_counts) if alias_counts else len(ps),
        'maximum_alias_count':max(alias_counts) if alias_counts else 0,
        'worst_average_kernel_denominator_bits':min(kernel_denominators).bit_length() if kernel_denominators else 1,
        'first_failed_second_inert_example':{'p':47,'birth':12,'second_pole':18}
    }
    return result
