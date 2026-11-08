#!/usr/bin/env python3
"""Source-bound exact finite pin-bed receipt; prospectively chosen epochs only."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.carrier_relative_targets import Carrier, Instrument, Target
from observational_succ.fourier_yoneda_pinbed import (
    CircleLaw, FuturePinBed, affine_push, bbp_epoch,
    bbp_surface_norm_error_squared, finite_affine_push, finite_convolution,
    finite_pin_support, law_support_closure, pin_surface,
    relative_truth_certificate, surface_energy, surface_energy_pairs,
    transported_pin, verify_bbp_trace,
)


def four_poles(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def decimal_outward(value, digits=18):
    scale = 10**digits
    low = (value.numerator*scale)//value.denominator
    def display(n):
        return f"{n//scale}.{n % scale:0{digits}d}"
    return [display(low), display(low+1)]


def file_hash(relative):
    return sha256((ROOT/relative).read_bytes()).hexdigest()


def run():
    records = []
    source_checks = 0
    for a in (17, 31, 61, 127):
        law, states = bbp_epoch(a)
        assert verify_bbp_trace(states)
        independent_unwrapped = Q(0)
        for n, state in enumerate(states[1:], 1):
            independent_unwrapped = 16*independent_unwrapped + four_poles(n)
            assert Q(state.numerator, state.conductor) == independent_unwrapped
            source_checks += 1
        value = surface_energy(law)
        if a in (17, 31):
            assert value == surface_energy_pairs(law)
        assert value > 0
        exact_trace = "\n".join(f"{s.n}:{s.conductor}:{s.numerator}" for s in states)
        records.append({
            "epoch": [a, 2*a], "sample_count": a,
            "source_trace_sha256": sha256(exact_trace.encode()).hexdigest(),
            "source_zero_and_every_transition_verified": True,
            "independent_four_pole_source_checked_through": 2*a-1,
            "exact_energy": str(value),
            "energy_decimal_outward": decimal_outward(value),
            "pair_oracle_also_run": a in (17, 31),
            "completed_pi_surface_norm_error_squared_upper": str(bbp_surface_norm_error_squared(a)),
            "scope": "one finite original-source epoch; not an asymptotic assertion",
        })

    k = (Q(1, 3),)*3 + (Q(0),)*3
    u = (Q(1, 6),)*6
    v = (Q(1, 4), Q(1, 8), Q(1, 8), Q(1, 4), Q(1, 8), Q(1, 8))
    assert finite_convolution(k, u) == finite_convolution(k, v)
    next_u = finite_convolution(k, finite_affine_push(u, 2))
    next_v = finite_convolution(k, finite_affine_push(v, 2))
    assert next_u != next_v

    step = tuple(((x >> 1) & 1) | 2 | ((((x >> 2) & 1) ^ 1) << 2) for x in range(8))
    carrier = Carrier("pinbed-f2-declared", 8, (
        Instrument("read", "bit-character", tuple(Q((-1)**(x & 1)) for x in range(8)), tuple(range(8))),
        Instrument("advance", "no-readout", (Q(0),)*8, step),
    ))
    target = Target(carrier.source, "hidden x3 is zero", tuple(Q(1-((x >> 2) & 1)) for x in range(8)))
    relative = relative_truth_certificate(carrier, target, 4)
    assert relative["relative_truth"] == "TRUE_COMPATIBLE"
    assert relative["invariant_truth"] is None

    aliases = []
    for q in (1, 3, 5, 7, 9, 17):
        law = CircleLaw(tuple((Q(j, q)+Q(k, 3*q), p/q)
                              for j in range(q)
                              for k, p in ((0, Q(1, 4)), (1, Q(3, 8)), (2, Q(3, 8)))))
        assert affine_push(law, 16) == law
        assert all(pin_surface(law, Q(i, q)) == 0 for i in range(q))
        e = surface_energy(law)
        assert e == Q(1, 6480*q**4)
        aliases.append({"sampled_pin_count": q, "sampled_centered_heights": ["0"]*q,
                        "exact_x16_invariant": True, "full_surface_energy": str(e)})

    bed = FuturePinBed(((-2, Q(1, 5)), (-1, Q(1)), (1, Q(1)), (2, Q(1, 5))), 2, Q(3, 4))
    hashes = {p: file_hash(p) for p in (
        "observational_succ/fourier_yoneda_pinbed.py",
        "observational_succ/integer_bbp_carrier.py",
        "tests/test_fourier_yoneda_pinbed.py",
        "research/2026-11-07/fourier_yoneda_pinbed/PREREGISTRATION.md",
        "research/2026-11-07/fourier_yoneda_pinbed/probe.py",
    )}
    return {
        "status": "PASS_EXACT_FINITE",
        "base_commit": "d32342d375f44ddf62221ad6aff2f534abdc0a03",
        "source": "original BBP four signed poles; literal U0=0; integer conductor engine",
        "source_steps_independently_checked_including_repeated_prefixes": source_checks,
        "fresh_epochs": records,
        "static_alias_next_step_split": {
            "initial_surface": finite_convolution(k, u),
            "next_uniform": next_u, "next_alternative": next_v,
            "support_completion": law_support_closure(6, finite_pin_support(k), (2,)),
        },
        "carrier_relative_truth": relative,
        "all_future_finite_pin_aliases": aliases,
        "discounted_completion": {
            "base_weights": bed.base, "discount": bed.discount,
            "sum_weight_at_two": bed.weight(2),
            "least_weight_at_two": bed.weight(2, least_envelope=True),
            "total_weight": bed.total_completed_weight,
            "squared_lipschitz_upper": bed.squared_lipschitz_bound,
            "depth_12_squared_distance_tail": bed.squared_distance_tail(12),
            "off_ray_mode_three": bed.weight(3),
        },
        "sha256": hashes,
        "universal_theorems_proved_by_this_finite_run": False,
        "source_selected_surface_decay": "OPEN",
        "pi_base16_normality": "OPEN",
    }


def encode(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(f"Unsupported receipt value: {type(value).__name__}")


if __name__ == "__main__":
    print(json.dumps(run(), default=encode, indent=2, sort_keys=True))
