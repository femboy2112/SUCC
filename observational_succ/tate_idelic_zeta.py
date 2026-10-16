"""Classical Tate zeta, with source-indexed exact SUCC interfaces.

The accompanying note proves the analytic assertions; this module implements
finite rational charts, normalization and coefficient maps. Rational charts
are not all ideles. No finite computation proves an infinite theorem, and no
nontrivial zero positions enter any construction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, prod

from .adelic_poisson_reconstruction import GaussianPoissonGenerator, RationalCoset
from .all_places_zeta import (
    continuation_tail_rational, glued_completed_zeta, place_primes,
    prime, product_formula_rational, rational_place_valuations,
)
from .tate_schwartz_functor import PadicBall, finite_source_logjets, local_mellin_shell


class TateIdelicError(ValueError):
    """A finite source chart or an analytic domain has been misdeclared."""


def _q(value, *, nonzero=False):
    if type(value) not in (int, Q):
        raise TateIdelicError("Exact integer/Fraction data required")
    value = Q(value)
    if nonzero and not value:
        raise TateIdelicError("Idelic coordinates must be nonzero")
    return value


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise TateIdelicError("An exact integer in the stated domain is required")
    return value


def _prime(p):
    try:
        place_primes((p,))
    except ValueError as exc:
        raise TateIdelicError("An actual prime place is required") from exc
    return p


@dataclass(frozen=True)
class RationalChartIdele:
    """An executable subspace of A_Q^times, closed under diagonal Q^times.

    The real component and each finite component are rational and nonzero.
    At primes not in ``overrides`` the component is ``finite_default``.
    A nonzero rational default is a p-adic unit at almost every prime.
    The mathematical quotient theorem is separately valid for *all* ideles.
    """

    real: Q
    finite_default: Q = Q(1)
    overrides: tuple[tuple[int, Q], ...] = ()
    source_id: str = "Q-standard-Tate"
    epoch: int = 0

    def __post_init__(self):
        object.__setattr__(self, "real", _q(self.real, nonzero=True))
        object.__setattr__(self, "finite_default", _q(self.finite_default, nonzero=True))
        if type(self.overrides) is not tuple:
            raise TateIdelicError("Finite exceptional-place data must be a tuple")
        try:
            ps = tuple(p for p, _ in self.overrides)
            place_primes(ps)
            values = tuple((p, _q(v, nonzero=True)) for p, v in self.overrides)
        except (TypeError, ValueError) as exc:
            raise TateIdelicError("Sorted distinct genuine-prime overrides required") from exc
        object.__setattr__(self, "overrides", values)
        if type(self.source_id) is not str or not self.source_id.strip():
            raise TateIdelicError("A declared source identity is required")
        _integer(self.epoch)

    def component(self, p: int) -> Q:
        _prime(p)
        return dict(self.overrides).get(p, self.finite_default)

    def finite_valuations(self) -> tuple[tuple[int, int], ...]:
        values = rational_place_valuations(self.finite_default)
        for p, value in self.overrides:
            values[p] = rational_place_valuations(value).get(p, 0)
        return tuple(sorted((p, k) for p, k in values.items() if k))

    @property
    def norm(self) -> Q:
        return abs(self.real) * prod((Q(p) ** -k for p, k in self.finite_valuations()), start=Q(1))

    def diagonal_action(self, a: int | Q) -> "RationalChartIdele":
        a = _q(a, nonzero=True)
        return RationalChartIdele(a * self.real, a * self.finite_default,
                                  tuple((p, a * v) for p, v in self.overrides),
                                  self.source_id, self.epoch)

    def quotient(self) -> "IdeleClassChart":
        q = prod((Q(p) ** k for p, k in self.finite_valuations()), start=Q(1))
        if self.real < 0:
            q = -q
        normalized = self.diagonal_action(1 / q)
        if normalized.real <= 0 or normalized.finite_valuations():
            raise AssertionError("Q^times normalization did not reach R_+ x Zhat^times")
        if normalized.real != self.norm or product_formula_rational(q) != 1:
            raise AssertionError("Idelic quotient norm disagrees with the product formula")
        return IdeleClassChart(q, normalized)


@dataclass(frozen=True)
class IdeleClassChart:
    """x = diagonal(rational_multiplier) * (r,u), r>0 and u in Zhat^times."""

    rational_multiplier: Q
    representative: RationalChartIdele

    def __post_init__(self):
        object.__setattr__(self, "rational_multiplier", _q(self.rational_multiplier, nonzero=True))
        if not isinstance(self.representative, RationalChartIdele):
            raise TateIdelicError("A typed rational idele representative is required")
        if self.representative.real <= 0 or self.representative.finite_valuations():
            raise TateIdelicError("The class representative must have positive real coordinate and finite units")

    def unit_residue(self, p: int, depth: int) -> int:
        _prime(p)
        _integer(depth, 1)
        u = self.representative.component(p)
        modulus = p ** depth
        return (u.numerator * pow(u.denominator, -1, modulus)) % modulus

    def reconstruct(self) -> RationalChartIdele:
        return self.representative.diagonal_action(self.rational_multiplier)


def multiplicative_shell_mass(p: int, k: int) -> Q:
    """(1-p^-1)^-1 * vol_add(p^k Zp^times) / |p^k|p = 1."""
    _prime(p)
    if type(k) is not int:
        raise TateIdelicError("A signed integer valuation shell is required")
    absolute_value = Q(p) ** -k
    additive_shell_volume = absolute_value * (1 - Q(1, p))
    return additive_shell_volume / (absolute_value * (1 - Q(1, p)))


def finite_euler_stage(primes: tuple[int, ...], s: int, depth: int = 8) -> dict:
    """Exact local Haar integrals and finite-shell product, s integer >=2."""
    try:
        ps = place_primes(primes)
    except ValueError as exc:
        raise TateIdelicError("Genuine finite prime stage required") from exc
    _integer(s, 2)
    _integer(depth)
    if s > 20 or depth > 100:
        raise TateIdelicError("Inherited exact shell implementation budget exceeded")
    shells = tuple(local_mellin_shell(p, s, 0, depth) for p in ps)
    prefix = prod((row["exact_partial"] for row in shells), start=Q(1))
    complete = prod((row["exact_full"] for row in shells), start=Q(1))
    return {"primes": ps, "s": s, "depth": depth, "finite_shell_product": prefix,
            "complete_finite_place_product": complete, "exact_shell_tail": complete - prefix,
            "all_prime_product_executed": False}


def euler_exhaustion_bound(prime_cutoff: int, sigma: int) -> dict:
    """For all Re(s)>=sigma>=2, |zeta(s)-prod_(p<=P) Lp(s)| <= B.

    Every coefficient omitted by that genuine complete prime prefix has n>P.
    Hence B=int_P^infinity x^-sigma dx. The theorem includes complex s;
    the certificate uses integral sigma so B is exact rational.
    """
    _integer(prime_cutoff, 2)
    _integer(sigma, 2)
    ps = tuple(p for p in range(2, prime_cutoff + 1) if prime(p))
    return {"primes": ps, "prime_cutoff": prime_cutoff, "sigma": sigma,
            "absolute_error_bound": Q(prime_cutoff) ** (1 - sigma) / (sigma - 1),
            "valid_half_plane": f"Re(s) >= {sigma}", "bound_includes_roundoff": False}


def real_gamma_even_integer(s: int) -> tuple[int, int]:
    """Exact Gamma_R(s) as coefficient * pi^exponent, for positive even s.

    Both real sign components are integrated with dx/|x|. With t=pi*x^2,
    Gamma_R(s)=pi^(-s/2) Gamma(s/2), not Gamma(s) or Gamma_R(s)/2.
    """
    _integer(s, 2)
    if s % 2:
        raise TateIdelicError("This exact pi-monomial chart requires even s")
    return factorial(s // 2 - 1), -(s // 2)


@dataclass(frozen=True)
class TateZeroModes:
    """Exact rational chart of residues forced by Poisson, not chosen by a fit.

    For the specified Haar measures vol(C_Q^1)=1. General zero modes are
    retained to make Fourier exchange and omission controls explicit.
    """
    phi_zero: Q = Q(1)
    fourier_phi_zero: Q = Q(1)

    def __post_init__(self):
        object.__setattr__(self, "phi_zero", _q(self.phi_zero))
        object.__setattr__(self, "fourier_phi_zero", _q(self.fourier_phi_zero))

    @property
    def residues(self) -> tuple[Q, Q]:
        return -self.phi_zero, self.fourier_phi_zero

    def pole_term(self, s: int | Q) -> Q:
        s = _q(s)
        if s in (0, 1):
            raise TateIdelicError("The meromorphic pole term is undefined at 0 and 1")
        return self.fourier_phi_zero / (s - 1) - self.phi_zero / s

    def fourier_exchange(self) -> "TateZeroModes":
        return TateZeroModes(self.fourier_phi_zero, self.phi_zero)


@dataclass(frozen=True)
class StandardTateSource:
    """Typed source law Phi=Gaussian tensor product_p 1_Zp.

    ``all places`` is a mathematical quantified rule, not a finite list with
    fabricated completeness. Source names/epochs are declarations, not
    physical authentication. The analytic theorem is in the companion note.
    """
    source_id: str = "Q-standard-Tate"
    epoch: int = 0

    def __post_init__(self):
        if type(self.source_id) is not str or not self.source_id.strip():
            raise TateIdelicError("A declared source identity is required")
        _integer(self.epoch)

    def poisson_generator(self) -> GaussianPoissonGenerator:
        return GaussianPoissonGenerator(RationalCoset(Q(0), Q(1), self.source_id, self.epoch))

    def local_test(self, p: int) -> PadicBall:
        _prime(p)
        return PadicBall(p, Q(0), 0, self.source_id, self.epoch)

    def evaluate_exponent(self, x: RationalChartIdele) -> Q | None:
        """Phi(x)=exp(-pi*returned_exponent); None means exact zero."""
        if not isinstance(x, RationalChartIdele) or (x.source_id, x.epoch) != (self.source_id, self.epoch):
            raise TateIdelicError("Source or epoch mismatch in the test/idele map")
        if any(k < 0 for _, k in x.finite_valuations()):
            return None
        return x.real ** 2

    def rational_orbit_exponent(self, representative: RationalChartIdele, q: int | Q) -> Q | None:
        """The Q^times-orbit source restricts EXACTLY to nonzero integers."""
        if representative.real <= 0 or representative.finite_valuations():
            raise TateIdelicError("An idele-class representative is required")
        return self.evaluate_exponent(representative.diagonal_action(q))

    def logarithmic_coefficients(self, cutoff: int, s: int = 2) -> dict:
        result = finite_source_logjets(cutoff, s)
        return dict(result, source_id=self.source_id, epoch=self.epoch,
                    gamma_log_derivative="(digamma(s/2)-log(pi))/2",
                    completed_log_derivative="Gamma_R'/Gamma_R - sum Lambda(n)n^-s",
                    domain="Re(s)>1", zeros_read=False)

    def completed(self, s, cutoff: int = 9, dps: int = 50):
        """Reuse the established theta evaluator; floating output is diagnostic.

        Truncation is bounded by ``tail_bound``. mpmath rounding/special-function
        evaluation are not interval certified, so this is not an enclosure.
        """
        return glued_completed_zeta(s, cutoff, cutoff, dps)

    def tail_bound(self, cutoff: int, real_bound: int, power: int = 96) -> Q:
        return continuation_tail_rational(1, cutoff, cutoff, real_bound, power)


def log_derivative_tail_bound(cutoff: int, sigma: int) -> Q:
    """Rational upper bound for |sum_(n>N) Lambda(n)n^-s|, Re(s)>=sigma>=2.

    Lambda(n)<=log(n), monotone log(x)/x^sigma for x>=2; integrate, then
    use log(N) < ceil(log_2(N)), without evaluating a transcendental log.
    """
    _integer(cutoff, 2)
    _integer(sigma, 2)
    log_upper = (cutoff - 1).bit_length()
    return Q(cutoff) ** (1 - sigma) * (Q(log_upper, sigma - 1) + Q(1, (sigma - 1) ** 2))


def omitted_place_witness(p: int, s: int = 2) -> dict:
    """Removing p changes the source coefficient at n=p from one to zero."""
    _prime(p)
    _integer(s, 2)
    return {"omitted_prime": p, "first_changed_integer_coefficient": p,
            "genuine_coefficient": 1, "mutant_coefficient": 0,
            "mutant_to_true_Euler_ratio_at_s": 1 - Q(p) ** -s,
            "finite_exact_source_witness": True}
