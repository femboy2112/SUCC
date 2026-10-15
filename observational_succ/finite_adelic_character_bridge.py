"""The finite adelic phase quotient and Pontryagin interface to profinite Z.

CLASSICAL EXACT SEQUENCE (locally compact abelian groups):
  0 -> Zhat -> A_f(Q) -> Q/Z -> 0.
For a restricted adele x=u/d (u in Zhat, d positive integer), the
quotient phase is sum_p {x_p}_p modulo 1, finite over p|d. Its kernel is
exactly Zhat and diagonal Q maps onto Q/Z with kernel Z.

The Tate standard character has finite sign - and real sign +:
 psi_f(x)=exp(-2*pi*i*quotient_phase(x)).
Thus chi_r(z)=exp(+2*pi*i*quotient_phase(r*z)) = psi_f(-r*z),
r in Q/Z, z in Zhat. NO unexplained sign change is allowed.

Computation uses finitely represented existing SUCC programs and exact
Fraction values. Statements over every p-adic value and Pontryagin
topological completeness are CLASSICAL imported proofs in the dossier.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

from .edge_carrier_reconstruction import (
    EdgeCarrierError, ProfiniteProgram, RationalSpan, prime,
)
from .finite_adele_localization import FiniteAdeleSpan
from .pontryagin_source_duality import (
    PontryaginSourceError, RationalCircleCharacter, _fraction
)


def _factor(n: int) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or not 1 <= n <= 2_000_000:
        raise PontryaginSourceError("Finite exceptional-prime factorization budget exceeded")
    residual=n
    factors=[]
    p=2
    while p*p<=residual:
        if residual%p == 0:
            v=0
            while residual%p == 0:
                residual//=p
                v+=1
            factors.append((p,v))
        p+=1
    if residual>1:
        factors.append((residual,1))
    return tuple(factors)


def finite_principal_parts(x: FiniteAdeleSpan) -> dict[int,F]:
    """Exact p-adic principal fractions of u/d, only for p dividing d.

    With d=p^v*d' and p not dividing d', the p-component of u/d has
    principal part ((u mod p^v)*inverse(d' mod p^v) mod p^v)/p^v.
    An arbitrary profinite numerator u is handled by *one genuine*
    residue query at the required p^v.
    """
    if not isinstance(x, FiniteAdeleSpan):
        raise PontryaginSourceError("A genuine source-typed finite adele fraction is required")
    d=x.denominator
    parts={}
    for p, v in _factor(d):
        m=p**v
        unit=d//m
        residue=x.numerator.residue(m)
        a=(residue*pow(unit,-1,m))%m
        if a:
            parts[p]=F(a,m)
    return parts


def finite_adele_phase(x: FiniteAdeleSpan) -> F:
    """The positive sum of p-principal parts, an element Q/Z."""
    return sum(finite_principal_parts(x).values(),F(0))%1


def finite_tate_character_phase(x: FiniteAdeleSpan) -> F:
    """The NEGATIVE finite-component Tate phase with exp(2πi * phase)."""
    return (-finite_adele_phase(x)) % 1


def quotient_receipt(x: FiniteAdeleSpan) -> dict:
    """Finite tested quotient map A_f -> Q/Z and exact integral kernel test."""
    parts=finite_principal_parts(x)
    phase=sum(parts.values(),F(0))%1
    # For coprime prime powers, distinct nonzero principal parts cannot
    # cancel modulo Z: the CRT decomposition Q/Z=direct_sum_p Q_p/Z_p.
    kernel_by_local=not parts
    kernel_by_phase=(phase==0)
    if kernel_by_local != kernel_by_phase:
        raise AssertionError("Q/Z sum destroyed genuine prime-component information")
    return {
        "source_id":x.numerator.source_id, "epoch":x.numerator.epoch,
        "denominator":x.denominator,
        "exceptional_prime_principal_parts":tuple(sorted(parts.items())),
        "quotient_phase":phase,
        "Tate_finite_negative_phase":(-phase)%1,
        "kernel_by_local_p_integrality":kernel_by_local,
        "kernel_by_global_Q_mod_Z_phase":kernel_by_phase,
        "exact_kernel_agreement":True,
        "all_adeles_have_finite_programs":False,
        "full_topological_sequence_proved_by_samples":False,
        "RH_proved":False,
    }


def quotient_additive_naturality(x: FiniteAdeleSpan,
                                y: FiniteAdeleSpan) -> dict:
    """The quotient map respects addition of actual finite adele source."""
    try:
        sum_xy=x.add(y)
    except EdgeCarrierError as err:
        raise PontryaginSourceError("Cannot glue incompatible finite adele sources") from err
    lhs=finite_adele_phase(sum_xy)
    rhs=(finite_adele_phase(x)+finite_adele_phase(y))%1
    if lhs!=rhs:
        raise AssertionError("Finite-adele quotient is not an additive character")
    return {"phase_of_sum":lhs,"sum_of_phases":rhs,
            "quotient_homomorphism_verified":True}


def diagonal_rational_reciprocity(q: int|F, *,
                                  source_id: str="Z-integer-modular-source",
                                  epoch: int=0) -> dict:
    """The all-place rational diagonal has zero total Tate phase.

    plus real q, minus finite sum of principal parts = integer.
    Normalization is exact; no infinite physical observer used.
    """
    r=_fraction(q,"Diagonal rational")
    x=FiniteAdeleSpan.diagonal_rational(RationalSpan(r.numerator,r.denominator),
                                       source_id=source_id,epoch=epoch)
    finite=finite_adele_phase(x)
    total=(r-finite)%1
    if total:
        raise AssertionError("Original global Q character failed reciprocity")
    return {"q":r, "finite_positive_phase":finite,
            "real_positive_phase":r%1,
            "finite_negative_Tate_phase":(-finite)%1,
            "all_places_total_phase":total,
            "global_diagonal_character_trivial":True,
            "original_source":"Q diagonal and ordinary real + finite p-adic - signs",
            "RH_proved":False}


def character_adele_pairing(r: RationalCircleCharacter,
                           z: ProfiniteProgram) -> dict:
    """Two independent routes to the same Pontryagin character phase.

    Direct: (a/n)*(z mod n) mod 1.
    Adelic: take the true finite adele r*z, sum its p-principal parts;
    standard Tate character for the same frequency is ψ_f(-r*z).
    """
    if not isinstance(r,RationalCircleCharacter) or not isinstance(z,ProfiniteProgram) or (
        r.source_id,r.epoch)!=(z.source_id,z.epoch):
        raise PontryaginSourceError("Pair only source-matched Q/Z and Zhat")
    q=r.frequency
    rational_x=FiniteAdeleSpan.diagonal_rational(
        RationalSpan(q.numerator,q.denominator),source_id=r.source_id,epoch=r.epoch
    )
    adele_product=rational_x.multiply(FiniteAdeleSpan(z))
    direct=r.evaluate(z)
    adele=finite_adele_phase(adele_product)
    if direct!=adele:
        raise AssertionError("Finite Tate principal parts do not reconstruct Pontryagin dual character")
    return {
        "frequency":q,"character_phase":direct,
        "finite_adele_principal_sum":adele,
        "finite_Tate_negative_phase":finite_tate_character_phase(adele_product),
        "standard_Tate_negative_is_character_of_minus_r":True,
        "dual_Tate_square_commutes":True,
        "source_id":r.source_id, "epoch":r.epoch,
        "global_topological_duality_verified_by_finite_test":False,
        "RH_proved":False,
    }


def annihilator_probe(x: FiniteAdeleSpan) -> dict:
    """A SOURCE-DERIVED witnessing z=e_p in Zhat for nonintegral x∈Af.

    If x_p is nonintegral, multiplication by the prime projector e_p
    isolates that place, so ψ_f(x*e_p) is nontrivial. Therefore the
    annihilator of Zhat in Af is Zhat itself (CLASSICAL; proof in dossier).
    """
    parts=finite_principal_parts(x)
    if not parts:
        return {
            "lies_in_Zhat":True,"annihilates_Zhat":True,
            "separating_prime":None,"separating_Tate_phase":F(0),
            "full_annihilator_equals_Zhat":"CLASSICAL_ADDITIVE_FOURIER_PROOF",
            "RH_proved":False
        }
    p=next(iter(sorted(parts)))
    projector=ProfiniteProgram.projector(
        p,source_id=x.numerator.source_id,epoch=x.numerator.epoch
    )
    isolated=x.multiply(FiniteAdeleSpan(projector))
    phase=finite_tate_character_phase(isolated)
    if phase==0 or phase!=(-parts[p])%1:
        raise AssertionError("A source-local projector cannot separate nonintegral adele")
    return {
        "lies_in_Zhat":False,"annihilates_Zhat":False,
        "separating_prime":p,"separating_Tate_phase":phase,
        "projector_source_residue":projector.residue(p),
        "full_annihilator_equals_Zhat":"CLASSICAL_ADDITIVE_FOURIER_PROOF",
        "RH_proved":False
    }


def finite_adelic_extension_non_split(n: int) -> dict:
    """Classical algebraic obstruction: no GROUP section Q/Z -> Af.

    Af is a Q-vector space and is therefore torsion-free; Q/Z has
    nonzero torsion. Any group section would embed torsion into Af.
    Code checks one natural lift, not every putative section.
    """
    if type(n) is not int or not 2 <= n <= 10000:
        raise PontryaginSourceError("Choose a finite torsion order n>=2")
    r=F(1,n)
    point=FiniteAdeleSpan.diagonal_rational(RationalSpan(1,n))
    multiplier=FiniteAdeleSpan.diagonal_rational(RationalSpan(n))
    multiplied=point.multiply(multiplier)
    phase_before=finite_adele_phase(point)
    phase_after=finite_adele_phase(multiplied)
    if phase_before!=r or phase_after!=0 or multiplied.numerator.residue(2)!=1:
        raise AssertionError("Adelic lift torsion obstruction not calibrated")
    return {
        "quotient_torsion_class":r,"torsion_order":n,
        "lift_adele_nonzero":True,"n_times_lift_is_Zhat_nonzero":True,
        "n_times_lift_phase":phase_after,
        "exact_sequence_splits_as_groups":False,
        "non_split_proof":"Af additive torsion-free but Q/Z nonzero torsion",
        "a_set_theoretic_section_is_forbidden":False,
        "full_theorem_proved_by_one_example":False,
        "RH_proved":False,
    }
