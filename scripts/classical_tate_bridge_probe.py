#!/usr/bin/env python3
"""Recompute actual committed finite Tate/Gamma/Euler probes, never RH."""
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from observational_succ.classical_tate_window import classical_tate_window_probe
from observational_succ.classical_tate_arch_global import arch_global_probe


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',action='store_true')
    opt=p.parse_args()
    actual={'kind':'CLASSICAL_TATE_SCHWARTZ_VERIFIED_BRIDGE_RECEIPT',
            'finite_atlas':classical_tate_window_probe(),
            'arch_global':arch_global_probe(),
            'local_Fourier_implemented_on_fixed_a_b_test_window':True,
            'unrestricted_source_unknown_support_or_precision_certified':False,
            'global_adelic_Poisson_deduced_from_finite_examples':False,
            'signed_Weil_positivity_or_RH_proved':False}
    path=ROOT/'research/2026-10-15/CLASSICAL_TATE_SCHWARTZ_RECEIPT.json'
    if opt.verify:
        if actual!=json.loads(path.read_text(encoding='utf-8')):
            raise SystemExit('CLASSICAL_TATE_SCHWARTZ RECEIPT DRIFT')
        print('Classical Tate: source/Gamma/Euler exact receipt verified')
    else:print(json.dumps(actual,indent=2,sort_keys=True))
if __name__=='__main__':main()
