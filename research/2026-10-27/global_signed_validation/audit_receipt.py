"""Independent receipt tampering controls; expected rejections must be specific."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent


def main():
    receipt=OUT/'exact_receipt.json'
    original=json.loads(receipt.read_text())
    changes={}
    data=copy.deepcopy(original)
    data['status']['normality_proved']=True
    changes['false_normality']=data
    data=copy.deepcopy(original)
    data['source_sha256']['observational_succ/succ_internal_matrix_walk.py']='0'*64
    changes['foreign_source']=data
    data=copy.deepcopy(original)
    data['fixed_mode_core']['block_loss']='1/13'
    changes['false_loss_constant']=data
    results=[]
    with tempfile.TemporaryDirectory(prefix='succ-global-controls-') as temporary:
        paths={'clean':receipt}
        for name,data in changes.items():
            path=Path(temporary)/f'{name}.json'
            path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
            paths[name]=path
        for name,path in paths.items():
            command=[sys.executable,'scripts/global_signed_probe.py','--verify','--receipt',str(path)]
            result=subprocess.run(command,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            log=OUT/f'receipt_{name}.log'
            log.write_text(result.stdout)
            passed=(result.returncode==0 and 'verified byte-for-byte' in result.stdout) if name=='clean' else (
                result.returncode!=0 and 'receipt mismatch: source, theorem scope, or finite result changed' in result.stdout)
            results.append({'name':name,'command':command,'exit_code':result.returncode,
                            'expected_behavior_observed':passed,'log':log.name,
                            'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()})
    (OUT/'receipt_mutation_results.json').write_text(json.dumps(results,indent=2)+'\n')
    if not all(x['expected_behavior_observed'] for x in results):
        raise SystemExit('receipt control failed')
    print('clean replay passed; three distinct receipt mutations rejected as intended')


if __name__=='__main__':main()
