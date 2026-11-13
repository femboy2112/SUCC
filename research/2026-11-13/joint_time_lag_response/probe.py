"""Replay the preregistered finite joint-field shells, saving exact enclosures."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

from observational_succ.duck_bbp import forcing
from observational_succ.joint_time_lag import (
    authentic_circle_path, source_shell_certificate, inverse_lag_certificate,
)
from observational_succ.oily_signed_certificate import Interval


def encode(value):
    if isinstance(value, Interval):
        return [str(value.lower), str(value.upper)]
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def main():
    rows = []
    for role, starts, lengths in (
            ('development', (16, 32, 64), (2, 4, 8)),
            ('held_out', (97, 193, 389), (3, 11, 31))):
        for start in starts:
            for h in (1, 2, 15):
                for length in lengths:
                    result = source_shell_certificate(start, length, h)
                    result['role'] = role
                    rows.append(result)
            print(f'completed {role} shell B={start}', flush=True)
    path = authentic_circle_path(2*389-1)
    for n in range(1, len(path)):
        independent = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        assert independent == forcing(n)
        assert path[n] == (16*path[n-1]+independent) % 1
    inverse = []
    eps = Q(1, 32)
    for n in (1, 2, 7, 19):
        for k in range(15):
            result = inverse_lag_certificate(Q(k, 15)+eps/(30*16**(n-1)), n, eps)
            inverse.append({'N': n, 'expected_alias': k, **result})
    output = {'scope': 'Exact finite certificates; no asymptotic inference',
              'source': 'Literal four-pole BBP, U_0=0',
              'baseline': 'db9fb4b84672050efa79b13377f1e73364598a14',
              'rows': rows, 'inverse_controls': inverse,
              'independent_source_steps_checked': len(path)-1,
              'calibration_history': [{
                  'initial_test': 'First circle phase rejects sign flip of -2/(8n-4)',
                  'verdict': 'REFUTED at n=1: the mutation adds exactly 1',
                  'repair': 'Retain integer alias; test unwrapped forcing and a noninteger sign mutation',
                  'theorem_or_source_code_changed': False}],
              'pi_normality': 'OPEN', 'R0': 'OPEN'}
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('RESULTS.json')
    target.write_text(json.dumps(encode(output), indent=2)+'\n')
    print(f'saved {len(rows)} source certificates and {len(inverse)} inverse controls')


if __name__ == '__main__':
    main()
