"""Replay the exact coherent-tail bulk certificate used by the regression test."""
import json
from fractions import Fraction
from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[3]
checks = runpy.run_path(str(root/'tests/test_signed_lag_fireworks_sharpness.py'))
result = checks['bulk_certificate']()
result['status'] = 'EXACT_FINITE_COHERENT_COUNTERSEED_BULK_CERTIFICATE'
result['seed'] = 'symbolic s*=-pi/16; not selected seed zero'
result['certified'] = result['norm_square_upper'] < result['analytic_upper']**2
result['limit_at_c_5_over_2'] = {'reduced_score': Fraction(24, 25),
                               'signed_transport_gap': Fraction(1, 25),
                               'status': 'PAPER_THEOREM_NOT_FINITE_EXTRAPOLATION'}
print(json.dumps(result, default=str, indent=2, sort_keys=True))
