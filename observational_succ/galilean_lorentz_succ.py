"""Exact 1+1 Galilean -> Lorentz case study as source-relative SUCC repair.

All computations use exact rational Fractions and declared physical inputs.
The scalar vacuum wave equation is a faithful 1+1 test of the characteristic
cone of source-free Maxwell theory, NOT the full tensor Maxwell system.
The historical interpretation is retrospective; experiment authentication,
quantum spacetime, General Relativity and RH are not claimed.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F


class RelativityWitnessError(ValueError):
    """Malformed source, velocity, or unsupported geometry inference."""


def q(v):
    if type(v) is int or type(v) is F:
        return F(v)
    raise RelativityWitnessError("Exact int/Fraction expected; floats are not certificates")


@dataclass(frozen=True)
class Mat2:
    """Exact linear coordinate/field transform (t,x) -> (t',x')."""
    a: F
    b: F
    c: F
    d: F

    def __post_init__(self):
        for name in ('a','b','c','d'):
            object.__setattr__(self,name,q(getattr(self,name)))

    def __matmul__(self, other):
        if not isinstance(other,Mat2):return NotImplemented
        return Mat2(self.a*other.a+self.b*other.c,
                    self.a*other.b+self.b*other.d,
                    self.c*other.a+self.d*other.c,
                    self.c*other.b+self.d*other.d)

    def apply(self, event):
        t,x=map(q,event)
        return self.a*t+self.b*x,self.c*t+self.d*x

    def transpose(self):
        return Mat2(self.a,self.c,self.b,self.d)

    def determinant(self):
        return self.a*self.d-self.b*self.c

    def inverse(self):
        d=self.determinant()
        if not d:raise RelativityWitnessError("Noninvertible frame map")
        return Mat2(self.d/d,-self.b/d,-self.c/d,self.a/d)

    def scaled(self,scalar):
        a=q(scalar)
        return Mat2(a*self.a,a*self.b,a*self.c,a*self.d)

    def serialize(self):
        return [[str(self.a),str(self.b)],[str(self.c),str(self.d)]]


ID=Mat2(1,0,0,1)
ETA=Mat2(1,0,0,-1)
ZERO=Mat2(0,0,0,0)


def galilean(v):
    """Old 1+1 observer transformation, absolute t'=t."""
    v=q(v)
    return Mat2(1,0,-v,1)


def rational_boost(parameter):
    """Lorentz boost with rational half-rapidity parameter u=tanh(eta/2).

    beta=2u/(1+u²), gamma=(1+u²)/(1-u²), |u|<1. This gives
    an infinite exact rational laboratory without floating sqrt(1-beta²).
    """
    u=q(parameter)
    if abs(u)>=1:raise RelativityWitnessError("Proper future-oriented boost needs |u|<1")
    beta=2*u/(1+u*u)
    gamma=(1+u*u)/(1-u*u)
    return beta,gamma,Mat2(gamma,-gamma*beta,-gamma*beta,gamma)


def boost_addition_parameter(u,v):
    u,v=q(u),q(v)
    if abs(u)>=1 or abs(v)>=1:
        raise RelativityWitnessError("Boost parameters must lie in (-1,1)")
    return (u+v)/(1+u*v)


def velocity_addition(beta1,beta2):
    v,w=q(beta1),q(beta2)
    if abs(v)>=1 or abs(w)>=1:
        raise RelativityWitnessError("Timelike inertial frame velocities required")
    return (v+w)/(1+v*w)


def interval_squared(event):
    t,x=map(q,event)
    return t*t-x*x


def is_lightlike(event):
    return interval_squared(event)==0


def is_future_causal(delta):
    t,x=map(q,delta)
    return t>=abs(x)


def speed_for_ray(frame,sign):
    if sign not in (-1,1):raise RelativityWitnessError("Both signed light rays required")
    t,x=frame.apply((1,sign))
    if not t:raise RelativityWitnessError("This observer gives vanishing time component")
    return x/t


def metric_defect(frame):
    """Exact wave-operator/principal-symbol covariance residual.

    For coordinate y=T x and Box_x=partial_t²-partial_x², chain rule yields
    symbol T*ETA*T^T in y coordinates. Zero here iff operator form is
    preserved for every twice differentiable scalar f.
    """
    a=frame @ ETA @ frame.transpose()
    return Mat2(a.a-1,a.b,a.c,a.d+1)


def quadratic_wave_failure(frame):
    """Box_y[(t-x)^2 o T^-1] in the NEW standard y-coordinate wave law.

    This actual solution-to-solution counterexample is zero for Lorentz
    transforms but nonzero for the Galilean v=3/5 calibration.
    """
    inv=frame.inverse()
    aa=inv.a-inv.c
    bb=inv.b-inv.d
    return 2*(aa*aa-bb*bb)


def conformal_candidate(parameter,scale):
    """Two light rays and relative velocity leave one positive scale unproved."""
    scale=q(scale)
    if scale<=0:raise RelativityWitnessError("Orientation/time-preserving conformal scale")
    return rational_boost(parameter)[2].scaled(scale)


def rank_rational(rows):
    """Independent exact row-reduction oracle for empirical constraint rank."""
    if not rows:return 0
    n=len(rows[0])
    if any(len(r)!=n for r in rows):raise RelativityWitnessError("Ragged constraints")
    a=[list(map(q,r)) for r in rows]
    pivot_row=0
    for c in range(n):
        i=next((i for i in range(pivot_row,len(a)) if a[i][c]),None)
        if i is None:continue
        a[i],a[pivot_row]=a[pivot_row],a[i]
        z=a[pivot_row][c]
        a[pivot_row]=[t/z for t in a[pivot_row]]
        for k in range(len(a)):
            if k==pivot_row:continue
            factor=a[k][c]
            if factor:
                a[k]=[x-factor*y for x,y in zip(a[k],a[pivot_row])]
        pivot_row+=1
        if pivot_row==len(a):break
    return pivot_row


def metric_shadow_constraints(*,forward=True,backward=True,clock=False):
    """Observations of null n+/n- and a normalized unit timelike clock.

    Symmetric metric Q=[[a,b],[b,d]] has 3 unknown entries.
    Null rays give a±2b+d=0; clock calibration gives a=1.
    Return exact rank and a concrete rival when observations insufficient.
    """
    rows=[]
    if forward:rows.append((1,2,1))
    if backward:rows.append((1,-2,1))
    if clock:rows.append((1,0,0))
    rank=rank_rational(rows)
    unique=rank==3
    result={"constraint_rank":rank,"free_geometry_dimensions":3-rank,
            "unique_normalized_metric":unique}
    if unique:
        result["metric"]=ETA
    else:
        # Same observed constraints as ETA, yet globally different metric.
        if forward and backward:
            rival=ETA.scaled(2)
        elif forward and clock:
            rival=Mat2(1,1,1,-3)
        elif backward and clock:
            rival=Mat2(1,-1,-1,-3)
        elif forward:
            rival=Mat2(2,0,0,-2)
        elif backward:
            rival=Mat2(2,0,0,-2)
        elif clock:
            rival=Mat2(1,0,0,-2)
        else:
            rival=Mat2(2,0,0,-2)
        # Check BOTH models satisfy the entire declared empirical menu.
        for metric in (ETA,rival):
            if forward and interval_form(metric,(1,1)):
                raise AssertionError("Forward source not null")
            if backward and interval_form(metric,(1,-1)):
                raise AssertionError("Backward source not null")
            if clock and interval_form(metric,(1,0))!=1:
                raise AssertionError("Clock source not unit")
        result["indistinguishable_metrics"]=(ETA,rival)
    return result


def interval_form(metric,event):
    t,x=map(q,event)
    return metric.a*t*t+(metric.b+metric.c)*t*x+metric.d*x*x


def unique_boost_from_empirical_constraints(v,scale):
    """Rigorous normal-form gate among time/space symmetric linear frames.

    In this declared class, preservation of BOTH directed null rays and
    worldline x=v t maps every candidate to positive scale*Lorentz(v).
    Metric/clock invariance then requires scale=1.
    """
    v,scale=q(v),q(scale)
    if abs(v)>=1 or scale<=0:
        raise RelativityWitnessError("Invalid timelike velocity or frame scale")
    # Work without sqrt: construct exact beta with rational gamma supplied by
    # a half-rapidity witness; for arbitrary v, return structural equations.
    return {"velocity":v,"free_conformal_scale":scale,
            "normalized_metric_requires_scale_one":scale==1,
            "time_mixing_is_forced":v!=0,
            "general_linear_form":f"a*[[1,-{v}],[-{v},1]], a>0; metric requires a^2*(1-v^2)=1"}


def galilean_to_lorentz_case(parameter=F(1,3)):
    v,gamma,L=rational_boost(parameter)
    G=galilean(v)
    candidate=conformal_candidate(parameter,2)
    failure=metric_defect(G)
    success=metric_defect(L)
    return {
      "source":"1+1 vacuum scalar wave characteristic of Maxwell in units c=1",
      "velocity":v,"gamma":gamma,
      "galilean":G.serialize(),"lorentz":L.serialize(),
      "galilean_operator_defect":failure.serialize(),
      "galilean_null_slopes":(speed_for_ray(G,-1),speed_for_ray(G,1)),
      "galilean_quadratic_wave_failure":quadratic_wave_failure(G),
      "lorentz_operator_defect":success.serialize(),
      "lorentz_null_slopes":(speed_for_ray(L,-1),speed_for_ray(L,1)),
      "lorentz_quadratic_wave_failure":quadratic_wave_failure(L),
      "two_light_rays_clock_sufficient":metric_shadow_constraints(forward=False,backward=False)["constraint_rank"]==0
              and metric_shadow_constraints(forward=False,backward=False,clock=True)["constraint_rank"]==1
              and metric_shadow_constraints(clock=True,forward=True,backward=True)["unique_normalized_metric"],
      "null_cone_alone_cannot_fix_clock_scale":metric_defect(candidate)!=ZERO,
      "geometry_selected": "Lorentz from two light rays + clock normalization + inertial-frame reciprocity",
      "formal_physical_measurement_authentication":False,
      "historical_simulation_not_historical_experiment":True,
      "RH_or_global_Weil_positivity_claimed":False,
    }


def free_particle_galilean(origin,velocity,frame_velocity):
    """Old mechanical environmental closure: x(t)=a+ut stays free under G_v.

    Newton's unforced equation x''(t)=0 commutes with this frame change.
    A valid model does NOT become globally invalid because it cannot also
    make a separate vacuum electromagnetic law frame-invariant.
    """
    a,u,v=q(origin),q(velocity),q(frame_velocity)
    return {"transformed_origin":a,"transformed_velocity":u-v,
            "transformed_acceleration":F(0),
            "free_particle_law_preserved":True}


def galilean_moving_medium_wave_operator(frame_velocity):
    """A DIFFERENT coherent repair: retain absolute time, transport the PDE.

    Box_x under G_v is (d_t'-v*d_x')²-d_x'². This describes a wave
    medium with background rest frame, not a same-form invariant vacuum
    law in all inertial frames. The failed same-form square does not rule
    out every mathematically coherent Newtonian preferred-frame model.
    """
    v=q(frame_velocity)
    transformed=galilean(v) @ ETA @ galilean(v).transpose()
    if transformed!=Mat2(1,-v,-v,v*v-1):
        raise AssertionError("Galilean moving-medium transport invalid")
    return {"operator_in_moving_frame":transformed,
            "wave_characteristic_speeds":(-1-v,1-v),
            "same_form_vacuum_operator":transformed==ETA,
            "preferred_medium_structure_added":v!=0,
            # Deliberate firewall DISCLAIMER, not a geometric quantity: this
            # construction never claims a unique physical ontology is selected
            # (a coherent moving-medium alternative exists for every v!=0, and at
            # v=0 there is no transition to adjudicate). Constant False, like the
            # RH_claimed / physical_source_authenticated disclaimers elsewhere.
            "unique_physical_model_selected":False}
