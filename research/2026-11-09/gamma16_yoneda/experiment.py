"""Reproduce exact 16x16 original source observations; no newly generated π digits.

Run from repository root:
    python research/2026-11-09/gamma16_yoneda/experiment.py --output /tmp/gamma16.json
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction
from collections import Counter
from hashlib import sha256
import json
import random
import sys

from observational_succ.bbp_gamma16_matrix import (
    pair_counts,exact_energy_split,primitive_sector_masses,difference_counts,
    stroboscopic_pair_split,de_bruijn_16,cyclic_word_energy,
    genuine_prime_stage_matrix_mixture,blocking_endpoint_jets,
)

BASE=Path(__file__).resolve().parent
DATA=BASE/'REUSED_HEX_40960.txt'
INPUT_SHA='c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527'


def rational(z:Fraction)->dict[str,int]:
    return {'n':z.numerator,'d':z.denominator}


def stats(digits):
    C=pair_counts(digits)
    E=exact_energy_split(C)
    return {'N':len(digits), 'energy':{k:rational(v) for k,v in E.items()},
            'min_pair_count':min(v for row in C for v in row),
            'max_pair_count':max(v for row in C for v in row)}


def receipt()->dict:
    source=DATA.read_bytes()
    if sha256(source).hexdigest()!=INPUT_SHA:
        raise AssertionError('original source-certified prefix hash mismatch')
    d=tuple(int(c,16) for c in source.decode('ascii').strip())
    if len(d)!=40960:raise AssertionError('expected exactly 40960 digits')
    rng=random.Random(20261109)
    shuffles=[]
    for _ in range(16):
        p=list(d)
        rng.shuffle(p)
        shuffles.append(stats(p))
    controls={
        'period16':stats(tuple(i%16 for i in range(40960))),
        'constant0':stats((0,)*40960),
        'sorted_same_histogram':stats(sorted(d)),
        'de_bruijn_order2':stats(de_bruijn_16(2)),
    }
    controls['de_bruijn_order2']['E3']=rational(cyclic_word_energy(de_bruijn_16(2),3))
    summary={
        'schema':'SUCC-GM16-2026-11-09-v1',
        'scope':'REUSED ORIGINAL ZERO BBP PREFIX; NO NEW HOLDOUT; ALL NONTRIVIAL LIMIT CLAIMS OPEN',
        'source':'femboy2112/SUCC draft #561 and #565, frozen authentic four poles and U0=0',
        'parent_pr565_head':'35a664c19e91ab5bd11678c82566ce88336e0309',
        'inherited_input_sha256':INPUT_SHA,
        'checkpoints':[stats(d[:n]) for n in (4096,8192,16384,32768,40960)],
        'final_counts_16x16':pair_counts(d),
        'final_difference_counts':difference_counts(pair_counts(d)),
        'final_stroboscopic':{k:rational(v) for k,v in stroboscopic_pair_split(d).items()},
        'final_cyclotomic_sector_diagnostics':{
            f'{a}:{b}':round(v,14) for (a,b),v in primitive_sector_masses(pair_counts(d)).items()},
        'source_endpoint_jets':{str(g):blocking_endpoint_jets(g) for g in range(1,6)},
        'source_prime_birth_partitions':[
            {k:(rational(v) if isinstance(v,Fraction) else
                 [rational(x) for x in v] if isinstance(v,tuple) and v and isinstance(v[0],Fraction) else
                 list(v) if isinstance(v,tuple) else v)
             for k,v in genuine_prime_stage_matrix_mixture(d,A,p).items()}
            for A,p in ((2048,4937),(8192,19681),(16384,39313))
        ],
        'controls':controls,
        'histogram_matched_shuffle':shuffles,
        'note':'Floats only for diagnostic cyclotomic sector; all main energy values and source jets exact.'
    }
    return summary

if __name__=='__main__':
    out=receipt()
    if len(sys.argv)==3 and sys.argv[1]=='--output':
        p=Path(sys.argv[2]);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print(f'wrote {p}  ({p.stat().st_size:,} bytes)')
    elif len(sys.argv)==1:
        print(json.dumps(out,indent=2,sort_keys=True))
    else:
        raise SystemExit('usage: experiment.py [--output PATH]')
