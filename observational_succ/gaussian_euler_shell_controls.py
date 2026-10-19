"""Exact Q(i) local Euler source: ramified 2 vs split 5 vs inert 3.

Classical Dedekind zeta_Q(i)=zeta_Q L(s,chi_-4) on Re(s)>1, one
frozen prime-power shell at a time. This is a bounded finite arithmetic
cross-check, NOT a completed Weil source intertwiner or an RH result.
"""
from fractions import Fraction as F
from .gaussian_prime_two_density import true_prime, local_prime_half_density_square

class GaussianEulerError(ValueError):
    pass

def chi_minus_four(p):
    p=true_prime(p)
    if p==2:return 0
    return 1 if p%4==1 else -1

def splitting_type(p):
    c=chi_minus_four(p)
    return "RAMIFIED_NORM_P" if c==0 else (
        "SPLIT_TWO_NORM_P" if c==1 else "INERT_ONE_NORM_P_SQUARED")

def gaussian_norm_shell_multiplier(p,k):
    """The exact coefficient times log(p) at ideal norm p^k.

    From -d/ds log(zeta_Q,p(s)*L_p(s,chi_-4)):
      coefficient at p^k = (1+chi_-4(p)^k) log p.
    """
    c=chi_minus_four(p)
    if type(k) is not int or k<1:
        raise GaussianEulerError("positive prime-power depth")
    return 1+c**k

def gaussian_vs_rational_local(p,sigma=2,depth=6):
    """Exact rational local Euler comparison at the convergent s=sigma."""
    p=true_prime(p)
    if type(sigma) is not int or sigma<2 or type(depth) is not int or depth<1:
        raise GaussianEulerError("convergent integer sigma and finite positive source depth")
    c=chi_minus_four(p);t=F(1,p**sigma)
    original=1/(1-t)
    twisted=1/(1-c*t)
    gaussian=original*twisted
    if c==0:separate=1/(1-t)
    elif c==1:separate=1/(1-t)**2
    else:separate=1/(1-t*t)
    if gaussian!=separate:
        raise ArithmeticError("local Gaussian splitting Euler factor mismatch")
    coefficients=tuple(gaussian_norm_shell_multiplier(p,k) for k in range(1,depth+1))
    if c==0 and coefficients!=(1,)*depth:
        raise ArithmeticError("ramified 2 failed rational zeta tower equality")
    return {"prime":p,"chi_minus_four":c,"splitting_type":splitting_type(p),
        "s":sigma,"depth":depth,"euler_Q":str(original),
        "chi_local":str(twisted),"euler_Qi":str(gaussian),
        "euler_Qi_direct_split_formula":str(separate),
        "coefficients_of_log_p_by_integer_norm_exponent":coefficients,
        "squared_half_density_by_norm_exponent":
            tuple(str(local_prime_half_density_square(p,k)) for k in range(1,depth+1)),
        "all_source_norms_finite":True,
        "full_completed_Weil_intertwiner_constructed":False,"RH_proved":False}

def original_source_ramified_two_tower(depth=4):
    if type(depth) is not int or not 1<=depth<=10:
        raise GaussianEulerError("finite genuine source depth")
    from . import source_weil_hierarchy as src
    from .tate_suzuki_shorting import verify_original_suzuki_source
    sha=verify_original_suzuki_source()["source_git_blob"]
    if sha!="0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise GaussianEulerError("mutant source SHA")
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise GaussianEulerError("first prime activation not original")
    if any(src.real_prime_power(2**k)!=2 for k in range(1,depth+1)):
        raise GaussianEulerError("source true 2^k tower changed")
    if src.real_prime_power(6) is not None:
        raise GaussianEulerError("fabricated Gaussian composite 6 impulse")
    r=gaussian_vs_rational_local(2,depth=depth)
    if not all(v==1 for v in r["coefficients_of_log_p_by_integer_norm_exponent"]):
        raise GaussianEulerError("first prime Gaussian-to-rational tower not matched")
    return {"source_sha":sha,"original_rational_prime2_full_tower":True,
        "gaussian_prime_ideal_norm2_tower_equal_by_LOG_DERIVATIVE":True,
        "rational_2_weights_squared":r["squared_half_density_by_norm_exponent"],
        "rational_prime2_W_E_I_L_prime_contact_replaced":False,
        "full_adelic_gamma_poles_completed":False,
        "RH_proved":False}
