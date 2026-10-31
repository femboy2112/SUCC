"""Read-only pinned ancestry, source bytes, inherited receipts and environment audit."""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PARENT='5f350af7808532e55d74e80c948c02bb385c6e70'


def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)


def run():
    totals={}
    for directory,key in [('prime_stroboscope','source_files'),
            ('arithmetic_barrier','files'),('gamma_all_places','files'),
            ('gamma_twist','files'),('selected_boundary_slip','sha256_files')]:
        base=HERE.parent/directory
        records=json.loads((base/'SOURCE_MANIFEST.json').read_text())[key]
        if isinstance(records,list): records={r['path']:r for r in records}
        for name,item in records.items():
            path=base/name
            raw=path.read_bytes()
            assert hashlib.sha256(raw).hexdigest()==item['sha256'],str(path)
            relative=path.relative_to(ROOT).as_posix()
            assert raw==git('show',PARENT+':'+relative),relative
        totals[directory]=len(records)
    remote=json.loads((HERE/'receipts/initial_remote.json').read_text())
    ancestry=[]
    for row in remote['rows']:
        p=row['info']
        subprocess.run(['git','merge-base','--is-ancestor',p['base_sha'],p['head_sha']],cwd=ROOT,check=True)
        local=git('rev-parse','origin/'+p['head']).decode().strip()
        assert local==p['head_sha'],(row['pr'],local)
        ancestry.append({'pr':row['pr'],'base':p['base_sha'],'head':local,'ancestor':True})
    names=['AGENTS.md','docs/METHOD.md','provenance/IMPORT_MANIFEST.json',
        'observational_succ/bbp_source_memory.py','observational_succ/bbp_two_adic.py',
        'observational_succ/succ_internal_matrix_walk.py',
        'research/2026-10-29/triangle_genesis_repair/MAIN_XVI_HANDOFF.md',
        'research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md']
    inputs={}
    for name in names:
        raw=(ROOT/name).read_bytes()
        assert raw==git('show',PARENT+':'+name)
        inputs[name]={'sha256':hashlib.sha256(raw).hexdigest(),
                      'git_blob':git('rev-parse',PARENT+':'+name).decode().strip()}
    return {'status':'PASS','parent':PARENT,'unchanged_inherited_manifest_files':totals,
        'ancestry':ancestry,'source_inputs':inputs,'python':sys.version,
        'packages':{p:importlib.metadata.version(p) for p in
                    ['mpmath','numpy','sympy','scipy','observational-succ']},
        'branch':git('branch','--show-current').decode().strip(),
        'main':git('rev-parse','origin/main').decode().strip()}


if __name__=='__main__': print(json.dumps(run(),indent=2))
