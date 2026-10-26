#!/usr/bin/env python3
"""Reproduce exact atom, layer-grading and golden-reference certificates.

Universal authority is in FOUR_POLE_ATOMIC_SUBSTRATE.md. This finite receipt
does not prove an infinite limit, selected Weyl cancellation, or normality.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import bbp_atomic_substrate as atoms
from observational_succ.euler_mascheroni_succ import gamma_bounds


def plain(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return plain(asdict(value))
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    return value


def outward(lower, upper, digits=20):
    scale = 10**digits
    lo = lower.numerator*scale//lower.denominator
    hi = -((-upper.numerator*scale)//upper.denominator)
    def show(number):
        sign = "-" if number < 0 else ""
        whole, fraction = divmod(abs(number), scale)
        return f"{sign}{whole}.{fraction:0{digits}d}"
    return {"lower": show(lo), "upper": show(hi),
            "endpoint_type": "outward rational decimal"}


def bracket_polynomial(a, b, c, bits=80):
    """Decreasing quadratic on [0,2/5], with its unique small root bracketed."""
    lo, hi = Q(), Q(2, 5)
    polynomial = lambda x: a*x*x+b*x+c
    assert polynomial(lo) > 0 > polynomial(hi)
    assert 2*a*lo+b < 0 and 2*a*hi+b < 0
    for _ in range(bits):
        middle = (lo+hi)/2
        if polynomial(middle) >= 0:
            lo = middle
        else:
            hi = middle
    return lo, hi


def receipt():
    paths = [
        "observational_succ/bbp_atomic_substrate.py",
        "observational_succ/bbp_natural_carrier.py",
        "observational_succ/euler_mascheroni_succ.py",
        "tests/test_bbp_atomic_substrate.py",
        "scripts/bbp_substrate_probe.py",
        "research/2026-10-26/bbp_mirror_polynomial_independent.py",
    ]
    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
              for name in paths}
    qlo, qhi = bracket_polynomial(1, -3, 1)
    g = lambda x: 1/(2-x)**2
    lower, upper = Q(), Q(2, 5)
    iterations = []
    for step in range(9):
        assert lower <= qlo < qhi <= upper
        assert upper-lower <= Q(2, 5)*Q(125, 256)**step
        iterations.append({
            "depth": step, "interval": outward(lower, upper),
            "exact_width": str(upper-lower),
            "proved_width_bound": str(Q(2, 5)*Q(125, 256)**step),
        })
        lower, upper = g(lower), g(upper)

    z, x = sp.symbols("z x")
    u, v = x-x*x/2, x*x/2
    original_pgf = 1/(2-z)**2
    paired_pgf = (8+z)/(4-z)**2
    shifted_pgf = original_pgf+(z-1)/8
    symbolic = {
        "original_fixed_point_factorization":
            sp.expand(z*(2-z)**2-1-(z-1)*(z*z-3*z+1)) == 0,
        "paired_fixed_point_factorization":
            sp.expand(z*(4-z)**2-(8+z)-(z-1)*(z*z-7*z+8)) == 0,
        "finite_prefix_fixed_point_factorization":
            sp.factor((shifted_pgf-z)*8*(2-z)**2
                      +(z-1)*(7*z*z-20*z+4)) == 0,
        "two_atom_layer_generating_function":
            sp.factor(((2-x)/(1-z*u)-x/(1-z*v))/8
                      -(1-x)/(4*(1-z*u)*(1-z*v))) == 0,
    }
    assert all(symbolic.values())
    endpoint_weights = []
    packet_checks = 0
    for j in range(13):
        p = ((2-x)*u**j-x*v**j)/8
        positive = (1-x)*sum(u**k*v**(j-k) for k in range(j+1))/4
        assert sp.expand(p-positive) == 0
        weight = Q(j+1, 2**(j+2))
        assert sp.diff(p, x).subs(x, 1) == -sp.Rational(weight.numerator, weight.denominator)
        endpoint_weights.append(str(weight))
        packet_checks += 1
    regrouped = [str(Q(2*j+1, 2**(2*j+2))+Q(2*j+2, 2**(2*j+3)))
                 for j in range(9)]
    assert regrouped == [str(Q(3*j+2, 4**(j+1))) for j in range(9)]
    qhatlo, qhathi = bracket_polynomial(7, -20, 4)
    assert qhathi < qlo
    gamma_lo, gamma_hi = gamma_bounds(4096, 32)
    offset = outward(1-qhi-gamma_hi, 1-qlo-gamma_lo)

    projective = []
    state = (Q(), Q(1))
    for step in range(5):
        projective.append({
            "step": step, "lift": plain(state),
            "slope": "infinity" if not state[1] else str(state[0]/state[1]),
        })
        state = tuple(sum((a*b for a, b in zip(row, state)), Q())
                      for row in atoms.COMPLEX_BLOCK)
    assert [row["slope"] for row in projective] == ["0", "-1", "infinity", "1", "0"]
    assert projective[-1]["lift"] == ["0", "-1/4"]

    coefficients = [atoms.atomic_coefficient(j) for j in range(24)]
    for j in range(16):
        assert coefficients[j+8] == coefficients[j]/16
    holds = {}
    for n in (1, 2, 7, 31, 97, 257, 1009, 65521):
        value = atoms.compiled_forcing(n)
        direct = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        assert value == direct
        holds[str(n)] = True

    return plain({
        "schema_version": 1,
        "status": "EXACT_FINITE_ATOMIC_AND_GRADED_SOURCE_CERTIFICATES",
        "baseline_commit": "7989be5753341c5e74d570e8fea51e00129d2d0a",
        "source_sha256": hashes,
        "source_forcing_holdouts": holds,
        "atomic_clock": atoms.atomic_clock_certificate(),
        "minimal_coefficient_realization": atoms.minimal_realization_certificate(),
        "first_24_kernel_coefficients": coefficients,
        "signed_projective_cycle": projective,
        "finite_atomic_tails": [
            atoms.atomic_tail_certificate(n, depth)
            for n in (0, 1, 8, 128) for depth in (1, 4, 12)],
        "graded_endpoint": {
            "symbolic_identities": symbolic,
            "packet_and_derivative_identities_checked": packet_checks,
            "weights_j_zero_through_12": endpoint_weights,
            "PGF": "1/(2-z)^2",
            "minimal_fixed_point_interval": outward(qlo, qhi),
            "complement_interval": outward(1-qhi, 1-qlo),
            "finite_rational_iterations": iterations,
            "Gamma2_log_mean_minus_fixed_point": offset,
            "gamma_prefix_count": 4096,
            "gamma_log_terms": 32,
        },
        "grading_controls": {
            "adjacent_group_weights": regrouped,
            "adjacent_group_PGF": "(8+z)/(4-z)^2",
            "adjacent_group_mean": "7/9",
            "adjacent_group_minimal_fixed_point": "1",
            "first_two_packet_redistribution_PGF": "1/(2-z)^2+(z-1)/8",
            "redistribution_minimal_fixed_point_interval": outward(qhatlo, qhathi),
            "redistribution_preserves_all_approximants_at_depth_at_least": 2,
        },
        "joint_law_control": {
            "natural_endpoint_mixed_moment_EJY": "4",
            "auxiliary_Poisson_coupling_mixed_moment_EJY": "6",
            "same_marginals_identify_joint_law": False,
        },
        "paper_defect_formula": "(M+2)/2^(M+1), uniform relative source error",
        "scope": {
            "all_n_authority_is_paper_proof": True,
            "four_state_tail_realization_claimed": False,
            "offset_is_ungraded_source_invariant": False,
            "Poisson_joint_mechanism_authenticated": False,
            "selected_Weyl_cancellation_proved": False,
            "pi_normality_proved": False,
            "RH_proved": False,
            "new_Lean_kernel_theorem": False,
        },
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    actual = receipt()
    if args.verify:
        if json.loads(args.verify.read_text()) != actual:
            raise SystemExit("SUBSTRATE_RECEIPT_MISMATCH: source or certificate changed")
        print("BBP_ATOMIC_SUBSTRATE_RECEIPT_VERIFIED")
    else:
        print(json.dumps(actual, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
