"""Exact source-typed local scaling trace bridge: SUCC/FUCC -> Connes.

Only off-identity p-adic fixed-point scalars, product formula, and source
chart comparisons are proved. Neither global Connes trace nor Weil PSD
is implied. No zeta-zero data enter the construction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt


class ConnesBridgeError(ValueError):
    """Invalid arithmetic source, scale, or local p-adic chart."""


class ContactSingularity(ConnesBridgeError):
    """At multiplier u=1, the off-identity fixed-point trace diverges."""


def _rational(x):
    if type(x) not in (int, Q):
        raise ConnesBridgeError("integer or Fraction required; floats/bools forbidden")
    return Q(x)


def _prime(p):
    if type(p) is not int or p < 2 or any(p % k == 0 for k in range(2, isqrt(p) + 1)):
        raise ConnesBridgeError("genuine prime place required")
    return p


def _valuation(n, p):
    if n == 0:
        raise ContactSingularity("valuation at zero is the contact singularity")
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _prime_divisors(n):
    n = abs(n)
    result = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.add(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        result.add(n)
    return result


@dataclass(frozen=True)
class RationalScale:
    """Declared arithmetic scaling chart, NOT a full adele class or N-FUCC inverse."""
    u: Q
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self):
        u = _rational(self.u)
        if not u:
            raise ConnesBridgeError("scaling cannot be zero")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise ConnesBridgeError("nonempty original source ID required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise ConnesBridgeError("nonnegative integer source epoch required")
        object.__setattr__(self, "u", u)

    def inverse(self):
        return type(self)(1 / self.u, self.source_id, self.epoch)


@dataclass(frozen=True)
class FixedPointStage:
    """Finite normalized delta count for rational u=a/b on b*Z_p.

    x=b*z, dx=|b|_p dz; p^r*1_{p^r Z_p}((u-1)*x)
    integrates to |b|_p * #ker[(a-b) on Z/p^r].
    """
    prime: int
    depth: int
    residue_fixed_points: int
    chart_volume: Q
    finite_delta_coefficient: Q
    stabilized: bool
    off_identity_coefficient: Q
    half_density_coefficient_squared: Q
    source_id: str
    epoch: int


def local_fixed_point(scale: RationalScale, p: int, depth: int) -> FixedPointStage:
    """Compute |1-u|_p^-1 and |u|_p/|1-u|_p^2 exactly (u!=1).

    Square root of second quantity is inversion-symmetric C_p(u).
    This is not a trace-class operator or a positive-type kernel.
    """
    if not isinstance(scale, RationalScale):
        raise ConnesBridgeError("RationalScale with source ID required")
    _prime(p)
    if type(depth) is not int or not 1 <= depth <= 32:
        raise ConnesBridgeError("finite integer depth must be 1..32")
    a, b = scale.u.numerator, scale.u.denominator
    if a == b:
        raise ContactSingularity("u=1 needs a Fourier-normalized principal value")
    va, vb, vd = _valuation(a, p), _valuation(b, p), _valuation(a-b, p)
    count = p ** min(vd, depth)
    volume = Q(p) ** -vb
    return FixedPointStage(
        p, depth, count, volume, volume * count, depth >= vd,
        Q(p) ** (vd-vb), Q(p) ** (2*vd-va-vb),
        scale.source_id, scale.epoch,
    )


def orientation_square_check(scale: RationalScale, p: int, depth: int = 4):
    """True reciprocity after half-density normalization, not positivity."""
    forward = local_fixed_point(scale, p, depth)
    reverse = local_fixed_point(scale.inverse(), p, depth)
    if forward.half_density_coefficient_squared != reverse.half_density_coefficient_squared:
        raise AssertionError("half-density reciprocity failed")
    return {
        "forward": forward, "inverse": reverse,
        "symmetric_squared": forward.half_density_coefficient_squared,
        "inversion_invariant": True, "off_identity_only": True,
        "canonical_contact_calibrated": False, "positive_type_established": False,
    }


def diagonal_rational_product(scale: RationalScale):
    """All-place rational product of off-identity LOCAL scalars equals 1.

    The cancellation is not an Euler/test-function product or Connes trace.
    """
    if not isinstance(scale, RationalScale):
        raise ConnesBridgeError("typed rational scaling source required")
    a, b = scale.u.numerator, scale.u.denominator
    if a == b:
        raise ContactSingularity("u=1 has a contact singularity")
    primes = tuple(sorted(_prime_divisors(a) | _prime_divisors(b) | _prime_divisors(a-b)))
    finite_squares, finite_plain = Q(1), Q(1)
    for p in primes:
        term = local_fixed_point(scale, p, 1)
        finite_squares *= term.half_density_coefficient_squared
        finite_plain *= term.off_identity_coefficient
    arch_squared = Q(abs(a*b), (a-b)**2)
    arch_plain = Q(b, abs(a-b))
    if finite_squares*arch_squared != 1 or finite_plain*arch_plain != 1:
        raise AssertionError("rational product formula failed")
    return {
        "rational_scale": scale.u, "exceptional_primes": primes,
        "finite_half_density_squared_product": finite_squares,
        "arch_half_density_squared": arch_squared,
        "global_half_density_squared_product": Q(1),
        "finite_plain_product": finite_plain, "arch_plain_factor": arch_plain,
        "source_id": scale.source_id, "epoch": scale.epoch,
        "this_is_a_global_trace_formula": False, "Weil_PSD_proved": False,
    }


def affine_word_fixed_point(word):
    """Analyze SUCC/FUCC affine endpoint locally, retaining original history.

    Affine ax+b has a unique rational fixed point b/(1-a) when a!=1.
    Its rational fixed point is NOT a descended SUCC action on A/Q^x.
    """
    from .affine_pontryagin_transfer import AffineSourceWord
    if not isinstance(word, AffineSourceWord):
        raise ConnesBridgeError("source-indexed AffineSourceWord required")
    a, b = word.normal_form()
    if a == 1:
        return {
            "kind": "identity_contact" if b == 0 else "no_fixed_point",
            "normal_form": (a,b), "source_id": word.source_id,
            "epoch": word.epoch,
        }
    return {
        "kind": "single_rational_fixed_point", "normal_form": (a,b),
        "fixed_point": Q(b,1-a),
        "local_scale": RationalScale(Q(a),word.source_id,word.epoch),
        "source_id":word.source_id, "epoch":word.epoch,
        "not_an_action_on_adele_classes":True,
    }


def idelic_place_vs_diagonal(p: int, source_id="Q-standard-Tate", epoch=0):
    """Compare one-place prime dilation and globally diagonal rational gauge.

    This is computed in existing SUCC RationalChartIdele, not a fake clock.
    """
    _prime(p)
    from .tate_idelic_zeta import RationalChartIdele
    local=RationalChartIdele(Q(1),Q(1),((p,Q(p)),),source_id,epoch)
    diagonal=RationalChartIdele(Q(p),Q(p),(),source_id,epoch)
    if local.norm != Q(1,p) or diagonal.norm != 1:
        raise AssertionError("one-place idelic scaling conflated with diagonal gauge")
    if local.quotient().representative.norm == diagonal.quotient().representative.norm:
        raise AssertionError("norm-detectable idelic classes were conflated")
    return {
        "p":p, "local_one_place_norm":local.norm,
        "diagonal_rational_norm":diagonal.norm,
        "same_idele_class":False, "global_connes_trace_construction":False,
        "source_id":source_id, "epoch":epoch,
    }


def succ_does_not_descend():
    """A/Q^x counterexample: -1 ~ -1/2; S sends them to 0, 1/2.

    Multiplicative scaling preserves 0 vs nonzero, so S is not defined
    on quotient classes. Affine source history != Connes scaling action.
    """
    x,y=Q(-1),Q(-1,2)
    return {
        "equivalent_source_representatives":(x,y),
        "rational_gauge_multiplier":Q(2),
        "successor_outputs":(x+1,y+1),
        "outputs_inequivalent":True,
        "S_action_descends_to_Connes_X":False,
    }


def prime_jet_half_density(p:int,k:int,source_id="Z-integer-modular-source",epoch=0):
    """Genuine local p^k yields C_p(p^k)^2=p^-k, not log(p)/p^(k/2).

    Primitive orbit log(p), contact, Fourier, Haar and signs still needed.
    """
    _prime(p)
    if type(k) is not int or not 1<=k<=64:
        raise ConnesBridgeError("positive integer prime jet depth 1..64 required")
    receipt=local_fixed_point(RationalScale(Q(p)**k,source_id,epoch),p,1)
    if receipt.off_identity_coefficient!=1 or receipt.half_density_coefficient_squared!=Q(1,p**k):
        raise AssertionError("prime jet local half-density failed")
    return {
        "genuine_prime":p,"jet_depth":k,"adelic_local_scale":Q(p)**k,
        "local_fixed_point_scalar":Q(1),
        "half_density_coefficient_squared":Q(1,p**k),
        "primitive_orbit_length_symbol":f"log({p})",
        "candidate_Weil_weight_symbol":f"log({p})/sqrt({p}^{k})",
        "full_Connes_trace_and_sign_verified":False,
        "source_id":source_id,"epoch":epoch,
    }
