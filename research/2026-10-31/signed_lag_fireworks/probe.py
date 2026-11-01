"""Deterministic exact probe; writes JSON only after all asserted checks pass."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from interval_oracle import circle_states, score_from_states
from transport import certificate, weighted_error


def valuation(k, p):
    v = 0
    while k % p == 0:
        v += 1
        k //= p
    return v


def stoneham_states(c, N, K):
    """Finite sum plus certified tail for the INFINITE normal control."""
    exponent = c
    partial = F(0)
    while exponent < N+K+32:
        partial += F(1, exponent*16**exponent)
        exponent *= c
    # sum_(ell>=j) c^-ell = c/[(c-1)c^j]; all exponents >= c^j.
    tail = F(c, (c-1)*exponent*16**exponent)
    U = [partial % 1]
    for _ in range(N):
        U.append((16*U[-1]) % 1)
    # Every reduced phase perturbation <= |h|16**(N+K)*tail.
    return U, F(44, 7)*16**(N+K)*tail


def run():
    rows = []
    known = {
        512: (F('-620250446467/163840000000000'), F('-7753130579303/2048000000000000')),
        1024: (F('-37498145618503/4096000000000000'), F('-14999258246173/1638400000000000')),
        1536: (F('-1446341069911/192000000000000'), F('-92565828465091/12288000000000000')),
    }
    cases = [(N, 4, 1, 'parent interval replay') for N in known]
    cases += [(N, K, h, 'fresh time and harmonic')
              for N, K in ((769, 4), (2048, 5), (4096, 6)) for h in (3, 5, 7, 11)]
    cases += [(1024, 17, h, 'deep conductor classes; transport may be vacuous') for h in (3, 11)]
    states = {}
    for N, K, h, role in cases:
        start = time.monotonic()
        if N not in states:
            states[N] = circle_states(N)
        score, lag_rows = score_from_states(states[N], K, h)
        if role == 'parent interval replay':
            a, b = known[N]
            assert max(a, score[0]) <= min(b, score[1]), (N, score, known[N])
        for lag in lag_rows:
            lag['v3_conductor'] = 1+valuation(lag['k'], 3)
            lag['v5_conductor'] = 1+valuation(lag['k'], 5)
        rows.append({'source': 'original signed four-pole BBP; literal U0=0',
                     'N': N, 'K': K, 'h': h, 'role': role,
                     'score': list(map(str, score)),
                     'new_transport_error': str(weighted_error(N, K, h)),
                     'weyl_squared_upper': str(certificate(N, K, h, score)),
                     'lags': lag_rows,
                     'runtime_seconds': round(time.monotonic()-start, 3)})
    for c in (3, 5):
        N, K = 256, 4
        U, tail = stoneham_states(c, N, K)
        for h in (1, 3, 5):
            (a, b), lags = score_from_states(U, K, h)
            error = abs(h)*tail  # total positive weight <1
            rows.append({'source': f'infinite Stoneham alpha_(16,{c})',
                         'source_contract': 'different source; classical normal control',
                         'N': N, 'K': K, 'h': h,
                         'score': [str(a-error), str(b+error)],
                         'infinite_series_score_error': str(error), 'lags': lags})
    files = ('interval_oracle.py', 'transport.py', 'probe.py')
    return {'status': 'FINITE EXACT INTERVALS; pi normality OPEN',
            'baseline': '030ee84b8b7f655fcf433375bfc0b347e0483c89',
            'source_sha256': {f: hashlib.sha256(Path(__file__).with_name(f).read_bytes()).hexdigest() for f in files},
            'rows': rows}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = run()
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    print(f'PASS: {len(data["rows"])} exact interval rows written to {args.output}')
