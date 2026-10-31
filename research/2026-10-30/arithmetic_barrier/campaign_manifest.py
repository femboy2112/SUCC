"""Pin and check campaign bytes and source provenance; not mathematical proof."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = '1a1524de28b155139d8fe84ea90fc2f117fbb9f3'
MANIFEST = HERE / 'SOURCE_MANIFEST.json'
EXCLUDED = {'SOURCE_MANIFEST.json', 'receipts/final-validation-complete.json',
            'receipts/final-validation-complete.log'}


def digest(data):
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)


def artifacts():
    return {str(p.relative_to(HERE)):digest(p.read_bytes())
            for p in sorted(HERE.rglob('*')) if p.is_file()
            and '__pycache__' not in p.parts and p.suffix != '.pyc'
            and str(p.relative_to(HERE)) not in EXCLUDED}


def source_inputs():
    paths = ['AGENTS.md','docs/METHOD.md','docs/CLAIM_LEDGER.md',
             'docs/OPERATIONAL_TRIANGLE.md','provenance/IMPORT_MANIFEST.json',
             'research/2026-10-29/triangle_genesis_repair/MAIN_XVI_HANDOFF.md',
             'research/2026-10-24/PI_LAG_ADVERSARIAL_REVIEW.md',
             'observational_succ/pi_carry_prefix_control.py']
    paths += [str(p.relative_to(ROOT)) for p in sorted(
        (ROOT/'research/2026-10-30/prime_stroboscope').iterdir()) if p.is_file()]
    result={}
    for path in paths:
        data=git('show',PARENT+':'+path)
        assert (ROOT/path).read_bytes()==data, ('changed historical source',path)
        result[path]={'commit':PARENT,**digest(data)}
    return result


def write():
    data={'parent':PARENT,'scope':'additive arithmetic_barrier namespace only',
          'excluded_to_avoid_recursive_hashing':sorted(EXCLUDED),
          'inputs':source_inputs(),'files':artifacts(),
          'proof_authority':'local paper proofs and finite exact/interval checks; no Lean or normality proof',
          'related_heads':'receipts/live_prs.json',
          'independence':'shared model family and source provenance; distinct arithmetic implementations'}
    MANIFEST.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'MANIFEST_WRITTEN','files':len(data['files']),
                      'source_inputs':len(data['inputs'])}))


def check():
    manifest=json.loads(MANIFEST.read_text())
    assert manifest['files']==artifacts(), 'deliverable bytes or inventory changed'
    assert manifest['inputs']==source_inputs(), 'pinned source mismatch'
    scoped_files=0
    related_refs=0
    for folder in ('transfer','signed_crt'):
        data=json.loads((HERE/folder/'SOURCE_MANIFEST.json').read_text())
        for path,record in data['files'].items():
            actual=digest((HERE/folder/path).read_bytes())
            assert all(actual[k]==v for k,v in record.items() if k in actual),(folder,path)
            scoped_files+=1
        for ref in data.get('source_references',[]):
            actual=digest(git('show',ref['commit']+':'+ref['path']))
            assert actual['sha256']==ref['sha256'],ref
            related_refs+=1
        for path,record in data.get('inputs',{}).items():
            assert digest((ROOT/path).read_bytes())['sha256']==record['sha256'],path
    arithmetic=json.loads((HERE/'arithmetic/independent_receipt.json').read_text())
    for path,sha in arithmetic['source_sha256'].items():
        assert digest((HERE/'arithmetic'/path).read_bytes())['sha256']==sha,path
    review=json.loads((HERE/'signed_crt/conductor_growth_review_receipt.json').read_text())
    assert review['reviewed_dossier_sha256']==digest((HERE/'SHARP_CONDUCTOR_GROWTH.md').read_bytes())['sha256']
    raw_receipts=0
    expected_failures={'math-catalog','baseline-math-catalog','independent-arithmetic',
                       'final-validation'}
    for path in (HERE/'receipts').glob('*.json'):
        if str(path.relative_to(HERE)) in EXCLUDED:
            continue
        data=json.loads(path.read_text())
        if 'log_sha256' in data:
            assert digest(path.with_suffix('.log').read_bytes())['sha256']==data['log_sha256'],path
            assert data['exit_code']==(1 if path.stem in expected_failures else 0),path
            raw_receipts+=1
    syntax_files=0
    links=0
    for name in manifest['files']:
        path=HERE/name
        if path.suffix=='.py':
            ast.parse(path.read_text(),filename=name)
            syntax_files+=1
        elif path.suffix=='.json':
            json.loads(path.read_text())
        elif path.suffix=='.md':
            for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target=target.split('#',1)[0]
                assert (path.parent/target).exists(),(name,target)
                links+=1
    namespace=str(HERE.relative_to(ROOT))+'/'
    changed=git('diff','--name-only',PARENT).decode().splitlines()
    assert all(path.startswith(namespace) for path in changed),changed
    # Check whitespace even if files are not yet staged by passing each script
    # through syntax checks above; Git's final staged diff check is separate.
    print(json.dumps({'status':'PASS_ARTIFACT_AND_SOURCE_VALIDATION',
                      'deliverables':len(manifest['files']),
                      'unchanged_parent_inputs':len(manifest['inputs']),
                      'scoped_manifest_files':scoped_files,
                      'related_commit_source_references':related_refs,
                      'raw_command_receipts':raw_receipts,
                      'python_syntax_files':syntax_files,'local_markdown_links':links,
                      'expected_failed_receipts_retained':sorted(expected_failures),
                      'mathematical_truth_established_by_manifest':False},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',action='store_true')
    group.add_argument('--check',action='store_true')
    args=parser.parse_args()
    write() if args.write else check()
