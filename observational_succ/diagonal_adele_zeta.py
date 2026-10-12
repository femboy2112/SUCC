"""Exact diagonal rational carrier: p-adic clock/Archimedean reciprocity.

All arithmetic proof receipts are exact Fraction/int computations. The local
p-adic partial observations are mathematically defined, not physical probes.
This module does NOT instantiate a real infinity, construct a Gamma factor,
prove RH, or infer quantum entanglement from deterministic coupling.

Theorems: rational product formula, global additive-character reciprocity,
shift/multiplier naturality, and bounded-height strong separation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, prod
from typing import Mapping, Sequence


class DiagonalSourceError(ValueError):
    """Invalid arithmetic source, unsupported inference, or false precision."""


def rational(x: int | F) -> F:
    if type(x) not in (int, F):
        raise DiagonalSourceError("Only exact integer or Fraction arithmetic")
    return F(x)


def prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(p % k for k in range(2, isqrt(p) + 1))


def factor_positive(n: int) -> dict[int, int]:
    if type(n) is not int or n < 1:
        raise DiagonalSourceError("Prime factorization requires positive integer")
    factors: dict[int,int] = {}
    q=n
    d=2
    while d*d <= q:
        while q % d == 0:
            factors[d]=factors.get(d,0)+1
            q//=d
        d+=1
    if q>1:
        factors[q]=factors.get(q,0)+1
    return factors


def valuation(q: int | F, p: int) -> int:
    """v_p(q); only nonzero rationals have finite valuation here."""
    q=rational(q)
    if not prime(p) or not q:
        raise DiagonalSourceError("Need authentic rational prime and nonzero rational")
    num,den=abs(q.numerator),q.denominator
    v=0
    while num%p==0:
        num//=p
        v+=1
    while den%p==0:
        den//=p
        v-=1
    return v


def valuations(q: int | F) -> dict[int,int]:
    q=rational(q)
    if not q:
        raise DiagonalSourceError("No multiplicative normalized product at zero")
    out=factor_positive(abs(q.numerator))
    for p,v in factor_positive(q.denominator).items():
        out[p]=out.get(p,0)-v
    return {p:out[p] for p in sorted(out) if out[p]}


def fractional_padic_part(q: int | F, p: int) -> F:
    """Canonical representative {q}_p in [0,1) for q mod Z_p.

    If v_p(q)=-k<0, divide out prime powers and invert denominator modulo
    p**k. By construction q-{q}_p belongs to Z_p.
    """
    q=rational(q)
    if not prime(p):
        raise DiagonalSourceError("Composite fake prime-place rejected")
    if not q:
        return F(0)
    v=valuation(q,p)
    if v>=0:
        return F(0)
    k=-v
    n,d=q.numerator,q.denominator
    while n%p==0:
        n//=p
    while d%p==0:
        d//=p
    modulus=p**k
    residue=(n*pow(d,-1,modulus))%modulus
    answer=F(residue,modulus)
    if q!=answer and valuation(q-answer,p)<0:
        raise AssertionError("Wrong p-adic fractional part")
    return answer


def additive_reciprocity(q: int | F) -> dict:
    """Sum_p {q}_p - q is an integer: diagonal global character cancels."""
    q=rational(q)
    places=tuple(sorted(factor_positive(q.denominator)))
    pieces={p:fractional_padic_part(q,p) for p in places}
    real_angle=-q
    finite_angle=sum(pieces.values(),F(0))
    total=real_angle+finite_angle
    if total.denominator!=1:
        raise AssertionError("Global additive character does not annihilate Q")
    return {"q":q,"real_angle":real_angle,"finite_angles":pieces,
            "finite_angle_sum":finite_angle,"total_integer":int(total),
            "diagonal_character_trivial":True}


def multiplicative_reciprocity(q: int | F) -> dict:
    """|q|_infty product_p |q|_p = 1 in standard normalizations."""
    q=rational(q)
    vs=valuations(q)
    p_norms={p:F(p)**(-v) for p,v in vs.items()}
    finite_product=prod(p_norms.values(),start=F(1))
    arch=abs(q)
    if arch*finite_product!=1:
        raise AssertionError("Normalized Q product formula failed")
    return {"q":q,"valuations":vs,"padic_norms":p_norms,
            "finite_norm_product":finite_product,"arch_norm":arch,
            "global_product":arch*finite_product}


def modulo_padic_integral(q: int | F, p: int, precision: int) -> int:
    """Residue q mod p^precision when q is in Z_p.

    Cannot call this for a rational with negative p-valuation: Q_p/p^kZ_p
    is an additive quotient, NOT a ring quotient on unrestricted Q_p.
    """
    q=rational(q)
    if not prime(p) or type(precision) is not int or precision<1:
        raise DiagonalSourceError("Finite prime/place precision must be positive")
    if q and valuation(q,p)<0:
        raise DiagonalSourceError("Non-p-integral q has no Z_p ring residue")
    m=p**precision
    return (q.numerator*pow(q.denominator,-1,m))%m


def finite_places_observe(q: int | F, precision: Mapping[int,int]) -> dict[int,int]:
    return {p:modulo_padic_integral(q,p,k) for p,k in sorted(precision.items())}


def padic_precision_equal(a: int | F,b: int | F,p:int,k:int)->bool:
    if not prime(p) or type(k) is not int:
        raise DiagonalSourceError("Authentic prime and integer valuation threshold required")
    d=rational(a)-rational(b)
    return d==0 or valuation(d,p)>=k


@dataclass(frozen=True)
class DiagonalCarrier:
    """One rational source, with two exact operations preserving all local maps."""
    address:F
    source_id:str="Q-diagonal"
    epoch:int=0

    def __post_init__(self):
        object.__setattr__(self,"address",rational(self.address))
        if not self.source_id or type(self.epoch) is not int or self.epoch<0:
            raise DiagonalSourceError("Source-id and nonnegative epoch required")

    def succ(self,increment:int|F)->"DiagonalCarrier":
        return DiagonalCarrier(self.address+rational(increment),self.source_id,self.epoch+1)

    def fucc(self,multiplier:int|F,*,require_prime:bool=False)->"DiagonalCarrier":
        m=rational(multiplier)
        if not m:
            raise DiagonalSourceError("Multiplier zero loses prime-jet information")
        if require_prime and (m.denominator!=1 or not prime(m.numerator)):
            raise DiagonalSourceError("Prime-FUCC requires authentic rational prime")
        return DiagonalCarrier(self.address*m,self.source_id,self.epoch+1)

    def source_circle(self)->F:
        """Global additive phase of rational address, represented mod 1."""
        return self.address%1

    def finite_circle(self)->F:
        """Finite-place sum of canonical local additive phases, mod 1."""
        return additive_reciprocity(self.address)["finite_angle_sum"]%1

    def commuting_square(self,increment:int|F,multiplier:int|F,precision:Mapping[int,int])->dict:
        """S_d V_m = V_m S_(d/m) if m!=0; or V_m S_d = S_(md) V_m.

        Check exact rational equality; finite reductions only if every produced
        address is p-integral for the requested prime clocks.
        """
        d,m=rational(increment),rational(multiplier)
        if m==0:
            raise DiagonalSourceError("No zero FUCC")
        lhs=self.succ(d).fucc(m)
        rhs=self.fucc(m).succ(m*d)
        if lhs.address!=rhs.address or lhs.source_id!=rhs.source_id:
            raise AssertionError("SUCC/FUCC covariance fails")
        views={p:modulo_padic_integral(lhs.address,p,k) for p,k in precision.items()}
        return {"law":"V_m o S_d = S_(m*d) o V_m",
                "common_address":lhs.address,"finite_views":views,
                "arch_address":lhs.address,"local_square_verified":True}


def bounded_height_injection(height:int,precision:Mapping[int,int],*,
                              certify_by_arch_gap:F|None=None)->dict:
    """Uniformly sound Q-diagonal separation for prime-integral height<=H.

    Let q=a/b and r=c/d with |a|,b,|c|,d<=H, b,d>0,
    both denominators units at every chosen prime.
    If q and r match to depth k_p then M=prod(p^k_p) divides ad-bc.
    If M>2H^2 they are equal. Alternatively if |q-r|<=epsilon and
    M>epsilon*H^2, equality follows.
    """
    if type(height) is not int or height<1 or not precision:
        raise DiagonalSourceError("Height>=1 and nonempty probe set required")
    ps=[]
    for p,k in precision.items():
        if not prime(p) or type(k) is not int or k<1:
            raise DiagonalSourceError("No composite or invalid precision")
        ps.append((p,k))
    m=prod(p**k for p,k in ps)
    cutoff=F(2*height**2) if certify_by_arch_gap is None else rational(certify_by_arch_gap)*height**2
    if cutoff<0:
        raise DiagonalSourceError("Archimedean separation tolerance must be nonnegative")
    return {"height":height,"modulus":m,"modulus_cutoff":cutoff,
            "injective":m>cutoff,"primes":tuple(sorted(ps)),
            "assumptions":"height-bound, P-integral denominators, equality at each p clock"
            +(" and arch gap bound" if certify_by_arch_gap is not None else "")}


def height_limited_source(height:int,precision:Mapping[int,int])->dict:
    """Independent exhaustive small-source audit against the uniform theorem."""
    if height>20:
        raise DiagonalSourceError("Exhaustive source enumeration capped at H<=20")
    formula=bounded_height_injection(height,precision)
    vals=tuple(sorted({F(a,b) for a in range(-height,height+1)
                      for b in range(1,height+1) if all(b%p for p in precision)}))
    signatures={}
    collisions=[]
    for q in vals:
        key=tuple(sorted(finite_places_observe(q,precision).items()))
        if key in signatures and signatures[key]!=q:
            collisions.append((signatures[key],q))
        else:
            signatures[key]=q
    if formula["injective"] and collisions:
        raise AssertionError("Strong approximation certificate has collision")
    return {"states":len(vals),"modulus":formula["modulus"],
            "provably_injective":formula["injective"],
            "observed_collisions":len(collisions),"collision_witness":collisions[:1]}


def no_height_limit_alias(primes:Mapping[int,int],attempt:int)->dict:
    """Produce q!=0 tiny in R and zero in all chosen p clock reductions.

    Set M=prod p^k and q=M/(M*N+1). Denom coprime to every chosen p;
    p-adic q is 0 mod p^k, while |q|_inf tends to zero as N grows.
    """
    if type(attempt) is not int or attempt<1:
        raise DiagonalSourceError("Attempt>=1 required")
    if not primes:
        raise DiagonalSourceError("Select genuine finite clocks")
    bound=bounded_height_injection(1,primes)
    m=bound["modulus"]
    q=F(m,m*attempt+1)
    if not all(modulo_padic_integral(q,p,k)==0 for p,k in primes.items()):
        raise AssertionError("Countermodel failed its p-clock aliases")
    norm=multiplicative_reciprocity(q)
    selected=prod((norm["padic_norms"].get(p,F(1)) for p in primes),start=F(1))
    outside=prod((v for p,v in norm["padic_norms"].items() if p not in primes),start=F(1))
    if selected!=F(1,m) or outside!=m*attempt+1:
        raise AssertionError("Missing-place compensation failed")
    return {"nonzero":q,"all_selected_prime_views_zero":True,
            "arch_abs":abs(q),"arch_upper_bound":F(1,attempt),
            "measured_prime_norm_product":selected,
            "unobserved_prime_norm_compensation":outside,
            "full_global_norm_product":norm["global_product"],
            "missing_resource":"uniform bounded height or bounded denominator"}


def local_euler_factor(p:int,s:int)->F:
    """Exact local unramified Euler factor at positive integral s."""
    if not prime(p) or type(s) is not int or s<1:
        raise DiagonalSourceError("Authentic rational prime and integral s>=1 required")
    return 1/(1-F(1,p**s))


def local_euler_product(prime_cutoff:int,s:int)->dict:
    """All primes <=cutoff and exact product; no claim of continuation."""
    if type(prime_cutoff) is not int or prime_cutoff<2 or type(s) is not int or s<2:
        raise DiagonalSourceError("Absolute convergence proof only uses integer s>=2")
    places=tuple(p for p in range(2,prime_cutoff+1) if prime(p))
    local={p:local_euler_factor(p,s) for p in places}
    partial=prod(local.values(),start=F(1))
    # For s>=2, each factor p^-s <= p^-2, and omitted primes are
    # a subset of positive integers n>cutoff. The exact telescope
    # product_{n>cutoff}(1-n^-2)^-1=(cutoff+1)/cutoff.
    upper=partial*F(prime_cutoff+1,prime_cutoff)
    return {"prime_cutoff":prime_cutoff,"s":s,"prime_places":places,
            "local_factors":local,"lower":partial,"upper":upper,
            "tail_multiplier":F(prime_cutoff+1,prime_cutoff),
            "tail_proof":"prime subset of integers and telescoping at s=2"}


def validate_euler_places(prime_cutoff:int,places:Sequence[int],s:int)->F:
    needed=tuple(p for p in range(2,prime_cutoff+1) if prime(p))
    if tuple(places)!=needed:
        raise DiagonalSourceError("Fake, missing, duplicated or reordered Euler places")
    return prod((local_euler_factor(p,s) for p in places),start=F(1))


def finite_place_joint_limit_escape(selected_primes:Sequence[int],level:int)->dict:
    """Diagonally nonzero q_n->0 in R x product_{p in P} Q_p, P FINITE.

    Let M_n=prod_{p in P}p^n, q_n=M_n/(M_n^2+1). The denominator
    is a p-unit for selected places, hence v_p(q_n)=n. Real q_n<1/M_n.
    Norm product forces exactly M_n^2+1 compensation at UNOBSERVED
    places. This does not converge to 0 in the FULL restricted adele ring;
    the image of Q in the full adeles is discrete.
    """
    places=tuple(selected_primes)
    if not places or len(set(places))!=len(places) or any(not prime(p) for p in places):
        raise DiagonalSourceError("Distinct genuine selected prime places required")
    if type(level) is not int or level<1:
        raise DiagonalSourceError("Finite positive convergence depth required")
    modulus=prod(p**level for p in places)
    denominator=modulus*modulus+1
    address=F(modulus,denominator)
    norm=multiplicative_reciprocity(address)
    for p in places:
        if valuation(address,p)!=level or modulo_padic_integral(address,p,level)!=0:
            raise AssertionError("Selected p-adic sequence does not converge")
    missing=prod((v for p,v in norm['padic_norms'].items() if p not in places),start=F(1))
    if missing!=denominator:
        raise AssertionError("Unobserved prime compensation missing")
    return {'selected_primes':places,'level':level,'diagonal_rational':address,
            'real_abs':abs(address),'real_upper_bound':F(1,modulus),
            'selected_prime_norms':{p:F(1,p**level) for p in places},
            'all_selected_clocks_read_zero':True,
            'outside_prime_norm_product':missing,
            'full_product_formula':norm['global_product'],
            'converges_in_finite_product':True,
            'converges_to_zero_in_full_adeles':False}
