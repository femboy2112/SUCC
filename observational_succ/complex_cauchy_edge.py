"""A constructive Cauchy-name specimen of C from the smaller field Q(i).

CLASSICAL theorem:
  metric_completion(Q(i), |.|_complex) ~= C
as complete topological fields. Rational Gaussian pairs alone give Q(i),
NOT C. This exact integer-sqrt construction produces one new point
sqrt(2)+i*r using a computable Cauchy NAME, but does not enumerate all C,
or identify a physical/analytic carrier as accessible.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

from .edge_carrier_reconstruction import (
    EdgeCarrierError, RationalSpan, GaussianRational,
)


@dataclass(frozen=True)
class GaussianCauchyRoot2:
    """Finite code for sqrt(2)+i*b, b a declared exact rational."""
    imaginary: RationalSpan
    source_id: str = "Q(i)-completion"

    def __post_init__(self) -> None:
        if not isinstance(self.imaginary,RationalSpan) or type(self.source_id) is not str or not self.source_id.strip():
            raise EdgeCarrierError("Cauchy name requires an exact Q(i) imaginary source")

    def stage(self, precision: int) -> dict:
        """Returns rational Gaussian lower and upper witnesses, no float."""
        if type(precision) is not int or not 0 <= precision <= 100:
            raise EdgeCarrierError("A bounded nonnegative decimal precision is required")
        D=10**precision
        a=isqrt(2*D*D)
        lower=F(a,D)
        upper=F(a+1,D)
        if not (lower*lower < 2 < upper*upper):
            raise AssertionError("Exact sqrt2 enclosure failed")
        approx=GaussianRational(RationalSpan(a,D),self.imaginary)
        return {
            "depth":precision, "source_id":self.source_id,
            "real_lower":lower,"real_upper":upper,
            "imaginary":self.imaginary.as_fraction(),
            "q_i_approximation":approx,
            "real_error_upper":F(1,D),
            "square_lower":lower*lower,"square_upper":upper*upper,
            "strict_positive_enclosure":True,
            "full_complex_plane_generated_by_one_program":False,
            "RH_proved":False,
        }

    def cauchy_receipt(self, fine:int, coarse:int) -> dict:
        """Uniform rate |z_m-z_n| < 10^-n for m>=n (imag equal)."""
        if (type(fine) is not int or type(coarse) is not int or
            fine<coarse or coarse<0):
            raise EdgeCarrierError("Need integer fine>=coarse>=0")
        a=self.stage(fine)
        b=self.stage(coarse)
        gap=abs(a["real_lower"]-b["real_lower"])
        bound=F(1,10**coarse)
        if gap >= bound and fine > coarse:
            raise AssertionError("Root2 approximants violate explicit Cauchy rate")
        return {
            "fine":fine,"coarse":coarse,
            "two_q_i_points":(a["q_i_approximation"].as_pair(),b["q_i_approximation"].as_pair()),
            "exact_difference":gap,
            "guaranteed_error":bound,
            "cauchy_rate_proved_by_sqrt2_enclosures":True,
            "limit_in_Q_i":False,
            "limit_in_C":"CLASSICAL_COMPLETION_THEOREM",
            "RH_proved":False,
        }


def sqrt2_is_not_gaussian_rational() -> dict:
    """Elementary parity proof, not finite rational search.

    If real sqrt(2)=a/b for coprime integers, a^2=2b^2 forces a even,
    so b even too: contradiction. In Q(i), real elements are rational
    by definition. Thus sqrt(2)+i*r for rational r is outside Q(i).
    """
    return {
        "target":"sqrt(2)+i*r, rational r",
        "real_sqrt2_irrational":"CLASSICAL_PARITY_PROOF",
        "target_not_in_Q_i":True,
        "target_in_metric_completion_of_Q_i":"CLASSICAL_COMPLETENESS_OF_C",
        "computable_cauchy_name_exists":True,
        "one_name_generates_every_complex_number":False,
        "RH_proved":False,
    }
