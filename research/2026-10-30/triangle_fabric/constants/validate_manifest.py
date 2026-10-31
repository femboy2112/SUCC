import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent; repo=root.parents[3]
r=json.loads((root/'SOURCE_MANIFEST.json').read_text())
for group,base in (('source_inputs',repo),('artifacts',root)):
    for item in r[group]:
        path=base/item['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'],item['path']
for meta in sorted((root/'receipts').glob('*.json')):
    record=json.loads(meta.read_text())
    log=meta.with_suffix('.log')
    assert record['exit_code']==0,meta
    assert hashlib.sha256(log.read_bytes()).hexdigest()==record['log_sha256'],meta
print('CONSTANTS_MANIFEST_PASS',len(r['source_inputs']),len(r['artifacts']))
