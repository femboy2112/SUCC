"""Authentic real Gamma Zeno singularity and local source-contact cancellation.

The bare Gamma geometric ladder diverges at x=0. For the *local germ*
h(x)=1 near 0, the true Suzuki renormalized difference
D_h(x)=h(x)+h(-x)-2 exp(-x/2)h(0)=2(1-e^(-x/2))
cancels the 1/x kernel singularity, and the product tends to 1/2.

The constant local germ is NOT a globally compact test function and this
does not evaluate the full signed Weil distribution or prove RH.
"""
from __future__ import annotations
from fractions import Fraction as Q
from .source_weil_hierarchy import exp_neg, WeilHierarchyError

class ZenoContactError(ValueError):pass


def source_gamma_contact(n):
    if type(n) is not int or not 1<=n<=16:
        raise ZenoContactError("positive dyadic probe depth 1..16 required")
    x=Q(1,2**n)
    half=exp_neg(x/2)
    twice=exp_neg(2*x)
    den=1-twice
    if den.lo<=0:raise ZenoContactError("source kernel denominator not certified positive")
    k=half/den
    difference=2*(1-half)
    integrand=difference*k
    if difference.lo<=0 or integrand.lo<=0:
        raise ZenoContactError("source analytic cancellation sign not certified")
    return {
        "source":"GENUINE_COMPLETED_REAL_GAMMA_LOCAL_GERM",
        "probe_depth":n,
        "distance_to_contact":x,
        "bare_gamma_kernel_interval":(k.lo,k.hi),
        "renormalized_difference_interval":(difference.lo,difference.hi),
        "renormalized_product_interval":(integrand.lo,integrand.hi),
        "analytic_limit_from_classical_elementary_exp":"1/2",
        "actual_contact_value_at_x_zero_directly_evaluated":False,
        "original_test_compact_support_authenticated":False,
        "full_signed_weil_form_identified":False,
        "rh_proved":False,
    }


def false_bare_at_contact():
    """Reject undefined 0/0 or bare infinity at the contact point."""
    raise ZenoContactError(
        "the bare real Gamma kernel at x=0 has no finite direct value; "
        "source-preserving test subtraction and limit theorem required")
