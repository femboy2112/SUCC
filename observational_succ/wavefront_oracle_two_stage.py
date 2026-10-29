"""Wavefront -> E1 -> E2, with exact Oily source-conditioned two-stage clocks.

All probabilities, transfer functions and recurrences are rational.  The
individual filter maps are deliberately PROPOSED observer transports whose
coefficients are extracted exactly from SUCC's authentic Oily packet source.
They are not an authenticated factor of the true expanding BBP phase orbit.

Source: PR #309/#310/#340 now present on main (2026-10-28).
  u(x)=x-x**2/2, v(x)=x**2/2,
  p_j(x)=(1-x)/4 * sum(u**k*v**(j-k), k=0..j).
No source import, frozen archive, or original BBP recurrence is altered.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


def _index(j: int, name: str = "index") -> int:
    if type(j) is not int or j < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return j


@dataclass(frozen=True)
class SourceGeometry:
    """Source-conditioned geometric loops. x=1 is their continuous limit."""
    x: Q

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", Q(self.x))
        if not Q(0) <= self.x <= Q(1):
            raise ValueError("source x must be in [0,1]")

    @property
    def u(self) -> Q:
        return self.x - self.x * self.x / 2

    @property
    def v(self) -> Q:
        return self.x * self.x / 2

    @property
    def normalization(self) -> Q:
        return (1 - self.u) * (1 - self.v)

    @property
    def discrim(self) -> Q:
        """(u-v)^2 = x^2(1-x)^2, exact pole collision at x=1."""
        return (self.u - self.v) ** 2

    def raw_grade(self, j: int) -> Q:
        """p_j, the genuine positive source packet. Zero at x=1."""
        _index(j, "grade")
        return (1 - self.x) / 4 * sum(
            (self.u ** k * self.v ** (j-k) for k in range(j+1)), Q(0)
        )

    def source_total(self) -> Q:
        """Sum of all raw grades, exact R(x), including R(1)=0."""
        return (1 - self.x) / (4 * self.normalization)

    def grade_probability(self, j: int) -> Q:
        """P_x(J=j)=p_j/R for x<1; analytic conditional limit for x=1."""
        _index(j, "grade")
        return self.normalization * sum(
            (self.u ** k * self.v ** (j-k) for k in range(j+1)), Q(0)
        )

    def mean_extra_delay(self) -> Q:
        """E[J], with J independent-geom sum for the declared observer model."""
        return self.u/(1-self.u) + self.v/(1-self.v)

    def variance_extra_delay(self) -> Q:
        return self.u/(1-self.u)**2 + self.v/(1-self.v)**2


def one_stage_prob(theta: Q, j: int) -> Q:
    """Causal geometric tail P(J=j)=(1-theta)*theta**j, 0<=theta<1."""
    theta = Q(theta)
    _index(j)
    if not Q(0) <= theta < Q(1):
        raise ValueError("requires 0<=theta<1")
    return (1-theta) * theta**j


def run_two_stages(signal: tuple[Q, ...] | list[Q], x: Q) -> tuple[tuple[Q,...],tuple[Q,...]]:
    """Each E_k(t) uses only the preceding stage's reports before t.

    At t<0, all signals and filters are zero.  The x=1 endpoint uses the
    limiting probability kernel, and is meaningful even though raw p_j(1)=0.
    """
    geometry = SourceGeometry(x)
    u,v = geometry.u,geometry.v
    w = tuple(Q(a) for a in signal)
    e1,e2=[],[]
    for t in range(len(w)):
        prev_e1 = e1[-1] if e1 else Q(0)
        prev_e2 = e2[-1] if e2 else Q(0)
        f1 = w[t-1] if t >= 1 else Q(0)
        next_e1 = u * prev_e1 + (1-u) * f1
        next_e2 = v * prev_e2 + (1-v) * prev_e1
        e1.append(next_e1)
        e2.append(next_e2)
    return tuple(e1),tuple(e2)


def recurrence_residual(signal: tuple[Q, ...] | list[Q], x: Q) -> tuple[Q,...]:
    """Exact second-order W->E2 differential residual at every t."""
    g=SourceGeometry(x)
    w=tuple(Q(v) for v in signal)
    _,e2=run_two_stages(w,x)
    def prev(arr,t):return arr[t] if 0<=t<len(arr) else Q(0)
    return tuple(
        e2[t]-(g.u+g.v)*prev(e2,t-1)+g.u*g.v*prev(e2,t-2)
        -g.normalization*prev(w,t-2)
        for t in range(len(w))
    )


def critical_grade(j: int) -> Q:
    """Exact Oily x=1 endpoint grade (j+1)/2**(j+2)."""
    _index(j,"grade")
    return Q(j+1, 2 ** (j+2))


def critical_rescaled_grade(j: int) -> int:
    """2**(j+2)*w_j=j+1 has second finite difference zero."""
    _index(j,"grade")
    return j+1


def critical_second_difference(j: int) -> int:
    """Forward Delta^2 in grade j; identically zero."""
    _index(j,"grade")
    return (critical_rescaled_grade(j+2)
            -2*critical_rescaled_grade(j+1)
            +critical_rescaled_grade(j))


def geometric_impulse_response(x: Q, t: int) -> Q:
    """Output E2(t) for wavefront impulse W(0)=1 (minimum delay 2)."""
    _index(t, "time")
    return SourceGeometry(x).grade_probability(t-2) if t>=2 else Q(0)


def finite_memory_information_defects(t: int, depth: int, innovation_variance: Q=Q(1)) -> tuple[Q,...]:
    """Linear unbiased conditional-mean MSE for an iid-innovation walk.

    Oracle W_t=xi_1+...+xi_t; E_j(t)=E[W_t|F_(t-j)] = W_(t-j)
    for t>=j.  Thus E[(W_t-E_j)^2]=j*Var(xi) for t>=depth.
    Means are known to observers; independent innovations have zero means.
    No unconditional generic-uncertainty theorem is asserted.
    """
    _index(t,"time");_index(depth,"depth")
    variance=Q(innovation_variance)
    if variance < 0 or depth > t:
        raise ValueError("nonnegative variance, depth<=t required")
    return tuple(j*variance for j in range(depth+1))


def finite_wavefront_past(states: tuple[int,...],t:int,depth:int) -> tuple[int,...]:
    """One observer receives only events with indices <=t-depth.

    This is a *causal receipt set*, not an inference/prediction algorithm.
    """
    _index(t,"time");_index(depth,"depth")
    if t>=len(states):raise ValueError("time exceeds declared finite history")
    cutoff=t-depth
    return states[:cutoff+1] if cutoff>=0 else ()


def depth_defect_residual(signal: tuple[Q, ...] | list[Q], x: Q) -> tuple[Q,...]:
    """D(t)=E1(t)-E2(t) obeys D(t)-v*D(t-1)=Delta_t E1(t).

    Equivalently, Delta_t E1(t)=(1-u)[W(t-1)-E1(t-1)].
    These scalar discrepancies can have either sign; they are NOT entropies.
    """
    g=SourceGeometry(x)
    e1,e2=run_two_stages(signal,x)
    d=[a-b for a,b in zip(e1,e2)]
    return tuple(
        d[t] - (g.v*d[t-1] if t else Q(0))
        - (e1[t] - (e1[t-1] if t else Q(0)))
        for t in range(len(d))
    )


def one_stage_forcing_residual(signal: tuple[Q, ...] | list[Q], x: Q) -> tuple[Q,...]:
    """Exact first-stage causal innovation equation residual."""
    g=SourceGeometry(x)
    w=tuple(Q(a) for a in signal)
    e1,_=run_two_stages(w,x)
    return tuple(
        e1[t]-(g.u*e1[t-1] if t else 0)
        -(1-g.u)*(w[t-1] if t else 0)
        for t in range(len(w))
    )


def equal_stage_critical_grade(depth: int, j: int) -> Q:
    """Declared m-stage extension at theta=1/2; only m=2 is authentic Oily.

    w_(m,j)=C(j+m-1,m-1)/2**(j+m).  This is not evidence that the
    original BBP source has more than its two authenticated loops.
    """
    from math import comb
    if type(depth) is not int or depth < 1:
        raise ValueError("observer depth must be a positive integer")
    _index(j, "grade")
    return Q(comb(j+depth-1,depth-1), 2**(j+depth))


def equal_stage_depth_difference(depth: int, j: int) -> int:
    """The mth forward difference of 2**(j+m) w_(m,j) is zero."""
    from math import comb
    if type(depth) is not int or depth < 1:
        raise ValueError("observer depth must be a positive integer")
    _index(j, "grade")
    return sum(((-1)**(depth-k)*comb(depth,k)*
                comb(j+k+depth-1,depth-1) for k in range(depth+1)))


def run_equal_stage_tower(signal: tuple[Q,...] | list[Q], depth: int, theta: Q=Q(1,2)) -> tuple[Q,...]:
    """Formal m-stage retarded tower; source-authentic grade only at m=2.

    Each stage is E_(k+1)(t)=theta*E_(k+1)(t-1)
                +(1-theta)*E_k(t-1), and E_0=W.
    """
    if type(depth) is not int or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    theta=Q(theta)
    if not Q(0)<=theta<Q(1):
        raise ValueError("requires 0<=theta<1")
    cur=tuple(Q(v) for v in signal)
    for _ in range(depth):
        nxt=[]
        for t in range(len(cur)):
            nxt.append(theta*(nxt[t-1] if t else Q(0))
                       +(1-theta)*(cur[t-1] if t else Q(0)))
        cur=tuple(nxt)
    return cur
