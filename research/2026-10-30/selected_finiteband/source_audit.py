"""Read-only inheritance, ancestry and dependency audit for this round."""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PARENT='fa598e3a5a1111c3445200f1ddf48dcdea6bdc09'


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)


def main():
    inherited={}
    for name,key in [('prime_stroboscope','source_files'),('arithmetic_barrier','files'),
                     ('gamma_all_places','files'),('gamma_twist','files'),
                     ('selected_boundary_slip','sha256_files'),('zero_boundary_dispersion','files'),
                     ('cylinder_tiling_collision','new_files'),('codex_finite_band_crt','files')]:
        base=HERE.parent/name
        data=json.loads((base/'SOURCE_MANIFEST.json').read_text())
        records=data[key]
        if isinstance(records,list):records={r['path']:r for r in records}
        for path,item in records.items():
            actual=ROOT/path if path.startswith('research/') else base/path
            raw=actual.read_bytes()
            want=item if isinstance(item,str) else item['sha256']
            assert hashlib.sha256(raw).hexdigest()==want,(name,path)
            assert raw==git('show',PARENT+':'+actual.relative_to(ROOT).as_posix())
        inherited[name]=len(records)
    ancestry=[]
    for row in json.loads((HERE/'receipts/initial-pr-refs.json').read_text()):
        subprocess.run(['git','merge-base','--is-ancestor',row['base'],row['head']],cwd=ROOT,check=True)
        ancestry.append({'pr':row['number'],'base':row['base'],'head':row['head'],'ancestor':True})
    names=['AGENTS.md','docs/METHOD.md','provenance/IMPORT_MANIFEST.json',
           'observational_succ/bbp_source_memory.py','observational_succ/bbp_two_adic.py',
           'observational_succ/succ_internal_matrix_walk.py',
           'research/2026-10-29/triangle_genesis_repair/MAIN_XVI_HANDOFF.md',
           'research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md']
    sources={}
    for name in names:
        raw=(ROOT/name).read_bytes()
        assert raw==git('show',PARENT+':'+name)
        sources[name]={'sha256':hashlib.sha256(raw).hexdigest(),
                       'git_blob':git('rev-parse',PARENT+':'+name).decode().strip()}
    # A file launched below research/ otherwise falls through to the shared
    # environment's editable installation in another worktree. Root -m test
    # discovery already has the current checkout first; make this audit explicit.
    sys.path.insert(0,str(ROOT))
    import observational_succ
    assert Path(observational_succ.__file__).resolve().is_relative_to(ROOT)
    print(json.dumps({'status':'PASS','parent':PARENT,'inherited_unchanged':inherited,
                      'ancestry':ancestry,'source_inputs':sources,'python':sys.version,
                      'import_path':observational_succ.__file__,
                      'packages':{n:importlib.metadata.version(n) for n in ('mpmath','numpy','sympy','scipy')},
                      'main_observed':git('rev-parse','origin/main').decode().strip()},indent=2))


if __name__=='__main__':main()
