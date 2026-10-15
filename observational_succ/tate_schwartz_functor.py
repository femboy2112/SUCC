"""Tate local Schwartz-Bruhat atom / source-indexed SUCC-FUCC functor.

A dense *rational coordinate* fragment of S(Q_p), with exact coset laws,
additive Fourier character, Haar normalization and affine-event covariance.
Analytic statements about all Q_p are classical theorems, not finite tests.
This is NOT a full restricted adelic product, Weil-form identification or RH
certificate. Original event identifiers are DECLARED, not physical probes.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

from .diagonal_adele_zeta import (
    DiagonalSourceError, fractional_padic_part, prime, rational, valuation,
)


class TateFunctorError(ValueError):
    """Missing genuine prime, source history, topology or lawful affine action."""


def _q(x: int | F) -> F:
    try:
        return rational(x)
    except (DiagonalSourceError, ValueError) as exc:
        raise TateFunctorError("Only exact integer or rational input") from exc


def _prime(p: int) -> int:
    if not prime(p):
        raise TateFunctorError("A genuine prime field Q_p is mandatory")
    return p


def _vp(x: F, p: int) -> int:
    if not x:
        raise TateFunctorError("No valuation of zero as an integer exponent")
    return valuation(x, p)


def _fractional(x: F, p: int) -> F:
    return fractional_padic_part(x, p)


@dataclass(frozen=True)
class PhaseAmplitude:
    """Exact A*exp(2*pi*i*phase), with rational phase modulo 1."""
    amplitude: F
    phase: F = F(0)

    def __post_init__(self) -> None:
        a, ph = _q(self.amplitude), _q(self.phase)
        object.__setattr__(self, "amplitude", a)
        object.__setattr__(self, "phase", ph % 1 if a else F(0))

    def times(self, other: "PhaseAmplitude") -> "PhaseAmplitude":
        if not isinstance(other, PhaseAmplitude):
            raise TateFunctorError("Phase multiplication requires compatible typed amplitudes")
        return PhaseAmplitude(self.amplitude * other.amplitude, self.phase + other.phase)


@dataclass(frozen=True)
class PadicBall:
    """Indicator of the compact-open coset a + p^k Z_p.

    Every a is represented by a rational dense chart, not by a complete Q_p
    point. Scalar q may be p or 1/p: both are invertible on Q_p even
    though p is NOT a unit of the finite ring Z/p^k Z.
    """
    p: int
    a: F
    k: int
    source_id: str = "rational-Qp-standard"
    epoch: int = 0

    def __post_init__(self) -> None:
        _prime(self.p)
        if type(self.k) is not int or not -128 <= self.k <= 128:
            raise TateFunctorError("Signed p-adic scale k must be an exact bounded integer")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise TateFunctorError("Nonempty original-source identifier required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise TateFunctorError("Source epoch must be nonnegative exact integer")
        a = _q(self.a)
        step = F(self.p) ** self.k
        # Canonical representative modulo p^k Zp (not ordinary real modulus).
        object.__setattr__(self, "a", step * _fractional(a / step, self.p))

    @property
    def volume(self) -> F:
        """Haar additive volume: vol(Z_p)=1, vol(p^k Z_p)=p^(-k)."""
        return F(self.p) ** (-self.k)

    def contains(self, x: int | F) -> bool:
        d = _q(x) - self.a
        return not d or _vp(d, self.p) >= self.k

    def shifted(self, d: int | F) -> "PadicBall":
        return PadicBall(self.p, self.a + _q(d), self.k, self.source_id, self.epoch)

    def scaled(self, q: int | F) -> "PadicBall":
        q = _q(q)
        if not q:
            raise TateFunctorError("q=0 destroys invertible Qp scaling")
        new_k = self.k + _vp(q, self.p)
        if not -128 <= new_k <= 128:
            raise TateFunctorError("Insufficient signed-level computation budget")
        return PadicBall(self.p, q * self.a, new_k, self.source_id, self.epoch)

    def fourier(self, xi: int | F) -> PhaseAmplitude:
        """At rational xi, integral 1_(a+p^k Zp)(x)*psi_p(x*xi) dx.

        psi_p(y)=exp(-2*pi*i*{y}_p), paired with real plus convention.
        The precise local Fourier law is vol(ball)*psi_p(a*xi)
        times indicator_(p^-k Zp)(xi).
        """
        xi = _q(xi)
        if xi and _vp(xi, self.p) < -self.k:
            return PhaseAmplitude(F(0))
        return PhaseAmplitude(self.volume, -_fractional(self.a * xi, self.p))

    def local_affine_fourier(self, d: int | F, q: int | F,
                            xi: int | F) -> dict:
        """Prove translation/dilation Fourier intertwining on an exact xi."""
        d, q, xi = _q(d), _q(q), _q(xi)
        if not q:
            raise TateFunctorError("Invertible dilation required")
        after = self.scaled(q).shifted(d)
        lhs = after.fourier(xi)
        # F[T_d D_q f](xi) = psi_p(d*xi) |q|_p F[f](q*xi).
        rhs = PhaseAmplitude(F(self.p) ** (-_vp(q, self.p)),
                             -_fractional(d * xi, self.p)).times(self.fourier(q * xi))
        if lhs != rhs:
            raise AssertionError("True local Qp Fourier affine square does not commute")
        return {
            "prime": self.p, "original": self, "after": after, "frequency": xi,
            "lhs": lhs, "rhs": rhs, "fourier_square": True,
            "true_Qp_scalar": q,
            "finite_ring_unit_required": False,
            "complete_Qp_Fourier_proved_by_finite_test": False,
            "RH_proved": False,
        }


@dataclass(frozen=True)
class SourceEvent:
    """One declared original-source operation, with immutable event receipt."""
    source_id: str
    epoch: int
    ordinal: int
    kind: str
    amount: F

    def __post_init__(self) -> None:
        if type(self.source_id) is not str or not self.source_id.strip():
            raise TateFunctorError("Source event requires a provenance token")
        if type(self.epoch) is not int or self.epoch < 0 or type(self.ordinal) is not int or self.ordinal < 0:
            raise TateFunctorError("Source event index and epoch must be exact nonnegative")
        if self.kind not in ("SUCC", "FUCC", "PRIME_JET_FUCC"):
            raise TateFunctorError("Only declared additive/multiplicative SUCC generators")
        amount = _q(self.amount)
        if self.kind != "SUCC" and not amount:
            raise TateFunctorError("Multiplicative arrow q=0 is invalid")
        if self.kind == "PRIME_JET_FUCC" and (
                amount.denominator != 1 or not prime(amount.numerator)):
            raise TateFunctorError("Prime-jet label must carry an authentic positive prime")
        object.__setattr__(self, "amount", amount)


@dataclass(frozen=True)
class SourceWord:
    """Faithful *receipt* of an affine word, nonfaithful bare Qp operator."""
    initial: PadicBall
    events: tuple[SourceEvent, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.initial, PadicBall) or type(self.events) is not tuple:
            raise TateFunctorError("One typed Qp source and exact event tuple required")
        for j, event in enumerate(self.events):
            if (not isinstance(event, SourceEvent) or
                event.source_id != self.initial.source_id or
                event.epoch != self.initial.epoch or event.ordinal != j):
                raise TateFunctorError("Source-identity / epoch / chronology mismatch")

    def affine(self) -> tuple[F, F]:
        """Affine map x -> A*x+B in exactly the execution order."""
        A, B = F(1), F(0)
        for event in self.events:
            if event.kind == "SUCC":
                B += event.amount
            else:
                A *= event.amount
                B *= event.amount
        return A, B

    def execute(self) -> PadicBall:
        actual = self.initial
        for event in self.events:
            actual = (actual.shifted(event.amount) if event.kind == "SUCC"
                      else actual.scaled(event.amount))
        A, B = self.affine()
        if actual != self.initial.scaled(A).shifted(B):
            raise AssertionError("Affine source-event functor not covariant")
        return actual

    def fourier_receipt(self, xi: int | F) -> dict:
        xi = _q(xi)
        A, B = self.affine()
        after = self.execute()
        lhs = after.fourier(xi)
        rhs = PhaseAmplitude(F(self.initial.p) ** (-_vp(A, self.initial.p)),
                             -_fractional(B * xi, self.initial.p)).times(
                                 self.initial.fourier(A * xi))
        if lhs != rhs:
            raise AssertionError("Source history does not intertwine local Fourier")
        return {
            "source_id": self.initial.source_id, "epoch": self.initial.epoch,
            "event_receipts": tuple((e.ordinal, e.kind, e.amount) for e in self.events),
            "affine_A": A, "affine_B": B,
            "fourier_naturality": True, "left": lhs, "right": rhs,
            "bare_operator_forgets_history": True,
            "history_receipts_retained": True,
            "analytical_all_places_functor_constructed": False,
            "RH_proved": False,
        }


def local_mellin_shell(p: int, s: int, first_k: int, depth: int) -> dict:
    """Normalized Tate multiplicative shell integral at an integer s>=2.

    f=1_(p^first_k Zp); Haar^times(vol(Zp^times))=1. Its zeta integral
    is sum_(k>=first_k) p^(-k*s). Exact finite-prefix + exact tail, with
    no zeros or Euler product continuation.
    """
    _prime(p)
    if (type(s) is not int or not 2 <= s <= 20 or
        type(first_k) is not int or not -32 <= first_k <= 32 or
        type(depth) is not int or not 0 <= depth <= 100):
        raise TateFunctorError("Integer Mellin shell requires finite exact resources")
    ratio = F(p) ** (-s)
    partial = sum((ratio**k for k in range(first_k, first_k + depth)), F(0))
    tail = ratio ** (first_k + depth) / (1-ratio)
    complete = ratio ** first_k / (1-ratio)
    if partial + tail != complete:
        raise AssertionError("Local Euler/Mellin shell calculation failed")
    return {
        "p": p, "s": s, "first_shell": first_k, "depth": depth,
        "exact_partial": partial, "exact_tail": tail, "exact_full": complete,
        "source": "genuine p-valuation, multiplicative Haar normalization",
        "gamma_factor_present": False, "analytic_continuation_claimed": False,
        "RH_proved": False,
    }


def critical_mellin_character(real_s: F, source_offset: F = F(0)) -> dict:
    """Algebraic half-density change-of-variables interface, not an integral.

    F(x)=x^(-1/2+offset)*h(log x); ∫ F(x)x^s dx/x
        =∫ h(t) exp((s-1/2+offset)*t) dt.
    At Re s=1/2, ordinary Fourier oscillation has ZERO real drift iff offset=0.
    """
    real_s, source_offset = _q(real_s), _q(source_offset)
    drift = real_s-F(1,2)+source_offset
    return {
        "real_s": real_s, "source_offset": source_offset,
        "real_exponent_in_log_clock": drift,
        "is_critical_fourier": drift == 0,
        "half_density_preserved": source_offset == 0,
        "full_complex_mellin_theorem_executed": False,
        "RH_proved": False,
    }


def first_missing_prime(prime_cutoff: int) -> dict:
    """A finite prime transcript leaves unseen source *mutants* possible.

    Countermodels below violate the FULL authentic Euler/von-Mangoldt
    source law. Thus this is a finite-OBSERVATION limitation, and NOT an
    epistemic obstruction when that complete source law is supplied.
    """
    if type(prime_cutoff) is not int or not 2 <= prime_cutoff <= 100_000:
        raise TateFunctorError("Finite positive authentic prime cutoff required")
    p = prime_cutoff + 1
    while not prime(p):
        p += 1
    return {
        "observed_source_cutoff": prime_cutoff, "first_unobserved_prime": p,
        "all_observed_prime_events_unchanged_under_mutant": True,
        "distinct_later_source_impulse": (p, p, "delta_log(p)"),
        "smooth_autocorrelation_can_detect_later_prime": True,
        "required_test_support_span": "strictly greater than log(p)",
        "mutant_satisfies_complete_actual_von_Mangoldt_source": False,
        "physical_observer_identifies_mutant_as_real": False,
        "Weil_full_test_factorization_from_finite_samples": False,
        "RH_proved": False,
    }



def local_euler_logjet(p: int, s: int, depth: int) -> dict:
    """Tate unramified local Mellin -> canonical prime-power logarithmic jet.

    -d/ds log[(1-p^-s)^-1] = log(p) * sum_(k>=1) p^(-k*s)
    for Re(s)>0. At positive integral s>=2 every ratio below is exact
    Fraction, while log(p) remains a FORMAL positive prime log symbol.
    """
    _prime(p)
    if type(s) is not int or not 2 <= s <= 20 or type(depth) is not int or not 0 <= depth <= 100:
        raise TateFunctorError("Exact local logjet needs s>=2 and bounded depth")
    ratio = F(p)**(-s)
    partial = sum((ratio**k for k in range(1,depth+1)),F(0))
    remainder = ratio**(depth+1)/(1-ratio)
    full = ratio/(1-ratio)
    if partial+remainder != full:
        raise AssertionError("Source prime logarithmic derivative fails")
    return {
        "prime": p, "s": s,
        "jet_labels": tuple((p**k,p) for k in range(1,depth+1)),
        "formal_log_prime": p,
        "coefficient_of_logp_partial": partial,
        "coefficient_of_logp_tail": remainder,
        "coefficient_of_logp_full": full,
        "derivative_identity": "-d/ds log[(1-p^-s)^-1]",
        "zero_inputs_used": False, "Weil_sign_proved": False,
    }


def finite_source_logjets(N: int, s: int) -> dict:
    """Exact arithmetic cross-check against existing authentic Λ tape.

    The *finite* coefficient grouping is an independent factorization
    oracle. The all-prime Euler logarithmic derivative identity holds for
    Re(s)>1 as an imported classical absolute-convergence theorem.
    It MUST NOT be evaluated as that Dirichlet series at Re(s)=1/2.
    """
    from .completed_weil_transport import von_mangoldt_labels
    if type(N) is not int or not 2 <= N <= 50_000:
        raise TateFunctorError("Source prime-power cutoff in [2,50000] required")
    if type(s) is not int or not 2 <= s <= 20:
        raise TateFunctorError("Only absolutely convergent integer s>=2")
    direct = []
    for p in range(2,N+1):
        if not prime(p):
            continue
        power = p
        while power <= N:
            direct.append((power,p))
            power *= p
    direct = tuple(sorted(direct))
    imported = von_mangoldt_labels(N)
    if direct != imported:
        raise AssertionError("Independent prime-power source != inherited Λ oracle")
    grouped={}
    for n,p in direct:
        grouped[p]=grouped.get(p,F(0))+F(n)**(-s)
    if any(grouped[p] != sum((F(n)**(-s) for n,q in direct if q==p),F(0)) for p in grouped):
        raise AssertionError("Grouped prime logarithmic coefficients inconsistent")
    return {
        "source_cutoff": N, "s": s, "prime_power_labels": direct,
        "formal_logp_coefficients": tuple(sorted(grouped.items())),
        "exact_original_von_Mangoldt_cross_oracle": True,
        "all_prime_logderivative_requires_Re_s_gt_1": True,
        "critical_line_dirichlet_series_converges": False,
        "completed_archimedean_and_poles_included": False,
        "RH_proved": False,
    }
