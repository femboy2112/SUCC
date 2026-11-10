"""Run the fixed signed-lag protocol; all mathematical endpoints are integers."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time
from lag_instrument import (HERE, PRIOR, Box, Interval, SCALE, ONE, ZERO,
                            phase, mean, sliding_energy, energy_from_lags,
                            signed_transport, verdict)
from source import common_history, direct_modular_residue, principal_pair, matched_seed
from prime_epochs import good_prime, order16, variation
from observational_succ.selected_orbit import original_forcing


def run(A):
    start = time.monotonic()
    menu = [H for H in (2, 4, 8, 16, 32, 64) if 4*H <= A]
    maximum = max(menu)
    p = good_prime(A)
    m = order16(p)
    data = common_history(2*A+maximum-2, A)
    D = data['denominator']
    residues = data['residues']
    for n in (A, A+A//2, 2*A-1, 2*A+maximum-2):
        assert residues[n-A] == direct_modular_residue(n, D)
    parts = [principal_pair(r, D, p) for r in residues[:A]]
    assert all(d == p for _, d in parts)
    primes = tuple(sorted({3, 5, 7, 11, p}))
    seed, _, _ = matched_seed(data, A, 32, Q(1, 2**20), primes)
    q = seed.denominator
    shift = seed.numerator*pow(16, A, q) % q
    shadow_residues = []
    for r in residues[:A]:
        shadow_residues.append(r*q+shift*D)
        shift = 16*shift % q
    cache = {}

    def local_phase(r):
        r %= p
        if r not in cache:
            cache[r] = phase(r, p)
        return cache[r]

    rows = []
    exact_checks = 0
    forcing_omission_rejections = 0
    for h in (1, 2, 3, 5):
        z = [phase(h*r, D) for r in residues]
        shadow = [phase(h*r, D*q) for r in shadow_residues]
        W = mean(z[:A])
        lags, gamma, marginals, full_means = [], [], [], []
        raw_lags = []
        for l in range(1, maximum):
            full = [z[n+l]*z[n].conjugate() for n in range(A)]
            short = mean(full[:A-l])*Box(Interval.ratio(A-l, A))
            k = h*(16**l-1)
            local = [local_phase(k*a) for a, _ in parts]
            cov, marginal = signed_transport(local, full)
            lags.append(short)
            gamma.append(cov)
            marginals.append(marginal)
            full_means.append(mean(full))
            raw_lags.append({'lag': l, 'frequency_hex': hex(k),
                             'local_frequency_zero': k % p == 0,
                             'truncated': short.as_dict(), 'full': full_means[-1].as_dict(),
                             'Gamma': cov.as_dict(), 'marginal_product': marginal.as_dict()})
            if l in (1, maximum//2, maximum-1):
                n = A+A//3
                F = sum((16**(l-j)*original_forcing(n+j) for j in range(1, l+1)), Q(0))
                u = Q(residues[n-A], D)
                later = Q(residues[n+l-A], D)
                assert (later-16**l*u-F).denominator == 1
                part = Q(*parts[n-A])
                v = k*(u-part)+h*F
                vbox = phase(v.numerator, v.denominator)
                lifted = full[n-A]*local[n-A].conjugate()
                assert lifted.re.overlaps(vbox.re) and lifted.im.overlaps(vbox.im)
                direct = phase(h*(residues[n+l-A]-residues[n-A]), D)
                assert direct.re.overlaps(full[n-A].re) and direct.im.overlaps(full[n-A].im)
                if (h*F).denominator != 1:
                    forcing_omission_rejections += 1
                exact_checks += 1
        apertures = []
        for H in menu:
            energy, unsigned = energy_from_lags(lags, H)
            direct = sliding_energy(z[:A], H)
            assert energy.overlaps(direct)
            vdC = energy*Interval.ratio(A+H-1, A)
            assert W.norm_squared().lo <= vdC.hi
            shadow_energy = sliding_energy(shadow, H)
            shadow_status = verdict(shadow_energy, 2, H)
            if H >= 4:
                assert shadow_status == 'REFUTED_FINITE'
            signed_cov, _ = energy_from_lags(gamma, H, ZERO)
            marginal_term, _ = energy_from_lags(marginals, H, ZERO)
            endpoint_term, _ = energy_from_lags([a-b for a, b in zip(full_means, lags)], H, ZERO)
            reconstructed = ONE.divide(H)+signed_cov+marginal_term-endpoint_term
            assert reconstructed.overlaps(energy)
            apertures.append({'H': H, 'energy': energy.as_list(), 'sliding_energy': direct.as_list(),
                              'signed_excess': (energy*Interval.ratio(H)-ONE).as_list(),
                              'unsigned_energy_bound': unsigned.as_list(), 'vdC_bound_squared': vdC.as_list(),
                              'SL2': verdict(energy, 2, H), 'shadow_energy': shadow_energy.as_list(),
                              'shadow_SL2': shadow_status, 'weighted_Gamma': signed_cov.as_list(),
                              'weighted_marginals': marginal_term.as_list(),
                              'weighted_deleted_endpoints': endpoint_term.as_list(),
                              'transport_reconstruction': reconstructed.as_list(),
                              'nonresonant_local_gate_eligible': H <= m and h % p != 0})
        rows.append({'h': h, 'W': W.as_dict(), 'shadow_W': mean(shadow).as_dict(),
                     'lags': raw_lags, 'apertures': apertures})
    assert forcing_omission_rejections > 0
    return {'A': A, 'p': p, 'm': m, 'epoch_gluing_l1': str(variation(A, p)),
            'source_last': data['last'], 'source_unwrapped_sha256': data['unwrapped_sha256'],
            'source_carry_sha256': data['carry_sha256'], 'source_denominator_bits': D.bit_length(),
            'independent_source_checks': 4, 'independent_phase_transport_checks': exact_checks,
            'forcing_omission_rejections': forcing_omission_rejections,
            'shadow': {'seed_numerator_hex': hex(seed.numerator), 'seed_denominator_hex': hex(q),
                       'K': 32, 'eta': '1/1048576', 'matched_primes': list(primes),
                       'literal_zero_authenticated': False, 'fixed_seed_across_epochs': False},
            'rows': rows, 'seconds': time.monotonic()-start}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stage', choices=('development', 'holdout', 'stress'), required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    epochs = {'development': (97, 193), 'holdout': (307, 613, 1229, 2459), 'stress': (4919,)}[args.stage]
    index = []
    for A in epochs:
        row = run(A)
        path = args.output/f'lag_{A}.json'
        path.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
        statuses = [ap['SL2'] for r in row['rows'] for ap in r['apertures']]
        index.append({'A': A, 'file': path.name, 'sha256': sha256(path.read_bytes()).hexdigest()})
        print(A, row['p'], row['m'], round(row['seconds'], 3),
              {s: statuses.count(s) for s in sorted(set(statuses))}, flush=True)
    paths = [HERE/'lag_instrument.py', HERE/'run_lag_probe.py', HERE/'PROTOCOL.md',
             PRIOR/'intervals.py', PRIOR/'source.py']
    receipt = {'stage': args.stage, 'scale': SCALE, 'protocol_commit': 'd613c66a',
               'epochs': index, 'hashes': {str(p.relative_to(HERE.parent)): sha256(p.read_bytes()).hexdigest() for p in paths},
               'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (args.output/f'{args.stage}.json').write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
