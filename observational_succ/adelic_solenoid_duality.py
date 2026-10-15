"""Rational-chart realization of the global compact adelic solenoid.

CLASSICAL HOMOGENEOUS CARRIER:
   A_Q / Q ~= (R x Zhat)/diag(Z)
where Zhat is the original projective SUCC finite-clock carrier.

Our code restricts the REAL coordinate to rationals and the Zhat point
to an existing finite-program source. It proves exact class/gauge
covariance on this dense source chart, not topological completeness of
the full quotient or an algorithm deciding arbitrary Zhat equality.

For every q in Q, the global character on [t,z] is
   exp(2*pi*i*( q*t - pp(q*z) )),
matching Tate's REAL (+), FINITE (-) character convention.
The complete continuous character group of the solenoid is Q_discrete
as a classical Pontryagin theorem, proved in the research dossier.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .edge_carrier_reconstruction import (
    EdgeCarrierError, ProfiniteProgram, RationalSpan
)
from .finite_adele_localization import FiniteAdeleSpan
from .finite_adelic_character_bridge import (
    finite_adele_phase, finite_principal_parts
)
from .pontryagin_source_duality import PontryaginSourceError
from .diagonal_adele_zeta import factor_positive
from .tate_lattice_descent import (
    RationalSChart, character_naturality
)


def _fraction(x,name:str)->F:
    if type(x) not in (int,F):
        raise PontryaginSourceError(f"Original {name} must be exact rational")
    return F(x)


def _int(x,name:str)->int:
    if type(x) is not int:
        raise PontryaginSourceError(f"Original {name} must be exact integer")
    return x


@dataclass(frozen=True)
class RationalSolenoidChart:
    """One rational Archimedean coordinate + finitely named profinite point."""
    real: F
    integral_finite: ProfiniteProgram

    def __post_init__(self) -> None:
        object.__setattr__(self,"real",_fraction(self.real,"real source coordinate"))
        if not isinstance(self.integral_finite,ProfiniteProgram):
            raise PontryaginSourceError("Integral finite source must be Zhat program")

    @property
    def source_id(self)->str:
        return self.integral_finite.source_id

    @property
    def epoch(self)->int:
        return self.integral_finite.epoch

    def diagonal_integer_shift(self,n:int)->"RationalSolenoidChart":
        """Gauge [t,z]=[t+n,z+n]. Keep an explicit source shift receipt."""
        k=_int(n,"diagonal gauge")
        # This is a QUOTIENT-STATE chart, not a causal event receipt.
        # The identity gauge must preserve its normal form literally;
        # otherwise adding the symbolic zero changes dataclass structure
        # even though every genuine modular observation is unchanged.
        if k==0:
            return self
        scalar=ProfiniteProgram.integer(k,source_id=self.source_id,epoch=self.epoch)
        return RationalSolenoidChart(self.real+k,self.integral_finite.add(scalar))

    def canonical(self)->"RationalSolenoidChart":
        """Choose real coordinate [0,1), with compensating integer shift."""
        k=self.real.numerator//self.real.denominator
        transformed=self.diagonal_integer_shift(-k)
        if not F(0)<=transformed.real<F(1):
            raise AssertionError("Rational real solenoid gauge not canonical")
        return transformed

    def equal_on_probe(self,other:"RationalSolenoidChart",modulus:int)->bool:
        """Necessary stage equality, NOT equality of arbitrary global points.

        Two classes agree iff their real-coordinate difference k is INTEGER
        and their profinite difference is diagonal k, on every modulus.
        """
        if not isinstance(other,RationalSolenoidChart) or (
            self.source_id,self.epoch)!=(other.source_id,other.epoch):
            raise PontryaginSourceError("Cannot compare mismatched carrier sources")
        if type(modulus) is not int or modulus<1 or modulus>2_000_000:
            raise PontryaginSourceError("One bounded genuine modular source probe required")
        k=other.real-self.real
        if k.denominator!=1:
            return False
        return (other.integral_finite.residue(modulus)-
                self.integral_finite.residue(modulus))%modulus == int(k)%modulus

    def character(self,q:int|F)->dict:
        """Evaluate the actual Tate global rational spectral character."""
        freq=_fraction(q,"dual rational character label")
        rational=RationalSpan(freq.numerator,freq.denominator)
        r=FiniteAdeleSpan.diagonal_rational(
            rational,source_id=self.source_id,epoch=self.epoch
        )
        product=r.multiply(FiniteAdeleSpan(self.integral_finite))
        positive_finite=finite_adele_phase(product)
        phase=(freq*self.real-positive_finite)%1
        return {
            "dual_frequency":freq,"source_id":self.source_id,
            "epoch":self.epoch,"real_plus_angle":(freq*self.real)%1,
            "finite_positive_principal_angle":positive_finite,
            "finite_Tate_negative_angle":(-positive_finite)%1,
            "global_Tate_character_phase":phase,
            "finite_character_is_typed":True,
            "RH_proved":False,
        }

    def gauge_character_naturality(self,q:int|F,k:int)->dict:
        """Check diag Z gauge invariance of every rational character."""
        before=self.character(q)
        after=self.diagonal_integer_shift(k).character(q)
        if before["global_Tate_character_phase"]!=after["global_Tate_character_phase"]:
            raise AssertionError("Global Tate character does not descend to A/Q")
        return {
            "step":k, "dual_rational":_fraction(q,"character"),
            "phase_before":before["global_Tate_character_phase"],
            "phase_after":after["global_Tate_character_phase"],
            "global_quotient_naturality":True,
            "all_global_points_finitely_checked":False,
        }

    def crosscheck_tate_S_atlas(self,q:int|F,
                               extra_primes:tuple[int,...]=())->dict:
        """Third independent previous Tate atlas model for same source phase.

        Choose S containing genuine denominator primes of q. At each p|den q,
        only k-digit residue z mod p^k is needed for {q*z}_p.
        Extra places must have integral q and therefore contribute zero.
        """
        freq=_fraction(q,"Tate S-character")
        base=tuple(sorted(factor_positive(freq.denominator)))
        from .edge_carrier_reconstruction import prime
        if type(extra_primes) is not tuple or any(not prime(p) for p in extra_primes):
            raise PontryaginSourceError("Only finite genuine S-place extensions")
        primes=tuple(sorted(set(base).union(extra_primes)))
        locals_={}
        for p in primes:
            n=freq.denominator
            exponent=0
            while n%p==0:
                n//=p
                exponent+=1
            modulus=p**max(1,exponent)
            locals_[p]=F(self.integral_finite.residue(modulus))
        chart=RationalSChart.from_places(
            primes,self.real,locals_,source_id=self.source_id,epoch=self.epoch
        )
        before=self.character(freq)["global_Tate_character_phase"]
        old=chart.character_phase(freq)
        projection=character_naturality(chart,base,freq)
        if before!=old or not projection["commutes"]:
            raise AssertionError("Original source rationals lost on Tate S-refinement")
        return {
            "source":self.source_id,"dual_frequency":freq,
            "original_character_phase":before,"old_Tate_phase":old,
            "S_places":primes,"minimal_S_places":base,
            "classical_Tate_refinement_square":projection["commutes"],
            "three_way_exact_agreement":True,
            "full_adelic_self_duality_finitely_verified":False,
        }

    def exact_nonzero_witness(self,modulus:int|None=None)->dict:
        """Conditionally separate nonzero classes with an explicit finite source probe.

        After canonical gauge [t,z], t∈[0,1). If t!=0, q=1 detects it
        because pp(z)=0. Otherwise a supplied modulus with z_n!=0
        gives q=1/n and a nonzero root. A missing source probe is not
        silently replaced by an omniscient zero oracle.
        """
        x=self.canonical()
        if x.real:
            q=F(1)
            reason="nonzero real canonical chart in [0,1)"
        else:
            if type(modulus) is not int or modulus<2:
                raise PontryaginSourceError("A nonzero Zhat source needs a genuine separating modulus")
            residue=x.integral_finite.residue(modulus)
            if residue==0:
                raise PontryaginSourceError("This probe cannot separate a zero observed residue")
            q=F(1,modulus)
            reason="nonzero original finite residue at supplied modulus"
        phase=x.character(q)["global_Tate_character_phase"]
        if phase==0:
            raise AssertionError("Specified original source separation failed")
        return {
            "original_real":self.real,"canonical_real":x.real,
            "character_witness_q":q,"nontrivial_phase":phase,
            "reason":reason,"certified_distinct_from_zero_in_quotient":True,
            "all_profinite_points_zero_decidable":False,
            "RH_proved":False,
        }


def quotient_adele_representative(
    real:int|F,finite:FiniteAdeleSpan
)->dict:
    """Recover a solenoid chart from the actual original (real, finite) adele.

    Pick alpha=pp(finite)∈Q/Z; subtract the *diagonal rational* alpha
    from both places, making finite component integral. The real change
    is source justified and we retain the exact original finite-adelic
    integral object as a numerator/denominator expression. This adapter
    does not magically DECIDE equality or construct a full program for it.
    """
    arch=_fraction(real,"Archimedean real chart")
    if not isinstance(finite,FiniteAdeleSpan):
        raise PontryaginSourceError("A genuine finite-adelic source required")
    alpha=finite_adele_phase(finite)
    rational=RationalSpan(alpha.numerator,alpha.denominator)
    lifted=FiniteAdeleSpan.diagonal_rational(
        rational,source_id=finite.numerator.source_id,epoch=finite.numerator.epoch
    )
    negative=FiniteAdeleSpan.diagonal_rational(
        RationalSpan(-1),source_id=finite.numerator.source_id,epoch=finite.numerator.epoch
    )
    z=finite.add(lifted.multiply(negative))
    if finite_adele_phase(z)!=0:
        raise AssertionError("Rational diagonal lift did not reach finite integral subgroup")
    return {
        "original_arch":arch,"original_finite":finite,
        "principal_part":alpha,"solenoid_real":arch-alpha,
        "integral_finite_adele_source":z,
        "finite_component_integral":True,
        "global_quotient_is_solenoid":"CLASSICAL_OPEN_SUBGROUP_ARGUMENT",
        "every_integral_finite_adele_computably_resolved":False,
        "RH_proved":False
    }


def adelic_solenoid_abstract_duality_receipt()->dict:
    """Typed declaration of a CLASSICAL theorem and its proof dependencies."""
    return {
        "global_carrier":"A_Q / diagonal(Q)",
        "identified_presentation":"(R x Zhat) / diagonal(Z)",
        "annihilator_in_R_cross_Zhat":"(lambda,r) with lambda+r integer",
        "lambda_real_frequency":"forced to be rational",
        "profinite_dual":"Q/Z with discrete topology",
        "completed_global_dual":"Q with discrete topology",
        "global_full_adelic_selfdual_group":"CLASSICAL_LOCAL_HAAR_PONTRYAGIN_INPUT",
        "diagonal_Q_annihilator":"Q",
        "covolume":"1 under vol(Zp)=1 and real Lebesgue",
        "formal_topological_proofs":"RESEARCH_PAPER_SECTION",
        "inferred_from_samples":False,
        "RH_proved":False,
    }
