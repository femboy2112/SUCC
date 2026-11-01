"""Exact carrier-relative Weyl, radix branch and original-BBP local-source laboratory.

Research only: no physical Planck constant, no signed real-circle saving. Operations
are finite basis maps and rational integer/residue arithmetic, not float matrices.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from collections import defaultdict
from math import gcd

BASE = 16


def modulus(level: int) -> int:
    if type(level) is not int or not 1 <= level <= 6:
        raise ValueError("finite positive radix16 precision level 1..6 required")
    return BASE**level


def shift(level: int, x: int, amount: int = 1) -> int:
    return (x + amount) % modulus(level)


def clock_exponent(level: int, x: int, character: int = 1) -> int:
    """Exact exponent for exp(2pi*i * character*x / 16**level)."""
    return character * x % modulus(level)


def commutator_exponent(level: int, amount: int, character: int = 1) -> int:
    """C_k S_a = zeta^(a*k) S_a C_k on H_level."""
    return amount * character % modulus(level)


def digit_embedding(level: int, digit: int, x: int) -> int:
    """J_(r,digit) |x> = |16*x+digit> in H_(r+1)."""
    if type(digit) is not int or not 0 <= digit < BASE:
        raise ValueError("source branch must be one exact base16 digit")
    if type(x) is not int or not 0 <= x < modulus(level):
        raise ValueError("coarse clock state is out of domain")
    return BASE * x + digit


def recover_branch(level: int, fine: int) -> tuple[int, int]:
    """Return exact digit and parent state from one fine basis element."""
    if type(fine) is not int or not 0 <= fine < modulus(level+1):
        raise ValueError("fine state is out of domain")
    x, a = divmod(fine, BASE)
    return a, x


def branch_shift(level: int, digit: int, x: int) -> tuple[int, int]:
    return recover_branch(level, shift(level+1, digit_embedding(level,digit,x)))


def branch_clock_phase(level: int, digit: int, x: int, k: int) -> tuple[int,int,int]:
    """Check k*(16*x+a) = 16*k*x + k*a modulo fine modulus."""
    fine = modulus(level+1)
    parent = modulus(level)
    lhs = clock_exponent(level+1, digit_embedding(level,digit,x), k)
    return lhs, (BASE*clock_exponent(level,x,k)+k*digit)%fine, (k*digit)%fine


def original_four_pole(n: int) -> F:
    if type(n) is not int or n<1:
        raise ValueError("original BBP source requires integer n >= 1")
    return (F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))


def original_combined(n: int) -> F:
    if type(n) is not int or n<1:
        raise ValueError("original BBP source requires integer n >= 1")
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_state(n: int) -> F:
    if type(n) is not int or n < 0:
        raise ValueError("time n>=0 required")
    x=F(0)
    for j in range(1,n+1):
        x=16*x+original_four_pole(j)
    return x


def two_adic_residue(x: F, level: int) -> int:
    """Only rational numbers with odd denominator have a Z_2 residue."""
    if not isinstance(x,(int,F)):
        raise TypeError("exact rational source required")
    y=F(x)
    q=modulus(level)
    if gcd(y.denominator,q)!=1:
        raise ValueError("non-2-integral denominator, no canonical local residue")
    return (y.numerator*pow(y.denominator,-1,q)) % q


@dataclass(frozen=True)
class SourceCarry:
    parent_level: int
    time: int
    state_before: int
    source_digit: int
    source_carry: int
    state_after: int


def source_carry_step(level: int, n: int) -> SourceCarry:
    """Exact BBP U_(n+1)=16(U_n+c)+a modulo 16^(r+1)."""
    if type(n) is not int or n<0:
        raise ValueError("n must be a nonnegative original-source time")
    if level >= 6:
        raise ValueError("fine level must exist")
    x=two_adic_residue(original_state(n),level)
    source=original_four_pole(n+1)
    rem=two_adic_residue(source,level+1)
    a=rem % BASE
    c=(rem-a)//BASE
    y=digit_embedding(level,a,(x+c)%modulus(level))
    assert y==two_adic_residue(original_state(n+1),level+1)
    return SourceCarry(level,n,x,a,c,y)


def real_phase_nonfactor_witness(level: int) -> tuple[F,F]:
    """Both equal 0 mod 16^r; fractional real phase separation exactly 1/3."""
    q=modulus(level)
    x,y=F(0),F(q,3)
    assert two_adic_residue(y,level)==two_adic_residue(x,level)
    assert y%1==F(1,3) # 16^r = 1 mod 3
    return x,y


def kinetic_basis(level: int, x: int, stride: int=1) -> dict[int,int]:
    """Finite graph kinetic (2I-S^stride-S^-stride) on one basis vector."""
    q=modulus(level)
    if not 0<=x<q: raise ValueError("kinetic basis out of domain")
    if type(stride) is not int or stride<1: raise ValueError("positive stride required")
    d=defaultdict(int)
    d[x]+=2
    d[(x+stride)%q]-=1
    d[(x-stride)%q]-=1
    return {i:v for i,v in d.items() if v}


def embed_linear(level: int, digit: int, vector: dict[int,int]) -> dict[int,int]:
    d=defaultdict(int)
    for x,v in vector.items():d[digit_embedding(level,digit,x)]+=v
    return {i:v for i,v in d.items() if v}


def quadratic_pisot_multiply(a: int,b: int) -> tuple[int,int]:
    """(2+sqrt 2)*(a+b sqrt2) in Z[sqrt 2]."""
    if type(a) is not int or type(b) is not int:
        raise TypeError("integer algebraic coordinates required")
    return (2*a+2*b,a+2*b)


def quadratic_pisot_division(a:int,b:int)->tuple[int,int,int]:
    """Unique digit d in {0,1}, w in Z[sqrt2] with a+b√2=(2+√2)w+d."""
    if type(a) is not int or type(b) is not int:
        raise TypeError("integer algebraic coordinates required")
    d=a%2
    w=(a-d-b, b-(a-d)//2)
    A,B=quadratic_pisot_multiply(*w)
    assert (A+d,B)==(a,b)
    return (d,*w)


def pisot_squared_matrix() -> tuple[tuple[int,int],tuple[int,int]]:
    """β²=2(3+2√2): β²Z[√2]=2Z[√2]; quotient=(Z/2)^2."""
    return ((6,8),(4,6))


def affine_compose(a:int,m:int,b:int,n:int) -> tuple[int,int]:
    if type(m) is not int or type(n) is not int or m<=0 or n<=0:
        raise ValueError("positive integral affine multipliers")
    return (a+m*b,m*n)


def symplectic_scaling(m:int)->tuple[tuple[F,F],tuple[F,F]]:
    if type(m) is not int or m<1:raise ValueError("positive integer dilation")
    return ((F(m),F(0)),(F(0),F(1,m)))


def symplectic_defect(m:int, dual_scale: F) -> F:
    """For diag(m,dual_scale), (M^T J M)_(0,1)-J_(0,1)."""
    return F(m)*F(dual_scale)-1


def elementary_uncertainty_bound(group_order:int,support_x:int,support_dual:int)->bool:
    if any(type(y) is not int or y<1 for y in (group_order,support_x,support_dual)):
        raise ValueError("positive finite support sizes")
    if support_x>group_order or support_dual>group_order:raise ValueError("support exceeds carrier")
    return support_x*support_dual>=group_order


def exact_cyclotomic_character_sum(level:int, support:tuple[int,...], character:int)->tuple[int,...]:
    """Exact coefficient vector in Z[zeta_(16**r)] via Phi_(16**r)=X^(Q/2)+1.

    Zero vector iff the character sum is exactly zero as a complex number.
    The domain is explicitly a POWER OF TWO clock; not valid for general quotients.
    """
    Q=modulus(level)
    half=Q//2
    terms=[0]*half
    for x in support:
        if type(x) is not int or not 0<=x<Q:
            raise ValueError("support point outside the finite clock")
        e=(character*x)%Q
        if e<half:terms[e]+=1
        else:terms[e-half]-=1
    return tuple(terms)


def same_level_dilation_kernel_size(level:int,m:int=16)->int:
    """Exact kernel size of x->m*x on Z/(16**r)."""
    if type(m) is not int or m<1:raise ValueError("positive integer dilation required")
    return gcd(modulus(level),m)


def source_symplectic_step(n: int, x: F, p: F) -> tuple[F,F]:
    """Exact affine canonical lift: (x,p)->(16*x+r(n+1),p/16)."""
    if type(n) is not int or n<0:
        raise ValueError("original source time n>=0")
    if not isinstance(x,(int,F)) or not isinstance(p,(int,F)):
        raise TypeError("exact rational canonical frame required")
    return (BASE*F(x)+original_four_pole(n+1), F(p,BASE))


def bbp_source_action(n:int)->tuple[F,F,F]:
    """(x_n,p_n,A_n=x_n*p_n) with original x0=0,p0=1."""
    if type(n) is not int or n<0:raise ValueError("n>=0")
    x,p=F(0),F(1)
    for j in range(n):x,p=source_symplectic_step(j,x,p)
    return x,p,x*p


def bbp_normalized_sum(n:int)->F:
    """Independent exact finite BBP sum, no phase or normality implication."""
    if type(n) is not int or n<0:raise ValueError("n>=0")
    return sum((original_combined(j)/BASE**j for j in range(1,n+1)),F(0))
