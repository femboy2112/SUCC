"""Exact finite rational holdout receipt, not an asymptotic proof."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('gaussian_unit_receipt',HERE/'gaussian_unit_gluing.py')
m=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(m)


def norm(x):
    if isinstance(x,Q):return [x.numerator,x.denominator]
    if isinstance(x,dict):return {str(k):norm(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [norm(v) for v in x]
    return x


def run():
    src=(HERE/'gaussian_unit_gluing.py').read_bytes()
    oracle=(HERE/'symbolic_oracle.py').read_bytes()
    out={
      'scope':'Finite exact observations only; paper proofs required for all-n claims',
      'date':'2026-11-03',
      'source':'ORIGINAL four BBP Mellin terms; literal U0=0',
      'pin':'child of draft PR 479, base 61bab5cb354e6143fd2fd7ce229ef1b8e9902538',
      'module_sha256':hashlib.sha256(src).hexdigest(),
      'symbolic_oracle_sha256':hashlib.sha256(oracle).hexdigest(),
      'hankel_determinant':4,
      'unit_restore':norm(m.exact_certificate()),
      'fresh_holdouts':{},
      'pi_normality_proved':False,
    }
    for n in (307,509,769,1021):
        rh,rg=m.mellin_channels(n)
        original=m.original_four_poles(n)
        assert rh+rg==original
        assert m.v2_rational(rh)==m.v2_rational(rg)==-5-m.v2_rational(n)
        assert m.v2_rational(original)>=0
        out['fresh_holdouts'][str(n)]={
          'channel_H':norm(rh),'channel_G':norm(rg),
          'original':norm(original),
          'channel_v2':m.v2_rational(rh),
          'source_v2':m.v2_rational(original),
          'source_matches':True,
        }
    return out


if __name__=='__main__':
    import sys
    result=run()
    p=HERE/'EXACT_RECEIPT.json'
    if '--verify' in sys.argv:
        assert result==json.loads(p.read_text())
        print('Exact Gaussian-unit gluing receipt: PASS')
    else:
        p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print('Exact Gaussian-unit gluing receipt generated:',p)
