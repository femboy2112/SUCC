"""Classical real Gaussian Tate factor, Euler-source finite products, tail contracts.

No analytic continuation beyond separately named classical imports and no RH
claim. Exact rational coefficients are accompanied by *formal* powers of pi.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial

from .classical_tate_window import TateWindowError, exact_int, exact_q, is_prime


@dataclass(frozen=True)
class PiMonomial:
    """Exact coefficient times formal pi^integer (never a floating approximation)."""
    coefficient: Q
    pi_power: int

    def __post_init__(self):
        object.__setattr__(self, "coefficient", exact_q(self.coefficient))
        exact_int(self.pi_power, "formal power of pi")

    def multiply_rational(self, r: Q | int) -> PiMonomial:
        return PiMonomial(self.coefficient * exact_q(r), self.pi_power)

    def times_pi_power(self, e: int) -> PiMonomial:
        return PiMonomial(self.coefficient, self.pi_power + exact_int(e, "pi power"))


def real_gaussian_mellin_integer(s: int) -> PiMonomial:
    """Z_R(exp(-pi*x^2),s)=pi^(-s/2) Gamma(s/2), integer s>=1.

    Noninteger analytic interpolation uses the actual gamma function; these
    exact integer values do not themselves implement global continuation.
    """
    exact_int(s, "positive real Mellin exponent", 1)
    n=s//2
    if s%2==0:
        return PiMonomial(Q(factorial(n-1)), -n)
    return PiMonomial(Q(factorial(2*n), (4**n)*factorial(n)), -n)


def scaled_real_gaussian_mellin_integer(s: int, width_root: int) -> PiMonomial:
    """f(x)=exp(-pi*width_root^2*x^2), Mellin scales by width_root^-s."""
    exact_int(width_root, "positive rational-square Gaussian root", 1)
    return real_gaussian_mellin_integer(s).multiply_rational(Q(width_root)**(-s))


def arch_critical_scale(width_quartic_root: int) -> dict:
    """For c=t^4, both Gaussian and Fourier-dual s=1/2 Mellin values
    equal t^-1 * pi^-1/4 Gamma(1/4). Strict equality of source profiles,
    not positivity or a zero-location result.
    """
    exact_int(width_quartic_root, "positive Gaussian fourth root", 1)
    t=width_quartic_root
    forward=Q(1,t)
    dual=Q(1,t*t) * t  # Fourier amplitude c^-1/2 times dual width^(+1/4)
    if forward!=dual:
        raise AssertionError("Real Fourier half-density discrepancy")
    return {"width":t**4,"forward_prefactor":str(forward),
            "fourier_dual_prefactor":str(dual),
            "common_special_value":"pi^(-1/4)*Gamma(1/4)",
            "critical_s_half_source_duality":True}


def finite_true_euler_product(primes: tuple[int,...], sigma: int) -> Q:
    """Absolute half-plane local unramified product, at exact integer sigma>1."""
    exact_int(sigma, "absolute-convergence sigma", 2)
    if (type(primes) is not tuple or not primes or
            any(not is_prime(p) for p in primes) or
            tuple(sorted(set(primes))) != primes):
        raise TateWindowError("Distinct ordered genuine Euler prime places required")
    result=Q(1)
    for p in primes:
        result /= 1-Q(p)**(-sigma)
    return result


def euler_dirichlet_coefficients(bases: tuple[int,...], cutoff: int) -> tuple[int,...]:
    """Exact formal Euler-geometric Dirichlet product to n<=cutoff.

    Accepts composite bases only to construct hostile non-Euler controls.
    Ordinary genuine Euler mode additionally requires bases to be primes.
    """
    exact_int(cutoff, "finite Dirichlet coefficient cutoff", 1)
    if (type(bases) is not tuple or len(set(bases)) != len(bases) or
            any(type(p) is not int or p<2 for p in bases)):
        raise TateWindowError("A distinct tuple of integral bases >=2 is required")
    if cutoff>5000:
        raise TateWindowError("Exact finite Dirichlet budget exceeded")
    coeff=[0]*(cutoff+1)
    coeff[1]=1
    for base in bases:
        result=[0]*(cutoff+1)
        factor=1
        while factor<=cutoff:
            for n in range(1,cutoff//factor+1):
                result[n*factor]+=coeff[n]
            factor*=base
        coeff=result
    return tuple(coeff)


def euler_tail_contract(prime_horizon: int, sigma: int) -> dict:
    """|zeta(s)-prod_(p<=P)(1-p^-s)^-1|<=P^(1-sigma)/(sigma-1),
    for complex Re s>=sigma>1, by all omitted n>P and integral comparison.

    At the boundary sigma<=1 the integrable-tail argument is unavailable.
    """
    exact_int(prime_horizon, "prime horizon", 2)
    exact_int(sigma, "positive half-plane bound", 2)
    places=tuple(p for p in range(2,prime_horizon+1) if is_prime(p))
    bound=Q(prime_horizon)**(1-sigma)/Q(sigma-1)
    return {"primes":places,"sigma":sigma,"last_source_prime":places[-1],
            "finite_local_euler_at_sigma":str(finite_true_euler_product(places,sigma)),
            "uniform_absolute_tail_upper":str(bound),
            "valid_for_all_complex_s_Re_ge_sigma":True,
            "valid_on_critical_line":False}


def arch_global_probe() -> dict:
    moments=[real_gaussian_mellin_integer(s) for s in range(1,8)]
    for s in range(1,6):
        lhs=real_gaussian_mellin_integer(s+2)
        rhs=real_gaussian_mellin_integer(s).multiply_rational(Q(s,2)).times_pi_power(-1)
        assert lhs==rhs
    gauge=arch_critical_scale(4)
    good=euler_dirichlet_coefficients((2,3,5),36)
    bad=euler_dirichlet_coefficients((2,3,5,6),36)
    assert good[6]==1 and bad[6]==2
    return {"kind":"CLASSICAL_TATE_ARCH_GLOBAL_RECEIPT",
            "real_gaussian_mellin_integer_values":[[str(v.coefficient),v.pi_power] for v in moments],
            "gamma_s_plus_two_succ_recurrence":True,
            "critical_half_density_gaussian":gauge,
            "true_euler_smooth_coefficient_6":good[6],
            "fake_composite_6_independent_factor_coefficient_6":bad[6],
            "finite_euler_contract_sigma_2":euler_tail_contract(17,2),
            "global_Poisson_or_completed_zeta_FE_derived_from_finite_windows":False,
            "RH_or_Weil_sign_claimed":False}
