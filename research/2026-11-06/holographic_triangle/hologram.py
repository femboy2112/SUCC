"""SUCC holographic triangle: exact source, 2-adic shadows, and carry seam.

Research-only. Original four signed BBP poles and literal U0=0.
All congruences in R_k=Z/(2**k); fractions must have ODD denominators.
None of these finite identities is a pi-normality or real Weyl estimate.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import floor

WEIGHTS = (4, -2, -1, -1)
POLES = (7, 4, 3, 2)


def forcing(n: int, weights=WEIGHTS) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("n must be an integer >= 1")
    if len(weights) != 4:
        raise ValueError("exact four signed pole weights required")
    return sum((Fraction(w, 8*n - a) for w, a in zip(weights, POLES)), Fraction())


def combined_forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("n must be an integer >= 1")
    return Fraction(120*n*n - 89*n + 16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def state(n: int, *, seed: Fraction | int = 0, source=forcing) -> Fraction:
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    y = Fraction(seed)
    for j in range(1, n+1):
        y = 16*y + source(j)
    return y


def mod_fraction(x: Fraction | int, k: int) -> int:
    if type(k) is not int or k < 1:
        raise ValueError("k must be positive")
    q = Fraction(x)
    if q.denominator % 2 == 0:
        raise ValueError("2-adic reduction requires an odd denominator")
    m = 1 << k
    return q.numerator * pow(q.denominator, -1, m) % m


@dataclass(frozen=True)
class Edges:
    p: int  # A+B
    q: int  # A+X
    s: int  # B+X=A
    k: int

    @property
    def modulus(self):
        return 1 << self.k

    def defect(self) -> int:
        return (self.p + self.q - 3*self.s) % self.modulus


@dataclass(frozen=True)
class Center:
    a: int  # unwrapped state U mod 2^k
    b: int  # integer carry C mod 2^k
    x: int  # rational fractional x mod 2^k
    k: int

    @property
    def seam(self):
        return (self.a-self.b-self.x) % (1 << self.k)


def center_from_rational(u: Fraction | int, k: int) -> Center:
    y = Fraction(u)
    b = y.numerator // y.denominator
    x = y-b
    return Center(mod_fraction(y,k), b%(1<<k), mod_fraction(x,k), k)


def edge_encode(center: Center) -> Edges:
    m = 1 << center.k
    return Edges((center.a+center.b)%m, (center.a+center.x)%m,
                 (center.b+center.x)%m,center.k)


def edge_decode(edges: Edges) -> Center:
    if edges.defect():
        raise ValueError("incompatible boundary: p + q != 3s")
    m = edges.modulus
    return Center(edges.s %m, (edges.p-edges.s)%m,
                  (edges.q-edges.s)%m,edges.k)


def boundary_step(edges: Edges, source: Fraction, carry_increment: int) -> Edges:
    k,m=edges.k,edges.modulus
    rr=mod_fraction(source,k)
    return Edges((16*edges.p+rr+carry_increment)%m,
                 (16*edges.q+2*rr-carry_increment)%m,
                 (16*edges.s+rr)%m,k)


def real_step(u: Fraction | int, source: Fraction) -> tuple[Fraction,int]:
    y=Fraction(u)
    x=y-(y.numerator//y.denominator)
    r=Fraction(source)
    t=(16*x+r).numerator//(16*x+r).denominator
    return 16*y+r,t


def numerator_from_shadow(edges: Edges, denominator: int) -> int:
    """Exact a from x=a/d with 0<=a<d, odd d<=2^K, if data admissible."""
    if type(denominator) is not int or denominator < 1 or denominator%2 == 0:
        raise ValueError("positive odd denominator required")
    if denominator>edges.modulus:
        raise ValueError("insufficient observation resolution")
    c=edge_decode(edges)
    a= (denominator*c.x)%edges.modulus
    if a>=denominator:
        raise ValueError("no numerator in the declared [0,d) range")
    return a


def primitive_h(n: int) -> Fraction:
    """Source-harmonic accumulation; equals exact digamma potential in dossier."""
    if type(n) is not int or n<0:
        raise ValueError("n>=0 required")
    return sum((forcing(j) for j in range(1,n+1)),Fraction())


def state_from_primitive(n: int) -> Fraction:
    """Independent Abel transform of r(n)=H(n)-H(n-1)."""
    if type(n) is not int or n < 0:
        raise ValueError("n>=0 required")
    return primitive_h(n)+15*sum((16**(n-1-j)*primitive_h(j)
                         for j in range(1,n)),Fraction())


def is_prime(n: int) -> bool:
    if n<2: return False
    if n%2==0:return n==2
    i=3
    while i*i<=n:
        if n%i==0:return False
        i+=2
    return True


def next_prime_after(n: int) -> int:
    p=n+1
    while not is_prime(p):p+=1
    return p


def first_pole(p: int) -> tuple[int, Fraction]:
    """Birth of p>5 in original source; c_p rational mod p."""
    if p<=5 or not is_prime(p):
        raise ValueError("odd prime p>5 required")
    if p%8==1:return (p+7)//8,Fraction(4)
    if p%8==5:return (p+3)//8,Fraction(-1)
    return (p+1)//4,Fraction(-1,2)


def source_denominator_witness(N: int) -> tuple[int,int,int]:
    """Bertrand + original pole-birth: d_(n_p)>N, n_p<N, for N>=6."""
    if type(N) is not int or N<6:
        raise ValueError("N must be integer >=6")
    p=next_prime_after(N)
    if not p<2*N:
        raise AssertionError("Bertrand prime failed")
    n,_=first_pole(p)
    assert 0<n<N
    d=state(n).denominator
    assert d%p==0 and d>N
    return p,n,d


