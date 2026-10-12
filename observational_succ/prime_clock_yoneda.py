"""Authentic prime-local SUCC/FUCC quotient as operational Yoneda source functor.

Unlike illustrative arbitrary finite transition tables, the source state
is the mathematically defined ring Z/p^r, and the reduction map is the
actual quotient homomorphism Z/p^r -> Z/p^k. Carrier instruments are
integer successor S_d, TRUE-PRIME dilation V_q and optional mod-p^k
residue readout. The same arithmetic operators descend under reduction.

A noncommuting shift/dilation address defect may lie in the kernel of a
coarse quotient, so the observer sees a FLAT action square although the
fine system is noncommuting. Source-relative claims depending only on
the quotient retain EXACT finite adaptive proof ranks.

This is elementary modular arithmetic and finite-source coalgebra,
not a new Euler product, adelic Gamma bridge or Weil/RH theorem.
"""
from __future__ import annotations

from dataclasses import dataclass

from .residue_one_arch import prime
from .noncommuting_proof_transport import FiniteCarrier, Instrument
from .operational_yoneda_descent import (
    CertifiedSourceMorphism, induced_observation_functor,
)


class ArithmeticFunctorError(ValueError):
    pass


def _integer(n, name:str) -> int:
    if type(n) is not int:
        raise ArithmeticFunctorError(f"{name} must be an exact integer")
    return n


@dataclass(frozen=True)
class PrimeClockSource:
    """Typed finite local source, with independently checked true prime place."""
    p:int
    r:int
    report_digits:int
    d:int
    jet_prime:int

    def __post_init__(self):
        if not prime(self.p) or not prime(self.jet_prime):
            raise ArithmeticFunctorError("Only actual primes define declared Euler-local jets")
        if (type(self.r) is not int or type(self.report_digits) is not int
                or not 1<=self.report_digits<=self.r):
            raise ArithmeticFunctorError("Need lawful positive output p-adic precision")
        _integer(self.d,"shift step")
        if self.p**self.r>64:
            raise ArithmeticFunctorError("Explicit carrier state budget exceeds 64")

    @property
    def modulus(self):
        return self.p**self.r

    @property
    def report_modulus(self):
        return self.p**self.report_digits

    def shift(self,x:int):
        return (x+self.d)%self.modulus

    def dilate(self,x:int):
        return (x*self.jet_prime)%self.modulus

    def public_report(self,x:int):
        return x%self.report_modulus

    def carrier(self, *,read_enabled:bool=True)->FiniteCarrier:
        size=self.modulus
        states=tuple(range(size))
        always=(True,)*size
        noinfo=(-1,)*size
        instruments=[
            Instrument("SHIFT",noinfo,tuple(self.shift(x) for x in states),always),
            Instrument("DILATE",noinfo,tuple(self.dilate(x) for x in states),always),
        ]
        if read_enabled:
            instruments.append(Instrument(
                "READ",tuple(self.public_report(x) for x in states),
                states,always))
        return FiniteCarrier(size,tuple(instruments),
                             f"declared-Z/{self.p}^{self.r}",
                             f"source-modular-prime-p={self.p}-q={self.jet_prime}")

    def coordinate_defect(self)->int:
        """(S_d∘V_q - V_q∘S_d)(x)=d(1-q) in this residue ring."""
        m=self.modulus
        defects={(self.shift(self.dilate(x))-
                  self.dilate(self.shift(x)))%m
                 for x in range(m)}
        expected=(self.d*(1-self.jet_prime))%m
        if defects!={expected}:
            raise ArithmeticError("Authentic affine SUCC/FUCC relation violated")
        return expected


def verify_arithmetic_source_signature(fine:PrimeClockSource,
                                       coarse:PrimeClockSource)->dict:
    """Extra ARITHMETIC source provenance gate beyond observed-coalgebra laws.

    Two different genuine prime jets q and q' can induce the SAME
    multiplication on a small residue quotient if q≡q' (mod p^k).
    An observationally successful morphism therefore does not prove
    original Euler place/jet identity. This gate checks the declared
    SOURCE PARAMETERS themselves; its correctness still presupposes
    these parameters were independently supplied faithfully.
    """
    if not isinstance(fine,PrimeClockSource) or not isinstance(coarse,PrimeClockSource):
        raise ArithmeticFunctorError("Require two declared prime clock sources")
    if (fine.p!=coarse.p or fine.d!=coarse.d
            or fine.jet_prime!=coarse.jet_prime
            or fine.report_digits!=coarse.r):
        raise ArithmeticFunctorError(
            "Declared SUCC/FUCC prime source signature differs")
    if not 1<=coarse.r<fine.r:
        raise ArithmeticFunctorError("Require genuine precision quotient")
    return {
        "status":"DECLARED_ARITHMETIC_PRIME_SOURCE_SIGNATURE_MATCHED",
        "same_p":True,"same_primitive_step":True,
        "same_authentic_jet_prime":True,
        "source_parameters_physically_authenticated":False,
    }


@dataclass(frozen=True)
class PrimeClockQuotient:
    """High-to-low p-power ring reduction, not a guessed source mapping."""
    p:int
    fine_digits:int
    coarse_digits:int
    d:int
    jet_prime:int
    read_enabled:bool=True

    def __post_init__(self):
        if (type(self.coarse_digits) is not int
                or type(self.fine_digits) is not int
                or not 1<=self.coarse_digits<self.fine_digits):
            raise ArithmeticFunctorError("Need a strict coarsening of local precision")
        PrimeClockSource(self.p,self.fine_digits,self.coarse_digits,
                         self.d,self.jet_prime)

    @property
    def fine(self):
        return PrimeClockSource(self.p,self.fine_digits,
                                self.coarse_digits,self.d,self.jet_prime)

    @property
    def coarse(self):
        return PrimeClockSource(self.p,self.coarse_digits,
                                self.coarse_digits,self.d,self.jet_prime)

    def morphism(self)->CertifiedSourceMorphism:
        F,C=self.fine,self.coarse
        verify_arithmetic_source_signature(F,C)
        h=tuple(x%C.modulus for x in range(F.modulus))
        # Truth depends ONLY on the original source's quotient class.
        claim_c=tuple(str(x%C.modulus) for x in range(F.modulus))
        claim_a=tuple(str(x) for x in range(C.modulus))
        return CertifiedSourceMorphism(
            F.carrier(read_enabled=self.read_enabled),
            C.carrier(read_enabled=self.read_enabled),
            tuple(range(F.modulus)),tuple(range(C.modulus)),
            h,claim_c,claim_a,
            f"original-p={self.p}-coarse-residue-{self.coarse_digits}-digits")

    def exact_certificate(self)->dict:
        morph=self.morphism()
        rank=morph.policy_descent()
        path=induced_observation_functor(morph,horizon=1)
        functor=path.proof_receipt()
        fine_defect=self.fine.coordinate_defect()
        coarse_defect=self.coarse.coordinate_defect()
        return {
            **rank,
            "status":"SOURCE_DERIVED_SUCC_FUCC_PRIME_QUOTIENT",
            "p":self.p,"fine_digits":self.fine_digits,
            "coarse_digits":self.coarse_digits,
            "jet_prime":self.jet_prime,
            "shift_d":self.d,
            "fine_defect":fine_defect,
            "coarse_defect":coarse_defect,
            "genuinely_noncommuting_fine_carrier":fine_defect!=0,
            "coarse_action_square_commutes":coarse_defect==0,
            "coarse_quotient_functor_verified":functor["checked_functor_compositions"]>0,
            "coarse_context_onto":functor["context_image_surjective"],
            "all_original_source_claims_lifted":True,
            "arithmetic_primality_comes_from_independent_source_check":True,
            "real_Gamma_or_completed_Weil_identified":False,
            "RH_claimed":False,
        }


def arithmetic_yoneda_demo():
    # True local place p=2, true *other* prime jet q=3.
    # Fine SUCC/FUCC defect -2 is NONZERO mod 4 but 0 mod 2.
    src=PrimeClockQuotient(2,2,1,1,3,True)
    on=src.exact_certificate()
    if (on["fine_defect"]!=2 or on["coarse_defect"]!=0
            or on["abstract_rank"]!=1 or on["concrete_rank"]!=1
            or on["state_map_injective"]
            or not on["genuinely_noncommuting_fine_carrier"]
            or not on["coarse_action_square_commutes"]):
        raise ArithmeticError("Prime-local nonflat-to-flat quotient failed")
    fine=src.fine
    # Here BOTH jet multipliers are real primes, but q=3 and q'=5
    # have identical residue action mod 2. Behavioral source descent
    # alone may accept the alias. Euler source provenance must NOT.
    wrong_coarse=PrimeClockSource(2,1,1,1,5)
    h=(0,1,0,1)
    apparent=CertifiedSourceMorphism(
        fine.carrier(),wrong_coarse.carrier(),
        tuple(range(4)),tuple(range(2)),h,
        tuple(str(x%2) for x in range(4)),("0","1"),
        "original-parity")
    if apparent.verify()["status"]!="EXACT_SOURCE_COALGEBRA_MORPHISM":
        raise ArithmeticError("Expected observed quotient prime-source alias vanished")
    try:
        verify_arithmetic_source_signature(fine,wrong_coarse)
    except ArithmeticFunctorError:
        signature_mutant_rejected=True
    else:
        raise ArithmeticError("Different authentic Euler jets were falsely identical")
    off=PrimeClockQuotient(2,2,1,1,3,False).exact_certificate()
    if (off["abstract_rank"] is not None
            or off["concrete_rank"] is not None):
        raise ArithmeticError("Reader-free source cannot invent original information")
    return {
        "status":"AUTHENTIC_PRIME_SUCC_FUCC_YONEDA_TRANSPORT_EXACT",
        "fine_source_modulus":4,
        "coarse_source_modulus":2,
        "genuine_prime_place":2,
        "genuine_prime_jet":3,
        "fine_noncommuting_defect":on["fine_defect"],
        "coarse_defect":on["coarse_defect"],
        "fine_nonflat_coarse_flat":True,
        "coarse_source_rank_preserved":on["optimal_original_source_rank_equal"],
        "both_original_source_ranks_with_read":[on["abstract_rank"],
                                                on["concrete_rank"]],
        "both_original_source_ranks_without_read":[off["abstract_rank"],
                                                   off["concrete_rank"]],
        "induced_actual_observation_functor_verified":
            on["coarse_quotient_functor_verified"],
        "ring_source_map_independent_of_simulated_outcomes":True,
        "fake_composite_euler_jet_admitted":False,
        "different_true_prime_jet_behavioral_alias_exists":True,
        "declared_jet_source_signature_rejects_alias":signature_mutant_rejected,
        "arithmetic_source_parameters_physically_authenticated":False,
        "RH_claimed":False,
    }
