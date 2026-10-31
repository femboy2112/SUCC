import hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
repo=root.parents[3]
record=json.loads((root/'SOURCE_MANIFEST.json').read_text())
for item in record['artifacts']:
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
for item in record['source_inputs']:
    p=repo/item['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['path']
for item in record['git_source_inputs']:
    data=subprocess.check_output(['git','show',item['commit']+':'+item['path']],cwd=repo)
    assert hashlib.sha256(data).hexdigest()==item['sha256'],item['path']
commands=json.loads((root/'receipts/COMMANDS.json').read_text())
for item in commands['completed_commands']:
    assert item['exit_code']==0
    assert hashlib.sha256((root/item['log']).read_bytes()).hexdigest()==item['log_sha256'],item['log']
print('FIBONACCI_COMPOSITION_MANIFEST_PASS',len(record['artifacts']),len(record['source_inputs']),len(record['git_source_inputs']))
