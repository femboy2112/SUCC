#!/usr/bin/env python3
"""Declared finite phase-frame diagnostics; all spectral numbers are numerical.

The exact population and sampling budgets have separate rational proofs.
This seeded PRNG run is reproducible, not a physical random-source experiment
and not an interval certification of the displayed eigenvalues.
"""
from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import random

import numpy as np

from observational_succ.bbp_collision_frame import (
    fejer_population_certificate, gamma_population_certificate,
    recommended_fejer_width, recommended_gamma_scale,
    source_spacing_certificate, smallest_gram_eigenvalue_upper,
)
from observational_succ.random_probe_frames import frame_sampling_certificate
from observational_succ.duck_bbp import tail_interval


HERE = Path(__file__).resolve().parent


def source(n):
    # Independent literal encoding of the original four-channel forcing.
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def original_phases(b):
    state = Q()
    phases = []
    for n in range(1, 2*b):
        state = 16*state+source(n)
        if n >= b:
            phases.append(float(state % 1))
    return np.exp(2j*np.pi*np.array(phases))


def scaled_rational(value, scale):
    # Integer multiplication and phase reduction precede floating evaluation.
    return float((value*int(scale)) % 1)


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def run():
    plan = json.loads((HERE/'receipts/numerical_probe_plan.json').read_text())
    rng = random.Random(plan['reproducible_prng_seed'])
    rows = []
    for b in plan['exploration_shells']+plan['fresh_holdout_shells']:
        spacing = source_spacing_certificate(b)
        width = recommended_fejer_width(b)
        population = fejer_population_certificate(b, width)
        sampling = frame_sampling_certificate(b, Q(1, 4), Q(1, 2), Q(1, 64))
        clocks = [1+rng.randrange(width)+rng.randrange(width)
                  for _ in range(sampling.independent_rows)]
        nodes = [source(n+1) for n in range(b, 2*b)]
        # Exact rational reductions avoid feeding large unwrapped phases
        # to the finite-precision exponential.
        turns = np.array([[scaled_rational(t, k) for t in nodes] for k in clocks])
        a = np.exp(2j*np.pi*turns)
        gram = a.conj().T@a/len(clocks)
        eigenvalues = np.linalg.eigvalsh(gram)
        lo, hi = float(eigenvalues[0]), float(eigenvalues[-1])
        assert lo > float(sampling.gram_eigenvalue_lower)-1e-10
        assert hi < float(sampling.gram_eigenvalue_upper)+1e-10

        differences = np.array([[float(t2-t1) for t2 in nodes] for t1 in nodes])
        lam = recommended_gamma_scale(b)
        gamma_gram = (1+lam*(1-np.exp(2j*np.pi*differences)))**-2
        gamma_eig = np.linalg.eigvalsh(gamma_gram)
        gamma_certificate = gamma_population_certificate(b, lam)
        assert gamma_eig[0] >= float(gamma_certificate.eigenvalue_interval[0])-1e-9
        assert gamma_eig[-1] <= float(gamma_certificate.eigenvalue_interval[1])+1e-9

        counter_turns = []
        for n in range(b, 2*b):
            lower, upper = tail_interval(n, 12)
            counter_turns.append(float(-(lower+upper)/2))
        carriers = {
            'authentic_zero_seed': original_phases(b),
            'locked': np.ones(b, dtype=complex),
            'zero_mean_roots_of_unity': np.exp(2j*np.pi*np.arange(b)/b),
            'same_forcing_counterseed_tail_midpoints':
                np.exp(2j*np.pi*np.array(counter_turns)),
        }
        locked_output = a@carriers['locked']/b
        outputs = {}
        for name, c in carriers.items():
            output = a@c/b
            recovered = b*np.linalg.solve(gram, a.conj().T@output/len(clocks))
            error = float(np.max(np.abs(recovered-c)))
            assert error < 1e-9
            energy = float(np.mean(np.abs(output)**2))
            oriented = float(np.mean(np.abs(output-locked_output)**2))
            escape = float(np.mean(1-c.real))
            assert lo/b-1e-10 <= energy <= hi/b+1e-10
            assert b*oriented/(2*hi)-1e-10 <= escape <= b*oriented/(2*lo)+1e-10
            outputs[name] = {
                'mean_real': float(c.mean().real),
                'mean_imaginary': float(c.mean().imag),
                'mean_modulus': float(abs(c.mean())),
                'raw_energy': energy,
                'B_times_raw_energy': b*energy,
                'oriented_residual_energy': oriented,
                'B_times_oriented_residual': b*oriented,
                'escape_mean': escape,
                'maximum_reconstruction_error': error,
            }
        assert outputs['locked']['mean_modulus'] == 1.0
        assert outputs['locked']['oriented_residual_energy'] == 0.0
        assert outputs['zero_mean_roots_of_unity']['mean_modulus'] < 1e-12
        rows.append({
            'B': b,
            'region': 'fresh_holdout' if b in plan['fresh_holdout_shells'] else 'exploration',
            'source_spacing_exact': serial(asdict(spacing)),
            'finite_fejer_width': width,
            'observed_clock_min': min(clocks),
            'observed_clock_max': max(clocks),
            'sampling_certificate': serial(asdict(sampling)),
            'empirical_gram_eigenvalue_min_numerical': lo,
            'empirical_gram_eigenvalue_max_numerical': hi,
            'population_gamma_scale': lam,
            'population_gamma_eigenvalue_min_numerical': float(gamma_eig[0]),
            'population_gamma_eigenvalue_max_numerical': float(gamma_eig[-1]),
            'subcritical_scale_B_squared_lower_eigenvalue_upper_exact':
                str(smallest_gram_eigenvalue_upper(b, 2*b*b*(1+b*b))),
            'carrier_diagnostics_numerical': outputs,
        })
    return {
        'status': 'PASS',
        'scope': 'Finite numerical diagnostics and exact input budgets; no interval spectral proof, physical independence, normality test, or asymptotic source estimate.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'plan_sha256': hashlib.sha256((HERE/'receipts/numerical_probe_plan.json').read_bytes()).hexdigest(),
        'numpy_version': np.__version__,
        'rows': rows,
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
