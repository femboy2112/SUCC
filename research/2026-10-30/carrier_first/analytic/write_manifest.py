"""Pin all parent bytes, read-only inputs and this analytic front's outputs."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE='1c6ce7d7ee83a0bd751bde8092e46ff798855fd3'
PARENT='research/2026-10-30/universal_nz_carrier'
SIBLINGS=[
 ('f650aab0c8710b502f3e08ec1cb2b351c26b2b3f','research/2026-10-30/selected_finiteband/arithmetic/ARITHMETIC_THEOREMS.md'),
 ('1573ec5b8fbd60b251cb16741bd5165271ec6dbf','research/2026-10-30/basel_line_circle/BASEL_CIRCLE_THEOREMS.md'),
 ('e14916aa2b4dfc2cce948facc729fb02ce1efafa','research/2026-10-30/carrier_adelic_transport/SPECTRAL_SOURCE_TRANSPORT.md'),
 ('e14916aa2b4dfc2cce948facc729fb02ce1efafa','research/2026-10-30/carrier_adelic_transport/ALL_ORDER_SHADOW.md'),
 ('e8a4978207871a47466cdbb6f15cc86fae784164','research/2026-10-30/dyadic_zeta_prime_exposure/README.md'),
 ('287b9e9214f0214586cb6f0a993e29b58bed496a','research/2026-10-30/summation_snapshot_arrows/README.md')]


def sha(b):return hashlib.sha256(b).hexdigest()


def main():
    inherited=[]
    for p in sorted((ROOT/PARENT).iterdir()):
        if not p.is_file():continue
        relative=str(p.relative_to(ROOT))
        old=subprocess.check_output(['git','show',BASE+':'+relative],cwd=ROOT)
        assert old==p.read_bytes(),relative
        inherited.append({'commit':BASE,'path':relative,'sha256':sha(old)})
    siblings=[]
    for commit,path in SIBLINGS:
        raw=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
        siblings.append({'commit':commit,'path':path,'sha256':sha(raw)})
    artifacts={str(p.relative_to(HERE)):sha(p.read_bytes())
               for p in sorted(HERE.rglob('*')) if p.is_file()
               and '__pycache__' not in p.parts and p.name!='SOURCE_MANIFEST.json'}
    for p in (HERE/'receipts').glob('*.json'):
        d=json.loads(p.read_text())
        assert d['exit_code']==0,p
        assert sha(p.with_suffix('.log').read_bytes())==d['log_sha256'],p
    result={'parent':BASE,'artifacts':artifacts,'sources':inherited+siblings,
            'literature_retrieved_utc_date':'2026-10-31',
            'literature':['https://dlmf.nist.gov/3.5','https://dlmf.nist.gov/18.2',
                          'https://dlmf.nist.gov/25.4','https://dlmf.nist.gov/25.5'],
            'authority':'local proofs; exact rational tests; same-model independent implementations; no new Lean'}
    (HERE/'SOURCE_MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','artifacts':len(artifacts),
                      'parent_files':len(inherited),'sibling_inputs':len(siblings)}))


if __name__=='__main__':main()
