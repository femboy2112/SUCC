"""ZENO-SUCC: exact finite successor, explicit tail, and typed limit transport.

This is a finite rational proof engine for declared mathematical laws, NOT a
device executing omega physical operations. General Cauchy completion,
preservation of closed properties and uniform continuity are classical
theorems in the accompanying dossier; code instantiates exact controls.

Historical dichotomy/Achilles/arrow/stadium framing is not a claim to have
reproduced every historical version of Zeno's arguments.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

class ZenoError(ValueError):
    pass


def rational(x):
    if type(x) not in (int, Q):
        raise ZenoError("exact integer/Fraction required; floats are not certificates")
    return Q(x)


def natural(n, *, upper=10_000):
    if type(n) is not int or not 0 <= n <= upper:
        raise ZenoError("exact finite SUCC stage and declared resource budget required")
    return n


@dataclass(frozen=True)
class GeometricSUCC:
    source_id: str
    epoch: int
    basis: str
    start: Q
    endpoint: Q
    ratio: Q

    def __post_init__(self):
        if any(type(x) is not str or not x.strip()
               for x in (self.source_id,self.basis)):
            raise ZenoError("source ID and common basis must be declared")
        if type(self.epoch) is not int or self.epoch<0:
            raise ZenoError("causal epoch cannot be inferred")
        for field in ("start","endpoint","ratio"):
            object.__setattr__(self,field,rational(getattr(self,field)))
        if not 0<self.ratio<1:
            raise ZenoError("strict geometric Zeno ratio required: 0<q<1")

    def state(self,n):
        natural(n)
        return self.endpoint+(self.start-self.endpoint)*self.ratio**n

    def signed_remainder(self,n):
        natural(n)
        return (self.endpoint-self.start)*self.ratio**n

    def error(self,n):
        return abs(self.signed_remainder(n))

    def finite_clock(self,n):
        """The finite mathematical accumulation schedule t_n=1-2^-n."""
        natural(n)
        return Q(1)-Q(1,2**n)

    def successor(self,n):
        natural(n,upper=9999)
        x=self.state(n)
        y=x+(Q(1)-self.ratio)*(self.endpoint-x)
        if y!=self.state(n+1):
            raise ArithmeticError("declared SUCC recurrence disagrees with exact source")
        return y

    def cauchy_pair(self,n,m):
        natural(n);natural(m)
        if m<n:raise ZenoError("future stage precedes source stage")
        actual=abs(self.state(m)-self.state(n))
        bound=self.error(n)
        if actual>bound:raise ArithmeticError("exact Cauchy-tail certificate violated")
        return {"source":self.source_id,"epoch":self.epoch,"basis":self.basis,
                "n":n,"m":m,"separation":actual,"tail_upper":bound,
                "proves_physical_omega_action":False}

    def modulus(self,tolerance,*,budget=10_000):
        """Least finite n with known tail <= tolerance, if budget suffices."""
        eps=rational(tolerance)
        natural(budget)
        if eps<=0:raise ZenoError("positive accuracy required")
        for n in range(budget+1):
            if self.error(n)<=eps:return n
        raise ZenoError("resource budget insufficient, not proof of nonconvergence")

    def interval(self,n):
        """An error interval, derived from SOURCE law, not fitted observations."""
        x=self.state(n);e=self.error(n)
        return (x-e,x+e)

    def affine_observer(self,n,slope,intercept):
        """Certified Lipschitz affine target y(x)=slope*x+intercept."""
        slope=rational(slope);intercept=rational(intercept)
        x=self.state(n);error=abs(slope)*self.error(n)
        y=slope*x+intercept
        goal=slope*self.endpoint+intercept
        if not y-error<=goal<=y+error:
            raise ArithmeticError("Lipschitz law did not transport through completion")
        return {"stage_value":y,"global_target":goal,
                "lower":y-error,"upper":y+error,"Lipschitz":abs(slope),
                "source_id":self.source_id,
                "mathematical_limit_proved_with_real_completeness":True,
                "physical_infinite_run_certified":False}


@dataclass(frozen=True)
class AchillesSUCC:
    """Achilles relative-speed decomposition; u < v is load bearing."""
    gap: Q
    pursuer_speed: Q
    tortoise_speed: Q

    def __post_init__(self):
        for field in ("gap","pursuer_speed","tortoise_speed"):
            object.__setattr__(self,field,rational(getattr(self,field)))
        if self.gap<=0 or self.pursuer_speed<=0 or not 0<=self.tortoise_speed<self.pursuer_speed:
            raise ZenoError("positive gap and pursuer strictly faster than tortoise")

    @property
    def ratio(self):return self.tortoise_speed/self.pursuer_speed

    @property
    def catch_time(self):return self.gap/(self.pursuer_speed-self.tortoise_speed)

    def finite_checkpoint(self,n):
        natural(n)
        t=self.catch_time*(1-self.ratio**n)
        x_a=self.pursuer_speed*t
        x_t=self.gap+self.tortoise_speed*t
        distance=x_t-x_a
        if distance != self.gap*self.ratio**n:
            raise ArithmeticError("Achilles source geometry changed")
        return {"n":n,"time":t,"pursuer":x_a,"tortoise":x_t,
                "remaining_gap":distance,"catch_time":self.catch_time,
                "infinite_catchup_actions_executed":False}


def arrow_snapshot_alias(t0=0):
    """Two lawful affine paths agree at the instant, disagree in derivative."""
    t0=rational(t0)
    # paths f(t)=0, g(t)=t-t0, same state f(t0)=g(t0)=0.
    return {"t0":t0,"static_readout":Q(),
            "velocity_candidates":(Q(),Q(1)),
            "future_delta_at_t0_plus_one":Q(1),
            "instantaneous_velocity_identified_from_position_only":False}


def stadium_relative_frame(t=Q(1,2)):
    """Illustrative relative-velocity calibration, not unique historical reading."""
    t=rational(t)
    if not 0<=t<=1:raise ZenoError("declared stadium sample time 0<=t<=1")
    right=t;left=-t
    return {"time":t,"right_mover":right,"left_mover":left,
            "relative_displacement":right-left,
            "one_body_displacement":right,
            "relative_speed":Q(2),
            "source_frame":"one shared stationary clock",
            "independent_interleaved_clocks_validated":False}


def pointwise_nonuniform_witness(n):
    """f_n(x)=x^n on [0,1] -> f=0 for x<1, f(1)=1, not uniformly.

    Exact Bernoulli: x=1-1/(2n), f_n(x)>=1/2 at every n>=1.
    """
    natural(n,upper=1000)
    if n==0:raise ZenoError("positive polynomial degree")
    x=Q(1)-Q(1,2*n)
    value=x**n
    if not Q(1,2)<=value or not x<1:
        raise ArithmeticError("Bernoulli finite counterexample failed")
    return {"n":n,"point":x,"finite_value":value,
            "pointwise_limit_value":Q(),
            "uniform_error_lower_bound":Q(1,2),
            "closedness_preservation_from_pointwise_claimed":False}


def derivative_nontransport(n):
    """f_n(x)=x^n/n uniformly ->0, yet f'_n(1)=1 for all n."""
    natural(n,upper=1000)
    if n==0:raise ZenoError("positive degree")
    return {"uniform_function_error_bound":Q(1,n),
            "derivative_at_one":Q(1),
            "limit_function_derivative_at_one":Q(),
            "uniform_derivative_convergence_certified":False}


def analytic_continuation_instability(n):
    """Entire h_n(z)=(z/2)^n small on |z|<=1 and huge at z=4."""
    natural(n,upper=2000)
    if n==0:raise ZenoError("strictly positive degree")
    return {"inner_disk_radius":Q(1),"analytic_domain":"entire",
            "inner_sup_upper":Q(1,2**n),
            "value_at_z_four":Q(2**n),
            "identity_theorem_violated":False,
            "numerical_continuation_stable_without_growth_bound":False}


def halting_alias_at_finite_horizon(horizon, later_halt):
    """Source class of scalar output laws, not an undecidability *proof*.

    A program that halts at step T>N and a never-halting program give
    identical stages 0..N; no bounded observation decides both limits.
    """
    natural(horizon)
    if type(later_halt) is not int or later_halt<=horizon:
        raise ZenoError("specified indistinguishable later halt > horizon")
    return {"horizon":horizon,"same_observed_prefix":tuple(Q() for _ in range(horizon+1)),
            "candidate_limits":(Q(),Q(1)),
            "finite_prefix_identifies_global_limit":False,
            "external_halting_oracle_used":False}
