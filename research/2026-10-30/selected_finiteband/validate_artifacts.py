"""Scoped reproducibility audit. Byte identity is not mathematical proof."""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PARENT='fa598e3a5a1111c3445200f1ddf48dcdea6bdc09'
EXCLUDED={'SOURCE_MANIFEST.json','receipts/artifact-audit-final.json','receipts/artifact-audit-final.log'}


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def locate(base,path):
    return ROOT/path if path.startswith(('research/','AGENTS.md','docs/','provenance/','observational_succ/')) else base/path


def checkrow(base,row):
    path=row['path'];commit=row.get('commit',row.get('git_commit'))
    raw=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT) if commit else locate(base,path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==row['sha256'],(path,commit)


def main():
    p=argparse.ArgumentParser();p.add_argument('--write-manifest',action='store_true');a=p.parse_args()
    paths={str(f.relative_to(HERE)):f for f in sorted(HERE.rglob('*')) if f.is_file()
           and '__pycache__' not in f.parts and str(f.relative_to(HERE)) not in EXCLUDED}
    manifest=HERE/'SOURCE_MANIFEST.json'
    if a.write_manifest:
        manifest.write_text(json.dumps({'parent':PARENT,'scope':'additions only in research/2026-10-30/selected_finiteband',
             'branch':'research/selected-finiteband-dispersion-2026-10-30',
             'authority':'local paper proofs and finite exact/interval certificates; same-model reviews; no new Lean theorem',
             'excluded':sorted(EXCLUDED)+['__pycache__'],
             'files':{n:{'sha256':digest(f),'bytes':f.stat().st_size} for n,f in paths.items()}},indent=2)+'\n')
    m=json.loads(manifest.read_text());assert set(m['files'])==set(paths)
    count={'artifacts':len(paths),'python':0,'json':1,'links':0,'command_logs':0,'nested_artifacts':0,'source_inputs':0}
    failures=[]
    for n,f in paths.items():
        assert digest(f)==m['files'][n]['sha256'],n
        assert f.stat().st_size==m['files'][n]['bytes'],n
        if f.suffix=='.py':ast.parse(f.read_text(),filename=n);count['python']+=1
        if f.suffix=='.md':
            s=re.sub(r'```.*?```','',f.read_text(),flags=re.S)
            s=re.sub(r'`[^`]*`','',s)
            for link in re.findall(r'\[[^\]]+\]\(([^\s)]+)\)',s):
                if '://' in link or link.startswith(('#','mailto:')):continue
                assert (f.parent/link.split('#')[0]).exists(),(n,link)
                count['links']+=1
        if f.suffix!='.json':continue
        d=json.loads(f.read_text());count['json']+=1
        if isinstance(d,dict):
            assert d.get('status')!='RUNNING',n
            for run in d.get('runs',[]):
                if not isinstance(run,dict):continue
                for stream in ('stdout','stderr'):
                    if stream+'_sha256' in run:
                        assert digest(f.parent/run[stream+'_file'])==run[stream+'_sha256'],(n,stream)
                        count['command_logs']+=1
                if 'exit_code' in run:assert run['exit_code']==0,(n,run)
            if 'exit_code' in d and 'log_sha256' in d:
                target=f.parent/d['log'] if 'log' in d else f.with_suffix('.log')
                assert digest(target)==d['log_sha256'],n
                count['command_logs']+=1
                if d['exit_code']!=0:failures.append(n)
    expected={'receipts/math-catalog.json','receipts/baseline-catalog.json',
              'receipts/source-audit.json','receipts/source-audit-final.json'}
    assert set(failures)==expected,failures
    for scope in ('kernel','arithmetic','cylinders'):
        base=HERE/scope;d=json.loads((base/'SOURCE_MANIFEST.json').read_text())
        rows=d['artifacts']
        if isinstance(rows,dict):rows=[{'path':k,'sha256':v if isinstance(v,str) else v['sha256']} for k,v in rows.items()]
        for row in rows:checkrow(base,row);count['nested_artifacts']+=1
        for key in ('sources','read_only_git_inputs','local_review_inputs','git_sources'):
            for row in d.get(key,[]):checkrow(base,row);count['source_inputs']+=1
    subprocess.run(['git','diff','--check',PARENT],cwd=ROOT,check=True)
    changed=subprocess.check_output(['git','diff','--name-only',PARENT],cwd=ROOT,text=True).splitlines()
    assert all(n.startswith('research/2026-10-30/selected_finiteband/') for n in changed),changed
    print(json.dumps({'status':'PASS','counts':count,'retained_failed_commands':failures,
                      'authority':'byte/provenance/structure only'},indent=2))


if __name__=='__main__':main()
