"""Replay exact finite receipts. Generation is opt-in; verification is read-only."""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

import hannibal as h

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


wm = load('hannibal_wm', HERE.parent/'weyl_mirror_campaign/weyl_mirror.py')
msa = load('hannibal_msa', HERE.parent/'mesoscopic_spectral_army/mesoscopic.py')


def ratio(x):
    return [x.numerator, x.denominator]


def bounded_cost(x):
    return {'interval':wm.rational_interval(x),
            'numerator_sha256':h.digest_integer(x.numerator),
            'denominator_sha256':h.digest_integer(x.denominator)}


def small():
    last = 12288
    states, carries = [], bytearray()
    for n, a, den, carry in h.full_source(last):
        if n:
            states.append(a)
            carries.append(carry)
    od, odd = wm.odd_modular_lift(384)
    fractions = h.phases(384)
    full = list(msa.original_modular_lift(384))[1:]
    assert fractions == [F(x, od) for x in odd]
    assert fractions == [F(x, d) for _, x, d in full]
    assert fractions == [F(x, den) for x in states[:384]]
    development = []
    for j in range(1, 13):
        A = 1 << j
        counts, E = wm.energy(states[A-1:2*A-1], den, h.slow_mesh(A))
        _, cap = h.iid_ceiling(counts)
        development.append({'A':A, 'mesh':len(counts), 'counts':counts,
                            'energy':ratio(E), 'iid_mean_ceiling':ratio(cap),
                            'candidate_pass':E <= cap})
    W = wm.mirror_wasserstein(states, den)
    matching = {}
    for frequency in (7,17,255,256):
        cost = wm.antiphase_matching_cost(states, den, frequency)
        row = bounded_cost(cost)
        ordered = sorted(((frequency*a)%den, n) for n,a in enumerate(states,1))
        permutation = [0]*last
        for i,(_,n) in enumerate(ordered):
            permutation[n-1] = ordered[(i+last//2)%last][1]
        assert sorted(permutation) == list(range(1,last+1))
        assert all(permutation[permutation[n]-1] == n+1 for n in range(last))
        row['permutation_sha256_u32_big_endian'] = sha256(
            b''.join(n.to_bytes(4,'big') for n in permutation)).hexdigest()
        row['coverage'] = last
        row['unmatched_mass'] = 0
        interval = row['interval']
        upper = F(interval['upper_numerator'],interval['denominator'])
        row['normalized_weyl_ceiling_rational'] = ratio(min(F(1),F(22,7)*upper))
        matching[str(frequency)] = row
    result = {'source':'all four original poles; literal U0=0',
              'status':'FINITE EXACT OBSERVATIONS; no asymptotic inference',
              'last':last, 'modulus_bits':den.bit_length(),
              'modulus_sha256':h.digest_integer(den),
              'literal_carry_sha256':sha256(carries).hexdigest(),
              'oracle_agreement_length':384, 'development_iid_candidate':development,
              'mirror_W1':bounded_cost(W), 'matching_costs':matching}
    # Independent O(A^2) Fraction pair enumeration; no trig/float comparisons.
    annuli = []
    A = 512
    epoch = states[A-1:2*A-1]
    for m in (64,256):
        row = h.annulus_census(epoch, den, A, m)
        # Use reduced fractions from a separate literal recurrence.
        fp = h.phases(2*A-1)[A-1:]
        oracle = h.exact_pair_oracle(fp, m)
        assert oracle == (row['ordered_near'], row['ordered_strict_inner'],
                          row['ordered_shell'])
        assert not row['violations']
        assert row['ordered_shell'] <= row['ordered_shell_ceiling']
        assert all(r['shell'] <= r['shell_ceiling'] and
                   r['near'] <= r['near_ceiling'] for r in row['lags'])
        annuli.append(row)
    witnesses = [h.witness_packets(states, den, A, m)
                 for A in (128,256) for m in (256,4096)]
    return {'FINITE_RECEIPT.json':result,
            'ANNULUS_RECEIPT.json':annuli, 'WITNESS_RECEIPT.json':witnesses}


def large():
    epochs = (16384,65536)
    counts = {A:{m:[0]*m for m in (h.slow_mesh(A),64,256)} for A in epochs}
    carries = sha256()
    for n, a, den, carry in h.full_source(2*max(epochs)-1):
        if not n:
            modulus_bits = den.bit_length()
            modulus_hash = h.digest_integer(den)
            continue
        carries.update(bytes([carry]))
        A = 1 << (n.bit_length()-1)
        if A in counts:
            for m, vector in counts[A].items():
                vector[m*a//den] += 1
    rows = []
    for A, meshes in counts.items():
        for m, vector in meshes.items():
            assert sum(vector) == A
            E, cap = h.iid_ceiling(vector)
            rows.append({'A':A, 'mesh':m, 'is_slow_mesh':m == h.slow_mesh(A),
                         'counts':vector, 'energy':ratio(E),
                         'declared_finite_threshold_9_over_8_pass':E < F(9,8),
                         'iid_mean_ceiling':ratio(cap), 'iid_candidate_pass':E <= cap})
    return {'LARGE_RECEIPT.json':{'source':'original four poles; U0=0',
            'status':'FINITE EXACT HISTOGRAMS; no universal energy bound',
            'last':2*max(epochs)-1, 'modulus_bits':modulus_bits,
            'modulus_sha256':modulus_hash, 'literal_carry_sha256':carries.hexdigest(),
            'epochs':rows}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--large', action='store_true')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--verify', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()
    output = large() if args.large else small()
    for name, data in output.items():
        path = HERE/name
        if args.verify:
            assert json.loads(path.read_text()) == data, name
            print(name+': exact replay PASS', flush=True)
        else:
            if path.exists():
                raise FileExistsError('refusing to overwrite an existing receipt: '+name)
            path.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
            print(name+': written', flush=True)
