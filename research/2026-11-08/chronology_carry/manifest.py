"""Hash this round's durable artifacts, including compressed raw source data."""
import argparse
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
MANIFEST=HERE/'ARTIFACT_MANIFEST.json'


def actual():
    return {str(p.relative_to(HERE)):{'sha256':sha256(p.read_bytes()).hexdigest(),
                                    'bytes':p.stat().st_size}
            for p in sorted(HERE.rglob('*'))
            if p.is_file() and p!=MANIFEST and '__pycache__' not in p.parts
            and p.suffix not in ('.pyc','.olean')}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true')
    args=ap.parse_args();files=actual()
    if args.write:MANIFEST.write_text(json.dumps({'files':files},indent=2,sort_keys=True)+'\n')
    else:assert json.loads(MANIFEST.read_text())['files']==files
    print('verified',len(files),'artifact hashes')


if __name__=='__main__':main()
