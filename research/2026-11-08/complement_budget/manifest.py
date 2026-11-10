"""Write or verify the complete dossier artifact manifest (excluding itself)."""
import argparse
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
TARGET=HERE/'ARTIFACT_MANIFEST.json'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    files={str(p.relative_to(HERE)):sha256(p.read_bytes()).hexdigest()
           for p in sorted(HERE.rglob('*')) if p.is_file() and p!=TARGET
           and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    payload={'scope':'Every dossier file except this manifest and Python caches',
             'count':len(files),'sha256':files}
    if args.write:TARGET.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    else:
        if json.loads(TARGET.read_text())!=payload:
            raise SystemExit('manifest mismatch')
    print(len(files),'artifact hashes','written' if args.write else 'verified')


if __name__=='__main__':main()
