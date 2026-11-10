"""Executed finite spectral-return and primitive-sector audit of inherited certified digits.

Use exact integer arithmetic; random shuffles are seeded diagnostics only.
This does not infer normality, iid sampling, or source-selected phase cancellation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path

from observational_succ.bbp_word_spectroscopy import (
 BASE, ORDERS, exact_reset_walk, spectral_refinement,
 word_counts_cyclic, word_energy, iid_exact_balanced_probability, full_word_reset_horizons,
)


def canonical(data: object) -> object:
    if isinstance(data, Fraction):
        return {"numerator": data.numerator, "denominator": data.denominator}
    if isinstance(data, dict):
        return {str(k):canonical(v) for k,v in data.items()}
    if isinstance(data, (tuple,list)):
        return [canonical(v) for v in data]
    return data


def de_bruijn(k: int, n: int) -> tuple[int,...]:
    """Deterministic Ford-sequence construction, not a random oracle."""
    a=[0]*(k*n)
    seq=[]
    def rec(t: int, p: int):
        if t>n:
            if n%p==0:
                seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            rec(t+1,p)
            for j in range(a[t-p]+1,k):
                a[t]=j
                rec(t+1,t)
    rec(1,1)
    assert len(seq)==k**n
    return tuple(seq)


def signed_work(digits, minimum_n=256, level=(1,2,4,8)):
    """Mean unnormalized signed surplus in fixed renormalized-energy bins.

    This is observational only: |R_N|^2 changes by (15/16)+2 surplus.
    """
    c=[0]*16; n=0; q=0; rows={v:[0,0] for v in level}
    for d in digits:
        before=16*c[d]-n
        centered=16*q-n*n
        renorm=Fraction(centered,15*n) if n else Fraction(0)
        if n>=minimum_n:
            for cut in level:
                if renorm>=cut:
                    rows[cut][0]+=before # average signed surplus (16*surplus)
                    rows[cut][1]+=1
        q+=2*c[d]+1
        c[d]+=1;n+=1
    return {str(cut):{"samples":ct,"mean_signed_surplus":Fraction(acc,16*ct) if ct else None}
            for cut,(acc,ct) in rows.items()}


def run(digit_path: Path, n: int=16384, shuffles: int=16) -> dict:
    raw=digit_path.read_bytes()
    text=raw.strip().decode('ascii')
    if any(c not in '0123456789abcdefABCDEF' for c in text):
        raise ValueError('not a valid certified hexadecimal prefix file')
    if len(text)<n:
        raise ValueError('insufficient certified source digits')
    digits=tuple(int(c,16) for c in text[:n])
    path_sha=hashlib.sha256(raw).hexdigest()
    steps=exact_reset_walk(digits)
    end=spectral_refinement(digits,max_depth=3)
    checkpoints={}
    for x in (16,32,64,128,256,512,1024,2048,4096,8192,16384):
        if x<=n:
            data=spectral_refinement(digits[:x],max_depth=3)
            checkpoints[str(x)]={str(k):{
                "E":data[str(k)]["energy"],
                "renormalized":data[str(k)]["renormalized_energy"],
                "sectors":data[str(k)]["primitive_sectors"]
            } for k in range(1,4)}
    rng=random.Random(20261108)
    shuffled=[]
    for i in range(shuffles):
        xs=list(digits)
        rng.shuffle(xs)
        walk=exact_reset_walk(xs)
        sp=spectral_refinement(xs, max_depth=3)
        shuffled.append({"index":i,"returns":{m:len(walk['spectral_zeros'][str(m)]) for m in ORDERS},
            "E1":sp['1']['energy'],"E2":sp['2']['energy'],"E3":sp['3']['energy'],
            "signed_high_energy_work":signed_work(xs)})
    cycle=tuple(range(16))*(n//16)
    assert len(cycle)==n
    db=de_bruijn(16,3)
    assert len(db)==4096 and n%4096==0
    db= db*(n//4096)
    controls={"repeated_16":spectral_refinement(cycle, 3),
              "repeated_de_bruijn_3":spectral_refinement(db, 4),
              "coherent_constant":spectral_refinement((0,)*n,3)}
    return canonical({
        "scope":"finite empirical zero-origin BBP digits; NOT pi normality",
        "input":{"file":str(digit_path), "bytes_sha256":path_sha, "digits":n,
                 "source_branch":"research/zero-origin-spectral-flux-2026-11-08"},
        "exact_reset_walk":steps,
        "exact_word_energy_zero_times":{str(k):full_word_reset_horizons(digits,k) for k in (1,2,3)},
        "sector_energy_final":end,
        "signed_high_energy_work":signed_work(digits),
        "checkpoints":checkpoints,
        "exact_iid_reference_16":iid_exact_balanced_probability(16),
        "controls":controls,
        "matched_histogram_shuffles":shuffled,
        "note":"All reset hits, energies, orthogonal sectors, graph ranks are exact integers/Fractions. Shuffles are illustrative and not blind controls."
    })


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--digits',type=Path,default=Path(__file__).resolve().parents[1]/'zero_origin_spectral_flux/CERTIFIED_HEX_16384.txt')
    parser.add_argument('--n',type=int,default=16384)
    parser.add_argument('--shuffles',type=int,default=16)
    parser.add_argument('--out',type=Path,default=Path('/tmp/bbp_reset_fourier_receipt.json'))
    args=parser.parse_args()
    receipt=run(args.digits,args.n,args.shuffles)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('wrote',args.out,'| sha256',hashlib.sha256(args.out.read_bytes()).hexdigest())
    print('reset hit counts', {m:len(xs) for m,xs in receipt['exact_reset_walk']['spectral_zeros'].items()})
    print('full histogram zeros',len(receipt['exact_reset_walk']['exact_uniform_histogram']))
    print('normalization at final horizon',[(k, float(row['renormalized_energy']['numerator']/row['renormalized_energy']['denominator'])) for k,row in receipt['sector_energy_final'].items()])

if __name__=='__main__': main()
