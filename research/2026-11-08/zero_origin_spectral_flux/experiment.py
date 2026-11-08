"""Reproducible finite zero-seed BBP energy/flux experiment (stdlib only)."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from fractions import Fraction
from pathlib import Path

from observational_succ.zero_origin_spectral_flux import (
    certified_zero_orbit, energy_checkpoint, energy_ladder,
    online_word_surplus, temporal_flux, spectral_feedback_toy,
    channel_phase_summary, signed_vdc_energy, de_bruijn_hex,
    histograms_cyclic, discrepancy_energy,
)


def machin_arctan_interval(reciprocal: int, terms: int) -> tuple[Fraction, Fraction]:
    """Independent rational arctan brackets; no BBP or pi-digit oracle."""
    x=Fraction(1,reciprocal)
    s=Fraction()
    xx=x
    for j in range(terms):
        s+=xx/(2*j+1) if j%2==0 else -xx/(2*j+1)
        xx*=x*x
    error=xx/(2*terms+1)
    return (s, s+error) if terms%2==0 else (s-error,s)


def machin_interval(terms5: int, terms239: int) -> tuple[Fraction,Fraction]:
    a,b=machin_arctan_interval(5,terms5)
    c,d=machin_arctan_interval(239,terms239)
    return 16*a-4*d, 16*b-4*c


def check_machin_prefix(digits: tuple[int,...], length: int = 64) -> dict:
    """Cross-check the first length digits via an independent Machin interval."""
    if len(digits) < length or length < 1:
        raise ValueError("not enough digits")
    terms5=max(8,length*2)
    terms239=max(5,length)
    lo,hi=machin_interval(terms5,terms239)
    if hi-lo>=Fraction(1,16**(length+1)):
        raise ArithmeticError("Machin interval not precise enough")
    for n in range(1,length+1):
        a=(16**n * lo).__floor__()
        b=(16**n * hi).__floor__()
        if a!=b or a%16!=digits[n-1]:
            raise AssertionError(f"Machin/BBP digit disagreement at {n}")
    return {"verified_digits":length,"machin_terms_1_5":terms5,
            "machin_terms_1_239":terms239,
            "interval_width_log2_approx":(hi-lo).numerator.bit_length()-(hi-lo).denominator.bit_length()}


def canonical_json(obj):
    if isinstance(obj,Fraction):
        return {"numerator":obj.numerator,"denominator":obj.denominator}
    raise TypeError(type(obj).__name__)


def experiment(n: int = 8192, seed: int = 20261108, shuffles: int = 16,
               maxdepth: int = 3) -> dict:
    if n<64 or n&(n-1) or n > 16384:
        raise ValueError("n must be a power of 2 from 64 to 16384")
    if maxdepth < 2 or maxdepth > 4:
        raise ValueError("depth must be 2..4")
    trace=certified_zero_orbit(n)
    pi_digits=trace.digits
    reference=check_machin_prefix(pi_digits,min(n,128))
    periodic=tuple(range(16))*(n//16)
    sorted_control=tuple(d for d in range(16) for _ in range(pi_digits.count(d)))
    shadow=(0,)*n
    db=de_bruijn_hex(3)
    debruijn=(db*(n//len(db)+1))[:n]
    rng=random.Random(seed)
    shuffled=list(pi_digits)
    rng.shuffle(shuffled)
    toy=spectral_feedback_toy(n, seed=seed, beta=0.65, window=64)
    controls={"BBP":pi_digits,
              "same_counts_shuffled":tuple(shuffled),
              "same_counts_sorted":sorted_control,
              "periodic_balanced":periodic,
              "debruijn_order3":debruijn,
              "coherent_shadow":shadow,
              "toy_spectral_feedback":toy}
    # Preserve a precommitted comparison window; no fitting to held-out samples.
    checkpoints=[x for x in (16,32,64,128,256,512,1024,2048,4096,8192,16384) if x<=n]
    progress=[]
    for count in checkpoints:
        p=pi_digits[:count]
        row=energy_checkpoint(p,maxdepth)
        row["signed_balance_depth1"]=online_word_surplus(p,1)["signed_surplus_mean"]
        progress.append(row)
    final={}
    for name,digits in controls.items():
        cp=energy_checkpoint(digits,maxdepth)
        incoming={str(depth):online_word_surplus(digits,depth)
                  for depth in range(1,maxdepth+1)}
        flux={f"h{h}_q{q}":temporal_flux(digits,h,q,1)
              for h,q in ((1,2),(1,4),(1,8),(1,16),(2,16),(4,16),(8,16))}
        final[name]={"checkpoint":cp,"online_flux":incoming,
                     "temporal_flux":flux,
                     "digits_sha256":hashlib.sha256(bytes(digits)).hexdigest(),
                     "longest_equal_run":longest_run(digits)}
    shuffleref=[]
    for i in range(shuffles):
        shuffled_i=list(pi_digits)
        random.Random(seed+i+1).shuffle(shuffled_i)
        sample=energy_checkpoint(shuffled_i,maxdepth)
        shuffleref.append({"seed":seed+i+1,
                          "energy":sample["word_energies"],
                          "max_temporal_line":sample["spectral"]["largest_nonzero_power"]})
    source=[]
    for a in (1,64,128,256,512,1024,2048,4096):
        if a>=n or a>trace.verified_phase_steps: continue
        epoch=trace.orbit_phases[a-1:min(n,2*a-1)]
        source.append({"n":a,"channel_suffix":channel_phase_summary(trace,a-1),
                       "signed_lag":signed_vdc_energy(epoch,1,min(64,len(epoch)))})
    return {"schema":"succ-zero-origin-spectral-flux-v1",
            "origin":"U0=0 exact BBP, pi digits by rational tail certification",
            "source":"r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)",
            "n":n,"first64":"".join("0123456789ABCDEF"[d] for d in pi_digits[:64]),
            "source_trace":{"max_tail_depth":trace.max_tail_depth,
                            "tail_refinements":trace.tail_refinements,
                            "verified_phase_steps":trace.verified_phase_steps,
                            "channel_trace_truncated":trace.verified_phase_steps<n,
                            "carry_range":[min(trace.carries),max(trace.carries)],
                            "first32_carries":list(trace.carries[:32])},
            "independent_machin_calibration":reference,
            "checkpoints":progress,
            "final_controls":final,
            "matched_shuffle_replicates":shuffleref,
            "source_phase_instruments":source,
            "scope":"FINITE OBSERVATIONS ONLY. Conservation identities are not negative drift or pi normality.",
            "seed":seed,"shuffles":shuffles}


def longest_run(digits):
    best=last=0
    for i,d in enumerate(digits):
        if i and d==digits[i-1]: last+=1
        else:last=1
        best=max(best,last)
    return best


def write_outputs(out_dir:Path,data:dict)->dict:
    out_dir.mkdir(parents=True,exist_ok=True)
    raw=json.dumps(data,default=canonical_json,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    outfile=out_dir/'finite_receipt.json'
    outfile.write_text(raw,encoding='utf-8')
    csv=out_dir/'progress.csv'
    import csv as csvmod
    with csv.open('w',encoding='utf-8',newline='') as fd:
        w=csvmod.writer(fd)
        w.writerow(['n','digit_E1','word_E2','word_E3','flux_1_to_2','flux_2_to_3',
                    'temporal_dc_h1','peak_nonzero_h1','peak_period_index'])
        for row in data['checkpoints']:
            es=row['word_energies'];fs=row['depth_flux'];sp=row['spectral'] or {}
            w.writerow([row['n'],es[0],es[1],es[2],fs[0],fs[1],
                        sp.get('dc_power'),sp.get('largest_nonzero_power'),
                        sp.get('largest_nonzero_index')])
    return {"receipt":str(outfile),"sha256":hashlib.sha256(raw.encode()).hexdigest(),
            "csv":str(csv)}


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n',type=int,default=8192)
    p.add_argument('--seed',type=int,default=20261108)
    p.add_argument('--shuffles',type=int,default=16)
    p.add_argument('--depth',type=int,default=3)
    p.add_argument('--out',type=Path,default=Path('/tmp/succ_zero_origin_energy'))
    args=p.parse_args(argv)
    info=experiment(args.n,args.seed,args.shuffles,args.depth)
    path=write_outputs(args.out,info)
    print(json.dumps(path,sort_keys=True))
    pi=info['final_controls']['BBP']['checkpoint']
    print('FIRST64',info['first64'])
    print('BBP_ENERGY',pi['word_energies'])
    print('CONTROL_E3',[(k,v['checkpoint']['word_energies'][2])
                         for k,v in info['final_controls'].items()])

if __name__=='__main__':
    main()
