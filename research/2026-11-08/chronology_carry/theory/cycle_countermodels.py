"""Exact periodic carry contrasts from the earlier frozen training table only."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json

from carry_control import occupation_identity


def run(table_path):
    table_path = Path(table_path)
    data = json.loads(table_path.read_text())
    scale = 1 << data['table_bits']
    out = {'table_sha256': sha256(table_path.read_bytes()).hexdigest(),
           'input_scope': 'frozen earlier training table only; no holdout source data read',
           'examples': []}
    for h in [1, 3]:
        for menu, depth in [('one', 1), ('two', 2)]:
            rows = data['tables'][str(h)][menu]
            table = {tuple(map(int, key.split(','))): tuple(Q(z, scale) for z in row['center'])
                     for key, row in rows.items()}
            mu = tuple(sum(z[i] for z in table.values()) / len(table) for i in [0, 1])
            candidates = []
            for digit in range(1, 15):
                word = (digit,) * depth
                result = occupation_identity(table, [word] * 4, 16, depth)
                assert result['boundary'] == (0, 0)
                contrast = result['innovation']
                assert contrast == tuple(table[word][i] - mu[i] for i in [0, 1])
                candidates.append((sum(z*z for z in contrast), digit, table[word], contrast))
            norm, digit, value, contrast = max(candidates)
            assert norm > (Q(1, 100) if depth == 1 else Q(4, 25))
            assert sum(z*z for z in value) < Q(1, 4)
            encode = lambda z: [str(v) for v in z]
            out['examples'].append({
                'h': h, 'menu': menu, 'depth': depth, 'constant_digit': digit,
                'completed_fixed_point': str(Q(digit, 15)),
                'reference_mean': encode(mu), 'cycle_model_mean': encode(value),
                'innovation_limit': encode(contrast), 'innovation_squared_exact': str(norm),
                'innovation_modulus_diagnostic': float(norm)**0.5,
                'residual_mean_modulus_limit_lower': '1/2',
            })
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    parser.add_argument('--table', type=Path, default=here.parent/'model/FROZEN_TABLE.json')
    parser.add_argument('--output', type=Path, default=here/'CYCLE_COUNTERMODELS.json')
    args = parser.parse_args()
    result = run(args.table)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'constant_cycle_cases': 56, 'published_examples': 4,
                      'all_exact_contrast_checks': 'PASS', 'holdout_read': False}))
