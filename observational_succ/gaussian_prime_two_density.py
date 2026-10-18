"""Gaussian 2=1^2+1^2 as form-preserving normalized source transport.

The Weil p^-1/2 applies to ALL rational primes, including Gaussian-inert 3.
This is a calibrated geometric REALIZATION of one half-density magnitude,
not a derivation of Suzuki's signed prime term or its completed Weil form.
"""
from fractions import Fraction as F


class GaussianDensityError(ValueError):
    pass


def integer(x):
    if type(x) is not int:raise GaussianDensityError("exact integer lattice only")
    return x


def gaussian_multiply_matrix(a,b):
    a,b=integer(a),integer(b)
    return ((a,-b),(b,a))


def matrix_product(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1))
                       for j in (0,1)) for i in (0,1))


def transpose(A):return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))


def lattice_norm_and_half_density(a,b):
    """M_z^T M_z=N(z)I, det M_z=N(z), isometric M_z/sqrt(N)."""
    a,b=integer(a),integer(b);norm=a*a+b*b
    if norm==0:raise GaussianDensityError("zero is not an index-bearing dilation")
    M=gaussian_multiply_matrix(a,b)
    gram=matrix_product(transpose(M),M)
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    if gram!=((norm,0),(0,norm)) or det!=norm:
        raise ArithmeticError("Gaussian norm/area form transport mismatch")
    return {"gaussian_element":(a,b),"matrix":M,
            "norm":norm,"lattice_index":det,
            "normalized_symmetric_form":"M^T M / N = I",
            "normalized_squared_amplitude":str(F(1,norm)),
            "complex_modulus_squared":norm,
            "signed_Weil_form_constructed":False,"RH_proved":False}


def true_prime(p):
    if type(p) is not int or p<=1:raise GaussianDensityError("true prime required")
    if any(p%d==0 for d in range(2,__import__("math").isqrt(p)+1)):
        raise GaussianDensityError("reject fake composite primitive")
    return p


def local_prime_half_density_square(p,k=1):
    p=true_prime(p)
    if type(k) is not int or k<1:raise GaussianDensityError("true positive valuation depth")
    return F(1,p**k)


def first_two_step_source():
    """Peano S(S(0))=2, Gaussian pi=1+i and its rotated square.

    SUCCESSOR S^2 and MULTIPLICATIVE Gaussian pi^2 are different actions.
    Half-density numbers coincide for index-two *one* Gaussian step
    and the separate 1D real rational multiplier 2; never identify them.
    """
    M=gaussian_multiply_matrix(1,1)
    square=matrix_product(M,M)
    J=((0,-1),(1,0))
    twice=((2*J[0][0],2*J[0][1]),(2*J[1][0],2*J[1][1]))
    if square!=twice:raise ArithmeticError("Gaussian (1+i)^2=2i false")
    index2=lattice_norm_and_half_density(1,1)
    if index2["normalized_squared_amplitude"]!="1/2":
        raise ArithmeticError("Gaussian index-two half-density wrong")
    # The map image is exactly the even parity sublattice x+y=0 mod2.
    if any(((M[0][0]*u+M[0][1]*v)+(M[1][0]*u+M[1][1]*v))%2
           for u in range(-2,3) for v in range(-2,3)):
        raise ArithmeticError("Gaussian index-two image parity condition wrong")
    return {"additive_two_successor_steps":2,
            "first_nonunit_positive_integer_prime":2,
            "gaussian_prime":(1,1),
            "gaussian_norm":2,
            "first_one_step_index_two_L2_squared_amplitude":"1/2",
            "two_gaussian_multiplicative_steps_matrix":square,
            "two_steps_equal_rational_multiplier_2_up_to_Gaussian_unit":True,
            "additive_S_squared_is_NOT_multiplicative_pi_squared":True,
            "real_line_1D_half_density_2":"1/sqrt(2) (separate carrier)",
            "gaussian_plane_2D_half_density_pi":"1/sqrt(2) (one step)",
            "gaussian_plane_two_step_density":"1/2",
            "Weil_half_density_uniquely_derived_from_Gaussian_2":False,
            "RH_proved":False}


def inert_prime_negative_control():
    """Rational prime 3 is Gaussian inert: no a²+b²=3, yet Weil 3^-1/2 exists."""
    if any(a*a+b*b==3 for a in range(-2,3) for b in range(-2,3)):
        raise ArithmeticError("Gaussian-inert 3 mutant")
    if local_prime_half_density_square(3)!=F(1,3):
        raise ArithmeticError("true p3 universal half density missing")
    return {"gaussian_norm_3_integer_solution":False,
            "rational_prime_3_original_local_squared_half_density":"1/3",
            "gaussian_norm_geometry_not_universal_explanation":True,
            "RH_proved":False}


def authenticated_two_prime_source():
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from . import source_weil_hierarchy as src
    receipt=verify_original_suzuki_source()
    if receipt["source_git_blob"]!="0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise GaussianDensityError("frozen signed source changed")
    if (src.authenticated_prime_wavefront(F(1,2))!=((2,2),)
         or src.real_prime_power(6) is not None):
        raise GaussianDensityError("authentic source prime-power tape invalid")
    inv=src.sqrt_inverse(2)
    if not inv.lo*inv.lo<=F(1,2)<=inv.hi*inv.hi:
        raise GaussianDensityError("genuine 2 half-density squared not enclosed")
    return {"source_sha":receipt["source_git_blob"],
            "source_weil_prime_wavefront":((2,2),),
            "true_source_sqrt2_inverse_interval":(str(inv.lo),str(inv.hi)),
            "gaussian_squared_normalized_index":"1/2",
            "same_number_not_same_carrier_intertwiner":True,
            "full_signed_Weil_form_identified":False,"RH_proved":False}
