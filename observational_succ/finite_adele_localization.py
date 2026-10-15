"""Finite-source localization interface for the finite adele ring of Q.

CLASSICAL THEOREM (not produced by finite computations):
    Zhat = inverse_limit_n Z/nZ ~= product_p Z_p
    A_f(Q) ~= S^-1 Zhat ~= Q tensor_Z Zhat, S=Z\\{0},
as topological rings, with the restricted product topology under the
identification. A finite presented span (u,d), u a declared computable
profinite program and d>0, represents u/d; not every adele has a finite
computable description. Equality of arbitrary such global programs is NOT
decided by finitely many local residues.

Adding the full Archimedean REAL carrier produces A_Q=R x A_f.
A rational Archimedean coordinate is only a dense local chart, not R.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .edge_carrier_reconstruction import (
    EdgeCarrierError, ProfiniteProgram, RationalSpan, integer, prime,
)


@dataclass(frozen=True)
class FiniteAdeleSpan:
    """Source-typed computably presented member of Zhat[1/nonzero Z]."""
    numerator: ProfiniteProgram
    denominator: int = 1

    def __post_init__(self) -> None:
        if not isinstance(self.numerator, ProfiniteProgram):
            raise EdgeCarrierError("The numerator must be a genuine profinite source program")
        if type(self.denominator) is not int or self.denominator < 1:
            raise EdgeCarrierError("Localization denominator must be a nonzero positive integer")

    @classmethod
    def diagonal_rational(cls, x: RationalSpan, *,
                          source_id: str = "Z-integer-modular-source",
                          epoch: int = 0) -> "FiniteAdeleSpan":
        if not isinstance(x, RationalSpan):
            raise EdgeCarrierError("Diagonal Q embedding requires a genuine rational source arrow")
        return cls(ProfiniteProgram.integer(x.numerator,source_id=source_id,epoch=epoch),x.denominator)

    def _compatible(self, other: "FiniteAdeleSpan") -> None:
        if (not isinstance(other,FiniteAdeleSpan) or
            (self.numerator.source_id,self.numerator.epoch) !=
            (other.numerator.source_id,other.numerator.epoch)):
            raise EdgeCarrierError("Only glue original-source compatible finite adeles")

    def add(self, other: "FiniteAdeleSpan") -> "FiniteAdeleSpan":
        self._compatible(other)
        L=ProfiniteProgram.integer(other.denominator,source_id=self.numerator.source_id,epoch=self.numerator.epoch)
        R=ProfiniteProgram.integer(self.denominator,source_id=self.numerator.source_id,epoch=self.numerator.epoch)
        u=self.numerator.multiply(L).add(other.numerator.multiply(R))
        return FiniteAdeleSpan(u,self.denominator*other.denominator)

    def multiply(self,other:"FiniteAdeleSpan")->"FiniteAdeleSpan":
        self._compatible(other)
        return FiniteAdeleSpan(self.numerator.multiply(other.numerator),
                               self.denominator*other.denominator)

    def cross_relation_at(self, other: "FiniteAdeleSpan", modulus: int) -> dict:
        """Necessary finite probe for u/d = v/e, NOT a global decision."""
        self._compatible(other)
        lhs=(other.denominator*self.numerator.residue(modulus))%modulus
        rhs=(self.denominator*other.numerator.residue(modulus))%modulus
        return {
            "modulus":modulus,"left_cross_residue":lhs,
            "right_cross_residue":rhs,"agrees_at_this_probe":lhs==rhs,
            "global_fraction_equality_from_one_probe":False,
            "denominator_multiplication_is_globally_injective":
                "CLASSICAL_TORSION_FREE_ZHAT",
            "RH_proved":False,
        }

    def local_integral_scaled(self,p:int,k:int)->dict:
        """Exact k-digit p-adic residue after clearing p part of denominator.

        d = p^v*u, with gcd(u,p)=1. x_p = p^-v y_p where
        y_p = u^-1 * numerator_p belongs to Z_p.
        k digits of y_p are computable from the original residue program.
        This reports a guaranteed lower valuation shift -v, not the
        exact valuation if numerator itself has additional p factors.
        """
        if not prime(p) or type(k) is not int or not 1<=k<=30:
            raise EdgeCarrierError("Genuine p and a bounded positive p-adic depth required")
        d=self.denominator
        v=0
        while d%p==0:
            d//=p
            v+=1
        modulus=p**k
        if modulus > 2_000_000:
            raise EdgeCarrierError('p-adic local probe exceeds source finite-clock resource bound')
        numerator=self.numerator.residue(modulus)
        integral=(numerator*pow(d,-1,modulus))%modulus
        return {
            "prime":p,"depth":k,"source_id":self.numerator.source_id,
            "denominator_p_order":v,
            "declared_scale_exponent":-v,
            "residue_of_p_to_v_times_x":integral,
            "modulus":modulus,
            "exact_qp_element_computed":False,
            "local_rational_chart_generated":True,
            "RH_proved":False,
        }


@dataclass(frozen=True)
class RationalArchimedeanAdeleChart:
    """A rational-arch coordinate in the FULL A_Q=R x A_f carrier.

    The rational component is not all R; full Tate topology/Haar measure
    are classical mathematical imports, not reconstructed by this code.
    """
    real: Fraction
    finite: FiniteAdeleSpan

    def __post_init__(self) -> None:
        if not isinstance(self.finite,FiniteAdeleSpan) or type(self.real) not in (int,Fraction):
            raise EdgeCarrierError("Rational real chart + genuine finite adele span required")
        object.__setattr__(self,"real",Fraction(self.real))

    @classmethod
    def diagonal_rational(cls,x:RationalSpan)->"RationalArchimedeanAdeleChart":
        if not isinstance(x,RationalSpan):
            raise EdgeCarrierError("Genuine Q arithmetic source required")
        return cls(x.as_fraction(),FiniteAdeleSpan.diagonal_rational(x))

    def add(self,other:"RationalArchimedeanAdeleChart")->"RationalArchimedeanAdeleChart":
        if not isinstance(other,RationalArchimedeanAdeleChart):
            raise EdgeCarrierError("Only add compatible original rational Archimedean charts")
        return RationalArchimedeanAdeleChart(self.real+other.real,self.finite.add(other.finite))

    def multiply(self,other:"RationalArchimedeanAdeleChart")->"RationalArchimedeanAdeleChart":
        if not isinstance(other,RationalArchimedeanAdeleChart):
            raise EdgeCarrierError("Only multiply genuine rational Archimedean charts")
        return RationalArchimedeanAdeleChart(self.real*other.real,self.finite.multiply(other.finite))


def local_idempotent_is_a_nonrational_adele(p:int)->dict:
    """True properness of the diagonal rational subgroup within A_f.

    e_p∈Zhat has p-component 1 and all other q-components 0.
    If diagonal rational a/b matched e_p, then a/b=0 in Q_q for
    any q!=p, which implies a=0, contradicting its p-component 1.
    """
    if not prime(p):
        raise EdgeCarrierError("A genuine finite place is required")
    point=FiniteAdeleSpan(ProfiniteProgram.projector(p),1)
    q=3 if p==2 else 2
    atp=point.local_integral_scaled(p,2)
    atq=point.local_integral_scaled(q,2)
    if atp["residue_of_p_to_v_times_x"] != 1 or atq["residue_of_p_to_v_times_x"] != 0:
        raise AssertionError("The nonrational local component witness failed")
    return {
        "p":p,"other_prime":q,
        "at_p":atp,"at_q":atq,
        "lies_in_Zhat":True,"lies_in_finite_adeles":True,
        "is_diagonal_rational":False,
        "full_Adele_inverse_limit_constructed_by_finite_probe":False,
        "rational_R_component_supplied":False,
        "RH_proved":False,
    }


def finite_adele_nonfield_control(p:int=2, q:int=3)->dict:
    """Idempotent zero divisors: A_f is a ring, not a field."""
    if not prime(p) or not prime(q) or p==q:
        raise EdgeCarrierError("Distinct genuine primes required")
    one=ProfiniteProgram.integer(1)
    negative=ProfiniteProgram.integer(-1)
    ep=ProfiniteProgram.projector(p)
    complement=one.add(negative.multiply(ep))
    left=FiniteAdeleSpan(ep)
    right=FiniteAdeleSpan(complement)
    for n in (p,q,p*q,p*p*q):
        if left.multiply(right).numerator.residue(n)!=0:
            raise AssertionError("Idempotent adelic zero divisor failed")
    if left.numerator.residue(p)!=1 or right.numerator.residue(q)!=1:
        raise AssertionError("Zero factors must be genuinely nonzero")
    return {
        "p":p,"q":q,
        "left_nonzero":True,"right_nonzero":True,
        "product_zero_in_all_finite_stages":"CLASSICAL_IDEMPOTENT_LAW",
        "finite_adeles_are_a_field":False,
        "RH_proved":False,
    }
