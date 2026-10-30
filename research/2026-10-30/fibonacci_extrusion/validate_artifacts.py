"""Byte, syntax and receipt validation; never mathematical proof authority."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
EXCLUDED={'SOURCE_MANIFEST.json','receipts/artifact-audit.json','receipts/artifact-audit.log'}

def files():
    return {p.relative_to(HERE).as_posix():p for p in sorted(HERE.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'
            and p.relative_to(HERE).as_posix() not in EXCLUDED}

def fingerprint(p):
    b=p.read_bytes()
    return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def main():
    if sys.argv[1:]==['--write']:
        data={'parent':'7b5a2b4534aa5e71865046ca8d3f723d8002b9fe',
              'branch':'research/fibonacci-triangle-extrusion-2026-10-30',
              'scope':'additive research; original source/seed/history unchanged',
              'exclusions':sorted(EXCLUDED),'files':{n:fingerprint(p) for n,p in files().items()},
              'inputs':json.loads((HERE/'receipts/source-audit.log').read_text())['inputs']}
        (HERE/'SOURCE_MANIFEST.json').write_text(json.dumps(data,indent=2)+'\n')
    elif sys.argv[1:]:
        raise SystemExit('usage: validate_artifacts.py [--write]')
    data=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
    found=files()
    assert set(data['files'])==set(found),'manifest membership changed'
    counts={'artifacts':len(found),'python':0,'json':0,'local_links':0,'command_logs':0,'source_inputs':0,'nested_artifacts':0}
    failures=[]
    for n,p in found.items():
        assert data['files'][n]==fingerprint(p),n
        if p.suffix=='.py':
            ast.parse(p.read_text(),filename=n); counts['python']+=1
        if p.suffix=='.json':
            d=json.loads(p.read_text()); counts['json']+=1
            if isinstance(d,dict) and 'log_sha256' in d:
                log=p.with_suffix('.log')
                assert fingerprint(log)['sha256']==d['log_sha256'],n
                counts['command_logs']+=1
                if d.get('exit_code',0): failures.append(n)
            if isinstance(d,dict) and d.get('status')=='RUNNING':
                raise AssertionError('unfinished receipt: '+n)
        if p.suffix=='.md':
            # Displayed algebra such as [a](b) is not a Markdown link.
            prose=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
            prose='\n'.join(line for line in prose.splitlines() if not line.startswith('    '))
            prose=re.sub(r'`[^`]*`','',prose)
            for target in re.findall(r'\]\(([^\s)]+)\)',prose):
                if target.startswith(('http:','https:','#','mailto:')):continue
                target=target.split('#')[0]
                if not target:continue
                assert (p.parent/target).exists(),(n,target)
                counts['local_links']+=1
    for item in data['inputs']:
        raw=subprocess.check_output(['git','show',item['commit']+':'+item['path']],cwd=ROOT)
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item
        counts['source_inputs']+=1
    for folder in ('composition','arrows','arithmetic'):
        mf=HERE/folder/'SOURCE_MANIFEST.json'
        sub=json.loads(mf.read_text())
        records=sub['artifacts']
        if isinstance(records,list):records={r['path']:r for r in records}
        for name,item in records.items():
            expected=item if isinstance(item,str) else item['sha256']
            assert fingerprint(mf.parent/name)['sha256']==expected,(folder,name)
            counts['nested_artifacts']+=1
        sources=sub['source_inputs']
        if isinstance(sources,dict):sources=[{'path':p,'sha256':v} for p,v in sources.items()]
        for item in sources+sub.get('git_source_inputs',[])+sub.get('pinned_git_sources',[]):
            commit=item.get('commit',sub.get('base_commit',sub.get('parent_commit',data['parent'])))
            raw=subprocess.check_output(['git','show',commit+':'+item['path']],cwd=ROOT)
            assert hashlib.sha256(raw).hexdigest()==item['sha256'],item
            counts['source_inputs']+=1
    changed=subprocess.check_output(['git','diff','--name-only',data['parent']],cwd=ROOT,text=True).splitlines()
    assert all(p.startswith('research/2026-10-30/fibonacci_extrusion/') for p in changed),changed
    print(json.dumps({'status':'PASS','counts':counts,'retained_failed_receipts':failures,
                     'authority':'byte/syntax/provenance only, no theorem or external referee certification'},indent=2))

if __name__=='__main__':main()
