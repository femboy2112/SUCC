"""Generate local front provenance; intentional overwrite only for this manifest."""
import hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
repo=root.parents[3]
BASE='6cf5050ff2cfd92e7a0c8876da5233be6ff117f5'
inputs=[
'AGENTS.md','provenance/IMPORT_MANIFEST.json',
'research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md',
'research/2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md',
'research/2026-10-29/triangular_harmonic_gamma_bbp/TRIANGULAR_HARMONIC_GAMMA_BBP.md',
'research/2026-10-29/oily_triangle_sheet/PASCAL_GOLDEN_HARMONIC.md',
'research/2026-10-29/cototient_pascal_gamma/COTOTIENT_GAMMA_TRIANGLE.md',
'research/2026-10-30/gamma_twist/geometry/GEOMETRY_DOSSIER.md',
'research/2026-10-30/zero_boundary_dispersion/spectral/SPECTRAL_DOSSIER.md',
'research/2026-10-25/GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=[]
for p in inputs:
    disk=repo/p
    old=subprocess.check_output(['git','show',f'{BASE}:{p}'],cwd=repo)
    assert disk.read_bytes()==old
    source.append({'path':p,'sha256':sha(disk),'git_blob':subprocess.check_output(
        ['git','rev-parse',f'{BASE}:{p}'],cwd=repo,text=True).strip()})
artifacts=[{'path':str(p.relative_to(root)),'sha256':sha(p),'bytes':p.stat().st_size}
           for p in sorted(root.rglob('*')) if p.is_file()
           and '__pycache__' not in p.parts and p.name!='SOURCE_MANIFEST.json']
record={'base_commit':BASE,'source_inputs':source,'artifacts':artifacts,
        'external_primary_sources':['https://dlmf.nist.gov/5.4','https://dlmf.nist.gov/5.5',
            'https://dlmf.nist.gov/5.9','https://dlmf.nist.gov/5.12'],
        'authority':'source and byte provenance; not semantic proof certification'}
(root/'SOURCE_MANIFEST.json').write_text(json.dumps(record,indent=2)+'\n')
print(f'MANIFEST {len(source)} source inputs, {len(artifacts)} artifacts')
