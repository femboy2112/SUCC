"""Exploratory causal ancestor reconstruction; NOT a preregistered model test.

Analytic tables read only past/current literal carries. Their signed residual
is bounded independently of measured W. The retained carry mean is nevertheless
asymptotically equivalent to W and is not granted decay.
"""
import argparse
from functools import lru_cache
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import signed_probe as sp
cm=sp.cm
from intervals import pi_box


def integer_word(carries, n, k, residues=False):
    if not 1<=k<=n<=len(carries):
        raise ValueError('a full causal carry word is required')
    word=carries[n-k:n]
    value=0
    for d in word:value=16*value+(d % 16 if residues else d)
    return value


@lru_cache(None)
def word_phase(h,k,value):
    return cm.phase(h*(2*value+1),2*16**k)


def analytic_bounds(n0,N,h,k,H,bad_count=0):
    if not 1<=k<n0 or not 1<=H<=N or not 0<=bad_count<=N:
        raise ValueError('valid time, memory, aperture and exception count required')
    pi_upper=Q(pi_box().hi,cm.SCALE)
    epsilon=pi_upper*abs(h)*(Q(1,16**k)+Q(2,(8*(n0-k)+1)**2))
    bad=Q(bad_count,N)
    factor=Q(N+H-1,N)
    _,rootfactor=cm.sqrt_bounds(factor)
    _,rootbad=cm.sqrt_bounds(bad)
    return {'phase_reconstruction_error_upper':sp.qrecord(epsilon),
            'bad_word_fraction':sp.qrecord(bad),
            'signed_residual_abs_upper':sp.qrecord(Q(2*k,N)+epsilon+2*bad),
            'sqrt_window_energy_upper':sp.qrecord(Q(2*k,H)*factor+
                rootfactor*(epsilon+2*rootbad))}


def run(source):
    n0,N,last=source['n0'],source['L'],source['last']
    carries=source['source']['carries']
    if len(carries)!=last or last-n0+1!=N:
        raise ValueError('source clock length or literal carry stream mismatch')
    out=[]
    for row in source['per_time_phases']:
        h=row['h'];f=[cm.unpacked(v) for v in row['boxes']]
        if len(f)!=N or row['start']!=n0:
            raise ValueError('phase row must cover the full declared source clock')
        W=cm.mean(f)
        for k in (2,3):
            literal=[];residue=[];bad=0
            for n in range(n0,last+1):
                v=integer_word(carries,n,k)
                w=integer_word(carries,n,k,True)
                literal.append(word_phase(h,k,v))
                residue.append(word_phase(h,k,w))
                bad+=any(d!=d%16 for d in carries[n-k:n])
            for name,g,bad_count in (('literal',literal,0),('residue',residue,bad)):
                error=[a-b for a,b in zip(f,g)]
                mean_g=cm.mean(g)
                mean_error=cm.mean(error)
                proof=analytic_bounds(n0,N,h,k,512,bad_count)
                window=sp.window_receipts(error,(512,))
                measured_upper=Q(**{v:window['rows'][0]['sqrt_V_upper'][v]
                                    for v in ('numerator','denominator')})
                proof_upper=Q(**{v:proof['sqrt_window_energy_upper'][v]
                                  for v in ('numerator','denominator')})
                residual_bound=Q(**{v:proof['signed_residual_abs_upper'][v]
                                     for v in ('numerator','denominator')})
                # Numerical enclosures are independently wider than the truth;
                # compare their LOW endpoints to proved upper bounds.
                residual_low,_=cm.magnitude_bounds(mean_error)
                energy_low=max(0,window['rows'][0]['V_interval'][0])
                assert residual_low<=residual_bound
                assert Q(energy_low,cm.SCALE)<=proof_upper**2
                _,mean_upper=cm.magnitude_bounds(mean_g)
                out.append({'h':h,'k':k,'table':name,'bad_words':bad_count,
                    'mean_prediction':cm.packed(mean_g),
                    'mean_residual':cm.packed(mean_error),
                    'pointwise_L2_squared':window['diagonal'],
                    'analytic_bounds':proof,'window':window,
                    'measured_window_certificate_upper':sp.qrecord(mean_upper+measured_upper),
                    'analytic_window_certificate_upper':sp.qrecord(mean_upper+proof_upper),
                    'analytic_signed_certificate_upper':sp.qrecord(mean_upper+residual_bound),
                    'W':cm.packed(W)})
                print('retrodiction',h,k,name,'mean',float(mean_upper),
                      'signed certificate',float(mean_upper+residual_bound),flush=True)
    return {'clock':{k:source[k] for k in ('A','p','m','q','L','n0','last')},
            'status':'EXPLORATORY SAME-HOLDOUT ANALYSIS; no model fitting or fresh holdout claim',
            'rows':out,'pi_normality':'OPEN','RH':'OPEN',
            'boundary':'Retained carry contrast approximates W; its decay remains OPEN.'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    raw=args.source.read_bytes()
    source=json.loads(gzip.decompress(raw) if args.source.suffix=='.gz' else raw)
    result=run(source)
    result['source_sha256']=sha256(raw).hexdigest()
    result['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':main()
