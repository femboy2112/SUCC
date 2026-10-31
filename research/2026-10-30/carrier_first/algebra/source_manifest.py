"""Byte/provenance validation, not a proof checker."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
PARENT='1c6ce7d7ee83a0bd751bde8092e46ff798855fd3'
SIBLING='e14916aa2b4dfc2cce948facc729fb02ce1efafa'
EXCLUDED={'SOURCE_MANIFEST.json','receipts/manifest-audit-final.json','receipts/manifest-audit-final.log'}


def sha(raw):return hashlib.sha256(raw).hexdigest()


def inputs():
    base='research/2026-10-30/universal_nz_carrier/'
    names=subprocess.check_output(['git','ls-tree','-r','--name-only',PARENT,base],cwd=ROOT,text=True).splitlines()
    names+=['AGENTS.md','docs/OPERATIONAL_TRIANGLE.md']
    result=[]
    for commit,paths in ((PARENT,names),(SIBLING,[
        'research/2026-10-30/carrier_adelic_transport/CARRIER_REALIZATION.md',
        'research/2026-10-30/carrier_adelic_transport/CLAIMS.md'])):
        for path in paths:
            raw=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
            result.append({'commit':commit,'path':path,'sha256':sha(raw)})
    return result


def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
    paths=[f for f in sorted(HERE.rglob('*')) if f.is_file() and '__pycache__' not in f.parts
           and str(f.relative_to(HERE)) not in EXCLUDED]
    manifest=HERE/'SOURCE_MANIFEST.json'
    if a.write:
        manifest.write_text(json.dumps({'parent':PARENT,'read_only_sibling':SIBLING,
          'authority':'paper, scoped Lean kernel, exact implementation checks; no external referee',
          'excluded':sorted(EXCLUDED)+['__pycache__'],
          'artifacts':[{'path':str(f.relative_to(HERE)),'sha256':sha(f.read_bytes())} for f in paths],
          'git_inputs':inputs()},indent=2)+'\n')
    m=json.loads(manifest.read_text())
    assert {row['path'] for row in m['artifacts']}=={str(f.relative_to(HERE)) for f in paths}
    for row in m['artifacts']:assert sha((HERE/row['path']).read_bytes())==row['sha256'],row['path']
    assert m['git_inputs']==inputs()
    expected={'lean-initial-failure','lean-negative-control'}
    failed=set()
    for p in (HERE/'receipts').glob('*.json'):
        if p.stem=='manifest-audit-final':continue
        d=json.loads(p.read_text())
        assert sha(p.with_suffix('.log').read_bytes())==d['log_sha256']
        if d['exit_code']!=0:failed.add(p.stem)
    assert failed==expected,failed
    leanlog=(HERE/'receipts/lean-final.log').read_text()
    assert 'sorryAx' not in leanlog and 'error:' not in leanlog
    print(json.dumps({'status':'PASS','artifacts':len(paths),'git_inputs':len(m['git_inputs']),
       'retained_nonzero_exits':sorted(failed),'scope':'byte hashes and execution metadata'},indent=2))


if __name__=='__main__':main()
