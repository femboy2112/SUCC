"""Preregistered causal carry-memory certificates on the authentic source."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys
import time
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from intervals import SCALE, BITS, phase, mean
from source import principal_pair
from prime_epochs import good_prime
from history_certificate import authenticate_history, certificate
from observational_succ.selected_orbit import original_forcing


def run(A):
    started = time.monotonic()
    p = good_prime(A)
    states = [Q(0)]
    carries = [0]
    digest = sha256()
    for n in range(1, 2*A):
        u = 16*states[-1]+original_forcing(n)
        carries.append(u//1-16*(states[-1]//1))
        states.append(u)
        digest.update(f'{u.numerator:x}/{u.denominator:x}\n'.encode())
    authenticate_history(states)
    rows = []
    for h in (1, 2, 3, 5):
        a, b, full = [], [], []
        for u in states[A:]:
            an, ad = principal_pair(u.numerator, u.denominator, p)
            a.append(phase(h*an, ad))
            b.append(phase(h*(u.numerator*ad-an*u.denominator), u.denominator*ad))
            full.append(phase(h*u.numerator, u.denominator))
        models = []
        for memory in (0, 1, 2, 3):
            labels = [tuple(carries[n-memory+1:n+1]) if memory else () for n in range(A, 2*A)]
            models.append(dict(memory=memory, **certificate(a, b, labels)))
        singleton = certificate(a, b, list(range(A)))
        lo = min(m['full_bound_expression'][0] for m in models)
        hi = min(m['full_bound_expression'][1] for m in models)
        verdict = 'REFUTED_FINITE' if lo > SCALE//2 else 'PASS_FINITE' if hi <= SCALE//2 else 'INCONCLUSIVE'
        rows.append({'h': h, 'W': mean(full).as_dict(), 'models': models,
                     'singleton': singleton, 'best_menu_bound_expression': [lo, hi], 'H_half_status': verdict})
    return {'A': A, 'p': p, 'source_authenticated': True, 'unwrapped_fraction_sha256': digest.hexdigest(),
            'rows': rows, 'seconds': time.monotonic()-started}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    index = []
    for A in (383, 769, 1543):
        row = run(A)
        path = args.output/f'history_{A}.json'
        path.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
        index.append({'A': A, 'file': path.name, 'sha256': sha256(path.read_bytes()).hexdigest()})
        print(A, row['p'], round(row['seconds'], 3), [r['H_half_status'] for r in row['rows']], flush=True)
    files = ('history_certificate.py', 'run_history_probe.py', 'HISTORY_PREREGISTRATION.md')
    result = {'scale': SCALE, 'bits': BITS, 'preregistration_commit': '0d0d57a9', 'epochs': index,
              'hashes': {f: sha256((HERE/f).read_bytes()).hexdigest() for f in files},
              'pi_normality': 'OPEN', 'RH': 'OPEN'}
    (args.output/'history_probe.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
