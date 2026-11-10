"""Verify or deliberately regenerate the round's artifact hashes."""
import argparse
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
MANIFEST=HERE/'ARTIFACT_MANIFEST.json'


def current():
    return {str(p.relative_to(HERE)):sha256(p.read_bytes()).hexdigest()
            for p in sorted(HERE.rglob('*')) if p.is_file() and p!=MANIFEST
            and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.pyo')}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true')
    args=ap.parse_args();data=current()
    if args.write:
        MANIFEST.write_text(json.dumps({'algorithm':'sha256','files':data},indent=2,sort_keys=True)+'\n')
    else:
        expected=json.loads(MANIFEST.read_text())['files']
        if data!=expected:
            changed=sorted(k for k in set(data)|set(expected) if data.get(k)!=expected.get(k))
            raise SystemExit('artifact mismatch: '+', '.join(changed))
    print(len(data),'artifact hashes verified' if not args.write else 'artifact hashes written')
