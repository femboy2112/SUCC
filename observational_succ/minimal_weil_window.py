"""Exact support/separation certificates for arithmetic Weil observations.

The mutation class has independently variable REAL coefficients at paired
genuine prime-power atoms. Mutants are coefficient tapes, not alternative
zeta functions. Gamma, contact and both pole channels are separate fixed data.
The analytic bump theorem is PT-C05, not a consequence of finite tests.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .suzuki_arch_intervals import log_interval
from .tate_weil_window import CompactWeilSourceWindow
from .tate_weil_distribution import TateWeilSource


def _rational(x):
    if type(x) not in (int, Q):
        raise ValueError("Exact rational half-support required")
    return Q(x)


def integer_log_bounds(n: int, terms: int = 32) -> tuple[Q, Q]:
    if type(n) is not int or n < 1:
        raise ValueError("Positive integer logarithm required")
    k = n.bit_length()-1
    lo2, hi2 = log_interval(Q(2), terms)
    lo, hi = log_interval(Q(n, 2**k), terms)
    return k*lo2+lo, k*hi2+hi


def minimum_arithmetic_window(a, *, terms: int = 32,
                              source: TateWeilSource = TateWeilSource()) -> dict:
    """Finite candidate enumeration + outward rational comparison; can refuse.

    Terms <=150 and ceil(2a)<=6 are execution limits, not analytic hypotheses.
    Unseparated endpoint comparisons are UNRESOLVED; no float sign guessing.
    """
    a = _rational(a)
    if a <= 0 or a > 3:
        raise ValueError("Execution half-support budget: 0<a<=3")
    if type(source) is not TateWeilSource:
        raise ValueError("Declared canonical TateWeilSource required")
    candidate = CompactWeilSourceWindow(a).certificate()
    active, outside, unresolved = [], [], []
    for n, p in candidate["included_genuine_prime_power_labels"]:
        bounds = integer_log_bounds(n, terms)
        row = (n, p, bounds)
        if bounds[1] < 2*a:
            active.append(row)
        elif bounds[0] >= 2*a:
            outside.append(row)
        else:
            unresolved.append(row)
    return {"source_id": source.source_id, "epoch": source.epoch,
            "canonical_character": source.character, "half_support": a,
            "active": tuple(active), "outside": tuple(outside),
            "unresolved": tuple(unresolved), "integer_cutoff": candidate["strict_integer_cutoff"],
            "outcome": "PROVEN_MINIMUM_FOR_TAPE_CLASS" if not unresolved else "UNRESOLVED",
            "mutation_class": "independent real coefficients at paired genuine prime-power atoms",
            "canonical_zero_coefficients_may_be_mutated": True,
            "mutants_are_genuine_zeta_sources": False,
            "Gamma_poles_contact_included": False,
            "authority": "PAPER_PROVED", "comparison_authority": "EXACT_FINITE_CHECK",
            "proof": "PT-C05"}


def autocorrelation_atom_witness(a, n: int, *, terms: int = 32) -> dict:
    """Exact certificate for two bumps centered at ±log(n)/2.

    eta(t)=exp(-1/(1-(t/epsilon)^2)) on |t|<epsilon, zero elsewhere;
    f(t)=eta(t+log(n)/2)+eta(t-log(n)/2). Then (f*f~)(log n)
    equals ||eta||² > epsilon/27 and vanishes at every other active atom.
    The proof is support arithmetic plus e<3, not quadrature of a bump.
    """
    if type(n) is not int:
        raise ValueError("Exact genuine prime-power atom required")
    window = minimum_arithmetic_window(a, terms=terms)
    if window["unresolved"]:
        return {"outcome": "UNRESOLVED", "unresolved": window["unresolved"]}
    active = {row[0]: row for row in window["active"]}
    if n not in active:
        raise ValueError("Atom is outside the open support or is not a genuine prime power")
    lo, hi = active[n][2]
    margins = [2*window["half_support"]-hi, lo]
    for other, _, (lower, upper) in active.values():
        margins.append(lower)  # exclude all atoms from the central bump at zero
        if other < n:
            margins.append(lo-upper)
        elif other > n:
            margins.append(lower-hi)
    if min(margins) <= 0:
        return {"outcome": "UNRESOLVED", "reason": "log intervals do not separate atoms"}
    epsilon = min(margins)/8
    return {"outcome": "PROVEN_SENSITIVE_AUTOCORRELATION", "atom": n,
            "log_interval": (lo, hi), "epsilon": epsilon,
            "centers": ("-log(n)/2", "+log(n)/2"),
            "f_formula": "eta(t+log(n)/2)+eta(t-log(n)/2)",
            "eta_formula": "exp(-1/(1-(t/epsilon)^2)) if |t|<epsilon, else 0",
            "autocorrelation_at_atom_lower_strict": epsilon/27,
            "unit_paired_coefficient_response_abs_lower_strict": 2*epsilon/27,
            "other_active_atoms": tuple(m for m in active if m != n),
            "positive_separation_margins": tuple(margins),
            "authority": "PAPER_PROVED", "support_check_authority": "EXACT_FINITE_CHECK",
            "mutants_are_genuine_zeta_sources": False, "proof": "PT-C05"}
