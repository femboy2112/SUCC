"""Exact selection likelihoods, observable innovations and inverse resolution.

Classical finite conditional-expectation identities, specialized to the native
BBP inverse fiber.  The original history, forcing and odd selector are reused.
The paper supplies all-horizon/continuous-domain proofs; these functions certify
finite instances.  A virtual reference probability is declared, not inferred
from the deterministic arithmetic orbit.  No selected Weyl saving is asserted.

Project predecessors: heuristic_evidence_martingales.py (Doob/Ville likelihoods),
bidirectional_source_histories.py (labelled path laws), selected_branch_operator.py
(odd inverse and discontinuity).  This module adds their signed innovation
pairing and an exact radix-resolution certificate, not a new probability engine.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from collections.abc import Mapping

from .bidirectional_source_histories import exact
from .lambda_source_duality import verify_original_history
from .selected_branch_operator import exact_odd_inverse
from .succ_internal_matrix_walk import authentic_r, circle


def _integer(value, name, lower=None, upper=None):
    if type(value) is not int or (lower is not None and value < lower) or (
        upper is not None and value > upper
    ):
        raise ValueError(f"invalid exact integer {name}")
    return value


def _law(law, name):
    if not isinstance(law, Mapping) or not law:
        raise ValueError(f"{name} must be a nonempty exact path law")
    if any(not isinstance(path, tuple) for path in law):
        raise ValueError("paths must be tuples of retained source labels")
    if len({len(path) for path in law}) != 1:
        raise ValueError("all paths must have one common finite depth")
    result = {path: exact(weight) for path, weight in law.items()}
    if any(weight < 0 for weight in result.values()) or sum(result.values()) != 1:
        raise ValueError(f"{name} must be a probability law")
    return {path: weight for path, weight in result.items() if weight}


@dataclass(frozen=True)
class Innovation:
    level: int
    likelihood_mean_increment: Q
    observable_mean_increment: Q
    likelihood_increment_square: Q
    observable_increment_square: Q
    signed_pairing: Q


@dataclass(frozen=True)
class LikelihoodCertificate:
    depth: int
    reference_expectation: Q
    selected_expectation: Q
    chi_square: Q
    observable_variance: Q
    innovations: tuple[Innovation, ...]

    @property
    def signed_difference(self):
        return sum((row.signed_pairing for row in self.innovations), Q())


def path_likelihood_certificate(reference, selected, observable):
    """Certify E_Q F-E_P F = sum E_P[(dR_t)(dM_t)] exactly.

    P and Q are normalized laws on equal-length retained-label tuples, Q<<P.
    F is rational; the complex theorem follows componentwise (no conjugation
    in the bilinear pairing). Prefix level zero is the trivial sigma-field.
    This function does not join unrelated horizon-dependent reference laws.
    """
    p, q = _law(reference, "reference"), _law(selected, "selected")
    if not set(q) <= set(p):
        raise ValueError("selected law is not absolutely continuous with reference")
    depth = len(next(iter(p)))
    if any(len(path) != depth for path in q):
        raise ValueError("reference and selected laws have different path depth")
    if not isinstance(observable, Mapping) or set(observable) != set(p):
        raise ValueError("observable must be specified on the whole reference support")
    f = {path: exact(value) for path, value in observable.items()}
    means_p = sum((p[path]*f[path] for path in p), Q())
    means_q = sum((weight*f[path] for path, weight in q.items()), Q())
    ratios, means = [], []
    for level in range(depth+1):
        mass, qmass, weighted = {}, {}, {}
        for path, weight in p.items():
            prefix = path[:level]
            mass[prefix] = mass.get(prefix, Q()) + weight
            qmass[prefix] = qmass.get(prefix, Q()) + q.get(path, Q())
            weighted[prefix] = weighted.get(prefix, Q()) + weight*f[path]
        ratios.append({prefix: qmass[prefix]/weight for prefix, weight in mass.items()})
        means.append({prefix: weighted[prefix]/weight for prefix, weight in mass.items()})
    rows = []
    for level in range(1, depth+1):
        drmean = dmmean = dr2 = dm2 = pairing = Q()
        for path, weight in p.items():
            now, previous = path[:level], path[:level-1]
            dr = ratios[level][now]-ratios[level-1][previous]
            dm = means[level][now]-means[level-1][previous]
            drmean += weight*dr
            dmmean += weight*dm
            dr2 += weight*dr*dr
            dm2 += weight*dm*dm
            pairing += weight*dr*dm
        if drmean or dmmean:
            raise ArithmeticError("conditional-expectation martingale failed")
        rows.append(Innovation(level, drmean, dmmean, dr2, dm2, pairing))
    chi = sum((weight*(q.get(path, Q())/weight-1)**2 for path, weight in p.items()), Q())
    variance = sum((weight*(f[path]-means_p)**2 for path, weight in p.items()), Q())
    result = LikelihoodCertificate(depth, means_p, means_q, chi, variance, tuple(rows))
    if result.signed_difference != means_q-means_p:
        raise ArithmeticError("selection/observable innovation identity failed")
    if sum((row.likelihood_increment_square for row in rows), Q()) != chi:
        raise ArithmeticError("likelihood quadratic decomposition failed")
    if sum((row.observable_increment_square for row in rows), Q()) != variance:
        raise ArithmeticError("observable quadratic decomposition failed")
    return result


def inverse_phase_certificate(radix, depth, frequency, selected_index, tail=Q()):
    """Compact exact character projection on a uniform radix**depth fiber.

    X_J=(tail+J)/radix**depth, J uniform. Reveal J modulo radix**t.
    A None conditional_phase denotes zero; a Fraction denotes the unit value
    exp(2*pi*i*phase). No transcendental approximation enters this certificate.
    The chosen word's likelihood is radix**t on its cylinder and zero elsewhere.
    All nonzero innovation pairings are multiples of the final selected phase.
    """
    _integer(radix, "radix", 2)
    _integer(depth, "finite certificate depth", 0, 4096)
    _integer(frequency, "frequency")
    size = radix**depth
    _integer(selected_index, "selected inverse index", 0, size-1)
    tail = exact(tail)
    if not 0 <= tail < 1:
        raise ValueError("canonical tail in [0,1) required")
    selected_phase = circle(frequency*(tail+selected_index)/size)
    if frequency % size == 0:
        first = None
    else:
        reduced, valuation = abs(frequency), 0
        while reduced % radix == 0:
            reduced //= radix
            valuation += 1
        first = depth-valuation
    rows = []
    for level in range(depth+1):
        retained = radix**level
        residue = selected_index % retained
        visible = frequency % (size//retained) == 0
        phase = circle(frequency*(tail+residue)/size) if visible else None
        if visible and phase != selected_phase:
            raise ArithmeticError("resolved phase is not the selected phase")
        rows.append({
            "level": level,
            "retained_residue": residue,
            "conditional_phase": phase,
            "likelihood_on_selected_cylinder": retained,
            "likelihood_second_moment": retained,
            "signed_pairing_amplitude": int(level > 0 and level == first),
        })
    return {
        "radix": radix, "depth": depth, "frequency": frequency,
        "fiber_size": size, "tail": tail, "selected_index": selected_index,
        "selected_phase": selected_phase, "first_observable_level": first,
        "initial_phase_amplitude": int(first is None), "levels": tuple(rows),
        "selected_path_reference_probability": Q(1, size),
        "selected_likelihood": size, "selected_chi_square": size-1,
        "relative_entropy_log_radix_coefficient": depth,
        "reference_law": "declared uniform inverse fiber",
        "normality_estimate": False,
    }


def authentic_inverse_window(states, start, steps, frequency, *, binary=False):
    """Attach the exact resolution certificate to a native authentic BBP window.

    states=(U_1,...,U_N), authenticated from U_0=0. start can be zero.
    The macro forcing and terminal state determine the virtual inverse fiber;
    the original odd denominator chooses its unique admissible member.
    """
    if not verify_original_history(states):
        raise ValueError("original zero-seed four-pole history required")
    _integer(start, "start", 0)
    _integer(steps, "steps", 1)
    _integer(frequency, "frequency")
    if type(binary) is not bool or start+steps > len(states):
        raise ValueError("window must stay inside the authenticated prefix")
    initial = Q() if start == 0 else states[start-1]
    terminal = states[start+steps-1]
    forcing = Q()
    for offset in range(1, steps+1):
        forcing = 16*forcing + authentic_r(start+offset)
    tail = circle(terminal-forcing)
    size = 16**steps
    if tail.denominator % 2 == 0:
        raise ArithmeticError("authentic odd denominator was lost")
    selected = (-tail.numerator*pow(tail.denominator, -1, size)) % size
    if (selected+tail)/size != circle(initial):
        raise ArithmeticError("macro inverse failed to recover authentic selected state")
    result = inverse_phase_certificate(2 if binary else 16, 4*steps if binary else steps,
                                       frequency, selected, tail)
    result.update({"source_start": start, "source_steps": steps,
                   "source_terminal": terminal, "macro_forcing": forcing,
                   "source_selected_state": circle(initial),
                   "source_authenticated": True})
    return result


def smooth_selector_obstruction(m, frequency, lipschitz=Q()):
    """Finite witnesses for the paper's sharp continuous-approximation barrier.

    For 16 not dividing h, the odd section's character has minimax uniform
    distance one from continuous complex functions on the circle. For an
    L-Lipschitz candidate, one of these 16 tails has error at least the returned
    rational bound. This is an ALL-ODD-CARRIER result, not an orbit lower bound.
    """
    _integer(m, "witness scale", 1)
    _integer(frequency, "frequency")
    lipschitz = exact(lipschitz)
    if frequency % 16 == 0 or lipschitz < 0:
        raise ValueError("non-16-divisible frequency and nonnegative Lipschitz bound required")
    conductor = 16*m+1
    tails = tuple(Q(16-j, conductor) for j in range(16))
    inverses = tuple(exact_odd_inverse(tail) for tail in tails)
    if tuple(item.digit for item in inverses) != tuple(range(16)):
        raise ArithmeticError("nearby tails failed to realize every inverse label")
    lower = max(Q(), 1-(Q(44, 7)*abs(frequency)+16*lipschitz)/conductor)
    return {"conductor": conductor, "frequency": frequency,
            "lipschitz": lipschitz, "tails": tails,
            "selected_digits": tuple(item.digit for item in inverses),
            "finite_error_lower": lower, "continuous_minimax_error": Q(1),
            "domain": "all odd-denominator tails, not the selected time orbit"}


def adaptive_coboundary_control(horizon, p=Q(3, 4)):
    """Positive mixing reference whose local phase losses do not multiply.

    X_0=1; X_n iid signs, P(+1)=p. Z_n=X_(n-1)*X_n is a unit phase.
    Its conditional mean modulus is |2p-1| but product Z_n=X_N.
    The twisted matrix is diag(1,-1) P diag(1,-1) and retains eigenvalue one.
    """
    _integer(horizon, "horizon", 1, 4096)
    p = exact(p)
    if not 0 < p < 1:
        raise ValueError("strictly positive two-state reference kernel required")
    kernel = ((p, 1-p), (p, 1-p))
    twisted = ((p, p-1), (-p, 1-p))
    power = ((Q(1), Q()), (Q(), Q(1)))
    for _ in range(horizon):
        power = tuple(tuple(sum((power[i][k]*twisted[k][j] for k in range(2)), Q())
                            for j in range(2)) for i in range(2))
    actual = sum(power[0], Q())
    if actual != 2*p-1 or power != twisted:
        raise ArithmeticError("coboundary telescoping witness failed")
    return {"horizon": horizon, "reference_kernel": kernel,
            "twisted_kernel": twisted, "twisted_power": power,
            "local_conditional_modulus": abs(2*p-1),
            "actual_product_expectation": actual,
            "false_product_of_local_moduli": abs(2*p-1)**horizon,
            "unit_eigenvector": (Q(1), Q(-1)),
            "universal_local_modulus_product_bound_valid": False,
            "instance_violates_modulus_product_bound":
                abs(actual) > abs(2*p-1)**horizon}
