"""Read-only source, ancestry and environment audit; not proof certification."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
import hashlib,json,subprocess,platform


def main():
    parent='1c6ce7d7ee83a0bd751bde8092e46ff798855fd3'
    D=ROOT/'research/2026-10-30/universal_nz_carrier'
    files=[]
    for p in sorted(D.iterdir()):
        if not p.is_file():continue
        rel=str(p.relative_to(ROOT));raw=p.read_bytes()
        assert raw==subprocess.check_output(['git','show',parent+':'+rel],cwd=ROOT)
        files.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
    manifest_rows=0
    for p in D.glob('*MANIFEST.json'):
        m=json.loads(p.read_text())
        for row in m['files']:
            raw=(D/row['name']).read_bytes()
            assert len(raw)==row['bytes']
            assert hashlib.sha256(raw).hexdigest()==row['sha256']
            assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()==row['git_blob_sha1']
            manifest_rows+=1
    snapshots=json.loads((Path(__file__).parent/'initial_refs_ci.json').read_text())
    edges=[]
    for row in snapshots['prs']:
        # Inspect ancestry without merging any sibling.
        result=subprocess.run(['git','merge-base','--is-ancestor',row['base_sha'],row['sha']],cwd=ROOT)
        assert result.returncode==0,row
        edges.append({'pr':row['pr'],'base_sha':row['base_sha'],'head_sha':row['sha']})
    import observational_succ,mpmath,sympy,numpy,scipy
    imported=Path(observational_succ.__file__).resolve()
    assert ROOT in imported.parents,imported
    original=[]
    for rel in ['AGENTS.md','docs/OPERATIONAL_TRIANGLE.md','docs/METHOD.md',
                'provenance/IMPORT_MANIFEST.json','research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md']:
        raw=(ROOT/rel).read_bytes()
        assert raw==subprocess.check_output(['git','show',snapshots['main']+':'+rel],cwd=ROOT)
        original.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest()})
    print(json.dumps({'status':'PASS','parent':parent,'unchanged_parent_files':files,
       'manifest_rows':manifest_rows,'verified_ancestry_edges':edges,'original_provenance':original,
       'environment':{'python':platform.python_version(),'package':str(imported),
         'mpmath':mpmath.__version__,'sympy':sympy.__version__,'numpy':numpy.__version__,'scipy':scipy.__version__}},indent=2))


if __name__=='__main__':main()
