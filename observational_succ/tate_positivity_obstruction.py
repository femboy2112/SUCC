"""Exact receipts for a scoped Tate-to-Weil positivity obstruction.

The analytic proof is in reviews/2026-10-15_TATE_WEIL_POSITIVITY_OBSTRUCTION.md.
For D=x*d/dx+1/2 and G=exp(-pi*x*x), A=(16/3)(D^2-1/16)
preserves Fourier self-duality and origin/integral normalization. Its
Mellin multiplier P(s)=1+(16/3)s(s-1) preserves the poles and every finite
Euler factor but adds auxiliary roots at 1/4,3/4. The source A^N G is
SIGNED, not a positive Gaussian-mixture claim.

These finite rational identities certify the arithmetic parts of the
paper argument. They do not prove the Fourier/Mellin/explicit-formula
theorems by computation and never input any nontrivial zeta-zero positions.
"""
from __future__ import annotations

from fractions import Fraction as F

from .shadow_archimedean_tests import polynomial_eval, rising


def _rational(value: int | F) -> F:
    if type(value) not in (int, F):
        raise ValueError("Exact rational coefficients required")
    return F(value)


def _polynomial(coefficients: tuple[int | F, ...]) -> tuple[F, ...]:
    if type(coefficients) is not tuple or not coefficients:
        raise ValueError("Nonempty exact coefficient tuple required")
    result = tuple(_rational(x) for x in coefficients)
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]
    return result


def dilation_polynomial(coefficients: tuple[int | F, ...]) -> tuple[F, ...]:
    """D[q(u)e^-u]=[2u q'(u)+(1/2-2u)q(u)]e^-u, u=pi*x^2."""
    p = _polynomial(coefficients)
    out = [F(0)] * (len(p) + 1)
    for k, value in enumerate(p):
        out[k] += (2*k + F(1, 2))*value
        out[k+1] -= 2*value
    return _polynomial(tuple(out))


def normalized_source_operator(coefficients: tuple[int | F, ...]) -> tuple[F, ...]:
    """Apply A=(16/3)(D^2-1/16) in the polynomial-times-Gaussian basis."""
    p = _polynomial(coefficients)
    d2 = dilation_polynomial(dilation_polynomial(p))
    return _polynomial(tuple(F(16, 3)*(value - (p[k]/16 if k < len(p) else 0))
                             for k, value in enumerate(d2)))


def relative_gaussian_mellin(coefficients: tuple[int | F, ...], s: int | F) -> F:
    """Exact Gamma-normalized polynomial Mellin law for real rational s>0.

    Integral over R^x with dx/|x| equals Gamma_R(s) times this rational.
    The Gamma moment identity is a classical analytic input.
    """
    p, ss = _polynomial(coefficients), _rational(s)
    if ss <= 0:
        raise ValueError("Actual Mellin integral requires s>0")
    return sum((value*rising(ss/2, k) for k, value in enumerate(p)), F(0))


def normalized_multiplier(s: int | F) -> F:
    """P(s)=1+(16/3)s(s-1), a polynomial defined at every rational s."""
    ss = _rational(s)
    return 1 + F(16, 3)*ss*(ss-1)


def _multiply(a: tuple[F, ...], b: tuple[F, ...]) -> tuple[F, ...]:
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def _integral(p: tuple[F, ...], lower: F, upper: F) -> F:
    """Exact monomial antiderivatives, independent of a numeric quadrature."""
    return sum((c*(upper**(k+1)-lower**(k+1))/(k+1)
                for k, c in enumerate(p)), F(0))


def odd_test_moments() -> dict:
    """f=x(1-x^2)^3 on [-1,1], with its exact L2 and derivative norms."""
    f = tuple(F(x) for x in (0, 1, 0, -3, 0, 3, 0, -1))
    derivative = tuple(k*f[k] for k in range(1, len(f)))
    half_first = _integral((F(0),)+f, F(0), F(1))
    l2 = _integral(_multiply(f, f), F(-1), F(1))
    derivative_l2 = _integral(_multiply(derivative, derivative), F(-1), F(1))
    return {"test_polynomial": f, "derivative_polynomial": derivative,
            "positive_half_first_moment": half_first,
            "l2_squared": l2, "derivative_l2_squared": derivative_l2}


def positivity_obstruction_certificate(multiplicity: int = 4096) -> dict:
    """Finite rational receipt for the complete signed-source countermodel.

    Analytic inequalities from the review are required hypotheses behind
    the interpretation of these bounds; no finite source-only computation
    substitutes for those proofs. A^multiplicity G need not be expanded.
    """
    if type(multiplicity) is not int or not 1 <= multiplicity <= 1_000_000:
        raise ValueError("Declare a positive finite multiplicity <= 1000000")
    moments = odd_test_moments()
    b, c = moments["l2_squared"], moments["derivative_l2_squared"]
    a = F(1, 4)
    transform_lower = 2*a*moments["positive_half_first_moment"]
    divisor_upper = -2*transform_lower**2
    # log(p)/sqrt(n)<p at n=2,3,4,5,7,8; base primes sum to 21.
    prime_labels = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2))
    prime_coefficient = 2*sum(p for _, p in prime_labels)
    canonical_upper = c + (17+prime_coefficient)*b
    if not canonical_upper < 4:
        raise AssertionError("Complete canonical source upper bound was lost")
    complete_upper = canonical_upper + multiplicity*divisor_upper
    coarse_upper = F(4) + multiplicity*divisor_upper
    q1 = normalized_source_operator((1,))
    if q1 != (F(1), F(-32), F(64, 3)):
        raise AssertionError("Wrong differential source multiplier")
    if (normalized_multiplier(0), normalized_multiplier(1)) != (1, 1):
        raise AssertionError("Pole residues changed")
    if normalized_multiplier(a) != 0 or normalized_multiplier(1-a) != 0:
        raise AssertionError("Polynomial auxiliary divisor changed")
    return {
        "multiplicity": multiplicity,
        "source_polynomial_first_iterate": q1,
        "first_iterate_ratio_at_u_1": polynomial_eval(q1, F(1)),
        "source_is_declared_signed": True,
        "finite_euler_factors_unchanged": True,
        "origin_and_integral_normalization": F(1),
        "pole_multiplier_values": (normalized_multiplier(0), normalized_multiplier(1)),
        "first_iterate_mellin_multiplier_s2": normalized_multiplier(2),
        "derived_auxiliary_polynomial_roots": (a, 1-a),
        "odd_test_moments": moments,
        "prime_power_support_envelope": prime_labels,
        "transform_at_quarter_lower_bound": transform_lower,
        "added_divisor_form_upper_bound": divisor_upper,
        "canonical_complete_form_strict_upper_bound": canonical_upper,
        "modified_complete_form_strict_upper_bound": complete_upper,
        "coarse_modified_strict_upper_bound": coarse_upper,
        "modified_complete_form_negative": complete_upper <= 0,
        "analytic_proof": "reviews/2026-10-15_TATE_WEIL_POSITIVITY_OBSTRUCTION.md",
        "actual_zeta_zero_positions_used": False,
        "canonical_weil_positivity_proved": False,
        "RH_proved": False,
    }
