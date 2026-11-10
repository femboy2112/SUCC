"""Independent direct repartition and 100-digit source readout.

Numerical corroboration of rigorous rectangles, not a second interval proof.
The event sweep is not used. Source history is shared and declared.
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,sys
import mpmath as mp
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from source_probe import common_history,principal_pair,direct_modular_residue


def run():
    A=673
    path=HERE/'results'/f'origin_{A}.json'
    record=json.loads(path.read_text())
    p,S=record['p'],record['scale']
    data=common_history(2*A-1,A)
    den,rr=data['denominator'],data['residues']
    checks=0
    for n in (A+7,A+29,2*A-17):
        assert rr[n-A]==direct_modular_residue(n,den)
    local=[principal_pair(r,den,p)[0] for r in rr]
    with mp.workdps(100):
        a=[mp.exp(2j*mp.pi*r/p) for r in local]
        z=[mp.exp(2j*mp.pi*mp.mpf(r)/den) for r in rr]
        for M in (4,16):
            cuts=sorted({0,p}|{M*r%p for r in local})
            accum={'original_zero':mp.mpc(0),'synthetic_conjugate':mp.mpc(0)}
            bs={'original_zero':[v/mp.exp(2j*mp.pi*r/p) for v,r in zip(z,local)],
                'synthetic_conjugate':[mp.conj(v) for v in a]}
            for left,right in zip(cuts,cuts[1:]):
                buckets={}
                for j,r in enumerate(local):
                    label=((2*M*r-left-right)//(2*p))%M
                    buckets.setdefault(label,[]).append(j)
                for family,b in bs.items():
                    f=mp.mpc(0)
                    for js in buckets.values():
                        f+=sum((a[j] for j in js),mp.mpc(0))*sum((b[j] for j in js),mp.mpc(0))/len(js)
                    accum[family]+=(right-left)*f/(p*A)
            for family,F in accum.items():
                row=next(r for r in record['rows'] if r['h']==1 and r['M']==M and r['family']==family)
                for value,ints in ((F.real,row['origin_average']['re']),(F.imag,row['origin_average']['im'])):
                    assert mp.mpf(ints[0])/S <= value <= mp.mpf(ints[1])/S
                    checks+=1
    return {'status':'PASS','authority':'Independent numerical corroboration, not rigorous interval proof',
            'A':A,'configurations':4,'scalar_containments':checks,'decimal_precision':100,
            'fresh_modular_source_checks':3,
            'independence':'Direct full repartition vs event sweep; source history and model family shared',
            'source_receipt_sha256':sha256(path.read_bytes()).hexdigest(),
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
