"""Verify research bytes, nested source manifests and recorded command outputs.

This is a provenance/structure check, never a semantic proof checker.
Use --write-manifest only after the research artifacts and receipts are final.
"""
from pathlib import Path
import argparse, ast, hashlib, json, re, subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='6cf5050ff2cfd92e7a0c8876da5233be6ff117f5'
EXCLUSIONS={'SOURCE_MANIFEST.json','receipts/artifact-validation.json',
            'receipts/artifact-validation.log'}

def digest(raw):return hashlib.sha256(raw).hexdigest()
def inventory():
    return {p.relative_to(HERE).as_posix():p for p in sorted(HERE.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and
            p.relative_to(HERE).as_posix() not in EXCLUSIONS}
def expected_hash(value):return value if isinstance(value,str) else value['sha256']

def verify():
    manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
    files=inventory();assert set(files)==set(manifest['files'])
    counts={'artifacts':len(files),'python':0,'json':0,'links':0,'nested_artifacts':0,
            'source_inputs':0,'command_log_hashes':0}
    failed=[]
    def records(data):
        if isinstance(data,dict):
            if 'exit_code' in data and 'command' in data:yield data
            for v in data.values():yield from records(v)
        elif isinstance(data,list):
            for v in data:yield from records(v)
    for name,p in files.items():
        raw=p.read_bytes();assert digest(raw)==manifest['files'][name]['sha256'],name
        if p.suffix=='.py':ast.parse(raw,filename=name);counts['python']+=1
        if p.suffix=='.md':
            for target in re.findall(r'\]\(([^)]+)\)',raw.decode()):
                if '://' in target or target.startswith('#'):continue
                target=target.split('#')[0]
                if target:
                    assert (p.parent/target).exists(),(name,target)
                    counts['links']+=1
        if p.suffix=='.json':
            data=json.loads(raw);counts['json']+=1
            assert not(isinstance(data,dict) and data.get('status')=='RUNNING'),name
            for record in records(data):
                if record['exit_code']!=0:failed.append(name)
                if record.get('log_sha256'):
                    log=(p.parent/Path(record['log']).name) if 'log' in record else p.with_suffix('.log')
                    assert log.exists(),(name,str(log))
                    assert digest(log.read_bytes())==record['log_sha256'],name
                    counts['command_log_hashes']+=1
            if p.name=='SOURCE_MANIFEST.json':
                artifact_map=data.get('artifacts',data.get('files',{}))
                if isinstance(artifact_map,list):artifact_map={v['path']:v for v in artifact_map}
                if isinstance(artifact_map,dict):
                    for rel,entry in artifact_map.items():
                        assert digest((p.parent/rel).read_bytes())==expected_hash(entry),(name,rel)
                        counts['nested_artifacts']+=1
                sources=data.get('source_inputs',data.get('inputs',[]))
                if isinstance(sources,dict):sources=[dict(v,path=k) if isinstance(v,dict) else {'path':k,'sha256':v} for k,v in sources.items()]
                sources=sources+data.get('read_only_siblings',[])
                for item in sources:
                    path=item['path'];sha=item.get('commit',data.get('parent',data.get('parent_commit',data.get('base_commit',BASE))))
                    content=subprocess.check_output(['git','show',sha+':'+path],cwd=ROOT)
                    assert digest(content)==item['sha256'],(name,path)
                    counts['source_inputs']+=1
    assert set(failed)=={'receipts/math-catalog.json','receipts/baseline-catalog.json'},failed
    return {'status':'PASS','counts':counts,'retained_failed_receipts':sorted(set(failed)),
            'authority':'byte/structure/provenance only; no theorem checking'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-manifest',action='store_true')
    args=parser.parse_args()
    if args.write_manifest:
        data={'parent_commit':BASE,'branch':'research/triangle-categorical-fabric-2026-10-30',
              'scope':'additions under research/2026-10-30/triangle_fabric only',
              'authority':'local paper proofs, exact finite certificates, shared-model reviews; no new Lean or external certification',
              'exclusions':sorted(EXCLUSIONS)+['__pycache__'],
              'files':{n:{'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size} for n,p in inventory().items()}}
        (HERE/'SOURCE_MANIFEST.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(verify(),indent=2))
if __name__=='__main__':main()
