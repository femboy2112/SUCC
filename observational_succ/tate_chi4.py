"""Source-exact chi4 Tate test: ramified Fourier, Hecke and theta interfaces.

All exact finite claims use rational/Gaussian-rational arithmetic and existing
SUCC source maps. The all-place theorems and convergence proofs are in
research/2026-10-15/TATE_CHI4_ARITHMETIC_CRUCIBLE.md. Interval overlap is a
consistency check, never a proof of a functional equation or GRH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .all_places_zeta import factors, rational_place_valuations
from .diagonal_adele_zeta import valuation
from .source_character_interaction import character_four, local_chi4_euler
from .source_model_interaction import exponential_moment_tail, upper_exp_neg
from .source_weil_hierarchy import I, iv
from .adelic_gaussian_interval import _gaussian_exp_pi_upper_lower
from .tate_schwartz_functor import PadicBall


class Chi4SourceError(ValueError):
    """Invalid source domain, phase, or finite resource budget."""


@dataclass(frozen=True)
class Chi4TateSource:
    """Declared immutable source identity for the genuine ramified Tate test.

    This is mathematical source provenance, not an authenticated physical
    experiment. Arithmetic, character and conductor are fixed by construction.
    """
    source_id: str = "chi4-standard-Tate"
    epoch: int = 0

    def __post_init__(self) -> None:
        if type(self.source_id) is not str or not self.source_id.strip():
            raise Chi4SourceError("A nonempty source identity is required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise Chi4SourceError("A nonnegative exact source epoch is required")

    @property
    def conductor(self) -> int:
        return 4

    @property
    def parity(self) -> int:
        return 1

    @property
    def root_number(self) -> int:
        return 1

    def two_adic_atoms(self) -> tuple[tuple[int, PadicBall], ...]:
        return tuple((coefficient, PadicBall(2, Q(a), 2, self.source_id, self.epoch))
                     for coefficient, a in ((1, 1), (-1, 3)))

    def local_mellin_receipt(self, s: int, primes: tuple[int, ...]) -> dict:
        _budget(s, 2, 12)
        if type(primes) is not tuple or tuple(sorted(set(primes))) != primes:
            raise Chi4SourceError("Unique sorted finite prime tuple required")
        local = tuple((p, Q(local_chi4_euler(p, s, 2)["full"])) for p in primes)
        return {"source_id": self.source_id, "epoch": self.epoch,
                "finite_places": local, "ramified_place_2_mass": ramified_mellin_mass(),
                "real_factor": "(4/pi)^((s+1)/2)*Gamma((s+1)/2)",
                "ramified_atoms": self.two_adic_atoms(),
                "finite_product_is_all_places": False, "zero_positions_used": False}


def _q(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise Chi4SourceError("Exact integer or rational source required")
    return Q(x)


def _budget(n: int, lo: int, hi: int) -> int:
    if type(n) is not int or not lo <= n <= hi:
        raise Chi4SourceError("Integer resource budget outside declared range")
    return n


def two_adic_hecke(x: int | Q) -> int:
    """chi_2(2^k u)=chi4(u mod 4); it is a nonzero character on Q_2^*."""
    x = _q(x)
    if not x:
        raise Chi4SourceError("A multiplicative character is undefined at zero")
    u = x / Q(2) ** valuation(x, 2)
    residue = (u.numerator * pow(u.denominator, -1, 4)) % 4
    return character_four(residue)


def diagonal_hecke_receipt(x: int | Q) -> dict:
    """Exact reciprocity at a rational diagonal, including sign and ramification."""
    x = _q(x)
    if not x:
        raise Chi4SourceError("Nonzero diagonal rational required")
    arch = 1 if x > 0 else -1
    local = tuple((p, character_four(p) ** (k % 2))
                  for p, k in rational_place_valuations(x).items() if p != 2)
    ramified = two_adic_hecke(x)
    value = arch * ramified
    for _, factor in local:
        value *= factor
    if value != 1:
        raise AssertionError("The Hecke character failed rational triviality")
    return {"rational": x, "real_sign_character": arch,
            "ramified_2_character": ramified, "unramified_factors": local,
            "diagonal_product": value, "zero_positions_used": False}


def ramified_test(x: int | Q) -> int:
    """f_2=chi_2 1_(Z_2^*)=1_(1+4Z_2)-1_(3+4Z_2)."""
    x = _q(x)
    return (int(PadicBall(2, Q(1), 2).contains(x))
            - int(PadicBall(2, Q(3), 2).contains(x)))


def ramified_fourier(xi: int | Q, finite_sign: int = -1) -> tuple[Q, Q]:
    """Direct exact two-coset Fourier transform, as (real, imaginary).

    Default finite minus is the reconstructed adelic convention. Positive
    finite sign is deliberately supported as an adversarial mutation.
    """
    xi = _q(xi)
    if type(finite_sign) is not int or finite_sign not in (-1, 1):
        raise Chi4SourceError("Fourier sign must be +1 or -1")
    roots = ((Q(1), Q(0)), (Q(0), Q(1)),
             (Q(-1), Q(0)), (Q(0), Q(-1)))
    real, imag = Q(0), Q(0)
    for a, coefficient in ((1, 1), (3, -1)):
        term = PadicBall(2, Q(a), 2).fourier(xi)
        if not term.amplitude:
            continue
        phase = -finite_sign * term.phase
        index = (4 * phase) % 4
        if index.denominator != 1:
            raise AssertionError("The supported frequency must have quarter phase")
        z = roots[index.numerator]
        real += coefficient * term.amplitude * z[0]
        imag += coefficient * term.amplitude * z[1]
    return real, imag


def ramified_fourier_closed(xi: int | Q, finite_sign: int = -1) -> tuple[Q, Q]:
    """Proved formula fhat_2(y)=(finite_sign*i/2) f_2(4y)."""
    xi = _q(xi)
    if type(finite_sign) is not int or finite_sign not in (-1, 1):
        raise Chi4SourceError("Fourier sign must be +1 or -1")
    return Q(0), Q(finite_sign, 2) * ramified_test(4 * xi)


def ramified_mellin_mass() -> Q:
    """Integral f_2(x) chi_2(x) |x|^s d^*x=1 for EVERY complex s.

    Each residue 1 or 3 mod 4 has additive mass 1/4; d^*x=2 dx/|x|_2
    gives mass 1/2 on each. There is no 2-Euler denominator, yet the
    ramified place cannot be removed from the Hecke/Fourier construction.
    """
    return sum((Q(1, 2) * ramified_test(a) * two_adic_hecke(a)
                for a in (1, 3)), Q(0))


def source_fourier_multiplier(real_sign: int = 1, finite_sign: int = -1) -> Q:
    """Multiply (2i*real_sign) and (i*finite_sign/2), exactly."""
    for sign in (real_sign, finite_sign):
        if type(sign) is not int or sign not in (-1, 1):
            raise Chi4SourceError("Fourier signs must be +1 or -1")
    return Q(-real_sign * finite_sign)


def logarithmic_source_tape(cutoff: int) -> tuple[tuple[int, int, int], ...]:
    """(n, prime p, chi4(n)) for actual n=p^k, including zero ramified terms.

    The coefficient represented is chi4(p)^k log(p). Analytic summation
    equals -L'/L only in Re(s)>1; this routine performs no continuation.
    """
    _budget(cutoff, 2, 50_000)
    rows = []
    for n in range(2, cutoff + 1):
        fac = factors(n)
        if len(fac) == 1:
            p, k = next(iter(fac.items()))
            sign = character_four(p) ** k
            if sign != character_four(n):
                raise AssertionError("Prime-power source and character disagree")
            rows.append((n, p, sign))
    return tuple(rows)


def validate_coefficient_tape(tape: tuple[int, ...]) -> dict:
    """Compare a candidate a_1,...,a_N against actual chi4 and Euler coherence.

    The multiplicativity witness is useful even before source comparison.
    A completely multiplicative wrong character can pass coherence, so the
    two verdicts are deliberately separate.
    """
    if type(tape) is not tuple or not tape or len(tape) > 2000:
        raise Chi4SourceError("A nonempty coefficient tuple of length <=2000")
    if any(type(x) is not int for x in tape):
        raise Chi4SourceError("Exact integer coefficients required")
    source = next(((n, a, character_four(n)) for n, a in enumerate(tape, 1)
                   if a != character_four(n)), None)
    multiplicative = None
    for a in range(1, isqrt(len(tape)) + 1):
        for b in range(a, len(tape) // a + 1):
            if tape[a*b-1] != tape[a-1] * tape[b-1]:
                multiplicative = (a, b, tape[a*b-1], tape[a-1]*tape[b-1])
                break
        if multiplicative is not None:
            break
    return {"first_source_mismatch": source,
            "multiplicativity_witness": multiplicative,
            "unit_normalization_witness": None if tape[0] == 1 else (1, tape[0], 1),
            "finite_cutoff": len(tape), "global_source_certified": False}


def theta_tail_bound(heat: int | Q, modes: int) -> Q:
    """Bound |Theta(t)-Theta_N(t)| by 4/(3t)*exp(-3t*N^2/4).

    pi>3 and monotone integral comparison suffice, provided 3*t*N^2>=2.
    upper_exp_neg supplies a proved rational exponential majorant.
    """
    t = _q(heat)
    _budget(modes, 1, 64)
    if t <= 0 or 3*t*modes*modes < 2:
        raise Chi4SourceError("Positive heat and decreasing Gaussian tail required")
    return Q(4)/(3*t) * upper_exp_neg(3*t*modes*modes/4, 128)


def theta_interval(heat: int | Q, modes: int) -> I:
    """Rational enclosure of the infinite odd theta, with analytic tail bound."""
    t = _q(heat)
    tail = theta_tail_bound(t, modes)
    finite = iv(0)
    for n in range(1, modes+1):
        coefficient = 2*n*character_four(n)
        if coefficient:
            finite += coefficient * _gaussian_exp_pi_upper_lower(t*n*n/4)
    return I(finite.lo-tail, finite.hi+tail)


def theta_functional_probe(heat: int | Q = 4, primal_modes: int = 3,
                           dual_modes: int = 10, conductor: int = 4,
                           root: int = 1) -> dict:
    """Certified consistency/refutation probe; a passing overlap proves no identity.

    A wrong conductor replaces exp(-pi*n^2*t/4) by exp(-pi*n^2*t/q).
    Exact square heat keeps t^-3/2 rational.
    """
    t = _q(heat)
    _budget(conductor, 1, 64)
    if t <= 0 or type(root) is not int or root not in (-1, 1):
        raise Chi4SourceError("Positive heat and root sign required")
    a, b = isqrt(t.numerator), isqrt(t.denominator)
    if a*a != t.numerator or b*b != t.denominator:
        raise Chi4SourceError("Rational square heat required for exact amplitude")
    direct = theta_interval(4*t/conductor, primal_modes)
    dual = theta_interval(4/(conductor*t), dual_modes) * (root / (t*Q(a, b)))
    disjoint = direct.hi < dual.lo or dual.hi < direct.lo
    return {"direct": (direct.lo, direct.hi), "dual": (dual.lo, dual.hi),
            "rigorously_disjoint": disjoint, "conductor": conductor,
            "root": root, "identity_proved_by_probe": False,
            "zero_positions_used": False}


def completed_theta_error(sigma_min: int | Q, sigma_max: int | Q,
                          modes: int, endpoint: int, derivative: int = 0) -> Q:
    """Uniform rational error for the entire split theta integral on a strip.

    Covers omitted modes and t>endpoint, not finite quadrature error.
    For the r-th s derivative, (log t/2)^r <= t^r/2^r.
    """
    lo, hi = _q(sigma_min), _q(sigma_max)
    if not -40 <= lo <= hi <= 40:
        raise Chi4SourceError("Ordered bounded real strip required")
    _budget(modes, 1, 64); _budget(endpoint, 1, 1000)
    _budget(derivative, 0, 2)
    ceil = lambda x: -((-x.numerator)//x.denominator)
    B = max(0, ceil((hi-1)/2), ceil(-lo/2))
    m = B + derivative
    return Q(1, 2**derivative) * (
        Q(4, 3) * exponential_moment_tail(Q(3*modes*modes, 4), 1, m)
        + Q(10, 3) * exponential_moment_tail(Q(3, 4), endpoint, m))


def arithmetic_mutation_receipts() -> dict:
    """Exact witnesses; transcendental conductor/root errors have separate probes."""
    genuine = tuple(character_four(n) for n in range(1, 13))
    non_euler = list(genuine); non_euler[8] = -1
    fake_six = list(genuine); fake_six[5] = 1
    return {
        "minimal_conductor_witness": (1, 3, 2, character_four(1), character_four(3)),
        "omitted_2_character_diagonal_minus_one": -1,
        "omitted_3_euler_at_s2": (Q(local_chi4_euler(3, 2, 2)["full"]), Q(1)),
        "fake_six_logjet_present_in_authentic_source": any(n == 6 for n, _, _ in logarithmic_source_tape(12)),
        "fake_six_tape": validate_coefficient_tape(tuple(fake_six)),
        "non_euler_prime_square_tape": validate_coefficient_tape(tuple(non_euler)),
        "even_theta_pair_at_n1": character_four(1)+character_four(-1),
        "odd_theta_pair_at_n1": character_four(1)-character_four(-1),
        "wrong_finite_phase_at_quarter": ramified_fourier(Q(1, 4), 1),
        "correct_finite_phase_at_quarter": ramified_fourier(Q(1, 4), -1),
        "zero_mode": ramified_test(0), "fourier_zero_mode": ramified_fourier(0),
        "wrong_single_phase_global_multiplier": source_fourier_multiplier(1, 1),
        "GRH_proved": False,
    }
