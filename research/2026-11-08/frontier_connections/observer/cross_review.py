"""Independent scalar-integer replay of the quadratic matrix instrument.

This shares its source quantizer/root primitive but not NumPy contractions.
The accompanying paper review was performed separately; this script checks
only exact finite arithmetic, never the paper theorem by itself.
"""
from pathlib import Path
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
FRONT=HERE.parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(FRONT/'arithmetic'))
import mixed_quadratic as mq
from intervals import phase


def main():
    cases=[]
    for p,xs in ((5,[1,2,4]),(13,[1,3,5,8]),(17,[1,2,4,8,16])):
        boxes=[phase(3*j+1,11) for j in range(len(xs))]
        result=mq.scan(xs,boxes,p,1,chunk=2,retain=True)
        roots,_=mq.root_table(p)
        centers=[mq.quantize(z)[0] for z in boxes]
        count=0
        for a,row in result['centers']:
            for b,expected in enumerate(row):
                re=im=0
                for x,(br,bi) in zip(xs,centers):
                    qr,qi=map(int,roots[a*x*x%p]);lr,li=map(int,roots[b*x%p])
                    zr=(br*qr-bi*qi)//mq.Q;zi=(br*qi+bi*qr)//mq.Q
                    re+=zr*lr-zi*li;im+=zr*li+zi*lr
                assert (re,im)==expected
                count+=1
        cases.append({'p':p,'m':len(xs),'all_integer_centers_matched':count,
                      'overflow_bound':result['overflow_bound']})
    paths=[FRONT/'ENERGY_THEOREMS.md',FRONT/'arithmetic/THEOREMS.md',
           FRONT/'arithmetic/mixed_quadratic.py']
    payload={'method':'Python arbitrary-precision scalar contractions versus NumPy int64 matrix centers; shared quantization and phase primitive',
             'cases':cases,'total_centers':sum(c['all_integer_centers_matched'] for c in cases),
             'proof_review':'RE1-4 and MQ1-5 independently reviewed; root notified of nonzero-seed wording and generic index-range check',
             'reviewed_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (HERE/'CROSS_REVIEW.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'total_centers':payload['total_centers'],'cases':len(cases)},sort_keys=True))


if __name__=='__main__':main()
