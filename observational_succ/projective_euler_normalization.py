"""Oriented projective p+1 sector as an exact normalized Euler vacuum.

This is an elementary, source-typed FINITE reconstruction: local projective
line P^1(F_p), a signed 2-sector compression, and compatible finite product
probabilities. Kolmogorov extension and Borel-Cantelli are classical paper
arguments. Not the real Archimedean place, global Tate/Connes trace or RH.
No floating point, no nontrivial zeta zeros.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt, prod


class ProjectiveEulerError(ValueError):
    """A fake prime, malformed orientation or unsupported carrier stage."""


def _prime(p):
    if type(p) is not int or p < 2 or p > 1_000_000 or any(
        p % q == 0 for q in range(2, isqrt(p)+1)
    ):
        raise ProjectiveEulerError("genuine integer prime <= 1,000,000 required")
    return p


def _stage(primes):
    if type(primes) is not tuple or len(primes) > 9 or primes != tuple(sorted(set(primes))):
        raise ProjectiveEulerError("ordered distinct prime tuple with <=9 places required")
    return tuple(_prime(p) for p in primes)


def projective_line(p):
    """Standard affine chart of P^1(F_p), plus the ONE point at infinity."""
    _prime(p)
    return tuple((1,a) for a in range(p)) + ((0,1),)


@dataclass(frozen=True)
class OrientedPrime:
    """Finite two-sector orbit vector, minus sign NOT forced by orientation.

    Signed normalized local vacuum has affine amplitude sqrt(p/(p+1)) and
    infinity amplitude sign/sqrt(p+1), with sign in {-1,+1}.
    The signed *unscaled* Euler vacuum has coefficient 1 and sign/sqrt(p).
    """
    p: int
    infinity_sign: int = -1
    source_id: str = "Q-original-FUCC-projective-model"
    epoch: int = 0

    def __post_init__(self):
        _prime(self.p)
        if type(self.infinity_sign) is not int or self.infinity_sign not in (-1,1):
            raise ProjectiveEulerError("an explicitly declared relative orientation phase +/-1 required")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise ProjectiveEulerError("declared source identity required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise ProjectiveEulerError("nonnegative integer epoch required")

    @property
    def p1_count(self):
        return len(projective_line(self.p))

    @property
    def raw_euler_norm_squared(self):
        return 1+Q(1,self.p)

    @property
    def local_mass(self):
        """(p affine directions as one, one distinguished infinity direction)."""
        return (Q(self.p,self.p+1),Q(1,self.p+1))

    def receipt(self):
        affine, boundary=self.local_mass
        assert affine+boundary==1 and self.p1_count==self.p+1
        assert (boundary/affine)==Q(1,self.p)
        return {
            "p":self.p,"affine_directions":self.p,"projective_infinity_directions":1,
            "p1_count":self.p1_count,"raw_euler_norm_squared":self.raw_euler_norm_squared,
            "affine_normalized_amplitude_squared":affine,
            "boundary_normalized_amplitude_squared":boundary,
            "relative_boundary_over_affine_amplitude_squared":boundary/affine,
            "boundary_sign":self.infinity_sign,"coherence_sign_not_fixed_by_counting":True,
            "same_as_archimedean_place":False,"Connes_trace_proved":False,
            "source_id":self.source_id,"epoch":self.epoch,
        }


@dataclass(frozen=True)
class ProjectiveCylinder:
    """Normalized finite prime occupation law with coherent sign labels.

    A probability marginal is NOT sufficient to recover the phase in
    the pure tensor state. Keep source sign + source ID as independent data.
    """
    local: tuple[OrientedPrime,...]

    def __post_init__(self):
        if type(self.local) is not tuple:
            raise ProjectiveEulerError("tuple of local source states required")
        ps=_stage(tuple(c.p for c in self.local))
        if any(type(c) is not OrientedPrime for c in self.local):
            raise ProjectiveEulerError("authentic OrientedPrime objects required")
        if self.local and len({(c.source_id,c.epoch) for c in self.local})!=1:
            raise ProjectiveEulerError("unrelated source IDs or epochs cannot be glued")
        if ps!=tuple(c.p for c in self.local):
            raise ProjectiveEulerError("unsorted prime source places")

    @property
    def primes(self):
        return tuple(c.p for c in self.local)

    @property
    def raw_norm_squared(self):
        return prod((c.raw_euler_norm_squared for c in self.local), start=Q(1))

    def distribution(self):
        """Keys are selected prime subsets: rational mass and relative sign."""
        result={}
        for k in range(len(self.local)+1):
            for chosen in combinations(self.local,k):
                included={c.p for c in chosen}
                prob, phase=Q(1),1
                for c in self.local:
                    if c.p in included:
                        prob*=Q(1,c.p+1)
                        phase*=c.infinity_sign
                    else:
                        prob*=Q(c.p,c.p+1)
                result[tuple(sorted(included))]=(prob,phase)
        if sum((v for v,_ in result.values()),Q(0))!=1:
            raise AssertionError("projective finite-cylinder sum !=1")
        return result

    def squarefree_coefficients(self):
        """Exact signed vacuum amplitudes: sign / sqrt(d*raw_norm_squared).

        Return squared amplitude and sign, never pretend its square root rational.
        """
        return tuple(sorted((
            prod(subset,start=1), phase, prob
        ) for subset,(prob,phase) in self.distribution().items()))

    def marginal(self, retained_primes):
        """Push the finite measure to an arbitrary retained subset."""
        if type(retained_primes) is not tuple or retained_primes != tuple(sorted(set(retained_primes))):
            raise ProjectiveEulerError("sorted distinct retained prime tuple required")
        if not set(retained_primes).issubset(self.primes):
            raise ProjectiveEulerError("cannot marginalize into never-observed prime places")
        keep=set(retained_primes)
        result={}
        for subset,(prob,_phase) in self.distribution().items():
            key=tuple(p for p in subset if p in keep)
            result[key]=result.get(key,Q(0))+prob
        return result

    def check_consistent_restriction(self, retained_primes):
        marginal=self.marginal(retained_primes)
        old={x.p:x for x in self.local}
        reduced=ProjectiveCylinder(tuple(old[p] for p in retained_primes))
        expected={s:mass for s,(mass,_phase) in reduced.distribution().items()}
        return {
            "all_cylinder_masses_match_exactly":marginal==expected,
            "source_prime_set":self.primes,"retained":retained_primes,
            "marginal":marginal,
            "this_proves_analytic_continuation":False,
        }


def projective_orientation_mutation(p):
    """Same probabilities, opposite local phase: orientation count alone cannot
    select true Möbius signs or the original Weil distribution.
    """
    positive=OrientedPrime(p,+1)
    negative=OrientedPrime(p,-1)
    q_pos=ProjectiveCylinder((positive,)).marginal((p,))
    q_neg=ProjectiveCylinder((negative,)).marginal((p,))
    if q_pos != q_neg:
        raise AssertionError("orientation phase unexpectedly changed probability")
    return {
        "prime":p,"same_observational_probabilities":True,
        "opposite_coherent_boundary_signs":True,
        "minus_sign_not_determined_by_p_plus_one":True,
        "global_Euler_or_Weil_sign_proved":False,
    }


def local_euler_identity(p, integer_power=1):
    """At s=integer_power, verify (1+p^-s)(1-p^-s)=1-p^(-2s)."""
    _prime(p)
    if type(integer_power) is not int or not 1<=integer_power<=10:
        raise ProjectiveEulerError("positive integer exponent <=10")
    x=Q(1,p**integer_power)
    return {"p":p,"s":integer_power,"lhs":(1+x)*(1-x),
            "rhs":1-x*x,"same":(1+x)*(1-x)==1-x*x,
            "global_analytic_residue_not_proved_by_finite_test":True}
