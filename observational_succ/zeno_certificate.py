"""Source-indexed Zeno laboratories: effective limits versus actual histories.

This is a finite exact rational implementation of *examples* and certificate
arithmetic. The general completion, continuity, and operator-form implications
are proved on paper in research/2026-10-14/ZENO_SUCC_GLOBAL_CERTIFICATES.md;
finite numerical tests are not claimed to prove those universal theorems.

The authentic signed Weil form is not evaluated here. A source-dependent
Gamma-tail budget is proved from its genuine OU-resolvent multiplier, but the
RH-hard signed lower bound is deliberately not assumed.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable


class ZenoTypeError(ValueError):
    """Rejected source, epoch, topology, domain, or exactness mismatch."""


def rational(value: int | F) -> F:
    if type(value) is int or isinstance(value, F):
        return F(value)
    raise ZenoTypeError("a rational exact certificate requires int or Fraction, not float")


def natural(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ZenoTypeError(f"natural stage must be integer >= {minimum}")
    return n


@dataclass(frozen=True)
class Stamp:
    source_id: str
    epoch: int
    basis: str
    domain: str

    def __post_init__(self):
        for s in (self.source_id, self.basis, self.domain):
            if not isinstance(s, str) or not s.strip():
                raise ZenoTypeError("named mathematical source/basis/domain required")
        natural(self.epoch)

    def compatible(self, other: "Stamp") -> bool:
        return self == other


@dataclass(frozen=True)
class FormalLimit:
    """Mathematical endpoint: it is NOT an actualized physical event."""
    stamp: Stamp
    value: F
    topology: str = "usual-real"
    physical_event_executed: bool = False

    def __post_init__(self):
        if self.physical_event_executed:
            raise ZenoTypeError("a formal metric limit is not an executed omega-event")
        rational(self.value)
        if self.topology != "usual-real":
            raise ZenoTypeError("this rational laboratory proves usual-real completion only")


@dataclass(frozen=True)
class GeometricZeno:
    """Finite-stage law x_n=x_0+a(1-r^n)/(1-r), a>=0, 0<=r<1."""
    stamp: Stamp
    x0: F
    increment: F
    ratio: F

    def __post_init__(self):
        for k in ("x0", "increment", "ratio"):
            object.__setattr__(self, k, rational(getattr(self, k)))
        if self.increment < 0 or not (F(0) <= self.ratio < F(1)):
            raise ZenoTypeError("require increment >=0 and 0<=ratio<1")

    def stage(self, n: int) -> F:
        natural(n)
        return self.x0 + self.increment * (1-self.ratio**n)/(1-self.ratio)

    def increment_at(self, n: int) -> F:
        natural(n)
        return self.increment * self.ratio**n

    def mathematical_limit(self) -> FormalLimit:
        return FormalLimit(self.stamp, self.x0 + self.increment/(1-self.ratio))

    def tail(self, n: int) -> F:
        natural(n)
        return self.increment*self.ratio**n/(1-self.ratio)

    def finite_error_certificate(self, n: int) -> dict:
        natural(n)
        endpoint=self.mathematical_limit().value
        t=self.tail(n)
        return {"stage":n,"value":self.stage(n),"tail_upper":t,
                "exact_gap":endpoint-self.stage(n),
                "passes_exact_identity":endpoint-self.stage(n)==t,
                "event_at_omega_executed":False}

    def stage_for_dyadic_error(self, k: int) -> int:
        """Effective modulus for this *specified law*. Find n with tail<=2^-k."""
        natural(k)
        threshold=F(1,2**k)
        if self.increment==0 or self.ratio==0:
            return 0 if self.tail(0)<=threshold else 1
        n=0
        # Strict geometric decrease makes this finite; avoids floating logs.
        t=self.tail(0)
        while t>threshold:
            n+=1
            t*=self.ratio
        return n


@dataclass(frozen=True)
class AchillesZeno:
    stamp: Stamp
    initial_gap: F
    achilles_speed: F
    tortoise_speed: F

    def __post_init__(self):
        for k in ("initial_gap","achilles_speed","tortoise_speed"):
            object.__setattr__(self,k,rational(getattr(self,k)))
        if not (self.initial_gap>0 and self.achilles_speed>self.tortoise_speed>=0):
            raise ZenoTypeError("gap positive; Achilles strictly faster; both forward")

    @property
    def ratio(self): return self.tortoise_speed/self.achilles_speed

    @property
    def catch_time(self): return self.initial_gap/(self.achilles_speed-self.tortoise_speed)

    def time_at(self,n:int)->F:
        natural(n)
        return self.catch_time*(1-self.ratio**n)

    def gap_at(self,n:int)->F:
        natural(n)
        return self.initial_gap*self.ratio**n

    def finite_identity(self,n:int)->bool:
        natural(n)
        t=self.time_at(n)
        return self.initial_gap-(self.achilles_speed-self.tortoise_speed)*t==self.gap_at(n)


@dataclass(frozen=True)
class RationalRootBracket:
    """Certified square-root-of-two bisection in real completion, NOT Q."""
    stamp: Stamp

    def bounds(self,n:int)->tuple[F,F]:
        natural(n)
        lo,hi=F(1),F(2)
        for _ in range(n):
            mid=(lo+hi)/2
            if mid*mid<2:
                lo=mid
            else:
                hi=mid
        assert lo*lo<2<hi*hi
        assert hi-lo==F(1,2**n)
        return lo,hi

    def source_actualization(self)->str:
        return "NO_RATIONAL_ROOT: completeness of R required; proof via odd/even parity"


@dataclass(frozen=True)
class ThomsonLamp:
    stamp: Stamp

    def time_at(self,n:int)->F:
        natural(n)
        return F(1)-F(1,2**n)

    def state_at(self,n:int)->int:
        natural(n)
        return n%2

    def convergent_endpoint_in_discrete_bits(self)->bool:
        # Parity alternates forever: no eventually constant tail.
        return False


@dataclass(frozen=True)
class HiddenTailMutant:
    """Arbitrarily late source mutation, matching ANY specified finite prefix."""
    stamp: Stamp
    agree_through: int

    def __post_init__(self): natural(self.agree_through)

    def baseline(self,n:int)->F:
        natural(n)
        return F(1)-F(1,2**n)

    def mutated(self,n:int)->F:
        natural(n)
        return self.baseline(n)+(F(1) if n>self.agree_through else F(0))

    def limit_pair(self)->tuple[F,F]: return F(1),F(2)

    def same_prefix(self)->bool:
        return all(self.baseline(n)==self.mutated(n) for n in range(self.agree_through+1))


@dataclass(frozen=True)
class IntervalEvidence:
    """Logical implication from a source-verified numerical interval.

    The caller MUST separately prove the given interval encloses the actual
    object. This class does not forge that external provenance.
    """
    stamp: Stamp
    lower: F
    upper: F

    def __post_init__(self):
        object.__setattr__(self,"lower",rational(self.lower))
        object.__setattr__(self,"upper",rational(self.upper))
        if self.lower>self.upper:
            raise ZenoTypeError("empty enclosure is not a certificate")

    def validate_same_source(self, other_stamp: Stamp):
        if not self.stamp.compatible(other_stamp):
            raise ZenoTypeError("source, epoch, domain or basis drift")


def enclosed_limit_sign(stage:IntervalEvidence, error:F, required_stamp:Stamp)->str:
    """Closed-cone gate given independently proved |limit-stage|<=error."""
    stage.validate_same_source(required_stamp)
    e=rational(error)
    if e<0: raise ZenoTypeError("negative error envelope")
    if stage.lower-e>0: return "STRICT_POSITIVE_CERTIFICATE_CONDITIONAL_ON_ENCLOSURE"
    if stage.upper+e<0: return "STRICT_NEGATIVE_CERTIFICATE_CONDITIONAL_ON_ENCLOSURE"
    if stage.lower-e>=0: return "NONNEGATIVE_CERTIFICATE_CONDITIONAL_ON_ENCLOSURE"
    if stage.upper+e<=0: return "NONPOSITIVE_CERTIFICATE_CONDITIONAL_ON_ENCLOSURE"
    return "UNDECIDED_CRITICAL_MARGIN"


def gamma_tail_budget(j:int)->F:
    """TRUE Gamma bath Fourier multiplier tail <=16/d^3+2/d^2, d=4J+1.

    For d_k=4k+1, r_J(xi)=sum_{k>=J}4/[d_k(xi^2+d_k^2/4)]
    <=sum 16/d_k^3 <=16/d_J^3+integral_J^infinity 16/(4x+1)^3 dx.
    The integral equals 2/d_J^2. This is a correct O(J^-2) rate and
    deliberately does NOT assert Gemini's false 1/(8J^2) bound.
    """
    natural(j,1)
    d=4*j+1
    return F(16,d**3)+F(2,d**2)


def gamma_tail_partial(j:int, count:int)->F:
    natural(j,1)
    natural(count)
    return sum((F(16,(4*k+1)**3) for k in range(j,j+count)), F(0))


def gemini_bad_gamma_bound(j:int)->F:
    natural(j,1)
    return F(1,8*j*j)


def signed_weil_zeno_gate(
    evidence: IntervalEvidence,
    j:int,
    derivative_norm_sq: F,
    required_stamp: Stamp
)->str:
    """For Q-Q_J in [0, epsilon_J ||v'||^2], classify ONE fixed v.

    NOT a universal sign claim; input Q_J interval must independently be
    authenticated and include prime, contact, poles and half-density.
    """
    evidence.validate_same_source(required_stamp)
    qnorm=rational(derivative_norm_sq)
    if qnorm<0:raise ZenoTypeError("negative Sobolev norm squared")
    e=gamma_tail_budget(j)*qnorm
    if evidence.lower>=0:
        return "TEST_NONNEGATIVE_CONDITIONAL_ON_AUTHENTIC_TRUNCATION"
    if evidence.upper+e<0:
        return "TEST_NEGATIVE_CONDITIONAL_ON_AUTHENTIC_TRUNCATION"
    return "TEST_UNDECIDED_NO_ALL_TEST_SIGN"


def hilbert_shadow(hidden_negative_coordinate:int, measured_prefix:int)->tuple[int,...]:
    """Diagonal of I-2P_M on first n coordinates. 1-indexed hidden mode."""
    natural(hidden_negative_coordinate,1)
    natural(measured_prefix)
    return tuple(-1 if k==hidden_negative_coordinate else 1 for k in range(1,measured_prefix+1))


def arrow_snapshot_countermodel()->dict:
    """x(t)=0 versus y(t)=t have identical position at t=0, velocities differ."""
    return {"time":F(0),"same_position":True,"velocity_static":F(0),
            "velocity_moving":F(1),"instantaneous_displacement":F(0)}


def stadium_relative_motion(delta_time: int|F, speed: int|F)->dict:
    """A stationary, B +v, C -v: relative B/C speed 2v, not v."""
    dt,v=rational(delta_time),rational(speed)
    if dt<0 or v<=0:raise ZenoTypeError("time>=0, v>0")
    return {"B_vs_A_distance":v*dt,"B_vs_C_distance":2*v*dt,
            "B_vs_A_velocity":v,"B_vs_C_velocity":2*v,
            "time_from_A":v*dt/v,"time_from_C":2*v*dt/(2*v)}


def typed_history(stage_count:int)->dict:
    """Formal list of modelled finite steps, not actual physical instrument outcomes."""
    natural(stage_count)
    return {"finite_steps":stage_count,"a_last_omega_event":False,
            "mathematical_limit_entails_executed_event":False,
            "physical_execution_certified":False}


def meta_limit_dependency(cases: Iterable[tuple[Stamp, Stamp]])->bool:
    """Only source-basis-domain coherent squares are admissible."""
    for left,right in cases:
        if not left.compatible(right):
            return False
    return True


def _fraction_matrix(matrix):
    rows=tuple(tuple(rational(x) for x in row) for row in matrix)
    n=len(rows)
    if any(len(row)!=n for row in rows):
        raise ZenoTypeError("finite Schur matrix must be square")
    if any(rows[i][j]!=rows[j][i] for i in range(n) for j in range(n)):
        raise ZenoTypeError("finite Schur matrix must be symmetric")
    return rows


def psd_exact(matrix)->bool:
    """Exact rational PSD test via recursive Schur complements.

    If pivot is zero, PSD forces its entire row/column zero. Nonzero
    off-diagonal with zero pivot produces a negative 2x2 minor.
    For positive pivot, Schur complement preserves PSD iff parent PSD.
    This handles singular matrices exactly; no eigenvalue rounding.
    """
    a=[list(r) for r in _fraction_matrix(matrix)]
    while a:
        p=a[0][0]
        if p<0:return False
        if p==0:
            if any(x!=0 for x in a[0][1:]):return False
            a=[r[1:] for r in a[1:]]
        else:
            col=[a[i][0] for i in range(1,len(a))]
            a=[[a[i+1][j+1]-col[i]*col[j]/p
                for j in range(len(col))] for i in range(len(col))]
    return True


@dataclass(frozen=True)
class ConditionalBlockSchur:
    """Exact arithmetic sufficient certificate for a finite-moment bottleneck.

    Input assertions about an infinite operator, in particular complement
    coercivity q_K>=kappa ||k||^2 and R>=B*B, are ASSUMPTIONS requiring a
    separate actual-source proof; the finite matrix PSD is checked exactly.
    """
    stamp: Stamp
    finite_form: tuple[tuple[F,...],...]
    cross_gram_upper: tuple[tuple[F,...],...]
    kappa: F

    def __post_init__(self):
        m=_fraction_matrix(self.finite_form)
        r=_fraction_matrix(self.cross_gram_upper)
        if len(m)!=len(r):raise ZenoTypeError("incompatible Schur blocks")
        k=rational(self.kappa)
        if k<=0:raise ZenoTypeError("strict positive complement coercivity required")
        object.__setattr__(self,"finite_form",m)
        object.__setattr__(self,"cross_gram_upper",r)
        object.__setattr__(self,"kappa",k)

    def finite_schur(self)->tuple[tuple[F,...],...]:
        return tuple(tuple(self.finite_form[i][j]-self.cross_gram_upper[i][j]/self.kappa
                           for j in range(len(self.finite_form)))
                     for i in range(len(self.finite_form)))

    def exact_finite_gate(self,required_stamp:Stamp)->str:
        if not self.stamp.compatible(required_stamp):raise ZenoTypeError("source drift")
        if not psd_exact(self.cross_gram_upper):
            return "REJECTED_CROSS_GRAM_NOT_PSD"
        if psd_exact(self.finite_schur()):
            return "FINITE_MATRIX_PSD_IF_INFINITE_SOURCE_BOUNDS_AUTHENTIC"
        return "SCHUR_SUFFICIENCY_FAILED_NOT_A_GLOBAL_NEGATIVE_WITNESS"


def zeno_two_level_budget(model_tail: F, geometry_tail:F, implementation_tail:F)->F:
    """Additive error budget only; no certification of components by naming."""
    values=[rational(x) for x in (model_tail,geometry_tail,implementation_tail)]
    if any(x<0 for x in values):raise ZenoTypeError("negative tail budget")
    return sum(values,F(0))
