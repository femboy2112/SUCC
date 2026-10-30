"""Pin inherited source bytes, refreshed ancestry and read-only sibling inputs."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='7b5a2b4534aa5e71865046ca8d3f723d8002b9fe'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)

def run():
    inputs=[]
    paths=['AGENTS.md','docs/METHOD.md','provenance/IMPORT_MANIFEST.json',
           'research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md',
           'research/2026-10-29/oily_triangle_sheet/PASCAL_GOLDEN_HARMONIC.md',
           'research/2026-10-30/triangle_fabric/README.md',
           'research/2026-10-30/triangle_fabric/constants/CONSTANTS_AND_COMPOSITION.md',
           'research/2026-10-30/triangle_fabric/category/CATEGORICAL_ARROWS.md',
           'research/2026-10-30/triangle_fabric/signed/SIGNED_FABRIC.md',
           'research/2026-10-30/triangle_fabric/period_preserving/PERIOD_FIBERS.md',
           'research/2026-10-30/triangle_fabric/NEXT_HANDOFF.md',
           'research/2026-10-30/zero_boundary_dispersion/README.md',
           'observational_succ/bbp_source_memory.py']
    for path in paths:
        raw=git('show',BASE+':'+path)
        assert raw==(ROOT/path).read_bytes(),path
        inputs.append({'path':path,'commit':BASE,'sha256':hashlib.sha256(raw).hexdigest()})
    for sha,path in [('5f05181339ea97a56999ca8b8ab10a2009c6c84d','research/2026-10-30/cylinder_tiling_collision/THEOREMS.md'),
                     ('992b3f9d77f1016300f1daf7db3c88da7392269b','research/2026-10-30/fibonacci_epicycle_demon/RESEARCH.md')]:
        raw=git('show',sha+':'+path)
        inputs.append({'path':path,'commit':sha,'sha256':hashlib.sha256(raw).hexdigest(),
                       'type':'read-only sibling; not merged'})
    old=HERE.parent/'triangle_fabric'
    manifest=json.loads((old/'SOURCE_MANIFEST.json').read_text())
    records=manifest['files']
    for path,item in records.items():
        raw=(old/path).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],path
        assert raw==git('show',BASE+':'+(old/path).relative_to(ROOT).as_posix()),path
    ancestry=[]
    first=json.loads((HERE/'receipts/live_refs_initial.json').read_text())['prs']
    other=json.loads((HERE/'receipts/related_refs.json').read_text())['prs']
    for row in first+other:
        subprocess.run(['git','merge-base','--is-ancestor',row['base_sha'],row['head_sha']],cwd=ROOT,check=True)
        ancestry.append({'pr':row['pr'],'head':row['head_sha'],'base':row['base_sha'],'ancestor':True})
    return {'status':'PASS','base':BASE,'inputs':inputs,'ancestry':ancestry,
            'parent_artifacts_unchanged':len(records),'python':sys.version,
            'branch':git('branch','--show-current').decode().strip()}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
