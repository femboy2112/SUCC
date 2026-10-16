"""Source-indexed reconstruction of the Pontryagin dual of profinite Z.

CLASSICAL THEOREM:
  Hom_cont( lim_(n|m) Z/mZ, Circle ) ~= (Q/Z)_discrete.
For r=a/n (mod Z) and x in Zhat, chi_r(x)=exp(2*pi*i*a*x_n/n).
The sign is POSITIVE here. The standard finite adelic local Tate character
uses the opposite sign, exp(-2*pi*i*{y}_p); the transition is chi_r(x)
=psi_f(-r*x), not psi_f(r*x).

This module computes exact phase classes in Q/Z on existing finitely
described profinite points. Full topology and all continuous characters
are handled by the classical proof in the research dossier, never by
finite samples or physical observer claims.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .edge_carrier_reconstruction import (
    EdgeCarrierError, ProfiniteProgram,
)
from .finite_fourier_carrier import CyclotomicElement


class PontryaginSourceError(ValueError):
    """Invalid character, wrong source, or an unlicensed finite/global inference."""


def _int(value, description: str) -> int:
    if type(value) is not int:
        raise PontryaginSourceError(f"{description} requires an exact integer")
    return value


def _fraction(value, description: str) -> F:
    if type(value) not in (int, F):
        raise PontryaginSourceError(f"{description} requires an exact rational")
    return F(value)


def _source(source_id: str, epoch: int) -> None:
    if type(source_id) is not str or not source_id.strip():
        raise PontryaginSourceError("Declare a nonempty original source identifier")
    if type(epoch) is not int or epoch < 0:
        raise PontryaginSourceError("Declare a nonnegative original source epoch")


def _modulus(n: int, *, maximum: int = 2_000_000) -> int:
    if type(n) is not int or not 1 <= n <= maximum:
        raise PontryaginSourceError("Finite observation modulus exceeds the declared budget")
    return n


@dataclass(frozen=True)
class FiniteCyclicCharacter:
    """A character of the source ring's additive cyclic group Z/nZ."""
    modulus: int
    label: int
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        n = _modulus(self.modulus)
        _source(self.source_id, self.epoch)
        a = _int(self.label, "Finite character coefficient")
        object.__setattr__(self, "label", a % n)

    @property
    def rational_frequency(self) -> F:
        return F(self.label, self.modulus) % 1

    def phase(self, x: int) -> F:
        """Exact rational phase of the root exp(2*pi*i*a*x/n)."""
        return F(self.label * _int(x, "Finite cyclic source value"),
                 self.modulus) % 1

    def character_root(self, x: int) -> CyclotomicElement:
        if self.modulus > 100:
            raise PontryaginSourceError("Exact cyclotomic root oracle requires n<=100")
        return CyclotomicElement.root(self.modulus,
                                      self.label*_int(x, "Finite cyclic value"))

    def lift(self, larger_modulus: int) -> "FiniteCyclicCharacter":
        """Dual arrow to Z/mZ -> Z/nZ when n | m: a -> a*m/n."""
        m = _modulus(larger_modulus)
        if m % self.modulus:
            raise PontryaginSourceError("A dual arrow requires n | m")
        return FiniteCyclicCharacter(
            m, self.label*(m//self.modulus), self.source_id, self.epoch
        )

    def naturality(self, x_m: int, m: int) -> dict:
        """Character of x_m modulo n equals lifted character modulo m."""
        upper = self.lift(m)
        x = _int(x_m, "Source residue")
        lhs = self.phase(x % self.modulus)
        rhs = upper.phase(x % m)
        if lhs != rhs:
            raise AssertionError("Dual map fails to commute with genuine source reduction")
        return {
            "small": self.modulus, "large": m, "label_small": self.label,
            "label_lifted": upper.label, "phase_small": lhs,
            "phase_large": rhs, "dual_naturality": True,
            "source_id": self.source_id, "epoch": self.epoch,
        }


@dataclass(frozen=True)
class RationalCircleCharacter:
    """One element of Q/Z as an exact normalized rational phase modulo 1.

    The normalized denominator n is the *minimum* cyclic modulus carrying
    this character, except that r=0 has denominator one. It is a finite
    description of one global character, NOT an enumeration of all Zhat.
    """
    frequency: F
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        _source(self.source_id, self.epoch)
        r = _fraction(self.frequency, "Q/Z frequency")
        object.__setattr__(self, "frequency", r % 1)

    def _check(self, other: "RationalCircleCharacter") -> None:
        if (not isinstance(other, RationalCircleCharacter) or
            (self.source_id, self.epoch) != (other.source_id, other.epoch)):
            raise PontryaginSourceError("Character composition requires the same source and epoch")

    def add(self, other: "RationalCircleCharacter") -> "RationalCircleCharacter":
        self._check(other)
        return RationalCircleCharacter(self.frequency + other.frequency,
                                        self.source_id, self.epoch)

    def neg(self) -> "RationalCircleCharacter":
        return RationalCircleCharacter(-self.frequency, self.source_id, self.epoch)

    def multiply_integer(self, n: int) -> "RationalCircleCharacter":
        return RationalCircleCharacter(
            self.frequency * _int(n, "Integer SUCC/FUCC multiplier"),
            self.source_id, self.epoch
        )

    def on_finite_clock(self, modulus: int) -> FiniteCyclicCharacter:
        m = _modulus(modulus)
        d = self.frequency.denominator
        if m % d:
            raise PontryaginSourceError("Requested probe does not resolve the character's conductor")
        label = self.frequency.numerator * (m//d)
        return FiniteCyclicCharacter(m, label, self.source_id, self.epoch)

    def evaluate(self, x: ProfiniteProgram) -> F:
        """Exact phase chi_r(x) using only the finite conductor clock."""
        if not isinstance(x, ProfiniteProgram) or (
            x.source_id, x.epoch) != (self.source_id, self.epoch):
            raise PontryaginSourceError("Original profinite source ID/epoch mismatch")
        n = _modulus(self.frequency.denominator)
        return self.on_finite_clock(n).phase(x.residue(n))

    def evaluate_via_refinement(self, x: ProfiniteProgram, m: int) -> dict:
        """Same global phase from two compatible original finite observations."""
        if not isinstance(x, ProfiniteProgram) or (
            x.source_id, x.epoch) != (self.source_id, self.epoch):
            raise PontryaginSourceError("Wrong original source for refined probe")
        coarse = self.evaluate(x)
        large = self.on_finite_clock(m).phase(x.residue(m))
        if coarse != large:
            raise AssertionError("Constructed character depends on choice of finite model")
        return {
            "conductor": self.frequency.denominator,
            "probe_modulus": m,
            "coarse_phase": coarse, "refined_phase": large,
            "character_gluing_verified": True,
            "all_Zhat_points_checked": False,
        }

    def dual_SUCC_translation(self, x: ProfiniteProgram, increment: int) -> dict:
        """chi_r(x+d)=chi_r(x)*chi_r(d): additive original-carrier action."""
        k = _int(increment, "SUCC translation")
        one = ProfiniteProgram.integer(k, source_id=self.source_id, epoch=self.epoch)
        if not isinstance(x, ProfiniteProgram) or (
            x.source_id, x.epoch) != (self.source_id, self.epoch):
            raise PontryaginSourceError("Missing original carrier for SUCC covariance")
        transformed = x.add(one)
        lhs = self.evaluate(transformed)
        rhs = (self.evaluate(x) + self.evaluate(one)) % 1
        if lhs != rhs:
            raise AssertionError("SUCC character group-law naturality failed")
        return {"frequency": self.frequency, "step": k, "lhs": lhs, "rhs": rhs,
                "translation_covariance": True}

    def dual_FUCC_multiplication(self, x: ProfiniteProgram, multiplier: int) -> dict:
        """chi_r(m*x)=chi_(m*r)(x): dual integer-scaling law."""
        m = _int(multiplier, "Original integer multiplier")
        if not isinstance(x, ProfiniteProgram) or (
            x.source_id, x.epoch) != (self.source_id, self.epoch):
            raise PontryaginSourceError("Wrong original carrier for multiplication")
        scalar = ProfiniteProgram.integer(m,source_id=self.source_id,epoch=self.epoch)
        lhs = self.evaluate(x.multiply(scalar))
        rhs = self.multiply_integer(m).evaluate(x)
        if lhs != rhs:
            raise AssertionError("Profinite FUCC operation not transported faithfully")
        return {"frequency": self.frequency, "multiplier": m,
                "lhs": lhs, "rhs": rhs, "dual_multiplication_covariance": True,
                "must_be_prime": False}


def phase_separation(x: ProfiniteProgram, modulus: int) -> dict:
    """One dual character 1/n retrieves the original Z/nZ observation.

    The family over ALL n is jointly faithful on Zhat, while finite
    prefixes are not. This finite command proves only one stage.
    """
    if not isinstance(x, ProfiniteProgram):
        raise PontryaginSourceError("Source must be an actual profinite program")
    n = _modulus(modulus)
    probe = RationalCircleCharacter(F(1,n),x.source_id,x.epoch)
    phase = probe.evaluate(x)
    recovered = phase*n
    if recovered.denominator != 1 or int(recovered) != x.residue(n):
        raise AssertionError("Finite dual phases cannot reconstruct a genuine residue")
    return {"modulus": n, "frequency": F(1,n), "phase": phase,
            "recovered_residue": int(recovered),
            "direct_original_residue": x.residue(n),
            "stage_separation_proved": True,
            "all_infinite_points_finitely_identified": False}


def finite_character_orthogonality(n: int, a: int) -> dict:
    """Finite exact Fourier calibration against the pre-existing cyclotomic oracle.

    sum_(x mod n) exp(2*pi*i*a*x/n) is n for a=0 mod n else 0.
    This is an exact check for a specified finite n, not a replacement
    proof of Pontryagin duality for all continuous characters.
    """
    m = _modulus(n,maximum=48)
    freq = _int(a, "Frequency coefficient") % m
    total = CyclotomicElement.scalar(m, 0)
    for x in range(m):
        total = total + CyclotomicElement.root(m, freq*x)
    expected = CyclotomicElement.scalar(m, m if freq == 0 else 0)
    if total != expected:
        raise AssertionError("Independent cyclotomic Fourier orthogonality failed")
    return {"modulus":m, "frequency":freq,
            "expected_zero":freq != 0, "sum":total.polynomial,
            "finite_character_orthogonality_exact":True,
            "general_duality_from_finite_samples":False}


def wrong_dual_arrow_witness() -> dict:
    """A naive unchanged character label is NOT a valid dual transition."""
    small, large, x = FiniteCyclicCharacter(3, 1), 6, 1
    lawful = small.lift(large)
    incorrect = FiniteCyclicCharacter(large,1)
    if lawful.phase(x) != small.phase(x) or incorrect.phase(x) == lawful.phase(x):
        raise AssertionError("Dual-arrow mutation failed to separate naturality")
    return {"small_modulus":3, "large_modulus":6, "source_residue":x,
            "correct_lifted_label":lawful.label,
            "mutant_unchanged_label":incorrect.label,
            "mutant_phase":incorrect.phase(x), "correct_phase":lawful.phase(x),
            "bad_dual_arrow_refuted":True,
            "RH_proved":False}



def no_uniform_character_conductor(modulus: int) -> dict:
    """Witness that no fixed finite clock detects EVERY global character.

    For any declared n, choose an authentic prime p>n. The nonzero
    profinite projector e_p is invisible in Z/nZ (since p does not
    divide n), but chi_(1/p)(e_p)=1/p mod 1 is nonzero. Thus:
      forall n exists r,z: pi_n(z)=0 but chi_r(z)!=1.
    Every particular chi_r still factors through its finite conductor.
    This is a proved elementary family, NOT proof that an individual
    continuous character is computationally inaccessible.
    """
    n=_modulus(modulus,maximum=50_000)
    from .edge_carrier_reconstruction import prime
    p=n+1
    while not prime(p):
        p+=1
    x=ProfiniteProgram.projector(p)
    zero=ProfiniteProgram.integer(0)
    witness=RationalCircleCharacter(F(1,p))
    coarse_equal=x.residue(n)==zero.residue(n)
    fine_diff=witness.evaluate(x)!=witness.evaluate(zero)
    if not coarse_equal or not fine_diff:
        raise AssertionError("Source-defined hidden-prime character was not distinguishing")
    return {
        "observer_modulus":n,
        "adversarial_new_prime":p,
        "source_point_residue":x.residue(n),
        "zero_residue":zero.residue(n),
        "separating_frequency":F(1,p),
        "character_phase_at_hidden_source":witness.evaluate(x),
        "character_phase_at_zero":witness.evaluate(zero),
        "same_declared_finite_observation":True,
        "separated_by_genuinely_new_character":True,
        "uniform_finite_clock_for_all_continuous_characters":False,
        "every_single_continuous_character_has_finite_conductor":
            "CLASSICAL_PONTRYAGIN_THEOREM",
        "all_global_points_have_finite_codes":False,
        "RH_proved":False,
    }
