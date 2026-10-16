#!/usr/bin/env python3
"""Build and audit an OPEN source tail packet. This does not certify a tail rate."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.source_proof_certificate import evidence_file
from observational_succ.spectral_tail_contract import make_open_tail_packet, audit_tail_packet


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    capsules = json.loads((ROOT/'research/2026-10-16/OBSERVER_SCHUR_CAPSULES.json').read_text())
    evidence = [evidence_file(ROOT, 'research/2026-10-16/'+name, 'PAPER_SOURCE_APPLICATION')
                for name in ('SPECTRAL_RESPONSE_MEASURE.md', 'FRACTIONAL_SOURCE_RANGE_AUDIT.md',
                             'AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md')]
    packet = make_open_tail_packet(capsules, evidence)
    result = {'packet': packet, 'audit': audit_tail_packet(packet, ROOT)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('Source tail contract retained OPEN:', args.output)


if __name__ == '__main__':
    main()
