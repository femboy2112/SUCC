"""Hash this front and the exact read-only mathematical inputs."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    local_sources=[
        'AGENTS.md','docs/METHOD.md',
        'research/2026-10-30/codex_finite_band_crt/CODEX_ASTRA_ULTRA_MEGA_ROUND.md',
        'research/2026-10-30/codex_finite_band_crt/FINITE_BAND_CERTIFICATE.md',
        'research/2026-10-30/codex_finite_band_crt/finite_band.py',
        'research/2026-10-30/codex_finite_band_crt/test_finite_band.py',
        'research/2026-10-30/codex_finite_band_crt/independent_oracle.py',
        'research/2026-10-30/cylinder_tiling_collision/THEOREMS.md',
        'research/2026-10-30/zero_boundary_dispersion/CYLINDER_UNION.md',
        'research/2026-10-30/zero_boundary_dispersion/cylinder_union.py',
        'research/2026-10-30/zero_boundary_dispersion/run_receipt.py',
    ]
    sources=[dict(path=p,sha256=digest((ROOT/p).read_bytes()),kind='inherited_file') for p in local_sources]
    commit='2d4fcc6db5657a2559b0e28ca8c8e1413b6c4548'
    for p in ('research/2026-10-30/frame_reset_crucible/RESEARCH.md',
              'research/2026-10-30/frame_reset_crucible/frame_reset.py'):
        data=subprocess.check_output(['git','show',commit+':'+p],cwd=ROOT)
        sources.append(dict(path=p,commit=commit,sha256=digest(data),kind='read_only_git_source'))
    # Cross-agent exact reviewed hashes remain in their dated receipts rather
    # than pretending a later live edit was covered by an earlier review.
    artifacts=[]
    for p in sorted(HERE.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.name!='SOURCE_MANIFEST.json':
            artifacts.append(dict(path=str(p.relative_to(ROOT)),sha256=digest(p.read_bytes())))
    payload=dict(parent_head='fa598e3a5a1111c3445200f1ddf48dcdea6bdc09',
                 artifacts=artifacts,sources=sources,
                 external_reference=dict(title='Bailey and Crandall, Random Generators and Normal Numbers (2002)',
                   url='https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf',
                   use='classical provenance; local Stoneham proof is self-contained',
                   checked_utc_date='2026-10-30'),
                 authority='paper proofs and finite implementations, same-model complementary checks; no external referee')
    (HERE/'SOURCE_MANIFEST.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(dict(artifact_count=len(artifacts),source_count=len(sources),
                         dossier_sha256=digest((HERE/'CYLINDERS_AND_STONEHAM.md').read_bytes()))))


if __name__=='__main__':
    main()
