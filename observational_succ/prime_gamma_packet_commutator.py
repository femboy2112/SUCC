"""Source-relevant noncommutation: true prime-2 edge swap versus Gamma OU.

A rigorous one-point lower bound on [A_b,E_(1/2)] f, extended by
continuity to a positive-measure set. Every statement preserves b=log 2
and the original kernel convention; no zero-data or artificial Gram.
"""
from fractions import Fraction as F


class NoncommutationError(ValueError):
    pass


def rational(x):
    if type(x) not in (int,F):
        raise NoncommutationError("exact rational source bounds only")
    return F(x)


def first_gamma_rung_prime_commutator(b_lower,b_upper):
    """Strict lower bound 3/16 for [A_b,E_(1/2)]1_[-1/8,1/8](-3/8).

    5/8<b<3/4: support f lies in unshifted center, hence A_b f=0.
    Set x=-3/8 and z=x+b in (1/4,3/8), with y in [-1/8,1/8].
    Then 0<z-y<1/2, exp(-(z-y)/2)>1-(z-y)/2>3/4.
    Integrated length 1/4 => [A_b,E]f(x)>3/16.
    Continuity of E f makes the commutator NONZERO on a set of measure>0.
    """
    lo,hi=rational(b_lower),rational(b_upper)
    if not (F(5,8)<lo<=hi<F(3,4)):
        raise NoncommutationError("true prime-edge geometry 5/8 < b < 3/4 required")
    x=-F(3,8)
    zlo,zhi=x+lo,x+hi
    left,right=-F(1,8),F(1,8)
    max_distance=zhi-left
    if not (zlo>right and max_distance<F(1,2)):
        raise ArithmeticError("wrong actual source center/edge geometry")
    # e^-t >= 1-t for t>=0, strictly > if t>0.
    kernel_floor=1-max_distance/2
    point_lower=(right-left)*kernel_floor
    if not point_lower>F(3,16):
        raise ArithmeticError("nonzero Gamma-prime commutator not certified")
    return {
        "gamma_rung_index":0,
        "alpha":"1/2",
        "true_prime_shift_interval":(str(lo),str(hi)),
        "test_source_center_indicator_support":("-1/8","1/8"),
        "test_point":str(x),
        "shifted_test_point_interval":(str(zlo),str(zhi)),
        "gamma_integral_strict_lower":str(point_lower),
        "uniform_3_over_16_strict":True,
        "prime_shift_annihilates_original_center_test":True,
        "prime_shift_and_gamma_rung_commute":False,
        "separate_prime_swap_eigenspaces_gamma_invariant_proved":False,
        "RH_proved":False,
    }


def original_source_commutator_witness():
    from . import source_weil_hierarchy as src
    from .tate_suzuki_shorting import verify_original_suzuki_source
    sha=verify_original_suzuki_source()["source_git_blob"]
    if sha!="0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise NoncommutationError("original signed Suzuki source mismatch")
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise NoncommutationError("fake or missing prime 2")
    b=src.log2_iv()
    ans=first_gamma_rung_prime_commutator(b.lo,b.hi)
    ans["source_git_blob"]=sha
    ans["source_type"]="ORIGINAL_PRIME_TWO_AND_FIRST_REAL_GAMMA_OU"
    return ans
