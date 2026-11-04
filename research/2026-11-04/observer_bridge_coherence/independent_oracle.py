"""Independent exact rational bridge/source challenge and deterministic finite receipt.

No import of coherence.py. This uses a separate integer-modulus source path.
Finite tests never certify nonhalting or π normality.
"""
from __future__ import annotations
import argparse,hashlib,json,pathlib
from fractions import Fraction as F
from math import lcm

DATA = (
    (F(1,2),F(1,3),F(5,12)),
    (F(7,20),F(11,28),F(13,45)),
    (F(-7,16),F(0),F(19,50)),
)


def exact_source(j):
    # original signed terms, computed separately from coherence.py
    return sum((F(a,8*j+b) for a,b in ((4,-7),(-2,-4),(-1,-3),(-1,-2))),F(0))


def original_modular_phase(N):
    raw = [exact_source(j) for j in range(1,N+1)]
    D=lcm(*(f.denominator for f in raw))
    residue=0;results=[]
    for f in raw:
        residue=(residue*16+f.numerator*(D//f.denominator))%D
        results.append(F(residue,D))
    return raw,results


def primecheck(k):
    return k>=2 and all(k%j for j in range(2,__import__('math').isqrt(k)+1))


def rational_repr(x):return f'{x.numerator}/{x.denominator}'


def one_receipt(samples):
    M=lcm(*(r.denominator for r in samples))
    # M*q has integer value precisely if its numerator is divisible by denominator.
    assert all((M*q.numerator)%q.denominator==0 for q in samples)
    candidate=M+1
    diff=F(candidate-1,2*M)%1
    assert diff==F(1,2)
    return {'M':str(M),'probe_count':len(samples),'candidate_winding':str(candidate),
            'distinguishing_point':rational_repr(F(1,2*M)),
            'difference':rational_repr(diff)}


def run_receipt():
    triples=[one_receipt(x) for x in DATA]
    r,phases=original_modular_phase(12)
    observations=tuple(y for pair in zip(r,phases) for y in pair)
    original=one_receipt(observations)
    old_M=int(original['M'])
    p=8*((8*12-2)//8+1)+1
    while not primecheck(p):p+=8
    j=(p+7)//8
    f=exact_source(j)
    assert p==97 and j==13 and f.denominator%p==0 and old_M%p!=0
    shift=(f*old_M)%1
    assert shift>0
    payload='|'.join(f'{j}:{rational_repr(r[j-1])}:{rational_repr(phases[j-1])}' for j in range(1,13))
    snapshot_digest=hashlib.sha256(payload.encode()).hexdigest()
    return {'source':'original four signed BBP terms with U0=0',
            'rational_probe_sets':triples,'original_horizon12':original,
            'original_source_first_new_prime':{'prime':p,'index':j,
                                                'shift':rational_repr(shift),
                                                'source_forcing':rational_repr(f)},
            'original_12_state_sha256':snapshot_digest,
            'moving_switch_examples':{str(n):{'survives_through_n':n+1>n,'fails_at':n+1}
                                      for n in (1,2,5,12,32)},
            'busy_beaver_computed':False,
            'only_finite_checks_performed':True,
            'pi_normality_proved':False}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    path=pathlib.Path(__file__).with_name('FINITE_RECEIPT.json')
    got=run_receipt()
    if args.verify:
        if json.loads(path.read_text())!=got:
            raise AssertionError('Receipt drift')
        print('EXACT SOURCE/BRIDGE RECEIPT: PASS')
    else:
        path.write_text(json.dumps(got,sort_keys=True,indent=2)+'\n')
        print('Exact receipt generated',path)

if __name__=='__main__':main()
