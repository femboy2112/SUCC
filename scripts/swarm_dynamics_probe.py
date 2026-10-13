#!/usr/bin/env python3
"""Reproducible exact cohort-D receipt; no external physical source claimed."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import json
from fractions import Fraction as F
from observational_succ.swarm_dynamics import (
    FiniteDynamics, stochastic_phase_source, noisy_latent_source,
    tent_uncertainty, les_fourier_counterexample, boost, causal_past,
)


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def receipt():
    hidden = FiniteDynamics("three-state-countermodel", "coarse-binary", 0,
                            (0, 2, 2), (0, 0, 1))
    noise = noisy_latent_source()
    cycle = FiniteDynamics("three-cycle", "pulse", 0, (1, 2, 0), (0, 0, 1))
    event, observer, parameter = (0, 2), (1, 0), F(1, 3)
    return encode({
        "schema": "SWM-D/1", "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "arithmetic": "exact integer/Fraction", "physical_authentication": False,
        "factor_countermodel": hidden.deterministic_factor(),
        "special_phase_factor": stochastic_phase_source().closure(),
        "hidden_noise_closure": noise.closure(),
        "noise_horizons": [noise.horizon_comparison((1, 0, 0, 0), n) for n in range(7)],
        "frontier": [tent_uncertainty((0, 1, 0, 1, 1, 0), n) for n in range(9)],
        "LES_negative_control": les_fourier_counterexample(),
        "delay_reconstruction": cycle.delay_quotient(2),
        "causal_access": {"before": causal_past(event, observer),
                          "after": causal_past(boost(event, parameter), boost(observer, parameter)),
                          "event_transformed": boost(event, parameter),
                          "observer_transformed": boost(observer, parameter)},
        "claims": {"deterministic_factor_criterion": "CLASSICAL / PROVED LOCAL",
                   "strong_lumpability_criterion": "CLASSICAL / PROVED LOCAL",
                   "closure_defect_horizon_bound": "CLASSICAL / PROVED LOCAL",
                   "finite_delay_bound": "CLASSICAL / PROVED LOCAL",
                   "generic_logistic_renormalization": "BLOCKED",
                   "quotient_Conley_invariance": "REFUTED",
                   "NS_global_regularity": "NOT CLAIMED"},
    })


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
