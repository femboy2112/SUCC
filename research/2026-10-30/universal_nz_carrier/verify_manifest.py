from pathlib import Path
from hashlib import sha1, sha256
import json
D=Path(__file__).resolve().parent
manifest=json.loads((D/'SOURCE_MANIFEST.json').read_text())
for item in manifest['files']:
    path=D/item['name']
    b=path.read_bytes()
    assert len(b)==item['bytes'],item['name']
    assert sha256(b).hexdigest()==item['sha256'],item['name']
    assert sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==item['git_blob_sha1'],item['name']
print(f"PASS {len(manifest['files'])} manifest bytes, SHA256 and Git blob SHA1")