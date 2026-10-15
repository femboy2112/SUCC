"""Two indispensable mathematical limit shapes beyond geometric Zeno.

(1) Holomorphic three-circles: analytic uniqueness is NOT stable numerical
    continuation without a source-certified outer growth bound.
(2) Signed double SUCC ladders: Fubini/limit order can fail even when each
    row and column sum is perfectly finite. No assertion about genuine Weil
    signed sums follows merely from this toy countermodel.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q


class AnalyticShapeError(ValueError):
    pass


def rat(x):
    if type(x) not in (int,Q):
        raise AnalyticShapeError("exact rational input required")
    return Q(x)


def index(n):
    if type(n) is not int or not 0<=n<=1024:
        raise AnalyticShapeError("bounded finite natural index")
    return n


@dataclass(frozen=True)
class EntireMonomialSource:
    """Exact mathematical entire function f(z)=c*(z/scale)^degree."""
    coefficient: Q
    scale: Q
    degree: int

    def __post_init__(self):
        object.__setattr__(self,"coefficient",rat(self.coefficient))
        object.__setattr__(self,"scale",rat(self.scale))
        index(self.degree)
        if self.scale<=0:raise AnalyticShapeError("positive source scale")

    def max_modulus_on_circle(self,r):
        r=rat(r)
        if r<=0:raise AnalyticShapeError("positive circle radius required")
        return abs(self.coefficient)*(r/self.scale)**self.degree

    def three_circle_exact(self,r_small=1,r_middle=2,r_large=4):
        """For r_mid²=r_small*r_large, exact Mmid²=Msmall*Mlarge.

        This equality is special to this monomial source. Hadamard's
        general inequality for holomorphic functions is a classical
        imported theorem, NOT proved by finite monomial tests.
        """
        r1,r2,r3=map(rat,(r_small,r_middle,r_large))
        if not 0<r1<r2<r3 or r2*r2!=r1*r3:
            raise AnalyticShapeError("exact geometric radius interpolation")
        x=self.max_modulus_on_circle(r1)
        y=self.max_modulus_on_circle(r2)
        z=self.max_modulus_on_circle(r3)
        if y*y!=x*z:raise ArithmeticError("analytic monomial source mismatched")
        return {"M_inner":x,"M_middle":y,"M_outer":z,
                "interpolation_squared_upper":x*z,
                "three_circle_theorem_for_arbitrary_holomorphic_input_proved":False,
                "authentic_zeta_global_growth_authenticated":False}

    def claimed_inner_only_stability(self):
        r=self.three_circle_exact()
        return {"inner_value":r["M_inner"],"outer_value":r["M_outer"],
                "middle_value":r["M_middle"],
                "inner_data_alone_certifies_outer":False,
                "source":"EXACT_ENTIRE_MONOMIAL"}


def conditional_three_circle_upper(inner,outer):
    """Theorem schema, not an authenticated growth-measurement instrument.

    If f holomorphic in neighborhood of disk |z|<=4 and
    M(1)<=inner, M(4)<=outer, then M(2)^2<=inner*outer.
    Those assumptions must be *independently* source-certified.
    """
    a,b=rat(inner),rat(outer)
    if a<0 or b<0:raise AnalyticShapeError("nonnegative source sup bounds")
    return {"squared_midpoint_bound_if_premises_hold":a*b,
            "radii":(Q(1),Q(2),Q(4)),
            "outer_bound_source_authenticated":False,
            "holomorphic_domain_source_authenticated":False,
            "source":"CONDITIONAL_HADAMARD_THREE_CIRCLE"}


def signed_double_successor(n,m):
    """Finite rectangle of a_{i,j}=1(j=i)-1(j=i+1).

    Formula S(N,M)=min(N,M)-min(N,M-1). For fixed N, M->inf:
    0. For fixed M>=1, N->inf: 1. Diagonal N=M: 1.
    """
    index(n);index(m)
    if m<1:raise AnalyticShapeError("column horizon M>=1")
    direct=sum((int(j==i)-int(j==i+1)
                for i in range(n) for j in range(m)))
    closed=min(n,m)-min(n,m-1)
    if direct!=closed:raise ArithmeticError("source signed-grid oracle mismatch")
    return {"source":"EXACT_SIGNED_DOUBLE_SUCC",
            "row_horizon":n,"column_horizon":m,
            "signed_rectangle_total":closed,
            "row_first_iterated_limit":0,
            "column_first_iterated_limit":1,
            "Fubini_or_Tonelli_without_signed_absolute_convergence":False}


def signed_double_diagonal(n):
    index(n)
    if n<1:raise AnalyticShapeError("n>=1")
    return {"equal_horizons":signed_double_successor(n,n)["signed_rectangle_total"],
            "one_extra_column":signed_double_successor(n,n+1)["signed_rectangle_total"],
            "joint_limit_exists":False,
            "physical_time_order_is_source_dependent":True}
