"""Suzuki finite-window arithmetic wavefront, exact rational shape/energy receipts.

The actual coefficient for n=p^j is c_n=log(p)/sqrt(n) and its translation
length is log(n). We certify all geometric coefficients as exact rational
multiples of these *symbolic* transcendental source quantities. No zeta-zero
coordinates, positivity assertion, or floating-point proof substitution.

Primary: Suzuki, Weil's quadratic form via the screw function,
arXiv:2606.09096v3, equations (1.3), (2.5), (8.7).
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt


class SuzukiWavefrontError(ValueError):
    pass


def positive_integer(n: int, lo: int = 1, hi: int = 1_000_000) -> int:
    if type(n) is not int or not lo <= n <= hi:
        raise SuzukiWavefrontError(f"expected integer between {lo} and {hi}")
    return n


def exact_fraction(x) -> Q:
    if type(x) not in (int, Q):
        raise SuzukiWavefrontError("only integers or exact Fraction inputs")
    return Q(x)


def prime_power(n: int) -> tuple[int, int] | None:
    """Return (genuine prime p, exponent j), or None for composites like 6."""
    positive_integer(n, 2)
    d = 2
    while d <= isqrt(n) and n % d:
        d += 1
    if d > isqrt(n):
        return (n, 1)  # n genuinely prime
    exponent = 0
    remainder = n
    while remainder % d == 0:
        remainder //= d
        exponent += 1
    return (d, exponent) if remainder == 1 else None


def source_jet(n: int) -> dict:
    """Coefficient is exactly 'log(p)/sqrt(n)' with location 'log(n)' when p^j."""
    pp = prime_power(n)
    if pp is None:
        return {"n": n, "prime_power": False, "weight": "0",
                "source_phase": "not-a-prime-power", "authentic": True}
    p, j = pp
    return {"n": n, "prime_power": True, "p": p, "exponent": j,
            "weight": f"log({p})/sqrt({n})", "source_phase": f"log({n})",
            "authentic": True}


def ratio_window(n: int, a_over_log_n) -> dict:
    """Exact source shape at a = r log(n); requires 1/2 < r < 1.

    Only states local to this ONE wavefront are described. Other active
    prime jets have to be included separately for a completed Weil form.
    """
    jet = source_jet(n)
    if not jet["prime_power"]:
        raise SuzukiWavefrontError("only genuine p^j jets can enter source")
    r = exact_fraction(a_over_log_n)
    if not Q(1, 2) < r < 1:
        raise SuzukiWavefrontError("disjoint-endpoint regime requires 1/2 < a/log n < 1")
    delta = 2*r - 1
    # Geometry after coordinates x/log(n): interval [-r,r], shift 1.
    return {"n": n, "r": str(r), "delta_over_log_n": str(delta),
            "g_raw_HS_sq_over_c_sq_log_n_fourth": str(delta**4 / 6),
            "g_zero_mean_HS_upper_same": True,
            "differentiated_op_norm_over_c": "1",
            "symmetric_tent_prime_rayleigh_over_c": "-1",
            "antisymmetric_tent_prime_rayleigh_over_c": "+1",
            "finite_source_jet": jet, "RH_proved": False}


def first_prime_window(r) -> dict:
    """Prove only jet 2 is active when a=r log2, 1/2<r<1.

    2a<log3 iff 2^(2*num)<3^den, an exact INTEGER comparison.
    """
    r = exact_fraction(r)
    v = ratio_window(2, r)
    if not (2 ** (2 * r.numerator) < 3 ** r.denominator):
        raise SuzukiWavefrontError("prime 3 or a later jet may be active")
    v.update({"only_active_arithmetic_jet": 2,
              "next_jet_excluded_by_exact_integer_inequality":
                  f"2^{2*r.numerator}<3^{r.denominator}",
              "pole_gamma_part_included": False})
    return v


def tent_certificate(delta) -> dict:
    """Exact endpoint tents in units of length ell=log(n):

    t(y)=min(y,delta-y) on 0<y<delta, 0 otherwise.
    v=t_L +/- t_R, where t_R(x)=t_L(x-ell).
    These piecewise-linear functions belong to H_0^1(-a,a).
    """
    delta = exact_fraction(delta)
    if not 0 < delta < 1:
        raise SuzukiWavefrontError("tent geometry needs 0<delta<1")
    norm2 = delta**3 / 6                 # two tents
    derivative2 = 2*delta                # physical derivative scales by 1/ell
    overlap = delta**3 / 12              # one shifted pair
    return {"delta_over_ell": str(delta),
            "norm2_in_dimensionless_variable": str(norm2),
            "shift_overlap_in_dimensionless_variable": str(overlap),
            "H1_seminorm_sq_in_dimensionless_variable": str(derivative2),
            "H1_over_L2_in_dimensionless_variable": str(derivative2/norm2),
            "prime_quadratic_symmetric_over_c": str(-2*overlap),
            "prime_quadratic_antisymmetric_over_c": str(2*overlap),
            "symmetric_Rayleigh_over_c": str(-2*overlap/norm2),
            "antisymmetric_Rayleigh_over_c": str(2*overlap/norm2),
            "zero_locations_read": False, "RH_proved": False}


def positive_dilation_log_energy_envelope(delta, cutoff_exponent: int,
                                           norm_sq, log_energy_ceiling) -> dict:
    """Certified bound requiring an externally justified E(v) upper bound.

    For Fourier E(v) = int log(e+|xi|)|vhat|^2/(2pi),
    and a single jet Q_n, |Q_n|/c_n <= (4/3)*delta*2^m*||v||²
      +(3/m)*E(v), since pi>3 and log2>2/3.
    The input log_energy_ceiling is a HYPOTHESIS, not a measured quantity.
    delta is an absolute real-coordinate endpoint-strip length, not delta/ell.
    """
    d, n2, E = [exact_fraction(v) for v in
                (delta, norm_sq, log_energy_ceiling)]
    positive_integer(cutoff_exponent, 1, 100)
    if d <= 0 or n2 < 0 or E < n2:  # E >= ||v||² from log(e+|xi|)>=1
        raise SuzukiWavefrontError("invalid length/norm/energy ceiling")
    m = cutoff_exponent
    c_norm = Q(4, 3)*d*(2**m)
    c_energy = Q(3, m)
    return {"cutoff_R": 2**m, "delta": str(d),
            "norm_sq": str(n2), "assumed_log_energy_ceiling": str(E),
            "L2_coefficient": str(c_norm), "log_energy_coefficient": str(c_energy),
            "certified_abs_prime_form_over_c_upper": str(c_norm*n2+c_energy*E),
            "conditional_on_energy_ceiling": True, "RH_proved": False}


def full_strength_energy_debt(power: int) -> dict:
    """Choose actual endpoint width delta=2^(-2m); full-strength prime
    Rayleigh implies an exact lower bound on Fourier log-energy per unit mass.
    """
    positive_integer(power, 1, 40)
    m = power
    delta = Q(1, 2**(2*m))
    low = Q(m, 3)*(1-Q(4, 3)*delta*(2**m))
    return {"m": m, "delta": str(delta),
            "needed_log_energy_over_mass_at_full_prime_shift_at_least": str(low),
            "genuine_half_density_factor_not_canceled": "log(p)/sqrt(p^j)",
            "inequality_source": "cutoff Fourier norm and log2>2/3, pi>3",
            "RH_proved": False}


def sampled_fake_source_control() -> dict:
    source = [source_jet(n) for n in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16)]
    true = [x for x in source if x["prime_power"]]
    impostors = [x["n"] for x in source if not x["prime_power"]]
    return {"tested": source, "genuine": [x["n"] for x in true],
            "correctly_excluded": impostors,
            "fake_composite_6_is_zero": 6 in impostors,
            "source_log_phase_not_fitted": True,
            "source_half_density_not_fitted": True,
            "no_unknown_zero_positions": True, "RH_proved": False}


def complete_receipt() -> dict:
    return {"source": "Suzuki 2606.09096v3 equations 1.3/2.5/8.7",
            "first_window": first_prime_window(Q(3, 5)),
            "tent": tent_certificate(Q(1, 5)),
            "sharp_wavefront_onset": {"at_delta_zero": "zero", "for_every_delta_positive":
                                       "operator norm c_n; raw HS norm c_n*delta^2/sqrt(6)"},
            "log_energy_debt": [full_strength_energy_debt(m) for m in (2, 4, 8, 16)],
            "fake_source_controls": sampled_fake_source_control(),
            "completed_archimedean_source_fully_certified": False,
            "global_relative_weil_positivity": False,
            "nontrivial_zero_positions_used": False,"RH_proved": False}


def validate_arithmetic_jet(n:int, claimed_prime:int,
                            claimed_exponent:int, claimed_density_exponent,
                            claimed_phase_n:int)->dict:
    """Typed semantic mutation gate; compare declared source labels exactly.

    claimed_phase_n is the integer index of 'log(claimed_phase_n)',
    not a fitted floating phase. Genuine source requires phase log(n).
    """
    j=source_jet(n)
    positive_integer(claimed_prime,2)
    positive_integer(claimed_exponent,1,100)
    positive_integer(claimed_phase_n,2)
    d=exact_fraction(claimed_density_exponent)
    good=bool(j['prime_power'] and j['p']==claimed_prime and
              j['exponent']==claimed_exponent and d==Q(1,2) and
              claimed_phase_n==n)
    return {'n':n,'accepted':good,
            'fake_composite_rejected':not j['prime_power'],
            'wrong_half_density_rejected':d!=Q(1,2),
            'wrong_log_phase_rejected':claimed_phase_n!=n,
            'truth_is_source_typed_not_fit_to_zeros':True,'RH_proved':False}
