"""Portable arithmetic sundial: two independent SUCC units, one rational report.

Elementary exact arithmetic (not a physical clock). Frames (a,b;u,v) retain
the original numerator/denominator and both integer step units. The ratio
alone is not a sufficient state for future SUCC dynamics. The determinant
D=u*b-v*a controls real drift and diagonal integer cancellation. Prime
clocks are actual congruences, with explicit nonunit obstructions.

Declared source/basis strings do NOT authenticate a physical source.
Nothing here establishes ABC, RH or signed completed-Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, prod, lcm

from .rad_ris_transport import rad, ris, is_prime, prime_powers, MAX_INTEGER


class SundialContractError(ValueError):
    """An original-source, unit, prime, or runtime contract is invalid."""


def _nn(n: int, name: str) -> int:
    if type(n) is not int or n < 0:
        raise SundialContractError(f"{name} must be a nonnegative integer")
    return n


def _pos(n: int, name: str) -> int:
    if type(n) is not int or n <= 0:
        raise SundialContractError(f"{name} must be a positive integer")
    return n


def _modulus(p: int, depth: int) -> int:
    if type(p) is not int or not is_prime(p):
        raise SundialContractError("a genuine prime modulus is required")
    if type(depth) is not int or not 1 <= depth <= 12:
        raise SundialContractError("depth must be 1..12")
    m = p ** depth
    if m > 2_000_000:
        raise SundialContractError("finite clock budget exceeded")
    return m


def _vp(n: int, p: int) -> int:
    _pos(n, "unit")
    r = 0
    while n % p == 0:
        n //= p
        r += 1
    return r


def _arm_clock(a: int, u: int, p: int, depth: int) -> tuple[int, int] | None:
    """Solve a+nu=0 modulo p^depth, including noninvertible units.

    Set t=min(depth,v_p(u)). Solvable iff p^t|a; solution then is
    one residue class modulo p^(depth-t). Modulus 1 means every n.
    """
    t = min(depth, _vp(u, p))
    scale = p ** t
    if a % scale:
        return None
    m = p ** (depth-t)
    if m == 1:
        return (0, 1)
    return ((-(a // scale) * pow(u // scale, -1, m)) % m, m)


def _intersect(a: tuple[int,int] | None, b: tuple[int,int] | None
               ) -> tuple[int,int] | None:
    if a is None or b is None:
        return None
    if (a[0]-b[0]) % gcd(a[1],b[1]):
        return None
    return a if a[1] >= b[1] else b


@dataclass(frozen=True)
class PrimeSundialReading:
    prime: int
    depth: int
    modulus: int
    numerator_class: tuple[int,int] | None
    denominator_class: tuple[int,int] | None
    diagonal_class: tuple[int,int] | None
    independent_grid_count: int
    diagonal_count: int
    relative_phase: int | None
    original_source: str
    unit_basis: str
    source_authenticated: bool = False


@dataclass(frozen=True)
class PortablePhaseWheel:
    prime_depths: tuple[tuple[int,int], ...]
    wheel: int
    phase_offset: int
    numerator_zero_time: int
    denominator_zero_time: int
    simultaneous_k: int
    simultaneous_l: int
    original_source: str
    unit_basis: str
    source_authenticated: bool = False


@dataclass(frozen=True)
class CRTSundialReceipt:
    offset: int
    prime_depths: tuple[tuple[int,int], ...]
    possible: bool
    class_modulus: int | None
    residue: int | None
    first_nonnegative_k: int | None
    first_nonnegative_l: int | None
    aligned_modulus: int
    original_source: str
    source_authenticated: bool = False


@dataclass(frozen=True)
class SundialThreeShadows:
    """Three mathematical rational probes; no physical probe access asserted.

    (0,0), (1,0), (0,1) determine normalized (a/b,u/b,v/b).
    """
    origin: Fraction
    numerator_step: Fraction
    denominator_step: Fraction
    normalized_a: Fraction
    normalized_u: Fraction
    normalized_v: Fraction
    original_source: str
    source_authenticated: bool = False
    counterfactual_probes_authorized: bool = False


@dataclass(frozen=True)
class BirthReading:
    arm: str
    original_radical: int
    original_residual: int
    residual_step: int
    new_prime_support: tuple[int,...]
    prime_birth_product: int
    actual_radical: int
    actual_residual: int


@dataclass(frozen=True)
class PortablePrimeSundial:
    """A source-indexed two-dimensional SUCC frame, a,b,u,v positive.

    Independent steps are (k,l) in N^2. Diagonal k=l=n is a CHOICE OF
    PATH, not the only lawful succession and not a physical time claim.
    """
    a: int
    b: int
    u: int
    v: int
    original_source: str
    unit_basis: str

    def __post_init__(self) -> None:
        for name in ("a","b","u","v"):
            _pos(getattr(self,name),name)
        for name in ("original_source","unit_basis"):
            if not isinstance(getattr(self,name),str) or not getattr(self,name):
                raise SundialContractError("nonempty source and unit-basis labels required")

    @classmethod
    def rad_anchored(cls, a: int, b: int, original_source: str,
                     unit_basis: str = "RAD-anchored numerator/denominator"
                     ) -> PortablePrimeSundial:
        if _pos(a,"a") > MAX_INTEGER or _pos(b,"b") > MAX_INTEGER:
            raise SundialContractError("RAD anchor exceeds bounded factorization")
        return cls(a,b,rad(a),rad(b),original_source,unit_basis)

    def arms(self,k:int,l:int)->tuple[int,int]:
        return self.a+_nn(k,"k")*self.u, self.b+_nn(l,"l")*self.v

    def ratio(self,k:int,l:int)->Fraction:
        A,B=self.arms(k,l)
        return Fraction(A,B)

    def determinant(self)->int:
        return self.u*self.b-self.v*self.a

    def wedge(self,k:int,l:int)->int:
        A,B=self.arms(k,l)
        return self.u*B-self.v*A

    def clock_origins(self)->tuple[Fraction,Fraction]:
        return Fraction(self.a,self.u),Fraction(self.b,self.v)

    def offset_phase(self)->Fraction:
        return Fraction(self.a,self.u)-Fraction(self.b,self.v)

    def diagonal_gcd(self,n:int)->int:
        return gcd(*self.arms(n,n))

    def diagonal_difference(self,n:int)->Fraction:
        B=self.arms(n,n)[1]
        return Fraction(self.determinant(),B*(B+self.v))

    def diagonal_stationary_error(self,n:int)->Fraction:
        B=self.arms(n,n)[1]
        return Fraction(-self.determinant(),self.v*B)

    def cross_mixed_difference(self,k:int,l:int)->Fraction:
        B=self.arms(k,l)[1]
        return Fraction(-self.u*self.v,B*(B+self.v))

    def diagonal_gcd_certificate(self,n:int)->dict:
        A,B=self.arms(n,n)
        D=self.determinant()
        g=gcd(A,B)
        return {"n":n,"A":A,"B":B,"D":D,"gcd":g,
                "gcd_divides_D":D%g==0,
                "bounded_by_abs_D_if_nonzero":D==0 or g<=abs(D),
                "ratio":str(Fraction(A,B))}

    def homogeneous_scale(self,m:int)->PortablePrimeSundial:
        """Scale ALL four coordinates; ratio/phase preserved, raw p-valuations not."""
        m=_pos(m,"homogeneous scale")
        return PortablePrimeSundial(m*self.a,m*self.b,m*self.u,m*self.v,
                                   self.original_source,self.unit_basis)

    def rebase(self,h:int,j:int)->PortablePrimeSundial:
        """New coordinate origins; clock phase transforms by +h-j."""
        A,B=self.arms(h,j)
        return PortablePrimeSundial(A,B,self.u,self.v,
                                   self.original_source,self.unit_basis)

    def three_shadows(self) -> SundialThreeShadows:
        """Recover complete projective source data from three ratio probes.

        These are mathematical counterfactual reports, not an authorization
        to reset a destructive original carrier or observe three branches.
        """
        q00,q10,q01=self.ratio(0,0),self.ratio(1,0),self.ratio(0,1)
        x=q00
        mu=q10-q00
        nu=q00/q01-1
        assert x==Fraction(self.a,self.b)
        assert mu==Fraction(self.u,self.b)
        assert nu==Fraction(self.v,self.b)
        return SundialThreeShadows(q00,q10,q01,x,mu,nu,self.original_source)

    @classmethod
    def reconstruct_three_shadows(cls,q00:Fraction,q10:Fraction,q01:Fraction,
                                  original_source:str,unit_basis:str
                                  )->PortablePrimeSundial:
        """Choose the *minimal integer projective representative*, not source.

        The rational dynamics are identical, but absolute source scale,
        common divisors and p-adic occupations are NOT recovered.
        """
        if any(type(q) is not Fraction for q in (q00,q10,q01)):
            raise SundialContractError("three ratio measurements must be exact Fractions")
        if q00<=0 or q10<=q00 or q01<=0 or q01>=q00:
            raise SundialContractError("three shadows must have positive SUCC units")
        x,mu,nu=q00,q10-q00,q00/q01-1
        B=lcm(x.denominator,mu.denominator,nu.denominator)
        A,U,V=x*B,mu*B,nu*B
        assert A.denominator==U.denominator==V.denominator==1
        frame=cls(int(A),B,int(U),int(V),original_source,unit_basis)
        assert gcd(gcd(frame.a,frame.b),gcd(frame.u,frame.v))==1
        assert frame.ratio(0,0)==q00
        assert frame.ratio(1,0)==q10
        assert frame.ratio(0,1)==q01
        return frame

    def projectively_equal(self,other:PortablePrimeSundial)->bool:
        """All ratio reports on N^2 coincide iff full frames are homothetic."""
        if not isinstance(other,PortablePrimeSundial):
            raise SundialContractError("comparison requires a full rational source frame")
        return (Fraction(self.a,self.b),Fraction(self.u,self.b),
                Fraction(self.v,self.b))==(
                Fraction(other.a,other.b),Fraction(other.u,other.b),
                Fraction(other.v,other.b))

    def prime_clock(self,p:int,depth:int=1,offset:int=0)->PrimeSundialReading:
        """Class of n with p^depth dividing A_n and B_(n+offset).

        If either unit is a nonunit mod p^depth, returns partial-clock
        congruence or None; NEVER invents an inverse. Relative phase
        exists only when both units are invertible.
        """
        M=_modulus(p,depth)
        if type(offset) is not int:
            raise SundialContractError("signed offset must be an exact integer")
        ra=_arm_clock(self.a,self.u,p,depth)
        rb=_arm_clock(self.b+offset*self.v,self.v,p,depth)
        both=_intersect(ra,rb)
        grid=0 if ra is None or rb is None else (M//ra[1])*(M//rb[1])
        count=0 if both is None else M//both[1]
        phase=None
        if gcd(self.u*self.v,M)==1:
            ka=(-self.a*pow(self.u,-1,M))%M
            lb=(-self.b*pow(self.v,-1,M))%M
            phase=(lb-ka)%M
            ph=self.offset_phase()
            assert phase==(ph.numerator*pow(ph.denominator,-1,M))%M
            if offset==0:
                assert (both is not None)==(self.determinant()%M==0)
        return PrimeSundialReading(p,depth,M,ra,rb,both,grid,count,phase,
                                   self.original_source,self.unit_basis)

    def phase_wheel(self,prime_depths:tuple[tuple[int,int],...])->PortablePhaseWheel:
        """CRT compression of all invertible prime-power origin differences."""
        if type(prime_depths) is not tuple or not prime_depths:
            raise SundialContractError("nonempty prime-clock tuple required")
        ps=tuple(p for p,_ in prime_depths)
        if ps != tuple(sorted(set(ps))):
            raise SundialContractError("distinct increasing prime clocks required")
        W=1
        for p,r in prime_depths:
            if type(p) is not int or type(r) is not int:
                raise SundialContractError("exact prime-depth pairs required")
            W*=_modulus(p,r)
        if W>2_000_000:
            raise SundialContractError("combined finite wheel budget exceeded")
        if gcd(self.u*self.v,W)!=1:
            raise SundialContractError("both units must be invertible modulo W")
        k=(-self.a*pow(self.u,-1,W))%W
        l=(-self.b*pow(self.v,-1,W))%W
        phase=(l-k)%W
        assert phase==(-self.determinant()*pow(self.u*self.v,-1,W))%W
        assert all(self.prime_clock(p,r).relative_phase==phase%(p**r)
                   for p,r in prime_depths)
        actual_k=k
        actual_l=k+phase
        A,B=self.arms(actual_k,actual_l)
        assert A%W==B%W==0 and actual_l%W==l
        return PortablePhaseWheel(prime_depths,W,phase,k,l,actual_k,actual_l,
                                  self.original_source,self.unit_basis)

    def crt_synchronize(self,prime_depths:tuple[tuple[int,int],...],
                        offset:int=0)->CRTSundialReceipt:
        """Construct a nonnegative diagonal/offset n across finitely many primes."""
        if type(prime_depths) is not tuple or not prime_depths:
            raise SundialContractError("nonempty prime-clock tuple required")
        if type(offset) is not int:
            raise SundialContractError("signed offset must be an exact integer")
        ps=tuple(p for p,_ in prime_depths)
        if ps!=tuple(sorted(set(ps))):
            raise SundialContractError("distinct increasing prime clocks required")
        W=1
        for p,r in prime_depths:
            if type(p) is not int or type(r) is not int:
                raise SundialContractError("exact prime-depth pair required")
            W*=_modulus(p,r)
        if W>2_000_000:
            raise SundialContractError("combined finite CRT budget exceeded")
        residue,period=0,1
        for p,r in prime_depths:
            c=self.prime_clock(p,r,offset).diagonal_class
            if c is None:
                return CRTSundialReceipt(offset,prime_depths,False,None,None,
                                         None,None,W,self.original_source)
            root,m=c
            if m>1:
                step=((root-residue)*pow(period,-1,m))%m
                residue=(residue+period*step)%(period*m)
                period*=m
        lower=max(0,-offset)
        n=residue if residue>=lower else residue+((lower-residue+period-1)//period)*period
        A,B=self.arms(n,n+offset)
        assert all(A%(p**r)==B%(p**r)==0 for p,r in prime_depths)
        return CRTSundialReceipt(offset,prime_depths,True,period,residue,
                                 n,n+offset,W,self.original_source)

    def rad_births(self,k:int,l:int)->tuple[BirthReading,BirthReading]:
        """Track prime births under RAD-anchored units without freezing RAD."""
        if self.a>MAX_INTEGER or self.b>MAX_INTEGER:
            raise SundialContractError("RAD original exceeds factorization budget")
        if self.u!=rad(self.a) or self.v!=rad(self.b):
            raise SundialContractError("RAD birth theorem requires RAD anchor")
        A,B=self.arms(k,l)
        if max(A,B)>MAX_INTEGER:
            raise SundialContractError("RAD endpoint exceeds factorization budget")
        ans=[]
        for arm,original,unit,step,value in (
            ("numerator",self.a,self.u,k,A),("denominator",self.b,self.v,l,B)):
            m=ris(original)+step
            births=tuple(p for p,_ in prime_powers(m) if unit%p)
            J=prod(births)
            newrad=unit*J
            newris=m//J
            assert newrad*newris==value
            assert newrad==rad(value) and newris==ris(value)
            ans.append(BirthReading(arm,unit,ris(original),m,births,J,newrad,newris))
        return ans[0],ans[1]

    def invertible_determinant_part(self)->tuple[int,int]:
        """Largest prime-to-u*v divisor M of |D| is simultaneously attainable."""
        D=abs(self.determinant())
        if D==0:
            raise SundialContractError("zero determinant has no finite gcd bound")
        M=D
        while (g:=gcd(M,self.u*self.v))>1:
            M//=g
        k=0 if M==1 else (-self.a*pow(self.u,-1,M))%M
        assert self.diagonal_gcd(k)%M==0
        return M,k

    def stationary_gcd_rule(self,n:int)->tuple[int,int]:
        """D=0: gcd(A_n,B_n)=t+n*gcd(u,v), with u'=u/g,v'=v/g."""
        _nn(n,"n")
        if self.determinant()!=0:
            raise SundialContractError("stationary gcd requires zero determinant")
        g=gcd(self.u,self.v)
        u1,v1=self.u//g,self.v//g
        assert self.a%u1==0 and self.b%v1==0
        t=self.a//u1
        assert self.b==v1*t
        ans=t+n*g
        assert self.diagonal_gcd(n)==ans
        return ans,g


def representation_alias_pair()->tuple[PortablePrimeSundial,PortablePrimeSundial]:
    """1/2=2/4 but the unit-one SUCC futures are 2/3 and 3/5."""
    return (PortablePrimeSundial(1,2,1,1,"two declared charts","unit=1"),
            PortablePrimeSundial(2,4,1,1,"two declared charts","unit=1"))
