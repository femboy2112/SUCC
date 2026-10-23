#!/usr/bin/env python3
"""Replay source-hashed exact witnesses for Carry the Truth; no zero inputs."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import source_faithful_carry as carry
from observational_succ import source_faithful_limits as limits
from observational_succ import source_faithful_memory as memory
from observational_succ import source_faithful_observers as observers
from observational_succ import source_faithful_resolvent as resolvent
from observational_succ import source_faithful_weil as weil

DESTINATION = ROOT / 'research/2026-10-23/SOURCE_FAITHFUL_EXACT_RECEIPT.json'


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return serial(asdict(value))
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def compact_band(lo, hi, bits=48):
    scale = 1 << bits
    return (Q((lo*scale).__floor__(), scale), Q((hi*scale).__ceil__(), scale))


def receipt():
    source_paths = sorted(
        [*ROOT.glob('observational_succ/source_faithful_*.py'),
         *ROOT.glob('tests/test_source_faithful_*.py'),
         *(ROOT/'observational_succ'/name for name in (
             'reality_pin_arithmetic.py', 'reality_pin_continuum.py',
             'boundary_realization_selection.py', 'tate_suzuki_shorting.py',
             'source_weil_hierarchy.py')),
         ROOT/'formal/SourceFaithfulCarry.lean',
         ROOT/'scripts/check_source_faithful_carry_lean.py', Path(__file__).resolve()])
    x, y, z = Q(-14, 15), Q(7, 135), Q(7, 625)
    pin = observers.pin_arithmetic_entries((x, x), (y, y), (z, z))
    kernel = limits.cycle_heat_brackets(128, Q(1, 8), Q(1, 4), 96)[0]
    gaussian = limits.gaussian_heat_bracket(Q(1, 4), Q(0))
    half_energy = weil.box_log_energy({n: 1 for n in range(13, 20)})
    result = {
        'schema': 'succ-source-faithful-exact-v1',
        'parent': '5e2ba04c8b4ab627b6b0add588609c347346a1a2',
        'source_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                          for p in source_paths},
        'original_signed_source': weil.source_fingerprint(),
        'carry': {
            'terminal_coordinates': {p: carry.radix_address(p*13, p) for p in (2, 3, 5, 7)},
            'visible_and_defect': {p: carry.uniform_defect(p) for p in (2, 3, 5, 7)},
            'successor_moments_a3': {n: carry.compressed_successor(n, 3) for n in range(7)},
            'energy_ratio_example': carry.energy_cocycle_ratio(7, 2, 5),
            'prime_power_8': carry.prime_power_at(8),
            'fake_primitive_6': carry.prime_power_at(6),
        },
        'memory': {
            'binary_antiperiodic_moments': memory.basis_moments(2, -1, 8),
            'binary_hidden_kernels': memory.memory_kernels(2, -1, 5),
            'minimal_hankel_determinants': {a: memory.hankel_determinant(a, -1, a)
                                            for a in (2, 3, 5, 7, 11)},
            'independent_elimination_agrees': all(
                memory.basis_moments(a, -1, 3*a) == memory.reconstruct_with_memory(a, -1, 3*a)
                for a in (2, 3, 5, 7)),
            'false_one_step_semigroup_rejected': memory.moment(2, -1, 2) != memory.moment(2, -1, 1)**2,
        },
        'limits': {
            'local_chart': limits.local_chart_certificate(720, Q(1, 24), Q(2)),
            'action_horizon': limits.action_horizon(720, Q(1, 24), Q(1),
                (('translate', Q(1, 3)), ('multiply', 3), ('translate', Q(-1, 7)))),
            'cyclic_multiplier_is_not_source_isometry': limits.cyclic_multiplier_defect(120, 5),
            'hidden_heat_defect': {a: limits.hidden_heat_defect(a) for a in (2, 3, 5, 7)},
            'certified_cycle_heat_density_at_origin': compact_band(8*kernel.lower, 8*kernel.upper),
            'certified_gaussian_density_at_origin': compact_band(gaussian.lower, gaussian.upper),
            'analytic_heat_error_budget': limits.heat_density_error_bound(128, Q(1, 8), Q(1, 2), 0),
            'rational_character_one_sixth': limits.rational_character_product_exponent(1, 6),
        },
        'observer': {
            'finite_horizon_classes_a5': {h: observers.carry_horizon_partition(5, h) for h in range(5)},
            'calibrated_carry_protocol': observers.carry_protocol(31, 7, Q(2, 3), Q(1, 7)),
            'synthetic_affine_energy_pin': pin,
            'unused_prime7_holdout': observers.arithmetic_prime_holdout(pin, 7),
            'offset_recovered': False,
        },
        'resolvent_memory': {
            'radix_two_exact_schur': resolvent.radix_two_schur(Q(1), Q(1, 8), Q(63, 65)),
            'radix_three_uniform_budget': resolvent.uniform_band_budget(3, Q(1, 32), 1, 1, 2),
            'bounded_alpha_band_required_for_memory_limit': True,
        },
        'weil_boundary': {
            'unweighted_growth_lower': {n: weil.unweighted_cluster_lower(n) for n in (4, 16, 31)},
            'half_density_box_energy': compact_band(half_energy.lo, half_energy.hi),
            'half_density_synthesis_norm_squared_upper': weil.compact_seed_synthesis_bound(1, 1),
            'phase_blind_schur_failure': weil.phase_blind_schur_counterexample(),
            'genuine_prime_atom_negative': weil.genuine_prime_two_negative_atom(),
            'completion_mutant_changes': weil.completion_mutation_differences(),
        },
        'authority': {
            'finite_witnesses_are_universal_proofs': False,
            'analytic_results_lean_certified': False,
            'physical_measurements_performed': False,
            'named_passive_cyclicity_proved': False,
            'original_S4_improved': False,
            'RH_proved': False,
        },
    }
    if not result['memory']['independent_elimination_agrees']:
        raise AssertionError('memory routes disagree')
    return serial(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--write', action='store_true')
    group.add_argument('--check', action='store_true')
    args = parser.parse_args()
    text = json.dumps(receipt(), indent=2, sort_keys=True)+'\n'
    if args.write:
        DESTINATION.write_text(text)
        print('Wrote '+str(DESTINATION.relative_to(ROOT)))
    elif args.check:
        if DESTINATION.read_text() != text:
            raise SystemExit('Exact source witness or executable fingerprint drift')
        print('Source-faithful exact receipt and listed executable fingerprints match')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
