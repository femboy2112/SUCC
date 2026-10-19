"""Full prime valuation tower and exact projective conditioning vs coarse-graining.

Local Tate Haar shells have weight p^(-s*k) for k>=0. After local
normalization, the β=1 geometric law on all k has P(k)=(1-1/p)p^-k.
Conditioning on k<=1 reproduces EXACTLY the previous p+1 projective
two-sector weights, but coarse-graining the event k>=1 DOES NOT.

Signs ε^k are Hilbert phase choices. Their linear Mellin/Dirichlet
generating factors differ for ε=+1 and -1. A phase-insensitive probability
model is not a signed Tate/Weil trace.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import isqrt


class PrimeTowerError(ValueError):
    """Nonprime, unnormalized source or unavailable conductor data."""


def _prime(p):
    if type(p) is not int or not 2<=p<=100000 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise PrimeTowerError("genuine prime place required")
    return p


def _depth(k):
    if type(k) is not int or not 0<=k<=100:
        raise PrimeTowerError("nonnegative finite prime power depth <=100")
    return k


@dataclass(frozen=True)
class FullPrimeTower:
    p: int
    beta: int = 1
    epsilon: int = -1
    source_id: str = "Q-standard-Tate"
    epoch: int = 0

    def __post_init__(self):
        _prime(self.p)
        if type(self.beta) is not int or not 1<=self.beta<=16:
            raise PrimeTowerError("real critical beta=1 or convergent integer beta>=2")
        if type(self.epsilon) is not int or self.epsilon not in (-1,1):
            raise PrimeTowerError("explicit phase ±1 required")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise PrimeTowerError("source identity required")
        if type(self.epoch) is not int or self.epoch<0:
            raise PrimeTowerError("nonnegative source epoch required")

    @property
    def r(self):
        return Q(1,self.p**self.beta)

    def probability(self,k):
        _depth(k)
        return (1-self.r)*self.r**k

    def phase(self,k):
        _depth(k)
        return self.epsilon**k

    def prefix(self,depth):
        _depth(depth)
        cells=tuple((k,self.probability(k),self.phase(k)) for k in range(depth+1))
        tail=self.r**(depth+1)
        if sum((q for _,q,_ in cells),Q(0))+tail!=1:
            raise AssertionError("local normalized valuation cylinder incomplete")
        return {
            "prime":self.p,"beta":self.beta,"epsilon":self.epsilon,
            "valuations":cells,"tail_probability":tail,
            "signed_Mellin_not_probabilities":True,"RH_proved":False,
        }

    def conditional_squarefree(self):
        """Actual P(k|k<=1) reweights the 0/1 source via projection."""
        permitted=self.probability(0)+self.probability(1)
        zero=self.probability(0)/permitted
        one=self.probability(1)/permitted
        if (zero,one)!=(1/(1+self.r),self.r/(1+self.r)):
            raise AssertionError("conditional normalized two-state law failed")
        return {
            "prime":self.p,"beta":self.beta,
            "conditional_k0":zero,"conditional_k1":one,
            "projective_p_plus_one_exact_when_beta_is_one":self.beta==1,
            "coarse_event_k_positive":self.r,
            "conditional_first_power_is_NOT_coarse_positive_valuation":
                one!=self.r,
            "discarded_higher_valuation_mass":self.r**2,
            "relative_phase":self.epsilon,
            "full_prime_tower_is_two_state":False,"RH_proved":False,
        }

    def linear_mellin_factor(self):
        """For integer beta>1, ∑ ε^k p^-beta*k = 1/(1-ε p^-beta).

        At beta=1 this is still a convergent *individual local* series,
        but all-prime Euler product is not absolutely convergent.
        """
        return 1/(1-self.epsilon*self.r)

    def phase_sensitive_shift_expectation(self):
        """<phi_eps, V_p phi_eps>=eps*sqrt(r); return sign and squared norm."""
        return {"sign":self.epsilon,"absolute_square":self.r,
                "independent_of_phase_if_only_probability_observed":True,
                "coherent_p_shift_detects_phase":True,
                "all_place_tate_trace_identified":False}

    def chi_minus_3_factor(self):
        """Proper conductor 3 Euler omission; the local Hecke character
        is never a zero-valued character of Q_3^x itself.
        """
        if self.p==3:
            return {"prime":3,"Euler_factor":Q(1),"ramified":True,
                    "character_value_at_divisible_integer":0,
                    "local_Hecke_character_itself_vanishes":False}
        eps=1 if self.p%3==1 else -1
        return {"prime":self.p,"Euler_factor":1/(1-eps*self.r),
                "ramified":False,"phase":eps,
                "same_as_uniform_minus":eps==-1}


def projective_from_tate_crosscheck(p):
    """Exact projective P1 p+1 2-state cylinder = geometric k<=1 conditioning.

    It is NOT the probability measure of all positive p-valuations.
    """
    from .projective_euler_normalization import OrientedPrime
    source=FullPrimeTower(p,beta=1,epsilon=-1)
    projected=source.conditional_squarefree()
    projective=OrientedPrime(p)
    if (projected["conditional_k0"],projected["conditional_k1"])!=projective.local_mass:
        raise AssertionError("PROJECTIVE_LOCAL_TATE_CONDITIONING_FAILED")
    return {
        "p":p,"true_full_source":"geometric_local_Tate_Haar_k>=0",
        "projective_source":"CONDITION_ON_k<=1",
        "conditional_mass":projective.local_mass,
        "coarse_nonzero_valuation_mass":source.r,
        "missing_p_squared_and_higher_mass":source.r**2,
        "phase_is_declared_not_forced_by_conditioning":True,
        "original_Weil_kernel_identified":False,
    }


def finite_tower_tate_crosscheck(primes,beta=2,depth=4):
    """Compare complete Euler product with existing canonical Tate source.

    This finite test does NOT establish full adelic Poisson or RH.
    """
    if type(primes) is not tuple or not primes or primes!=tuple(sorted(set(primes))):
        raise PrimeTowerError("ordered nonempty genuine prime stage required")
    if len(primes)>6 or type(beta) is not int or not 2<=beta<=10:
        raise PrimeTowerError("finite original source budget")
    _depth(depth)
    from .tate_idelic_zeta import finite_euler_stage
    for p in primes:_prime(p)
    local=tuple(FullPrimeTower(p,beta,epsilon=1) for p in primes)
    source=finite_euler_stage(primes,beta,depth)
    own=Q(1)
    for tower in local:
        own*=tower.linear_mellin_factor()
    if source["complete_finite_place_product"]!=own:
        raise AssertionError("FULL_PRIME_TOWER_TATE_EULER_DISAGREEMENT")
    return {
        "primes":primes,"beta":beta,"source_real_Tate_Euler":source["complete_finite_place_product"],
        "independent_full_tower_product":own,
        "agreement_all_local_prime_powers":True,
        "squarefree_projective_product_equal_to_full_zeta":False,
        "completed_arch_gamma_and_trace_verified":False,
    }


def finite_full_valuation_cylinder(primes,depth,beta=2):
    """Independent finite-stage exact probability for full k=0..depth and tails.

    Each local prefix has subprobability mass (1-r^(depth+1)).
    """
    if type(primes) is not tuple or primes != tuple(sorted(set(primes))) or len(primes)>5:
        raise PrimeTowerError("ordered original prime set required")
    _depth(depth)
    if type(beta) is not int or not 1<=beta<=10:
        raise PrimeTowerError("beta integer in 1..10")
    towers=tuple(FullPrimeTower(p,beta) for p in primes)
    vectors=tuple(product(*(range(depth+1) for p in primes)))
    rows=tuple((ks,
        Q(1) if not primes else Q(1)*__import__('math').prod((tower.probability(k) for tower,k in zip(towers,ks))))
               for ks in vectors)
    total=sum((q for _,q in rows),Q(0))
    expected=Q(1)
    for tower in towers:
        expected*=1-tower.r**(depth+1)
    if total!=expected:
        raise AssertionError("FINITE_FULL_TOWER_MASS_DISAGREEMENT")
    return {"primes":primes,"beta":beta,"depth":depth,
            "probabilities":rows,"finite_retained_mass":total,
            "truncated_mass_formula":expected,
            "omitted_tail_mass":1-total,"all_prime_limit_executed":False}
