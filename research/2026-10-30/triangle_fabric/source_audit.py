"""Verify inherited source bytes and exact sibling ancestry without editing them."""
from pathlib import Path
import hashlib, json, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='6cf5050ff2cfd92e7a0c8876da5233be6ff117f5'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def run():
    counts={}
    for folder,key in [('prime_stroboscope','source_files'),('arithmetic_barrier','files'),
        ('gamma_all_places','files'),('gamma_twist','files'),
        ('selected_boundary_slip','sha256_files'),('zero_boundary_dispersion','files')]:
        parent=HERE.parent/folder
        records=json.loads((parent/'SOURCE_MANIFEST.json').read_text())[key]
        if isinstance(records,list):records={r['path']:r for r in records}
        for name,entry in records.items():
            path=parent/name;raw=path.read_bytes()
            assert hashlib.sha256(raw).hexdigest()==entry['sha256'],str(path)
            assert raw==git('show',BASE+':'+path.relative_to(ROOT).as_posix()),str(path)
        counts[folder]=len(records)
    remote=json.loads((HERE/'receipts/initial_remote.json').read_text())
    ancestry=[]
    for p in remote['prs']:
        subprocess.run(['git','merge-base','--is-ancestor',p['base_sha'],p['head_sha']],cwd=ROOT,check=True)
        ancestry.append({'pr':p['pr'],'head':p['head_sha'],'base':p['base_sha'],'ancestor':True})
    names=['AGENTS.md','docs/METHOD.md','provenance/IMPORT_MANIFEST.json',
       'docs/OPERATIONAL_TRIANGLE.md','docs/PI_SELECTED_CATEGORICAL_FRONTIER.md',
       'research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md',
       'research/2026-10-25/GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md',
       'observational_succ/duck_bbp_fourier.py','observational_succ/bbp_source_memory.py',
       'research/2026-10-30/zero_boundary_dispersion/NEXT_HANDOFF.md']
    sources=[]
    for path in names:
        raw=(ROOT/path).read_bytes();assert raw==git('show',BASE+':'+path)
        sources.append({'path':path,'commit':BASE,'sha256':hashlib.sha256(raw).hexdigest(),
                        'blob':git('rev-parse',BASE+':'+path).decode().strip()})
    for sha,path in [('419cf7c280e7be11542ecbd6edef6c70fa7050e5','research/2026-10-30/noether_radix_ward/NOETHER_RADIX_WARD.md'),
                     ('ba66c2e4217d1d6eec407b142ed467c48e39ed1c','research/2026-10-30/count_out/COUNTING_QUOTIENT.md')]:
        raw=git('show',sha+':'+path)
        sources.append({'path':path,'commit':sha,'sha256':hashlib.sha256(raw).hexdigest(),
                        'blob':git('rev-parse',sha+':'+path).decode().strip(),'type':'read-only sibling, not merged'})
    return {'status':'PASS','base':BASE,'unchanged_inherited_manifest_files':counts,
            'ancestry':ancestry,'inputs':sources,'python':sys.version,
            'branch':git('branch','--show-current').decode().strip(),
            'main_at_audit':git('rev-parse','origin/main').decode().strip()}
if __name__=='__main__':print(json.dumps(run(),indent=2))
