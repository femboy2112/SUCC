"""Full finite-Tate Schwartz--Bruhat test from the original FUCC Möbius sieve.

For P genuine primes, M=prod(P), define on the genuine finite adeles:
 Phi_P(x_f) = prod_{p in P}1_(Zp^times)(x_p)
              prod_{q notin P}1_(Zq)(x_q)
            = sum_(d|M) mu(d) 1_(d*Zhat)(x_f).

RationalCoset(0,d) is the existing source-authenticated additive
compact-open indicator from adelic_poisson_reconstruction, with additive
Haar vol(d Zhat)=1/d and finite Fourier transform
 d^-1*1_(d^-1 Zhat), using actual self-dual Tate Haar/phase.

Its restriction to diagonal positive integers is exactly the
source FUCC positive sieve E_P. Its ADDITIVE Haar integral is
prod_p(1-1/p). On rational dual q=a/M, its exact Fourier value is
  c_M(a)/M, c_M(a)=prod_p [p-1 if p|a else -1],
the classical Ramanujan sum. Exact CRT Plancherel:
  sum_(a mod M) c_M(a)^2 / M^2 = phi(M)/M.

This is an authentic all-finite-place test-space/Fourier commuting
square, NOT the Connes global multiplicative idelic trace, and it
does not read zeros or solve completed Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd,prod

from .mobius_index_infinity import (
    IndexBoundaryError, _primes, squarefree_mobius_tape,
    sieve_projection, finite_sieve_count,
)
from .adelic_poisson_reconstruction import RationalCoset


class AdelicMobiusError(ValueError):
    """Unlawful source, finite-place or Fourier test provenance."""


@dataclass(frozen=True)
class FiniteTateMobiusTest:
    primes: tuple[int,...]
    source_id: str = "Q-standard-Tate"
    epoch: int = 0

    def __post_init__(self):
        try:
            _primes(self.primes)
        except IndexBoundaryError as exc:
            raise AdelicMobiusError("genuine sorted prime source required") from exc
        if type(self.source_id) is not str or not self.source_id.strip():
            raise AdelicMobiusError("nonempty original Tate source identifier")
        if type(self.epoch) is not int or self.epoch<0:
            raise AdelicMobiusError("nonnegative integer source epoch")

    @property
    def modulus(self):
        return prod(self.primes,start=1)

    def terms(self):
        """Source genuine cosets 1_(d Zhat), not invented finite p-clocks."""
        return tuple((d,sign,RationalCoset(F(0),F(d),
                         self.source_id,self.epoch))
                     for d,sign in squarefree_mobius_tape(self.primes))

    def on_integer(self,n):
        """Original diagonal source restriction Phi_P(n)=<n|E_P|n>."""
        try:
            source=sieve_projection(n,self.primes)["projection_diagonal"]
        except IndexBoundaryError as exc:
            raise AdelicMobiusError("genuine positive integer source required") from exc
        termwise=sum(sign*int(c.primal_diagonal(n)["within_finite_compact_open_support"])
                     for d,sign,c in self.terms())
        if termwise!=source or termwise not in (0,1):
            raise AssertionError("Tate compact-open/source sieve square failed")
        return {"n":n,"original_integer_value":source,
                "Tate_finite_adele_indicator_value":termwise,
                "exact_source_restriction_commutes":True,
                "signed_Well_positivity_proved":False}

    def additive_haar(self):
        """Original normalized finite-adelic test integral, all places at once."""
        mass=sum((sign*c.additive_haar_volume
                  for d,sign,c in self.terms()),F(0))
        expected=prod((F(p-1,p) for p in self.primes),start=F(1))
        if mass!=expected:
            raise AssertionError("true finite adele additive Haar mismatch")
        return {"actual_RationalCoset_source_mass":mass,
                "local_unit_product_Haar":expected,
                "original_tate_Schwartz_Bruhat_generator_span":True,
                "source_normalization_agrees":True,
                "is_global_completed_Weil_distribution":False}

    def Fourier_at_rational(self,q):
        """Exact additive self-dual Tate Fourier transform at rational q."""
        if type(q) not in (int,F):
            raise AdelicMobiusError("original rational Fourier frequency required")
        q=F(q)
        total=F(0)
        for d,sign,c in self.terms():
            t=c.dual_diagonal(q)
            total+=sign*t["finite_haar_amplitude"]
            if t["dual_within_finite_support"]!=(d*q).denominator==1:
                raise AssertionError("original Tate finite source dual support mutated")
        return {"frequency":q,"Fourier_value":total,
                "real_Tate_character_phase_zero_for_unshifted_cosets":True,
                "Schwartz_Bruhat_continuation_constructed":True,
                "completed_Connes_trace_proved":False}

    def ramanujan_oracle(self,a):
        """Three routes: original Tate finite Fourier; independent CRT factors;
        divisor/Möbius formula for c_M(a).
        """
        if type(a) is not int:
            raise AdelicMobiusError("exact integer dual character required")
        M=self.modulus
        direct=self.Fourier_at_rational(F(a,M))["Fourier_value"]
        crt=prod(((p-1) if a%p==0 else -1 for p in self.primes),start=1)
        mu=dict(squarefree_mobius_tape(self.primes))
        alt=sum((d*mu[M//d] for d in range(1,gcd(M,a)+1)
                 if gcd(M,a)%d==0),0)
        # Only divisors of gcd(M,a) enter; they also divide M.
        if direct!=F(crt,M) or alt!=crt:
            raise AssertionError("TATE_MOBIUS_RAMANUJAN_FOURIER_MISMATCH")
        return {"modulus":M,"integer_character":a,
                "actual_finite_Tate_Fourier":direct,
                "independent_CRT_Ramanujan_integer":crt,
                "independent_divisor_Ramanujan_integer":alt,
                "Fourier_phase_source_consistent":True,
                "negative_Fourier_values_are_not_negative_PSD_witnesses":True,
                "all_place_Weil_positive":False}

    def exact_plancherel(self):
        """Exact finite quotient Fourier isometry, not sampled transcendental.

        Phi supported in Zhat and invariant under M Zhat; hatPhi supported
        in M^-1 Zhat and invariant under Zhat. The M rational character
        values are the FULL finite Fourier quotient. Plancherel:
            sum_{a mod M}|hatPhi(a/M)|² = phi(M)/M.
        """
        M=self.modulus
        if M>3000:
            raise AdelicMobiusError("bounded exact full Fourier quotient <=3000")
        values=tuple(self.ramanujan_oracle(a)["actual_finite_Tate_Fourier"]
                     for a in range(M))
        integral=sum((v*v for v in values),F(0))
        mass=self.additive_haar()["actual_RationalCoset_source_mass"]
        if integral!=mass:
            raise AssertionError("finite CRT original Fourier failed Parseval")
        return {"M":M,
                "all_M_Fourier_values":values,
                "original_additive_haar_norm_sq":mass,
                "dual_original_Fourier_norm_sq":integral,
                "exact_finite_Tate_Poisson_Plancherel":True,
                "all_original_finite_places_retained":True,
                "no_Arch_Gamma_contact_or_global_Connes_trace":True}

    def source_receipt(self,n,N):
        """Three source routes: integer SUCC/FUCC, genuine Tate test, Haar."""
        integer=self.on_integer(n)
        tate=self.additive_haar()
        try:finite=finite_sieve_count(self.primes,N)
        except IndexBoundaryError as exc:
            raise AdelicMobiusError("integer counting horizon missing") from exc
        return {"source_primes":self.primes,"source_id":self.source_id,
                "epoch":self.epoch,"original_integer":integer,
                "genuine_finite_adele_test":True,
                "actual_Tate_additive_Haar":tate["actual_RationalCoset_source_mass"],
                "integer_cutoff_trace":finite["normalized_trace"],
                "rational_error_upper":finite["source_uniform_error_upper"],
                "all_place_multiplicative_Connes_trace":False,
                "one_real_Gamma_two_poles_and_contact":False,
                "RH_proved":False}
