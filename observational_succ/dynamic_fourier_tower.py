"""Exact, source-relative Fourier functor on a tower of finite cyclic quotients.

Given a surjection Z/M -> Z/N (N|M), push FORWARD source amplitudes by
summing over fibers. Its unnormalized Fourier transform is exactly the
restriction of fine Fourier data to the annihilator dual subgroup.

Normalized orthogonal conditional expectation has an exact rational
ENERGY receipt even when the normalized amplitudes involve square roots.
Spectral debt is audited from the full declared source, not available to
an observer seeing only the coarse pushforward.

This is CLASSICAL Pontryagin duality and conditional expectation in a
new-to-ObsSUCC finite proof interface, NOT the adele Fourier transform.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Sequence

from .diagonal_adele_zeta import DiagonalSourceError, prime
from .finite_fourier_carrier import (
    CyclotomicElement, exact_dft,
)


def _rational(x: object) -> F:
    if type(x) is int or type(x) is F:
        return F(x)
    raise DiagonalSourceError("Source amplitudes must be exact rational values")


def _moduli(fine: int, coarse: int, place_prime: int | None = None) -> int:
    if (type(fine) is not int or type(coarse) is not int or
            not 2 <= coarse < fine <= 100 or fine % coarse):
        raise DiagonalSourceError("Exact proper quotient Z/M -> Z/N with N|M required")
    if place_prime is not None:
        if not prime(place_prime):
            raise DiagonalSourceError("Declared local place must be truly prime")
        for n in (fine, coarse):
            q = n
            while q % place_prime == 0:
                q //= place_prime
            if q != 1:
                raise DiagonalSourceError("Both clock levels must be powers of declared prime")
    return fine // coarse


def sum_fibers(values: Sequence[int | F], coarse: int,
               *, place_prime: int | None = None) -> tuple[F, ...]:
    x = tuple(_rational(v) for v in values)
    _moduli(len(x), coarse, place_prime)
    return tuple(sum((x[j] for j in range(h, len(x), coarse)), F())
                 for h in range(coarse))


def lift_character(z: CyclotomicElement, fine: int) -> CyclotomicElement:
    """Apply Q(zeta_N)->Q(zeta_M), zeta_N maps to zeta_M^(M/N)."""
    if type(fine) is not int or not 2 <= z.modulus <= fine <= 100 or fine % z.modulus:
        raise DiagonalSourceError("Characters must lift through an actual quotient")
    k = fine // z.modulus
    total = CyclotomicElement.scalar(fine, 0)
    for i, a in enumerate(z.polynomial):
        if a:
            total = total + CyclotomicElement.root(fine, k * i).scale(a)
    return total


def _conjugate(z: CyclotomicElement) -> CyclotomicElement:
    total = CyclotomicElement.scalar(z.modulus, 0)
    for i, a in enumerate(z.polynomial):
        if a:
            total = total + CyclotomicElement.root(z.modulus, -i).scale(a)
    return total


def _real_rational(z: CyclotomicElement) -> F:
    if len(z.polynomial) != 1:
        raise AssertionError("A full character-orbit energy sum must be rational")
    return z.polynomial[0]


def exact_fourier_restriction(values: Sequence[int | F], coarse: int,
                              *, place_prime: int | None = None) -> dict:
    """Verify Fourier(sum_fibers x)(r)=Fourier(x)((M/N)*r) exactly.

    The TWO transforms live in different cyclotomic fields; comparison uses
    the canonical inclusion induced by the quotient's dual injection.
    """
    x = tuple(_rational(v) for v in values)
    k = _moduli(len(x), coarse, place_prime)
    coarse_sp = exact_dft(sum_fibers(x, coarse))
    fine_sp = exact_dft(x)
    for r in range(coarse):
        if lift_character(coarse_sp[r], len(x)) != fine_sp[k * r]:
            raise AssertionError("Finite Fourier/refinement naturality square fails")
    return {"source_modulus": len(x), "quotient_modulus": coarse,
            "dual_injection": tuple(k * r for r in range(coarse)),
            "all_character_squares_exact": True,
            "place_prime": place_prime,
            "full_adelic_or_archimedean_completion": False}


def exact_spectral_debt(values: Sequence[int | F], coarse: int,
                        *, place_prime: int | None = None) -> dict:
    """Compute lost ℓ² energy of orthogonally normalized fiber averaging.

    Hidden energy equals sum of squared Fourier coefficients outside the
    quotient's dual subgroup / M. A coarse observer CANNOT compute it
    from its report without access to the source or an independent bound.
    """
    x = tuple(_rational(v) for v in values)
    k = _moduli(len(x), coarse, place_prime)
    y = sum_fibers(x, coarse, place_prime=place_prime)
    fine_e = sum((v * v for v in x), F())
    retained_e = sum((v * v for v in y), F()) / k
    debt = fine_e - retained_e
    if debt < 0:
        raise AssertionError("Fiber conditional expectation must contract energy")
    spectrum = exact_dft(x)
    omitted = CyclotomicElement.scalar(len(x), 0)
    for j, v in enumerate(spectrum):
        if j % k:
            omitted = omitted + v * _conjugate(v)
    spectral_debt = _real_rational(omitted) / len(x)
    if debt != spectral_debt:
        raise AssertionError("Fourier omitted-mode debt disagrees with source-side debt")
    sq = exact_fourier_restriction(x, coarse, place_prime=place_prime)
    return {"fine_energy": fine_e, "retained_energy": retained_e,
            "unseen_spectral_debt": debt, "omitted_fourier_energy": spectral_debt,
            "coarse_report": y, "exact_quotient_fourier": sq,
            "observer_can_know_debt_from_coarse_report_alone": False}


def verify_fourier_tower(values: Sequence[int | F],
                         levels: Sequence[int], *, source_id: str,
                         source_version: int, place_prime: int | None = None) -> dict:
    """An exact source-versioned tower of composable observation quotients.

    levels are FINEST to COARSEST, each a genuine divisor of the previous.
    The source vector is simulator-only, not an E observer receipt.
    """
    if (type(source_id) is not str or not source_id or
            type(source_version) is not int or source_version < 0):
        raise DiagonalSourceError("Nonempty source provenance and source epoch required")
    x = tuple(_rational(v) for v in values)
    moduli = tuple(levels)
    if len(moduli) < 2 or type(moduli[0]) is not int or moduli[0] != len(x):
        raise DiagonalSourceError("Include original source clock and a proper quotient")
    for a, b in zip(moduli, moduli[1:]):
        _moduli(a, b, place_prime)
    base = len(x)
    from_fine = {base: x}
    # Composition of raw pushforwards (no costly squared-root normalization).
    current = x
    for a, b in zip(moduli, moduli[1:]):
        current = sum_fibers(current, b, place_prime=place_prime)
        if current != sum_fibers(x, b, place_prime=place_prime):
            raise AssertionError("SUCC Fourier observation paths fail to commute")
        from_fine[b] = current
    # Rational energy normalization is relative to ORIGINAL resolution.
    energies = tuple(F(n, base) * sum((v * v for v in from_fine[n]), F())
                     for n in moduli)
    debts = tuple(a - b for a, b in zip(energies, energies[1:]))
    if any(d < 0 for d in debts):
        raise AssertionError("Projection tower energy cannot increase")
    if sum(debts, F()) != energies[0] - energies[-1]:
        raise AssertionError("Missing or double-counted observer spectral debt")
    top = exact_spectral_debt(x, moduli[-1], place_prime=place_prime)
    if top["unseen_spectral_debt"] != sum(debts, F()):
        raise AssertionError("Composed Fourier loss does not match one-shot loss")
    return {"source_id": source_id, "source_version": source_version,
            "moduli_finest_to_coarsest": moduli, "energy_by_level": energies,
            "stage_debts": debts, "total_debt": sum(debts, F()),
            "composition_square": True, "Fourier_square": True,
            "physical_source_authenticated": False}


def observational_alias(values_a: Sequence[int | F],
                        values_b: Sequence[int | F], coarse: int) -> dict:
    a, b = tuple(_rational(v) for v in values_a), tuple(_rational(v) for v in values_b)
    if len(a) != len(b):
        raise DiagonalSourceError("Source alternatives must inhabit same fine clock")
    ca = sum_fibers(a, coarse)
    cb = sum_fibers(b, coarse)
    return {"same_coarse_report": ca == cb,
            "source_states_identical": a == b,
            "fine_difference_energy": sum(((u-v)**2 for u, v in zip(a, b)), F()),
            "claim_all_fine_modes_recovered": (a == b) if ca == cb else False}


def claim_target_debt(values: Sequence[int | F],
                      claim_weights: Sequence[int | F], coarse: int) -> dict:
    """Exact source-to-claim Cauchy-Schwarz continuity bound.

    Let P be orthogonal fiber averaging and let linear T_a(x)=<a,x>.
    Then T_a(x)-T_a(Px)=<a-Pa,x-Px> and
       |T_a(x)-T_a(Px)|^2 <= ||a-Pa||^2 * ||x-Px||^2.
    A claim factors through all coarse reports iff a=Pa.
    """
    x = tuple(_rational(v) for v in values)
    a = tuple(_rational(v) for v in claim_weights)
    if len(x) != len(a):
        raise DiagonalSourceError("Source and original-source claim must share a fine clock")
    k = _moduli(len(x), coarse)
    px = tuple(sum_fibers(x, coarse)[i % coarse] / k for i in range(len(x)))
    pa = tuple(sum_fibers(a, coarse)[i % coarse] / k for i in range(len(a)))
    lost = sum((v * (u - p) for v, u, p in zip(a, x, px)), F())
    witness_squared = lost * lost
    source_debt = sum(((u-p)**2 for u, p in zip(x, px)), F())
    claim_debt = sum(((u-p)**2 for u, p in zip(a, pa)), F())
    upper = source_debt * claim_debt
    if witness_squared > upper:
        raise AssertionError("Original-claim Fourier debt bound violated")
    return {"source_debt": source_debt, "claim_sensitivity_debt": claim_debt,
            "actual_squared_claim_loss": witness_squared,
            "upper_squared_claim_loss": upper,
            "claim_factors_through_coarse_observer": claim_debt == 0}


def disappearing_energy_unbounded_claim(n: int) -> dict:
    """Hostile family: vanishing spectral debt with diverging target error.

    x=(1/n,0,-1/n,0) has coarse Z/2 report zero and lost energy 2/n².
    a=(n²,0,-n²,0) has ||(I-P)a||²=2n^4. The same original-source
    linear target evaluates to 2n while a coarse observer sees zero.
    No uniform claim operator norm means no limit claim transport.
    """
    if type(n) is not int or n < 1:
        raise DiagonalSourceError("Positive integer refinement parameter required")
    x = (F(1,n), F(0), F(-1,n), F(0))
    a = (F(n*n), F(0), F(-n*n), F(0))
    result = claim_target_debt(x, a, 2)
    if result['source_debt'] != F(2,n*n) or result['actual_squared_claim_loss'] != 4*n*n:
        raise AssertionError("Unbounded-claim negative control broken")
    return {"n": n, "unseen_energy": result['source_debt'],
            "squared_original_claim_error": result['actual_squared_claim_loss'],
            "source_difference_tends_to_zero": True,
            "original_claim_error_diverges": True,
            "uniform_operator_norm_available": False}


def source_update_descent(matrix: Sequence[Sequence[int | F]], coarse: int) -> dict:
    """Exact causal source-update / coarse-observer commuting-square theorem.

    For a declared linear fine-carrier update U:Q^M->Q^M and a surjective
    observer A:Q^M->Q^N summing residue fibers, a lawful coarse update V
    satisfying A U = V A exists iff U(ker A) lies in ker A. The induced
    V is unique. Failing this emits an explicit invisible input whose
    post-update coarse value is NONZERO: a proof of lost future closure.

    No claim of a quantum physical instrument; U is a declared linear map.
    """
    rows = tuple(tuple(_rational(v) for v in row) for row in matrix)
    m = len(rows)
    _moduli(m, coarse)
    if any(len(row) != m for row in rows):
        raise DiagonalSourceError("State-changing carrier map must be square")

    def act(f: tuple[F, ...]) -> tuple[F, ...]:
        return tuple(sum((rows[i][j] * f[j] for j in range(m)), F()) for i in range(m))

    def basis(j: int) -> tuple[F, ...]:
        return tuple(F(i == j) for i in range(m))

    columns = tuple(sum_fibers(act(basis(h)), coarse) for h in range(coarse))
    for j in range(coarse, m):
        observed = sum_fibers(act(basis(j)), coarse)
        expected = columns[j % coarse]
        if observed != expected:
            hidden = tuple(F(int(i == j) - int(i == j % coarse)) for i in range(m))
            if sum_fibers(hidden, coarse) != (F(0),) * coarse:
                raise AssertionError("Obstruction witness must be invisible before U")
            revealed = sum_fibers(act(hidden), coarse)
            if revealed == (F(0),) * coarse:
                raise AssertionError("Noncommuting observer/update square has false witness")
            return {"coarse_dynamics_exists": False,
                    "obstruction_invisible_source": hidden,
                    "obstruction_revealed_report": revealed,
                    "source_mapping_requires_fine_information": True,
                    "RH_or_physical_entanglement_claimed": False}
    v = tuple(tuple(columns[j][i] for j in range(coarse)) for i in range(coarse))
    for j in range(m):
        aj = sum_fibers(basis(j),coarse)
        lhs = sum_fibers(act(basis(j)), coarse)
        rhs = tuple(sum((v[i][h]*aj[h] for h in range(coarse)), F())
                    for i in range(coarse))
        if lhs != rhs:
            raise AssertionError("Supposedly descended dynamics do not commute")
    return {"coarse_dynamics_exists": True,
            "induced_coarse_matrix": v,
            "verified_on_all_source_basis_vectors": True,
            "source_mapping_requires_fine_information": False,
            "RH_or_physical_entanglement_claimed": False}
