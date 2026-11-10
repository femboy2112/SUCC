"""Refresh exact source-read and local artifact hashes after review."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    source_paths=(
        'AGENTS.md','docs/METHOD.md','observational_succ/selected_orbit.py',
        'research/2026-11-07/learning_yoneda/arithmetic/THEOREMS.md',
        'research/2026-11-07/learning_yoneda/arithmetic/PRIME_EPOCH_THEOREM.md',
        'research/2026-11-07/learning_yoneda/arithmetic/finite_adelic.py',
        'research/2026-11-07/learning_yoneda/arithmetic/EXTERNAL_SOURCE_AUDIT.json',
        'research/2026-11-08/covariance_forge/spectral/THEOREMS.md',
    )
    sources=[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'scope':'pinned current worktree source'}
             for p in source_paths]
    old_pin='f6560d9378b76ec4bca2e8b2bfbef591e0020fa3'
    old_path='research/2026-11-06/prime_frobenius_spectral/THEOREMS.md'
    data=subprocess.check_output(['git','show',f'{old_pin}:{old_path}'],cwd=ROOT)
    sources.append({'commit':old_pin,'path':old_path,'sha256':sha(data),
                    'scope':'read PF01--PF04; source-forced prime product and valuations'})
    result={'read_scope':'actual local proofs/code plus pinned PR532 proof, not PR descriptions',
            'research_baseline':'47ec1ccf9d3579897abb94c047f3b4dc13b4cb70',
            'sources':sources,
            'external_imports':[
                {'name':'PNT and PNT in fixed arithmetic progression',
                 'url':'https://kskedlaya.org/ant/chap-primes-in-ap.html',
                 'theorem':'4.12','status':'classical imported; primary reference checked by root in prior round'},
                {'name':'Bourgain--Konyagin 2003',
                 'url':'https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf',
                 'theorem':'2.1, printed page78',
                 'sha256':'2d87a571d068007f2d6ed2657beb4e37d4dab56e858b2128852a70077dfa7fb6',
                 'status':'via pinned PE theorem; primary PDF visually checked by root in prior round'}]}
    (HERE/'SOURCE_READ_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
    artifacts={p.name:sha(p.read_bytes()) for p in sorted(HERE.iterdir())
               if p.is_file() and p.name!='ARTIFACT_HASHES.json'}
    (HERE/'ARTIFACT_HASHES.json').write_text(json.dumps(artifacts,indent=2)+'\n')
    print(f'Hashed {len(sources)} source records and {len(artifacts)} local artifacts.')


if __name__=='__main__':
    main()
