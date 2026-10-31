"""Seal or verify additive research artifacts and their immutable inputs.

This checks bytes, domains of receipt claims, and syntax; it does not prove
the mathematical statements. --write intentionally refreshes the manifest.
"""
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = '1c6ce7d7ee83a0bd751bde8092e46ff798855fd3'
MAIN = 'e18ba565ca540adb7edf3292f5593929e76d91c5'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def files():
    for p in sorted(HERE.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts:
            continue
        rel = str(p.relative_to(HERE))
        if rel == 'SOURCE_MANIFEST.json' or rel.startswith('receipts/final-audit'):
            continue
        if p.suffix in ('.pyc', '.olean', '.ilean'):
            continue
        yield rel, p


def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', commit+':'+path], cwd=ROOT)


def expected_manifest():
    parent_dir = ROOT/'research/2026-10-30/universal_nz_carrier'
    sources = []
    for p in sorted(parent_dir.iterdir()):
        if p.is_file():
            path = str(p.relative_to(ROOT))
            sources.append({'commit':PARENT,'path':path,'sha256':sha(git_bytes(PARENT,path))})
    for path in ('AGENTS.md', 'docs/METHOD.md', 'docs/OPERATIONAL_TRIANGLE.md',
                 'provenance/IMPORT_MANIFEST.json',
                 'research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md'):
        sources.append({'commit':MAIN,'path':path,'sha256':sha(git_bytes(MAIN,path))})
    return {'parent':PARENT,'main':MAIN,
            'branch':'research/carrier-first-certified-transport-2026-10-30',
            'excluded':['SOURCE_MANIFEST.json','receipts/final-audit*','__pycache__','*.pyc','*.olean','*.ilean'],
            'artifacts':{rel:{'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for rel,p in files()},
            'sources':sources,
            'authority':'paper proofs, scoped Lean subset, exact finite tests and same-model reconstruction; no external referee',
            'pi_normality':'OPEN','rh':'OPEN'}


def main():
    expected = expected_manifest()
    manifest = HERE/'SOURCE_MANIFEST.json'
    if sys.argv[1:] == ['--write']:
        manifest.write_text(json.dumps(expected,indent=2)+'\n')
        print(json.dumps({'manifest_written':str(manifest.relative_to(ROOT)),
                          'artifacts':len(expected['artifacts']),'inputs':len(expected['sources'])}))
        return
    assert not sys.argv[1:], 'only --write is accepted'
    assert json.loads(manifest.read_text()) == expected, 'root artifact manifest mismatch'
    seen = set()
    local_pins = 0
    for front in ('algebra','analytic','selected'):
        m = json.loads((HERE/front/'SOURCE_MANIFEST.json').read_text())
        rows = m['artifacts']
        items = rows.items() if isinstance(rows,dict) else ((r['path'],r['sha256']) for r in rows)
        for path,digest in items:
            assert sha((HERE/front/path).read_bytes()) == digest, (front,path)
            local_pins += 1
        for row in m.get('sources',m.get('git_inputs',[])):
            key = row['commit'],row['path']
            if key in seen:
                continue
            assert sha(git_bytes(*key)) == row['sha256'],key
            seen.add(key)
    for row in expected['sources']:
        assert sha((ROOT/row['path']).read_bytes()) == row['sha256'],row['path']
    # The helper is byte-preserved execution infrastructure from PR415.
    helper = git_bytes('f650aab0c8710b502f3e08ec1cb2b351c26b2b3f',
                      'research/2026-10-30/selected_finiteband/run_receipt.py')
    for front in ('','algebra','analytic','selected'):
        assert (HERE/front/'run_receipt.py').read_bytes() == helper,front
    expected_nonzero = {
        'receipts/band-countermodel.json',
        'selected/receipts/signed-probe.json',
        'algebra/receipts/lean-initial-failure.json',
        'algebra/receipts/lean-negative-control.json',
    }
    receipts = []
    python_files = 0
    links = 0
    for rel,p in files():
        if p.suffix == '.py':
            ast.parse(p.read_text(),filename=rel)
            python_files += 1
        if p.suffix == '.json':
            data = json.loads(p.read_text())
            if isinstance(data,dict) and 'command' in data and 'log_sha256' in data:
                raw = p.with_suffix('.log').read_bytes()
                assert sha(raw) == data['log_sha256'], rel
                assert len(raw) == data['log_bytes'],rel
                assert not data.get('timed_out'),rel
                code = data['exit_code']
                assert code == (1 if rel in expected_nonzero else 0),(rel,code)
                receipts.append({'path':rel,'exit_code':code})
        if p.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if '://' in link or link.startswith('#'):
                    continue
                target = link.split('#')[0]
                assert (p.parent/target).exists(),(rel,link)
                links += 1
    assert expected_nonzero <= {r['path'] for r in receipts}
    native = (HERE/'receipts/native-suite.log').read_text()
    assert 'Ran 10008 tests' in native and '\nOK\n' in native
    lean = (HERE/'algebra/receipts/lean-final.log').read_text()
    assert 'sorryAx' not in lean
    diff = subprocess.check_output(['git','diff','--name-only',PARENT],cwd=ROOT,text=True).splitlines()
    assert all(p.startswith('research/2026-10-30/carrier_first/') for p in diff),diff
    print(json.dumps({'status':'PASS','root_artifacts':len(expected['artifacts']),
                      'front_artifact_pins':local_pins,'unique_front_git_inputs':len(seen),
                      'unchanged_parent_files':46,'original_provenance_files':5,
                      'python_syntax_files':python_files,'local_markdown_links':links,
                      'checked_receipts':receipts,
                      'expected_nonzero_receipts':sorted(expected_nonzero),
                      'scope':'bytes, syntax, declared exit statuses and source fidelity; not analytic proof authority'},indent=2))


if __name__ == '__main__':
    main()
