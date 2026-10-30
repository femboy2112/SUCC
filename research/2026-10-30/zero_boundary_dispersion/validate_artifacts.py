"""Verify scoped artifact bytes, source manifests, receipts and local links.

This validates provenance/structure, not mathematical truth. Preserve failed
receipts. --write-manifest is an intentional inventory update, not a test.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PARENT='5f350af7808532e55d74e80c948c02bb385c6e70'
EXCLUDED={'SOURCE_MANIFEST.json','receipts/artifact-validation.json',
          'receipts/artifact-validation.log','receipts/artifact-validation-final.json',
          'receipts/artifact-validation-final.log'}


def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def check(p,sha):
    assert p.is_file(),f'missing {p}'
    assert digest(p)==sha,f'hash mismatch {p}'


def locate(base,name):
    return ROOT/name if name.startswith(('research/','AGENTS.md','docs/','provenance/','observational_succ/')) else base/name


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write-manifest',action='store_true')
    args=p.parse_args()
    paths={str(f.relative_to(HERE)):f for f in sorted(HERE.rglob('*'))
        if f.is_file() and '__pycache__' not in f.parts and str(f.relative_to(HERE)) not in EXCLUDED}
    manifest=HERE/'SOURCE_MANIFEST.json'
    if args.write_manifest:
        manifest.write_text(json.dumps({'parent_commit':PARENT,
          'branch':'research/zero-boundary-dispersion-2026-10-30',
          'authority':'local paper proofs; finite integer Lean component only; shared-model reviews',
          'scope':'additions under research/2026-10-30/zero_boundary_dispersion only',
          'exclusions':sorted(EXCLUDED)+['__pycache__'],
          'files':{name:{'sha256':digest(f),'bytes':f.stat().st_size} for name,f in paths.items()}},indent=2)+'\n')
    m=json.loads(manifest.read_text())
    assert set(m['files'])==set(paths),'artifact inventory changed'
    for name,item in m['files'].items():
        check(paths[name],item['sha256'])
        assert paths[name].stat().st_size==item['bytes']
    counts={'artifacts':len(paths),'python':0,'json':1,'links':0,'receipts':0,
            'nested_artifacts':0,'source_inputs':0}
    failed=[]
    for name,f in paths.items():
        if f.suffix=='.py': ast.parse(f.read_text(),filename=name);counts['python']+=1
        if f.suffix=='.md':
            for link in re.findall(r'\[[^\]]+\]\(([^\s)]+)\)',f.read_text()):
                if '://' in link or link.startswith(('#','mailto:')): continue
                target=link.split('#',1)[0]
                assert (f.parent/target).exists(),f'broken link {name}: {link}'
                counts['links']+=1
        if f.suffix!='.json': continue
        data=json.loads(f.read_text());counts['json']+=1
        rows=data if isinstance(data,list) else data.get('runs',[data])
        for i,row in enumerate(rows):
            if not isinstance(row,dict) or 'exit_code' not in row: continue
            if 'log_sha256' not in row: continue
            check(f.parent/row['log'] if 'log' in row else f.with_suffix('.log'),row['log_sha256'])
            counts['receipts']+=1
            if row['exit_code']!=0: failed.append(name+(':'+str(i) if 'runs' in data else ''))
        if isinstance(data,dict): assert data.get('status')!='RUNNING',f'unfinished receipt {name}'
    expected={'receipts/math-catalog.json','receipts/baseline-catalog.json',
              'diophantine/receipts/lean_initial.json','spectral/command_receipts.json:1'}
    assert set(failed)==expected,failed
    for scope in ('diophantine','crt','spectral'):
        base=HERE/scope;data=json.loads((base/'SOURCE_MANIFEST.json').read_text())
        artifacts=data['artifacts']
        if isinstance(artifacts,dict): artifacts=[{'path':name,'sha256':sha} for name,sha in artifacts.items()]
        for row in artifacts:
            check(locate(base,row['path']),row['sha256']);counts['nested_artifacts']+=1
        for row in data.get('source_inputs',data.get('inputs',[])):
            if 'git_commit' in row:
                raw=subprocess.check_output(['git','show',row['git_commit']+':'+row['path']],cwd=ROOT)
                assert hashlib.sha256(raw).hexdigest()==row['sha256']
            else: check(locate(base,row['path']),row['sha256'])
            counts['source_inputs']+=1
    subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
    print(json.dumps({'status':'PASS','counts':counts,'retained_failed_receipts':sorted(failed),
        'authority':'byte/structure/provenance check only'},indent=2))


if __name__=='__main__':main()
