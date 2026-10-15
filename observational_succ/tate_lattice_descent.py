"""Tate's finite-S additive lattice and exact rational observer charts.

The infinite topological statements are CLASSICAL inputs proved in the
research dossier. Code checks exact statements on a dense rational slice;
its finite tests neither construct all Q_p points nor certify RH/Weil signs.

Source provenance is DECLARED, not physical authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import prod
from typing import Mapping

from .diagonal_adele_zeta import (
    factor_positive, fractional_padic_part, prime, rational, valuation, valuations,
)


class TateLatticeError(ValueError):
    """Invalid prime atlas, arithmetic source, or unsupported descent."""


def prime_atlas(primes: tuple[int, ...]) -> tuple[int, ...]:
    """An ordered finite collection of genuine prime places (no fake p=6)."""
    if type(primes) is not tuple or any(not prime(p) for p in primes):
        raise TateLatticeError("Finite atlas must consist of actual rational primes")
    if tuple(sorted(set(primes))) != primes:
        raise TateLatticeError("Prime atlas must be sorted and without duplicates")
    return primes


def s_integer(q: int | F, primes: tuple[int, ...]) -> bool:
    """Membership in Gamma_S = Z[S^-1], exactly, even for zero."""
    primes = prime_atlas(primes)
    q = rational(q)
    return all(p in primes for p in factor_positive(q.denominator))


def s_unit(q: int | F, primes: tuple[int, ...]) -> bool:
    """Invertible element of Z[S^-1], the permitted diagonal automorphism."""
    primes = prime_atlas(primes)
    q = rational(q)
    return q != 0 and s_integer(q, primes) and s_integer(1 / q, primes)


def s_modulus_receipt(q: int | F, primes: tuple[int, ...]) -> dict:
    """Local Jacobian vs missing-prime defect; finite equality is exact.

    If q is an S-unit, q Gamma_S = Gamma_S and modulus 1 is a CONSEQUENCE
    of classical Haar/covolume rigidity (the software checks the arithmetic).
    If q lies in Gamma_S but is not an S-unit, it induces a covering on X_S
    with finite index [Gamma_S:q Gamma_S] = modulus (an integer >=2).
    Otherwise q does not even preserve the lattice by inclusion.
    """
    primes = prime_atlas(primes)
    q = rational(q)
    if q == 0:
        raise TateLatticeError("Zero is not a group automorphism")
    vals = valuations(q)
    norm = abs(q) * prod((F(p) ** (-vals.get(p, 0)) for p in primes), start=F(1))
    missing = prod((F(p) ** v for p, v in vals.items() if p not in primes), start=F(1))
    if norm != missing:
        raise AssertionError("Local modulus and missing-prime source disagree")
    is_endomorphism = s_integer(q, primes)
    is_automorphism = s_unit(q, primes)
    if is_automorphism and norm != 1:
        raise AssertionError("A lattice automorphism must have modulus one")
    if is_endomorphism and (norm.denominator != 1 or norm < 1):
        raise AssertionError("Lattice inclusion must have integral index")
    return {
        "q": q, "S": primes, "local_haar_modulus": norm,
        "outside_prime_defect": missing,
        "lattice_inclusion": is_endomorphism,
        "lattice_automorphism": is_automorphism,
        "quotient_cover_degree": int(norm) if is_endomorphism else None,
        "uses_full_product_formula": True,
        "RH_proved": False,
    }


@dataclass(frozen=True)
class RationalSChart:
    """Rational dense chart in G_S = R x (product of Q_p, p in S).

    The R coordinate is restricted to rational values for exact computation.
    It is NOT the complete LCA space G_S. 'loc' is in prime-atlas order.
    The diagonal lattice Gamma_S acts by adding the same S-integer to ALL
    coordinates; quotient is X_S = G_S / Gamma_S.
    """
    primes: tuple[int, ...]
    arch: F
    loc: tuple[F, ...]
    source_id: str = "Q-standard-additive"
    epoch: int = 0

    def __post_init__(self) -> None:
        prime_atlas(self.primes)
        if type(self.loc) is not tuple or len(self.loc) != len(self.primes):
            raise TateLatticeError("Exactly one p-adic coordinate per declared prime")
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise TateLatticeError("Nonempty source identifier required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise TateLatticeError("Nonnegative source epoch required")
        object.__setattr__(self, "arch", rational(self.arch))
        object.__setattr__(self, "loc", tuple(rational(v) for v in self.loc))

    @classmethod
    def from_places(cls, primes: tuple[int, ...], arch: int | F,
                    local: Mapping[int, int | F], *,
                    source_id: str = "Q-standard-additive", epoch: int = 0) -> "RationalSChart":
        prime_atlas(primes)
        if set(local) != set(primes):
            raise TateLatticeError("Missing or invented finite-place coordinate")
        return cls(primes, rational(arch), tuple(rational(local[p]) for p in primes),
                   source_id, epoch)

    def diagonal_shift(self, gamma: int | F) -> "RationalSChart":
        gamma = rational(gamma)
        if not s_integer(gamma, self.primes):
            raise TateLatticeError("Only Gamma_S may act as a diagonal gauge")
        return RationalSChart(self.primes, self.arch + gamma,
                             tuple(x + gamma for x in self.loc),
                             self.source_id, self.epoch)

    def gauge(self) -> F:
        """Canonical Gamma_S translation sending every local x_p into Z_p.

        Add an integer to put the real coordinate into [0,1); every finite
        coordinate then has nonnegative p-valuation (or is zero).
        """
        delta = sum((fractional_padic_part(x, p)
                     for p, x in zip(self.primes, self.loc)), F(0))
        delta += (self.arch - delta).__floor__()
        if not s_integer(delta, self.primes):
            raise AssertionError("Principal-part approximation escaped Gamma_S")
        return delta

    def canonical(self) -> "RationalSChart":
        gamma = self.gauge()
        chart = self.diagonal_shift(-gamma)
        if not 0 <= chart.arch < 1:
            raise AssertionError("Real unit-cell normalization failed")
        for p, x in zip(chart.primes, chart.loc):
            if x and valuation(x, p) < 0:
                raise AssertionError("p-adic integral chart normalization failed")
        return chart

    def equivalent(self, other: "RationalSChart") -> bool:
        self._compatible(other)
        gap = self.arch - other.arch
        return s_integer(gap, self.primes) and all(
            x - y == gap for x, y in zip(self.loc, other.loc)
        )

    def _compatible(self, other: "RationalSChart") -> None:
        if (self.primes, self.source_id, self.epoch) != (
                other.primes, other.source_id, other.epoch):
            raise TateLatticeError("Different atlas/source/epoch is not a lawful comparison")

    def scale(self, q: int | F, *, require_automorphism: bool = False) -> "RationalSChart":
        """Affine FUCC multiplier on the local quotient when q belongs to Gamma_S.

        For an S-integer that is not an S-unit the descended map is a covering,
        not an automorphism. This is a model of loss of reversible access.
        """
        q = rational(q)
        if q == 0 or not s_integer(q, self.primes):
            raise TateLatticeError('Nonzero lattice-preserving multiplier required')
        if require_automorphism and not s_unit(q, self.primes):
            raise TateLatticeError('Inverse does not descend to this atlas')
        return RationalSChart(self.primes, q * self.arch,
                             tuple(q * x for x in self.loc),
                             self.source_id, self.epoch)

    def character_phase(self, q: int | F) -> F:
        """Exact phase in Q/Z of chi_q(x)=exp(2pi*i(theta_S(q x))).

        The pairing uses real + and p-adic -; the simultaneous opposite
        sign is an equivalent convention. The result is gauge invariant for
        q in Gamma_S, because chi_q(Gamma_S) = 1.
        """
        q = rational(q)
        if not s_integer(q, self.primes):
            raise TateLatticeError("The dual character must lie in Gamma_S")
        phase = q * self.arch - sum((fractional_padic_part(q * x, p)
                                   for p, x in zip(self.primes, self.loc)), F(0))
        return phase % 1

    def project(self, subprimes: tuple[int, ...]) -> "RationalSChart":
        """Canonical quotient bonding map X_T -> X_S for S subset T.

        Kill the omitted local principal parts using Gamma_T first; merely
        dropping the omitted coordinates is WRONG and fails gauge descent.
        """
        prime_atlas(subprimes)
        if not set(subprimes).issubset(self.primes):
            raise TateLatticeError("Cannot project to previously unobserved primes")
        omitted = sum((fractional_padic_part(x, p)
                       for p, x in zip(self.primes, self.loc)
                       if p not in subprimes), F(0))
        local = {p: x - omitted for p, x in zip(self.primes, self.loc)
                 if p in subprimes}
        return RationalSChart.from_places(subprimes, self.arch - omitted, local,
                                          source_id=self.source_id,
                                          epoch=self.epoch).canonical()


def character_naturality(chart: RationalSChart,
                         subprimes: tuple[int, ...], q: int | F) -> dict:
    """Exact naturality square: chi_T(q,x) = chi_S(q, pi_T,S x)."""
    small = chart.project(subprimes)
    q = rational(q)
    if not s_integer(q, subprimes):
        raise TateLatticeError("Restriction requires q in the smaller dual lattice")
    lhs = chart.character_phase(q)
    rhs = small.character_phase(q)
    return {"larger": chart.primes, "smaller": subprimes, "q": q,
            "larger_phase": lhs, "smaller_phase": rhs,
            "commutes": lhs == rhs}


def finite_depth_alias(p: int, depth: int, *, source_id: str = "Q-standard-additive") -> dict:
    """Exact nonzero local class invisible to all q=j/p^k with k<=depth.

    Chart x=(0,p^depth) at the p-coordinate. For every integer j and k<=depth,
    chi_(j/p^k)(x)=1, whereas the next character has phase -1/p.
    No finite-depth phase agreement implies zero in X_{p}.
    """
    if not prime(p) or type(depth) is not int or depth < 0 or depth > 96:
        raise TateLatticeError("Genuine prime and bounded nonnegative depth required")
    x = RationalSChart((p,), F(0), (F(p**depth),), source_id)
    for k in range(depth + 1):
        for j in (-7, -1, 0, 1, 7):
            if x.character_phase(F(j, p**k)) != 0:
                raise AssertionError("Finite-depth aliases should be invisible")
    witness = x.character_phase(F(1, p**(depth+1)))
    if witness != F(1, 2) and p == 2:
        raise AssertionError("Expected exact dyadic half-period witness")
    if witness == 0:
        raise AssertionError("Deeper character failed to distinguish nonzero class")
    return {"p": p, "depth": depth, "hidden": x.loc[0],
            "all_shallow_character_phases_zero": True,
            "first_deeper_phase": witness,
            "nonzero_quotient_class": not x.equivalent(
                RationalSChart((p,), F(0), (F(0),), source_id)),
            "finite_depth_complete": False}


def successor_history_kernel(primes: tuple[int, ...], d: int | F) -> dict:
    """No-go: a nonzero lattice SUCC event becomes identity on X_S.

    Exact nonfaithfulness witness for bare quotient-state encodings. The
    lift and signed source-event displacement must be retained separately.
    """
    primes = prime_atlas(primes)
    d = rational(d)
    if d == 0 or not s_integer(d, primes):
        raise TateLatticeError("Nonzero lawful lattice displacement required")
    start = RationalSChart(primes, F(0), tuple(F(0) for _ in primes))
    finish = start.diagonal_shift(d)
    return {
        "S": primes, "event_displacement": d,
        "lift_changes": start != finish,
        "same_global_quotient_state": start.equivalent(finish),
        "quotient_state_functor_faithful_on_events": False,
        "required_extra_record": "source-indexed Gamma_S transition cocycle",
    }


def prime_extension_obstruction(primes: tuple[int, ...], new_prime: int) -> dict:
    """One-prime solenoidal extension and its nonsplitting witness.

    Classical theorem (NOT proved by executing finite code):
       0 -> Z_p -> X_(S union {p}) -> X_S -> 0
    is an exact sequence of compact abelian groups. It has no continuous
    section, even a non-homomorphic one. Pontryagin duality identifies its
    quotient with the nonzero p-primary torsion group C_(p^infinity), while
    the larger dual Gamma_T sits in torsion-free Q. Also X_T is connected
    but a continuous section would trivialize it as X_S x Z_p, a
    disconnected space. Here we verify only finite rational witnesses.
    """
    primes = prime_atlas(primes)
    if not prime(new_prime) or new_prime in primes:
        raise TateLatticeError('Adjoin exactly one genuinely new prime')
    enlarged = tuple(sorted((*primes, new_prime)))
    order_p = F(1, new_prime)
    if not (s_integer(order_p, enlarged)
            and not s_integer(order_p, primes)
            and s_integer(new_prime * order_p, primes)):
        raise AssertionError('Dual quotient p-torsion witness failed')
    kernel_class = RationalSChart(enlarged, F(0), tuple(
        F(1) if p == new_prime else F(0) for p in enlarged))
    origin = RationalSChart(enlarged, F(0), tuple(F(0) for _ in enlarged))
    small_origin = RationalSChart(primes, F(0), tuple(F(0) for _ in primes))
    if kernel_class.equivalent(origin):
        raise AssertionError('Proposed p-adic kernel must be nontrivial')
    if not kernel_class.project(primes).equivalent(small_origin):
        raise AssertionError('Proposed kernel point must project to identity')
    return {
        'S': primes,
        'T': enlarged,
        'added_prime': new_prime,
        'dual_torsion_witness': order_p,
        'order_in_dual_quotient': new_prime,
        'nonzero_rational_kernel_class': True,
        'projects_to_identity': True,
        'infinite_kernel_type': 'Z_p (CLASSICAL; not constructed by finite code)',
        'global_extension_split': False,
        'continuous_section_exists': False,
        'section_obstruction': 'connected X_T vs disconnected X_S x Z_p',
        'full_topological_claim_proved_by_execution': False,
        'RH_proved': False,
    }


def reversibility_descent_obstruction(primes: tuple[int, ...], new_prime: int) -> dict:
    """A T-unit p-automorphism projects to an S-map of degree p.

    For T=S+{p}, multiplication by p on X_T is reversible, while on X_S
    it is a p-fold covering. The inverse 1/p does not descend to X_S.
    This is classical arithmetic, witnessed exactly on rational charts.
    """
    primes = prime_atlas(primes)
    if not prime(new_prime) or new_prime in primes:
        raise TateLatticeError('Need a new genuine prime')
    T = tuple(sorted((*primes, new_prime)))
    p = new_prime
    if not s_unit(p, T) or s_unit(p, primes):
        raise AssertionError('Prime multiplication atlas typing failed')
    if s_modulus_receipt(p, primes)['quotient_cover_degree'] != p:
        raise AssertionError('Missing-prime covering degree failed')
    if s_modulus_receipt(p, T)['quotient_cover_degree'] != 1:
        raise AssertionError('T-unit not reversible')
    # Diagonal 1/p is not an S-integer, giving exact p-torsion in X_S.
    x_s = RationalSChart(primes, F(1, p), tuple(F(1, p) for _ in primes))
    z_s = RationalSChart(primes, F(0), tuple(F(0) for _ in primes))
    if x_s.equivalent(z_s) or not x_s.scale(p).equivalent(z_s):
        raise AssertionError('Expected nonzero p-kernel on smaller quotient')
    # A lift with zero p-coordinate carries information invisible to X_S.
    x_t = RationalSChart(T, F(1, p), tuple(
        F(0) if q == p else F(1, p) for q in T))
    if not x_t.project(primes).equivalent(x_s):
        raise AssertionError('Large-stage lifted witness did not descend')
    y_t = x_t.scale(p, require_automorphism=True)
    z_t = RationalSChart(T, F(0), tuple(F(0) for _ in T))
    if y_t.equivalent(z_t) or not y_t.project(primes).equivalent(z_s):
        raise AssertionError('Missing p-information was not transferred to fiber')
    if not y_t.scale(F(1, p), require_automorphism=True).equivalent(x_t):
        raise AssertionError('Full-stage inverse failed')
    return {
        'S': primes,
        'T': T,
        'new_prime': p,
        'cover_degree_at_S': p,
        'automorphism_degree_at_T': 1,
        'small_map_noninjective': True,
        'large_map_reversible': True,
        'inverse_exists_on_S': False,
        'lost_observer_class_survives_in_T_kernel_fiber': True,
        'valid_correlated_global_source_witness': True,
        'RH_proved': False,
    }
