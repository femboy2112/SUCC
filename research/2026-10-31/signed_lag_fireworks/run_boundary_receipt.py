"""Print reproducible exact finite boundary witnesses as JSON."""
from fractions import Fraction
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import boundary


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


result = {
    'status': 'EXACT_FINITE_CONTROLS_NOT_NORMALITY_PROOF',
    'source_parent': '030ee84b8b7f655fcf433375bfc0b347e0483c89',
    'seed_definition': 'symbolic irrational s=q-pi/16; q is rational',
    'source_selected_seed': '0',
    'shadows': [],
    'remainder_mutant_counterexample': {
        'z': [[1, 0], [1, 0]], 'N': 2, 'K': 3, 'm': 2,
        'B_K': boundary.window_energy(((1, 0), (1, 0)), 3),
        'mutant_without_remainder': Fraction(2, 3)*boundary.window_energy(((1, 0), (1, 0)), 2)
    }
}
for M in (8, 32, 512):
    data = boundary.dyadic_shadow(M)
    data['prefix_weyl_error_upper_h1'] = boundary.shadow_prefix_weyl_error_upper(M)
    data['prefix_lag_error_upper_h11_K4'] = boundary.shadow_lag_error_upper(M, M, 4, 11)
    data['completed_orbit_integral_at_start'] = (16**data['coherence_start']*data['q']).denominator == 1
    data['critical_lag_lower_at_N_16pow7_h1'] = boundary.shadow_lag_lower(16**7, 7, 1, M)
    result['shadows'].append(data)
print(json.dumps(result, default=encode, indent=2, sort_keys=True))
