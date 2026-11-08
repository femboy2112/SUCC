"""Independent high-precision readout of retained outward source rectangles.

This is a numerical cross-check, not a replacement for the rational interval
proof. It shares the pinned source-history builder, but does not import the
phase enclosure or conditional projection implementation under review.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import sys

import mpmath as mp

HERE=Path(__file__).resolve().parent
DOSSIER=HERE.parent
sys.path.insert(0,str(DOSSIER.parents[2]))
sys.path.insert(0,str(DOSSIER.parent/'covariance_forge'))
from source import common_history


def project(v,labels):
    indices={}
    for i,label in enumerate(labels):
        indices.setdefault(label,[]).append(i)
    result=[None]*len(v)
    for ids in indices.values():
        value=mp.fsum(v[i] for i in ids)/len(ids)
        for i in ids:
            result[i]=value
    return result


def run():
    checks=rows=source_checks=0
    receipts=[]
    with mp.workdps(100):
        def mean(v):
            return mp.fsum(v)/len(v)
        def e(q):
            return mp.expj(2*mp.pi*(mp.mpf(q.numerator%q.denominator)/q.denominator))
        for A in (137,2203):
            path=DOSSIER/'results'/f'quotient_{A}.json'
            raw=json.loads(path.read_text())
            state=common_history(2*A-1,A)
            D=state['denominator'];rs=state['residues'];p=raw['p']
            assert state['unwrapped_sha256']==raw['source']['unwrapped_sha256']
            assert state['carry_sha256']==raw['source']['carry_sha256']
            # Fresh times and direct modular four-ray sums, independent of
            # the source recurrence. The algebraic algorithm is classical.
            for j in (7,A//3,A-8):
                n=A+j
                value=sum(c*pow(16,n-k,8*k-o)*(D//(8*k-o))
                          for k in range(1,n+1)
                          for c,o in ((4,7),(-2,4),(-1,3),(-1,2)))%D
                assert value==rs[j]
                source_checks+=1
            exponent=0;other=D
            while other%p==0:
                exponent+=1;other//=p
            assert exponent==1
            local=[F((r*pow(other,-1,p))%p,p) for r in rs]
            seed=F(int(raw['shadow']['seed_numerator_hex'],16),
                   int(raw['shadow']['seed_denominator_hex'],16))
            original=[F(r,D) for r in rs]
            shadow=[q+F(seed.numerator*pow(16,A+j,seed.denominator)%seed.denominator,
                        seed.denominator) for j,q in enumerate(original)]
            cache={}
            for h in (1,3):
                a=[e(h*q) for q in local]
                for family,full in (('original_zero',original),('matched_wrong_seed',shadow),
                                    ('synthetic_conjugate',[F()]*A)):
                    # Construct the complementary phase directly from the
                    # exact rational difference, not by multiplying boxes.
                    b=[e(h*(q-x)) for q,x in zip(full,local)]
                    z=[e(h*q) for q in full]
                    cache[h,family]=(a,b,z)
            def check(value,bounds):
                nonlocal checks
                lower,upper=[mp.mpf(x)/raw['scale'] for x in bounds]
                assert lower-mp.mpf('1e-80')<=value<=upper+mp.mpf('1e-80')
                checks+=1
            def check_complex(value,box):
                check(value.real,box['re']);check(value.imag,box['im'])
                check(abs(value)**2,box['abs_squared'])
            for row in raw['rows']:
                a,b,z=cache[row['h'],row['family']]
                M=row['cells'];theta=F(row['cell_origin'])
                labels=[int(M*((x+theta)%1)) for x in local]
                pa,pb,pz=[project(v,labels) for v in (a,b,z)]
                da=[x-y for x,y in zip(a,pa)];db=[x-y for x,y in zip(b,pb)]
                lifted=[x*y for x,y in zip(a,pb)]
                w=mean(z);coarse=mean([x*y for x,y in zip(pa,pb)])
                res=mean([x*y for x,y in zip(da,db)])
                va=mean([abs(x)**2 for x in da]);vb=mean([abs(x)**2 for x in db])
                marginal=mean(a)*mean(b)
                for field,value in [('W',w),('coarse_signal',coarse),('residual',res),
                                     ('marginal_product',marginal),('total_covariance',w-marginal),
                                     ('coarse_covariance',coarse-marginal)]:
                    check_complex(value,row[field])
                for field,value in [('Va',va),('Vb',vb),('cauchy_bound_squared',va*vb),
                                     ('model_error_squared',mean([abs(x-y)**2 for x,y in zip(z,lifted)])),
                                     ('demodulation_gap_squared',mean([abs(x-y)**2 for x,y in zip(lifted,pz)]))]:
                    check(value,row[field])
                rows+=1
            receipts.append({'A':A,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    return {'status':'100-digit independent numerical containment cross-check; not a new interval proof',
            'rows':rows,'scalar_containments':checks,'fresh_exact_source_checks':source_checks,
            'shared_provenance':['common_history builder','underlying four-pole source and source data'],
            'independent':['mpmath phase evaluation','direct rational complementary phase','conditional grouping',
                           'fresh modular source times'],
            'rounding_tolerance':'1e-80','inputs':receipts,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=HERE/'SOURCE_REVIEW.json')
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
