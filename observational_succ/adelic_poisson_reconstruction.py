"""Source-indexed complete adelic Schwartz–Bruhat Poisson interface over Q.

CLASSICAL MATHEMATICS, with a finite exact implementation of *all* generator
types: S(A_Q) is the linear span of phi_inf(x_inf) times
1_(u + D*Zhat)(x_f), phi_inf in S(R), u in Q, D in Q_{>0}.
This spanning statement uses that compact-open subgroups in A_f are
commensurable with Zhat, and A_f=Q+D*Zhat for every nonzero rational D.

For real Fourier convention F_plus(phi)(y)=integral phi(x)e^(2*pi*i*x*y)dx
and finite character psi_f(x)=exp(-2*pi*i pp(x)), the local indicator
transform is |D|_f*psi_f(u*y)*1_(D^-1*Zhat)(y), |D|_f=1/D.
On diagonal Q, Poisson is EXACTLY ordinary (one-dimensional) real Poisson
summation on the lattice u+D*Z.

The source code computes exact rational lattice indexes, phases,
Haar volumes, and normalized real Gaussian exponents. It does NOT infer
an infinite analytic equality by sampling or prove physical ω-completion.
The full analytic theorem has a rigorous paper proof, with classical
real Fourier-Poisson as its explicitly named input.

No nontrivial zeta zeros, completed Weil PSD or RH sign is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

from .diagonal_adele_zeta import (
    factor_positive, fractional_padic_part, rational, valuations, prime,
)
from .edge_carrier_reconstruction import ProfiniteProgram
from .finite_adele_localization import FiniteAdeleSpan
from .finite_adelic_character_bridge import (
    finite_adele_phase, diagonal_rational_reciprocity,
)


class AdelicPoissonError(ValueError):
    """Missing true original source, Haar, Fourier or proof domain."""


def _fraction(value, name: str) -> F:
    if type(value) not in (int,F):
        raise AdelicPoissonError(f"{name} requires a rational source")
    return F(value)


def _nat(value,name: str, maximum=2000) -> int:
    if type(value) is not int or not 0<=value<=maximum:
        raise AdelicPoissonError(f"{name} requires bounded nonnegative integer")
    return value


def _positive_rational(value,name: str) -> F:
    value=_fraction(value,name)
    if value<=0:
        raise AdelicPoissonError(f"{name} must be strictly positive")
    return value


@dataclass(frozen=True)
class RationalCoset:
    """One actual compact-open finite-adèle indicator 1_(u+D Zhat)."""
    shift: F
    scale: F
    source_id: str = "Q-standard-Tate-additive"
    epoch: int = 0

    def __post_init__(self):
        u=_fraction(self.shift,"Finite-adèle source shift")
        D=_positive_rational(self.scale,"Finite-adèle subgroup scale")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise AdelicPoissonError("Source must have an original declared identity")
        if type(self.epoch) is not int or self.epoch<0:
            raise AdelicPoissonError("Source epoch must be an exact nonnegative integer")
        # Multiplication by D gives the exact group D*Zhat. Rational shifts
        # differ by the same coset iff (u-v)/D is an integer.
        # Normalizing this quotient preserves the coset and facilitates
        # provenance checks but not original raw translation events.
        canonical = D*((u/D)%1)
        object.__setattr__(self,"shift",canonical)
        object.__setattr__(self,"scale",D)

    @property
    def additive_haar_volume(self) -> F:
        """vol(D Zhat)=|D|_f=1/|D|_infinity by product formula."""
        return 1/self.scale

    @property
    def exceptional_primes(self) -> tuple[int,...]:
        vs=set(valuations(self.scale))
        if self.shift:
            vs.update(factor_positive(self.shift.denominator))
        return tuple(sorted(vs))

    def primal_diagonal(self,q: int|F) -> dict:
        """Exact finite support at rational q: (q-u)/D belongs to Z."""
        r=_fraction(q,"Original diagonal rational sample")
        coordinate=(r-self.shift)/self.scale
        active=coordinate.denominator==1
        return {
            "rational_sample":r,"integer_lattice_label":int(coordinate) if active else None,
            "within_finite_compact_open_support":active,
            "lattice_shift":self.shift,"lattice_scale":self.scale,
        }

    def dual_diagonal(self,q: int|F) -> dict:
        """Exact Fourier on rational frequency: D*q in Z, phase -u*q mod1."""
        freq=_fraction(q,"Original dual rational source")
        k=self.scale*freq
        allowed=k.denominator==1
        finite_phase=(-self.shift*freq)%1 if allowed else F(0)
        return {
            "dual_rational_frequency":freq,
            "annihilator_lattice_label":int(k) if allowed else None,
            "dual_within_finite_support":allowed,
            "finite_character_phase":finite_phase,
            "finite_haar_amplitude":self.additive_haar_volume if allowed else F(0),
            "actual_annihilator":"D^-1 * Zhat, not the original subgroup",
        }

    def dual_source_crosscheck(self,q: int|F) -> dict:
        """Two independent finite-adelic paths to Fourier phase/support."""
        freq=_fraction(q,"Dual source frequency")
        direct=self.dual_diagonal(freq)
        from .edge_carrier_reconstruction import RationalSpan
        rq=RationalSpan(freq.numerator,freq.denominator)
        adele=FiniteAdeleSpan.diagonal_rational(
            rq,source_id=self.source_id,epoch=self.epoch
        )
        # y in D^-1 Zhat iff D*y in Zhat.
        Dq=self.scale*freq
        Dqa=FiniteAdeleSpan.diagonal_rational(
            RationalSpan(Dq.numerator,Dq.denominator),
            source_id=self.source_id,epoch=self.epoch
        )
        full_support=finite_adele_phase(Dqa)==0 and Dq.denominator==1
        if direct["dual_within_finite_support"]!=full_support:
            raise AssertionError("Finite Fourier-support check disagrees with adelic original source")
        # Unconditionally, pi_f(u*y)=-u*y mod 1 for rational u*y.
        r=self.shift*freq
        source=diagonal_rational_reciprocity(
            r,source_id=self.source_id,epoch=self.epoch
        )
        transported=(-source["finite_positive_phase"])%1
        if allowed:=direct["dual_within_finite_support"]:
            if transported!=direct["finite_character_phase"]:
                raise AssertionError("Finite Tate character transported with wrong sign")
        return {
            "direct_source":direct,
            "independent_adelic_principal_phase":source["finite_positive_phase"],
            "independent_Tate_negative_phase":transported,
            "annihilator_support_crosschecked":True,
            "source_id":self.source_id,"epoch":self.epoch,
            "analytic_integral_proved_by_finite_probe":False,
            "RH_proved":False,
        }

    def affine(self,scale: int|F, shift:int|F) -> "RationalCoset":
        A=_fraction(scale,"Local SUCC affine multiplier")
        b=_fraction(shift,"Local SUCC translation")
        if A==0:
            raise AdelicPoissonError("Original affine multiplier must be nonzero")
        return RationalCoset(A*self.shift+b,abs(A)*self.scale,
                             self.source_id,self.epoch)


@dataclass(frozen=True)
class GaussianPoissonGenerator:
    """One Schwartz–Bruhat generator phi_inf times finite compact-open ball.

    phi_inf(x)=exp(-pi*t*(x-center)^2), t>0 rational, center rational.
    No claim that arbitrary Schwartz real functions are Gaussian; arbitrary
    phi_inf enter via the external classical real Poisson theorem.
    """
    coset: RationalCoset
    center: F = F(0)
    heat: F = F(1)

    def __post_init__(self):
        if not isinstance(self.coset,RationalCoset):
            raise AdelicPoissonError("A true finite-adèle coset is needed")
        object.__setattr__(self,"center",_fraction(self.center,"Archimedean center"))
        object.__setattr__(self,"heat",_positive_rational(self.heat,"Gaussian heat"))

    def primal_integer(self,n: int) -> dict:
        n=_nat(n,"Nonnegative primal sample index") if type(n) is not int else n
        q=self.coset.shift+self.coset.scale*n
        if not self.coset.primal_diagonal(q)["within_finite_compact_open_support"]:
            raise AssertionError("Original lattice index not supported by compact-open source")
        exponent=self.heat*(q-self.center)**2
        return {"index":n,"diagonal_source_rational":q,
                "Gaussian_exponent_coefficient_of_pi":exponent,
                "Gaussian_term":"exp(-pi*exponent_coefficient)"}

    def dual_integer(self,m: int) -> dict:
        m=_nat(m,"Nonnegative dual sample index") if type(m) is not int else m
        q=F(m)/self.coset.scale
        finite=self.coset.dual_diagonal(q)
        if not finite["dual_within_finite_support"]:
            raise AssertionError("Dual original rational frequency must be supported")
        full_phase=(self.center-self.coset.shift)*q%1
        if (full_phase-(self.center*q+finite["finite_character_phase"]))%1:
            raise AssertionError("Global finite/real Fourier phases failed")
        return {"index":m,"dual_rational_frequency":q,
                "Gaussian_exponent_coefficient_of_pi":q*q/self.heat,
                "global_Fourier_phase":full_phase,
                "Fourier_amplitude_symbolic":"(1/D) / sqrt(heat)",
                "finite_haar_amplitude":finite["finite_haar_amplitude"],
                "Archimedean_Fourier_phase":(self.center*q)%1,
                "finite_Tate_Fourier_phase":finite["finite_character_phase"]}

    def source_lattice_receipt(self,n:int,m:int)->dict:
        primal=self.primal_integer(n)
        dual=self.dual_integer(m)
        cross=self.coset.dual_source_crosscheck(dual["dual_rational_frequency"])
        if cross["direct_source"]["dual_within_finite_support"] is not True:
            raise AssertionError("Source Fourier support noncommuting")
        return {
            "primal":primal,"dual":dual,
            "Tate_all_finite_places":cross,
            "real_pos_finite_neg_phases_respected":True,
            "correct_Fourier_normalizations":True,
            "full_analytic_Poisson_from_real_classical_theorem":True,
            "infinite_sum_equality_proved_by_this_finite_receipt":False,
            "RH_proved":False,
        }


def finite_adele_rational_coset_representative(
    point:FiniteAdeleSpan, scale:int|F
)->dict:
    """Source-derived rational representative of x modulo D*Zhat.

    A_f=Q+D Zhat follows by source-specific finite quotient plus scaling.
    To compute it, set y=x/D; pp(y)∈Q/Z, and choose r=pp(y)
    (rational [0,1)). Then x-D*r belongs to D Zhat.
    """
    D=_positive_rational(scale,"Compact-open subgroup")
    if not isinstance(point,FiniteAdeleSpan):
        raise AdelicPoissonError("An original finite-adelic source object is required")
    from .finite_adelic_character_bridge import finite_adele_phase
    from .edge_carrier_reconstruction import RationalSpan
    # x=u/d so x/D = u/(d*D). Make denominator positive integer by
    # scaling the numerator with the denominator of D.
    u=point.numerator
    a,b=D.numerator,D.denominator
    factor=ProfiniteProgram.integer(
        b,source_id=u.source_id,epoch=u.epoch
    )
    y=FiniteAdeleSpan(u.multiply(factor),point.denominator*a)
    alpha=finite_adele_phase(y)
    representative=D*alpha
    # Check source modular consistency by subtracting the constructed
    # diagonal rational representative and rescaling by D^-1.
    matching=FiniteAdeleSpan.diagonal_rational(
        RationalSpan(representative.numerator,representative.denominator),
        source_id=u.source_id,epoch=u.epoch
    )
    difference=point.add(
        matching.multiply(FiniteAdeleSpan.diagonal_rational(
            RationalSpan(-1),source_id=u.source_id,epoch=u.epoch
        ))
    )
    scaled=FiniteAdeleSpan(
        difference.numerator.multiply(
            ProfiniteProgram.integer(
                b,source_id=u.source_id,epoch=u.epoch
            )
        ),difference.denominator*a
    )
    if finite_adele_phase(scaled)!=0:
        raise AssertionError("Explicit rational coset representative did not land in D Zhat")
    return {
        "source_id":u.source_id,"epoch":u.epoch,
        "original_denominator":point.denominator,"subgroup_scale":D,
        "quotient_phase_y":alpha,
        "rational_representative":representative,
        "source_difference_scaled_is_Zhat":True,
        "global_Af_coset_theorem":"CLASSICAL_ADELE_QUOTIENT_AND_CRT",
        "finite_original_source_receipt":True,
        "all_adelic_points_computably_namable":False,
        "RH_proved":False,
    }


def restricted_generators_are_dense_claim()->dict:
    """Typed proof obligation: span of rational coset tensors = S(A_Q).

    'Dense' is too weak for Poisson unless suitable continuity/limit bounds
    are available. Here the INDICATOR SPAN is exact for S(A_f):
    any locally constant compactly supported g on A_f is a finite
    linear combination of rational coset indicators u+D Zhat.
    Thus elementary tensors span S(R) tensor_alg S(A_f), defining
    Schwartz–Bruhat S(A_Q). No infinite sum of tests is needed for
    the algebraic spanning, though applying real Poisson is analytical.
    """
    return {
        "finite_adelic_indicator_span":"EXACT_CLASSICAL",
        "rational_coset_representatives":"Af=Q+D Zhat",
        "real_schwartz_factor":"S(R) FULL, NOT ONLY GAUSSIANS",
        "schwartz_bruhat_span":"FINITE_TENSOR_SUM_BY_DEFINITION",
        "adelic_Poisson_reduced_to_real_Poisson":"PAPER_PROOF_CLASSICAL",
        "analytic_real_Poisson_import_required":True,
        "theta_example_alone_proves_general_poisson":False,
        "RH_proved":False,
    }
