"""Exact base-16 Stoneham conductor stage and observer/frame-reset controls.

Research only. This is not an arithmetic proof of pi normality.
"""
from __future__ import annotations
from fractions import Fraction
from math import log
from collections import Counter

B=16
C=3

def stage_info(n:int)->tuple[int,int]:
    if n<3: raise ValueError("n must be >= 3")
    p=1
    while 3**(p+1)<=n: p+=1
    return p, 3**p

def stoneham_residue(n:int)->tuple[int,int]:
    """z_n = {16^n sum_{3^k<=n} 1/(3^k 16^(3^k))} as a/q; exact."""
    p,q=stage_info(n)
    a=sum((3**(p-k)*pow(16,n-3**k,q) for k in range(1,p+1)))%q
    return a,q

def complete_stage(p:int)->tuple[int,...]:
    if p<1: raise ValueError("positive stage")
    return tuple(stoneham_residue(n)[0] for n in range(3**p,3**(p+1)))

def next_pulse_error_bound(p:int)->Fraction:
    """Upper bound for positive true orbit-vs-rational-surrogate error on stage p."""
    return Fraction(1,32*3**p)

def actual_tail_partial(n:int,last_k:int)->Fraction:
    """Exact first pieces of true fractional remainder; remaining omitted tail positive."""
    p,_=stage_info(n)
    return sum((Fraction(1,3**k*16**(3**k-n)) for k in range(p+1,last_k+1)),Fraction(0))

def arc_contains(residue:int,denom:int,start:Fraction,length:Fraction)->bool:
    """Containment of residue/denom in half-open circle arc."""
    y=(Fraction(residue,denom)-start)%1
    return y<length

def circle_distance_to_arc(residue:int,denom:int,start:Fraction,length:Fraction)->Fraction:
    """Distance on circle between rational point and closed arc."""
    z=(Fraction(residue,denom)-start)%1
    if z<=length: return Fraction(0)
    return min(z-length,1-z)

def enlarged_arc_count(p:int,start:Fraction,length:Fraction)->int:
    """Count stage sites whose rational surrogate lies within epsilon of arc."""
    e=next_pulse_error_bound(p)
    return sum(circle_distance_to_arc(a,3**p,start,length)<=e for a in complete_stage(p))

def certified_hit_upper(N:int,start:Fraction,length:Fraction)->int:
    """Certified bound on actual orbit arc hits by rational surrogates, not simulated digits."""
    count=min(N,3)
    for n in range(3,N):
        p,q=stage_info(n)
        a,_=stoneham_residue(n)
        count += circle_distance_to_arc(a,q,start,length)<=next_pulse_error_bound(p)
    return count

def uniform_hotspot_bound(N:int,length:Fraction)->Fraction:
    """For all arcs of this length, proven A_N(I) <= 3N length+18P+3."""
    if N<4: return Fraction(N)
    p,_=stage_info(N-1)
    return 3*N*length+18*p+3

def stage_fourier_zero(p:int,h:int)->bool:
    """Exact root-of-unity sum over stage p is 0 iff 3^(p-1) does NOT divide h."""
    return h%(3**(p-1))!=0

def stage_character_formula(p:int,h:int)->tuple[int,int,int]:
    """Root-of-unity sum: returns magnitude, phase numerator modulo modulus, modulus."""
    q=3**p
    if stage_fourier_zero(p,h):return 0,0,q
    return 6*3**(p-1),h%q,q

def fraction_to_digits(x:Fraction,N:int,b:int=16)->tuple[int,...]:
    n=x.numerator%x.denominator
    den=x.denominator
    out=[]
    for _ in range(N):
        n*=b
        d,n=divmod(n,den)
        out.append(d)
    return tuple(out)

def stoneham_prefix(N:int,k:int=6)->tuple[int,...]:
    """Rigorous digits: lower/upper rational truncation agree through N digits.
    k>=1. First omitted pulse at exponent 3^(k+1), far beyond N.
    """
    if N>=3**(k+1):raise ValueError("need N<next pulse for easy certificate")
    a=sum((Fraction(1,3**i*16**(3**i)) for i in range(1,k+1)),Fraction(0))
    upper=a+Fraction(1,2*3**k*16**(3**(k+1)))
    if (a*16**N).__floor__()!=(upper*16**N).__floor__():
        raise AssertionError("not enough tail accuracy for prefix")
    return fraction_to_digits(a,N)

def champernowne_prefix(N:int)->tuple[int,...]:
    words=[];count=0;n=1
    while count<N:
        word=format(n,"X")
        words.append(word);count+=len(word);n+=1
    return tuple(int(c,16) for c in ''.join(words)[:N])

def cylinder_frequency(digits:tuple[int,...],word:tuple[int,...])->tuple[int,int]:
    k=len(word)
    if not k:raise ValueError("word nonempty")
    num=len(digits)-k+1
    if num<=0:return 0,0
    cnt=sum(tuple(digits[i:i+k])==word for i in range(num))
    return cnt,num

def frame_reset_table(digits:tuple[int,...],word:tuple[int,...])->tuple[int,...]:
    """Next digit after any exact fixed history, empirical sampling not conditional probability."""
    k=len(word);hist=[0]*16
    for i in range(len(digits)-k):
        if tuple(digits[i:i+k])==word:hist[digits[i+k]]+=1
    return tuple(hist)

def chosen_digit_zero_ratio(digits:tuple[int,...])->tuple[int,int]:
    """Choice policy computes deterministic digit at index and selects zero digits: adversarial."""
    chosen=[x for x in digits if x==0]
    return len(chosen),sum(x==0 for x in chosen)

def debruijn_16_order2()->tuple[int,...]:
    """An explicit order-2 de Bruijn cycle for 16 symbols (FKM algorithm)."""
    k,n=16,2
    a=[0]*(k*n+1)
    ans=[]
    def db(t,p):
        if t>n:
            if n%p==0:
                ans.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,k):
                a[t]=j
                db(t+1,t)
    db(1,1)
    return tuple(ans)

def cycle_word_counts(cycle:tuple[int,...],k:int)->Counter:
    n=len(cycle)
    return Counter(tuple(cycle[(i+j)%n] for j in range(k)) for i in range(n))

def conditional_next_digit_on_cycle(cycle:tuple[int,...],word:tuple[int,...])->tuple[int,...]:
    n=len(cycle);k=len(word);counts=[0]*16
    for i in range(n):
        if all(cycle[(i+j)%n]==word[j] for j in range(k)):
            counts[cycle[(i+k)%n]]+=1
    return tuple(counts)

def cylinder_index(word:tuple[int,...])->int:
    v=0
    for d in word:
        if not (0<=d<16):raise ValueError("hex digit outside range")
        v=16*v+d
    return v

def cylinder_interval(word:tuple[int,...])->tuple[Fraction,Fraction]:
    """Exact half-open base-16 prefix cylinder."""
    if not word:raise ValueError('word nonempty')
    a=cylinder_index(word)
    q=16**len(word)
    return Fraction(a,q), Fraction(a+1,q)

def lebesgue_frame_reset_mass(word:tuple[int,...],low:Fraction,high:Fraction)->tuple[Fraction,Fraction]:
    """Mass of word plus recentered target, and mass of word; exact Haar."""
    if not (0<=low<=high<=1):raise ValueError('target interval subset [0,1]')
    q=16**len(word)
    return Fraction(high-low,q),Fraction(1,q)


def bbp_forcing(n:int)->Fraction:
    if n<1:raise ValueError('n>=1')
    a=8*n-7
    return 4/Fraction(a)-2/Fraction(a+3)-1/Fraction(a+4)-1/Fraction(a+5)

def bbp_selected(n:int,seed:Fraction=Fraction(0))->Fraction:
    if n<0:raise ValueError('n>=0')
    u=Fraction(seed)
    for m in range(1,n+1):u=16*u+bbp_forcing(m)
    return u

def bbp_tail_bound(n:int)->Fraction:
    """Original-source already-established bound on 16^(n-1) pi - U_n, n>=1."""
    if n<1:raise ValueError('n>=1')
    return Fraction(1,(8*n+1)**2)


def conductor_stage(n:int,c:int)->int:
    if c not in (3,5):raise ValueError('calibrated coprime conductors are c=3 or c=5')
    if n<c:raise ValueError('n before first conductor pulse')
    p=1
    while c**(p+1)<=n:p+=1
    return p

def conductor_residue(n:int,c:int)->tuple[int,int]:
    """Original rational stage of alpha_{16,c}, c in {3,5}."""
    p=conductor_stage(n,c);q=c**p
    return sum(c**(p-k)*pow(16,n-c**k,q) for k in range(1,p+1))%q,q

def conductor_complete_stage(p:int,c:int)->tuple[int,...]:
    if p<1:raise ValueError('p>=1')
    return tuple(conductor_residue(n,c)[0] for n in range(c**p,c**(p+1)))

def conductor_tail_bound(p:int,c:int)->Fraction:
    if p<1 or c not in (3,5):raise ValueError('p>=1, c=3 or5')
    return Fraction(1,16*(c-1)*c**p)

def conductor_hotspot_bound(N:int,length:Fraction,c:int)->Fraction:
    """A_N(I) <= c N |I| + 3 c(c-1) P + c for N >= c+1."""
    if c not in (3,5):raise ValueError('c=3 or5')
    if N<=c:return Fraction(N)
    p=conductor_stage(N-1,c)
    return c*N*length+3*c*(c-1)*p+c

def conductor_certified_upper(N:int,start:Fraction,length:Fraction,c:int)->int:
    """Exact rational stage-surrogate enclosure for hits of true alpha_{16,c}."""
    count=min(N,c)
    for n in range(c,N):
        p=conductor_stage(n,c)
        a,q=conductor_residue(n,c)
        count+=circle_distance_to_arc(a,q,start,length)<=conductor_tail_bound(p,c)
    return count

def conductor_character_formula(p:int,h:int,c:int)->tuple[int,int,int]:
    """Full stage root sum represented by mag*exp(2pi i phase /q)."""
    if p<1 or c not in (3,5):raise ValueError('invalid stage/conductor')
    q=c**p
    if h%(c**(p-1))!=0:return (0,0,q)
    return ((c-1)*q,h%q,q)

def nonunit_two_hex_pulses(K:int)->tuple[tuple[int,int],...]:
    """Exact isolated nonzero hex digit (position, value) for alpha_{16,2}."""
    if K<0:raise ValueError('nonnegative K')
    return tuple((2**k+(k+3)//4,2**(4*((k+3)//4)-k)) for k in range(1,K+1))


def stoneham_general_prefix(N:int,c:int,K:int)->tuple[int,...]:
    """Certify digits of alpha_{16,c} for c in 2,3,5, avoiding decimal floats."""
    if c not in (2,3,5):raise ValueError('c=2,3,5')
    if N>=c**(K+1):raise ValueError('K too small for bound')
    alpha=sum((Fraction(1,c**k*16**(c**k)) for k in range(1,K+1)),Fraction(0))
    # sum omitted 1/c^k <= 1/((c-1)c^K), every omitted radix term has 16^(-c^(K+1)) factor or smaller.
    upper=alpha+Fraction(1,(c-1)*c**K*16**(c**(K+1)))
    if int(alpha*16**N)!=int(upper*16**N):raise AssertionError('prefix not certified')
    return fraction_to_digits(alpha,N)
