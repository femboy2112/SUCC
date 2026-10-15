"""Finite exact certificates for affine-equivariant arithmetic observation kernels.

Universal theorems have paper proofs in CARRIER_LOCKED_DUAL_SUCC_THEOREMS.md.
A stochastic source model is NOT an authenticated physical carrier or RH proof.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd


class CarrierRigidityError(ValueError):
    pass


def _int(value: int, low: int = 1, high: int = 100_000) -> int:
    if type(value) is not int or not low <= value <= high:
        raise CarrierRigidityError(f"expected an integer in [{low},{high}]")
    return value


def distribution(data: dict[int, Q], *, allow_zero: bool = False) -> dict[int, Q]:
    if not data or len(data) > 10_000:
        raise CarrierRigidityError("nonempty bounded probability law required")
    result = {}
    for k, v in data.items():
        _int(k, 0 if allow_zero else 1)
        if type(v) not in (int, Q):
            raise CarrierRigidityError("exact rational probabilities only")
        value = Q(v)
        if value < 0:
            raise CarrierRigidityError("negative probability")
        if value:
            result[k] = value
    if sum(result.values(), Q()) != 1:
        raise CarrierRigidityError("probabilities must sum to one")
    return result


def translated(mu: dict[int, Q], d: int) -> dict[int, Q]:
    _int(d, 0)
    if any(k + d > 100_000 for k in mu):
        raise CarrierRigidityError("translated address exceeds budget")
    return {k + d: v for k, v in mu.items()}


def scaled(mu: dict[int, Q], p: int) -> dict[int, Q]:
    _int(p, 2)
    if any(k * p > 100_000 for k in mu):
        raise CarrierRigidityError("scaled address exceeds budget")
    return {k * p: v for k, v in mu.items()}


def tv(mu: dict[int, Q], nu: dict[int, Q]) -> Q:
    return sum((abs(mu.get(k, Q()) - nu.get(k, Q()))
                for k in mu.keys() | nu.keys()), Q()) / 2


def shifted_noise_kernel(noise: dict[int, Q], p: int) -> dict[int, dict[int, Q]]:
    _int(p, 2, 64)
    z = distribution(noise, allow_zero=True)
    return {n: translated(z, n) for n in range(1, p + 1)}


def _depth(p: int, bound: int) -> int:
    _int(p, 2)
    _int(bound, 1)
    n, power = 0, 1
    while power <= bound:
        power *= p
        n += 1
    return n


def affine_stability_certificate(
        kernels: dict[int, dict[int, Q]], p: int, B: int, target_n: int = 1
) -> dict:
    """Exact finite check of the sharp tail-aware affine stability theorem."""
    _int(p, 2, 32)
    _int(B, 1, 100_000)
    _int(target_n, 1, p)
    if set(kernels) != set(range(1, p + 1)):
        raise CarrierRigidityError("complete laws for n=1,...,p required")
    laws = {n: distribution(kernels[n]) for n in range(1, p + 1)}
    eS = max(tv(laws[n + 1], translated(laws[n], 1)) for n in range(1, p))
    eV = tv(laws[p], scaled(laws[1], p))
    delta = (p - 1) * eS + eV
    r = _depth(p, B)
    positive_in_window = sum((v for m, v in laws[1].items()
                              if 2 <= m <= B + 1), Q())
    beyond = sum((v for m, v in laws[1].items() if m > B + 1), Q())
    displaced = 1 - laws[1].get(1, Q())
    observed_target_tv = 1 - laws[target_n].get(target_n, Q())
    bound_window = r * delta
    bound_target = (target_n - 1) * eS + bound_window + beyond
    if positive_in_window > bound_window or observed_target_tv > bound_target:
        raise ArithmeticError("affine stability inequality violated")
    return {
        "p": p, "B": B, "r": r,
        "successor_TV_max": str(eS), "dilation_TV": str(eV),
        "affine_defect": str(delta),
        "nonzero_noise_within_B": str(positive_in_window),
        "affine_window_bound": str(bound_window), "noise_tail": str(beyond),
        "noise_nonzero": str(displaced), "target_TV": str(observed_target_tv),
        "target_TV_bound": str(bound_target),
        "exact_affine_covariance": eS == 0 and eV == 0,
        "identity_for_this_kernel": all(laws[n] == {n: Q(1)} for n in laws),
        "certified": True, "zero_locations_read": False, "RH_proved": False,
    }


def sharp_chain_noise(p: int, r: int, alpha: Q) -> tuple[dict[int, Q], int]:
    _int(p, 2, 32)
    _int(r, 1, 10)
    if type(alpha) not in (int, Q) or not 0 <= alpha <= 1:
        raise CarrierRigidityError("alpha must be exact and in [0,1]")
    alpha = Q(alpha)
    if p ** r + p > 100_000:
        raise CarrierRigidityError("chain exceeds finite address budget")
    noise = {0: 1 - alpha}
    for j in range(r):
        noise[p ** j] = alpha / r
    return distribution(noise, allow_zero=True), p ** (r - 1)


def cyclic_uniform_control(modulus: int, p: int) -> dict:
    _int(modulus, 2, 100)
    _int(p, 2, 100)
    if gcd(modulus, p) != 1:
        raise CarrierRigidityError("dilation must permute finite clock")
    u = {k: Q(1, modulus) for k in range(modulus)}
    succ = {(k + 1) % modulus: v for k, v in u.items()}
    dil = {(p * k) % modulus: v for k, v in u.items()}
    if succ != u or dil != u:
        raise ArithmeticError("finite Haar action failed")
    return {"modulus": modulus, "p": p, "source_action_covariant": True,
            "not_identity": modulus > 1, "finite_clock_is_not_full_integer_carrier": True,
            "zero_locations_read": False, "RH_proved": False}


def gaussian_mix_control() -> dict:
    """Change of *test state*; arithmetic remains intact, T is not a carrier map.

    T h(x) = (22 h(x) + 20 h(4x) + 5 h(x/4))/47.
    """
    weights = {Q(1): Q(22, 47), Q(4): Q(20, 47), Q(1, 4): Q(5, 47)}
    m1 = sum((w * a for a, w in weights.items()), Q())
    m2 = sum((w * a * a for a, w in weights.items()), Q())
    variance = m2 - m1 * m1
    if not (sum(weights.values(), Q()) == 1 and m1 == Q(413, 188)
            and variance == Q(43425, 17672)):
        raise ArithmeticError("incorrect Archimedean witness")
    c2 = (Q(22) + Q(20, 16) + Q(5) * 16) / 47
    return {"first_scale_moment": str(m1), "second_scale_moment": str(m2),
            "observable_variance": str(variance),
            "successor_commutator_coordinate": str(1 - m1),
            "Mellin_distortion_s2": str(c2),
            "T_commutes_with_dilations": True,
            "T_is_not_affine_source_equivalence": True,
            "underlying_arithmetic_changed": False,
            "altered_test_is_valid_state": True,
            "zero_locations_read": False, "RH_proved": False}
