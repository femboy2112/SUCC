"""Exact Pascal 2↔3 transport, p-adic conjugacy and Haar countertests.

Research only, stacked on SUCC draft #427. Arithmetic testable on finite
integer inputs; global homeomorphism/measure claims have paper proofs.
No π-normality, RH or general positive-Pisot functor claim.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import comb

def pascal_forward(seq):
    """B(a)_n = sum_k binom(n,k) a_k."""
    a=tuple(seq)
    return tuple(sum(comb(n,k)*a[k] for k in range(n+1))
                 for n in range(len(a)))

def pascal_inverse(seq):
    """Exact signed binomial inversion."""
    a=tuple(seq)
    return tuple(sum((-1)**(n-k)*comb(n,k)*a[k] for k in range(n+1))
                 for n in range(len(a)))

def binomial_integer(n:int,k:int)->int:
    """Generalized binomial coefficient for integer n, nonnegative k."""
    if type(n) is not int or type(k) is not int or k<0:
        raise ValueError("integer n, k>=0")
    if n>=0:return comb(n,k) if k<=n else 0
    return (-1)**k*comb(k-n-1,k)

def three_pow_in_two_adics(n:int,a:int)->int:
    """(1+2)^n modulo 2^a via convergent Pascal/binomial series."""
    if type(n) is not int or type(a) is not int or not 1<=a<=64:
        raise ValueError("integer n and dyadic precision a in 1..64")
    q=2**a
    return sum(binomial_integer(n,k)*2**k for k in range(a))%q

def sixteen_pow_in_three_adics(n:int,b:int)->int:
    """(1+15)^n modulo 3^b, valid for signed integer n."""
    if type(n) is not int or type(b) is not int or not 1<=b<=32:
        raise ValueError("integer n and triadic precision b in 1..32")
    q=3**b
    return sum(binomial_integer(n,k)*15**k for k in range(b))%q

def v_p_integer(n:int,p:int)->int:
    if type(n) is not int or n==0 or type(p) is not int or p<2:
        raise ValueError("nonzero integer and prime p>=2")
    z=abs(n);v=0
    while z%p==0:z//=p;v+=1
    return v

# Explicit prefix-free complete binary code for ternary symbols:
# 0 -> 00; 1 -> 01; 2 -> 1. A binary stream parses uniquely.

def odd_binary_to_ternary_unit(u:int)->int:
    """Finite-integer restriction of a Cantor homeomorphism Z2^× -> Z3^×."""
    if type(u) is not int or u<1 or u%2!=1:
        raise ValueError("positive odd 2-adic unit required")
    t=u>>1
    y=1+(t&1)  # first ternary digit: 1 or 2
    t>>=1
    power=3
    while t:
        bit=t&1;t>>=1
        if bit: digit=2
        else:
            digit=t&1;t>>=1
        y+=digit*power;power*=3
    return y

def ternary_unit_to_odd_binary(y:int)->int:
    """Exact inverse prefix-code map on positive 3-adic units."""
    if type(y) is not int or y<1 or y%3==0:
        raise ValueError("positive 3-adic unit required")
    leading=y%3;t=y//3
    u=1+((leading-1)<<1)
    bitpos=2
    while t:
        digit=t%3;t//=3
        if digit==2:
            u+=1<<bitpos;bitpos+=1
        else:
            if digit==1:u+=1<<(bitpos+1)
            bitpos+=2
    return u

def binary_affine_to_ternary(x:int)->int:
    """Natural restriction of H: Z2→Z3, H(2x+1)=3H(x), H(-1)=0."""
    if type(x) is not int or x<-1:
        raise ValueError("integer x>=-1")
    if x==-1:return 0
    u=x+1;n=0
    while u%2==0:u//=2;n+=1
    return 3**n*odd_binary_to_ternary_unit(u)

def ternary_to_binary_affine(y:int)->int:
    """Natural restriction of H^(-1), y>=0. y=0 maps to 2-adic fixed -1."""
    if type(y) is not int or y<0:
        raise ValueError("nonnegative integer y")
    if y==0:return -1
    n=0
    while y%3==0:y//=3;n+=1
    return 2**n*ternary_unit_to_odd_binary(y)-1

def induced_ternary_prefix_probabilities(m:int)->dict[tuple[int,...],Fraction]:
    """Exact image distribution of binary Haar on m 3-adic unit digits."""
    if type(m) is not int or not 1<=m<=8:
        raise ValueError("prefix depth 1..8")
    from itertools import product
    result={}
    for first in (1,2):
        for tail in product((0,1,2),repeat=m-1):
            p=Fraction(1,2)
            for digit in tail:
                p*=Fraction(1,2) if digit==2 else Fraction(1,4)
            result[(first,*tail)]=p
    return result

def empirical_prefix_probabilities(m:int)->dict[tuple[int,...],Fraction]:
    """Exhaustive fair binary bits; exactly enough to resolve m ternary digits."""
    if type(m) is not int or not 1<=m<=7:
        raise ValueError("finite exhaustive depth 1..7")
    length=1+2*(m-1)
    total=2**length
    hist=Counter()
    for binary_tail in range(total):
        u=1+(binary_tail<<1)
        v=odd_binary_to_ternary_unit(u)
        hist[tuple(v//3**k%3 for k in range(m))]+=1
    return {w:Fraction(n,total) for w,n in hist.items()}

def predicted_shell_measures(n:int)->tuple[Fraction,Fraction]:
    """P_Haar2(v3(H(x))>=n), P_Haar3(v3(y)>=n)."""
    if type(n) is not int or n<0:raise ValueError("nonnegative depth")
    return Fraction(1,2**n),Fraction(1,3**n)

def quadratic_product(x:tuple[int,int],y:tuple[int,int])->tuple[int,int]:
    """Multiplication in Q(sqrt(2)), coordinates a+b sqrt(2)."""
    a,b=x;c,d=y
    return a*c+2*b*d,a*d+b*c

def quadratic_power(x:tuple[int,int],n:int)->tuple[int,int]:
    if type(n) is not int or n<0:raise ValueError("n>=0")
    result=(1,0)
    for _ in range(n):result=quadratic_product(result,x)
    return result

def algebraic_pascal_conjugate_trace(seq):
    """Applied to exact traces Tr((a+b√2)^k); Pascal shifts a by +1."""
    return pascal_forward(seq)


def pascal_codeword_count_law(m:int)->tuple[Fraction,...]:
    """Under fair binary bits, A=#one-bit codewords among m ternary outputs.

    A ~ Binomial(m,1/2): exact Pascal triangle normalized by row sum.
    """
    if type(m) is not int or not 0<=m<=64:
        raise ValueError("integer count depth 0..64")
    return tuple(Fraction(comb(m,a),2**m) for a in range(m+1))

def native_ternary_codeword_count_law(m:int)->tuple[Fraction,...]:
    """Under ternary Haar A=#digit2 ~ Binomial(m,1/3)."""
    if type(m) is not int or not 0<=m<=64:
        raise ValueError("integer count depth 0..64")
    return tuple(Fraction(comb(m,a)*2**(m-a),3**m) for a in range(m+1))

def word_law_pair(word:tuple[int,...])->tuple[Fraction,Fraction]:
    """Two exact probabilities of one word under transported and native Haar."""
    if type(word) is not tuple or any(d not in (0,1,2) or type(d) is not int for d in word):
        raise ValueError("ternary tuple required")
    m=len(word); a=word.count(2)
    return Fraction(1,2**(2*m-a)),Fraction(1,3**m)

def mean_binary_code_length(m:int)->Fraction:
    """One- and two-bit codewords require expected 3m/2 source bits."""
    if type(m) is not int or m<0:raise ValueError("nonnegative m")
    return Fraction(3*m,2)


def original_bbp_two_residues(N:int,a:int)->tuple[int,...]:
    """Original four signed poles, U0=0, exact n=0,...,N-1 in Z/2^a.

    Finite independent implementation of the inherited SUCC DSI isometry.
    """
    if type(N) is not int or N<1 or type(a) is not int or not 1<=a<=18:
        raise ValueError("positive N, dyadic bits a=1..18")
    q=2**a;u=0;rows=[u]
    for n in range(1,N):
        A=120*n*n-89*n+16
        D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        u=(16*u+A*pow(D,-1,q))%q
        rows.append(u)
    return tuple(rows)

def selected_source_ternary_histogram(b:int):
    """Genuine BBP source time distribution of H(U_n) modulo 3^b."""
    if type(b) is not int or not 1<=b<=6:
        raise ValueError("ternary depth 1..6")
    q=2**(2*b);r=3**b
    states=original_bbp_two_residues(q,2*b)
    return dict(Counter(binary_affine_to_ternary(x)%r for x in states))

def selected_source_joint_ternary_clock(b:int):
    """Compare H(U_n) and authentic 16^n mod3^b over CRT joint period."""
    if type(b) is not int or not 1<=b<=4:
        raise ValueError("joint source depth 1..4")
    q=2**(2*b);r=3**b;L=3**(b-1);N=q*L
    states=original_bbp_two_residues(N,2*b)
    observed=Counter((binary_affine_to_ternary(x)%r,pow(16,n,r))
                      for n,x in enumerate(states))
    local=selected_source_ternary_histogram(b)
    clock={pow(16,n,r) for n in range(L)}
    expected={(v,z):count for v,count in local.items() for z in clock}
    return {'period':N,'observed':dict(observed),'expected':expected,
            'exact_factorization':dict(observed)==expected}

def selected_source_unit_pascal_histogram(m:int):
    """Authentic BBP source conditional binary unit -> ternary prefix law.

    Source DSI guarantees U_n mod2^(2m) visits EVERY residue once per
    complete period. Condition U_n+1 odd; induced path count is Pascal.
    """
    if type(m) is not int or not 1<=m<=6:
        raise ValueError("unit output prefix depth m 1..6")
    q=2**(2*m);seq=original_bbp_two_residues(q,2*m)
    unit=[x+1 for x in seq if (x+1)%2==1]
    c=Counter(tuple((odd_binary_to_ternary_unit(u)//3**k)%3
                    for k in range(m)) for u in unit)
    return {'total':len(unit),'probabilities':
            {w:Fraction(n,len(unit)) for w,n in c.items()},
            'expected':induced_ternary_prefix_probabilities(m)}
