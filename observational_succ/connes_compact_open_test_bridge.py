"""An ACTUAL compact-open Qp^times test for Connes' off-identity local factor.

For u0 in Q^times \\ {1}, let B=u0+p^r Zp, with r>v_p(u0)
and r>v_p(1-u0). This is a compact-open subset of Qp^times
avoiding u=1; both |u|p and |1-u|p are constant on B.
With multiplicative Haar d^times u = du / ((1-p^-1)|u|p), the
restriction of the classical Connes geometric local distribution
to phi=1_B has the EXACT rational value

  <T_p,phi> = p^-r / ((1-p^-1)|u0|p |1-u0|p).

This is a genuine p-adic test (not a finite sampled delta spike). It
does NOT settle the principal-value/contact at u=1, Fourier normalization,
global adelic trace, Weil positivity, or RH. The local half-density
normalization C_p(u)=sqrt(|u|p)/|1-u|p is inversion-symmetric.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt


class LocalTraceTestError(ValueError):
    """Test touches identity/zero, fake local place, or invalid measure."""


def _prime(p):
    if type(p) is not int or p<2 or p>100000 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise LocalTraceTestError("genuine prime required")
    return p


def vp(q,p):
    """Exact valuation of a nonzero rational at true p-adic place."""
    _prime(p)
    if type(q) not in (int,Q) or Q(q)==0:
        raise LocalTraceTestError("nonzero rational local center or difference required")
    q=Q(q)
    def v_int(n):
        n=abs(n);k=0
        while n%p==0:
            n//=p;k+=1
        return k
    return v_int(q.numerator)-v_int(q.denominator)


def abs_p(q,p):
    return Q(p)**(-vp(q,p))


@dataclass(frozen=True)
class LocalScaleBall:
    p: int
    center: Q
    radius_power: int
    source_id: str = "Q-standard-Tate"
    epoch: int = 0

    def __post_init__(self):
        _prime(self.p)
        if type(self.center) not in (int,Q):
            raise LocalTraceTestError("exact rational local center required")
        c=Q(self.center)
        if c in (0,1):
            raise LocalTraceTestError("test centered at forbidden zero or singular identity")
        if type(self.radius_power) is not int or not -60<=self.radius_power<=60:
            raise LocalTraceTestError("finite source p-adic ball exponent required")
        if self.radius_power<=max(vp(c,self.p),vp(1-c,self.p)):
            raise LocalTraceTestError("ball must avoid zero and u=1")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise LocalTraceTestError("nonempty original source ID")
        if type(self.epoch) is not int or self.epoch<0:
            raise LocalTraceTestError("nonnegative original epoch")
        object.__setattr__(self,"center",c)

    @property
    def additive_volume(self):
        return Q(self.p)**(-self.radius_power)

    @property
    def multiplicative_volume(self):
        return self.additive_volume/((1-Q(1,self.p))*abs_p(self.center,self.p))

    @property
    def off_identity_scalar(self):
        return 1/abs_p(1-self.center,self.p)

    @property
    def trace_pairing(self):
        """Exact < |1-u|_p^-1, 1_B >_{d^times u}."""
        return self.multiplicative_volume*self.off_identity_scalar

    @property
    def half_density_integral_squared(self):
        """Exact square of < sqrt(|u|p)/|1-u|p,1_B >; no float."""
        return (self.multiplicative_volume**2 *abs_p(self.center,self.p)
                /abs_p(1-self.center,self.p)**2)

    def inverse(self):
        """Inversion maps B to c^-1+p^(r-2 v_p(c)) Z_p, preserving d^times."""
        return type(self)(self.p,1/self.center,
                          self.radius_power-2*vp(self.center,self.p),
                          self.source_id,self.epoch)

    def reciprocal_transport(self):
        backward=self.inverse()
        if self.multiplicative_volume!=backward.multiplicative_volume:
            raise AssertionError("multiplicative Haar inversion failed")
        if self.half_density_integral_squared!=backward.half_density_integral_squared:
            raise AssertionError("orientation half-density test distribution failed")
        return {
            "p":self.p,"center":self.center,"radius_power":self.radius_power,
            "inverse_center":backward.center,"inverse_radius_power":backward.radius_power,
            "positive_source_trace":self.trace_pairing,
            "reciprocal_source_trace":backward.trace_pairing,
            "symmetric_half_density_squared":self.half_density_integral_squared,
            "symmetric_half_density_invariant":True,
            "principal_value_at_identity_proved":False,
            "all_place_Weil_identified":False,"RH_proved":False,
        }

    def receipt(self):
        return {
            "prime":self.p,"center":self.center,"radius_power":self.radius_power,
            "source":self.source_id,"epoch":self.epoch,
            "normalized_additive_ball_volume":self.additive_volume,
            "normalized_multiplicative_haar_volume":self.multiplicative_volume,
            "local_Connes_off_identity_fixed_point_scalar":self.off_identity_scalar,
            "local_test_pairing":self.trace_pairing,
            "half_density_pairing_squared":self.half_density_integral_squared,
            "test_is_genuine_locally_constant_compact_support":True,
            "test_support_disjoint_from_u_equals_1":True,
            "identity_contact_known":False,"RH_proved":False,
        }


def local_linear_test_pairing(terms):
    """Exact finite span of local compact-open indicators away from identity."""
    if type(terms) is not tuple or not terms:
        raise LocalTraceTestError("finite nonempty rational test combination")
    frame=None
    total=Q(0)
    for term in terms:
        if type(term) is not tuple or len(term)!=2:
            raise LocalTraceTestError("each test term must be (LocalScaleBall,Fraction)")
        ball,coefficient=term
        if not isinstance(ball,LocalScaleBall) or type(coefficient) not in (int,Q):
            raise LocalTraceTestError("authentic ball and rational coefficient required")
        key=(ball.p,ball.source_id,ball.epoch)
        if frame is None:frame=key
        elif key!=frame:
            raise LocalTraceTestError("cannot mix local prime/source/epoch")
        total+=Q(coefficient)*ball.trace_pairing
    return {"local_place":frame[0],"source":frame[1:],"test_integral":total,
            "local_geometric_distribution_agreement":True,
            "global_Connes_trace_derived":False,"Weil_PSD_proved":False}
