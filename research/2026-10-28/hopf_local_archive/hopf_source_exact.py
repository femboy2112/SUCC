"""Pure-Fraction quaternionic Hopf observables of SUCC's genuine chiral BBP source.

LOCAL RESEARCH, not a replacement for any SUCC source module.  Source facts
are tied to femboy2112/SUCC PR #333@a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5,
main@6dd80730c3575d91f746546a25da5aedbd2e2737.

The original carrier K ⊕ K is coordinatewise multiplicative.  Embedding its
four rational coordinates in the Hamilton quaternions is an additive/Q-linear
IDENTIFICATION ONLY, NOT a ring map or a quaternionic SUCC axiom.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable

SOURCE_ID = "original-signed-four-pole-BBP-rank2-chiral-PR333-a0e4bfd9"


def _q(a: object) -> F:
    return F(a)


@dataclass(frozen=True)
class H:
    """Hamilton rational quaternion a+bi+cj+dk; right/left order matters."""
    a: F = F(0)
    b: F = F(0)
    c: F = F(0)
    d: F = F(0)

    def __post_init__(self) -> None:
        for key in ("a", "b", "c", "d"):
            object.__setattr__(self, key, F(getattr(self, key)))

    def __iter__(self):
        return iter((self.a, self.b, self.c, self.d))

    def __add__(self, other: H) -> H:
        if not isinstance(other, H): return NotImplemented
        return H(*(x+y for x,y in zip(self,other)))

    def __neg__(self) -> H:
        return H(*(-x for x in self))

    def __sub__(self, other: H) -> H:
        return self + (-other)

    def __mul__(self, other: H) -> H:
        if not isinstance(other, H): return NotImplemented
        a,b,c,d=self
        e,f,g,h=other
        return H(a*e-b*f-c*g-d*h,
                 a*f+b*e+c*h-d*g,
                 a*g-b*h+c*e+d*f,
                 a*h+b*g-c*f+d*e)

    def scale(self, x: F) -> H:
        return H(*(F(x)*v for v in self))

    def conj(self) -> H:
        return H(self.a,-self.b,-self.c,-self.d)

    def norm2(self) -> F:
        return sum((x*x for x in self),F(0))

    def inverse(self) -> H:
        n=self.norm2()
        if not n: raise ZeroDivisionError("quaternion zero has no inverse")
        return self.conj().scale(F(1)/n)


ONE = H(1)
ZERO = H()
I = H(0,1)
J = H(0,0,1)
K = H(0,0,0,1)


@dataclass(frozen=True)
class Sphere4:
    R: H
    B: F

    def __post_init__(self):
        object.__setattr__(self, "B", F(self.B))
        if self.R.norm2()+self.B*self.B != 1:
            raise ValueError("not an exact point of the unit S^4")

    def as_rational5(self) -> tuple[F,...]:
        return tuple(self.R)+(self.B,)


def hopf(q1: H, q2: H) -> Sphere4:
    """Hopf invariant of a nonzero pair, using (2 q1 conjugate(q2), n1-n2)."""
    if not isinstance(q1,H) or not isinstance(q2,H):
        raise TypeError("requires exactly two H vectors")
    den=q1.norm2()+q2.norm2()
    if not den: raise ValueError("(0,0) cannot be Hopf-normalized")
    return Sphere4((q1*q2.conj()).scale(F(2,1)/den),
                   (q1.norm2()-q2.norm2())/den)


def hopf_decode_given_q2(p: Sphere4,q2: H) -> H:
    """From chosen source gauge q2 ≠ 0: q1=R q2/(1-B)."""
    if q2.norm2()==0 or p.B==1:
        raise ValueError("source-anchored decoder needs nonzero q2")
    return (p.R*q2).scale(F(1)/(1-p.B))



# The actual odd chiral successor is an orientation-reversing quaternion
# similarity, transporting RIGHT Hopf fibers to LEFT Hopf fibers.  This is
# a two-chart / handedness-labelled observation, not one fixed S4 chart.
LEFT_FACTOR = I+K
RIGHT_FACTOR = (ONE-I-J-K).scale(F(1,4))


def t_odd_quaternion_factor(q: H) -> H:
    """T(q)=(i+k) conjugate(q) (1-i-j-k)/4, exactly over Q."""
    return LEFT_FACTOR*q.conj()*RIGHT_FACTOR


def hopf_left(q1: H,q2: H) -> Sphere4:
    """LEFT Sp(1) quotient: relative quaternion 2 conjugate(q2) q1 / D."""
    den=q1.norm2()+q2.norm2()
    if not den: raise ValueError("(0,0) cannot be Hopf-normalized")
    return Sphere4((q2.conj()*q1).scale(F(2)/den),
                   (q1.norm2()-q2.norm2())/den)


def hopf_right_to_left_odd(p: Sphere4) -> Sphere4:
    """Odd SUCC moves from right-gauge S4_R to left-gauge S4_L."""
    r=RIGHT_FACTOR
    return Sphere4(r.inverse()*p.R.conj()*r,p.B)


def hopf_left_to_right_odd(p: Sphere4) -> Sphere4:
    """Next odd SUCC moves from left-gauge S4_L to right-gauge S4_R."""
    l=LEFT_FACTOR
    return Sphere4(l*p.R.conj()*l.inverse(),p.B)


def hopf_two_step_base(p: Sphere4) -> Sphere4:
    """The genuine T^2 action descends: R -> (1-k)R(1+k)/2, B fixed."""
    return Sphere4(((ONE-K)*p.R*(ONE+K)).scale(F(1,2)),p.B)

# Q-linear chiral rank-two source successor from PR #333, in coordinates
# (Re z, Im z, Re w, Im w) and embedding (z,w) -> z+w j.
T = (
    (F(1,2),F(0),  F(0), F(1,2)),
    (F(1,2),F(0),  F(0),F(-1,2)),
    (F(0),F(-1,2),F(1,2),F(0)),
    (F(0),F(-1,2),F(-1,2),F(0)),
)


def t_step(x: H) -> H:
    values=tuple(x)
    return H(*(sum((row[j]*values[j] for j in range(4)),F(0)) for row in T))


def t_iter(x: H,n: int) -> H:
    if type(n) is not int or n<0 or n>10000:
        raise ValueError("nonnegative bounded iteration count required")
    for _ in range(n): x=t_step(x)
    return x


def j_chirality(x: H) -> H:
    """PR333 J(z,w)=(conj(w),conj(z)), NOT quaternion right j."""
    return H(x.c,-x.d,x.a,-x.b)


def t2_quaternion_factor(x: H) -> H:
    """Exact source factor: T² x=(1-k) x (1+i)/4."""
    return ((ONE-K)*x*(ONE+I)).scale(F(1,4))


def t_power_matrix(m: int) -> tuple[tuple[F,...],...]:
    if not 0<=m<=128: raise ValueError("m outside test horizon")
    mat=tuple(tuple(F(int(i==j)) for j in range(4)) for i in range(4))
    for _ in range(m):
        mat=tuple(tuple(sum((T[i][r]*mat[r][j] for r in range(4)),F(0))
                        for j in range(4)) for i in range(4))
    return mat


SOURCE_ORIGIN = H(2)
ORIGINAL_TAPS = (F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0))
CHIRAL_EVEN_TAPS = (F(4),F(2),F(0),F(-1),F(-1),F(-1,2),F(0),F(1,4))
CHIRAL_ODD_TAPS = (F(0),F(-2),F(0),F(-1),F(0),F(-1,2),F(0),F(-1,4))


def chiral_readouts(x: H) -> tuple[F,F]:
    even=2*(x.a+x.c)
    odd=-2*(x.b+x.d)
    return even,odd


def source_tap(x: H) -> F:
    ev,odd=chiral_readouts(x)
    return ev+odd


def source_moment(n: int, lane: str="total") -> F:
    if type(n) is not int or not 1<=n<=100000:
        raise ValueError("positive source time required")
    if lane=="total":tap=ORIGINAL_TAPS
    elif lane=="even":tap=CHIRAL_EVEN_TAPS
    elif lane=="odd":tap=CHIRAL_ODD_TAPS
    else:raise ValueError("unknown authentic channel")
    return sum((c/F(8*(n-1)+j+1) for j,c in enumerate(tap)),F(0))


def pole_quaternion(n: int) -> H:
    """Exactly four SIGNED, source-authenticated BBP partial fractions."""
    if type(n) is not int or n<1: raise ValueError("source begins at n=1")
    return H(F(4,8*n-7),F(-2,8*n-4),F(-1,8*n-3),F(-1,8*n-2))


def original_forcing(n: int) -> F:
    return sum(tuple(pole_quaternion(n)),F(0))


def original_numerator_denominator(n: int) -> F:
    return F(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def unwrapped_zero_seed(n: int, seed: F=F(0), lane: str="total") -> F:
    if type(n) is not int or not 0<=n<=256:
        raise ValueError("n outside declared real zero-seed verification horizon")
    state=F(seed)
    for t in range(1,n+1):
        state=16*state+source_moment(t,lane)
    return state


def paired_unwrapped_zero_seed(n: int) -> tuple[F,F,F]:
    up=unwrapped_zero_seed(n,lane="even")
    down=unwrapped_zero_seed(n,lane="odd")
    return up,down,up+down


def consecutive_hopf(n: int) -> Sphere4:
    x=t_iter(SOURCE_ORIGIN,n)
    return hopf(x,t_step(x))


def source_sphere_chart(x: H) -> Sphere4:
    """Gauge-fixed, LOSSLESS inverse-stereographic chart, q2=1."""
    return hopf(x,ONE)


def source_chart_next(p: Sphere4) -> Sphere4:
    """A sphere homeomorphism with north fixed. Not the naive pairwise action."""
    if p.B==1: return Sphere4(ZERO,F(1))
    return source_sphere_chart(t_step(hopf_decode_given_q2(p,ONE)))


def source_chart_latitude_next(B: F) -> F:
    """B = (||x||²-1)/(||x||²+1); T halves ||x||²."""
    B=F(B)
    if not -1<=B<=1: raise ValueError("latitude not in S4")
    return (3*B-1)/(3-B)


def source_labelled_mixed_hopf(n: int) -> Sphere4:
    """Compare genuine signed pole quartet at n with genuine chiral T^(n-1)b."""
    if type(n) is not int or not 1<=n<=256:
        raise ValueError("finite original source index required")
    return hopf(pole_quaternion(n),t_iter(SOURCE_ORIGIN,n-1))


def source_labelled_decode_poles(n: int,p: Sphere4) -> H:
    """The Hopf point ALONE does not invert: authenticated q2(n) is needed."""
    if type(n) is not int or not 1<=n<=256:
        raise ValueError("finite original source index required")
    return hopf_decode_given_q2(p,t_iter(SOURCE_ORIGIN,n-1))


def as_serializable(p: Sphere4) -> dict[str,object]:
    return {"R": [str(t) for t in p.R],"B":str(p.B)}


def coherent_changed_seed_tail_prefix(n: int,terms: int=32) -> F:
    """Finite rational preview of real coherent-seed trajectory -sum_k 16^-k r(n+k).

    The infinite limit is the U_n orbit from the alternative real seed
    U_0=-pi/16, using the original BBP identity.  The prefix is NOT the
    complete infinite tail and is never passed off as such.
    """
    if type(n) is not int or n<0 or type(terms) is not int or not 1<=terms<=128:
        raise ValueError("finite nonnegative index and 1..128 terms required")
    return -sum((source_moment(n+k)/F(16**k) for k in range(1,terms+1)), F(0))


def coherent_changed_seed_tail_bound(n: int) -> F:
    """Universal paper bound: |U_n(seed=-pi/16)| ≤ 8/[15 (n+1)^2].

    Proof: 0<r(j)≤8/j² for all j≥1, from the four-pole combined
    rational polynomial passport and termwise simple factor bounds.
    """
    if type(n) is not int or n<0: raise ValueError("nonnegative index")
    return F(8,15*(n+1)**2)
