"""Deterministic exact rational receipt for research interpreter and cyclic joins."""
import argparse
import hashlib
import json
from pathlib import Path
from lcm_carrier import bbp_prefix,cyclic_join_finite,prior_independence_countermodels,source_subgroup_clock
from source_sound import (ARITH,BBP,Claim,Proof,Context,Checker)


def value():
    states=bbp_prefix(24)
    raw={'bbp':[(x.time,str(x.clock),str(x.numerator),str(x.last_carry)) for x in states],
         'join':[(r.a,r.b,r.gcd,r.lcm,r.kernel_size,r.image_size) for r in
                   (cyclic_join_finite(a,b) for a,b in ((2,3),(6,10),(12,18),(5,7),(9,15)))],
         'coupling':prior_independence_countermodels()}
    digest=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    p=Proof('BBP_ORIGIN',Claim(BBP,'BBP_REGISTER',(0,1,0,None)))
    for s in states[1:]:
        p=Proof('BBP_STEP',Claim(BBP,'BBP_REGISTER',(s.time,s.clock,s.numerator,s.last_carry)),(p,))
    verdict=Checker(Context()).check(p)
    assert verdict.open_hypotheses==frozenset()
    assert verdict.status()=='EXACT_FINITE_ARITHMETIC_OR_LOGIC'
    assert states[-1].clock==source_subgroup_clock(24)
    return {
        'task':'source-sound-calculus / intrinsic-LCM-carrier',
        'claim':'exact finite source groups and original zero-seeded BBP carrier, not normality',
        'source':'original four signed BBP poles, U0=0',
        'finite_horizon':24,
        'sample_join_clocks':[(a,b) for a,b in ((2,3),(6,10),(12,18),(5,7),(9,15))],
        'bbp_final_Q':str(states[-1].clock),
        'bbp_final_remainder':str(states[-1].numerator%states[-1].clock),
        'phase_priors':prior_independence_countermodels(),
        'original_exact_data_sha256':digest,
        'calculus_ledger':'exact arithmetic/model-relative/conditional separate',
        'pi_base16_normality':'OPEN','RH':'OPEN'
    }


def content():
    return json.dumps(value(),indent=2,sort_keys=True)+'\n'

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    x=content()
    if args.write:args.write.write_text(x)
    if args.verify:
        assert args.verify.read_text()==x,'finite source receipt mismatch'
        print('SOURCE_SOUND_LCM_EXACT_RECEIPT_VERIFIED')
    if not args.write and not args.verify:print(x)
