"""Exact 2+1 Minkowski frames and causal observations for ObsSUCC.

Classical special relativity + Lamport-style partial causal orders, implemented
with Fractions. A frame transformation is a coordinate change, NOT a physical
intervention on the carrier or an empirically attested human cognitive model.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from typing import Hashable


class FrameError(ValueError):
    """Invalid frame, source history, superluminal receipt or causal cut."""


def q(v: int | F) -> F:
    if type(v) not in (int, F):
        raise FrameError("Only exact integer/Fraction coordinates are certificates")
    return F(v)


@dataclass(frozen=True)
class EventPoint:
    t: F
    x: F
    y: F = F(0)

    def __post_init__(self):
        for p in ("t", "x", "y"):
            object.__setattr__(self, p, q(getattr(self, p)))

    def difference(self, other: "EventPoint") -> "EventPoint":
        return EventPoint(self.t-other.t, self.x-other.x, self.y-other.y)

    def interval(self) -> F:
        """Minkowski quadratic form, units c=1, signature (+,-,-)."""
        return self.t*self.t-self.x*self.x-self.y*self.y


def causally_before(p: EventPoint, r: EventPoint, *, strict: bool = False) -> bool:
    d = r.difference(p)
    return (d.t > 0 if strict else d.t >= 0) and d.interval() >= 0


def spacelike(p: EventPoint, r: EventPoint) -> bool:
    return r.difference(p).interval() < 0


def _matmul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(3)), F(0))
                       for j in range(3)) for i in range(3))


def _det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


@dataclass(frozen=True)
class LorentzFrame:
    """Exact proper orthochronous rational Lorentz matrix in 2+1 dimensions."""
    matrix: tuple[tuple[F, F, F], tuple[F, F, F], tuple[F, F, F]]

    def __post_init__(self):
        if (type(self.matrix) is not tuple or len(self.matrix) != 3
                or any(type(row) is not tuple or len(row) != 3 for row in self.matrix)):
            raise FrameError("Exact 3x3 Lorentz matrix required")
        m = tuple(tuple(q(v) for v in row) for row in self.matrix)
        object.__setattr__(self, "matrix", m)
        eta = (F(1), F(-1), F(-1))
        for i in range(3):
            for j in range(3):
                pairing = sum((eta[k]*m[k][i]*m[k][j] for k in range(3)), F(0))
                if pairing != (eta[i] if i == j else 0):
                    raise FrameError("Lorentz matrix fails metric preservation")
        if _det(m) != 1 or m[0][0] < 1:
            raise FrameError("Proper orthochronous Lorentz frame required")

    @classmethod
    def identity(cls) -> "LorentzFrame":
        return cls(((F(1), F(0), F(0)),
                    (F(0), F(1), F(0)),
                    (F(0), F(0), F(1))))

    @classmethod
    def boost(cls, axis: str, parameter: F) -> "LorentzFrame":
        """Rational tanh(rapidity/2): gamma=(1+r²)/(1-r²), gamma*v=2r/(1-r²).

        Positive r means positive observer velocity; t'=gamma*(t-v*x_axis).
        """
        r = q(parameter)
        if axis not in ("x", "y") or not F(-1) < r < F(1):
            raise FrameError("Choose x/y and rational rapidity parameter in (-1,1)")
        gamma = (1+r*r)/(1-r*r)
        sigma = 2*r/(1-r*r)
        m = [list(row) for row in cls.identity().matrix]
        j = 1 if axis == "x" else 2
        m[0][0], m[0][j], m[j][0], m[j][j] = gamma, -sigma, -sigma, gamma
        return cls(tuple(tuple(row) for row in m))


    @classmethod
    def pure_boost(cls, vx: F, vy: F) -> "LorentzFrame":
        """Coordinate boost at a rational velocity with rational Lorentz factor.

        This is a pure boost in arbitrary spatial direction; checking rational
        square roots is a REPRESENTATION restriction, not a physics restriction.
        """
        vx, vy = q(vx), q(vy)
        speed2 = vx*vx + vy*vy
        if speed2 >= 1:
            raise FrameError("Superluminal or null inertial-frame velocity")
        one_minus = 1-speed2
        p, d = isqrt(one_minus.numerator),isqrt(one_minus.denominator)
        if p*p!=one_minus.numerator or d*d!=one_minus.denominator:
            raise FrameError("Lorentz gamma irrational: this exact rational sublab cannot express it")
        gamma = F(d,p)
        if speed2==0:return cls.identity()
        vs=(vx,vy)
        m = [[F(0)]*3 for _ in range(3)]
        m[0][0]=gamma
        for i in range(2):
            m[0][i+1]=m[i+1][0]=-gamma*vs[i]
            for j in range(2):
                m[i+1][j+1]=(int(i==j) + (gamma-1)*vs[i]*vs[j]/speed2)
        return cls(tuple(tuple(row) for row in m))

    def decompose_boost_then_rotation(self)->tuple["LorentzFrame","LorentzFrame"]:
        """Exact L=B(v) R for rational L when resulting pure boost rational.

        R fixes time coordinate and rotates the two spatial axes. This is the
        Wigner/Thomas rotation phenomenon; no state or proof knowledge is created.
        """
        m=self.matrix
        gamma=m[0][0]
        vx,vy=-m[1][0]/gamma,-m[2][0]/gamma
        pure=LorentzFrame.pure_boost(vx,vy)
        rotation=self.then(pure.inverse())
        if (rotation.matrix[0]!=(F(1),F(0),F(0))
              or rotation.matrix[1][0]!=0 or rotation.matrix[2][0]!=0):
            raise AssertionError("Not a pure spatial Wigner rotation")
        if rotation.then(pure)!=self:
            raise AssertionError("Lorentz decomposition order corrupted")
        return pure,rotation

    def apply(self, p: EventPoint) -> EventPoint:
        x = (p.t,p.x,p.y)
        t,xnew,y = (sum((self.matrix[i][k]*x[k] for k in range(3)),F(0))
                    for i in range(3))
        return EventPoint(t,xnew,y)

    def then(self, next_frame: "LorentzFrame") -> "LorentzFrame":
        """Apply self, then next_frame; order matters for transverse boosts."""
        if not isinstance(next_frame,LorentzFrame):
            raise FrameError("Cannot compose non-Lorentz frame")
        return LorentzFrame(_matmul(next_frame.matrix,self.matrix))

    def inverse(self) -> "LorentzFrame":
        eta = (F(1),F(-1),F(-1))
        m = self.matrix
        return LorentzFrame(tuple(tuple(eta[i]*m[j][i]*eta[j] for j in range(3))
                                  for i in range(3)))


@dataclass(frozen=True)
class CausalEvent:
    ident: str
    point: EventPoint
    kind: str
    source_id: str
    parents: tuple[str, ...] = ()
    payload: tuple[Hashable, ...] = ()

    def __post_init__(self):
        if not self.ident or not self.source_id or self.kind not in (
                "probe", "relay", "reason", "checkpoint"):
            raise FrameError("Every event requires source, ID and typed kind")
        if not isinstance(self.point,EventPoint) or len(set(self.parents)) != len(self.parents):
            raise FrameError("Bad event point or repeated predecessor")


@dataclass(frozen=True)
class CausalLedger:
    """Source-indexed, immutable finite event DAG; parent arrows obey light cones.

    Parent edges express ACTUAL causal links and must not be inferred from mere
    timelike separation. Source IDs are declared, not physical attestations.
    """
    events: tuple[CausalEvent, ...]

    def __post_init__(self):
        if not self.events or any(not isinstance(e,CausalEvent) for e in self.events):
            raise FrameError("Nonempty exact event ledger required")
        ids = [e.ident for e in self.events]
        if len(set(ids)) != len(ids) or len({e.source_id for e in self.events})!=1:
            raise FrameError("Distinct events on one declared carrier required")
        items = {e.ident:e for e in self.events}
        for e in self.events:
            for p in e.parents:
                if p not in items or p == e.ident:
                    raise FrameError("Unknown/self causal predecessor")
                if not causally_before(items[p].point,e.point,strict=True):
                    raise FrameError("Parent event cannot signal along the proposed edge")
        status={}
        def visit(k):
            if status.get(k)==1:raise FrameError("Causal dependency cycle")
            if status.get(k)==2:return
            status[k]=1
            for p in items[k].parents:visit(p)
            status[k]=2
        for k in ids:visit(k)

    def get(self,ident:str)->CausalEvent:
        for e in self.events:
            if e.ident==ident:return e
        raise FrameError("Unknown causal event")

    def downclosure(self,observed:tuple[str,...])->frozenset[str]:
        seen=set()
        def gather(k):
            if k in seen:return
            e=self.get(k)
            seen.add(k)
            for x in e.parents:gather(x)
        for x in observed:gather(x)
        return frozenset(seen)

    def is_downset(self,observed:tuple[str,...]) -> bool:
        return set(observed)==set(self.downclosure(observed))

    def causal_ancestry(self,anchor:str)->frozenset[str]:
        return self.downclosure((anchor,))

    def slice_at_anchor(self,frame:LorentzFrame,anchor:str)->frozenset[str]:
        """Coordinate-simultaneous-or-prior slice; NOT accessible evidence."""
        pivot=frame.apply(self.get(anchor).point).t
        result=frozenset(e.ident for e in self.events if frame.apply(e.point).t<=pivot)
        if not self.is_downset(tuple(result)):
            raise AssertionError("Proper Lorentz time must preserve causal ancestry")
        return result

    def compare_slices(self,left:LorentzFrame,right:LorentzFrame,anchor:str)->dict:
        a=self.get(anchor).point
        u=self.slice_at_anchor(left,anchor)
        v=self.slice_at_anchor(right,anchor)
        mismatch=u.symmetric_difference(v)
        if any(not spacelike(self.get(k).point,a) for k in mismatch):
            raise AssertionError("A causal comparable event changed its time order")
        return {"left":tuple(sorted(u)),"right":tuple(sorted(v)),
                "mismatch":tuple(sorted(mismatch)),
                "all_mismatches_spacelike_to_anchor":True,
                "causal_past":tuple(sorted(e.ident for e in self.events
                         if causally_before(e.point,a)))}

    def certified_probes_at(self,checkpoint:str)->tuple[CausalEvent,...]:
        """Causal ancestors actually linked by parent/relay edges, not all past events."""
        anchor=self.get(checkpoint)
        if anchor.kind!="checkpoint":raise FrameError("Only designated E checkpoints can accept proofs")
        ids=self.causal_ancestry(checkpoint)
        return tuple(e for e in self.events if e.ident in ids and e.kind=="probe")


def physical_frame_demo()->dict:
    E=LorentzFrame.identity(); xboost=LorentzFrame.boost("x",F(1,3))
    yboost=LorentzFrame.boost("y",F(1,3))
    a=EventPoint(0,-1);b=EventPoint(0,1);origin=EventPoint(0,0)
    xa=xboost.apply(a); xb=xboost.apply(b)
    if (xa.t,xb.t)!=(F(3,4),F(-3,4)):
        raise AssertionError("Unexpected relativity-of-simultaneity calibration")
    assert xboost.then(yboost).matrix!=yboost.then(xboost).matrix
    assert xboost.apply(EventPoint(5,3)).t==F(4)
    assert xboost.apply(EventPoint(5,3)).x==F(0)
    ledger=CausalLedger((
        CausalEvent("left",a,"probe","carrier"),
        CausalEvent("right",b,"probe","carrier"),
        CausalEvent("origin",origin,"checkpoint","carrier"),
        CausalEvent("received",EventPoint(1,0),"checkpoint","carrier",("left","right"))))
    comp=ledger.compare_slices(E,xboost,"origin")
    return {"boost_x":str(xboost.matrix),"boost_y":str(yboost.matrix),
      "spacelike_order_E":[str(a.t),str(b.t)],
      "spacelike_order_boosted":[str(xa.t),str(xb.t)],
      "same_past_as_ledger":comp["causal_past"],
      "slice_mismatch":comp["mismatch"],
      "mismatch_only_spacelike":comp["all_mismatches_spacelike_to_anchor"],
      "noncollinear_boosts_commute":False,
      "receipt_minimum_E_time": "1",
      "physical_knowledge_inferred_from_coordinate_time":False}


def epistemic_flux_demo()->dict:
    """One observer's eight event receipts over a moving timelike worldline.

    Events per coordinate time are NOT Lorentz-invariant; proper-time rate
    is intrinsic to the specified physical worldline + event count. This is
    a clock-reparametrization control, not a law of psychological cognition.
    """
    start=EventPoint(0,0)
    end=EventPoint(5,3)
    boost=LorentzFrame.boost('x',F(1,3))
    dt=end.t-start.t
    dtproper=boost.apply(end).t-boost.apply(start).t
    dxprime=boost.apply(end).x-boost.apply(start).x
    event_count=8
    if dxprime!=0 or dtproper!=4 or end.difference(start).interval()!=16:
        raise AssertionError("Wrong 3/5 observer calibration")
    return {"events":event_count,"E_elapsed_coordinate_time":str(dt),
            "climber_elapsed_proper_time":str(dtproper),
            "E_coordinate_rate":str(F(event_count)/dt),
            "climber_proper_rate":str(F(event_count)/dtproper),
            "physical_clock_ratio":str(dt/dtproper),
            "knowledge_claim_preserved_only_if_source_equivariant":True,
            "literal_cognitive_lorentz_law_demonstrated":False}
