#!/usr/bin/env python3
"""Deterministic exact receipt and optional independently computed diagnostics."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import mobius_signed_contrasts as M

PARENT = '461942c0bf616518e668d236d1c6b1596665a7dd'
RECEIPT = ROOT / 'research/2026-10-25/MOBIUS_MATRIX_RECEIPT.json'


def blob_hash(path):
    raw = path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def phase_hash(poly):
    return hashlib.sha256(repr(poly.terms).encode()).hexdigest()


def outward_decimal(interval, places=12):
    low, high = interval; scale = 10**places
    return [str(Q((low*scale).__floor__(), scale)), str(Q((high*scale).__ceil__(), scale))]


def report():
    parent_blob = blob_hash(ROOT/'observational_succ/succ_internal_matrix_walk.py')
    if parent_blob != 'fa1abb9dbeee0d7b4d9972e3b0e40a5feaed3c9e':
        raise RuntimeError('Pinned IMW dependency changed: inspect before regenerating receipt')
    states = M.source_states(13)
    grid = M.PrimeGrid((3, 5, 7), (2, 1, 1))
    walk = M.RefinedMatrixWalk.build(13, grid, (0, 1, 4))
    recovered = M.invert_thresholds(grid, walk.thresholds(), 3)
    assert recovered == dict(walk.blocks)
    clock = M.primitive_clock_budget(states, 6)
    cols = tuple(tuple(M.PrimeGrid((p,), (1,)).signature(n)[0] for n in range(1, 4)) for p in (5, 7))
    contrast = M.boolean_energy_contrast(states[:3], cols)
    control = M.coherent_seed_control(48, 16, (3, 5, 7))
    gains = M.refinement_energy(states[:8], (0,)*8, tuple(range(8)))[0]
    paths = [ROOT/'observational_succ/mobius_signed_contrasts.py',
             ROOT/'tests/test_mobius_signed_contrasts.py', Path(__file__).resolve()]
    return {
        'parent_commit': PARENT,
        'source': 'original U0=0; four signed BBP poles; exact integer lifts',
        'authority': 'exact finite replay plus separate paper proofs; no asymptotic inference',
        'dependency_blob': parent_blob,
        'file_blobs': {str(p.relative_to(ROOT)): blob_hash(p) for p in paths},
        'mobius_blocks_equal_direct_grams': True,
        'source_horizon': len(states), 'observer_grid': {'primes': list(grid.primes), 'depths': list(grid.depths)},
        'occupied_cells': sum(block[0][0] != M.PhasePoly.zero() for _, block in walk.blocks),
        'source_mask_period': grid.modulus,
        'pole_tail_densities': {str(p): [str(M.pole_tail_density(p, k)) for k in (1, 2, 3)] for p in (2, 3, 5, 7, 11)},
        'authentic_p5_p7_N3_interaction_interval': outward_decimal(M.real_phase_interval(contrast)),
        'nested_full_gain_N8_interval': outward_decimal(M.real_phase_interval(gains)),
        'clock_6_primitive_energy_hashes': {str(d): phase_hash(e) for d, e in clock['energies'].items()},
        'clock_6_raw_mean_error': str(clock['raw_mean_error_cap']),
        'clock_transport_N257_Q77_H8': {k: str(v) for k, v in M.clock_transport_caps(257, 77, 8).items()},
        'counterfeit': {'horizon': 48, 'window_start': 16, 'seed': str(control['initial']),
                        'radius': str(control['radius']),
                        'every_partition_gain_cap_h1': str(control['all_partition_gain_cap_h1']),
                        'preserves_exact_forcing': True, 'preserves_zero_initial': False},
        'pi_normality_proved': False, 'RH_proved': False, 'new_Lean_authority': False,
    }


def diagnostics():
    """Independent literal rational forcing; high precision is NOT a certificate.

    Training horizon 128/h1; held-out horizons 256,512,1024 and h=2,3,5,17.
    The finite band E<=4*K/N is a diagnostic to falsify, NOT an all-N theorem.
    No parameter is fitted to the holdout. All tested rows are retained.
    """
    import mpmath as mp
    histories = []; u = Q()
    for n in range(1, 1025):
        r = Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        u = 16*u+r; histories.append(u)
    histories = tuple(histories)
    M.authenticate(histories)
    grids = (M.PrimeGrid(), M.PrimeGrid((7, 11, 13), (2, 2, 1)), M.PrimeGrid((3, 5, 7), (1, 1, 1)))
    signatures = {grid: tuple(grid.signature(n) for n in range(1, 1025)) for grid in grids}
    rows = []
    def energy(z, labels):
        cells = {}
        for v, a in zip(z, labels):
            c, s = cells.get(a, (0, mp.mpc(0))); cells[a] = (c+1, s+v)
        return sum(abs(s)**2/c for c, s in cells.values())/len(z), len(cells)
    with mp.workdps(80):
        for h in (1, 2, 3, 5, 17):
            phases = tuple((h*x) % 1 for x in histories)
            z = tuple(mp.exp(2*mp.pi*mp.j*mp.mpf(x.numerator)/x.denominator) for x in phases)
            for n in (128, 256, 512, 1024):
                for grid in grids:
                    e, k = energy(z[:n], signatures[grid][:n])
                    rows.append({'N': n, 'h': h, 'primes': list(grid.primes), 'depths': list(grid.depths),
                                 'energy': mp.nstr(e, 18), 'occupied_cells': k,
                                 'N_energy_per_cell': mp.nstr(n*e/k, 18), 'finite_band_pass': bool(e <= mp.mpf(4)*k/n),
                                 'complete_CRT_balance_available': grid.modulus <= n,
                                 'role': 'training' if n == 128 and h == 1 else 'fresh_holdout'})
        counterfeit = M.counterfeit_states(1024)
        control_phases = tuple(x % 1 for x in counterfeit)
        z = tuple(mp.exp(2*mp.pi*mp.j*mp.mpf(x.numerator)/x.denominator) for x in control_phases)
        controls = []
        for grid in grids:
            e, k = energy(z, signatures[grid])
            controls.append({'N': 1024, 'fixed_authentic_mask_primes': list(grid.primes),
                             'energy': mp.nstr(e, 18), 'occupied_cells': k,
                             'finite_band_pass': bool(e <= mp.mpf(4)*k/1024)})
    return {'authority': '80-digit numerical diagnostics, not interval or infinite proof',
            'method': 'independent combined rational forcing; exact reduction mod1 BEFORE floating evaluation',
            'candidate_band': 'E <= 4*K/N; finite sanity check ONLY', 'rows': rows,
            'nonnormal_controls_with_identical_observer_masks': controls}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--diagnostics', action='store_true')
    args = parser.parse_args()
    if args.diagnostics:
        print(json.dumps(diagnostics(), indent=2, sort_keys=True)); return
    actual = report()
    if args.verify:
        if not RECEIPT.exists() or json.loads(RECEIPT.read_text()) != actual:
            raise SystemExit('MOBIUS_MATRIX_RECEIPT_MISMATCH')
        print('MOBIUS_MATRIX_EXACT_RECEIPT_VERIFIED'); return
    text = json.dumps(actual, indent=2, sort_keys=True)+'\n'
    if args.write:
        RECEIPT.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
