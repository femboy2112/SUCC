#!/usr/bin/env python3
"""Replay exact swarm receipts. This verifies finite computations, not paper proofs."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
# Source-qualified: many-worlds-swarm (#50) is a parallel assembly of the same
# swarm; the atlas (#49) is canonical in SWARM_ATLAS. These probes reproduce the
# #50 receipts, kept distinct here so they do not collide with the atlas receipts.
ATLAS = ROOT / 'research/2026-10-13/MW_SWARM_RECEIPTS'
PAIRS = (
    ('swarm_categories_probe.py', 'A_CATEGORIES_RECEIPT.json'),
    ('swarm_completion_probe.py', 'B_COMPLETION_RECEIPT.json'),
    ('swarm_probability_probe.py', 'SWARM_PROBABILITY_RECEIPT.json'),
    ('swarm_dynamics_probe.py', 'D_RECEIPT.json'),
    ('swarm_arithmetic_probe.py', 'ARITHMETIC_RECEIPT.json'),
    ('swarm_f_probe.py', 'F_EXACT_RECEIPT.json'),
    ('swarm_x01_completion_transport_probe.py', 'X01_RECEIPT.json'),
    ('swarm_x02_probe.py', 'X02_RECEIPT.json'),
    ('swarm_x03_probe.py', 'X03_RECEIPT.json'),
    ('swarm_x04_probe.py', 'X04_RECEIPT.json'),
    ('swarm_x05_probe.py', 'X05_RECEIPT.json'),
    ('swarm_x06_probe.py', 'X06_RECEIPT.json'),
    ('swarm_cross_x07_probe.py', 'X07_RECEIPT.json'),
    ('swarm_x08_probe.py', 'X08_RECEIPT.json'),
    ('swarm_cross09_probe.py', 'X09_RECEIPT.json'),
    ('swarm_cross_x10_probe.py', 'X10_RECEIPT.json'),
    ('swarm_x11_proof_limits_probe.py', 'X11_RECEIPT.json'),
    ('swarm_x12_probe.py', 'X12_RECEIPT.json'),
)


def main():
    for script, receipt in PAIRS:
        result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script)],
                                cwd=ROOT, text=True, capture_output=True, check=True)
        actual = json.loads(result.stdout)
        expected = json.loads((ATLAS / receipt).read_text())
        if actual != expected:
            changed = sorted(k for k in actual.keys() | expected.keys()
                             if actual.get(k) != expected.get(k))
            raise SystemExit(f'{receipt}: drift in {changed}')
        print(f'PASS {receipt}', flush=True)
    print(f'{len(PAIRS)} exact receipts reproduced; no paper-proof promotion.')


if __name__ == '__main__':
    main()
