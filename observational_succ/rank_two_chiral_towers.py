"""Exact rank-two Gaussian SUCC with source-faithful BBP transfer.

Pure Fraction Q(i) algebra. Independent coordinate multiplication is an
algebra law; the source successor is merely Q-linear, NOT a unital ring map.
The joint carrier has rank 2 over Q(i), rational dimension 4.
The signed BBP coefficients are readouts, NOT Weyl cancellation.

Mathematical proof and limitations:
  research/2026-10-27/BBP_RANK_TWO_CHIRAL_E_TOWERS.md
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache

SOURCE = "original-four-pole-BBP-chiral-rank2-source-v1"
TAPS = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1), Q(0), Q(0))


@dataclass(frozen=True)
class Gaussian:
    re: Q
    im: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "re", Q(self.re))
        object.__setattr__(self, "im", Q(self.im))

    def __add__(self, other: Gaussian) -> Gaussian:
        return Gaussian(self.re + other.re, self.im + other.im)

    def __neg__(self) -> Gaussian:
        return Gaussian(-self.re, -self.im)

    def __sub__(self, other: Gaussian) -> Gaussian:
        return self + (-other)

    def __mul__(self, other: Gaussian) -> Gaussian:
        if not isinstance(other, Gaussian):
            return NotImplemented
        return Gaussian(self.re * other.re - self.im * other.im,
                        self.re * other.im + self.im * other.re)

    def scale(self, value: Q) -> Gaussian:
        q = Q(value)
        return Gaussian(q * self.re, q * self.im)

    def conj(self) -> Gaussian:
        return Gaussian(self.re, -self.im)

    def norm(self) -> Q:
        return self.re * self.re + self.im * self.im


ZERO = Gaussian(0)
ONE = Gaussian(1)
G = Gaussian(Q(1, 2), Q(1, 2))
G_BAR = G.conj()


@dataclass(frozen=True)
class RankTwo:
    left: Gaussian
    right: Gaussian

    def __add__(self, other: RankTwo) -> RankTwo:
        return RankTwo(self.left + other.left, self.right + other.right)

    def __neg__(self) -> RankTwo:
        return RankTwo(-self.left, -self.right)

    def __sub__(self, other: RankTwo) -> RankTwo:
        return self + (-other)

    def scale(self, q: Q) -> RankTwo:
        return RankTwo(self.left.scale(q), self.right.scale(q))

    def multiply(self, other: RankTwo) -> RankTwo:
        """Independent, unital coordinate-wise carrier multiplication."""
        return RankTwo(self.left * other.left, self.right * other.right)


UNIT = RankTwo(ONE, ONE)
ORIGIN = RankTwo(Gaussian(2), ZERO)


def chirality(state: RankTwo) -> RankTwo:
    """J(z,w)=(conj(w),conj(z)), involutive Q-algebra automorphism."""
    return RankTwo(state.right.conj(), state.left.conj())


def split(state: RankTwo) -> tuple[RankTwo, RankTwo]:
    reflected = chirality(state)
    return ((state + reflected).scale(Q(1, 2)),
            (state - reflected).scale(Q(1, 2)))


def from_sectors(even_z: Gaussian, odd_z: Gaussian) -> RankTwo:
    """Even=(z,bar z), odd=(w,-bar w); reconstruct joint point."""
    return RankTwo(even_z + odd_z, even_z.conj() - odd_z.conj())


def independent_left(state: RankTwo) -> RankTwo:
    return RankTwo(G * state.left, state.right)


def independent_right(state: RankTwo) -> RankTwo:
    return RankTwo(state.left, G_BAR * state.right)


def paired_gain(state: RankTwo) -> RankTwo:
    return independent_right(independent_left(state))


def source_successor(state: RankTwo) -> RankTwo:
    """Q-linear coupled source: G on even, H(z)=g*conj(z) on odd."""
    even, odd = split(state)
    a, b = even.left, odd.left
    return from_sectors(G * a, G * b.conj())


def iterate(state: RankTwo, steps: int) -> RankTwo:
    if type(steps) is not int or not 0 <= steps <= 20000:
        raise ValueError("steps must be integer within declared finite budget")
    for _ in range(steps):
        state = source_successor(state)
    return state


def source_readout(state: RankTwo) -> Q:
    """Source-authentic readout 4*Re(even z)-4*Im(odd z)."""
    even, odd = split(state)
    return 4 * even.left.re - 4 * odd.left.im


def chiral_readouts(state: RankTwo) -> tuple[Q, Q]:
    even, odd = split(state)
    return 4 * even.left.re, -4 * odd.left.im


def impulse(index: int) -> Q:
    if type(index) is not int or index < 0:
        raise ValueError("nonnegative impulse index required")
    k, r = divmod(index, 8)
    return TAPS[r] / 16**k


def impulse_from_towers(index: int) -> Q:
    return source_readout(iterate(ORIGIN, index))


@lru_cache(maxsize=1)
def first_shell_channels() -> tuple[tuple[Q, ...], tuple[Q, ...]]:
    even, odd = [], []
    state = ORIGIN
    for _ in range(8):
        a, b = chiral_readouts(state)
        even.append(a)
        odd.append(b)
        state = source_successor(state)
    return tuple(even), tuple(odd)


def source_moment(n: int, *, channel: str = "total") -> Q:
    """Mellin moment of the first complete eight-step source shell."""
    if type(n) is not int or not 1 <= n <= 100_000:
        raise ValueError("positive finite moment time required")
    even, odd = first_shell_channels()
    if channel == "even": coeff = even
    elif channel == "odd": coeff = odd
    elif channel == "total": coeff = TAPS
    else: raise ValueError("channel must be total, even or odd")
    return sum((c / (8*(n-1)+j+1) for j, c in enumerate(coeff)), Q(0))


def authentic_four_poles(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("original source begins at n=1")
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def original_zero_seed_prefix(steps: int) -> Q:
    """Original unwrapped rational U_steps, not the shrinking linear impulse."""
    if type(steps) is not int or not 0 <= steps <= 256:
        raise ValueError("finite source prefix limit 256")
    state = Q(0)
    for n in range(1, steps + 1):
        state = 16*state + source_moment(n)
    return state


def source_8_shell_sums() -> tuple[Q, Q, Q]:
    even, odd = first_shell_channels()
    return sum(even, Q(0)), sum(odd, Q(0)), sum((j*TAPS[j] for j in range(8)), Q(0))


def polynomial_denominator() -> tuple[Q, ...]:
    """det(I-tG) det(I-tH), ascending polynomial coefficients."""
    a=(Q(1),Q(-1),Q(1,2))
    b=(Q(1),Q(0),Q(-1,2))
    res=[Q(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b): res[i+j]+=x*y
    return tuple(res)


def transfer_numerator_from_first_terms() -> tuple[Q, ...]:
    """D(t)*sum c_n t^n up to degree 4, a finite polynomial certificate."""
    d=polynomial_denominator()
    return tuple(sum((d[j]*TAPS[n-j] for j in range(n+1)),Q(0)) for n in range(5))


@dataclass(frozen=True)
class MacroEPoint:
    """One typed joint object, never inferred from separate marginal reports."""
    source: str
    time: int
    state: RankTwo

    @staticmethod
    def original() -> MacroEPoint:
        return MacroEPoint(SOURCE, 0, ORIGIN)

    def advance(self) -> MacroEPoint:
        if self.source != SOURCE or self.time < 0:
            raise ValueError("non-source-labelled point")
        return MacroEPoint(self.source, self.time + 1, source_successor(self.state))

    def views(self) -> tuple[Gaussian, Gaussian, Q, Gaussian]:
        """Independent carrier positions, exact source readout, product."""
        return (self.state.left, self.state.right,
                source_readout(self.state),
                self.state.left * self.state.right)


def validate_common_source_even(left: Gaussian, right: Gaussian) -> RankTwo:
    """Require an actual J-fixed joint state; no-ghost negative control."""
    if right != left.conj():
        raise ValueError("two marginal reports do not glue to the chiral graph")
    return RankTwo(left, right)


def conditional_binary_joint() -> dict[tuple[int,int], Q]:
    """Declared common-bit model: X,Y independent GIVEN B, correlated overall."""
    out = {(x,y): Q(0) for x in (0,1) for y in (0,1)}
    for b in (0,1):
        p = Q(1,4) if b==0 else Q(3,4)
        for x in (0,1):
            for y in (0,1):
                px=p if x else 1-p
                py=p if y else 1-p
                out[(x,y)] += Q(1,2)*px*py
    return out


def covariance_binary(joint: dict[tuple[int,int],Q]) -> Q:
    ex=sum((Q(x)*q for (x,y),q in joint.items()),Q(0))
    ey=sum((Q(y)*q for (x,y),q in joint.items()),Q(0))
    exy=sum((Q(x*y)*q for (x,y),q in joint.items()),Q(0))
    return exy-ex*ey


def signed_phase_no_go_bound_pi_units(h: int) -> Q:
    """For source taps c_n, |sum(e(h c_n)-1)|<=pi*this for any N.

    Sum |c_n|<=8*(16/15)=128/15. This proves normalized phases -> 1,
    NOT 0. Cannot substitute contracting source for the selected BBP U_n.
    """
    if type(h) is not int or not h:
        raise ValueError("nonzero integer phase frequency required")
    return Q(256*abs(h), 15)


def chiral_zero_seed_states(steps: int) -> tuple[Q, Q]:
    """Two independent rational SUCC recurrences on correlated source lanes.

    Each has its own U(0)=0 and U(n)=16U(n-1)+r_lane(n). The combined
    state equals the authentic zero-selected BBP U_n by exact arithmetic.
    """
    if type(steps) is not int or not 0 <= steps <= 256:
        raise ValueError("finite paired-source horizon 0..256")
    up, down = Q(0), Q(0)
    for n in range(1, steps+1):
        up = 16*up+source_moment(n,channel="even")
        down=16*down+source_moment(n,channel="odd")
    return up, down


def chiral_phase_remainders(steps: int, h: int=1) -> tuple[Q,Q,Q]:
    """Exact mod-1 phase product in additive Q/Z coordinates, not a
    claim that the two sequences are probabilistically independent.
    """
    if type(h) is not int or h==0:
        raise ValueError("nonzero integer real Fourier character required")
    up,down=chiral_zero_seed_states(steps)
    return (Q(h*up)%1,Q(h*down)%1,Q(h*(up+down))%1)


def shell_hankel_det() -> Q:
    """An independent exact 4x4 determinant of the source Hankel array."""
    mat=[[impulse(i+j) for j in range(4)] for i in range(4)]
    det=Q(1)
    for k in range(4):
        pivot=next((i for i in range(k,4) if mat[i][k]),None)
        if pivot is None: return Q(0)
        if pivot!=k:
            mat[k],mat[pivot]=mat[pivot],mat[k]
            det=-det
        entry=mat[k][k]
        det*=entry
        for j in range(k+1,4):
            factor=mat[j][k]/entry
            for col in range(k,4):
                mat[j][col]-=factor*mat[k][col]
    return det
